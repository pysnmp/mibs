#!/usr/bin/env python3
"""Union two Helm repository indexes, so publishing can only ever add.

``helm repo index --merge`` takes one base, which makes whichever file is
passed the single source of truth. That is what let the published index go
stale: the base was ``charts/index.yaml`` in the repository, the step that
wrote it back could not push to a protected ``main``, and its failure skipped
the step that publishes. Twenty-one releases went unindexed, 1.17.3 to 2.6.1.

A union has no single source of truth to lose. An entry present in either
input survives, so a failed fetch of the published index, or a republish from
an older checkout, degrades to "nothing added" rather than to "versions
deleted". Charts are immutable once released, so two entries for one version
are the same entry and either will do.
"""

import sys

import yaml


def key(entry: dict) -> tuple:
    """Sort newest first, with a release ahead of its own prereleases.

    Semver orders 1.17.10 above 1.17.9, which a string sort does not, and
    ranks 1.17.0 above 1.17.0-beta.1. Anything unparsable sorts last rather
    than raising: an index that lists a version this cannot read is still an
    index, and dropping the entry would be the failure this file exists to
    prevent.
    """
    version = str(entry.get("version", ""))
    head, _, pre = version.partition("-")
    try:
        parts = tuple(int(x) for x in head.split("."))

    except ValueError:
        return (0, (), True, version)

    return (1, parts, not pre, pre)


def union(*indexes: dict) -> dict:
    """Every entry from every index, once, keyed by chart name and version."""
    merged: dict = {}
    out: dict = {}

    for index in indexes:
        for name, versions in (index.get("entries") or {}).items():
            for entry in versions or ():
                merged.setdefault((name, entry.get("version")), entry)

        for field, value in index.items():
            if field != "entries":
                out.setdefault(field, value)

    entries: dict = {}

    for (name, _version), entry in merged.items():
        entries.setdefault(name, []).append(entry)

    for versions in entries.values():
        versions.sort(key=key, reverse=True)

    out["entries"] = entries
    out.setdefault("apiVersion", "v1")

    return out


def read(path: str) -> dict:
    """One index file, or an empty index where it is absent or unreadable.

    A missing file is the ordinary case on a cold start, and an unreadable one
    must not fail the publish: the other input still carries every version.
    """
    try:
        with open(path, encoding="utf-8") as handle:
            return yaml.safe_load(handle) or {}

    except (OSError, yaml.YAMLError) as exc:
        print(f"{path}: {exc}; treating as empty", file=sys.stderr)
        return {}


def main(argv: "list[str]") -> int:
    """``merge_chart_index.py <in> [<in> ...] <out>``."""
    if len(argv) < 3:
        print(f"usage: {argv[0]} <index> [<index> ...] <output>", file=sys.stderr)
        return 2

    *sources, destination = argv[1:]
    merged = union(*(read(path) for path in sources))
    counts = sum(len(v) for v in merged["entries"].values())

    with open(destination, "w", encoding="utf-8") as handle:
        yaml.safe_dump(merged, handle, default_flow_style=False, sort_keys=False)

    print(f"merged {len(sources)} indexes into {counts} entries")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
