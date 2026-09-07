#!/usr/bin/env bash
#
# The other two artifacts splunk-connect-for-snmp binds to by default, beside
# the OID index that tests/index-contract.sh covers:
#
#   asn1/@mib@    MIB_SOURCES. Handed to compiler.addMibCompiler(), so pysmi
#                 fetches and compiles raw ASN.1 over HTTP, per module, at
#                 runtime. @mib@ is substituted with a bare module name, which
#                 is why the naming convention below is load-bearing.
#   standard.txt  MIB_STANDARD. Bound as a constant and never read -- see
#                 "standard.txt has no reader" below.
#
# Two different promises, so two different kinds of check. The asn1 naming
# convention is a live contract and is asserted. standard.txt is characterized:
# its shape is pinned so a change declares itself, but the pins record what the
# file is rather than claiming a consumer depends on it.
#
# Runs without Docker and without a build. Checks needing built output are
# skipped only when output/ is absent; see tests/index-contract.sh for why that
# distinction matters.
#
# See pysnmp/mibs#362.

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

# ---------------------------------------------------------------------------
# asn1/@mib@ -- the naming convention MIB_SOURCES substitution rests on
# ---------------------------------------------------------------------------
#
# sc4snmp configures a single source template and lets pysmi substitute:
#
#     MIB_SOURCES = "https://pysnmp.github.io/mibs/asn1/@mib@"
#
# pysmi replaces @mib@ with the module name verbatim and requests that path. So
# a published name is only reachable if it is exactly the module name -- an
# added extension makes every URL a 404, and a character needing percent-
# encoding makes that one module unfetchable while the rest keep working, which
# is the harder failure to notice.
#
# Asserted over src/, which is what determines the published names, so this runs
# on a clean checkout. Re-asserted over output/asn1/ when a build is present.

echo "== asn1: source filenames are bare module names"

# The two .mib-sources control files are build input, not MIBs; the Makefile
# drops them with grep -v '^\.' when it composes the published tree.
# sort -u, not sort: 58 basenames occur in more than one source directory, and
# `comm` pairs duplicate lines -- so a non-unique list would report every extra
# occurrence as unpublished. What is published is one file per name.
SRC_NAMES="$(mktemp)"
find src -type f -exec basename {} \; | grep -v '^\.' | sort -u >"$SRC_NAMES"

DOTTED="$(grep -c '\.' "$SRC_NAMES" || true)"
if [ "$DOTTED" = "0" ]; then
  pass "no source module name carries an extension"
else
  fail "$DOTTED source module names carry an extension; @mib@ substitution would 404"
  grep '\.' "$SRC_NAMES" | head -5 >&2
fi

UNSAFE="$(grep -c '[^A-Za-z0-9._~-]' "$SRC_NAMES" || true)"
if [ "$UNSAFE" = "0" ]; then
  pass "every source module name is URL-safe unescaped"
else
  fail "$UNSAFE source module names need percent-encoding; those modules are unfetchable"
  grep '[^A-Za-z0-9._~-]' "$SRC_NAMES" | head -5 >&2
fi
# Deliberately not removed here: the published-set check below compares against
# it, and a name-shape check that passes while the module is unreachable is the
# gap that check exists to close.
trap 'rm -f "$SRC_NAMES"' EXIT

# ---------------------------------------------------------------------------
# standard.txt -- characterized, not depended on
# ---------------------------------------------------------------------------
#
# standard.txt has no reader.
#
# sc4snmp binds MIB_STANDARD at splunk_connect_for_snmp/snmp/manager.py:57 and
# never reads it. The chart plumbs the variable onto five workloads and
# docker-compose sets it, all to a value nothing consumes.
#
# It was read once. 5b6600c ("feat: Load all standard mibs", 2022-01-16) fetched
# the file and called loadModules() per line, falling back to the hardcoded
# DEFAULT_STANDARD_MIBS list on a non-200. 824fa56 ("feat: configure group of
# hosts", 2022-09-09) deleted the commented-out remains and left the fallback as
# the only path. It has been the only path since, through sc4snmp 1.17.0.
#
# That the fallback won is unsurprising once you look at what the file contains:
# the Makefile builds it with `grep -v '^RFC' | grep -v '^SNMPv2'`, so every
# SNMPv2* module is excluded by construction -- SNMPv2-MIB among them, the
# module holding sysDescr and sysUpTime. A consumer preloading exactly this list
# would not have the core SMI module loaded. DEFAULT_STANDARD_MIBS names
# SNMPv2-MIB explicitly.
#
# So this is pinned as characterization: the shape so a change declares itself,
# and the SNMPv2 exclusion so the gap stays visible. It is deliberately not a
# membership pin -- pinning a sampled set would assert the list is authoritative
# for something, and it is not.

if [ -f output/standard.txt ]; then
  echo "== standard.txt: one bare module name per line"

  BLANK="$(grep -c '^[[:space:]]*$' output/standard.txt || true)"
  [ "$BLANK" = "0" ] || fail "$BLANK blank lines in standard.txt"
  [ "$BLANK" = "0" ] && pass "no blank lines"

  # One field, so no consumer can mistake it for the CSV that sits beside it.
  NOTBARE="$(grep -c '[,[:space:]]' output/standard.txt || true)"
  [ "$NOTBARE" = "0" ] || fail "$NOTBARE lines carry a comma or whitespace"
  [ "$NOTBARE" = "0" ] && pass "every line is a single bare token"

  STDDOTTED="$(grep -c '\.' output/standard.txt || true)"
  [ "$STDDOTTED" = "0" ] || fail "$STDDOTTED entries carry an extension"
  [ "$STDDOTTED" = "0" ] && pass "no entry carries an extension"

  STDDUPES="$(sort output/standard.txt | uniq -d | grep -c . || true)"
  [ "$STDDUPES" = "0" ] || fail "$STDDUPES module names appear more than once"
  [ "$STDDUPES" = "0" ] && pass "no module name appears twice"

  echo "== standard.txt: the SNMPv2 and RFC exclusions, pinned as they are"
  # Not a defect to fix here. Correcting the list would change what any future
  # reader loads, and there is no reader to benefit; #366 decides its fate.
  for excluded in SNMPv2-MIB SNMPv2-SMI SNMPv2-TC; do
    if grep -qx "$excluded" output/standard.txt; then
      fail "$excluded is present, but the build excludes every SNMPv2* module"
    else
      pass "$excluded absent (excluded by construction -- see the note above)"
    fi
  done

  RFCENTRIES="$(grep -c '^RFC' output/standard.txt || true)"
  [ "$RFCENTRIES" = "0" ] || fail "$RFCENTRIES RFC* entries, which the build excludes"
  [ "$RFCENTRIES" = "0" ] && pass "no RFC* entries"

  # A floor, not an exact count: modules are added and removed routinely, and an
  # exact pin would fail on every legitimate addition. What this catches is the
  # file collapsing to a handful of entries or to nothing, which is what a broken
  # find or a changed src/ layout would produce.
  STDCOUNT="$(grep -c . output/standard.txt || true)"
  if [ "$STDCOUNT" -ge 250 ]; then
    pass "$STDCOUNT entries, above the floor of 250"
  else
    fail "standard.txt has $STDCOUNT entries, below the floor of 250 -- looks truncated"
  fi
elif [ -d output ]; then
  fail "output/standard.txt is missing, but output/ exists -- the build did not complete"
else
  echo "== output/ absent, skipping the standard.txt checks"
  echo "     run 'make index' first to include them"
fi

if [ -d output/asn1 ]; then
  echo "== asn1: published filenames are bare module names"
  PUB="$(mktemp)"
  find output/asn1 -maxdepth 1 -type f -exec basename {} \; | sort >"$PUB"

  PUBCOUNT="$(grep -c . "$PUB" || true)"
  PUBDOTTED="$(grep -c '\.' "$PUB" || true)"
  PUBUNSAFE="$(grep -c '[^A-Za-z0-9._~-]' "$PUB" || true)"

  [ "$PUBDOTTED" = "0" ] || fail "$PUBDOTTED published filenames carry an extension"
  [ "$PUBDOTTED" = "0" ] && pass "no published filename carries an extension"

  [ "$PUBUNSAFE" = "0" ] || fail "$PUBUNSAFE published filenames need percent-encoding"
  [ "$PUBUNSAFE" = "0" ] && pass "every published filename is URL-safe unescaped"

  # Same reasoning as the standard.txt floor.
  if [ "$PUBCOUNT" -ge 250 ]; then
    pass "$PUBCOUNT modules published, above the floor of 250"
  else
    fail "output/asn1 holds $PUBCOUNT modules, below the floor of 250 -- looks truncated"
  fi

  # -------------------------------------------------------------------------
  # Every source module reaches the published tree
  # -------------------------------------------------------------------------
  #
  # A correctly-named module nothing publishes is worse than a badly-named one:
  # index.py still indexes it, so MIB_INDEX names a module MIB_SOURCES answers
  # 404 for, and the two published artifacts disagree.
  #
  # Nineteen modules were in that state, all under src/vendor/alcatel/stellar,
  # two of them carrying 30 rows in index-frozen.csv between them. Fixed in
  # pysnmp/mibs#371: scripts/vendorsingle.sh compiled with a recursive find but
  # published with `cp -f $1/*`, which is not recursive, so a nested vendor
  # directory never reached output/asn1. The exception list this check carried
  # is gone with them; the assertion is now absolute.
  echo "== asn1: every source module reaches the published tree"
  MISSING="$(mktemp)"
  comm -23 "$SRC_NAMES" "$PUB" >"$MISSING"
  UNPUBLISHED="$(grep -c . "$MISSING" || true)"

  if [ "$UNPUBLISHED" = "0" ]; then
    pass "every source module is published"
  else
    fail "$UNPUBLISHED source modules are absent from output/asn1"
    head -10 "$MISSING" >&2
  fi
  rm -f "$MISSING" "$PUB"
elif [ -d output ]; then
  fail "output/asn1 is missing, but output/ exists -- the build did not complete"
fi

echo
if [ "$FAILURES" -gt 0 ]; then
  echo "FAILED: $FAILURES check(s)" >&2
  exit 1
fi
echo "PASS"
