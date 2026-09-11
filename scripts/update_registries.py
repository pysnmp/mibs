#!/usr/bin/env python3
#
# This file is part of pysnmp/mibs.
#
"""Keep the IANA registry snapshots this corpus names its OID arcs from.

The corpus build names arcs from two IANA registries. Both are **committed**
here rather than fetched at build time, because ``pysmi/corpus/driver.py``
opens on the property that a build fetches nothing: *a build with the network
unplugged produces the same corpus as one without*. The Private Enterprise
Numbers registry changes daily. Fetching it at build time would end that
property, and two builds of the same sources would stop agreeing.

===========================  =========================================
file                         what it is
===========================  =========================================
``registries/smi-numbers.xml``  IANA's SMI Numbers registry, whole. It
                                names the ``1.3.6.1`` subtree, which is
                                otherwise named by whichever MIB
                                happened to mention an arc -- in this
                                corpus that gave ``1.3`` and ``1.3.6``
                                to OCCAM-ETHERLIKE-MIB and
                                ``1.3.6.1.6.3`` (``snmpModules``) to
                                RAPID-CITY.
``registries/pen-snapshot.csv`` The Private Enterprise Numbers
                                registry, reduced to the enterprise
                                arcs this corpus actually uses.
===========================  =========================================

Why the PEN snapshot is reduced
-------------------------------

IANA publishes 66,807 registrations in a 5.1 MB file and revises it daily.
Committing all of it would mean a 4 MB CSV and a monthly diff of the whole
registry. The arcs this corpus reaches are 351 of them.

The cost is staleness: a module arriving later under an arc the snapshot
predates has no registrant, and its page renders nameless. That is not silent.
``--validate`` says so offline against the committed index, and the corpus
build says so too -- pysmi reports ``arcs.unregistered-enterprises`` and warns
naming the numbers.

Which arcs those are comes from ``index-frozen.csv``, which is committed, so
the reduction is a pure function of two files in this repository and one
download. A refresh that changes nothing produces no diff.

Usage
-----

.. code-block:: sh

   # Offline. Does the committed snapshot still cover the committed index?
   uv run python scripts/update_registries.py --validate

   # What the monthly sweep runs: re-fetch and report what has moved.
   uv run python scripts/update_registries.py --check

   # Take the new registries.
   uv run python scripts/update_registries.py --update

Exit codes follow ``update_vendor_mibs.py``: ``1`` for a difference somebody
has to look at, ``2`` for an unreachable publisher, because an outage says
nothing about our registries and the exit code should not claim otherwise.
"""

from __future__ import annotations

import csv
import pathlib
import sys
import urllib.error
import urllib.request

from pysmi.registry.pen import ENTERPRISES, load_registry, reduce_registry
from pysmi.registry.smi import parse_smi_numbers

ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRIES = ROOT / "registries"

#: The frozen legacy index: what ``index.csv`` replays, so that consumers
#: keying on it keep the answers they already have. Committed, so the arcs it
#: reaches can be checked offline.
FROZEN = ROOT / "index-frozen.csv"

#: The ranked index a build writes -- the corpus's own live answer for which
#: module owns which OID, and what ``entity.json`` and ``arcs.json`` are built
#: from. Not committed; read when a build is on disk.
RANKED = ROOT / "output" / "index-v2.csv"

#: The enterprise arcs this corpus publishes under, one number per line. The
#: reduction's input, committed so that ``--check`` and ``--update`` are a pure
#: function of files in this repository plus one download.
#:
#: Both indexes, because the two do not agree: the ranked index reaches ten
#: arcs the frozen one does not, and the frozen one replays five the corpus no
#: longer compiles a module for. A reader resolving an OID through either
#: published index should reach a named registrant, so the list is the union.
ARCS = REGISTRIES / "enterprise-arcs.txt"

PEN_URL = "https://www.iana.org/assignments/enterprise-numbers/enterprise-numbers"
PEN_SNAPSHOT = REGISTRIES / "pen-snapshot.csv"

SMI_URL = "https://www.iana.org/assignments/smi-numbers/smi-numbers.xml"
SMI_SNAPSHOT = REGISTRIES / "smi-numbers.xml"

#: Long enough for a 5 MB file from a host that is sometimes slow, short
#: enough that a hung fetch does not hold a scheduled run open all day.
TIMEOUT = 300

EX_OK = 0
EX_DIFFERS = 1
EX_UNREACHABLE = 2

#: The prefix an enterprise arc sits under, with its trailing dot.
_PREFIX = f"{ENTERPRISES}."


class Unreachable(Exception):
    """A registry could not be fetched. Says nothing about our snapshots."""


def arcs_in(path: pathlib.Path) -> set[int]:
    """The enterprise numbers one index file reaches."""
    found: set[int] = set()

    with path.open(newline="", encoding="utf-8") as fileObj:
        for row in csv.reader(fileObj):
            if len(row) < 2 or not row[1].startswith(_PREFIX):
                continue

            number = row[1][len(_PREFIX) :].split(".")[0]

            if number.isdigit():
                found.add(int(number))

    return found


def published_arcs() -> list[int]:
    """The enterprise numbers both published indexes reach, ascending.

    From the build's ranked index where one is on disk, since that is the
    corpus's live answer, unioned with the frozen index the legacy one
    replays. Where there is no build, the committed list stands.
    """
    found = arcs_in(FROZEN)

    if RANKED.exists():
        found |= arcs_in(RANKED)

    elif ARCS.exists():
        found |= read_arcs()

    return sorted(found)


def read_arcs(path: pathlib.Path = ARCS) -> set[int]:
    """The committed arc list."""
    found = set()

    for line in path.read_text(encoding="utf-8").splitlines():
        entry = line.partition("#")[0].strip()

        if entry:
            found.add(int(entry))

    return found


def write_arcs(arcs: list[int]) -> None:
    """Commit the arc list, one number per line under a comment saying what it is."""
    ARCS.write_text(
        "# The enterprise arcs this corpus publishes under, from index-frozen.csv\n"
        "# and the build's index-v2.csv. Input to the PEN snapshot's reduction.\n"
        "# Regenerated by scripts/update_registries.py --update after a build.\n"
        + "".join(f"{x}\n" for x in arcs),
        encoding="utf-8",
    )


def fetch(url: str) -> str:
    """One registry, as its publisher serves it.

    Raises:
        Unreachable: the publisher did not answer.
    """
    request = urllib.request.Request(  # noqa: S310 - https, and not user input
        url, headers={"User-Agent": "pysnmp-mibs"}
    )

    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:  # noqa: S310
            return response.read().decode("utf-8", "replace")

    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise Unreachable(f"{url}: {exc}") from exc


def reduced_pen(published: str, arcs: list[int] | None = None) -> str:
    """What this repository commits, from what IANA publishes."""
    return reduce_registry(
        published, None, sorted(read_arcs()) if arcs is None else arcs
    )


def validate() -> int:
    """Offline: do the committed files still answer for the committed index?

    Cheap enough for every pull request, and it needs no build: the arc list
    and the snapshot are both committed, and so is the index they have to
    cover.
    """
    missing_files = [
        str(x.relative_to(ROOT))
        for x in (PEN_SNAPSHOT, SMI_SNAPSHOT, ARCS)
        if not x.exists()
    ]

    if missing_files:
        for name in missing_files:
            sys.stderr.write(f"{name} is missing\n")

        return EX_DIFFERS

    listed = read_arcs()
    held = set(load_registry(PEN_SNAPSHOT))
    named = parse_smi_numbers(SMI_SNAPSHOT.read_text(encoding="utf-8"))

    print(f"enterprise-arcs.txt: {len(listed)} arcs")
    print(
        f"pen-snapshot.csv: {len(held)} registrants, naming "
        f"{len(listed & held)} of them"
    )
    print(f"smi-numbers.xml: {len(named)} arcs")

    # A gap is not a failure. IANA's registry has holes of its own, and a
    # snapshot that cannot name an arc nobody registered is not stale, it is
    # correct. --check is what notices a registry that has moved.
    unnamed = sorted(listed - held)

    if unnamed:
        print(
            f"{len(unnamed)} arc(s) no registrant names: "
            f"{', '.join(str(x) for x in unnamed[:10])}"
        )

    problems = []

    # An arc the frozen index reaches and the list does not means the list was
    # not regenerated. Only the frozen half is checkable offline; the ranked
    # half needs a build, and the corpus job's own report covers it.
    behind = sorted(arcs_in(FROZEN) - listed)

    if behind:
        problems.append(
            f"{len(behind)} arc(s) in index-frozen.csv are not in "
            f"enterprise-arcs.txt: {', '.join(str(x) for x in behind[:10])}"
        )

    # A registrant for an arc no index reaches is dead weight, and unlike a
    # gap it is entirely ours to fix.
    extra = sorted(held - listed)

    if extra:
        problems.append(
            f"{len(extra)} registrant(s) in the snapshot for arcs no index "
            f"reaches: {', '.join(str(x) for x in extra[:10])}"
        )

    if problems:
        for problem in problems:
            sys.stderr.write(f"{problem}\n")

        sys.stderr.write("Run --update to re-reduce the snapshot.\n")

        return EX_DIFFERS

    return EX_OK


def check() -> int:
    """Re-fetch both registries and report anything that has moved."""
    try:
        published = fetch(PEN_URL)
        smi = fetch(SMI_URL)

    except Unreachable as exc:
        sys.stderr.write(f"{exc}\n")
        return EX_UNREACHABLE

    moved = []

    if reduced_pen(published) != PEN_SNAPSHOT.read_text(encoding="utf-8"):
        moved.append("pen-snapshot.csv")

    if smi != SMI_SNAPSHOT.read_text(encoding="utf-8"):
        moved.append("smi-numbers.xml")

    if not moved:
        print("registries: both snapshots match what IANA publishes")
        return EX_OK

    for name in moved:
        print(f"{name}: IANA has revised this registry")

    print("\nRun --update and review the diff.")

    return EX_DIFFERS


def update() -> int:
    """Take the current registries."""
    try:
        published = fetch(PEN_URL)
        smi = fetch(SMI_URL)

    except Unreachable as exc:
        sys.stderr.write(f"{exc}\n")
        return EX_UNREACHABLE

    REGISTRIES.mkdir(exist_ok=True)

    arcs = published_arcs()
    write_arcs(arcs)

    PEN_SNAPSHOT.write_text(reduced_pen(published, arcs), encoding="utf-8")
    SMI_SNAPSHOT.write_text(smi, encoding="utf-8")

    held = set(load_registry(PEN_SNAPSHOT))

    if not RANKED.exists():
        sys.stderr.write(
            f"note: no build at {RANKED.relative_to(ROOT)}, so the arc list "
            f"stands as committed. Run `make corpus` first to pick up arcs a "
            f"newly added module reaches.\n"
        )

    print(
        f"enterprise-arcs.txt: {len(arcs)} arcs\n"
        f"pen-snapshot.csv: {len(held)} registrants, naming "
        f"{len(held)} of them"
    )
    print(f"smi-numbers.xml: {len(parse_smi_numbers(smi))} arcs")

    return EX_OK


def main(argv: list[str]) -> int:
    modes = {"--validate": validate, "--check": check, "--update": update}

    if len(argv) != 2 or argv[1] not in modes:
        sys.stderr.write(
            f"Usage: {argv[0]} (--validate | --check | --update)\n"
            "  --validate  offline: the committed snapshot against the "
            "committed index\n"
            "  --check     re-fetch both registries and report what moved\n"
            "  --update    take the current registries\n"
        )
        return 64

    return modes[argv[1]]()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
