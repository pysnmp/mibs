# Contributing MIBs you already have

This page covers `mibcontribute`, the tool that offers a MIB directory to this
distribution. Use it if you have your own MIBs and want the ones this site is
missing, or behind on, to reach it. Writing a pull request is not required, and
neither is knowing Python: what it asks of you is one command and a read of
what it wrote.

[Contributing a MIB](contributing.md) is the other path, for a change you
intend to write yourself.

## One command

`mibcontribute` ships with [pysmi](https://pysnmp.github.io/pysmi/), which is
the compiler this distribution is built with. It arrived in pysmi 5.2.0, so
name that floor: an older pysmi installs `mibdump` and the rest without it.

```sh
pip install "pysnmp-pysmi>=5.2"
mibcontribute ./my-mibs
```

```text
2 module(s) worth offering: 1 the distribution carries an older copy of,
1 it does not carry.

    ACME-CHASSIS-MIB      2024-03-11  against 2015-05-01
    ACME-POWER-MIB        2024-03-11  against not carried

Wrote mib-contribution/issue.md
```

That reads every module in the directory, asks this site what it publishes for
each, and writes the result as a GitHub issue. It sends nothing. There is no
report to produce first and no build to run: point it at the directory your
MIBs are in, including the one a [mibserver deployment](chart.md) mounts.

## What it compares

Which of two copies of a module wins is not a judgement the tool makes. It is
pysmi's `rank_by_revision`, the rule this corpus is built with: the newest
MODULE-IDENTITY revision wins, and configured order breaks a tie. A module it
reports is a module a build would prefer.

| what it found | reported |
|---|---|
| the published copy is newer | no. This distribution is current for that module |
| the published copy is the same text | no. There is nothing to offer |
| your copy is newer | **yes**, as a better copy |
| this distribution has no copy | **yes**, as a module it does not carry |

A copy that wins on source order rather than on revision is not reported as
better unless `--include-differing` asks: two copies of one name are as often
two different modules that reuse a name as two revisions of one.

A module is offered under the name it declares rather than the name of the file
it was found in, because that is the name this distribution would publish it
under. A file that declares no module at all is passed over and named in the
log.

## What it compares against

`--corpus` takes a directory, a `.zip`, or a URL with `@mib@` where the module
name goes. It defaults to this site, which costs one request per module:

```sh
mibcontribute --corpus=./asn1 ./my-mibs
mibcontribute --corpus=./mibs-asn1.zip ./my-mibs
```

A scan of a large collection should use a local copy. An unpacked
`mibs-asn1.zip` or a mounted `ghcr.io/pysnmp/mibs/corpus` is a directory like
any other. See [getting the MIBs](channels.md).

## Filing it

| `--submit` | what happens | what it needs |
|---|---|---|
| `none` | the files are written and nothing is sent. The default | nothing |
| `url` | a GitHub issue URL with the report already in it is printed, for you to read and post | a GitHub account in your browser |
| `gh` | the issue is created by the GitHub CLI | `gh`, already authenticated |

```sh
mibcontribute ./my-mibs --submit=url
mibcontribute ./my-mibs --submit=gh
```

GitHub accepts no issue anonymously, and this repository cannot file one on
your behalf. `--submit=url` is the closest thing to it: no credential is read,
stored or sent by the tool, the report travels as a link you inspect first, and
the issue is posted by your browser under whatever account that browser is
signed in as.

An issue body holds 65,536 characters, which is smaller than some single MIBs.
The body carries as many modules in full as it holds and names the rest as
being in `mib-contribution/contribution.zip`, which the GitHub web form takes
as a drag and drop.

`--module=ACME-CHASSIS-MIB` offers one module rather than everything found;
repeat it for a few. `--per-module` writes one issue per module instead of one
issue for all of them, which is the shape to use when the modules are
unrelated: one module per issue is one module per pull request.

Read `mib-contribution/issue.md` before you post it. A MIB edited at your site
can carry hostnames, contacts or ticket numbers in its comments, and those are
published with the rest of the text. No path from your machine reaches the
issue: the tool names every file relative to the directory it scanned.

## What is already reported

Before submitting anything, the tracker is searched and the modules an issue or
pull request is already open for are left out. A closed issue does not stop a
report, because it was closed for a reason nothing can read back; the module is
offered again with the old issue named beside it.

| flag | |
|---|---|
| `--allow-duplicates` | offer a module even where an issue for it is open |
| `--require-duplicate-check` | submit nothing if the tracker cannot be searched |

A search that cannot run does not stop a person from filing. An unattended run
should invert that with `--require-duplicate-check`.

## What happens to the issue

It carries the module names, both revisions, both digests and the MIB sources,
which is what a pull request against this repository needs, plus one question
no scan can answer: where the files came from. `mib-sources.json` records a
publisher for every module under `src/`, which is what lets
[the monthly workflow](https://github.com/pysnmp/mibs/blob/main/.github/workflows/mib-freshness.yml)
notice the next revision without waiting for another report. Answer it in the
issue, with the publisher's URL and the device the files came from, and the
pull request can be written from the issue alone.

Every issue carries `<!-- mib-contribution v1 -->` and a `json` block holding
the findings, so the set is one search away and each one can be read without
parsing prose.

## Importing a scan into the tree

The other half runs here rather than on a contributor's machine, and is what
the freshness process uses: a scan of a published collection, imported into a
branch. `mibcontribute` writes the bundle and
`scripts/import_contribution.py` puts it where it belongs:

```sh
mibcontribute --quiet --corpus=./asn1 --output-directory=./found ./collection
uv run python scripts/import_contribution.py --contribution=found \
  --vendor=example --publisher=example-mibs --issue=123 --submit
```

It writes each module to `src/vendor/<vendor>/<MODULE>`, records
`{"publisher": ...}` for each in `mib-sources.json`, commits on a branch, and
with `--submit` pushes it and opens the pull request. The ASN.1 is in the diff,
so the body carries the findings and not the module text.

| flag | |
|---|---|
| `--contribution` | the directory `mibcontribute --output-directory` wrote |
| `--vendor` | the directory under `src/vendor/`. Nothing in a MIB says which vendor's tree it is filed under here |
| `--publisher` | a publisher `mib-sources.json` already defines. Left off, the provenance is a question for review |
| `--issue` | the issue this closes, named in the pull request body |
| `--checkout` | the clone to commit into. It must be this repository, and its tree must be clean |
| `--branch`, `--base` | the branch to commit on, and what to open the pull request against |

A publisher the manifest does not define is refused rather than written: an
entry naming one that does not exist fails
`scripts/update_vendor_mibs.py --validate`, which CI runs on every pull
request.

A module [this distribution does not carry on purpose](absent-modules.md) is
refused the same way, before the branch is made, and the refusal names the
section that excluded it. A scan offers what a collection holds: pointing
`mibcontribute` at net-snmp's MIB directory offered 24 modules, and 17 of them
already had a decision recorded against them. None of those decisions says "a
file under `src/vendor`" — each says the module is obsolete, superseded,
withdrawn or never published, and writing one under a vendor would undo that
silently. Offer the rest with `--module`.

## Standard or vendor

`src/vendor` is the only tree here, so a standard module offered to it is a
module filed in the wrong repository: standards-track text belongs in pysmi's
bundle, and a copy here would shadow the bundled one for every consumer.

The module's own registration says which it is. A module rooted under
`::= { enterprises N }` is that enterprise's, whatever else the file suggests
— look up `N` in `registries/pen-snapshot.csv` ([what that is](registries.md))
for whose. Two things that look like the answer are not:

- **The directory the collection kept it in.** observium files by directory
  and had put `DPI20-MIB` (`enterprises 2`, IBM) and `RFC7777-MIB`
  (`enterprises 18`, Wellfleet) under `rfc/`.
- **The module's name.** `RFC7777-MIB` is a private arc wearing an RFC
  number, and `SSH-MIB` and `COMMUNITY-MIB` read as standard and are not.

A module that really is standard and that pysmi does not bundle is a pysmi
pull request, not one here.
