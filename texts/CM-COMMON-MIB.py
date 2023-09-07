#
# PySNMP MIB module CM-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/CM-COMMON-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 11:36:06 2023
# On host fv-az174-692 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, IpAddress, Counter64, Bits, ModuleIdentity, NotificationType, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "IpAddress", "Counter64", "Bits", "ModuleIdentity", "NotificationType", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1))
cmCommonMIB.setRevisions(('2021-01-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmCommonMIB.setRevisionsDescriptions(('\n             Notes from release 202005120000Z,\n             (1) Added TEXTUAL-CONVENTION: SfpIdentifierValue.\n\n             Notes from release 201908140000Z\n             (1) add xg120Proac product\n\n             Notes from release 201903110000Z\n             (1) add xg118ProacSH product\n\n             Notes from release 201809240000Z\n             (1) add xg118ProSH product\n\n             Notes from release 201807260000Z\n             (1) add ge102ProH and ge102ProEFMH product\n             \n             Notes from release 201804190000Z\n             (1) add xg116ProH product\n\n             Notes from release 201611100000Z\n             (1) add xg116Pro product\n             (2) add xg120Pro subproduct  \n             Notes from release 201607110000Z\n             (1) renamed FlowSecureState to FlowSecState since it cannot be moved from fsp150cm-connectguard.mib\n             Notes from release 201607080000Z\n             (1)  moved FlowSecureState from fsp150cm-connectguard.mib\n             Notes from release 201502040000Z\n             (1) add xg210c subproduct             \n\n             Notes from release 201412010000Z,\n             (1) Added new Textual Convention: Decimal32\n\n             Notes from release 201405210000Z,\n             (1) Added new EthernetMediaType literals:\n                 - auto,\n                 - none.\n\n             Notes from release 201311280000Z\n             (1) Added new Secondary State literal - mon-tx \n             \n             Notes from release 201202150000Z (post GE20x R5.2.3CC)\n             (1) Added  speed-auto-detect to EthernetPortSpeed \n\n             Notes from release 201108010000Z\n             (1) Post EG-X merge (R5.1.1)\n\n             Notes from release 201107080000Z\n             (1)Moved CmPmIntervalType from fsp150cm-perf.mib to this MIB\n             (2)Added interval-5min to TC CmPmIntervalType\n\n\n             Notes from release 201002120000Z\n             (1)New Textual Conventions : ClassOfServiceType and SignalDirectionType\n             (2)New product OIDs (used for sysOid) : ge201 and ge201se\n\n             Notes from release 200803160000Z,\n             (1)EthernetPortSpeed textual convention now has additional literals,\n                   speed-auto-1000MB-full-master and speed-auto-1000MB-full-slave \n             (2)Added textual convention SfpMediaType\n\n             Notes from release 200803030000Z,\n             (1)MIB version ready for release FSP150CM.',))
if mibBuilder.loadTexts: cmCommonMIB.setLastUpdated('202101270000Z')
if mibBuilder.loadTexts: cmCommonMIB.setOrganization('ADVA Optical Networking SE')
if mibBuilder.loadTexts: cmCommonMIB.setContactInfo('Web URL: http://adva.com/\n        E-mail:  support@adva.com\n        Postal:  ADVA Optical Networking SE\n             Campus Martinsried\n             Fraunhoferstrasse 9a\n             82152 Martinsried/Munich\n             Germany\n        Phone: +49 089 89 06 65 0\n        Fax:  +49 089 89 06 65 199 ')
if mibBuilder.loadTexts: cmCommonMIB.setDescription('This module defines the Common MIB definitions used by \n             the FSP150CM and FSP150CC product lines. \n             Copyright (C) ADVA.')
subproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1))
f3Capabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2))
nemihubshelf = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 1))
ge101 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 2))
ge206 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 3))
ge201 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 4))
ge201se = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 5))
ge206f = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 6))
cmagg = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 7))
ge112 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 8))
ge114 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 9))
ge206v = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 10))
xg210 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 11))
t1804 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 12))
t3204 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 13))
gesyncprobe = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 14))
ge114H = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 15))
ge114PH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 16))
ge114S = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 17))
ge114SH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 18))
sh1pcs = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 19))
ge112Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 20))
ge112ProM = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 21))
ge114Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 22))
ge114ProC = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 23))
ge114ProSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 24))
ge114ProCSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 25))
ge114ProHE = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 26))
xg210c = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 27))
ge112ProH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 28))
ge114G = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 29))
ge114ProVMH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 30))
ge114ProVMCH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 31))
ge114ProVMCSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 32))
ge112ProVM = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 33))
ge101Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 34))
go102ProS = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 35))
go102ProSP = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 36))
cx101Pro30A = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 37))
cx102Pro30A = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 38))
xg116Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 39))
xg120Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 40))
xg116ProH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 41))
ge102ProH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 42))
ge102ProEFMH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 43))
go102ProSM = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 44))
xg118ProSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 45))
xg118ProacSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 46))
ge114ProVMSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 47))
ge104 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 48))
xg120ProSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 49))
class PortType(TextualConvention, Integer32):
    description = 'Enumerations for types of ports.\n             eth-access  - Ethernet Access Port, \n             eth-network - Ethernet Network Port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eth-access", 1), ("eth-network", 2))

class TrafficDirection(TextualConvention, Integer32):
    description = 'Enumerations for direction of traffic.  \n             a2n     - Access to Network direction, \n             n2a     - Network to Access direction,\n             ingress - Entering system direction,\n             egress  - Away from system direction,\n             n2n     - Network to Network direction.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("a2n", 1), ("n2a", 2), ("ingress", 3), ("egress", 4), ("n2n", 5))

class VlanId(TextualConvention, Integer32):
    description = 'Textual Convention for the Vlan Id.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class VlanPriority(TextualConvention, Integer32):
    description = 'Textual Convention for the Vlan Priority.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class VlanTagType(TextualConvention, Integer32):
    description = 'Textual Convention for the Type of VLAN Tag.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("inner-vlantag", 1), ("outer-vlantag", 2), ("n2a-priorityMapping", 3), ("mplsLabel", 4), ("vcLabel", 5), ("encapOuterVlanTag", 6))

class AdminState(TextualConvention, Integer32):
    description = "Administrative State used for FSP150CM entities.\n         in-service - represents normal, in-service, traffic passing\n                      state of the Entity;\n         management - represents the traffic passing state, \n                      however, alarms are not reported\n         maintenance- represents the mandatory state of operating \n                      loopbacks, ECPA test as well as Etherjack \n                      diagnosis operations, alarms are not reported \n         disabled   - represents the disabled state, user traffic is not passed,\n                      management traffic is passed, alarms are not reported\n         unassigned - represents the disabled state, \n                      traffic(user or management) is not passed,\n                      alarms are not monitored.\n         monitored  - represents the monitored state.  \n                      Used for retrieving performance monitoring on entity, but entity can't be used for normal operation.\n                      Alarms are reported "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("in-service", 1), ("management", 2), ("maintenance", 3), ("disabled", 4), ("unassigned", 5), ("monitored", 6))

class OperationalState(TextualConvention, Integer32):
    description = 'Operational State used for FSP150CM entities.\n         normal - represents operational state UP,\n         outage - represents operational state DOWN.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("outage", 2))

class SecondaryState(TextualConvention, Bits):
    description = 'Secondary state used for FSP150CM entities.\n         active                 - Active,\n         automaticinservice     - Automatic In Service,\n         facilityfailure        - Facility Failure,\n         fault                  - Fault,\n         loopback               - Loopback,\n         maintenance            - Maintenance,\n         mismatchedeqpt         - Mismatched Equipment,\n         standbyhot             - Standby Hot,\n         supportingentityoutage - Supporting Entity Outage,\n         unassigned             - Unassigned,\n         unequipped             - Unequipped,\n         disabled               - Disabled,\n         forcedoffline          - Forced offline,\n         initializing           - Initializing,\n         prtcl                  - Protocol,\n         blckd                  - Blocked,\n         mon-tx                 - Monitor TX,\n         mir-rx                 - Mirror RX,\n         cema                   - CEMA,\n         lkdo                   - LKDO'
    status = 'current'
    namedValues = NamedValues(("not-applicable", 0), ("active", 1), ("automaticinservice", 2), ("facilityfailure", 3), ("fault", 4), ("loopback", 5), ("maintenance", 6), ("mismatchedeqpt", 7), ("standbyhot", 8), ("supportingentityoutage", 9), ("unassigned", 10), ("unequipped", 11), ("disabled", 12), ("forcedoffline", 13), ("initializing", 14), ("prtcl", 15), ("blckd", 16), ("mon-tx", 17), ("mir-rx", 18), ("cema", 19), ("lkdo", 20), ("nomber", 21))

class EthernetPortSpeed(TextualConvention, Integer32):
    description = 'Describes the Ethernet Port Speed.\n         speed-unknown    : speed unknown \n         speed-10MB-full  : fixed speed 10MB full duplex\n         speed-10MB-half  : fixed speed 10MB half duplex\n         speed-100MB-full : fixed speed 100MB full duplex\n         speed-100MB-half : fixed speed 100MB half duplex\n         speed-1000MB-full    : fixed speed 1000MB full duplex\n         speed-1000MB-half    : fixed speed 1000MB half duplex\n         speed-auto       : Auto negotiation, advertise all speeds \n         speed-auto-10MB-full : Auto negotiation, advertise 10MB full duplex \n         speed-auto-10MB-half : Auto negotiation, advertise 10MB half duplex \n         speed-auto-100MB-full: Auto negotiation, advertise 100MB full duplex \n         speed-auto-100MB-half: Auto negotiation, advertise 100MB half duplex \n         speed-auto-1000MB-full: Auto negotiation, advertise 1000MB full duplex \n         speed-auto-1000MB-half: Auto negotiation, advertise 1000MB half duplex \n         speed-negotiating    : Auto negotiating, transient state\n         speed-auto-1000MB-full-master : Auto negotiation, advertise 1000MB full duplex, sync master\n         speed-auto-1000MB-full-slave : Auto negotiation, advertise 1000MB full duplex, sync slave\n         speed-none :                   Used to denote speed, when negotiating \n         speed-auto-1000MB-full-master-preferred : Auto negotiation,  \n                                                   advertise 1000MB full duplex, preferred sync master\n         speed-auto-1000MB-full-slave-preferred : Auto negotiation, \n                                                   advertise 1000MB full duplex, preferred sync slave\n         speed-10G-full  : fixed speed 10G full duplex\n         speed-auto-detect  : Auto detect speed; iterate through available speeds and test \n                              the link with remote end - if link is up at given speed, this speed is configured\n         .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    namedValues = NamedValues(("speed-unknown", 0), ("speed-10MB-full", 1), ("speed-10MB-half", 2), ("speed-100MB-full", 3), ("speed-100MB-half", 4), ("speed-1000MB-full", 5), ("speed-1000MB-half", 6), ("speed-auto", 7), ("speed-auto-10MB-full", 8), ("speed-auto-10MB-half", 9), ("speed-auto-100MB-full", 10), ("speed-auto-100MB-half", 11), ("speed-auto-1000MB-full", 12), ("speed-auto-1000MB-half", 13), ("speed-negotiating", 14), ("speed-auto-1000MB-full-master", 15), ("speed-auto-1000MB-full-slave", 16), ("speed-none", 17), ("speed-auto-1000MB-full-master-preferred", 18), ("speed-auto-1000MB-full-slave-preferred", 19), ("speed-10G-full", 20), ("speed-auto-detect", 21))

class EthernetMediaType(TextualConvention, Integer32):
    description = 'Describes the Ethernet Port Media Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("not-applicable", 0), ("copper", 1), ("fiber", 2), ("coppersfp", 3), ("auto", 4), ("none", 5), ("xdsl", 6), ("vmServerBackplane", 7))

class PerfCounter64(TextualConvention, Counter64):
    description = 'This type represents a non-negative 64-bit integer. The initial\n         value of this integer will  be 0.  It will increment with time,\n         however, the value will revert back to 0 when the time period\n         for history interval elapses.  Typically,  this will be noticed\n         at 15minute intervals and 1 day intervals.  Only the rollover\n         interval periods will keep counting to a maximum 64-bit value\n         and will wrap to 0 when this occurs.'
    status = 'current'

class PerfCounter32(TextualConvention, Counter32):
    description = 'This type represents a non-negative 32-bit integer. The initial\n         value of this integer will  be 0.  It will increment with time,\n         however, the value will revert back to 0 when the time period\n         for history interval elapses.  Typically,  this will be noticed\n         at 15minute intervals and 1 day intervals.  Only the rollover\n         interval periods will keep counting to a maximum 32-bit value\n         and will wrap to 0 when this occurs.'
    status = 'current'

class IpVersion(TextualConvention, Integer32):
    description = 'This type allows choice of IPv4 or IPv6 address specification.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class IpPriorityMapMode(TextualConvention, Integer32):
    description = 'This type allows choice of IP Priority Mapping Mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("not-applicable", 0), ("none", 1), ("priomap-tos", 2), ("priomap-dscp", 3))

class PriorityMapMode(TextualConvention, Integer32):
    description = 'This type allows choice of Priority Mapping Mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("priomap-none", 1), ("priomap-tos", 2), ("priomap-dscp", 3), ("priomap-8021p", 4), ("priomap-8021p-inner", 5), ("priomap-exp", 6), ("priomap-exp-inner", 7))

class SfpConnectorValue(TextualConvention, Integer32):
    description = 'This lists the SFP connector values.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("not-applicable", 0), ("unknown", 1), ("sc", 2), ("fcs1cu", 3), ("fcs2cu", 4), ("bnc-tnc", 5), ("fccoaxhdr", 6), ("fjack", 7), ("lc", 8), ("mt-rj", 9), ("mu", 10), ("sg", 11), ("optpigtail", 12), ("hssdc", 13), ("cupigtail", 14), ("vendorspecific", 15), ("rj45", 16))

class SfpIdentifierValue(TextualConvention, Integer32):
    description = 'This lists the SFP identifier values.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("notApplicable", 0), ("unknown", 1), ("gbic", 2), ("modsol", 3), ("sfp", 4), ("xbi300pin", 5), ("xenpak", 6), ("xfp", 7), ("xff", 8), ("xfpE", 9), ("xpak", 10), ("x2", 11), ("vendorSpecific", 12))

class RestartType(TextualConvention, Integer32):
    description = 'Restart Type used across all card types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("not-applicable", 0), ("warm-start", 1), ("cold-start", 2), ("boot-maintenance", 3), ("boot-normal", 4), ("boot-pxe", 5))

class SfpMediaType(TextualConvention, Integer32):
    description = 'Describes the SFP Media Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("not-applicable", 0), ("singlemode", 1), ("multimode", 2), ("multimode62-5", 3), ("copper", 4))

class ScheduleType(TextualConvention, Integer32):
    description = 'Describes the Schedule Type of a scheduled operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("periodic", 1), ("one-shot", 2))

class SchedActivityStatus(TextualConvention, Integer32):
    description = 'Scheduled Group Activity Status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("initial", 1), ("active", 2), ("suspended", 3), ("completed", 4))

class SchedActivityAction(TextualConvention, Integer32):
    description = 'Scheduled Activity Action.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-applicable", 0), ("suspend", 1), ("resume", 2))

class MepDestinationType(TextualConvention, Integer32):
    description = 'Destination MEP Types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-applicable", 0), ("mepid", 1), ("macaddress", 2))

class ClassOfServiceType(TextualConvention, Integer32):
    description = 'Class of Service Types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("cos-not-applicable", 0), ("cos-zero", 1), ("cos-one", 2), ("cos-two", 3), ("cos-three", 4), ("cos-four", 5), ("cos-five", 6), ("cos-six", 7), ("cos-seven", 8))

class SignalDirectionType(TextualConvention, Integer32):
    description = 'Signal Direction Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("input", 1), ("output", 2))

class AfpTagControl(TextualConvention, Integer32):
    description = 'Describes the Afp Tag Control.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ctag", 1), ("stag", 2), ("both", 3))

class CmP2PFlowType(TextualConvention, Integer32):
    description = 'Describes the Agg Flow Type,incluing e-line.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("eline", 1))

class CmTrafficACLPriorityType(TextualConvention, Integer32):
    description = 'Describes the Traffic acl priority type, including tos, dscp and traffic class.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notApplicable", 0), ("acl-tos", 1), ("acl-dscp", 2))

class CmTrafficAclFilterActionType(TextualConvention, Integer32):
    description = 'Enumerations for Access Control List \n          permit - Permit access, \n          deny   - Deny access.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("permit", 1), ("deny", 2))

class CmTrafficAclFilterType(TextualConvention, Integer32):
    description = 'Describes the Traffic acl filter type, including \n          MAC\n          IPV4\n          IPV6.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mac", 1), ("ipv4", 2), ("ipv6", 3))

class CmTrafficAclProtocolType(TextualConvention, Integer32):
    description = 'Describes the Traffic acl protocol type, including \n          tcp\n          udp.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notApplicable", 0), ("tcp", 1), ("udp", 2))

class VlanEthertype(TextualConvention, Integer32):
    description = 'Describes the Vlan Ether Type, \n          cvlan, \n          svlan.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cvlan", 1), ("svlan", 2))

class CmPmBinAction(TextualConvention, Integer32):
    description = 'Provides ability to clear the contents of PM bin.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("not-applicable", 0), ("clear", 1))

class CmPmIntervalType(TextualConvention, Integer32):
    description = 'Describes the Performance Monitoring Interval Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("interval-15min", 1), ("interval-1day", 2), ("rollover", 3), ("interval-5min", 4))

class TDMFrequencySourceType(TextualConvention, Integer32):
    description = 'Enumerations for TDM Frequency Source\n             loopTiming,\n             systemTiming,\n             lineTiming'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("loopTiming", 1), ("systemTiming", 2), ("lineTiming", 3))

class F3DisplayString(TextualConvention, OctetString):
    description = 'This object is similar with DisplayString, \n            and the difference is its length is 2047.\n            \n            Any object defined using this syntax may not exceed 2047\n            characters in length.'
    status = 'current'
    displayHint = '2047a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2047)

class Decimal32(TextualConvention, Unsigned32):
    description = 'The value is encoded in a Decimal32 interchange format.\n         The decimal value should be calculated as follows:\n\n         (-1)^sign x 10^(exponent-101) x mantissa\n\n         The individual components of the equation are coded in two different\n         formats depending on the range of the mantissa.\n\n         Format A:\n         Second and third bits can be: 00, 01 or 10\n\n         s EEeeeeee mmmmmmm mmmmmmmm mmmmmmmm\n\n         sign: coded on a 1 bit - s\n         exponent: coded on 8 bits - EEeeeeee\n         where EE: 00, 01 or 10\n         mantissa: coded on 24 bits - 0mmmmmmm mmmmmmmm mmmmmmmm\n\n         Format B:\n         For a larger mantissa.\n         Second and third bits are: 11\n\n         s 11 EEeeeeee mmmmm mmmmmmmm mmmmmmmm\n\n         sign: coded on a 1 bit - s\n         exponent: coded on 8 bits - EEeeeeee\n         where EE: 00, 01 or 10\n         mantissa: coded on 24 bits - 100mmmmm mmmmmmmm mmmmmmmm'
    status = 'current'

class UserInterfaceType(TextualConvention, Integer32):
    description = 'Denotes used user interface type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("cli", 1), ("gui", 2), ("netconf", 3), ("snmp", 4))

class FlowSecState(TextualConvention, Integer32):
    description = 'Flow secure state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("secureNormal", 1), ("secureBlocked", 2), ("unsecureNormal", 3), ("unsecureBlocked", 4))

class UsbOperationalMode(TextualConvention, Integer32):
    description = 'Types of usb operational mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cellular-modem", 1), ("srv-access", 2), ("nte-access", 3))

mibBuilder.exportSymbols("CM-COMMON-MIB", PerfCounter32=PerfCounter32, SchedActivityAction=SchedActivityAction, UserInterfaceType=UserInterfaceType, xg116ProH=xg116ProH, ge114ProVMH=ge114ProVMH, go102ProS=go102ProS, CmTrafficACLPriorityType=CmTrafficACLPriorityType, ScheduleType=ScheduleType, ge102ProEFMH=ge102ProEFMH, PYSNMP_MODULE_ID=cmCommonMIB, xg120ProSH=xg120ProSH, subproducts=subproducts, ge102ProH=ge102ProH, ge114ProSH=ge114ProSH, ge114G=ge114G, ge114ProHE=ge114ProHE, xg120Pro=xg120Pro, ge114ProCSH=ge114ProCSH, ge114ProVMCH=ge114ProVMCH, ge112ProVM=ge112ProVM, cmCommonMIB=cmCommonMIB, ge112=ge112, ge114ProVMSH=ge114ProVMSH, ge114Pro=ge114Pro, f3Capabilities=f3Capabilities, PriorityMapMode=PriorityMapMode, AdminState=AdminState, IpVersion=IpVersion, CmTrafficAclProtocolType=CmTrafficAclProtocolType, FlowSecState=FlowSecState, ClassOfServiceType=ClassOfServiceType, ge114=ge114, go102ProSP=go102ProSP, F3DisplayString=F3DisplayString, ge114ProC=ge114ProC, TDMFrequencySourceType=TDMFrequencySourceType, cx102Pro30A=cx102Pro30A, ge206v=ge206v, t1804=t1804, CmTrafficAclFilterType=CmTrafficAclFilterType, CmPmIntervalType=CmPmIntervalType, ge114ProVMCSH=ge114ProVMCSH, RestartType=RestartType, ge206=ge206, VlanTagType=VlanTagType, ge112ProH=ge112ProH, gesyncprobe=gesyncprobe, ge206f=ge206f, ge112Pro=ge112Pro, UsbOperationalMode=UsbOperationalMode, SignalDirectionType=SignalDirectionType, TrafficDirection=TrafficDirection, ge112ProM=ge112ProM, CmPmBinAction=CmPmBinAction, SfpConnectorValue=SfpConnectorValue, CmP2PFlowType=CmP2PFlowType, ge114S=ge114S, SfpMediaType=SfpMediaType, ge101=ge101, xg210=xg210, ge201se=ge201se, EthernetPortSpeed=EthernetPortSpeed, MepDestinationType=MepDestinationType, OperationalState=OperationalState, xg210c=xg210c, ge114PH=ge114PH, sh1pcs=sh1pcs, nemihubshelf=nemihubshelf, SfpIdentifierValue=SfpIdentifierValue, xg118ProSH=xg118ProSH, AfpTagControl=AfpTagControl, PortType=PortType, cx101Pro30A=cx101Pro30A, ge114SH=ge114SH, PerfCounter64=PerfCounter64, SchedActivityStatus=SchedActivityStatus, CmTrafficAclFilterActionType=CmTrafficAclFilterActionType, go102ProSM=go102ProSM, VlanPriority=VlanPriority, ge114H=ge114H, t3204=t3204, ge104=ge104, xg116Pro=xg116Pro, Decimal32=Decimal32, EthernetMediaType=EthernetMediaType, cmagg=cmagg, IpPriorityMapMode=IpPriorityMapMode, SecondaryState=SecondaryState, VlanId=VlanId, ge201=ge201, VlanEthertype=VlanEthertype, xg118ProacSH=xg118ProacSH, ge101Pro=ge101Pro)
