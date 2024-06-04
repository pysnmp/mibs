#
# PySNMP MIB module STE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hwg/STE-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 10:07:01 2024
# On host fv-az1773-903 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, Bits, Gauge32, iso, Unsigned32, NotificationType, ModuleIdentity, enterprises, Integer32, ObjectIdentity, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Bits", "Gauge32", "iso", "Unsigned32", "NotificationType", "ModuleIdentity", "enterprises", "Integer32", "ObjectIdentity", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class UnitType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("celsius", 1), ("fahrenheit", 2), ("kelvin", 3), ("percent", 4))

class OnOff(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class InputAlarmState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("normal", 0), ("alarm", 1))

class IOName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class SensorState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("invalid", 0), ("normal", 1), ("outofrangelo", 2), ("outofrangehi", 3), ("alarmlo", 4), ("alarmhi", 5))

class SensorSN(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class SensorName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class SensorValue(Integer32):
    pass

class SensorID(Integer32):
    pass

class SensorString(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 10)

hwgroup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796))
x390 = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4))
ste = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 1))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 1, 70))
infoAddressMAC = MibScalar((1, 3, 6, 1, 4, 1, 21796, 4, 1, 70, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: infoAddressMAC.setStatus('mandatory')
inpTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 4, 1, 1), )
if mibBuilder.loadTexts: inpTable.setStatus('mandatory')
inpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 4, 1, 1, 1), ).setIndexNames((0, "STE-MIB", "inpIndex"))
if mibBuilder.loadTexts: inpEntry.setStatus('mandatory')
inpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 1, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: inpIndex.setStatus('mandatory')
inpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 1, 1, 2), OnOff()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpValue.setStatus('mandatory')
inpName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 1, 1, 3), IOName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpName.setStatus('mandatory')
inpAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 1, 1, 4), InputAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpAlarmState.setStatus('mandatory')
sensTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 4, 1, 3), )
if mibBuilder.loadTexts: sensTable.setStatus('mandatory')
sensEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 4, 1, 3, 1), ).setIndexNames((0, "STE-MIB", "sensIndex"))
if mibBuilder.loadTexts: sensEntry.setStatus('mandatory')
sensIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 3, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: sensIndex.setStatus('mandatory')
sensName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 3, 1, 2), SensorName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensName.setStatus('mandatory')
sensState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 3, 1, 3), SensorState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensState.setStatus('mandatory')
sensString = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 3, 1, 4), SensorString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensString.setStatus('mandatory')
sensValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 3, 1, 5), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensValue.setStatus('mandatory')
sensSN = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 3, 1, 6), SensorSN()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensSN.setStatus('mandatory')
sensUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 3, 1, 7), UnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensUnit.setStatus('mandatory')
sensID = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 1, 3, 1, 8), UnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensID.setStatus('mandatory')
mibBuilder.exportSymbols("STE-MIB", UnitType=UnitType, sensString=sensString, infoAddressMAC=infoAddressMAC, sensID=sensID, sensName=sensName, InputAlarmState=InputAlarmState, sensTable=sensTable, inpIndex=inpIndex, SensorString=SensorString, inpTable=inpTable, inpAlarmState=inpAlarmState, info=info, OnOff=OnOff, sensValue=sensValue, inpName=inpName, sensUnit=sensUnit, sensState=sensState, sensEntry=sensEntry, sensSN=sensSN, x390=x390, SensorState=SensorState, SensorSN=SensorSN, SensorValue=SensorValue, ste=ste, SensorID=SensorID, IOName=IOName, SensorName=SensorName, sensIndex=sensIndex, inpValue=inpValue, PositiveInteger=PositiveInteger, inpEntry=inpEntry, hwgroup=hwgroup)
