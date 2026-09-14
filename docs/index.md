# The pysnmp MIB distribution

This site publishes the MIB modules that pysnmp and other SNMP tooling resolve
against: 5,510 modules as ASN.1 source and as JSON, with OID indexes and a
SQLite model of the whole corpus. Fetch them over HTTPS, unpack them from a
release archive, or mount them as an OCI image.

[MIBs Depot](https://mibsdepot.com/browse/) publishes the same corpus as pages
to read: one per module, one per OID arc, one per registrant, including the
DESCRIPTION text that the files carry and no browser renders. Use it to look a
MIB up; use this site to fetch one.

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

`@mib@` is pysmi's placeholder for the module name. It is not part of a URL you
open in a browser.

The source list is ordered and the first hit wins. Put a local directory ahead
of the URL to override a module or to compile without network access.

[Resolving MIBs](using.md) covers polling by name, translating a trap,
and overriding a module with a local copy. [Getting the MIBs](channels.md) covers
getting the modules by means other than HTTPS. The {docs}`pysnmp` documentation
covers what to do with a resolved name.

## What is published

| path | contents |
|---|---|
| `asn1/<MODULE>` | the MIB source, under its bare module name |
| `json/<MODULE>.json` | the same module as data: names, OIDs, syntax, access, status |
| `index-v2.csv` | OID to module, one row per OID |
| `index.csv` | **deprecated.** The frozen predecessor of `index-v2.csv`. See [the indexes](channels.md#the-indexes) |
| `standard.txt` | the standard module names |
| `core.db` | the SMI model as a SQLite database. See [the corpus database](corpora.md#the-corpus-database) |

This site serves no HTML listing of `asn1/` or `json/`. Programs index the
corpus with `index-v2.csv` and `core.db`, both published here. Readers index it
at [MIBs Depot](https://mibsdepot.com/browse/), which renders a page per module
and per OID arc from the same build.

194 modules that this site once served are no longer carried anywhere.
[Removed modules](absent-modules.md) lists them, grouped by the reason each was
dropped and what restoring it would take.

## What is in the repository

MIB content, and the configuration that describes how to build it. The build
itself is {docs}`pysmi <pysmi>`'s `mibcorpus`. This repository holds no
compiler, no dependency resolver and no OID indexer. It held versions of all
three until {issue}`365`; each was a second implementation of pysmi's and each
had drifted from it.

| path | contents |
|---|---|
| `src/vendor/*` | the MIB sources, one directory per vendor |
| `corpus.json` | the source set the published corpus is built from |
| `corpus-compact.json` | the same source set, without the standard modules |
| `index-frozen.csv` | the OID index snapshot `index.csv` replays |
| `charts/mibserver` | the Helm chart |
| `docker/` | the images: the corpus, and pysmi for the chart's init container |

To add a MIB, drop the file under `src/vendor/<vendor>/` and open a pull
request. See [contributing](contributing.md).

## Related projects

Four repositories make up the stack. pysnmp is the SNMP engine; this
distribution supplies the modules that let it name managed objects. pysmi and
pyasn1 sit underneath pysnmp, which loads them for you.

| project | role |
|---|---|
| {docs}`pysnmp <pysnmp>` | the engine: SNMP v1, v2c and v3 as manager, agent or proxy |
| {docs}`pysmi <pysmi>` | the MIB compiler, and the `mibcorpus` driver that builds this distribution |
| {docs}`pyasn1 <pyasn1>` | the ASN.1 codec underneath both |

```{toctree}
:maxdepth: 2
:hidden:

Browse the MIBs <https://mibsdepot.com/browse/>
using
channels
corpora
manifests
chart
deploying
contributing
absent-modules
mib-sources
registries
```
