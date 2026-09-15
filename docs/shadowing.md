# Reporting a module you hold a better copy of

This page covers `scripts/report_shadowing.py`, which turns a build's record of
a resolution into a GitHub issue carrying the MIBs it found. Use it when your
own MIB directory holds a newer copy of a module than this distribution
publishes, and you want that fixed without cutting a pull request yourself.

## What the build already knows

A local MIB directory resolved against the published corpus is one source set
with two namespaces in it. `charts/mibserver` arranges that in an init
container; `mibcorpus` does it on a command line. Where both namespaces hold a
module of one name, one copy is compiled and published and the other is passed
over.

pysmi decides between them by one rule: the newest MODULE-IDENTITY revision
wins, and the configured order breaks a tie. `report.json` records every such
pair under `shadowed`, naming the copy used, the copies passed over, and which
half of the rule decided.

Three outcomes are possible, and one of them is worth sending back here.

| the copy that won | what it means |
|---|---|
| the published copy | this distribution is current for that module |
| your copy, on a newer revision | this distribution is behind. **Report it** |
| your copy, on source order | the two files carry the same revision, or none. Often two different modules that reuse one name |

`scripts/report_shadowing.py` reads that report, keeps the second row, and
writes the issue.

## Producing the report

The script is one file, and it imports nothing but the standard library and
pysmi, which is already installed wherever `mibcorpus` runs. A checkout of this
repository is not needed:

```sh
curl -O https://raw.githubusercontent.com/pysnmp/mibs/main/scripts/report_shadowing.py
```

`mibcorpus` resolves against a directory, so the published corpus has to be on
disk. Unpack `mibs-asn1.zip` from a release, or mount
`ghcr.io/pysnmp/mibs/corpus`. See [getting the MIBs](channels.md).

1. Resolve your MIBs against the published tree, emitting the report:

   ```sh
   mibcorpus --quiet \
     --resolve-namespace=standard:base:package:pysmi.mibs.asn1 \
     --resolve-namespace=vendor:corpus:./asn1 \
     --namespace=vendor:local:./my-mibs \
     --output-directory=./out --emit=report
   ```

   The order is precedence: `corpus` is written before `local`, so your copy
   wins only by carrying a newer revision and never by being named last.

2. Read what would be reported. Nothing is sent by this command:

   ```sh
   python3 scripts/report_shadowing.py --report=out/report.json
   ```

3. Read `shadowing/issue.md`.

Running it against a `mibserver` deployment is the same command over the
report the init container already wrote:

```sh
kubectl exec deploy/mibserver -- cat /usr/share/nginx/overlay/report.json >report.json
```

The overlay names its namespace `local`, which is what `--namespace` defaults
to. A build that names yours something else has to say so:
`--namespace=my-mibs`.

## What it writes

Into `shadowing/`, or wherever `--out` names:

| file | contents |
|---|---|
| `issue.md` | the issue body, with the ASN.1 of every module that fits in it |
| `findings.json` | the same findings as data: module, both revisions, both digests |
| `mibs/<MODULE>` | each MIB as it is on your disk, byte for byte |
| `shadowed-mibs.zip` | the same files, to attach to the issue |

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

There is no way to open a GitHub issue without an account: GitHub accepts none
anonymously, and this repository cannot accept one on your behalf. `--submit=url`
is the closest thing to it, and the difference is worth stating exactly. No
credential is read, stored or sent by the script; the report travels as a link
you inspect, and the issue is posted by your browser under whatever account
that browser is signed in as.

Both paths take `--yes` as well, which is what says the MIB text in
`issue.md` may be published:

```sh
python3 scripts/report_shadowing.py --report=out/report.json --submit=url --yes
python3 scripts/report_shadowing.py --report=out/report.json --submit=gh --yes
```

Where the report is too long to carry in a URL, `--submit=url` prints a shorter
one and names the file to paste into the body. Attach `shadowed-mibs.zip` to
the issue in either case; the GitHub web form takes it as a drag and drop.

`--submit=gh --gist` uploads the MIBs as a secret gist and links it from the
issue instead of inlining them. A secret gist is not private: anybody with the
link can read it, which is the point of putting the link in a public issue.

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
Nothing is uploaded, indexed or phoned home by the default command.

## What happens next

The issue carries what a pull request against this repository needs, except
for one thing no build can supply: where the files came from.
`mib-sources.json` records a publisher for every module under `src/`, which is
what lets [the monthly workflow](https://github.com/pysnmp/mibs/blob/main/.github/workflows/mib-freshness.yml)
notice the next revision without waiting for another report. The issue opens
with that question. Answer it in the issue, with the publisher's URL and the
device the files were taken from, and the pull request can be written from the
issue alone.

Every issue carries `<!-- mib-shadowing-report v1 -->` and a `json` block
holding the findings, so the set is one search away and each one can be read
without parsing prose.
