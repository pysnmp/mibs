# The pysnmp MIB distribution

SNMP names things in MIB modules. Without the module that defines it, an agent
answering `1.3.6.1.2.1.2.2.1.8.1` tells you the value is `2`; with it, the same
answer reads `IF-MIB::ifOperStatus.1 = down`. This is where the pysnmp
organization publishes those modules.

It is a distribution, though not one `pip` resolves. You can use it live over
HTTPS or install it locally, and the content is the same either way.

## Resolving a MIB

pysnmp applications point pysmi at the published tree:

```python
from pysnmp.smi import builder, compiler, view

mibBuilder = builder.MibBuilder()
compiler.addMibCompiler(
    mibBuilder, sources=["https://pysnmp.github.io/mibs/asn1/@mib@"]
)
mibBuilder.loadModules("IF-MIB")
mibView = view.MibViewController(mibBuilder)
```

`@mib@` is pysmi's placeholder for the module name, not part of any URL you
would open. The source list is ordered and the first hit wins, so putting a
local directory in front of it is how you override a module or work offline.

[Using the distribution](using.md) covers polling by name, translating a trap
and overriding a module with a local copy; [channels](channels.md) covers
getting the modules somewhere other than over HTTPS. The {docs}`pysnmp` covers
what to do with a resolved name.

## What is published

| | |
|---|---|
| `asn1/<MODULE>` | the MIB source, under its bare module name |
| `json/<MODULE>.json` | the same module as data — names, OIDs, syntax, access, status |
| `index-v2.csv` | OID to module, one row per OID |
| `index.csv` | **deprecated** — the frozen predecessor of `index-v2.csv`; see [the index](channels.md#the-indexes) |
| `standard.txt` | the standard module names |
| `core.db` | the SMI model as a SQLite database; see [the corpus database](corpora.md#the-corpus-database) |

There is no HTML index over `asn1/` or `json/`: the trees are generated and a
listing of several thousand files would help nobody. What indexes the corpus is
`index-v2.csv` and `core.db`, and both are published. Browse
{repo}`mibs` to see what the sources are.

Some modules the site used to serve are no longer carried anywhere.
[Absent modules](absent-modules.md) lists all 194, grouped by why each went and
what it would take to bring it back.

## What is here

MIB **content**, and the configuration that says how to build it. The build
itself is {docs}`pysmi <pysmi>`'s `mibcorpus`, so this
repository holds no compiler, no dependency resolver and no OID indexer of its
own — the ones it used to hold were second implementations of pysmi's, and each
had drifted from it ({issue}`365`).

| | |
|---|---|
| `src/vendor/*` | the MIB sources, one directory per vendor |
| `corpus.json` | the source set the published corpus is built from |
| `corpus-compact.json` | the same source set, without the standard modules |
| `index-frozen.csv` | the OID index snapshot `index.csv` replays |
| `charts/mibserver` | the Helm chart |
| `docker/` | the images: the corpus, and pysmi for the chart's init container |

Adding a MIB is a file drop under `src/vendor/<vendor>/` and a CI run — see
[contributing](contributing.md).

## Where this sits

Four repositories, one stack. pysnmp is the engine and this distribution is
what lets it talk about managed objects by name; pysmi and pyasn1 sit
underneath and pysnmp reaches them for you.

| | |
|---|---|
| {docs}`pysnmp <pysnmp>` | the engine — SNMP v1, v2c and v3 as manager, agent or proxy |
| {docs}`pysmi <pysmi>` | the MIB compiler, and the `mibcorpus` driver that builds this distribution |
| {docs}`pyasn1 <pyasn1>` | the ASN.1 codec underneath both |

```{toctree}
:maxdepth: 2
:hidden:

using
channels
corpora
manifests
chart
contributing
absent-modules
mib-sources
```
