# Contributing a module

Missing modules and corrections go to
{repo}`mibs` as pull requests. Adding a MIB is
a file drop under `src/vendor/<vendor>/` and a CI run — there is no registration
step and no index to edit, because
[`mibcorpus`](https://pysnmp.github.io/pysmi/stable/mibcorpus.html) derives both from
the sources.

Say where the module came from. `mib-sources.json` records the provenance of
every module under `src/`, in the shape pysmi already uses for the base MIBs it
bundles:

```
checked-in text  ==  the publisher's text  +  our patch
```

[Where the MIBs come from](mib-sources.md) explains why that record exists and
what it is for.

## What is and is not carried

The standard modules and the widely published vendor ones. Not every MIB ever
written, and where a device ships its own, that copy is authoritative — what is
here is a snapshot.

An SNMP engine does not need any of it to start. The modules pysnmp resolves
during start-up are compiled into the package, which is why
`pip install pysnmplib` works on a machine with no network. This distribution
matters the moment you want to name something outside that set.

[Absent modules](absent-modules.md) lists the 194 modules the site used to
serve and no longer carries, grouped by why each went and what it would take to
bring it back.

## Before you open the pull request

The contract scripts under `tests/` are what CI runs, and each can be run
locally:

| | |
|---|---|
| `tests/index-contract.sh` | the published indexes answer for what the corpus carries |
| `tests/artifact-contract.sh` | the published names are what `asn1/@mib@` can fetch |
| `tests/chart-contract.sh` | the chart renders what `charts/mibserver/rendered/` records |
| `tests/serving-contract.sh` | the corpus image answers the paths the site does |
| `tests/runtime-compile-contract.py` | a released pysnmp compiles what this build publishes |

That the compact corpus is a byte-identical subset of the published one is
checked upstream, in pysmi's `tests/test_corpus_publish_invariance.py`, because
`publish: false` is pysmi's feature — see [The corpora](corpora.md).

The lint and format the four sibling repositories share applies here too:

```
uvx pre-commit run --all-files
```
