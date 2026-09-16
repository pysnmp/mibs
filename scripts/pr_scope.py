#!/usr/bin/env python3
#
# This file is part of pysnmp/mibs.
#
"""What a pull request changed, in modules rather than in files.

CI builds the whole corpus on every pull request and holds it to every
contract, which answers *is the corpus still sound* and never answers *what
does the module I just added look like*. The whole-corpus site that build
produces is not published anywhere a reviewer can reach, and would not help
if it were: the two pages the review is about are in it somewhere.

The preview build answers the second question, and it needs a module set to
build. This turns a list of changed paths into one. The mapping is not
"the file name", for three reasons the tree actually contains:

- A module is what its file **declares**. The corpus is flat and named by
  module, so ``src/vendor/foo/BAR-MIB`` declaring ``BAZ-MIB`` publishes
  ``BAZ-MIB``, and a preview asking for ``BAR-MIB`` would be told no such
  module exists.
- A patch is MIB content. ``scripts/mib-patches/cisco/CISCO-IPMCAST-MIB.patch``
  is the record of what this repository changed in Cisco's text, and a pull
  request editing only the patch has changed what the site says about that
  module. ``mib-sources.json`` names the source each patch belongs to.
- A change to neither is still a change worth previewing when it is a change
  to how pages are *built*. A pysmi bump renders every page differently and
  touches no MIB at all; see :py:data:`CANARY`.

Usage:

    # What the pull request changed, against its base.
    uv run python scripts/pr_scope.py --base=origin/main --out=preview

    # The same from a list of paths, for a caller that already has one.
    uv run python scripts/pr_scope.py --changed-from=paths.txt --out=preview

It writes ``<out>/modules.txt`` -- one module name per line, which is what
``mibcorpus --publish-only-from`` reads -- and ``<out>/scope.json``, the whole
answer including what it decided not to build and why.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import TypedDict

from pysmi.mibinfo import module_names

#: The repository root, which every path here is relative to.
ROOT = Path(__file__).resolve().parent.parent

#: Where the corpus reads its modules from. Kept in step with the ``include``
#: in ``corpus.json``: a directory that is not a namespace is not in the
#: corpus, so a file under it is not MIB content however much it looks like
#: one. ``broken/`` is the case that matters -- it holds modules this corpus
#: deliberately does not carry.
SOURCES = "src/"

#: Where the repairs live, as ``<vendor>/<MODULE>.patch``.
PATCHES = "scripts/mib-patches/"

#: The provenance manifest, which maps a patch back to the module it repairs.
#: Consulted rather than trusted: a patch it does not name still repairs the
#: module its file name gives, and ``update_vendor_mibs.py --validate``
#: already refuses a patch no entry applies.
SOURCES_MANIFEST = "mib-sources.json"

#: Paths that change how a page is built without changing what is on it.
#: A pysmi bump is the case this exists for: it touches no MIB and it can
#: change every module page in the corpus, which is exactly the change a
#: reviewer most wants to see rendered and least expects to be able to.
#:
#: Matched as prefixes, so a directory covers what is under it.
TOOLCHAIN = (
    "pyproject.toml",
    "uv.lock",
    "corpus.json",
    "corpus-preview.json",
    "theme/",
    "registries/",
    ".github/workflows/pr-mib-preview.yml",
    "scripts/pr_scope.py",
)

#: What a toolchain change previews instead of nothing.
#:
#: Three modules chosen to cover the three things a module page can be, so
#: that a rendering change shows up in the preview rather than on the live
#: site a release later:
#:
#: - ``IF-MIB`` comes from the standard namespace, is the module every other
#:   contract in this repository names, and has ninety definitions -- enough
#:   for the object table to be worth looking at.
#: - ``CISCO-IPMCAST-MIB`` carries a patch, so it is the one that renders the
#:   repair panel: the defect, the note and the diff.
#: - ``TEL2N-MIB`` is a small vendor module from a single-module namespace,
#:   which is the shape most of this corpus is.
CANARY = ("CISCO-IPMCAST-MIB", "IF-MIB", "TEL2N-MIB")

#: File names under ``src/`` that are not modules and are not meant to be.
#: Anything else there that declares no module is an error: it is either a
#: MIB too damaged to lex a header out of, or a file that does not belong in
#: a source namespace, and both want a person rather than a silent omission.
NOT_MODULES = (".index", "README", "README.md", "README.txt")


class Scope(TypedDict):
    """What to preview, and what was decided about everything else.

    Written to ``scope.json`` and read by the workflow and by
    :py:mod:`pr_report`, so the key names are an interface rather than an
    internal shape.
    """

    #: ``mibs``, ``toolchain`` or ``none``.
    verdict: str
    #: The modules to build, sorted. Empty for ``none``.
    modules: list[str]
    #: Per module, why it is in the preview: ``source``, ``patch``, or both.
    reasons: dict[str, list[str]]
    #: Source paths the change deleted, which cannot be rendered.
    removed: list[str]
    #: Paths under the sources that declare no MIB module. An error.
    undeclared: list[str]
    #: Whether :py:data:`CANARY` is what is being built.
    canary: bool


def changed_paths(base: str) -> list[str]:
    """Paths this branch changed against *base*, as git reports them.

    Three dots: the changes on this side of the merge base, not everything
    that has happened on the base branch since. A pull request is the former,
    and previewing the latter would rebuild half the corpus the first time
    main moved.
    """
    found = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD"],
        cwd=ROOT,
        capture_output=True,
        check=True,
        text=True,
    )

    return [x for x in found.stdout.splitlines() if x.strip()]


def patch_owners() -> dict[str, str]:
    """Each patch file, mapped to the source path it repairs.

    Read from ``mib-sources.json``, which records the repair beside the
    module it belongs to. A patch the manifest does not name is not in here
    and falls back to its own file name, which is what the manifest's own
    check requires it to be anyway.
    """
    manifest = ROOT / SOURCES_MANIFEST

    if not manifest.is_file():
        return {}

    with manifest.open(encoding="utf-8") as fileObj:
        recorded = json.load(fileObj)

    return {
        entry["patch"]: path
        for path, entry in recorded.get("modules", {}).items()
        if entry.get("patch")
    }


def declared_by(path: str) -> list[str]:
    """The modules a file in the working tree declares.

    Empty when the file is gone -- a pull request may delete a MIB, and a
    module that is no longer in the tree cannot be built -- and empty when
    the text declares no module at all, which the caller tells apart by
    whether the file exists.
    """
    where = ROOT / path

    if not where.is_file():
        return []

    return module_names(where.read_text(encoding="utf-8", errors="replace"))


def scope(paths: list[str]) -> Scope:
    """What to preview, given what changed.

    Returns:
        The whole answer: ``verdict`` is ``mibs``, ``toolchain`` or ``none``;
        ``modules`` is what to build; and the rest is what was decided about
        each changed path, so that a pull request comment can say why a file
        it touched is not in the preview.
    """
    owners = patch_owners()

    modules: dict[str, list[str]] = {}
    removed: list[str] = []
    undeclared: list[str] = []

    def record(module: str, why: str) -> None:
        modules.setdefault(module, [])

        if why not in modules[module]:
            modules[module].append(why)

    for path in sorted(paths):
        if path.startswith(PATCHES) and path.endswith(".patch"):
            # A patch changed, so what this repository serves for that module
            # changed with it -- including when the patch was deleted, which
            # means the module is back to the publisher's text.
            source = owners.get(path[len(PATCHES) :])
            declared = declared_by(source) if source else []

            for module in declared or [Path(path).stem]:
                record(module, "patch")

            continue

        if not path.startswith(SOURCES):
            continue

        name = Path(path).name

        if name.startswith(".") or name in NOT_MODULES:
            continue

        declared = declared_by(path)

        if declared:
            for module in declared:
                record(module, "source")

            continue

        if (ROOT / path).exists():
            # There and unreadable as a MIB. Reported rather than skipped:
            # a preview that quietly leaves out the file the pull request is
            # about has answered the wrong question.
            undeclared.append(path)

        else:
            removed.append(path)

    if modules:
        verdict = "mibs"
        wanted = sorted(modules)

    elif any(x.startswith(TOOLCHAIN) for x in paths):
        verdict = "toolchain"
        wanted = sorted(CANARY)

    else:
        verdict = "none"
        wanted = []

    return Scope(
        verdict=verdict,
        modules=wanted,
        reasons={k: sorted(v) for k, v in sorted(modules.items())},
        removed=removed,
        undeclared=undeclared,
        canary=verdict == "toolchain",
    )


def main(argv: "list[str] | None" = None) -> int:
    """Run the scope, writing what the preview build reads."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--base", help="git ref this branch is measured against")
    source.add_argument(
        "--changed-from",
        type=Path,
        help="file of changed paths, one per line, instead of asking git",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("preview"),
        help="directory to write modules.txt and scope.json into",
    )
    options = parser.parse_args(argv)

    if options.changed_from:
        paths = [
            x.strip()
            for x in options.changed_from.read_text(encoding="utf-8").splitlines()
            if x.strip()
        ]

    else:
        paths = changed_paths(options.base)

    found = scope(paths)

    options.out.mkdir(parents=True, exist_ok=True)
    (options.out / "scope.json").write_text(
        json.dumps(found, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (options.out / "modules.txt").write_text(
        "".join(f"{x}\n" for x in found["modules"]), encoding="utf-8"
    )

    json.dump(found, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")

    if found["undeclared"]:
        for path in found["undeclared"]:
            sys.stderr.write(
                f"::error file={path}::this file is under {SOURCES} and declares "
                f"no MIB module. Either it is a module too damaged to read a "
                f"header out of, or it does not belong in a source namespace.\n"
            )

        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
