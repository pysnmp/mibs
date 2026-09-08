#!/usr/bin/env bash
#
# What charts/mibserver promises, asserted against the manifests it renders to.
#
# Two things, and they are different kinds of check.
#
# The first is drift: rendered/ is committed as evidence of what the chart
# produces, and nothing regenerated it, so a template edit could leave those
# files describing a chart that no longer exists. render_manifests.sh --check
# re-renders and fails on a difference, which turns the committed manifests
# back into evidence rather than decoration.
#
# The second is behaviour. pysnmp/mibs#208 was a user unable to mount an
# existing PVC: readOnlyRootFilesystem was derived from localMibs.pathToMibs
# alone, so supplying only persistence.existingClaim left the container with a
# read-only root and every write in the entrypoint failed. The fix made both
# inputs count. What is asserted below is that property -- writable root from
# *either* input -- rather than the shape of the template that currently
# implements it.
#
# The behavioural checks run against a *fresh* render, not against the
# committed one. Asserting the committed manifests would only restate what is
# already in the repository: a chart that regressed would keep passing them
# until the drift check happened to catch it, which is the wrong check failing
# for the wrong reason. Rendering first makes each assertion a statement about
# the chart.
#
# Needs helm; needs no cluster and no build.
#
# See pysnmp/mibs#372.

set -euo pipefail

cd "$(dirname "$0")/.."

FAILURES=0

fail() {
  echo "FAIL: $*" >&2
  FAILURES=$((FAILURES + 1))
}

pass() {
  echo "  ok   $*"
}

if ! command -v helm >/dev/null 2>&1; then
  echo "FAIL: helm is not installed, so the chart cannot be rendered" >&2
  exit 1
fi

MANIFESTS="$(mktemp -d)"
trap 'rm -rf "$MANIFESTS"' EXIT

./render_manifests.sh --out "$MANIFESTS"

# ---------------------------------------------------------------------------
# rendered/ is what the chart actually renders to
# ---------------------------------------------------------------------------

echo "rendered manifests are current"

if diff -ru rendered/manifests "$MANIFESTS" >/dev/null; then
  pass "rendered/manifests matches charts/mibserver"
else
  diff -ru rendered/manifests "$MANIFESTS" || true
  fail "rendered/manifests is stale -- run ./render_manifests.sh and commit"
fi

# ---------------------------------------------------------------------------
# Nothing this project builds runs on the serving path
# ---------------------------------------------------------------------------
#
# The point of the chart's rework: nginx is upstream's, unmodified, and the
# corpus reaches it as a read-only image volume. Asserted because it is easy to
# undo by accident -- a one-line values change would put us back in the
# business of publishing a patched nginx.

echo "the serving container"

deployment() {
  echo "$MANIFESTS/$1/mibserver/templates/deployment.yaml"
}

SERVING_IMAGE="$(
  grep -A1 'name: mibserver$' "$(deployment default)" \
    | grep -o 'image: ".*"' | head -1 || true
)"
if [ -z "$SERVING_IMAGE" ]; then
  SERVING_IMAGE="$(grep -o 'image: "nginx[^"]*"' "$(deployment default)" | head -1 || true)"
fi

if printf '%s' "$SERVING_IMAGE" | grep -q 'nginx'; then
  pass "the serving image is nginx ($SERVING_IMAGE)"
else
  fail "expected an nginx image on the serving container, got: ${SERVING_IMAGE:-none}"
fi

if grep -q 'image: "ghcr.io/pysnmp/mibs/container' "$(deployment default)"; then
  fail "the deployment still runs an image this repository builds nginx into"
else
  pass "no nginx image of ours is deployed"
fi

# The corpus as an image volume is what replaced baking it into that image.
if grep -q 'reference: "ghcr.io/pysnmp/mibs/corpus' "$(deployment default)"; then
  pass "the corpus is mounted as an image volume"
else
  fail "the corpus is not mounted as an image volume"
fi

# ---------------------------------------------------------------------------
# The root filesystem is read-only in every case (pysnmp/mibs#208)
# ---------------------------------------------------------------------------
#
# Rendered above from rendered/values_*.yaml:
#
#   default            neither input      -- no local MIBs, no init container
#   tests_create_pvc   pathToMibs only    -- chart creates the PVC
#   tests_existing_pvc existingClaim only -- chart uses that PVC
#
# #208 was a user unable to mount an existing PVC: readOnlyRootFilesystem was
# derived from pathToMibs alone, so supplying only existingClaim left the
# container with a read-only root and every write in the entrypoint failed.
#
# That defect cannot recur, because nothing writes to the root filesystem any
# more: there is no entrypoint, the config is a ConfigMap and a user's compiled
# MIBs go to an emptyDir before nginx starts. So the assertion inverts -- the
# root is read-only in *every* case now, including the two that had to be
# writable before.
#
# What #208 was really about still has to hold, and it is asserted below on its
# own terms: both inputs produce a deployment that compiles the user's MIBs
# from the storage they supplied.

echo "local MIB storage"

assert_read_only() {
  local case_name="$1" want="$2" file
  file="$(deployment "$case_name")"

  if [ ! -f "$file" ]; then
    fail "$case_name: no rendered deployment at $file"
    return
  fi

  if grep -q "readOnlyRootFilesystem: $want" "$file" \
    && ! grep -q "readOnlyRootFilesystem: $( [ "$want" = true ] && echo false || echo true )" "$file"; then
    pass "$case_name: readOnlyRootFilesystem is $want throughout"
  else
    fail "$case_name: expected readOnlyRootFilesystem $want, got: $(
      grep -o 'readOnlyRootFilesystem: .*' "$file" | tr '\n' ' '
    )"
  fi
}

assert_read_only default true
assert_read_only tests_create_pvc true
assert_read_only tests_existing_pvc true

assert_compiles_local_mibs() {
  local case_name="$1" file
  file="$(deployment "$case_name")"

  if grep -q 'name: compile-local-mibs' "$file"; then
    pass "$case_name: user MIBs are compiled by an init container"
  else
    fail "$case_name: no init container to compile the supplied MIBs"
  fi

  if grep -q 'mountPath: /local-mibs' "$file"; then
    pass "$case_name: the supplied storage is mounted for that compile"
  else
    fail "$case_name: the supplied storage reaches nothing"
  fi
}

assert_compiles_local_mibs tests_create_pvc
assert_compiles_local_mibs tests_existing_pvc

if grep -q 'name: compile-local-mibs' "$(deployment default)"; then
  fail "default: an init container runs where no MIBs were supplied"
else
  pass "default: no init container, so nothing of ours runs at all"
fi

if [ -f "$MANIFESTS/tests_create_pvc/mibserver/templates/pv-claim.yaml" ]; then
  pass "tests_create_pvc: the chart creates a PersistentVolumeClaim"
else
  fail "tests_create_pvc: pathToMibs did not produce a PersistentVolumeClaim"
fi

if [ -f "$MANIFESTS/tests_existing_pvc/mibserver/templates/pv-claim.yaml" ]; then
  fail "tests_existing_pvc: the chart created a PVC where one was supplied"
else
  pass "tests_existing_pvc: no PersistentVolumeClaim is created"
fi

# The claim named in rendered/values_existing_pvc.yaml, which the deployment
# has to mount rather than one of its own.
if grep -q 'claimName: "mibs-hostpath-pvc"' "$(deployment tests_existing_pvc)"; then
  pass "tests_existing_pvc: the supplied claim is the one mounted"
else
  fail "tests_existing_pvc: expected claimName mibs-hostpath-pvc, got: $(
    grep -o 'claimName: .*' "$(deployment tests_existing_pvc)" | tr '\n' ' '
  )"
fi

echo
if [ "$FAILURES" -ne 0 ]; then
  echo "$FAILURES check(s) failed" >&2
  exit 1
fi

echo "chart contract holds"
