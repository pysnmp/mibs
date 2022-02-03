#
# PySNMP MIB module MDS-IF-LW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-IF-LW-MIB
# Produced by pysmi-1.1.8 at Thu Feb  3 21:05:30 2022
# On host fv-az36-616 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mdsInterfaces, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsInterfaces")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Gauge32, Integer32, Bits, TimeTicks, Counter64, MibIdentifier, NotificationType, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "Integer32", "Bits", "TimeTicks", "Counter64", "MibIdentifier", "NotificationType", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Unsigned32")
TextualConvention, TruthValue, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "MacAddress", "DisplayString")
mdsIfLwMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6))
mdsIfLwMIB.setRevisions(('2018-09-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsIfLwMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: mdsIfLwMIB.setLastUpdated('201809130000Z')
if mibBuilder.loadTexts: mdsIfLwMIB.setOrganization('GE MDS LLC\n      http://www.gemds.com')
if mibBuilder.loadTexts: mdsIfLwMIB.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n       T 585-242-9600\n       F 585-242-9620\n\n       175 Science Parkway\n       Rochester, New York 14620\n       USA')
if mibBuilder.loadTexts: mdsIfLwMIB.setDescription('The MIB module to describe the licenced narrowband interface.')
mIfLwMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1))
mIfLwConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 1))
mIfLwStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2))
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
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))
    namedValues = NamedValues(("qpsk25", 2), ("qpsk50", 3), ("qpsk75", 4), ("qam16r50", 5), ("qam16r75", 6))

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

mIfLwStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1), )
if mibBuilder.loadTexts: mIfLwStatusTable.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusTable.setDescription('This table contains status of LW interfaces. This table has \n         a sparse dependent relationship on the ifTable. For each entry in \n         this table, there exists an entry in the ifTable.')
mIfLwStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mIfLwStatusEntry.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEntry.setDescription('Each entry contains status of a cellular interface.')
mIfLwLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 1), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwLinkStatus.setStatus('current')
if mibBuilder.loadTexts: mIfLwLinkStatus.setDescription('Link State.')
mIfLwInitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 2), InitStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwInitStatus.setStatus('current')
if mibBuilder.loadTexts: mIfLwInitStatus.setDescription('State of the NIC Initialization.')
mIfLwCurrentDeviceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 3), DeviceModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwCurrentDeviceMode.setStatus('current')
if mibBuilder.loadTexts: mIfLwCurrentDeviceMode.setDescription('The current device mode.')
mIfLwAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 4), AlarmFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwAlarms.setStatus('current')
if mibBuilder.loadTexts: mIfLwAlarms.setDescription('The current NIC alarms.')
mIfLwSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwSerialNumber.setStatus('current')
if mibBuilder.loadTexts: mIfLwSerialNumber.setDescription('Serial Number.')
mIfLwFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 6), FirmwareRevision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwFirmwareRevision.setStatus('current')
if mibBuilder.loadTexts: mIfLwFirmwareRevision.setDescription('NIC Firmware Revision.')
mIfLwHardwareId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 7), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwHardwareId.setStatus('current')
if mibBuilder.loadTexts: mIfLwHardwareId.setDescription('The Hardware ID.')
mIfLwHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 8), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwHardwareRevision.setStatus('current')
if mibBuilder.loadTexts: mIfLwHardwareRevision.setDescription('The Hardware Revision.')
mIfLwTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwTemperature.setStatus('current')
if mibBuilder.loadTexts: mIfLwTemperature.setDescription('The transceiver temperature.')
mIfLwApInfoApAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoApAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLwApInfoApAddress.setDescription('MAC address of access point this device is linked to.')
mIfLwApInfoIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 11), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoIpAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLwApInfoIpAddress.setDescription('IP address of access point this device is linked to.')
mIfLwApInfoConnectedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoConnectedTime.setStatus('current')
if mibBuilder.loadTexts: mIfLwApInfoConnectedTime.setDescription('Time elapsed since link established.')
mIfLwApInfoRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoRssi.setStatus('current')
if mibBuilder.loadTexts: mIfLwApInfoRssi.setDescription('Average received signal strength index.')
mIfLwApInfoSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoSnr.setStatus('current')
if mibBuilder.loadTexts: mIfLwApInfoSnr.setDescription('Average error vector magnitude.')
mIfLwApInfoMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 15), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoMod.setStatus('current')
if mibBuilder.loadTexts: mIfLwApInfoMod.setDescription('Last modulation')
mIfLwMacStatsTxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsTxSuccess.setStatus('current')
if mibBuilder.loadTexts: mIfLwMacStatsTxSuccess.setDescription('Successful transmissions.')
mIfLwMacStatsTxQueueFull = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsTxQueueFull.setStatus('current')
if mibBuilder.loadTexts: mIfLwMacStatsTxQueueFull.setDescription('Failed transmissions, MAC queue full.')
mIfLwMacStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsTxError.setStatus('current')
if mibBuilder.loadTexts: mIfLwMacStatsTxError.setDescription('Packets dropped for other reasons. Currently unused.')
mIfLwMacStatsTxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsTxRetry.setStatus('current')
if mibBuilder.loadTexts: mIfLwMacStatsTxRetry.setDescription('Re-transmission count due to to previously unsuccessful transmission.')
mIfLwMacStatsRxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsRxSuccess.setStatus('current')
if mibBuilder.loadTexts: mIfLwMacStatsRxSuccess.setDescription('Valid packet received.')
mIfLwMacStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsRxError.setStatus('current')
if mibBuilder.loadTexts: mIfLwMacStatsRxError.setDescription('Valid packet received.')
mIfLwModemStatsTxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwModemStatsTxSuccess.setStatus('current')
if mibBuilder.loadTexts: mIfLwModemStatsTxSuccess.setDescription('Modem successfully transmitted a packet')
mIfLwModemStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwModemStatsTxError.setStatus('current')
if mibBuilder.loadTexts: mIfLwModemStatsTxError.setDescription('Modem failed to transmit a packet')
mIfLwModemStatsRxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwModemStatsRxSuccess.setStatus('current')
if mibBuilder.loadTexts: mIfLwModemStatsRxSuccess.setDescription('Modem successfully received a packet')
mIfLwModemStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 25), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwModemStatsRxError.setStatus('current')
if mibBuilder.loadTexts: mIfLwModemStatsRxError.setDescription('Modem failed to receive a packet')
mIfLwLastRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwLastRssi.setStatus('current')
if mibBuilder.loadTexts: mIfLwLastRssi.setDescription('Lasr received signal strength index.')
mIfLwLastSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 27), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwLastSnr.setStatus('current')
if mibBuilder.loadTexts: mIfLwLastSnr.setDescription('Last error vector magnitude.')
mIfLwLastMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 28), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwLastMod.setStatus('current')
if mibBuilder.loadTexts: mIfLwLastMod.setDescription('Last modulation')
mIfLwLastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 29), RateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwLastRate.setStatus('current')
if mibBuilder.loadTexts: mIfLwLastRate.setDescription('Last rate in kbps')
mIfLwActiveNic = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 30), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwActiveNic.setStatus('current')
if mibBuilder.loadTexts: mIfLwActiveNic.setDescription('If nic is active')
mIfLwStatusConnRemTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2), )
if mibBuilder.loadTexts: mIfLwStatusConnRemTable.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemTable.setDescription('The list of connected remotes.')
mIfLwStatusConnRemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-LW-MIB", "mIfLwStatusConnRemAddress"))
if mibBuilder.loadTexts: mIfLwStatusConnRemEntry.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemEntry.setDescription('The connected remote status entry.')
mIfLwStatusConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemAddress.setDescription('Address of connected remote.')
mIfLwStatusConnRemIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemIpAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemIpAddress.setDescription('Ip address of connected remote.')
mIfLwStatusConnRemTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemTimeToLive.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemTimeToLive.setDescription('Time left until this entry is aged out.')
mIfLwStatusConnRemLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 4), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemLinkStatus.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemLinkStatus.setDescription('The status of the connection to a remote device.')
mIfLwStatusConnRemNicId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 5), UnsignedShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemNicId.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemNicId.setDescription('The RF connection identifier for the connected remote device.')
mIfLwStatusConnRemRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemRssi.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemRssi.setDescription('received signal strength index.')
mIfLwStatusConnRemSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemSnr.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemSnr.setDescription('link quality index.')
mIfLwStatusConnRemMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 8), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemMod.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemMod.setDescription('Last modulation')
mIfLwStatusConnRemStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxPackets.setDescription('tx packets')
mIfLwStatusConnRemStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxBytes.setDescription('tx bytes')
mIfLwStatusConnRemStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxPackets.setDescription('rx packets')
mIfLwStatusConnRemStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxBytes.setDescription('rx bytes')
mIfLwStatusConnRemStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxError.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxError.setDescription('tx error')
mIfLwStatusConnRemStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxError.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxError.setDescription('rx error')
mIfLwStatusConnRemStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxDrop.setDescription('tx drop')
mIfLwStatusConnRemStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxDrop.setDescription('rx drop')
mIfLwStatusConnRemStatsGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 17), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsGateway.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsGateway.setDescription('The mac address of the next hop')
mIfLwStatusConnRemStatsAllIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsAllIp.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsAllIp.setDescription('String version of all IP addresses')
mIfLwStatusConnRemStatsName = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsName.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsName.setDescription('System name')
mIfLwStatusConnRemStatsAlarmed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsAlarmed.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsAlarmed.setDescription('Is alarmed')
mIfLwStatusConnRemStatsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 21), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsVersion.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsVersion.setDescription('Host firmware version')
mIfLwStatusConnRemStatsTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTemp.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTemp.setDescription('System temprature in celsius')
mIfLwStatusConnRemStatsDwnRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsDwnRssi.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsDwnRssi.setDescription('Downstream RSSI')
mIfLwStatusConnRemStatsDwnSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsDwnSnr.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsDwnSnr.setDescription('Downstream SNR')
mIfLwStatusConnRemStatsDwnMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 25), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsDwnMod.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsDwnMod.setDescription('Downstream Modulation')
mIfLwStatusEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3), )
if mibBuilder.loadTexts: mIfLwStatusEndpointTable.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointTable.setDescription('The list of endpoints.')
mIfLwStatusEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-LW-MIB", "mIfLwStatusEndpointAddress"))
if mibBuilder.loadTexts: mIfLwStatusEndpointEntry.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointEntry.setDescription('The endpoint status entry.')
mIfLwStatusEndpointAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointAddress.setDescription('Address of endpoint.')
mIfLwStatusEndpointIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointIpAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointIpAddress.setDescription('Ip address of endpoint.')
mIfLwStatusEndpointTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointTimeToLive.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointTimeToLive.setDescription('Time left until this entry is aged out.')
mIfLwStatusEndpointRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointRemAddress.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointRemAddress.setDescription('The MAC address of the remote device servicing this endpoint.')
mIfLwStatusEndpointStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxPackets.setDescription('tx packets')
mIfLwStatusEndpointStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxBytes.setDescription('tx bytes')
mIfLwStatusEndpointStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxPackets.setDescription('rx packets')
mIfLwStatusEndpointStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxBytes.setDescription('rx bytes')
mIfLwStatusEndpointStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxError.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxError.setDescription('tx error')
mIfLwStatusEndpointStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxError.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxError.setDescription('rx error')
mIfLwStatusEndpointStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxDrop.setDescription('tx drop')
mIfLwStatusEndpointStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxDrop.setDescription('rx drop')
mdsIfLwMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3))
mdsIfLwMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 1))
mdsIfLwMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2))
mIfLwCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 1, 1)).setObjects(("MDS-IF-LW-MIB", "mIfLwStatusGroup"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemGroup"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLwCompliance = mIfLwCompliance.setStatus('current')
if mibBuilder.loadTexts: mIfLwCompliance.setDescription('The compliance statement for SNMP entities that \n            implement the MDS-IF-LW-MIB.')
mIfLwStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2, 1)).setObjects(("MDS-IF-LW-MIB", "mIfLwLinkStatus"), ("MDS-IF-LW-MIB", "mIfLwInitStatus"), ("MDS-IF-LW-MIB", "mIfLwCurrentDeviceMode"), ("MDS-IF-LW-MIB", "mIfLwAlarms"), ("MDS-IF-LW-MIB", "mIfLwSerialNumber"), ("MDS-IF-LW-MIB", "mIfLwFirmwareRevision"), ("MDS-IF-LW-MIB", "mIfLwHardwareId"), ("MDS-IF-LW-MIB", "mIfLwHardwareRevision"), ("MDS-IF-LW-MIB", "mIfLwTemperature"), ("MDS-IF-LW-MIB", "mIfLwApInfoApAddress"), ("MDS-IF-LW-MIB", "mIfLwApInfoIpAddress"), ("MDS-IF-LW-MIB", "mIfLwApInfoConnectedTime"), ("MDS-IF-LW-MIB", "mIfLwApInfoRssi"), ("MDS-IF-LW-MIB", "mIfLwApInfoSnr"), ("MDS-IF-LW-MIB", "mIfLwApInfoMod"), ("MDS-IF-LW-MIB", "mIfLwMacStatsTxSuccess"), ("MDS-IF-LW-MIB", "mIfLwMacStatsTxQueueFull"), ("MDS-IF-LW-MIB", "mIfLwMacStatsTxError"), ("MDS-IF-LW-MIB", "mIfLwMacStatsTxRetry"), ("MDS-IF-LW-MIB", "mIfLwMacStatsRxSuccess"), ("MDS-IF-LW-MIB", "mIfLwMacStatsRxError"), ("MDS-IF-LW-MIB", "mIfLwModemStatsTxSuccess"), ("MDS-IF-LW-MIB", "mIfLwModemStatsTxError"), ("MDS-IF-LW-MIB", "mIfLwModemStatsRxSuccess"), ("MDS-IF-LW-MIB", "mIfLwModemStatsRxError"), ("MDS-IF-LW-MIB", "mIfLwLastRssi"), ("MDS-IF-LW-MIB", "mIfLwLastSnr"), ("MDS-IF-LW-MIB", "mIfLwLastMod"), ("MDS-IF-LW-MIB", "mIfLwLastRate"), ("MDS-IF-LW-MIB", "mIfLwActiveNic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLwStatusGroup = mIfLwStatusGroup.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusGroup.setDescription('A collection of objects providing information about\n        common LW interface status.')
mIfLwStatusConnRemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2, 2)).setObjects(("MDS-IF-LW-MIB", "mIfLwStatusConnRemAddress"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemIpAddress"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemTimeToLive"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemLinkStatus"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemNicId"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemRssi"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemSnr"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemMod"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxPackets"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxBytes"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxPackets"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxBytes"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxError"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxError"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxDrop"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxDrop"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsGateway"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsAllIp"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsName"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsAlarmed"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsVersion"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTemp"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsDwnRssi"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsDwnSnr"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsDwnMod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLwStatusConnRemGroup = mIfLwStatusConnRemGroup.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusConnRemGroup.setDescription('A collection of objects providing information about\n        connected remotes status.')
mIfLwStatusEndpointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2, 3)).setObjects(("MDS-IF-LW-MIB", "mIfLwStatusEndpointAddress"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointIpAddress"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointTimeToLive"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointRemAddress"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxPackets"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxBytes"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxPackets"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxBytes"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxError"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxError"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxDrop"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxDrop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLwStatusEndpointGroup = mIfLwStatusEndpointGroup.setStatus('current')
if mibBuilder.loadTexts: mIfLwStatusEndpointGroup.setDescription('A collection of objects providing information about\n        endpoints status.')
mibBuilder.exportSymbols("MDS-IF-LW-MIB", mIfLwCompliance=mIfLwCompliance, FrequencyType=FrequencyType, mIfLwStatusConnRemEntry=mIfLwStatusConnRemEntry, mIfLwStatusConnRemStatsName=mIfLwStatusConnRemStatsName, mIfLwStatusEndpointStatsTxError=mIfLwStatusEndpointStatsTxError, mIfLwStatusConnRemMod=mIfLwStatusConnRemMod, mIfLwStatusEndpointStatsTxBytes=mIfLwStatusEndpointStatsTxBytes, mIfLwStatusEndpointStatsTxDrop=mIfLwStatusEndpointStatsTxDrop, mIfLwAlarms=mIfLwAlarms, mIfLwStatusConnRemStatsVersion=mIfLwStatusConnRemStatsVersion, mIfLwApInfoMod=mIfLwApInfoMod, InetIpAddress=InetIpAddress, UnsignedShort=UnsignedShort, mIfLwMacStatsTxRetry=mIfLwMacStatsTxRetry, ChannelType=ChannelType, mIfLwStatusGroup=mIfLwStatusGroup, mIfLwModemStatsTxSuccess=mIfLwModemStatsTxSuccess, mIfLwStatusEndpointTable=mIfLwStatusEndpointTable, LinkStatus=LinkStatus, mIfLwMacStatsTxQueueFull=mIfLwMacStatsTxQueueFull, mIfLwCurrentDeviceMode=mIfLwCurrentDeviceMode, mIfLwStatusEndpointEntry=mIfLwStatusEndpointEntry, mIfLwMacStatsRxSuccess=mIfLwMacStatsRxSuccess, mIfLwLastSnr=mIfLwLastSnr, mIfLwStatusConnRemStatsAlarmed=mIfLwStatusConnRemStatsAlarmed, mIfLwStatusEndpointAddress=mIfLwStatusEndpointAddress, ModulationModeType=ModulationModeType, mdsIfLwMIBCompliances=mdsIfLwMIBCompliances, mIfLwMacStatsRxError=mIfLwMacStatsRxError, InitStatus=InitStatus, mIfLwStatusEndpointStatsRxError=mIfLwStatusEndpointStatsRxError, UnsignedByte=UnsignedByte, mIfLwStatusEndpointStatsRxPackets=mIfLwStatusEndpointStatsRxPackets, mdsIfLwMIBGroups=mdsIfLwMIBGroups, mIfLwApInfoIpAddress=mIfLwApInfoIpAddress, mIfLwStatusConnRemStatsRxError=mIfLwStatusConnRemStatsRxError, mIfLwStatusConnRemRssi=mIfLwStatusConnRemRssi, mIfLwStatusConnRemLinkStatus=mIfLwStatusConnRemLinkStatus, mIfLwFirmwareRevision=mIfLwFirmwareRevision, mIfLwStatusEndpointStatsTxPackets=mIfLwStatusEndpointStatsTxPackets, mIfLwStatusConnRemStatsRxPackets=mIfLwStatusConnRemStatsRxPackets, FirmwareRevision=FirmwareRevision, mIfLwStatusConnRemStatsAllIp=mIfLwStatusConnRemStatsAllIp, mIfLwStatusConnRemAddress=mIfLwStatusConnRemAddress, mIfLwStatusConnRemStatsTxError=mIfLwStatusConnRemStatsTxError, mIfLwInitStatus=mIfLwInitStatus, mIfLwStatusConnRemStatsTxDrop=mIfLwStatusConnRemStatsTxDrop, mIfLwStatusEndpointStatsRxBytes=mIfLwStatusEndpointStatsRxBytes, mIfLwLastMod=mIfLwLastMod, mIfLwStatusEndpointStatsRxDrop=mIfLwStatusEndpointStatsRxDrop, mIfLwStatusConnRemStatsTemp=mIfLwStatusConnRemStatsTemp, mIfLwSerialNumber=mIfLwSerialNumber, mIfLwStatusEntry=mIfLwStatusEntry, mIfLwStatusConnRemNicId=mIfLwStatusConnRemNicId, mIfLwStatusConnRemStatsRxBytes=mIfLwStatusConnRemStatsRxBytes, mIfLwModemStatsTxError=mIfLwModemStatsTxError, mIfLwStatus=mIfLwStatus, RateType=RateType, mIfLwStatusConnRemStatsDwnMod=mIfLwStatusConnRemStatsDwnMod, mIfLwApInfoRssi=mIfLwApInfoRssi, mIfLwStatusConnRemStatsTxPackets=mIfLwStatusConnRemStatsTxPackets, mIfLwMacStatsTxSuccess=mIfLwMacStatsTxSuccess, mIfLwApInfoConnectedTime=mIfLwApInfoConnectedTime, mIfLwLinkStatus=mIfLwLinkStatus, mIfLwLastRate=mIfLwLastRate, mIfLwStatusConnRemStatsRxDrop=mIfLwStatusConnRemStatsRxDrop, mdsIfLwMIB=mdsIfLwMIB, mIfLwModemStatsRxSuccess=mIfLwModemStatsRxSuccess, mIfLwHardwareId=mIfLwHardwareId, mIfLwMIBObjects=mIfLwMIBObjects, mIfLwStatusConnRemIpAddress=mIfLwStatusConnRemIpAddress, PYSNMP_MODULE_ID=mdsIfLwMIB, mIfLwStatusConnRemTimeToLive=mIfLwStatusConnRemTimeToLive, mIfLwStatusConnRemStatsDwnSnr=mIfLwStatusConnRemStatsDwnSnr, mIfLwConfig=mIfLwConfig, mIfLwApInfoApAddress=mIfLwApInfoApAddress, mIfLwActiveNic=mIfLwActiveNic, mIfLwMacStatsTxError=mIfLwMacStatsTxError, mdsIfLwMIBConformance=mdsIfLwMIBConformance, DeviceModeType=DeviceModeType, mIfLwHardwareRevision=mIfLwHardwareRevision, mIfLwTemperature=mIfLwTemperature, mIfLwStatusConnRemStatsDwnRssi=mIfLwStatusConnRemStatsDwnRssi, mIfLwStatusConnRemGroup=mIfLwStatusConnRemGroup, mIfLwStatusEndpointTimeToLive=mIfLwStatusEndpointTimeToLive, mIfLwStatusEndpointGroup=mIfLwStatusEndpointGroup, mIfLwStatusEndpointIpAddress=mIfLwStatusEndpointIpAddress, mIfLwLastRssi=mIfLwLastRssi, mIfLwStatusTable=mIfLwStatusTable, mIfLwStatusConnRemTable=mIfLwStatusConnRemTable, mIfLwApInfoSnr=mIfLwApInfoSnr, mIfLwStatusEndpointRemAddress=mIfLwStatusEndpointRemAddress, mIfLwStatusConnRemStatsTxBytes=mIfLwStatusConnRemStatsTxBytes, mIfLwModemStatsRxError=mIfLwModemStatsRxError, mIfLwStatusConnRemSnr=mIfLwStatusConnRemSnr, mIfLwStatusConnRemStatsGateway=mIfLwStatusConnRemStatsGateway, FecType=FecType, AlarmFlags=AlarmFlags)
