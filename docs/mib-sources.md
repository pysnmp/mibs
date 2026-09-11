# Where the MIBs in `src/` come from

Every module under `src/` came from somewhere. For most of this
repository's life that somewhere was not written down.

MIBs arrived in bulk — from the snmplabs collection this repository
began as, and from librenms — and were hand-repaired whenever one would
not compile. The repair went into the file, next to the vendor's own
text, and after that the two were indistinguishable. A module carrying a
deliberate one-line fix and a module eight years behind its vendor look
exactly alike on disk. Nothing could tell us which modules had fallen
behind, because nothing recorded what they were supposed to match.

`mib-sources.json` records it, using the shape pysmi already uses for the
base MIBs it bundles:

```
checked-in text  ==  the publisher's text  +  our patch
```

The vendor's own bytes are the baseline. Our change, where we have one,
sits beside it in `scripts/mib-patches/` where it can be read, reviewed
and re-applied to a newer revision. A module with a publisher and no
patch must match that publisher byte for byte.

Once that holds, "has the vendor revised this?" becomes a question a
machine can ask, and [the monthly workflow](https://github.com/pysnmp/mibs/blob/main/.github/workflows/mib-freshness.yml)
asks it.

## What this does not recover

Two things, and neither is a gap to be closed later.

**A module whose publisher serves nothing fetchable has no baseline.**
Plenty of vendors publish MIBs only behind a support login, or only
inside a firmware image, or not at all. Those modules stay unmanaged.
`--report` counts them, so the size of the gap stays visible rather than
being quietly excluded from a green check.

**An edit made before the file reached us is invisible.** The snmplabs
and librenms collections were themselves hand-repaired for years, and
those repairs arrived here inside the imported file. Our git history
starts at the import; it cannot see behind it. So adopting a source turns
silent patching into visible patching only for edits made *since* the
import — anything older stays silent, and shows up merely as a
difference nobody can explain.

`--explain` is honest about this. It reports which differing lines a
commit of ours wrote, and says plainly when the rest trace no further
back than the import — which may mean a repair somebody made in 2015, or
a revision the vendor has published since. Our history cannot say which,
and the tool does not pretend otherwise. Somebody has to read the two
texts.

## Using it

```sh
# Does the manifest still describe the tree? Offline, so ordinary CI
# runs it on every pull request.
uv run python scripts/update_vendor_mibs.py --validate

# What the monthly workflow runs. Re-fetches everything with a
# publisher and reports what no longer matches.
uv run python scripts/update_vendor_mibs.py --check

# How much of src/ has a publisher behind it at all.
uv run python scripts/update_vendor_mibs.py --report

# Why does our copy of this module differ from the vendor's?
uv run python scripts/update_vendor_mibs.py --explain src/vendor/cisco/CISCO-ENTITY-ALARM-MIB

# It is a fix of ours: keep it, as a patch against the vendor's text.
# Nothing on disk changes -- the patch reproduces the file exactly.
uv run python scripts/update_vendor_mibs.py --adopt src/vendor/cisco/CISCO-ENTITY-ALARM-MIB

# It was only stale: take the vendor's text, patches re-applied.
uv run python scripts/update_vendor_mibs.py --update src/vendor/cisco/CISCO-BGP4-MIB

# Adopt a vendor directory wholesale: everything that already matches
# the publisher is recorded, and everything that does not is listed for
# somebody to --explain.
uv run python scripts/update_vendor_mibs.py --discover cisco-mibs-v2 src/vendor/cisco
```

`--update` is the only mode that rewrites a MIB, and it refuses partway:
a half-refreshed vendor directory compiles into a tree that is neither
the old set nor the new one.

## What `--check` treats as failure

Not everything it reports is a problem to fix this month.

A module that no longer matches its publisher, a patch that no longer
applies, a source that has stopped serving the module it should — those
fail the run. So does a *recorded* divergence that has since been
resolved, because a note nobody removed is a note that stops being read.

A divergence somebody has already written down does **not** fail the run.
It is listed every month under "known divergences, awaiting review", and
that backlog is the honest state of this repository: 52 modules that
differ from their vendor for reasons nobody has yet worked out. Failing
on them every month would train everybody to ignore the one month the
sweep says something new.

An unreachable publisher exits `2` rather than `1`. An outage says
nothing about our MIBs, and the exit code should not claim otherwise.

## Adding a publisher

A publisher belongs in `mib-sources.json` when it serves the vendor's own
MIB text at a URL that can be fetched without a login and that keeps
working. Two kinds are supported:

- `file` — one URL per module, with `{module}` standing in for the name.
- `archive` — one zip holding many modules, with `member` naming the path
  inside it.

Pin a **live** URL, not a dated release artefact. A frozen URL would make
the copy here unfalsifiable: the fetch would compare equal forever while
the vendor moved on, which is exactly the blindness this exists to end.

Then run `--discover` and read what it could not place.

### Sources that do not work

Worth recording, so nobody spends an afternoon rediscovering it:

| Vendor | What happens |
| --- | --- |
| Arista | `arista.com/assets/data/docs/MIBs/` answers 200 with a bot-check HTML page, not MIB text |
| MikroTik | the download link is an opaque file-share URL serving an HTML wrapper |
| Juniper, Huawei, HPE/Comware, Fortinet, Nokia | MIB bundles are behind a support login |
| Cisco Small Business (`CISCOSB-*`), UCS | not in `cisco/cisco-mibs`; published only inside firmware images |

The `--check` sweep guards against the first two specifically: a fetch
that succeeds but does not contain the module it should is reported as
`not-a-module` rather than being adopted as the vendor's text. Without
that, a vendor putting its downloads behind a bot check would silently
replace real MIBs with an error page.
