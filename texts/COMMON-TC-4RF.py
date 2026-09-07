#
# PySNMP MIB module COMMON-TC-4RF (http://snmplabs.com/pysmi)
# ASN.1 source COMMON-TC-4RF
# Source digest sha256:515cae852f5a64d2a53582c5233d2ef3f0a9f2d3f4e70f062920caa5a54e4c36
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
fourRFGeneric, fourRFModules = mibBuilder.importSymbols("MIB-4RF", "fourRFGeneric", "fourRFModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
fourRFCommonTCModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 14817, 2, 4))
fourRFCommonTCModule.setRevisions(('2007-04-30 00:00', '2004-02-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fourRFCommonTCModule.setRevisionsDescriptions(('Second draft', 'First draft',))
if mibBuilder.loadTexts: fourRFCommonTCModule.setLastUpdated('2007-04-30 00:00')
if mibBuilder.loadTexts: fourRFCommonTCModule.setOrganization('www.4rf.com')
if mibBuilder.loadTexts: fourRFCommonTCModule.setContactInfo('postal:   4RF Communications Ltd\n                    26 Glover Street\n                    Ngauranga\n                    PO Box 13-506\n                    Wellington 6032\n                    New Zealand\n                    \n          phone:    +64 4 499 6000\n          email:    support@4rf.com')
if mibBuilder.loadTexts: fourRFCommonTCModule.setDescription('Common 4RF MIB Textual Conventions.')
class FourRFSimpleLedState(TextualConvention, Integer32):
    description = 'The possible states for a simple LED.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class FourRFTriColourLedState(TextualConvention, Integer32):
    description = 'The possible states of a three-colour LED.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("off", 0), ("green", 1), ("red", 2), ("orange", 3))

class FourRFAlarmSeverity(TextualConvention, Integer32):
    description = 'The possible alarm severities, not all values need be used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 3, 4))
    namedValues = NamedValues(("noSeverity", 0), ("minor", 3), ("major", 4))

class FourRFAlarmPresent(TextualConvention, Integer32):
    description = 'The possible alarm states, alarmPresent indicates that the\n                 alarm is active.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("noAlarmPresent", 0), ("alarmPresent", 1))

class FourRFAlarmEnabled(TextualConvention, Integer32):
    description = 'Indicates whether an alarm is enabled or not, it may be useful\n                 to allow specific alarms to be enabled or disabled by the user.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class FourRFAlarmStatus(TextualConvention, Integer32):
    description = 'This is used to identify current alarm status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("noAlarm", 0), ("informationAlarm", 1), ("warningAlarm", 2), ("minorAlarm", 3), ("majorAlarm", 4), ("criticalAlarm", 5))

class FourRFMHSBStatus(TextualConvention, Integer32):
    description = 'This is used to give the state of an MHSB terminal.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notAvailable", 0), ("active", 1), ("standby", 2))

class FourRFMHSBCommand(TextualConvention, Integer32):
    description = 'This is used to send a command to an MHSB terminal.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("noCommand", 0), ("clearSwitchedAlarm", 1), ("forceSwitchover", 2))

class FourRFHardwareVersion(DisplayString):
    description = 'The hardware version details.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class FourRFSerialNumber(TextualConvention, OctetString):
    description = 'A module/terminal serial number format xxxx-xxx.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class FourRFResetType(TextualConvention, Integer32):
    description = 'The possible types of reset.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("softReset", 1), ("hardReset", 2), ("watchdogReset", 3))

class FourRFImageType(TextualConvention, Integer32):
    description = 'The possible image types to upload.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("kernel", 1), ("rootfs", 2), ("mib", 3), ("configuration", 4), ("firmware", 5))

class FourRFImageStatus(TextualConvention, Integer32):
    description = "The possible image status values, currentImage means it is the running.\n         selectedImage means that the image has been selected and will be used\n         following the next reboot of the system, currentNotSelected means that \n         the image is currently in use but won't be following a reboot."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("inactiveImage", 0), ("currentImage", 1), ("currentNotSelected", 2), ("selectedImage", 3))

class FourRFImageVersion(DisplayString):
    description = 'The image version details.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class FourRFProcessResultType(TextualConvention, Integer32):
    description = 'The possible states for a process which takes time to complete.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("executing", 1), ("writingToFlash", 2), ("succeeded", 3), ("failed", 4))

class FourRFTftpFileName(DisplayString):
    description = 'The name of a file to transfered using TFTP.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class FourRFFileSize(TextualConvention, Unsigned32):
    description = 'A size of a file in bytes.'
    status = 'current'

class FourRFFrequency(TextualConvention, Unsigned32):
    description = 'A frequency value in Hz.'
    status = 'current'

class FourRFTxPower(TextualConvention, Integer32):
    description = 'A transmitter power value in dBm.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))
    namedValues = NamedValues(("noPower", 0), ("dbm10", 10), ("dbm11", 11), ("dbm12", 12), ("dbm13", 13), ("dbm14", 14), ("dbm15", 15), ("dbm16", 16), ("dbm17", 17), ("dbm18", 18), ("dbm19", 19), ("dbm20", 20), ("dbm21", 21), ("dbm22", 22), ("dbm23", 23), ("dbm24", 24), ("dbm25", 25), ("dbm26", 26), ("dbm27", 27), ("dbm28", 28), ("dbm29", 29), ("dbm30", 30), ("dbm31", 31), ("dbm32", 32), ("dbm33", 33), ("dbm34", 34), ("dbm35", 35), ("dbm36", 36), ("dbm37", 37), ("dbm38", 38), ("dbm39", 39), ("dbm40", 40))

class FourRFChannelWidth(TextualConvention, Integer32):
    description = 'The possible channel width values.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 13, 20, 25, 30, 33, 35, 40, 42, 45, 50, 55, 60, 70))
    namedValues = NamedValues(("invalidChannel", 0), ("channel20KHz", 1), ("channel25KHz", 2), ("channel50KHz", 3), ("channel75KHz", 4), ("channel100KHz", 5), ("channel125KHz", 6), ("channel150KHz", 7), ("channel200KHz", 9), ("channel250KHz", 10), ("channel400KHz", 13), ("channel500KHz", 20), ("channel800KHz", 25), ("channel1MHz", 30), ("channel1point25MHz", 33), ("channel1point35MHz", 35), ("channel1point75MHz", 40), ("channel2MHz", 42), ("channel2point5MHz", 45), ("channel3point5MHz", 50), ("channel5point25MHz", 55), ("channel7MHz", 60), ("channel14MHz", 70))

class FourRFNetworkClockStatus(TextualConvention, Integer32):
    description = 'The possible modulation types for the radio.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("active", 0), ("inactive", 1), ("holdover", 2))

class FourRFRSSI(TextualConvention, Integer32):
    description = 'A receiver RSSI value, in dBm.'
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2000, 2000)

class FourRFSNR(TextualConvention, Integer32):
    description = 'A signal to noise ratio in dBm.'
    status = 'current'
    displayHint = 'd-2'

class FourRFModulationType(TextualConvention, Integer32):
    description = 'The possible modulation types for the radio.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("modQPSK", 0), ("mod16QAM", 1), ("mod32QAM", 2), ("mod64QAM", 3), ("mod128QAM", 4), ("mod256QAM", 5), ("modNone", 6))

class FourRFTemperature(TextualConvention, Integer32):
    description = 'A temperature value in degrees Celcius.'
    status = 'current'

class FourRFErrorCounter(TextualConvention, Counter32):
    description = 'An error counter, e.g. for the uncorrectable error count.'
    status = 'current'

class FourRFRfBand(TextualConvention, Integer32):
    description = 'This is used to identify the frequency band of the transmitter\n                 The bands are: \n                     330 to 400 MHz (300 MHz)\n                     400 to 470 MHz (400 MHz)\n                     1350 to 1550 MHz (1400 MHz) .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 10, 20, 24, 26, 28, 30))
    namedValues = NamedValues(("invalidBand", 0), ("band300MHz", 10), ("band400MHz", 20), ("band700MHz", 24), ("band800MHz", 26), ("band900MHz", 28), ("band1400MHz", 30))

class FourRFFanStatus(TextualConvention, Integer32):
    description = 'This is used to identify current fan status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notFitted", 0), ("fanOkay", 1), ("fanFailed", 2))

class FourRFClockSource(TextualConvention, Integer32):
    description = 'This is used to identify the clock source for the terminal.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("networkClock", 0), ("linkClock", 1), ("internalClock", 2))

class FourRFNetworkClockSelect(TextualConvention, Integer32):
    description = 'This is used to select the priority of the clocks to use.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("primary", 1), ("secondary", 2))

class FourRFLoopback(TextualConvention, Integer32):
    description = 'This is used to control loopback or monitor status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("loopbackOff", 0), ("loopbackOn", 1))

class FourRFWebUserGroup(TextualConvention, Integer32):
    description = 'This is used to identify the group to which a web user belongs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("readOnlyGroup", 0), ("readWriteGroup", 1), ("adminGroup", 2))

class FourRFWebUserEnabled(TextualConvention, Integer32):
    description = 'This is used to identify whether a web user is enabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("userDisabled", 0), ("userEnabled", 1))

class FourRFTimeZone(TextualConvention, Integer32):
    description = 'This is used to assign an offset in minutes based on GMT timezone.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-720, -660, -600, -540, -480, -420, -360, -300, -240, -210, -180, -120, -60, 0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 800))
    namedValues = NamedValues(("gmtMinusTwelve", -720), ("gmtMinusEleven", -660), ("gmtMinusTen", -600), ("gmtMinusNine", -540), ("gmtMinusEight", -480), ("gmtMinusSeven", -420), ("gmtMinusSix", -360), ("gmtMinusFive", -300), ("gmtMinusFour", -240), ("gmtMinusThreePointFive", -210), ("gmtMinusThree", -180), ("gmtMinusTwo", -120), ("gmtMinusOne", -60), ("gmt", 0), ("gmtPlusOne", 60), ("gmtPlusTwo", 120), ("gmtPlusThree", 180), ("gmtPlusFour", 240), ("gmtPlusFive", 300), ("gmtPlusSix", 360), ("gmtPlusSeven", 420), ("gmtPlusEight", 480), ("gmtPlusNine", 540), ("gmtPlusTen", 600), ("gmtPlusEleven", 660), ("gmtPlusTwelve", 720), ("gmtPlusThirteen", 800))

mibBuilder.exportSymbols("COMMON-TC-4RF", FourRFAlarmEnabled=FourRFAlarmEnabled, FourRFAlarmPresent=FourRFAlarmPresent, FourRFAlarmSeverity=FourRFAlarmSeverity, FourRFAlarmStatus=FourRFAlarmStatus, FourRFChannelWidth=FourRFChannelWidth, FourRFClockSource=FourRFClockSource, FourRFErrorCounter=FourRFErrorCounter, FourRFFanStatus=FourRFFanStatus, FourRFFileSize=FourRFFileSize, FourRFFrequency=FourRFFrequency, FourRFHardwareVersion=FourRFHardwareVersion, FourRFImageStatus=FourRFImageStatus, FourRFImageType=FourRFImageType, FourRFImageVersion=FourRFImageVersion, FourRFLoopback=FourRFLoopback, FourRFMHSBCommand=FourRFMHSBCommand, FourRFMHSBStatus=FourRFMHSBStatus, FourRFModulationType=FourRFModulationType, FourRFNetworkClockSelect=FourRFNetworkClockSelect, FourRFNetworkClockStatus=FourRFNetworkClockStatus, FourRFProcessResultType=FourRFProcessResultType, FourRFRSSI=FourRFRSSI, FourRFResetType=FourRFResetType, FourRFRfBand=FourRFRfBand, FourRFSNR=FourRFSNR, FourRFSerialNumber=FourRFSerialNumber, FourRFSimpleLedState=FourRFSimpleLedState, FourRFTemperature=FourRFTemperature, FourRFTftpFileName=FourRFTftpFileName, FourRFTimeZone=FourRFTimeZone, FourRFTriColourLedState=FourRFTriColourLedState, FourRFTxPower=FourRFTxPower, FourRFWebUserEnabled=FourRFWebUserEnabled, FourRFWebUserGroup=FourRFWebUserGroup, PYSNMP_MODULE_ID=fourRFCommonTCModule, fourRFCommonTCModule=fourRFCommonTCModule)
