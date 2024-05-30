#
# PySNMP MIB module SCTE-HMS-HEADENDIDENT-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/scte/SCTE-HMS-HEADENDIDENT-TC-MIB
# Produced by pysmi-1.1.12 at Thu May 30 02:11:41 2024
# On host fv-az1567-87 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, enterprises, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Unsigned32, ModuleIdentity, NotificationType, MibIdentifier, Counter64, ObjectIdentity, Integer32, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Unsigned32", "ModuleIdentity", "NotificationType", "MibIdentifier", "Counter64", "ObjectIdentity", "Integer32", "Gauge32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hmsTextualConventionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 1))
hmsTextualConventionMIB.setRevisions(('2008-07-23 13:00', '2008-07-12 13:00', '2008-01-16 13:00', '2007-12-17 00:00',))
if mibBuilder.loadTexts: hmsTextualConventionMIB.setLastUpdated('200807231300Z')
if mibBuilder.loadTexts: hmsTextualConventionMIB.setOrganization('SCTE HMS Working Group')
class VideoInputFrameRateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("autoSelect", 2), ("f24Hz", 3), ("f25Hz", 4), ("f29Hz97", 5), ("f30Hz", 6), ("f29or30Hz", 7), ("f48Hz", 8), ("f50Hz", 9), ("f59Hz94", 10), ("f60Hz", 11), ("f59or60Hz", 12))

class QAMChannelModulationFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("qam64", 3), ("qam256", 4), ("qam128", 5), ("qam512", 6), ("qam1024", 7))

class QAMChannelInterleaveMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("fecI8J16", 3), ("fecI16J8", 4), ("fecI32J4", 5), ("fecI64J2", 6), ("fecI128J1", 7), ("fecI12J17", 8), ("fecI128J2", 9), ("fecI128J3", 10), ("fecI128J4", 11), ("fecI128J5", 12), ("fecI128J6", 13), ("fecI128J7", 14), ("fecI128J8", 15))

class ProgDataType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("video", 1), ("audio", 2), ("data", 3), ("other", 4))

class DeviceEnableDisableValues(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("notSupported", 3))

class MpegErrorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("good", 1), ("errors", 2), ("notSupported", 3))

class HePIDValue(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 8191), ValueRangeConstraint(65535, 65535), )
class HeClockSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("internal", 3), ("external", 4), ("ntp", 5), ("none", 6))

class HeResetValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("reset", 1), ("running", 2), ("resetting", 3))

class HeTenthVolt(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class HeTenthdBm(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class HeTenthdBmV(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class HeTenthCentigrade(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class HeHundredthNanoMeter(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-2'

class HeTenthdB(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class HeOnOffControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("on", 2), ("meaningless", 3))

class HeOnOffStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("off", 1), ("on", 2))

class HeAlarmControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("alarmEnabled", 1), ("alarmDisabled", 2))

class HeTrapRegenerate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("trapRegenerate", 1), ("trapNormal", 2))

class HeDigitalAlarmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("status", 5), ("clear", 6), ("information", 7))

class HeDigitalAlarmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("communication", 1), ("process", 2), ("session", 3), ("capacity", 4), ("maintenance", 5), ("provisioning", 6), ("programMgmt", 7), ("redundancy", 8), ("other", 9))

class HeFaultStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("fault", 2))

class HeMilliAmp(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-3'

class HeHundredthWatts(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-2'

mibBuilder.exportSymbols("SCTE-HMS-HEADENDIDENT-TC-MIB", HeTenthdBmV=HeTenthdBmV, QAMChannelModulationFormat=QAMChannelModulationFormat, HeDigitalAlarmSeverity=HeDigitalAlarmSeverity, HeTenthCentigrade=HeTenthCentigrade, HeAlarmControl=HeAlarmControl, HeResetValue=HeResetValue, HeFaultStatus=HeFaultStatus, HePIDValue=HePIDValue, HeHundredthNanoMeter=HeHundredthNanoMeter, HeTenthdBm=HeTenthdBm, HeOnOffStatus=HeOnOffStatus, HeDigitalAlarmType=HeDigitalAlarmType, PYSNMP_MODULE_ID=hmsTextualConventionMIB, MpegErrorStatus=MpegErrorStatus, HeOnOffControl=HeOnOffControl, ProgDataType=ProgDataType, VideoInputFrameRateType=VideoInputFrameRateType, hmsTextualConventionMIB=hmsTextualConventionMIB, HeTenthVolt=HeTenthVolt, HeTenthdB=HeTenthdB, HeClockSource=HeClockSource, HeHundredthWatts=HeHundredthWatts, HeMilliAmp=HeMilliAmp, QAMChannelInterleaveMode=QAMChannelInterleaveMode, DeviceEnableDisableValues=DeviceEnableDisableValues, HeTrapRegenerate=HeTrapRegenerate)
