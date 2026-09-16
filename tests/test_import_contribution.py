#!/usr/bin/env python3
#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Tests for turning a contribution bundle into a pull request.

Run directly; no test framework, and no network:

    uv run python tests/test_import_contribution.py

What this script does is small and what it can get wrong is not. It writes
files into a checkout of this repository and commits them, so the refusals are
as much the subject as the import: a directory that is not a bundle, a
directory that is not this repository, a tree with somebody's unfinished work
in it, and a publisher `mib-sources.json` does not define -- which is what
`scripts/update_vendor_mibs.py --validate` rejects in the CI run of the pull
request this just opened.

The bundle in these tests is written by hand rather than by `mibcontribute`,
because the interface between the two is the files, and a test that produced
them with the tool would not notice the day the tool stopped writing one.
"""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

import import_contribution

FAILURES: list[str] = []

#: A module this distribution does not carry.
NEW = """NEW-MIB DEFINITIONS ::= BEGIN
newMib MODULE-IDENTITY
    LAST-UPDATED "202402010000Z"
    ::= { enterprises 99995 }
END
"""

#: A module it carries an older copy of.
NEWER = """NEWER-MIB DEFINITIONS ::= BEGIN
newerMib MODULE-IDENTITY
    LAST-UPDATED "202106020000Z"
    ::= { enterprises 99999 }
END
"""


def check(name: str, got: object, want: object) -> None:
    """Record one expectation."""
    if got == want:
        sys.stdout.write(f"  PASS  {name}\n")
    else:
        sys.stdout.write(f"  FAIL  {name}\n        got {got!r}, want {want!r}\n")
        FAILURES.append(name)


def check_true(name: str, got: object) -> None:
    """Record one expectation that only has to be true."""
    check(name, bool(got), True)


def bundle(directory: pathlib.Path) -> pathlib.Path:
    """A contribution bundle, in the shape `mibcontribute` writes one."""
    out = directory / "found"
    (out / "mibs").mkdir(parents=True)
    (out / "mibs" / "NEW-MIB").write_text(NEW, encoding="utf-8")
    (out / "mibs" / "NEWER-MIB").write_text(NEWER, encoding="utf-8")
    (out / "findings.json").write_text(
        json.dumps(
            {
                "report": "mib-contribution v1",
                "pysmi": "5.2.0",
                "archive": "contribution.zip",
                "modules": [
                    {
                        "module": "NEW-MIB",
                        "verdict": "not carried",
                        "precedence": "",
                        "offered": {
                            "file": "NEW-MIB",
                            "revision": "202402010000Z",
                            "digest": "sha256:a",
                            "bytes": len(NEW),
                        },
                        "published": None,
                        "inline": True,
                    },
                    {
                        "module": "NEWER-MIB",
                        "verdict": "newer",
                        "precedence": "newest MODULE-IDENTITY revision",
                        "offered": {
                            "file": "NEWER-MIB",
                            "revision": "202106020000Z",
                            "digest": "sha256:b",
                            "bytes": len(NEWER),
                        },
                        "published": {
                            "file": "NEWER-MIB",
                            "revision": "201103040000Z",
                            "digest": "sha256:c",
                            "bytes": 120,
                        },
                        "inline": True,
                    },
                ],
            }
        ),
        encoding="utf-8",
    )

    return out


def checkout(directory: pathlib.Path) -> pathlib.Path:
    """A clone shaped like this repository, with somewhere to push.

    Enough of it for an import to be written into: the two paths the import
    refuses to work without, a commit to branch from, and an origin, because
    --submit pushes before it asks for the pull request.
    """
    origin = directory / "origin.git"
    clone = directory / "clone"
    subprocess.run(["git", "init", "--quiet", "--bare", str(origin)], check=True)
    subprocess.run(
        ["git", "init", "--quiet", "--initial-branch=main", str(clone)], check=True
    )

    for name, value in (("user.email", "t@example.net"), ("user.name", "Test")):
        subprocess.run(["git", "-C", str(clone), "config", name, value], check=True)

    (clone / "src" / "vendor").mkdir(parents=True)
    (clone / "src" / "vendor" / ".keep").write_text("", encoding="utf-8")
    (clone / "mib-sources.json").write_text(
        json.dumps(
            {"modules": {}, "publishers": {"example-mibs": {"name": "Example"}}}
        ),
        encoding="utf-8",
    )
    subprocess.run(["git", "-C", str(clone), "add", "-A"], check=True)
    subprocess.run(
        ["git", "-C", str(clone), "commit", "--quiet", "-m", "initial"], check=True
    )
    subprocess.run(
        ["git", "-C", str(clone), "remote", "add", "origin", str(origin)], check=True
    )

    return clone


def git(clone: pathlib.Path, *arguments: str) -> str:
    """One git command against the test checkout."""
    return subprocess.run(
        ["git", "-C", str(clone), *arguments],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()


def instead_of(name: str, replacement: object) -> object:
    """Put *replacement* in the module under *name*, returning what was there."""
    original = getattr(import_contribution, name)
    setattr(import_contribution, name, replacement)

    return original


def test_the_modules_land_in_a_branch() -> None:
    """The import itself: files written, provenance recorded, one commit."""
    sys.stdout.write("\ntest_the_modules_land_in_a_branch\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        clone = checkout(directory)
        code = import_contribution.main(
            [
                f"--contribution={bundle(directory)}",
                f"--checkout={clone}",
                "--vendor=example",
                "--publisher=example-mibs",
            ]
        )
        committed = git(
            clone, "show", "--name-only", "--format=", "mibs/example-contribution"
        )
        manifest = json.loads(
            git(clone, "show", "mibs/example-contribution:mib-sources.json")
        )

        check("exit", code, 0)
        check(
            "both modules",
            sorted(x for x in committed.splitlines() if x.startswith("src/")),
            ["src/vendor/example/NEW-MIB", "src/vendor/example/NEWER-MIB"],
        )
        check(
            "the bytes are the offered ones",
            git(clone, "show", "mibs/example-contribution:src/vendor/example/NEW-MIB"),
            NEW.strip(),
        )
        check(
            "provenance",
            manifest["modules"]["src/vendor/example/NEWER-MIB"],
            {"publisher": "example-mibs"},
        )
        check(
            "the checkout is back where it started",
            git(clone, "rev-parse", "--abbrev-ref", "HEAD"),
            "main",
        )


def test_the_commit_says_what_decided_it() -> None:
    """A reviewer reading the log should not have to open the scan."""
    sys.stdout.write("\ntest_the_commit_says_what_decided_it\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        clone = checkout(directory)
        import_contribution.main(
            [
                f"--contribution={bundle(directory)}",
                f"--checkout={clone}",
                "--vendor=example",
            ]
        )
        message = git(clone, "log", "-1", "--format=%B", "mibs/example-contribution")

        check(
            "subject",
            message.splitlines()[0],
            "feat(example): add 1 module and refresh 1 more from one collection",
        )
        check_true(
            "names both modules", "NEW-MIB" in message and "NEWER-MIB" in message
        )
        check_true("gives the revisions", "was 2011-03-04" in message)
        check_true("says what read them", "pysmi 5.2.0" in message)
        check_true(
            "no line is too long for a log",
            max(len(x) for x in message.splitlines()) <= 79,
        )


def test_the_subject_says_which_kind() -> None:
    """feat for what the corpus gains, fix for what it replaces."""
    sys.stdout.write("\ntest_the_subject_says_which_kind\n")

    new = {"module": "A-MIB", "verdict": "not carried"}
    better = {"module": "B-MIB", "verdict": "newer"}

    check(
        "one new",
        import_contribution.title_for([new], "example"),
        "feat(example): add A-MIB, which the corpus does not carry",
    )
    check(
        "two new",
        import_contribution.title_for([new, new], "example"),
        "feat(example): add 2 modules the corpus does not carry",
    )
    check(
        "one better",
        import_contribution.title_for([better], "example"),
        "fix(example): refresh B-MIB from a newer publication",
    )
    check(
        "both",
        import_contribution.title_for([new, better], "example"),
        "feat(example): add 1 module and refresh 1 more from one collection",
    )


def test_the_pull_request_carries_the_evidence_and_not_the_mibs() -> None:
    """The ASN.1 is in the diff. The body is what the diff does not say."""
    sys.stdout.write("\ntest_the_pull_request_carries_the_evidence_and_not_the_mibs\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        found = bundle(directory)
        clone = checkout(directory)
        import_contribution.main(
            [
                f"--contribution={found}",
                f"--checkout={clone}",
                "--vendor=example",
                "--issue=42",
            ]
        )
        body = (found / "pull-request.md").read_text(encoding="utf-8")

        check("the table", "| `NEWER-MIB` | 2021-06-02 | 2011-03-04 |" in body, True)
        check("a module not carried", "| not carried |" in body, True)
        check("closes the issue", "Closes #42" in body, True)
        check("no ASN.1", "DEFINITIONS ::= BEGIN" in body, False)


def test_submitting_pushes_and_opens_the_pull_request() -> None:
    """What --submit runs, without running gh."""
    sys.stdout.write("\ntest_submitting_pushes_and_opens_the_pull_request\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        clone = checkout(directory)
        calls: list[list[str]] = []

        def recorder(arguments: list[str]) -> str:
            calls.append(arguments)

            return "https://github.com/pysnmp/mibs/pull/9"

        original = instead_of("run_gh", recorder)

        try:
            code = import_contribution.main(
                [
                    f"--contribution={bundle(directory)}",
                    f"--checkout={clone}",
                    "--vendor=example",
                    "--submit",
                ]
            )
        finally:
            instead_of("run_gh", original)

        check("exit", code, 0)
        check(
            "pushed",
            git(clone, "ls-remote", "--heads", "origin").count(
                "mibs/example-contribution"
            ),
            1,
        )
        check("created the pull request", calls[0][:2], ["pr", "create"])
        check(
            "from the branch it pushed",
            calls[0][calls[0].index("--head") + 1],
            "mibs/example-contribution",
        )


def test_a_directory_that_is_not_a_bundle_is_refused() -> None:
    """The input is two files beside each other, and half of it is not enough."""
    sys.stdout.write("\ntest_a_directory_that_is_not_a_bundle_is_refused\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        empty = ""

        try:
            import_contribution.read_bundle(directory)
        except import_contribution.Refused as exc:
            empty = str(exc)

        check_true("no findings.json", "is not there" in empty)

        found = bundle(directory)
        (found / "mibs" / "NEW-MIB").unlink()
        incomplete = ""

        try:
            import_contribution.read_bundle(found)
        except import_contribution.Refused as exc:
            incomplete = str(exc)

        check_true("a module that is not beside it", "is incomplete" in incomplete)


def test_the_checkout_must_be_this_repository_and_clean() -> None:
    """Two refusals: the wrong directory, and somebody's unfinished work in it."""
    sys.stdout.write("\ntest_the_checkout_must_be_this_repository_and_clean\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        elsewhere = ""

        try:
            import_contribution.require_checkout(directory)
        except import_contribution.Refused as exc:
            elsewhere = str(exc)

        check_true("not a checkout", "is not a checkout" in elsewhere)

        clone = checkout(directory)
        (clone / "mib-sources.json").write_text("{}", encoding="utf-8")
        dirty = ""

        try:
            import_contribution.require_checkout(clone)
        except import_contribution.Refused as exc:
            dirty = str(exc)

        check_true("dirty tree", "uncommitted changes" in dirty)


def test_a_publisher_the_manifest_does_not_define_is_refused() -> None:
    """An entry naming one that does not exist is what --validate rejects."""
    sys.stdout.write("\ntest_a_publisher_the_manifest_does_not_define_is_refused\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        clone = checkout(directory)
        refused = ""

        try:
            import_contribution.record_provenance(
                clone, ["src/vendor/example/NEW-MIB"], "nobody"
            )
        except import_contribution.Refused as exc:
            refused = str(exc)

        check_true("refused", "defines no publisher 'nobody'" in refused)
        check_true("named the ones it has", "example-mibs" in refused)

        written = import_contribution.record_provenance(clone, [], "")

        check("no publisher writes nothing", written, False)


def test_a_module_the_page_excludes_is_refused() -> None:
    """A scan offers what a collection holds, not what this repository wants.

    Pointing mibcontribute at net-snmp's MIB directory offered 24 modules and
    17 of them were on docs/absent-modules.md, each with a decision already
    recorded against it. None of those decisions says "a file under
    src/vendor", so an import that wrote one would be undoing the decision
    silently -- and for the RFC group, filing the module under the vendor that
    happened to ship a copy says something untrue about who publishes it.
    """
    sys.stdout.write("\ntest_a_module_the_page_excludes_is_refused\n")

    page = """# Removed modules

Prose naming `EXTREME-VLAN-MIB`, which this distribution does carry.

## What used to be here

`AGENTX-MIB` was listed until pysmi carried it.

## Deleted here deliberately: 3 modules

| why | modules |
|---|---|
| Obsolete | IANA-CHARSET-MIB, IANA-LANGUAGE-MIB |

`COFFEE-POT-MIB` was withdrawn as well, and is named in prose rather than in
the table because the page names a module either way.

## The count reads declarations, not filenames

`EXTREME-BASE-MIB` declared 34 once.
"""

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        clone = checkout(directory)
        (clone / "docs").mkdir()
        (clone / "docs" / "absent-modules.md").write_text(page, encoding="utf-8")

        excluded = import_contribution.excluded_modules(clone)

        check("reads the deliberate section only", len(excluded), 3)
        check_true("a table row", "IANA-LANGUAGE-MIB" in excluded)
        check_true("and a backticked name", "COFFEE-POT-MIB" in excluded)
        check_true("not the column heading", "modules" not in excluded)
        check_true(
            "not prose about a carried module", "EXTREME-VLAN-MIB" not in excluded
        )
        check_true("nor one the prose says has come back", "AGENTX-MIB" not in excluded)
        check_true(
            "nor one under the closing prose", "EXTREME-BASE-MIB" not in excluded
        )

        refused = ""

        try:
            import_contribution.require_carryable(
                clone, ["NET-SNMP-SYSTEM-MIB", "COFFEE-POT-MIB"]
            )
        except import_contribution.Refused as exc:
            refused = str(exc)

        check_true("refuses the excluded one", "COFFEE-POT-MIB" in refused)
        check_true("naming the section", "Deleted here deliberately" in refused)
        check_true("counts them", "1 of 2 module(s)" in refused)
        check_true(
            "leaves the carryable one out of it", "NET-SNMP-SYSTEM-MIB" not in refused
        )

        import_contribution.require_carryable(clone, ["NET-SNMP-SYSTEM-MIB"])

        check_true("and passes a module it does not name", True)


def test_a_bundle_naming_a_path_is_refused() -> None:
    """findings.json is data, and it names the files this reads and commits."""
    sys.stdout.write("\ntest_a_bundle_naming_a_path_is_refused\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        found = bundle(directory)
        secret = directory / "id_rsa"
        secret.write_text("a private key\n", encoding="utf-8")

        for module in ("../../id_rsa", "../id_rsa", "/etc/passwd", ".."):
            refused = ""

            try:
                import_contribution.bundle_file(found, module)
            except import_contribution.Refused as exc:
                refused = str(exc)

            check_true(f"{module!r} refused", "is not a MIB module name" in refused)

        check(
            "the key was not read",
            import_contribution.MODULE_NAME.match("../../id_rsa"),
            None,
        )


def test_a_symlink_in_a_bundle_is_refused() -> None:
    """A link where the MIB should be is a file from somewhere else."""
    sys.stdout.write("\ntest_a_symlink_in_a_bundle_is_refused\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        found = bundle(directory)
        secret = directory / "secret"
        secret.write_text("not a MIB\n", encoding="utf-8")
        (found / "mibs" / "NEW-MIB").unlink()

        try:
            (found / "mibs" / "NEW-MIB").symlink_to(secret)
        except (OSError, NotImplementedError):
            sys.stdout.write("  SKIP  this platform does not make symlinks\n")
            return

        refused = ""

        try:
            import_contribution.read_bundle(found)
        except import_contribution.Refused as exc:
            refused = str(exc)

        check_true("refused", "is a symbolic link" in refused)


def test_the_bundle_beside_the_checkout_does_not_refuse_the_import() -> None:
    """The documented command writes the bundle where it is about to import from."""
    sys.stdout.write(
        "\ntest_the_bundle_beside_the_checkout_does_not_refuse_the_import\n"
    )

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        clone = checkout(directory)
        found = bundle(directory)
        inside = clone / "found"
        inside.mkdir()
        (inside / "findings.json").write_text(
            (found / "findings.json").read_text(), encoding="utf-8"
        )
        (inside / "mibs").mkdir()

        for module in ("NEW-MIB", "NEWER-MIB"):
            (inside / "mibs" / module).write_text(
                (found / "mibs" / module).read_text(), encoding="utf-8"
            )

        code = import_contribution.main(
            [
                f"--contribution={inside}",
                f"--checkout={clone}",
                "--vendor=example",
            ]
        )

        check("an untracked bundle is not a dirty tree", code, 0)

        (clone / "mib-sources.json").write_text("{}", encoding="utf-8")
        dirty = ""

        try:
            import_contribution.require_checkout(clone)
        except import_contribution.Refused as exc:
            dirty = str(exc)

        check_true("a modified tracked file still is", "uncommitted changes" in dirty)


def test_an_undefined_publisher_leaves_the_checkout_alone() -> None:
    """A refusal after the branch and the writes is a checkout somebody has to clean."""
    sys.stdout.write("\ntest_an_undefined_publisher_leaves_the_checkout_alone\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        clone = checkout(directory)
        code = import_contribution.main(
            [
                f"--contribution={bundle(directory)}",
                f"--checkout={clone}",
                "--vendor=example",
                "--publisher=nobody",
            ]
        )

        check("refused", code, 2)
        check("still on main", git(clone, "rev-parse", "--abbrev-ref", "HEAD"), "main")
        check(
            "no branch was made",
            git(clone, "branch", "--list", "mibs/example-contribution"),
            "",
        )
        check(
            "nothing was written",
            (clone / "src" / "vendor" / "example").exists(),
            False,
        )


def main() -> int:
    """Run every case and report."""
    test_the_modules_land_in_a_branch()
    test_the_commit_says_what_decided_it()
    test_the_subject_says_which_kind()
    test_the_pull_request_carries_the_evidence_and_not_the_mibs()
    test_submitting_pushes_and_opens_the_pull_request()
    test_a_directory_that_is_not_a_bundle_is_refused()
    test_the_checkout_must_be_this_repository_and_clean()
    test_a_publisher_the_manifest_does_not_define_is_refused()
    test_a_module_the_page_excludes_is_refused()
    test_a_bundle_naming_a_path_is_refused()
    test_a_symlink_in_a_bundle_is_refused()
    test_the_bundle_beside_the_checkout_does_not_refuse_the_import()
    test_an_undefined_publisher_leaves_the_checkout_alone()

    if FAILURES:
        sys.stderr.write(f"\n{len(FAILURES)} check(s) failed:\n")
        for name in FAILURES:
            sys.stderr.write(f"  {name}\n")
        return 1

    sys.stdout.write("\nAll checks passed.\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
