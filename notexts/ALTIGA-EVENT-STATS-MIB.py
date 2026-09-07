#
# PySNMP MIB module ALTIGA-EVENT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ALTIGA-EVENT-STATS-MIB
# Source digest sha256:3887d99a4d563a68af1f5ed62866b278d0f03fe3bc0410aa62643ed2a4e8a40c
# Produced by pysmi-2.3.0
#
alEventMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alEventMibModule")
alEventGroup, alStatsEvent = mibBuilder.importSymbols("ALTIGA-MIB", "alEventGroup", "alStatsEvent")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaEventStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2))
altigaEventStatsMibModule.setRevisions(('2003-01-13 00:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaEventStatsMibModule.setLastUpdated('2003-01-13 00:00')
if mibBuilder.loadTexts: altigaEventStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsEventGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1))
alStatsEventNotificationId = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alStatsEventNotificationId.setStatus('current')
alEventStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alEventStatsTable.setStatus('current')
alEventStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), (0, "ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"))
if mibBuilder.loadTexts: alEventStatsEntry.setStatus('current')
alEventStatsClass = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsClass.setStatus('current')
alEventStatsEventNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsEventNumber.setStatus('current')
alEventStatsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 4, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alEventStatsCount.setStatus('current')
altigaEventStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1))
altigaEventStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1))
altigaEventStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 1)).setObjects(("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsMibCompliance = altigaEventStatsMibCompliance.setStatus('deprecated')
altigaEventStatsMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 8, 2, 1, 1, 2)).setObjects(("ALTIGA-EVENT-STATS-MIB", "altigaEventStatsGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsMibComplianceRev1 = altigaEventStatsMibComplianceRev1.setStatus('current')
altigaEventStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 2)).setObjects(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsGroup = altigaEventStatsGroup.setStatus('deprecated')
altigaEventStatsGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 4, 3)).setObjects(("ALTIGA-EVENT-STATS-MIB", "alEventStatsClass"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsEventNumber"), ("ALTIGA-EVENT-STATS-MIB", "alEventStatsCount"), ("ALTIGA-EVENT-STATS-MIB", "alStatsEventNotificationId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaEventStatsGroupRev1 = altigaEventStatsGroupRev1.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-EVENT-STATS-MIB", PYSNMP_MODULE_ID=altigaEventStatsMibModule, alEventStatsClass=alEventStatsClass, alEventStatsCount=alEventStatsCount, alEventStatsEntry=alEventStatsEntry, alEventStatsEventNumber=alEventStatsEventNumber, alEventStatsTable=alEventStatsTable, alStatsEventGlobal=alStatsEventGlobal, alStatsEventNotificationId=alStatsEventNotificationId, altigaEventStatsGroup=altigaEventStatsGroup, altigaEventStatsGroupRev1=altigaEventStatsGroupRev1, altigaEventStatsMibCompliance=altigaEventStatsMibCompliance, altigaEventStatsMibComplianceRev1=altigaEventStatsMibComplianceRev1, altigaEventStatsMibCompliances=altigaEventStatsMibCompliances, altigaEventStatsMibConformance=altigaEventStatsMibConformance, altigaEventStatsMibModule=altigaEventStatsMibModule)
