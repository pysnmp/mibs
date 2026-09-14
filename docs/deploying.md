# Publishing the sites

Every push to `main` builds three trees and publishes each to its own host.
Two of the three need nothing set up:

| tree | goes to | needs |
|---|---|---|
| `github-pages` | [`pysnmp.github.io/mibs/`](https://pysnmp.github.io/mibs/) | nothing. It uses the repository's own token |
| `depot-site` | [`mibsdepot.com`](https://mibsdepot.com) | the Cloudflare setup below |
| `depot-data` | [`data.mibsdepot.com`](https://data.mibsdepot.com) | the Cloudflare setup below |

This page covers the depot half, once, in order. Until it is done the build
still runs in full: all three trees are written and held to every contract, and
only the two depot deploys are skipped. Nothing here is needed to develop on
this repository, and a fork never needs it at all.

Where each piece goes and why, rather than how to create it, is in
[the corpus variants](corpora.md#where-each-tree-goes).

```{note}
The site is served by what Cloudflare calls a *Worker*, and **there is no
Worker code**. `wrangler.jsonc` declares a directory of static assets and
nothing else: no script, no entrypoint, and nothing of this project's running
per request.
Cloudflare now hosts static files under the Workers name, which is why the
dashboard, the token permission and the `wrangler deploy` command all say
Worker for something that is a pile of HTML.

The distinction is not cosmetic. Requests answered by a Worker's script are
metered at 100,000 a day on the free plan, with cache hits counted. Requests
answered by its assets are free and unlimited. Serving these pages out of R2
would have needed a script, to turn `/mib/IF-MIB/` into that directory's
`index.html`; static assets do it without one.
```

## Before you start

- The domain on a Cloudflare account you administer. Everything below is free
  tier: R2 includes 10 GB-month of storage, 1 million writes and 10 million
  reads a month with no egress charge, and Workers static assets serve up to
  20,000 files with unlimited requests.
- Admin on the repository, to set secrets.

Steps 1 to 6 can be done in any order; 7, 8 and 9 depend on what came before.

## 1. Create the bucket

R2 object storage → **Create bucket**. Any name; you will type it again in
step 6. Location and storage class can stay on their defaults; the corpus is
590 MB of small files read from everywhere.

## 2. Give the bucket its hostname

The bucket → **Settings** → under **Custom Domains**, **Add** →
`data.mibsdepot.com` → **Continue** → review the DNS record → **Connect
Domain**. The status goes from *Initializing* to *Active* within a few
minutes.

Do this before step 7 if you can. The sync in step 7 works without it, because
it writes to the bucket over the S3 API rather than over the hostname, but
nothing can read what it wrote until the domain is live.

## 3. Create the R2 credentials

R2 object storage → under **Account Details**, **Manage** next to **API
Tokens** → **Create Account API token**.

Give it **Object Read & Write**, and scope it to the one bucket from step 1
rather than to all of them. The build writes objects and deletes the ones a
dropped module leaves behind; it never creates or configures a bucket, so it
does not need admin.

You get an **Access Key ID** and a **Secret Access Key**. The secret is shown
once. These are the S3-compatible endpoint's credentials and are not part of
the token in the next step.

## 4. Create the Workers token

Manage Account → **API Tokens** → **Create Token** → use the **`Edit
Cloudflare Workers`** template.

The template grants more than this deploy uses: Workers KV Storage, Workers R2
Storage and Zone → Workers Routes. None apply here, because the Worker has no
bindings and its hostname is attached by hand in step 8 rather than declared as
a route. Use it anyway. It is the set Cloudflare
maintains for `wrangler deploy`, and a token narrower than what wrangler
actually calls fails with

```
✘ [ERROR] A request to the Cloudflare API
  (/accounts/<id>/workers/services/<name>) failed.
  Authentication error [code: 10000]
```

which names no permission and takes a full build to reach.

The account-level permissions it must have in any case are **Workers Scripts:
Edit** and **Account Settings: Read**; wrangler also reads **User →
Memberships → Read** when reporting who it is logged in as. If you build a
custom token and hit the error above, the template is the answer rather than
guessing at the next permission.

## 5. Find the account ID

Shown on the R2 overview page under **Account Details**, and it is also the
hex string in the dashboard URL.

## 6. Tell GitHub

Repository **Settings** → **Secrets and variables** → **Actions**. Note the
two tabs on that page. Four of these are secrets and one is a variable, and the
difference matters:

| | tab | value |
|---|---|---|
| `CLOUDFLARE_API_TOKEN` | Secrets | step 4 |
| `CLOUDFLARE_ACCOUNT_ID` | Secrets | step 5 |
| `R2_ACCESS_KEY_ID` | Secrets | step 3 |
| `R2_SECRET_ACCESS_KEY` | Secrets | step 3 |
| `CLOUDFLARE_R2_BUCKET` | **Variables** | the bucket name from step 1 |

A bucket name is not a secret, so it is read from `vars`. A secret of that name
is not read at all. Entering it on the wrong tab previously left the variable
empty, skipped the data deploy and passed the job, leaving the depot without
updates. The build now fails and names the cause. See
[if something is wrong](#if-something-is-wrong).

**Repository, not environment.** These are repository-wide Actions secrets and
variables rather than deployment environment ones, because the job that
publishes is the same job that builds the corpus and runs its contracts. An
environment's protection rules would gate the contracts too, and a rule that
holds up a test is a rule people learn to click through.

There is no switch to turn on. Holding the token is the decision to publish,
and the Worker's name is in `wrangler.jsonc`.

## 7. Let it run

The next push to `main` deploys. Nothing needs to be triggered by hand; a
merge is enough.

The first R2 sync uploads the whole tree: 11,025 objects, 590 MB, about 11,000
of the million writes a month the free tier includes. Every
sync after it uploads only what changed, because the sync compares checksums
rather than timestamps.

The first Worker deploy creates the Worker. `wrangler` prints the URL it
deployed to; open it and the site should be there, on a `workers.dev` address,
before it has a domain of its own.

## 8. Give the site its hostname

Only possible after step 7, because the Worker does not exist until its first
deploy.

**Workers & Pages** → in **Overview**, select the Worker → **Settings** →
**Domains & Routes** → **Add** → **Custom Domain** → enter `mibsdepot.com` →
**Add Custom Domain**. Cloudflare creates the DNS record for you.

Add `www.mibsdepot.com` the same way if you want it to resolve; nothing in the
corpus links to it.

## 9. Check it

Four requests, which between them cover both hosts and both kinds of path:

```console
$ curl -sI https://mibsdepot.com/ | head -1
HTTP/2 200

$ curl -sI https://mibsdepot.com/mib/IF-MIB/ | head -1
HTTP/2 200

$ curl -s https://data.mibsdepot.com/asn1/IF-MIB | head -1
IF-MIB DEFINITIONS ::= BEGIN

$ curl -sI https://data.mibsdepot.com/asn1/IF-MIB | grep -i content-type
content-type: text/plain; charset=utf-8
```

The second is the one worth doing deliberately. `/mib/IF-MIB/` is a directory
URL with no file at that path, and it is the form every link in the site uses;
a host that does not resolve it to `index.html` answers 404 there while the
front page still works.

The fourth is why `asn1/` is uploaded in a pass of its own. Its files carry no
extension, as in `asn1/IF-MIB`, because pysmi substitutes a bare module name
into the `@mib@` source URL. A file whose name carries no extension is typed as
a stream of bytes by default, which makes a browser download a MIB rather than
display it.

## Afterwards

Nothing else is manual. Each push to `main` rebuilds all three trees and
publishes them, and each publish is held to the same contracts first: every
source module reaches the published tree, the two data trees are byte
identical, and each tree fits its host.

That last one is worth knowing about before it fires. The three ceilings are
GitHub's 1 GB, the 20,000 files and 25 MiB per file that static assets allow,
and R2's 10 GB. The build fails rather than the deploy, so a corpus that has
outgrown a host says so while there is still room to decide what to do about
it.

## If something is wrong

**`R2 credentials are set but the CLOUDFLARE_R2_BUCKET *variable* is empty`.**
the bucket name went in as a secret. Move it to the Variables tab.

**`CLOUDFLARE_R2_BUCKET names a bucket but R2_ACCESS_KEY_ID and
R2_SECRET_ACCESS_KEY are not both set`.** The reverse: one of the two halves
from step 3 is missing or was pasted empty.

**`the depot is not wired up on this repository`.** A notice, not a failure.
Neither half is configured, which is correct before step 6 and on every fork.

**The job is green but nothing appeared.** Check the run's step list. A
deploy that was skipped shows as skipped; if both ran and the site is still
unreachable, it is step 2 or step 8 that is missing, not the build.

**`Authentication error [code: 10000]` from the site deploy.** The Workers
token does not carry what `wrangler deploy` calls. Recreate it from the `Edit
Cloudflare Workers` template; see step 4. The failing request names the
Worker, so a 10000 there is about the token rather than about the account id
or the name.

**`/mib/IF-MIB/` answers 404 but `/` is fine.** `html_handling` in
`wrangler.jsonc` is not doing its job. It should be `auto-trailing-slash`,
which serves an asset at `mib/IF-MIB/index.html` for that path.
