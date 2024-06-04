#
# PySNMP MIB module IEEE8021-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IEEE8021-CFM-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:14:18 2024
# On host fv-az1385-751 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
IEEE8021VlanIndex, ieee802dot1mibs = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021VlanIndex", "ieee802dot1mibs")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
LldpChassisId, LldpChassisIdSubtype, LldpPortId, LldpPortIdSubtype = mibBuilder.importSymbols("LLDP-MIB", "LldpChassisId", "LldpChassisIdSubtype", "LldpPortId", "LldpPortIdSubtype")
VlanId, VlanIdOrNone = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "VlanIdOrNone")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Gauge32, Unsigned32, MibIdentifier, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, TimeTicks, Integer32, Counter64, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "TimeTicks", "Integer32", "Counter64", "ModuleIdentity", "Bits")
TimeStamp, TAddress, TDomain, DisplayString, TruthValue, RowStatus, MacAddress, TimeInterval, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TAddress", "TDomain", "DisplayString", "TruthValue", "RowStatus", "MacAddress", "TimeInterval", "TextualConvention")
ieee8021CfmMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 8))
ieee8021CfmMib.setRevisions(('2011-02-27 00:00', '2008-11-18 00:00', '2008-10-15 00:00', '2007-06-10 00:00',))
if mibBuilder.loadTexts: ieee8021CfmMib.setLastUpdated('201102270000Z')
if mibBuilder.loadTexts: ieee8021CfmMib.setOrganization('IEEE 802.1 Working Group')
dot1agNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 0))
dot1agMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1))
dot1agCfmConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 2))
dot1agCfmStack = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 1))
dot1agCfmDefaultMd = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 2))
dot1agCfmVlan = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 3))
dot1agCfmConfigErrorList = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 4))
dot1agCfmMd = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 5))
dot1agCfmMa = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 6))
dot1agCfmMep = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 1, 7))
class Dot1agCfmMaintDomainNameType(TextualConvention, Integer32):
    reference = '21.6.5, Table 21-19'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("dnsLikeName", 2), ("macAddressAndUint", 3), ("charString", 4))

class Dot1agCfmMaintDomainName(TextualConvention, OctetString):
    reference = '21.6.5'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 43)

class Dot1agCfmMaintAssocNameType(TextualConvention, Integer32):
    reference = '21.6.5.4, Table 21-20'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 32))
    namedValues = NamedValues(("primaryVid", 1), ("charString", 2), ("unsignedInt16", 3), ("rfc2865VpnId", 4), ("iccFormat", 32))

class Dot1agCfmMaintAssocName(TextualConvention, OctetString):
    reference = '802.1ag clauses 21.6.5.4, 21.6.5.5, 21.6.5.6'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 45)

class Dot1agCfmMDLevel(TextualConvention, Integer32):
    reference = '802.1ag clauses 18.3, 21.4.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class Dot1agCfmMDLevelOrNone(TextualConvention, Integer32):
    reference = '802.1ag clauses 18.3, 12.14.3.1.3:c'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class Dot1agCfmMpDirection(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.6.3.2:c'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("down", 1), ("up", 2))

class Dot1agCfmPortStatus(TextualConvention, Integer32):
    reference = '12.14.7.6.3:f, 20.19.3 and 21.5.4'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("psNoPortStateTLV", 0), ("psBlocked", 1), ("psUp", 2))

class Dot1agCfmInterfaceStatus(TextualConvention, Integer32):
    reference = '12.14.7.6.3:g, 20.19.4 and 21.5.5'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("isNoInterfaceStatusTLV", 0), ("isUp", 1), ("isDown", 2), ("isTesting", 3), ("isUnknown", 4), ("isDormant", 5), ("isNotPresent", 6), ("isLowerLayerDown", 7))

class Dot1agCfmHighestDefectPri(TextualConvention, Integer32):
    reference = '20.1.2, 12.14.7.7.2:c and 20.33.9'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("defRDICCM", 1), ("defMACstatus", 2), ("defRemoteCCM", 3), ("defErrorCCM", 4), ("defXconCCM", 5))

class Dot1agCfmLowestAlarmPri(TextualConvention, Integer32):
    reference = '12.14.7.1.3:k and 20.9.5'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("allDef", 1), ("macRemErrXcon", 2), ("remErrXcon", 3), ("errXcon", 4), ("xcon", 5), ("noXcon", 6))

class Dot1agCfmMepId(TextualConvention, Unsigned32):
    reference = '802.1ag clauses 3.19 and 19.2.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8191)

class Dot1agCfmMepIdOrZero(TextualConvention, Unsigned32):
    reference = '19.2.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), )
class Dot1agCfmMhfCreation(TextualConvention, Integer32):
    reference = '12.14.5.1.3:c and 22.2.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("defMHFnone", 1), ("defMHFdefault", 2), ("defMHFexplicit", 3), ("defMHFdefer", 4))

class Dot1agCfmIdPermission(TextualConvention, Integer32):
    reference = '12.14.6.1.3:d and 21.5.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("sendIdNone", 1), ("sendIdChassis", 2), ("sendIdManage", 3), ("sendIdChassisManage", 4), ("sendIdDefer", 5))

class Dot1agCfmCcmInterval(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.6.1.3:e, 20.8.1 and 21.6.1.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("intervalInvalid", 0), ("interval300Hz", 1), ("interval10ms", 2), ("interval100ms", 3), ("interval1s", 4), ("interval10s", 5), ("interval1min", 6), ("interval10min", 7))

class Dot1agCfmFngState(TextualConvention, Integer32):
    reference = '12.14.7.1.3:f and 20.35'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("fngReset", 1), ("fngDefect", 2), ("fngReportDefect", 3), ("fngDefectReported", 4), ("fngDefectClearing", 5))

class Dot1agCfmRelayActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:g, 20.36.2.5, 21.9.5, and Table 21-27'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rlyHit", 1), ("rlyFdb", 2), ("rlyMpdb", 3))

class Dot1agCfmIngressActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:g, 20.36.2.6, 21.9.8.1, and Table 21-30 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("ingNoTlv", 0), ("ingOk", 1), ("ingDown", 2), ("ingBlocked", 3), ("ingVid", 4))

class Dot1agCfmEgressActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:o, 20.36.2.10, 21.9.9.1, and Table 21-32'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("egrNoTlv", 0), ("egrOK", 1), ("egrDown", 2), ("egrBlocked", 3), ("egrVid", 4))

class Dot1agCfmRemoteMepState(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.6.3:b, 20.22'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("rMepIdle", 1), ("rMepStart", 2), ("rMepFailed", 3), ("rMepOk", 4))

class Dot1afCfmIndexIntegerNextFree(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class Dot1agCfmMepDefects(TextualConvention, Bits):
    reference = '802.1ag clauses 12.14.7.1.3:o, 12.14.7.1.3:p, 12.14.7.1.3:q, 12.14.7.1.3:r, and 12.14.7.1.3:s.'
    status = 'current'
    namedValues = NamedValues(("bDefRDICCM", 0), ("bDefMACstatus", 1), ("bDefRemoteCCM", 2), ("bDefErrorCCM", 3), ("bDefXconCCM", 4))

class Dot1agCfmConfigErrors(TextualConvention, Bits):
    reference = '12.14.4.1.3:b and clauses 22.2.3 and 22.2.4'
    status = 'current'
    namedValues = NamedValues(("cfmLeak", 0), ("conflictingVids", 1), ("excessiveLevels", 2), ("overlappedLevels", 3))

class Dot1agCfmPbbComponentIdentifier(TextualConvention, Unsigned32):
    reference = '12.3 l)'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

dot1agCfmStackTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1), )
if mibBuilder.loadTexts: dot1agCfmStackTable.setStatus('deprecated')
dot1agCfmStackEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmStackifIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmStackVlanIdOrNone"), (0, "IEEE8021-CFM-MIB", "dot1agCfmStackMdLevel"), (0, "IEEE8021-CFM-MIB", "dot1agCfmStackDirection"))
if mibBuilder.loadTexts: dot1agCfmStackEntry.setStatus('deprecated')
dot1agCfmStackifIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dot1agCfmStackifIndex.setStatus('deprecated')
dot1agCfmStackVlanIdOrNone = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 2), VlanIdOrNone())
if mibBuilder.loadTexts: dot1agCfmStackVlanIdOrNone.setStatus('deprecated')
dot1agCfmStackMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 3), Dot1agCfmMDLevel())
if mibBuilder.loadTexts: dot1agCfmStackMdLevel.setStatus('deprecated')
dot1agCfmStackDirection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 4), Dot1agCfmMpDirection())
if mibBuilder.loadTexts: dot1agCfmStackDirection.setStatus('deprecated')
dot1agCfmStackMdIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmStackMdIndex.setStatus('deprecated')
dot1agCfmStackMaIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmStackMaIndex.setStatus('deprecated')
dot1agCfmStackMepId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 7), Dot1agCfmMepIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmStackMepId.setStatus('deprecated')
dot1agCfmStackMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 1, 1, 1, 8), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmStackMacAddress.setStatus('deprecated')
dot1agCfmVlanTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1), )
if mibBuilder.loadTexts: dot1agCfmVlanTable.setStatus('deprecated')
dot1agCfmVlanEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmVlanComponentId"), (0, "IEEE8021-CFM-MIB", "dot1agCfmVlanVid"))
if mibBuilder.loadTexts: dot1agCfmVlanEntry.setStatus('deprecated')
dot1agCfmVlanComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 1), Dot1agCfmPbbComponentIdentifier())
if mibBuilder.loadTexts: dot1agCfmVlanComponentId.setStatus('deprecated')
dot1agCfmVlanVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 2), VlanId())
if mibBuilder.loadTexts: dot1agCfmVlanVid.setStatus('deprecated')
dot1agCfmVlanPrimaryVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 3), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmVlanPrimaryVid.setStatus('deprecated')
dot1agCfmVlanRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 3, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmVlanRowStatus.setStatus('deprecated')
dot1agCfmDefaultMdDefLevel = MibScalar((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 1), Dot1agCfmMDLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmDefaultMdDefLevel.setStatus('current')
dot1agCfmDefaultMdDefMhfCreation = MibScalar((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("defMHFnone", 1), ("defMHFdefault", 2), ("defMHFexplicit", 3))).clone('defMHFnone')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmDefaultMdDefMhfCreation.setStatus('current')
dot1agCfmDefaultMdDefIdPermission = MibScalar((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("sendIdNone", 1), ("sendIdChassis", 2), ("sendIdManage", 3), ("sendIdChassisManage", 4))).clone('sendIdNone')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmDefaultMdDefIdPermission.setStatus('current')
dot1agCfmDefaultMdTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4), )
if mibBuilder.loadTexts: dot1agCfmDefaultMdTable.setStatus('deprecated')
dot1agCfmDefaultMdEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmDefaultMdComponentId"), (0, "IEEE8021-CFM-MIB", "dot1agCfmDefaultMdPrimaryVid"))
if mibBuilder.loadTexts: dot1agCfmDefaultMdEntry.setStatus('deprecated')
dot1agCfmDefaultMdComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 1), Dot1agCfmPbbComponentIdentifier())
if mibBuilder.loadTexts: dot1agCfmDefaultMdComponentId.setStatus('deprecated')
dot1agCfmDefaultMdPrimaryVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 2), VlanId())
if mibBuilder.loadTexts: dot1agCfmDefaultMdPrimaryVid.setStatus('deprecated')
dot1agCfmDefaultMdStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmDefaultMdStatus.setStatus('deprecated')
dot1agCfmDefaultMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 4), Dot1agCfmMDLevelOrNone().clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmDefaultMdLevel.setStatus('deprecated')
dot1agCfmDefaultMdMhfCreation = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 5), Dot1agCfmMhfCreation().clone('defMHFdefer')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmDefaultMdMhfCreation.setStatus('deprecated')
dot1agCfmDefaultMdIdPermission = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 2, 4, 1, 6), Dot1agCfmIdPermission().clone('sendIdDefer')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmDefaultMdIdPermission.setStatus('deprecated')
dot1agCfmConfigErrorListTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1), )
if mibBuilder.loadTexts: dot1agCfmConfigErrorListTable.setStatus('deprecated')
dot1agCfmConfigErrorListEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmConfigErrorListVid"), (0, "IEEE8021-CFM-MIB", "dot1agCfmConfigErrorListIfIndex"))
if mibBuilder.loadTexts: dot1agCfmConfigErrorListEntry.setStatus('deprecated')
dot1agCfmConfigErrorListVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1, 1), VlanId())
if mibBuilder.loadTexts: dot1agCfmConfigErrorListVid.setStatus('deprecated')
dot1agCfmConfigErrorListIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: dot1agCfmConfigErrorListIfIndex.setStatus('deprecated')
dot1agCfmConfigErrorListErrorType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 4, 1, 1, 3), Dot1agCfmConfigErrors()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmConfigErrorListErrorType.setStatus('deprecated')
dot1agCfmMdTableNextIndex = MibScalar((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 1), Dot1afCfmIndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdTableNextIndex.setStatus('current')
dot1agCfmMdTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2), )
if mibBuilder.loadTexts: dot1agCfmMdTable.setStatus('current')
dot1agCfmMdEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"))
if mibBuilder.loadTexts: dot1agCfmMdEntry.setStatus('current')
dot1agCfmMdIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmMdIndex.setStatus('current')
dot1agCfmMdFormat = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 2), Dot1agCfmMaintDomainNameType().clone('charString')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdFormat.setStatus('current')
dot1agCfmMdName = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 3), Dot1agCfmMaintDomainName().clone('DEFAULT')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdName.setStatus('current')
dot1agCfmMdMdLevel = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 4), Dot1agCfmMDLevel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdMdLevel.setStatus('current')
dot1agCfmMdMhfCreation = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("defMHFnone", 1), ("defMHFdefault", 2), ("defMHFexplicit", 3))).clone('defMHFnone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdMhfCreation.setStatus('current')
dot1agCfmMdMhfIdPermission = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("sendIdNone", 1), ("sendIdChassis", 2), ("sendIdManage", 3), ("sendIdChassisManage", 4))).clone('sendIdNone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdMhfIdPermission.setStatus('current')
dot1agCfmMdMaNextIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 7), Dot1afCfmIndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdMaNextIndex.setStatus('current')
dot1agCfmMdRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 5, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdRowStatus.setStatus('current')
dot1agCfmMaNetTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1), )
if mibBuilder.loadTexts: dot1agCfmMaNetTable.setStatus('current')
dot1agCfmMaNetEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"))
if mibBuilder.loadTexts: dot1agCfmMaNetEntry.setStatus('current')
dot1agCfmMaIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmMaIndex.setStatus('current')
dot1agCfmMaNetFormat = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 2), Dot1agCfmMaintAssocNameType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaNetFormat.setStatus('current')
dot1agCfmMaNetName = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 3), Dot1agCfmMaintAssocName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaNetName.setStatus('current')
dot1agCfmMaNetCcmInterval = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 4), Dot1agCfmCcmInterval().clone('interval1s')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaNetCcmInterval.setStatus('current')
dot1agCfmMaNetRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaNetRowStatus.setStatus('current')
dot1agCfmMaCompTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2), )
if mibBuilder.loadTexts: dot1agCfmMaCompTable.setStatus('deprecated')
dot1agCfmMaCompEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMaComponentId"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"))
if mibBuilder.loadTexts: dot1agCfmMaCompEntry.setStatus('deprecated')
dot1agCfmMaComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 1), Dot1agCfmPbbComponentIdentifier())
if mibBuilder.loadTexts: dot1agCfmMaComponentId.setStatus('deprecated')
dot1agCfmMaCompPrimaryVlanId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 2), VlanIdOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaCompPrimaryVlanId.setStatus('deprecated')
dot1agCfmMaCompMhfCreation = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 3), Dot1agCfmMhfCreation().clone('defMHFdefer')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaCompMhfCreation.setStatus('deprecated')
dot1agCfmMaCompIdPermission = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 4), Dot1agCfmIdPermission().clone('sendIdDefer')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaCompIdPermission.setStatus('deprecated')
dot1agCfmMaCompNumberOfVids = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaCompNumberOfVids.setStatus('deprecated')
dot1agCfmMaCompRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaCompRowStatus.setStatus('deprecated')
dot1agCfmMaMepListTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3), )
if mibBuilder.loadTexts: dot1agCfmMaMepListTable.setStatus('current')
dot1agCfmMaMepListEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaMepListIdentifier"))
if mibBuilder.loadTexts: dot1agCfmMaMepListEntry.setStatus('current')
dot1agCfmMaMepListIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3, 1, 1), Dot1agCfmMepId())
if mibBuilder.loadTexts: dot1agCfmMaMepListIdentifier.setStatus('current')
dot1agCfmMaMepListRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 6, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaMepListRowStatus.setStatus('current')
dot1agCfmMepTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1), )
if mibBuilder.loadTexts: dot1agCfmMepTable.setStatus('current')
dot1agCfmMepEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
if mibBuilder.loadTexts: dot1agCfmMepEntry.setStatus('current')
dot1agCfmMepIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 1), Dot1agCfmMepId())
if mibBuilder.loadTexts: dot1agCfmMepIdentifier.setStatus('current')
dot1agCfmMepIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepIfIndex.setStatus('current')
dot1agCfmMepDirection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 3), Dot1agCfmMpDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepDirection.setStatus('current')
dot1agCfmMepPrimaryVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepPrimaryVid.setStatus('current')
dot1agCfmMepActive = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepActive.setStatus('current')
dot1agCfmMepFngState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 6), Dot1agCfmFngState().clone('fngReset')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepFngState.setStatus('current')
dot1agCfmMepCciEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepCciEnabled.setStatus('current')
dot1agCfmMepCcmLtmPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepCcmLtmPriority.setStatus('current')
dot1agCfmMepMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepMacAddress.setStatus('current')
dot1agCfmMepLowPrDef = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 10), Dot1agCfmLowestAlarmPri().clone('macRemErrXcon')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepLowPrDef.setStatus('current')
dot1agCfmMepFngAlarmTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 11), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(250, 1000)).clone(250)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepFngAlarmTime.setStatus('current')
dot1agCfmMepFngResetTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 12), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(250, 1000)).clone(1000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepFngResetTime.setStatus('current')
dot1agCfmMepHighestPrDefect = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 13), Dot1agCfmHighestDefectPri()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepHighestPrDefect.setStatus('current')
dot1agCfmMepDefects = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 14), Dot1agCfmMepDefects()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDefects.setStatus('current')
dot1agCfmMepErrorCcmLastFailure = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1522))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepErrorCcmLastFailure.setStatus('current')
dot1agCfmMepXconCcmLastFailure = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1522))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepXconCcmLastFailure.setStatus('current')
dot1agCfmMepCcmSequenceErrors = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepCcmSequenceErrors.setStatus('current')
dot1agCfmMepCciSentCcms = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepCciSentCcms.setStatus('current')
dot1agCfmMepNextLbmTransId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepNextLbmTransId.setStatus('current')
dot1agCfmMepLbrIn = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrIn.setStatus('current')
dot1agCfmMepLbrInOutOfOrder = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrInOutOfOrder.setStatus('current')
dot1agCfmMepLbrBadMsdu = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrBadMsdu.setStatus('current')
dot1agCfmMepLtmNextSeqNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLtmNextSeqNumber.setStatus('current')
dot1agCfmMepUnexpLtrIn = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepUnexpLtrIn.setStatus('current')
dot1agCfmMepLbrOut = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrOut.setStatus('current')
dot1agCfmMepTransmitLbmStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 26), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmStatus.setStatus('current')
dot1agCfmMepTransmitLbmDestMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 27), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDestMacAddress.setStatus('current')
dot1agCfmMepTransmitLbmDestMepId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 28), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDestMepId.setStatus('current')
dot1agCfmMepTransmitLbmDestIsMepId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 29), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDestIsMepId.setStatus('current')
dot1agCfmMepTransmitLbmMessages = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmMessages.setStatus('current')
dot1agCfmMepTransmitLbmDataTlv = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 31), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDataTlv.setStatus('current')
dot1agCfmMepTransmitLbmVlanPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmVlanPriority.setStatus('current')
dot1agCfmMepTransmitLbmVlanDropEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 33), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmVlanDropEnable.setStatus('current')
dot1agCfmMepTransmitLbmResultOK = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 34), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmResultOK.setStatus('current')
dot1agCfmMepTransmitLbmSeqNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 35), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmSeqNumber.setStatus('current')
dot1agCfmMepTransmitLtmStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 36), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmStatus.setStatus('current')
dot1agCfmMepTransmitLtmFlags = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 37), Bits().clone(namedValues=NamedValues(("useFDBonly", 0))).clone(namedValues=NamedValues(("useFDBonly", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmFlags.setStatus('current')
dot1agCfmMepTransmitLtmTargetMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 38), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTargetMacAddress.setStatus('current')
dot1agCfmMepTransmitLtmTargetMepId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 39), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTargetMepId.setStatus('current')
dot1agCfmMepTransmitLtmTargetIsMepId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 40), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTargetIsMepId.setStatus('current')
dot1agCfmMepTransmitLtmTtl = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 41), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTtl.setStatus('current')
dot1agCfmMepTransmitLtmResult = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 42), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmResult.setStatus('current')
dot1agCfmMepTransmitLtmSeqNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 43), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmSeqNumber.setStatus('current')
dot1agCfmMepTransmitLtmEgressIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 44), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmEgressIdentifier.setStatus('current')
dot1agCfmMepRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 45), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepRowStatus.setStatus('current')
dot1agCfmMepPbbTeCanReportPbbTePresence = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 46), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepPbbTeCanReportPbbTePresence.setStatus('current')
dot1agCfmMepPbbTeTrafficMismatchDefect = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 47), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepPbbTeTrafficMismatchDefect.setStatus('current')
dot1agCfmMepPbbTransmitLbmLtmReverseVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 48), IEEE8021VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepPbbTransmitLbmLtmReverseVid.setStatus('current')
dot1agCfmMepPbbTeMismatchAlarm = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 49), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepPbbTeMismatchAlarm.setStatus('current')
dot1agCfmMepPbbTeLocalMismatchDefect = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 50), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepPbbTeLocalMismatchDefect.setStatus('current')
dot1agCfmMepPbbTeMismatchSinceReset = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 1, 1, 51), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepPbbTeMismatchSinceReset.setStatus('current')
dot1agCfmLtrTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2), )
if mibBuilder.loadTexts: dot1agCfmLtrTable.setStatus('current')
dot1agCfmLtrEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "IEEE8021-CFM-MIB", "dot1agCfmLtrSeqNumber"), (0, "IEEE8021-CFM-MIB", "dot1agCfmLtrReceiveOrder"))
if mibBuilder.loadTexts: dot1agCfmLtrEntry.setStatus('current')
dot1agCfmLtrSeqNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmLtrSeqNumber.setStatus('current')
dot1agCfmLtrReceiveOrder = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmLtrReceiveOrder.setStatus('current')
dot1agCfmLtrTtl = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrTtl.setStatus('current')
dot1agCfmLtrForwarded = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrForwarded.setStatus('current')
dot1agCfmLtrTerminalMep = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrTerminalMep.setStatus('current')
dot1agCfmLtrLastEgressIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrLastEgressIdentifier.setStatus('current')
dot1agCfmLtrNextEgressIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrNextEgressIdentifier.setStatus('current')
dot1agCfmLtrRelay = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 8), Dot1agCfmRelayActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrRelay.setStatus('current')
dot1agCfmLtrChassisIdSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 9), LldpChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrChassisIdSubtype.setStatus('current')
dot1agCfmLtrChassisId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 10), LldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrChassisId.setStatus('current')
dot1agCfmLtrManAddressDomain = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 11), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrManAddressDomain.setStatus('current')
dot1agCfmLtrManAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 12), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrManAddress.setStatus('current')
dot1agCfmLtrIngress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 13), Dot1agCfmIngressActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngress.setStatus('current')
dot1agCfmLtrIngressMac = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 14), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngressMac.setStatus('current')
dot1agCfmLtrIngressPortIdSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 15), LldpPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngressPortIdSubtype.setStatus('current')
dot1agCfmLtrIngressPortId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 16), LldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngressPortId.setStatus('current')
dot1agCfmLtrEgress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 17), Dot1agCfmEgressActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgress.setStatus('current')
dot1agCfmLtrEgressMac = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 18), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgressMac.setStatus('current')
dot1agCfmLtrEgressPortIdSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 19), LldpPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgressPortIdSubtype.setStatus('current')
dot1agCfmLtrEgressPortId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 20), LldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgressPortId.setStatus('current')
dot1agCfmLtrOrganizationSpecificTlv = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 2, 1, 21), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 1500), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrOrganizationSpecificTlv.setStatus('current')
dot1agCfmMepDbTable = MibTable((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3), )
if mibBuilder.loadTexts: dot1agCfmMepDbTable.setStatus('current')
dot1agCfmMepDbEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier"))
if mibBuilder.loadTexts: dot1agCfmMepDbEntry.setStatus('current')
dot1agCfmMepDbRMepIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 1), Dot1agCfmMepId())
if mibBuilder.loadTexts: dot1agCfmMepDbRMepIdentifier.setStatus('current')
dot1agCfmMepDbRMepState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 2), Dot1agCfmRemoteMepState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbRMepState.setStatus('current')
dot1agCfmMepDbRMepFailedOkTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbRMepFailedOkTime.setStatus('current')
dot1agCfmMepDbMacAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbMacAddress.setStatus('current')
dot1agCfmMepDbRdi = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbRdi.setStatus('current')
dot1agCfmMepDbPortStatusTlv = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 6), Dot1agCfmPortStatus().clone('psNoPortStateTLV')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbPortStatusTlv.setStatus('current')
dot1agCfmMepDbInterfaceStatusTlv = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 7), Dot1agCfmInterfaceStatus().clone('isNoInterfaceStatusTLV')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbInterfaceStatusTlv.setStatus('current')
dot1agCfmMepDbChassisIdSubtype = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 8), LldpChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbChassisIdSubtype.setStatus('current')
dot1agCfmMepDbChassisId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 9), LldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbChassisId.setStatus('current')
dot1agCfmMepDbManAddressDomain = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 10), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbManAddressDomain.setStatus('current')
dot1agCfmMepDbManAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 11), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDbManAddress.setStatus('current')
dot1agCfmMepDbRMepIsActive = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 8, 1, 7, 3, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmMepDbRMepIsActive.setStatus('current')
dot1agCfmFaultAlarm = NotificationType((1, 3, 111, 2, 802, 1, 1, 8, 0, 1)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMepHighestPrDefect"))
if mibBuilder.loadTexts: dot1agCfmFaultAlarm.setStatus('current')
dot1agCfmCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 2, 1))
dot1agCfmGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 8, 2, 2))
dot1agCfmStackGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 1)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmStackMdIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmStackMaIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmStackMepId"), ("IEEE8021-CFM-MIB", "dot1agCfmStackMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmStackGroup = dot1agCfmStackGroup.setStatus('deprecated')
dot1agCfmDefaultMdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 2)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefLevel"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefMhfCreation"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefIdPermission"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdLevel"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdMhfCreation"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdIdPermission"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmDefaultMdGroup = dot1agCfmDefaultMdGroup.setStatus('deprecated')
dot1agCfmVlanIdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 3)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmVlanPrimaryVid"), ("IEEE8021-CFM-MIB", "dot1agCfmVlanRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmVlanIdGroup = dot1agCfmVlanIdGroup.setStatus('deprecated')
dot1agCfmConfigErrorListGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 4)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmConfigErrorListErrorType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmConfigErrorListGroup = dot1agCfmConfigErrorListGroup.setStatus('deprecated')
dot1agCfmMdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 5)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMdTableNextIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMdName"), ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"), ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"), ("IEEE8021-CFM-MIB", "dot1agCfmMdMhfCreation"), ("IEEE8021-CFM-MIB", "dot1agCfmMdMhfIdPermission"), ("IEEE8021-CFM-MIB", "dot1agCfmMdMaNextIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMdRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmMdGroup = dot1agCfmMdGroup.setStatus('current')
dot1agCfmMaGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 6)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetCcmInterval"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetRowStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"), ("IEEE8021-CFM-MIB", "dot1agCfmMaCompMhfCreation"), ("IEEE8021-CFM-MIB", "dot1agCfmMaCompIdPermission"), ("IEEE8021-CFM-MIB", "dot1agCfmMaCompRowStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmMaCompNumberOfVids"), ("IEEE8021-CFM-MIB", "dot1agCfmMaMepListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmMaGroup = dot1agCfmMaGroup.setStatus('deprecated')
dot1agCfmMepGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 7)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"), ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"), ("IEEE8021-CFM-MIB", "dot1agCfmMepActive"), ("IEEE8021-CFM-MIB", "dot1agCfmMepFngState"), ("IEEE8021-CFM-MIB", "dot1agCfmMepCciEnabled"), ("IEEE8021-CFM-MIB", "dot1agCfmMepCcmLtmPriority"), ("IEEE8021-CFM-MIB", "dot1agCfmMepMacAddress"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLowPrDef"), ("IEEE8021-CFM-MIB", "dot1agCfmMepFngAlarmTime"), ("IEEE8021-CFM-MIB", "dot1agCfmMepFngResetTime"), ("IEEE8021-CFM-MIB", "dot1agCfmMepHighestPrDefect"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDefects"), ("IEEE8021-CFM-MIB", "dot1agCfmMepErrorCcmLastFailure"), ("IEEE8021-CFM-MIB", "dot1agCfmMepXconCcmLastFailure"), ("IEEE8021-CFM-MIB", "dot1agCfmMepCcmSequenceErrors"), ("IEEE8021-CFM-MIB", "dot1agCfmMepCciSentCcms"), ("IEEE8021-CFM-MIB", "dot1agCfmMepNextLbmTransId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrIn"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrInOutOfOrder"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrBadMsdu"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLtmNextSeqNumber"), ("IEEE8021-CFM-MIB", "dot1agCfmMepUnexpLtrIn"), ("IEEE8021-CFM-MIB", "dot1agCfmMepLbrOut"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDestMacAddress"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDestMepId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDestIsMepId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmMessages"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDataTlv"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmVlanPriority"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmVlanDropEnable"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmResultOK"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmSeqNumber"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmFlags"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTargetMacAddress"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTargetMepId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTargetIsMepId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmTtl"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmResult"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmSeqNumber"), ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmEgressIdentifier"), ("IEEE8021-CFM-MIB", "dot1agCfmMepRowStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrForwarded"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrRelay"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrChassisIdSubtype"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrChassisId"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrManAddress"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrManAddressDomain"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngress"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngressMac"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngressPortIdSubtype"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrIngressPortId"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgress"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgressMac"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgressPortIdSubtype"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrEgressPortId"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrTerminalMep"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrLastEgressIdentifier"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrNextEgressIdentifier"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrTtl"), ("IEEE8021-CFM-MIB", "dot1agCfmLtrOrganizationSpecificTlv"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmMepGroup = dot1agCfmMepGroup.setStatus('current')
dot1agCfmMepDbGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 8)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepState"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepFailedOkTime"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbMacAddress"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRdi"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbPortStatusTlv"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbInterfaceStatusTlv"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbChassisIdSubtype"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbChassisId"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbManAddressDomain"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbManAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmMepDbGroup = dot1agCfmMepDbGroup.setStatus('current')
dot1agCfmNotificationsGroup = NotificationGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 9)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmFaultAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmNotificationsGroup = dot1agCfmNotificationsGroup.setStatus('current')
ieee8021CfmMaNetGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 10)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetCcmInterval"), ("IEEE8021-CFM-MIB", "dot1agCfmMaNetRowStatus"), ("IEEE8021-CFM-MIB", "dot1agCfmMaMepListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021CfmMaNetGroup = ieee8021CfmMaNetGroup.setStatus('current')
ieee8021CfmDefaultMdDefGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 8, 2, 2, 11)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefLevel"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefMhfCreation"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdDefIdPermission"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021CfmDefaultMdDefGroup = ieee8021CfmDefaultMdDefGroup.setStatus('current')
dot1agCfmCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 8, 2, 1, 1)).setObjects(("IEEE8021-CFM-MIB", "dot1agCfmStackGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmDefaultMdGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmConfigErrorListGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMdGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMaGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMepGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmMepDbGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmNotificationsGroup"), ("IEEE8021-CFM-MIB", "dot1agCfmVlanIdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmCompliance = dot1agCfmCompliance.setStatus('deprecated')
mibBuilder.exportSymbols("IEEE8021-CFM-MIB", dot1agCfmMepCcmSequenceErrors=dot1agCfmMepCcmSequenceErrors, dot1agCfmGroups=dot1agCfmGroups, dot1agCfmLtrTable=dot1agCfmLtrTable, dot1agCfmLtrIngressPortId=dot1agCfmLtrIngressPortId, dot1agCfmConformance=dot1agCfmConformance, dot1agCfmMepTransmitLtmEgressIdentifier=dot1agCfmMepTransmitLtmEgressIdentifier, dot1agCfmLtrIngressPortIdSubtype=dot1agCfmLtrIngressPortIdSubtype, ieee8021CfmMib=ieee8021CfmMib, dot1agCfmMaNetRowStatus=dot1agCfmMaNetRowStatus, Dot1agCfmFngState=Dot1agCfmFngState, dot1agCfmMepTransmitLbmSeqNumber=dot1agCfmMepTransmitLbmSeqNumber, dot1agCfmMepDbInterfaceStatusTlv=dot1agCfmMepDbInterfaceStatusTlv, dot1agCfmConfigErrorListIfIndex=dot1agCfmConfigErrorListIfIndex, dot1agCfmStackifIndex=dot1agCfmStackifIndex, dot1agCfmMepDbChassisId=dot1agCfmMepDbChassisId, dot1agCfmMaNetName=dot1agCfmMaNetName, dot1agCfmCompliances=dot1agCfmCompliances, dot1agCfmMepPrimaryVid=dot1agCfmMepPrimaryVid, dot1agCfmMepTransmitLbmStatus=dot1agCfmMepTransmitLbmStatus, dot1agCfmMepCcmLtmPriority=dot1agCfmMepCcmLtmPriority, dot1agCfmConfigErrorListGroup=dot1agCfmConfigErrorListGroup, dot1agCfmVlanRowStatus=dot1agCfmVlanRowStatus, dot1agCfmLtrOrganizationSpecificTlv=dot1agCfmLtrOrganizationSpecificTlv, dot1agCfmConfigErrorListVid=dot1agCfmConfigErrorListVid, Dot1agCfmMaintAssocName=Dot1agCfmMaintAssocName, dot1agCfmMa=dot1agCfmMa, dot1agCfmLtrEgressMac=dot1agCfmLtrEgressMac, dot1agCfmMepTable=dot1agCfmMepTable, dot1agCfmMepDirection=dot1agCfmMepDirection, dot1agCfmMepTransmitLbmDestIsMepId=dot1agCfmMepTransmitLbmDestIsMepId, dot1agCfmVlan=dot1agCfmVlan, dot1agCfmMdMhfIdPermission=dot1agCfmMdMhfIdPermission, dot1agCfmMaNetEntry=dot1agCfmMaNetEntry, dot1agCfmLtrIngress=dot1agCfmLtrIngress, dot1agCfmConfigErrorListErrorType=dot1agCfmConfigErrorListErrorType, dot1agCfmMaComponentId=dot1agCfmMaComponentId, dot1agCfmFaultAlarm=dot1agCfmFaultAlarm, dot1agCfmMepDbTable=dot1agCfmMepDbTable, dot1agCfmStackMdLevel=dot1agCfmStackMdLevel, dot1agCfmMepPbbTransmitLbmLtmReverseVid=dot1agCfmMepPbbTransmitLbmLtmReverseVid, dot1agCfmMepDbManAddressDomain=dot1agCfmMepDbManAddressDomain, Dot1agCfmMpDirection=Dot1agCfmMpDirection, dot1agCfmMdTable=dot1agCfmMdTable, dot1agCfmLtrEntry=dot1agCfmLtrEntry, dot1agCfmNotificationsGroup=dot1agCfmNotificationsGroup, dot1agCfmMepNextLbmTransId=dot1agCfmMepNextLbmTransId, dot1agCfmMepTransmitLbmMessages=dot1agCfmMepTransmitLbmMessages, dot1agCfmMepPbbTeMismatchSinceReset=dot1agCfmMepPbbTeMismatchSinceReset, dot1agCfmStackDirection=dot1agCfmStackDirection, dot1agCfmVlanComponentId=dot1agCfmVlanComponentId, dot1agCfmConfigErrorListTable=dot1agCfmConfigErrorListTable, dot1agCfmVlanIdGroup=dot1agCfmVlanIdGroup, Dot1agCfmMhfCreation=Dot1agCfmMhfCreation, dot1agCfmMdEntry=dot1agCfmMdEntry, dot1agCfmMepDbMacAddress=dot1agCfmMepDbMacAddress, PYSNMP_MODULE_ID=ieee8021CfmMib, dot1agCfmStackMepId=dot1agCfmStackMepId, dot1agCfmMepLowPrDef=dot1agCfmMepLowPrDef, dot1agCfmLtrEgressPortId=dot1agCfmLtrEgressPortId, dot1agCfmMaCompEntry=dot1agCfmMaCompEntry, dot1agCfmMdRowStatus=dot1agCfmMdRowStatus, dot1agCfmConfigErrorListEntry=dot1agCfmConfigErrorListEntry, dot1agCfmMepTransmitLbmVlanDropEnable=dot1agCfmMepTransmitLbmVlanDropEnable, dot1agCfmLtrChassisId=dot1agCfmLtrChassisId, Dot1agCfmHighestDefectPri=Dot1agCfmHighestDefectPri, dot1agCfmMepTransmitLtmTargetMacAddress=dot1agCfmMepTransmitLtmTargetMacAddress, dot1agCfmMepDbRMepIsActive=dot1agCfmMepDbRMepIsActive, dot1agCfmMepTransmitLbmDestMacAddress=dot1agCfmMepTransmitLbmDestMacAddress, Dot1agCfmMaintDomainNameType=Dot1agCfmMaintDomainNameType, dot1agCfmMaIndex=dot1agCfmMaIndex, dot1agCfmMepTransmitLtmResult=dot1agCfmMepTransmitLtmResult, dot1agCfmMepPbbTeTrafficMismatchDefect=dot1agCfmMepPbbTeTrafficMismatchDefect, dot1agCfmVlanTable=dot1agCfmVlanTable, dot1agCfmMepPbbTeLocalMismatchDefect=dot1agCfmMepPbbTeLocalMismatchDefect, dot1agCfmMepRowStatus=dot1agCfmMepRowStatus, dot1agCfmMepTransmitLbmResultOK=dot1agCfmMepTransmitLbmResultOK, dot1agCfmMaGroup=dot1agCfmMaGroup, dot1agCfmStackTable=dot1agCfmStackTable, dot1agCfmMepDbManAddress=dot1agCfmMepDbManAddress, dot1agCfmVlanVid=dot1agCfmVlanVid, Dot1agCfmMDLevel=Dot1agCfmMDLevel, dot1agCfmDefaultMdDefMhfCreation=dot1agCfmDefaultMdDefMhfCreation, dot1agCfmMepActive=dot1agCfmMepActive, dot1agCfmMepDbRMepIdentifier=dot1agCfmMepDbRMepIdentifier, dot1agCfmMaCompTable=dot1agCfmMaCompTable, dot1agCfmMepXconCcmLastFailure=dot1agCfmMepXconCcmLastFailure, dot1agCfmStackMacAddress=dot1agCfmStackMacAddress, dot1agCfmMaNetFormat=dot1agCfmMaNetFormat, dot1agCfmMaMepListRowStatus=dot1agCfmMaMepListRowStatus, Dot1agCfmCcmInterval=Dot1agCfmCcmInterval, dot1agCfmMepIdentifier=dot1agCfmMepIdentifier, Dot1agCfmMaintAssocNameType=Dot1agCfmMaintAssocNameType, dot1agCfmMepFngAlarmTime=dot1agCfmMepFngAlarmTime, dot1agCfmMepTransmitLtmStatus=dot1agCfmMepTransmitLtmStatus, dot1agCfmMepDbPortStatusTlv=dot1agCfmMepDbPortStatusTlv, dot1agCfmLtrSeqNumber=dot1agCfmLtrSeqNumber, dot1agCfmMep=dot1agCfmMep, dot1agCfmMaMepListIdentifier=dot1agCfmMaMepListIdentifier, dot1agCfmMepDbGroup=dot1agCfmMepDbGroup, Dot1agCfmMepId=Dot1agCfmMepId, dot1agCfmLtrEgress=dot1agCfmLtrEgress, ieee8021CfmMaNetGroup=ieee8021CfmMaNetGroup, dot1agCfmLtrIngressMac=dot1agCfmLtrIngressMac, dot1agCfmMdIndex=dot1agCfmMdIndex, dot1agCfmDefaultMdEntry=dot1agCfmDefaultMdEntry, dot1agCfmVlanPrimaryVid=dot1agCfmVlanPrimaryVid, dot1agCfmMepDbRdi=dot1agCfmMepDbRdi, dot1agCfmVlanEntry=dot1agCfmVlanEntry, dot1agCfmMepFngState=dot1agCfmMepFngState, Dot1agCfmLowestAlarmPri=Dot1agCfmLowestAlarmPri, dot1agMIBObjects=dot1agMIBObjects, dot1agCfmMepDbChassisIdSubtype=dot1agCfmMepDbChassisIdSubtype, Dot1agCfmIngressActionFieldValue=Dot1agCfmIngressActionFieldValue, dot1agCfmMaCompRowStatus=dot1agCfmMaCompRowStatus, dot1agCfmMepLtmNextSeqNumber=dot1agCfmMepLtmNextSeqNumber, dot1agCfmMepLbrOut=dot1agCfmMepLbrOut, dot1agCfmStackVlanIdOrNone=dot1agCfmStackVlanIdOrNone, Dot1agCfmConfigErrors=Dot1agCfmConfigErrors, Dot1agCfmMepIdOrZero=Dot1agCfmMepIdOrZero, dot1agCfmLtrNextEgressIdentifier=dot1agCfmLtrNextEgressIdentifier, dot1agCfmLtrTerminalMep=dot1agCfmLtrTerminalMep, dot1agCfmMepCciSentCcms=dot1agCfmMepCciSentCcms, Dot1agCfmInterfaceStatus=Dot1agCfmInterfaceStatus, dot1agCfmMepLbrInOutOfOrder=dot1agCfmMepLbrInOutOfOrder, dot1agCfmMepTransmitLtmTtl=dot1agCfmMepTransmitLtmTtl, dot1agCfmMepFngResetTime=dot1agCfmMepFngResetTime, dot1agCfmMdGroup=dot1agCfmMdGroup, dot1agCfmMdFormat=dot1agCfmMdFormat, Dot1agCfmRelayActionFieldValue=Dot1agCfmRelayActionFieldValue, dot1agCfmStackMdIndex=dot1agCfmStackMdIndex, dot1agCfmMepTransmitLtmFlags=dot1agCfmMepTransmitLtmFlags, dot1agCfmMepDbEntry=dot1agCfmMepDbEntry, dot1agCfmMepIfIndex=dot1agCfmMepIfIndex, dot1agCfmMepDbRMepState=dot1agCfmMepDbRMepState, dot1agCfmDefaultMdMhfCreation=dot1agCfmDefaultMdMhfCreation, dot1agCfmMepHighestPrDefect=dot1agCfmMepHighestPrDefect, dot1agCfmMaMepListEntry=dot1agCfmMaMepListEntry, dot1agCfmMepPbbTeMismatchAlarm=dot1agCfmMepPbbTeMismatchAlarm, dot1agCfmLtrManAddress=dot1agCfmLtrManAddress, ieee8021CfmDefaultMdDefGroup=ieee8021CfmDefaultMdDefGroup, dot1agCfmMdMdLevel=dot1agCfmMdMdLevel, dot1agCfmDefaultMdComponentId=dot1agCfmDefaultMdComponentId, dot1agCfmMaMepListTable=dot1agCfmMaMepListTable, dot1agCfmMepTransmitLbmDestMepId=dot1agCfmMepTransmitLbmDestMepId, dot1agCfmLtrChassisIdSubtype=dot1agCfmLtrChassisIdSubtype, dot1agCfmMepTransmitLbmVlanPriority=dot1agCfmMepTransmitLbmVlanPriority, dot1agCfmStackGroup=dot1agCfmStackGroup, dot1agCfmConfigErrorList=dot1agCfmConfigErrorList, dot1agCfmMepCciEnabled=dot1agCfmMepCciEnabled, dot1agCfmMd=dot1agCfmMd, dot1agCfmMepDefects=dot1agCfmMepDefects, Dot1agCfmMDLevelOrNone=Dot1agCfmMDLevelOrNone, dot1agCfmDefaultMdLevel=dot1agCfmDefaultMdLevel, dot1agCfmLtrEgressPortIdSubtype=dot1agCfmLtrEgressPortIdSubtype, dot1agCfmMdMhfCreation=dot1agCfmMdMhfCreation, dot1agCfmMdMaNextIndex=dot1agCfmMdMaNextIndex, dot1agCfmLtrTtl=dot1agCfmLtrTtl, dot1agCfmMaCompMhfCreation=dot1agCfmMaCompMhfCreation, dot1agCfmMepPbbTeCanReportPbbTePresence=dot1agCfmMepPbbTeCanReportPbbTePresence, dot1agCfmLtrManAddressDomain=dot1agCfmLtrManAddressDomain, Dot1agCfmIdPermission=Dot1agCfmIdPermission, dot1agCfmMepTransmitLtmTargetMepId=dot1agCfmMepTransmitLtmTargetMepId, dot1agCfmMepUnexpLtrIn=dot1agCfmMepUnexpLtrIn, dot1agCfmMepDbRMepFailedOkTime=dot1agCfmMepDbRMepFailedOkTime, Dot1agCfmEgressActionFieldValue=Dot1agCfmEgressActionFieldValue, Dot1agCfmMaintDomainName=Dot1agCfmMaintDomainName, dot1agCfmMepLbrBadMsdu=dot1agCfmMepLbrBadMsdu, dot1agCfmDefaultMdDefIdPermission=dot1agCfmDefaultMdDefIdPermission, dot1agCfmCompliance=dot1agCfmCompliance, Dot1agCfmRemoteMepState=Dot1agCfmRemoteMepState, dot1agCfmDefaultMdStatus=dot1agCfmDefaultMdStatus, dot1agCfmMepTransmitLtmSeqNumber=dot1agCfmMepTransmitLtmSeqNumber, dot1agCfmDefaultMdGroup=dot1agCfmDefaultMdGroup, Dot1agCfmPbbComponentIdentifier=Dot1agCfmPbbComponentIdentifier, dot1agCfmMepEntry=dot1agCfmMepEntry, dot1agCfmStack=dot1agCfmStack, dot1agCfmMaCompIdPermission=dot1agCfmMaCompIdPermission, dot1agCfmLtrRelay=dot1agCfmLtrRelay, Dot1afCfmIndexIntegerNextFree=Dot1afCfmIndexIntegerNextFree, dot1agCfmMaCompPrimaryVlanId=dot1agCfmMaCompPrimaryVlanId, Dot1agCfmPortStatus=Dot1agCfmPortStatus, dot1agCfmLtrLastEgressIdentifier=dot1agCfmLtrLastEgressIdentifier, dot1agCfmMaNetCcmInterval=dot1agCfmMaNetCcmInterval, dot1agCfmDefaultMdDefLevel=dot1agCfmDefaultMdDefLevel, dot1agCfmMaCompNumberOfVids=dot1agCfmMaCompNumberOfVids, dot1agCfmMepLbrIn=dot1agCfmMepLbrIn, dot1agNotifications=dot1agNotifications, dot1agCfmMepGroup=dot1agCfmMepGroup, dot1agCfmStackEntry=dot1agCfmStackEntry, dot1agCfmMdTableNextIndex=dot1agCfmMdTableNextIndex, dot1agCfmDefaultMdTable=dot1agCfmDefaultMdTable, dot1agCfmStackMaIndex=dot1agCfmStackMaIndex, dot1agCfmMepTransmitLbmDataTlv=dot1agCfmMepTransmitLbmDataTlv, Dot1agCfmMepDefects=Dot1agCfmMepDefects, dot1agCfmMdName=dot1agCfmMdName, dot1agCfmMepTransmitLtmTargetIsMepId=dot1agCfmMepTransmitLtmTargetIsMepId, dot1agCfmDefaultMdIdPermission=dot1agCfmDefaultMdIdPermission, dot1agCfmMepErrorCcmLastFailure=dot1agCfmMepErrorCcmLastFailure, dot1agCfmMaNetTable=dot1agCfmMaNetTable, dot1agCfmMepMacAddress=dot1agCfmMepMacAddress, dot1agCfmLtrReceiveOrder=dot1agCfmLtrReceiveOrder, dot1agCfmDefaultMd=dot1agCfmDefaultMd, dot1agCfmDefaultMdPrimaryVid=dot1agCfmDefaultMdPrimaryVid, dot1agCfmLtrForwarded=dot1agCfmLtrForwarded)
