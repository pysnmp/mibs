#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Tests for the pull request preview scope.

Run directly; no test framework, and no network:

    uv run python tests/test_pr_scope.py

The scope decides what a pull request preview builds, and every way it can be
wrong is quiet. Too narrow and the reviewer is shown a site that does not
contain the module under review. Too wide and a dependency bump builds 5,510
modules onto a preview host. Named the wrong thing and the build is refused
by pysmi for a module nobody asked about.

So what is pinned here is the mapping, in the four shapes a pull request to
this repository actually takes:

- a MIB added or edited under ``src/``
- a repair edited under ``scripts/mib-patches/``, which changes what this
  repository serves for a module without touching the module's own path
- a change to how pages are built and to no MIB at all -- the pysmi bump
- a change to neither, which must preview nothing rather than everything
"""

from __future__ import annotations

import json
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

import pr_scope

FAILURES: list[str] = []

ROOT = pathlib.Path(__file__).resolve().parent.parent


def check(name: str, got: object, want: object) -> None:
    """Record one expectation."""
    if got == want:
        sys.stdout.write(f"  PASS  {name}\n")
    else:
        sys.stdout.write(f"  FAIL  {name}\n        got {got!r}, want {want!r}\n")
        FAILURES.append(name)


def test_a_changed_module_is_previewed() -> None:
    """The ordinary case: a vendor MIB edited in place."""
    sys.stdout.write("\ntest_a_changed_module_is_previewed\n")

    found = pr_scope.scope(["src/vendor/2n/TEL2N-MIB"])

    check("verdict", found["verdict"], "mibs")
    check("modules", found["modules"], ["TEL2N-MIB"])
    check("reason", found["reasons"]["TEL2N-MIB"], ["source"])


def test_the_module_is_what_the_file_declares() -> None:
    """Not what the file is called.

    The corpus is flat and named by module, so this is the name the preview
    has to ask for. A file named for something else is rare and the whole
    reason this reads the text rather than the path.
    """
    sys.stdout.write("\ntest_the_module_is_what_the_file_declares\n")

    with tempfile.TemporaryDirectory() as scratch:
        root = pathlib.Path(scratch)
        (root / "src" / "vendor" / "acme").mkdir(parents=True)
        (root / "src" / "vendor" / "acme" / "WRONGLY-NAMED").write_text(
            "ACME-MIB DEFINITIONS ::= BEGIN\nEND\n"
        )

        original = pr_scope.ROOT
        pr_scope.ROOT = root

        try:
            found = pr_scope.scope(["src/vendor/acme/WRONGLY-NAMED"])

        finally:
            pr_scope.ROOT = original

    check("modules", found["modules"], ["ACME-MIB"])


def test_a_patch_only_change_is_previewed() -> None:
    """A repair is MIB content.

    Editing ``scripts/mib-patches/cisco/CISCO-IPMCAST-MIB.patch`` changes
    what this repository says about that module -- the defect it cites, the
    note under it, the diff on the page -- while touching no path under
    ``src/``. A scope reading only source paths would preview nothing.
    """
    sys.stdout.write("\ntest_a_patch_only_change_is_previewed\n")

    found = pr_scope.scope(["scripts/mib-patches/cisco/CISCO-IPMCAST-MIB.patch"])

    check("verdict", found["verdict"], "mibs")
    check("modules", found["modules"], ["CISCO-IPMCAST-MIB"])
    check("reason", found["reasons"]["CISCO-IPMCAST-MIB"], ["patch"])


def test_a_deleted_patch_still_names_its_module() -> None:
    """Removing a repair changes the module back to the publisher's text.

    That is a change to what the site serves, so it is previewed. The patch
    file is gone, and ``mib-sources.json`` still names the source it applied
    to, which is why the manifest is consulted rather than the path alone.
    """
    sys.stdout.write("\ntest_a_deleted_patch_still_names_its_module\n")

    owners = pr_scope.patch_owners()
    path = "cisco/CISCO-IPMCAST-MIB.patch"

    check("the manifest names the patch", path in owners, True)
    check(
        "it names the source it repairs",
        owners.get(path),
        "src/vendor/cisco/CISCO-IPMCAST-MIB",
    )


def test_one_module_named_twice_is_named_once() -> None:
    """A pull request that edits a MIB and its patch together.

    The usual shape of a repair: ``--adopt`` rewrites the patch so that it
    still reproduces the file. Both paths change, and the preview builds one
    module.
    """
    sys.stdout.write("\ntest_one_module_named_twice_is_named_once\n")

    found = pr_scope.scope(
        [
            "src/vendor/cisco/CISCO-IPMCAST-MIB",
            "scripts/mib-patches/cisco/CISCO-IPMCAST-MIB.patch",
        ]
    )

    check("modules", found["modules"], ["CISCO-IPMCAST-MIB"])
    check(
        "both reasons are kept",
        found["reasons"]["CISCO-IPMCAST-MIB"],
        ["patch", "source"],
    )


def test_a_deleted_module_is_reported_and_not_built() -> None:
    """It is not in the tree, so there is nothing to render.

    Reported rather than dropped: a pull request that removes a module has
    done something worth saying out loud, and asking pysmi to publish a
    module that is gone would fail the build instead.
    """
    sys.stdout.write("\ntest_a_deleted_module_is_reported_and_not_built\n")

    found = pr_scope.scope(["src/vendor/acme/GONE-MIB"])

    check("nothing to build", found["modules"], [])
    check("it is named", found["removed"], ["src/vendor/acme/GONE-MIB"])
    check("verdict", found["verdict"], "none")


def test_a_file_that_is_not_a_mib_is_an_error() -> None:
    """Under ``src/`` and declaring no module.

    Either a MIB too damaged to lex a header out of, or a file that does not
    belong in a source namespace. Both want a person: a preview that quietly
    leaves out the file the pull request is about has answered the wrong
    question.
    """
    sys.stdout.write("\ntest_a_file_that_is_not_a_mib_is_an_error\n")

    with tempfile.TemporaryDirectory() as scratch:
        root = pathlib.Path(scratch)
        (root / "src" / "vendor" / "acme").mkdir(parents=True)
        (root / "src" / "vendor" / "acme" / "NOT-A-MIB").write_text(
            "<html>the vendor's download page</html>\n"
        )

        original = pr_scope.ROOT
        pr_scope.ROOT = root

        try:
            found = pr_scope.scope(["src/vendor/acme/NOT-A-MIB"])

        finally:
            pr_scope.ROOT = original

    check("it is named", found["undeclared"], ["src/vendor/acme/NOT-A-MIB"])
    check("nothing to build", found["modules"], [])


def test_a_toolchain_change_previews_the_canary() -> None:
    """The pysmi bump.

    It touches no MIB and can change every page in the corpus, which is
    exactly the change a reviewer most wants rendered. Previewing nothing
    would be the easy answer and the useless one.
    """
    sys.stdout.write("\ntest_a_toolchain_change_previews_the_canary\n")

    for path in ("uv.lock", "pyproject.toml", "theme/style.css", "corpus.json"):
        found = pr_scope.scope([path])

        check(f"{path}: verdict", found["verdict"], "toolchain")
        check(f"{path}: modules", found["modules"], sorted(pr_scope.CANARY))
        check(f"{path}: flagged as canary", found["canary"], True)


def test_the_canary_modules_are_in_the_corpus() -> None:
    """A canary naming a module this repository does not carry fails every
    toolchain pull request, at the point where the contributor has no idea
    why. Two of the three are files here; IF-MIB comes from the standard
    namespace pysmi bundles, so it is checked against that.
    """
    sys.stdout.write("\ntest_the_canary_modules_are_in_the_corpus\n")

    from pysmi.compiler import bundled_mib_names

    bundled = set(bundled_mib_names("pysmi.mibs.asn1"))

    for module in pr_scope.CANARY:
        here = list((ROOT / "src").rglob(module))
        check(f"{module} is carried", bool(here) or module in bundled, True)


def test_a_mib_change_wins_over_the_canary() -> None:
    """A pull request that bumps pysmi *and* edits a MIB.

    The MIB is what the review is about. Building the canary beside it would
    put three modules nobody touched into the preview.
    """
    sys.stdout.write("\ntest_a_mib_change_wins_over_the_canary\n")

    found = pr_scope.scope(["uv.lock", "src/vendor/2n/TEL2N-MIB"])

    check("verdict", found["verdict"], "mibs")
    check("modules", found["modules"], ["TEL2N-MIB"])


def test_a_change_to_neither_previews_nothing() -> None:
    """A documentation typo, a chart edit, a workflow unrelated to this one.

    Previewing nothing is the right answer and it has to be a *quiet* one:
    the check passes and says why, because a red cross on a docs pull request
    teaches everybody to ignore this check.
    """
    sys.stdout.write("\ntest_a_change_to_neither_previews_nothing\n")

    found = pr_scope.scope(
        ["docs/using.md", "README.md", "charts/mibserver/Chart.yaml"]
    )

    check("verdict", found["verdict"], "none")
    check("modules", found["modules"], [])


def test_the_written_files_are_what_the_build_reads() -> None:
    """``modules.txt`` is passed to ``mibcorpus --publish-only-from``.

    One bare name per line, which is what that flag reads. A file with
    anything else in it is a build that asks for a module by the wrong name.
    """
    sys.stdout.write("\ntest_the_written_files_are_what_the_build_reads\n")

    with tempfile.TemporaryDirectory() as scratch:
        out = pathlib.Path(scratch) / "preview"
        changed = pathlib.Path(scratch) / "changed.txt"
        changed.write_text("src/vendor/2n/TEL2N-MIB\n")

        code = pr_scope.main([f"--changed-from={changed}", f"--out={out}"])

        check("exit code", code, 0)
        check("modules.txt", (out / "modules.txt").read_text(), "TEL2N-MIB\n")
        check(
            "scope.json",
            json.loads((out / "scope.json").read_text())["verdict"],
            "mibs",
        )


def main() -> int:
    """Run every case and report."""
    test_a_changed_module_is_previewed()
    test_the_module_is_what_the_file_declares()
    test_a_patch_only_change_is_previewed()
    test_a_deleted_patch_still_names_its_module()
    test_one_module_named_twice_is_named_once()
    test_a_deleted_module_is_reported_and_not_built()
    test_a_file_that_is_not_a_mib_is_an_error()
    test_a_toolchain_change_previews_the_canary()
    test_the_canary_modules_are_in_the_corpus()
    test_a_mib_change_wins_over_the_canary()
    test_a_change_to_neither_previews_nothing()
    test_the_written_files_are_what_the_build_reads()

    if FAILURES:
        sys.stderr.write(f"\n{len(FAILURES)} check(s) failed:\n")
        for name in FAILURES:
            sys.stderr.write(f"  {name}\n")
        return 1

    sys.stdout.write("\nAll checks passed.\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
