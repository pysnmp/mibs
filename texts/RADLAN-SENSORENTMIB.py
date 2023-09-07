#
# PySNMP MIB module RADLAN-SENSORENTMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SENSORENTMIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:30:32 2023
# On host fv-az407-692 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
entityPhysicalGroup, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entityPhysicalGroup", "entPhysicalIndex")
EntitySensorValue, entPhySensorEntry = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue", "entPhySensorEntry")
rlEnv, = mibBuilder.importSymbols("RADLAN-HWENVIROMENT", "rlEnv")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, ModuleIdentity, MibIdentifier, Unsigned32, Bits, ObjectIdentity, Gauge32, Counter64, iso, Counter32, mib_2, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Bits", "ObjectIdentity", "Gauge32", "Counter64", "iso", "Counter32", "mib-2", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention")
rlSensor = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 83, 4))
rlSensor.setRevisions(('2003-09-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSensor.setRevisionsDescriptions(('ADDED this MODULE-IDENTITY clause.',))
if mibBuilder.loadTexts: rlSensor.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlSensor.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlSensor.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlSensor.setDescription('The private MIB module definition for sensors in Radlan devices.')
rlEntPhySensorTable = MibTable((1, 3, 6, 1, 4, 1, 89, 83, 3), )
if mibBuilder.loadTexts: rlEntPhySensorTable.setStatus('current')
if mibBuilder.loadTexts: rlEntPhySensorTable.setDescription('The addition to the table of sensors maintained by the environmental\n                monitor.')
rlEntPhySensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 83, 3, 1), )
entPhySensorEntry.registerAugmentions(("RADLAN-SENSORENTMIB", "rlEntPhySensorEntry"))
rlEntPhySensorEntry.setIndexNames(*entPhySensorEntry.getIndexNames())
if mibBuilder.loadTexts: rlEntPhySensorEntry.setStatus('current')
if mibBuilder.loadTexts: rlEntPhySensorEntry.setDescription('An additon to the entry in the sensor table, representing the\n                maximum/minimum values for the sensor associated.')
rlEnvPhySensorMinValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 1), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvPhySensorMinValue.setStatus('current')
if mibBuilder.loadTexts: rlEnvPhySensorMinValue.setDescription('Minimum value for the Sensor being instrumented.')
rlEnvPhySensorMaxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 2), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvPhySensorMaxValue.setStatus('current')
if mibBuilder.loadTexts: rlEnvPhySensorMaxValue.setDescription('Maximum value for the Sensor being instrumented.')
rlEnvPhySensorTestValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 3), EntitySensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEnvPhySensorTestValue.setStatus('current')
if mibBuilder.loadTexts: rlEnvPhySensorTestValue.setDescription('Test/reference value for the Sensor being instrumented.')
mibBuilder.exportSymbols("RADLAN-SENSORENTMIB", rlEnvPhySensorTestValue=rlEnvPhySensorTestValue, rlEnvPhySensorMaxValue=rlEnvPhySensorMaxValue, rlEntPhySensorTable=rlEntPhySensorTable, rlSensor=rlSensor, PYSNMP_MODULE_ID=rlSensor, rlEnvPhySensorMinValue=rlEnvPhySensorMinValue, rlEntPhySensorEntry=rlEntPhySensorEntry)
