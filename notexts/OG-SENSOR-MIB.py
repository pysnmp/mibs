#
# PySNMP MIB module OG-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-SENSOR-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 13:35:01 2024
# On host fv-az975-559 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Bits, Counter32, ModuleIdentity, Gauge32, TimeTicks, MibIdentifier, Unsigned32, Integer32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Counter32", "ModuleIdentity", "Gauge32", "TimeTicks", "MibIdentifier", "Unsigned32", "Integer32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogSensorMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 13))
ogSensorMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))
if mibBuilder.loadTexts: ogSensorMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogSensorMib.setOrganization('Opengear Inc.')
ogSensorMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10))
ogsensStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1))
ogsensStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3), )
if mibBuilder.loadTexts: ogsensStatusTable.setStatus('current')
ogsensStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1), ).setIndexNames((0, "OG-SENSOR-MIB", "ogsensStatusIndex"))
if mibBuilder.loadTexts: ogsensStatusEntry.setStatus('current')
ogsensStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogsensStatusIndex.setStatus('current')
ogsensStatusName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusName.setStatus('current')
ogsensStatusDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusDevType.setStatus('current')
ogsensStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusType.setStatus('current')
ogsensStatusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 13, 10, 1, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsensStatusValue.setStatus('current')
ogSensorMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 2))
ogsensMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 2, 0))
ogsensEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 13, 2, 0, 200)).setObjects(("OG-SENSOR-MIB", "ogsensStatusName"), ("OG-SENSOR-MIB", "ogsensStatusDevType"), ("OG-SENSOR-MIB", "ogsensStatusType"), ("OG-SENSOR-MIB", "ogsensStatusValue"))
if mibBuilder.loadTexts: ogsensEventOccurred.setStatus('current')
ogSensorMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3))
ogSensorMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 1))
ogSensorMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2))
ogSensorMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 1, 1)).setObjects(("OG-SENSOR-MIB", "ogSensorMibGroup"), ("OG-SENSOR-MIB", "ogsensNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogSensorMibCompliance = ogSensorMibCompliance.setStatus('current')
ogSensorMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2, 1)).setObjects(("OG-SENSOR-MIB", "ogsensStatusName"), ("OG-SENSOR-MIB", "ogsensStatusDevType"), ("OG-SENSOR-MIB", "ogsensStatusType"), ("OG-SENSOR-MIB", "ogsensStatusValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogSensorMibGroup = ogSensorMibGroup.setStatus('current')
ogsensNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 13, 3, 2, 2)).setObjects(("OG-SENSOR-MIB", "ogsensEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogsensNotificationsGroup = ogsensNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OG-SENSOR-MIB", ogsensStatusName=ogsensStatusName, ogSensorMibGroups=ogSensorMibGroups, ogsensStatusType=ogsensStatusType, ogsensEventOccurred=ogsensEventOccurred, ogSensorMibCompliance=ogSensorMibCompliance, ogSensorMibGroup=ogSensorMibGroup, ogsensMibNotifications=ogsensMibNotifications, ogsensStatusDevType=ogsensStatusDevType, ogsensStatus=ogsensStatus, ogsensStatusValue=ogsensStatusValue, ogsensStatusEntry=ogsensStatusEntry, ogSensorMibNotificationPrefix=ogSensorMibNotificationPrefix, ogsensStatusTable=ogsensStatusTable, ogSensorMibObjects=ogSensorMibObjects, ogSensorMib=ogSensorMib, ogSensorMibCompliances=ogSensorMibCompliances, ogsensStatusIndex=ogsensStatusIndex, PYSNMP_MODULE_ID=ogSensorMib, ogsensNotificationsGroup=ogsensNotificationsGroup, ogSensorMibConformance=ogSensorMibConformance)
