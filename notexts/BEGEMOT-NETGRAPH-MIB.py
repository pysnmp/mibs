#
# PySNMP MIB module BEGEMOT-NETGRAPH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-NETGRAPH
# Produced by pysmi-1.1.8 at Sun Jan 16 00:42:42 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Bits, Counter64, ModuleIdentity, NotificationType, Counter32, Unsigned32, Gauge32, TimeTicks, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Bits", "Counter64", "ModuleIdentity", "NotificationType", "Counter32", "Unsigned32", "Gauge32", "TimeTicks", "MibIdentifier", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BEGEMOT-NETGRAPH-MIB", PYSNMP_MODULE_ID=begemotNg, begemotNgTypeTable=begemotNgTypeTable, begemotNgResBufSiz=begemotNgResBufSiz, begemotNgTypeStatus=begemotNgTypeStatus, begemotNgHookPeerType=begemotNgHookPeerType, begemotNgHookNodeId=begemotNgHookNodeId, begemotNgHookEntry=begemotNgHookEntry, NgTypeName=NgTypeName, begemotNgNodeStatus=begemotNgNodeStatus, begemotNgNodeEntry=begemotNgNodeEntry, NgNodeName=NgNodeName, begemotNgObjects=begemotNgObjects, begemotNgMsgReadErrs=begemotNgMsgReadErrs, begemotNgNodeHooks=begemotNgNodeHooks, begemotNgHookHook=begemotNgHookHook, NgNodeId=NgNodeId, NgNodeIdOrZero=NgNodeIdOrZero, begemotNgHookTable=begemotNgHookTable, NgNodeNameOrEmpty=NgNodeNameOrEmpty, begemotNgTooLargeDatas=begemotNgTooLargeDatas, begemotNgNoMems=begemotNgNoMems, begemotNgControlNodeName=begemotNgControlNodeName, begemotNgTypeName=begemotNgTypeName, begemotNgTooLargeMsgs=begemotNgTooLargeMsgs, begemotNgNodeName=begemotNgNodeName, begemotNgNodeId=begemotNgNodeId, begemotNgTimeout=begemotNgTimeout, begemotNgDebugLevel=begemotNgDebugLevel, begemotNgConfig=begemotNgConfig, begemotNgDataReadErrs=begemotNgDataReadErrs, begemotNgHookPeerNodeId=begemotNgHookPeerNodeId, begemotNgNodeType=begemotNgNodeType, begemotNg=begemotNg, begemotNgTypeEntry=begemotNgTypeEntry, begemotNgNodeTable=begemotNgNodeTable, begemotNgHookPeerHook=begemotNgHookPeerHook, begemotNgStats=begemotNgStats, begemotNgHookStatus=begemotNgHookStatus, NgHookName=NgHookName)
