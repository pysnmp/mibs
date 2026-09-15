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

## When you are not going to write one

A MIB set can be contributed without a pull request. Resolve your own MIB
directory against the published corpus, and `scripts/contribute_mibs.py` turns
the build's own record of what it decided into an issue carrying the module
names, both revisions and the MIB sources themselves. It reports the modules
this distribution publishes an older copy of and the modules it does not carry
at all. See [contributing MIBs you already have](contributing-mibs.md).

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

## Seeing the module before it is published

Every pull request gets a rendered preview of the modules it touches, and
nothing else. The full CI build answers *is the corpus still sound*; it builds
5,510 modules into a site nobody can reach, and the two pages under review
would be somewhere inside it. The preview answers the other question.

It is one `mibcorpus` run over the whole source set publishing only what
changed, so the module's imports resolve against all 5,510 exactly as they
will on the live site -- a build over the changed files alone would fail on
the first `IMPORTS`. A module built this way is byte for byte the module built
whole; that is pysmi's guarantee and
[its own tests](https://pysnmp.github.io/pysmi/stable/mibcorpus.html) hold it
to it.

Three kinds of change reach the preview:

| you changed | it previews |
|---|---|
| a MIB under `src/` | that module, by the name the file **declares** |
| a repair under `scripts/mib-patches/` | the module it repairs, patch panel and all |
| a dependency, the theme, or a corpus manifest | three canary modules |

The third is the one worth explaining. A pysmi bump changes no MIB and can
change every page in the corpus, so previewing nothing would be the easy
answer and the useless one. It renders `IF-MIB`, `CISCO-IPMCAST-MIB` and
`TEL2N-MIB` instead -- one standard module with ninety definitions, one
carrying a repair so the defect and diff render, one plain vendor module.

A pull request that changes none of those previews nothing and passes. A red
cross on a documentation typo teaches everybody to ignore the check.

The same thing runs locally:

```sh
uv run python scripts/pr_scope.py --base=origin/main --out=preview-scope
uv run mibcorpus \
  --manifest=corpus-preview.json \
  --output-directory=output/preview \
  --patch-directory=scripts/mib-patches \
  --publish-only-from=preview-scope/modules.txt \
  --oid-registry=registries/smi-numbers.xml \
  --oid-registry=registries/pen-snapshot.csv \
  --fail-on-errors
python3 -m http.server -d output/preview
```

`--fail-on-errors` is what makes this a test rather than a rendering: a module
that will not compile fails, and `output/preview/report.json` names it under
`selected.failed`. A file under `src/` that declares no MIB module at all
fails earlier, in the scope, because a preview that quietly leaves out the
file the pull request is about has answered the wrong question.

Where the preview is *published* is the Cloudflare setup in
[Publishing the sites](deploying.md#the-pull-request-preview). Without it the
build still runs in full and the site is attached to the run as an artifact,
which is also what happens for a pull request from a fork, where the
credentials are not readable.

## Before you open the pull request

The contract scripts under `tests/` are what CI runs. Run them locally first:

| script | asserts |
|---|---|
| `tests/index-contract.sh` | the published indexes answer for what the corpus carries |
| `tests/artifact-contract.sh` | the published names are what `asn1/@mib@` can fetch |
| `tests/chart-contract.sh` | the chart renders what `charts/mibserver/rendered/` records |
| `tests/serving-contract.sh` | the corpus image answers the paths the site does |
| `tests/runtime-compile-contract.py` | a released pysnmp compiles what this build publishes |
| `tests/test_pr_scope.py` | the preview builds the modules a change touched |

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
