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
# A writable root follows from either local-MIB input (pysnmp/mibs#208)
# ---------------------------------------------------------------------------
#
# Rendered above from rendered/values_*.yaml:
#
#   default            neither input      -- read-only root, no volume
#   tests_create_pvc   pathToMibs only    -- writable root, chart creates the PVC
#   tests_existing_pvc existingClaim only -- writable root, chart uses that PVC
#
# The third case is the one that regressed. It is asserted by name rather than
# only by "a volume exists", because mounting the wrong claim would satisfy the
# weaker check.

echo "local MIB storage"

deployment() {
  echo "$MANIFESTS/$1/mibserver/templates/deployment.yaml"
}

assert_read_only() {
  local case_name="$1" want="$2" file
  file="$(deployment "$case_name")"

  if [ ! -f "$file" ]; then
    fail "$case_name: no rendered deployment at $file"
    return
  fi

  if grep -q "readOnlyRootFilesystem: $want" "$file"; then
    pass "$case_name: readOnlyRootFilesystem is $want"
  else
    fail "$case_name: expected readOnlyRootFilesystem $want, got: $(
      grep -o 'readOnlyRootFilesystem: .*' "$file" | tr '\n' ' '
    )"
  fi
}

assert_read_only default true
assert_read_only tests_create_pvc false
assert_read_only tests_existing_pvc false

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
