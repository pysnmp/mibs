#!/usr/bin/env python3
#
# This file is part of pysnmp/mibs.
#
"""The preview, written as the note a reviewer reads.

Separate from :py:mod:`pr_scope` because it answers a different question.
The scope decides what to build, before the build; this describes what the
build produced, after it. Separate from the workflow because a report is the
half of a check people actually read, and one assembled out of shell in a
YAML file is one nobody can run.

The same text goes to two places, for two reasons. The job summary is written
on every run, including a pull request from a fork where the token is
read-only and cannot comment. The comment is what a reviewer sees without
opening the run, and is updated in place rather than added to, so a branch
pushed to ten times carries one note saying what is true now.

Usage:

    uv run python scripts/pr_report.py \\
        --scope=preview-scope/scope.json \\
        --report=output/preview/report.json \\
        --tree=output/preview \\
        --url=https://....workers.dev
"""

import argparse
import json
import sys
from pathlib import Path

#: Top-level keys of a jsondoc document that are not MIB symbols. Everything
#: else in it is a definition, which is what makes a count of them worth
#: printing: a module page carrying no definitions is a module that compiled
#: and said nothing, and the number is where that shows.
NOT_SYMBOLS = ("meta", "imports")

#: Why a module is in the preview, in the words the table prints.
WHY = {
    "source": "the MIB changed",
    "patch": "its repair changed",
    "canary": "canary",
}

#: The marker that makes the comment findable again on the next push. HTML
#: comment, so a reader never sees it and the next run does.
MARKER = "<!-- mib-preview -->"


def definitions(tree: Path, module: str) -> int:
    """How many symbols the module defines, from the document it compiled to."""
    document = tree / "json" / f"{module}.json"

    if not document.is_file():
        return 0

    with document.open(encoding="utf-8") as fileObj:
        return len([x for x in json.load(fileObj) if x not in NOT_SYMBOLS])


def render(
    scope: dict, report: dict, tree: Path, url: str, *, built: bool = True
) -> str:
    """The note, in Markdown.

    Keyword Args:
        built: whether the build succeeded. A failed build is the one case
            where there is something to say and nothing to link to, and it
            is the case this note exists for: the module that did not
            compile is named here rather than only in the run log.
    """
    failed = set(report.get("selected", {}).get("failed", ()))
    out = ["### MIB preview", ""]

    if not built:
        # Named first, because it is the answer. A reader who stops after
        # one line should already know which module to open.
        named = sorted(failed) or scope["modules"]
        out += [
            "**The preview build failed.** "
            + (
                f"{', '.join('`' + x + '`' for x in named)} did not compile."
                if failed
                else "No module reached the site."
            ),
            "",
            "The corpus is built from the whole source set, so this is the module",
            "as it will be published, not as it reads beside its own imports. The",
            "compiler's own message is in the run log, under **Build the",
            "preview**.",
            "",
        ]

    if scope["canary"]:
        out += [
            "This pull request changes no MIB. It changes how the pages are built,",
            "so these three are rendered as canaries: one standard module, one",
            "carrying a repair, one plain vendor module.",
            "",
        ]

    if url and built:
        out += [f"**[Browse the preview]({url}/browse/)**", ""]

    elif not built:
        out += [
            "Nothing was published, so there is no site to browse. What the build",
            "did write is attached to the run as the `mib-preview-site` artifact.",
            "",
        ]

    else:
        out += [
            "No preview host is configured for this run, so the site is attached",
            "to it as the `mib-preview-site` artifact.",
            "",
        ]

    out += ["| Module | Why | Definitions | Page |", "| --- | --- | --- | --- |"]

    for module in scope["modules"]:
        reasons = ", ".join(
            WHY.get(x, x) for x in scope["reasons"].get(module) or ["canary"]
        )

        if module in failed:
            out.append(f"| `{module}` | {reasons} | **did not compile** | — |")
            continue

        page = f"[{module}]({url}/mib/{module}/)" if url and built else "—"
        out.append(f"| `{module}` | {reasons} | {definitions(tree, module)} | {page} |")

    if scope["removed"]:
        out += [
            "",
            "Removed by this pull request, so there is nothing to render:",
            "",
            *(f"- `{x}`" for x in scope["removed"]),
        ]

    out += [
        "",
        "<sub>Built from the whole corpus, publishing only these modules, so their",
        "imports resolve against all 5,510 as they will on the live site."
        + (
            "</sub>"
            if not built
            else " The\npreview carries no sitemap and asks not to be indexed.</sub>"
        ),
        "",
        MARKER,
    ]

    return "\n".join(out) + "\n"


def main(argv: "list[str] | None" = None) -> int:
    """Print the note."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--scope", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--tree", type=Path, required=True)
    parser.add_argument("--url", default="")
    parser.add_argument(
        "--build-outcome",
        default="success",
        help=(
            "what the build step did, as GitHub reports it. Anything other "
            "than success renders the failure note instead of the links."
        ),
    )
    options = parser.parse_args(argv)

    with options.scope.open(encoding="utf-8") as fileObj:
        scope = json.load(fileObj)

    # A build that failed before writing its report leaves nothing to read.
    # That is the case with the most to say, so it must not be the case that
    # ends in a traceback: the scope still knows which modules were asked
    # for, and naming them is better than saying nothing.
    try:
        with options.report.open(encoding="utf-8") as fileObj:
            report = json.load(fileObj)

    except (OSError, ValueError):
        report = {}

    sys.stdout.write(
        render(
            scope,
            report,
            options.tree,
            options.url.strip().rstrip("/"),
            built=options.build_outcome == "success",
        )
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
