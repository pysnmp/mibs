# Quarantined MIBs

The modules under `broken/` are not in the distribution. Almost all of them
are here because they do not compile, and they were moved out of `src/` so
that `src/` means one thing: every module in it builds. A few compile and are
here for a different reason, described under
[Not defective, but not usable here either](#not-defective-but-not-usable-here-either).

There are 309 of them, across 60 vendor namespaces.

Nothing resolves an OID to one of these today. `output/index.csv` is generated
on each build from the JSON the compiler produces, and pysmi writes no output
for a module it rejects — so a row naming one of these modules stops being
emitted whether or not the file moves. `index-frozen.csv`, the checked-in
compatibility snapshot, names none of them either. Their ASN.1 was published
only because `scripts/vendorsingle.sh` copies source text regardless of
whether the module compiled.

## Bring one back

These are wanted. If you have a copy of one of these modules that compiles —
a newer revision from the vendor, a corrected copy, a copy from a different
distribution — open a pull request that moves the file from `broken/vendor/<vendor>/`
back to `src/vendor/<vendor>/` with your text in place of ours. The build is the
test: if it compiles, it belongs in `src/`.

Please replace the module rather than editing it to compile. A descriptor
renamed to get past the parser changes the OID a name resolves to, and that
is a worse answer than no answer.

## Not defective, but not usable here either

Two things under `broken/` compile perfectly well. They are here because what
they say cannot be served from a flat distribution alongside what else is
here, which is a different problem from a module the compiler refuses.

`vendor/alcatel-aos6` is Alcatel-Lucent Enterprise's AOS 6 line — OmniSwitch
6600, 6800, 6850, 6450, 7000, 8000, 9000 — on `1.3.6.1.4.1.6486.800`. AOS 7,
in `src/vendor/alcatel-aos7`, carries **56 of the same module names** on
`.801`: not later revisions of the same modules, different registrations
reusing the names. A distribution keyed by bare module name can serve one of
each, so it serves AOS 7's, whose text is current to 2024-07-15 against AOS
6's 2019-10-07. Twenty modules only AOS 6 had go with it; nothing else in the
corpus imported any of them.

`vendor/extreme/BROCADE-MAPS-MIB` imports `swVfId` from `SYSTEM-MIB`. The
only `SYSTEM-MIB` here is Nokia's, which carries no MODULE-IDENTITY and does
not define `swVfId`. It compiled against that copy — the module name resolved
and the missing symbol did not stop it — so the published output referred to
something no module defines. Brocade's own `SYSTEM-MIB`, from FabricOS, is
what it wants and is not in this corpus. A copy of that would bring this
module back.

## Restoration notes

Things a replacement has to settle, found while quarantining these.

`DASAN-EPON-MIB` and `DASAN-GEPON-MIB` both declare `dasanPonMIB
MODULE-IDENTITY ::= { dasanMgmt 11 }`, with the same `LAST-UPDATED` and
different children under it — `{ dasanPonMIB 2 }` in one, `{ dasanPonMIB 1 }`
in the other. Two modules cannot both own that identity, so these are
conflicting registrations rather than two copies of one module. Whoever
restores them has to say which module owns `dasanMgmt 11`; restoring both as
they stand puts the conflict back.

## Why each one is here

Measured with pysmi 3.0.0-rc.1+ (`pysnmp/pysmi@next`), each namespace resolving
its own directory first and the rest of the corpus after it — the same order
`scripts/vendorsingle.sh` builds in. Three shapes:

- **138 root defects** — the module's own text is rejected.
- **72 consequential** — rejected while compiling a defective module it imports.
- **21 dependent** — compiles, but imports a module in this list.

A consequential or dependent entry usually returns to `src/` on its own once
the module it imports is replaced.

### bdcom

| module | reason |
| --- | --- |
| `NMS-CARD-SYS-MIB` | Duplicate symbol found: cardSysIndex |
| `NMS-CHASSIS` | Bad grammar near token type LOWERCASE_IDENTIFIER, value nmsAuxEntry |
| `NMS-EPON-OLT-PON` | Bad grammar near token type UPPERCASE_IDENTIFIER, value FiberProtectGroup |
| `NMS-FAN-TRAP` | Bad grammar near token type UPPERCASE_IDENTIFIER, value FanIndex |
| `NMS-GPON-MIB` | Bad grammar near token type ACCESS, value ACCESS |

### calix

| module | reason |
| --- | --- |
| `E5-120-AS-ATM-MIB` | needs `E5-120-MIB` (also here), which does not compile |
| `E5-120-IESCOMMON-MIB` | needs `E5-120-MIB` (also here), which does not compile |
| `E5-120-MIB` | Bad grammar near token type QUOTED_STRING, value "0:00" |
| `E5-120-TRAPS-MIB` | needs `E5-120-MIB` (also here), which does not compile |
| `E5-121-AS-ATM-MIB` | needs `E5-121-MIB` (also here), which does not compile |
| `E5-121-IESCOMMON-MIB` | needs `E5-121-MIB` (also here), which does not compile |
| `E5-121-MIB` | Bad grammar near token type QUOTED_STRING, value "0:00" |
| `E5-121-TRAPS-MIB` | needs `E5-121-MIB` (also here), which does not compile |
| `E7-Calix-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value e7VdslBondedInterfaceAdminStatus |

### ceraos

| module | reason |
| --- | --- |
| `MWRM-NETWORK-MIB` | Duplicate symbol found: alarmTrap |

### chatsworth

| module | reason |
| --- | --- |
| `CPI-UNITY-MIB` | Duplicate symbol found: configuration |

### ciena

| module | reason |
| --- | --- |
| `CIENA-CES-BENCHMARK-MIB` | no such bit as "p" for symbol "cienaCesBenchmarkProfileEntrySPcp" |

### cirpack

| module | reason |
| --- | --- |
| `KMIB` | Duplicate symbol found: kKey |

### comtrol

| module | reason |
| --- | --- |
| `COMTROL-ES8510-MIB` | Bad grammar near token type {, value { |

### comware

| module | reason |
| --- | --- |
| `HH3C-ACFP-MIB` | unknown type "(('Integer32', ''), ValueRanges(kind='range', bounds=((0, 2147483647),)))" for defval "hh3cAcfpServerMaxLi |

### cxr-networks

| module | reason |
| --- | --- |
| `CXR-TS-MIB` | imports a module in this list |

### cyberark

| module | reason |
| --- | --- |
| `CYBER-ARK-MIB` | Duplicate symbol found: cyberArkTrapGroup |

### dasan

| module | reason |
| --- | --- |
| `DASAN-AUTORESET-MIB` | needs `DASAN-SWITCH-MIB` (also here), which does not compile |
| `DASAN-BRIDGE-MIB` | needs `DASAN-SWITCH-MIB` (also here), which does not compile |
| `DASAN-DHCP-R-MIB` | needs `DASAN-ROUTER-MIB` (also here), which does not compile |
| `DASAN-EPON-MIB` | imports a module in this list |
| `DASAN-GEPON-MIB` | imports a module in this list |
| `DASAN-GIGABIT-OPTIC-TRANSCEIVER-MIB` | needs `DASAN-SWITCH-MIB` (also here), which does not compile |
| `DASAN-MCAST-MIB` | needs `DASAN-SWITCH-MIB` (also here), which does not compile |
| `DASAN-NOTIFICATION` | imports a module in this list |
| `DASAN-NOTIFICATION-V1` | imports a module in this list |
| `DASAN-QOS-MIB` | needs `DASAN-SWITCH-MIB` (also here), which does not compile |
| `DASAN-ROUTER-MIB` | Duplicate symbol found: dsRouterPortCRCcnt |
| `DASAN-SNMP-MIB` | needs `DASAN-SWITCH-MIB` (also here), which does not compile |
| `DASAN-SWITCH-MIB` | Bad grammar near token type NUMBER, value 100 |
| `DASAN-THRESHOLD-MIB` | needs `DASAN-SWITCH-MIB` (also here), which does not compile |
| `DASAN-TS-1000-MIB` | needs `DASAN-SWITCH-MIB` (also here), which does not compile |
| `DASAN-USER-MANAGEMENT-MIB` | needs `DASAN-SWITCH-MIB` (also here), which does not compile |
| `DPW-ATM-MIB` | Unknown parent symbol: mplsATMPWMIB |
| `SLE-PERFORMANCEMGMT-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value sleSfpmonThresholdEntry |

### datacom

| module | reason |
| --- | --- |
| `DMswitch-MIB` | Unknown parents for symbols: switchSessionEntry |

### dcn

| module | reason |
| --- | --- |
| `DCN-MIB` | Bad grammar near token type COLON_COLON_EQUAL, value ::= |

### dell

| module | reason |
| --- | --- |
| `DELL-TL4000-MIB` | Duplicate symbol found: eventStatusChange |

### dkt

| module | reason |
| --- | --- |
| `IDKT-F2-MIB` | Bad grammar near token type UPPERCASE_IDENTIFIER, value F2FWDMacAddress |

### dpstelecom

| module | reason |
| --- | --- |
| `DPS-MIB-V38` | imports a module in this list |
| `DPS-MIB-V38-V2` | imports a module in this list |
| `DPS-TEXT-RTU-MIB` | imports a module in this list |

### dragonwave

| module | reason |
| --- | --- |
| `DRAGONWAVE-HORIZON-IDU-MIB` | unknown type "(('OctetString', ''), '')" for defval "on" of symbol "hzIduEnetPort2Description" |
| `HORIZON-ODU-MIB` | unknown type "(('OctetString', ''), '')" for defval "on" of symbol "hzOduEnetPort2Description" |

### edgecos

| module | reason |
| --- | --- |
| `ECS4110-MIB` | Unknown parents for symbols: pethPseMainExtEntry, pethPsePortExtEntry |
| `ECS4210-MIB` | Bad grammar near token type {, value { |
| `ECS4510-MIB` | unknown type "(('OctetString', ''), ValueRanges(kind='size', bounds=((0, 8),)))" for defval "none" of symbol "ospfMultiP |
| `ECS4610-24F-MIB` | Bad grammar near token type {, value { |
| `ES3528MO-MIB` | Bad grammar near token type {, value { |

### emerson

| module | reason |
| --- | --- |
| `EES-POWER-FERRO-MIB` | Bad grammar near token type COLON_COLON_EQUAL, value ::= |
| `NETSURE-MIB-004-A` | Bad grammar near token type COLON_COLON_EQUAL, value ::= |

### endrun

| module | reason |
| --- | --- |
| `TEMPUSLXUNISON-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value gpsNTPNotPolling |

### fiberhome

| module | reason |
| --- | --- |
| `WRI-CPU-MIB` | imports a module in this list |
| `WRI-DEVICE-MIB` | imports a module in this list |
| `WRI-MEMORY-MIB` | imports a module in this list |
| `WRI-POWER-MIB` | imports a module in this list |
| `WRI-SMI` | Duplicate module identity |
| `WRI-TEMPERATURE-MIB` | imports a module in this list |
| `WRI-VOLTAGE-MIB` | imports a module in this list |

### fs

| module | reason |
| --- | --- |
| `FS-MIB` | Unknown parents for symbols: pethPseMainExtEntry, pethPsePortExtEntry |
| `GBNDeviceSWAPI-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value oemQueueWeightEntry |
| `GBNL2QACL-MIB` | Bad grammar near token type {, value { |
| `GBNL2Switch-MIB` | Bad grammar near token type {, value { |
| `GBNL3IPPool-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value ipPoolEntry |
| `GBNL3PIM-MIB` | Bad grammar near token type {, value { |
| `GBNL3Rip-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value gbnL3RipEntry |
| `GBNPlatformGNLink-MIB` | Bad grammar near token type {, value { |
| `GBNPlatformOAM-MIB` | Bad grammar near token type {, value { |
| `GBNPlatformOAMMailalarm-MIB` | needs `GBNPlatformOAM-MIB` (also here), which does not compile |
| `GBNPlatformOAMSntpClient-MIB` | needs `GBNPlatformOAM-MIB` (also here), which does not compile |
| `GBNPlatformOAMSsh-MIB` | needs `GBNPlatformOAM-MIB` (also here), which does not compile |
| `GBNPlatformOAMSyslog-MIB` | Bad grammar near token type MAX_ACCESS, value MAX-ACCESS |
| `GBNPlatformOAMTelnet-MIB` | needs `GBNPlatformOAM-MIB` (also here), which does not compile |
| `GBNServiceCM-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value gbn8021xCmConfEntry |
| `GBNServiceRADIUS-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value gbnRadiusConfEntry |
| `LAG-ARCH-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value lagTrunkGroupEntry |

### hikvision

| module | reason |
| --- | --- |
| `HIKVISION-MIB` | Bad grammar near token type NUMBER, value 2000 |

### hillstone

| module | reason |
| --- | --- |
| `HILLSTONE-DNS-MIB` | Duplicate symbol found: HillstoneStaticDnsServAddressEntry |
| `HILLSTONE-STATISTICS-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value hillstoneAtkEventStatisticsEntry |
| `HILLSTONE-ZONE-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value hillstoneZoneIFEntry |

### himoinsa

| module | reason |
| --- | --- |
| `DISMUNTELv00-MIB` | Bad grammar near token type UPPERCASE_IDENTIFIER, value PFCTotal |

### hp

| module | reason |
| --- | --- |
| `HP-OV-TOPO-DB` | Bad grammar near token type SIZE, value SIZE |
| `HP-SWITCH-TRAP-MIB` | no symbol "hpSwitchJ9573" in module "HP-ICF-OID" |
| `HPN-ICF-ACFP-MIB` | unknown type "(('Integer32', ''), ValueRanges(kind='range', bounds=((0, 2147483647),)))" for defval "hpnicfAcfpServerMax |
| `HPN-ICF-EOC-COMMON-MIB` | imports a module in this list |
| `HPN-ICF-HPEOC-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value hpnicfHPEOCTemplateGlobalEntry |
| `HPN-ICF-RPR-MIB` | Unknown parents for symbols: hpnicfRprTrapIpAddress |
| `HPNSADIMM-MIB` | Unknown parents for symbols: hpnsaDIMMHPLocalEntry |

### ibm

| module | reason |
| --- | --- |
| `GPFS-MIB` | Duplicate symbol found: gpfsDiskName |
| `IBM-CPS-MIB` | imports a module in this list |
| `IBM-ELAN-MIB` | Unknown parents for symbols: atmDevLineSpeed, idleVccTime, lecsMaxVccs |
| `IBM-LAN-EMULATION-EXTENSION-MIB` | Unknown parents for symbols: ibmVlanConfAgingTimer |
| `IBM-LES-LECS-MIB` | Unknown parents for symbols: lesLecsAtmDevLineSpeed |
| `IBM-NetFinity-Text-Alert-MIB` | imports a module in this list |
| `IBM-TS3500-MIBv1` | imports a module in this list |
| `IBMIROCAUTH-MIB` | no symbol "IpAddress" in module "SNMPv2-SMI-v1" |
| `IMM-MIB` | Duplicate symbol found: ctrlName |

### ict

| module | reason |
| --- | --- |
| `ICT-DISTRIBUTION-PANEL-MIB` | Unknown parents for symbols: busEntry |

### ignitenet

| module | reason |
| --- | --- |
| `ES4552BH2-MIB` | Unknown parents for symbols: pethPseMainExtEntry, pethPsePortExtEntry |

### juniper

| module | reason |
| --- | --- |
| `JNX-MPLS-TE-P2MP-STD-MIB` | no symbol "jnxP2mpExperiment" in module "JUNIPER-EXPERIMENT-MIB" |
| `JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB` | no symbol "jnxExampleMibRoot" in module "JUNIPER-EXPERIMENT-MIB" |
| `L2L3-VPN-MCAST-MIB` | no symbol "jnxL2L3VpnMcastExperiment" in module "JUNIPER-EXPERIMENT-MIB" |
| `MCAST-VPN-MIB` | no symbol "jnxMvpnExperiment" in module "JUNIPER-EXPERIMENT-MIB" |
| `MPLS-MLDP-STD-MIB` | no symbol "jnxMldpExperiment" in module "JUNIPER-EXPERIMENT-MIB" |
| `OSPFV3-MIB-JUNIPER` | no symbol "jnxOspfv3Experiment" in module "JUNIPER-EXPERIMENT-MIB" |

### openaccess

| module | reason |
| --- | --- |
| `OACOMMON-MIB` | Bad grammar near token type UPPERCASE_IDENTIFIER, value Type |

### orvaldi

| module | reason |
| --- | --- |
| `companyMIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value companyMIB |

### panasonic

| module | reason |
| --- | --- |
| `ipPbxNs-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value ipPbxNs-MIB |

### pbi

| module | reason |
| --- | --- |
| `PBI-4000P-5000P-MIB` | Duplicate symbol found: multicastIPAddress |

### pbn

| module | reason |
| --- | --- |
| `NMS-IF-MIB` | Bad grammar near token type UPPERCASE_IDENTIFIER, value IfIndex |

### perle

| module | reason |
| --- | --- |
| `PERLE-IOLAN-SDS-MIB` | Bad grammar near token type ;, value ; |

### poweralert

| module | reason |
| --- | --- |
| `TRIPPLITE-MIB` | Bad grammar near token type STRING, value STRING |

### proware

| module | reason |
| --- | --- |
| `proware-SNMP-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value proware-SNMP-MIB |

### qtech

| module | reason |
| --- | --- |
| `QTECH-MIB` | Bad grammar near token type UPPERCASE_IDENTIFIER, value CableLengthInfo |

### quanta

| module | reason |
| --- | --- |
| `NETGEAR-AUTHENTICATION-MANAGER-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-BGP-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-BOXSERVICES-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-CAPTIVE-PORTAL-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-DCBX-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-DENIALOFSERVICE-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-DHCPCLIENT-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-DHCPSERVER-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-DNS-RESOLVER-CONTROL-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-DOT1X-ADVANCED-FEATURES-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-DOT1X-AUTHENTICATION-SERVER-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-FIPSNOOPING-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-GREENETHERNET-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-INVENTORY-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-IPV6-LOOPBACK-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-IPV6-TUNNEL-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-ISDP-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-KEYING-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-LLPF-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-LOGGING-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-LOOPBACK-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-MGMT-SECURITY-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-MMRP-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-MRP-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-MULTICAST-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-MVR-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-MVRP-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-NSF-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-OUTBOUNDTELNET-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-PFC-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-PORTSECURITY-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-POWER-ETHERNET-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-QOS-ACL-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-QOS-AUTOVOIP-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-QOS-COS-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-QOS-DIFFSERV-EXTENSIONS-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-QOS-DIFFSERV-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-QOS-ISCSI-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-QOS-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-RADIUS-AUTH-CLIENT-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-ROUTE-POLICY-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-ROUTING-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-ROUTING6-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-SFLOW-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-SNTP-CLIENT-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-SWITCHING-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-TIMERANGE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-TIMEZONE-PRIVATE-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-UDLD-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `NETGEAR-VPC-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |
| `QUANTA-LB6M-REF-MIB` | Duplicate symbol found: lb6m |
| `TACACS-CLIENT-MIB` | needs `QUANTA-LB6M-REF-MIB` (also here), which does not compile |

### raisecom

| module | reason |
| --- | --- |
| `RAISECOM-COMMON-MANAGEMENT-MIB` | Bad grammar near token type {, value { |
| `RAISECOM-OPTICAL-TRANSCEIVER-MIB` | imports a module in this list |
| `RAISECOM-PON-DEVICE-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value raisecomSubFanEntry |

### redlion

| module | reason |
| --- | --- |
| `SIXNET-MIB` | Duplicate symbol found: sixnetCompliance1 |

### riedo

| module | reason |
| --- | --- |
| `NETTRACK-E3METER-CTR-SNMP-MIB` | Bad grammar near token type NUMBER, value 1 |
| `NETTRACK-E3METER-SNMP-MIB` | Unknown parents for symbols: e3IpmRcmTableEntry |

### ruckus

| module | reason |
| --- | --- |
| `RUCKUS-ZD-WLAN-CONFIG-MIB` | unknown type "(('Integer32', ''), ValueRanges(kind='range', bounds=((0, 1024),)))" for defval "none" of symbol "ruckusZD |

### screenos

| module | reason |
| --- | --- |
| `NETSCREEN-SET-ADMIN-USR-MIB` | Bad grammar near token type {, value { |
| `NETSCREEN-UAC-MIB` | Bad grammar near token type {, value { |

### siemens

| module | reason |
| --- | --- |
| `SN-MSPS-SCX200-MIB` | Duplicate symbol found: snMspsTrapRmActiveState |

### snrerd

| module | reason |
| --- | --- |
| `SNR-ERD-4` | Duplicate symbol found: tempCritNotif |

### sonicwall

| module | reason |
| --- | --- |
| `SNWL-SSLVPN-MIB` | Unknown parent symbol: sonicwall |

### sophos

| module | reason |
| --- | --- |
| `SFOS-FIREWALL-MIB` | Duplicate symbol found: sfosIPSecVpnPolicyName |

### teltonika

| module | reason |
| --- | --- |
| `TELTONIKA-MIB` | Duplicate symbol found: hotSpotId |

### tplink

| module | reason |
| --- | --- |
| `TPLINK-POWER-OVER-ETHERNET-MIB` | Duplicate symbol found: tpPoeRecoveryPort |
| `TPLINK-SYSINFO-MIB` | Bad grammar near token type NUMBER, value 9600 |

### ubiquoss

| module | reason |
| --- | --- |
| `UBIQUOSS-10GEPON-PM-GROUP-MIB` | Duplicate symbol found: pm10gHqosQueue0Bytes |
| `UBIQUOSS-10GEPON-PON-MAC-GROUP-MIB` | imports a module in this list |
| `UBIQUOSS-10GEPON-PON-PROFILE-GROUP-MIB` | Bad grammar near token type COLON_COLON_EQUAL, value ::= |
| `UBIQUOSS-10GEPON-SOFTWARE-MANAGEMENT-GROUP-MIB` | Unknown parent symbol: ubiSoftwareMIB |
| `UBIQUOSS-EPON-MIB` | Bad grammar near token type }, value } |
| `UBIQUOSS-EPON-ONTMANAGER-GROUP-MIB` | Bad grammar near token type (, value ( |
| `UBIQUOSS-EPON-PM-GROUP-MIB` | Bad grammar near token type }, value } |
| `UBIQUOSS-EPON-PM-MIB` | Bad grammar near token type COLON_COLON_EQUAL, value ::= |
| `UBIQUOSS-EPON-PON-MAC-GROUP-MIB` | Bad grammar near token type }, value } |
| `UBIQUOSS-EPON-PON-PROFILE-GROUP-MIB` | Bad grammar near token type }, value } |
| `UBIQUOSS-EPON-SERVICE-POLICY-GROUP-MIB` | Bad grammar near token type }, value } |
| `UBIQUOSS-EPON-SOFTWARE-MANAGEMENT-GROUP-MIB` | Bad grammar near token type }, value } |
| `UBIQUOSS-STP-MIB` | imports a module in this list |
| `UBIQUOSS-SWITCH-INTERFACE-MIB` | Bad grammar near token type {, value { |
| `UBQS-ACCESS-LIST-MIB` | Bad grammar near token type (, value ( |
| `UBQS-ARP-MIB` | Illegal character '/', 1936 characters left unparsed |
| `UBQS-AUTO-RESET-MIB` | Bad grammar near token type }, value } |
| `UBQS-CFM-MIB` | Bad grammar near token type }, value } |
| `UBQS-CPU-MAC-FILTER-MIB` | Bad grammar near token type }, value } |
| `UBQS-ENTITY-ALARM-MIB` | Bad grammar near token type }, value } |
| `UBQS-ERPS-MIB` | Bad grammar near token type }, value } |
| `UBQS-MPLS-MIB` | Bad grammar near token type }, value } |
| `UBQS-MPLS-PW-MIB` | Bad grammar near token type }, value } |
| `UBQS-MPLS-RSVP-MIB` | Bad grammar near token type }, value } |
| `UBQS-NTP-MIB` | Bad grammar near token type }, value } |
| `UBQS-OSPF-MIB` | Bad grammar near token type }, value } |
| `UBQS-QOS-MIB` | Bad grammar near token type (, value ( |
| `UBQS-REDUNDANCY-MIB` | Bad grammar near token type }, value } |
| `UBQS-SLD-MIB` | Bad grammar near token type {, value { |
| `UBQS-SYSLOG-MIB` | Bad grammar near token type }, value } |
| `UBQS-SYSTEM-ACCESS-MIB` | Bad grammar near token type }, value } |

### ubnt

| module | reason |
| --- | --- |
| `UBNT-AirFIBER-MIB` | Bad grammar near token type {, value { |

### unitrends

| module | reason |
| --- | --- |
| `UNITRENDS-SNMP` | Unknown parents for symbols: eventlogProbeTableEntry |

### watchguard

| module | reason |
| --- | --- |
| `WATCHGUARD-POLICY-MIB` | Bad grammar near token type {, value { |

### wut

| module | reason |
| --- | --- |
| `WebGraph-Thermo-Hygro-Barometer-MIB` | Bad grammar near token type COLON_COLON_EQUAL, value ::= |

### zmtel

| module | reason |
| --- | --- |
| `ZMTEL-ODU-MIB` | Bad grammar near token type MODULE_IDENTITY, value MODULE-IDENTITY |

### zyxel

| module | reason |
| --- | --- |
| `IES5206-MIB` | Bad grammar near token type NUMBER, value 1 |
| `IES5206-TRAPS-MIB` | needs `IES5206-MIB` (also here), which does not compile |
| `ZYXEL-GS2200-24-MIB` | Duplicate symbol found: newRoot |
| `ZYXEL-GS4012F-MIB` | Duplicate symbol found: newRoot |
| `ZYXEL-IES5000-MIB` | Bad grammar near token type MAX_ACCESS, value MAX-ACCESS |
| `ZYXEL-MGS3712-MIB` | Duplicate symbol found: newRoot |
| `ZYXEL-SAM1216` | Duplicate symbol found: igmpGroupIp |
| `ZYXEL-ZYWALL-ZLD-COMMON-MIB` | Bad grammar near token type LOWERCASE_IDENTIFIER, value vpnStatusEntry |

