#
# PySNMP MIB module BLUECOAT-SG-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-SENSOR-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 08:03:19 2024
# On host fv-az1110-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, TimeTicks, iso, NotificationType, MibIdentifier, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Counter64, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "TimeTicks", "iso", "NotificationType", "MibIdentifier", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Counter64", "Integer32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "TimeStamp")
deviceSensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 1))
deviceSensorMIB.setRevisions(('2015-11-26 03:00', '2013-07-11 03:00', '2007-11-05 03:00', '2002-11-06 03:00',))
if mibBuilder.loadTexts: deviceSensorMIB.setLastUpdated('201511260300Z')
if mibBuilder.loadTexts: deviceSensorMIB.setOrganization('Blue Coat Systems, Inc.')
deviceSensorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1))
deviceSensorMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2))
deviceSensorMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0))
class SensorUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("truthvalue", 2), ("specialEnum", 3), ("volts", 4), ("celsius", 5), ("rpm", 6))

class SensorCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("ok", 1), ("unknown", 2), ("notInstalled", 3), ("voltageLowWarning", 4), ("voltageLowCritical", 5), ("noPower", 6), ("voltageHighWarning", 7), ("voltageHighCritical", 8), ("voltageHighSevere", 9), ("temperatureHighWarning", 10), ("temperatureHighCritical", 11), ("temperatureHighSevere", 12), ("fanSlowWarning", 13), ("fanSlowCritical", 14), ("fanStopped", 15))

class ExpBase10(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-24, 24)

class SensorValue(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class SensorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3), ("notInstalled", 4))

deviceSensorValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1))
deviceSensorValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1), )
if mibBuilder.loadTexts: deviceSensorValueTable.setStatus('current')
deviceSensorValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-SENSOR-MIB", "deviceSensorIndex"))
if mibBuilder.loadTexts: deviceSensorValueEntry.setStatus('current')
deviceSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceSensorIndex.setStatus('current')
deviceSensorTrapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorTrapEnabled.setStatus('current')
deviceSensorUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 3), SensorUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorUnits.setStatus('current')
deviceSensorScale = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 4), ExpBase10()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorScale.setStatus('current')
deviceSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 5), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorValue.setStatus('current')
deviceSensorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 6), SensorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorCode.setStatus('current')
deviceSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 7), SensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorStatus.setStatus('current')
deviceSensorTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 8), TimeStamp()).setUnits('Hundredths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorTimeStamp.setStatus('current')
deviceSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorName.setStatus('current')
deviceSensorTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0, 1)).setObjects(("BLUECOAT-SG-SENSOR-MIB", "deviceSensorName"), ("BLUECOAT-SG-SENSOR-MIB", "deviceSensorValue"), ("BLUECOAT-SG-SENSOR-MIB", "deviceSensorCode"))
if mibBuilder.loadTexts: deviceSensorTrap.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-SENSOR-MIB", deviceSensorValueTable=deviceSensorValueTable, SensorCode=SensorCode, deviceSensorUnits=deviceSensorUnits, deviceSensorMIBNotifications=deviceSensorMIBNotifications, SensorUnits=SensorUnits, deviceSensorMIB=deviceSensorMIB, deviceSensorMIBNotificationsPrefix=deviceSensorMIBNotificationsPrefix, deviceSensorName=deviceSensorName, deviceSensorTimeStamp=deviceSensorTimeStamp, deviceSensorTrapEnabled=deviceSensorTrapEnabled, deviceSensorMIBObjects=deviceSensorMIBObjects, deviceSensorScale=deviceSensorScale, SensorValue=SensorValue, deviceSensorCode=deviceSensorCode, deviceSensorStatus=deviceSensorStatus, SensorStatus=SensorStatus, deviceSensorValue=deviceSensorValue, deviceSensorIndex=deviceSensorIndex, deviceSensorValues=deviceSensorValues, PYSNMP_MODULE_ID=deviceSensorMIB, deviceSensorTrap=deviceSensorTrap, ExpBase10=ExpBase10, deviceSensorValueEntry=deviceSensorValueEntry)
