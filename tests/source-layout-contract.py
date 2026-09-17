#!/usr/bin/env python3
#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""One module, one file, named for the module it holds.

``src/`` is the repository's input, and everything downstream assumes a
shape it never actually asserted: that a path under ``src/vendor/`` names
the module inside it. The freshness tooling looks a module up by that
path. The publisher stages each file by that name. A reviewer reads a
diff on ``src/vendor/acme/ACME-MIB`` believing it is a change to
``ACME-MIB``.

A file holding several modules breaks all three. It publishes once per
module it declares, the same bytes written out under every name, so a
vendor blob declaring dozens of modules squared its own size in the
distribution, and every copy carried all the other modules with it. A
change to any one of them showed up as a diff against a file named for a
different module. No build step failed over it, and no check reported
the shape.

This one does. Every file under ``src/`` declares exactly one module,
is named for that module, and carries no extension. Vendors ship
``.mib``, ``.my``, ``.txt`` and bare names interchangeably and a
contributor's own collection may be any mixture -- the convention is
what this repository stores, not what it accepts, and
``scripts/import_contribution.py`` normalises on the way in.

Splitting a combined file is a solved problem: pysmi 5.3's
``pysmi.mibinfo.module_text`` cuts one module out of a file at the lexer's
own token boundaries, preamble and introducing comment included, which is
how the Extreme blob was split without changing a byte of any module's
compiled output.

One interaction is worth knowing before splitting anything with
provenance. ``scripts/mib_sources.py`` confirms drift by comparing the
publisher's *whole* served file, plus our patch, against what is checked
in. Split a module out of a file the publisher serves combined and that
comparison can no longer hold, because the two sides are no longer the
same unit. No module in the tree is both today -- the one combined file
had no ``mib-sources.json`` entry -- so the answer is not machinery, it
is: if you split a module that has provenance, the entry needs rewriting
at the same time.

Run directly; no test framework, and no network:

    uv run python tests/source-layout-contract.py [src-dir]
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

from mib_sources import module_names

#: How many failures of one kind to name before saying "and N more". A
#: first run after a bad import can trip hundreds, and a wall of them
#: buries the other two kinds underneath.
SHOWN = 20


def offences(
    root: pathlib.Path,
) -> tuple[list[str], list[str], list[str], set[str], int]:
    """Read every file under *root* and sort what is wrong with it.

    Returns:
        Extensioned names, combined files, misnamed files, the paths those
        name between them, and the number of files read -- so a run that
        matched nothing because it was pointed at the wrong directory says
        so rather than passing.
    """
    extensioned: list[str] = []
    combined: list[str] = []
    misnamed: list[str] = []
    offending: set[str] = set()
    read = 0

    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.name.startswith("."):
            # Hidden files are this repository's own metadata, not MIBs:
            # src/vendor/cisco/.mib-sources is a per-vendor note, and
            # naming it for a module it does not hold would be worse.
            continue

        read += 1
        shown = path.relative_to(root.parent)

        if "." in path.name:
            extensioned.append(f"{shown}: has an extension; store it as {path.stem}")
            offending.add(str(shown))

        declared = module_names(path.read_bytes())
        named = ", ".join(declared[:4]) + (", ..." if len(declared) > 4 else "")

        if len(declared) > 1:
            combined.append(f"{shown}: declares {len(declared)} modules ({named})")
            offending.add(str(shown))
        elif not declared:
            combined.append(f"{shown}: declares no MIB module at all")
            offending.add(str(shown))
        elif declared[0] != path.stem:
            misnamed.append(f"{shown}: declares {declared[0]}")
            offending.add(str(shown))

    return extensioned, combined, misnamed, offending, read


def report(title: str, remedy: str, found: list[str]) -> None:
    """Print one kind of failure, capped, with what to do about it."""
    if not found:
        return

    sys.stderr.write(f"\n{title} ({len(found)}):\n")

    for line in found[:SHOWN]:
        sys.stderr.write(f"  {line}\n")

    if len(found) > SHOWN:
        sys.stderr.write(f"  ... and {len(found) - SHOWN} more\n")

    sys.stderr.write(f"  -> {remedy}\n")


def main(argv: list[str]) -> int:
    """Check the tree and say what is wrong with it."""
    root = pathlib.Path(argv[1] if len(argv) > 1 else "src")

    if not root.is_dir():
        sys.stderr.write(f"{root}: not a directory\n")
        return 1

    extensioned, combined, misnamed, offending, read = offences(root)

    if not read:
        sys.stderr.write(f"{root}: no files to check -- wrong directory?\n")
        return 1

    report(
        "Files carrying an extension",
        "rename to the bare module name; the corpus addresses modules by name",
        extensioned,
    )
    report(
        "Files not holding exactly one module",
        "split with pysmi.mibinfo.module_text, one module per file, each named"
        " for its module -- and rewrite any mib-sources.json entry for it,"
        " which compares the publisher's whole file",
        combined,
    )
    report(
        "Files named for a module they do not declare",
        "rename the file to the module it declares, or fix the declaration",
        misnamed,
    )

    if offending:
        sys.stderr.write(
            f"\n{len(offending)} of {read} files under {root} break the layout"
            " contract.\n"
        )
        return 1

    sys.stdout.write(
        f"{read} files under {root}: one module each, named for it, no extensions.\n"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
