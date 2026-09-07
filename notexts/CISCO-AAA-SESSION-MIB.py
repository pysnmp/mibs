#
# PySNMP MIB module CISCO-AAA-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-AAA-SESSION-MIB
# Source digest sha256:5427826d0d706b06fa2f4fc225dfa7068d972f6535922e49fd2a565e1fed493d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowPointer, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "TextualConvention", "TruthValue")
ciscoAAASessionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 150))
ciscoAAASessionMIB.setRevisions(('2006-03-21 00:00', '2002-04-11 00:00', '1999-11-16 00:00',))
if mibBuilder.loadTexts: ciscoAAASessionMIB.setLastUpdated('2006-03-21 00:00')
if mibBuilder.loadTexts: ciscoAAASessionMIB.setOrganization('Cisco Systems, Inc.')
class CctCallId(TextualConvention, Unsigned32):
    status = 'current'

class CasnSessionId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

casnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1))
casnActive = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1))
casnGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2))
casnActiveTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnActiveTableEntries.setStatus('current')
casnActiveTableHighWaterMark = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnActiveTableHighWaterMark.setStatus('current')
casnActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: casnActiveTable.setStatus('current')
casnActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-AAA-SESSION-MIB", "casnSessionId"))
if mibBuilder.loadTexts: casnActiveEntry.setStatus('current')
casnSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 1), CasnSessionId()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: casnSessionId.setStatus('current')
casnUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnUserId.setStatus('current')
casnIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnIpAddr.setStatus('current')
casnIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 4), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: casnIdleTime.setStatus('current')
casnDisconnect = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: casnDisconnect.setStatus('current')
casnCallTrackerId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 6), CctCallId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnCallTrackerId.setStatus('current')
casnNasPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 7), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnNasPort.setStatus('current')
casnVaiIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 1, 3, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnVaiIfIndex.setStatus('current')
casnTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnTotalSessions.setStatus('current')
casnDisconnectedSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 150, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casnDisconnectedSessions.setStatus('current')
casnMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 2))
casnMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 2, 1))
casnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3))
casnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1))
casnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2))
casnMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1, 1)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveGroup"), ("CISCO-AAA-SESSION-MIB", "casnGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnMIBCompliance = casnMIBCompliance.setStatus('deprecated')
casnMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 1, 2)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveGroup"), ("CISCO-AAA-SESSION-MIB", "casnGeneralGroup"), ("CISCO-AAA-SESSION-MIB", "casnActiveGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnMIBComplianceRev1 = casnMIBComplianceRev1.setStatus('current')
casnActiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 1)).setObjects(("CISCO-AAA-SESSION-MIB", "casnActiveTableEntries"), ("CISCO-AAA-SESSION-MIB", "casnActiveTableHighWaterMark"), ("CISCO-AAA-SESSION-MIB", "casnUserId"), ("CISCO-AAA-SESSION-MIB", "casnIpAddr"), ("CISCO-AAA-SESSION-MIB", "casnIdleTime"), ("CISCO-AAA-SESSION-MIB", "casnDisconnect"), ("CISCO-AAA-SESSION-MIB", "casnCallTrackerId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnActiveGroup = casnActiveGroup.setStatus('current')
casnGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 2)).setObjects(("CISCO-AAA-SESSION-MIB", "casnTotalSessions"), ("CISCO-AAA-SESSION-MIB", "casnDisconnectedSessions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnGeneralGroup = casnGeneralGroup.setStatus('current')
casnActiveGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 150, 3, 2, 3)).setObjects(("CISCO-AAA-SESSION-MIB", "casnNasPort"), ("CISCO-AAA-SESSION-MIB", "casnVaiIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casnActiveGroupSup1 = casnActiveGroupSup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAA-SESSION-MIB", CasnSessionId=CasnSessionId, CctCallId=CctCallId, PYSNMP_MODULE_ID=ciscoAAASessionMIB, casnActive=casnActive, casnActiveEntry=casnActiveEntry, casnActiveGroup=casnActiveGroup, casnActiveGroupSup1=casnActiveGroupSup1, casnActiveTable=casnActiveTable, casnActiveTableEntries=casnActiveTableEntries, casnActiveTableHighWaterMark=casnActiveTableHighWaterMark, casnCallTrackerId=casnCallTrackerId, casnDisconnect=casnDisconnect, casnDisconnectedSessions=casnDisconnectedSessions, casnGeneral=casnGeneral, casnGeneralGroup=casnGeneralGroup, casnIdleTime=casnIdleTime, casnIpAddr=casnIpAddr, casnMIBCompliance=casnMIBCompliance, casnMIBComplianceRev1=casnMIBComplianceRev1, casnMIBCompliances=casnMIBCompliances, casnMIBConformance=casnMIBConformance, casnMIBGroups=casnMIBGroups, casnMIBNotificationPrefix=casnMIBNotificationPrefix, casnMIBNotifications=casnMIBNotifications, casnMIBObjects=casnMIBObjects, casnNasPort=casnNasPort, casnSessionId=casnSessionId, casnTotalSessions=casnTotalSessions, casnUserId=casnUserId, casnVaiIfIndex=casnVaiIfIndex, ciscoAAASessionMIB=ciscoAAASessionMIB)
