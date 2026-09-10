#!/usr/bin/env python3
"""The compact corpus must be a subset of the published one, not a second rendering of it.

Both corpora are built from the same source set. They differ in one line:
``corpus-compact.json`` marks the standard namespace ``"publish": false``, so
pysmi's bundled modules resolve what the vendor modules import without being
carried into the output tree.

The whole reason that is worth doing rests on a property nothing has been
checking: that leaving the standard modules *unpublished* does not change how
the vendor modules **compile**. If it did, the compact corpus would be a
different corpus that happens to share module names -- a runtime mounting it
would get subtly different answers from the ones this repository publishes, and
the difference would be invisible, because both builds succeed and both produce
plausible output.

So: for every module both corpora carry, compare the compiled jsondoc byte for
byte, and compare the OID index rows they each claim. Names are not enough --
two builds agreeing on *which* modules exist while disagreeing on what is *in*
them is exactly the failure this is for.

The index comparison allows one difference, because the selection creates it by
design: an arc whose published winner is a standard module falls to a vendor
module in the compact corpus, which does not publish the standard one. Those are
counted and reported, not failed. Everything else -- a winner the published
corpus never compiled, or two modules that are both published in both corpora
resolving differently -- is a genuine divergence.

One limit worth stating, since a test that overstates itself is worse than one
that does less. On a ceded arc this cannot tell *which* vendor module ought to
win: the fingerprint carries one winner per OID, not the set of claimants, so
any substitute the published corpus compiled at all is accepted. What bounds
that is the ceiling below -- the category may not grow unnoticed. Checking the
substitute itself would mean fingerprinting every claimant of every arc, which
is a much larger artifact for a case that today covers 58 arcs out of 97,032.

Run in two steps, because the two corpora are built by separate CI jobs and
neither has the other's tree:

    tests/corpus-agreement.py fingerprint <json-dir> <index-v2.csv> <out.json>
    tests/corpus-agreement.py compare <full.json> <compact.json>

``fingerprint`` reduces a build to a few hundred kilobytes -- a hash per module
and the index rows -- which is what crosses between jobs. ``compare`` is the
contract.
"""

import hashlib
import json
import os
import sys

# A build that produced almost nothing would satisfy every comparison below
# vacuously: no shared modules means no mismatched ones. The floor is what
# makes a pass mean something. It is well under the ~5,300 vendor modules the
# corpus carries, so ordinary content churn never trips it, and a build that
# collapsed to a handful of modules cannot pass by being empty.
SHARED_MODULE_FLOOR = 4000

# Arcs the compact corpus is expected to resolve differently, because the module
# that wins them in the published corpus is a standard one it does not publish.
# There were 58 at the time of writing, all under 1.2.840.10006.300.43, where
# quanta's LAG-MIB takes over from IEEE8023-LAG-MIB. The exemption is what keeps
# that from failing the build; the ceiling is what keeps the exemption from
# quietly growing into a licence for the two corpora to diverge wherever they
# like. A vendor module that starts shadowing a standard arc trips this, and
# should: it means something in the compact corpus now answers differently from
# what this repository publishes, and someone should decide whether that is
# intended before it ships.
CEDED_ARC_CEILING = 80


def fingerprint(json_dir: str, index_path: str, out_path: str) -> int:
    """Reduce one build to what the comparison needs."""
    modules = {}
    for name in os.listdir(json_dir):
        if not name.endswith(".json"):
            continue
        with open(os.path.join(json_dir, name), "rb") as fp:
            modules[name[: -len(".json")]] = hashlib.sha256(fp.read()).hexdigest()

    index = {}
    with open(index_path, encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if not line:
                continue
            module, _, oid = line.partition(",")
            index[oid] = module

    with open(out_path, "w", encoding="utf-8") as fp:
        json.dump({"modules": modules, "index": index}, fp)

    print(f"{out_path}: {len(modules)} modules, {len(index)} index rows")
    return 0


def compare(full_path: str, compact_path: str) -> int:
    with open(full_path, encoding="utf-8") as fp:
        full = json.load(fp)
    with open(compact_path, encoding="utf-8") as fp:
        compact = json.load(fp)

    failures = []

    full_modules = full["modules"]
    compact_modules = compact["modules"]
    shared = sorted(set(full_modules) & set(compact_modules))

    # The compact corpus carries a subset of the source set, so anything it has
    # that the published corpus does not is a selection bug: the two manifests
    # have stopped describing one corpus.
    extra = sorted(set(compact_modules) - set(full_modules))
    if extra:
        failures.append(
            f"{len(extra)} module(s) in the compact corpus but not the published one: "
            + ", ".join(extra[:10])
            + (", ..." if len(extra) > 10 else "")
        )

    if len(shared) < SHARED_MODULE_FLOOR:
        failures.append(
            f"only {len(shared)} shared module(s), below the floor of {SHARED_MODULE_FLOOR} -- "
            "a comparison over this few modules passes by being empty, not by being right"
        )

    mismatched = [m for m in shared if full_modules[m] != compact_modules[m]]
    if mismatched:
        failures.append(
            f"{len(mismatched)} of {len(shared)} shared module(s) compiled differently: "
            + ", ".join(mismatched[:10])
            + (", ..." if len(mismatched) > 10 else "")
        )

    # An OID both indexes carry can legitimately name a different module in
    # each. Where the published corpus' winner is a standard module, the compact
    # corpus does not publish it, so the arc falls to whichever vendor module
    # also claims it -- IEEE8023-LAG-MIB gives way to quanta's LAG-MIB at
    # 1.2.840.10006.300.43, for instance. That is the selection working. What
    # would not be is a compact winner the published corpus never compiled at
    # all, or a disagreement where both claimants *are* published in both: those
    # mean the two builds resolved the same corpus differently.
    full_index = full["index"]
    compact_index = compact["index"]
    shared_oids = set(full_index) & set(compact_index)
    disagreed, ceded = [], 0
    for oid in sorted(shared_oids):
        full_winner, compact_winner = full_index[oid], compact_index[oid]
        if full_winner == compact_winner:
            continue
        if full_winner not in compact_modules and compact_winner in full_modules:
            ceded += 1
            continue
        disagreed.append(oid)
    if disagreed:
        detail = ", ".join(
            f"{oid} ({full_index[oid]} vs {compact_index[oid]})"
            for oid in disagreed[:5]
        )
        failures.append(
            f"{len(disagreed)} of {len(shared_oids)} shared OID(s) resolve to a different "
            f"module: {detail}" + (", ..." if len(disagreed) > 5 else "")
        )

    if ceded > CEDED_ARC_CEILING:
        failures.append(
            f"{ceded} arc(s) ceded to a vendor claimant, above the ceiling of "
            f"{CEDED_ARC_CEILING} -- the compact corpus is answering differently "
            "from the published one on more arcs than it used to; confirm the "
            "new ones are intended and raise the ceiling, or stop shadowing them"
        )

    if failures:
        print("corpus agreement: FAIL")
        for line in failures:
            print(f"  - {line}")
        return 1

    print(
        f"corpus agreement: OK -- {len(shared)} shared module(s) identical, "
        f"{len(shared_oids) - ceded} shared OID(s) agree, {ceded} ceded to a "
        "vendor claimant where the compact corpus does not publish the winner "
        f"(published {len(full_modules)}, compact {len(compact_modules)})"
    )
    return 0


def main(argv: list[str]) -> int:
    if len(argv) == 5 and argv[1] == "fingerprint":
        return fingerprint(argv[2], argv[3], argv[4])
    if len(argv) == 4 and argv[1] == "compare":
        return compare(argv[2], argv[3])
    print(
        "usage: corpus-agreement.py fingerprint <json-dir> <index-v2.csv> <out.json>\n"
        "       corpus-agreement.py compare <full.json> <compact.json>",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
