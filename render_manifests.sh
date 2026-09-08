#!/usr/bin/env bash
#
# Render charts/mibserver into rendered/manifests, one directory per values
# file, so a chart change shows up as a manifest diff a reviewer can read.
#
#   ./render_manifests.sh              regenerate rendered/manifests
#   ./render_manifests.sh --check      fail if rendered/manifests is stale
#   ./render_manifests.sh --out DIR    render into DIR instead
#
# The committed renders are only evidence if something regenerates them, so
# --check re-renders and fails on a difference rather than writing. --out is
# for a caller that wants to assert against a fresh render rather than against
# the committed one -- see tests/chart-contract.sh, which needs both.
#
# See pysnmp/mibs#372.

set -euo pipefail

cd "$(dirname "$0")"

DIR="rendered"
COMMITTED="$DIR/manifests"
CHART="charts/mibserver"

# Baked into every rendered resource name and instance label, so it has to be
# fixed rather than left to helm's "release-name" placeholder -- otherwise the
# renders depend on how the command was invoked.
RELEASE="default"

# The chart's kubeVersion is >=1.33, and `helm template` without a cluster
# checks it against the helm binary's built-in default -- which helm 4 sets to
# v1.20.0, refusing to render this chart at all. So every render here names a
# version instead of taking whichever one the installed helm assumes. No
# template reads .Capabilities, so this only satisfies the constraint.
KUBE_VERSION="1.33.0"

mode="write"
out=""
case "${1:-}" in
  "") ;;
  --check) mode="check" ;;
  --out)
    mode="out"
    out="${2:?--out needs a directory}"
    ;;
  *)
    echo "usage: $0 [--check | --out DIR]" >&2
    exit 2
    ;;
esac

# Always rendered into an empty directory, never over what is already there.
# helm's --output-dir appends to a file it did not create in this run, so
# rendering onto the committed tree concatenates the new manifest onto the old
# one; and a template that stops being rendered would otherwise leave its stale
# file behind for ever.
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

# Substituted out of the renders so a release bump is not a manifest diff.
APPVERSION="$(sed -n 's/^appVersion: "\(.*\)"$/\1/p' "$CHART/Chart.yaml")"
if [ -z "$APPVERSION" ]; then
  echo "could not read appVersion from $CHART/Chart.yaml" >&2
  exit 1
fi

render() {
  local name="$1"
  shift
  helm template "$RELEASE" "$CHART" --namespace default \
    --kube-version "$KUBE_VERSION" \
    --output-dir "$STAGE/$name" "$@" >/dev/null
  # helm creates this for subchart output; nothing here has subcharts, and an
  # empty directory git cannot track would read as a diff under --check.
  rm -rf "${STAGE:?}/$name/mibserver/charts"
}

# The chart's own defaults, under the name they are committed as.
render default

for values in "$DIR"/values_*.yaml; do
  [ -f "$values" ] || continue
  case_name="$(basename "$values" .yaml)"
  render "tests_${case_name#values_}" --values "$values"
done

# GNU sed reads `-i ''` as a filename and BSD sed reads a bare `-i` as one, so
# neither spelling is portable. A suffix both accept, and a delete, is. The
# `-i ''` form meant this script only ever ran on macOS (pysnmp/mibs#372).
find "$STAGE" -type f -exec sed -i.bak "s/$APPVERSION/CURRENT-VERSION/g" {} +
find "$STAGE" -type f -name '*.bak' -delete

# Drop trailing blank lines and end every file with exactly one newline.
# Without this the committed renders are a function of whichever helm the
# renderer happened to have: across helm 3.16 and helm 4.2 -- which is what
# azure/setup-helm installs today -- the entire tree is identical except that
# helm 4 leaves a trailing whitespace-only line behind. Blank means blank or
# whitespace-only, because that line is eight spaces rather than nothing.
#
# Trailing lines only. Trailing spaces *within* the manifests are left alone,
# because they are part of what the chart emits and normalising them would
# hide a template change.
#
# Deliberately the only normalisation, and why the helm version is not pinned:
# anything else that differs between helm versions is a real change to the
# manifests and should fail the check rather than be smoothed over.
find "$STAGE" -type f | while IFS= read -r file; do
  sed -e :a -e '/^[[:space:]]*$/{$d;N;ba' -e '}' "$file" >"$file.tmp"
  printf '%s\n' "$(cat "$file.tmp")" >"$file"
  rm -f "$file.tmp"
done

replace() {
  local dest="$1"
  rm -rf "${dest:?}"
  mkdir -p "$(dirname "$dest")"
  cp -R "$STAGE" "$dest"
}

case "$mode" in
  check)
    if diff -ru "$COMMITTED" "$STAGE"; then
      echo "rendered manifests match the chart"
    else
      echo >&2
      echo "rendered/manifests is stale -- run ./render_manifests.sh and commit" >&2
      exit 1
    fi
    ;;
  out) replace "$out" ;;
  write) replace "$COMMITTED" ;;
esac
