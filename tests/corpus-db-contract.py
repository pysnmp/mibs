#!/usr/bin/env python3
"""What ``core.db`` must be true of before it is published.

The corpus database is read by pysnmp with stdlib ``sqlite3`` and no pysmi
import, out of a file mounted read-only from an image volume. Everything
checked here is something that, if it slipped, would surface as a pod that
will not start or a trap that will not resolve -- not as a build that went
red.

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

#: SQLite's ``application_id`` for a corpus -- ``PSMI`` as big-endian ASCII.
APPLICATION_ID = 0x50534D49

#: The corpus schema this repository publishes.
SCHEMA_VERSION = 1

#: Floors, not counts. The corpus grows every time anyone adds a MIB, so a
#: test pinning its size fails on the next contribution; what these catch is a
#: build that produced an empty or half-written database and published it.
FLOORS = {"module": 4000, "node": 100000, "oid_index": 50000, "type": 10000}

#: Modules whose absence would be silent. The database builds, opens and then
#: cannot resolve ``ifDescr`` for anybody -- which is the one way this corpus
#: differs from the compact one, and the one way to get that wrong.
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
    # then answer nothing.
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
    """Every check that needs the database open."""
    one = lambda sql, *args: db.execute(sql, args).fetchone()  # noqa: E731

    # The header a reader gates on before it trusts a single table.
    check(
        one("PRAGMA application_id")[0] == APPLICATION_ID,
        f"application_id is {one('PRAGMA application_id')[0]:#x}, not PSMI",
    )
    check(
        one("PRAGMA user_version")[0] == SCHEMA_VERSION,
        f"schema version is {one('PRAGMA user_version')[0]}, not {SCHEMA_VERSION}",
    )

    meta = dict(db.execute("SELECT key, value FROM meta"))

    check(
        meta.get("schema_version") == str(SCHEMA_VERSION),
        f"meta.schema_version is {meta.get('schema_version')!r}",
    )

    # No prose, and the corpus says so. A reader asked for texts has to be able
    # to refuse rather than silently hand back modules carrying none.
    check(meta.get("texts") == "0", f"meta.texts is {meta.get('texts')!r}")

    # Every table and index the schema specifies. A missing one is a reader
    # that raises on its first query rather than at open.
    present = {
        (row[0], row[1])
        for row in db.execute("SELECT type, name FROM sqlite_master")
    }

    for table in ("meta", "module", "type", "node", "symbol", "import", "oid_index"):
        check(("table", table) in present, f"table {table} is missing")

    for index in ("node_by_module", "node_by_name"):
        check(("index", index) in present, f"index {index} is missing")

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

    check_ordering(db)
    check_referential(db)

    # Integrity last: it reads the whole file, so everything cheaper has had
    # its say by the time this runs.
    integrity = one("PRAGMA integrity_check")[0]
    check(integrity == "ok", f"integrity_check: {integrity}")


def check_ordering(db):
    """That ``oid_key`` orders bytewise the way OIDs order numerically.

    Nothing about a mis-ordered key raises. A walk simply visits nodes in an
    order that is not OID order, which reads as a MIB defect rather than as an
    encoding defect, so it is worth a direct check on real data.
    """
    start = db.execute(
        "SELECT oid_key FROM node WHERE oid = ? LIMIT 1", ("1.3.6.1.2.1.2.2.1.1",)
    ).fetchone()

    if not check(start, "IF-MIB::ifIndex is not in the corpus"):
        return

    walk = [
        row[0]
        for row in db.execute(
            "SELECT DISTINCT oid FROM node WHERE oid_key > ? ORDER BY oid_key LIMIT 2",
            (start[0],),
        )
    ]

    check(
        walk == ["1.3.6.1.2.1.2.2.1.2", "1.3.6.1.2.1.2.2.1.3"],
        f"GETNEXT from ifIndex gave {walk}",
    )

    # The whole corpus, in the order the key imposes, must be the order the
    # arcs impose. This is the check that catches string comparison (1.3.10
    # below 1.3.9) and single-byte arcs (256 lost), on every OID rather than
    # on a chosen few.
    previous = None
    misordered = 0

    for (oid,) in db.execute("SELECT DISTINCT oid FROM node ORDER BY oid_key"):
        arcs = tuple(int(x) for x in oid.split("."))

        if previous is not None and arcs < previous:
            misordered += 1

        previous = arcs

    check(misordered == 0, f"{misordered} nodes are out of OID order by oid_key")


def check_referential(db):
    """That nothing points at a row that is not there.

    A node naming a module the corpus lacks is an OID that resolves to
    something a consumer then cannot load -- which is how the published index
    came to name modules the site answers 404 for.
    """
    for table in ("node", "oid_index"):
        orphans = db.execute(
            f"SELECT count(*) FROM {table} "  # noqa: S608
            "WHERE module NOT IN (SELECT name FROM module)"
        ).fetchone()[0]
        check(orphans == 0, f"{orphans} {table} rows name a module the corpus lacks")

    dangling = db.execute(
        "SELECT count(*) FROM node WHERE syntax IS NOT NULL "
        "AND syntax NOT IN (SELECT id FROM type)"
    ).fetchone()[0]
    check(dangling == 0, f"{dangling} nodes reference a missing type row")

    # Scalars and columns carry a syntax. Anything else is a node a runtime
    # cannot render a value for, and a reader must refuse rather than guess.
    untyped = db.execute(
        "SELECT count(*) FROM node "
        "WHERE nodetype IN ('scalar', 'column') AND syntax IS NULL"
    ).fetchone()[0]
    check(untyped == 0, f"{untyped} scalars or columns have no syntax")

    # The hash is what says two corpora agree on a module; a NULL one silently
    # means "cannot tell".
    unhashed = db.execute(
        "SELECT count(*) FROM module WHERE content_hash IS NULL OR content_hash = ''"
    ).fetchone()[0]
    check(unhashed == 0, f"{unhashed} modules carry no content hash")

    bad = db.execute(
        "SELECT count(*) FROM module "
        "WHERE tier NOT IN ('standard', 'draft', 'vendor')"
    ).fetchone()[0]
    check(bad == 0, f"{bad} modules carry a tier outside the vocabulary")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "output-db")
