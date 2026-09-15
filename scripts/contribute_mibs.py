#!/usr/bin/env python3
#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Offer a MIB set to this distribution, as an issue or as a pull request.

Two people run this and they are not the same person. One has their own MIBs
mounted beside the published corpus, is not going to write a pull request, and
has a module this distribution is behind on or has never carried. The other is
the freshness process, sweeping a MIB collection somebody published, and can
put what it finds straight into a branch. Both need the same three answers,
which is why this is one script: which modules are worth offering, what
evidence says so, and has somebody offered them already.

The evidence is a build's own. ``mibcorpus`` resolves a MIB directory against
the published corpus by the rule the corpus is built with -- the newest
MODULE-IDENTITY revision wins, configured order breaks a tie -- and
``report.json`` records what it decided: the pairs both sets hold under
``shadowed``, and where every published module came from under ``provenance``.
Two kinds of module come out of that, and a scan of a collection turns up both:

    a better copy    both sets hold it, and the offered copy won on revision
    not carried      no namespace here holds it at all

Three things it deliberately does not do. It does not treat a copy that won on
source order as better, unless asked with ``--include-differing``: two copies
of one name are as often two different modules as two revisions of one. It
does not send anything without both ``--submit`` and ``--yes``, because a MIB
from somebody's tree can be a vendor file under a licence that forbids
redistribution, or a file carrying site detail in its comments. And it writes
no absolute path into an issue, because a path from this machine names this
machine.

Before submitting it searches the tracker for what is already open, so the
second report of a module is left out rather than filed. An unattended run
should add ``--require-duplicate-check``, which stops rather than filing
blind when the search cannot run.

Revisions and digests are read with pysmi, which produced the report this
reads and is therefore installed wherever this runs. This repository keeps no
second implementation of a rule pysmi publishes.

Usage:

    # Resolve a MIB directory against a published corpus. --emit=asn1 is not
    # optional: the pass that stages it is the pass that records what resolved.
    mibcorpus --resolve-namespace=vendor:corpus:./asn1 \\
        --namespace=vendor:local:./my-mibs \\
        --output-directory=./out --emit=asn1 --emit=report

    # What would be offered, written to ./contribution and sent nowhere.
    python3 scripts/contribute_mibs.py --report=out/report.json

    # File it from your browser, under your own account, with no token here.
    python3 scripts/contribute_mibs.py --report=out/report.json --submit=url --yes

    # File it with the GitHub CLI, which must already be authenticated.
    python3 scripts/contribute_mibs.py --report=out/report.json --submit=gh --yes

    # The freshness process: commit the modules and open the pull request.
    python3 scripts/contribute_mibs.py --report=out/report.json \\
        --submit=pr --yes --checkout=../mibs \\
        --vendor=example --publisher=example-mibs
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
import urllib.error
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
MARKER = "<!-- mib-contribution v1 -->"

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

#: The verdict for a module no namespace but the scanned one holds. Not a
#: precedence decision at all: nothing here was passed over, because there was
#: nothing here.
NOT_CARRIED = "not carried"


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
    """One module worth sending here: a better copy of one, or one not carried."""

    #: Module name, which is the name the corpus publishes it under.
    module: str
    #: What this module is. See :py:data:`VERDICTS` and :py:data:`NOT_CARRIED`.
    verdict: str
    #: The precedence rule that decided, in pysmi's words. Empty for a module
    #: nothing decided, which is one no other namespace holds.
    precedence: str
    #: The copy that won, which is the scanned set's.
    local: Copy
    #: The copy that was passed over. ``None`` for a module this distribution
    #: does not carry, where there was none.
    published: Copy | None
    #: The scanned copy's ASN.1 text, which is what the issue carries.
    text: str
    #: The scanned copy's bytes as they are on disk, which is what the archive
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
            "published": self.published.as_dict() if self.published else None,
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


def package_directory(source: str) -> Path | None:
    """The directory a ``package:`` namespace reads, when it is importable here.

    A manifest names the standard modules as ``package:pysmi.mibs.asn1`` rather
    than as a path. The modules are still files, and whether this distribution
    carries a module is a question about all of them.
    """
    try:
        spec = importlib.util.find_spec(source.split(":", 1)[1])
    except (ImportError, ValueError):
        return None

    if spec is None:
        return None

    for location in spec.submodule_search_locations or ():
        return Path(location)

    if spec.origin:
        return Path(spec.origin).parent

    return None


def carried_names(report: dict, mine: tuple[str, ...]) -> set[str]:
    """Every module name the namespaces that are not the scanned set hold.

    ``shadowed`` cannot answer this. It records the modules more than one
    namespace held a *differing* copy of, so it is silent about a module only
    one namespace has, which is exactly the module worth contributing. The
    answer is the file names in the other namespaces: the published corpus is
    a flat tree named for the modules it carries.

    Both the name and the stem are counted, so a collection storing
    ``IF-MIB.mib`` beside a corpus storing ``IF-MIB`` does not read as a module
    this distribution lacks.
    """
    names: set[str] = set()

    for namespace in report.get("namespaces", ()):
        if str(namespace.get("name", "")) in mine:
            continue

        source = str(namespace.get("source", ""))

        if source.startswith("package:"):
            directory = package_directory(source)
        elif source:
            directory = Path(source)
        else:
            continue

        if directory is None or not directory.is_dir():
            continue

        for found in directory.rglob("*"):
            if found.is_file():
                names.add(found.name)
                names.add(found.stem)

    return names


def require_resolution(report: dict) -> None:
    """Refuse a report that records no resolution, which reads as nothing to offer.

    ``shadowed`` and ``provenance`` are written by the pass that stages the
    ASN.1 tree. A build asked for ``--emit=report`` alone runs no such pass and
    writes both keys empty, which is indistinguishable here from a MIB set with
    nothing in it this distribution wants. Saying which one it is costs a line;
    reading an empty issue costs a reporter their patience.
    """
    if report.get("shadowed") or report.get("provenance"):
        return

    raise Refused(
        "this report records no resolution at all: `shadowed` and `provenance` "
        "are both empty. They are written by the pass that stages the ASN.1, so "
        "a build asked for `--emit=report` alone does not fill them in. Re-run "
        "`mibcorpus` with `--emit=asn1 --emit=report`."
    )


def collect(
    report: dict,
    mine: tuple[str, ...],
    *,
    include_differing: bool = False,
    skip_new: bool = False,
    only: tuple[str, ...] = (),
) -> list[Finding]:
    """Every module in the report worth sending to this distribution.

    Two kinds, and a scan of a MIB collection turns up both. A module this
    distribution carries an older copy of, which the build decided by reading
    both; and a module it does not carry at all, which is the larger half of
    what a collection has to offer.

    Args:
        report: a parsed ``report.json`` from a build that resolved a MIB
            directory against the published corpus.
        mine: the namespaces holding the MIBs being offered. Everything else
            in the report is this distribution.
        include_differing: also report a module the scanned copy won by source
            order rather than by revision. Off by default: two copies of one
            name are often two different modules rather than two revisions of
            one, and the rule cannot tell them apart.
        skip_new: leave out the modules this distribution does not carry.
        only: report just these modules, when given.

    Returns:
        One finding per module, module name order.
    """
    roots = namespace_roots(report)
    missing = [x for x in mine if x not in roots]

    if missing:
        raise Refused(
            f"the report holds no namespace named {', '.join(missing)}. "
            f"It holds {', '.join(sorted(roots)) or 'none with a directory'}. "
            "Name the one your MIBs are in with --namespace."
        )

    found = better_copies(report, mine, roots, include_differing=include_differing)

    if not skip_new:
        found += not_carried(report, mine, roots)

    if only:
        found = [x for x in found if x.module in only]

    return sorted(found, key=lambda x: x.module)


def read_module(module: str, path: str) -> tuple[str, bytes]:
    """The MIB a report resolved, refusing what this machine cannot read.

    A report names what the build read. Run somewhere else, or after the
    sources moved, it names a file that is not there, and an issue offering a
    module whose text nobody can attach is worse than no issue.
    """
    on_disk = local_path(path)

    if on_disk is None or not on_disk.is_file():
        raise Refused(
            f"{module} was resolved from {path}, which is not a file here. "
            "Run this on the machine the build ran on, and before the sources "
            "move."
        )

    return read_source(on_disk)


def better_copies(
    report: dict,
    mine: tuple[str, ...],
    roots: dict[str, str],
    *,
    include_differing: bool,
) -> list[Finding]:
    """The modules both sets hold, where the scanned copy is the one that won."""
    revision_of, source_digest, _ = pysmi_reader()
    provenance = report.get("provenance", {})
    found = []

    for module, record in sorted(report.get("shadowed", {}).items()):
        used = str(record.get("used", ""))

        if namespace_of(used, roots) not in mine:
            continue

        precedence = str(record.get("precedence", ""))

        if precedence != PRECEDENCE_NEWEST and not include_differing:
            continue

        passed = [
            (x, namespace_of(x, roots))
            for x in record.get("shadowed", ())
            if namespace_of(x, roots) not in mine
        ]

        if not passed:
            continue

        text, raw = read_module(module, used)
        their_path, their_namespace = passed[0]
        theirs_on_disk = local_path(their_path)
        their_text = ""

        if theirs_on_disk is not None and theirs_on_disk.is_file():
            their_text, _ = read_source(theirs_on_disk)

        found.append(
            Finding(
                module=module,
                verdict=VERDICTS.get(precedence, "differs"),
                precedence=precedence,
                local=Copy(
                    namespace=namespace_of(used, roots),
                    file=relative_file(used, roots[namespace_of(used, roots)]),
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


def not_carried(
    report: dict, mine: tuple[str, ...], roots: dict[str, str]
) -> list[Finding]:
    """The modules the scanned set holds and no other namespace does.

    Read from ``provenance``, which names the namespace every published module
    came from, against the file names the other namespaces hold. A module the
    build attributed elsewhere is one this distribution already has, whether
    or not the two copies agree.
    """
    revision_of, source_digest, _ = pysmi_reader()
    carried = carried_names(report, mine)
    found = []

    for module, origin in sorted(report.get("provenance", {}).items()):
        namespace = str(origin.get("namespace", ""))

        if namespace not in mine or module in carried:
            continue

        root = roots.get(namespace, "")
        file = str(origin.get("file", "")) or module
        text, raw = read_module(module, str(Path(root) / file))

        found.append(
            Finding(
                module=module,
                verdict=NOT_CARRIED,
                precedence="",
                local=Copy(
                    namespace=namespace,
                    file=file,
                    revision=revision_of(text) or "",
                    digest=str(origin.get("digest", "")) or source_digest(text),
                    size=len(raw),
                ),
                published=None,
                text=text,
                raw=raw,
            )
        )

    return found


def title_for(findings: list[Finding]) -> str:
    """What the issue is called, from what it holds."""
    if len(findings) == 1:
        one = findings[0]

        if one.verdict == NOT_CARRIED:
            return f"{one.module}: a module this distribution does not carry"

        if one.verdict == "newer" and one.published:
            return (
                f"{one.module}: a newer copy "
                f"({describe_revision(one.local.revision)}, against "
                f"{describe_revision(one.published.revision)} published)"
            )

        return f"{one.module}: a copy that differs from the published one"

    named = ", ".join(x.module for x in findings[:3])
    rest = f" and {len(findings) - 3} more" if len(findings) > 3 else ""
    new = len([x for x in findings if x.verdict == NOT_CARRIED])

    if new == len(findings):
        return f"{new} modules this distribution does not carry: {named}{rest}"

    return f"{len(findings)} modules to add or replace: {named}{rest}"


def payload(
    findings: list[Finding], inline: set[str], version: str, archive: str
) -> dict:
    """The report as data, for an agent picking the issue up.

    The same facts as the table above it, in the form that does not have to be
    parsed out of prose: a pull request for one of these modules needs the
    name, the two revisions and the digest of the text it should carry.
    """
    return {
        "report": "mib-contribution v1",
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
    sources: bool = True,
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
        sources: whether the body accounts for the ASN.1 at all. A pull
            request carries it in the diff, where it can be reviewed line by
            line, so its body neither inlines it nor names an archive.
    """
    new = [x for x in findings if x.verdict == NOT_CARRIED]
    better = [x for x in findings if x.verdict != NOT_CARRIED]
    out = [
        f"### {len(findings)} module{'s' if len(findings) != 1 else ''} for this "
        "distribution",
        "",
        MARKER,
        "",
        "`mibcorpus` resolved a MIB directory against this distribution's published",
        "corpus, by the rule the corpus is built with. What it found:",
        "",
    ]

    if better:
        out += [
            f"- **{len(better)} module{'s' if len(better) != 1 else ''} "
            "published here in an older copy.** The build read both and took the "
            "one below.",
        ]

    if new:
        out += [
            f"- **{len(new)} module{'s' if len(new) != 1 else ''} this "
            "distribution does not carry.**",
        ]

    out += [
        "",
        "| module | offered | published | what decided |",
        "| --- | --- | --- | --- |",
    ]

    for one in findings:
        published = (
            describe_revision(one.published.revision)
            if one.published
            else "not carried"
        )
        out.append(
            f"| `{one.module}` | {describe_revision(one.local.revision)} "
            f"| {published} | {one.precedence or 'nothing to compare'} |"
        )

    out += [
        "",
        "#### What this issue still needs",
        "",
        "A module is merged here with its provenance: `mib-sources.json` records a",
        "publisher for every module under `src/`, so that the next revision is",
        "noticed by a build rather than by a reader. Fill these in:",
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

    outside = [x for x in findings if x.module not in inline] if sources else []

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
            "| | offered | published |",
            "| --- | --- | --- |",
            f"| revision | {describe_revision(one.local.revision)} "
            f"| {describe_revision(one.published.revision) if one.published else 'not carried'} |",
            f"| bytes | {one.local.size:,} | {one.published.size:,} |"
            if one.published
            else f"| bytes | {one.local.size:,} | |",
            f"| digest | `{one.local.digest}` "
            f"| `{one.published.digest or 'not read'}` |"
            if one.published
            else f"| digest | `{one.local.digest}` | |",
            "",
        ]

        if sources and one.module in inline:
            out += [
                f"<details><summary>{one.module}, as it was offered</summary>",
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
        "<sub>Written by `scripts/contribute_mibs.py` from a `mibcorpus` report.",
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


def compose(
    findings: list[Finding],
    version: str,
    archive: str,
    gist: str = "",
    *,
    sources: bool = True,
) -> str:
    """The issue body, with as many modules inlined as it holds."""
    empty: set[str] = set()

    if not sources:
        return render(
            findings,
            inline=empty,
            version=version,
            archive=archive,
            gist=gist,
            sources=False,
        )

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


#: What a duplicate search reads before it stops. GitHub returns 100 results a
#: page, and a tracker with more than this many contribution issues open is one
#: where a maintainer, not this script, should be deciding what is a duplicate.
DUPLICATE_PAGES = 3

#: How many modules are worth one search each, over and above the one search
#: that finds every issue this tool has filed. The search API allows ten
#: unauthenticated requests a minute, and a report of 200 modules would spend
#: that in seconds.
DUPLICATE_SEARCHES = 8

#: What a contribution issue says about itself, in the form a search matches.
#: The marker is an HTML comment, and GitHub's search tokenises it down to
#: this.
MARKER_TEXT = "mib-contribution"


def search_issues(repository: str, query: str, pages: int = 1) -> list[dict]:
    """Issues and pull requests matching a GitHub search.

    Through `gh` where it is installed, which spends its authentication and
    the rate limit that comes with it, and over the public API otherwise.
    ``GITHUB_TOKEN`` is used when it is set, for the same reason.

    Raises:
        Refused: when neither transport could answer.
    """
    results: list[dict] = []

    for page in range(1, pages + 1):
        if shutil.which("gh"):
            answer = run_gh(
                [
                    "api",
                    "-X",
                    "GET",
                    "search/issues",
                    "-f",
                    f"q={query}",
                    "-f",
                    "per_page=100",
                    "-f",
                    f"page={page}",
                ]
            )
        else:
            request = urllib.request.Request(
                "https://api.github.com/search/issues?"
                + urllib.parse.urlencode({"q": query, "per_page": 100, "page": page}),
                headers={
                    "Accept": "application/vnd.github+json",
                    "User-Agent": "pysnmp-mibs-contribute",
                },
            )
            token = os.environ.get("GITHUB_TOKEN", "")

            if token:
                request.add_header("Authorization", f"Bearer {token}")

            try:
                # The URL is this module's own constant with a query string
                # on it; nothing the caller passes decides the scheme.
                with urllib.request.urlopen(  # noqa: S310
                    request, timeout=30
                ) as response:
                    answer = response.read().decode("utf-8")
            except (urllib.error.URLError, OSError, TimeoutError) as exc:
                raise Refused(f"the GitHub search could not be reached: {exc}") from exc

        try:
            found = json.loads(answer).get("items", [])
        except json.JSONDecodeError as exc:
            raise Refused(f"the GitHub search answered something else: {exc}") from exc

        results += found

        if len(found) < 100:
            break

    return results


def modules_named(issue: dict) -> set[str]:
    """Which modules an existing issue is about.

    An issue this tool filed carries its findings as JSON, which names them
    exactly. One filed by hand carries whatever its author wrote, so the title
    is read too, for the module-shaped words in it.
    """
    body = str(issue.get("body") or "")
    named = set(re.findall(r'"module":\s*"([A-Za-z0-9][\w-]*)"', body))

    return named | set(
        re.findall(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b", str(issue.get("title") or ""))
    )


def existing_contributions(
    repository: str, modules: list[str]
) -> dict[str, list[dict]]:
    """The issues and pull requests already offering each of *modules*.

    One search finds everything this tool has filed, whoever filed it, because
    every issue it writes carries the same marker. A short report then spends a
    search per module as well, which is what finds the issue somebody opened by
    hand before this tool existed.

    Returns:
        Module name to the issues naming it, newest first. Modules nothing
        names are absent rather than empty.
    """
    found: dict[str, list[dict]] = {}
    wanted = set(modules)

    for issue in search_issues(
        repository, f'repo:{repository} "{MARKER_TEXT}" in:body', DUPLICATE_PAGES
    ):
        for module in modules_named(issue) & wanted:
            found.setdefault(module, []).append(issue)

    if len(modules) <= DUPLICATE_SEARCHES:
        for module in modules:
            for issue in search_issues(
                repository, f'repo:{repository} "{module}" in:title,body'
            ):
                if issue["number"] not in {x["number"] for x in found.get(module, ())}:
                    found.setdefault(module, []).append(issue)

    return found


def describe_duplicate(issue: dict) -> str:
    """One existing issue, as the line that says not to file another."""
    kind = "pull request" if issue.get("pull_request") else "issue"
    state = str(issue.get("state", "open"))

    return f"{kind} #{issue['number']} ({state}): {issue.get('title', '')}"


def without_duplicates(
    findings: list[Finding], repository: str, *, required: bool
) -> list[Finding]:
    """The findings nothing has been filed about yet, and a note about the rest.

    An open issue or pull request naming a module is reason not to file a
    second one: the module is already somebody's to deal with, and a duplicate
    costs a maintainer the time this tool exists to save. A closed one is not,
    since it was closed for a reason nothing here can read, so the module is
    reported again with the old issue named beside it.

    Args:
        findings: what would be reported.
        repository: the repository to search.
        required: whether a search that cannot run stops the submission. An
            unattended run should say yes: filing duplicates every month is
            worse than filing nothing until the search works again.
    """
    try:
        existing = existing_contributions(repository, [x.module for x in findings])
    except Refused as refusal:
        if required:
            raise

        sys.stdout.write(
            f"The duplicate check could not run ({refusal}). Submitting anyway; "
            "check the tracker yourself.\n\n"
        )
        return findings

    keep = []

    for one in findings:
        open_ones = [
            x for x in existing.get(one.module, ()) if x.get("state") == "open"
        ]

        if open_ones:
            sys.stdout.write(
                f"{one.module} is already open here, so it is left out:\n"
                + "".join(f"  {describe_duplicate(x)}\n" for x in open_ones)
            )
            continue

        closed = existing.get(one.module, [])

        if closed:
            sys.stdout.write(
                f"{one.module} was reported before and closed. Reporting it "
                "again:\n" + "".join(f"  {describe_duplicate(x)}\n" for x in closed)
            )

        keep.append(one)

    if len(keep) != len(findings):
        sys.stdout.write("\n")

    return keep


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


def git(checkout: Path, *arguments: str) -> str:
    """One git command in the checkout, with its failure reported as its own message."""
    finished = subprocess.run(
        ["git", "-C", str(checkout), *arguments],
        capture_output=True,
        text=True,
        check=False,
    )

    if finished.returncode:
        raise Refused(
            f"`git {' '.join(arguments)}` exited {finished.returncode}: "
            f"{finished.stderr.strip() or 'no error text'}"
        )

    return finished.stdout.strip()


def require_checkout(checkout: Path) -> Path:
    """The checkout a pull request can be written into, or the reason it cannot.

    A pull request writes MIBs into ``src/vendor/`` and provenance into
    ``mib-sources.json``, so it needs this repository rather than any
    repository. It also needs a clean tree: the commit it makes is `git add` of
    the paths it wrote, and a tree carrying somebody's unfinished work would
    have that reviewed as part of a MIB import.
    """
    resolved = checkout.resolve()

    if (
        not (resolved / "src" / "vendor").is_dir()
        or not (resolved / "mib-sources.json").is_file()
    ):
        raise Refused(
            f"{resolved} is not a checkout of the MIB distribution: --submit=pr "
            "writes into src/vendor/ and mib-sources.json, and neither is here. "
            "Clone pysnmp/mibs and pass --checkout."
        )

    if git(resolved, "status", "--porcelain"):
        raise Refused(
            f"{resolved} has uncommitted changes. --submit=pr commits what it "
            "writes, and a dirty tree would go into that commit. Commit or stash "
            "first."
        )

    return resolved


def record_provenance(checkout: Path, paths: list[str], publisher: str) -> Path | None:
    """Name the publisher of every module this pull request adds.

    ``mib-sources.json`` is what lets a build notice the next revision of a
    module rather than waiting for somebody to report it again, which is the
    whole of why the monthly sweep exists. A pull request that adds a module
    without it adds a module nothing will ever check.

    Returns:
        The manifest, when it was changed. ``None`` when no publisher was
        named, which leaves the question for review.
    """
    if not publisher:
        return None

    manifest = checkout / "mib-sources.json"
    parsed = json.loads(manifest.read_text(encoding="utf-8"))

    if publisher not in parsed.get("publishers", {}):
        raise Refused(
            f"mib-sources.json defines no publisher {publisher!r}. It defines "
            f"{', '.join(sorted(parsed.get('publishers', {})))}. Add the "
            "publisher in its own pull request first, or leave --publisher off "
            "and answer it in review."
        )

    for path in paths:
        parsed.setdefault("modules", {})[path] = {"publisher": publisher}

    manifest.write_text(
        json.dumps(parsed, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    return manifest


def commit_subject(findings: list[Finding], vendor: str) -> str:
    """The commit's first line, in the form this repository writes them.

    ``feat`` for modules the corpus gains and ``fix`` for copies it replaces,
    because that is what the release notes are generated from: a module added
    is a feature of the distribution and a module refreshed is a repair of one.
    """
    new = [x for x in findings if x.verdict == NOT_CARRIED]
    better = [x for x in findings if x.verdict != NOT_CARRIED]

    if new and not better:
        if len(new) == 1:
            return (
                f"feat({vendor}): add {new[0].module}, which the corpus does not carry"
            )

        return f"feat({vendor}): add {len(new)} modules the corpus does not carry"

    if better and not new:
        if len(better) == 1:
            return f"fix({vendor}): refresh {better[0].module} from a newer publication"

        return f"fix({vendor}): refresh {len(better)} modules from a newer publication"

    return (
        f"feat({vendor}): add {len(new)} module{'s' if new[1:] else ''} and "
        f"refresh {len(better)} more from one collection"
    )


def commit_message(submission: Submission, vendor: str) -> str:
    """The commit: what changed, and what a build read to decide it."""
    new = [x for x in submission.findings if x.verdict == NOT_CARRIED]
    better = [x for x in submission.findings if x.verdict != NOT_CARRIED]
    lines = [commit_subject(submission.findings, vendor), ""]

    if better:
        lines += [
            *textwrap.wrap(
                f"{len(better)} module{'s' if better[1:] else ''} this "
                f"distribution publishes an older copy of. A build resolved the "
                f"two against each other and took the copy here, on the rule the "
                f"corpus is built with: the newest MODULE-IDENTITY revision "
                f"wins, and configured order breaks a tie.",
                width=76,
            ),
            "",
        ]

    if new:
        lines += [
            *textwrap.wrap(
                f"{len(new)} module{'s' if new[1:] else ''} the corpus has "
                f"never carried, held by the same collection.",
                width=76,
            ),
            "",
        ]

    for one in submission.findings:
        published = (
            describe_revision(one.published.revision)
            if one.published
            else "not carried"
        )
        lines.append(
            f"    {one.module:<40} {describe_revision(one.local.revision)}  "
            f"was {published}"
        )

    return "\n".join(lines) + "\n"


def submit_pr(
    submission: Submission,
    options: argparse.Namespace,
    version: str,
) -> str:
    """Write the MIBs into a checkout, commit them on a branch, and open the pull request.

    This is the half the freshness process uses. A scan that already knows the
    publisher it read from can put the modules where they belong and say so,
    which leaves review the question worth reviewing: whether the text is
    right.
    """
    checkout = require_checkout(Path(options.checkout))
    branch = options.branch or f"mibs/{submission.slug.lower()}"
    vendor = options.vendor

    if not vendor:
        raise Refused(
            "--submit=pr needs --vendor, which is the directory under "
            "src/vendor/ the modules belong in. Nothing in a MIB says which "
            "vendor's tree it is filed under here."
        )

    started = git(checkout, "rev-parse", "--abbrev-ref", "HEAD")
    git(checkout, "switch", "--create", branch)
    written = []

    for one in submission.findings:
        path = checkout / "src" / "vendor" / vendor / one.module
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(one.raw)
        written.append(f"src/vendor/{vendor}/{one.module}")

    manifest = record_provenance(checkout, written, options.publisher)
    message = submission.directory / "commit.txt"
    message.write_text(commit_message(submission, vendor), encoding="utf-8")

    git(checkout, "add", *written, *(["mib-sources.json"] if manifest else []))
    git(checkout, "commit", "--file", str(message))

    submission.body = compose(submission.findings, version, "", sources=False)
    body = submission.directory / "pull-request.md"
    body.write_text(submission.body, encoding="utf-8")

    git(checkout, "push", "--set-upstream", "origin", branch)
    url = run_gh(
        [
            "pr",
            "create",
            "--repo",
            options.repository,
            "--head",
            branch,
            "--base",
            options.base,
            "--title",
            submission.title,
            "--body-file",
            str(body),
        ]
    ).splitlines()[-1]

    git(checkout, "switch", started)

    return url


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
        "--skip-new",
        action="store_true",
        help="report only better copies of modules this distribution carries",
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
        choices=("none", "url", "gh", "pr"),
        default="none",
        help="none writes the files and sends nothing; url prints a prefilled "
        "GitHub issue URL for you to review and post; gh files the issue with "
        "the GitHub CLI; pr commits the MIBs to a checkout and opens a pull "
        "request",
    )
    parser.add_argument(
        "--checkout",
        type=Path,
        default=Path(),
        help="with --submit=pr, the clone of the distribution to commit into",
    )
    parser.add_argument(
        "--vendor",
        default="",
        help="with --submit=pr, the src/vendor/ directory the modules belong in",
    )
    parser.add_argument(
        "--publisher",
        default="",
        help="with --submit=pr, the mib-sources.json publisher these came from",
    )
    parser.add_argument(
        "--branch",
        default="",
        help="with --submit=pr, the branch to commit on (default: mibs/<slug>)",
    )
    parser.add_argument(
        "--base",
        default="main",
        help="with --submit=pr, the branch to open the pull request against",
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
        "--check-duplicates",
        action="store_true",
        help="search the repository for what is already reported, without submitting",
    )
    parser.add_argument(
        "--allow-duplicates",
        action="store_true",
        help="report a module even where an issue for it is open",
    )
    parser.add_argument(
        "--require-duplicate-check",
        action="store_true",
        help="submit nothing if the duplicate search cannot run. For unattended runs",
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

    require_resolution(parsed)

    findings = collect(
        parsed,
        tuple(options.namespace) or ("local",),
        include_differing=options.include_differing,
        skip_new=options.skip_new,
        only=tuple(options.module),
    )

    if not findings:
        sys.stdout.write(
            "Every module in this report is one this distribution already "
            "carries, in a copy the build preferred. Nothing to report.\n"
        )
        return 0

    if (options.submit != "none" or options.check_duplicates) and not (
        options.allow_duplicates
    ):
        findings = without_duplicates(
            findings, options.repository, required=options.require_duplicate_check
        )

        if not findings:
            sys.stdout.write(
                "Everything in this report is already open here. Nothing to file.\n"
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
                slug="contribution",
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
            "--submit=url --yes to post it from your browser, --submit=gh "
            "--yes to file it with the GitHub CLI, or --submit=pr --yes to open "
            "a pull request from a checkout.\n"
        )
        return 0

    if not options.yes:
        raise Refused(
            "--submit publishes these MIB sources, in a public issue or in a "
            "pull request. Read the issue.md files above, then add --yes."
        )

    labels = tuple(options.label)
    sys.stdout.write("\n")

    for submission in submissions:
        if options.submit == "pr":
            submission.url = submit_pr(submission, options, version)
            sys.stdout.write(f"{submission.url}\n")
            continue

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
