# mibs

The MIB distribution for [pysnmp](https://pysnmp.github.io/pysnmp/): thousands
of MIB modules, published live over HTTPS, as release archives and as OCI
images, so an SNMP engine can name a managed object instead of counting OID
arcs.

**Documentation: <https://pysnmp.github.io/mibs/>**

pysnmp applications resolve modules straight from the site:

```
https://pysnmp.github.io/mibs/asn1/@mib@
```

`@mib@` is pysmi's placeholder for the module name. The other two channels, and
what each carries, are in
[Channels](https://pysnmp.github.io/mibs/channels.html).

## What is here

MIB **content**, and the configuration that says how to build it. The build
itself is [pysmi](https://pysnmp.github.io/pysmi/)'s `mibcorpus`, so this
repository holds no compiler, no dependency resolver and no OID indexer of its
own — the ones it used to hold were second implementations of pysmi's, and each
had drifted from it (pysnmp/mibs#365).

| | |
|---|---|
| `src/vendor/*` | the MIB sources, one directory per vendor |
| `corpus.json` | the source set the published corpus is built from |
| `corpus-compact.json` | the same source set, without the standard modules |
| `index-frozen.csv` | the OID index snapshot `index.csv` replays |
| `charts/mibserver` | the Helm chart |
| `docker/` | the images: the corpus, and pysmi for the chart's init container |
| `docs/` | this project's documentation, and the Sphinx project that builds it |

Adding a MIB is a file drop under `src/vendor/<vendor>/` and a CI run. See
[Contributing a module](https://pysnmp.github.io/mibs/contributing.html).

## Building

```
make corpus           # the published corpus, into output/
make corpus-compact   # the same corpus without the standard modules
make corpus-db        # the corpus database, into output-db/
```

Each is one `mibcorpus` invocation over a manifest. Two runs over the same
sources produce the same bytes, with no network access; `output/report.json`
records what was built, what failed to compile, and how long it took. The
manifest format is documented in
[Manifests and the build](https://pysnmp.github.io/mibs/manifests.html).

The documentation is a uv project of its own under `docs/`, because the corpus
build is pinned to the interpreter its output is fingerprinted on and current
Sphinx needs a newer one:

```
uv run --directory docs --locked --group dev sphinx-build -n -W --keep-going -b html . _build
```

CI builds it on every ref and deploys it to the site root beside the corpus, so
the documentation for a channel and the channel itself ship together.

## Where this sits

Four repositories, one stack.

| | |
|---|---|
| [pysnmp](https://pysnmp.github.io/pysnmp/) | the engine — SNMP v1, v2c and v3 as manager, agent or proxy |
| **mibs** | this distribution — what lets the engine say `ifOperStatus` rather than `.1.8.1` |
| [pysmi](https://pysnmp.github.io/pysmi/) | the MIB compiler, and the `mibcorpus` driver that builds this distribution |
| [pyasn1](https://pysnmp.github.io/pyasn1/) | the ASN.1 codec underneath both |

These are maintained forks of Ilya Etingof's original work. Ilya passed away on
10 August 2022; his work remains of great use to the Python community.

BSD-2-Clause. See [LICENSE](LICENSE).
