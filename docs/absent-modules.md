# Removed modules

This page lists the 31 modules that `index-frozen.csv` names and this
distribution no longer carries, with the reason each was dropped.

`index-frozen.csv` is a snapshot of what `index.csv` answered before this
repository began correcting it, and it is never rewritten: an OID that had an
answer keeps that answer. That guarantee covers the rows, not the modules they
name. 31 of the modules named there are carried neither in `src/` nor in
pysmi's bundle, so `asn1/NAME` and `json/NAME.json` return 404 for them, and
223 index rows name a module this site does not serve.

Nothing fails to compile because of this. No module still in the corpus imports
any of the 31. What is lost is the site answering for their OIDs, and most of
these are leaf modules, which are polled directly and imported by nothing. That
nothing imports a module is not evidence that nothing used it.

This page is the record of which modules those are and why each was dropped.

| | |
|---|---|
| modules named by `index-frozen.csv` | 5,347 |
| carried nowhere | **31** |
| index rows naming them | **223** |
| surviving modules with a dangling import | **0** |

## What used to be here

Two groups have gone, and they were the bulk of the page: 65 consortium
modules and 98 RFC modules that pysmi's manifest named but its wheel did not
ship, held in `pysmi/mibs/future/`. This repository had deleted its own copies
in #351, #375 and #384 on the grounds that the bundle supplied them, and then
the bundle stopped.

pysnmp/pysmi#323 promoted the whole held tier -- all 274 modules, 163 of them
named here -- so the wheel now carries every module its manifest names. The
hold had rested on a survey showing nothing in this corpus imported one of
them, which was true and was the wrong question to ask of a general-purpose
compiler. What settled it was that pgmillon/observium, an independent
monitoring distribution, ships 200 of the 274.

Those 1,402 index rows resolve again. What is left below is the group that was
never about packaging.

## Deleted here deliberately: 31 modules

These are not an accident of packaging. Each was removed by a decision recorded
in the PR named beside it, and none of them should come back.

| why | modules |
|---|---|
| **Obsolete.** Publisher marked every object `STATUS obsolete` (#353) | AC-PM-ATM-MIB, AcAtm, ARUBAWIRED-MCLAG-MIB, CISCO-GPRS-GTP-MIB, CTRON-SSR-L2-MIB, CTRON-SSR-L3-MIB, HP-ENTITY-MIB, Juniper-RADIUS-Disconnect-MIB, VMWARE-VCOPS-EVENT-MIB |
| **Superseded.** Pre-publication draft whose published successor is bundled, often under a different name (#358) | ADSL-DMT-LINE-MIB, DOCS-BPI2-MIB, DOCS-CABLE-DEVICE-TRAP-MIB, DOCS-IF-EXT-MIB, DOCS-SUBMGT-MIB, INT-SERV-GUARANTEED-MIB, ISIS-D13-MIB, MPLS-TC-MIB, MSTP-MIB, RTCPXR-MIB, XGCP-MIB |
| **Superseded.** Multicast drafts, importers repointed to the RFC (#367) | DVMRP-MIB, IGMP-MIB, IPMROUTE-MIB |
| **Never published.** Draft that never became a standard, squatting an assigned `mib-2` arc (#352, #359) | INT-SERV-MIB, SYSLOG-MIB, T11-FC-SP-CERTS-MIB, T11-ZONE-SERVER-MIB |
| **Withdrawn.** RFC 8096 withdrew the module (pysmi#176) | IPV6-ICMP-MIB, IPV6-TCP-MIB, IPV6-UDP-MIB |
| **Not bundled, no importers** (#375) | COFFEE-POT-MIB |

## The count reads declarations, not filenames

`tests/index-contract.sh` counts these by comparing the names in the frozen
index against what `src/` and the bundle carry. Until this was written it
compared against *file basenames*, which is not the same question: a file may
declare more than one module. `src/vendor/extreme/EXTREME-BASE-MIB` declared 34,
33 of them with no file of their own, and all 34 compiled and served, so
`asn1/EXTREME-VLAN-MIB` returned 200 while the check counted those 33 as carried
nowhere.

The check reads the `NAME DEFINITIONS ::= BEGIN` line out of each file, so the
number it pins is the number above. `src/` no longer holds a file like that one:
that MIB is stored as 34 files, and `tests/source-layout-contract.py` fails the
build if any file under `src/` declares more or fewer than one module.
