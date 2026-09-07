#!/usr/bin/env bash
#
# The OID index is a published contract. splunk-connect-for-snmp reads it by
# default on every deployment -- MIB_INDEX, parsed into an OID-to-module map in
# splunk_connect_for_snmp/snmp/manager.py -- so its shape and its answers are
# things this repository owes downstream, not internal detail.
#
# Nothing asserted this before. tests/smoke-test.sh covers that index.csv is
# *served* and is comma-separated; it says nothing about which module a given
# OID resolves to, and that is the part consumers actually use.
#
# Two files, two different promises:
#
#   index-frozen.csv  the snapshot index.csv replays, so consumers keep the
#                     answers they already have. Deliberately frozen by #352;
#                     several of its answers are wrong and stay wrong on
#                     purpose. See "known-wrong" below.
#   output/index-v2.csv  the ranked index, where collisions are resolved by
#                     rule. This is where corrections land.
#
# Runs without Docker and without a build. Checks that need built output are
# skipped when output/ is absent, so a contributor can run this on a clean
# checkout.
#
# See pysnmp/mibs#362.

set -euo pipefail

cd "$(dirname "$0")/.."

FROZEN="index-frozen.csv"
FAILURES=0

fail() {
  echo "FAIL: $*" >&2
  FAILURES=$((FAILURES + 1))
}

pass() {
  echo "  ok   $*"
}

echo "== $FROZEN exists and is readable"
[ -r "$FROZEN" ] || {
  echo "FAIL: $FROZEN is missing" >&2
  exit 1
}

echo "== shape: every row is exactly two fields"
BADFIELDS="$(awk -F, 'NF != 2 {c++} END {print c+0}' "$FROZEN")"
[ "$BADFIELDS" = "0" ] || fail "$BADFIELDS rows are not two fields"
[ "$BADFIELDS" = "0" ] && pass "all rows have two fields"

echo "== shape: column order is MIBNAME,OID"
# sc4snmp does mib_map[row[1]] = row[0], so a column swap would be silent and
# total: every lookup would miss and every MIB would look unknown.
NOTOID="$(awk -F, '$2 !~ /^[0-9]+(\.[0-9]+)*$/ {c++} END {print c+0}' "$FROZEN")"
[ "$NOTOID" = "0" ] || fail "$NOTOID rows have a non-OID in field 2"
[ "$NOTOID" = "0" ] && pass "field 2 is a dotted-decimal OID throughout"

OIDFIRST="$(awk -F, '$1 ~ /^[0-9]+(\.[0-9]+)*$/ {c++} END {print c+0}' "$FROZEN")"
[ "$OIDFIRST" = "0" ] || fail "$OIDFIRST rows have an OID in field 1 -- columns may be swapped"
[ "$OIDFIRST" = "0" ] && pass "field 1 is never an OID"

echo "== shape: one module per OID"
# The consumer parses into a dict, so a second row for an OID would be silently
# discarded. index.py emits one winner per OID; this asserts that holds.
DUPES="$(cut -d, -f2 "$FROZEN" | sort | uniq -d | wc -l | tr -d ' ')"
[ "$DUPES" = "0" ] || fail "$DUPES OIDs appear more than once"
[ "$DUPES" = "0" ] && pass "no OID appears twice"

echo "== shape: no empty module names"
EMPTY="$(awk -F, '$1 == "" {c++} END {print c+0}' "$FROZEN")"
[ "$EMPTY" = "0" ] || fail "$EMPTY rows have an empty module name"
[ "$EMPTY" = "0" ] && pass "no empty module names"

echo "== answers: the OIDs sc4snmp preloads"
# splunk_connect_for_snmp/snmp/manager.py DEFAULT_STANDARD_MIBS, and the OID
# each one anchors. These are pinned AS THEY ARE, not as they should be:
# index.csv is a compatibility freeze, so a changed answer here is a downstream
# behaviour change and must be a deliberate act.
#
# Four of these are wrong, and stay wrong while the freeze stands. They are the
# concrete argument for moving consumers to the ranked index -- see
# pysnmp/mibs#366 step 0. RFC-correct answers in the third column.
#
#   oid                 frozen answer          rfc-correct
check_answer() {
  local oid="$1" expected="$2" note="${3:-}"
  local got
  got="$(awk -F, -v o="$oid" '$2 == o {print $1}' "$FROZEN")"
  if [ "$got" != "$expected" ]; then
    fail "$oid resolves to '${got:-<absent>}', pinned as '$expected'"
  else
    pass "$oid -> $expected${note:+  ($note)}"
  fi
}

check_answer 1.3.6.1.2.1.1  JANITZA-MIB-UMG96  "WRONG, rfc says SNMPv2-MIB -- frozen"
check_answer 1.3.6.1.2.1.2  IF-MIB
check_answer 1.3.6.1.2.1.4  IP-MIB
check_answer 1.3.6.1.2.1.6  IPV6-TCP-MIB       "WRONG, rfc says TCP-MIB -- frozen"
check_answer 1.3.6.1.2.1.7  IPV6-UDP-MIB       "WRONG, rfc says UDP-MIB -- frozen"
check_answer 1.3.6.1.2.1.25 HOST-RESOURCES-MIB
check_answer 1.3.6.1.6.3.1  RAPID-CITY         "WRONG, rfc says SNMPv2-MIB -- frozen"

echo "== every module named in the index is still carried somewhere"
# A row naming a MIB nothing carries resolves to a module that can never be
# served. index.py drops such rows when it replays the snapshot, so these are
# harmless in the published output -- but they are rot, and the count should
# not grow.
#
# "Carried" means src/ or pysmi's bundled ASN.1, since 'make bundled-asn1'
# stages the bundle into the published tree alongside src/.
#
# COFFEE-POT-MIB joined them when src/standard was deleted: pysmi does not
# bundle it and nothing imports it, so the snapshot's two rows for it now name
# a module the site cannot serve.
DEAD_MODULE_CEILING=61
DEAD_ROW_CEILING=335

if BUNDLE="$(uv run python -c 'import importlib.util,pathlib;print(importlib.util.find_spec("pysmi.mibs.asn1").submodule_search_locations[0])' 2>/dev/null)" \
   && [ -d "$BUNDLE" ]; then
  CARRIED="$(mktemp)"
  DEAD_LIST="$(mktemp)"
  { find src -type f -exec basename {} \; ; find "$BUNDLE" -maxdepth 1 -type f ! -name '__*' -exec basename {} \; ; } | sort -u >"$CARRIED"
  # comm pairs duplicate lines, so the dead *module* set is computed from the
  # unique names and the dead *row* count is then counted back over the index.
  cut -d, -f1 "$FROZEN" | sort -u | comm -23 - "$CARRIED" >"$DEAD_LIST"
  DEAD_MODULES="$(grep -c . "$DEAD_LIST" || true)"
  DEAD_ROWS="$(awk -F, 'NR==FNR {dead[$0]; next} $1 in dead {c++} END {print c+0}' "$DEAD_LIST" "$FROZEN")"
  rm -f "$CARRIED" "$DEAD_LIST"

  if [ "$DEAD_MODULES" -gt "$DEAD_MODULE_CEILING" ]; then
    fail "$DEAD_MODULES modules in the index are carried nowhere, above the pinned ceiling of $DEAD_MODULE_CEILING"
  elif [ "$DEAD_ROWS" -gt "$DEAD_ROW_CEILING" ]; then
    fail "$DEAD_ROWS index rows name a module carried nowhere, above the pinned ceiling of $DEAD_ROW_CEILING"
  else
    pass "$DEAD_MODULES modules / $DEAD_ROWS rows name nothing carried, within the pinned ceiling"
  fi
else
  echo "  skip pysmi bundle not importable; cannot tell rot from bundled modules"
fi

if [ -d output ]; then
  # The workflow creates output/asn1 before 'make index', so output/ existing
  # says nothing about whether the index was built. Skipping on a missing
  # index.csv would let an incomplete generation pass this script silently,
  # which is the one thing a contract test must not do. Once output/ exists,
  # both files are required.
  echo "== built output: both index files are present"
  for artifact in output/index.csv output/index-v2.csv; do
    if [ -f "$artifact" ]; then
      pass "$artifact exists"
    else
      fail "$artifact is missing, but output/ exists -- the index build did not complete"
    fi
  done

  if [ -f output/index.csv ]; then
    echo "== built output: index.csv replays the frozen snapshot"
    # index.py writes index.csv from index-frozen.csv, dropping only rows whose
    # module is no longer compiled. So index.csv must be a subset, with no row
    # the snapshot does not contain.
    EXTRA="$(comm -13 <(sort "$FROZEN") <(sort output/index.csv) | wc -l | tr -d ' ')"
    [ "$EXTRA" = "0" ] || fail "output/index.csv has $EXTRA rows absent from $FROZEN"
    [ "$EXTRA" = "0" ] && pass "index.csv introduces no row the snapshot lacks"
  fi

  if [ -f output/index-v2.csv ]; then
    echo "== built output: index-v2.csv carries the corrections"
    V2="$(awk -F, '$2 == "1.3.6.1.6.3.1" {print $1}' output/index-v2.csv)"
    [ "$V2" = "SNMPv2-MIB" ] \
      || fail "index-v2.csv resolves 1.3.6.1.6.3.1 to '${V2:-<absent>}', expected SNMPv2-MIB"
    [ "$V2" = "SNMPv2-MIB" ] && pass "index-v2.csv fixes 1.3.6.1.6.3.1 -> SNMPv2-MIB"
  fi
else
  echo "== output/ absent, skipping the built-index checks"
  echo "     run 'make index' first to include them"
fi

echo
if [ "$FAILURES" -gt 0 ]; then
  echo "FAILED: $FAILURES check(s)" >&2
  exit 1
fi
echo "PASS"
