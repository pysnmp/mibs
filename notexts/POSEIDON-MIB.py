#
# PySNMP MIB module POSEIDON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hwg/POSEIDON-MIB
# Produced by pysmi-1.1.8 at Wed Sep 13 14:57:40 2023
# On host fv-az629-233 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
NotificationType, TimeTicks, Counter64, MibIdentifier, Gauge32, Integer32, ModuleIdentity, IpAddress, iso, enterprises, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter64", "MibIdentifier", "Gauge32", "Integer32", "ModuleIdentity", "IpAddress", "iso", "enterprises", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class OnOff(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class OutputType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("onOff", 0), ("rts", 1), ("dtr", 2))

class OutputMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("manual", 0), ("autoAlarm", 1), ("autoTriggerEq", 2), ("autoTriggerHi", 3), ("autoTriggerLo", 4))

class UnitType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("celsius", 0), ("fahrenheit", 1), ("kelvin", 2), ("percent", 3), ("volt", 4), ("miliAmper", 5), ("noUnit", 6), ("pulse", 7), ("switch", 8), ("dewPoint", 9), ("absoluteHumidity", 10), ("pressure", 11), ("universal", 12))

class InputAlarmSetup(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("inactive", 0), ("activeOff", 1), ("activeOn", 2))

class InputAlarmState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("normal", 0), ("alarm", 1))

class SensorState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("invalid", 0), ("normal", 1), ("alarmstate", 2), ("alarm", 3))

class SensorID(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IOName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 20)

class SensorName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 15)

class SensorValue(Integer32):
    pass

class SensorString(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 10)

class SensorUnitString(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 4)

class SensorFlags(Integer32):
    pass

class TimeStamp(TimeTicks):
    pass

hwgroup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796))
charonII = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3))
poseidon = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 3))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 3, 70))
setup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99))
inpTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1), )
if mibBuilder.loadTexts: inpTable.setStatus('current')
inpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1), ).setIndexNames((0, "POSEIDON-MIB", "inpIndex"))
if mibBuilder.loadTexts: inpEntry.setStatus('current')
inpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: inpIndex.setStatus('current')
inpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 2), OnOff()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpValue.setStatus('current')
inpName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 3), IOName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inpName.setStatus('current')
inpAlarmSetup = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 4), InputAlarmSetup()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inpAlarmSetup.setStatus('current')
inpAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 1, 1, 5), InputAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpAlarmState.setStatus('current')
outTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2), )
if mibBuilder.loadTexts: outTable.setStatus('current')
outEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1), ).setIndexNames((0, "POSEIDON-MIB", "outIndex"))
if mibBuilder.loadTexts: outEntry.setStatus('current')
outIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: outIndex.setStatus('current')
outValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 2), OnOff()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outValue.setStatus('current')
outName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 3), IOName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outName.setStatus('current')
outType = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 4), OutputType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outType.setStatus('current')
outMode = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 2, 1, 5), OutputMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outMode.setStatus('current')
sensTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3), )
if mibBuilder.loadTexts: sensTable.setStatus('current')
sensEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1), ).setIndexNames((0, "POSEIDON-MIB", "sensIndex"))
if mibBuilder.loadTexts: sensEntry.setStatus('current')
sensIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: sensIndex.setStatus('current')
sensName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 2), SensorName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensName.setStatus('current')
sensState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 4), SensorState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensState.setStatus('current')
sensString = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 5), SensorString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensString.setStatus('current')
sensValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 6), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensValue.setStatus('current')
sensValueRaw = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 7), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensValueRaw.setStatus('current')
sensID = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 8), SensorID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensID.setStatus('current')
sensUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 9), UnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensUnit.setStatus('current')
sensUnitString = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 3, 1, 10), SensorUnitString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensUnitString.setStatus('current')
tsAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50))
tsAlarmsPresent = MibScalar((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmsPresent.setStatus('current')
tsAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2), )
if mibBuilder.loadTexts: tsAlarmTable.setStatus('current')
tsAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1), ).setIndexNames((0, "POSEIDON-MIB", "tsAlarmIdx"))
if mibBuilder.loadTexts: tsAlarmEntry.setStatus('current')
tsAlarmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: tsAlarmIdx.setStatus('current')
tsAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 2), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmId.setStatus('current')
tsAlarmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inputStateAlarm", 1), ("temperatureOutOfRange", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmDescr.setStatus('current')
tsAlarmSensName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 4), SensorName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmSensName.setStatus('current')
tsAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 50, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmTime.setStatus('current')
infoAddressMAC = MibScalar((1, 3, 6, 1, 4, 1, 21796, 3, 3, 70, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: infoAddressMAC.setStatus('current')
sensSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1))
unitType = MibScalar((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 1), UnitType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitType.setStatus('current')
sensSetupTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2), )
if mibBuilder.loadTexts: sensSetupTable.setStatus('current')
sensSetupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1), ).setIndexNames((0, "POSEIDON-MIB", "sensSetupIndex"))
if mibBuilder.loadTexts: sensSetupEntry.setStatus('current')
sensSetupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: sensSetupIndex.setStatus('current')
sensSetupName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 2), SensorName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensSetupName.setStatus('current')
sensFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 5), SensorFlags()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensFlags.setStatus('current')
sensLimitMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 6), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensLimitMin.setStatus('current')
sensLimitMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 7), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensLimitMax.setStatus('current')
sensHysteresis = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 3, 99, 1, 2, 1, 8), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensHysteresis.setStatus('current')
inpAlarmStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 3) + (0,1)).setObjects(("SNMPv2-MIB", "sysName"), ("POSEIDON-MIB", "infoAddressMAC"), ("POSEIDON-MIB", "inpName"), ("POSEIDON-MIB", "inpValue"), ("POSEIDON-MIB", "inpAlarmState"))
sensAlarmStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 3) + (0,2)).setObjects(("SNMPv2-MIB", "sysName"), ("POSEIDON-MIB", "infoAddressMAC"), ("POSEIDON-MIB", "sensName"), ("POSEIDON-MIB", "sensID"), ("POSEIDON-MIB", "sensState"), ("POSEIDON-MIB", "sensValue"), ("POSEIDON-MIB", "sensUnit"))
tsTrapAlarmStart = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 3) + (0,3)).setObjects(("SNMPv2-MIB", "sysName"), ("POSEIDON-MIB", "infoAddressMAC"), ("POSEIDON-MIB", "tsAlarmId"), ("POSEIDON-MIB", "tsAlarmDescr"))
tsTrapAlarmEnd = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 3) + (0,4)).setObjects(("SNMPv2-MIB", "sysName"), ("POSEIDON-MIB", "infoAddressMAC"), ("POSEIDON-MIB", "tsAlarmId"), ("POSEIDON-MIB", "tsAlarmDescr"))
mibBuilder.exportSymbols("POSEIDON-MIB", sensIndex=sensIndex, inpTable=inpTable, sensSetupTable=sensSetupTable, tsAlarmSensName=tsAlarmSensName, outName=outName, sensName=sensName, sensValueRaw=sensValueRaw, sensSetupIndex=sensSetupIndex, outType=outType, tsAlarmDescr=tsAlarmDescr, tsTrapAlarmStart=tsTrapAlarmStart, inpName=inpName, setup=setup, sensValue=sensValue, tsAlarm=tsAlarm, tsAlarmTable=tsAlarmTable, poseidon=poseidon, InputAlarmSetup=InputAlarmSetup, sensLimitMin=sensLimitMin, sensString=sensString, sensLimitMax=sensLimitMax, outValue=outValue, inpIndex=inpIndex, hwgroup=hwgroup, OutputType=OutputType, tsAlarmTime=tsAlarmTime, inpValue=inpValue, sensEntry=sensEntry, inpAlarmStateChanged=inpAlarmStateChanged, SensorID=SensorID, PositiveInteger=PositiveInteger, inpEntry=inpEntry, SensorValue=SensorValue, UnitType=UnitType, outEntry=outEntry, inpAlarmSetup=inpAlarmSetup, sensSetupName=sensSetupName, IOName=IOName, OnOff=OnOff, InputAlarmState=InputAlarmState, SensorName=SensorName, SensorString=SensorString, SensorFlags=SensorFlags, info=info, sensUnit=sensUnit, tsAlarmIdx=tsAlarmIdx, sensAlarmStateChanged=sensAlarmStateChanged, sensUnitString=sensUnitString, sensID=sensID, sensHysteresis=sensHysteresis, tsAlarmEntry=tsAlarmEntry, outMode=outMode, tsAlarmId=tsAlarmId, sensSetup=sensSetup, inpAlarmState=inpAlarmState, sensTable=sensTable, unitType=unitType, sensSetupEntry=sensSetupEntry, SensorState=SensorState, sensState=sensState, OutputMode=OutputMode, infoAddressMAC=infoAddressMAC, charonII=charonII, sensFlags=sensFlags, outTable=outTable, outIndex=outIndex, TimeStamp=TimeStamp, tsAlarmsPresent=tsAlarmsPresent, tsTrapAlarmEnd=tsTrapAlarmEnd, SensorUnitString=SensorUnitString)
