#
# PySNMP MIB module HWg-WLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hwg/HWg-WLD-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 07:54:59 2023
# On host fv-az555-184 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
TimeTicks, Counter64, ModuleIdentity, iso, enterprises, Counter32, NotificationType, Bits, MibIdentifier, ObjectIdentity, IpAddress, Integer32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ModuleIdentity", "iso", "enterprises", "Counter32", "NotificationType", "Bits", "MibIdentifier", "ObjectIdentity", "IpAddress", "Integer32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
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
mibBuilder.exportSymbols("HWg-WLD-MIB", SensorValue=SensorValue, wldTable=wldTable, SensorID=SensorID, wldID=wldID, SensorState=SensorState, wldStateToNormal=wldStateToNormal, wldState=wldState, wldEntry=wldEntry, wldIndex=wldIndex, wldValue=wldValue, PositiveInteger=PositiveInteger, x390=x390, wldName=wldName, wldPeriodicAlarm=wldPeriodicAlarm, hwgwld=hwgwld, wldSN=wldSN, wldStateToAlarm=wldStateToAlarm, SensorSN=SensorSN, SensorName=SensorName, info=info, hwgroup=hwgroup, infoAddressMAC=infoAddressMAC)
