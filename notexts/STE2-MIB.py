#
# PySNMP MIB module STE2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hwg/STE2-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 07:35:27 2023
# On host fv-az362-181 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, MibIdentifier, ModuleIdentity, enterprises, TimeTicks, ObjectIdentity, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, Counter64, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "enterprises", "TimeTicks", "ObjectIdentity", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "Counter64", "IpAddress", "Bits")
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
ste2 = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 9))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 9, 70))
infoAddressMAC = MibScalar((1, 3, 6, 1, 4, 1, 21796, 4, 9, 70, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: infoAddressMAC.setStatus('mandatory')
inpTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 4, 9, 1), )
if mibBuilder.loadTexts: inpTable.setStatus('mandatory')
inpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 4, 9, 1, 1), ).setIndexNames((0, "STE2-MIB", "inpIndex"))
if mibBuilder.loadTexts: inpEntry.setStatus('mandatory')
inpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 1, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: inpIndex.setStatus('mandatory')
inpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 1, 1, 2), OnOff()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpValue.setStatus('mandatory')
inpName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 1, 1, 3), IOName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpName.setStatus('mandatory')
inpAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 1, 1, 4), InputAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpAlarmState.setStatus('mandatory')
sensTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 4, 9, 3), )
if mibBuilder.loadTexts: sensTable.setStatus('mandatory')
sensEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1), ).setIndexNames((0, "STE2-MIB", "sensIndex"))
if mibBuilder.loadTexts: sensEntry.setStatus('mandatory')
sensIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: sensIndex.setStatus('mandatory')
sensName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 2), SensorName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensName.setStatus('mandatory')
sensState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 3), SensorState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensState.setStatus('mandatory')
sensString = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 4), SensorString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensString.setStatus('mandatory')
sensValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 5), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensValue.setStatus('mandatory')
sensSN = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 6), SensorSN()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensSN.setStatus('mandatory')
sensUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 7), UnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensUnit.setStatus('mandatory')
sensID = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 9, 3, 1, 8), UnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensID.setStatus('mandatory')
mibBuilder.exportSymbols("STE2-MIB", sensState=sensState, IOName=IOName, SensorString=SensorString, UnitType=UnitType, x390=x390, inpIndex=inpIndex, sensSN=sensSN, inpName=inpName, InputAlarmState=InputAlarmState, sensName=sensName, sensEntry=sensEntry, info=info, SensorName=SensorName, sensValue=sensValue, OnOff=OnOff, infoAddressMAC=infoAddressMAC, sensUnit=sensUnit, SensorState=SensorState, PositiveInteger=PositiveInteger, sensString=sensString, inpAlarmState=inpAlarmState, sensIndex=sensIndex, inpTable=inpTable, sensID=sensID, ste2=ste2, sensTable=sensTable, SensorID=SensorID, inpValue=inpValue, hwgroup=hwgroup, inpEntry=inpEntry, SensorValue=SensorValue, SensorSN=SensorSN)
