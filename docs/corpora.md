# The corpora

One source set, rendered three ways. Which one you want follows from what the
consumer already has.

## The published corpus

Carries the standard modules, because its consumers fetch them from it:
splunk-connect-for-snmp resolves `asn1/@mib@` against this site for every
module it meets. This is what the site serves, what the release archives
contain, and what the [`mibserver` chart](chart.md) mounts.

## Where each tree goes

The published corpus goes to three places, and `corpus.json` names them as
three *publications* rather than as three builds:

| publication | destination | carries |
|---|---|---|
| `github-pages` | [`pysnmp.github.io/mibs/`](https://pysnmp.github.io/mibs/) | `asn1/`, `json/`, both indexes, `standard.txt`, this documentation |
| `depot-site` | [`mibsdepot.com`](https://mibsdepot.com) | the browsable pages — one per module, OID arc and registrant — and this documentation |
| `depot-data` | [`data.mibsdepot.com`](https://data.mibsdepot.com) | `asn1/`, `json/`, both indexes, `standard.txt`, `search.db` |

`mibcorpus` writes all three from one parse of the 5,510 modules. Parsing is
about three quarters of a pass, so three publications cost roughly what one and
a half builds would, and — the part that matters more — the three trees are
projections of a single parse rather than three runs that have to be trusted to
agree. CI asserts the two data trees are byte-identical anyway, artifact by
artifact, because "they came from the same parse" is a claim and a `diff` is a
check.

**Why the pages and the files are on different hosts.** Every link the site
generator writes is a directory URL — `../../mib/IF-MIB/` — which a host has to
resolve to that directory's `index.html`. Object storage does not: it serves
the key it is given, so `/mib/IF-MIB/` is a 404 unless something on the serving
path rewrites it. Static assets resolve it natively and run no script to do so,
which is the distinction that matters on a free plan: requests to a Worker's
*script* are metered, at 100,000 a day with cache hits counted, and requests to
its *assets* are not. What assets cost instead is a file count — 20,000 per
version — and the browsable pages are 7,430 of them, with 11,025 more files
beside them that never needed resolving at all, before the per-module downloads
that are still to come.

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
configuration. The depot half reads five settings, all of them **repository**
secrets and variables under Settings → Secrets and variables → **Actions** —
not environment ones, because the job that publishes is the same job that
builds and checks, and an environment's protection rules would gate the
contracts too.

Four are *secrets*:

| secret | |
|---|---|
| `CLOUDFLARE_API_TOKEN` | account token, permissions below |
| `CLOUDFLARE_ACCOUNT_ID` | the account the Worker and bucket live in |
| `R2_ACCESS_KEY_ID` | an R2 API token's two halves, for the |
| `R2_SECRET_ACCESS_KEY` | S3-compatible endpoint — not part of the first token |

and one is a *variable*, `CLOUDFLARE_R2_BUCKET`, because a bucket name is not
a secret. Getting that last distinction wrong is the one mistake this
arrangement can make quietly, so the build refuses it: R2 credentials present
with the variable empty fails the job and says why.

There is no separate switch to set. Holding the token is the decision to
publish, and the Worker's name is in `wrangler.jsonc` where it can be read.

The API token needs **Account → Workers Scripts: Edit** and **Account →
Account Settings: Read**. The `Edit Cloudflare Workers` template also grants
Workers KV Storage, Workers R2 Storage and Zone → Workers Routes, none of
which this deploy uses: the Worker has no bindings, and its hostname is
attached by hand rather than declared as a route. Create it under Manage
Account → API Tokens → Create Token; the R2 pair comes from a different place,
R2 object storage → Account Details → Manage next to API Tokens, at **Object
Read & Write**.

Each hostname is attached once, by hand, and neither is named in this
repository: `mibsdepot.com` to the Worker, and `data.mibsdepot.com` to the
bucket. Nothing here claims a domain it does not own, so a fork holding its
own token publishes to its own.

Unset, the deploy steps are skipped and everything before them still runs: a
fork, and this repository before the Cloudflare side existed, builds all three
trees and holds them to the same contracts. That is deliberate — a publishing
step nobody can exercise until release day is a step nobody has tested.

## The compact corpus

The same source set with the standard namespace declared `"publish": false` —
a [resolution source](manifests.md) rather than a published one. It carries
only what a runtime that already has the standard modules does not have, since
pysmi bundles 210 of them and its wheel ships their compiled form. Each module
in it is byte-identical to the same module in the published corpus.

It is not served over HTTP; it is published as an image to mount:

```
ghcr.io/pysnmp/mibs/corpus-compact:<version>
```

`publish: false` is the only difference between the two manifests in this
repository. `corpus.json` and `corpus-compact.json` are otherwise identical,
which is what makes the compact corpus a subset of the published one rather
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

**Built from `corpus-db.json`, whose source set is `corpus.json`'s — not the
compact manifest.** The two differ only in what they emit. The compact corpus
leaves the standard modules out because a runtime that has pysmi already holds
them as Python — but a database is consulted *by OID*, and one missing
`1.3.6.1.2.1` cannot resolve `ifDescr` for anybody. There is one corpus; vendor
is a column in it rather than a partition of it.

**No prose.** No DESCRIPTION, no REFERENCE. They are about a third of a
generated module's bytes, pysnmp discards them under the default
`loadTexts=False`, and `json/` already serves the one consumer that wants them
— a MIB browser. A second database for prose would be the largest thing this
repository publishes and would duplicate a channel that already works.
