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
  docker rm -f "$CID" >/dev/null
  CID=""
}

# curl straight into grep/head trips SIGPIPE under pipefail, so land it on disk first
fetch() {
  curl -sf "http://127.0.0.1:${PORT}/$1" -o "$WORK/$2"
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
docker logs "$CID" >"$WORK/logs.txt" 2>&1
grep -q 'No local mibs. Skipping' "$WORK/logs.txt" || fail "expected the no-local-mibs branch"
fetch index.csv base.csv || fail "index.csv is not being served"
grep -q ',' "$WORK/base.csv" || fail "index.csv is not in name,oid form"
fetch asn1/SNMPv2-SMI smi.txt || fail "asn1 tree is not being served"
BASE_LINES="$(wc -l <"$WORK/base.csv" | tr -d ' ')"
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

# mktemp -d is 0700; the container runs as 10001 and has to read the mount
chmod -R a+rX "$WORK/vendor"

start -v "$WORK/vendor:/app/new_mibs/src/vendor:ro"
fetch index.csv merged.csv || fail "index.csv is not being served after the local mib compile"
grep -q '^SMOKE-TEST-MIB,1\.3\.6\.1\.4\.1\.99999$' "$WORK/merged.csv" \
  || fail "compiled mib is missing from the merged index"
fetch asn1/SMOKE-TEST-MIB smoke.txt || fail "compiled mib is not being served from asn1/"
fetch asn1/SNMPv2-SMI smi2.txt || fail "merge clobbered the prebuilt asn1 tree"
MERGED_LINES="$(wc -l <"$WORK/merged.csv" | tr -d ' ')"
[ "$MERGED_LINES" -gt "$BASE_LINES" ] || fail "merged index did not grow ($MERGED_LINES vs $BASE_LINES)"
stop

echo "PASS"
