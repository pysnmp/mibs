#
# PySNMP MIB module ARISTA-ENTITY-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-ENTITY-SENSOR-MIB
# Produced by pysmi-1.1.12 at Wed May 29 10:52:21 2024
# On host fv-az1200-312 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
entPhysicalDescr, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalDescr", "entPhysicalIndex")
entPhySensorValue, EntitySensorValue = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "entPhySensorValue", "EntitySensorValue")
entStateAlarm, = mibBuilder.importSymbols("ENTITY-STATE-MIB", "entStateAlarm")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Bits, TimeTicks, ModuleIdentity, Gauge32, IpAddress, Counter64, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Bits", "TimeTicks", "ModuleIdentity", "Gauge32", "IpAddress", "Counter64", "Integer32", "ObjectIdentity")
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
mibBuilder.exportSymbols("ARISTA-ENTITY-SENSOR-MIB", aristaEntSensorMIB=aristaEntSensorMIB, aristaEntSensorMibConformance=aristaEntSensorMibConformance, aristaEntSensorNotificationsGroup=aristaEntSensorNotificationsGroup, aristaEntSensorThresholdLowWarning=aristaEntSensorThresholdLowWarning, aristaEntSensorMibObjects=aristaEntSensorMibObjects, aristaEntSensorStatusDescr=aristaEntSensorStatusDescr, aristaEntSensorMibGroups=aristaEntSensorMibGroups, aristaEntSensorMibCompliance=aristaEntSensorMibCompliance, aristaEntSensorAlarm=aristaEntSensorAlarm, aristaEntSensorThresholdGroup=aristaEntSensorThresholdGroup, aristaEntSensorThresholdHighCritical=aristaEntSensorThresholdHighCritical, aristaEntSensorThresholdEntry=aristaEntSensorThresholdEntry, PYSNMP_MODULE_ID=aristaEntSensorMIB, aristaEntSensorThresholdLowCritical=aristaEntSensorThresholdLowCritical, aristaEntSensorMibNotifications=aristaEntSensorMibNotifications, aristaEntSensorThresholdTable=aristaEntSensorThresholdTable, aristaEntSensorThresholdHighWarning=aristaEntSensorThresholdHighWarning, aristaEntSensorMibCompliances=aristaEntSensorMibCompliances)
