#
# PySNMP MIB module CISCO-MEMORY-POOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MEMORY-POOL-MIB
# Source digest sha256:a3233f34e65991d75c907d4d0999e676bfd66792cafa35d7e2954022a17b81f7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
Percent, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "Percent")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoMemoryPoolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 48))
ciscoMemoryPoolMIB.setRevisions(('2013-09-18 00:00', '2001-07-31 00:00', '1996-02-01 00:00',))
if mibBuilder.loadTexts: ciscoMemoryPoolMIB.setLastUpdated('2013-09-18 00:00')
if mibBuilder.loadTexts: ciscoMemoryPoolMIB.setOrganization('Cisco Systems, Inc.')
class CiscoMemoryPoolTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

ciscoMemoryPoolObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 1))
ciscoMemoryPoolTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoMemoryPoolTable.setStatus('current')
ciscoMemoryPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolType"))
if mibBuilder.loadTexts: ciscoMemoryPoolEntry.setStatus('current')
ciscoMemoryPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 1), CiscoMemoryPoolTypes()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoMemoryPoolType.setStatus('current')
ciscoMemoryPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolName.setStatus('current')
ciscoMemoryPoolAlternate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolAlternate.setStatus('current')
ciscoMemoryPoolValid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolValid.setStatus('current')
ciscoMemoryPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 5), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolUsed.setStatus('current')
ciscoMemoryPoolFree = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 6), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolFree.setStatus('current')
ciscoMemoryPoolLargestFree = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 7), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolLargestFree.setStatus('current')
ciscoMemoryPoolLowMemoryNotifThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 1, 1, 8), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoMemoryPoolLowMemoryNotifThreshold.setStatus('current')
ciscoMemoryPoolUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoMemoryPoolUtilizationTable.setStatus('current')
ciscoMemoryPoolUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1), ).setMaxAccess("notaccessible")
ciscoMemoryPoolEntry.registerAugmentions(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilizationEntry"))
ciscoMemoryPoolUtilizationEntry.setIndexNames(*ciscoMemoryPoolEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoMemoryPoolUtilizationEntry.setStatus('current')
ciscoMemoryPoolUtilization1Min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1, 1), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolUtilization1Min.setStatus('current')
ciscoMemoryPoolUtilization5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1, 2), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolUtilization5Min.setStatus('current')
ciscoMemoryPoolUtilization10Min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 2, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMemoryPoolUtilization10Min.setStatus('current')
ciscoMemoryPoolLowMemoryNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 48, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoMemoryPoolLowMemoryNotifEnable.setStatus('current')
ciscoMemoryPoolNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 2))
ciscoMemoryPoolMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 2, 0))
ciscoMemoryPoolLowMemoryNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 48, 2, 0, 1)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"))
if mibBuilder.loadTexts: ciscoMemoryPoolLowMemoryNotif.setStatus('current')
ciscoMemoryPoolLowMemoryRecoveryNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 48, 2, 0, 2)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"))
if mibBuilder.loadTexts: ciscoMemoryPoolLowMemoryRecoveryNotif.setStatus('current')
ciscoMemoryPoolConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 3))
ciscoMemoryPoolCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1))
ciscoMemoryPoolGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2))
ciscoMemoryPoolCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1, 1)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCompliance = ciscoMemoryPoolCompliance.setStatus('deprecated')
ciscoMemoryPoolComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1, 2)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolGroup"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilizationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolComplianceRev1 = ciscoMemoryPoolComplianceRev1.setStatus('deprecated')
ciscoMemoryPoolComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 1, 3)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolGroupRev1"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilizationGroup"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolNotificationGroup"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolNotificationCtrlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolComplianceRev2 = ciscoMemoryPoolComplianceRev2.setStatus('current')
ciscoMemoryPoolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 1)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolAlternate"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolValid"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolFree"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLargestFree"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolGroup = ciscoMemoryPoolGroup.setStatus('deprecated')
ciscoMemoryPoolUtilizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 2)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilization1Min"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilization5Min"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUtilization10Min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolUtilizationGroup = ciscoMemoryPoolUtilizationGroup.setStatus('current')
ciscoMemoryPoolNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 3)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryNotif"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryRecoveryNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolNotificationGroup = ciscoMemoryPoolNotificationGroup.setStatus('current')
ciscoMemoryPoolNotificationCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 4)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolNotificationCtrlGroup = ciscoMemoryPoolNotificationCtrlGroup.setStatus('current')
ciscoMemoryPoolGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 48, 3, 2, 5)).setObjects(("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolName"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolAlternate"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolValid"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolUsed"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolFree"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLargestFree"), ("CISCO-MEMORY-POOL-MIB", "ciscoMemoryPoolLowMemoryNotifThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolGroupRev1 = ciscoMemoryPoolGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-MEMORY-POOL-MIB", CiscoMemoryPoolTypes=CiscoMemoryPoolTypes, PYSNMP_MODULE_ID=ciscoMemoryPoolMIB, ciscoMemoryPoolAlternate=ciscoMemoryPoolAlternate, ciscoMemoryPoolCompliance=ciscoMemoryPoolCompliance, ciscoMemoryPoolComplianceRev1=ciscoMemoryPoolComplianceRev1, ciscoMemoryPoolComplianceRev2=ciscoMemoryPoolComplianceRev2, ciscoMemoryPoolCompliances=ciscoMemoryPoolCompliances, ciscoMemoryPoolConformance=ciscoMemoryPoolConformance, ciscoMemoryPoolEntry=ciscoMemoryPoolEntry, ciscoMemoryPoolFree=ciscoMemoryPoolFree, ciscoMemoryPoolGroup=ciscoMemoryPoolGroup, ciscoMemoryPoolGroupRev1=ciscoMemoryPoolGroupRev1, ciscoMemoryPoolGroups=ciscoMemoryPoolGroups, ciscoMemoryPoolLargestFree=ciscoMemoryPoolLargestFree, ciscoMemoryPoolLowMemoryNotif=ciscoMemoryPoolLowMemoryNotif, ciscoMemoryPoolLowMemoryNotifEnable=ciscoMemoryPoolLowMemoryNotifEnable, ciscoMemoryPoolLowMemoryNotifThreshold=ciscoMemoryPoolLowMemoryNotifThreshold, ciscoMemoryPoolLowMemoryRecoveryNotif=ciscoMemoryPoolLowMemoryRecoveryNotif, ciscoMemoryPoolMIB=ciscoMemoryPoolMIB, ciscoMemoryPoolMIBNotificationPrefix=ciscoMemoryPoolMIBNotificationPrefix, ciscoMemoryPoolName=ciscoMemoryPoolName, ciscoMemoryPoolNotificationCtrlGroup=ciscoMemoryPoolNotificationCtrlGroup, ciscoMemoryPoolNotificationGroup=ciscoMemoryPoolNotificationGroup, ciscoMemoryPoolNotifications=ciscoMemoryPoolNotifications, ciscoMemoryPoolObjects=ciscoMemoryPoolObjects, ciscoMemoryPoolTable=ciscoMemoryPoolTable, ciscoMemoryPoolType=ciscoMemoryPoolType, ciscoMemoryPoolUsed=ciscoMemoryPoolUsed, ciscoMemoryPoolUtilization10Min=ciscoMemoryPoolUtilization10Min, ciscoMemoryPoolUtilization1Min=ciscoMemoryPoolUtilization1Min, ciscoMemoryPoolUtilization5Min=ciscoMemoryPoolUtilization5Min, ciscoMemoryPoolUtilizationEntry=ciscoMemoryPoolUtilizationEntry, ciscoMemoryPoolUtilizationGroup=ciscoMemoryPoolUtilizationGroup, ciscoMemoryPoolUtilizationTable=ciscoMemoryPoolUtilizationTable, ciscoMemoryPoolValid=ciscoMemoryPoolValid)
