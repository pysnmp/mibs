#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Tests for the per-module dates the site's second recent list is ordered by.

Run directly; no test framework, and no network:

    uv run python tests/test_module_dates.py

Every date a MIB carries is its publisher's, so "what have we changed lately"
is a question the corpus cannot answer out of its own contents. It is answered
from this repository's history instead, and every way that can go wrong is
quiet -- a wrong date is still a date, and a page of them reads as fact.

So what is pinned here is what the history means:

- the date is the *last* commit to touch a module, not the first
- a module this tree no longer carries is not dated
- this repository's own metadata is not a module
- a module the corpus takes from pysmi is not this repository's to date, even
  where this tree holds a file of the same name
- a truncated history is refused rather than published, because a shallow
  clone dates the few modules it can reach and silently omits the rest

The tests build throwaway repositories with commits at fixed dates, since
asserting against this repository's real history would pin the tests to
whatever was committed last.
"""

from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

import module_dates

FAILURES: list[str] = []


def check(name: str, got: object, want: object) -> None:
    """Record one expectation."""
    if got == want:
        sys.stdout.write(f"  PASS  {name}\n")
    else:
        sys.stdout.write(f"  FAIL  {name}\n        got {got!r}, want {want!r}\n")
        FAILURES.append(name)


def git(root: pathlib.Path, *arguments: str, date: str = "") -> None:
    """One git command in *root*, optionally at a fixed commit date."""
    stamp = f"{date}T12:00:00" if date else ""
    environment = {
        **os.environ,
        "GIT_AUTHOR_NAME": "Test",
        "GIT_AUTHOR_EMAIL": "test@example.com",
        "GIT_COMMITTER_NAME": "Test",
        "GIT_COMMITTER_EMAIL": "test@example.com",
    }

    if stamp:
        environment["GIT_AUTHOR_DATE"] = stamp
        environment["GIT_COMMITTER_DATE"] = stamp

    subprocess.run(
        ("git", *arguments),
        cwd=root,
        env=environment,
        check=True,
        capture_output=True,
    )


def commit(root: pathlib.Path, date: str, **modules: str) -> None:
    """One commit at *date*, writing each named module under ``src/vendor``."""
    where = root / "src" / "vendor" / "acme"
    where.mkdir(parents=True, exist_ok=True)

    for name, body in modules.items():
        (where / name).write_text(body, encoding="utf-8")

    git(root, "add", "-A")
    git(root, "commit", "-m", f"at {date}", date=date)


def repository(scratch: str) -> pathlib.Path:
    """An initialised repository with no commits yet."""
    root = pathlib.Path(scratch)
    git(root, "init", "-q", "-b", "main")

    return root


def test_the_date_is_the_last_commit_to_touch_a_module() -> None:
    """Not the first. "What have we done lately" is about the latest change."""
    sys.stdout.write("\ntest_the_date_is_the_last_commit_to_touch_a_module\n")

    with tempfile.TemporaryDirectory() as scratch:
        root = repository(scratch)
        commit(root, "2020-01-01", **{"OLD-MIB": "first", "KEPT-MIB": "first"})
        commit(root, "2026-09-17", **{"OLD-MIB": "second"})

        found = module_dates.present(root)

        check("the edited module", found.get("OLD-MIB"), "2026-09-17")
        check("the untouched one", found.get("KEPT-MIB"), "2020-01-01")


def test_a_module_the_tree_no_longer_carries_is_not_dated() -> None:
    """The history names every file it ever held. The corpus is what is here
    now, and a date for a module nothing can look up is weight."""
    sys.stdout.write("\ntest_a_module_the_tree_no_longer_carries_is_not_dated\n")

    with tempfile.TemporaryDirectory() as scratch:
        root = repository(scratch)
        commit(root, "2020-01-01", **{"GONE-MIB": "x", "KEPT-MIB": "x"})
        os.remove(root / "src" / "vendor" / "acme" / "GONE-MIB")
        git(root, "add", "-A")
        git(root, "commit", "-m", "drop it", date="2026-09-17")

        found = module_dates.present(root)

        check("the removed module", "GONE-MIB" in found, False)
        check("the kept one", found.get("KEPT-MIB"), "2020-01-01")


def test_this_repositorys_own_metadata_is_not_a_module() -> None:
    """src/vendor/cisco/.mib-sources is a note about where MIBs came from,
    and the layout contract skips it for the same reason."""
    sys.stdout.write("\ntest_this_repositorys_own_metadata_is_not_a_module\n")

    with tempfile.TemporaryDirectory() as scratch:
        root = repository(scratch)
        commit(root, "2026-09-17", **{"REAL-MIB": "x", ".mib-sources": "a note"})

        found = module_dates.present(root)

        check("the module", found.get("REAL-MIB"), "2026-09-17")
        check("the note", ".mib-sources" in found, False)


def test_a_module_is_dated_by_name_and_not_by_path() -> None:
    """The published corpus is flat and named by module, which is what the
    site looks a date up by."""
    sys.stdout.write("\ntest_a_module_is_dated_by_name_and_not_by_path\n")

    with tempfile.TemporaryDirectory() as scratch:
        root = repository(scratch)
        commit(root, "2026-09-17", **{"DEEP-MIB": "x"})

        check("keyed by module", list(module_dates.present(root)), ["DEEP-MIB"])


def test_a_history_with_no_sources_dates_nothing() -> None:
    """Rather than failing. A repository whose src/ is empty has nothing to
    say here, which is different from being unable to say it."""
    sys.stdout.write("\ntest_a_history_with_no_sources_dates_nothing\n")

    with tempfile.TemporaryDirectory() as scratch:
        root = repository(scratch)
        (root / "src").mkdir()
        (root / "README.md").write_text("nothing here", encoding="utf-8")
        git(root, "add", "-A")
        git(root, "commit", "-m", "no MIBs", date="2026-09-17")

        check("no dates", module_dates.present(root), {})


def test_a_full_checkout_is_not_shallow() -> None:
    """The guard that keeps a truncated history from being published as
    though the modules it cannot reach had not been touched."""
    sys.stdout.write("\ntest_a_full_checkout_is_not_shallow\n")

    with tempfile.TemporaryDirectory() as scratch:
        root = repository(scratch)
        commit(root, "2026-09-17", **{"REAL-MIB": "x"})

        check("not shallow", module_dates.shallow(root), False)


def test_every_date_is_one_the_site_can_sort_by() -> None:
    """pysmi refuses anything but YYYY-MM-DD, since the lists sort on these
    and print them verbatim."""
    sys.stdout.write("\ntest_every_date_is_one_the_site_can_sort_by\n")

    with tempfile.TemporaryDirectory() as scratch:
        root = repository(scratch)
        commit(root, "2026-09-17", **{"REAL-MIB": "x"})

        shapes = {
            len(x) == 10 and x[4] == "-" and x[7] == "-"
            for x in module_dates.present(root).values()
        }

        check("all YYYY-MM-DD", shapes, {True})


def test_a_module_the_corpus_takes_from_pysmi_is_not_dated_here() -> None:
    """The site publishes pysmi's copy for those, so a date read off this
    history would be about a file the page does not render.

    Two names collide today. The check is that whatever collides is excluded,
    not that those two are -- the bundle grows.
    """
    sys.stdout.write("\ntest_a_module_the_corpus_takes_from_pysmi_is_not_dated_here\n")

    root = pathlib.Path(__file__).resolve().parent.parent
    bundled = module_dates.standard()

    check("the bundle is readable", bool(bundled), True)

    if module_dates.shallow(root):
        sys.stdout.write("  SKIP  this checkout is shallow\n")

        return

    dated = set(module_dates.present(root))

    check("none of the bundle is dated", sorted(dated & bundled), [])


def test_this_repository_dates_every_module_it_supplies() -> None:
    """Over the real tree, because the contract worth holding is that the
    site does not quietly omit modules: every file the layout contract counts,
    less the ones the corpus takes from pysmi, should come out with a date."""
    sys.stdout.write("\ntest_this_repository_dates_every_module_it_supplies\n")

    root = pathlib.Path(__file__).resolve().parent.parent

    if module_dates.shallow(root):
        sys.stdout.write("  SKIP  this checkout is shallow\n")

        return

    held = {
        x.name
        for x in (root / module_dates.SOURCES).rglob("*")
        if x.is_file() and not x.name.startswith(".")
    }
    found = module_dates.present(root)
    supplied = held - module_dates.standard()

    check("every module dated", sorted(supplied - set(found)), [])
    check("nothing extra", sorted(set(found) - supplied), [])


def test_an_unreadable_bundle_is_fatal() -> None:
    """Rather than a warning and a partial answer.

    Every module the exclusion cannot name is one this would date from a file
    the site does not serve, so a dates file written without it carries the
    specific falsehood the exclusion exists to prevent.
    """
    sys.stdout.write("\ntest_an_unreadable_bundle_is_fatal\n")

    was = module_dates.STANDARD

    try:
        module_dates.STANDARD = "pysmi.mibs.no_such_package"

        try:
            module_dates.standard()
            check("it exits", False, True)

        except SystemExit as exc:
            check("it exits", True, True)
            check("it says why", "cannot be excluded" in str(exc), True)

    finally:
        module_dates.STANDARD = was


def test_the_written_file_is_what_the_build_reads() -> None:
    """The manifest names it, so its shape is a contract with pysmi: an
    object of module name to YYYY-MM-DD."""
    sys.stdout.write("\ntest_the_written_file_is_what_the_build_reads\n")

    with tempfile.TemporaryDirectory() as scratch:
        where = os.path.join(scratch, "dates.json")
        code = module_dates.main(["--output", where, "--allow-shallow"])
        written = json.loads(pathlib.Path(where).read_text(encoding="utf-8"))

        check("it exits clean", code, 0)
        check("an object", isinstance(written, dict), True)
        check(
            "of strings",
            {type(x) for x in written.values()} <= {str},
            True,
        )


def main() -> int:
    """Run every check."""
    test_the_date_is_the_last_commit_to_touch_a_module()
    test_a_module_the_tree_no_longer_carries_is_not_dated()
    test_this_repositorys_own_metadata_is_not_a_module()
    test_a_module_is_dated_by_name_and_not_by_path()
    test_a_history_with_no_sources_dates_nothing()
    test_a_full_checkout_is_not_shallow()
    test_every_date_is_one_the_site_can_sort_by()
    test_a_module_the_corpus_takes_from_pysmi_is_not_dated_here()
    test_an_unreadable_bundle_is_fatal()
    test_this_repository_dates_every_module_it_supplies()
    test_the_written_file_is_what_the_build_reads()

    if FAILURES:
        sys.stderr.write(f"\n{len(FAILURES)} check(s) failed:\n")
        for name in FAILURES:
            sys.stderr.write(f"  {name}\n")
        return 1

    sys.stdout.write("\nAll checks passed.\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
