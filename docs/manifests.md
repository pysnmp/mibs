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

`mibcorpus` is [pysmi's corpus driver](https://pysnmp.github.io/pysmi/stable/mibcorpus.html).
Nothing in this repository compiles a MIB.

## The manifest format

A manifest is the whole of a corpus's definition: which sources it is built
from, which of them it *carries*, and how a tie between two of them is broken.
`mibcorpus --manifest` takes one, and everything else about a build is an
output flag.

```json
{
  "version": 1,
  "namespaces": [
    { "name": "standard", "source": "package:pysmi.mibs.asn1", "tier": "standard" },
    { "include": "src/vendor/*", "tier": "vendor" }
  ]
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
