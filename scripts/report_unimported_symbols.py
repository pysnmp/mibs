#!/usr/bin/env python3
#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Modules that use a standard symbol without naming it in IMPORTS.

RFC 2578 section 3.2 says every symbol a module uses and did not define
itself has to be in its ``IMPORTS`` clause. Two different things break that
rule here, and only one of them is visible to the compiler.

The visible one is ``SMI-MISSING-IMPORT``: a symbol undefined, unimported,
and exported by exactly one SMIv2 base module. pysmi supplies the import
rather than failing, records the module in ``report.json``'s ``repaired``
map, and the CI step "No module is repaired at build time" fails the build
over it. Eighteen modules were fixed that way in #435.

The invisible one is this. A macro the grammar already knows --
``MODULE-IDENTITY``, ``TEXTUAL-CONVENTION``, ``NOTIFICATION-TYPE`` -- or a
base type the relaxed parser resolves never becomes an undefined symbol, so
``missing_canonical_imports`` has nothing to report, ``repaired`` stays empty
and ``mibdump --strict-imports`` passes. ``AH_TRAP_MIB`` and ``EDFA-oa-MIB``
were found in #435 by a reviewer reading the diff, which does not scale to
6,976 modules.

What this looks for
-------------------

Only uses the grammar makes unambiguous, so that a finding is a fact rather
than a guess:

* a macro invocation, ``<descriptor> <MACRO>`` alone on a line
* a type reference, ``SYNTAX <Type>``

and only for names on the two closed lists below. A module that shows one and
neither defines nor imports the name is missing an import. Nothing here infers
what the vendor meant; the repair is a separate decision.

The baseline
------------

562 modules already carry this, about 8% of the corpus, and they cannot all
be fixed at once. ``unimported-symbols.txt`` records what is known, and
``--check`` fails only on a module that is not in it -- so the debt cannot
grow while it is being paid down, and a module fixed and removed from the
baseline cannot come back.

Usage:

    uv run python scripts/report_unimported_symbols.py           # report
    uv run python scripts/report_unimported_symbols.py --check   # CI gate
    uv run python scripts/report_unimported_symbols.py --baseline  # rewrite it
"""

from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
BASELINE = ROOT / "unimported-symbols.txt"

#: SMI macros. A macro is invoked as ``<descriptor> <MACRO>`` on a line of its
#: own, which no other construct looks like.
MACROS = frozenset(
    {
        "AGENT-CAPABILITIES",
        "MODULE-COMPLIANCE",
        "MODULE-IDENTITY",
        "NOTIFICATION-GROUP",
        "NOTIFICATION-TYPE",
        "OBJECT-GROUP",
        "OBJECT-IDENTITY",
        "OBJECT-TYPE",
        "TEXTUAL-CONVENTION",
        "TRAP-TYPE",
    }
)

#: Base types and the textual conventions SNMPv2-TC publishes. Counted only
#: where they appear as ``SYNTAX <Type>``, which is a type reference and
#: nothing else.
TYPES = frozenset(
    {
        "AutonomousType",
        "Counter32",
        "Counter64",
        "DateAndTime",
        "DisplayString",
        "Gauge32",
        "InstancePointer",
        "Integer32",
        "IpAddress",
        "MacAddress",
        "Opaque",
        "PhysAddress",
        "RowPointer",
        "RowStatus",
        "SnmpAdminString",
        "StorageType",
        "TestAndIncr",
        "TimeInterval",
        "TimeStamp",
        "TimeTicks",
        "TruthValue",
        "Unsigned32",
        "VariablePointer",
    }
)

USE_MACRO = re.compile(r"^[ \t]*[a-zA-Z][\w-]*[ \t]+([A-Z][A-Z0-9-]+)[ \t]*$", re.M)
USE_SYNTAX = re.compile(r"\bSYNTAX[ \t]+([A-Za-z][\w-]*)")
IMPORTS = re.compile(r"IMPORTS(.*?);", re.S)
DEFINES = re.compile(r"^[ \t]*([A-Za-z][\w-]*)[ \t]*::=", re.M)
COMMENT = re.compile(r"--.*?(?:--|$)", re.M)


def missing(text: str) -> list[str]:
    """Standard symbols a module's text uses and does not account for.

    Args:
        text: the module's ASN.1 source.

    Returns:
        The names, sorted. Empty when the module accounts for everything it
        uses, which is what most of the corpus does.
    """
    body = COMMENT.sub("", text)
    clause = IMPORTS.search(body)
    imported = set(re.findall(r"[A-Za-z][\w-]*", clause.group(1))) if clause else set()
    defined = set(DEFINES.findall(body))
    used = {name for name in USE_MACRO.findall(body) if name in MACROS}
    used |= {name for name in USE_SYNTAX.findall(body) if name in TYPES}

    return sorted(used - imported - defined)


def scan() -> dict[str, list[str]]:
    """Every module under ``src/`` that is missing one, by repository path."""
    found = {}

    for path in sorted(SRC.rglob("*")):
        if not path.is_file():
            continue

        names = missing(path.read_text(errors="replace"))

        if names:
            found[path.relative_to(ROOT).as_posix()] = names

    return found


def read_baseline() -> dict[str, list[str]]:
    """The recorded debt, as ``path: symbols``."""
    if not BASELINE.is_file():
        return {}

    out = {}

    for line in BASELINE.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()

        if line:
            path, _, names = line.partition(" ")
            out[path] = sorted(filter(None, names.split(",")))

    return out


def write_baseline(found: dict[str, list[str]]) -> None:
    """Record what the tree holds now."""
    lines = [
        "# Modules using a standard symbol they do not import, by path.",
        "# Written by scripts/report_unimported_symbols.py --baseline.",
        "# A module may leave this file. Nothing may join it without a person",
        "# deciding to record the debt rather than fix it.",
        "",
    ]
    lines += [f"{path} {','.join(names)}" for path, names in sorted(found.items())]
    BASELINE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="fail on a new one")
    group.add_argument("--baseline", action="store_true", help="rewrite the record")
    options = parser.parse_args(argv)

    found = scan()

    if options.baseline:
        write_baseline(found)
        print(f"recorded {len(found)} modules in {BASELINE.relative_to(ROOT)}")
        return 0

    if options.check:
        known = read_baseline()
        fresh = {p: n for p, n in found.items() if p not in known}
        grown = {
            p: sorted(set(n) - set(known[p]))
            for p, n in found.items()
            if p in known and set(n) - set(known[p])
        }

        for path, names in sorted(fresh.items()):
            print(
                f"  {path}: uses {', '.join(names)} without importing", file=sys.stderr
            )

        for path, names in sorted(grown.items()):
            print(f"  {path}: newly uses {', '.join(names)}", file=sys.stderr)

        if fresh or grown:
            print(
                f"\n{len(fresh) + len(grown)} module(s) use a standard symbol they do "
                "not import, beyond what unimported-symbols.txt records. Add the "
                "symbol to the FROM group for the module that exports it -- "
                "SNMPv2-SMI for the base types and macros, SNMPv2-TC for the "
                "textual conventions.",
                file=sys.stderr,
            )
            return 1

        gone = sorted(set(known) - set(found))

        for path in gone:
            print(f"  {path}: fixed, and still in the baseline")

        if gone:
            print(
                f"\n{len(gone)} module(s) no longer need their baseline entry. Run "
                "scripts/report_unimported_symbols.py --baseline.",
                file=sys.stderr,
            )
            return 1

        print(f"no module uses a standard symbol beyond the {len(known)} recorded")
        return 0

    counts = collections.Counter(name for names in found.values() for name in names)
    print(f"{len(found)} modules, {sum(counts.values())} uses")

    for name, count in counts.most_common():
        print(f"  {count:>4}  {name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
