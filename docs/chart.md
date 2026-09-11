# The mibserver chart

Serves the published corpus inside a cluster, for deployments that would rather
not give every compile egress to the public site.

Install from the OCI registry:

```
helm install mibserver oci://ghcr.io/pysnmp/charts/mibserver --version 1.17.0
```

```{warning}
The classic chart repository at `https://pysnmp.github.io/mibs/charts`
(`helm repo add`) is being retired. Existing versions remain downloadable, but
new releases are published to the OCI registry above. Migrate to
`oci://ghcr.io/pysnmp/charts`.
```

## Kubernetes 1.33 or newer

The chart mounts the corpus as an [image
volume](https://kubernetes.io/docs/concepts/storage/volumes/#image). The
chart's `kubeVersion` refuses anything below 1.33, but **the version check is
not sufficient on its own** — on 1.33 and 1.34 the feature ships beta and
*disabled*:

| Kubernetes | `ImageVolume` |
|---|---|
| 1.33, 1.34 | beta, **off by default** — enable the gate on the API server *and* the kubelet |
| 1.35 | beta, on by default |
| 1.36+ | stable |

The runtime has to implement it too: containerd 2.1+ (2.0 has no support at
all) and CRI-O 1.33+ for the beta surface — CRI-O 1.31 carries only the
original alpha.

Below 1.35 with the gate left at its default, `helm install` succeeds and the
pod then fails to start, because a version constraint is all a chart can
express. If that is your cluster, enable the gate before installing.

What this buys: the container serving MIBs is `nginxinc/nginx-unprivileged`
from upstream, unmodified. This project no longer publishes an nginx image, so
an nginx CVE is upstream's to fix and yours to pick up by bumping `image.tag` —
not something that waits on a release here. The endpoints, ports and paths are
unchanged.

## Local MIBs

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

IPv6 listener support is disabled by default. Enabling it adds IPv6 listeners
while preserving the existing IPv4 listeners on both endpoints:

- MIB content: TCP/8000
- NGINX status and readiness: TCP/8080

The listeners are rendered into the chart's `nginx.conf` from `ipv6Enabled`, so
the config a pod runs is complete as deployed and nothing rewrites it at
start-up.
