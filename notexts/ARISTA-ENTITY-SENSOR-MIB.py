#
# PySNMP MIB module ARISTA-ENTITY-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-ENTITY-SENSOR-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 09:10:02 2023
# On host fv-az247-870 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
entPhysicalIndex, entPhysicalDescr = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalDescr")
EntitySensorValue, entPhySensorValue = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue", "entPhySensorValue")
entStateAlarm, = mibBuilder.importSymbols("ENTITY-STATE-MIB", "entStateAlarm")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, ObjectIdentity, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, iso, Bits, Integer32, Counter64, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "iso", "Bits", "Integer32", "Counter64", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaEntSensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 12))
aristaEntSensorMIB.setRevisions(('2014-08-15 00:00', '2013-05-09 09:50',))
if mibBuilder.loadTexts: aristaEntSensorMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaEntSensorMIB.setOrganization('Arista Networks, Inc.')
aristaEntSensorMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 12, 0))
aristaEntSensorMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 12, 1))
aristaEntSensorMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 12, 2))
aristaEntSensorThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1), )
if mibBuilder.loadTexts: aristaEntSensorThresholdTable.setStatus('current')
aristaEntSensorThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aristaEntSensorThresholdEntry.setStatus('current')
aristaEntSensorThresholdLowWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1, 1), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEntSensorThresholdLowWarning.setStatus('current')
aristaEntSensorThresholdLowCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1, 2), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEntSensorThresholdLowCritical.setStatus('current')
aristaEntSensorThresholdHighWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1, 3), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEntSensorThresholdHighWarning.setStatus('current')
aristaEntSensorThresholdHighCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1, 4), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEntSensorThresholdHighCritical.setStatus('current')
aristaEntSensorStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 12, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaEntSensorStatusDescr.setStatus('current')
aristaEntSensorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 12, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("ENTITY-STATE-MIB", "entStateAlarm"))
if mibBuilder.loadTexts: aristaEntSensorAlarm.setStatus('current')
aristaEntSensorMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 12, 2, 1))
aristaEntSensorMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 12, 2, 2))
aristaEntSensorMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 12, 2, 1, 1)).setObjects(("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorThresholdGroup"), ("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaEntSensorMibCompliance = aristaEntSensorMibCompliance.setStatus('current')
aristaEntSensorThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 12, 2, 2, 1)).setObjects(("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorThresholdLowWarning"), ("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorThresholdLowCritical"), ("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorThresholdHighWarning"), ("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorThresholdHighCritical"), ("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorStatusDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaEntSensorThresholdGroup = aristaEntSensorThresholdGroup.setStatus('current')
aristaEntSensorNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 12, 2, 2, 2)).setObjects(("ARISTA-ENTITY-SENSOR-MIB", "aristaEntSensorAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaEntSensorNotificationsGroup = aristaEntSensorNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-ENTITY-SENSOR-MIB", aristaEntSensorThresholdEntry=aristaEntSensorThresholdEntry, aristaEntSensorMibObjects=aristaEntSensorMibObjects, aristaEntSensorThresholdTable=aristaEntSensorThresholdTable, aristaEntSensorThresholdGroup=aristaEntSensorThresholdGroup, aristaEntSensorThresholdHighCritical=aristaEntSensorThresholdHighCritical, aristaEntSensorNotificationsGroup=aristaEntSensorNotificationsGroup, aristaEntSensorStatusDescr=aristaEntSensorStatusDescr, aristaEntSensorAlarm=aristaEntSensorAlarm, aristaEntSensorMibCompliance=aristaEntSensorMibCompliance, PYSNMP_MODULE_ID=aristaEntSensorMIB, aristaEntSensorThresholdHighWarning=aristaEntSensorThresholdHighWarning, aristaEntSensorMibGroups=aristaEntSensorMibGroups, aristaEntSensorThresholdLowCritical=aristaEntSensorThresholdLowCritical, aristaEntSensorMibCompliances=aristaEntSensorMibCompliances, aristaEntSensorMibNotifications=aristaEntSensorMibNotifications, aristaEntSensorMIB=aristaEntSensorMIB, aristaEntSensorThresholdLowWarning=aristaEntSensorThresholdLowWarning, aristaEntSensorMibConformance=aristaEntSensorMibConformance)
