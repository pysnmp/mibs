#
# PySNMP MIB module BEGEMOT-NETGRAPH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-NETGRAPH
# Produced by pysmi-1.1.8 at Thu Apr 27 09:30:31 2023
# On host fv-az590-874 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Gauge32, Counter32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, IpAddress, Unsigned32, ModuleIdentity, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Gauge32", "Counter32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "IpAddress", "Unsigned32", "ModuleIdentity", "Integer32", "iso")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BEGEMOT-NETGRAPH-MIB", begemotNgConfig=begemotNgConfig, begemotNgNodeEntry=begemotNgNodeEntry, begemotNgNodeStatus=begemotNgNodeStatus, NgNodeName=NgNodeName, begemotNgResBufSiz=begemotNgResBufSiz, begemotNgTypeTable=begemotNgTypeTable, begemotNgTypeEntry=begemotNgTypeEntry, begemotNgMsgReadErrs=begemotNgMsgReadErrs, begemotNgHookPeerType=begemotNgHookPeerType, begemotNgHookStatus=begemotNgHookStatus, begemotNgDataReadErrs=begemotNgDataReadErrs, NgNodeIdOrZero=NgNodeIdOrZero, begemotNgHookNodeId=begemotNgHookNodeId, NgNodeId=NgNodeId, NgHookName=NgHookName, NgTypeName=NgTypeName, begemotNgNodeType=begemotNgNodeType, begemotNgHookEntry=begemotNgHookEntry, begemotNgTypeName=begemotNgTypeName, begemotNgControlNodeName=begemotNgControlNodeName, begemotNgNoMems=begemotNgNoMems, begemotNgHookPeerNodeId=begemotNgHookPeerNodeId, begemotNgTooLargeMsgs=begemotNgTooLargeMsgs, PYSNMP_MODULE_ID=begemotNg, NgNodeNameOrEmpty=NgNodeNameOrEmpty, begemotNgHookTable=begemotNgHookTable, begemotNg=begemotNg, begemotNgHookPeerHook=begemotNgHookPeerHook, begemotNgStats=begemotNgStats, begemotNgNodeTable=begemotNgNodeTable, begemotNgObjects=begemotNgObjects, begemotNgNodeHooks=begemotNgNodeHooks, begemotNgTooLargeDatas=begemotNgTooLargeDatas, begemotNgNodeName=begemotNgNodeName, begemotNgHookHook=begemotNgHookHook, begemotNgTimeout=begemotNgTimeout, begemotNgNodeId=begemotNgNodeId, begemotNgDebugLevel=begemotNgDebugLevel, begemotNgTypeStatus=begemotNgTypeStatus)
