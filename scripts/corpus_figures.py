#!/usr/bin/env python3
#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""The corpus's own figures, for the documentation to state at publish time.

Every count this distribution publishes changes when a MIB is added: the
modules, the arcs, the index rows, the pages the site renders. Written into
prose by hand, each of them is wrong at the next contribution and is a diff to
review on every one after that. So none of them is written by hand. The
documentation names a figure and this supplies it, read from what the build
and the committed artifacts already state:

==============================  ==========================================
``report.json``                 what the corpus build counted -- modules,
                                nodes, arcs, registrants, pages, bytes.
                                Written by ``make corpus`` into every
                                published tree.
``index-frozen.csv``            the frozen legacy index, committed
``registries/pen-snapshot.csv`` the reduced PEN registry, committed
``unimported-symbols.txt``      the missing-import baseline, committed
``src/vendor/``                 the source tree itself
==============================  ==========================================

The committed artifacts are themselves generated, so a figure taken from one
is a figure nobody typed. They answer without a build, which is what lets
``sphinx-build`` run on a fresh checkout. What only the build knows -- pages
rendered, bytes written, nodes defined -- falls back to a phrase naming the
scale rather than to a number nobody measured, so a local docs build states
nothing false and the published site, which builds the corpus first, states
the figure exactly. See ``docs/conf.py``.

Usage:

    uv run python scripts/corpus_figures.py             # the figures, as text
    uv run python scripts/corpus_figures.py --json      # as JSON
"""

import argparse
import csv
import json
import os
import pathlib
import re
import sys
from typing import Any

#: The repository root, from this file's own location.
ROOT = pathlib.Path(__file__).resolve().parent.parent

#: Where ``make corpus`` leaves a build report, best first. Every published
#: tree carries one and they agree on the corpus; they differ in which
#: artifacts the publication asked for, and ``github-pages`` is the tree that
#: emits the indexes the figures below want.
REPORTS = (
    "output/github-pages/report.json",
    "output/depot-site/report.json",
    "output/depot-data/report.json",
    "output-db/report.json",
)

#: The environment variable naming a report directly, for a docs build whose
#: corpus was built somewhere else -- a CI job that downloaded the
#: ``corpus-report`` artifact rather than building the corpus itself.
REPORT_ENV = "MIBS_CORPUS_REPORT"


def read_report(root: pathlib.Path = ROOT) -> dict[str, Any]:
    """Every build report this checkout has, merged block by block.

    One report per publication, and a publication carries only what it
    emitted: ``github-pages`` emits the indexes and the closure, ``depot-site``
    emits the pages and the registrants, ``depot-data`` emits the database.
    Reading the first report found therefore answers for one publication's
    artifacts and falls back for every other -- which is how the page count
    came to read "thousands of" on a build that knew it exactly.

    So the reports are merged rather than chosen: for each block, the first
    report carrying it wins, in :py:data:`REPORTS` order. They are reports of
    the same corpus from the same run, so they agree on what they share.

    Args:
        root: the repository root.

    Returns:
        The merged report, or an empty mapping where this checkout has no
        build. A report that will not parse is skipped rather than fatal: the
        figures then fall back like any other build-less checkout, rather than
        failing a documentation build over a truncated artifact.
    """
    named = os.environ.get(REPORT_ENV)
    paths = [pathlib.Path(named)] if named else [root / x for x in REPORTS]
    merged: dict[str, Any] = {}

    for path in paths:
        if not path.is_file():
            continue

        try:
            with open(path, encoding="utf-8") as fileObj:
                found = json.load(fileObj)

        except (OSError, ValueError):
            continue

        if not isinstance(found, dict):
            continue

        for key, value in found.items():
            # A block a publication did not emit is written as an empty
            # mapping, and must not shadow the publication that did emit it.
            if key not in merged or merged[key] in ({}, [], "", None):
                merged[key] = value

    return merged


def _count_lines(path: pathlib.Path, *, header: bool = False) -> int:
    """Rows of a committed artifact, or 0 where it is absent.

    Blank lines and ``#`` comments do not count -- ``unimported-symbols.txt``
    carries a header of them saying what the file is for -- and *header* drops
    the first row of a file that names its columns.
    """
    try:
        with open(path, encoding="utf-8") as fileObj:
            rows = [
                line for line in fileObj if line.strip() and not line.startswith("#")
            ]

    except OSError:
        return 0

    return max(len(rows) - 1, 0) if header else len(rows)


def _index_modules(path: pathlib.Path) -> int:
    """Distinct modules the frozen index names, or 0 where it is absent.

    ``index-frozen.csv`` is ``MODULE,OID`` with no header row, so every first
    field is a module name.
    """
    try:
        with open(path, encoding="utf-8", newline="") as fileObj:
            return len({row[0] for row in csv.reader(fileObj) if row})

    except OSError:
        return 0


def _vendors(root: pathlib.Path) -> int:
    """Namespaces under ``src/vendor/``, which is one directory per vendor."""
    where = root / "src" / "vendor"

    try:
        return sum(1 for x in where.iterdir() if x.is_dir())

    except OSError:
        return 0


def _source_modules(root: pathlib.Path) -> int:
    """Files under ``src/``, which the layout contract holds to one module each.

    ``tests/source-layout-contract.py`` is what makes this a module count
    rather than a file count: every file under ``src/`` declares exactly one
    module and is named for it.
    """
    where = root / "src"

    try:
        # Hidden files are this repository's own metadata rather than MIBs --
        # src/vendor/cisco/.mib-sources is a per-vendor note -- and
        # tests/source-layout-contract.py skips them for that reason, so the
        # contract this docstring cites does not hold them to one module each.
        return sum(
            1 for x in where.rglob("*") if x.is_file() and not x.name.startswith(".")
        )

    except OSError:
        return 0


def _megabytes(*where: pathlib.Path) -> "int | None":
    """Megabytes of the given directories, or ``None`` where none of them exist.

    Measured off the tree rather than taken from the report, which counts
    pages and rows and not the bytes an artifact weighs. ``None`` rather than
    zero where no build wrote any of them, because the two are different
    answers: a tree that exists and weighs under half a megabyte rounds to 0
    and is a measurement, while a tree that was never written is the case
    :py:func:`_size` has a phrase for.
    """
    total = 0
    written = False

    for tree in where:
        if not tree.is_dir():
            continue

        written = True
        total += sum(x.stat().st_size for x in tree.rglob("*") if x.is_file())

    return round(total / 1e6) if written else None


def _data_tree(root: pathlib.Path) -> pathlib.Path:
    """The published tree the size figures are measured over.

    ``depot-data`` is the one carrying every artifact, ``github-pages`` the
    fallback for a build that wrote only that publication. Whichever exists is
    the same corpus; they differ in whether ``json/`` carries the MIB texts.
    """
    for tree in ("output/depot-data", "output/github-pages"):
        where = root / tree

        if where.is_dir():
            return where

    return root / "output" / "depot-data"


def _grouped(count: int) -> str:
    """A count as prose states it, grouped so the magnitude is readable."""
    return f"{count:,}"


def _size(megabytes: "int | None", scale: str) -> str:
    """A size with its unit, so the fallback reads as a size too.

    ``580 MB`` where the build wrote the tree and ``most of a gigabyte``
    where it did not. The unit is inside the figure rather than in the prose
    around it, because "a few hundred MB" is not a phrase and "a few hundred
    megabytes" is.

    A measured zero renders as ``0 MB``: only a size nobody measured takes the
    phrase.
    """
    return scale if megabytes is None else f"{_grouped(megabytes)} MB"


def _count(block: "dict[str, Any]", key: str) -> "int | None":
    """One count out of a report block, or ``None`` where it has none.

    ``None`` rather than zero, because a build that counted none of something
    and a build that did not count it are different answers: a corpus with no
    unnamed arcs reports ``0`` and a publication that emitted no arc index
    reports nothing at all. Only the second wants a fallback, which is why
    ``0 arcs unnamed`` -- the good outcome -- reaches the page as a number.

    A field that is present and is not a number is absent for this purpose.
    ``report.json`` is an artifact read off disk, and a documentation build
    that raised ``ValueError`` partway through substituting its figures would
    fail over a field it could have ignored.
    """
    if not isinstance(block, dict) or key not in block:
        return None

    found = block[key]

    if isinstance(found, bool) or not isinstance(found, (int, float, str)):
        return None

    try:
        return int(found)

    except (TypeError, ValueError):
        return None


def _pairs(count: "int | None") -> "int | None":
    """Twice a count, for the two data trees that carry a file per module."""
    return None if count is None else count * 2


def _scaled(count: "int | None") -> "int | None":
    """Bytes as megabytes, keeping a missing figure missing."""
    return None if count is None else round(count / 1e6)


def _reported(count: "int | None", committed: int) -> int:
    """*count* where the build reported one, the committed artifact otherwise.

    ``is None`` rather than falsy: a build that indexed no legacy rows, or
    resolved no registrant arcs, reported that -- and answering it with the
    committed file's row count would put a different number on the page than
    the build measured.
    """
    return committed if count is None else count


def _figure(count: "int | None", scale: str) -> str:
    """*count* where the build supplied one, and *scale* where it did not.

    A phrase where the figure is missing, because "the site is 0 pages" is
    false and "the site is thousands of pages" is true of every corpus this
    documentation describes. A supplied zero is a measurement and is rendered
    as ``0``. The published build always has the report, so the published
    sentence always carries the number.
    """
    return scale if count is None else _grouped(count)


def _namespaces(report: dict[str, Any], tier: str) -> "tuple[int, int | None]":
    """Namespaces of one tier, and the modules they supplied between them.

    The module count is ``None`` where the report names no namespace of this
    tier, which is what a report-less checkout looks like. Summing nothing
    gives a real zero, and a page reading "0 standard modules" over a corpus
    that has them is the falsehood :py:func:`_figure` exists to avoid.
    """
    found = [
        x
        for x in report.get("namespaces") or []
        if isinstance(x, dict) and x.get("tier") == tier
    ]

    if not found:
        return 0, None

    counted = [_count(x, "modules") for x in found]

    # A namespace block that does not say how many modules it supplied makes
    # the total unknowable, and summing the rest gives an under-count that
    # reads exactly like a real figure. The phrase is the honest answer.
    if any(x is None for x in counted):
        return len(found), None

    return len(found), sum(x for x in counted if x is not None)


def figures(root: pathlib.Path = ROOT) -> dict[str, str]:
    """Every figure the documentation names, ready to substitute.

    Args:
        root: the repository root.

    Returns:
        Figure name to the text to render, each already grouped. A name is
        always present, so a page naming one cannot fail to build; what
        changes between a checkout with a build and one without is whether
        the value is a number or a phrase.
    """
    report = read_report(root)
    site = report.get("site") or {}
    nodes = report.get("nodes") or {}
    index = report.get("index") or {}
    entity = report.get("entity") or {}
    arcs = report.get("arcs") or {}
    closure = report.get("closure") or {}
    db = report.get("db") or {}

    vendors, vendor_modules = _namespaces(report, "vendor")
    _standard, standard_modules = _namespaces(report, "standard")

    # The source tree answers for the vendor side without a build, and it is
    # the figure a contributor is looking at: how many vendors src/vendor
    # holds is a property of the checkout, not of a compile.
    directories = _vendors(root)
    pen_rows = _count_lines(root / "registries" / "pen-snapshot.csv", header=True)
    data = _data_tree(root)

    return {
        # The corpus itself.
        "modules": _figure(_count(report, "modules"), "thousands of"),
        "standard_modules": _figure(standard_modules, "several hundred"),
        "vendor_modules": _figure(vendor_modules, "thousands of"),
        "vendors": _grouped(directories or vendors),
        "source_files": _grouped(_source_modules(root)),
        # What it defines.
        "nodes": _figure(_count(nodes, "defined"), "hundreds of thousands of"),
        "indexed_oids": _figure(_count(nodes, "distinct"), "tens of thousands of"),
        "index_rows": _figure(
            _reported(_count(index, "legacy"), _count_lines(root / "index-frozen.csv")),
            "tens of thousands of",
        ),
        "frozen_modules": _grouped(_index_modules(root / "index-frozen.csv")),
        # Who registered it.
        # The snapshot is reduced to the arcs this corpus reaches, so its row
        # count is the registrant count for a checkout with no build. The two
        # can differ by the arcs the snapshot predates, which is what the
        # build's `unregistered` names.
        "registrants": _figure(
            _reported(_count(entity, "arcs"), pen_rows), "a few hundred"
        ),
        "pen_rows": _grouped(pen_rows),
        "unregistered": _figure(_count(entity, "unregistered"), "a handful"),
        "arcs": _figure(_count(arcs, "arcs"), "tens of thousands of"),
        "unnamed_arcs": _figure(_count(arcs, "unnamed"), "a handful"),
        # What the site renders.
        "pages": _figure(_count(site, "pages"), "thousands of"),
        "module_pages": _figure(_count(site, "modules"), "thousands of"),
        "site_bytes": _size(_scaled(_count(site, "bytes")), "a few hundred megabytes"),
        # The two data trees, one file per module each, and what they weigh on
        # the object storage they are synced to.
        "data_files": _figure(_pairs(_count(report, "modules")), "thousands of"),
        "data_bytes": _size(
            _megabytes(data / "asn1", data / "json"), "a few hundred megabytes"
        ),
        # The lean tree explicitly: docs/corpora.md cites this against the
        # texts-carrying one, and _data_tree prefers depot-data, whose json/
        # is the tree with the texts in it.
        "json_bytes": _size(
            _megabytes(root / "output" / "github-pages" / "json"),
            "a couple of hundred megabytes",
        ),
        "pages_tree_bytes": _size(
            _megabytes(root / "output" / "github-pages"), "most of a gigabyte"
        ),
        # Corpus health.
        "incomplete_closures": _figure(_count(closure, "incomplete"), "a handful"),
        "unimported": _grouped(_count_lines(root / "unimported-symbols.txt")),
        "db_rows": _figure(_count(db, "node"), "hundreds of thousands of"),
        "pysmi": str(report.get("version") or ""),
    }


#: Numbers the documentation may state outright, because they are not this
#: corpus's to change: a platform's limits, a protocol's, a wire format's.
#: Everything else comma-grouped in a page is a count of something the corpus
#: holds, and belongs in :py:func:`figures` instead.
ALLOWED: "frozenset[str]" = frozenset(
    {
        # Cloudflare's free plan: assets per version, and metered requests to
        # a Worker script per day. docs/deploying.md, docs/corpora.md.
        "20,000",
        "19,000",
        "100,000",
        # An issue body's character limit, which is what makes a MIB too big
        # to paste. docs/contributing-mibs.md.
        "65,536",
        # R2's included writes a month. docs/deploying.md.
        "1,000,000",
    }
)

#: Where the documentation lives, relative to the repository root.
PAGES = "docs"

#: A comma-grouped number. Every count this corpus publishes is in the
#: thousands or above, so this is the shape that goes stale here.
#:
#: It does not see an ungrouped one: "210 modules" passes. pysnmp/pysmi#326
#: widened the sibling check in pysmi to a number followed by a unit, and
#: doing the same here reports nineteen counts across five pages -- the
#: inventory absent-modules.md keeps of its own tables, historical records of
#: what a past release moved, a vendor file's size. Each wants a decision,
#: and several want a figure this module does not compute yet, so widening
#: this is its own change. See pysnmp/mibs#441.
GROUPED = re.compile(r"\b\d{1,3}(?:,\d{3})+\b")


def stated(root: pathlib.Path = ROOT) -> "list[tuple[str, int, str]]":
    """Comma-grouped counts written into the documentation by hand.

    A count typed into a page is wrong at the next contribution and is a diff
    to review on every one after that, which is what :py:func:`figures` exists
    to prevent. This is the check that it stays prevented.

    :py:data:`GROUPED` says which shape is looked for, and what it does not
    catch.

    Fenced code blocks are skipped: a sample of a report or a command's output
    is a transcript, and a transcript states what it stated.

    Args:
        root: the repository root.

    Returns:
        ``(path, line number, the line)`` per finding, in file order.
    """
    found = []

    for page in sorted((root / PAGES).glob("*.md")) + sorted(
        (root / PAGES).glob("*.rst")
    ):
        fenced = False

        with open(page, encoding="utf-8") as fileObj:
            for number, line in enumerate(fileObj, start=1):
                if line.lstrip().startswith("```"):
                    fenced = not fenced
                    continue

                if fenced:
                    continue

                if [x for x in GROUPED.findall(line) if x not in ALLOWED]:
                    found.append((str(page.relative_to(root)), number, line.rstrip()))

    return found


def main(argv: "list[str] | None" = None) -> int:
    """Print the figures, for a person or for a build that wants the JSON."""
    parsed = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parsed.add_argument(
        "--json", action="store_true", help="write the figures as a JSON object"
    )
    parsed.add_argument(
        "--check",
        action="store_true",
        help="fail on a count written into the documentation by hand",
    )
    options = parsed.parse_args(argv)

    if options.check:
        written = stated()

        for path, number, line in written:
            print(f"{path}:{number}: {line.strip()}")

        if written:
            print(
                f"\n{len(written)} line(s) state a count outright. Name a figure "
                f"from {pathlib.Path(__file__).name} instead -- {{{{ modules }}}} in "
                f"Markdown, |modules| in reStructuredText -- so the page is right "
                f"after the next MIB is added. A limit that is not this corpus's "
                f"to change goes on ALLOWED."
            )

        return 1 if written else 0

    found = figures()

    if options.json:
        json.dump(found, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")

        return 0

    if not read_report():
        print(
            f"No build report found. Run `make corpus`, or set {REPORT_ENV}, "
            f"for the figures only a build knows.\n"
        )

    width = max(len(x) for x in found)

    for name in sorted(found):
        print(f"{name:<{width}}  {found[name]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
