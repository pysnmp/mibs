# mibs

This MIB Repository is based on the original repository provided by snmplabs with updates from the mib collection from librenms.

In Addition an index is published allowing remote clients to identify a mib based on OID alone. All hosted on github pages.

pysnmplib (formerly pysnmp) applications can retrieve mibs from `https://pysnmp.github.io/mibs/asn1/@mib@`

## What is here

MIB **content**, and the configuration that says how to build it. The build
itself is [pysmi](https://github.com/pysnmp/pysmi)'s `mibcorpus`, so this
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

Adding a MIB is a file drop under `src/vendor/<vendor>/` and a CI run.

## Building

```
make corpus           # the published corpus, into output/
make corpus-compact   # the same corpus without the standard modules
make corpus-db        # the corpus database, into output-db/
```

Each is one `mibcorpus` invocation over a manifest. Two runs over the same
sources produce the same bytes, with no network access; `output/report.json`
records what was built, what failed to compile, and how long it took.

## The two corpora

**The published corpus** carries the standard modules, because its consumers
fetch them from it: splunk-connect-for-snmp resolves `asn1/@mib@` against this
site for every module it meets. This is what gh-pages serves and what the
`mibserver` chart mounts.

**The compact corpus** is the same source set with the standard namespace
declared `"publish": false` — a resolution source rather than a published one.
It carries only what a runtime that already has the standard modules does not
have, since pysmi bundles 210 of them and its wheel ships their compiled form.
Each module in it is byte-identical to the same module in the published corpus.
It is not served over HTTP; it is published as an image to mount:

```
ghcr.io/pysnmp/mibs/corpus-compact:<version>
```

## The corpus database

`core.db` is the same source set a third way: the SMI model as data, one row
per node, keyed for lookup by OID and by name and ordered so a GETNEXT walk is
a range query. pysnmp reads it with stdlib `sqlite3` and no pysmi import; the
file format is specified in pysmi's `corpus-schema` document.

It exists because of two questions `index-v2.csv` cannot answer. The index is
`MODULE,OID` and carries a module's *anchors*, so it says which module to load
and nothing else — a leaf like `ifDescr` is not in it at all, and getting from
an OID to a name, a syntax and an access level still means compiling the
module's ASN.1 or parsing its whole JSON document. And an anchor index has no
per-node ordering, so a walk cannot be served from one. Both are one indexed
row here.

Measured on the corpus this repository builds:

| | |
|---|---|
| modules | 5,510 |
| nodes | 767,870 |
| distinct type specifications | 47,226 |
| indexed OIDs | 98,867 |
| size | 256 MB, 36 MB gzipped |
| build | one `mibcorpus` invocation, ~5 minutes |

**Built from `corpus.json`, not the compact manifest.** The compact corpus
leaves the standard modules out because a runtime that has pysmi already holds
them as Python — but a database is consulted *by OID*, and one missing
`1.3.6.1.2.1` cannot resolve `ifDescr` for anybody. There is one corpus; vendor
is a column in it rather than a partition of it.

**No prose.** No DESCRIPTION, no REFERENCE. They are about a third of a
generated module's bytes, pysnmp discards them under the default
`loadTexts=False`, and `json/` already serves the one consumer that wants them
— a MIB browser. A second database for prose would be the largest thing this
repository publishes and would duplicate a channel that already works.

## Three channels, three shapes

What each channel carries follows from who consumes it, so they are not the
same set:

| | carries | for |
|---|---|---|
| **gh-pages** | `asn1/`, `json/`, `index.csv` (deprecated), `index-v2.csv`, `standard.txt` | anyone resolving a MIB over HTTP |
| **Release archives** | one zip per format | an offline or air-gapped install, or a build that vendors the corpus |
| **`corpus` image** | what gh-pages serves | the `mibserver` chart, which mounts it and serves it — so it has to answer the same paths the site does |
| **`corpus-compact` image** | `asn1/` and `index-v2.csv` | a pysnmp runtime — what it needs to poll and to translate a trap OID, and nothing more |

The release archives are attached to each GitHub release:

| asset | |
|---|---|
| `mibs-asn1.zip` | the MIB sources |
| `mibs-json.zip` | the same modules as data |
| `mibs-index.zip` | `index.csv`, `index-v2.csv`, `standard.txt` |
| `mibs-compact.zip` | the compact corpus |
| `mibs-core-db.zip` | the corpus database |

The two images differ because they are consumed differently. `corpus-compact`
is a dependency a runtime mounts, so it carries the two things a runtime reads:
the ASN.1 it compiles, and the index that says which module answers for an OID.
`json/` is data for other tooling and `standard.txt` is a compatibility surface
of the published corpus; pysnmp reads neither.

`corpus` is not a dependency — it is the document root the chart hands to nginx,
so it mirrors the site. Trimming it would 404 endpoints the chart itself
advertises: splunk-connect-for-snmp's deployment sets `MIB_STANDARD` to
`standard.txt` on the service this chart provides.

## What is published, and what is not

| | |
|---|---|
| `asn1/<MODULE>` | the MIB source, under its bare module name |
| `json/<MODULE>.json` | the same module as data — names, OIDs, syntax, access, status |
| `index.csv` | **deprecated** — OID to module, one row per OID; replays `index-frozen.csv` |
| `index-v2.csv` | the same index without the frozen answers |
| `standard.txt` | the standard module names |

Some modules the site used to serve are no longer carried anywhere, so
`asn1/NAME` and `json/NAME.json` return 404 for them while `index.csv` still
names them. [`docs/absent-modules.md`](docs/absent-modules.md) lists all 194,
grouped by why each went and what it would take to bring it back.

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

Migration is pysnmp/mibs#366 and the retirement window is pysnmp/mibs#325;
neither file goes away before that has shipped and been taken up. New
consumers should read `core.db`, or `index-v2.csv` if they want a text file.

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

## Images

| Image | What it is |
|---|---|
| `ghcr.io/pysnmp/mibs/corpus` | the published corpus, `FROM scratch` — no base, no shell, nothing to patch |
| `ghcr.io/pysnmp/mibs/corpus-compact` | the compact corpus, likewise |
| `ghcr.io/pysnmp/mibs/corpus-db` | `core.db` alone, likewise — what a pysnmp runtime mounts |
| `ghcr.io/pysnmp/mibs/tools` | pysmi on an upstream Python base, for the chart's local-MIB init container |

The corpus images hold the build output and nothing else, so they are mounted
rather than run. `ghcr.io/pysnmp/mibs/container` — nginx with the corpus baked
into it — is no longer published; the chart deploys upstream nginx and mounts
the corpus image instead.

## Helm chart

Install from the OCI registry:

```
helm install mibserver oci://ghcr.io/pysnmp/charts/mibserver --version 1.17.0
```

> **Deprecated:** the classic chart repository at `https://pysnmp.github.io/mibs/charts`
> (`helm repo add`) is being retired. Existing versions remain downloadable, but new releases
> are published to the OCI registry above. Migrate to `oci://ghcr.io/pysnmp/charts`.

### Kubernetes 1.33 or newer

The chart mounts the corpus as an [image
volume](https://kubernetes.io/docs/concepts/storage/volumes/#image). The
chart's `kubeVersion` refuses anything below 1.33, but **the version check is
not sufficient on its own** — on 1.33 and 1.34 the feature ships beta and
*disabled*:

| Kubernetes | `ImageVolume` |
|---|---|
| 1.33, 1.34 | beta, **off by default** — enable the gate on the API server *and* the kubelet |
| 1.35 | beta, on by default |
| 1.36+ | stable |

The runtime has to implement it too: containerd 2.1+ (2.0 has no support at
all) and CRI-O 1.33+ for the beta surface — CRI-O 1.31 carries only the
original alpha.

Below 1.35 with the gate left at its default, `helm install` succeeds and the
pod then fails to start, because a version constraint is all a chart can
express. If that is your cluster, enable the gate before installing.

What this buys: the container serving MIBs is `nginxinc/nginx-unprivileged`
from upstream, unmodified. This project no longer publishes an nginx image, so
an nginx CVE is upstream's to fix and yours to pick up by bumping
`image.tag` — not something that waits on a release here. The endpoints, ports
and paths are unchanged.

### Local MIBs

`localMibs.pathToMibs` and `localMibs.persistence.existingClaim` work as
before: point either at your own MIB sources and they are served beside the
published corpus, and indexed into `index.csv` with it.

What changed is where the compile happens. An init container runs `mibcorpus`
over the supplied sources, resolving them against the published corpus, and
writes what it produced into an `emptyDir` the serving container reads. Nothing
compiles inside the nginx container, and its root filesystem is read-only in
every configuration.

The published corpus wins where both hold a module: the overlay adds to what
this deployment serves rather than replacing it.

## IPv6 listeners

IPv6 listener support is disabled by default. Enabling it adds IPv6 listeners while preserving the existing IPv4 listeners on both endpoints:

- MIB content: TCP/8000
- NGINX status and readiness: TCP/8080

The listeners are rendered into the chart's `nginx.conf` from `ipv6Enabled`, so
the config a pod runs is complete as deployed and nothing rewrites it at
start-up.
