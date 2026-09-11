# Channels

Three ways to get the same content, chosen by how you consume it rather than
by what they carry.

| | carries | for |
|---|---|---|
| **The site** (`pysnmp.github.io/mibs/`) | `asn1/`, `json/`, `index.csv` (deprecated), `index-v2.csv`, `standard.txt`, and this documentation | anyone resolving a MIB over HTTPS |
| **Release archives** | one zip per format | an offline or air-gapped install, or a build that vendors the distribution |
| **`corpus` image** | what the site serves | the [`mibserver` chart](chart.md), which mounts it and serves it — so it has to answer the same paths the site does |
| **`corpus-compact` image** | `asn1/` and `index-v2.csv` | a pysnmp runtime — what it needs to poll and to translate a trap OID, and nothing more |

## Live over HTTPS

One module per request, which is what pysmi fetches from by default:

```
https://pysnmp.github.io/mibs/asn1/IF-MIB
https://pysnmp.github.io/mibs/json/IF-MIB.json
```

Nothing to install and nothing to keep current. It needs egress from wherever
the compile happens, which is the reason the other two channels exist.

## Installed from the archive

Every release attaches the same content as zips, for build systems and
air-gapped sites that would rather fetch once than reach out per module:

| asset | |
|---|---|
| `mibs-asn1.zip` | the MIB sources |
| `mibs-json.zip` | the same modules as data |
| `mibs-index.zip` | `index.csv`, `index-v2.csv`, `standard.txt` |
| `mibs-compact.zip` | the compact corpus |
| `mibs-core-db.zip` | the corpus database |

Unpack `mibs-asn1.zip` somewhere and name that directory as a pysmi source;
nothing else changes.

## Installed as an OCI image

To mount alongside a container that needs the modules without giving it egress:

| image | what it is |
|---|---|
| `ghcr.io/pysnmp/mibs/corpus` | the published corpus, `FROM scratch` — no base, no shell, nothing to patch |
| `ghcr.io/pysnmp/mibs/corpus-compact` | the [compact corpus](corpora.md#the-compact-corpus), likewise |
| `ghcr.io/pysnmp/mibs/corpus-db` | [`core.db`](corpora.md#the-corpus-database) alone, likewise — what a pysnmp runtime mounts |
| `ghcr.io/pysnmp/mibs/tools` | pysmi on an upstream Python base, for the chart's local-MIB init container |

The corpus images hold the build output and nothing else, so they are mounted
rather than run. `ghcr.io/pysnmp/mibs/container` — nginx with the corpus baked
into it — is no longer published; the chart deploys upstream nginx and mounts
the corpus image instead.

The two corpus images differ because they are consumed differently.
`corpus-compact` is a dependency a runtime mounts, so it carries the two things
a runtime reads: the ASN.1 it compiles, and the index that says which module
answers for an OID. `json/` is data for other tooling and `standard.txt` is a
compatibility surface of the published corpus; pysnmp reads neither.

`corpus` is not a dependency — it is the document root the chart hands to
nginx, so it mirrors the site. Trimming it would 404 endpoints the chart itself
advertises: splunk-connect-for-snmp's deployment sets `MIB_STANDARD` to
`standard.txt` on the service this chart provides.

## What is not published

**No compiled pysnmp modules.** `notexts/` and `texts/` used to carry them and
no longer exist. A pysnmp module is not data: it is Python that
`MibBuilder.loadModule()` runs through `exec()`, written to be executed rather
than imported — `mibBuilder` arrives as an injected global, which is why the
first line of one calls a name it never defines. Serving that over HTTP hands
every consumer a way to execute code fetched from this site, authenticated by
nothing but TLS. Compromise the site or the transport and you have arbitrary
code in every process that loads a MIB.

Nothing needed them. pysnmp resolves MIBs from local directories by default and
ships no remote source; splunk-connect-for-snmp binds `MIB_SOURCES` to
`asn1/@mib@` and compiles with pysmi. **Pull the MIB and compile it** — that is
the safe shape, and it is what consumers already do. Where a compiled form was
wanted only to avoid running a compiler, `json/` carries the same facts in a
format that is parsed rather than run.

The two trees were about half the corpus: 603 MB of 1237 MB.

```{warning}
The same reasoning applies to a MIB you supply yourself. A module compiled by
pysmi becomes Python that pysnmp imports, so treat an ASN.1 MIB source the way
you would treat any other code you are about to run, and compile from somewhere
you trust.
```

## The indexes

`index-v2.csv` maps OID to module, one row per OID. It carries a module's
*anchors*, so it says which module to load and nothing else.

`core.db` answers what an anchor index cannot — a leaf like `ifDescr`, a
syntax, an access level, and the ordering a GETNEXT walk needs. See
[the corpus database](corpora.md#the-corpus-database).

### `index.csv` is deprecated

It keeps being published and keeps replaying `index-frozen.csv`, so nothing
that reads it breaks today. What has changed is that it has a successor and no
longer has a reason to grow one.

`index.csv` exists to preserve answers it has already given, including the ones
now known to be wrong — that is what makes it a freeze rather than a stale
copy. Corrections have always landed in `index-v2.csv`. So the file is, by
construction, the one artifact here that is allowed to be incorrect, and it is
the one a consumer keying on it is most likely to be reading.

It has exactly one known consumer, splunk-connect-for-snmp, which parses it
into a `mib_map` and walks an arriving OID's tail against it, longest prefix
first, to decide which module to load and compile. Every part of that is now
better served by `core.db`:

| what sc4snmp does with `index.csv` | with `core.db` |
|---|---|
| parse the CSV into a dict at startup | open the file; no parse, no resident copy |
| chop the OID against `mib_map` | `find_module()`, one indexed query per arc |
| compile the named module's ASN.1 on the trap path | read the node's row |
| — | `next_node()`, which the index cannot answer at all |

Migration is {issue}`366` and the retirement window is {issue}`325`; neither
file goes away before that has shipped and been taken up. New consumers should
read `core.db`, or `index-v2.csv` if they want a text file.
