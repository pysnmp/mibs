#
# PySNMP MIB module BLUECOAT-SG-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-SENSOR-MIB
# Produced by pysmi-1.1.12 at Tue May 28 13:38:21 2024
# On host fv-az768-311 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, NotificationType, ObjectIdentity, IpAddress, Bits, TimeTicks, iso, Unsigned32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "NotificationType", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks", "iso", "Unsigned32", "MibIdentifier", "ModuleIdentity")
TruthValue, TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "TimeStamp", "DisplayString")
deviceSensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 1))
deviceSensorMIB.setRevisions(('2015-11-26 03:00', '2013-07-11 03:00', '2007-11-05 03:00', '2002-11-06 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: deviceSensorMIB.setRevisionsDescriptions(('Add new value (notInstalled) to SensorStatus', 'Access level for deviceSensorTrapEnabled changed.', 'Minor corrections and reformatting.', 'Initial revision of this MIB.',))
if mibBuilder.loadTexts: deviceSensorMIB.setLastUpdated('201511260300Z')
if mibBuilder.loadTexts: deviceSensorMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: deviceSensorMIB.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: deviceSensorMIB.setDescription('The sensor MIB is used to monitor\n                         the values of sensors')
deviceSensorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1))
deviceSensorMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2))
deviceSensorMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0))
class SensorUnits(TextualConvention, Integer32):
    description = 'Sensor measurement unit types. Valid values are:\n                other(1)        - a measure other than those listed below.\n                truthvalue(2)   - value takes { true(1), false(2) }.\n                specialEnum(3)  - value takes user defined enumerated values.\n                volts(4)        - electrical potential.\n                celsius(5)      - temperature.\n                rpm(6)          - revolutions per minute.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("truthvalue", 2), ("specialEnum", 3), ("volts", 4), ("celsius", 5), ("rpm", 6))

class SensorCode(TextualConvention, Integer32):
    description = 'Interpretation of the current sensor value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("ok", 1), ("unknown", 2), ("notInstalled", 3), ("voltageLowWarning", 4), ("voltageLowCritical", 5), ("noPower", 6), ("voltageHighWarning", 7), ("voltageHighCritical", 8), ("voltageHighSevere", 9), ("temperatureHighWarning", 10), ("temperatureHighCritical", 11), ("temperatureHighSevere", 12), ("fanSlowWarning", 13), ("fanSlowCritical", 14), ("fanStopped", 15))

class ExpBase10(TextualConvention, Integer32):
    description = "Exponent base 10 for the current sensor value.\n                         For example '-1' means value*(1/10)."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-24, 24)

class SensorValue(TextualConvention, Integer32):
    description = 'For sensors that measure volts and celsius,\n                         this item is a fixed point number.\n                         For sensors that measure rpm, this item\n                         can take only nonnegative values.\n                         For sensors of type truthvalue, this item\n                         can take only two values: true(1), false(2).\n                         For sensors of type specialEnum, this item\n                         can take any value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class SensorStatus(TextualConvention, Integer32):
    description = 'Indicates the operational status of the sensor.\n                         ok(1) means the agent can read the sensor value.\n                         unavailable(2) means that the agent presently\n                         can not report the sensor value.\n                         nonoperational(3) means that the sensor is broken.\n                         notInstalled(4) means that the sensor or device is not present.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3), ("notInstalled", 4))

deviceSensorValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1))
deviceSensorValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1), )
if mibBuilder.loadTexts: deviceSensorValueTable.setStatus('current')
if mibBuilder.loadTexts: deviceSensorValueTable.setDescription('Table of sensors.')
deviceSensorValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-SENSOR-MIB", "deviceSensorIndex"))
if mibBuilder.loadTexts: deviceSensorValueEntry.setStatus('current')
if mibBuilder.loadTexts: deviceSensorValueEntry.setDescription('An deviceSensorValueTable entry describes the\n                         present reading of a sensor, the measurement units\n                         and sensor operational status.')
deviceSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceSensorIndex.setStatus('current')
if mibBuilder.loadTexts: deviceSensorIndex.setDescription('An arbitrary value which uniquely identifies the sensor')
deviceSensorTrapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorTrapEnabled.setStatus('current')
if mibBuilder.loadTexts: deviceSensorTrapEnabled.setDescription('This variable controls generation of\n                         deviceSensorTrap for this sensor.\n                         When this variable is true(1), generation of\n                         deviceSensorTrap is enabled.  When this variable\n                         is false(2), generation of deviceSensorTrap is\n                         disabled. The default start-up value is true(1).')
deviceSensorUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 3), SensorUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorUnits.setStatus('current')
if mibBuilder.loadTexts: deviceSensorUnits.setDescription('This variable indicates the type of data\n                         reported by the deviceSensorValue.\n                         This variable is set by the agent at start-up\n                         and the value does not change during operation.')
deviceSensorScale = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 4), ExpBase10()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorScale.setStatus('current')
if mibBuilder.loadTexts: deviceSensorScale.setDescription('Power of 10 to apply to the value\n                         reported by the deviceSensorValue.\n                         This variable is set by the agent at start-up\n                         and the value does not change during operation.')
deviceSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 5), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorValue.setStatus('current')
if mibBuilder.loadTexts: deviceSensorValue.setDescription("This variable reports the most recent measurement\n                         seen by the sensor. To correctly display or interpret\n                         this variable's value, you must also know\n                         deviceSensorUnits.")
deviceSensorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 6), SensorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorCode.setStatus('current')
if mibBuilder.loadTexts: deviceSensorCode.setDescription('This variable reports how to interpret\n                         deviceSensorValue for the sensor.')
deviceSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 7), SensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorStatus.setStatus('current')
if mibBuilder.loadTexts: deviceSensorStatus.setDescription('This variable indicates the present operational\n                         status of the sensor.')
deviceSensorTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 8), TimeStamp()).setUnits('Hundredths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorTimeStamp.setStatus('current')
if mibBuilder.loadTexts: deviceSensorTimeStamp.setDescription('This variable indicates the age of the value\n                         reported by deviceSensorValue.')
deviceSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorName.setStatus('current')
if mibBuilder.loadTexts: deviceSensorName.setDescription('The textual name of the sensor.')
deviceSensorTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0, 1)).setObjects(("BLUECOAT-SG-SENSOR-MIB", "deviceSensorName"), ("BLUECOAT-SG-SENSOR-MIB", "deviceSensorValue"), ("BLUECOAT-SG-SENSOR-MIB", "deviceSensorCode"))
if mibBuilder.loadTexts: deviceSensorTrap.setStatus('current')
if mibBuilder.loadTexts: deviceSensorTrap.setDescription('The sensor value warrants a notification.')
mibBuilder.exportSymbols("BLUECOAT-SG-SENSOR-MIB", deviceSensorUnits=deviceSensorUnits, deviceSensorScale=deviceSensorScale, deviceSensorValue=deviceSensorValue, SensorValue=SensorValue, deviceSensorIndex=deviceSensorIndex, deviceSensorCode=deviceSensorCode, SensorStatus=SensorStatus, deviceSensorValueTable=deviceSensorValueTable, PYSNMP_MODULE_ID=deviceSensorMIB, deviceSensorMIBNotifications=deviceSensorMIBNotifications, deviceSensorMIB=deviceSensorMIB, deviceSensorValues=deviceSensorValues, deviceSensorTrap=deviceSensorTrap, deviceSensorTrapEnabled=deviceSensorTrapEnabled, SensorUnits=SensorUnits, SensorCode=SensorCode, deviceSensorMIBObjects=deviceSensorMIBObjects, ExpBase10=ExpBase10, deviceSensorValueEntry=deviceSensorValueEntry, deviceSensorStatus=deviceSensorStatus, deviceSensorMIBNotificationsPrefix=deviceSensorMIBNotificationsPrefix, deviceSensorTimeStamp=deviceSensorTimeStamp, deviceSensorName=deviceSensorName)
