# Contributing MIBs you already have

This page covers `scripts/contribute_mibs.py`, which offers a MIB set to this
distribution as a GitHub issue or as a pull request. Use it if you have your
own MIB directory and either a newer copy of a module than this site publishes
or a module it does not carry. Writing a pull request is not required, and
neither is knowing Python or SNMP tooling: what the script asks of you is one
`mibcorpus` command and a read of what it wrote.

[Contributing a MIB](contributing.md) is the other path, for a change you
intend to write yourself.

## What a build already knows

A MIB directory resolved against the published corpus is one source set with
two namespaces in it. `charts/mibserver` arranges that in an init container;
`mibcorpus` does it on a command line. The build then answers two questions
without being asked, and `report.json` records both.

| what it records | what it means |
|---|---|
| `shadowed` | the modules both sets hold a differing copy of, which copy was used, and which rule decided |
| `provenance` | the namespace every published module came from |

pysmi decides between two copies by one rule: the newest MODULE-IDENTITY
revision wins, and the configured order breaks a tie. Three outcomes are
possible and two of them are worth sending here.

| what the build found | worth reporting |
|---|---|
| the published copy won | no. This distribution is current for that module |
| your copy won on a newer revision | **yes.** This distribution is behind |
| your copy won on source order | not by default. The two files carry the same revision, or none, and two copies of one name are as often two different modules as two revisions of one. `--include-differing` reports them |
| no namespace here holds the module | **yes.** This is the larger half of what a collection has to offer |

## Producing the report

The script is one file, and it imports nothing but the standard library and
pysmi, which is already installed wherever `mibcorpus` runs. A checkout of this
repository is not needed:

```sh
curl -O https://raw.githubusercontent.com/pysnmp/mibs/main/scripts/contribute_mibs.py
```

`mibcorpus` resolves against a directory, so the published corpus has to be on
disk. Unpack `mibs-asn1.zip` from a release, or mount
`ghcr.io/pysnmp/mibs/corpus`. See [getting the MIBs](channels.md).

1. Resolve your MIBs against the published tree:

   ```sh
   mibcorpus --quiet \
     --resolve-namespace=standard:base:package:pysmi.mibs.asn1 \
     --resolve-namespace=vendor:corpus:./asn1 \
     --namespace=vendor:local:./my-mibs \
     --output-directory=./out --emit=asn1 --emit=report
   ```

   `--emit=asn1` is not optional. The pass that stages the ASN.1 tree is the
   pass that records what resolved, so a build asked for `--emit=report` alone
   writes `shadowed` and `provenance` empty and the script refuses it.

   The namespace order is precedence: `corpus` is written before `local`, so
   your copy wins by carrying a newer revision and never by being named last.

2. Read what would be offered. Nothing is sent by this command:

   ```sh
   python3 contribute_mibs.py --report=out/report.json
   ```

3. Read `contribution/issue.md`.

Running it against a `mibserver` deployment is the same command over the report
the init container already wrote:

```sh
kubectl exec deploy/mibserver -- cat /usr/share/nginx/overlay/report.json >report.json
```

The overlay names its namespace `local`, which is what `--namespace` defaults
to. A build that names yours something else has to say so:
`--namespace=my-mibs`.

## What it writes

Into `contribution/`, or wherever `--out` names:

| file | contents |
|---|---|
| `issue.md` | the issue body, with the ASN.1 of every module that fits in it |
| `findings.json` | the same findings as data: module, both revisions, both digests |
| `mibs/<MODULE>` | each MIB as it is on your disk, byte for byte |
| `contribution.zip` | the same files, to attach to the issue |

A GitHub issue body holds 65,536 characters, which is smaller than some single
MIBs and much smaller than a set of them. The body carries as many modules in
full as it holds, smallest first, and names the rest as being in the archive.

`--per-module` writes one issue per module instead of one issue for all of
them. One module per issue is one module per pull request, which is the shape
to use when the modules are unrelated.

## Filing it

| `--submit` | what happens | what it needs |
|---|---|---|
| `none` | the files are written and nothing is sent. The default | nothing |
| `url` | a GitHub issue URL with the report already in it is printed. You open it, read it, and post it | a GitHub account in your browser |
| `gh` | the issue is created by the GitHub CLI | `gh`, already authenticated |
| `pr` | the MIBs are committed to a checkout and a pull request is opened | `gh`, and a clone of this repository |

There is no way to open a GitHub issue without an account: GitHub accepts none
anonymously, and this repository cannot accept one on your behalf.
`--submit=url` is the closest thing to it, and the difference is worth stating
exactly. No credential is read, stored or sent by the script; the report
travels as a link you inspect, and the issue is posted by your browser under
whatever account that browser is signed in as.

Every path takes `--yes` as well, which is what says the MIB text in `issue.md`
may be published:

```sh
python3 contribute_mibs.py --report=out/report.json --submit=url --yes
python3 contribute_mibs.py --report=out/report.json --submit=gh --yes
```

Where the report is too long to carry in a URL, `--submit=url` prints a shorter
one and names the file to paste into the body. Attach `contribution.zip` to the
issue in either case; the GitHub web form takes it as a drag and drop.

`--submit=gh --gist` uploads the MIBs as a secret gist and links it from the
issue instead of inlining them. A secret gist is not private: anybody with the
link can read it, which is the point of putting the link in a public issue.

## What is already reported

Before submitting anything, the script searches this repository for the modules
it is about to offer and leaves out the ones an issue or pull request is
already open for. A closed issue does not stop a report, because it was closed
for a reason nothing here can read; the report is filed again with the old
issue named beside it.

The search is one query for every issue this script has filed, matched on the
marker each of them carries, and one query per module for reports up to eight
modules long. It runs through `gh` where that is installed and over the public
API otherwise, which is rate limited; `GITHUB_TOKEN` is used when it is set.

| flag | |
|---|---|
| `--check-duplicates` | run the search without submitting, to see what is already open |
| `--allow-duplicates` | report a module even where an issue for it is open |
| `--require-duplicate-check` | submit nothing if the search cannot run. For unattended runs |

A search that cannot run does not stop a person from filing: the script says so
and carries on. An unattended run should invert that with
`--require-duplicate-check`, because filing duplicates every month is worse
than filing nothing until the search works again.

## What it will not send

Read `issue.md` before posting it. Two things decide whether you can, and
neither is something a script can answer:

- **The licence.** A vendor MIB from a device or a support portal carries the
  vendor's terms. This distribution publishes a module under those terms or not
  at all.
- **The file's own contents.** A MIB edited at your site can carry hostnames,
  contacts or ticket numbers in its comments, and those are published with the
  rest of the text.

What the script does answer, it answers the same way every time. No absolute
path from your machine reaches an issue: a report records the paths the build
read, and those name the host it ran on, so every file is named relative to its
namespace instead. Nothing is submitted without both `--submit` and `--yes`.
The default command reads files and writes files, and the only thing that
leaves your machine before you have read `issue.md` is the duplicate search,
which sends module names and no MIB text.

## Scanning a collection

The second use is the freshness process rather than a single deployment. The
source set is a published MIB collection, the run is unattended, and what it
finds goes into a branch instead of into prose:

```sh
python3 scripts/contribute_mibs.py --report=out/report.json \
  --namespace=scanned \
  --submit=pr --yes \
  --checkout=../mibs \
  --vendor=example --publisher=example-mibs \
  --require-duplicate-check
```

`--submit=pr` writes each module to `src/vendor/<vendor>/<MODULE>`, records
`{"publisher": ...}` for each in `mib-sources.json`, commits on a branch named
for the contribution, pushes it and opens the pull request. The ASN.1 is in the
diff, so the pull request body carries the findings and the evidence and not
the module text.

| flag | |
|---|---|
| `--checkout` | the clone to commit into. It must be this repository, and its tree must be clean |
| `--vendor` | the directory under `src/vendor/`. Nothing in a MIB says which vendor's tree it is filed under here |
| `--publisher` | a publisher `mib-sources.json` already defines. Left off, the provenance is a question for review |
| `--branch` | the branch to commit on. Defaults to `mibs/<slug>` |
| `--base` | the branch to open the pull request against. Defaults to `main` |

A publisher the manifest does not define is refused rather than written: a
manifest entry naming one that does not exist fails
`scripts/update_vendor_mibs.py --validate`, which CI runs on every pull
request.

## What happens next

The issue carries what a pull request against this repository needs, except for
one thing no build can supply: where the files came from.
`mib-sources.json` records a publisher for every module under `src/`, which is
what lets [the monthly workflow](https://github.com/pysnmp/mibs/blob/main/.github/workflows/mib-freshness.yml)
notice the next revision without waiting for another report. The issue opens
with that question. Answer it in the issue, with the publisher's URL and the
device the files were taken from, and the pull request can be written from the
issue alone.

Every issue carries `<!-- mib-contribution v1 -->` and a `json` block holding
the findings, so the set is one search away and each one can be read without
parsing prose.
