#
# This file is part of the pysnmp/mibs MIB repository.
# License: BSD-2-Clause
#
"""Keep the MIBs in ``src/`` honest about where their text came from.

A maintainer tool and a scheduled check, not part of building the site:

    uv run python scripts/update_vendor_mibs.py --check
    uv run python scripts/update_vendor_mibs.py --report
    uv run python scripts/update_vendor_mibs.py --update [PATH ...]
    uv run python scripts/update_vendor_mibs.py --adopt PATH ...
    uv run python scripts/update_vendor_mibs.py --explain PATH ...
    uv run python scripts/update_vendor_mibs.py --discover PUBLISHER DIR

``--check`` is what the monthly workflow runs: it re-fetches every module
``mib-sources.json`` covers and reports anything whose checked-in bytes no
longer equal the publisher's text with our patch applied. See
``scripts/mib_sources.py`` for the model and for what it cannot recover.
"""

from __future__ import annotations

import argparse
import datetime
import pathlib
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from mib_sources import (  # noqa: E402
    PATCHES,
    ROOT,
    SRC,
    NotAModule,
    Unreachable,
    apply_patch,
    attribute,
    changed_ranges,
    fetch,
    load_manifest,
    make_patch,
    module_of,
    revision_of,
    save_manifest,
    wanted_text,
)

#: How many publisher requests are in flight at once. Cisco alone accounts
#: for over a thousand modules in a sweep; serialising them would take the
#: better part of an hour, and a hundred at a time is impolite to a host
#: doing us a favour.
WORKERS = 8


def covered(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """The modules the manifest claims a publisher for."""
    modules: dict[str, dict[str, Any]] = manifest["modules"]

    return modules


def publisher_for(manifest: dict[str, Any], entry: dict[str, Any]) -> dict[str, Any]:
    """The publisher record an entry names."""
    name = entry["publisher"]
    try:
        found: dict[str, Any] = manifest["publishers"][name]
    except KeyError:
        raise SystemExit(f"no such publisher: {name!r}") from None

    return found


class Finding:
    """One thing a sweep noticed about one module."""

    def __init__(self, path: str, kind: str, detail: str) -> None:
        self.path = path
        self.kind = kind
        self.detail = detail

    def __str__(self) -> str:
        return f"{self.path}: {self.detail}"


def inspect(
    path: str, entry: dict[str, Any], publisher: dict[str, Any]
) -> Finding | None:
    """Compare one checked-in module against its publisher.

    Returns:
        What is wrong with it, or None if the publisher's text with our
        patch applied is exactly what is on disk.
    """
    local = ROOT / path

    if not local.is_file():
        return Finding(path, "missing", "in the manifest but not checked in")

    recorded = entry.get("divergence")

    try:
        upstream = fetch(path, entry, publisher)
    except Unreachable as exc:
        return Finding(path, "unreachable", str(exc))
    except NotAModule as exc:
        return Finding(path, "not-a-module", str(exc))

    ours = local.read_bytes()

    if "patch" in entry:
        try:
            expected = apply_patch(
                upstream, (PATCHES / entry["patch"]).read_text(), path
            )
        except ValueError as exc:
            return Finding(path, "patch-stale", str(exc).split(": ", 1)[-1])
    else:
        expected = upstream

    if ours == expected:
        if recorded:
            return Finding(
                path,
                "divergence-resolved",
                "recorded as diverging, but now matches its publisher -- "
                "drop the divergence record from mib-sources.json",
            )
        return None

    if recorded:
        return Finding(
            path,
            "known-divergence",
            f"ours {revision_of(ours)}, published "
            f"{revision_of(upstream)} -- {recorded.get('note', 'recorded')}"
            f" (since {recorded.get('recorded', '?')})",
        )

    return Finding(
        path,
        "drift",
        f"no longer matches its publisher (ours {revision_of(ours)}, "
        f"published {revision_of(upstream)})",
    )


def sweep(manifest: dict[str, Any], paths: list[str] | None = None) -> list[Finding]:
    """Inspect every covered module, or just *paths*, in parallel."""
    modules = covered(manifest)
    wanted = paths if paths is not None else sorted(modules)
    findings = []

    def one(path: str) -> Finding | None:
        entry = modules[path]

        return inspect(path, entry, publisher_for(manifest, entry))

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        for finding in pool.map(one, wanted):
            if finding is not None:
                findings.append(finding)

    return sorted(findings, key=lambda f: (f.kind, f.path))


#: Which findings mean the repository is wrong, as against merely
#: behind in a way somebody has already written down. A sweep that only
#: turns up known divergences stays green: the backlog is recorded in
#: the manifest, and re-reporting it as failure every month would train
#: everyone to ignore the one month it says something new.
FATAL = {
    "missing",
    "not-a-module",
    "patch-stale",
    "drift",
    "divergence-resolved",
}


def check(manifest: dict[str, Any]) -> int:
    """Report every module that no longer matches its publisher.

    Returns:
        0 if nothing is wrong, 1 if something is, 2 if a publisher could
        not be reached at all -- an outage says nothing about our MIBs,
        and the exit code says so rather than looking like drift.
    """
    findings = sweep(manifest)
    modules = covered(manifest)
    fatal = [f for f in findings if f.kind in FATAL]
    unreachable = [f for f in findings if f.kind == "unreachable"]
    known = [f for f in findings if f.kind == "known-divergence"]

    for group, title in (
        (fatal, "Out of step with their publisher"),
        (known, "Known divergences, awaiting review"),
        (unreachable, "Publishers that could not be reached"),
    ):
        if group:
            sys.stderr.write(f"\n{title}:\n")
            for finding in group:
                sys.stderr.write(f"  {finding}\n")

    checked = len(modules)
    clean = checked - len(findings)
    sys.stdout.write(
        f"\n{clean} of {checked} covered modules match their publisher; "
        f"{len(known)} known divergences.\n"
    )

    if fatal:
        sys.stderr.write(
            f"\n{len(fatal)} module(s) need attention. Run --explain on one "
            "to see whether the difference is a fix of ours worth keeping "
            "as a patch, or a copy that has simply fallen behind.\n"
        )
        return 1

    if unreachable:
        sys.stderr.write(
            f"\n{len(unreachable)} publisher(s) unreachable; the sweep is "
            "incomplete rather than failing.\n"
        )
        return 2

    return 0


def validate(manifest: dict[str, Any]) -> int:
    """Check the manifest against the working tree, without the network.

    Everything ``--check`` can be sure of before it fetches anything: a
    publisher that no entry names, an entry naming one that does not
    exist, a patch file that has been deleted, a path no longer in the
    tree. Cheap enough to run in ordinary CI, where a monthly sweep is
    too slow and needs a third-party site to be up.

    Returns:
        The process exit code: 0 if the manifest is coherent, 1 if not.
    """
    modules = covered(manifest)
    publishers = manifest["publishers"]
    problems = []

    for path in sorted(modules):
        entry = modules[path]

        if entry.get("publisher") not in publishers:
            problems.append(
                f"{path}: names publisher {entry.get('publisher')!r}, "
                "which is not defined"
            )
        if not (ROOT / path).is_file():
            problems.append(f"{path}: in the manifest but not in the tree")
        if "patch" in entry:
            if not (PATCHES / entry["patch"]).is_file():
                problems.append(f"{path}: its patch {entry['patch']} is gone")
            if not entry.get("reason"):
                problems.append(
                    f"{path}: carries a patch with no reason recorded. A "
                    "patch nobody wrote down the purpose of cannot be "
                    "reviewed when the publisher revises the text under it."
                )

    named = {entry.get("publisher") for entry in modules.values()}
    for name in sorted(set(publishers) - named):
        problems.append(f"publisher {name!r} is defined but unused")

    for patch in sorted(PATCHES.rglob("*.patch")):
        relative = patch.relative_to(PATCHES).as_posix()
        if not any(e.get("patch") == relative for e in modules.values()):
            problems.append(f"{relative}: a patch no entry applies")

    if problems:
        sys.stderr.write("mib-sources.json does not match the tree:\n")
        for problem in problems:
            sys.stderr.write(f"  {problem}\n")
        return 1

    sys.stdout.write(
        f"{len(modules)} entries across {len(publishers)} publishers; "
        "manifest and tree agree.\n"
    )

    return 0


def report(manifest: dict[str, Any]) -> int:
    """Say how much of ``src/`` has a publisher behind it, per directory.

    Coverage is the honest number here. Most of this repository has no
    fetchable source and is not going to get one, so a sweep that only
    counted what it covers would read as a clean bill of health for a
    tree it never looked at.
    """
    modules = covered(manifest)
    tracked: dict[str, int] = {}
    total: dict[str, int] = {}

    for path in sorted(modules):
        tracked[str(pathlib.PurePosixPath(path).parent)] = (
            tracked.get(str(pathlib.PurePosixPath(path).parent), 0) + 1
        )

    for entry in sorted(SRC.rglob("*")):
        if not entry.is_file() or entry.name.startswith("."):
            continue
        directory = entry.parent.relative_to(ROOT).as_posix()
        total[directory] = total.get(directory, 0) + 1

    covered_count = sum(tracked.values())
    total_count = sum(total.values())

    sys.stdout.write("Directory                          covered / total\n")
    for directory in sorted(total):
        have = tracked.get(directory, 0)
        if not have:
            continue
        sys.stdout.write(f"  {directory:<38} {have:>5} / {total[directory]:<5}\n")

    uncovered = sorted(d for d in total if not tracked.get(d))
    sys.stdout.write(
        f"\n{covered_count} of {total_count} checked-in modules have a "
        f"publisher on record.\n"
        f"{len(uncovered)} directories have none at all.\n"
    )

    return 0


def explain(manifest: dict[str, Any], paths: list[str]) -> int:
    """Say, for each path, what our copy does to the publisher's text.

    This is the question ``--check`` cannot answer on its own. A file
    that differs from its publisher is either carrying a fix of ours or
    simply old, and the difference between the two is in our git
    history: a hunk some later commit wrote is a fix, a hunk that traces
    no further back than the import is text we received that way.

    The second kind is the limit this repository has to live with. It
    may be a repair snmplabs or librenms made before we ever saw the
    file, or it may be a revision the vendor has since published past.
    Nothing here can tell those apart, and this says so rather than
    guessing.
    """
    modules = covered(manifest)

    for path in paths:
        entry = modules.get(path)
        if entry is None:
            sys.stderr.write(f"{path}: no publisher on record\n")
            continue

        local = (ROOT / path).read_bytes()
        try:
            upstream = fetch(path, entry, publisher_for(manifest, entry))
        except (Unreachable, NotAModule) as exc:
            sys.stderr.write(f"{path}: {exc}\n")
            continue

        sys.stdout.write(f"\n{path}\n")
        sys.stdout.write(
            f"  ours {revision_of(local)}, " f"published {revision_of(upstream)}\n"
        )

        if local == upstream:
            sys.stdout.write("  identical to the publisher's text\n")
            continue

        ranges, deletions = changed_ranges(upstream, local)
        subjects, inherited = attribute(path, ranges)
        lines = sum(stop - start + 1 for start, stop in ranges)

        sys.stdout.write(
            f"  {lines} line(s) of ours the publisher does not have, "
            f"in {len(ranges)} hunk(s); {deletions} hunk(s) drop "
            "publisher text\n"
        )

        if subjects:
            sys.stdout.write("  written by commits of ours:\n")
            for subject in subjects:
                sys.stdout.write(f"    {subject}\n")

        if inherited:
            sys.stdout.write(
                "  some of it traces no further back than the import: "
                "either a repair made before this repository received "
                "the file, or a revision the vendor has published since. "
                "Our history cannot say which.\n"
            )

        if not ranges:
            sys.stdout.write(
                "  -> our copy only drops publisher text, which leaves "
                "nothing for git to attribute. Read both texts: this is "
                "as likely to be a repair made before the import as a "
                "revision we never took.\n"
            )
        elif subjects and not inherited:
            sys.stdout.write(
                "  -> every differing line was last written by a commit "
                "of ours. Read the subjects above before adopting: a "
                "bulk refresh of a vendor directory is a commit of ours "
                "too, and adopting one would freeze a stale drop as a "
                "patch.\n"
            )
        elif inherited and not subjects:
            sys.stdout.write(
                "  -> nothing of ours is in it: compare the two texts "
                "before deciding, and --update if it is only stale\n"
            )
        else:
            sys.stdout.write(
                "  -> part ours, part inherited: adopting takes both, "
                "so read the patch before committing it\n"
            )

    return 0


def adopt(manifest: dict[str, Any], paths: list[str]) -> int:
    """Record what our copy does to the publisher's text, as a patch.

    Nothing on disk changes: the patch is cut so that the publisher's
    text with it applied is byte for byte the file already checked in.
    What changes is that the difference becomes readable, attributed to
    the commit that made it, and checked every month against a
    publisher who may revise the text under it.
    """
    modules = covered(manifest)
    failed = 0

    for path in paths:
        entry = modules.get(path)
        if entry is None:
            sys.stderr.write(f"{path}: no publisher on record\n")
            failed += 1
            continue

        local = (ROOT / path).read_bytes()
        try:
            upstream = fetch(path, entry, publisher_for(manifest, entry))
        except (Unreachable, NotAModule) as exc:
            sys.stderr.write(f"{path}: {exc}\n")
            failed += 1
            continue

        if local == upstream:
            sys.stderr.write(f"{path}: nothing to adopt\n")
            continue

        module = module_of(path)
        vendor = pathlib.PurePosixPath(path).parent.name
        relative = f"{vendor}/{module}.patch"
        patch = make_patch(upstream, local, module)

        # Cut it, then prove it: a patch that does not reproduce the
        # checked-in bytes exactly would quietly rewrite the MIB the
        # next time --update ran.
        if apply_patch(upstream, patch, path) != local:
            sys.stderr.write(f"{path}: generated patch does not round-trip\n")
            failed += 1
            continue

        target = PATCHES / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(patch)

        entry["patch"] = relative
        subjects, inherited = attribute(path, changed_ranges(upstream, local)[0])
        if subjects:
            entry.setdefault("reason", subjects[0].split(" ", 2)[-1])
        if inherited:
            entry["provenance"] = (
                "partly inherited: some of this patch traces no further "
                "back than the import, so what it repairs is not recorded "
                "anywhere"
            )
        entry.pop("divergence", None)

        sys.stdout.write(f"{path}: patch written to {relative}\n")

    save_manifest(manifest)

    return 1 if failed else 0


def update(manifest: dict[str, Any], paths: list[str]) -> int:
    """Rewrite the checked-in files from their publisher, patches applied.

    The only thing that makes a MIB in ``src/`` change here. Refusing
    partway leaves every file untouched: a half-refreshed vendor
    directory compiles into a tree that is neither the old set nor the
    new one.
    """
    modules = covered(manifest)
    wanted = paths or sorted(modules)
    staged: dict[str, bytes] = {}

    for path in wanted:
        entry = modules.get(path)
        if entry is None:
            sys.stderr.write(f"{path}: no publisher on record\n")
            return 1

        try:
            staged[path] = wanted_text(path, entry, publisher_for(manifest, entry))
        except (Unreachable, NotAModule, ValueError) as exc:
            sys.stderr.write(f"{path}: {exc}\n")
            sys.stderr.write("Nothing written; src/ is unchanged.\n")
            return 1

    changed = 0
    for path, data in staged.items():
        local = ROOT / path
        if local.is_file() and local.read_bytes() == data:
            continue
        local.write_bytes(data)
        modules[path].pop("divergence", None)
        sys.stdout.write(f"{path}: refreshed ({len(data)} bytes)\n")
        changed += 1

    save_manifest(manifest)
    sys.stdout.write(f"{changed} of {len(staged)} module(s) refreshed.\n")

    return 0


def discover(manifest: dict[str, Any], name: str, directory: str) -> int:
    """Ask a publisher which modules in *directory* it still serves.

    How a vendor gets adopted. Every file in the directory that the
    publisher serves and that matches byte for byte is added to the
    manifest outright -- that is the bulk of any vendor, and it needs no
    judgement. What is left over is the interesting part, and is only
    listed: a module the publisher does not serve stays unmanaged, and
    one whose text differs needs somebody to run --explain and decide.
    """
    modules = covered(manifest)
    publisher = manifest["publishers"][name]
    root = ROOT / directory

    if not root.is_dir():
        raise SystemExit(f"{directory}: not a directory")

    candidates = sorted(
        entry.relative_to(ROOT).as_posix()
        for entry in root.iterdir()
        if entry.is_file() and not entry.name.startswith(".")
    )

    def one(path: str) -> tuple[str, str, str]:
        if path in modules:
            return path, "known", ""
        try:
            upstream = fetch(path, {}, publisher)
        except NotAModule as exc:
            return path, "unserved", str(exc)
        except Unreachable as exc:
            return path, "unserved", str(exc)

        if (ROOT / path).read_bytes() == upstream:
            return path, "matches", ""

        return (
            path,
            "differs",
            (
                f"ours {revision_of((ROOT / path).read_bytes())}, "
                f"published {revision_of(upstream)}"
            ),
        )

    outcomes: dict[str, list[tuple[str, str]]] = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        for path, outcome, detail in pool.map(one, candidates):
            outcomes.setdefault(outcome, []).append((path, detail))

    for path, _ in outcomes.get("matches", []):
        modules[path] = {"publisher": name}

    today = datetime.date.today().isoformat()
    for path, detail in outcomes.get("differs", []):
        modules[path] = {
            "publisher": name,
            "divergence": {
                "recorded": today,
                "note": "not yet reviewed",
            },
        }

    save_manifest(manifest)

    for outcome, title in (
        ("matches", "adopted, identical to the publisher"),
        ("differs", "adopted, but our text differs -- run --explain"),
        ("unserved", "not served by this publisher, left unmanaged"),
        ("known", "already in the manifest"),
    ):
        group = outcomes.get(outcome, [])
        sys.stdout.write(f"\n{len(group)} {title}\n")
        if outcome in ("differs", "unserved"):
            for path, detail in sorted(group):
                sys.stdout.write(f"  {path}{': ' + detail if detail else ''}\n")

    return 0


def main() -> int:
    """Parse the arguments and run the mode asked for."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--check",
        action="store_true",
        help="report modules that no longer match their publisher",
    )
    mode.add_argument(
        "--validate",
        action="store_true",
        help="check the manifest against the tree, without the network",
    )
    mode.add_argument(
        "--report",
        action="store_true",
        help="say how much of src/ has a publisher on record",
    )
    mode.add_argument(
        "--update",
        action="store_true",
        help="rewrite checked-in files from their publisher, patched",
    )
    mode.add_argument(
        "--adopt",
        action="store_true",
        help="record what our copy does to the publisher's text",
    )
    mode.add_argument(
        "--explain",
        action="store_true",
        help="say whether a difference is a fix of ours or staleness",
    )
    mode.add_argument(
        "--discover",
        nargs=2,
        metavar=("PUBLISHER", "DIRECTORY"),
        help="ask a publisher which modules in a directory it serves",
    )
    parser.add_argument("paths", nargs="*", help="repository-relative paths")
    arguments = parser.parse_args()

    manifest = load_manifest()

    if arguments.check:
        return check(manifest)
    if arguments.validate:
        return validate(manifest)
    if arguments.report:
        return report(manifest)
    if arguments.discover:
        return discover(manifest, *arguments.discover)

    if not arguments.paths and not arguments.update:
        parser.error("this mode needs at least one path")

    if arguments.update:
        return update(manifest, arguments.paths)
    if arguments.adopt:
        return adopt(manifest, arguments.paths)

    return explain(manifest, arguments.paths)


if __name__ == "__main__":
    sys.exit(main())
