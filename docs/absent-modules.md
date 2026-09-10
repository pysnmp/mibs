# Modules the site used to serve and no longer does

`index-frozen.csv` is a snapshot of what `index.csv` answered before this
repository began correcting it, and it is deliberately never rewritten: an OID
that had an answer keeps that answer. That guarantee is about the *rows*, not
about the modules they name. 194 of the modules named there are now carried
nowhere — not in `src/`, not in pysmi's bundle — so `asn1/NAME` and
`json/NAME.json` return 404 for them, and 1,625 index rows point at something
the site will not serve.

Nothing fails to compile because of this. No module still in the corpus imports
any of the 194. What is lost is the site answering for their OIDs, and most of
these are leaf modules — the class that gets polled directly and imported by
nothing, so "nothing imports it" is not evidence that nothing wanted it.

This file is the record of which modules those are and why each one went. It is
the answer to "the site used to have X".

| | |
|---|---|
| modules named by `index-frozen.csv` | 5,347 |
| carried nowhere | **194** |
| index rows naming them | **1,625** |
| surviving modules with a dangling import | **0** |

Three groups, and they need different things.

## 1. Held back in pysmi — 65 consortium modules

These are published by a standards body or industry consortium, not by a vendor
and not by the IETF. pysmi's manifest carries all of them, but its wheel stages
only part of the bundle; these sit in `pysmi/mibs/future/` and are not shipped.
This repository deleted its own copies in #351, #375 and #384 on the grounds
that the bundle supplied them, and then the bundle stopped.

To bring one back, promote it in pysmi:

```
update_bundled_mibs.py --promote NAME
```

Re-homing them here is the other option, and unlike the RFC group below it is a
real one: `src/standard/<body>/` is the layout #338 established so that a
consortium module could be filed under the consortium that publishes it. Each
of these had a home there — `src/standard/cablelabs/DOCS-QOS3-MIB`,
`src/standard/iee/IEEE8021-CFM-V2-MIB`, `src/standard/mef/MEF-UNI-EVC-MIB` —
and the deletions are in git.

| publisher | count | modules |
|---|---|---|
| IEEE 802.1 | 26 | IEEE8021-CFM-V2-MIB, IEEE8021-CN-MIB, IEEE8021-DDCFM-MIB, IEEE8021-DEVID-MIB, IEEE8021-ECMP-MIB, IEEE8021-EVB-MIB, IEEE8021-FQTSS-MIB, IEEE8021-MIRP-MIB, IEEE8021-MSTP-MIB, IEEE8021-MVRPX-MIB, IEEE8021-PB-MIB, IEEE8021-PBB-MIB, IEEE8021-PBBTE-MIB, IEEE8021-PE-MIB, IEEE8021-PFC-MIB, IEEE8021-PSFP-MIB, IEEE8021-Preemption-MIB, IEEE8021-SPANNING-TREE-MIB, IEEE8021-SRP-MIB, IEEE8021-ST-MIB, IEEE8021-TPMR-MIB, IEEE8021-TSN-REMOTE-MANAGEMENT-MIB, LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB, LLDP-EXT-DOT1-MIB, LLDP-EXT-DOT3-MIB, LLDP-EXT-DOT3-V2-MIB |
| CableLabs | 14 | DOCS-DIAG-MIB, DOCS-DRF-MIB, DOCS-IF-M-CMTS-MIB, DOCS-IFEXT2-MIB, DOCS-L2VPN-MIB, DOCS-LOADBAL3-MIB, DOCS-LOADBALANCING-MIB, DOCS-MCAST-AUTH-MIB, DOCS-MCAST-MIB, DOCS-QOS-MIB, DOCS-QOS3-MIB, DOCS-SEC-MIB, DOCS-SUBMGT3-MIB, DOCS-TEST-MIB |
| ATM Forum | 5 | ATM-DXI-MIB, ATM-FORUM-ADDR-REG, ATM-FORUM-ILMI40-MIB, ATM-FORUM-M4-MIB, ATM-SOFT-PVC-MIB |
| DMTF | 5 | DMTF-DMI-MIB, DMTF-LAN-ADAPTER-MIB, DMTF-MOBILE-MIB, DMTF-MONITOR-MIB, DMTF-SERVICE-LAYER-MIB |
| IANA | 5 | IANA-CHARSET-MIB, IANA-LANGUAGE-MIB, IANA-PRINTER-MIB, IANAPowerStateSet-MIB, IANATn3270eTC-MIB |
| MEF | 3 | MEF-SOAM-PM-MIB, MEF-SOAM-TC-MIB, MEF-UNI-EVC-MIB |
| SCTE | 3 | SCTE-HMS-HEADENDIDENT-TC-MIB, SCTE-HMS-MPEG-MIB, SCTE-HMS-QAM-MIB |
| IEC | 1 | IEC-62439-3-MIB |
| IEEE 802.3 | 1 | IEEE8023-DOT3-LLDP-EXT-V2-MIB |
| PROFIBUS | 1 | LLDP-EXT-PNO-MIB |
| unattributed | 1 | LLDP-EXT-DCBX-MIB |

## 2. Held back in pysmi — 98 RFC modules

Same mechanism, different publisher. These are IETF modules, and `src/` is not
where they would come back to: `src/vendor` holds what a vendor publishes, and
filing an RFC module under the vendor that happened to ship a copy of it says
something untrue about who publishes it. Promotion in pysmi is the route.

`ADSL-LINE-EXT-MIB`, `ADSL2-LINE-MIB`, `ADSL2-LINE-TC-MIB`, `AGENTX-MIB`,
`APPC-MIB`, `APPN-DLUR-MIB`, `APPN-TRAP-MIB`, `APS-MIB`, `ARC-MIB`,
`ATM-ACCOUNTING-INFORMATION-MIB`, `ATM2-MIB`, `CHARACTER-MIB`, `CLNS-MIB`,
`COPS-CLIENT-MIB`, `DECNET-PHIV-MIB`, `DISMAN-EXPRESSION-MIB`,
`DISMAN-NSLOOKUP-MIB`, `DISMAN-SCHEDULE-MIB`, `DISMAN-TRACEROUTE-MIB`,
`DOCS-BPI-MIB`, `DOCS-IETF-CABLE-DEVICE-NOTIFICATION-MIB`,
`DOCS-IETF-QOS-MIB`, `DOT12-IF-MIB`, `DOT12-RPTR-MIB`, `DS0-MIB`,
`DS0BUNDLE-MIB`, `EBN-MIB`, `ENERGY-OBJECT-MIB`, `ETHER-CHIPSET-MIB`,
`ETHER-WIS`, `FCIP-MGMT-MIB`, `FIBRE-CHANNEL-FE-MIB`, `FLOW-METER-MIB`,
`FR-ATM-PVC-SERVICE-IWF-MIB`, `FR-MFR-MIB`, `GMPLS-LSR-STD-MIB`,
`GMPLS-TE-STD-MIB`, `HC-ALARM-MIB`, `HOST-RESOURCES-TYPES`, `HPR-IP-MIB`,
`IF-INVERTED-STACK-MIB`, `INTEGRATED-SERVICES-GUARANTEED-MIB`,
`IPATM-IPMC-MIB`, `IPMCAST-MIB`, `IPOA-MIB`, `IPS-AUTH-MIB`, `ITU-ALARM-MIB`,
`Job-Monitoring-MIB`, `LANGTAG-TC-MIB`, `MIOX25-MIB`, `MPLS-ID-STD-MIB`,
`MPLS-LDP-GENERIC-STD-MIB`, `MTA-MIB`, `Modem-MIB`, `NOTIFICATION-LOG-MIB`,
`NTPv4-MIB`, `OPT-IF-MIB`, `OSPF-TRAP-MIB`, `PARALLEL-MIB`, `PCE-PCEP-MIB`,
`PINT-MIB`, `PPP-BRIDGE-NCP-MIB`, `PPP-IP-NCP-MIB`, `PPP-LCP-MIB`,
`PPP-SEC-MIB`, `Printer-MIB`, `RADIUS-ACC-SERVER-MIB`,
`RADIUS-AUTH-SERVER-MIB`, `RFC1285-MIB`, `RFC1414-MIB`, `RS-232-MIB`,
`RSTP-MIB`, `RTP-MIB`, `SCSI-MIB`, `SCTP-MIB`, `SIP-MIB`, `SLAPM-MIB`,
`SMUX-MIB`, `SNMP-TLS-TM-MIB`, `SNMP-TSM-MIB`, `SOURCE-ROUTING-MIB`,
`T11-FC-FABRIC-CONFIG-SERVER-MIB`, `T11-FC-FABRIC-LOCK-MIB`,
`T11-FC-FSPF-MIB`, `T11-FC-ROUTE-MIB`, `T11-FC-RSCN-MIB`,
`T11-FC-SP-AUTHENTICATION-MIB`, `T11-FC-SP-POLICY-MIB`, `T11-FC-SP-SA-MIB`,
`T11-FC-SP-TC-MIB`, `T11-FC-SP-ZONING-MIB`, `T11-FC-VIRTUAL-FABRIC-MIB`,
`TN3270E-MIB`, `TN3270E-RT-MIB`, `TOKENRING-MIB`,
`TOKENRING-STATION-SR-MIB`, `URI-TC-MIB`, `WWW-MIB`

## 3. Deleted here on purpose — 31 modules

These are not an accident of packaging. Each was removed by a decision recorded
in the PR named beside it, and none of them should come back.

| why | modules |
|---|---|
| **Obsolete** — publisher marked every object `STATUS obsolete` (#353) | AC-PM-ATM-MIB, AcAtm, ARUBAWIRED-MCLAG-MIB, CISCO-GPRS-GTP-MIB, CTRON-SSR-L2-MIB, CTRON-SSR-L3-MIB, HP-ENTITY-MIB, Juniper-RADIUS-Disconnect-MIB, VMWARE-VCOPS-EVENT-MIB |
| **Superseded** — pre-publication draft whose published successor is bundled, often under a different name (#358) | ADSL-DMT-LINE-MIB, DOCS-BPI2-MIB, DOCS-CABLE-DEVICE-TRAP-MIB, DOCS-IF-EXT-MIB, DOCS-SUBMGT-MIB, INT-SERV-GUARANTEED-MIB, ISIS-D13-MIB, MPLS-TC-MIB, MSTP-MIB, RTCPXR-MIB, XGCP-MIB |
| **Superseded** — multicast drafts, importers repointed to the RFC (#367) | DVMRP-MIB, IGMP-MIB, IPMROUTE-MIB |
| **Never published** — draft that never became a standard, squatting an assigned `mib-2` arc (#352, #359) | INT-SERV-MIB, SYSLOG-MIB, T11-FC-SP-CERTS-MIB, T11-ZONE-SERVER-MIB |
| **Withdrawn** — RFC 8096 withdrew the module (pysmi#176) | IPV6-ICMP-MIB, IPV6-TCP-MIB, IPV6-UDP-MIB |
| **Not bundled, no importers** (#375) | COFFEE-POT-MIB |

## A module can be carried without a file of its own

`tests/index-contract.sh` counts these by comparing the names in the frozen
index against what `src/` and the bundle carry. Until this was written it
compared against *file basenames*, which is not the same question: a file may
declare more than one module. `src/vendor/extreme/EXTREME-BASE-MIB` declares 30,
and all 30 compile and serve — `asn1/EXTREME-VLAN-MIB` returns 200 — while the
check counted every one of them as carried nowhere.

That inflated the figure by 30 modules and 112 rows. The check now reads the
`NAME DEFINITIONS ::= BEGIN` line out of each file, so the number it pins is the
number above.
