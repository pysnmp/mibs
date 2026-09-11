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

    if FAILURES:
        sys.stderr.write(f"\n{len(FAILURES)} check(s) failed:\n")
        for name in FAILURES:
            sys.stderr.write(f"  {name}\n")
        return 1

    sys.stdout.write("\nAll checks passed.\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
