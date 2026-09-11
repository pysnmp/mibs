# Manifests and the build

## Building

```
make corpus           # the published corpus, into output/
make corpus-compact   # the same corpus without the standard modules
make corpus-db        # the corpus database, into output-db/
```

Each is one `mibcorpus` invocation over a manifest. Two runs over the same
sources produce the same bytes, with no network access; `output/report.json`
records what was built, what failed to compile, and how long it took.

`mibcorpus` is [pysmi's corpus driver](https://pysnmp.github.io/pysmi/mibcorpus.html).
Nothing in this repository compiles a MIB.

## The manifest format

A manifest is the whole of a corpus's definition: which sources it is built
from, which of them it *carries*, how a tie between two of them is broken,
which artifacts the build writes, and what must be true of the result.
`mibcorpus --manifest` takes one.

```json
{
  "version": 1,
  "namespaces": [
    { "name": "standard", "source": "package:pysmi.mibs.asn1", "tier": "standard" },
    { "include": "src/vendor/*", "tier": "vendor" }
  ],
  "emit": ["asn1", "json", "index", "index-v2", "standard", "report"],
  "expect": {
    "modules": { "min": 5000 },
    "failures": { "max": 25 },
    "namespaces-present": ["standard"]
  }
}
```

| field | |
|---|---|
| `version` | the manifest format's version, not the corpus's |
| `namespaces` | the source sets, **in precedence order** |
| `name` | what the namespace is called in the build report |
| `source` | one directory, or `package:` and a dotted package name for the modules a Python package ships |
| `include` | a glob standing in for `source`, expanding to one namespace per directory it matches — `src/vendor/*` is ~285 of them, each named for its directory |
| `tier` | `standard`, `draft` or `vendor`. Not decoration: it is what tells the OID index that a standard module owns an arc a vendor module also defines |
| `publish` | `false` makes the namespace a *resolution* source — its modules satisfy what the published ones import and reach no output tree. Defaults to `true` |

Paths are relative to the manifest's own directory, so a manifest can be moved
with the tree it describes.

**Order is precedence.** Two namespaces holding a module of one name is normal
— a vendor shipping its own copy of an IETF module, say — and the earlier
namespace wins. That is why `standard` is written first above.

## What the build writes

`emit` is the artifact set, and it is what makes the three manifests in this
repository three different corpora over one source set.

| value | |
|---|---|
| `asn1` | the tree of MIB sources, named `asn1/<MODULE-NAME>` with no extension |
| `json` | one JSON document per module, with prose |
| `index` | `index.csv`, the v1 OID index |
| `index-v2` | `index-v2.csv`, the v2 OID index |
| `standard` | `standard.txt`, the list of standard module names |
| `core-db` | `core.db`, the SMI model as SQLite |
| `report` | `report.json`, what was built and what failed |

`core-db` stages the JSON documents it needs internally and removes them when
it is done, so a database build does not require the caller to hold a scratch
tree or to emit `json` it does not want.

## What must be true of the result

`expect` is checked against the build report, and a build that misses it fails
rather than publishing.

| key | |
|---|---|
| `modules.min` | fewest modules that may compile |
| `failures.max` | most modules that may fail to compile |
| `namespaces-present` | namespaces that must appear in the *published* set |

`namespaces-present` reads the published set rather than the source set, which
is what makes it catch the mistake worth catching: a manifest that resolves
against the standard modules but forgets to publish them builds happily and
serves a corpus nothing can resolve against. `corpus-compact.json` omits the
key because leaving `standard` unpublished is the whole point of it.

The floors are deliberately slack. They are there to catch a source set that
collapsed — a vendor directory that did not get checked out, a glob that
stopped matching — not to pin a number that legitimately moves every time a
MIB is added.
