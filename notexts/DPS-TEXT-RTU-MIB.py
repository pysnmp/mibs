#
# PySNMP MIB module DPS-TEXT-RTU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dpstelecom/DPS-TEXT-RTU-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 12:10:26 2023
# On host fv-az741-387 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dpsAlarmControl, = mibBuilder.importSymbols("DPS-MIB-V38", "dpsAlarmControl")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, iso, Unsigned32, MibIdentifier, Gauge32, ModuleIdentity, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "iso", "Unsigned32", "MibIdentifier", "Gauge32", "ModuleIdentity", "Counter32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dpsTEXTRTUv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 5))
dpsTEXTRTUv2Ident = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 5, 1))
class AnalogThresholds(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("noAlarms", 0), ("minorUnder", 1), ("minorOver", 2), ("majorUnder", 3), ("majorOver", 4), ("notDetected", 5))

class RTUCAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("latch", 1), ("release", 2), ("momentary", 3), ("syncStanding", 4), ("syncAnalogs", 5))

dpsTEXTRTUv2DateTime = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsTEXTRTUv2DateTime.setStatus('current')
dpsTEXTRTUv2DeviceType = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsTEXTRTUv2DeviceType.setStatus('current')
dpsTEXTRTUv2Phone = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsTEXTRTUv2Phone.setStatus('current')
dpsTEXTRTUv2AlarmGrid = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 5, 2))
dpsTEXTRTUv2ADisplay = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsTEXTRTUv2ADisplay.setStatus('current')
dpsTEXTRTUv2APoint = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsTEXTRTUv2APoint.setStatus('current')
dpsTEXTRTUv2APntDesc = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsTEXTRTUv2APntDesc.setStatus('current')
dpsTEXTRTUv2AState = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsTEXTRTUv2AState.setStatus('current')
dpsTEXTRTUAnalogvalue = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsTEXTRTUAnalogvalue.setStatus('current')
dpsTEXTRTUAnalogthresholds = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 6), AnalogThresholds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsTEXTRTUAnalogthresholds.setStatus('current')
dpsTEXTRTUv2ControlGrid = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 5, 3))
dpsTEXTRTUv2CDisplay = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsTEXTRTUv2CDisplay.setStatus('current')
dpsTEXTRTUv2CPoint = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsTEXTRTUv2CPoint.setStatus('current')
dpsTEXTRTUv2CMOMTime = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsTEXTRTUv2CMOMTime.setStatus('current')
dpsTEXTRTUv2CAction = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 5, 3, 4), RTUCAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsTEXTRTUv2CAction.setStatus('current')
dpsTEXTRTUv2AlarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 5, 100)).setObjects(("DPS-TEXT-RTU-MIB", "sysDescr"), ("DPS-TEXT-RTU-MIB", "sysLocation"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2DateTime"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2DeviceType"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2Phone"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2ADisplay"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2APoint"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2APntDesc"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2AState"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUAnalogvalue"))
if mibBuilder.loadTexts: dpsTEXTRTUv2AlarmSet.setStatus('current')
dpsTEXTRTUv2AlarmClear = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 5, 200)).setObjects(("DPS-TEXT-RTU-MIB", "sysDescr"), ("DPS-TEXT-RTU-MIB", "sysLocation"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2DateTime"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2DeviceType"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2Phone"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2ADisplay"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2APoint"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2APntDesc"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2AState"), ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUAnalogvalue"))
if mibBuilder.loadTexts: dpsTEXTRTUv2AlarmClear.setStatus('current')
mibBuilder.exportSymbols("DPS-TEXT-RTU-MIB", dpsTEXTRTUv2=dpsTEXTRTUv2, dpsTEXTRTUv2DeviceType=dpsTEXTRTUv2DeviceType, dpsTEXTRTUv2AlarmGrid=dpsTEXTRTUv2AlarmGrid, dpsTEXTRTUv2DateTime=dpsTEXTRTUv2DateTime, dpsTEXTRTUv2CMOMTime=dpsTEXTRTUv2CMOMTime, dpsTEXTRTUv2APntDesc=dpsTEXTRTUv2APntDesc, RTUCAction=RTUCAction, dpsTEXTRTUv2CDisplay=dpsTEXTRTUv2CDisplay, dpsTEXTRTUv2AState=dpsTEXTRTUv2AState, dpsTEXTRTUv2ControlGrid=dpsTEXTRTUv2ControlGrid, dpsTEXTRTUv2CPoint=dpsTEXTRTUv2CPoint, dpsTEXTRTUv2AlarmSet=dpsTEXTRTUv2AlarmSet, dpsTEXTRTUAnalogvalue=dpsTEXTRTUAnalogvalue, dpsTEXTRTUAnalogthresholds=dpsTEXTRTUAnalogthresholds, dpsTEXTRTUv2APoint=dpsTEXTRTUv2APoint, dpsTEXTRTUv2AlarmClear=dpsTEXTRTUv2AlarmClear, dpsTEXTRTUv2ADisplay=dpsTEXTRTUv2ADisplay, dpsTEXTRTUv2Ident=dpsTEXTRTUv2Ident, AnalogThresholds=AnalogThresholds, dpsTEXTRTUv2Phone=dpsTEXTRTUv2Phone, dpsTEXTRTUv2CAction=dpsTEXTRTUv2CAction)
