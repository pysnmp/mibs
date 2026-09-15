#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Tests for the note the pull request preview leaves behind.

Run directly; no test framework, and no network:

    uv run python tests/test_pr_report.py

The report is the half of a check people actually read, and the case with
the most to say is the one that had nothing: until pysnmp/mibs#423 a failed
build skipped the report, the comment and the artifact, so a contributor
whose MIB would not compile got a red cross and a run log to go digging in.

What is pinned here is that the failure renders at all, and that it names
the module in its first line -- a reader who stops after one sentence
should already know which file to open.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

import pr_report

FAILURES: list[str] = []

SCOPE = {
    "verdict": "mibs",
    "modules": ["TEL2N-MIB"],
    "reasons": {"TEL2N-MIB": ["source"]},
    "removed": [],
    "undeclared": [],
    "canary": False,
}


def check(name: str, got: object, want: object) -> None:
    """Record one expectation."""
    if got == want:
        sys.stdout.write(f"  PASS  {name}\n")
    else:
        sys.stdout.write(f"  FAIL  {name}\n        got {got!r}, want {want!r}\n")
        FAILURES.append(name)


def test_a_failed_build_names_the_module() -> None:
    """The first line answers the question the red cross raises."""
    sys.stdout.write("\ntest_a_failed_build_names_the_module\n")

    report = {
        "selected": {
            "requested": ["TEL2N-MIB"],
            "published": [],
            "failed": ["TEL2N-MIB"],
        }
    }
    note = pr_report.render(SCOPE, report, pathlib.Path("nowhere"), "", built=False)
    first = [x for x in note.splitlines() if x.strip()][1]

    check("says it failed", "failed" in first, True)
    check("names the module", "TEL2N-MIB" in first, True)
    check("marks it in the table", "**did not compile**" in note, True)
    check("offers no browse link", "Browse the preview" in note, False)


def test_a_failed_build_with_no_report_still_renders() -> None:
    """A build can die before it writes one.

    The scope still knows what was asked for, and saying that is better than
    a traceback where the note should be.
    """
    sys.stdout.write("\ntest_a_failed_build_with_no_report_still_renders\n")

    note = pr_report.render(SCOPE, {}, pathlib.Path("nowhere"), "", built=False)

    check("still renders", note.startswith("### MIB preview"), True)
    check("says it failed", "The preview build failed." in note, True)
    check("still lists what was asked for", "`TEL2N-MIB`" in note, True)
    check("carries the marker", pr_report.MARKER in note, True)


def test_a_successful_build_is_unchanged() -> None:
    """The failure path must not have cost the ordinary one its links."""
    sys.stdout.write("\ntest_a_successful_build_is_unchanged\n")

    report = {
        "selected": {
            "requested": ["TEL2N-MIB"],
            "published": ["TEL2N-MIB"],
            "failed": [],
        }
    }
    note = pr_report.render(SCOPE, report, pathlib.Path("nowhere"), "https://e.invalid")

    check("links the site", "https://e.invalid/browse/" in note, True)
    check("links the module", "https://e.invalid/mib/TEL2N-MIB/" in note, True)
    check("says nothing about failing", "did not compile" in note, False)


def main() -> int:
    """Run every case and report."""
    test_a_failed_build_names_the_module()
    test_a_failed_build_with_no_report_still_renders()
    test_a_successful_build_is_unchanged()

    if FAILURES:
        sys.stderr.write(f"\n{len(FAILURES)} check(s) failed:\n")
        for name in FAILURES:
            sys.stderr.write(f"  {name}\n")
        return 1

    sys.stdout.write("\nAll checks passed.\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
