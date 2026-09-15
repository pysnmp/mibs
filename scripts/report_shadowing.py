#!/usr/bin/env python3
#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Report the modules a local MIB set holds a better copy of than this distribution.

A deployment that mounts its own MIBs beside the published corpus resolves the
two together. ``charts/mibserver`` does it in an init container and
``mibcorpus`` does it on a command line, by the same rule in both: the newest
MODULE-IDENTITY revision wins and configured order breaks a tie. Where both
sets hold a module, one copy is used and the other is passed over, and
``report.json`` records the pair under ``shadowed``.

The half of that record worth sending back is the modules where the local copy
won on a newer revision. Each one is a module this distribution is behind on,
established by a build rather than by a reader's impression, with the newer
text sitting on the same disk. This script turns those records into a GitHub
issue carrying the module names, both revisions, and the MIB sources
themselves, so that reporting one costs a command instead of a pull request.

Three things it deliberately does not do. It does not decide that a module is
worth reporting when the local copy won on source order alone, unless asked
with ``--include-differing``: two copies of one name are often two different
modules. It does not send anything without both ``--submit`` and ``--yes``,
because a MIB from a local tree can be a vendor file under a licence that
forbids redistribution, or a file carrying site detail in its comments. It
writes no absolute path into an issue, because a path from this machine names
this machine.

Revisions and digests are read with pysmi, which produced the report this
reads and is therefore already installed wherever it is run. This repository
keeps no second implementation of a rule pysmi publishes.

Usage:

    # Resolve a local directory against a published corpus and write a report.
    mibcorpus --resolve-namespace=standard:corpus:./asn1 \\
        --namespace=vendor:local:./my-mibs \\
        --output-directory=./out --emit=report

    # What would be reported, written to ./shadowing and sent nowhere.
    uv run python scripts/report_shadowing.py --report=out/report.json

    # File it, in a browser, under your own account and with no token here.
    uv run python scripts/report_shadowing.py --report=out/report.json \\
        --submit=url --yes

    # File it with the GitHub CLI, which must already be authenticated.
    uv run python scripts/report_shadowing.py --report=out/report.json \\
        --submit=gh --yes
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
import webbrowser
import zipfile
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

#: The marker that makes these issues findable as a set, whoever filed them and
#: whatever the title says. HTML comment, so a reader never sees it and a
#: maintainer searching the tracker does.
MARKER = "<!-- mib-shadowing-report v1 -->"

#: What GitHub accepts in an issue body, in characters.
BODY_LIMIT = 65536

#: What this fills of it. The remainder is the margin between the length
#: counted while choosing what to inline and the length of the rendered
#: result.
INLINE_BUDGET = 60000

#: Longest prefilled issue URL this will hand to a browser. GitHub's own front
#: end refuses a request line well before the theoretical limit, and a URL that
#: is refused loses the whole report; over this, the body goes to a file to
#: paste instead.
URL_LIMIT = 6000

#: pysmi's name for the rule that decided, when it decided on the text rather
#: than on the order the sources were configured in. This is the finding worth
#: reporting: the local copy is a later revision of the same module.
PRECEDENCE_NEWEST = "newest MODULE-IDENTITY revision"

#: What each ``precedence`` value in a report means about the two copies, in
#: the words the issue prints. Anything pysmi adds later reads as ``differs``,
#: which is the conservative reading of a rule this does not know.
VERDICTS = {
    PRECEDENCE_NEWEST: "newer",
    "source order; equal MODULE-IDENTITY revisions": "same revision, different text",
    "source order; no MODULE-IDENTITY revision to compare": "no revision to compare",
}


#: pysmi's reader for a module's MODULE-IDENTITY revision, normalised.
Revision = Callable[[str], "str | None"]

#: pysmi's digest of a MIB source, as ``report.json`` records it.
Digest = Callable[[str], str]


class Refused(Exception):
    """Something this will not do, phrased for the person who asked."""


@dataclass
class Copy:
    """One of the two copies of a module, as the issue describes it."""

    #: The namespace that supplied it, from the report.
    namespace: str
    #: Path relative to that namespace's root. Never the absolute path: it
    #: names the machine the build ran on, which is nobody's business here.
    file: str
    #: Normalised MODULE-IDENTITY revision, or an empty string for a module
    #: carrying none, which is every SMIv1 module.
    revision: str
    #: pysmi's digest of the text, as ``report.json`` records it.
    digest: str
    #: Size of the text, in bytes.
    size: int

    def as_dict(self) -> dict[str, object]:
        """This copy as plain data, for the block an agent reads."""
        return {
            "file": self.file,
            "revision": self.revision,
            "digest": self.digest,
            "bytes": self.size,
        }


@dataclass
class Finding:
    """One module the local set holds a differing copy of, and won with."""

    #: Module name, which is the name the corpus publishes it under.
    module: str
    #: What the precedence rule says about the pair. See :py:data:`VERDICTS`.
    verdict: str
    #: The rule itself, in pysmi's words.
    precedence: str
    #: The copy that won, which is the local one.
    local: Copy
    #: The copy that was passed over, which is this distribution's.
    published: Copy
    #: The local copy's ASN.1 text, which is what the issue carries.
    text: str
    #: The local copy's bytes as they are on disk, which is what the archive
    #: carries. Decoding is lossy for a MIB that is not UTF-8; the archive is
    #: what a pull request should be cut from.
    raw: bytes

    def as_dict(self, *, attached: bool) -> dict[str, object]:
        """This finding as plain data, for the block an agent reads."""
        return {
            "module": self.module,
            "verdict": self.verdict,
            "precedence": self.precedence,
            "local": self.local.as_dict(),
            "published": self.published.as_dict(),
            "inline": attached,
        }


@dataclass
class Submission:
    """One issue: what it says, what it carries, and where that was written."""

    slug: str
    title: str
    findings: list[Finding]
    directory: Path
    body: str = ""
    #: The archive of MIB sources, written by :py:func:`write_bundle` before
    #: anything reads it. ``directory`` until then.
    archive: Path = Path()
    url: str = ""


def pysmi_reader() -> tuple[Revision, Digest, str]:
    """pysmi's revision and digest functions, and the version they came from.

    Raises:
        Refused: when pysmi is not importable, which means this is not being
            run where the report was produced.
    """
    try:
        from pysmi import __version__ as version
        from pysmi.compiler import revision_of, source_digest
    except ImportError as exc:
        raise Refused(
            "this reads revisions and digests with pysmi, which is what produced "
            "the report and what a pull request here would be checked with. "
            "Install it with `pip install pysnmp-pysmi` and run this where the "
            "MIBs are."
        ) from exc

    return revision_of, source_digest, version


def namespace_roots(report: dict) -> dict[str, str]:
    """Each namespace in the report, mapped to the directory it reads.

    A ``package:`` namespace is left out: its modules come from an installed
    Python package rather than from a path, so nothing in a report's file
    paths can be matched back to it.
    """
    roots = {}

    for namespace in report.get("namespaces", ()):
        source = str(namespace.get("source", ""))

        if not source or source.startswith("package:"):
            continue

        roots[str(namespace["name"])] = str(Path(source).resolve())

    return roots


def local_path(path: str) -> Path | None:
    """The file a report names, for the readers that name one with a URL.

    ``report.json`` records what a reader was asked for, and pysmi's file
    reader records that as a ``file://`` URL rather than as a path. A module
    fetched over HTTP is not a file on this machine at all, and returns
    ``None``.
    """
    parsed = urllib.parse.urlparse(path)

    if parsed.scheme == "file":
        return Path(urllib.request.url2pathname(parsed.path))

    if parsed.scheme and len(parsed.scheme) > 1:
        return None

    return Path(path)


def namespace_of(path: str, roots: dict[str, str]) -> str:
    """Which namespace supplied the file at *path*, by longest root that holds it.

    Longest rather than first, because a namespace nested inside another one
    is a legitimate arrangement and the inner one is the more specific answer.
    """
    found = local_path(path)

    if found is None:
        return ""

    resolved = str(found.resolve())
    best = ""

    for name, root in roots.items():
        if (resolved == root or resolved.startswith(root.rstrip("/") + "/")) and len(
            root
        ) > len(roots.get(best, "")):
            best = name

    return best


def relative_file(path: str, root: str) -> str:
    """The file at *path*, named relative to its namespace root.

    Falls back to the bare file name, which is all a path outside the root can
    contribute without naming the machine it is on. No absolute path reaches an
    issue: a build's own paths name the machine it ran on.
    """
    found = local_path(path)

    if found is None:
        return path.rsplit("/", 1)[-1]

    try:
        return f"{found.resolve().relative_to(root)}"
    except ValueError:
        return found.name


def read_source(path: Path) -> tuple[str, bytes]:
    """The MIB at *path*, as text to print and as the bytes to attach.

    A MIB that is not valid UTF-8 is decoded as Latin-1 rather than refused:
    the decoded text is what the issue prints and the bytes are what a pull
    request would be cut from, so a lossy decode costs display and not the
    report.
    """
    raw = path.read_bytes()

    try:
        return raw.decode("utf-8"), raw
    except UnicodeDecodeError:
        return raw.decode("latin-1"), raw


def describe_revision(revision: str) -> str:
    """A normalised ``YYYYMMDDHHMMZ`` revision, as a date to read."""
    if not revision or len(revision) < 8:
        return "none"

    return f"{revision[0:4]}-{revision[4:6]}-{revision[6:8]}"


def collect(
    report: dict,
    mine: tuple[str, ...],
    *,
    include_differing: bool = False,
    only: tuple[str, ...] = (),
) -> list[Finding]:
    """Every module in the report whose local copy beat a published one.

    Args:
        report: a parsed ``report.json`` from a build that resolved a local
            namespace against the published corpus.
        mine: the namespaces that are the user's own. Everything else in the
            report is the distribution.
        include_differing: also report a module the local copy won by source
            order rather than by revision. Off by default: two copies of one
            name are often two different modules rather than two revisions of
            one, and the rule cannot tell them apart.
        only: report just these modules, when given.

    Returns:
        One finding per module, module name order.
    """
    revision_of, source_digest, _ = pysmi_reader()
    roots = namespace_roots(report)
    missing = [x for x in mine if x not in roots]

    if missing:
        raise Refused(
            f"the report holds no namespace named {', '.join(missing)}. "
            f"It holds {', '.join(sorted(roots)) or 'none with a directory'}. "
            "Name your own with --namespace."
        )

    provenance = report.get("provenance", {})
    found = []

    for module, record in sorted(report.get("shadowed", {}).items()):
        if only and module not in only:
            continue

        used = str(record.get("used", ""))
        winner = namespace_of(used, roots)

        if winner not in mine:
            continue

        precedence = str(record.get("precedence", ""))
        verdict = VERDICTS.get(precedence, "differs")

        if precedence != PRECEDENCE_NEWEST and not include_differing:
            continue

        passed = [
            (x, namespace_of(x, roots))
            for x in record.get("shadowed", ())
            if namespace_of(x, roots) not in mine
        ]

        if not passed:
            continue

        mine_on_disk = local_path(used)

        if mine_on_disk is None or not mine_on_disk.is_file():
            raise Refused(
                f"{module} was resolved from {used}, which is not a file here. "
                "Run this on the machine the build ran on, and before the "
                "sources move."
            )

        text, raw = read_source(mine_on_disk)
        their_path, their_namespace = passed[0]
        theirs_on_disk = local_path(their_path)
        their_text = ""

        if theirs_on_disk is not None and theirs_on_disk.is_file():
            their_text, _ = read_source(theirs_on_disk)

        found.append(
            Finding(
                module=module,
                verdict=verdict,
                precedence=precedence,
                local=Copy(
                    namespace=winner,
                    file=relative_file(used, roots[winner]),
                    revision=revision_of(text) or "",
                    digest=provenance.get(module, {}).get("digest")
                    or source_digest(text),
                    size=len(raw),
                ),
                published=Copy(
                    namespace=their_namespace,
                    file=relative_file(their_path, roots.get(their_namespace, "")),
                    revision=(their_text and revision_of(their_text)) or "",
                    digest=source_digest(their_text) if their_text else "",
                    size=len(their_text.encode("utf-8")) if their_text else 0,
                ),
                text=text,
                raw=raw,
            )
        )

    return found


def title_for(findings: list[Finding]) -> str:
    """What the issue is called, from what it holds."""
    if len(findings) == 1:
        one = findings[0]

        if one.verdict == "newer":
            return (
                f"{one.module}: a local copy is newer "
                f"({describe_revision(one.local.revision)} here, "
                f"{describe_revision(one.published.revision)} published)"
            )

        return f"{one.module}: a local copy differs from the published one"

    named = ", ".join(x.module for x in findings[:3])
    rest = f" and {len(findings) - 3} more" if len(findings) > 3 else ""

    return (
        f"{len(findings)} modules a local MIB set holds a better copy of: {named}{rest}"
    )


def payload(
    findings: list[Finding], inline: set[str], version: str, archive: str
) -> dict:
    """The report as data, for an agent picking the issue up.

    The same facts as the table above it, in the form that does not have to be
    parsed out of prose: a pull request for one of these modules needs the
    name, the two revisions and the digest of the text it should carry.
    """
    return {
        "report": "mib-shadowing v1",
        "pysmi": version,
        "archive": archive,
        "modules": [x.as_dict(attached=x.module in inline) for x in findings],
    }


def render(
    findings: list[Finding],
    *,
    inline: set[str],
    version: str,
    archive: str,
    gist: str = "",
) -> str:
    """The issue, in Markdown.

    Args:
        findings: what to report, which is at least one module.
        inline: the modules whose ASN.1 text the body carries. The rest are in
            the archive, because an issue body holds 65,536 characters and a
            MIB set can hold more.
        version: the pysmi that read the revisions.
        archive: the file name the archive was written under.
        gist: URL the MIB sources were uploaded to, when they were.
    """
    out = [
        f"### A local MIB set holds a better copy of {len(findings)} "
        f"module{'s' if len(findings) != 1 else ''}",
        "",
        MARKER,
        "",
        "`mibcorpus` resolved a local MIB directory against this distribution's",
        "published corpus. In each module below the local copy won, so the",
        "published copy is the one to replace.",
        "",
        "| module | local | published | why the local copy won |",
        "| --- | --- | --- | --- |",
    ]

    for one in findings:
        out.append(
            f"| `{one.module}` | {describe_revision(one.local.revision)} "
            f"| {describe_revision(one.published.revision)} | {one.precedence or 'source order'} |"
        )

    out += [
        "",
        "#### What this issue still needs",
        "",
        "A module cannot be merged here without its provenance: `mib-sources.json`",
        "records a publisher for every module under `src/`, so that a later",
        "revision can be noticed by a build rather than by a reader. Fill these in:",
        "",
        "- Publisher, and the URL the files were downloaded from:",
        "- Device and software release they were taken from:",
        "- Vendor directory they belong under (`src/vendor/<vendor>/`):",
        "- [ ] These files may be redistributed.",
        "",
    ]

    if gist:
        out += [
            f"The MIB sources are attached as a gist: {gist}",
            "",
        ]

    outside = [x for x in findings if x.module not in inline]

    if outside and not gist:
        out += [
            f"{len(outside)} of these {'is' if len(outside) == 1 else 'are'} too long "
            "for an issue body. The ASN.1 is in",
            f"`{archive}`, attached to this issue:",
            "",
            *(f"- `{x.module}`" for x in outside),
            "",
        ]

    for one in findings:
        out += [
            f"#### {one.module}",
            "",
            "| | local | published |",
            "| --- | --- | --- |",
            f"| revision | {describe_revision(one.local.revision)} | {describe_revision(one.published.revision)} |",
            f"| bytes | {one.local.size:,} | {one.published.size:,} |",
            f"| digest | `{one.local.digest}` | `{one.published.digest or 'not read'}` |",
            "",
        ]

        if one.module in inline:
            out += [
                f"<details><summary>{one.module}, as the local set holds it</summary>",
                "",
                "```",
                one.text.replace("```", "``\u200b`"),
                "```",
                "",
                "</details>",
                "",
            ]

    out += [
        "#### Report data",
        "",
        "```json",
        json.dumps(payload(findings, inline, version, archive), indent=2),
        "```",
        "",
        "<sub>Written by `scripts/report_shadowing.py` from a `mibcorpus` report.",
        "Revisions and digests are pysmi's, read from the files themselves.</sub>",
    ]

    return "\n".join(out) + "\n"


def choose_inline(findings: list[Finding], overhead: int) -> set[str]:
    """Which modules the body carries, smallest first until the budget is gone.

    Smallest first because the number of modules an issue states in full is
    worth more than which ones: a reader who has five of six modules in front
    of them is one download from the sixth.
    """
    room = INLINE_BUDGET - overhead
    inline: set[str] = set()

    for one in sorted(findings, key=lambda x: len(x.text)):
        cost = len(one.text) + 200

        if cost > room:
            continue

        inline.add(one.module)
        room -= cost

    return inline


def compose(findings: list[Finding], version: str, archive: str, gist: str = "") -> str:
    """The issue body, with as many modules inlined as it holds."""
    empty: set[str] = set()
    overhead = len(
        render(findings, inline=empty, version=version, archive=archive, gist=gist)
    )
    inline = choose_inline(findings, overhead)
    body = render(findings, inline=inline, version=version, archive=archive, gist=gist)

    if len(body) <= BODY_LIMIT:
        return body

    return render(findings, inline=empty, version=version, archive=archive, gist=gist)


def write_bundle(submission: Submission, version: str) -> None:
    """Write the issue, the data and the MIBs, and leave the paths on the submission."""
    directory = submission.directory
    mibs = directory / "mibs"
    mibs.mkdir(parents=True, exist_ok=True)

    for one in submission.findings:
        (mibs / one.module).write_bytes(one.raw)

    archive = directory / f"{submission.slug}.zip"

    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for one in submission.findings:
            bundle.writestr(one.module, one.raw)

    submission.archive = archive
    submission.body = compose(submission.findings, version, archive.name)

    (directory / "issue.md").write_text(submission.body, encoding="utf-8")
    (directory / "findings.json").write_text(
        json.dumps(
            payload(
                submission.findings,
                {x.module for x in submission.findings},
                version,
                archive.name,
            ),
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def issue_url(repository: str, title: str, body: str, labels: tuple[str, ...]) -> str:
    """A GitHub new-issue URL with the report already in it."""
    query = {"title": title, "body": body}

    if labels:
        query["labels"] = ",".join(labels)

    return f"https://github.com/{repository}/issues/new?" + urllib.parse.urlencode(
        query
    )


def run_gh(arguments: list[str]) -> str:
    """One `gh` invocation, with its failure reported as its own message."""
    if not shutil.which("gh"):
        raise Refused(
            "--submit=gh needs the GitHub CLI on PATH. Install it from "
            "https://cli.github.com/, or use --submit=url, which needs no "
            "credentials here."
        )

    finished = subprocess.run(
        ["gh", *arguments], capture_output=True, text=True, check=False
    )

    if finished.returncode:
        raise Refused(
            f"`gh {' '.join(arguments)}` exited {finished.returncode}: "
            f"{finished.stderr.strip() or 'no error text'}"
        )

    return finished.stdout.strip()


def submit_gh(
    submission: Submission,
    repository: str,
    labels: tuple[str, ...],
    version: str,
    *,
    gist: bool,
) -> str:
    """File the issue with the GitHub CLI, under the account it is signed in as."""
    run_gh(["auth", "status"])

    if gist:
        files = [
            str(submission.directory / "mibs" / x.module) for x in submission.findings
        ]
        url = run_gh(
            [
                "gist",
                "create",
                "--desc",
                f"MIB sources for {submission.title}",
                *files,
            ]
        ).splitlines()[-1]

        submission.body = compose(submission.findings, version, "", gist=url)
        (submission.directory / "issue.md").write_text(
            submission.body, encoding="utf-8"
        )

    arguments = [
        "issue",
        "create",
        "--repo",
        repository,
        "--title",
        submission.title,
        "--body-file",
        str(submission.directory / "issue.md"),
    ]

    for label in labels:
        arguments += ["--label", label]

    return run_gh(arguments).splitlines()[-1]


def describe(submission: Submission) -> str:
    """What this submission would publish, for the person about to publish it."""
    return (
        f"{submission.title}\n"
        f"  {len(submission.findings)} module(s): "
        f"{', '.join(x.module for x in submission.findings)}\n"
        f"  body {len(submission.body):,} characters, archive {submission.archive}\n"
    )


def main(argv: list[str] | None = None) -> int:
    """Write the report, and file it when asked twice."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report",
        type=Path,
        required=True,
        help="report.json from a mibcorpus run over your MIBs and the corpus",
    )
    parser.add_argument(
        "--namespace",
        action="append",
        default=[],
        help="a namespace in that report that is yours (default: local)",
    )
    parser.add_argument(
        "--module",
        action="append",
        default=[],
        help="report only this module; repeatable",
    )
    parser.add_argument(
        "--include-differing",
        action="store_true",
        help="also report a module your copy won on source order rather than revision",
    )
    parser.add_argument(
        "--per-module",
        action="store_true",
        help="one issue per module rather than one issue for all of them",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("shadowing"),
        help="directory to write the issue, the data and the MIBs into",
    )
    parser.add_argument(
        "--submit",
        choices=("none", "url", "gh"),
        default="none",
        help="none writes the files and sends nothing; url prints a prefilled "
        "GitHub issue URL for you to review and post; gh files it with the "
        "GitHub CLI",
    )
    parser.add_argument(
        "--repository",
        default="pysnmp/mibs",
        help="the repository to file against (default: pysnmp/mibs)",
    )
    parser.add_argument(
        "--label",
        action="append",
        default=[],
        help="a label to apply; the repository must already have it",
    )
    parser.add_argument(
        "--gist",
        action="store_true",
        help="with --submit=gh, upload the MIBs as a secret gist and link it",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="with --submit=url, open the URL in a browser",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="confirm that the MIBs in this report may be published",
    )
    options = parser.parse_args(argv)

    try:
        return report(options)
    except Refused as refusal:
        sys.stderr.write(f"{refusal}\n")
        return 2


def report(options: argparse.Namespace) -> int:
    """Everything main does, with its failures still exceptions."""
    _, _, version = pysmi_reader()

    if not options.report.is_file():
        raise Refused(
            f"{options.report} is not a file. Produce one with `mibcorpus "
            "--emit=report` over your MIBs and the published corpus."
        )

    with options.report.open(encoding="utf-8") as fileObj:
        parsed = json.load(fileObj)

    findings = collect(
        parsed,
        tuple(options.namespace) or ("local",),
        include_differing=options.include_differing,
        only=tuple(options.module),
    )

    if not findings:
        sys.stdout.write(
            "No module in this report has a local copy that beat the published "
            "one. Nothing to report.\n"
        )
        return 0

    if options.per_module:
        submissions = [
            Submission(
                slug=x.module,
                title=title_for([x]),
                findings=[x],
                directory=options.out / x.module,
            )
            for x in findings
        ]
    else:
        submissions = [
            Submission(
                slug="shadowed-mibs",
                title=title_for(findings),
                findings=findings,
                directory=options.out,
            )
        ]

    for submission in submissions:
        write_bundle(submission, version)

    sys.stdout.write(f"Wrote {len(submissions)} report(s) under {options.out}:\n\n")

    for submission in submissions:
        sys.stdout.write(describe(submission))

    if options.submit == "none":
        sys.stdout.write(
            "\nRead each issue.md before sending it: a MIB from a local tree can "
            "carry site detail in its comments, and a vendor's licence decides "
            "whether its text may be republished here. Then re-run with "
            "--submit=url --yes, or --submit=gh --yes.\n"
        )
        return 0

    if not options.yes:
        raise Refused(
            "--submit publishes these MIB sources in a public issue. Read the "
            "issue.md files above, then add --yes."
        )

    labels = tuple(options.label)
    sys.stdout.write("\n")

    for submission in submissions:
        if options.submit == "gh":
            submission.url = submit_gh(
                submission,
                options.repository,
                labels,
                version,
                gist=options.gist,
            )
            sys.stdout.write(f"{submission.url}\n")
            continue

        url = issue_url(options.repository, submission.title, submission.body, labels)

        if len(url) > URL_LIMIT:
            short = (
                f"{MARKER}\n\nThe report for this is in the attached "
                f"`{submission.archive.name}` and in the comment below. Paste the "
                "contents of `issue.md` here."
            )
            url = issue_url(options.repository, submission.title, short, labels)
            sys.stdout.write(
                f"The report is too long to carry in a URL. Open the URL below, "
                f"paste {submission.directory / 'issue.md'} into the body, and "
                f"attach {submission.archive}.\n"
            )
        else:
            sys.stdout.write(
                f"Open this, check it, and post it. Attach {submission.archive} "
                "for the MIB sources.\n"
            )

        sys.stdout.write(f"{url}\n")
        submission.url = url

        if options.open:
            webbrowser.open(url)

    return 0


if __name__ == "__main__":
    sys.exit(main())
