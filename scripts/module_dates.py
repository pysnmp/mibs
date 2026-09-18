#!/usr/bin/env python3
#
# This file is part of the pysnmp MIB distribution.
#
"""When this repository last changed each module it carries.

Every date a MIB carries is its publisher's: LAST-UPDATED and the REVISION
clauses say when the vendor changed the module. The site's recent lists are
ordered by those, which answers *what has the industry published lately* and
cannot answer *what have we done lately* -- a module added here today may
carry a revision from decades back.

This writes the second date, which the corpus cannot know: per module, the
commit that last touched its file. A repository that commits what it publishes
makes that close enough to "when we published it", and it costs nothing to
keep right because nobody maintains it -- the history is the record.

``mibcorpus`` reads the file this writes, named by ``site.changed`` in
``corpus.json``, and offers it beside the publishers' dates as a second tab on
``browse/``.

**Only the modules this repository supplies are covered.** The standard
namespace comes from pysmi's bundle rather than from this tree, so this
repository has no commit that last touched those modules and says nothing
about them: a module this file does not name is listed under no such date. See
the ``site.changed`` section of pysmi's ``mibcorpus`` documentation.
"""

import argparse
import json
import os
import pathlib
import subprocess
import sys
from typing import Final

#: The repository root, from this file's own location.
ROOT: Final = pathlib.Path(__file__).resolve().parent.parent

#: The tree whose history this reads. One file per module, named for the
#: module, which ``tests/source-layout-contract.py`` is what makes true.
SOURCES: Final = "src"

#: The package ``corpus.json`` resolves the standard namespace against. A
#: module this carries is published from pysmi's copy rather than from this
#: tree, whatever this tree holds under the same name.
STANDARD: Final = "pysmi.mibs.asn1"

#: Where the dates land by default, inside the build directory rather than in
#: the tree: this is derived from the history on every build, so a committed
#: copy would be a second thing to keep right.
OUTPUT: Final = os.path.join("output", "module-dates.json")


def _git(*arguments: str, root: pathlib.Path = ROOT) -> str:
    """One git command's output, or a failure that names it."""
    try:
        finished = subprocess.run(
            ("git", *arguments),
            cwd=root,
            capture_output=True,
            text=True,
            check=True,
        )

    except (OSError, subprocess.CalledProcessError) as exc:
        stderr = getattr(exc, "stderr", "") or str(exc)

        raise SystemExit(f"git {' '.join(arguments)} failed: {stderr.strip()}") from exc

    return finished.stdout


def shallow(root: pathlib.Path = ROOT) -> bool:
    """Whether this checkout has had its history truncated.

    Worth its own check because the failure is silent otherwise: a shallow
    clone answers every question this asks, and answers them from the handful
    of commits it has. Modules nothing touched inside that window come out
    undated, so the site would list a few recent ones and quietly omit the
    rest -- which reads as "we have not touched those" rather than as "this
    build could not tell".
    """
    return _git("rev-parse", "--is-shallow-repository", root=root).strip() == "true"


def dates(root: pathlib.Path = ROOT) -> "dict[str, str]":
    """Per module, the day this repository last changed its file.

    One pass over the history rather than a command per file: ``git log``
    walks newest first, so the first commit naming a path is the last one to
    have touched it, and a corpus of thousands of modules is one command
    rather than thousands.

    Args:
        root: the repository root.

    Returns:
        Module name to ``YYYY-MM-DD``, for the modules under
        :py:data:`SOURCES` that the history names. A file the history does not
        name -- one added in a commit this checkout does not have -- is absent
        rather than dated from something else.
    """
    written = _git(
        "log",
        "--pretty=format:%cs",
        "--name-only",
        # A rename is the same module arriving at a new path, and following it
        # would date the module by the commit that moved it rather than by the
        # one that last changed what it says. The new path is what this tree
        # holds, so the rename itself is the change worth dating.
        "--no-renames",
        "--",
        SOURCES,
        root=root,
    )

    found: dict[str, str] = {}
    date = ""

    for line in written.splitlines():
        if not line:
            continue

        # `%cs` is the committer date as YYYY-MM-DD, which is the format the
        # site wants; a line of that shape starts a commit's file list.
        if len(line) == 10 and line[4] == line[7] == "-":
            date = line
            continue

        module = os.path.basename(line)

        # The layout contract holds every file under src/ to one module named
        # for it, and skips the hidden files this repository keeps its own
        # notes in -- src/vendor/cisco/.mib-sources is not a MIB.
        if module and not module.startswith(".") and module not in found:
            found[module] = date

    return found


def standard() -> "frozenset[str]":
    """The modules the corpus takes from pysmi rather than from this tree.

    ``corpus.json`` resolves its standard namespace against
    :py:data:`STANDARD`, and pysmi adjudicates in the bundle's favour for
    every module it claims authority over, so the copy the site publishes for
    one of these is pysmi's -- whatever this tree holds under the same name.

    Two names collide today, ``ATM-FORUM-SRVC-REG`` and ``MPLS-FTN-STD-MIB``.
    Without this the site would say this repository updated them on the day
    it last touched its own copy, over a page rendered from the text pysmi
    publishes. Dating a module nobody serves from here is the one way a date
    read off the history can be false rather than merely coarse.

    Raises:
        SystemExit: pysmi is not importable, so which modules to exclude
            cannot be known.
    """
    try:
        from pysmi.compiler import bundled_mib_names

        return bundled_mib_names(STANDARD)

    except (ImportError, OSError) as exc:
        # Not a warning and a partial answer. Every module this cannot name
        # is one this would then date from a file the site does not serve, so
        # a dates file written without it is the specific falsehood the
        # exclusion exists to prevent -- and the build that reads the file
        # needs pysmi anyway, so nothing reaches a page from here that could
        # not have imported it.
        raise SystemExit(
            f"cannot read {STANDARD}, so the modules the corpus takes from "
            f"pysmi cannot be excluded and this would date them from files "
            f"the site does not publish: {exc}"
        ) from exc


def present(root: pathlib.Path = ROOT) -> "dict[str, str]":
    """The dates, for the modules this repository supplies to the corpus.

    Three things are left out. The history names every file it ever held,
    including the ones since removed, and a date for a module the corpus does
    not carry is weight nothing looks up. This repository's own metadata is
    not a module. And a module the corpus takes from pysmi is not this
    repository's to date -- see :py:func:`standard`.
    """
    where = root / SOURCES
    held = {
        x.name for x in where.rglob("*") if x.is_file() and not x.name.startswith(".")
    }
    found = dates(root)

    return {x: found[x] for x in sorted((held & set(found)) - standard())}


def main(argv: "list[str] | None" = None) -> int:
    """Write the dates file the corpus manifest names."""
    parsed = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parsed.add_argument(
        "--output",
        default=OUTPUT,
        help=f"where to write the dates (default: {OUTPUT})",
    )
    parsed.add_argument(
        "--allow-shallow",
        action="store_true",
        help="write what a truncated history knows rather than failing",
    )
    options = parsed.parse_args(argv)

    if shallow() and not options.allow_shallow:
        sys.stderr.write(
            "ERROR: this checkout is shallow, so most modules would come out "
            "undated and the site would read as though they had not been "
            "touched. Check out with fetch-depth: 0, or pass --allow-shallow "
            "to write what this history knows.\n"
        )

        return 1

    found = present()
    where = pathlib.Path(options.output)

    if not where.is_absolute():
        where = ROOT / where

    where.parent.mkdir(parents=True, exist_ok=True)

    with open(where, "w", encoding="utf-8") as fileObj:
        json.dump(found, fileObj, indent=1, sort_keys=True)
        fileObj.write("\n")

    newest = max(found.values(), default="never")
    print(f"{len(found)} modules dated from the history, newest {newest}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
