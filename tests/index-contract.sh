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
# 1.3.6.1.6.3.1 was one such deliberate act. It is corrected in the snapshot
# rather than left to index-v2.csv, because the freeze exists to stop answers a
# consumer depends on from moving, and nothing depended on that OID resolving to
# a Nortel switch MIB -- it was alphabetical order, preserved by accident.
#
# Three are still wrong and stay wrong while the freeze stands. They are the
# concrete argument for moving consumers to the ranked index -- see
# pysnmp/mibs#366. RFC-correct answers in the third column.
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
check_answer 1.3.6.1.6.3.1  SNMPv2-MIB         "corrected in the snapshot"

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
#
# The ceilings went 61/335 -> 224/1737 when pysmi 3.0.0rc5 held 275 of its 485
# bundled modules in pysmi/mibs/future/ (pysnmp/pysmi#220). The wheel carries
# 210, so 163 modules this repository used to publish by staging the bundle are
# no longer staged, and the snapshot's rows for them name nothing carried.
#
# Those 163 were removed deliberately, upstream, as modules nothing imports --
# not defective, and not rot appearing here. Nothing in src/ imports any of
# them, so no module fails to compile; the effect is that the site no longer
# answers for their OIDs.
#
# Every one of them is an IETF module, so src/ is not where they would come
# back: src/vendor holds what a vendor publishes, and filing an RFC module
# under the vendor that happened to ship a copy of it says something untrue
# about who publishes it. The ceilings come back down by promoting the module
# in pysmi -- `update_bundled_mibs.py --promote NAME`, which any use justifies
# -- not by relaxing this check further, and not by adding the text here.
# Anything above these numbers is unaccounted for and should fail.
DEAD_MODULE_CEILING=224
DEAD_ROW_CEILING=1737

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
    echo "== built output: index.csv keeps every answer it can still serve"
    # index.csv is a compatibility index, not a literal freeze. It may drop a
    # row whose module is gone, and may add an OID the snapshot never carried.
    # What it may never do is hand a caller a different module for an OID whose
    # snapshot answer the site can still serve -- that is the breaking change.
    CHANGED="$(awk -F, '
      NR==FNR { sub(/\.json$/, "", $0); carried[$0]; next }
      FILENAME == snapshot { was[$2] = $1; next }
      ($2 in was) && was[$2] != $1 && (was[$2] in carried) {
        printf "  %s: %s -> %s\n", $2, was[$2], $1; c++
      }
      END { exit (c > 0) }
    ' <(ls output/json) snapshot="$FROZEN" "$FROZEN" output/index.csv)" \
      && pass "index.csv changes no answer whose module is still carried" \
      || fail "index.csv reassigns OIDs away from modules it still serves:"$'\n'"$CHANGED"

    echo "== built output: index.csv resolves the SMI base arcs by RFC, not alphabet"
    # The same arcs the index-v2 block below checks, asserted on index.csv too.
    # These were alphabetical accidents the freeze preserved rather than answers
    # a consumer chose -- 1.3.6.1 answering RAPID-CITY, enterprises answering
    # PBI-MAIN-MIB, mib-2 answering CTELS100-NG-MIB. Correcting them in the
    # snapshot is what puts them right for every reader of index.csv, not only
    # for the readers who move to index-v2.csv.
    check_v1() {
      got="$(awk -F, -v k="$1" '$2 == k {print $1}' output/index.csv)"
      if [ "$got" = "$2" ]; then
        pass "index.csv resolves $1 -> $2${3:+  ($3)}"
      else
        fail "index.csv resolves $1 to '${got:-<absent>}', expected $2"
      fi
    }
    check_v1 1.3.6.1        SNMPv2-SMI   internet
    check_v1 1.3.6.1.1      SNMPv2-SMI   directory
    check_v1 1.3.6.1.2      SNMPv2-SMI   mgmt
    check_v1 1.3.6.1.3      SNMPv2-SMI   experimental
    check_v1 1.3.6.1.4      SNMPv2-SMI   private
    check_v1 1.3.6.1.4.1    SNMPv2-SMI   enterprises
    check_v1 1.3.6.1.2.1    SNMPv2-SMI   mib-2
    check_v1 1.3.6.1.2.1.10 SNMPv2-SMI   transmission
    check_v1 1.3.6.1.2.1.3  RFC1213-MIB  "at -- SMIv2 dropped it"
    check_v1 1.3.6.1.2.1.8  RFC1213-MIB  "egp -- SMIv2 dropped it"
    check_v1 1.3.6.1.6.3.1  SNMPv2-MIB
  fi

  if [ -f output/index-v2.csv ]; then
    echo "== built output: index-v2.csv carries the corrections"
    V2="$(awk -F, '$2 == "1.3.6.1.6.3.1" {print $1}' output/index-v2.csv)"
    [ "$V2" = "SNMPv2-MIB" ] \
      || fail "index-v2.csv resolves 1.3.6.1.6.3.1 to '${V2:-<absent>}', expected SNMPv2-MIB"
    [ "$V2" = "SNMPv2-MIB" ] && pass "index-v2.csv fixes 1.3.6.1.6.3.1 -> SNMPv2-MIB"

    # The SMI base arcs. RFC1065-SMI (1988), RFC1155-SMI (1990) and SNMPv2-SMI
    # (1999) define the root arcs identically, and RFC1158-MIB, RFC1213-MIB and
    # SNMPv2-SMI define mib-2 and transmission identically. None carries a
    # MODULE-IDENTITY or a revision date, so every rank term ties and the winner
    # used to be whichever module name sorted first -- handing ten arcs to the
    # 1988 and 1990 modules. The RFC-number tiebreak decides them by publication
    # order instead (pysnmp/mibs#378).
    #
    # at and egp are the two RFC 2578 did not carry forward, so SNMPv2-SMI does
    # not define them and RFC1213-MIB is the right answer there, not SNMPv2-SMI.
    check_v2() {
      got="$(awk -F, -v k="$1" '$2 == k {print $1}' output/index-v2.csv)"
      if [ "$got" = "$2" ]; then
        pass "index-v2.csv resolves $1 -> $2${3:+  ($3)}"
      else
        fail "index-v2.csv resolves $1 to '${got:-<absent>}', expected $2"
      fi
    }

    echo "== built output: index-v2.csv resolves the SMI base arcs by RFC, not alphabet"
    check_v2 1.3.6.1        SNMPv2-SMI   internet
    check_v2 1.3.6.1.1      SNMPv2-SMI   directory
    check_v2 1.3.6.1.2      SNMPv2-SMI   mgmt
    check_v2 1.3.6.1.3      SNMPv2-SMI   experimental
    check_v2 1.3.6.1.4      SNMPv2-SMI   private
    check_v2 1.3.6.1.4.1    SNMPv2-SMI   enterprises
    check_v2 1.3.6.1.2.1    SNMPv2-SMI   mib-2
    check_v2 1.3.6.1.2.1.10 SNMPv2-SMI   transmission
    check_v2 1.3.6.1.2.1.3  RFC1213-MIB  "at -- SMIv2 dropped it"
    check_v2 1.3.6.1.2.1.8  RFC1213-MIB  "egp -- SMIv2 dropped it"
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
