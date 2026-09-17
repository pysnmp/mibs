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
    """The build report, or ``{}`` where this checkout has no build.

    Args:
        root: the repository root.

    Returns:
        The report as written, or an empty mapping. A report that will not
        parse counts as no report: the figures then fall back like any other
        build-less checkout, rather than failing a documentation build over a
        truncated artifact.
    """
    named = os.environ.get(REPORT_ENV)
    paths = [pathlib.Path(named)] if named else [root / x for x in REPORTS]

    for path in paths:
        if not path.is_file():
            continue

        try:
            with open(path, encoding="utf-8") as fileObj:
                found = json.load(fileObj)

        except (OSError, ValueError):
            continue

        if isinstance(found, dict):
            return found

    return {}


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
        return sum(1 for x in where.rglob("*") if x.is_file())

    except OSError:
        return 0


def _megabytes(*where: pathlib.Path) -> int:
    """Megabytes of the given directories, or 0 where no build wrote them.

    Measured off the tree rather than taken from the report, which counts
    pages and rows and not the bytes an artifact weighs. A directory the build
    did not write contributes nothing, and nothing at all answers 0, which
    :py:func:`_figure` turns into a phrase.
    """
    total = 0

    for tree in where:
        if not tree.is_dir():
            continue

        total += sum(x.stat().st_size for x in tree.rglob("*") if x.is_file())

    return round(total / 1e6)


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


def _size(megabytes: int, scale: str) -> str:
    """A size with its unit, so the fallback reads as a size too.

    ``580 MB`` where the build wrote the tree and ``most of a gigabyte``
    where it did not. The unit is inside the figure rather than in the prose
    around it, because "a few hundred MB" is not a phrase and "a few hundred
    megabytes" is.
    """
    return f"{_grouped(megabytes)} MB" if megabytes else scale


def _exact(block: "dict[str, Any]", key: str, scale: str) -> str:
    """A figure whose zero is a real answer rather than a missing one.

    ``0 arcs unnamed`` is the good outcome and worth stating, so these cannot
    use :py:func:`_figure` -- it reads any zero as "the build did not say".
    The key being present is what separates the two: a publication that did
    not emit the arc names writes no ``arcs`` block at all.
    """
    if key not in block:
        return scale

    try:
        return _grouped(int(block[key] or 0))

    except (TypeError, ValueError):
        return scale


def _figure(count: int, scale: str) -> str:
    """*count* where the build supplied one, and *scale* where it did not.

    A phrase rather than a zero or a ``?``: a sentence reading "the site is 0
    pages" is false, and one reading "the site is thousands of pages" is true
    of every corpus this documentation describes. The published build always
    has the report, so the published sentence always carries the number.
    """
    return _grouped(count) if count else scale


def _namespaces(report: dict[str, Any], tier: str) -> tuple[int, int]:
    """Namespaces of one tier, and the modules they supplied between them."""
    found = [
        x
        for x in report.get("namespaces") or []
        if isinstance(x, dict) and x.get("tier") == tier
    ]

    return len(found), sum(int(x.get("modules") or 0) for x in found)


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
        "modules": _figure(int(report.get("modules") or 0), "thousands of"),
        "standard_modules": _figure(standard_modules, "several hundred"),
        "vendor_modules": _figure(vendor_modules, "thousands of"),
        "vendors": _grouped(directories or vendors),
        "source_files": _grouped(_source_modules(root)),
        # What it defines.
        "nodes": _figure(int(nodes.get("defined") or 0), "hundreds of thousands of"),
        "indexed_oids": _figure(
            int(nodes.get("distinct") or 0), "tens of thousands of"
        ),
        "index_rows": _figure(
            int(index.get("legacy") or 0) or _count_lines(root / "index-frozen.csv"),
            "tens of thousands of",
        ),
        "frozen_modules": _grouped(_index_modules(root / "index-frozen.csv")),
        # Who registered it.
        # The snapshot is reduced to the arcs this corpus reaches, so its row
        # count is the registrant count for a checkout with no build. The two
        # can differ by the arcs the snapshot predates, which is what the
        # build's `unregistered` names.
        "registrants": _figure(
            int(entity.get("arcs") or 0) or pen_rows, "a few hundred"
        ),
        "pen_rows": _grouped(pen_rows),
        "unregistered": _exact(entity, "unregistered", "a handful"),
        "arcs": _figure(int(arcs.get("arcs") or 0), "tens of thousands of"),
        "unnamed_arcs": _exact(arcs, "unnamed", "a handful"),
        # What the site renders.
        "pages": _figure(int(site.get("pages") or 0), "thousands of"),
        "module_pages": _figure(int(site.get("modules") or 0), "thousands of"),
        "site_bytes": _size(
            round(int(site.get("bytes") or 0) / 1e6), "a few hundred megabytes"
        ),
        # The two data trees, one file per module each, and what they weigh on
        # the object storage they are synced to.
        "data_files": _figure(int(report.get("modules") or 0) * 2, "thousands of"),
        "data_bytes": _size(
            _megabytes(data / "asn1", data / "json"), "a few hundred megabytes"
        ),
        "json_bytes": _size(_megabytes(data / "json"), "a couple of hundred megabytes"),
        "pages_tree_bytes": _size(
            _megabytes(root / "output" / "github-pages"), "most of a gigabyte"
        ),
        # Corpus health.
        "incomplete_closures": _exact(closure, "incomplete", "a handful"),
        "unimported": _grouped(_count_lines(root / "unimported-symbols.txt")),
        "db_rows": _figure(int(db.get("node") or 0), "hundreds of thousands of"),
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


def stated(root: pathlib.Path = ROOT) -> "list[tuple[str, int, str]]":
    """Comma-grouped numbers written into the documentation by hand.

    A count typed into a page is wrong at the next contribution and is a diff
    to review on every one after that, which is what :py:func:`figures` exists
    to prevent. This is the check that it stays prevented.

    Fenced code blocks are skipped: a sample of a report or a command's output
    is a transcript, and a transcript states what it stated.

    Args:
        root: the repository root.

    Returns:
        ``(path, line number, the line)`` per finding, in file order.
    """
    found = []
    grouped = re.compile(r"\b\d{1,3}(?:,\d{3})+\b")

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

                if [x for x in grouped.findall(line) if x not in ALLOWED]:
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
