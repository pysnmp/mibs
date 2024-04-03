#
# PySNMP MIB module ARISTA-ENTITY-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-ENTITY-SENSOR-MIB
# Produced by pysmi-1.1.11 at Wed Apr  3 13:41:33 2024
# On host fv-az1499-203 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
entPhysicalDescr, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalDescr", "entPhysicalIndex")
entPhySensorValue, EntitySensorValue = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "entPhySensorValue", "EntitySensorValue")
entStateAlarm, = mibBuilder.importSymbols("ENTITY-STATE-MIB", "entStateAlarm")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Integer32, Gauge32, IpAddress, Bits, Counter32, MibIdentifier, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Integer32", "Gauge32", "IpAddress", "Bits", "Counter32", "MibIdentifier", "TimeTicks", "Unsigned32")
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
mibBuilder.exportSymbols("ARISTA-ENTITY-SENSOR-MIB", aristaEntSensorStatusDescr=aristaEntSensorStatusDescr, aristaEntSensorThresholdGroup=aristaEntSensorThresholdGroup, aristaEntSensorMibNotifications=aristaEntSensorMibNotifications, aristaEntSensorMIB=aristaEntSensorMIB, aristaEntSensorMibObjects=aristaEntSensorMibObjects, aristaEntSensorThresholdTable=aristaEntSensorThresholdTable, aristaEntSensorMibConformance=aristaEntSensorMibConformance, aristaEntSensorThresholdEntry=aristaEntSensorThresholdEntry, aristaEntSensorThresholdLowWarning=aristaEntSensorThresholdLowWarning, aristaEntSensorThresholdHighCritical=aristaEntSensorThresholdHighCritical, aristaEntSensorMibCompliances=aristaEntSensorMibCompliances, aristaEntSensorNotificationsGroup=aristaEntSensorNotificationsGroup, aristaEntSensorThresholdHighWarning=aristaEntSensorThresholdHighWarning, aristaEntSensorMibCompliance=aristaEntSensorMibCompliance, aristaEntSensorMibGroups=aristaEntSensorMibGroups, aristaEntSensorThresholdLowCritical=aristaEntSensorThresholdLowCritical, PYSNMP_MODULE_ID=aristaEntSensorMIB, aristaEntSensorAlarm=aristaEntSensorAlarm)
