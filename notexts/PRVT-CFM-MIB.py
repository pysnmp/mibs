#
# PySNMP MIB module PRVT-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-CFM-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 16:54:25 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, TimeTicks, Counter32, Unsigned32, Integer32, ObjectIdentity, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "TimeTicks", "Counter32", "Unsigned32", "Integer32", "ObjectIdentity", "Bits", "NotificationType")
MacAddress, TDomain, TAddress, TimeStamp, TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TDomain", "TAddress", "TimeStamp", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
prvtCfmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 131))
prvtCfmMIB.setRevisions(('2014-04-17 00:00', '2011-04-11 00:00',))
if mibBuilder.loadTexts: prvtCfmMIB.setLastUpdated('201404170000Z')
if mibBuilder.loadTexts: prvtCfmMIB.setOrganization('BATM Advanced Communication')
class LldpChassisIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notSet", 0), ("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7))

class LldpChassisId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '250a'

class LldpPortIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notSet", 0), ("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7))

class LldpPortId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '250a'

class PrvtCfmMaintAssocName(TextualConvention, OctetString):
    reference = '802.1ag clauses 21.6.5.4, 21.6.5.5, 21.6.5.6'
    status = 'current'
    displayHint = '45a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 22)

class PrvtCfmMaintAssocNameOrNone(TextualConvention, OctetString):
    status = 'current'
    displayHint = '22a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 22)

class PrvtCfmMhfCreation(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.5.1.3:c and 22.2.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("defMHFnone", 1), ("defMHFdefault", 2), ("defMHFexplicit", 3), ("defMHFdefer", 4))

class PrvtCfmMhfCreationDef(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.5.1.3:c and 22.2.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("defMHFnone", 1), ("defMHFdefault", 2), ("defMHFexplicit", 3))

class PrvtCfmIdPermission(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.6.1.3:d and 21.5.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("sendIdNone", 1), ("sendIdChassis", 2), ("sendIdManage", 3), ("sendIdChassisManage", 4), ("sendIdDefer", 5))

class PrvtCfmIdPermissionDef(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.6.1.3:d and 21.5.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("sendIdNone", 1), ("sendIdChassis", 2), ("sendIdManage", 3), ("sendIdChassisManage", 4))

class PrvtCfmMaintAssocNameType(TextualConvention, Integer32):
    reference = '802.1ag clause 21.6.5.4, Table 21-20'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 32))
    namedValues = NamedValues(("primaryVid", 1), ("charString", 2), ("icc", 32))

class PrvtCfmCcmInterval(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.6.1.3:e, 20.8.1 and 21.6.1.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("interval300Hz", 1), ("interval10ms", 2), ("interval100ms", 3), ("interval1s", 4), ("interval10s", 5), ("interval1min", 6), ("interval10min", 7))

class PrvtCfmIndexIntegerNextFree(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class PrvtCfmMaintDomainNameType(TextualConvention, Integer32):
    reference = '802.1ag clause 21.6.5, Table 21-19'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 4))
    namedValues = NamedValues(("none", 1), ("charString", 4))

class PrvtCfmMaintDomainName(TextualConvention, OctetString):
    reference = '802.1ag clause 21.6.5'
    status = 'current'
    displayHint = '43a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 22)

class PrvtCfmMaintDomainNameOrNone(TextualConvention, OctetString):
    status = 'current'
    displayHint = '22a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 22)

class PrvtCfmMDLevelTC(TextualConvention, Integer32):
    reference = '802.1ag clauses 18.3, 21.4.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class PrvtCfmMpDirection(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.6.3.2:c'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("down", 1), ("up", 2))

class PrvtCfmMepIdOrZero(TextualConvention, Unsigned32):
    reference = '802.1ag clause 19.2.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 8191)

class PrvtCfmMepId(TextualConvention, Unsigned32):
    reference = '802.1ag clauses 3.19 and 19.2.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8191)

class PrvtCfmFngState(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.1.3:f and 20.35'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("fngReset", 1), ("fngDefect", 2), ("fngReportDefect", 3), ("fngDefectReported", 4), ("fngDefectClearing", 5))

class PrvtCfmLowestAlarmPri(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.1.3:k and 20.9.5'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("allDef", 1), ("macRemErrXcon", 2), ("remErrXcon", 3), ("errXcon", 4), ("xcon", 5), ("noXcon", 6))

class PrvtCfmHighestDefectPri(TextualConvention, Integer32):
    reference = '802.1ag clause 20.1.2, 12.14.7.7.2:c and 20.33.9'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("defRDICCM", 1), ("defMACstatus", 2), ("defRemoteCCM", 3), ("defErrorCCM", 4), ("defXconCCM", 5))

class PrvtCfmRelayActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:g, 20.36.2.5, 21.9.5, and Table 21-27'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rlyHit", 1), ("rlyFdb", 2), ("rlyMpdb", 3))

class PrvtCfmIngressActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:g, 20.36.2.6, 21.9.8.1, and Table 21-30'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ingOk", 1), ("ingDown", 2), ("ingBlocked", 3), ("ingVid", 4))

class PrvtCfmEgressActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:o, 20.36.2.10, 21.9.9.1, and Table 21-32'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notSet", 0), ("egrOK", 1), ("egrDown", 2), ("egrBlocked", 3), ("egrVid", 4))

class PrvtCfmRemoteMepState(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.6.3:b, 20.22'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("rMepIdle", 1), ("rMepStart", 2), ("rMepFailed", 3), ("rMepOk", 4))

class PrvtCfmPortStatus(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.6.3:f, 20.19.3 and 21.5.4'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("psNoPortStateTLV", 0), ("psBlocked", 1), ("psUp", 2))

class PrvtCfmInterfaceStatus(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.6.3:g, 20.19.4 and 21.5.5'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("isNoInterfaceStatusTLV", 0), ("isUp", 1), ("isDown", 2), ("isTesting", 3), ("isUnknown", 4), ("isDormant", 5), ("isNotPresent", 6), ("isLowerLayerDown", 7))

prvtCfmMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 0))
prvtCfmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1))
prvtCfmUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCfmUpdateInterval.setStatus('current')
prvtCfmShutdown = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCfmShutdown.setStatus('current')
prvtCfmStack = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 3))
prvtCfmStackTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 3, 1), )
if mibBuilder.loadTexts: prvtCfmStackTable.setStatus('current')
prvtCfmStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 3, 1, 1), ).setIndexNames((0, "PRVT-CFM-MIB", "prvtCfmStackInterfaceIndex"), (0, "PRVT-CFM-MIB", "prvtCfmStackServiceIdOrNone"), (0, "PRVT-CFM-MIB", "prvtCfmStackMdLevel"), (0, "PRVT-CFM-MIB", "prvtCfmStackDirection"))
if mibBuilder.loadTexts: prvtCfmStackEntry.setStatus('current')
prvtCfmStackInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 3, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: prvtCfmStackInterfaceIndex.setStatus('current')
prvtCfmStackServiceIdOrNone = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 3, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: prvtCfmStackServiceIdOrNone.setStatus('current')
prvtCfmStackMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 3, 1, 1, 3), PrvtCfmMDLevelTC())
if mibBuilder.loadTexts: prvtCfmStackMdLevel.setStatus('current')
prvtCfmStackDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 3, 1, 1, 4), PrvtCfmMpDirection())
if mibBuilder.loadTexts: prvtCfmStackDirection.setStatus('current')
prvtCfmStackMdName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 3, 1, 1, 5), PrvtCfmMaintDomainNameOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmStackMdName.setStatus('current')
prvtCfmStackMaName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 3, 1, 1, 6), PrvtCfmMaintAssocNameOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmStackMaName.setStatus('current')
prvtCfmStackMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 3, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmStackMepId.setStatus('current')
prvtCfmStackMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 3, 1, 1, 8), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmStackMacAddress.setStatus('current')
prvtCfmMd = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 4))
prvtCfmMdTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 4, 2), )
if mibBuilder.loadTexts: prvtCfmMdTable.setStatus('current')
prvtCfmMdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 4, 2, 1), ).setIndexNames((0, "PRVT-CFM-MIB", "prvtCfmMdName"))
if mibBuilder.loadTexts: prvtCfmMdEntry.setStatus('current')
prvtCfmMdName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 4, 2, 1, 1), PrvtCfmMaintDomainName())
if mibBuilder.loadTexts: prvtCfmMdName.setStatus('current')
prvtCfmMdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 4, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMdRowStatus.setStatus('current')
prvtCfmMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 4, 2, 1, 4), PrvtCfmMDLevelTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMdLevel.setStatus('current')
prvtCfmMdFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 4, 2, 1, 5), PrvtCfmMaintDomainNameType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMdFormat.setStatus('current')
prvtCfmMdMhfCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 4, 2, 1, 6), PrvtCfmMhfCreationDef()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMdMhfCreation.setStatus('current')
prvtCfmMdMhfIdPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 4, 2, 1, 7), PrvtCfmIdPermissionDef()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMdMhfIdPermission.setStatus('current')
prvtCfmMa = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5))
prvtCfmMaTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1), )
if mibBuilder.loadTexts: prvtCfmMaTable.setStatus('current')
prvtCfmMaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1), ).setIndexNames((0, "PRVT-CFM-MIB", "prvtCfmMdName"), (0, "PRVT-CFM-MIB", "prvtCfmMaName"))
if mibBuilder.loadTexts: prvtCfmMaEntry.setStatus('current')
prvtCfmMaName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 1), PrvtCfmMaintAssocName())
if mibBuilder.loadTexts: prvtCfmMaName.setStatus('current')
prvtCfmMaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaRowStatus.setStatus('current')
prvtCfmMaServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967294))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaServiceId.setStatus('current')
prvtCfmMaVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaVlanId.setStatus('current')
prvtCfmMaMhfCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 6), PrvtCfmMhfCreation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaMhfCreation.setStatus('current')
prvtCfmMaPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 7), PrvtCfmIdPermission()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaPermission.setStatus('current')
prvtCfmMaFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 8), PrvtCfmMaintAssocNameType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaFormat.setStatus('current')
prvtCfmMaCcmInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 9), PrvtCfmCcmInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaCcmInterval.setStatus('current')
prvtCfmMaAisLckReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 10), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaAisLckReceive.setStatus('current')
prvtCfmMaAisLckLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaAisLckLevel.setStatus('current')
prvtCfmMaAisLckInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("interval1s", 1), ("interval1min", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaAisLckInterval.setStatus('current')
prvtCfmMaAisLckPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaAisLckPriority.setStatus('current')
prvtCfmMaClearConnectivity = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 5, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaClearConnectivity.setStatus('current')
prvtCfmMep = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6))
prvtCfmMepTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1), )
if mibBuilder.loadTexts: prvtCfmMepTable.setStatus('current')
prvtCfmMepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1), ).setIndexNames((0, "PRVT-CFM-MIB", "prvtCfmMdName"), (0, "PRVT-CFM-MIB", "prvtCfmMaName"), (0, "PRVT-CFM-MIB", "prvtCfmMepIdentifier"))
if mibBuilder.loadTexts: prvtCfmMepEntry.setStatus('current')
prvtCfmMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 1), PrvtCfmMepId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepIdentifier.setStatus('current')
prvtCfmMepRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepRowStatus.setStatus('current')
prvtCfmMepInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepInterfaceIndex.setStatus('current')
prvtCfmMepDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 4), PrvtCfmMpDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepDirection.setStatus('current')
prvtCfmMepShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepShutdown.setStatus('current')
prvtCfmMepFngState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 6), PrvtCfmFngState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepFngState.setStatus('current')
prvtCfmMepCciEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 7), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepCciEnabled.setStatus('current')
prvtCfmMepCcmLtmPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepCcmLtmPriority.setStatus('current')
prvtCfmMepMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepMacAddress.setStatus('current')
prvtCfmMepLowPrDef = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 10), PrvtCfmLowestAlarmPri()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepLowPrDef.setStatus('current')
prvtCfmMepHighestPrDefect = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 11), PrvtCfmHighestDefectPri()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepHighestPrDefect.setStatus('current')
prvtCfmMepDefects = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 12), Bits().clone(namedValues=NamedValues(("bDefRDICCM", 0), ("bDefMACstatus", 1), ("bDefRemoteCCM", 2), ("bDefErrorCCM", 3), ("bDefXconCCM", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepDefects.setStatus('current')
prvtCfmMepErrorCcmLastFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepErrorCcmLastFailure.setStatus('current')
prvtCfmMepXconCcmLastFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepXconCcmLastFailure.setStatus('current')
prvtCfmMepCcmSequenceErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepCcmSequenceErrors.setStatus('current')
prvtCfmMepCciSentCcms = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepCciSentCcms.setStatus('current')
prvtCfmMepNextLbmTransId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepNextLbmTransId.setStatus('current')
prvtCfmMepLbrIn = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepLbrIn.setStatus('current')
prvtCfmMepLbrInOutOfOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepLbrInOutOfOrder.setStatus('current')
prvtCfmMepLbrBadMsdu = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepLbrBadMsdu.setStatus('current')
prvtCfmMepLtmNextSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepLtmNextSeqNumber.setStatus('current')
prvtCfmMepUnexpLtrIn = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepUnexpLtrIn.setStatus('current')
prvtCfmMepLbrOut = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepLbrOut.setStatus('current')
prvtCfmMepTransmitLbmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 24), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmStatus.setStatus('current')
prvtCfmMepTransmitLbmDestMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 25), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmDestMacAddress.setStatus('current')
prvtCfmMepTransmitLbmDestMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 26), PrvtCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmDestMepId.setStatus('current')
prvtCfmMepTransmitLbmDestIsMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 27), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmDestIsMepId.setStatus('current')
prvtCfmMepTransmitLbmMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmMessages.setStatus('current')
prvtCfmMepTransmitLbmDataTlv = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 29), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1462))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmDataTlv.setStatus('current')
prvtCfmMepTransmitLbmVlanPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmVlanPriority.setStatus('current')
prvtCfmMepTransmitLbmVlanDropEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 31), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmVlanDropEnable.setStatus('current')
prvtCfmMepTransmitLbmResultOK = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 32), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmResultOK.setStatus('current')
prvtCfmMepTransmitLbmSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 33), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmSeqNumber.setStatus('current')
prvtCfmMepTransmitLtmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 34), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLtmStatus.setStatus('current')
prvtCfmMepTransmitLtmFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 35), Bits().clone(namedValues=NamedValues(("useFDBonly", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLtmFlags.setStatus('current')
prvtCfmMepTransmitLtmTargetMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 36), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLtmTargetMacAddress.setStatus('current')
prvtCfmMepTransmitLtmTargetMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 37), PrvtCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLtmTargetMepId.setStatus('current')
prvtCfmMepTransmitLtmTargetIsMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 38), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLtmTargetIsMepId.setStatus('current')
prvtCfmMepTransmitLtmTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 39), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLtmTtl.setStatus('current')
prvtCfmMepTransmitLtmResult = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 40), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepTransmitLtmResult.setStatus('current')
prvtCfmMepTransmitLtmSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 41), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepTransmitLtmSeqNumber.setStatus('current')
prvtCfmMepTransmitLtmEgressIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 42), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLtmEgressIdentifier.setStatus('current')
prvtCfmMepAlarmSupressed = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 43), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepAlarmSupressed.setStatus('current')
prvtCfmMepAisCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 44), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepAisCondition.setStatus('current')
prvtCfmMepLckCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 45), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepLckCondition.setStatus('current')
prvtCfmMepAisLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 46), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("lifetime35s", 1), ("lifetime35min", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepAisLifetime.setStatus('current')
prvtCfmMepLckLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 47), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("lifetime35s", 1), ("lifetime35min", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepLckLifetime.setStatus('current')
prvtCfmMepTransmitMcastLbm = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 48), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitMcastLbm.setStatus('current')
prvtCfmMepTransmitLbmInfinite = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 49), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmInfinite.setStatus('current')
prvtCfmMepTransmitLbmDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 50), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmDelay.setStatus('current')
prvtCfmMepTransmitLbmTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 51), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmTimeout.setStatus('current')
prvtCfmMepTransmitLtmTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 52), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepTransmitLtmTimeout.setStatus('current')
prvtCfmMepTransmitLbmSentPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 53), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmSentPkts.setStatus('current')
prvtCfmMepTransmitLbmSuccessRate = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 54), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmSuccessRate.setStatus('current')
prvtCfmMepTransmitLbmMinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 55), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmMinTime.setStatus('current')
prvtCfmMepTransmitLbmAvgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 56), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmAvgTime.setStatus('current')
prvtCfmMepTransmitLbmMaxTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 57), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmMaxTime.setStatus('current')
prvtCfmMepFngAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 58), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(250, 1000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepFngAlarmTime.setStatus('current')
prvtCfmMepFngResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 59), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(250, 1000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMepFngResetTime.setStatus('current')
prvtCfmMepTransmitLbmRemainingMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 60), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmRemainingMessages.setStatus('current')
prvtCfmMepTransmitLbmCurrentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 1, 1, 61), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepTransmitLbmCurrentStatus.setStatus('current')
prvtCfmMepDbTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2), )
if mibBuilder.loadTexts: prvtCfmMepDbTable.setStatus('current')
prvtCfmMepDbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1), ).setIndexNames((0, "PRVT-CFM-MIB", "prvtCfmMdName"), (0, "PRVT-CFM-MIB", "prvtCfmMaName"), (0, "PRVT-CFM-MIB", "prvtCfmMepIdentifier"), (0, "PRVT-CFM-MIB", "prvtCfmMepDbRMepIdentifier"))
if mibBuilder.loadTexts: prvtCfmMepDbEntry.setStatus('current')
prvtCfmMepDbRMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: prvtCfmMepDbRMepIdentifier.setStatus('current')
prvtCfmMepDbRMepState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1, 2), PrvtCfmRemoteMepState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepDbRMepState.setStatus('current')
prvtCfmMepDbRMepFailedOkTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepDbRMepFailedOkTime.setStatus('current')
prvtCfmMepDbMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepDbMacAddress.setStatus('current')
prvtCfmMepDbRdi = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepDbRdi.setStatus('current')
prvtCfmMepDbPortStatusTlv = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1, 6), PrvtCfmPortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepDbPortStatusTlv.setStatus('current')
prvtCfmMepDbInterfaceStatusTlv = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1, 7), PrvtCfmInterfaceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepDbInterfaceStatusTlv.setStatus('current')
prvtCfmMepDbChassisIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1, 8), LldpChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepDbChassisIdSubtype.setStatus('current')
prvtCfmMepDbChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1, 9), LldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepDbChassisId.setStatus('current')
prvtCfmMepDbManAddressDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1, 10), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepDbManAddressDomain.setStatus('current')
prvtCfmMepDbManAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 2, 1, 11), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmMepDbManAddress.setStatus('current')
prvtCfmLtrTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3), )
if mibBuilder.loadTexts: prvtCfmLtrTable.setStatus('current')
prvtCfmLtrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1), ).setIndexNames((0, "PRVT-CFM-MIB", "prvtCfmMdName"), (0, "PRVT-CFM-MIB", "prvtCfmMaName"), (0, "PRVT-CFM-MIB", "prvtCfmMepIdentifier"), (0, "PRVT-CFM-MIB", "prvtCfmLtrSeqNumber"), (0, "PRVT-CFM-MIB", "prvtCfmLtrReceiveOrder"))
if mibBuilder.loadTexts: prvtCfmLtrEntry.setStatus('current')
prvtCfmLtrSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: prvtCfmLtrSeqNumber.setStatus('current')
prvtCfmLtrReceiveOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: prvtCfmLtrReceiveOrder.setStatus('current')
prvtCfmLtrTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrTtl.setStatus('current')
prvtCfmLtrForwarded = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrForwarded.setStatus('current')
prvtCfmLtrTerminalMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrTerminalMep.setStatus('current')
prvtCfmLtrLastEgressIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrLastEgressIdentifier.setStatus('current')
prvtCfmLtrNextEgressIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrNextEgressIdentifier.setStatus('current')
prvtCfmLtrRelay = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 8), PrvtCfmRelayActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrRelay.setStatus('current')
prvtCfmLtrChassisIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 9), LldpChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrChassisIdSubtype.setStatus('current')
prvtCfmLtrChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 10), LldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrChassisId.setStatus('current')
prvtCfmLtrManAddressDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 11), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrManAddressDomain.setStatus('current')
prvtCfmLtrManAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 12), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrManAddress.setStatus('current')
prvtCfmLtrIngress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 13), PrvtCfmIngressActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrIngress.setStatus('current')
prvtCfmLtrIngressMac = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 14), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrIngressMac.setStatus('current')
prvtCfmLtrIngressPortIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 15), LldpPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrIngressPortIdSubtype.setStatus('current')
prvtCfmLtrIngressPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 16), LldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrIngressPortId.setStatus('current')
prvtCfmLtrEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 17), PrvtCfmEgressActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrEgress.setStatus('current')
prvtCfmLtrEgressMac = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 18), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrEgressMac.setStatus('current')
prvtCfmLtrEgressPortIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 19), LldpPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrEgressPortIdSubtype.setStatus('current')
prvtCfmLtrEgressPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 20), LldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrEgressPortId.setStatus('current')
prvtCfmLtrOrganizationSpecificTlv = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 21), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrOrganizationSpecificTlv.setStatus('current')
prvtCfmLtrTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrTime.setStatus('current')
prvtCfmLtrSourceMac = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 3, 1, 23), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLtrSourceMac.setStatus('current')
prvtCfmLbrTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 4), )
if mibBuilder.loadTexts: prvtCfmLbrTable.setStatus('current')
prvtCfmLbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 4, 1), ).setIndexNames((0, "PRVT-CFM-MIB", "prvtCfmMdName"), (0, "PRVT-CFM-MIB", "prvtCfmMaName"), (0, "PRVT-CFM-MIB", "prvtCfmMepIdentifier"), (0, "PRVT-CFM-MIB", "prvtCfmLbrSeqNumber"), (0, "PRVT-CFM-MIB", "prvtCfmLbrReceiveOrder"))
if mibBuilder.loadTexts: prvtCfmLbrEntry.setStatus('current')
prvtCfmLbrSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: prvtCfmLbrSeqNumber.setStatus('current')
prvtCfmLbrReceiveOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 4, 1, 2), Unsigned32())
if mibBuilder.loadTexts: prvtCfmLbrReceiveOrder.setStatus('current')
prvtCfmLbrTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLbrTime.setStatus('current')
prvtCfmLbrMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 4, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLbrMacAddress.setStatus('current')
prvtCfmLbrBadMsdu = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 6, 4, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmLbrBadMsdu.setStatus('current')
prvtCfmProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7))
prvtCfmProfileTableNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 1), PrvtCfmIndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmProfileTableNextIndex.setStatus('current')
prvtCfmProfileTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2), )
if mibBuilder.loadTexts: prvtCfmProfileTable.setStatus('current')
prvtCfmProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1), ).setIndexNames((0, "PRVT-CFM-MIB", "prvtCfmProfileIndex"))
if mibBuilder.loadTexts: prvtCfmProfileEntry.setStatus('current')
prvtCfmProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: prvtCfmProfileIndex.setStatus('current')
prvtCfmProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileRowStatus.setStatus('current')
prvtCfmProfileDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileDescr.setStatus('current')
prvtCfmProfilePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfilePriority.setStatus('current')
prvtCfmProfileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileRate.setStatus('current')
prvtCfmProfileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1462))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileSize.setStatus('current')
prvtCfmProfileBucketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileBucketSize.setStatus('current')
prvtCfmProfile1wJitterError = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfile1wJitterError.setStatus('current')
prvtCfmProfile1wJitterWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfile1wJitterWarning.setStatus('current')
prvtCfmProfileJitterError = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileJitterError.setStatus('current')
prvtCfmProfileJitterErrorPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileJitterErrorPeriod.setStatus('current')
prvtCfmProfileJitterWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileJitterWarning.setStatus('current')
prvtCfmProfileJitterWarningPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileJitterWarningPeriod.setStatus('current')
prvtCfmProfileFrameLossError = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileFrameLossError.setStatus('current')
prvtCfmProfileFrameLossWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileFrameLossWarning.setStatus('current')
prvtCfmProfileLatencyError = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileLatencyError.setStatus('current')
prvtCfmProfileLatencyErrorPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileLatencyErrorPeriod.setStatus('current')
prvtCfmProfileLatencyWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileLatencyWarning.setStatus('current')
prvtCfmProfileLatencyWarningPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileLatencyWarningPeriod.setStatus('current')
prvtCfmProfileOneWayJitterEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 20), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileOneWayJitterEnabled.setStatus('current')
prvtCfmProfileTwoWayJitterEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 21), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileTwoWayJitterEnabled.setStatus('current')
prvtCfmProfileFramelossEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 22), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileFramelossEnabled.setStatus('current')
prvtCfmProfileLatencyEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 7, 2, 1, 23), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProfileLatencyEnabled.setStatus('current')
prvtCfmProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8))
prvtCfmProcessTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 1), )
if mibBuilder.loadTexts: prvtCfmProcessTable.setStatus('current')
prvtCfmProcessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 1, 1), ).setIndexNames((0, "PRVT-CFM-MIB", "prvtCfmProcessIndex"), (0, "PRVT-CFM-MIB", "prvtCfmMdName"), (0, "PRVT-CFM-MIB", "prvtCfmMaName"))
if mibBuilder.loadTexts: prvtCfmProcessEntry.setStatus('current')
prvtCfmProcessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: prvtCfmProcessIndex.setStatus('current')
prvtCfmProcessRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProcessRowStatus.setStatus('current')
prvtCfmProcessProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProcessProfileIndex.setStatus('current')
prvtCfmProcessName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmProcessName.setStatus('current')
prvtCfmProcessShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProcessShutdown.setStatus('current')
prvtCfmProcessRepeatInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 420))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProcessRepeatInterval.setStatus('current')
prvtCfmProcessPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cfm", 1), ("y1731", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmProcessPacketType.setStatus('current')
prvtCfmProcessUnreturnedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmProcessUnreturnedPkts.setStatus('current')
prvtCfmProcessResultTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 2), )
if mibBuilder.loadTexts: prvtCfmProcessResultTable.setStatus('current')
prvtCfmProcessResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 2, 1), ).setIndexNames((0, "PRVT-CFM-MIB", "prvtCfmMdName"), (0, "PRVT-CFM-MIB", "prvtCfmMaName"), (0, "PRVT-CFM-MIB", "prvtCfmProcessIndex"), (0, "PRVT-CFM-MIB", "prvtCfmMepDbRMepIdentifier"))
if mibBuilder.loadTexts: prvtCfmProcessResultEntry.setStatus('current')
prvtCfmProcessResultOneWayJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmProcessResultOneWayJitter.setStatus('current')
prvtCfmProcessResultTwoWayJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmProcessResultTwoWayJitter.setStatus('current')
prvtCfmProcessResultLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmProcessResultLatency.setStatus('current')
prvtCfmProcessResultFrameloss = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 8, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCfmProcessResultFrameloss.setStatus('current')
prvtCfmMaAisLckVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 9))
prvtCfmMaAisLckVlanTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 9, 1), )
if mibBuilder.loadTexts: prvtCfmMaAisLckVlanTable.setStatus('current')
prvtCfmMaAisLckVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 9, 1, 1), ).setIndexNames((0, "PRVT-CFM-MIB", "prvtCfmMdName"), (0, "PRVT-CFM-MIB", "prvtCfmMaName"), (0, "PRVT-CFM-MIB", "prvtCfmMaAisLckVlanId"))
if mibBuilder.loadTexts: prvtCfmMaAisLckVlanEntry.setStatus('current')
prvtCfmMaAisLckVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: prvtCfmMaAisLckVlanId.setStatus('current')
prvtCfmMaAisLckVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 1, 9, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtCfmMaAisLckVlanRowStatus.setStatus('current')
prvtCfm1wJitterThreshold = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 0, 1)).setObjects(("PRVT-CFM-MIB", "prvtCfmProcessResultOneWayJitter"), ("PRVT-CFM-MIB", "prvtCfmProfile1wJitterWarning"), ("PRVT-CFM-MIB", "prvtCfmProfile1wJitterError"))
if mibBuilder.loadTexts: prvtCfm1wJitterThreshold.setStatus('current')
prvtCfmJitterThreshold = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 0, 2)).setObjects(("PRVT-CFM-MIB", "prvtCfmProcessResultTwoWayJitter"), ("PRVT-CFM-MIB", "prvtCfmProfileJitterWarning"), ("PRVT-CFM-MIB", "prvtCfmProfileJitterWarningPeriod"), ("PRVT-CFM-MIB", "prvtCfmProfileJitterError"), ("PRVT-CFM-MIB", "prvtCfmProfileJitterErrorPeriod"))
if mibBuilder.loadTexts: prvtCfmJitterThreshold.setStatus('current')
prvtCfmFrameLossThreshold = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 0, 3)).setObjects(("PRVT-CFM-MIB", "prvtCfmProcessResultFrameloss"), ("PRVT-CFM-MIB", "prvtCfmProfileFrameLossWarning"), ("PRVT-CFM-MIB", "prvtCfmProfileFrameLossError"))
if mibBuilder.loadTexts: prvtCfmFrameLossThreshold.setStatus('current')
prvtCfmLatencyThreshold = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 0, 4)).setObjects(("PRVT-CFM-MIB", "prvtCfmProcessResultLatency"), ("PRVT-CFM-MIB", "prvtCfmProfileLatencyWarning"), ("PRVT-CFM-MIB", "prvtCfmProfileLatencyWarningPeriod"), ("PRVT-CFM-MIB", "prvtCfmProfileLatencyError"), ("PRVT-CFM-MIB", "prvtCfmProfileLatencyErrorPeriod"))
if mibBuilder.loadTexts: prvtCfmLatencyThreshold.setStatus('current')
prvtCfmUnexpectedPriority = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 0, 5)).setObjects(("PRVT-CFM-MIB", "prvtCfmMepDirection"), ("PRVT-CFM-MIB", "prvtCfmMepDbMacAddress"), ("PRVT-CFM-MIB", "prvtCfmMepInterfaceIndex"))
if mibBuilder.loadTexts: prvtCfmUnexpectedPriority.setStatus('current')
prvtCfmFaultAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 0, 6)).setObjects(("PRVT-CFM-MIB", "prvtCfmMepDirection"), ("PRVT-CFM-MIB", "prvtCfmMepHighestPrDefect"), ("PRVT-CFM-MIB", "prvtCfmMepInterfaceIndex"))
if mibBuilder.loadTexts: prvtCfmFaultAlarm.setStatus('current')
prvtCfmAisLckRecieved = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 0, 7)).setObjects(("PRVT-CFM-MIB", "prvtCfmMepAisCondition"))
if mibBuilder.loadTexts: prvtCfmAisLckRecieved.setStatus('current')
prvtCfmAisLckCleared = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 0, 8)).setObjects(("PRVT-CFM-MIB", "prvtCfmMepAisCondition"))
if mibBuilder.loadTexts: prvtCfmAisLckCleared.setStatus('current')
prvtCfmFaultAlarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 131, 0, 9)).setObjects(("PRVT-CFM-MIB", "prvtCfmMepDirection"), ("PRVT-CFM-MIB", "prvtCfmMepFngState"))
if mibBuilder.loadTexts: prvtCfmFaultAlarmCleared.setStatus('current')
mibBuilder.exportSymbols("PRVT-CFM-MIB", LldpChassisIdSubtype=LldpChassisIdSubtype, prvtCfmMaCcmInterval=prvtCfmMaCcmInterval, prvtCfmMepTransmitLtmTimeout=prvtCfmMepTransmitLtmTimeout, prvtCfmAisLckCleared=prvtCfmAisLckCleared, prvtCfmMdMhfCreation=prvtCfmMdMhfCreation, prvtCfmLtrTable=prvtCfmLtrTable, prvtCfmMepTransmitLbmInfinite=prvtCfmMepTransmitLbmInfinite, PrvtCfmMaintDomainNameOrNone=PrvtCfmMaintDomainNameOrNone, PrvtCfmRemoteMepState=PrvtCfmRemoteMepState, prvtCfmLtrNextEgressIdentifier=prvtCfmLtrNextEgressIdentifier, PrvtCfmFngState=PrvtCfmFngState, PrvtCfmEgressActionFieldValue=PrvtCfmEgressActionFieldValue, prvtCfmMepTransmitLbmDestMepId=prvtCfmMepTransmitLbmDestMepId, prvtCfmMepTransmitLtmTargetMepId=prvtCfmMepTransmitLtmTargetMepId, prvtCfmMepMacAddress=prvtCfmMepMacAddress, prvtCfmMaServiceId=prvtCfmMaServiceId, prvtCfmStackTable=prvtCfmStackTable, prvtCfmMepTransmitLtmResult=prvtCfmMepTransmitLtmResult, prvtCfmMepTransmitLbmCurrentStatus=prvtCfmMepTransmitLbmCurrentStatus, prvtCfmProfile1wJitterWarning=prvtCfmProfile1wJitterWarning, prvtCfmProcessRepeatInterval=prvtCfmProcessRepeatInterval, prvtCfmProcessPacketType=prvtCfmProcessPacketType, prvtCfmMepLckLifetime=prvtCfmMepLckLifetime, prvtCfmProcessResultOneWayJitter=prvtCfmProcessResultOneWayJitter, prvtCfmMepTransmitLbmDataTlv=prvtCfmMepTransmitLbmDataTlv, prvtCfmMepLckCondition=prvtCfmMepLckCondition, prvtCfmUpdateInterval=prvtCfmUpdateInterval, prvtCfmMepLbrInOutOfOrder=prvtCfmMepLbrInOutOfOrder, prvtCfmMepTransmitLbmSentPkts=prvtCfmMepTransmitLbmSentPkts, prvtCfmMepNextLbmTransId=prvtCfmMepNextLbmTransId, prvtCfmMaAisLckLevel=prvtCfmMaAisLckLevel, prvtCfmLtrIngressMac=prvtCfmLtrIngressMac, prvtCfmLtrEgressPortIdSubtype=prvtCfmLtrEgressPortIdSubtype, prvtCfmProcessResultEntry=prvtCfmProcessResultEntry, prvtCfmJitterThreshold=prvtCfmJitterThreshold, prvtCfmMepAisLifetime=prvtCfmMepAisLifetime, prvtCfmProfileLatencyErrorPeriod=prvtCfmProfileLatencyErrorPeriod, prvtCfmShutdown=prvtCfmShutdown, prvtCfmProfileSize=prvtCfmProfileSize, prvtCfmMepDbRMepIdentifier=prvtCfmMepDbRMepIdentifier, PrvtCfmIngressActionFieldValue=PrvtCfmIngressActionFieldValue, prvtCfmMdFormat=prvtCfmMdFormat, prvtCfmMdTable=prvtCfmMdTable, PrvtCfmIndexIntegerNextFree=PrvtCfmIndexIntegerNextFree, prvtCfmProfileTableNextIndex=prvtCfmProfileTableNextIndex, prvtCfmLtrTtl=prvtCfmLtrTtl, prvtCfmMepTransmitLtmTargetMacAddress=prvtCfmMepTransmitLtmTargetMacAddress, prvtCfmMepTransmitLtmTargetIsMepId=prvtCfmMepTransmitLtmTargetIsMepId, prvtCfmLbrEntry=prvtCfmLbrEntry, prvtCfmStack=prvtCfmStack, prvtCfmStackServiceIdOrNone=prvtCfmStackServiceIdOrNone, prvtCfmMaTable=prvtCfmMaTable, prvtCfmProfilePriority=prvtCfmProfilePriority, prvtCfmProfileBucketSize=prvtCfmProfileBucketSize, prvtCfmMepDefects=prvtCfmMepDefects, prvtCfmLbrTable=prvtCfmLbrTable, prvtCfmProcessEntry=prvtCfmProcessEntry, prvtCfmMepTransmitMcastLbm=prvtCfmMepTransmitMcastLbm, prvtCfmMepTransmitLbmTimeout=prvtCfmMepTransmitLbmTimeout, prvtCfmMepTransmitLbmResultOK=prvtCfmMepTransmitLbmResultOK, prvtCfmMepXconCcmLastFailure=prvtCfmMepXconCcmLastFailure, prvtCfmMepTransmitLtmSeqNumber=prvtCfmMepTransmitLtmSeqNumber, prvtCfmProcessShutdown=prvtCfmProcessShutdown, prvtCfmMepDbRMepState=prvtCfmMepDbRMepState, prvtCfmMaAisLckInterval=prvtCfmMaAisLckInterval, prvtCfmProfileFramelossEnabled=prvtCfmProfileFramelossEnabled, prvtCfmMepFngState=prvtCfmMepFngState, prvtCfmMepTransmitLbmMinTime=prvtCfmMepTransmitLbmMinTime, prvtCfmMepCciEnabled=prvtCfmMepCciEnabled, prvtCfmLtrEgressMac=prvtCfmLtrEgressMac, prvtCfmMepLbrIn=prvtCfmMepLbrIn, prvtCfmProcessIndex=prvtCfmProcessIndex, prvtCfmProfileFrameLossWarning=prvtCfmProfileFrameLossWarning, prvtCfmMaAisLckVlanId=prvtCfmMaAisLckVlanId, prvtCfmMepTransmitLbmMaxTime=prvtCfmMepTransmitLbmMaxTime, PYSNMP_MODULE_ID=prvtCfmMIB, prvtCfmStackInterfaceIndex=prvtCfmStackInterfaceIndex, prvtCfmMepDbPortStatusTlv=prvtCfmMepDbPortStatusTlv, prvtCfmLtrChassisIdSubtype=prvtCfmLtrChassisIdSubtype, prvtCfmLtrIngressPortId=prvtCfmLtrIngressPortId, prvtCfmLtrOrganizationSpecificTlv=prvtCfmLtrOrganizationSpecificTlv, prvtCfmMaAisLckPriority=prvtCfmMaAisLckPriority, prvtCfmProfileEntry=prvtCfmProfileEntry, prvtCfmAisLckRecieved=prvtCfmAisLckRecieved, prvtCfmProfileRate=prvtCfmProfileRate, prvtCfmProcessTable=prvtCfmProcessTable, prvtCfmMaAisLckVlanEntry=prvtCfmMaAisLckVlanEntry, prvtCfmMepDbChassisIdSubtype=prvtCfmMepDbChassisIdSubtype, prvtCfmMaMhfCreation=prvtCfmMaMhfCreation, prvtCfmMaEntry=prvtCfmMaEntry, PrvtCfmIdPermissionDef=PrvtCfmIdPermissionDef, prvtCfmMaAisLckReceive=prvtCfmMaAisLckReceive, prvtCfmMepTransmitLbmDelay=prvtCfmMepTransmitLbmDelay, prvtCfmLtrLastEgressIdentifier=prvtCfmLtrLastEgressIdentifier, PrvtCfmInterfaceStatus=PrvtCfmInterfaceStatus, prvtCfmMdEntry=prvtCfmMdEntry, prvtCfmMaVlanId=prvtCfmMaVlanId, prvtCfmMepTransmitLbmRemainingMessages=prvtCfmMepTransmitLbmRemainingMessages, prvtCfmMepCcmLtmPriority=prvtCfmMepCcmLtmPriority, prvtCfmMepTransmitLbmStatus=prvtCfmMepTransmitLbmStatus, prvtCfmMepDbManAddress=prvtCfmMepDbManAddress, prvtCfmMaPermission=prvtCfmMaPermission, prvtCfmMepTransmitLbmMessages=prvtCfmMepTransmitLbmMessages, PrvtCfmRelayActionFieldValue=PrvtCfmRelayActionFieldValue, prvtCfmLtrEgressPortId=prvtCfmLtrEgressPortId, prvtCfmMepTransmitLbmVlanDropEnable=prvtCfmMepTransmitLbmVlanDropEnable, PrvtCfmMaintDomainName=PrvtCfmMaintDomainName, prvtCfmProfileTwoWayJitterEnabled=prvtCfmProfileTwoWayJitterEnabled, prvtCfmLatencyThreshold=prvtCfmLatencyThreshold, prvtCfmMaAisLckVlanRowStatus=prvtCfmMaAisLckVlanRowStatus, prvtCfmLbrReceiveOrder=prvtCfmLbrReceiveOrder, LldpPortId=LldpPortId, prvtCfmProfile1wJitterError=prvtCfmProfile1wJitterError, prvtCfmMepDbChassisId=prvtCfmMepDbChassisId, prvtCfmProcess=prvtCfmProcess, PrvtCfmMpDirection=PrvtCfmMpDirection, prvtCfmMaAisLckVlan=prvtCfmMaAisLckVlan, prvtCfmLtrEntry=prvtCfmLtrEntry, prvtCfmMepDbRMepFailedOkTime=prvtCfmMepDbRMepFailedOkTime, prvtCfmMepTransmitLtmTtl=prvtCfmMepTransmitLtmTtl, prvtCfmStackEntry=prvtCfmStackEntry, prvtCfmLtrTerminalMep=prvtCfmLtrTerminalMep, prvtCfmProfileJitterWarningPeriod=prvtCfmProfileJitterWarningPeriod, prvtCfmProcessUnreturnedPkts=prvtCfmProcessUnreturnedPkts, prvtCfmMepFngAlarmTime=prvtCfmMepFngAlarmTime, prvtCfmMIBNotifications=prvtCfmMIBNotifications, prvtCfmMIB=prvtCfmMIB, prvtCfmMepTransmitLbmAvgTime=prvtCfmMepTransmitLbmAvgTime, prvtCfmLtrIngressPortIdSubtype=prvtCfmLtrIngressPortIdSubtype, prvtCfmProfileIndex=prvtCfmProfileIndex, prvtCfmLtrSourceMac=prvtCfmLtrSourceMac, prvtCfmLtrTime=prvtCfmLtrTime, prvtCfmMd=prvtCfmMd, prvtCfmProfileLatencyError=prvtCfmProfileLatencyError, prvtCfmMepCcmSequenceErrors=prvtCfmMepCcmSequenceErrors, prvtCfmMepDbManAddressDomain=prvtCfmMepDbManAddressDomain, prvtCfmMepAlarmSupressed=prvtCfmMepAlarmSupressed, PrvtCfmIdPermission=PrvtCfmIdPermission, prvtCfmMepDbInterfaceStatusTlv=prvtCfmMepDbInterfaceStatusTlv, prvtCfmMepTransmitLtmFlags=prvtCfmMepTransmitLtmFlags, PrvtCfmPortStatus=PrvtCfmPortStatus, prvtCfmStackMdName=prvtCfmStackMdName, prvtCfmMepRowStatus=prvtCfmMepRowStatus, prvtCfmLbrTime=prvtCfmLbrTime, prvtCfmProfileLatencyWarning=prvtCfmProfileLatencyWarning, PrvtCfmLowestAlarmPri=PrvtCfmLowestAlarmPri, prvtCfmMepDbTable=prvtCfmMepDbTable, prvtCfmMaClearConnectivity=prvtCfmMaClearConnectivity, prvtCfmStackMepId=prvtCfmStackMepId, prvtCfmLbrSeqNumber=prvtCfmLbrSeqNumber, prvtCfmMepTransmitLbmSuccessRate=prvtCfmMepTransmitLbmSuccessRate, prvtCfmProcessRowStatus=prvtCfmProcessRowStatus, prvtCfmMepShutdown=prvtCfmMepShutdown, prvtCfmLtrManAddress=prvtCfmLtrManAddress, PrvtCfmMepIdOrZero=PrvtCfmMepIdOrZero, prvtCfmMdLevel=prvtCfmMdLevel, prvtCfmMepTable=prvtCfmMepTable, prvtCfmMepTransmitLbmDestMacAddress=prvtCfmMepTransmitLbmDestMacAddress, prvtCfmProfileTable=prvtCfmProfileTable, prvtCfmProcessResultTable=prvtCfmProcessResultTable, prvtCfmMaFormat=prvtCfmMaFormat, prvtCfmMdMhfIdPermission=prvtCfmMdMhfIdPermission, prvtCfmLtrEgress=prvtCfmLtrEgress, PrvtCfmMhfCreation=PrvtCfmMhfCreation, prvtCfmProcessResultTwoWayJitter=prvtCfmProcessResultTwoWayJitter, prvtCfmMepTransmitLbmDestIsMepId=prvtCfmMepTransmitLbmDestIsMepId, prvtCfmLbrMacAddress=prvtCfmLbrMacAddress, prvtCfmMepDbRdi=prvtCfmMepDbRdi, prvtCfmMepDbMacAddress=prvtCfmMepDbMacAddress, prvtCfmMepHighestPrDefect=prvtCfmMepHighestPrDefect, PrvtCfmMepId=PrvtCfmMepId, prvtCfmLtrSeqNumber=prvtCfmLtrSeqNumber, prvtCfmMepFngResetTime=prvtCfmMepFngResetTime, prvtCfmLtrForwarded=prvtCfmLtrForwarded, prvtCfmMepInterfaceIndex=prvtCfmMepInterfaceIndex, prvtCfmMepLbrOut=prvtCfmMepLbrOut, prvtCfmStackMaName=prvtCfmStackMaName, PrvtCfmMaintDomainNameType=PrvtCfmMaintDomainNameType, prvtCfmMaName=prvtCfmMaName, prvtCfmMepLowPrDef=prvtCfmMepLowPrDef, prvtCfmProfileJitterError=prvtCfmProfileJitterError, prvtCfmMepLtmNextSeqNumber=prvtCfmMepLtmNextSeqNumber, PrvtCfmHighestDefectPri=PrvtCfmHighestDefectPri, prvtCfmStackDirection=prvtCfmStackDirection, LldpPortIdSubtype=LldpPortIdSubtype, prvtCfmMepEntry=prvtCfmMepEntry, prvtCfmLtrIngress=prvtCfmLtrIngress, prvtCfmProfileFrameLossError=prvtCfmProfileFrameLossError, prvtCfmProfileLatencyWarningPeriod=prvtCfmProfileLatencyWarningPeriod, prvtCfmProfileRowStatus=prvtCfmProfileRowStatus, prvtCfmProfileJitterWarning=prvtCfmProfileJitterWarning, prvtCfmLtrReceiveOrder=prvtCfmLtrReceiveOrder, prvtCfmMepTransmitLtmEgressIdentifier=prvtCfmMepTransmitLtmEgressIdentifier, prvtCfmFrameLossThreshold=prvtCfmFrameLossThreshold, prvtCfmProfileJitterErrorPeriod=prvtCfmProfileJitterErrorPeriod, prvtCfmLbrBadMsdu=prvtCfmLbrBadMsdu, prvtCfmFaultAlarm=prvtCfmFaultAlarm, prvtCfmProcessName=prvtCfmProcessName, prvtCfmMepTransmitLbmSeqNumber=prvtCfmMepTransmitLbmSeqNumber, prvtCfmMa=prvtCfmMa, PrvtCfmMhfCreationDef=PrvtCfmMhfCreationDef, PrvtCfmCcmInterval=PrvtCfmCcmInterval, prvtCfmFaultAlarmCleared=prvtCfmFaultAlarmCleared, prvtCfmProfileOneWayJitterEnabled=prvtCfmProfileOneWayJitterEnabled, PrvtCfmMaintAssocNameOrNone=PrvtCfmMaintAssocNameOrNone, prvtCfmMepLbrBadMsdu=prvtCfmMepLbrBadMsdu, prvtCfmMepUnexpLtrIn=prvtCfmMepUnexpLtrIn, prvtCfmMIBObjects=prvtCfmMIBObjects, prvtCfmMepCciSentCcms=prvtCfmMepCciSentCcms, prvtCfmMaRowStatus=prvtCfmMaRowStatus, prvtCfmMdName=prvtCfmMdName, PrvtCfmMaintAssocNameType=PrvtCfmMaintAssocNameType, prvtCfmProcessResultLatency=prvtCfmProcessResultLatency, LldpChassisId=LldpChassisId, prvtCfmLtrRelay=prvtCfmLtrRelay, prvtCfmMep=prvtCfmMep, prvtCfmMaAisLckVlanTable=prvtCfmMaAisLckVlanTable, prvtCfmStackMdLevel=prvtCfmStackMdLevel, prvtCfmMepDbEntry=prvtCfmMepDbEntry, prvtCfmLtrManAddressDomain=prvtCfmLtrManAddressDomain, PrvtCfmMDLevelTC=PrvtCfmMDLevelTC, prvtCfmProcessResultFrameloss=prvtCfmProcessResultFrameloss, prvtCfmProfileDescr=prvtCfmProfileDescr, prvtCfm1wJitterThreshold=prvtCfm1wJitterThreshold, PrvtCfmMaintAssocName=PrvtCfmMaintAssocName, prvtCfmProcessProfileIndex=prvtCfmProcessProfileIndex, prvtCfmMdRowStatus=prvtCfmMdRowStatus, prvtCfmProfile=prvtCfmProfile, prvtCfmProfileLatencyEnabled=prvtCfmProfileLatencyEnabled, prvtCfmMepTransmitLtmStatus=prvtCfmMepTransmitLtmStatus, prvtCfmMepAisCondition=prvtCfmMepAisCondition, prvtCfmStackMacAddress=prvtCfmStackMacAddress, prvtCfmMepErrorCcmLastFailure=prvtCfmMepErrorCcmLastFailure, prvtCfmMepIdentifier=prvtCfmMepIdentifier, prvtCfmUnexpectedPriority=prvtCfmUnexpectedPriority, prvtCfmLtrChassisId=prvtCfmLtrChassisId, prvtCfmMepDirection=prvtCfmMepDirection, prvtCfmMepTransmitLbmVlanPriority=prvtCfmMepTransmitLbmVlanPriority)
