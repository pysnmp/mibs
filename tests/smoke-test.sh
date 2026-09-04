#!/usr/bin/env bash
set -euo pipefail

IMAGE="${1:?usage: smoke-test.sh <image>}"
PORT="${SMOKE_PORT:-18000}"
WORK="$(mktemp -d)"
CID=""

cleanup() {
  [ -n "$CID" ] && docker rm -f "$CID" >/dev/null 2>&1
  rm -rf "$WORK"
  return 0
}
trap cleanup EXIT

fail() {
  echo "FAIL: $*" >&2
  [ -n "$CID" ] && docker logs "$CID" 2>&1 | tail -40 >&2
  exit 1
}

start() {
  CID="$(docker run -d -p "${PORT}:8000" "$@" "$IMAGE")"
  for _ in $(seq 1 120); do
    if curl -sf "http://127.0.0.1:${PORT}/index.csv" -o /dev/null; then
      return 0
    fi
    if [ -z "$(docker ps -q --filter "id=$CID")" ]; then
      fail "container exited before serving"
    fi
    sleep 2
  done
  fail "timed out waiting for nginx"
}

stop() {
  docker logs "$CID" >"$WORK/logs.txt" 2>&1
  docker rm -f "$CID" >/dev/null
  CID=""
}

echo "== runtime image must not carry build tooling"
for tool in poetry pipx pip pip3 parallel make gcc; do
  if docker run --rm --entrypoint sh "$IMAGE" -c "command -v $tool" >/dev/null 2>&1; then
    fail "$tool is present in the runtime image"
  fi
done

echo "== runtime image must carry a working interpreter and mibdump"
docker run --rm --entrypoint sh "$IMAGE" \
  -c 'command -v mibdump >/dev/null && python -c "import pysmi, yaml"' \
  || fail "mibdump/python runtime is broken"

echo "== baseline: serves the prebuilt index with no local mibs"
start
grep -q 'No local mibs. Skipping' <(docker logs "$CID" 2>&1) || fail "expected the no-local-mibs branch"
curl -sf "http://127.0.0.1:${PORT}/index.csv" | head -1 | grep -q ',' || fail "index.csv is not being served"
curl -sf -o /dev/null "http://127.0.0.1:${PORT}/asn1/SNMPv2-SMI" || fail "asn1 tree is not being served"
BASE_LINES="$(curl -sf "http://127.0.0.1:${PORT}/index.csv" | wc -l | tr -d ' ')"
[ "$BASE_LINES" -gt 1000 ] || fail "index.csv looks truncated ($BASE_LINES lines)"
stop

echo "== local mibs: compiles a vendor mib mounted at runtime"
mkdir -p "$WORK/vendor/smoke"
cat >"$WORK/vendor/smoke/SMOKE-TEST-MIB" <<'MIB'
SMOKE-TEST-MIB DEFINITIONS ::= BEGIN
IMPORTS
    MODULE-IDENTITY, OBJECT-TYPE, enterprises, Integer32
        FROM SNMPv2-SMI;
smokeTest MODULE-IDENTITY
    LAST-UPDATED "202601010000Z"
    ORGANIZATION "smoke"
    CONTACT-INFO "smoke"
    DESCRIPTION "Smoke test MIB"
    ::= { enterprises 99999 }
smokeValue OBJECT-TYPE
    SYNTAX Integer32
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION "A value"
    ::= { smokeTest 1 }
END
MIB

start -v "$WORK/vendor:/app/new_mibs/src/vendor:ro"
curl -sf "http://127.0.0.1:${PORT}/index.csv" | grep -q '^SMOKE-TEST-MIB,1\.3\.6\.1\.4\.1\.99999$' \
  || fail "compiled mib is missing from the merged index"
curl -sf -o /dev/null "http://127.0.0.1:${PORT}/asn1/SMOKE-TEST-MIB" \
  || fail "compiled mib is not being served from asn1/"
curl -sf -o /dev/null "http://127.0.0.1:${PORT}/asn1/SNMPv2-SMI" \
  || fail "merge clobbered the prebuilt asn1 tree"
MERGED_LINES="$(curl -sf "http://127.0.0.1:${PORT}/index.csv" | wc -l | tr -d ' ')"
[ "$MERGED_LINES" -gt "$BASE_LINES" ] || fail "merged index did not grow ($MERGED_LINES vs $BASE_LINES)"
stop

echo "PASS"
