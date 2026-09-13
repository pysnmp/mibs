# The IANA registries this corpus names OID arcs from

An OID tree is only useful if it says what each arc *is*. Until now this
repository had one source for that: whichever MIB happened to mention an
arc on its way somewhere else. That gets the arcs a module actually
registers right, and gets the arcs above them wrong.

Measured against this corpus:

| arc | is | was attributed to |
|---|---|---|
| `1.3` | `identified-organization` | `OCCAM-ETHERLIKE-MIB` |
| `1.3.6` | `dod` | `OCCAM-ETHERLIKE-MIB` |
| `1.3.6.1.6` | `snmpv2` | `RAPID-CITY` |
| `1.3.6.1.6.3` | `snmpModules` | `RAPID-CITY` |

A tree that says `snmpModules` belongs to a Nortel enterprise MIB is wrong
in a way that matters, and no ranking over MIB text can fix it, because
the fact is not in the MIB text. And nothing at all names a bare
enterprise arc: no module registers `1.3.6.1.4.1.9`, only what hangs
beneath it.

Two IANA registries answer both, and both are committed here:

| file | what it is |
|---|---|
| `registries/smi-numbers.xml` | IANA's SMI Numbers registry, whole. 1,076 arcs, naming the `1.3.6.1` subtree. |
| `registries/pen-snapshot.csv` | The Private Enterprise Numbers registry, reduced to the arcs this corpus uses. 360 registrants. |
| `registries/enterprise-arcs.txt` | Which arcs those are: the input to the reduction. |

## Why committed rather than fetched

`pysmi`'s corpus driver opens on a property: *a build with the network
unplugged produces the same corpus as one without*. The enterprise
registry changes daily. Fetching either at build time would end that
property, and two builds of the same sources would stop agreeing — the
same class of defect as the shell pipeline that resolved missing
dependencies from its own last publish.

So the registries are inputs, the same way a MIB is. `make corpus` and
the CI build both pass them with `--oid-registry`.

## Why the PEN snapshot is reduced

IANA publishes 66,807 registrations in a 5.1 MB file. This corpus reaches
361 enterprise arcs. Committing the whole registry would mean a ~4 MB CSV
and a monthly diff of the entire thing, most of it about vendors no module
here has ever mentioned.

The cost of reducing is staleness: a module arriving later under an arc
the snapshot predates has no registrant, and its page renders nameless.
That is not silent. Two things say so:

- `scripts/update_registries.py --validate` — offline, run on every pull
  request. Compares the committed arc list against `index-frozen.csv` and
  the committed snapshot against that list.
- the corpus build itself — pysmi reports `unregistered` in `entity.json`
  and warns naming the numbers.

Today that is one arc: **1004849**, which `DAHUA-SNMP-MIB` registers
under and IANA has no registration for. The snapshot is not stale; the
registry has a hole.

## Which arcs, and why from two indexes

`registries/enterprise-arcs.txt` is the union of the arcs reached by
`index-frozen.csv` and by the build's `index-v2.csv`. The two do not
agree — the ranked index reaches ten arcs the frozen one does not, and
the frozen one replays five the corpus no longer compiles a module for.
Both are published, so a reader resolving an OID through either should
reach a named registrant.

## Refreshing them

```sh
# Offline. Does the committed snapshot still cover the committed index?
uv run python scripts/update_registries.py --validate

# What the monthly sweep runs: re-fetch and report what has moved.
uv run python scripts/update_registries.py --check

# Take the new registries. Run `make corpus` first if the corpus has
# gained modules, so the arc list picks up the arcs they reach.
uv run python scripts/update_registries.py --update
```

`--check` runs in [the monthly
workflow](https://github.com/pysnmp/mibs/blob/main/.github/workflows/mib-freshness.yml)
beside the MIB sweep, for the same reason: the registries have a
publisher and a baseline in exactly the same sense the MIBs do. Nothing
there writes to the repository — a registry revision is a change somebody
reviews, not one a robot lands.

Because the enterprise registry moves daily, `--check` will usually report
that `pen-snapshot.csv` differs. What it is saying is "the reduced
snapshot is a month behind", which is the state this file exists to
surface rather than a problem to fix the same day.
