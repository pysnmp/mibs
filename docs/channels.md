# Channels

Five ways to obtain the corpus. They carry the same content; choose by how you
consume it.

| channel | carries | use when |
|---|---|---|
| **Distribution site** (`pysnmp.github.io/mibs/`) | `asn1/`, `json/`, `index.csv` (deprecated), `index-v2.csv`, `standard.txt`, this documentation | a program resolves MIBs over HTTPS |
| **MIBs Depot** (`mibsdepot.com`) | every module, OID arc and registrant as a page, plus the files above | a person is looking a MIB up |
| **Release archives** | one zip per format | installing offline or air-gapped, or vendoring the distribution into a build |
| **`corpus` image** | what the distribution site serves | the [`mibserver` chart](chart.md) mounts and serves it, so it answers the same paths as the site |
| **`corpus-compact` image** | `asn1/` and `index-v2.csv` | a pysnmp runtime needs to poll and translate trap OIDs, and nothing more |

## Live over HTTPS

One module per request. This is what pysmi fetches from by default:

```
https://pysnmp.github.io/mibs/asn1/IF-MIB
https://pysnmp.github.io/mibs/json/IF-MIB.json
```

Nothing to install and nothing to keep current. It requires egress from
wherever the compile runs. The other channels exist for environments that have
none.

**This URL is stable.** pysnmp's documentation names
`https://pysnmp.github.io/mibs/asn1/@mib@` as the remote source to add, and
splunk-connect-for-snmp binds `MIB_SOURCES` to it. Both are in released
software that will not be re-released to follow a redirect. The distribution
site continues to serve what it serves today.

## The two sites

The corpus is published twice, to two hosts, for two kinds of reader.

| site | serves |
|---|---|
| [`pysnmp.github.io/mibs/`](https://pysnmp.github.io/mibs/) | the files, and this documentation. What a program fetches. |
| [`mibsdepot.com`](https://mibsdepot.com/browse/) | the corpus as pages to read: one per module, one per OID arc, one per registrant, including the DESCRIPTION text that the files carry and no browser renders |
| [`data.mibsdepot.com`](https://data.mibsdepot.com) | the depot's copy of the files, so that a link on a depot page resolves without crossing to the other site |

One build writes all three. `corpus.json` declares a publication per
destination, and `mibcorpus` writes them from a single parse of the 5,510
modules, so the three trees cannot disagree about what a module contains. CI
also compares the two data trees artifact by artifact and fails if they differ.

The split across two hosts follows a file-count limit. The browsable site is
7,430 files of HTML; the files beside it are another 11,025. A host that
resolves a directory URL to its `index.html` without running code serves at
most 20,000 files on the free plan. Pages that need that resolution go to the
host that performs it; files addressed by exact name go to object storage,
where the file count is not capped. See
[the corpora](corpora.md#where-each-tree-goes).

## Installed from the archive

Every release attaches the same content as zip files, for build systems and
air-gapped sites that fetch once rather than per module:

| asset | contents |
|---|---|
| `mibs-asn1.zip` | the MIB sources |
| `mibs-json.zip` | the same modules as data |
| `mibs-index.zip` | `index.csv`, `index-v2.csv`, `standard.txt` |
| `mibs-compact.zip` | the compact corpus |
| `mibs-core-db.zip` | the corpus database |

Unpack `mibs-asn1.zip` and name that directory as a pysmi source. Nothing else
changes.

## Installed as an OCI image

Mount these alongside a container that needs the modules without egress:

| image | contents |
|---|---|
| `ghcr.io/pysnmp/mibs/corpus` | the published corpus, `FROM scratch`: no base image, no shell, nothing to patch |
| `ghcr.io/pysnmp/mibs/corpus-compact` | the [compact corpus](corpora.md#the-compact-corpus), likewise |
| `ghcr.io/pysnmp/mibs/corpus-db` | [`core.db`](corpora.md#the-corpus-database) alone, likewise. This is what a pysnmp runtime mounts |
| `ghcr.io/pysnmp/mibs/tools` | pysmi on an upstream Python base, for the chart's local-MIB init container |

The corpus images hold build output and nothing else, so they are mounted
rather than run. `ghcr.io/pysnmp/mibs/container`, which was nginx with the
corpus baked in, is no longer published. The chart deploys upstream nginx and
mounts the corpus image instead.

The two corpus images differ because they are consumed differently.
`corpus-compact` is a dependency that a runtime mounts, so it carries the two
things a runtime reads: the ASN.1 it compiles, and the index that says which
module answers for an OID. pysnmp reads neither `json/`, which is data for
other tooling, nor `standard.txt`, which is a compatibility surface of the
published corpus.

`corpus` is the document root the chart hands to nginx, so it mirrors the site.
Trimming it would return 404 for endpoints the chart advertises:
splunk-connect-for-snmp's deployment sets `MIB_STANDARD` to `standard.txt` on
the service this chart provides.

## What is not published

**No compiled pysnmp modules.** The `notexts/` and `texts/` trees carried them
and no longer exist.

A compiled pysnmp module is not data. It is Python that
`MibBuilder.loadModule()` passes to `exec()`, written to be executed rather
than imported: `mibBuilder` arrives as an injected global, which is why the
first line of such a module calls a name it never defines. Serving those over
HTTP would give every consumer a way to execute code fetched from this site,
authenticated by nothing but TLS. An attacker who compromised the site or the
transport would have arbitrary code execution in every process that loads a
MIB.

Nothing required them. pysnmp resolves MIBs from local directories by default
and ships no remote source. splunk-connect-for-snmp binds `MIB_SOURCES` to
`asn1/@mib@` and compiles with pysmi. Pull the MIB and compile it. Where a
compiled form was wanted only to avoid running a compiler, `json/` carries the
same facts in a format that is parsed rather than executed.

The two trees were 603 MB of a 1,237 MB corpus.

```{warning}
The same reasoning applies to a MIB you supply yourself. A module compiled by
pysmi becomes Python that pysnmp executes. Treat an ASN.1 MIB source as code
you are about to run, and compile only from a source you trust.
```

## The indexes

`index-v2.csv` maps OID to module, one row per OID. It carries a module's
anchors, so it identifies the module to load and nothing further.

`core.db` answers what an anchor index cannot: a leaf such as `ifDescr`, a
syntax, an access level, and the ordering a GETNEXT walk requires. See
[the corpus database](corpora.md#the-corpus-database).

### `index.csv` is deprecated

`index.csv` is still published and still replays `index-frozen.csv`, so nothing
that reads it breaks today. It has a successor, and it will not be extended.

The file exists to preserve answers it has already given, including answers now
known to be wrong. Preserving them is what makes it a freeze rather than a
stale copy.
Corrections land in `index-v2.csv`. By construction, `index.csv` is the one
artifact here permitted to be incorrect, and it is the one a consumer keying on
it is most likely to be reading.

It has one known consumer, splunk-connect-for-snmp, which parses it into a
`mib_map` and walks an arriving OID's tail against it, longest prefix first, to
decide which module to load and compile. `core.db` serves every part of that
better:

| what sc4snmp does with `index.csv` | with `core.db` |
|---|---|
| parse the CSV into a dict at startup | open the file: no parse, no resident copy |
| chop the OID against `mib_map` | `find_module()`, one indexed query per arc |
| compile the named module's ASN.1 on the trap path | read the node's row |
| not possible | `next_node()` |

Migration is tracked in {issue}`366` and the retirement window in {issue}`325`.
Neither file is withdrawn before that work has shipped and been taken up. New
consumers should read `core.db`, or `index-v2.csv` for a text format.
