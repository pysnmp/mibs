#!/usr/bin/env python3
#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Regenerate the inventory half of `broken/README.md` from a build.

The page has two halves. Above `## Why each one is here` is prose: what
`broken/` is for, how to bring a module back, the handful of modules that are
quarantined for a reason other than a defect. That is written by hand and this
does not touch it.

Below it is one table per vendor naming every quarantined module and why. That
is a rendering of what the compiler says, and every import into `broken/` or
restoration out of it leaves it wrong. Nothing was regenerating it, so it drifted
-- the same way pysmi's bundled-MIB inventory had drifted from its generator.

The measurement is a corpus build with `src/vendor/*` resolving and
`broken/vendor/*` publishing, which is the arrangement that asks "would this
module compile if it came back?" and nothing else. Each entry lands in one of
two shapes:

* **root defect** -- the compiler rejected the module's own text.
* **consequential** -- it was rejected while compiling a module it imports that
  is also quarantined, or it compiles and imports one.

A module that compiles and imports nothing quarantined is in neither: it is
here for a reason the prose has to state, and this refuses rather than
inventing one for it. It names every such module in the refusal, because each
one costs a build to find.

Usage:

    uv run python scripts/update_broken_inventory.py [--check]
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "broken" / "README.md"

#: Where the generated half starts. Everything from here down is replaced.
HEADING = "## Why each one is here"

#: ``IMPORTS a, b FROM MODULE-NAME c FROM OTHER-MODULE;`` -- the module names a
#: module imports from, which is what makes an entry consequential when the
#: module itself compiles.
IMPORTS = re.compile(rb"\bFROM\s+([A-Za-z][\w-]*)")

#: The error the compiler gives for a module rejected because of another one.
#: The name in it is what makes an entry consequential rather than a defect.
BLAMES = re.compile(r'\bMIB ([A-Za-z][\w-]*)|module "([A-Za-z][\w-]*)"')

#: Namespaces the prose accounts for under "Not defective, but not usable here
#: either". Their modules are not defects to describe, and a build says nothing
#: useful about them: what keeps them out of `src/` is that the corpus is keyed
#: by bare module name, not anything the compiler can see.
NOT_DEFECTIVE = {"alcatel-aos6"}

#: What the table says for one of those, pointing at the prose that explains it.
ACCOUNTED_FOR = (
    "compiles; see [Not defective](#not-defective-but-not-usable-here-either)"
)


class Refused(Exception):
    """Something this will not do, phrased for the person who asked."""


def quarantined() -> dict[str, pathlib.Path]:
    """Every module under `broken/`, by name."""
    return {
        path.name: path
        for path in sorted((ROOT / "broken").rglob("*"))
        if path.is_file() and path.name != "README.md" and not path.name.startswith(".")
    }


def build(destination: pathlib.Path) -> dict:
    """Compile `broken/` against `src/`, and hand back the report.

    Args:
        destination: a directory for the artifacts, which are thrown away.

    Returns:
        The build report pysmi wrote.

    Raises:
        Refused: the build did not produce one.
    """
    command = [
        "uv",
        "run",
        "mibcorpus",
        "--resolve-namespace=standard:standard:package:pysmi.mibs.asn1",
        *(
            f"--resolve-namespace=vendor:{path.name}:{path.relative_to(ROOT)}"
            for path in sorted((ROOT / "src/vendor").iterdir())
            if path.is_dir()
        ),
        *(
            f"--namespace=vendor:{path.name}:{path.relative_to(ROOT)}"
            for path in sorted((ROOT / "broken/vendor").iterdir())
            if path.is_dir()
        ),
        f"--output-directory={destination}",
        "--emit=report",
        "--emit=index",
    ]
    subprocess.run(command, cwd=ROOT, check=True, capture_output=True)
    report = destination / "report.json"

    if not report.is_file():
        raise Refused(f"the build wrote no report to {destination}")

    return json.loads(report.read_text(encoding="utf-8"))


def cell(text: str) -> str:
    """Error text safe to put in a Markdown table cell.

    Two things the compiler hands back that the table cannot take verbatim.
    A pipe ends the cell, and an error naming a symbol with one in it would
    silently add a column. And an "Illegal character" message quotes the
    character it refused, which for A3COM0074-SMA-VLAN-SUPPORT is a literal
    NUL -- git then calls the whole page binary and stops diffing it, which
    is how this was found.

    Args:
        text: what the compiler said.

    Returns:
        The same text with pipes escaped and unprintables spelled out.
    """
    out = []

    for char in text:
        if char == "|":
            out.append("\\|")
        elif char.isprintable():
            out.append(char)
        else:
            out.append(f"\\x{ord(char):02x}")

    return "".join(out)


def reason_for(
    module: str, vendor: str, error: str | None, imports: set[str], here: set[str]
) -> str | None:
    """Why this module is quarantined, in the words the table carries.

    Args:
        module: the module being described.
        vendor: the namespace it sits in under `broken/`.
        error: what the compiler said, or None if it compiled.
        imports: the modules it imports.
        here: every quarantined module name.

    Returns:
        One cell of the table, or None when this module needs a decision that
        only a person can make. The caller collects those and reports them
        together: each one costs a build to find, so finding them one at a
        time is finding them one build at a time.
    """
    if vendor in NOT_DEFECTIVE:
        return ACCOUNTED_FOR

    if error is None:
        blocking = sorted(imports & here - {module})

        if blocking:
            return f"needs `{blocking[0]}` (also here), which does not compile"

        return None

    blamed = {
        name
        for match in BLAMES.finditer(error)
        for name in match.groups()
        if name and name != module
    }
    consequential = sorted(blamed & here)

    if consequential:
        return f"needs `{consequential[0]}` (also here), which does not compile"

    # The compiler's own words, trimmed to a table cell. Truncating loses the
    # tail of a long defval message and keeps the row readable; the module and
    # the symbol, which is what a person searches for, are at the front.
    said = " ".join(error.split())
    said = said.split(" at MIB ")[0]
    said = said[:117] + "…" if len(said) > 118 else said

    return cell(said)


def sections(rows: dict[str, tuple[str, str]]) -> list[str]:
    """The generated half of the page, as lines."""
    by_vendor: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)

    for module, (vendor, reason) in rows.items():
        by_vendor[vendor].append((module, reason))

    shapes = collections.Counter(
        "accounted for"
        if reason == ACCOUNTED_FOR
        else "consequential"
        if "also here" in reason
        else "root defect"
        for _, reason in rows.values()
    )
    out = [
        HEADING,
        "",
        "Generated by `scripts/update_broken_inventory.py` from a build with",
        "`src/vendor/*` resolving and `broken/vendor/*` publishing -- the",
        "arrangement that asks whether a module would compile if it came back,",
        "and nothing else. Two shapes:",
        "",
        "- **root defect** -- the module's own text is rejected.",
        "- **consequential** -- it is rejected, or cannot be served, because a",
        "  module it imports is also here.",
        "",
        "A consequential entry usually returns to `src/` on its own once the",
        "module it imports is replaced.",
        "",
        f"{shapes['root defect']} root defects, "
        f"{shapes['consequential']} consequential, and "
        f"{shapes['accounted for']} the prose above accounts for.",
        "",
    ]

    for vendor in sorted(by_vendor):
        out += [f"### {vendor}", "", "| module | reason |", "| --- | --- |"]
        out += [
            f"| `{module}` | {reason} |" for module, reason in sorted(by_vendor[vendor])
        ]
        out.append("")

    return out


def compose() -> str:
    """The whole page: the prose as it stands, the inventory rebuilt."""
    here = quarantined()
    prose = PAGE.read_text(encoding="utf-8")

    if HEADING not in prose:
        raise Refused(f"{PAGE} has no '{HEADING}' heading to regenerate under")

    with tempfile.TemporaryDirectory() as scratch:
        report = build(pathlib.Path(scratch))

    errors = report.get("failed", {}).get("json", {})
    names = set(here)
    rows: dict[str, tuple[str, str]] = {}
    undecided = []

    for module, path in here.items():
        imports = {
            match.group(1).decode("ascii", "replace")
            for match in IMPORTS.finditer(path.read_bytes())
        }
        reason = reason_for(
            module, path.parent.name, errors.get(module), imports, names
        )

        if reason is None:
            undecided.append(str(path.relative_to(ROOT)))
            continue

        rows[module] = (path.parent.name, reason)

    if undecided:
        raise Refused(
            "These compile and import nothing quarantined, so nothing here can "
            "say why they are under broken/. Restore each one to src/, or "
            "describe it under '## Not defective, but not usable here either' "
            "and add its namespace to NOT_DEFECTIVE:\n\n  "
            + "\n  ".join(sorted(undecided))
        )

    kept = prose[: prose.index(HEADING)]

    return kept + "\n".join(sections(rows)).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero if the page is not what a build produces",
    )
    options = parser.parse_args(argv)

    try:
        wanted = compose()
    except Refused as refusal:
        print(refusal, file=sys.stderr)
        return 2

    if options.check:
        if PAGE.read_text(encoding="utf-8") == wanted:
            print(f"{PAGE.relative_to(ROOT)} is what a build produces")
            return 0

        print(
            f"{PAGE.relative_to(ROOT)} is not what a build produces. Run "
            f"scripts/update_broken_inventory.py.",
            file=sys.stderr,
        )
        return 1

    PAGE.write_text(wanted, encoding="utf-8")
    print(f"wrote {PAGE.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
