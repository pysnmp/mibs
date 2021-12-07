#
# PySNMP MIB module RADLAN-SENSORENTMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SENSORENTMIB
# Produced by pysmi-1.1.3 at Tue Dec  7 13:56:55 2021
# On host fv-az33-388 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
entityPhysicalGroup, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entityPhysicalGroup", "entPhysicalIndex")
EntitySensorValue, entPhySensorEntry = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue", "entPhySensorEntry")
rlEnv, = mibBuilder.importSymbols("RADLAN-HWENVIROMENT", "rlEnv")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
mib_2, iso, NotificationType, MibIdentifier, Integer32, Counter32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Gauge32, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "iso", "NotificationType", "MibIdentifier", "Integer32", "Counter32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Gauge32", "ModuleIdentity", "Bits", "Unsigned32")
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
mibBuilder.exportSymbols("RADLAN-SENSORENTMIB", rlEnvPhySensorTestValue=rlEnvPhySensorTestValue, rlEnvPhySensorMaxValue=rlEnvPhySensorMaxValue, PYSNMP_MODULE_ID=rlSensor, rlSensor=rlSensor, rlEntPhySensorTable=rlEntPhySensorTable, rlEnvPhySensorMinValue=rlEnvPhySensorMinValue, rlEntPhySensorEntry=rlEntPhySensorEntry)
