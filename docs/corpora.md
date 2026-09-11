# The corpora

One source set, rendered three ways. Which one you want follows from what the
consumer already has.

## The published corpus

Carries the standard modules, because its consumers fetch them from it:
splunk-connect-for-snmp resolves `asn1/@mib@` against this site for every
module it meets. This is what the site serves, what the release archives
contain, and what the [`mibserver` chart](chart.md) mounts.

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
[corpus schema](https://pysnmp.github.io/pysmi/corpus-schema.html).

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
