#
# PySNMP MIB module MDS-IF-LN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-IF-LN-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:03:06 2024
# On host fv-az1433-299 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mdsInterfaces, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsInterfaces")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, iso, Gauge32, Unsigned32, Integer32, IpAddress, TimeTicks, Counter32, Bits, NotificationType, MibIdentifier, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Gauge32", "Unsigned32", "Integer32", "IpAddress", "TimeTicks", "Counter32", "Bits", "NotificationType", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "TextualConvention", "DisplayString")
mdsIfLnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5))
mdsIfLnMIB.setRevisions(('2018-05-16 00:00', '2017-11-15 00:00', '2016-09-21 00:00', '2015-09-14 00:00', '2015-09-09 00:00', '2015-08-21 00:00', '2015-08-03 00:00', '2015-06-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsIfLnMIB.setRevisionsDescriptions(('Updated conformance statments based on smilint.', 'Added ne FSK modems.', 'Added Error init status.', 'Fixed description of mIfLnActive* objects.', 'Fixed renaming of mIfLnCurrentModem to mIfLnCurrentDeviceMode.', 'Added active and last packet parameters.', 'Restructured some parameters.', 'Initial version.',))
if mibBuilder.loadTexts: mdsIfLnMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsIfLnMIB.setOrganization('GE MDS LLC\n      http://www.gemds.com')
if mibBuilder.loadTexts: mdsIfLnMIB.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n       T 585-242-9600\n       F 585-242-9620\n\n       175 Science Parkway\n       Rochester, New York 14620\n       USA')
if mibBuilder.loadTexts: mdsIfLnMIB.setDescription('The MIB module to describe the licenced narrowband interface.')
mIfLnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1))
mIfLnConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 1))
mIfLnStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2))
class UnsignedByte(TextualConvention, Unsigned32):
    description = 'xs:unsignedByte'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    description = 'xs:unsignedShort'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class LinkStatus(TextualConvention, Integer32):
    description = 'Link state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("initializing", 0), ("scanning", 1), ("negotiating", 2), ("authenticating", 3), ("associated", 4), ("disassociated", 5))

class InitStatus(TextualConvention, Integer32):
    description = 'State of the NIC Initialization.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("off", 0), ("initializing", 1), ("discovering", 2), ("reprogramming", 3), ("configuring", 4), ("complete", 5), ("error", 6))

class DeviceModeType(TextualConvention, Integer32):
    description = 'Device Mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("remote", 0), ("accessPoint", 1), ("storeAndForward", 2), ("test", 3))

class ModulationModeType(TextualConvention, Integer32):
    description = 'modulation'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 4, 16, 32, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73))
    namedValues = NamedValues(("unknown", 0), ("qpsk", 4), ("qam16", 16), ("qam32", 32), ("qam64", 64), ("fsk9600", 65), ("fsk9600m", 66), ("fsk19200", 67), ("fsk19200m", 68), ("fsk3200", 69), ("fsk19200e", 70), ("fsk19200n", 71), ("fsk38400n", 72), ("fsk38400e", 73))

class ModulationType(TextualConvention, Integer32):
    description = 'modulation'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("qpsk", 0), ("qam16", 1), ("qam64", 2), ("automatic", 3))

class SerialModulationType(TextualConvention, Integer32):
    description = 'modulation for serial'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 5))
    namedValues = NamedValues(("fsk9600", 3), ("fsk9600m", 4), ("fsk19200", 5))

class AlarmFlags(TextualConvention, Bits):
    description = 'Alarms'
    status = 'current'
    namedValues = NamedValues(("notCalibrated", 23), ("temperature", 0))

class FirmwareRevision(TextualConvention, OctetString):
    description = 'Firmware revision'
    status = 'current'
    displayHint = '32a'

class InetIpAddress(TextualConvention, OctetString):
    description = 'IP Address'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class FrequencyType(TextualConvention, OctetString):
    description = 'Frequency'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class ChannelType(TextualConvention, OctetString):
    description = 'Channel'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class FecType(TextualConvention, Integer32):
    description = 'Forward error corection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("adaptiveGain", 1), ("lowGain", 2))

class RateType(TextualConvention, OctetString):
    description = 'Rate'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

mIfLnStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1), )
if mibBuilder.loadTexts: mIfLnStatusTable.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusTable.setDescription('This table contains status of LN interfaces. This table has \n         a sparse dependent relationship on the ifTable. For each entry in \n         this table, there exists an entry in the ifTable.')
mIfLnStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mIfLnStatusEntry.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEntry.setDescription('Each entry contains status of a cellular interface.')
mIfLnLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 1), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnLinkStatus.setStatus('current')
if mibBuilder.loadTexts: mIfLnLinkStatus.setDescription('Link State.')
mIfLnInitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 2), InitStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnInitStatus.setStatus('current')
if mibBuilder.loadTexts: mIfLnInitStatus.setDescription('State of the NIC Initialization.')
mIfLnCurrentDeviceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 3), DeviceModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnCurrentDeviceMode.setStatus('current')
if mibBuilder.loadTexts: mIfLnCurrentDeviceMode.setDescription('The current device mode.')
mIfLnAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 4), AlarmFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnAlarms.setStatus('current')
if mibBuilder.loadTexts: mIfLnAlarms.setDescription('The current NIC alarms.')
mIfLnSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnSerialNumber.setStatus('current')
if mibBuilder.loadTexts: mIfLnSerialNumber.setDescription('Serial Number.')
mIfLnFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 6), FirmwareRevision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnFirmwareRevision.setStatus('current')
if mibBuilder.loadTexts: mIfLnFirmwareRevision.setDescription('NIC Firmware Revision.')
mIfLnHardwareId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 7), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnHardwareId.setStatus('current')
if mibBuilder.loadTexts: mIfLnHardwareId.setDescription('The Hardware ID.')
mIfLnHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 8), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnHardwareRevision.setStatus('current')
if mibBuilder.loadTexts: mIfLnHardwareRevision.setDescription('The Hardware Revision.')
mIfLnTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnTemperature.setStatus('current')
if mibBuilder.loadTexts: mIfLnTemperature.setDescription('The transceiver temperature.')
mIfLnApInfoApAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoApAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLnApInfoApAddress.setDescription('MAC address of access point this device is linked to.')
mIfLnApInfoIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 11), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoIpAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLnApInfoIpAddress.setDescription('IP address of access point this device is linked to.')
mIfLnApInfoConnectedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoConnectedTime.setStatus('current')
if mibBuilder.loadTexts: mIfLnApInfoConnectedTime.setDescription('Time elapsed since link established.')
mIfLnApInfoRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoRssi.setStatus('current')
if mibBuilder.loadTexts: mIfLnApInfoRssi.setDescription('Average received signal strength index.')
mIfLnApInfoEvm = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoEvm.setStatus('current')
if mibBuilder.loadTexts: mIfLnApInfoEvm.setDescription('Average error vector magnitude.')
mIfLnApInfoMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 15), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnApInfoMod.setStatus('current')
if mibBuilder.loadTexts: mIfLnApInfoMod.setDescription('Last modulation')
mIfLnMacStatsTxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnMacStatsTxSuccess.setStatus('current')
if mibBuilder.loadTexts: mIfLnMacStatsTxSuccess.setDescription('Successful transmissions.')
mIfLnMacStatsTxQueueFull = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnMacStatsTxQueueFull.setStatus('current')
if mibBuilder.loadTexts: mIfLnMacStatsTxQueueFull.setDescription('Failed transmissions, MAC queue full.')
mIfLnMacStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnMacStatsTxError.setStatus('current')
if mibBuilder.loadTexts: mIfLnMacStatsTxError.setDescription('Packets dropped for other reasons. Currently unused.')
mIfLnMacStatsTxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnMacStatsTxRetry.setStatus('current')
if mibBuilder.loadTexts: mIfLnMacStatsTxRetry.setDescription('Re-transmission count due to to previously unsuccessful transmission.')
mIfLnMacStatsRxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnMacStatsRxSuccess.setStatus('current')
if mibBuilder.loadTexts: mIfLnMacStatsRxSuccess.setDescription('Valid packet received.')
mIfLnModemStatsTxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnModemStatsTxSuccess.setStatus('current')
if mibBuilder.loadTexts: mIfLnModemStatsTxSuccess.setDescription('Modem successfully transmitted a packet')
mIfLnModemStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnModemStatsTxError.setStatus('current')
if mibBuilder.loadTexts: mIfLnModemStatsTxError.setDescription('Modem failed to transmit a packet')
mIfLnModemStatsRxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnModemStatsRxSuccess.setStatus('current')
if mibBuilder.loadTexts: mIfLnModemStatsRxSuccess.setDescription('Modem successfully received a packet')
mIfLnModemStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnModemStatsRxError.setStatus('current')
if mibBuilder.loadTexts: mIfLnModemStatsRxError.setDescription('Modem failed to receive a packet')
mIfLnActiveTxFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 25), FrequencyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveTxFrequency.setStatus('current')
if mibBuilder.loadTexts: mIfLnActiveTxFrequency.setDescription('The transmit frequency for the Radio')
mIfLnActiveRxFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 26), FrequencyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveRxFrequency.setStatus('current')
if mibBuilder.loadTexts: mIfLnActiveRxFrequency.setDescription('The recieve frequency for the Radio')
mIfLnActiveChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 27), ChannelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveChannel.setStatus('current')
if mibBuilder.loadTexts: mIfLnActiveChannel.setDescription('The active channel for the Radio')
mIfLnActiveModulation = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 28), ModulationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveModulation.setStatus('current')
if mibBuilder.loadTexts: mIfLnActiveModulation.setDescription('The active modulation for the Radio')
mIfLnActiveFec = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 29), FecType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveFec.setStatus('current')
if mibBuilder.loadTexts: mIfLnActiveFec.setDescription('The active Forward Error Correction (FEC) for the Radio')
mIfLnLastRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnLastRssi.setStatus('current')
if mibBuilder.loadTexts: mIfLnLastRssi.setDescription('Lasr received signal strength index.')
mIfLnLastEvm = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 31), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnLastEvm.setStatus('current')
if mibBuilder.loadTexts: mIfLnLastEvm.setDescription('Last error vector magnitude.')
mIfLnLastMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 32), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnLastMod.setStatus('current')
if mibBuilder.loadTexts: mIfLnLastMod.setDescription('Last modulation')
mIfLnLastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 33), RateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnLastRate.setStatus('current')
if mibBuilder.loadTexts: mIfLnLastRate.setDescription('Last rate in kbps')
mIfLnActiveNic = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 1, 1, 34), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnActiveNic.setStatus('current')
if mibBuilder.loadTexts: mIfLnActiveNic.setDescription('If the nic is active')
mIfLnStatusConnRemTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2), )
if mibBuilder.loadTexts: mIfLnStatusConnRemTable.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemTable.setDescription('The list of connected remotes.')
mIfLnStatusConnRemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-LN-MIB", "mIfLnStatusConnRemAddress"))
if mibBuilder.loadTexts: mIfLnStatusConnRemEntry.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemEntry.setDescription('The connected remote status entry.')
mIfLnStatusConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemAddress.setDescription('Address of connected remote.')
mIfLnStatusConnRemIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemIpAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemIpAddress.setDescription('Ip address of connected remote.')
mIfLnStatusConnRemTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemTimeToLive.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemTimeToLive.setDescription('Time left until this entry is aged out.')
mIfLnStatusConnRemLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 4), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemLinkStatus.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemLinkStatus.setDescription('The status of the connection to a remote device.')
mIfLnStatusConnRemNicId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 5), UnsignedShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemNicId.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemNicId.setDescription('The RF connection identifier for the connected remote device.')
mIfLnStatusConnRemRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemRssi.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemRssi.setDescription('received signal strength index.')
mIfLnStatusConnRemEvm = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemEvm.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemEvm.setDescription('link quality index.')
mIfLnStatusConnRemMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 8), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemMod.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemMod.setDescription('Last modulation')
mIfLnStatusConnRemStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxPackets.setDescription('tx packets')
mIfLnStatusConnRemStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxBytes.setDescription('tx bytes')
mIfLnStatusConnRemStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxPackets.setDescription('rx packets')
mIfLnStatusConnRemStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxBytes.setDescription('rx bytes')
mIfLnStatusConnRemStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxError.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxError.setDescription('tx error')
mIfLnStatusConnRemStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxError.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxError.setDescription('rx error')
mIfLnStatusConnRemStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTxDrop.setDescription('tx drop')
mIfLnStatusConnRemStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsRxDrop.setDescription('rx drop')
mIfLnStatusConnRemStatsGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 17), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsGateway.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsGateway.setDescription('The mac address of the next hop')
mIfLnStatusConnRemStatsAllIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsAllIp.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsAllIp.setDescription('String version of all IP addresses')
mIfLnStatusConnRemStatsName = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsName.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsName.setDescription('System name')
mIfLnStatusConnRemStatsAlarmed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsAlarmed.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsAlarmed.setDescription('Is alarmed')
mIfLnStatusConnRemStatsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 21), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsVersion.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsVersion.setDescription('Host firmware version')
mIfLnStatusConnRemStatsTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTemp.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsTemp.setDescription('System temprature in celsius')
mIfLnStatusConnRemStatsDwnRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsDwnRssi.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsDwnRssi.setDescription('Downstream RSSI')
mIfLnStatusConnRemStatsDwnEvm = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsDwnEvm.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsDwnEvm.setDescription('Downstream EVM')
mIfLnStatusConnRemStatsDwnMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 2, 1, 25), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsDwnMod.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemStatsDwnMod.setDescription('Downstream Modulation')
mIfLnStatusEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3), )
if mibBuilder.loadTexts: mIfLnStatusEndpointTable.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointTable.setDescription('The list of endpoints.')
mIfLnStatusEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-LN-MIB", "mIfLnStatusEndpointAddress"))
if mibBuilder.loadTexts: mIfLnStatusEndpointEntry.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointEntry.setDescription('The endpoint status entry.')
mIfLnStatusEndpointAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointAddress.setDescription('Address of endpoint.')
mIfLnStatusEndpointIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointIpAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointIpAddress.setDescription('Ip address of endpoint.')
mIfLnStatusEndpointTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointTimeToLive.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointTimeToLive.setDescription('Time left until this entry is aged out.')
mIfLnStatusEndpointRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointRemAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointRemAddress.setDescription('The MAC address of the remote device servicing this endpoint.')
mIfLnStatusEndpointStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxPackets.setDescription('tx packets')
mIfLnStatusEndpointStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxBytes.setDescription('tx bytes')
mIfLnStatusEndpointStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxPackets.setDescription('rx packets')
mIfLnStatusEndpointStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxBytes.setDescription('rx bytes')
mIfLnStatusEndpointStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxError.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxError.setDescription('tx error')
mIfLnStatusEndpointStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxError.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxError.setDescription('rx error')
mIfLnStatusEndpointStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsTxDrop.setDescription('tx drop')
mIfLnStatusEndpointStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 1, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointStatsRxDrop.setDescription('rx drop')
mdsIfLnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3))
mdsIfLnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 1))
mdsIfLnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2))
mIfLnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 1, 1)).setObjects(("MDS-IF-LN-MIB", "mIfLnStatusGroup"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemGroup"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLnCompliance = mIfLnCompliance.setStatus('current')
if mibBuilder.loadTexts: mIfLnCompliance.setDescription('The compliance statement for SNMP entities that \n            implement the MDS-IF-LN-MIB.')
mIfLnStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2, 1)).setObjects(("MDS-IF-LN-MIB", "mIfLnLinkStatus"), ("MDS-IF-LN-MIB", "mIfLnInitStatus"), ("MDS-IF-LN-MIB", "mIfLnCurrentDeviceMode"), ("MDS-IF-LN-MIB", "mIfLnAlarms"), ("MDS-IF-LN-MIB", "mIfLnSerialNumber"), ("MDS-IF-LN-MIB", "mIfLnFirmwareRevision"), ("MDS-IF-LN-MIB", "mIfLnHardwareId"), ("MDS-IF-LN-MIB", "mIfLnHardwareRevision"), ("MDS-IF-LN-MIB", "mIfLnTemperature"), ("MDS-IF-LN-MIB", "mIfLnApInfoApAddress"), ("MDS-IF-LN-MIB", "mIfLnApInfoIpAddress"), ("MDS-IF-LN-MIB", "mIfLnApInfoConnectedTime"), ("MDS-IF-LN-MIB", "mIfLnApInfoRssi"), ("MDS-IF-LN-MIB", "mIfLnApInfoEvm"), ("MDS-IF-LN-MIB", "mIfLnApInfoMod"), ("MDS-IF-LN-MIB", "mIfLnMacStatsTxSuccess"), ("MDS-IF-LN-MIB", "mIfLnMacStatsTxQueueFull"), ("MDS-IF-LN-MIB", "mIfLnMacStatsTxError"), ("MDS-IF-LN-MIB", "mIfLnMacStatsTxRetry"), ("MDS-IF-LN-MIB", "mIfLnMacStatsRxSuccess"), ("MDS-IF-LN-MIB", "mIfLnModemStatsTxSuccess"), ("MDS-IF-LN-MIB", "mIfLnModemStatsTxError"), ("MDS-IF-LN-MIB", "mIfLnModemStatsRxSuccess"), ("MDS-IF-LN-MIB", "mIfLnModemStatsRxError"), ("MDS-IF-LN-MIB", "mIfLnActiveTxFrequency"), ("MDS-IF-LN-MIB", "mIfLnActiveRxFrequency"), ("MDS-IF-LN-MIB", "mIfLnActiveChannel"), ("MDS-IF-LN-MIB", "mIfLnActiveModulation"), ("MDS-IF-LN-MIB", "mIfLnActiveFec"), ("MDS-IF-LN-MIB", "mIfLnLastRssi"), ("MDS-IF-LN-MIB", "mIfLnLastEvm"), ("MDS-IF-LN-MIB", "mIfLnLastMod"), ("MDS-IF-LN-MIB", "mIfLnLastRate"), ("MDS-IF-LN-MIB", "mIfLnActiveNic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLnStatusGroup = mIfLnStatusGroup.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusGroup.setDescription('A collection of objects providing information about\n        common LN interface status.')
mIfLnStatusConnRemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2, 2)).setObjects(("MDS-IF-LN-MIB", "mIfLnStatusConnRemAddress"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemIpAddress"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemTimeToLive"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemLinkStatus"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemNicId"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemRssi"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemEvm"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemMod"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxPackets"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxBytes"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxPackets"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxBytes"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxError"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxError"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTxDrop"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsRxDrop"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsGateway"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsAllIp"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsName"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsAlarmed"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsVersion"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsTemp"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsDwnRssi"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsDwnEvm"), ("MDS-IF-LN-MIB", "mIfLnStatusConnRemStatsDwnMod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLnStatusConnRemGroup = mIfLnStatusConnRemGroup.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusConnRemGroup.setDescription('A collection of objects providing information about\n        connected remotes status.')
mIfLnStatusEndpointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 5, 3, 2, 3)).setObjects(("MDS-IF-LN-MIB", "mIfLnStatusEndpointAddress"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointIpAddress"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointTimeToLive"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointRemAddress"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxPackets"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxBytes"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxPackets"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxBytes"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxError"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxError"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsTxDrop"), ("MDS-IF-LN-MIB", "mIfLnStatusEndpointStatsRxDrop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLnStatusEndpointGroup = mIfLnStatusEndpointGroup.setStatus('current')
if mibBuilder.loadTexts: mIfLnStatusEndpointGroup.setDescription('A collection of objects providing information about\n        endpoints status.')
mibBuilder.exportSymbols("MDS-IF-LN-MIB", mIfLnStatusConnRemGroup=mIfLnStatusConnRemGroup, mIfLnStatusEndpointStatsTxBytes=mIfLnStatusEndpointStatsTxBytes, mIfLnStatusEndpointStatsRxPackets=mIfLnStatusEndpointStatsRxPackets, mIfLnLastEvm=mIfLnLastEvm, mIfLnActiveNic=mIfLnActiveNic, mIfLnStatusEndpointStatsTxError=mIfLnStatusEndpointStatsTxError, mIfLnStatusEntry=mIfLnStatusEntry, DeviceModeType=DeviceModeType, mIfLnStatusConnRemStatsDwnRssi=mIfLnStatusConnRemStatsDwnRssi, mIfLnMacStatsRxSuccess=mIfLnMacStatsRxSuccess, mIfLnStatusGroup=mIfLnStatusGroup, mIfLnStatusConnRemTimeToLive=mIfLnStatusConnRemTimeToLive, mIfLnStatusConnRemStatsTxBytes=mIfLnStatusConnRemStatsTxBytes, mIfLnStatusConnRemStatsVersion=mIfLnStatusConnRemStatsVersion, mIfLnTemperature=mIfLnTemperature, PYSNMP_MODULE_ID=mdsIfLnMIB, mdsIfLnMIBGroups=mdsIfLnMIBGroups, SerialModulationType=SerialModulationType, mIfLnStatusConnRemStatsTxError=mIfLnStatusConnRemStatsTxError, mIfLnStatusEndpointEntry=mIfLnStatusEndpointEntry, mIfLnApInfoRssi=mIfLnApInfoRssi, mIfLnApInfoMod=mIfLnApInfoMod, mIfLnModemStatsRxError=mIfLnModemStatsRxError, mIfLnStatusConnRemStatsDwnEvm=mIfLnStatusConnRemStatsDwnEvm, mdsIfLnMIBCompliances=mdsIfLnMIBCompliances, mIfLnStatusConnRemStatsTemp=mIfLnStatusConnRemStatsTemp, mIfLnStatusConnRemAddress=mIfLnStatusConnRemAddress, FecType=FecType, mIfLnCompliance=mIfLnCompliance, mIfLnApInfoConnectedTime=mIfLnApInfoConnectedTime, mIfLnStatusConnRemTable=mIfLnStatusConnRemTable, mIfLnLastRate=mIfLnLastRate, mIfLnStatusConnRemLinkStatus=mIfLnStatusConnRemLinkStatus, mIfLnStatusConnRemStatsDwnMod=mIfLnStatusConnRemStatsDwnMod, mIfLnHardwareId=mIfLnHardwareId, InitStatus=InitStatus, mIfLnStatusConnRemStatsAllIp=mIfLnStatusConnRemStatsAllIp, ModulationModeType=ModulationModeType, mIfLnStatusEndpointStatsTxDrop=mIfLnStatusEndpointStatsTxDrop, mIfLnStatusEndpointGroup=mIfLnStatusEndpointGroup, mIfLnStatusConnRemStatsAlarmed=mIfLnStatusConnRemStatsAlarmed, mIfLnStatusEndpointIpAddress=mIfLnStatusEndpointIpAddress, mIfLnFirmwareRevision=mIfLnFirmwareRevision, RateType=RateType, mIfLnMacStatsTxError=mIfLnMacStatsTxError, mIfLnActiveFec=mIfLnActiveFec, LinkStatus=LinkStatus, mIfLnStatus=mIfLnStatus, mIfLnStatusEndpointStatsRxDrop=mIfLnStatusEndpointStatsRxDrop, mIfLnLastMod=mIfLnLastMod, mIfLnApInfoEvm=mIfLnApInfoEvm, mIfLnLinkStatus=mIfLnLinkStatus, mIfLnStatusEndpointTable=mIfLnStatusEndpointTable, FirmwareRevision=FirmwareRevision, mIfLnActiveChannel=mIfLnActiveChannel, mIfLnStatusEndpointTimeToLive=mIfLnStatusEndpointTimeToLive, mIfLnModemStatsTxSuccess=mIfLnModemStatsTxSuccess, InetIpAddress=InetIpAddress, mIfLnStatusConnRemNicId=mIfLnStatusConnRemNicId, FrequencyType=FrequencyType, mIfLnStatusEndpointRemAddress=mIfLnStatusEndpointRemAddress, AlarmFlags=AlarmFlags, mIfLnCurrentDeviceMode=mIfLnCurrentDeviceMode, mIfLnApInfoIpAddress=mIfLnApInfoIpAddress, mIfLnInitStatus=mIfLnInitStatus, mIfLnStatusConnRemStatsName=mIfLnStatusConnRemStatsName, mIfLnSerialNumber=mIfLnSerialNumber, mIfLnModemStatsRxSuccess=mIfLnModemStatsRxSuccess, ModulationType=ModulationType, UnsignedShort=UnsignedShort, mIfLnStatusConnRemStatsRxBytes=mIfLnStatusConnRemStatsRxBytes, mIfLnMIBObjects=mIfLnMIBObjects, mIfLnApInfoApAddress=mIfLnApInfoApAddress, mdsIfLnMIBConformance=mdsIfLnMIBConformance, mIfLnStatusConnRemRssi=mIfLnStatusConnRemRssi, mIfLnStatusConnRemStatsTxDrop=mIfLnStatusConnRemStatsTxDrop, mIfLnStatusEndpointStatsRxBytes=mIfLnStatusEndpointStatsRxBytes, mIfLnStatusConnRemStatsRxPackets=mIfLnStatusConnRemStatsRxPackets, mIfLnMacStatsTxSuccess=mIfLnMacStatsTxSuccess, mIfLnStatusTable=mIfLnStatusTable, mIfLnStatusConnRemStatsRxError=mIfLnStatusConnRemStatsRxError, mIfLnLastRssi=mIfLnLastRssi, mIfLnStatusEndpointStatsRxError=mIfLnStatusEndpointStatsRxError, mIfLnStatusConnRemStatsGateway=mIfLnStatusConnRemStatsGateway, mIfLnModemStatsTxError=mIfLnModemStatsTxError, mdsIfLnMIB=mdsIfLnMIB, mIfLnMacStatsTxQueueFull=mIfLnMacStatsTxQueueFull, mIfLnStatusConnRemStatsRxDrop=mIfLnStatusConnRemStatsRxDrop, mIfLnStatusConnRemMod=mIfLnStatusConnRemMod, mIfLnActiveRxFrequency=mIfLnActiveRxFrequency, mIfLnStatusConnRemEntry=mIfLnStatusConnRemEntry, mIfLnMacStatsTxRetry=mIfLnMacStatsTxRetry, mIfLnStatusConnRemIpAddress=mIfLnStatusConnRemIpAddress, mIfLnStatusEndpointAddress=mIfLnStatusEndpointAddress, mIfLnStatusConnRemStatsTxPackets=mIfLnStatusConnRemStatsTxPackets, mIfLnStatusEndpointStatsTxPackets=mIfLnStatusEndpointStatsTxPackets, mIfLnActiveTxFrequency=mIfLnActiveTxFrequency, mIfLnConfig=mIfLnConfig, ChannelType=ChannelType, mIfLnHardwareRevision=mIfLnHardwareRevision, mIfLnAlarms=mIfLnAlarms, mIfLnActiveModulation=mIfLnActiveModulation, mIfLnStatusConnRemEvm=mIfLnStatusConnRemEvm, UnsignedByte=UnsignedByte)
