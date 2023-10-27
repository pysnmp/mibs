#
# PySNMP MIB module SCTE-HMS-HEADENDIDENT-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/scte/SCTE-HMS-HEADENDIDENT-TC-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 06:54:45 2023
# On host fv-az550-936 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, ModuleIdentity, enterprises, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, TimeTicks, iso, Counter64, Integer32, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "ModuleIdentity", "enterprises", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "TimeTicks", "iso", "Counter64", "Integer32", "ObjectIdentity", "Counter32")
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

mibBuilder.exportSymbols("SCTE-HMS-HEADENDIDENT-TC-MIB", HeDigitalAlarmType=HeDigitalAlarmType, HeAlarmControl=HeAlarmControl, MpegErrorStatus=MpegErrorStatus, HeOnOffControl=HeOnOffControl, QAMChannelInterleaveMode=QAMChannelInterleaveMode, HeTenthCentigrade=HeTenthCentigrade, HeMilliAmp=HeMilliAmp, QAMChannelModulationFormat=QAMChannelModulationFormat, HeHundredthNanoMeter=HeHundredthNanoMeter, PYSNMP_MODULE_ID=hmsTextualConventionMIB, VideoInputFrameRateType=VideoInputFrameRateType, ProgDataType=ProgDataType, HeDigitalAlarmSeverity=HeDigitalAlarmSeverity, HeTenthdBmV=HeTenthdBmV, HeTenthVolt=HeTenthVolt, HeTrapRegenerate=HeTrapRegenerate, HeClockSource=HeClockSource, HeTenthdBm=HeTenthdBm, HeFaultStatus=HeFaultStatus, HeTenthdB=HeTenthdB, DeviceEnableDisableValues=DeviceEnableDisableValues, HeHundredthWatts=HeHundredthWatts, HePIDValue=HePIDValue, HeOnOffStatus=HeOnOffStatus, hmsTextualConventionMIB=hmsTextualConventionMIB, HeResetValue=HeResetValue)
