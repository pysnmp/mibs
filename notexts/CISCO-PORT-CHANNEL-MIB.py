#
# PySNMP MIB module CISCO-PORT-CHANNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PORT-CHANNEL-MIB
# Source digest sha256:0157c41ddfdfdcdab667534272e68a7cfa7cbf4ceb67337f60e639387fab7ccf
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
PortMemberList, = mibBuilder.importSymbols("CISCO-ST-TC", "PortMemberList")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TimeStamp", "TruthValue")
ciscoPortChannelMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 285))
ciscoPortChannelMIB.setRevisions(('2017-02-28 00:00', '2004-09-13 00:00', '2004-06-08 00:00', '2004-03-11 00:00', '2003-05-28 00:00', '2002-10-02 00:00',))
if mibBuilder.loadTexts: ciscoPortChannelMIB.setLastUpdated('2017-02-28 00:00')
if mibBuilder.loadTexts: ciscoPortChannelMIB.setOrganization('Cisco Systems Inc.')
ciscoPortChannelObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 285, 1))
portChannelMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 285, 2))
portChannelConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1))
portChannelStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 2))
portChannelNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 3))
portChannelNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 3, 0))
class PortChannelMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("auto", 1), ("on", 2), ("off", 3), ("desirable", 4))

class PortChannelGroupMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("active", 2))

portChannelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: portChannelTable.setStatus('current')
portChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-PORT-CHANNEL-MIB", "portChannelIndex"))
if mibBuilder.loadTexts: portChannelEntry.setStatus('current')
portChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: portChannelIndex.setStatus('current')
portChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portChannelIfIndex.setStatus('current')
portChannelAdminChannelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 3), PortChannelMode().clone('on')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: portChannelAdminChannelMode.setStatus('current')
portChannelOperChannelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 4), PortChannelMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portChannelOperChannelMode.setStatus('current')
portChannelAddType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("force", 2))).clone('normal')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: portChannelAddType.setStatus('current')
portChannelLastActionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("successful", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portChannelLastActionStatus.setStatus('current')
portChannelLastActionStatusCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portChannelLastActionStatusCause.setStatus('current')
portChannelLastActionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portChannelLastActionTime.setStatus('current')
portChannelMemberList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 9), PortMemberList().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: portChannelMemberList.setStatus('current')
portChannelCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portChannelCreationTime.setStatus('current')
portChannelRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: portChannelRowStatus.setStatus('current')
portChannelMemberOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 1, 1, 12), PortMemberList().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: portChannelMemberOperStatus.setStatus('current')
portChannelProtocolEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portChannelProtocolEnable.setStatus('current')
portChannelGrpIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: portChannelGrpIfExtTable.setStatus('current')
portChannelGrpIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: portChannelGrpIfExtEntry.setStatus('current')
portChannelGrpIfAutoCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 3, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portChannelGrpIfAutoCreation.setStatus('current')
portChannelExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: portChannelExtTable.setStatus('current')
portChannelExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1), ).setMaxAccess("notaccessible")
portChannelEntry.registerAugmentions(("CISCO-PORT-CHANNEL-MIB", "portChannelExtEntry"))
portChannelExtEntry.setIndexNames(*portChannelEntry.getIndexNames())
if mibBuilder.loadTexts: portChannelExtEntry.setStatus('current')
portChannelExtChannelGrpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1, 1), PortChannelGroupMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portChannelExtChannelGrpMode.setStatus('current')
portChannelExtAutoCreated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portChannelExtAutoCreated.setStatus('current')
portChannelExtPersistent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portChannelExtPersistent.setStatus('current')
portChannelExtOperChannelGrpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1, 4), PortChannelGroupMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portChannelExtOperChannelGrpMode.setStatus('current')
portChannelExtFcipEnhanced = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 285, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portChannelExtFcipEnhanced.setStatus('current')
portChannelMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1))
portChannelMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 2))
portChannelMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1, 1)).setObjects(("CISCO-PORT-CHANNEL-MIB", "portChannelGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portChannelMIBCompliance = portChannelMIBCompliance.setStatus('deprecated')
portChannelMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1, 2)).setObjects(("CISCO-PORT-CHANNEL-MIB", "portChannelGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portChannelMIBCompliance1 = portChannelMIBCompliance1.setStatus('deprecated')
portChannelMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1, 3)).setObjects(("CISCO-PORT-CHANNEL-MIB", "portChannelGroup"), ("CISCO-PORT-CHANNEL-MIB", "portChannelGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portChannelMIBCompliance2 = portChannelMIBCompliance2.setStatus('deprecated')
portChannelMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1, 4)).setObjects(("CISCO-PORT-CHANNEL-MIB", "portChannelGroup"), ("CISCO-PORT-CHANNEL-MIB", "portChannelGroupRev1"), ("CISCO-PORT-CHANNEL-MIB", "portChannelProtocolGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portChannelMIBCompliance3 = portChannelMIBCompliance3.setStatus('deprecated')
portChannelMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 1, 5)).setObjects(("CISCO-PORT-CHANNEL-MIB", "portChannelGroup"), ("CISCO-PORT-CHANNEL-MIB", "portChannelGroupRev1"), ("CISCO-PORT-CHANNEL-MIB", "portChannelProtocolGroup"), ("CISCO-PORT-CHANNEL-MIB", "portChannelFcipGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portChannelMIBCompliance4 = portChannelMIBCompliance4.setStatus('current')
portChannelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 2, 1)).setObjects(("CISCO-PORT-CHANNEL-MIB", "portChannelIfIndex"), ("CISCO-PORT-CHANNEL-MIB", "portChannelAdminChannelMode"), ("CISCO-PORT-CHANNEL-MIB", "portChannelOperChannelMode"), ("CISCO-PORT-CHANNEL-MIB", "portChannelAddType"), ("CISCO-PORT-CHANNEL-MIB", "portChannelLastActionStatus"), ("CISCO-PORT-CHANNEL-MIB", "portChannelLastActionStatusCause"), ("CISCO-PORT-CHANNEL-MIB", "portChannelLastActionTime"), ("CISCO-PORT-CHANNEL-MIB", "portChannelMemberList"), ("CISCO-PORT-CHANNEL-MIB", "portChannelCreationTime"), ("CISCO-PORT-CHANNEL-MIB", "portChannelRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portChannelGroup = portChannelGroup.setStatus('current')
portChannelGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 2, 2)).setObjects(("CISCO-PORT-CHANNEL-MIB", "portChannelMemberOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portChannelGroupRev1 = portChannelGroupRev1.setStatus('current')
portChannelProtocolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 2, 3)).setObjects(("CISCO-PORT-CHANNEL-MIB", "portChannelProtocolEnable"), ("CISCO-PORT-CHANNEL-MIB", "portChannelGrpIfAutoCreation"), ("CISCO-PORT-CHANNEL-MIB", "portChannelExtChannelGrpMode"), ("CISCO-PORT-CHANNEL-MIB", "portChannelExtAutoCreated"), ("CISCO-PORT-CHANNEL-MIB", "portChannelExtPersistent"), ("CISCO-PORT-CHANNEL-MIB", "portChannelExtOperChannelGrpMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portChannelProtocolGroup = portChannelProtocolGroup.setStatus('current')
portChannelFcipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 285, 2, 2, 4)).setObjects(("CISCO-PORT-CHANNEL-MIB", "portChannelExtFcipEnhanced"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portChannelFcipGroup = portChannelFcipGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PORT-CHANNEL-MIB", PYSNMP_MODULE_ID=ciscoPortChannelMIB, PortChannelGroupMode=PortChannelGroupMode, PortChannelMode=PortChannelMode, ciscoPortChannelMIB=ciscoPortChannelMIB, ciscoPortChannelObjects=ciscoPortChannelObjects, portChannelAddType=portChannelAddType, portChannelAdminChannelMode=portChannelAdminChannelMode, portChannelConfig=portChannelConfig, portChannelCreationTime=portChannelCreationTime, portChannelEntry=portChannelEntry, portChannelExtAutoCreated=portChannelExtAutoCreated, portChannelExtChannelGrpMode=portChannelExtChannelGrpMode, portChannelExtEntry=portChannelExtEntry, portChannelExtFcipEnhanced=portChannelExtFcipEnhanced, portChannelExtOperChannelGrpMode=portChannelExtOperChannelGrpMode, portChannelExtPersistent=portChannelExtPersistent, portChannelExtTable=portChannelExtTable, portChannelFcipGroup=portChannelFcipGroup, portChannelGroup=portChannelGroup, portChannelGroupRev1=portChannelGroupRev1, portChannelGrpIfAutoCreation=portChannelGrpIfAutoCreation, portChannelGrpIfExtEntry=portChannelGrpIfExtEntry, portChannelGrpIfExtTable=portChannelGrpIfExtTable, portChannelIfIndex=portChannelIfIndex, portChannelIndex=portChannelIndex, portChannelLastActionStatus=portChannelLastActionStatus, portChannelLastActionStatusCause=portChannelLastActionStatusCause, portChannelLastActionTime=portChannelLastActionTime, portChannelMIBCompliance1=portChannelMIBCompliance1, portChannelMIBCompliance2=portChannelMIBCompliance2, portChannelMIBCompliance3=portChannelMIBCompliance3, portChannelMIBCompliance4=portChannelMIBCompliance4, portChannelMIBCompliance=portChannelMIBCompliance, portChannelMIBCompliances=portChannelMIBCompliances, portChannelMIBConformance=portChannelMIBConformance, portChannelMIBGroups=portChannelMIBGroups, portChannelMemberList=portChannelMemberList, portChannelMemberOperStatus=portChannelMemberOperStatus, portChannelNotification=portChannelNotification, portChannelNotifications=portChannelNotifications, portChannelOperChannelMode=portChannelOperChannelMode, portChannelProtocolEnable=portChannelProtocolEnable, portChannelProtocolGroup=portChannelProtocolGroup, portChannelRowStatus=portChannelRowStatus, portChannelStatistics=portChannelStatistics, portChannelTable=portChannelTable)
