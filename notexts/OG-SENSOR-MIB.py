#
# PySNMP MIB module OG-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-SENSOR-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 17:01:40 2021
# On host fv-az135-491 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, TimeTicks, ModuleIdentity, Bits, IpAddress, Counter64, NotificationType, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Bits", "IpAddress", "Counter64", "NotificationType", "iso", "Unsigned32")
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
mibBuilder.exportSymbols("OG-SENSOR-MIB", ogsensStatusTable=ogsensStatusTable, ogsensEventOccurred=ogsensEventOccurred, ogSensorMibGroup=ogSensorMibGroup, PYSNMP_MODULE_ID=ogSensorMib, ogSensorMibCompliance=ogSensorMibCompliance, ogSensorMibCompliances=ogSensorMibCompliances, ogSensorMibConformance=ogSensorMibConformance, ogsensStatusDevType=ogsensStatusDevType, ogsensMibNotifications=ogsensMibNotifications, ogSensorMibGroups=ogSensorMibGroups, ogsensStatusEntry=ogsensStatusEntry, ogSensorMibObjects=ogSensorMibObjects, ogsensStatusName=ogsensStatusName, ogsensNotificationsGroup=ogsensNotificationsGroup, ogsensStatusType=ogsensStatusType, ogSensorMibNotificationPrefix=ogSensorMibNotificationPrefix, ogSensorMib=ogSensorMib, ogsensStatus=ogsensStatus, ogsensStatusIndex=ogsensStatusIndex, ogsensStatusValue=ogsensStatusValue)
