#
# PySNMP MIB module ARISTA-ENTITY-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-ENTITY-SENSOR-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:49:51 2022
# On host fv-az42-349 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
entPhysicalDescr, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalDescr", "entPhysicalIndex")
entPhySensorValue, EntitySensorValue = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "entPhySensorValue", "EntitySensorValue")
entStateAlarm, = mibBuilder.importSymbols("ENTITY-STATE-MIB", "entStateAlarm")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Gauge32, Unsigned32, ObjectIdentity, Counter64, iso, MibIdentifier, Integer32, IpAddress, Counter32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Gauge32", "Unsigned32", "ObjectIdentity", "Counter64", "iso", "MibIdentifier", "Integer32", "IpAddress", "Counter32", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ARISTA-ENTITY-SENSOR-MIB", aristaEntSensorThresholdHighWarning=aristaEntSensorThresholdHighWarning, aristaEntSensorThresholdLowWarning=aristaEntSensorThresholdLowWarning, aristaEntSensorMibCompliance=aristaEntSensorMibCompliance, aristaEntSensorMibGroups=aristaEntSensorMibGroups, aristaEntSensorMibObjects=aristaEntSensorMibObjects, PYSNMP_MODULE_ID=aristaEntSensorMIB, aristaEntSensorThresholdLowCritical=aristaEntSensorThresholdLowCritical, aristaEntSensorMibNotifications=aristaEntSensorMibNotifications, aristaEntSensorAlarm=aristaEntSensorAlarm, aristaEntSensorMibConformance=aristaEntSensorMibConformance, aristaEntSensorThresholdHighCritical=aristaEntSensorThresholdHighCritical, aristaEntSensorMibCompliances=aristaEntSensorMibCompliances, aristaEntSensorThresholdTable=aristaEntSensorThresholdTable, aristaEntSensorStatusDescr=aristaEntSensorStatusDescr, aristaEntSensorThresholdGroup=aristaEntSensorThresholdGroup, aristaEntSensorNotificationsGroup=aristaEntSensorNotificationsGroup, aristaEntSensorThresholdEntry=aristaEntSensorThresholdEntry, aristaEntSensorMIB=aristaEntSensorMIB)
