import csv
import json
import os
import re

JSON_DIR = "output/json"
SRC_DIR = "src"
DRAFT_DIR = os.path.join("src", "standard", "internet-drafts")
FROZEN = "index-frozen.csv"
LEGACY_OUT = "output/index.csv"
CURRENT_OUT = "output/index-v2.csv"

TIER_STANDARD = 0
TIER_DRAFT = 1
TIER_VENDOR = 2


def classify():
    tiers = {}
    for root, _, files in os.walk(SRC_DIR):
        if root.startswith(DRAFT_DIR):
            tier = TIER_DRAFT
        elif root.startswith(os.path.join("src", "vendor")):
            tier = TIER_VENDOR
        else:
            tier = TIER_STANDARD
        for name in files:
            tiers[name] = min(tier, tiers.get(name, tier))
    return tiers


def revision_rank(jmib):
    newest = 0
    for data in jmib.values():
        if not isinstance(data, dict) or data.get("class") != "moduleidentity":
            continue
        revisions = data.get("revisions", [])
        if not isinstance(revisions, list):
            continue
        for rev in revisions:
            if not isinstance(rev, dict):
                continue
            revision = rev.get("revision")
            if not isinstance(revision, str):
                continue
            digits = re.sub(r"\D", "", revision)[:12]
            if digits:
                newest = max(newest, int(digits.ljust(12, "0")))
    return newest


def arcs(oid):
    """Sort key placing an OID after every prefix of it, numerically."""
    try:
        return tuple(int(arc) for arc in oid.split("."))
    except ValueError:
        return ()


OBJECT_CLASSES = ("objecttype", "notificationtype")
ANCHOR_CLASSES = ("moduleidentity", "objectidentity")

tiers = classify()
index: dict[str, tuple] = {}
modules = set()

for filename in sorted(os.listdir(JSON_DIR)):
    module = filename.replace(".json", "")
    modules.add(module)
    with open(os.path.join(JSON_DIR, filename), "r") as read_file:
        jmib = json.load(read_file)

    has_identity = any(
        isinstance(d, dict) and d.get("class") == "moduleidentity"
        for d in jmib.values()
    )
    statuses = [
        d.get("status")
        for d in jmib.values()
        if isinstance(d, dict) and d.get("class") in OBJECT_CLASSES
    ]
    rank = (
        1 if statuses and all(s == "obsolete" for s in statuses) else 0,
        tiers.get(module, TIER_STANDARD),
        0 if has_identity else 1,
        -revision_rank(jmib),
        module,
    )

    oids = [
        data["oid"]
        for data in jmib.values()
        if isinstance(data, dict)
        and data.get("class") in ANCHOR_CLASSES
        and isinstance(data.get("oid"), str)
    ]
    if not oids:
        oids = [
            data["oid"]
            for data in jmib.values()
            if isinstance(data, dict)
            and "class" in data
            and isinstance(data.get("oid"), str)
        ]

    if not oids and "-TC" not in filename:
        print(f"Unable to index {JSON_DIR}/{filename}")

    for oid in oids:
        index[oid] = rank if oid not in index else min(index[oid], rank)

with open(CURRENT_OUT, "w") as f:
    for oid, rank in sorted(index.items(), key=lambda item: arcs(item[0])):
        f.write(f"{rank[-1]},{oid}\n")

# The legacy index answers to consumers that key on the module name a given OID
# resolves to, so the one thing it must never do is change an answer it has
# already given. Everything else is fair game:
#
#   - a row whose module is no longer compiled is dropped, because it names a
#     MIB the site cannot serve;
#   - an OID the snapshot never carried is added from the ranked index, because
#     a caller that had no answer for it cannot be broken by getting one.
#
# Without the second rule a MIB added to this repo would never reach the legacy
# index at all, and a consumer that has not moved to index-v2.csv would keep
# resolving nothing for it.
#
# The snapshot only ships with the corpus. The container runs this script again
# over just the MIBs a user mounted at runtime, and there the snapshot has
# nothing to say about modules it predates, so the ranked index is the answer
# and the caller merges it into the index already being served.
if os.path.exists(FROZEN):
    kept: dict[str, str] = {}
    dropped = 0
    with open(FROZEN, newline="") as src:
        for row in csv.reader(src):
            if len(row) < 2:
                continue
            module, oid = row[0], row[1]
            if module not in modules:
                dropped += 1
                continue
            kept[oid] = module
    added = 0
    for oid, rank in index.items():
        if oid not in kept:
            kept[oid] = rank[-1]
            added += 1
    with open(LEGACY_OUT, "w") as out:
        for oid, module in sorted(kept.items(), key=lambda item: arcs(item[0])):
            out.write(f"{module},{oid}\n")
    print(
        f"{LEGACY_OUT}: {len(kept)} OIDs, {dropped} rows dropped as absent, "
        f"{added} added from the ranked index"
    )
else:
    with open(LEGACY_OUT, "w") as out:
        for oid, rank in sorted(index.items(), key=lambda item: arcs(item[0])):
            out.write(f"{rank[-1]},{oid}\n")
    print(f"{LEGACY_OUT}: no frozen snapshot, wrote {len(index)} ranked OIDs")
print(f"{CURRENT_OUT}: {len(index)} OIDs")
