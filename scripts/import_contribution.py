#!/usr/bin/env python3
#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Turn a `mibcontribute` bundle into a pull request against this repository.

`mibcontribute` is pysmi's tool, and it stops where a contributor's knowledge
stops: it reports the modules this distribution publishes an older copy of and
the modules it does not carry, and writes them out as an issue and an archive.
What it cannot know is where a module belongs here -- which directory under
`src/vendor/` is that vendor's, and which publisher in `mib-sources.json` the
files came from -- because nothing in a MIB says either. This does that half,
which is the half that needs this repository rather than any repository.

The freshness process is the caller this exists for. It scans a published MIB
collection, knows the publisher it read from because it chose it, and can put
what it found into a branch rather than into prose:

    mibcontribute --corpus=./asn1 --output-directory=./found ./collection
    uv run python scripts/import_contribution.py --contribution=found \\
        --vendor=example --publisher=example-mibs --submit

A person doing the same by hand runs it without `--submit` and reads the
branch before pushing it.

The bundle is the interface, not a Python import. `mibcontribute` writes
`findings.json` and `mibs/<MODULE>` beside each other, this reads them, and
nothing here re-derives a decision pysmi made: which copy is better was
settled by the scan, with the same function a corpus build uses.

Usage:

    uv run python scripts/import_contribution.py --contribution=<DIRECTORY> \\
        --vendor=<VENDOR> [--publisher=<ID>] [--issue=<N>] [--submit]
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

#: What `mibcontribute` calls the modules it found nothing here carries.
NOT_CARRIED = "not carried"

#: What a module name may be, in a bundle that arrived from somewhere else.
#: RFC 2578 Section 3.1 allows letters, digits and hyphens; the underscore is
#: here because vendors use it. What this excludes is the point: a bundle is
#: data, this reads a file path out of it, and "../" in that path would read
#: and then commit a file from somewhere else entirely.
MODULE_NAME = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$")


class Refused(Exception):
    """Something this will not do, phrased for the person who asked."""


def read_bundle(directory: Path) -> tuple[list[dict], dict[str, bytes]]:
    """The findings a `mibcontribute` run wrote, and the MIBs beside them.

    Args:
        directory: what `mibcontribute --output-directory` named.

    Returns:
        The findings, and each module's bytes as the scan read them.

    Raises:
        Refused: the directory is not a bundle, or a module it names is not
            beside it.
    """
    findings = directory / "findings.json"

    if not findings.is_file():
        raise Refused(
            f"{findings} is not there. Produce a bundle with `mibcontribute "
            f"--output-directory={directory} <your MIBs>` first."
        )

    parsed = json.loads(findings.read_text(encoding="utf-8"))
    modules = parsed.get("modules", [])
    sources = {}

    for one in modules:
        module = str(one["module"])
        sources[module] = bundle_file(directory, module).read_bytes()

    if not modules:
        raise Refused(f"{findings} holds no modules, so there is nothing to import.")

    return modules, sources


def bundle_file(directory: Path, module: str) -> Path:
    """The file a bundle holds for one module, refusing one that is not in it.

    Everything this reads it goes on to commit, and with ``--submit`` to push.
    A bundle is a directory somebody sends: it can name a module
    ``../../id_rsa`` or leave a symbolic link where the MIB should be, and
    either would have this publish a file nobody meant to publish.

    Args:
        directory: the bundle.
        module: the module name, as ``findings.json`` gives it.

    Returns:
        The file to read.

    Raises:
        Refused: the name is not a module name, the file is not there, or it is
            not inside the bundle.
    """
    if not MODULE_NAME.match(module):
        raise Refused(
            f"{module!r} is not a MIB module name. findings.json names the files "
            "this reads, so a name that is a path is refused rather than followed."
        )

    mibs = (directory / "mibs").resolve()
    path = directory / "mibs" / module

    if path.is_symlink():
        raise Refused(
            f"{path} is a symbolic link. A bundle carries MIB text, and what "
            "this reads it commits."
        )

    if not path.is_file():
        raise Refused(
            f"{directory / 'findings.json'} names {module}, which is not at "
            f"{path}. The bundle is incomplete; run the scan again."
        )

    if not path.resolve().is_relative_to(mibs):
        raise Refused(f"{path} is not inside {mibs}.")

    return path


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
    """The checkout this can commit into, or the reason it cannot.

    It writes MIBs into ``src/vendor/`` and provenance into
    ``mib-sources.json``, so it needs this repository rather than any
    repository. It also needs a clean tree: the commit it makes is a `git add`
    of the paths it wrote, and a tree carrying somebody's unfinished work would
    have that reviewed as part of a MIB import.
    """
    resolved = checkout.resolve()

    if (
        not (resolved / "src" / "vendor").is_dir()
        or not (resolved / "mib-sources.json").is_file()
    ):
        raise Refused(
            f"{resolved} is not a checkout of this distribution: an import writes "
            "into src/vendor/ and mib-sources.json, and neither is here."
        )

    # Tracked changes only. The commit adds the paths this wrote by name, so an
    # untracked file cannot reach it -- and the bundle being imported is often
    # an untracked directory right here, which would otherwise make the
    # documented command refuse itself. What is worth refusing is a modified
    # file, which switching branches carries onto the new one.
    if git(resolved, "status", "--porcelain", "--untracked-files=no"):
        raise Refused(
            f"{resolved} has uncommitted changes to tracked files. An import "
            "commits what it writes, and those changes would follow it onto the "
            "branch. Commit or stash first."
        )

    return resolved


def require_publisher(checkout: Path, publisher: str) -> None:
    """Refuse a publisher the manifest does not define, before anything is written.

    Args:
        checkout: the clone being imported into.
        publisher: the publisher named on the command line, or an empty string.

    Raises:
        Refused: the publisher is not one ``mib-sources.json`` defines, which is
            what ``scripts/update_vendor_mibs.py --validate`` rejects in CI.
    """
    if not publisher:
        return

    defined = json.loads(
        (checkout / "mib-sources.json").read_text(encoding="utf-8")
    ).get("publishers", {})

    if publisher not in defined:
        raise Refused(
            f"mib-sources.json defines no publisher {publisher!r}. It defines "
            f"{', '.join(sorted(defined))}. Add the publisher in its own pull "
            "request first, or leave --publisher off and answer it in review."
        )


def record_provenance(checkout: Path, paths: list[str], publisher: str) -> bool:
    """Name the publisher of every module this import adds.

    ``mib-sources.json`` is what lets a build notice the next revision of a
    module rather than waiting for somebody to report it again, which is the
    whole of why the monthly sweep exists. A module added without it is a
    module nothing will ever check.

    Returns:
        Whether the manifest was written.

    Raises:
        Refused: the publisher is not one the manifest defines, which is what
            ``scripts/update_vendor_mibs.py --validate`` rejects in CI.
    """
    if not publisher:
        return False

    manifest = checkout / "mib-sources.json"
    parsed = json.loads(manifest.read_text(encoding="utf-8"))
    require_publisher(checkout, publisher)

    for path in paths:
        parsed.setdefault("modules", {})[path] = {"publisher": publisher}

    manifest.write_text(
        json.dumps(parsed, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    return True


def describe_revision(revision: str) -> str:
    """A normalised ``YYYYMMDDHHMMZ`` revision, as a date to read."""
    if not revision or len(revision) < 8:
        return "none"

    return f"{revision[0:4]}-{revision[4:6]}-{revision[6:8]}"


def published_revision(finding: dict) -> str:
    """What this distribution publishes for a module, as a date or as nothing."""
    published = finding.get("published")

    if not published:
        return "not carried"

    return describe_revision(str(published.get("revision", "")))


def title_for(modules: list[dict], vendor: str) -> str:
    """The commit subject and the pull request title.

    ``feat`` for modules the corpus gains and ``fix`` for copies it replaces,
    because that is what the release notes are generated from: a module added
    is a feature of the distribution and a module refreshed is a repair of one.
    """
    new = [x for x in modules if x.get("verdict") == NOT_CARRIED]
    better = [x for x in modules if x.get("verdict") != NOT_CARRIED]

    if new and not better:
        if len(new) == 1:
            return (
                f"feat({vendor}): add {new[0]['module']}, which the corpus does "
                "not carry"
            )

        return f"feat({vendor}): add {len(new)} modules the corpus does not carry"

    if better and not new:
        if len(better) == 1:
            return (
                f"fix({vendor}): refresh {better[0]['module']} from a newer publication"
            )

        return f"fix({vendor}): refresh {len(better)} modules from a newer publication"

    return (
        f"feat({vendor}): add {len(new)} module{'s' if new[1:] else ''} and refresh "
        f"{len(better)} more from one collection"
    )


def table(modules: list[dict]) -> list[str]:
    """What is being imported, as the rows both the commit and the body carry."""
    return [
        f"| `{x['module']}` | {describe_revision(str(x['offered']['revision']))} "
        f"| {published_revision(x)} | {x.get('precedence') or 'nothing to compare'} |"
        for x in modules
    ]


def commit_message(modules: list[dict], vendor: str, source: str) -> str:
    """The commit: what changed, and what decided it."""
    new = [x for x in modules if x.get("verdict") == NOT_CARRIED]
    better = [x for x in modules if x.get("verdict") != NOT_CARRIED]
    lines = [title_for(modules, vendor), ""]

    if better:
        lines += [
            *textwrap.wrap(
                f"{len(better)} module{'s' if better[1:] else ''} this distribution "
                "publishes an older copy of. A scan resolved the two against each "
                "other and took the copy offered, on the rule the corpus is built "
                "with: the newest MODULE-IDENTITY revision wins, and configured "
                "order breaks a tie.",
                width=76,
            ),
            "",
        ]

    if new:
        lines += [
            *textwrap.wrap(
                f"{len(new)} module{'s' if new[1:] else ''} the corpus has never "
                "carried, from the same source.",
                width=76,
            ),
            "",
        ]

    for one in modules:
        lines.append(
            f"    {one['module']:<40} "
            f"{describe_revision(str(one['offered']['revision']))}  "
            f"was {published_revision(one)}"
        )

    lines += ["", f"Scanned with mibcontribute, pysmi {source}."]

    return "\n".join(lines) + "\n"


def pull_request_body(modules: list[dict], vendor: str, issue: str) -> str:
    """The pull request, which says what a reviewer cannot read off the diff.

    The ASN.1 is in the diff, so the body carries the evidence instead: what
    each module's revision was here, what it is now, and what decided that.
    """
    out = [
        f"Imported into `src/vendor/{vendor}/` from a `mibcontribute` scan.",
        "",
        "| module | imported | was | what decided |",
        "| --- | --- | --- | --- |",
        *table(modules),
        "",
        "Which copy is better was decided by `rank_by_revision`, the rule the",
        "corpus is built with, so each module here is one a build would prefer.",
        "",
    ]

    if issue:
        out += [f"Closes #{issue}", ""]

    return "\n".join(out)


def run_gh(arguments: list[str]) -> str:
    """One `gh` invocation, with its failure reported as its own message."""
    if not shutil.which("gh"):
        raise Refused(
            "--submit needs the GitHub CLI on PATH. Install it from "
            "https://cli.github.com/, or push the branch and open the pull "
            "request yourself."
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


def import_bundle(options: argparse.Namespace) -> int:
    """Write the modules into a branch, and open the pull request when asked."""
    modules, sources = read_bundle(options.contribution)
    checkout = require_checkout(options.checkout)
    branch = options.branch or f"mibs/{options.vendor}-contribution"

    # Before the branch and before any write: a refusal here would otherwise
    # leave the checkout on a new branch full of uncommitted MIBs.
    require_publisher(checkout, options.publisher)
    started = git(checkout, "rev-parse", "--abbrev-ref", "HEAD")

    git(checkout, "switch", "--create", branch)
    written = []

    for one in modules:
        module = str(one["module"])
        path = checkout / "src" / "vendor" / options.vendor / module
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(sources[module])
        written.append(f"src/vendor/{options.vendor}/{module}")

    manifest = record_provenance(checkout, written, options.publisher)
    message = options.contribution / "commit.txt"
    scanned = str(
        json.loads((options.contribution / "findings.json").read_text()).get(
            "pysmi", ""
        )
    )
    message.write_text(
        commit_message(modules, options.vendor, scanned), encoding="utf-8"
    )

    git(checkout, "add", *written, *(["mib-sources.json"] if manifest else []))
    git(checkout, "commit", "--file", str(message.resolve()))

    body = options.contribution / "pull-request.md"
    body.write_text(
        pull_request_body(modules, options.vendor, options.issue), encoding="utf-8"
    )

    sys.stdout.write(
        f"{len(written)} module(s) committed on {branch} in {checkout}:\n"
        + "".join(f"  {x}\n" for x in written)
    )

    if not options.publisher:
        sys.stdout.write(
            "\nNo --publisher was given, so mib-sources.json records nothing for "
            "these. A module with no publisher on record is one the monthly sweep "
            "cannot check; say where they came from in review.\n"
        )

    if not options.submit:
        sys.stdout.write(
            f"\nRead the branch, then push it and open the pull request with the "
            f"body in {body}, or re-run with --submit.\n"
        )
        git(checkout, "switch", started)
        return 0

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
            title_for(modules, options.vendor),
            "--body-file",
            str(body.resolve()),
        ]
    ).splitlines()[-1]
    git(checkout, "switch", started)
    sys.stdout.write(f"\n{url}\n")

    return 0


def main(argv: list[str] | None = None) -> int:
    """Import the bundle named on the command line."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--contribution",
        type=Path,
        required=True,
        help="the directory mibcontribute wrote: findings.json and mibs/",
    )
    parser.add_argument(
        "--vendor",
        required=True,
        help="the src/vendor/ directory these modules belong in",
    )
    parser.add_argument(
        "--publisher",
        default="",
        help="the mib-sources.json publisher they came from",
    )
    parser.add_argument(
        "--issue",
        default="",
        help="the issue this closes, named in the pull request body",
    )
    parser.add_argument(
        "--checkout",
        type=Path,
        default=Path(),
        help="the clone to commit into (default: the working directory)",
    )
    parser.add_argument(
        "--branch",
        default="",
        help="the branch to commit on (default: mibs/<vendor>-contribution)",
    )
    parser.add_argument(
        "--base",
        default="main",
        help="the branch to open the pull request against",
    )
    parser.add_argument(
        "--repository",
        default="pysnmp/mibs",
        help="the repository to open the pull request in",
    )
    parser.add_argument(
        "--submit",
        action="store_true",
        help="push the branch and open the pull request with the GitHub CLI",
    )
    options = parser.parse_args(argv)

    try:
        return import_bundle(options)
    except Refused as refusal:
        sys.stderr.write(f"{refusal}\n")
        return 2


if __name__ == "__main__":
    sys.exit(main())
