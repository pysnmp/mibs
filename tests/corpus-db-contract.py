#!/usr/bin/env python3
"""What *this repository's* ``core.db`` must be true of before it is published.

Most of what a corpus database has to satisfy is not this repository's to
assert. Whether the header identifies a corpus, whether every table and index
the schema names is there, whether ``oid_key`` orders the whole file the way
the arcs do, whether a node references a type row that exists -- those are
properties of the *format*, and the format belongs to pysmi. Asserting them
here put a requirement about pysmi's output in a repository that only consumes
it, where it could drift from the specification it was transcribed from and
keep passing.

pysmi owns them now, as :py:func:`pysmi.corpus.db.validate`, which this calls.
A build that fails it prints what pysmi found and stops.

What is left is what only this repository can know: that the database it just
built is the one it meant to build. The selection is right, the build options
were what they should be, and the artifact about to be published is a single
readable file rather than the wreckage of a half-finished run.

The checks are Python rather than shell, unlike this directory's other
contracts, for one reason: ``sqlite3`` the module is guaranteed wherever this
build runs, because the build is Python, while ``sqlite3`` the command-line
tool is a separate package that a runner image is free to stop shipping. A
contract that silently stops running is worse than no contract.

Usage: ``tests/corpus-db-contract.py [output-db]``
"""

import os
import sqlite3
import sys

from pysmi.corpus.db import validate

#: Floors, not counts. The corpus grows every time anyone adds a MIB, so a
#: test pinning its size fails on the next contribution; what these catch is a
#: build that produced an empty or half-written database and published it.
FLOORS = {"module": 4000, "node": 100000, "oid_index": 50000, "type": 10000}

#: Modules whose absence would be silent. The database builds, opens, passes
#: every structural check pysmi makes -- and then cannot resolve ``ifDescr``
#: for anybody, because this build was pointed at the compact manifest instead
#: of the full one. That is the mistake this file exists to catch.
REQUIRED_MODULES = ("SNMPv2-MIB", "SNMPv2-TC", "SNMPv2-SMI", "IF-MIB")

failures: "list[str]" = []


def check(condition, message):
    """Record a failure without stopping: one run should name them all."""
    if not condition:
        failures.append(message)

    return condition


def main(directory):
    """Check the database in *directory*, and say what is wrong with it."""
    path = os.path.join(directory, "core.db")

    if not os.path.exists(path):
        sys.exit(f"corpus-db-contract: no database at {path}")

    print(f"== {path} ({os.path.getsize(path) / 1e6:.1f} MB)")

    # One file. A -wal or -journal beside it is something the image would not
    # carry and immutable=1 refuses to replay, so the corpus would open and
    # then answer nothing. pysmi asserts its writer leaves none; this asserts
    # nothing else in this directory did, which pysmi cannot see.
    for suffix in ("-wal", "-journal", "-shm"):
        check(
            not os.path.exists(path + suffix),
            f"{path}{suffix} exists; a published corpus is one file",
        )

    # Readable by whoever mounts it. A build under a restrictive umask makes a
    # corpus only the build uid can read, which stays invisible until a
    # container running as another user opens it -- the same defect that had
    # every module in the served corpus stored 0600 (pysnmp/mibs#365).
    mode = os.stat(path).st_mode & 0o777
    check(mode & 0o044, f"core.db is mode {mode:o}; only its owner can read it")

    # Everything about the format, in one call. open_db inside it refuses a
    # file that is not a corpus or is a schema version pysmi does not
    # implement, so a wrong header arrives here as a PySmiError rather than as
    # a check of ours.
    for problem in validate(path):
        check(False, problem)

    # Opened the way a consumer opens it, so a file that only works when
    # writable fails here rather than in a pod.
    db = sqlite3.connect(f"file:{os.path.abspath(path)}?immutable=1", uri=True)

    try:
        run(db)

    finally:
        db.close()

    if failures:
        print(f"\ncorpus-db-contract: {len(failures)} failure(s)")

        for failure in failures:
            print(f"  - {failure}")

        sys.exit(1)

    print("corpus-db-contract: ok")


def run(db):
    """What this build meant to produce, as opposed to what a corpus must be."""
    one = lambda sql, *args: db.execute(sql, args).fetchone()

    meta = dict(db.execute("SELECT key, value FROM meta"))

    # No prose, and the corpus says so. That is this build's choice -- the
    # target passes no texts -- and a reader asked for texts has to be able to
    # refuse rather than silently hand back modules carrying none.
    check(meta.get("texts") == "0", f"meta.texts is {meta.get('texts')!r}")

    counts = {
        table: one(f"SELECT count(*) FROM {table}")[0]  # noqa: S608
        for table in ("module", "node", "type", "symbol", "import", "oid_index")
    }

    print(
        "   {module} modules, {node} nodes, {type} types, "
        "{oid_index} indexed OIDs".format(**counts)
    )

    for table, floor in FLOORS.items():
        check(
            counts[table] >= floor,
            f"only {counts[table]} rows in {table}; expected at least {floor}",
        )

    for module in REQUIRED_MODULES:
        check(
            one("SELECT 1 FROM module WHERE name = ?", module),
            f"{module} is not in the corpus",
        )

    # A leaf, by OID and by name. ifDescr is the case the published index
    # cannot answer at all -- it carries anchors -- so it is the one to name.
    row = one(
        "SELECT name FROM node WHERE oid = ? AND module = 'IF-MIB'",
        "1.3.6.1.2.1.2.2.1.2",
    )
    check(row and row[0] == "ifDescr", f"1.3.6.1.2.1.2.2.1.2 is {row and row[0]!r}")

    row = one("SELECT oid FROM node WHERE module = 'IF-MIB' AND name = 'ifType'")
    check(
        row and row[0] == "1.3.6.1.2.1.2.2.1.3",
        f"IF-MIB::ifType is at {row and row[0]!r}",
    )

    # Longest-prefix resolution: the anchor an instance OID chops back to.
    row = one("SELECT module FROM oid_index WHERE oid = ?", "1.3.6.1.2.1.2")
    check(row and row[0] == "IF-MIB", f"1.3.6.1.2.1.2 is owned by {row and row[0]!r}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "output-db")
