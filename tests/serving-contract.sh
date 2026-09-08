#!/usr/bin/env bash
#
# What the deployment serves, asserted against real nginx and the real config.
#
# The old tests/smoke-test.sh built an image of ours and poked at it. There is
# no image of ours to poke at any more: nginx comes from upstream unmodified,
# the corpus arrives as a read-only volume, and the only thing this project
# still authors on the serving path is the nginx.conf the chart renders. So
# that is what this tests -- the rendered config, running under the nginx the
# chart deploys, over the corpus the build just produced.
#
# What it cannot test here is the Kubernetes half: an image volume needs a
# cluster. The volume delivers a directory, and a bind mount delivers a
# directory, so what is asserted below is everything downstream of that -- the
# document roots, the overlay precedence, and the merged index. The chart's own
# manifest shape is tests/chart-contract.sh.
#
# Takes the corpus to serve as its argument, defaulting to output/. CI passes
# the *image* content instead, extracted from docker/corpus.Dockerfile, so what
# is asserted is what a pod would mount rather than what the build left on the
# runner -- the two differ in file modes, which is the whole of the difference
# between serving the corpus and answering 403 for it.
#
# Needs docker and helm. Needs a corpus from `make corpus`.
#
# See pysnmp/mibs#365 and pysnmp/pysmi#182.

set -euo pipefail

cd "$(dirname "$0")/.."

CORPUS="${1:-output}"
CHART="charts/mibserver"

FAILURES=0

fail() {
  echo "FAIL: $*" >&2
  FAILURES=$((FAILURES + 1))
}

pass() {
  echo "  ok   $*"
}

if [ ! -d "$CORPUS/asn1" ]; then
  echo "$CORPUS holds no corpus -- run 'make corpus' first" >&2
  exit 1
fi

CORPUS="$(cd "$CORPUS" && pwd)"
echo "== serving $CORPUS"

WORK="$(mktemp -d)"
CONTAINER=""
cleanup() {
  [ -n "$CONTAINER" ] && docker rm -f "$CONTAINER" >/dev/null 2>&1 || true
  rm -rf "$WORK"
}
trap cleanup EXIT

# ---------------------------------------------------------------------------
# The config under test is the one the chart renders, not a copy of it
# ---------------------------------------------------------------------------

echo "== rendering nginx.conf and the serving image from $CHART"

# Read out of the rendered manifests rather than out of values.yaml, and
# without a YAML parser: this runs on a runner whose python is whatever the
# image ships, and the only tools it should need are the ones that deploy the
# chart. The image is taken from the deployment because that is what a pod
# pulls -- values.yaml is where it comes from, not what it resolves to.
NGINX_IMAGE="$(
  helm template default "$CHART" --namespace default \
    --show-only templates/deployment.yaml \
    | sed -n 's/^ *image: "\(nginx[^"]*\)"$/\1/p' | head -1
)"

if [ -z "$NGINX_IMAGE" ]; then
  echo "FAIL: the rendered deployment names no nginx image" >&2
  exit 1
fi

# The ConfigMap holds one key, as a block scalar indented four spaces. Print
# what follows "nginx.conf: |" until the indentation stops, and undo it.
helm template default "$CHART" --namespace default \
  --show-only templates/configmap.yaml \
  | awk '
      /^  nginx\.conf: \|/ { inside = 1; next }
      inside && /^    / { sub(/^    /, ""); print; next }
      inside && /^$/ { print ""; next }
      inside { exit }
    ' >"$WORK/nginx.conf"

grep -q "listen       8000;" "$WORK/nginx.conf" || {
  echo "FAIL: rendered config has no MIB listener" >&2
  exit 1
}
pass "config rendered from the chart"

# An overlay of the shape the init container leaves behind: one module that is
# not in the corpus, and an index naming it.
mkdir -p "$WORK/overlay/asn1"
printf 'LOCAL-ONLY-MIB DEFINITIONS ::= BEGIN\nEND\n' >"$WORK/overlay/asn1/LOCAL-ONLY-MIB"
sort -u - "$CORPUS/index.csv" <<'ROW' >"$WORK/overlay/index.csv"
LOCAL-ONLY-MIB,1.3.6.1.4.1.99999.1
ROW
chmod -R a+rX "$WORK"

echo "== starting $NGINX_IMAGE over the built corpus"
CONTAINER="$(
  docker run -d --rm \
    --user 10001:10001 \
    --read-only \
    --tmpfs /tmp \
    -v "$CORPUS:/usr/share/nginx/html:ro" \
    -v "$WORK/overlay:/usr/share/nginx/overlay:ro" \
    -v "$WORK/nginx.conf:/etc/nginx/nginx.conf:ro" \
    -p 18000:8000 -p 18080:8080 \
    "$NGINX_IMAGE" nginx -g 'daemon off;'
)"

# The pod's own readiness probe is the status port, so wait on the same thing.
for _ in $(seq 1 40); do
  if curl -fsS http://127.0.0.1:18080/ >/dev/null 2>&1; then
    break
  fi
  sleep 0.5
done

curl -fsS http://127.0.0.1:18080/ >/dev/null 2>&1 || {
  echo "FAIL: nginx never became ready" >&2
  docker logs "$CONTAINER" >&2 || true
  exit 1
}
pass "nginx serves the status port with a read-only root filesystem"

# The status code, and the body on disk. Deliberately not curl -f: a 403 or a
# 404 is an answer this test has something to say about, not a failure to get
# one.
get() {
  curl -sS -o "$WORK/body" -w '%{http_code}' "http://127.0.0.1:18000$1"
}

# ---------------------------------------------------------------------------
# The three artifacts splunk-connect-for-snmp binds to by default
# ---------------------------------------------------------------------------

echo "== MIB_SOURCES: asn1/@mib@ is a bare module name"
code="$(get /asn1/SNMPv2-MIB)"
if [ "$code" = "200" ] && grep -q "SNMPv2-MIB DEFINITIONS" "$WORK/body"; then
  pass "asn1/SNMPv2-MIB is served and is that module"
else
  fail "asn1/SNMPv2-MIB returned $code"
fi

echo "== MIB_INDEX: index.csv"
code="$(get /index.csv)"
if [ "$code" = "200" ] && grep -q '^SNMPv2-MIB,' "$WORK/body"; then
  pass "index.csv is served and carries its rows"
else
  fail "index.csv returned $code"
fi

echo "== MIB_STANDARD: standard.txt"
code="$(get /standard.txt)"
[ "$code" = "200" ] || fail "standard.txt returned $code"
[ "$code" = "200" ] && pass "standard.txt is served"

echo "== the other published trees"
for path in /json/IF-MIB.json /notexts/IF-MIB.py /texts/IF-MIB.py /index-v2.csv; do
  code="$(get "$path")"
  [ "$code" = "200" ] || fail "$path returned $code"
  [ "$code" = "200" ] && pass "$path is served"
done

# ---------------------------------------------------------------------------
# The overlay: what a user's own MIBs reach, and what they cannot take over
# ---------------------------------------------------------------------------

echo "== overlay: a module only the user supplied is served"
code="$(get /asn1/LOCAL-ONLY-MIB)"
if [ "$code" = "200" ] && grep -q "LOCAL-ONLY-MIB DEFINITIONS" "$WORK/body"; then
  pass "asn1/LOCAL-ONLY-MIB falls through to the overlay"
else
  fail "asn1/LOCAL-ONLY-MIB returned $code"
fi

echo "== overlay: the merged index is what index.csv answers with"
code="$(get /index.csv)"
if [ "$code" = "200" ] \
  && grep -q '^LOCAL-ONLY-MIB,' "$WORK/body" \
  && grep -q '^SNMPv2-MIB,' "$WORK/body"; then
  pass "index.csv carries both the published rows and the local one"
else
  fail "merged index.csv returned $code without both halves"
fi

echo "== overlay: the corpus wins for a module both hold"
# The overlay is a fallback, not an override. A user copy of a published module
# must not silently replace what this deployment promises to serve.
mkdir -p "$WORK/overlay/asn1"
printf 'NOT-THE-PUBLISHED-COPY\n' >"$WORK/overlay/asn1/SNMPv2-MIB"
code="$(get /asn1/SNMPv2-MIB)"
if [ "$code" = "200" ] && grep -q "SNMPv2-MIB DEFINITIONS" "$WORK/body"; then
  pass "the published copy still answers"
else
  fail "the overlay took over a published module"
fi
rm -f "$WORK/overlay/asn1/SNMPv2-MIB"

echo "== a module nothing holds is a 404"
code="$(get /asn1/NO-SUCH-MIB)"
[ "$code" = "404" ] || fail "an absent module returned $code rather than 404"
[ "$code" = "404" ] && pass "absent modules 404"

echo
if [ "$FAILURES" = "0" ]; then
  echo "PASS"
else
  echo "$FAILURES check(s) failed" >&2
  exit 1
fi
