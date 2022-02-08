#
# PySNMP MIB module MDS-IF-LN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-IF-LN-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 22:32:10 2022
# On host fv-az36-646 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mdsInterfaces, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsInterfaces")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Integer32, Counter32, MibIdentifier, ObjectIdentity, TimeTicks, Gauge32, Unsigned32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Integer32", "Counter32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Gauge32", "Unsigned32", "NotificationType", "ModuleIdentity")
DisplayString, TruthValue, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "TextualConvention")
mdsIfLnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5))
mdsIfLnMIB.setRevisions(('2018-05-16 00:00', '2017-11-15 00:00', '2016-09-21 00:00', '2015-09-14 00:00', '2015-09-09 00:00', '2015-08-21 00:00', '2015-08-03 00:00', '2015-06-03 00:00',))
if mibBuilder.loadTexts: mdsIfLnMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsIfLnMIB.setOrganization('GE MDS LLC http://www.gemds.com')
mIfLnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1))
mIfLnConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 1))
mIfLnStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2))
class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class LinkStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("initializing", 0), ("scanning", 1), ("negotiating", 2), ("authenticating", 3), ("associated", 4), ("disassociated", 5))

class InitStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("off", 0), ("initializing", 1), ("discovering", 2), ("reprogramming", 3), ("configuring", 4), ("complete", 5), ("error", 6))

class DeviceModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("remote", 0), ("accessPoint", 1), ("storeAndForward", 2), ("test", 3))

class ModulationModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 4, 16, 32, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73))
    namedValues = NamedValues(("unknown", 0), ("qpsk", 4), ("qam16", 16), ("qam32", 32), ("qam64", 64), ("fsk9600", 65), ("fsk9600m", 66), ("fsk19200", 67), ("fsk19200m", 68), ("fsk3200", 69), ("fsk19200e", 70), ("fsk19200n", 71), ("fsk38400n", 72), ("fsk38400e", 73))

class ModulationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("qpsk", 0), ("qam16", 1), ("qam64", 2), ("automatic", 3))

class SerialModulationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 5))
    namedValues = NamedValues(("fsk9600", 3), ("fsk9600m", 4), ("fsk19200", 5))

class AlarmFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("notCalibrated", 23), ("temperature", 0))

class FirmwareRevision(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'

class InetIpAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class FrequencyType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class ChannelType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class FecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("adaptiveGain", 1), ("lowGain", 2))

class RateType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

mIfLnStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1), )
if mibBuilder.loadTexts: mIfLnStatusTable.setStatus('current')
mIfLnStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mIfLnStatusEntry.setStatus('current')
mIfLnLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 1), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnLinkStatus.setStatus('current')
mIfLnInitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 2), InitStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnInitStatus.setStatus('current')
mIfLnCurrentDeviceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 3), DeviceModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnCurrentDeviceMode.setStatus('current')
mIfLnAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 4), AlarmFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnAlarms.setStatus('current')
mIfLnSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnSerialNumber.setStatus('current')
mIfLnFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 6), FirmwareRevision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnFirmwareRevision.setStatus('current')
mIfLnHardwareId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 7), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnHardwareId.setStatus('current')
mIfLnHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 8), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnHardwareRevision.setStatus('current')
mIfLnTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnTemperature.setStatus('current')
mIfLnApInfoApAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoApAddress.setStatus('current')
mIfLnApInfoIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 11), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoIpAddress.setStatus('current')
mIfLnApInfoConnectedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoConnectedTime.setStatus('current')
mIfLnApInfoRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoRssi.setStatus('current')
mIfLnApInfoEvm = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoEvm.setStatus('current')
mIfLnApInfoMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 15), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoMod.setStatus('current')
mIfLnMacStatsTxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnMacStatsTxSuccess.setStatus('current')
mIfLnMacStatsTxQueueFull = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnMacStatsTxQueueFull.setStatus('current')
mIfLnMacStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnMacStatsTxError.setStatus('current')
mIfLnMacStatsTxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnMacStatsTxRetry.setStatus('current')
mIfLnMacStatsRxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnMacStatsRxSuccess.setStatus('current')
mIfLnModemStatsTxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnModemStatsTxSuccess.setStatus('current')
mIfLnModemStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnModemStatsTxError.setStatus('current')
mIfLnModemStatsRxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnModemStatsRxSuccess.setStatus('current')
mIfLnModemStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnModemStatsRxError.setStatus('current')
mIfLnActiveTxFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 25), FrequencyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveTxFrequency.setStatus('current')
mIfLnActiveRxFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 26), FrequencyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveRxFrequency.setStatus('current')
mIfLnActiveChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 27), ChannelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveChannel.setStatus('current')
mIfLnActiveModulation = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 28), ModulationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveModulation.setStatus('current')
mIfLnActiveFec = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 29), FecType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveFec.setStatus('current')
mIfLnLastRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnLastRssi.setStatus('current')
mIfLnLastEvm = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 31), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnLastEvm.setStatus('current')
mIfLnLastMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 32), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnLastMod.setStatus('current')
mIfLnLastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 33), RateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnLastRate.setStatus('current')
mIfLnActiveNic = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 34), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveNic.setStatus('current')
mIfLnStatusConnRemTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2), )
if mibBuilder.loadTexts: mIfLnStatusConnRemTable.setStatus('current')
mIfLnStatusConnRemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-LN-MIB", "mIfLnStatusConnRemAddress"))
if mibBuilder.loadTexts: mIfLnStatusConnRemEntry.setStatus('current')
mIfLnStatusConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemAddress.setStatus('current')
mIfLnStatusConnRemIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemIpAddress.setStatus('current')
mIfLnStatusConnRemTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemTimeToLive.setStatus('current')
mIfLnStatusConnRemLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 4), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemLinkStatus.setStatus('current')
mIfLnStatusConnRemNicId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 5), UnsignedShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemNicId.setStatus('current')
mIfLnStatusConnRemRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemRssi.setStatus('current')
mIfLnStatusConnRemEvm = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemEvm.setStatus('current')
mIfLnStatusConnRemMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 8), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemMod.setStatus('current')
mIfLnStatusConnRemStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxPackets.setStatus('current')
mIfLnStatusConnRemStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxBytes.setStatus('current')
mIfLnStatusConnRemStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxPackets.setStatus('current')
mIfLnStatusConnRemStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxBytes.setStatus('current')
mIfLnStatusConnRemStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxError.setStatus('current')
mIfLnStatusConnRemStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxError.setStatus('current')
mIfLnStatusConnRemStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxDrop.setStatus('current')
mIfLnStatusConnRemStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxDrop.setStatus('current')
mIfLnStatusConnRemStatsGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 17), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsGateway.setStatus('current')
mIfLnStatusConnRemStatsAllIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsAllIp.setStatus('current')
mIfLnStatusConnRemStatsName = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsName.setStatus('current')
mIfLnStatusConnRemStatsAlarmed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsAlarmed.setStatus('current')
mIfLnStatusConnRemStatsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 21), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsVersion.setStatus('current')
mIfLnStatusConnRemStatsTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTemp.setStatus('current')
mIfLnStatusConnRemStatsDwnRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsDwnRssi.setStatus('current')
mIfLnStatusConnRemStatsDwnEvm = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsDwnEvm.setStatus('current')
mIfLnStatusConnRemStatsDwnMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 25), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsDwnMod.setStatus('current')
mIfLnStatusEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3), )
if mibBuilder.loadTexts: mIfLnStatusEndpointTable.setStatus('current')
mIfLnStatusEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-LN-MIB", "mIfLnStatusEndpointAddress"))
if mibBuilder.loadTexts: mIfLnStatusEndpointEntry.setStatus('current')
mIfLnStatusEndpointAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointAddress.setStatus('current')
mIfLnStatusEndpointIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointIpAddress.setStatus('current')
mIfLnStatusEndpointTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointTimeToLive.setStatus('current')
mIfLnStatusEndpointRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointRemAddress.setStatus('current')
mIfLnStatusEndpointStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxPackets.setStatus('current')
mIfLnStatusEndpointStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxBytes.setStatus('current')
mIfLnStatusEndpointStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxPackets.setStatus('current')
mIfLnStatusEndpointStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxBytes.setStatus('current')
mIfLnStatusEndpointStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxError.setStatus('current')
mIfLnStatusEndpointStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxError.setStatus('current')
mIfLnStatusEndpointStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxDrop.setStatus('current')
mIfLnStatusEndpointStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxDrop.setStatus('current')
mdsIfLnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3))
mdsIfLnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 1))
mdsIfLnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2))
mIfLnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 1, 1)).setObjects(("MDS-IF-LN-MIB", "mIfLnStatusGroup"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemGroup"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLnCompliance = mIfLnCompliance.setStatus('current')
mIfLnStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2, 1)).setObjects(("MDS-IF-LN-MIB", "mIfLnLinkStatus"), ("MDS-IF-LN-MIB", "mIfLnInitStatus"), ("MDS-IF-LN-MIB", "mIfLnCurrentDeviceMode"), ("MDS-IF-LN-MIB", "mIfLnAlarms"), ("MDS-IF-LN-MIB", "mIfLnSerialNumber"), ("MDS-IF-LN-MIB", "mIfLnFirmwareRevision"), ("MDS-IF-LN-MIB", "mIfLnHardwareId"), ("MDS-IF-LN-MIB", "mIfLnHardwareRevision"), ("MDS-IF-LN-MIB", "mIfLnTemperature"), ("MDS-IF-LN-MIB", "mIfLnApInfoApAddress"), ("MDS-IF-LN-MIB", "mIfLnApInfoIpAddress"), ("MDS-IF-LN-MIB", "mIfLnApInfoConnectedTime"), ("MDS-IF-LN-MIB", "mIfLnApInfoRssi"), ("MDS-IF-LN-MIB", "mIfLnApInfoEvm"), ("MDS-IF-LN-MIB", "mIfLnApInfoMod"), ("MDS-IF-LN-MIB", "mIfLnMacStatsTxSuccess"), ("MDS-IF-LN-MIB", "mIfLnMacStatsTxQueueFull"), ("MDS-IF-LN-MIB", "mIfLnMacStatsTxError"), ("MDS-IF-LN-MIB", "mIfLnMacStatsTxRetry"), ("MDS-IF-LN-MIB", "mIfLnMacStatsRxSuccess"), ("MDS-IF-LN-MIB", "mIfLnModemStatsTxSuccess"), ("MDS-IF-LN-MIB", "mIfLnModemStatsTxError"), ("MDS-IF-LN-MIB", "mIfLnModemStatsRxSuccess"), ("MDS-IF-LN-MIB", "mIfLnModemStatsRxError"), ("MDS-IF-LN-MIB", "mIfLnActiveTxFrequency"), ("MDS-IF-LN-MIB", "mIfLnActiveRxFrequency"), ("MDS-IF-LN-MIB", "mIfLnActiveChannel"), ("MDS-IF-LN-MIB", "mIfLnActiveModulation"), ("MDS-IF-LN-MIB", "mIfLnActiveFec"), ("MDS-IF-LN-MIB", "mIfLnLastRssi"), ("MDS-IF-LN-MIB", "mIfLnLastEvm"), ("MDS-IF-LN-MIB", "mIfLnLastMod"), ("MDS-IF-LN-MIB", "mIfLnLastRate"), ("MDS-IF-LN-MIB", "mIfLnActiveNic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLnStatusGroup = mIfLnStatusGroup.setStatus('current')
mIfLnStatusConnRemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2, 2)).setObjects(("MDS-IF-LN-MIB", "mIfLnStatusConnRemAddress"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemIpAddress"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemTimeToLive"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemLinkStatus"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemNicId"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemRssi"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemEvm"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemMod"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxPackets"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxBytes"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxPackets"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxBytes"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxError"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxError"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxDrop"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxDrop"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsGateway"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsAllIp"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsName"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsAlarmed"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsVersion"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTemp"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsDwnRssi"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsDwnEvm"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsDwnMod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLnStatusConnRemGroup = mIfLnStatusConnRemGroup.setStatus('current')
mIfLnStatusEndpointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2, 3)).setObjects(("MDS-IF-LN-MIB", "mIfLnStatusEndpointAddress"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointIpAddress"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointTimeToLive"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointRemAddress"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxPackets"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxBytes"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxPackets"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxBytes"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxError"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxError"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxDrop"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxDrop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLnStatusEndpointGroup = mIfLnStatusEndpointGroup.setStatus('current')
mibBuilder.exportSymbols("MDS-IF-LN-MIB", mIfLnStatusConnRemStatsRxBytes=mIfLnStatusConnRemStatsRxBytes, mIfLnModemStatsTxSuccess=mIfLnModemStatsTxSuccess, mIfLnActiveTxFrequency=mIfLnActiveTxFrequency, mIfLnCurrentDeviceMode=mIfLnCurrentDeviceMode, mIfLnFirmwareRevision=mIfLnFirmwareRevision, mIfLnHardwareId=mIfLnHardwareId, RateType=RateType, mIfLnStatusConnRemStatsTemp=mIfLnStatusConnRemStatsTemp, LinkStatus=LinkStatus, mIfLnStatusConnRemTable=mIfLnStatusConnRemTable, mIfLnStatusConnRemStatsAllIp=mIfLnStatusConnRemStatsAllIp, mIfLnHardwareRevision=mIfLnHardwareRevision, mIfLnStatusEndpointStatsTxBytes=mIfLnStatusEndpointStatsTxBytes, mIfLnMacStatsRxSuccess=mIfLnMacStatsRxSuccess, mIfLnStatusConnRemStatsTxError=mIfLnStatusConnRemStatsTxError, mIfLnStatusConnRemStatsTxBytes=mIfLnStatusConnRemStatsTxBytes, mIfLnStatusEndpointStatsTxDrop=mIfLnStatusEndpointStatsTxDrop, ModulationType=ModulationType, UnsignedByte=UnsignedByte, mIfLnTemperature=mIfLnTemperature, mIfLnActiveRxFrequency=mIfLnActiveRxFrequency, mIfLnStatusTable=mIfLnStatusTable, mIfLnMacStatsTxRetry=mIfLnMacStatsTxRetry, FecType=FecType, mdsIfLnMIBCompliances=mdsIfLnMIBCompliances, mIfLnStatusEndpointStatsRxError=mIfLnStatusEndpointStatsRxError, mIfLnStatusConnRemStatsVersion=mIfLnStatusConnRemStatsVersion, mIfLnStatusEndpointStatsTxError=mIfLnStatusEndpointStatsTxError, mIfLnStatusConnRemEvm=mIfLnStatusConnRemEvm, mIfLnLastRssi=mIfLnLastRssi, mIfLnApInfoApAddress=mIfLnApInfoApAddress, mIfLnStatusEndpointEntry=mIfLnStatusEndpointEntry, mIfLnActiveModulation=mIfLnActiveModulation, mIfLnLastEvm=mIfLnLastEvm, mIfLnMacStatsTxError=mIfLnMacStatsTxError, mIfLnStatusEndpointIpAddress=mIfLnStatusEndpointIpAddress, mIfLnStatusEndpointStatsRxPackets=mIfLnStatusEndpointStatsRxPackets, mIfLnStatusGroup=mIfLnStatusGroup, mIfLnStatusEndpointTimeToLive=mIfLnStatusEndpointTimeToLive, mdsIfLnMIBConformance=mdsIfLnMIBConformance, mIfLnMacStatsTxQueueFull=mIfLnMacStatsTxQueueFull, mIfLnModemStatsRxError=mIfLnModemStatsRxError, ChannelType=ChannelType, mIfLnModemStatsRxSuccess=mIfLnModemStatsRxSuccess, mIfLnActiveFec=mIfLnActiveFec, mIfLnConfig=mIfLnConfig, mIfLnStatusConnRemEntry=mIfLnStatusConnRemEntry, mIfLnActiveChannel=mIfLnActiveChannel, InetIpAddress=InetIpAddress, mIfLnStatusConnRemMod=mIfLnStatusConnRemMod, mIfLnStatusConnRemStatsRxPackets=mIfLnStatusConnRemStatsRxPackets, UnsignedShort=UnsignedShort, mIfLnStatusConnRemIpAddress=mIfLnStatusConnRemIpAddress, mIfLnLastMod=mIfLnLastMod, mIfLnStatusEndpointAddress=mIfLnStatusEndpointAddress, InitStatus=InitStatus, mIfLnLinkStatus=mIfLnLinkStatus, mIfLnStatusConnRemStatsRxDrop=mIfLnStatusConnRemStatsRxDrop, mIfLnStatusConnRemStatsGateway=mIfLnStatusConnRemStatsGateway, mIfLnStatusConnRemLinkStatus=mIfLnStatusConnRemLinkStatus, mIfLnInitStatus=mIfLnInitStatus, FrequencyType=FrequencyType, mIfLnStatusConnRemStatsDwnEvm=mIfLnStatusConnRemStatsDwnEvm, mIfLnMIBObjects=mIfLnMIBObjects, mIfLnStatusConnRemStatsTxDrop=mIfLnStatusConnRemStatsTxDrop, mIfLnApInfoRssi=mIfLnApInfoRssi, mIfLnStatusEndpointGroup=mIfLnStatusEndpointGroup, mIfLnStatus=mIfLnStatus, mIfLnApInfoEvm=mIfLnApInfoEvm, mdsIfLnMIBGroups=mdsIfLnMIBGroups, mIfLnStatusConnRemNicId=mIfLnStatusConnRemNicId, SerialModulationType=SerialModulationType, mIfLnStatusConnRemStatsName=mIfLnStatusConnRemStatsName, mIfLnStatusConnRemStatsAlarmed=mIfLnStatusConnRemStatsAlarmed, mIfLnStatusEndpointStatsRxBytes=mIfLnStatusEndpointStatsRxBytes, mIfLnStatusConnRemTimeToLive=mIfLnStatusConnRemTimeToLive, mIfLnApInfoMod=mIfLnApInfoMod, mIfLnStatusEndpointStatsTxPackets=mIfLnStatusEndpointStatsTxPackets, mIfLnStatusConnRemStatsTxPackets=mIfLnStatusConnRemStatsTxPackets, mIfLnCompliance=mIfLnCompliance, mIfLnModemStatsTxError=mIfLnModemStatsTxError, AlarmFlags=AlarmFlags, mIfLnApInfoIpAddress=mIfLnApInfoIpAddress, mIfLnStatusConnRemAddress=mIfLnStatusConnRemAddress, mIfLnStatusEndpointRemAddress=mIfLnStatusEndpointRemAddress, mIfLnActiveNic=mIfLnActiveNic, mIfLnStatusEntry=mIfLnStatusEntry, mIfLnStatusConnRemRssi=mIfLnStatusConnRemRssi, mIfLnAlarms=mIfLnAlarms, mIfLnLastRate=mIfLnLastRate, mIfLnStatusConnRemStatsDwnRssi=mIfLnStatusConnRemStatsDwnRssi, mIfLnStatusConnRemGroup=mIfLnStatusConnRemGroup, mIfLnApInfoConnectedTime=mIfLnApInfoConnectedTime, mIfLnStatusEndpointStatsRxDrop=mIfLnStatusEndpointStatsRxDrop, PYSNMP_MODULE_ID=mdsIfLnMIB, mIfLnSerialNumber=mIfLnSerialNumber, ModulationModeType=ModulationModeType, mIfLnStatusEndpointTable=mIfLnStatusEndpointTable, FirmwareRevision=FirmwareRevision, mIfLnStatusConnRemStatsDwnMod=mIfLnStatusConnRemStatsDwnMod, DeviceModeType=DeviceModeType, mIfLnMacStatsTxSuccess=mIfLnMacStatsTxSuccess, mIfLnStatusConnRemStatsRxError=mIfLnStatusConnRemStatsRxError, mdsIfLnMIB=mdsIfLnMIB)
