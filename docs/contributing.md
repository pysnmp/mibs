# Contributing a MIB

Missing modules and corrections go to {repo}`mibs` as pull requests. To add a
MIB, drop the file under `src/vendor/<vendor>/` and open a pull request. There
is no registration step and no index to edit:
[`mibcorpus`](https://pysnmp.github.io/pysmi/stable/mibcorpus.html) derives both
from the sources.

Record where the module came from. `mib-sources.json` holds the provenance of
every module under `src/`, in the form pysmi already uses for the base MIBs it
bundles:

```
checked-in text  ==  the publisher's text  +  our patch
```

[MIB sources and patches](mib-sources.md) describes that record and what it is
for.

## What is and is not carried

The standard modules, and the widely published vendor ones. Not every MIB ever
written. Where a device ships its own copy, that copy is authoritative and this
one is a snapshot.

An SNMP engine does not need this distribution to start. The modules pysnmp
resolves during start-up are compiled into the package, which is why
`pip install pysnmplib` works on a machine with no network. The distribution
matters once you need to name something outside that set.

[Removed modules](absent-modules.md) lists the 194 modules this site once served
and no longer carries, grouped by the reason each was dropped and what
restoring it would take.

## Before you open the pull request

The contract scripts under `tests/` are what CI runs. Run them locally first:

| script | asserts |
|---|---|
| `tests/index-contract.sh` | the published indexes answer for what the corpus carries |
| `tests/artifact-contract.sh` | the published names are what `asn1/@mib@` can fetch |
| `tests/chart-contract.sh` | the chart renders what `charts/mibserver/rendered/` records |
| `tests/serving-contract.sh` | the corpus image answers the paths the site does |
| `tests/runtime-compile-contract.py` | a released pysnmp compiles what this build publishes |

That the compact corpus is a byte-identical subset of the published one is
checked upstream, in pysmi's `tests/test_corpus_publish_invariance.py`, because
`publish: false` is pysmi's feature. See [Corpus variants](corpora.md).

Run the lint and format that the four sibling repositories share:

```
uvx pre-commit run --all-files
```

## Writing documentation

Prose in `docs/`, `README.md` and `theme/` follows
[`STYLE.md`](https://github.com/pysnmp/mibs/blob/main/STYLE.md). The short
version: state what a page is in its first sentence, put enumerable facts in
tables, keep the em dash for a genuine break in a sentence, and do not give
systems intentions.
