#
# PySNMP MIB module RADLAN-SENSORENTMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SENSORENTMIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:07:00 2024
# On host fv-az1433-299 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
entityPhysicalGroup, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entityPhysicalGroup", "entPhysicalIndex")
EntitySensorValue, entPhySensorEntry = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue", "entPhySensorEntry")
rlEnv, = mibBuilder.importSymbols("RADLAN-HWENVIROMENT", "rlEnv")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, Unsigned32, mib_2, Integer32, ObjectIdentity, iso, TimeTicks, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Unsigned32", "mib-2", "Integer32", "ObjectIdentity", "iso", "TimeTicks", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Bits", "IpAddress")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
rlSensor = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 83, 4))
rlSensor.setRevisions(('2003-09-21 00:00',))
if mibBuilder.loadTexts: rlSensor.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlSensor.setOrganization('Radlan Computer Communications Ltd.')
rlEntPhySensorTable = MibTable((1, 3, 6, 1, 4, 1, 89, 83, 3), )
if mibBuilder.loadTexts: rlEntPhySensorTable.setStatus('current')
rlEntPhySensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 83, 3, 1), )
entPhySensorEntry.registerAugmentions(("RADLAN-SENSORENTMIB", "rlEntPhySensorEntry"))
rlEntPhySensorEntry.setIndexNames(*entPhySensorEntry.getIndexNames())
if mibBuilder.loadTexts: rlEntPhySensorEntry.setStatus('current')
rlEnvPhySensorMinValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 1), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvPhySensorMinValue.setStatus('current')
rlEnvPhySensorMaxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 2), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvPhySensorMaxValue.setStatus('current')
rlEnvPhySensorTestValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 3), EntitySensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEnvPhySensorTestValue.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SENSORENTMIB", rlEnvPhySensorMinValue=rlEnvPhySensorMinValue, rlEnvPhySensorMaxValue=rlEnvPhySensorMaxValue, rlEnvPhySensorTestValue=rlEnvPhySensorTestValue, rlEntPhySensorEntry=rlEntPhySensorEntry, rlEntPhySensorTable=rlEntPhySensorTable, rlSensor=rlSensor, PYSNMP_MODULE_ID=rlSensor)
