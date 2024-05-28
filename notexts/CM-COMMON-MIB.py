#
# PySNMP MIB module CM-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/CM-COMMON-MIB
# Produced by pysmi-1.1.12 at Tue May 28 13:54:49 2024
# On host fv-az529-55 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, ModuleIdentity, Bits, NotificationType, IpAddress, Unsigned32, MibIdentifier, Counter32, Gauge32, Counter64, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "ModuleIdentity", "Bits", "NotificationType", "IpAddress", "Unsigned32", "MibIdentifier", "Counter32", "Gauge32", "Counter64", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1))
cmCommonMIB.setRevisions(('2021-01-27 00:00',))
if mibBuilder.loadTexts: cmCommonMIB.setLastUpdated('202101270000Z')
if mibBuilder.loadTexts: cmCommonMIB.setOrganization('ADVA Optical Networking SE')
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
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eth-access", 1), ("eth-network", 2))

class TrafficDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("a2n", 1), ("n2a", 2), ("ingress", 3), ("egress", 4), ("n2n", 5))

class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class VlanPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class VlanTagType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("inner-vlantag", 1), ("outer-vlantag", 2), ("n2a-priorityMapping", 3), ("mplsLabel", 4), ("vcLabel", 5), ("encapOuterVlanTag", 6))

class AdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("in-service", 1), ("management", 2), ("maintenance", 3), ("disabled", 4), ("unassigned", 5), ("monitored", 6))

class OperationalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("outage", 2))

class SecondaryState(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("not-applicable", 0), ("active", 1), ("automaticinservice", 2), ("facilityfailure", 3), ("fault", 4), ("loopback", 5), ("maintenance", 6), ("mismatchedeqpt", 7), ("standbyhot", 8), ("supportingentityoutage", 9), ("unassigned", 10), ("unequipped", 11), ("disabled", 12), ("forcedoffline", 13), ("initializing", 14), ("prtcl", 15), ("blckd", 16), ("mon-tx", 17), ("mir-rx", 18), ("cema", 19), ("lkdo", 20), ("nomber", 21))

class EthernetPortSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    namedValues = NamedValues(("speed-unknown", 0), ("speed-10MB-full", 1), ("speed-10MB-half", 2), ("speed-100MB-full", 3), ("speed-100MB-half", 4), ("speed-1000MB-full", 5), ("speed-1000MB-half", 6), ("speed-auto", 7), ("speed-auto-10MB-full", 8), ("speed-auto-10MB-half", 9), ("speed-auto-100MB-full", 10), ("speed-auto-100MB-half", 11), ("speed-auto-1000MB-full", 12), ("speed-auto-1000MB-half", 13), ("speed-negotiating", 14), ("speed-auto-1000MB-full-master", 15), ("speed-auto-1000MB-full-slave", 16), ("speed-none", 17), ("speed-auto-1000MB-full-master-preferred", 18), ("speed-auto-1000MB-full-slave-preferred", 19), ("speed-10G-full", 20), ("speed-auto-detect", 21))

class EthernetMediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("not-applicable", 0), ("copper", 1), ("fiber", 2), ("coppersfp", 3), ("auto", 4), ("none", 5), ("xdsl", 6), ("vmServerBackplane", 7))

class PerfCounter64(TextualConvention, Counter64):
    status = 'current'

class PerfCounter32(TextualConvention, Counter32):
    status = 'current'

class IpVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class IpPriorityMapMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("not-applicable", 0), ("none", 1), ("priomap-tos", 2), ("priomap-dscp", 3))

class PriorityMapMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("priomap-none", 1), ("priomap-tos", 2), ("priomap-dscp", 3), ("priomap-8021p", 4), ("priomap-8021p-inner", 5), ("priomap-exp", 6), ("priomap-exp-inner", 7))

class SfpConnectorValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("not-applicable", 0), ("unknown", 1), ("sc", 2), ("fcs1cu", 3), ("fcs2cu", 4), ("bnc-tnc", 5), ("fccoaxhdr", 6), ("fjack", 7), ("lc", 8), ("mt-rj", 9), ("mu", 10), ("sg", 11), ("optpigtail", 12), ("hssdc", 13), ("cupigtail", 14), ("vendorspecific", 15), ("rj45", 16))

class SfpIdentifierValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("notApplicable", 0), ("unknown", 1), ("gbic", 2), ("modsol", 3), ("sfp", 4), ("xbi300pin", 5), ("xenpak", 6), ("xfp", 7), ("xff", 8), ("xfpE", 9), ("xpak", 10), ("x2", 11), ("vendorSpecific", 12))

class RestartType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("not-applicable", 0), ("warm-start", 1), ("cold-start", 2), ("boot-maintenance", 3), ("boot-normal", 4), ("boot-pxe", 5))

class SfpMediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("not-applicable", 0), ("singlemode", 1), ("multimode", 2), ("multimode62-5", 3), ("copper", 4))

class ScheduleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("periodic", 1), ("one-shot", 2))

class SchedActivityStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("initial", 1), ("active", 2), ("suspended", 3), ("completed", 4))

class SchedActivityAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-applicable", 0), ("suspend", 1), ("resume", 2))

class MepDestinationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-applicable", 0), ("mepid", 1), ("macaddress", 2))

class ClassOfServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("cos-not-applicable", 0), ("cos-zero", 1), ("cos-one", 2), ("cos-two", 3), ("cos-three", 4), ("cos-four", 5), ("cos-five", 6), ("cos-six", 7), ("cos-seven", 8))

class SignalDirectionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("input", 1), ("output", 2))

class AfpTagControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ctag", 1), ("stag", 2), ("both", 3))

class CmP2PFlowType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("eline", 1))

class CmTrafficACLPriorityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notApplicable", 0), ("acl-tos", 1), ("acl-dscp", 2))

class CmTrafficAclFilterActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("permit", 1), ("deny", 2))

class CmTrafficAclFilterType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mac", 1), ("ipv4", 2), ("ipv6", 3))

class CmTrafficAclProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notApplicable", 0), ("tcp", 1), ("udp", 2))

class VlanEthertype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cvlan", 1), ("svlan", 2))

class CmPmBinAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("not-applicable", 0), ("clear", 1))

class CmPmIntervalType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("interval-15min", 1), ("interval-1day", 2), ("rollover", 3), ("interval-5min", 4))

class TDMFrequencySourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("loopTiming", 1), ("systemTiming", 2), ("lineTiming", 3))

class F3DisplayString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2047a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2047)

class Decimal32(TextualConvention, Unsigned32):
    status = 'current'

class UserInterfaceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("cli", 1), ("gui", 2), ("netconf", 3), ("snmp", 4))

class FlowSecState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("secureNormal", 1), ("secureBlocked", 2), ("unsecureNormal", 3), ("unsecureBlocked", 4))

class UsbOperationalMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cellular-modem", 1), ("srv-access", 2), ("nte-access", 3))

mibBuilder.exportSymbols("CM-COMMON-MIB", ge206f=ge206f, xg118ProacSH=xg118ProacSH, TDMFrequencySourceType=TDMFrequencySourceType, ge206=ge206, f3Capabilities=f3Capabilities, ge114SH=ge114SH, ge102ProH=ge102ProH, VlanTagType=VlanTagType, UsbOperationalMode=UsbOperationalMode, xg210=xg210, CmTrafficAclProtocolType=CmTrafficAclProtocolType, ge112ProVM=ge112ProVM, ge114ProVMCSH=ge114ProVMCSH, xg120Pro=xg120Pro, IpVersion=IpVersion, CmPmBinAction=CmPmBinAction, SchedActivityStatus=SchedActivityStatus, ge114ProVMCH=ge114ProVMCH, CmTrafficAclFilterActionType=CmTrafficAclFilterActionType, t3204=t3204, SfpMediaType=SfpMediaType, PerfCounter64=PerfCounter64, ge201se=ge201se, go102ProS=go102ProS, FlowSecState=FlowSecState, xg116ProH=xg116ProH, CmP2PFlowType=CmP2PFlowType, subproducts=subproducts, ge101=ge101, MepDestinationType=MepDestinationType, ge114=ge114, ge114PH=ge114PH, gesyncprobe=gesyncprobe, UserInterfaceType=UserInterfaceType, go102ProSM=go102ProSM, xg120ProSH=xg120ProSH, SfpConnectorValue=SfpConnectorValue, ge112ProH=ge112ProH, cx102Pro30A=cx102Pro30A, ge102ProEFMH=ge102ProEFMH, EthernetPortSpeed=EthernetPortSpeed, F3DisplayString=F3DisplayString, CmTrafficAclFilterType=CmTrafficAclFilterType, ge112ProM=ge112ProM, ge112Pro=ge112Pro, SfpIdentifierValue=SfpIdentifierValue, ge112=ge112, ge101Pro=ge101Pro, ge201=ge201, PerfCounter32=PerfCounter32, PriorityMapMode=PriorityMapMode, AdminState=AdminState, ge114ProVMSH=ge114ProVMSH, Decimal32=Decimal32, sh1pcs=sh1pcs, ge114ProCSH=ge114ProCSH, ge114S=ge114S, ScheduleType=ScheduleType, CmTrafficACLPriorityType=CmTrafficACLPriorityType, IpPriorityMapMode=IpPriorityMapMode, VlanPriority=VlanPriority, ge114ProSH=ge114ProSH, PortType=PortType, EthernetMediaType=EthernetMediaType, xg116Pro=xg116Pro, nemihubshelf=nemihubshelf, SignalDirectionType=SignalDirectionType, RestartType=RestartType, ge114ProVMH=ge114ProVMH, AfpTagControl=AfpTagControl, OperationalState=OperationalState, xg210c=xg210c, VlanEthertype=VlanEthertype, CmPmIntervalType=CmPmIntervalType, ge114H=ge114H, SchedActivityAction=SchedActivityAction, ge206v=ge206v, cmagg=cmagg, SecondaryState=SecondaryState, cx101Pro30A=cx101Pro30A, ge114Pro=ge114Pro, TrafficDirection=TrafficDirection, ge114ProHE=ge114ProHE, ge114ProC=ge114ProC, ClassOfServiceType=ClassOfServiceType, ge114G=ge114G, t1804=t1804, cmCommonMIB=cmCommonMIB, VlanId=VlanId, xg118ProSH=xg118ProSH, PYSNMP_MODULE_ID=cmCommonMIB, go102ProSP=go102ProSP, ge104=ge104)
