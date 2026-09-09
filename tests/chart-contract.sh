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

CHART="charts/mibserver"

# The chart's kubeVersion is >=1.33, and `helm template` without a cluster
# checks it against the helm binary's built-in default -- which helm 4 sets to
# v1.20.0, refusing to render this chart at all. So every render here names a
# version instead of taking whichever one the installed helm assumes.
#
# It is read twice over: helm checks it against the chart's kubeVersion, and
# deployment.yaml compares .Capabilities.KubeVersion.Version against the same
# floor and fails the render below it, which is what catches a parent chart
# installing this one as a dependency (helm checks kubeVersion only on the
# chart it was handed).
KUBE_VERSION="1.33.0"
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
# The Kubernetes floor holds even when helm is not checking it
# ---------------------------------------------------------------------------
#
# helm checks Chart.yaml's kubeVersion against the chart it was told to
# install, not against a dependency's metadata -- so a parent chart with no
# constraint of its own renders this one anywhere, and that is exactly how
# splunk-connect-for-snmp installs it. The template guards it too. Asserted
# here on both sides: a version below the floor is refused, and the shapes real
# distributions report are not.

echo "the Kubernetes floor"

guard() {
  helm template default "$CHART" --namespace default --kube-version "$1" \
    >/dev/null 2>&1 && echo rendered || echo refused
}

if [ "$(guard 1.32.0)" = "refused" ]; then
  pass "1.32.0 is refused"
else
  fail "1.32.0 rendered, and the image volume it emits needs 1.33"
fi

# The other half, and the more dangerous one: a guard that rejects a cluster
# that would have worked is worse than no guard. Managed distributions do not
# report a bare semver.
for version in 1.33.0 1.34.1 1.35.0 1.33.0-eks-ba74326 1.33.0-gke.1234 1.33.2-rancher1; do
  if [ "$(guard "$version")" = "rendered" ]; then
    pass "$version renders"
  else
    fail "$version was refused, but it is at or above the floor"
  fi
done

# ---------------------------------------------------------------------------
# The init container compiles with the same pysmi the corpus was built with
# ---------------------------------------------------------------------------
#
# A user's MIBs are compiled at start-up and served beside the published
# corpus, so the compiler behind the tools image and the compiler behind the
# corpus have to be one version. uv.lock is that version -- `make corpus` runs
# through uv -- and the Dockerfile has to name it rather than a range that
# resolves to whatever is newest on the day the image is built.

# Nothing this serves is text/html, which is all nginx compresses by default.
CONF="$(helm template default "$CHART" --namespace default --kube-version "$KUBE_VERSION" \
  --show-only templates/configmap.yaml)"
for directive in "gzip_types" "gzip_min_length" "gzip_vary on;"; do
  if printf '%s' "$CONF" | grep -q "$directive"; then
    pass "nginx.conf sets $directive"
  else
    fail "nginx.conf lost $directive; the corpus goes out uncompressed"
  fi
done

echo "the tools image"

LOCKED_PYSMI="$(
  awk '/^name = "pysnmp-pysmi"$/ { found = 1; next }
       found && /^version = / { gsub(/^version = "|"$/, ""); print; exit }' uv.lock
)"
PINNED_PYSMI="$(
  sed -n 's/^ARG PYSMI_VERSION="\(.*\)"$/\1/p' docker/tools.Dockerfile
)"

if [ -z "$LOCKED_PYSMI" ]; then
  fail "uv.lock names no pysnmp-pysmi version"
elif [ "$PINNED_PYSMI" = "$LOCKED_PYSMI" ]; then
  pass "the tools image installs pysmi $PINNED_PYSMI, the version uv.lock resolves"
else
  fail "the tools image installs pysmi '$PINNED_PYSMI', but uv.lock resolves $LOCKED_PYSMI"
fi

if grep -q 'pysnmp-pysmi==\${PYSMI_VERSION}' docker/tools.Dockerfile; then
  pass "it is installed as an exact version"
else
  fail "docker/tools.Dockerfile no longer installs an exact pysmi version"
fi

# ---------------------------------------------------------------------------
# The renders are a function of the chart, not of when they were rendered
# ---------------------------------------------------------------------------
#
# The drift check above is only usable if a render is reproducible. It was not:
# checksum/config hashed the rendered ConfigMap, whose labels carry the chart
# version, so every release changed a manifest no one had edited -- and since
# CI renders the pull request merged into main, the check began failing on
# every open branch the moment a release landed. The version is substituted out
# of the rendered text; it has to be out of the hash as well.

echo "renders do not depend on the chart version"

BUMPED="$(mktemp -d)"
BUMP_CHART="$BUMPED/chart"
trap 'rm -rf "$MANIFESTS" "$BUMPED"' EXIT

cp -R "$CHART" "$BUMP_CHART"
sed -i.bak -e 's/^version: .*/version: 99.99.99/' \
  -e 's/^appVersion: .*/appVersion: "99.99.99"/' "$BUMP_CHART/Chart.yaml"
rm -f "$BUMP_CHART/Chart.yaml.bak"

BUMPED_SUM="$(
  helm template default "$BUMP_CHART" --namespace default --kube-version "$KUBE_VERSION" \
    --show-only templates/deployment.yaml \
    | sed -n 's/^ *checksum\/config: \(.*\)$/\1/p' | head -1
)"
CURRENT_SUM="$(
  sed -n 's/^ *checksum\/config: \(.*\)$/\1/p' "$(
    echo "$MANIFESTS/default/mibserver/templates/deployment.yaml"
  )" | head -1
)"

if [ -z "$CURRENT_SUM" ]; then
  fail "the deployment carries no checksum/config annotation"
elif [ "$BUMPED_SUM" = "$CURRENT_SUM" ]; then
  pass "checksum/config survives a release bump"
else
  fail "checksum/config changed on a release bump alone: $CURRENT_SUM -> $BUMPED_SUM"
fi

# ...and still does what it is there for: a changed nginx.conf must roll the
# pods, so a values change that reaches the config has to reach the hash.
IPV6_SUM="$(
  helm template default "$CHART" --namespace default --kube-version "$KUBE_VERSION" \
    --set ipv6Enabled=true --show-only templates/deployment.yaml \
    | sed -n 's/^ *checksum\/config: \(.*\)$/\1/p' | head -1
)"

if [ -n "$IPV6_SUM" ] && [ "$IPV6_SUM" != "$CURRENT_SUM" ]; then
  pass "checksum/config still changes when the config does"
else
  fail "checksum/config did not change when ipv6Enabled added listeners"
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

# An upgrade carrying a values file from before this chart pinned the tag has
# image.tag: "", which rendered "nginxinc/nginx-unprivileged:" -- a reference
# no runtime can pull.
EMPTY_TAG="$(
  helm template default "$CHART" --namespace default --kube-version "$KUBE_VERSION" --set image.tag="" \
    --show-only templates/deployment.yaml \
    | sed -n 's/^ *image: "\(nginx[^"]*\)"$/\1/p' | head -1
)"

case "$EMPTY_TAG" in
  *:) fail "an empty image.tag renders $EMPTY_TAG, which nothing can pull" ;;
  "") fail "an empty image.tag renders no nginx image at all" ;;
  *) pass "an empty image.tag falls back to $EMPTY_TAG" ;;
esac


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

# Dropping every capability does not set no_new_privs, so a setuid binary
# could still gain privileges.
if grep -q 'allowPrivilegeEscalation: false' "$(deployment default)"; then
  pass "privilege escalation is disabled"
else
  fail "the serving container may escalate privileges"
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
#   default                 neither input      -- no local MIBs, no init container
#   tests_create_pvc        pathToMibs only    -- chart creates the PVC
#   tests_existing_pvc      existingClaim only -- chart uses that PVC
#   tests_null_persistence  pathToMibs, persistence omitted entirely
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

# Nothing in this pod talks to the Kubernetes API, so nothing should be handed
# a credential for it.
if grep -q 'automountServiceAccountToken: false' "$(deployment default)"; then
  pass "the pod is not handed a ServiceAccount token"
else
  fail "the pod still automounts a ServiceAccount token"
fi

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

# A values file that omits persistence, or nulls it, is a supported override
# and used to fail the render: every guard reached into the map for
# existingClaim, storageClass and size. That it renders at all is the
# assertion; that it renders the same deployment as pathToMibs alone is what
# makes it supported rather than merely tolerated.
assert_compiles_local_mibs tests_null_persistence
assert_read_only tests_null_persistence true

if [ -f "$MANIFESTS/tests_null_persistence/mibserver/templates/pv-claim.yaml" ]; then
  pass "tests_null_persistence: the chart still creates the claim it promises"
else
  fail "tests_null_persistence: pathToMibs produced no PersistentVolumeClaim"
fi

# The other half: keys present but empty. helm deletes a null key when it
# merges, so dig's default covers that; an empty string survives the merge and
# dig hands it straight back. That reached the manifest as `storage:` with
# nothing after it, which the API rejects.
assert_compiles_local_mibs tests_empty_persistence
CLAIM="$MANIFESTS/tests_empty_persistence/mibserver/templates/pv-claim.yaml"

if [ -f "$CLAIM" ] \
  && grep -qE 'storageClassName: [^ ]' "$CLAIM" \
  && grep -qE 'storage: [0-9]' "$CLAIM"; then
  pass "tests_empty_persistence: an empty storageClass and size fall back to the defaults"
else
  fail "tests_empty_persistence: rendered an empty quantity or storage class: $(
    grep -E 'storageClassName|storage:' "$CLAIM" 2>/dev/null | tr '\n' ' '
  )"
fi

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
