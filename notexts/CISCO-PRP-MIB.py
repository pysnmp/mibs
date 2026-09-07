#
# PySNMP MIB module CISCO-PRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PRP-MIB
# Source digest sha256:b907178174e9d974929aac96dbb46173a69799b83b8de66433da36e3cae95a68
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 866))
ciscoPrpMIB.setRevisions(('2019-09-11 00:00',))
if mibBuilder.loadTexts: ciscoPrpMIB.setLastUpdated('2019-09-11 00:00')
if mibBuilder.loadTexts: ciscoPrpMIB.setOrganization('Cisco Systems, Inc.')
class PrpStatus(TextualConvention, Integer32):
    reference = 'Prp channel or LAN status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("stateUp", 1), ("stateDown", 2))

ciscoPrpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 0))
ciscoPrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 1))
ciscoPrpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2))
ciscoPrpChannelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoPrpChannelTable.setStatus('current')
ciscoPrpChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-PRP-MIB", "ciscoPrpChannelIndex"))
if mibBuilder.loadTexts: ciscoPrpChannelEntry.setStatus('current')
ciscoPrpChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 1), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoPrpChannelIndex.setStatus('current')
ciscoPrpChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelId.setStatus('current')
ciscoPrpChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelName.setStatus('current')
ciscoPrpChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 4), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelStatus.setStatus('current')
ciscoPrpChannelLanAStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 5), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelLanAStatus.setStatus('current')
ciscoPrpChannelLanBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 6), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelLanBStatus.setStatus('current')
ciscoPrpChannelStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelStatus"))
if mibBuilder.loadTexts: ciscoPrpChannelStateChange.setStatus('current')
ciscoPrpLanAStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 2)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanAStatus"))
if mibBuilder.loadTexts: ciscoPrpLanAStateChange.setStatus('current')
ciscoPrpLanBStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 3)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanBStatus"))
if mibBuilder.loadTexts: ciscoPrpLanBStateChange.setStatus('current')
ciscoPrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 1))
ciscoPrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2))
ciscoPrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 1, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpMIBMainObjectGroup"), ("CISCO-PRP-MIB", "ciscoPrpMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBCompliance = ciscoPrpMIBCompliance.setStatus('current')
ciscoPrpMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanAStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanBStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBMainObjectGroup = ciscoPrpMIBMainObjectGroup.setStatus('current')
ciscoPrpMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2, 2)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelStateChange"), ("CISCO-PRP-MIB", "ciscoPrpLanAStateChange"), ("CISCO-PRP-MIB", "ciscoPrpLanBStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBNotificationGroup = ciscoPrpMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PRP-MIB", PYSNMP_MODULE_ID=ciscoPrpMIB, PrpStatus=PrpStatus, ciscoPrpChannelEntry=ciscoPrpChannelEntry, ciscoPrpChannelId=ciscoPrpChannelId, ciscoPrpChannelIndex=ciscoPrpChannelIndex, ciscoPrpChannelLanAStatus=ciscoPrpChannelLanAStatus, ciscoPrpChannelLanBStatus=ciscoPrpChannelLanBStatus, ciscoPrpChannelName=ciscoPrpChannelName, ciscoPrpChannelStateChange=ciscoPrpChannelStateChange, ciscoPrpChannelStatus=ciscoPrpChannelStatus, ciscoPrpChannelTable=ciscoPrpChannelTable, ciscoPrpLanAStateChange=ciscoPrpLanAStateChange, ciscoPrpLanBStateChange=ciscoPrpLanBStateChange, ciscoPrpMIB=ciscoPrpMIB, ciscoPrpMIBCompliance=ciscoPrpMIBCompliance, ciscoPrpMIBCompliances=ciscoPrpMIBCompliances, ciscoPrpMIBConform=ciscoPrpMIBConform, ciscoPrpMIBGroups=ciscoPrpMIBGroups, ciscoPrpMIBMainObjectGroup=ciscoPrpMIBMainObjectGroup, ciscoPrpMIBNotificationGroup=ciscoPrpMIBNotificationGroup, ciscoPrpMIBNotifs=ciscoPrpMIBNotifs, ciscoPrpMIBObjects=ciscoPrpMIBObjects)
