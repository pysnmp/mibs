#!/usr/bin/env python3
"""The published tree, driven the way splunk-connect-for-snmp drives it.

``tests/index-contract.sh`` and ``tests/artifact-contract.sh`` check the
artifacts as files. This checks them as a working MIB source: a real
``MibBuilder`` with a runtime compiler over ``output/asn1``, resolving varbinds
through the same three steps sc4snmp takes.

sc4snmp's poll loop, from ``splunk_connect_for_snmp/snmp/manager.py``:

1. at startup, ``compiler.addMibCompiler(builder,
   sources=[MIB_SOURCES])``, then ``loadModules()`` over
   ``DEFAULT_STANDARD_MIBS``
2. per varbind, resolve it and ask ``is_mib_resolved()`` whether the name that
   came back is a real one or a bare SMI anchor
3. when it is a bare anchor, ``is_mib_known()`` walks the OID tail arc by arc
   against the index, longest prefix first, and ``load_mibs()`` loads whatever
   module the index names

Steps 2 and 3 are reproduced here verbatim rather than approximated,
because the point is to test their behaviour against our artifacts and not
our reading of them. They are the only code in this file copied from
elsewhere, and they are marked.

Two things about this setup are worth stating, because both make the test
weaker than it looks if left implicit.

**pysmi's bundle backs MIB_SOURCES.** ``pysnmp.smi.compiler.addMibCompiler``
constructs a ``MibCompiler`` without passing ``useBundledMibs``, which
defaults to True, so pysmi's own bundled ASN.1 is registered as a priority
source ahead of anything from ``sources=``. It carries ~300 standard
modules. Every module in ``DEFAULT_STANDARD_MIBS`` is among them, so
sc4snmp's startup preload is satisfied whether or not this repository
publishes anything -- deleting all six from ``output/asn1`` changes nothing
observable. What ``MIB_SOURCES`` uniquely supplies is vendor MIBs and the
standard modules the bundle lacks.

So the end-to-end section below tests the deployed path and proves it works; it
does not prove our tree is what served it. ``check_tree_is_self_sufficient()``
is the part that pins our artifact, by compiling with the bundle switched off.

**``@mib@`` is an HTTP-only template.** ``getReadersFromUrls`` builds an
``HttpReader`` from the whole URL, which substitutes, but a ``file://`` URL
becomes a ``FileReader`` over the literal path -- so ``file://...//@mib@``
reads a directory named ``@mib@``, which does not exist, and silently
supplies nothing. The local spelling is the directory alone. An earlier
draft of this file had the ``@mib@`` form and passed every check on the
bundle without reading our tree at all.

Output matches the two shell contract tests so all three read alike in CI.

See pysnmp/mibs#362.
"""

import csv
import os
import pathlib
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
os.chdir(ROOT)

TREE = ROOT / "output" / "asn1"
FROZEN = ROOT / "index-frozen.csv"

FAILURES = 0


def fail(message):
    global FAILURES
    print(f"FAIL: {message}", file=sys.stderr)
    FAILURES += 1


def ok(message):
    print(f"  ok   {message}")


# --- copied from sc4snmp, unmodified ----------------------------------------
# splunk_connect_for_snmp/snmp/manager.py at 1.17.0.
#
# Unmodified means unmodified, down to `is_mib_resolved(id)` shadowing a
# builtin: the value of this block is that it diffs clean against theirs, so a
# reader can confirm at a glance that we test their behaviour and not our
# transcription of it. Renaming would be safe and would cost exactly that.

DEFAULT_STANDARD_MIBS = [
    "HOST-RESOURCES-MIB",
    "IF-MIB",
    "IP-MIB",
    "SNMPv2-MIB",
    "TCP-MIB",
    "UDP-MIB",
]


def is_mib_resolved(id):
    return not id.startswith(
        ("RFC1213-MIB::", "SNMPv2-SMI::enterprises.", "SNMPv2-SMI::mib-2")
    )


def is_mib_known(oid, mib_map):
    oid_list = tuple(oid.split("."))
    # if oid match enterprise, then search should stop if there is no match to
    # vendor
    start = 6 if oid.startswith("1.3.6.1.4.1") else 5
    for i in range(len(oid_list), start, -1):
        oid_to_check = ".".join(oid_list[:i])
        if oid_to_check in mib_map:
            return True, mib_map[oid_to_check]
    return False, ""


# --- end copied code --------------------------------------------------------

#: One varbind per preloaded module, chosen to be an object the module defines
#: rather than one it imports, so a resolution failure names the right module.
PRELOADED_VARBINDS = [
    ("1.3.6.1.2.1.1.1.0", "SNMPv2-MIB::sysDescr.0"),
    ("1.3.6.1.2.1.2.2.1.2.1", "IF-MIB::ifDescr.1"),
    ("1.3.6.1.2.1.4.20.1.1.1.2.3.4", "IP-MIB::ipAdEntAddr.1.2.3.4"),
    ("1.3.6.1.2.1.6.13.1.1", "TCP-MIB::tcpConnState"),
    ("1.3.6.1.2.1.7.5.1.1", "UDP-MIB::udpLocalAddress"),
    ("1.3.6.1.2.1.25.1.1.0", "HOST-RESOURCES-MIB::hrSystemUptime.0"),
]

#: The lazy-load path: an OID none of the preloaded six covers, which sc4snmp
#: therefore takes to the index. Each entry is the OID, the module the frozen
#: index names for it, and the name that must come back once that module loads.
LAZY_LOADED = [
    (
        "1.3.6.1.2.1.17.1.1.0",
        "BRIDGE-MIB",
        "BRIDGE-MIB::dot1dBaseBridgeAddress.0",
    ),
    (
        "1.3.6.1.2.1.47.1.1.1.1.2.1",
        "ENTITY-MIB",
        "ENTITY-MIB::entPhysicalDescr.1",
    ),
    # RMON. This was a known failure until the runtime pin moved to
    # pysnmplib: ``RFC1271-MIB`` imports ``DisplayString`` from
    # ``RFC1158-MIB``, which is in pysmi's ``PySnmpCodeGen.baseMibs``, so the
    # runtime compiler defers to the copy pysnmp ships rather than compiling
    # it. lextudio/pysnmp shipped a 2017 copy exporting two symbols, none of
    # them ``DisplayString``. pysnmp/pysnmp#198 deleted that base layer, so
    # pysmi's own module is what loads and the import resolves.
    (
        "1.3.6.1.2.1.16.1.1.1.1.1",
        "RFC1271-MIB",
        "RFC1271-MIB::etherStatsIndex.1",
    ),
]

#: Failures recorded rather than omitted, so a fix flips a test.
#:
#: Empty. RMON was the only entry and it moved into ``LAZY_LOADED`` when the
#: runtime pin moved from lextudio/pysnmp to pysnmplib -- see #381 for why the
#: old pin meant no release of pysnmp/pysnmp could ever be observed here, and
#: the note on that entry for what fixed it.
#:
#: Kept as a list rather than deleted with its last entry: the distinction it
#: draws is still the one this file needs. A wrong-but-frozen index answer in
#: ``tests/index-contract.sh`` is a compatibility guarantee, and pinning one as
#: a bug would assert a guarantee is a defect. An entry here is a hard failure
#: that preserves nothing and that no consumer can depend on.
KNOWN_FAILURES: list[tuple[str, str, str]] = []

#: Modules output/asn1 must be able to supply without pysmi's bundle helping.
#: The preloaded six plus the lazy-load targets: everything this file asserts a
#: resolution for.
SELF_SUFFICIENT = DEFAULT_STANDARD_MIBS + [m for _, m, _ in LAZY_LOADED]


def load_index():
    mib_map = {}
    with FROZEN.open() as handle:
        for row in csv.reader(handle):
            if len(row) == 2:
                mib_map[row[1]] = row[0]
    return mib_map


def check_tree_is_self_sufficient():
    """Compile from output/asn1 alone, with pysmi's bundle switched off.

    This is the check that pins our artifact rather than pysmi's. With
    ``useBundledMibs=False`` a module the tree lacks reports ``missing``
    instead of being quietly supplied from elsewhere, so a module dropped
    from the published corpus fails here and nowhere else.
    """
    # The pre-commit mypy hook runs isolated, with no project
    # dependencies installed, hence the ignores on these imports.
    from pysmi.codegen import PySnmpCodeGen  # type: ignore
    from pysmi.compiler import MibCompiler  # type: ignore
    from pysmi.parser import SmiV1CompatParser  # type: ignore
    from pysmi.reader import getReadersFromUrls  # type: ignore
    from pysmi.writer import PyFileWriter  # type: ignore

    print("== output/asn1 supplies these, with pysmi's bundle disabled")

    compiler = MibCompiler(
        SmiV1CompatParser(),
        PySnmpCodeGen(),
        PyFileWriter(tempfile.mkdtemp(prefix="mibs-contract-tree-")),
        useBundledMibs=False,
    )
    compiler.add_sources(*getReadersFromUrls(f"file://{TREE}"))

    # noDeps=False so an IMPORT the tree cannot satisfy surfaces here too,
    # which is the more likely way the corpus breaks.
    results = compiler.compile(*SELF_SUFFICIENT, noDeps=False)

    for module in SELF_SUFFICIENT:
        status = results.get(module, "<absent>")
        if status in ("compiled", "untouched", "unprocessed"):
            ok(f"{module} ({status})")
        else:
            fail(f"{module} is '{status}' from output/asn1 alone")

    unsatisfied = {
        name: status
        for name, status in results.items()
        if status not in ("compiled", "untouched", "unprocessed")
        and name not in SELF_SUFFICIENT
    }
    if unsatisfied:
        fail(f"dependencies the tree cannot satisfy: {unsatisfied}")
    else:
        ok(f"every dependency resolves within the tree ({len(results)})")


def main():
    if not TREE.is_dir():
        if (ROOT / "output").is_dir():
            fail(
                "output/asn1 is missing, but output/ exists -- "
                "the build did not complete"
            )
            return 1
        print("== output/asn1 absent, skipping the runtime-compile checks")
        print("     run 'make index' first to include them")
        print()
        print("PASS")
        return 0

    from pysnmp.smi import builder as smi_builder  # type: ignore
    from pysnmp.smi import compiler, rfc1902, view  # type: ignore

    check_tree_is_self_sufficient()

    mib_map = load_index()
    # A scratch destination, so the test never writes into ~/.pysnmp/mibs and
    # never reads a module an earlier run left behind.
    destination = tempfile.mkdtemp(prefix="mibs-contract-")

    builder = smi_builder.MibBuilder()
    compiler.addMibCompiler(
        builder, sources=[f"file://{TREE}"], destination=destination
    )

    # sc4snmp calls the camelCase spellings. Under pysnmplib those are the
    # API rather than deprecated aliases -- it defines no snake_case names at
    # all -- so this file calls them directly and there are no
    # DeprecationWarnings to filter. Their disappearance would still be a
    # downstream break, so the check stays.
    #
    # Worth stating plainly, because it is the cost of #381's answer: sc4snmp
    # installs lextudio/pysnmp, not pysnmplib. This section pins the names it
    # calls, against the runtime we publish rather than the one it deploys. It
    # catches us removing them; it cannot catch lextudio removing them.
    print("== the spellings sc4snmp calls exist")
    # Probed on an instance rather than the class, since a name may be served
    # through __getattr__.
    for owner, label, name in (
        (compiler, "pysnmp.smi.compiler", "addMibCompiler"),
        (builder, "MibBuilder", "loadModules"),
        (
            rfc1902.ObjectIdentity("1.3.6.1"),
            "ObjectIdentity",
            "resolveWithMib",
        ),
    ):
        if callable(getattr(owner, name, None)):
            ok(f"{label}.{name}")
        else:
            fail(f"{label}.{name} is gone; sc4snmp calls it directly")

    print("== sc4snmp's startup preload loads")
    for module in DEFAULT_STANDARD_MIBS:
        try:
            builder.loadModules(module)
            ok(f"{module} loaded")
        except Exception as exc:  # noqa: BLE001 -- the failure is the finding
            fail(f"{module} did not load: {exc}")

    def resolve(oid):
        identity = rfc1902.ObjectIdentity(oid)
        identity.resolveWithMib(view.MibViewController(builder))
        return identity.prettyPrint()

    print("== varbinds under those modules resolve to their names")
    for oid, expected in PRELOADED_VARBINDS:
        got = resolve(oid)
        if got == expected:
            ok(f"{oid} -> {expected}")
        else:
            fail(f"{oid} resolved to '{got}', expected '{expected}'")

    print("== the lazy-load path: unresolved, index lookup, load, resolve")
    for oid, expected_module, expected_name in LAZY_LOADED:
        before = resolve(oid)
        if is_mib_resolved(before):
            # Not a failure of the artifacts, but it means this case is no
            # longer exercising the path it was chosen for.
            fail(
                f"{oid} already resolves to '{before}', so sc4snmp would "
                f"never consult the index for it -- this case no longer "
                f"tests the lazy path"
            )
            continue
        ok(f"{oid} is unresolved before the lookup ({before})")

        found, module = is_mib_known(oid, mib_map)
        if not found or module != expected_module:
            fail(
                f"index answers '{module or '<absent>'}' for {oid}, "
                f"expected {expected_module}"
            )
            continue
        ok(f"index answers {module} for {oid}")

        if not (TREE / module).is_file():
            fail(f"{module} is in the index but not in the published tree")
            continue

        try:
            builder.loadModules(module)
        except Exception as exc:  # noqa: BLE001
            fail(f"{module} is published but does not load: {exc}")
            continue

        after = resolve(oid)
        if after == expected_name:
            ok(f"{oid} -> {expected_name} after loading {module}")
        else:
            fail(
                f"{oid} resolved to '{after}' after loading {module}, "
                f"expected '{expected_name}'"
            )

    if KNOWN_FAILURES:
        print("== known failures: still failing, and for the same reason")
    for oid, module, marker in KNOWN_FAILURES:
        found, named = is_mib_known(oid, mib_map)
        if named != module:
            fail(
                f"index now answers '{named or '<absent>'}' for {oid} "
                f"rather than {module}; re-check whether this known "
                f"failure still applies"
            )
            continue

        try:
            builder.loadModules(module)
        except Exception as exc:  # noqa: BLE001
            if marker in str(exc):
                ok(f"{oid} -> {module} still fails on {marker} (see KNOWN_FAILURES)")
            else:
                fail(
                    f"{oid} -> {module} fails, but on '{exc}' rather "
                    f"than {marker}; the known failure has changed and "
                    f"needs re-diagnosing"
                )
            continue

        fail(
            f"{oid} -> {module} now loads. This is good news: move it into "
            f"LAZY_LOADED with its expected name and delete it from "
            f"KNOWN_FAILURES"
        )

    print()
    if FAILURES:
        print(f"FAILED: {FAILURES} check(s)", file=sys.stderr)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
