#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Tests for the MIB provenance tooling.

Run directly; no test framework, and no network:

    uv run python tests/test_mib_sources.py

The cases here are the ones where being subtly wrong would be invisible.
This tooling's whole value is that a maintainer can believe what it says
about where a MIB came from, so the behaviour worth pinning down is not
"does it fetch a file" but the two judgements underneath:

- Attribution has to be per line. A hunk mixing a repair of ours with
  lines the import brought in is the normal shape of these files, and
  crediting the whole hunk to its newest commit hides the inherited part
  -- the one thing --explain exists to be honest about.
- Confirming drift has to compare the publisher's bytes, not just the
  verdict. Two different mangled responses both read as "drift", and
  agreeing on the verdict alone would confirm the very thing looking
  twice is meant to rule out.

Both were wrong once and looked right. That is what earns them a test.
"""

from __future__ import annotations

import pathlib
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

import mib_sources
import update_vendor_mibs

FAILURES: list[str] = []


def check(name: str, got: object, want: object) -> None:
    """Record one expectation."""
    if got == want:
        sys.stdout.write(f"  PASS  {name}\n")
    else:
        sys.stdout.write(f"  FAIL  {name}\n        got {got!r}, want {want!r}\n")
        FAILURES.append(name)


MODULE = b"""ACME-MIB DEFINITIONS ::= BEGIN
IMPORTS
    MODULE-IDENTITY FROM SNMPv2-SMI;

acmeMIB MODULE-IDENTITY
    LAST-UPDATED "202401150000Z"
    ORGANIZATION "Acme"
    CONTACT-INFO "nobody"
    DESCRIPTION  "A module for testing."
    ::= { 1 3 6 1 4 1 99 }

END
"""

BOT_WALL = b"""<!DOCTYPE html>
<html lang="en"><head><title>Just a moment...</title></head>
<body>Checking your browser before accessing this site.</body></html>
"""


def test_module_recognition() -> None:
    """A MIB is recognised; a vendor's bot wall is not mistaken for one."""
    sys.stdout.write("\nrecognising MIB text\n")

    check("names the module", mib_sources.module_names(MODULE), ["ACME-MIB"])
    check("reads its revision", mib_sources.revision_of(MODULE), "2024-01-15")
    check("finds no module in an HTML page", mib_sources.module_names(BOT_WALL), [])

    try:
        mib_sources.require_module(BOT_WALL, "ACME-MIB")
        check("rejects an HTML page", "accepted", "NotAModule")
    except mib_sources.NotAModule:
        check("rejects an HTML page", "NotAModule", "NotAModule")

    # A publisher reissuing a module under a new name at the old path is
    # not a fetch we may believe: adopting it would replace a module that
    # every importer still asks for by its old name.
    try:
        mib_sources.require_module(MODULE, "ACME-RENAMED-MIB")
        check("rejects a renamed module", "accepted", "NotAModule")
    except mib_sources.NotAModule:
        check("rejects a renamed module", "NotAModule", "NotAModule")

    # A publisher who starts serving the module inside a bundle is the
    # same kind of layout move, and what a sweep fetches it writes into
    # src/, where a file holds one module and is named for it. Refusing
    # here is what keeps a bundle from being committed and then failing
    # tests/source-layout-contract.py after the fact.
    combined = MODULE + MODULE.replace(b"ACME-MIB", b"ACME-SECOND-MIB")
    check(
        "reads both names",
        mib_sources.module_names(combined),
        ["ACME-MIB", "ACME-SECOND-MIB"],
    )

    try:
        mib_sources.require_module(combined, "ACME-MIB")
        check("rejects a module served inside a bundle", "accepted", "NotAModule")
    except mib_sources.NotAModule as refusal:
        check("rejects a module served inside a bundle", "NotAModule", "NotAModule")
        check(
            "says what it served",
            "declaring 2 modules" in str(refusal),
            True,
        )


def test_patch_round_trip() -> None:
    """A generated patch reproduces our text, and a moved one refuses."""
    sys.stdout.write("\npatching\n")

    ours = MODULE.replace(b"MODULE-IDENTITY FROM", b"MODULE-IDENTITY, Unsigned32 FROM")
    patch = mib_sources.make_patch(MODULE, ours, "ACME-MIB")

    check("round-trips exactly", mib_sources.apply_patch(MODULE, patch, "t"), ours)

    # The strictness is the point: a patch that no longer matches means
    # the publisher revised the text under it, which is the thing the
    # monthly sweep exists to notice rather than fuzz past.
    moved = MODULE.replace(b"IMPORTS", b"-- a new comment\nIMPORTS")
    try:
        mib_sources.apply_patch(moved, patch, "t")
        check("refuses when context moved", "applied", "ValueError")
    except ValueError:
        check("refuses when context moved", "ValueError", "ValueError")


def test_patch_header_is_not_applied() -> None:
    """A patch's reason sits above its diff and changes no MIB text.

    pysnmp/mibs#408: every patch now opens with the defect it repairs, and
    the applier has to read past that rather than take the first character
    of "Defect:" for a diff mark.
    """
    sys.stdout.write("\npatch headers\n")

    ours = MODULE.replace(b"MODULE-IDENTITY FROM", b"MODULE-IDENTITY, Unsigned32 FROM")
    diff = mib_sources.make_patch(MODULE, ours, "ACME-MIB")
    header = (
        "Defect: SMI-MISSING-IMPORT "
        "https://pysnmp.github.io/pysmi/stable/mib-defects.html"
        "#smi-missing-import\n\nThe module uses Unsigned32 without importing it.\n\n"
    )

    check(
        "a headed patch applies",
        mib_sources.apply_patch(MODULE, header + diff, "t"),
        ours,
    )
    check(
        "the header changes nothing",
        mib_sources.apply_patch(MODULE, header + diff, "t"),
        mib_sources.apply_patch(MODULE, diff, "t"),
    )


def test_shipped_patches_carry_a_reason() -> None:
    """Every patch in the tree names the defect it repairs and still applies.

    The reason is what decides whether a patch should still exist once a
    publisher moves under it, so a patch without one is a diff and a blank.
    """
    sys.stdout.write("\nshipped patches\n")

    from pysmi.patches import split_patch

    found = sorted(mib_sources.PATCHES.rglob("*.patch"))
    check("there are patches to check", bool(found), True)

    for path in found:
        header, diff = split_patch(path.read_text())
        name = path.stem

        check(f"{name} names a defect", bool(header.defects), True)
        check(f"{name} links it", all(x.url for x in header.defects), True)
        check(f"{name} says more than the identifier", bool(header.body), True)
        check(f"{name} still has a diff", diff.startswith("--- "), True)


def test_deletion_only_attribution() -> None:
    """Removing publisher text leaves nothing for git to attribute."""
    sys.stdout.write("\nchanged ranges\n")

    ranges, deletions = mib_sources.changed_ranges(
        b"line1\nline2\nline3\n", b"line1\nline3\n"
    )

    # Not a detail: adopt() branches on this to decide what it may claim
    # about provenance, and saying "inherited" here would assert
    # something nothing established.
    check("no lines of ours to blame", ranges, [])
    check("counts the deletion", deletions, 1)


def test_attribution_is_per_line() -> None:
    """A hunk spanning an import and a repair reports both, not one."""
    sys.stdout.write("\nattribution\n")

    work = pathlib.Path(tempfile.mkdtemp())

    def git(*args: str) -> None:
        subprocess.run(("git", *args), cwd=work, check=True, capture_output=True)

    git("init", "-q", ".")
    git("config", "user.email", "test@example.invalid")
    git("config", "user.name", "test")

    mib = work / "src" / "vendor" / "acme" / "ACME-MIB"
    mib.parent.mkdir(parents=True)

    mib.write_text("inherited-line\nline2\nline3\n")
    git("add", "-A")
    git("commit", "-qm", "import mibs")

    mib.write_text("inherited-line\nline2\nrepaired-line\n")
    git("add", "-A")
    git("commit", "-qm", "fix: repair line 3")

    root = mib_sources.ROOT
    try:
        mib_sources.ROOT = work
        subjects, inherited = mib_sources.attribute(
            "src/vendor/acme/ACME-MIB", [(1, 3)]
        )
    finally:
        mib_sources.ROOT = root

    # Asking who last touched the *range* answers for line 3 alone and
    # reports the hunk as entirely ours, dropping lines 1-2 on the floor.
    check(
        "credits the repair",
        [s.split(" ", 1)[1] for s in subjects],
        ["fix: repair line 3"],
    )
    check("still reports the inherited lines", inherited, True)


def test_drift_is_confirmed_on_the_bytes() -> None:
    """Two looks must agree about the text, not merely about the verdict."""
    sys.stdout.write("\nconfirming drift\n")

    ours = MODULE
    published = MODULE  # what a healthy publisher serves

    # Two *different* mangled responses. Each differs from our copy, so
    # each reads as "drift" on its own -- the case that slips through if
    # only the verdict is compared.
    mangled_a = MODULE.replace(b"IMPORTS", b"IMPORTS ")
    mangled_b = MODULE.replace(b"IMPORTS", b"IMPORTS\t")

    root = update_vendor_mibs.ROOT
    pause = update_vendor_mibs.CONFIRM_PAUSE
    fetch = update_vendor_mibs.fetch
    work = pathlib.Path(tempfile.mkdtemp())
    (work / "src").mkdir()
    (work / "src" / "ACME-MIB").write_bytes(ours)

    def run(responses: list[bytes]) -> str:
        served = list(responses)

        def fake(path: str, entry: dict, publisher: dict) -> bytes:
            return served.pop(0) if served else responses[-1]

        update_vendor_mibs.fetch = fake
        found = update_vendor_mibs.confirmed(
            "src/ACME-MIB", {"publisher": "p"}, {"kind": "file", "url": "x"}
        )

        return found.kind if found else "clean"

    try:
        update_vendor_mibs.ROOT = work
        update_vendor_mibs.CONFIRM_PAUSE = 0

        check("a stable match is clean", run([published, published]), "clean")
        check("one bad response is unstable", run([mangled_a, published]), "unstable")
        check(
            "two different bad ones are unstable",
            run([mangled_a, mangled_b]),
            "unstable",
        )
        check("a stable difference is drift", run([mangled_a, mangled_a]), "drift")
    finally:
        update_vendor_mibs.ROOT = root
        update_vendor_mibs.CONFIRM_PAUSE = pause
        update_vendor_mibs.fetch = fetch


def test_archive_failure_is_settled_once() -> None:
    """Modules racing for one unreachable archive ask the publisher once.

    Deliberately concurrent. A sweep reaches this from several workers at
    the same instant, which is the only situation the locking exists for
    -- calling one after another would pass just as happily against an
    implementation that lets every caller start its own download.

    So all three arrive together on a barrier, and the refusing download
    dawdles long enough that the two that lose the race are genuinely
    waiting on the first rather than finding a result already there.
    """
    sys.stdout.write("\narchive fetching\n")

    attempts = {"count": 0}
    counted = threading.Lock()
    arrive = threading.Barrier(3)

    download = mib_sources.download
    archives = dict(mib_sources._archives)
    locks = dict(mib_sources._archive_locks)

    def refusing(url: str) -> bytes:
        with counted:
            attempts["count"] += 1
        time.sleep(0.2)  # hold the others on the lock
        raise mib_sources.Unreachable(f"{url}: refused")

    def caller(module: str) -> BaseException | None:
        arrive.wait(timeout=10)
        try:
            mib_sources.fetch(
                f"src/vendor/acme/{module}",
                {},
                {
                    "kind": "archive",
                    "url": "https://example.invalid/mibs.zip",
                    "member": "{module}.txt",
                },
            )
        except mib_sources.Unreachable as exc:
            return exc

        return None

    try:
        mib_sources._archives.clear()
        mib_sources._archive_locks.clear()
        mib_sources.download = refusing

        with ThreadPoolExecutor(max_workers=3) as pool:
            caught = list(pool.map(caller, ("ONE-MIB", "TWO-MIB", "THREE-MIB")))

        check("every module is told", [e is not None for e in caught], [True] * 3)
        check("the publisher is asked once", attempts["count"], 1)

        # Each waiter gets its own exception. Re-raising one shared
        # instance across threads piles their tracebacks into each other.
        check("each caller gets its own", len({id(e) for e in caught}), 3)
    finally:
        mib_sources.download = download
        mib_sources._archives.clear()
        mib_sources._archives.update(archives)
        mib_sources._archive_locks.clear()
        mib_sources._archive_locks.update(locks)


def test_a_revision_is_compared_with_its_century() -> None:
    """A module revised in both stamp formats reports the newer revision.

    SMIv1 writes YYMMDDHHMMZ and SMIv2 writes YYYYMMDDHHMMZ, and a module
    revised across the change carries both. Compared as written, the
    two-digit form wins on its first character, so the newest revision of a
    module last touched in the nineties and again this century read as the
    nineties one. That is the date a maintainer is shown when deciding
    whether our copy has fallen behind: net-snmp's UCD-SNMP-MIB and ours
    both reported 1999-12-09 while they were four years apart.

    The century is whichever one puts the date in the past. A revision cannot
    have been made in the future, and SMI is younger than any MIB it could
    date, so there is no pivot year here to fall out of date.
    """
    sys.stdout.write("\nrevision stamps\n")

    mixed = MODULE.replace(
        b'LAST-UPDATED "202401150000Z"',
        b'LAST-UPDATED "202008210000Z"\n    REVISION     "9912090000Z"',
    )

    check("takes the later of the two", mib_sources.revision_of(mixed), "2020-08-21")
    check(
        "reads a two-digit year alone",
        mib_sources.revision_of(MODULE.replace(b'"202401150000Z"', b'"9912090000Z"')),
        "1999-12-09",
    )
    check(
        "and a sixties one as the century that is in the past",
        mib_sources.revision_of(MODULE.replace(b'"202401150000Z"', b'"6501020000Z"')),
        "1965-01-02",
    )
    check(
        "a year not yet reached is the one before it",
        mib_sources.revision_of(MODULE.replace(b'"202401150000Z"', b'"0501020000Z"')),
        "2005-01-02",
    )


def test_a_bundle_folds_into_a_recorded_divergence() -> None:
    """A publisher serving the module in a bundle is refused, and reported once.

    Both halves matter and they pull opposite ways. The refusal is what
    keeps an unattended --update from writing a file that declares several
    modules into src/. Reporting it as a failure every month, for a module
    a maintainer has already looked at and recorded, is what trains
    everybody to ignore the run.
    """
    sys.stdout.write("\nserving a module inside a bundle\n")

    refusal = mib_sources.Bundled("served A-MIB 3 times over in one file")
    check("is refused as a fetch", isinstance(refusal, mib_sources.NotAModule), True)

    def refuse(path, entry, publisher):
        raise refusal

    fetched = update_vendor_mibs.fetch
    update_vendor_mibs.fetch = refuse

    try:
        recorded = update_vendor_mibs.inspect(
            "src/vendor/cisco/CISCO-ATM-CELL-LAYER-CAPABILITY",
            {
                "publisher": "p",
                "divergence": {"note": "reviewed", "recorded": "2026-09-07"},
            },
            {"kind": "file", "url": "https://example.invalid/{module}"},
        )
        fresh = update_vendor_mibs.inspect(
            "src/vendor/cisco/CISCO-ATM-CELL-LAYER-CAPABILITY",
            {"publisher": "p"},
            {"kind": "file", "url": "https://example.invalid/{module}"},
        )
    finally:
        update_vendor_mibs.fetch = fetched

    check(
        "a recorded divergence absorbs it",
        recorded and recorded.kind,
        "known-divergence",
    )
    check(
        "and keeps the reason",
        bool(recorded and "3 times over" in recorded.detail),
        True,
    )
    check("an unrecorded one fails the run", fresh and fresh.kind, "not-a-module")


def main() -> int:
    """Run every case and report."""
    test_module_recognition()
    test_patch_round_trip()
    test_patch_header_is_not_applied()
    test_shipped_patches_carry_a_reason()
    test_deletion_only_attribution()
    test_attribution_is_per_line()
    test_drift_is_confirmed_on_the_bytes()
    test_archive_failure_is_settled_once()
    test_a_revision_is_compared_with_its_century()
    test_a_bundle_folds_into_a_recorded_divergence()

    if FAILURES:
        sys.stderr.write(f"\n{len(FAILURES)} check(s) failed:\n")
        for name in FAILURES:
            sys.stderr.write(f"  {name}\n")
        return 1

    sys.stdout.write("\nAll checks passed.\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
