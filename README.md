# mibs

The MIB distribution for [pysnmp](https://pysnmp.github.io/pysnmp/): 5,510 MIB
modules published over HTTPS, as release archives and as OCI images, so an SNMP
engine can name a managed object instead of counting OID arcs.

| | |
|---|---|
| Browse the MIBs | <https://mibsdepot.com/browse/> |
| Documentation | <https://pysnmp.github.io/mibs/> |

pysnmp applications resolve modules from the distribution site:

```
https://pysnmp.github.io/mibs/asn1/@mib@
```

`@mib@` is pysmi's placeholder for the module name. This URL does not change.

[MIBs Depot](https://mibsdepot.com/browse/) publishes the same corpus as pages
to read: one per module, one per OID arc, one per registrant, carrying the
DESCRIPTION text that the files hold and no browser renders. Both sites are
produced by one build. The other channels, and what each carries, are in
[Channels](https://pysnmp.github.io/mibs/channels.html).

## What is here

MIB content, and the configuration that describes how to build it. The build
itself is [pysmi](https://pysnmp.github.io/pysmi/)'s `mibcorpus`. This
repository holds no compiler, no dependency resolver and no OID indexer. It
held versions of all three until pysnmp/mibs#365; each was a second
implementation of pysmi's and each had drifted from it.

| path | contents |
|---|---|
| `src/vendor/*` | the MIB sources, one directory per vendor |
| `corpus.json` | the source set the published corpus is built from, and what it emits |
| `corpus-compact.json` | the same source set, without the standard modules |
| `corpus-db.json` | the same source set again, emitting only `core.db` |
| `index-frozen.csv` | the OID index snapshot `index.csv` replays |
| `charts/mibserver` | the Helm chart |
| `docker/` | the images: the corpus, and pysmi for the chart's init container |
| `docs/` | this project's documentation, and the Sphinx project that builds it |

To add a MIB, drop the file under `src/vendor/<vendor>/` and open a pull
request. See
[Contributing a module](https://pysnmp.github.io/mibs/contributing.html).

## Building

```
make corpus           # the published corpus, into output/
make corpus-compact   # the same corpus without the standard modules
make corpus-db        # the corpus database, into output-db/
```

Each target is one `mibcorpus` invocation over a manifest. Two runs over the
same sources produce the same bytes and neither needs network access.
`output/github-pages/report.json` records what was built, what failed to
compile, and how long it took. The manifest format is documented in
[Build manifests](https://pysnmp.github.io/mibs/manifests.html).

The documentation is a separate uv project under `docs/`. It needs a newer
interpreter than the corpus build, which is pinned to the one its output is
fingerprinted on:

```
uv run --directory docs --locked --group dev sphinx-build -n -W --keep-going -b html . _build
```

CI builds the documentation on every ref and deploys it to the root of both
sites, beside the corpus it describes.

## Related projects

Four repositories make up the stack.

| project | role |
|---|---|
| [pysnmp](https://pysnmp.github.io/pysnmp/) | the engine: SNMP v1, v2c and v3 as manager, agent or proxy |
| **mibs** | this distribution: the modules that let the engine say `ifOperStatus` rather than `.1.8.1` |
| [pysmi](https://pysnmp.github.io/pysmi/) | the MIB compiler, and the `mibcorpus` driver that builds this distribution |
| [pyasn1](https://pysnmp.github.io/pyasn1/) | the ASN.1 codec underneath both |

These are maintained forks of Ilya Etingof's original work. Ilya passed away on
10 August 2022; his work remains of great use to the Python community.

BSD-2-Clause. See [LICENSE](LICENSE).
