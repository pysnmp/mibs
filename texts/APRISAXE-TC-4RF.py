#
# PySNMP MIB module APRISAXE-TC-4RF (http://snmplabs.com/pysmi)
# ASN.1 source APRISAXE-TC-4RF
# Source digest sha256:2cc2453d08f47685c41f64933ebea7a8b32cccde453c6d0f9bbe56d114a8bbeb
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
fourRFModules, = mibBuilder.importSymbols("MIB-4RF", "fourRFModules")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fourRFAprisaXETCModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 14817, 2, 6))
fourRFAprisaXETCModule.setRevisions(('2007-04-30 00:00', '2004-12-03 01:52',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fourRFAprisaXETCModule.setRevisionsDescriptions(('Second draft', 'First draft',))
if mibBuilder.loadTexts: fourRFAprisaXETCModule.setLastUpdated('2007-04-30 00:00')
if mibBuilder.loadTexts: fourRFAprisaXETCModule.setOrganization('www.4rf.com')
if mibBuilder.loadTexts: fourRFAprisaXETCModule.setContactInfo('postal:   4RF Communications Ltd\n                    26 Glover Street\n                    Ngauranga\n                    PO Box 13-506\n                    Wellington 6032\n                    New Zealand\n                    \n          phone:    +64 4 499 6000\n          email:    support@4rf.com')
if mibBuilder.loadTexts: fourRFAprisaXETCModule.setDescription('Textual Conventions for the AprisaXE project')
class AprisaXESlotNumber(TextualConvention, Integer32):
    description = 'Represents a slot number in the AprisaXE, the slots include\n                 the modem, transmitter and receiver as well as the MUX cards.\n         H/W Slot    Card      Slot Name\n         0         Aux/Modem    Aux\n         1         MUX Card     H\n         2         MUX Card     G\n         3         MUX Card     F\n         4         MUX Card     E\n         5         MUX Card     D\n         6         MUX Card     C\n         7         MUX Card     B\n         8         MUX Card     A\n         9         Transmitter  Transmitter\n         10        Receiver     Receiver\n                Slots may or may not be populated.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 255))
    namedValues = NamedValues(("rxSlot", 0), ("txSlot", 1), ("slotA", 2), ("slotB", 3), ("slotC", 4), ("slotD", 5), ("slotE", 6), ("slotF", 7), ("slotG", 8), ("slotH", 9), ("auxSlot", 10), ("noSlot", 255))

class AprisaXEHardwareVersion(TextualConvention, Integer32):
    description = 'Represents a single byte hardware version number.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class AprisaXECardType(TextualConvention, Integer32):
    description = 'This is used to identify the type of MUX card in a slot.\n                  The values for the enumerations match the hardware type\n                  values returned from the MUX card FPGAs and EEPROMs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 224, 227, 228, 229, 231, 232, 233, 234, 235, 236, 237, 238, 213, 197))
    namedValues = NamedValues(("none", 0), ("motherboard", 224), ("transmitterCard", 227), ("receiverCard", 228), ("quadJETCard", 229), ("quadFourWireCard", 231), ("dualFXOCard", 232), ("dualFXSCard", 233), ("modemCard", 234), ("quadV24Card", 235), ("hssCard", 236), ("pscCard", 237), ("picCard", 238), ("dualJETCard", 213), ("singleJETCard", 197))

class AprisaXEAlarmSource(TextualConvention, Integer32):
    description = 'This is used to identify the source of an alarm.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 50, 51, 60, 70, 71, 100, 101))
    namedValues = NamedValues(("none", 0), ("modem", 1), ("transmitter", 2), ("receiver", 3), ("quadJET", 4), ("quadFourWire", 5), ("dualFxo", 6), ("dualFxs", 7), ("quadV24", 8), ("highSpeedSync", 9), ("psc", 10), ("pic", 11), ("dualJET", 12), ("singleJET", 13), ("external1", 50), ("external2", 51), ("remote", 60), ("user1", 70), ("user2", 71), ("system", 100), ("swUpgrade", 101))

class AprisaXEPortNumber(TextualConvention, Integer32):
    description = 'This is used to identify a port e.g. reporting an alarm.\n                  Not all alarms are associated with a port, in these cases\n                  noPort will be used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("noPort", 0), ("portOne", 1), ("portTwo", 2), ("portThree", 3), ("portFour", 4))

class AprisaXEAlarmOutput(TextualConvention, Integer32):
    description = 'This is used to map alarm to external outputs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("externalOutput1", 1), ("externalOutput2", 2), ("externalOutput3", 3), ("externalOutput4", 4))

class AprisaXEAlarmMapping(TextualConvention, Integer32):
    description = 'This is used to map alarm to external outputs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("localMajor", 1), ("localMinor", 2), ("remoteMajor", 3), ("remoteMinor", 4), ("remoteInput1", 5), ("remoteInput2", 6))

class AprisaXEAlarmPolarity(TextualConvention, Integer32):
    description = 'This is used to indicate the polarity indicating an alarm\n                 present on the external outputs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("polarityLow", 0), ("polarityHigh", 1))

class AprisaXEAdcVoltage(TextualConvention, Integer32):
    description = 'A voltage read from an ADC, in millivolts.'
    status = 'current'
    displayHint = 'd-3'

class AprisaXEDbValue(TextualConvention, Integer32):
    description = "A value displayed in dB's."
    status = 'current'
    displayHint = 'd-1'

class AprisaXEIQData(TextualConvention, OctetString):
    description = 'A sequence of IQ data pairs, each individual value is 16 bit\n                 thus a single IQ pair is 32 bits.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 200)

class AprisaXEAlarmType(TextualConvention, Integer32):
    description = 'The type of an alarm.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 120, 150, 151, 152, 153, 154, 155, 200, 201, 202, 203, 204, 205, 206, 207, 220, 221, 222, 226, 227, 250, 251, 252, 253, 254, 255, 300, 301, 325, 350, 351, 352, 353, 354, 355, 400, 401, 402, 403, 404, 405, 406, 407, 408, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 525, 550, 551, 552, 575, 576, 577, 578, 579, 580, 600, 601, 602, 603, 604, 605, 606, 607, 608))
    namedValues = NamedValues(("none", 0), ("txADCChZeroHi", 1), ("txADCChZeroLo", 2), ("txADCChOneHi", 3), ("txADCChOneLo", 4), ("txADCChTwoHi", 5), ("txADCChTwoLo", 6), ("txADCChThreeHi", 7), ("txADCChThreeLo", 8), ("txADCChFourHi", 9), ("txADCChFourLo", 10), ("txADCChFiveHi", 11), ("txADCChFiveLo", 12), ("txADCChSixHi", 13), ("txADCChSixLo", 14), ("txADCChSevenHi", 15), ("txADCChSevenLo", 16), ("txADCChEightHi", 17), ("txADCChEightLo", 18), ("txADCChNineHi", 19), ("txADCCNineLo", 20), ("txADCChTenHi", 21), ("txADCChTenLo", 22), ("txADCChElevenHi", 23), ("txADCChElevenLo", 24), ("txSynthLD", 25), ("tx5VFail", 26), ("tx11VFail", 27), ("tx28VFail", 28), ("txEEFail", 29), ("txTSensorFail", 30), ("txReturnLoss", 31), ("txAmplifierBalance", 32), ("txMibFail", 33), ("rxADCChZeroHi", 50), ("rxADCChZeroLo", 51), ("rxADCChOneHi", 52), ("rxADCChOneLo", 53), ("rxADCChTwoHi", 54), ("rxADCChTwoLo", 55), ("rxADCChThreeHi", 56), ("rxADCChThreeLo", 57), ("rxADCChFourHi", 58), ("rxADCChFourLo", 59), ("rxADCChFiveHi", 60), ("rxADCChFiveLo", 61), ("rxADCChSixHi", 62), ("rxADCChSixLo", 63), ("rxADCChSevenHi", 64), ("rxADCChSevenLo", 65), ("rxADCChEightHi", 66), ("rxADCChEightLo", 67), ("rxADCChNineHi", 68), ("rxADCCNineLo", 69), ("rxADCChTenHi", 70), ("rxADCChTenLo", 71), ("rxRSSIHi", 72), ("rxRSSILo", 73), ("rx12VFail", 74), ("rxSynthLD", 75), ("rxEEFail", 76), ("rxOff", 77), ("rxMibFail", 78), ("mdLOS", 100), ("mdLink", 101), ("mdStatus", 102), ("mdDemodAlignmentLost", 103), ("mdTdmAlignmentLost", 104), ("mdRefAFail", 105), ("mdRefBFail", 106), ("mdClkSyncFail", 107), ("mdNetClkConfig", 108), ("mdUCEPresent", 109), ("mdInitFail", 110), ("mdEEFail", 120), ("muxId", 150), ("muxInit", 151), ("muxStat", 152), ("muxClk", 153), ("muxMibEEFail", 154), ("muxCharEEFail", 155), ("e1LOF", 200), ("e1AIS", 201), ("e1RAI", 202), ("e1RMAI", 203), ("e1TS16AIS", 204), ("e1TS16LOS", 205), ("e1LOS", 206), ("e1CRC4", 207), ("t1LOF", 220), ("t1AIS", 221), ("t1RAI", 222), ("t1LOS", 226), ("t1CRC6", 227), ("mbHwHsc", 250), ("mbFan1Fail", 251), ("mbFan2Fail", 252), ("mbInvalidConfig", 253), ("mbCardMismatch", 254), ("mbEEFail", 255), ("ccDataFail", 300), ("ccNoBandwidth", 301), ("mhsbSwitchToStandby", 325), ("externalAlarm1", 350), ("externalAlarm2", 351), ("externalOutputAlarm1", 352), ("externalOutputAlarm2", 353), ("externalOutputAlarm3", 354), ("externalOutputAlarm4", 355), ("remoteMajorAlarm", 400), ("remoteMinorAlarm", 401), ("fxoCodecOvld", 402), ("fxoBillToneOvld", 403), ("fxoUnplug", 404), ("fxoCurrentOvld", 405), ("fxsCalibError", 406), ("fxsDCDCError", 407), ("fxsCASLock", 408), ("hssTdmLock", 500), ("hss32MhzReset", 501), ("hssTdmReset", 502), ("hssLoss", 503), ("hssRxFifoFull", 504), ("hssRxFifoEmpty", 505), ("hssTxFifoFull", 506), ("hssTxFifoEmpty", 507), ("hssRxClockInvalid", 508), ("hssTxClockInvalid", 509), ("v24CtrlLineLoss", 525), ("altImageTableUsed", 550), ("defaultImageTableUsed", 551), ("uploadFail", 552), ("pscDemuxAlignmentLost", 575), ("pscTDMAlignmentLost", 576), ("pscMuxAlignmentError", 577), ("pscCompanionTxFail", 578), ("pscSoftwareOverride", 579), ("pscInvalidSwitchValue", 580), ("hsdParamMismatch", 600), ("hsdCompanionLost", 601), ("hsdPMTxFreq", 602), ("hsdPMRxFreq", 603), ("hsdPMTermModState", 604), ("hsdPMTermRfChWidth", 605), ("hsdPMTxPower", 606), ("hsdPMModemIntlvEna", 607), ("lastAlarm", 608))

class AprisaXEChannelControlType(TextualConvention, Integer32):
    description = 'This is used to set the control the channels, enabling and\n                 disabling E1/T1 ports.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class AprisaXETdmPortType(TextualConvention, Integer32):
    description = 'This is used to set the port out to the TDM bus.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("tdmAo", 0), ("tdmBo", 1), ("tdmCo", 2), ("tdmDo", 3), ("tdmAi", 4), ("tdmBi", 5), ("tdmCi", 6), ("tdmDi", 7))

class AprisaXETdmBus(TextualConvention, Integer32):
    description = 'This is used to set the TDM bus to use.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("tdmBusA", 0), ("tdmBusB", 1), ("tdmBusC", 2), ("tdmBusD", 3))

class AprisaXEQuadJetTrafficType(TextualConvention, Integer32):
    description = 'This is used to set the traffic rate for the Quad JET card.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("e1Traffic", 0), ("t1Traffic", 1), ("j1Traffic", 2))

class AprisaXEQuadJetLineEncoding(TextualConvention, Integer32):
    description = 'This is used to set the line encoding for the Quad JET card the \n                 default is HDB3 for E1 and B8ZS for T1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 4, 1))
    namedValues = NamedValues(("defaultLineEncoding", 0), ("hDB3LineEncoding", 2), ("b8ZSLineEncoding", 4), ("amiLineEncoding", 1))

class AprisaXEQuadJetWaveFormShapers(TextualConvention, Integer32):
    description = 'This is used to set the T1 Tx Waveform Shaper for a port;\n                 The default value is 0~133 ft.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))
    namedValues = NamedValues(("wfs0To133Ft", 2), ("wfs133To266Ft", 3), ("wfs266To399Ft", 4), ("wfs399To533Ft", 5), ("wfs533To655Ft", 6))

class AprisaXEQuadJetMultiframeEnable(TextualConvention, Integer32):
    description = 'This is used to enable/disable support for transport of T1 SF \n                 and ESF multiframe sync for a port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("t1MFOff", 0), ("t1MFOn", 1))

class AprisaXEDataStatus(TextualConvention, Integer32):
    description = 'This indicates the state of receiver, transmitter or MUX card \n                 MIB orcharacterisation data.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("invalid", 0), ("valid", 1))

class AprisaXEAdpcmCompression(TextualConvention, Integer32):
    description = 'This defines the Compression available on ADPCM.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("kbits16", 0), ("kbits24", 1), ("kbits32", 2), ("kbits64", 3), ("kbits0", 4))

class AprisaXESignalState(TextualConvention, Integer32):
    description = 'This indicates the state of CAS signalling.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("normal", 0), ("invert", 1))

class AprisaXEPcmLaw(TextualConvention, Integer32):
    description = 'Type of PCM encoding available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("alaw", 0), ("ulaw", 1))

class AprisaXE4WRxGain(TextualConvention, Integer32):
    description = 'The gain in half dB steps for 4wire mux cards.'
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))
    namedValues = NamedValues(("dbpos40", 0), ("dbpos35", 1), ("dbpos30", 2), ("dbpos25", 3), ("dbpos20", 4), ("dbpos15", 5), ("dbpos10", 6), ("dbpos05", 7), ("dbpos0", 8), ("dbneg05", 9), ("dbneg10", 10), ("dbneg15", 11), ("dbneg20", 12), ("dbneg25", 13), ("dbneg30", 14), ("dbneg35", 15), ("dbneg40", 16), ("dbneg45", 17), ("dbneg50", 18), ("dbneg55", 19), ("dbneg60", 20), ("dbneg65", 21), ("dbneg70", 22), ("dbneg75", 23), ("dbneg80", 24), ("dbneg85", 25), ("dbneg90", 26), ("dbneg95", 27), ("dbneg100", 28), ("dbneg105", 29), ("dbneg110", 30), ("dbneg115", 31), ("dbneg120", 32), ("dbneg125", 33), ("dbneg130", 34), ("dbneg135", 35), ("dbneg140", 36))

class AprisaXE4WTxGain(TextualConvention, Integer32):
    description = 'The gain in half dB steps for 4wire mux cards.'
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))
    namedValues = NamedValues(("pos140", 0), ("pos135", 1), ("pos130", 2), ("pos125", 3), ("pos120", 4), ("pos115", 5), ("pos110", 6), ("pos105", 7), ("pos100", 8), ("pos95", 9), ("pos90", 10), ("pos85", 11), ("pos80", 12), ("pos75", 13), ("pos70", 14), ("pos65", 15), ("pos60", 16), ("pos55", 17), ("pos50", 18), ("pos45", 19), ("pos40", 20), ("pos35", 21), ("pos30", 22), ("pos25", 23), ("pos20", 24), ("pos15", 25), ("pos10", 26), ("pos05", 27), ("pos0", 28), ("neg05", 29), ("neg10", 30), ("neg15", 31), ("neg20", 32), ("neg25", 33), ("neg30", 34), ("neg35", 35), ("neg40", 36))

class AprisaXE4WInputLevel(TextualConvention, Integer32):
    description = 'The input (A->D) level in half dB steps for the 4wire mux cards.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
    namedValues = NamedValues(("q4emadpos40", 36), ("q4emadpos35", 35), ("q4emadpos30", 34), ("q4emadpos25", 33), ("q4emadpos20", 32), ("q4emadpos15", 31), ("q4emadpos10", 30), ("q4emadpos05", 29), ("q4emadpos0", 28), ("q4emadneg05", 27), ("q4emadneg10", 26), ("q4emadneg15", 25), ("q4emadneg20", 24), ("q4emadneg25", 23), ("q4emadneg30", 22), ("q4emadneg35", 21), ("q4emadneg40", 20), ("q4emadneg45", 19), ("q4emadneg50", 18), ("q4emadneg55", 17), ("q4emadneg60", 16), ("q4emadneg65", 15), ("q4emadneg70", 14), ("q4emadneg75", 13), ("q4emadneg80", 12), ("q4emadneg85", 11), ("q4emadneg90", 10), ("q4emadneg95", 9), ("q4emadneg100", 8), ("q4emadneg105", 7), ("q4emadneg110", 6), ("q4emadneg115", 5), ("q4emadneg120", 4), ("q4emadneg125", 3), ("q4emadneg130", 2), ("q4emadneg135", 1), ("q4emadneg140", 0))

class AprisaXE4WOutputLevel(TextualConvention, Integer32):
    description = 'The output (D->A) level in half dB steps for the 4wire mux cards.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))
    namedValues = NamedValues(("q4emdapos40", 0), ("q4emdapos35", 1), ("q4emdapos30", 2), ("q4emdapos25", 3), ("q4emdapos20", 4), ("q4emdapos15", 5), ("q4emdapos10", 6), ("q4emdapos05", 7), ("q4emdapos0", 8), ("q4emdaneg05", 9), ("q4emdaneg10", 10), ("q4emdaneg15", 11), ("q4emdaneg20", 12), ("q4emdaneg25", 13), ("q4emdaneg30", 14), ("q4emdaneg35", 15), ("q4emdaneg40", 16), ("q4emdaneg45", 17), ("q4emdaneg50", 18), ("q4emdaneg55", 19), ("q4emdaneg60", 20), ("q4emdaneg65", 21), ("q4emdaneg70", 22), ("q4emdaneg75", 23), ("q4emdaneg80", 24), ("q4emdaneg85", 25), ("q4emdaneg90", 26), ("q4emdaneg95", 27), ("q4emdaneg100", 28), ("q4emdaneg105", 29), ("q4emdaneg110", 30), ("q4emdaneg115", 31), ("q4emdaneg120", 32), ("q4emdaneg125", 33), ("q4emdaneg130", 34), ("q4emdaneg135", 35), ("q4emdaneg140", 36))

class AprisaXEFXSInputLevel(TextualConvention, Integer32):
    description = 'The output (A->D) level in half dB steps for the DFXS mux cards.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1))
    namedValues = NamedValues(("dfxsadpos20", 23), ("dfxsadpos15", 22), ("dfxsadpos10", 21), ("dfxsadpos05", 20), ("dfxsadpos0", 19), ("dfxsadneg05", 18), ("dfxsadneg10", 17), ("dfxsadneg15", 16), ("dfxsadneg20", 15), ("dfxsadneg25", 14), ("dfxsadneg30", 13), ("dfxsadneg35", 12), ("dfxsadneg40", 11), ("dfxsadneg45", 10), ("dfxsadneg50", 9), ("dfxsadneg55", 8), ("dfxsadneg60", 7), ("dfxsadneg65", 6), ("dfxsadneg70", 5), ("dfxsadneg75", 4), ("dfxsadneg80", 3), ("dfxsadneg85", 2), ("dfxsadneg90", 1))

class AprisaXEFXSOutputLevel(TextualConvention, Integer32):
    description = 'The output (D->A) level in half dB steps for the DFXS mux cards.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))
    namedValues = NamedValues(("dfxsdapos25", 1), ("dfxsdapos20", 2), ("dfxsdapos15", 3), ("dfxsdapos10", 4), ("dfxsdapos05", 5), ("dfxsdapos0", 6), ("dfxsdaneg05", 7), ("dfxsdaneg10", 8), ("dfxsdaneg15", 9), ("dfxsdaneg20", 10), ("dfxsdaneg25", 11), ("dfxsdaneg30", 12), ("dfxsdaneg35", 13), ("dfxsdaneg40", 14), ("dfxsdaneg45", 15), ("dfxsdaneg50", 16), ("dfxsdaneg55", 17), ("dfxsdaneg60", 18), ("dfxsdaneg65", 19), ("dfxsdaneg70", 20), ("dfxsdaneg75", 21), ("dfxsdaneg80", 22), ("dfxsdaneg85", 23), ("dfxsdaneg90", 24), ("dfxsdaneg95", 25))

class AprisaXEFXOInputLevel(TextualConvention, Integer32):
    description = 'The output (A->D) level in half dB steps for the DFXO mux cards.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
    namedValues = NamedValues(("dfxoadpos10", 22), ("dfxoadpos05", 21), ("dfxoadpos0", 20), ("dfxoadneg05", 19), ("dfxoadneg10", 18), ("dfxoadneg15", 17), ("dfxoadneg20", 16), ("dfxoadneg25", 15), ("dfxoadneg30", 14), ("dfxoadneg35", 13), ("dfxoadneg40", 12), ("dfxoadneg45", 11), ("dfxoadneg50", 10), ("dfxoadneg55", 9), ("dfxoadneg60", 8), ("dfxoadneg65", 7), ("dfxoadneg70", 6), ("dfxoadneg75", 5), ("dfxoadneg80", 4), ("dfxoadneg85", 3), ("dfxoadneg90", 2), ("dfxoadneg95", 1), ("dfxoadneg100", 0))

class AprisaXEFXOOutputLevel(TextualConvention, Integer32):
    description = 'The output (D->A) level in half dB steps for the DFXO mux cards.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))
    namedValues = NamedValues(("dfxodapos10", 18), ("dfxodapos05", 19), ("dfxodapos0", 20), ("dfxodaneg05", 21), ("dfxodaneg10", 22), ("dfxodaneg15", 23), ("dfxodaneg20", 24), ("dfxodaneg25", 25), ("dfxodaneg30", 26), ("dfxodaneg35", 27), ("dfxodaneg40", 28), ("dfxodaneg45", 29), ("dfxodaneg50", 30), ("dfxodaneg55", 31), ("dfxodaneg60", 32), ("dfxodaneg65", 33), ("dfxodaneg70", 34), ("dfxodaneg75", 35), ("dfxodaneg80", 36), ("dfxodaneg85", 37), ("dfxodaneg90", 38), ("dfxodaneg95", 39), ("dfxodaneg100", 40))

class AprisaXEFXOCountry(TextualConvention, Integer32):
    description = 'The country code for FXO mux cards this will need to be completed later.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71))
    namedValues = NamedValues(("argentina", 0), ("australia", 1), ("austria", 2), ("bahrain", 3), ("belgium", 4), ("brazil", 5), ("bulgaria", 6), ("canada", 7), ("chile", 8), ("china", 9), ("columbia", 10), ("croatia", 11), ("cyprus", 12), ("czechrep", 13), ("denmark", 14), ("ecuador", 15), ("egypt", 16), ("elslavador", 17), ("finland", 18), ("france", 19), ("germany", 20), ("greece", 21), ("guam", 22), ("hongkong", 23), ("hungary", 24), ("iceland", 25), ("india", 26), ("indonesia", 27), ("ireland", 28), ("israel", 29), ("italy", 30), ("japan", 31), ("jordan", 32), ("kazakhstan", 33), ("kuwait", 34), ("latvia", 35), ("lebanon", 36), ("luxembourg", 37), ("macao", 38), ("malaysia", 39), ("malta", 40), ("mexico", 41), ("morocco", 42), ("netherlands", 43), ("newzealand", 44), ("nigeria", 45), ("norway", 46), ("oman", 47), ("pakistan", 48), ("peru", 49), ("philippines", 50), ("poland", 51), ("portugal", 52), ("romania", 53), ("russia", 54), ("saudiarabia", 55), ("singapore", 56), ("slovakia", 57), ("slovenia", 58), ("southafrica", 59), ("southkorea", 60), ("spain", 61), ("sweden", 62), ("switzerland", 63), ("syria", 64), ("taiwan", 65), ("tbr21", 66), ("thailand", 67), ("uae", 68), ("uk", 69), ("usa", 70), ("yemen", 71))

class AprisaXEFXSPMLevel(TextualConvention, Integer32):
    description = 'Type of SPM level.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("l0", 0), ("l1", 1), ("l2", 2), ("l3", 3), ("l4", 4), ("l5", 5), ("l6", 6), ("l7", 7), ("l8", 8), ("l9", 9), ("l10", 10), ("l11", 11), ("l12", 12), ("l13", 13), ("l14", 14), ("l15", 15), ("l16", 16), ("l17", 17), ("l18", 18), ("l19", 19), ("l20", 20), ("l21", 21), ("l22", 22), ("l23", 23), ("l24", 24), ("l25", 25), ("l26", 26), ("l27", 27))

class AprisaXEFXSPathMute(TextualConvention, Integer32):
    description = 'The status of the Path Mute function for the DFXS.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 16, 32))
    namedValues = NamedValues(("noMute", 0), ("muteRx", 16), ("muteTx", 32))

class AprisaXETableCommand(TextualConvention, Integer32):
    description = 'A command sent to add or delete table entries.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("noCommand", 0), ("addCommand", 1), ("deleteCommand", 2))

class AprisaXEQuadJetConnectionType(TextualConvention, Integer32):
    description = 'Indicates whether a connection is for data or CAS signalling.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("dataConnection", 0), ("casConnection", 1), ("tsLoopbackConnection", 2))

class AprisaXEInterfaceCnxnType(TextualConvention, Integer32):
    description = 'This describes the interface connection type. The\n                 values are arbitrary and are primarily used to\n                 identify instances of aggregate connections.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13))
    namedValues = NamedValues(("none", 0), ("unframedE1Intf", 1), ("unframedT1Intf", 2), ("aggregateIntf", 3), ("fourWireIntf", 4), ("fxoIntf", 5), ("fxsIntf", 6), ("v24AsyncIntf", 7), ("custEthernetIntf", 8), ("mgmtEthernetIntf", 9), ("syncSerialIntf", 10), ("hssControlIntf", 12), ("dropAndInsertIntf", 13))

class AprisaXEConnectionID(TextualConvention, Integer32):
    description = 'Represents a unique cross-connection identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AprisaXEPcmMode(TextualConvention, Integer32):
    description = 'The current PCM mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 10))
    namedValues = NamedValues(("pcm31c", 0), ("pcm30c", 1), ("pcm31", 2), ("pcm30", 3), ("unframed", 4), ("off", 5), ("t1sf", 6), ("t1esf", 7), ("t1sf4", 8), ("t1esf16", 10))

class AprisaXESerialEquipmentMode(TextualConvention, Integer32):
    description = 'Mode describing the behaviour of the serial interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("noCable", 0), ("dceMode", 1), ("dteMode", 2))

class AprisaXEHssSerialMode(TextualConvention, Integer32):
    description = 'Mode describing the type of serial interface, e.g. V.35.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("v11Mode", 0), ("rs530AMode", 1), ("rs530Mode", 2), ("x21Mode", 3), ("v35Mode", 4), ("rs449v36Mode", 5), ("rs232v28Mode", 6), ("noSerialCable", 7))

class AprisaXE2WireSignalState(TextualConvention, Integer32):
    description = 'This indicates the state of the CAS signalling bits\n                 as normal, inverted and disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("fxTransNormal", 0), ("fxTransInvert", 1), ("fxForcedNormal", 2), ("fxForcedInvert", 3))

class AprisaXEEthernetPortNumber(TextualConvention, Integer32):
    description = 'Ethernet port numbers.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("eth1", 1), ("eth2", 2), ("eth3", 3), ("eth4", 4))

class AprisaXEEthernetGroup(TextualConvention, Integer32):
    description = 'Used for Ethernet groupings.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("user1", 1), ("user2", 2), ("user3", 3), ("user4", 4), ("userAndMgmt", 5))

class AprisaXEEthernetFrameRate(TextualConvention, Integer32):
    description = 'The frame rate limits allowed by the Marvell switch.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unlimited", 0), ("limit128kbps", 1), ("limit256kbps", 2), ("limit512kbps", 3), ("limit1Mbps", 4), ("limit2Mbps", 5), ("limit4Mbps", 6), ("limit8Mbps", 7))

class AprisaXEEthernetPortPriority(TextualConvention, Integer32):
    description = 'Indicates the bandwidth allocated to a port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3, 5, 7))
    namedValues = NamedValues(("fromFrame", 0), ("low", 1), ("medium", 3), ("high", 5), ("vHigh", 7))

class AprisaXEEthernetGrouping(TextualConvention, Integer32):
    description = 'Indicates whether Ethernet Grouping is enabled or disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ethGroupDisabled", 0), ("ethGroupEnabled", 1))

class AprisaXEEthernetPrioQueueScheduling(TextualConvention, Integer32):
    description = 'Indicates the QOS priority scheduling scheme.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("weighted", 0), ("strict", 1))

class AprisaXEEthernetPrioQueueMapping(TextualConvention, Integer32):
    description = 'Indicates the QOS priority mapping scheme.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("standard", 0), ("cisco", 1))

class AprisaXEDefaultAction(TextualConvention, Integer32):
    description = 'Indicates whether, or not, MIB values should be defaulted.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("dontSetToDefaults", 0), ("setToDefaults", 1))

class AprisaXEQuadJetLoopbacks(TextualConvention, Integer32):
    description = 'This indicates the E1 loopback setting on a port; \n                   OFF, Line or Radio Facing.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("e1LoopbacksOff", 0), ("e1LineLoopbackOn", 1), ("e1RadioLoopbackOn", 2))

class AprisaXECCActivationStatus(TextualConvention, Integer32):
    description = 'Indicates the current state of cross connect \n                   activation for the port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ccActivated", 0), ("ccActivationFailed", 1), ("ccBusyActivating", 2))

class AprisaXESysSoftwareStatus(TextualConvention, Integer32):
    description = 'Indicates consistency of inventory file and system software.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("sysInventoryConsistent", 0), ("sysInventoryInconsistent", 1))

class AprisaXEPSCActiveRadio(TextualConvention, Integer32):
    description = 'This indicates the active radio for the PSC card.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 0, 2))
    namedValues = NamedValues(("autoSelect", 1), ("manualA", 0), ("manualB", 2))

class AprisaXEPSCActiveTx(TextualConvention, Integer32):
    description = 'This indicates the active transmitter card.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("txa", 0), ("txb", 1))

mibBuilder.exportSymbols("APRISAXE-TC-4RF", AprisaXE2WireSignalState=AprisaXE2WireSignalState, AprisaXE4WInputLevel=AprisaXE4WInputLevel, AprisaXE4WOutputLevel=AprisaXE4WOutputLevel, AprisaXE4WRxGain=AprisaXE4WRxGain, AprisaXE4WTxGain=AprisaXE4WTxGain, AprisaXEAdcVoltage=AprisaXEAdcVoltage, AprisaXEAdpcmCompression=AprisaXEAdpcmCompression, AprisaXEAlarmMapping=AprisaXEAlarmMapping, AprisaXEAlarmOutput=AprisaXEAlarmOutput, AprisaXEAlarmPolarity=AprisaXEAlarmPolarity, AprisaXEAlarmSource=AprisaXEAlarmSource, AprisaXEAlarmType=AprisaXEAlarmType, AprisaXECCActivationStatus=AprisaXECCActivationStatus, AprisaXECardType=AprisaXECardType, AprisaXEChannelControlType=AprisaXEChannelControlType, AprisaXEConnectionID=AprisaXEConnectionID, AprisaXEDataStatus=AprisaXEDataStatus, AprisaXEDbValue=AprisaXEDbValue, AprisaXEDefaultAction=AprisaXEDefaultAction, AprisaXEEthernetFrameRate=AprisaXEEthernetFrameRate, AprisaXEEthernetGroup=AprisaXEEthernetGroup, AprisaXEEthernetGrouping=AprisaXEEthernetGrouping, AprisaXEEthernetPortNumber=AprisaXEEthernetPortNumber, AprisaXEEthernetPortPriority=AprisaXEEthernetPortPriority, AprisaXEEthernetPrioQueueMapping=AprisaXEEthernetPrioQueueMapping, AprisaXEEthernetPrioQueueScheduling=AprisaXEEthernetPrioQueueScheduling, AprisaXEFXOCountry=AprisaXEFXOCountry, AprisaXEFXOInputLevel=AprisaXEFXOInputLevel, AprisaXEFXOOutputLevel=AprisaXEFXOOutputLevel, AprisaXEFXSInputLevel=AprisaXEFXSInputLevel, AprisaXEFXSOutputLevel=AprisaXEFXSOutputLevel, AprisaXEFXSPMLevel=AprisaXEFXSPMLevel, AprisaXEFXSPathMute=AprisaXEFXSPathMute, AprisaXEHardwareVersion=AprisaXEHardwareVersion, AprisaXEHssSerialMode=AprisaXEHssSerialMode, AprisaXEIQData=AprisaXEIQData, AprisaXEInterfaceCnxnType=AprisaXEInterfaceCnxnType, AprisaXEPSCActiveRadio=AprisaXEPSCActiveRadio, AprisaXEPSCActiveTx=AprisaXEPSCActiveTx, AprisaXEPcmLaw=AprisaXEPcmLaw, AprisaXEPcmMode=AprisaXEPcmMode, AprisaXEPortNumber=AprisaXEPortNumber, AprisaXEQuadJetConnectionType=AprisaXEQuadJetConnectionType, AprisaXEQuadJetLineEncoding=AprisaXEQuadJetLineEncoding, AprisaXEQuadJetLoopbacks=AprisaXEQuadJetLoopbacks, AprisaXEQuadJetMultiframeEnable=AprisaXEQuadJetMultiframeEnable, AprisaXEQuadJetTrafficType=AprisaXEQuadJetTrafficType, AprisaXEQuadJetWaveFormShapers=AprisaXEQuadJetWaveFormShapers, AprisaXESerialEquipmentMode=AprisaXESerialEquipmentMode, AprisaXESignalState=AprisaXESignalState, AprisaXESlotNumber=AprisaXESlotNumber, AprisaXESysSoftwareStatus=AprisaXESysSoftwareStatus, AprisaXETableCommand=AprisaXETableCommand, AprisaXETdmBus=AprisaXETdmBus, AprisaXETdmPortType=AprisaXETdmPortType, PYSNMP_MODULE_ID=fourRFAprisaXETCModule, fourRFAprisaXETCModule=fourRFAprisaXETCModule)
