# mibs

This MIB Repository is based on the original repository provided by snmplabs with updates from the mib collection from librenms.

In Addition an index is published allowing remote clients to identify a mib based on OID alone. All hosted on github pages.

pysnmplib (formerly pysnmp) applications can retrieve mibs from `https://pysnmp.github.io/mibs/asn1/@mib@`

## What is here

MIB **content**, and the configuration that says how to build it. The build
itself is [pysmi](https://github.com/pysnmp/pysmi)'s `mibcorpus`, so this
repository holds no compiler, no dependency resolver and no OID indexer of its
own — the ones it used to hold were second implementations of pysmi's, and each
had drifted from it (pysnmp/mibs#365).

| | |
|---|---|
| `src/vendor/*` | the MIB sources, one directory per vendor |
| `corpus.json` | the source set the published corpus is built from |
| `corpus-compact.json` | the same source set, without the standard modules |
| `index-frozen.csv` | the OID index snapshot `index.csv` replays |
| `charts/mibserver` | the Helm chart |
| `docker/` | the images: the corpus, and pysmi for the chart's init container |

Adding a MIB is a file drop under `src/vendor/<vendor>/` and a CI run.

## Building

```
make corpus           # the published corpus, into output/
make corpus-compact   # the same corpus without the standard modules
```

Both are one `mibcorpus` invocation over a manifest. Two runs over the same
sources produce the same bytes, with no network access; `output/report.json`
records what was built, what failed to compile, and how long it took.

## The two corpora

**The published corpus** carries the standard modules, because its consumers
fetch them from it: splunk-connect-for-snmp resolves `asn1/@mib@` against this
site for every module it meets. This is what gh-pages serves and what the
`mibserver` chart mounts.

**The compact corpus** is the same source set with the standard namespace
declared `"publish": false` — a resolution source rather than a published one.
It carries only what a runtime that already has the standard modules does not
have, since pysmi bundles 210 of them and its wheel ships their compiled form.
Each module in it is byte-identical to the same module in the published corpus.
It is not served over HTTP; it is published as an image to mount:

```
ghcr.io/pysnmp/mibs/corpus-compact:<version>
```

## Images

| Image | What it is |
|---|---|
| `ghcr.io/pysnmp/mibs/corpus` | the published corpus, `FROM scratch` — no base, no shell, nothing to patch |
| `ghcr.io/pysnmp/mibs/corpus-compact` | the compact corpus, likewise |
| `ghcr.io/pysnmp/mibs/tools` | pysmi on an upstream Python base, for the chart's local-MIB init container |

The corpus images hold the build output and nothing else, so they are mounted
rather than run. `ghcr.io/pysnmp/mibs/container` — nginx with the corpus baked
into it — is no longer published; the chart deploys upstream nginx and mounts
the corpus image instead.

## Helm chart

Install from the OCI registry:

```
helm install mibserver oci://ghcr.io/pysnmp/charts/mibserver --version 1.17.0
```

> **Deprecated:** the classic chart repository at `https://pysnmp.github.io/mibs/charts`
> (`helm repo add`) is being retired. Existing versions remain downloadable, but new releases
> are published to the OCI registry above. Migrate to `oci://ghcr.io/pysnmp/charts`.

### Kubernetes 1.33 or newer

The chart mounts the corpus as an [image
volume](https://kubernetes.io/docs/concepts/storage/volumes/#image), which is
beta in Kubernetes 1.33 and needs a runtime that implements it (containerd
2.0+, CRI-O 1.31+). The chart's `kubeVersion` refuses anything older rather
than scheduling a pod whose document root never appears.

What this buys: the container serving MIBs is `nginxinc/nginx-unprivileged`
from upstream, unmodified. This project no longer publishes an nginx image, so
an nginx CVE is upstream's to fix and yours to pick up by bumping
`image.tag` — not something that waits on a release here. The endpoints, ports
and paths are unchanged.

### Local MIBs

`localMibs.pathToMibs` and `localMibs.persistence.existingClaim` work as
before: point either at your own MIB sources and they are served beside the
published corpus, and indexed into `index.csv` with it.

What changed is where the compile happens. An init container runs `mibcorpus`
over the supplied sources, resolving them against the published corpus, and
writes what it produced into an `emptyDir` the serving container reads. Nothing
compiles inside the nginx container, and its root filesystem is read-only in
every configuration.

The published corpus wins where both hold a module: the overlay adds to what
this deployment serves rather than replacing it.

## IPv6 listeners

IPv6 listener support is disabled by default. Enabling it adds IPv6 listeners while preserving the existing IPv4 listeners on both endpoints:

- MIB content: TCP/8000
- NGINX status and readiness: TCP/8080

The listeners are rendered into the chart's `nginx.conf` from `ipv6Enabled`, so
the config a pod runs is complete as deployed and nothing rewrites it at
start-up.
