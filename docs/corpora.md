# Corpus variants

One source set is rendered three ways: the published corpus, the compact
corpus, and the corpus database. Choose by what the consumer already has.

## The published corpus

The published corpus carries the standard modules, because its consumers fetch
them from it: splunk-connect-for-snmp resolves `asn1/@mib@` against this site
for every module it encounters. This is what the site serves, what the release
archives contain, and what the [`mibserver` chart](chart.md) mounts.

## Where each tree goes

The published corpus goes to three places, and `corpus.json` names them as
three *publications* rather than as three builds:

| publication | destination | carries |
|---|---|---|
| `github-pages` | [`pysnmp.github.io/mibs/`](https://pysnmp.github.io/mibs/) | `asn1/`, `json/`, both indexes, `standard.txt`, this documentation |
| `depot-site` | [`mibsdepot.com`](https://mibsdepot.com/browse/) | the browsable pages, one per module, OID arc and registrant, and this documentation |
| `depot-data` | [`data.mibsdepot.com`](https://data.mibsdepot.com) | `asn1/`, `json/`, both indexes, `standard.txt`, `search.db` |

`mibcorpus` writes all three from one parse of the 5,510 modules. Parsing is
about three quarters of a pass, so three publications cost roughly what one and
a half builds would. More importantly, the three trees are projections of a
single parse rather than three runs that must be trusted to agree. CI compares
the two data trees artifact by artifact regardless, because a shared parse is a
claim and a `diff` is a check.

**Why the pages and the files are on different hosts.** Every link the site
generator writes is a directory URL, `../../mib/IF-MIB/`, which a host must
resolve to that directory's `index.html`. Object storage does not resolve it.
It serves the key it is given, so `/mib/IF-MIB/` returns 404 unless something
on the serving path rewrites it.

Static assets resolve it natively and run no script to do so. That distinction
decides the cost on a free plan: requests to a Worker's script are metered at
100,000 a day with cache hits counted, and requests to its assets are not.

Static assets are limited instead by file count: 20,000 per version. The
browsable pages are 7,430 of them. The 11,025 files beside them need no
resolution at all, and the per-module downloads still to come would add more.

So the split follows the constraint rather than the content: **pages that need
resolving go where resolving is free, and files addressed by exact name go
where the file count is not capped.** Nothing on a module page links into
`asn1/` or `json/`, so the two halves can sit on different hostnames without a
broken link between them.

**Why `pysnmp.github.io/mibs/` stays.** pysnmp's own docstrings name
`https://pysnmp.github.io/mibs/asn1/@mib@` as the remote MIB source to add, and
splunk-connect-for-snmp binds `MIB_SOURCES` to the same path. Those are in
released software. The distribution site keeps serving exactly what it serves
today; the depot is an addition, not a move.

### What the depot deploy needs

The GitHub Pages half deploys from the repository's own token and needs no
configuration. The depot half reads four secrets and one variable, set once;
[publishing the sites](deploying.md) is the procedure.

There is no switch among them. Holding the Cloudflare token is the decision to
publish, and the Worker's name is in `wrangler.jsonc`, so a repository that
has not been given credentials builds and checks all three trees and publishes
the one it can. Neither hostname is named in this repository.
`mibsdepot.com` is attached to the Worker and `data.mibsdepot.com` to the
bucket, each by hand in the Cloudflare dashboard. Nothing here claims a domain
it does not own, and a fork holding its own token publishes to its own.

## The compact corpus

The same source set with the standard namespace declared `"publish": false`,
making it a [resolution source](manifests.md) rather than a published one. It
carries only what a runtime that already holds the standard modules lacks:
pysmi bundles 210 of them and its wheel ships their compiled form. Each module
in it is byte-identical to the same module in the published corpus.

It is not served over HTTP; it is published as an image to mount:

```
ghcr.io/pysnmp/mibs/corpus-compact:<version>
```

`publish: false` is the only difference between the two manifests in this
repository. `corpus.json` and `corpus-compact.json` are otherwise identical,
which makes the compact corpus a subset of the published one rather
than a second rendering of it. pysmi holds that claim to account, in
`tests/test_corpus_publish_invariance.py`: it builds one source set twice, with
the standard namespace published and unpublished, and asserts every shared
module has the same `content_hash` in both. The check belongs there because
`publish: false` is pysmi's feature, and a hermetic test on every pysmi commit
catches a regression earlier than a fingerprint comparison on this repository's
release schedule did.

## The corpus database

`core.db` is the same source set a third way: the SMI model as data, one row
per node, keyed for lookup by OID and by name and ordered so a GETNEXT walk is
a range query. pysnmp reads it with stdlib `sqlite3` and no pysmi import; the
file format is specified in pysmi's
[corpus schema](https://pysnmp.github.io/pysmi/stable/corpus-schema.html).

It exists because of two questions `index-v2.csv` cannot answer. The index is
`MODULE,OID` and carries a module's *anchors*, so it says which module to load
and nothing else. A leaf such as `ifDescr` is not in it at all, so getting from
an OID to a name, a syntax and an access level means compiling the module's
ASN.1 or parsing its whole JSON document. An anchor index also has no per-node
ordering, so a walk cannot be served from one. In `core.db` both are a single
indexed row.

Measured on the corpus this repository builds:

| | |
|---|---|
| modules | 5,510 |
| nodes | 767,870 |
| distinct type specifications | 47,226 |
| indexed OIDs | 98,867 |
| size | 256 MB, 36 MB gzipped |
| build | one `mibcorpus` invocation, ~5 minutes |

**Built from `corpus-db.json`, whose source set is `corpus.json`'s, not the
compact manifest.** The two differ only in what they emit. The compact corpus
omits the standard modules because a runtime with pysmi already holds them as
Python. A database is consulted by OID, and a database missing `1.3.6.1.2.1`
cannot resolve `ifDescr` for anyone. There is one corpus; vendor is a column in
it rather than a partition of it.

**No prose.** No DESCRIPTION, no REFERENCE. They are about a third of a
generated module's bytes, pysnmp discards them under the default
`loadTexts=False`, and `json/` already serves the one consumer that wants them
the one consumer that wants it, a MIB browser. A second database for prose
would be the largest artifact this repository publishes and would duplicate a
channel that already works.
