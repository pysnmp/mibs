#!/usr/bin/env python3
#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Tests for the shadowing reporter.

Run directly; no test framework, and no network:

    uv run python tests/test_contribute_mibs.py

The reporter turns a build's own record of a resolution into a public issue
carrying MIB text, and the ways it can be wrong divide in two.

It can report the wrong thing. A module the published copy won is not a
finding; a module two namespaces hold at the same revision is not a finding
either, because two copies of one name are as often two different modules as
two revisions of one. Both look like findings in a report's ``shadowed`` map,
which records every pair whatever decided it.

It can say too much. The paths in a report are the build host's own, an issue
body is public, and a MIB set is larger than an issue body holds. So what is
pinned here is that no absolute path reaches a rendered issue, that a body
stays inside GitHub's limit with the modules it could not fit named instead,
and that nothing is submitted without the flag that says it may be.

The fixtures are written as ``mibcorpus`` writes them, down to the ``file://``
URLs its file reader records, because that spelling is what the mapping from a
path back to a namespace has to survive.
"""

from __future__ import annotations

import io
import json
import pathlib
import subprocess
import sys
import tempfile
import zipfile
from contextlib import redirect_stdout

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))

import contribute_mibs

FAILURES: list[str] = []

#: A module whose local copy is eight years ahead of the published one.
NEWER = """NEWER-MIB DEFINITIONS ::= BEGIN
-- LAST-UPDATED is what the precedence rule reads.
newerMib MODULE-IDENTITY
    LAST-UPDATED "202106020000Z"
    ::= { enterprises 99999 }
END
"""

#: The same module as this distribution publishes it.
OLDER = """NEWER-MIB DEFINITIONS ::= BEGIN
newerMib MODULE-IDENTITY
    LAST-UPDATED "201103040000Z"
    ::= { enterprises 99999 }
END
"""

#: A module no namespace but the offered one holds. The larger half of what a
#: scanned collection has to offer, and the half ``shadowed`` cannot report.
NOT_CARRIED_MIB = """NEW-MIB DEFINITIONS ::= BEGIN
newMib MODULE-IDENTITY
    LAST-UPDATED "202402010000Z"
    ::= { enterprises 99995 }
END
"""

#: Two copies of one name at one revision, differing in text. Not a finding
#: unless asked for: this is what a vendor reusing a module name looks like.
TIED = """TIED-MIB DEFINITIONS ::= BEGIN
tiedMib MODULE-IDENTITY
    LAST-UPDATED "201501010000Z"
    ::= { enterprises 99997 }
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


def fixture(
    directory: pathlib.Path,
    *,
    tied: bool = False,
    published_wins: bool = False,
    new: bool = False,
    big: int = 0,
) -> dict:
    """A corpus root, a local root and the report a build over both would write.

    Keyword Args:
        tied: also hold ``TIED-MIB`` in both roots, local copy used.
        published_wins: also hold ``OURS-MIB`` in both, published copy used.
        new: also hold ``NEW-MIB``, which only the offered set has.
        big: pad the local ``NEWER-MIB`` to this many bytes, for the cases
            about an issue body's size limit.
    """
    corpus = directory / "corpus"
    local = directory / "mine"
    corpus.mkdir()
    local.mkdir()

    padding = f"-- {'x' * big}\n" if big else ""
    (local / "NEWER-MIB").write_text(padding + NEWER, encoding="utf-8")
    (corpus / "NEWER-MIB").write_text(OLDER, encoding="utf-8")

    shadowed = {
        "NEWER-MIB": {
            "used": (local / "NEWER-MIB").as_uri(),
            "shadowed": [(corpus / "NEWER-MIB").as_uri()],
            "precedence": "newest MODULE-IDENTITY revision",
        }
    }

    if tied:
        (local / "TIED-MIB").write_text(TIED, encoding="utf-8")
        (corpus / "TIED-MIB").write_text(TIED.replace("99997", "99996"), "utf-8")
        shadowed["TIED-MIB"] = {
            "used": (local / "TIED-MIB").as_uri(),
            "shadowed": [(corpus / "TIED-MIB").as_uri()],
            "precedence": "source order; equal MODULE-IDENTITY revisions",
        }

    if published_wins:
        (local / "OURS-MIB").write_text(OLDER.replace("NEWER", "OURS"), "utf-8")
        (corpus / "OURS-MIB").write_text(NEWER.replace("NEWER", "OURS"), "utf-8")
        shadowed["OURS-MIB"] = {
            "used": (corpus / "OURS-MIB").as_uri(),
            "shadowed": [(local / "OURS-MIB").as_uri()],
            "precedence": "newest MODULE-IDENTITY revision",
        }

    if new:
        (local / "NEW-MIB").write_text(NOT_CARRIED_MIB, encoding="utf-8")

    # What the staging pass records: where every published module came from.
    # A module the corpus copy won is attributed to the corpus, which is what
    # keeps it out of the offer.
    provenance = {
        x.name: {"namespace": "local", "file": x.name, "digest": ""}
        for x in sorted(local.iterdir())
    }

    if published_wins:
        provenance["OURS-MIB"] = {
            "namespace": "corpus",
            "file": "OURS-MIB",
            "digest": "",
        }

    return {
        "version": "5.1.0",
        "namespaces": [
            {
                "name": "base",
                "tier": "standard",
                "source": "package:pysmi.mibs.asn1",
                "modules": 210,
                "publish": False,
            },
            {
                "name": "corpus",
                "tier": "vendor",
                "source": str(corpus),
                "modules": 1,
                "publish": False,
            },
            {
                "name": "local",
                "tier": "vendor",
                "source": str(local),
                "modules": 1,
                "publish": True,
            },
        ],
        "shadowed": shadowed,
        "provenance": provenance,
    }


def write_report(directory: pathlib.Path, report: dict) -> pathlib.Path:
    """The report on disk, where the command line expects one."""
    path = directory / "report.json"
    path.write_text(json.dumps(report), encoding="utf-8")

    return path


def run(arguments: list[str]) -> tuple[int, str]:
    """One command line, with its exit code and what it printed."""
    printed = io.StringIO()

    with redirect_stdout(printed):
        code = contribute_mibs.main(arguments)

    return code, printed.getvalue()


def test_a_newer_local_copy_is_reported() -> None:
    """The finding the whole tool exists for."""
    sys.stdout.write("\ntest_a_newer_local_copy_is_reported\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        found = contribute_mibs.collect(fixture(directory), ("local",))

        one = found[0]
        # An empty Copy where there is none, so that a finding carrying no
        # published copy fails these checks rather than raising through them.
        published = one.published or contribute_mibs.Copy("", "", "", "", 0)

        check("one finding", [x.module for x in found], ["NEWER-MIB"])
        check("verdict", one.verdict, "newer")
        check("local revision", one.local.revision, "202106020000Z")
        check("published revision", published.revision, "201103040000Z")
        check("local namespace", one.local.namespace, "local")
        check("published namespace", published.namespace, "corpus")
        check_true("digest read", one.local.digest.startswith("sha256:"))


def test_a_module_the_published_copy_won_is_not_a_finding() -> None:
    """Shadowing is recorded in both directions; only one of them is a report."""
    sys.stdout.write("\ntest_a_module_the_published_copy_won_is_not_a_finding\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        report = fixture(directory, published_wins=True)
        found = contribute_mibs.collect(report, ("local",))

        check("OURS-MIB left out", [x.module for x in found], ["NEWER-MIB"])


def test_a_tie_is_reported_only_when_asked_for() -> None:
    """A copy that won on source order is not evidence of a better copy."""
    sys.stdout.write("\ntest_a_tie_is_reported_only_when_asked_for\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        report = fixture(directory, tied=True)

        check(
            "default",
            [x.module for x in contribute_mibs.collect(report, ("local",))],
            ["NEWER-MIB"],
        )

        asked = contribute_mibs.collect(report, ("local",), include_differing=True)

        check(
            "--include-differing", [x.module for x in asked], ["NEWER-MIB", "TIED-MIB"]
        )
        check(
            "verdict",
            [x.verdict for x in asked if x.module == "TIED-MIB"],
            ["same revision, different text"],
        )


def test_a_namespace_that_is_not_in_the_report_is_an_error() -> None:
    """Naming the wrong namespace reports nothing, which must not read as nothing to report."""
    sys.stdout.write("\ntest_a_namespace_that_is_not_in_the_report_is_an_error\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        report = fixture(directory)
        refused = ""

        try:
            contribute_mibs.collect(report, ("mine",))
        except contribute_mibs.Refused as exc:
            refused = str(exc)

        check_true("refused", "no namespace named mine" in refused)
        check_true("names the ones it has", "corpus, local" in refused)


def test_the_issue_carries_no_path_from_this_machine() -> None:
    """A build's paths name the build host. An issue is public."""
    sys.stdout.write("\ntest_the_issue_carries_no_path_from_this_machine\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        found = contribute_mibs.collect(fixture(directory), ("local",))
        body = contribute_mibs.compose(found, "5.1.0", "contribution.zip")

        check("no absolute path", str(directory) in body, False)
        check("no file URL", "file://" in body, False)
        check("names the file", "`NEWER-MIB`" in body, True)
        check("carries the marker", contribute_mibs.MARKER in body, True)


def test_a_module_too_long_to_inline_is_named_instead() -> None:
    """An issue body holds 65,536 characters and a MIB set can hold more."""
    sys.stdout.write("\ntest_a_module_too_long_to_inline_is_named_instead\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        report = fixture(directory, big=contribute_mibs.BODY_LIMIT + 1000)
        found = contribute_mibs.collect(report, ("local",))
        body = contribute_mibs.compose(found, "5.1.0", "contribution.zip")

        check_true("inside the limit", len(body) <= contribute_mibs.BODY_LIMIT)
        check("text left out", "DEFINITIONS ::= BEGIN" in body, False)
        check("named instead", "too long" in body, True)
        check(
            "and said so in the data",
            json.loads(body.split("```json\n")[1].split("\n```")[0])["modules"][0][
                "inline"
            ],
            False,
        )


def test_the_bundle_holds_the_mib_and_the_data() -> None:
    """What a reporter drags into the issue, and what an agent reads back."""
    sys.stdout.write("\ntest_the_bundle_holds_the_mib_and_the_data\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        path = write_report(directory, fixture(directory))
        out = directory / "shadowing"
        code, printed = run([f"--report={path}", f"--out={out}"])

        check("exit", code, 0)
        check("issue written", (out / "issue.md").is_file(), True)
        check("MIB written", (out / "mibs" / "NEWER-MIB").is_file(), True)
        check_true(
            "MIB is the local copy", NEWER in (out / "mibs" / "NEWER-MIB").read_text()
        )

        with zipfile.ZipFile(out / "contribution.zip") as bundle:
            check("archive", bundle.namelist(), ["NEWER-MIB"])

        data = json.loads((out / "findings.json").read_text(encoding="utf-8"))

        check("data names the module", data["modules"][0]["module"], "NEWER-MIB")
        check("data carries the verdict", data["modules"][0]["verdict"], "newer")
        check("nothing was submitted", "github.com" in printed, False)


def test_submitting_takes_a_second_flag() -> None:
    """--submit publishes MIB text. Reading it first is the point of --yes."""
    sys.stdout.write("\ntest_submitting_takes_a_second_flag\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        path = write_report(directory, fixture(directory))
        out = directory / "shadowing"
        code, printed = run([f"--report={path}", f"--out={out}", "--submit=url"])

        check("refused", code, 2)
        check("no URL printed", "issues/new" in printed, False)
        check("wrote the files anyway", (out / "issue.md").is_file(), True)


def test_the_url_carries_the_report() -> None:
    """The path for a reporter who will not hand a token to a script."""
    sys.stdout.write("\ntest_the_url_carries_the_report\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        path = write_report(directory, fixture(directory))
        out = directory / "shadowing"
        code, printed = run(
            [f"--report={path}", f"--out={out}", "--submit=url", "--yes"]
        )
        url = printed.strip().splitlines()[-1]

        check("exit", code, 0)
        check_true(
            "the repository",
            url.startswith("https://github.com/pysnmp/mibs/issues/new?"),
        )
        check_true("the title", "NEWER-MIB" in url)
        check_true("the body", "mib-contribution" in url)
        check_true(
            "nothing longer than a browser takes",
            len(url) <= contribute_mibs.URL_LIMIT,
        )


def test_a_report_too_long_for_a_url_is_left_in_a_file() -> None:
    """A URL GitHub refuses loses the whole report, so an over-long one is not built."""
    sys.stdout.write("\ntest_a_report_too_long_for_a_url_is_left_in_a_file\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        report = fixture(directory, big=contribute_mibs.URL_LIMIT)
        path = write_report(directory, report)
        out = directory / "shadowing"
        code, printed = run(
            [f"--report={path}", f"--out={out}", "--submit=url", "--yes"]
        )
        url = printed.strip().splitlines()[-1]

        check("exit", code, 0)
        check_true("says where the body is", "issue.md" in printed)
        check_true("the URL is the short one", len(url) <= contribute_mibs.URL_LIMIT)
        check_true("and still carries the marker", "mib-contribution" in url)


def test_one_issue_per_module_when_asked() -> None:
    """One module per issue is one module per pull request, and one per agent."""
    sys.stdout.write("\ntest_one_issue_per_module_when_asked\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        report = fixture(directory, tied=True)
        path = write_report(directory, report)
        out = directory / "shadowing"
        code, _ = run(
            [
                f"--report={path}",
                f"--out={out}",
                "--include-differing",
                "--per-module",
            ]
        )

        check("exit", code, 0)
        check(
            "one directory each",
            sorted(x.name for x in out.iterdir()),
            ["NEWER-MIB", "TIED-MIB"],
        )
        check("each with its issue", (out / "TIED-MIB" / "issue.md").is_file(), True)

        one = (out / "NEWER-MIB" / "issue.md").read_text(encoding="utf-8")

        check("about its own module", "NEWER-MIB" in one, True)
        check("and no other", "TIED-MIB" in one, False)


def test_the_cli_names_the_module_it_was_asked_for() -> None:
    """--module reports one of a report's findings and not the rest."""
    sys.stdout.write("\ntest_the_cli_names_the_module_it_was_asked_for\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        report = fixture(directory, tied=True)
        found = contribute_mibs.collect(
            report, ("local",), include_differing=True, only=("TIED-MIB",)
        )

        check("just that one", [x.module for x in found], ["TIED-MIB"])


def test_a_report_with_nothing_to_say_says_so() -> None:
    """A deployment whose MIBs are all behind ours must not produce an issue."""
    sys.stdout.write("\ntest_a_report_with_nothing_to_say_says_so\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        report = fixture(directory)
        report["shadowed"] = {}
        path = write_report(directory, report)
        out = directory / "shadowing"
        code, printed = run([f"--report={path}", f"--out={out}"])

        check("exit", code, 0)
        check("said so", "Nothing to report." in printed, True)
        check("wrote nothing", out.exists(), False)


def test_the_gh_command_is_the_one_documented() -> None:
    """What the authenticated path runs, without running it."""
    sys.stdout.write("\ntest_the_gh_command_is_the_one_documented\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        path = write_report(directory, fixture(directory))
        out = directory / "shadowing"
        calls: list[list[str]] = []
        original = contribute_mibs.run_gh

        def recorder(arguments: list[str]) -> str:
            calls.append(arguments)
            return "https://github.com/pysnmp/mibs/issues/1"

        contribute_mibs.run_gh = recorder

        try:
            code, printed = run(
                [
                    f"--report={path}",
                    f"--out={out}",
                    "--submit=gh",
                    "--yes",
                    "--label=mib-contribution",
                ]
            )
        finally:
            contribute_mibs.run_gh = original

        check("exit", code, 0)
        check("checked the login first", calls[0], ["auth", "status"])
        check(
            "created the issue",
            calls[1][:4],
            ["issue", "create", "--repo", "pysnmp/mibs"],
        )
        check(
            "from the file it wrote",
            calls[1][calls[1].index("--body-file") + 1],
            str(out / "issue.md"),
        )
        check("with the label", calls[1][-2:], ["--label", "mib-contribution"])
        check("printed the issue", "issues/1" in printed, True)


def test_a_gist_replaces_the_inline_mib() -> None:
    """The authenticated path can put the sources somewhere an issue body fits."""
    sys.stdout.write("\ntest_a_gist_replaces_the_inline_mib\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        path = write_report(directory, fixture(directory))
        out = directory / "shadowing"
        calls: list[list[str]] = []
        original = contribute_mibs.run_gh

        def recorder(arguments: list[str]) -> str:
            calls.append(arguments)

            if arguments[0] == "gist":
                return "https://gist.github.com/example/1"

            return "https://github.com/pysnmp/mibs/issues/1"

        contribute_mibs.run_gh = recorder

        try:
            code, _ = run(
                [f"--report={path}", f"--out={out}", "--submit=gh", "--yes", "--gist"]
            )
        finally:
            contribute_mibs.run_gh = original

        body = (out / "issue.md").read_text(encoding="utf-8")

        check("exit", code, 0)
        check("the gist was created", calls[1][:2], ["gist", "create"])
        check("from the files it wrote", calls[1][-1], str(out / "mibs" / "NEWER-MIB"))
        check("the issue links it", "https://gist.github.com/example/1" in body, True)


def checkout(directory: pathlib.Path) -> pathlib.Path:
    """A clone shaped like this repository, with somewhere to push.

    Enough of it for a pull request to be written into: the two paths
    ``--submit=pr`` refuses to work without, a commit to branch from, and an
    origin, because the submission pushes before it asks for the pull request.
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
    (clone / "mib-sources.json").write_text(
        json.dumps(
            {
                "modules": {},
                "publishers": {"example-mibs": {"name": "Example Networks"}},
            }
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


def instead_of(name: str, replacement: object) -> object:
    """Put *replacement* in the module under *name*, returning what was there."""
    original = getattr(contribute_mibs, name)
    setattr(contribute_mibs, name, replacement)

    return original


def test_a_module_this_distribution_does_not_carry_is_offered() -> None:
    """The half of a collection that shadowing cannot report: what is missing."""
    sys.stdout.write("\ntest_a_module_this_distribution_does_not_carry_is_offered\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        found = contribute_mibs.collect(fixture(directory, new=True), ("local",))
        offered = {x.module: x for x in found}

        check("both kinds", sorted(offered), ["NEW-MIB", "NEWER-MIB"])
        check("verdict", offered["NEW-MIB"].verdict, contribute_mibs.NOT_CARRIED)
        check("nothing was passed over", offered["NEW-MIB"].published, None)
        check("revision read", offered["NEW-MIB"].local.revision, "202402010000Z")

        body = contribute_mibs.compose(found, "5.1.0", "contribution.zip")

        check("the table says so", "| not carried |" in body, True)
        check(
            "and the data does",
            json.loads(body.split("```json\n")[1].split("\n```")[0])["modules"][0][
                "published"
            ],
            None,
        )


def test_a_module_this_distribution_carries_is_not_new() -> None:
    """A module both sets hold is a better copy at most, never a missing one."""
    sys.stdout.write("\ntest_a_module_this_distribution_carries_is_not_new\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        report = fixture(directory, new=True)
        found = contribute_mibs.collect(report, ("local",), skip_new=True)

        check("--skip-new", [x.module for x in found], ["NEWER-MIB"])

        # NEWER-MIB is attributed to the offered set in provenance and is still
        # not a missing module, because the corpus root holds a file by that
        # name.
        every = contribute_mibs.collect(report, ("local",))

        check(
            "carried modules are not offered as new",
            [x.verdict for x in every if x.module == "NEWER-MIB"],
            ["newer"],
        )


def test_a_report_with_no_resolution_is_refused() -> None:
    """`--emit=report` alone writes an empty record, which is not an empty result."""
    sys.stdout.write("\ntest_a_report_with_no_resolution_is_refused\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        report = fixture(directory)
        report["shadowed"] = {}
        report["provenance"] = {}
        path = write_report(directory, report)
        code, printed = run([f"--report={path}", f"--out={directory / 'out'}"])

        check("refused", code, 2)
        check("said nothing was reported", "Nothing to report" in printed, False)


def test_an_open_issue_stops_a_second_report() -> None:
    """A module somebody already reported is somebody's already."""
    sys.stdout.write("\ntest_an_open_issue_stops_a_second_report\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        path = write_report(directory, fixture(directory, new=True))
        original = instead_of(
            "search_issues",
            lambda repository, query, pages=1: (
                [
                    {
                        "number": 7,
                        "state": "open",
                        "title": "NEWER-MIB is out of date",
                        "body": '{"module": "NEWER-MIB"}',
                    }
                ]
                if "mib-contribution" in query
                else []
            ),
        )

        try:
            code, printed = run(
                [
                    f"--report={path}",
                    f"--out={directory / 'out'}",
                    "--check-duplicates",
                ]
            )
        finally:
            instead_of("search_issues", original)

        check("exit", code, 0)
        check("said which one", "NEWER-MIB is already open here" in printed, True)
        check("named the issue", "issue #7 (open)" in printed, True)
        check("kept the other", "NEW-MIB" in printed, True)


def test_a_closed_issue_does_not() -> None:
    """Closed for a reason nothing here can read, so the module is offered again."""
    sys.stdout.write("\ntest_a_closed_issue_does_not\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        path = write_report(directory, fixture(directory))
        original = instead_of(
            "search_issues",
            lambda repository, query, pages=1: [
                {
                    "number": 7,
                    "state": "closed",
                    "title": "NEWER-MIB",
                    "body": '{"module": "NEWER-MIB"}',
                }
            ],
        )

        try:
            code, printed = run(
                [
                    f"--report={path}",
                    f"--out={directory / 'out'}",
                    "--check-duplicates",
                ]
            )
        finally:
            instead_of("search_issues", original)

        check("exit", code, 0)
        check("said so", "was reported before and closed" in printed, True)
        check("reported anyway", (directory / "out" / "issue.md").is_file(), True)


def test_an_unattended_run_can_refuse_to_file_blind() -> None:
    """Filing a duplicate every month is worse than filing nothing this month."""
    sys.stdout.write("\ntest_an_unattended_run_can_refuse_to_file_blind\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        path = write_report(directory, fixture(directory))

        def unreachable(repository: str, query: str, pages: int = 1) -> list[dict]:
            raise contribute_mibs.Refused("the GitHub search could not be reached")

        original = instead_of("search_issues", unreachable)

        try:
            without = run(
                [f"--report={path}", f"--out={directory / 'a'}", "--check-duplicates"]
            )
            with_flag = run(
                [
                    f"--report={path}",
                    f"--out={directory / 'b'}",
                    "--check-duplicates",
                    "--require-duplicate-check",
                ]
            )
        finally:
            instead_of("search_issues", original)

        check("by default it carries on", without[0], 0)
        check("and says so", "could not run" in without[1], True)
        check("--require-duplicate-check stops", with_flag[0], 2)


def test_the_pull_request_is_committed_to_the_checkout() -> None:
    """The freshness process's half: the modules land in a branch, not in prose."""
    sys.stdout.write("\ntest_the_pull_request_is_committed_to_the_checkout\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        clone = checkout(directory)
        path = write_report(directory, fixture(directory, new=True))
        calls: list[list[str]] = []

        def recorder(arguments: list[str]) -> str:
            calls.append(arguments)

            return "https://github.com/pysnmp/mibs/pull/9"

        original = instead_of("run_gh", recorder)

        try:
            code, printed = run(
                [
                    f"--report={path}",
                    f"--out={directory / 'out'}",
                    "--submit=pr",
                    "--yes",
                    "--allow-duplicates",
                    f"--checkout={clone}",
                    "--vendor=example",
                    "--publisher=example-mibs",
                ]
            )
        finally:
            instead_of("run_gh", original)

        committed = subprocess.run(
            [
                "git",
                "-C",
                str(clone),
                "show",
                "--name-only",
                "--format=%s",
                "mibs/contribution",
            ],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        manifest = json.loads(
            subprocess.run(
                ["git", "-C", str(clone), "show", "mibs/contribution:mib-sources.json"],
                capture_output=True,
                text=True,
                check=True,
            ).stdout
        )

        check("exit", code, 0)
        check("printed the pull request", "pull/9" in printed, True)
        check(
            "the MIB is in the branch", "src/vendor/example/NEW-MIB" in committed, True
        )
        check(
            "so is the older module's replacement",
            "src/vendor/example/NEWER-MIB" in committed,
            True,
        )
        check(
            "provenance was recorded",
            manifest["modules"]["src/vendor/example/NEW-MIB"],
            {"publisher": "example-mibs"},
        )
        check("gh opened it", calls[0][:2], ["pr", "create"])
        check(
            "against the branch it pushed",
            calls[0][calls[0].index("--head") + 1],
            "mibs/contribution",
        )
        check(
            "the body carries no ASN.1, which is in the diff",
            "DEFINITIONS ::= BEGIN"
            in (directory / "out" / "pull-request.md").read_text(),
            False,
        )
        check(
            "and the checkout is back where it started",
            subprocess.run(
                ["git", "-C", str(clone), "rev-parse", "--abbrev-ref", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
            ).stdout.strip(),
            "main",
        )


def test_a_pull_request_needs_this_repository_and_a_clean_tree() -> None:
    """Two refusals: the wrong directory, and somebody's unfinished work in it."""
    sys.stdout.write("\ntest_a_pull_request_needs_this_repository_and_a_clean_tree\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        elsewhere = ""

        try:
            contribute_mibs.require_checkout(directory)
        except contribute_mibs.Refused as exc:
            elsewhere = str(exc)

        check("not a checkout", "is not a checkout" in elsewhere, True)

        clone = checkout(directory)
        (clone / "mib-sources.json").write_text("{}", encoding="utf-8")
        dirty = ""

        try:
            contribute_mibs.require_checkout(clone)
        except contribute_mibs.Refused as exc:
            dirty = str(exc)

        check("dirty tree", "uncommitted changes" in dirty, True)


def test_a_publisher_the_manifest_does_not_define_is_refused() -> None:
    """A provenance entry naming a publisher that does not exist fails --validate."""
    sys.stdout.write("\ntest_a_publisher_the_manifest_does_not_define_is_refused\n")

    with tempfile.TemporaryDirectory() as name:
        directory = pathlib.Path(name)
        clone = checkout(directory)
        refused = ""

        try:
            contribute_mibs.record_provenance(
                clone, ["src/vendor/example/NEW-MIB"], "nobody"
            )
        except contribute_mibs.Refused as exc:
            refused = str(exc)

        check("refused", "defines no publisher 'nobody'" in refused, True)
        check("named the ones it has", "example-mibs" in refused, True)


def main() -> int:
    """Run every case and report."""
    test_a_newer_local_copy_is_reported()
    test_a_module_the_published_copy_won_is_not_a_finding()
    test_a_tie_is_reported_only_when_asked_for()
    test_a_namespace_that_is_not_in_the_report_is_an_error()
    test_the_issue_carries_no_path_from_this_machine()
    test_a_module_too_long_to_inline_is_named_instead()
    test_the_bundle_holds_the_mib_and_the_data()
    test_submitting_takes_a_second_flag()
    test_the_url_carries_the_report()
    test_a_report_too_long_for_a_url_is_left_in_a_file()
    test_one_issue_per_module_when_asked()
    test_the_cli_names_the_module_it_was_asked_for()
    test_a_report_with_nothing_to_say_says_so()
    test_the_gh_command_is_the_one_documented()
    test_a_gist_replaces_the_inline_mib()
    test_a_module_this_distribution_does_not_carry_is_offered()
    test_a_module_this_distribution_carries_is_not_new()
    test_a_report_with_no_resolution_is_refused()
    test_an_open_issue_stops_a_second_report()
    test_a_closed_issue_does_not()
    test_an_unattended_run_can_refuse_to_file_blind()
    test_the_pull_request_is_committed_to_the_checkout()
    test_a_pull_request_needs_this_repository_and_a_clean_tree()
    test_a_publisher_the_manifest_does_not_define_is_refused()

    if FAILURES:
        sys.stderr.write(f"\n{len(FAILURES)} check(s) failed:\n")
        for name in FAILURES:
            sys.stderr.write(f"  {name}\n")
        return 1

    sys.stdout.write("\nAll checks passed.\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
