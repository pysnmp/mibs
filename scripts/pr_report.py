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


def render(scope: dict, report: dict, tree: Path, url: str) -> str:
    """The note, in Markdown."""
    failed = set(report.get("selected", {}).get("failed", ()))
    out = ["### MIB preview", ""]

    if scope["canary"]:
        out += [
            "This pull request changes no MIB. It changes how the pages are built,",
            "so these three are rendered as canaries: one standard module, one",
            "carrying a repair, one plain vendor module.",
            "",
        ]

    if url:
        out += [f"**[Browse the preview]({url}/browse/)**", ""]

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

        page = f"[{module}]({url}/mib/{module}/)" if url else "—"
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
        "imports resolve against all 5,510 as they will on the live site. The",
        "preview carries no sitemap and asks not to be indexed.</sub>",
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
    options = parser.parse_args(argv)

    with options.scope.open(encoding="utf-8") as fileObj:
        scope = json.load(fileObj)

    with options.report.open(encoding="utf-8") as fileObj:
        report = json.load(fileObj)

    sys.stdout.write(
        render(scope, report, options.tree, options.url.strip().rstrip("/"))
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
