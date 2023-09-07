#
# PySNMP MIB module HWg-WLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hwg/HWg-WLD-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:26:30 2023
# On host fv-az407-692 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Bits, TimeTicks, Counter64, IpAddress, ModuleIdentity, iso, NotificationType, Counter32, Unsigned32, ObjectIdentity, NotificationType, enterprises, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Counter64", "IpAddress", "ModuleIdentity", "iso", "NotificationType", "Counter32", "Unsigned32", "ObjectIdentity", "NotificationType", "enterprises", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class SensorState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3))
    namedValues = NamedValues(("invalid", 0), ("normal", 1), ("alarm", 3))

class SensorValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("normal", 0), ("flooded", 1), ("disconnect", 2), ("invalid", 3))

class SensorSN(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class SensorName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class SensorID(Integer32):
    pass

hwgroup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796))
x390 = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4))
hwgwld = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 5))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 5, 70))
infoAddressMAC = MibScalar((1, 3, 6, 1, 4, 1, 21796, 4, 5, 70, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: infoAddressMAC.setStatus('mandatory')
wldTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 4, 5, 4), )
if mibBuilder.loadTexts: wldTable.setStatus('mandatory')
wldEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1), ).setIndexNames((0, "HWg-WLD-MIB", "wldIndex"))
if mibBuilder.loadTexts: wldEntry.setStatus('mandatory')
wldIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wldIndex.setStatus('mandatory')
wldName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 2), SensorName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wldName.setStatus('mandatory')
wldState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 3), SensorState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wldState.setStatus('mandatory')
wldSN = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 4), SensorSN()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wldSN.setStatus('mandatory')
wldID = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 5), SensorID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wldID.setStatus('mandatory')
wldValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 6), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wldValue.setStatus('mandatory')
wldStateToAlarm = NotificationType((1, 3, 6, 1, 4, 1, 21796, 4, 5) + (0,1)).setObjects(("SNMPv2-MIB", "sysName"), ("HWg-WLD-MIB", "infoAddressMAC"), ("HWg-WLD-MIB", "wldIndex"), ("HWg-WLD-MIB", "wldName"), ("HWg-WLD-MIB", "wldState"), ("HWg-WLD-MIB", "wldSN"), ("HWg-WLD-MIB", "wldID"), ("HWg-WLD-MIB", "wldValue"))
wldStateToNormal = NotificationType((1, 3, 6, 1, 4, 1, 21796, 4, 5) + (0,2)).setObjects(("SNMPv2-MIB", "sysName"), ("HWg-WLD-MIB", "infoAddressMAC"), ("HWg-WLD-MIB", "wldIndex"), ("HWg-WLD-MIB", "wldName"), ("HWg-WLD-MIB", "wldState"), ("HWg-WLD-MIB", "wldSN"), ("HWg-WLD-MIB", "wldID"), ("HWg-WLD-MIB", "wldValue"))
wldPeriodicAlarm = NotificationType((1, 3, 6, 1, 4, 1, 21796, 4, 5) + (0,3)).setObjects(("SNMPv2-MIB", "sysName"), ("HWg-WLD-MIB", "infoAddressMAC"), ("HWg-WLD-MIB", "wldIndex"), ("HWg-WLD-MIB", "wldName"), ("HWg-WLD-MIB", "wldState"), ("HWg-WLD-MIB", "wldSN"), ("HWg-WLD-MIB", "wldID"), ("HWg-WLD-MIB", "wldValue"))
mibBuilder.exportSymbols("HWg-WLD-MIB", info=info, SensorState=SensorState, SensorSN=SensorSN, wldState=wldState, infoAddressMAC=infoAddressMAC, SensorName=SensorName, wldValue=wldValue, wldStateToAlarm=wldStateToAlarm, hwgwld=hwgwld, PositiveInteger=PositiveInteger, wldSN=wldSN, SensorValue=SensorValue, wldID=wldID, wldIndex=wldIndex, wldPeriodicAlarm=wldPeriodicAlarm, wldTable=wldTable, hwgroup=hwgroup, wldName=wldName, x390=x390, wldStateToNormal=wldStateToNormal, SensorID=SensorID, wldEntry=wldEntry)
