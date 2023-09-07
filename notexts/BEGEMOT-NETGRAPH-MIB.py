#
# PySNMP MIB module BEGEMOT-NETGRAPH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-NETGRAPH
# Produced by pysmi-1.1.8 at Thu Sep  7 13:32:50 2023
# On host fv-az422-951 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, ObjectIdentity, MibIdentifier, IpAddress, Unsigned32, iso, Bits, Integer32, TimeTicks, NotificationType, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "IpAddress", "Unsigned32", "iso", "Bits", "Integer32", "TimeTicks", "NotificationType", "Gauge32", "Counter32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
begemotNg = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 2))
if mibBuilder.loadTexts: begemotNg.setLastUpdated('200311140000Z')
if mibBuilder.loadTexts: begemotNg.setOrganization('Fraunhofer FOKUS, CATS')
begemotNgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1))
class NgTypeName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class NgNodeName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class NgNodeNameOrEmpty(TextualConvention, OctetString):
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class NgHookName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class NgNodeId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NgNodeIdOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

begemotNgConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1))
begemotNgControlNodeName = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 1), NgNodeName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgControlNodeName.setStatus('current')
begemotNgResBufSiz = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1024, 65536)).clone(20000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotNgResBufSiz.setStatus('current')
begemotNgTimeout = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 10000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotNgTimeout.setStatus('current')
begemotNgDebugLevel = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotNgDebugLevel.setStatus('current')
begemotNgStats = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2))
begemotNgNoMems = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgNoMems.setStatus('current')
begemotNgMsgReadErrs = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgMsgReadErrs.setStatus('current')
begemotNgTooLargeMsgs = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgTooLargeMsgs.setStatus('current')
begemotNgDataReadErrs = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgDataReadErrs.setStatus('current')
begemotNgTooLargeDatas = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgTooLargeDatas.setStatus('current')
begemotNgTypeTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3), )
if mibBuilder.loadTexts: begemotNgTypeTable.setStatus('current')
begemotNgTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3, 1), ).setIndexNames((0, "BEGEMOT-NETGRAPH-MIB", "begemotNgTypeName"))
if mibBuilder.loadTexts: begemotNgTypeEntry.setStatus('current')
begemotNgTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3, 1, 1), NgTypeName())
if mibBuilder.loadTexts: begemotNgTypeName.setStatus('current')
begemotNgTypeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loaded", 1), ("unloaded", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: begemotNgTypeStatus.setStatus('current')
begemotNgNodeTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4), )
if mibBuilder.loadTexts: begemotNgNodeTable.setStatus('current')
begemotNgNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1), ).setIndexNames((0, "BEGEMOT-NETGRAPH-MIB", "begemotNgNodeId"))
if mibBuilder.loadTexts: begemotNgNodeEntry.setStatus('current')
begemotNgNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 1), NgNodeId())
if mibBuilder.loadTexts: begemotNgNodeId.setStatus('current')
begemotNgNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgNodeStatus.setStatus('current')
begemotNgNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 3), NgNodeNameOrEmpty()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgNodeName.setStatus('current')
begemotNgNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 4), NgTypeName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgNodeType.setStatus('current')
begemotNgNodeHooks = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgNodeHooks.setStatus('current')
begemotNgHookTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5), )
if mibBuilder.loadTexts: begemotNgHookTable.setStatus('current')
begemotNgHookEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1), ).setIndexNames((0, "BEGEMOT-NETGRAPH-MIB", "begemotNgHookNodeId"), (0, "BEGEMOT-NETGRAPH-MIB", "begemotNgHookHook"))
if mibBuilder.loadTexts: begemotNgHookEntry.setStatus('current')
begemotNgHookNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 1), NgNodeId())
if mibBuilder.loadTexts: begemotNgHookNodeId.setStatus('current')
begemotNgHookHook = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 2), NgHookName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgHookHook.setStatus('current')
begemotNgHookStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgHookStatus.setStatus('current')
begemotNgHookPeerNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 4), NgNodeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgHookPeerNodeId.setStatus('current')
begemotNgHookPeerHook = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 5), NgHookName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgHookPeerHook.setStatus('current')
begemotNgHookPeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 2, 1, 5, 1, 6), NgTypeName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotNgHookPeerType.setStatus('current')
mibBuilder.exportSymbols("BEGEMOT-NETGRAPH-MIB", begemotNgHookStatus=begemotNgHookStatus, begemotNgStats=begemotNgStats, begemotNgTooLargeMsgs=begemotNgTooLargeMsgs, begemotNgTypeName=begemotNgTypeName, begemotNgObjects=begemotNgObjects, begemotNgControlNodeName=begemotNgControlNodeName, begemotNgDebugLevel=begemotNgDebugLevel, begemotNgNodeStatus=begemotNgNodeStatus, begemotNgHookPeerType=begemotNgHookPeerType, begemotNg=begemotNg, begemotNgNodeHooks=begemotNgNodeHooks, begemotNgNodeId=begemotNgNodeId, begemotNgDataReadErrs=begemotNgDataReadErrs, begemotNgTimeout=begemotNgTimeout, begemotNgResBufSiz=begemotNgResBufSiz, begemotNgHookHook=begemotNgHookHook, begemotNgNodeName=begemotNgNodeName, begemotNgHookPeerNodeId=begemotNgHookPeerNodeId, begemotNgNodeType=begemotNgNodeType, begemotNgNodeEntry=begemotNgNodeEntry, begemotNgNoMems=begemotNgNoMems, NgNodeName=NgNodeName, NgTypeName=NgTypeName, begemotNgNodeTable=begemotNgNodeTable, NgNodeId=NgNodeId, NgNodeNameOrEmpty=NgNodeNameOrEmpty, NgNodeIdOrZero=NgNodeIdOrZero, begemotNgTooLargeDatas=begemotNgTooLargeDatas, begemotNgConfig=begemotNgConfig, begemotNgHookNodeId=begemotNgHookNodeId, begemotNgMsgReadErrs=begemotNgMsgReadErrs, begemotNgHookEntry=begemotNgHookEntry, begemotNgHookPeerHook=begemotNgHookPeerHook, begemotNgTypeTable=begemotNgTypeTable, begemotNgTypeStatus=begemotNgTypeStatus, begemotNgTypeEntry=begemotNgTypeEntry, begemotNgHookTable=begemotNgHookTable, NgHookName=NgHookName, PYSNMP_MODULE_ID=begemotNg)
