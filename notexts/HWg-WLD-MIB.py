#
# PySNMP MIB module HWg-WLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hwg/HWg-WLD-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 09:13:51 2024
# On host fv-az532-988 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, NotificationType, Counter32, iso, Counter64, IpAddress, Bits, Unsigned32, enterprises, ModuleIdentity, ObjectIdentity, TimeTicks, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "NotificationType", "Counter32", "iso", "Counter64", "IpAddress", "Bits", "Unsigned32", "enterprises", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Gauge32", "MibIdentifier")
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
mibBuilder.exportSymbols("HWg-WLD-MIB", wldName=wldName, wldState=wldState, wldPeriodicAlarm=wldPeriodicAlarm, hwgroup=hwgroup, SensorValue=SensorValue, hwgwld=hwgwld, wldID=wldID, SensorState=SensorState, wldValue=wldValue, SensorID=SensorID, infoAddressMAC=infoAddressMAC, PositiveInteger=PositiveInteger, wldStateToAlarm=wldStateToAlarm, info=info, wldStateToNormal=wldStateToNormal, wldIndex=wldIndex, wldSN=wldSN, SensorName=SensorName, wldEntry=wldEntry, x390=x390, wldTable=wldTable, SensorSN=SensorSN)
