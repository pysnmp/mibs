#
# PySNMP MIB module RS-XX8000-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/RS-XX8000-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu May 30 02:21:10 2024
# On host fv-az775-912 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rsRegModules, rsProdBroadcastTransmitter = mibBuilder.importSymbols("RS-COMMON-MIB", "rsRegModules", "rsProdBroadcastTransmitter")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Unsigned32, Integer32, IpAddress, Counter32, ModuleIdentity, Bits, NotificationType, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Integer32", "IpAddress", "Counter32", "ModuleIdentity", "Bits", "NotificationType", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Counter64")
TruthValue, TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "DateAndTime")
rsXx8000MibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2566, 149, 1, 163))
rsXx8000MibModule.setRevisions(('2011-05-11 08:00', '2011-02-23 08:00', '2010-05-06 08:00', '2009-12-08 08:00', '2009-09-10 08:00', '2009-06-26 09:00', '2009-06-03 09:00', '2009-04-30 09:00', '2009-03-13 09:00', '2009-02-10 16:00', '2008-12-12 14:00', '2008-10-20 09:00', '2008-10-10 09:00', '2008-09-30 09:00', '2008-09-03 09:00', '2008-07-23 15:30', '2008-06-16 09:00', '2008-06-10 08:00', '2008-06-02 10:30', '2008-05-13 15:00', '2008-04-23 11:00', '2008-02-18 13:30', '2008-02-11 12:00', '2008-02-06 12:00', '2007-12-17 12:00', '2007-10-02 10:00', '2007-09-04 13:00', '2007-06-29 10:00', '2007-05-16 10:00', '2007-03-14 10:00', '2006-12-21 10:00', '2006-11-20 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsXx8000MibModule.setRevisionsDescriptions(('FailDelayMode, FailDelayStatus added', 'trapSinkInformUnacknowledged obsoleted', 'ntpSyncFailed, indexProgram added', 'excSFNIdleRegulation, excInput1Available, excInput2Available,\n                excInput1LPAvailable, excInput2LPAvailable added to\n                LogbookEntryMessagesExcTv', "new value 'inconsistent' for textual convention TvStandard\n                additional values for LogbookEntryMessagesNetCCU", 'new textual convention InputSource', 'intPwrSupply, extPwrSupply added to LogbookEntryMessagesNetCCU;\n                rackTemperatureWarning added to LogbookEntryMessagesOST', 'Sx801 messages added to LogbookEntryMessagesExcTv', 'reserveInputLost added to LogbookEntryMessagesExcTv\n                rackProbeNotCalibrated added to LogbookEntryMessagesOST\n                update LogbookEntryMessagesNSU\n                update LogbookEntryMessagesNetCCU', 'add to eventHistoryModule: gps, dvbRecMon, gpParIO\n                LogbookEntryMessagesExcTv updated', 'new: swMaintenance and eventTx,\n                rackExtCoolingWarning renamed to rackGpiWarning\n                rackExtCoolingFault renamed to rackGpiFault', 'LogbookEntryMessagesNSU:\n                antennaRedundancySumWarning(196)\n                tcbTxBPowerSupply(197)\n                txBPosition(198)\n                antennaRedundancySumFault(226)\n                LogbookEntryMessagesNetCCU:\n                monitorFaultExcA(107)\n                monitorFaultExcA(108)', "eventHistoryTable with new index 'eventHistoryTxIdx'", 'NTP configuration', 'eventHistoryModule: additional values for pump and antenna', "- new TC 'AtvStandard'\n                - obsoleted TC LogbookEntryMessagesExcATV and DVB\n                  -> use LogbookEntryMessagesExcTv", "new TC 'TvStandard'", 'dateTime with UTC values\n                LogbookMaxEntryNumber: range to max 255', 'LogbookEntryMessagesExcTv extended', 'LogbookEntryMessagesExcTv extended\n                added TrapHandling under snmpConfig', 'new TC EqualizerCalibrationState\n                new TC LogbookEntryMessagesExcTv\n                remove LogbookEntryMessagesExcMediaFLO', 'add A8 to IndexTransmitter', 'updated LogbookEntryMessagesExcATV, added LockState', 'update LogbookEntryMessagesExcMediaFLO\n                add transmitterConfig with dateTime\n                new TCs: TimeOfDay and NoValue', 'update LogbookEntryMessagesNSU\n                update LogbookEntryMessagesNetCCU\n                new TCs: ProdInfoModuleNameTv and ProdInfoModuleNameFm', 'extend trapSinkTable\n                extend LogbookEntryMessagesOST (2 new messages for PumpUnit)', 'Added logbook messages for PumpUnit and \n                logbook messages (TC) for MediaFLO.', 'Enhanced logbook messages for ExcFM.', 'Added logbook messages (TC) for XV703 transposers.', 'Enhanced logbook messsages for ExcDVB and ExcFM (TextualConvention).', 'Added IndexAB for easier handling of exciterA/B and outputstageA/B in other MIBs.', 'This is the initial version.',))
if mibBuilder.loadTexts: rsXx8000MibModule.setLastUpdated('201105110800Z')
if mibBuilder.loadTexts: rsXx8000MibModule.setOrganization('Rohde&Schwarz GmbH & Co. KG')
if mibBuilder.loadTexts: rsXx8000MibModule.setContactInfo('Torsten Huebscher\n                Department 7TS2\n                Broadcasting Division\n                Muehldorfstrasse 15\n                81671 Munich, Germany\n                torsten.huebscher@rohde-schwarz.com')
if mibBuilder.loadTexts: rsXx8000MibModule.setDescription('This MIB defines general objects of XX8000 transmitting systems from Rohde & Schwarz.\n                \n                Use this MIB for things all transmitters support via SNMP, e.g.:\n                - product information\n                - installation / configuration issues (trapsinks, managers aso.)\n                \n                The following MIBs are related to this:\n                - RS-COMMON-MIB         - mandatory for this MIB.')
class ReadableString(TextualConvention, OctetString):
    description = 'An octet string containing a human-readable string.  This\n                string may have originally been encoded as specified\n                in EN 300 468 Annex A, but this is not a requirement.\n                \n                To maintain generality, the information is represented\n                using the ISO/IEC IS 10646-1 character set, encoded as an\n                octet string using the UTF-8 transformation format\n                described in RFC2279.\n                \n                Control codes are interpreted as specified in EN 300 468\n                Annex A, section A.1.  The interpretation of other control\n                codes is undefined.\n                \n                For information encoded in 7-bit US-ASCII, the UTF-8\n                encoding is identical to the US-ASCII encoding.\n                \n                UTF-8 may require multiple bytes to represent a single\n                character/code point; thus the length of this object in\n                octets may be different from the number of characters\n                encoded.  Similarly, size constraints refer to the number\n                of encoded octets, not the number of characters represented\n                by an encoding.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class FloatingPoint(TextualConvention, OctetString):
    description = "FloatingPoint provides a way of representing non-integer\n                numbers in SNMP. Numbers are represented as a string of\n                ASCII characters in the natural way. So for example, '3',\n                '3.142' and '0.3142E1' are all valid numbers.\n                \n                The syntax for the string is as follows.  [] enclose an\n                optional element, | is the separator for a set of\n                alternatives.  () enclose syntax which is to be viewed\n                as a unit.\n                \n                FloatingPoint ::= [Sign]\n                                  (Float1 | Float2 | DigitSequence)\n                                  [ExponentPart]\n                \n                Float1        ::= DigitSequence '.' [DigitSequence]\n                Float2        ::= '.' DigitSequence\n                DigitSequence ::= Digit [DigitSequence]\n                \n                ExponentPart  ::= ('e' | 'E') [Sign] DigitSequence\n                \n                Digit         ::= '0'..'9'\n                Sign          ::= '+' | '-'"
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 63)

class TimeOfDay(TextualConvention, OctetString):
    description = 'A time of day specification.\n                \n                 octets  contents    range\n                 ------  --------    -----\n                   1      hour       0..23\n                   2      minute     0..59\n                   3      second     0..59\n                \n                For example, 1:30:17 PM would be displayed as 13:30:17.\n                \n                The second can be omitted.\n                '
    status = 'current'
    displayHint = '1d:1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(2, 2), ValueSizeConstraint(3, 3), )
class EventMask(TextualConvention, Integer32):
    description = 'Enables / Disables this event.\n                enable(1)  --> active, will be sent in case the event occurs\n                disable(2) --> inactive, will not be sent in case the event occurs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class EventPriority(TextualConvention, Integer32):
    description = 'The priority of the event.\n                Users can freely set this value in range 0..255.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class EventClass(TextualConvention, Integer32):
    description = "These are the levels of events a transmitter has.\n                Info(3): Are events which only inform about changes, e.g. 'local/remote'\n                  or 'reboot of the control unit'. They don't affect the transmission.\n                Warning(2): Are minor problems which do not influence transmission itself,\n                  but may cause a bigger problem when no action is taken, e.g.\n                  'RF Loop Program'. Warnings may appear and disappear without the need\n                  of acknowledgment.\n                Fault(1): Have a direct impact on the transmission, e.g.\n                  'failure power supply'. Faults never disappear without acknowledgment."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fault", 1), ("warning", 2), ("info", 3))

class EventState(TextualConvention, Integer32):
    description = 'The current state of an event:\n                    active(1)   --> event is active (coming)\n                    inactive(2) --> event is inactive (going)\n                This is used in all logbooks and in all event handling tables.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

class EventMaxEntryNumber(TextualConvention, Integer32):
    description = 'The maximum number of events.\n                This is used in other MIBs as a placeholder.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 999)

class SwitchOnOff(TextualConvention, Integer32):
    description = 'This is for all on/off-switches.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class Trigger(TextualConvention, Integer32):
    description = 'Trigger for starting a certain action.\n                idle(1)    --> ready, do nothing\n                trigger(2) --> do now\n                \n                A GET will always return idle(1). \n                A SET idle(1) will return NO_ERROR without doing anything.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("idle", 1), ("trigger", 2))

class LogbookEntryMessagesNetCCU(TextualConvention, Integer32):
    description = 'Inserted information in the logbook of NetCCU.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 30, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 70, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 107, 108, 109))
    namedValues = NamedValues(("local", 3), ("rfOn", 4), ("excAutoReady", 6), ("excAutoChanged", 7), ("ostAutoReady", 8), ("ostAutoChanged", 9), ("rfOnSound1", 10), ("rfOnSound2", 11), ("activeExcA", 12), ("activeExcB", 13), ("activeOstA", 14), ("activeOstB", 15), ("rfOnVision", 16), ("rfOnActiveExc", 17), ("rfOnDLoad", 18), ("rfOkDLoad", 19), ("swBackupStarted", 20), ("swBackupDone", 21), ("swBackupFailed", 22), ("swRestoreStarted", 23), ("swRestoreDone", 24), ("swRestoreFailed", 25), ("optionKeyExpired", 30), ("txModeSwitchOverStarted", 37), ("txModeSwitchOverEnded", 38), ("reboot", 40), ("rfLoopProgram", 41), ("rfLoopReserve", 42), ("rfWarning", 43), ("reflectionWarning", 44), ("intPwrSupply", 45), ("extPwrSupply", 46), ("rfVisionWarning", 47), ("rfSound1Warning", 48), ("rfSound2Warning", 49), ("fanFault", 51), ("sumWarningRec", 52), ("sumWarningExcA", 53), ("sumWarningExcB", 54), ("sumWarningOstA", 55), ("sumWarningOstB", 56), ("rfDLoadWarning", 57), ("rfDLoadReflection", 58), ("receiverConnect", 59), ("receiverSumFault", 60), ("txModeInconsistent", 61), ("boardTemperatureWarning", 62), ("optionKeyWillExpire", 70), ("powerSupply", 81), ("rfFail", 82), ("reflectionFault", 83), ("boardTemperature", 84), ("excSwitch", 85), ("ostSwitch", 86), ("connectionExcA", 87), ("connectionExcB", 88), ("connectionOstA", 89), ("connectionOstB", 90), ("rfVision", 91), ("rfSound1Fault", 92), ("rfSound2Fault", 93), ("connectionRec", 95), ("summaryFaultRec", 96), ("summaryFaultExcA", 97), ("summaryFaultExcB", 98), ("summaryFaultOstA", 99), ("summaryFaultOstB", 100), ("rfDLoadFault", 101), ("rfDLoadReflectionFault", 102), ("apaConnect", 103), ("absorber", 104), ("monitorFaultExcA", 107), ("monitorFaultExcB", 108), ("txModeSwitchOverFailed", 109))

class LogbookEntryMessagesExcTv(TextualConvention, Integer32):
    description = 'Inserted information in the logbook of TV exciters.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 170, 171, 172, 173, 174, 175, 176, 177, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 205, 210, 211, 212, 213, 214, 215, 220, 221, 222, 223, 230, 231, 240, 241, 250, 251, 256, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 280, 300, 301, 320, 321, 322, 323, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 500, 501, 502, 503, 550, 551, 552, 553, 554, 555, 556, 557, 600, 601, 602, 603, 604, 605, 606, 607, 608, 640, 641, 642, 643, 644, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710), SingleValueConstraint(711, 712, 713, 714, 715, 716, 717, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 770, 771, 772, 800, 801, 802, 803, 804, 805, 806, 807, 808))
    namedValues = NamedValues(("excReboot", 0), ("excSumFault", 1), ("excSumWarning", 2), ("excLocal", 3), ("excExciterOn", 4), ("excRfOk", 5), ("excNoInput", 6), ("excReference", 7), ("excRfOn", 8), ("excMute", 9), ("excRelieveReq", 10), ("excSwDiag", 11), ("excOneFan", 12), ("excNoCCUComm", 13), ("excSwUpdated", 14), ("excBiosUpdated", 15), ("excPowerSupply", 16), ("excTemperature", 17), ("excFans", 18), ("excHwMainboard", 19), ("excHwCfCard", 20), ("excOutputOpen", 21), ("excRebootRqst", 22), ("excHwEEPROM", 23), ("excWatchdog", 24), ("excRfFail", 25), ("excLoopOpen", 26), ("excNoFPGA", 27), ("excCarrierLock", 28), ("excInputFail", 30), ("excOptionExpired", 37), ("excOptionWillEnd", 38), ("excFPGAConfig", 40), ("excHwIIFBoard", 41), ("excHwRfBoard", 42), ("excHwSynth1", 43), ("excHwSynth2", 44), ("excHwSynth3", 45), ("excMuteAudio1", 46), ("excMuteAudio2", 47), ("excVideoInp1", 48), ("excVideoInp2", 49), ("excVideoInpAct", 50), ("excRfOutExcV", 51), ("excRfOutAntV", 52), ("excRfOutExcA1", 53), ("excRfOutAntA1", 54), ("excRfOutExcA2", 55), ("excRfOutAntA2", 56), ("excClippingAntInp", 57), ("excNoHeadroomAnt", 58), ("excAudioMode", 59), ("excWhiteLine", 60), ("excWhiteLineLnAmp", 61), ("excWhiteLineLnAmpW", 62), ("excSyncCheck", 63), ("excWhiteLimiter", 64), ("excDevLimAud1", 65), ("excDevLimAud2", 66), ("excVideoInpClip", 67), ("excAud1InpClip", 68), ("excAud2InpClip", 69), ("excNICAM728Data", 70), ("excNICAM728Carr", 71), ("excAud2OutClip", 72), ("excRfMonFail", 73), ("excRfVideoFail", 74), ("excRfAudio1Fail", 75), ("excRfAudio2Fail", 76), ("excAudioLoopOpen", 77), ("excVideoLoopOpen", 78), ("excTestMode", 100), ("excExtRefFail", 101), ("excExtRefWeak", 102), ("excExtPPSFail", 103), ("excInputSwitched", 104), ("excInputFail2", 105), ("excWrongDatarate", 106), ("excFifoOverUnderflow", 107), ("excDelayChanged", 108), ("excSFNDelay", 109), ("excNoMIP", 110), ("excWrongMFArrivalTime", 111), ("excExtPPSAsynchron", 112), ("excPacketUnlock", 113), ("excMaxDelayChanged", 114), ("excReferenceAbsent", 115), ("excNoPPS", 116), ("excRfFailAmplifier", 117), ("excWarningAmplifier", 118), ("excAmpOverflow", 119), ("excModError", 120), ("excFLOModErr", 121), ("excInput1", 122), ("excInput2", 123), ("excInput1LP", 124), ("excInput2LP", 125), ("excNoReserveAvailable", 126), ("excSynthesizerUnlocked", 127), ("excSFNIdleRegulation", 128), ("excAmpVSWR", 170), ("excAmpTempWarn", 171), ("excAmpTempFault", 172), ("excAmpRegulation", 173), ("excAmpTransistor", 174), ("excAmpReducedPower", 175), ("excHWAmpEEPROM", 176), ("excRFWarningAmp", 177), ("excModSfnRAMInitErr", 180), ("excModTransportErr", 181), ("excModFIFOParErr", 182), ("excModFIFOSeqErr", 183), ("excModSfnBufEmpty", 184), ("excModSfnBufFull", 185), ("excModSsfMultiple", 186), ("excModSsfMissing", 187), ("excModLofTS1", 188), ("excModLofTS2", 189), ("excModCoreStall", 190), ("excModIqInactive", 191), ("excModMtiVersErr", 192), ("excModCoreReset", 193), ("excModConfigChanged", 194), ("excSFNBuffer", 195), ("excModIdleMode", 196), ("excSFNBufferTooEmpty", 197), ("excModMemError", 198), ("excSfnBufferTooFull", 199), ("excMissingSIP", 205), ("excTCLevelOutOfRange", 210), ("excTCLevelOverflow", 211), ("excInputFail3", 212), ("excInputWarning", 213), ("excEchoWarning", 214), ("xlxInputStepProtection", 215), ("excExt1PPSReference", 220), ("excInt1PPSReference", 221), ("exc5MHzReference", 222), ("exc10MHzReference", 223), ("excPrecorrectionSetupInfo", 230), ("excPrecorrectionSetupFail", 231), ("excFramecounter", 240), ("excMissingIIP", 241), ("excPSUOvertemp", 250), ("excPowerSupplyWarning", 251), ("excNSUConnected", 256), ("excMonHWError", 260), ("excRecvRxAUXHWError", 261), ("excRecvHWError", 262), ("excMonNoFrontendLock", 263), ("excRecvAUXNoFrontendLock", 264), ("excRecvNoFrontendLock", 265), ("excMonBadInputSignal", 266), ("excRecvAUXBadInputSignal", 267), ("excRecvBadInputSignal", 268), ("excMonNoInputSignal", 269), ("excRecvAUXWarningInputSignal", 270), ("excRecvWarningInputSignal", 271), ("excMonAUXHWError", 272), ("excMonAUXNoFrontendLock", 273), ("excMonAUXBadInputSignal", 274), ("excMonitorNoInputFail", 280), ("excNoSfnData", 300), ("excNoMobileDtvContent", 301), ("excInput1Available", 320), ("excInput2Available", 321), ("excInput1LPAvailable", 322), ("excInput2LPAvailable", 323), ("excRfTest", 400), ("excPRBSInsertion", 401), ("excTestEnsemble", 402), ("excInvalidTII", 403), ("excTIITransmission", 404), ("excTxModeChange", 405), ("excTIIChange", 406), ("excNullTIST", 407), ("excTISTJitter", 408), ("excTS1FrameLock", 409), ("excTS2FrameLock", 410), ("excCrcViolationRateTooHigh", 411), ("excSeamlessReady", 412), ("excTestFIC", 413), ("dvbt2NoL1Present", 500), ("dvbt2InvalidConfiguration", 501), ("dvbT2UnsupportedConfiguration", 502), ("dvbt2BandwidthMismatch", 503), ("iqHeader1Integrity", 550), ("iqHeader2Integrity", 551), ("iqHeader1Issues", 552), ("iqHeader2Issues", 553), ("iqInputRegulation", 554), ("iqWrongConfiguration", 555), ("iqTseMute", 556), ("iqInputOrder", 557), ("sx801PowerFail7Vpositive", 600), ("sx801PowerFail7Vnegative", 601), ("sx801PowerFail12V", 602), ("preAmpTemperatureFault", 603), ("preAmpRFFault", 604), ("parIoExcLink", 605), ("parIoTxLink", 606), ("parIoGpIoLink", 607), ("rfBoardRFFault", 608), ("sx801PhaseError", 640), ("sx801ReflectionWarning", 641), ("sx801ReflectionFault", 642), ("sx801RfWarning", 643), ("sx801AmplShutdown", 644), ("sx801PA1Supply1TooHot", 650), ("sx801PA1Supply2TooHot", 651), ("sx801PA1ReserveSupplyTooHot", 652), ("sx801PA1Supply1Fail", 653), ("sx801PA1Supply2Fail", 654), ("sx801PA1ReserveSupplyFail", 655), ("sx801PA1AcFail", 656), ("sx801PA1BlowerFail", 657), ("sx801PA1TransistorFail", 658), ("sx801PA1DriverFail", 659), ("sx801PA1RfInFail", 660), ("sx801PA1Reflection", 661), ("sx801PA1VSWR", 662), ("sx801PA1PowerFail", 663), ("sx801PA1Regulation", 664), ("sx801PA1Temperature", 665), ("sx801PA1Communication", 666), ("sx801PA1Update", 667), ("sx801PA2Supply1TooHot", 675), ("sx801PA2Supply2TooHot", 676), ("sx801PA2ReserveSupplyTooHot", 677), ("sx801PA2Supply1Fail", 678), ("sx801PA2Supply2Fail", 679), ("sx801PA2ReserveSupplyFail", 680), ("sx801PA2AcFail", 681), ("sx801PA2BlowerFail", 682), ("sx801PA2TransistorFail", 683), ("sx801PA2DriverFail", 684), ("sx801PA2RfInFail", 685), ("sx801PA2Reflection", 686), ("sx801PA2VSWR", 687), ("sx801PA2PowerFail", 688), ("sx801PA2Regulation", 689), ("sx801PA2Temperature", 690), ("sx801PA2Communication", 691), ("sx801PA2Update", 692), ("pa3Supply1TooHot", 700), ("pa3Supply2TooHot", 701), ("pa3ReserveSupplyTooHot", 702), ("pa3Supply1Fault", 703), ("pa3Supply2Fault", 704), ("pa3ReserveSupplyFault", 705), ("pa3ACFault", 706), ("pa3BlowerFault", 707), ("pa3TransistorFault", 708), ("pa3DriverFault", 709), ("pa3RFinFault", 710)) + NamedValues(("pa3Reflection", 711), ("pa3VSWR", 712), ("pa3PowerFault", 713), ("pa3Regulation", 714), ("pa3Temperature", 715), ("pa3Communication", 716), ("pa3Update", 717), ("pa4Supply1TooHot", 725), ("pa4Supply2TooHot", 726), ("pa4ReserveSupplyTooHot", 727), ("pa4Supply1Fault", 728), ("pa4Supply2Fault", 729), ("pa4ReserveSupplyFault", 730), ("pa4ACFault", 731), ("pa4BlowerFault", 732), ("pa4TransistorFault", 733), ("pa4DriverFault", 734), ("pa4RFinFault", 735), ("pa4Reflection", 736), ("pa4VSWR", 737), ("pa4PowerFault", 738), ("pa4Regulation", 739), ("pa4Temperature", 740), ("pa4Communication", 741), ("pa4Update", 742), ("tse800NoConnect", 770), ("tse800Warning", 771), ("tse800Fault", 772), ("automaticOn", 800), ("automaticFault", 801), ("autoCtrlExcActive", 802), ("autoPrgmExcActive", 803), ("changeoverByUser", 804), ("changeoverByAuto", 805), ("automaticReady", 806), ("autoPrgmExcNoConnect", 807), ("autoPrgmExcFault", 808))

class LogbookEntryMessagesExcDVB(TextualConvention, Integer32):
    description = 'Inserted information in the logbook of DVB exciters.\n                \n                This is obsolete! Please use LogbookEntryMessagesExcTv!'
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 16, 17, 18, 19, 20, 21, 23, 25, 26, 28, 30, 37, 38, 40, 41, 42, 43, 44, 45, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 127))
    namedValues = NamedValues(("excReboot", 0), ("excSummaryFault", 1), ("excSummaryWarning", 2), ("excLocal", 3), ("excOn", 4), ("excRfOk", 5), ("excNoInput", 6), ("excReferenceFail", 7), ("excRfOn", 8), ("excMute", 9), ("excFanWarning", 12), ("excNoCommunicationToNetCCU", 13), ("excPowerSupply", 16), ("excBoardTemperature", 17), ("excFanFault", 18), ("excSelfTest", 19), ("excHwCfCard", 20), ("excOutputOpen", 21), ("excHwEeprom", 23), ("excRfFail", 25), ("excLoop", 26), ("excCarrierLock", 28), ("excInputFault", 30), ("excOptionExpired", 37), ("excOptionExpires", 38), ("excHwFpgaConfig", 40), ("excHwIifBoard", 41), ("excHwRfBoard", 42), ("excHwSynth1", 43), ("excHwSynth2", 44), ("excHwSynth3", 45), ("excTestMode", 100), ("excExtRefFail", 101), ("excExtRefWeak", 102), ("excExtPPSFail", 103), ("excWrongConfig", 104), ("excInputFail", 105), ("excWrongDatarate", 106), ("excFifoWarning", 107), ("excExtDelayChanged", 108), ("excWrongDelay", 109), ("excNoMIP", 110), ("excWrongMFArrivalTime", 111), ("excExtPPSAsynchron", 112), ("excPacketUnlock", 113), ("excMaxDelayChanged", 114), ("excNoReference", 115), ("excNoPPS", 116), ("excRfFailAmplifier", 117), ("excWarningAmplifier", 118), ("excOverflowAmplifier", 119), ("excSynthUnlock", 127))

class LogbookEntryMessagesExcFM(TextualConvention, Integer32):
    description = 'Inserted information in the logbook of FM exciters.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 15, 16, 21, 23, 25, 26, 27, 28, 30, 32, 33, 34, 36, 37, 38, 41, 42, 43, 47, 48, 49, 50, 51, 67, 71, 81, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125))
    namedValues = NamedValues(("excReboot", 0), ("excSummaryFault", 1), ("excSummaryWarning", 2), ("excLocal", 3), ("excOn", 4), ("excRfOk", 5), ("excNoInput", 6), ("excReferenceFail", 7), ("excRfOn", 8), ("excMute", 9), ("excNoCommunicationToNetCCU", 13), ("excBiosUpdated", 15), ("excPowerSupply", 16), ("excOutputOpen", 21), ("excEEPROMError", 23), ("excRfFail", 25), ("excLoop", 26), ("excFPGANotLoaded", 27), ("excCarrierLock", 28), ("excInputFault", 30), ("ostSummaryFault", 32), ("excSoftFault", 33), ("ostSoftFault", 34), ("ostSummaryWarning", 36), ("excOptionKeyExpired", 37), ("excOptionKeyWarning", 38), ("excTemperatureWarning", 41), ("excTemperatureFault", 42), ("excRfUnitFault", 43), ("excFan1NotOk", 47), ("excFan2NotOk", 48), ("excMainPLLUnlocked", 49), ("excMainUPCUnlocked", 50), ("excMainCLKUnlocked", 51), ("exc12VFanWarning", 67), ("exc12VRackControllerWarning", 71), ("excInfoFrequencyChanged", 81), ("excLevelAESLeftTooLow", 84), ("excLevelAESRightTooLow", 85), ("excLevelMPXTooLow", 86), ("excNoDataInput", 87), ("excLevelAFLeftTooLow", 88), ("excLevelAFRightTooLow", 89), ("excLevelAUX1TooLow", 90), ("excLevelAUX2TooLow", 91), ("excLevelAUX3TooLow", 92), ("excLevelAESLeftTooHigh", 93), ("excLevelAESRightTooHigh", 94), ("excLevelMPXTooHigh", 95), ("excLevelAFLeftTooHigh", 97), ("excLevelAFRightTooHigh", 98), ("excLevelAUX1TooHigh", 99), ("excLevelAUX2TooHigh", 100), ("excLevelAUX3TooHigh", 101), ("excAESNoClock", 102), ("excAESParityBiphaseError", 103), ("excAESStateNotValid", 104), ("excInpCh1NotOk", 105), ("excInpCh2NotOk", 106), ("excInpCh1Active", 107), ("excInpCh2Active", 108), ("excInpAutomaticActive", 109), ("recSummaryWarning", 110), ("recSummaryFault", 111), ("ostRfPresent", 112), ("recRfWarning", 113), ("recCarrierNotPresent", 114), ("recNoConnection", 115), ("ostRfWarn", 116), ("ostRfFault", 117), ("ostNoInput", 118), ("recRfFault", 119), ("recRfPresent", 120), ("ostPowerRegulationActive", 121), ("ostTemperatureWarning", 122), ("ostSwrWarning", 123), ("ostSwrFault", 124), ("ostNoConnection", 125))

class LogbookEntryMessagesOST(TextualConvention, Integer32):
    description = 'Inserted information in the logbook of outputstage.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129))
    namedValues = NamedValues(("ostRfOn", 42), ("ostRfOk", 43), ("ostRfReduced", 44), ("ostNoInput", 45), ("ostRfWarning", 46), ("ostReflectionWarning", 47), ("ostRackWarning", 48), ("ostCoolingWarning", 49), ("ostRfFail", 50), ("ostReflectionFault", 51), ("ostACFault", 52), ("ostCoolingFault", 53), ("ostCommunicationFault", 54), ("rackLinkOk", 58), ("rackOn", 59), ("reducedRfExcA", 60), ("reducedRfExcB", 61), ("rackGpiWarning", 62), ("rackFan1Fault", 63), ("rackFan2Fault", 64), ("rackCoolingSumWarning", 65), ("rackAmplifierSumFault", 66), ("rackGpiFault", 67), ("rackTemperatureFault", 68), ("rackACFault", 69), ("rackCoolingSumFault", 70), ("rackTempFaultAbs1", 71), ("rackTempFaultAbs2", 72), ("rackDCFault", 73), ("ampNumberDiffers", 76), ("ampOn", 77), ("ampDCOk", 78), ("ampACOk", 79), ("ampRfInFail", 80), ("ampRfFail", 81), ("ampReflectionFault", 82), ("ampTemperatureFault", 83), ("ampFanFault", 84), ("ampTransistorFault", 85), ("pucFault", 86), ("pucWarning", 87), ("pucLink", 88), ("pucFan1Link", 89), ("pucFan2Link", 90), ("pucFan3Link", 91), ("pucFan4Link", 92), ("pucPump1Link", 93), ("pucPump2Link", 94), ("pucOn", 95), ("pucFan1", 96), ("pucFan2", 97), ("pucFan3", 98), ("pucFan4", 99), ("pucPump1", 100), ("pucPump2", 101), ("pucPressure", 102), ("pucMaintenance", 103), ("pucConfig", 104), ("pucFan1Fault", 105), ("pucFan2Fault", 106), ("pucFan3Fault", 107), ("pucFan4Fault", 108), ("pucPump1Fault", 109), ("pucPump2Fault", 110), ("pucPressureFault", 111), ("pucFilter", 117), ("pucPuOff", 118), ("rackProbeNotCalibrated", 119), ("rackTemperatureWarning", 120), ("rackSumFault", 121), ("rackAbsorberFault", 122), ("rackOvervoltageProtection", 123), ("psu1Fault", 124), ("psu2Fault", 125), ("psuRFault", 126), ("ampDriverFault", 127), ("ctxPowerFault", 128), ("ampRegulationFault", 129))

class LogbookEntryMessagesNSU(TextualConvention, Integer32):
    description = 'Inserted information in the logbook of Nplus1-Switchoverunit.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 196, 197, 198, 200, 201, 226))
    namedValues = NamedValues(("local", 3), ("automaticOn", 5), ("automaticReady", 6), ("automaticChangeover", 7), ("swBackupStarted", 10), ("program1RfOn", 11), ("program2RfOn", 12), ("program3RfOn", 13), ("program4RfOn", 14), ("program5RfOn", 15), ("program6RfOn", 16), ("program7RfOn", 17), ("program8RfOn", 18), ("programReserveRfOn", 19), ("swBackupDone", 20), ("txA1ToDummyLoad", 21), ("txA2ToDummyLoad", 22), ("txA3ToDummyLoad", 23), ("txA4ToDummyLoad", 24), ("txA5ToDummyLoad", 25), ("txA6ToDummyLoad", 26), ("txA7ToDummyLoad", 27), ("txA8ToDummyLoad", 28), ("txBToDummyLoad", 29), ("optionkeyExpired", 30), ("txA1Local", 31), ("txA2Local", 32), ("txA3Local", 33), ("txA4Local", 34), ("txA5Local", 35), ("txA6Local", 36), ("txA7Local", 37), ("txA8Local", 38), ("txBLocal", 39), ("reboot", 40), ("txA1SumWarning", 41), ("txA2SumWarning", 42), ("txA3SumWarning", 43), ("txA4SumWarning", 44), ("txA5SumWarning", 45), ("txA6SumWarning", 46), ("txA7SumWarning", 47), ("txA8SumWarning", 48), ("txBSumWarning", 49), ("swBackupFailed", 50), ("txA1NoConnect", 51), ("txA2NoConnect", 52), ("txA3NoConnect", 53), ("txA4NoConnect", 54), ("txA5NoConnect", 55), ("txA6NoConnect", 56), ("txA7NoConnect", 57), ("txA8NoConnect", 58), ("txBNoConnect", 59), ("swRestoreStarted", 60), ("txA1SumFault", 61), ("txA2SumFault", 62), ("txA3SumFault", 63), ("txA4SumFault", 64), ("txA5SumFault", 65), ("txA6SumFault", 66), ("txA7SumFault", 67), ("txA8SumFault", 68), ("txBSumFault", 69), ("swRestoreDone", 70), ("swRestoreFailed", 80), ("connBoardTxA1Updating", 81), ("connBoardTxA2Updating", 82), ("connBoardTxA3Updating", 83), ("connBoardTxA4Updating", 84), ("connBoardTxA5Updating", 85), ("connBoardTxA6Updating", 86), ("connBoardTxA7Updating", 87), ("connBoardTxA8Updating", 88), ("connBoardTxBUpdating", 89), ("inputSwitchUpdating", 90), ("connBoardTxA1SumWarning", 91), ("connBoardTxA2SumWarning", 92), ("connBoardTxA3SumWarning", 93), ("connBoardTxA4SumWarning", 94), ("connBoardTxA5SumWarning", 95), ("connBoardTxA6SumWarning", 96), ("connBoardTxA7SumWarning", 97), ("connBoardTxA8SumWarning", 98), ("connBoardTxBSumWarning", 99), ("inputSwitchSumWarning", 100), ("fanFault", 101), ("sumWngRCV", 102), ("rcvNoConnect", 103), ("sumFltRCV", 104), ("optionkeyWillExpire", 105), ("powerSupply", 106), ("boardTemperature", 107), ("automaticFault", 108), ("rcvNoConnectx", 109), ("sumFltRCVx", 110), ("connBoardTxA1SumFault", 111), ("connBoardTxA2SumFault", 112), ("connBoardTxA3SumFault", 113), ("connBoardTxA4SumFault", 114), ("connBoardTxA5SumFault", 115), ("connBoardTxA6SumFault", 116), ("connBoardTxA7SumFault", 117), ("connBoardTxA8SumFault", 118), ("connBoardTxBSumFault", 119), ("inputSwitchSumFault", 120), ("outputSwitch", 122), ("inputSwitchChangeOver", 123), ("txBParameterSet", 124), ("antennaRedundancySumWarning", 196), ("tcbTxBPowerSupply", 197), ("txBPosition", 198), ("intPwrSupply", 200), ("extPwrSupply", 201), ("antennaRedundancySumFault", 226))

class LogbookEntryMessagesXV703(TextualConvention, Integer32):
    description = 'Inserted information in the logbook of XV703 transposers.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("noNetCCUConnection", 0), ("summaryFault", 1), ("summaryWarning", 2), ("local", 3), ("on", 4), ("ok", 5), ("fanWarning", 7), ("rfOn", 8), ("updatedBIOS", 9), ("powerSupply", 10), ("boardTemperature", 11), ("fanFault", 12), ("reboot", 14), ("loopOpen", 15), ("noConnection", 16), ("ampFail", 17), ("ifrPllFail", 18), ("rfiPllFail", 19), ("refFreqFail", 20), ("pInFail", 21), ("rfFail", 22))

class LogbookEntrySlope(TextualConvention, Integer32):
    description = 'These are the information which are inserted in the logbook.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("set", 1), ("reset", 2))

class LogbookMaxEntryNumber(TextualConvention, Integer32):
    description = 'The maximum number of entries in a logbook. \n                This is used in other MIBs as a placeholder.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class IndexTransmitter(TextualConvention, Integer32):
    description = 'This is used for Nplus1 systems to indicate a transmitter (physical view).\n                TransmitterB(1) is the reserve transmitter, transmitterA1(2) to transmitterA8(9) are the main transmitter.\n                In difference to the logical view, transmitterB(1) has special parameters available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("transmitterB", 1), ("transmitterA1", 2), ("transmitterA2", 3), ("transmitterA3", 4), ("transmitterA4", 5), ("transmitterA5", 6), ("transmitterA6", 7), ("transmitterA7", 8), ("transmitterA8", 9))

class IndexRack(TextualConvention, Integer32):
    description = 'This is used for systems with more than 1 rack to display a designated rack.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 10)

class IndexAmplifier(TextualConvention, Integer32):
    description = 'This is used to display a designated amplifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 10)

class IndexProgram(TextualConvention, Integer32):
    description = 'This is used for Nplus1 systems to indicate a program sent out (logical view).\n                ProgramRes(1) is the reserve program, program1(2) to program8(9) are the main programs.\n                In difference to the physical view, programRes(1) has no special parameters available. Furthermore it has no priority.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("programRes", 1), ("program1", 2), ("program2", 3), ("program3", 4), ("program4", 5), ("program5", 6), ("program6", 7), ("program7", 8), ("program8", 9))

class IndexAB(TextualConvention, Integer32):
    description = 'The value for the module A (exciterA, outputstageA) or \n                B (exciterB, outputstageB) for alarms.\n                This is a helper column.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("a", 1), ("b", 2))

class ProdInfoModuleNameTv(TextualConvention, Integer32):
    description = 'The product information module names for TV.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 50, 100, 101))
    namedValues = NamedValues(("exciter", 1), ("exciterMainboard", 2), ("exciterInputInterface", 3), ("exciterRfBoard", 4), ("exciterSynth1", 5), ("exciterSynth2", 6), ("exciterSynth3", 7), ("netCCU", 50), ("rackcontroller", 100), ("amplifier", 101))

class ProdInfoModuleNameFm(TextualConvention, Integer32):
    description = 'The product information module names for FM.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 50, 100, 101))
    namedValues = NamedValues(("exciter", 1), ("exciterMainboard", 2), ("exciterBootprog", 3), ("exciterBootload", 4), ("exciterOs", 5), ("exciterFpga", 6), ("netCCU", 50), ("rackcontroller", 100), ("amplifier", 101))

class ProdInfoModuleNameNsu(TextualConvention, Integer32):
    description = 'The product information module names for NSU.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(70))
    namedValues = NamedValues(("tcBoard", 70))

class LogbookEntryMessagesExcATV(TextualConvention, Integer32):
    description = 'Inserted information in the logbook of ATV exciters.\n                \n                This is obsolete! Please use LogbookEntryMessagesExcTv!'
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 25, 26, 27, 28, 30, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 100, 101, 102, 103, 104, 106, 107, 108, 109, 110, 111, 113, 114, 115, 116, 117, 118, 119, 127))
    namedValues = NamedValues(("reboot", 0), ("summaryFault", 1), ("summaryWarning", 2), ("local", 3), ("exciterOn", 4), ("rfOk", 5), ("noInput", 6), ("reference", 7), ("rfOn", 8), ("mute", 9), ("relieveReq", 10), ("oneFan", 12), ("noCcuComm", 13), ("swUpdated", 14), ("biosUpdated", 15), ("powerSupply", 16), ("temperature", 17), ("fans", 18), ("hwMainboard", 19), ("hwCfCard", 20), ("outputOpen", 21), ("hwEEPROM", 23), ("rfFail", 25), ("loopOpen", 26), ("noFPGA", 27), ("carrierLock", 28), ("inputFail", 30), ("optionExpired", 37), ("optionWillEnd", 38), ("fpgaConfig", 40), ("hwIifBoard", 41), ("hwRfBoard", 42), ("hwSynth1", 43), ("hwSynth2", 44), ("hwSynth3", 45), ("muteAudio1", 46), ("muteAudio2", 47), ("videoInput1", 48), ("videoInput2", 49), ("videoInputAct", 50), ("rfOutExcV", 51), ("rfOutAntV", 52), ("rfOutExcA1", 53), ("rfOutAntA1", 54), ("rfOutExcA2", 55), ("rfOutAntA2", 56), ("clippingAntennaInput", 57), ("noHeadroomAntenna", 58), ("audioMode", 59), ("whiteLine", 60), ("whiteLineLnAmp", 61), ("whiteLineLnAmpW", 62), ("syncCheck", 63), ("whiteLimiter", 64), ("devLimAud1", 65), ("devLimAud2", 66), ("videoInputClipping", 67), ("aud1InpClip", 68), ("aud2InpClip", 69), ("nicam728Data", 70), ("nicam728Carr", 71), ("aud2OutClip", 72), ("rfMonFail", 73), ("rfVideoFail", 74), ("rfAudio1Fail", 75), ("rfAudio2Fail", 76), ("audioLoopOpen", 77), ("videoLoopOpen", 78), ("testMode", 100), ("extRefFail", 101), ("extRefWeak", 102), ("extPpsFail", 103), ("wrongConfig", 104), ("wrongDatarate", 106), ("fifoOverUnderFlow", 107), ("delayChanged", 108), ("wrongDelay", 109), ("noMIP", 110), ("wrongMfArrivalTime", 111), ("packetUnlock", 113), ("maxDelayChanged", 114), ("referenceAbsent", 115), ("noPPS", 116), ("rfFailAmplifier", 117), ("warningAmplifier", 118), ("amplifierOverflow", 119), ("synthesizerUnlocked", 127))

class LockState(TextualConvention, Integer32):
    description = 'This is for carrier locking.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("locked", 1), ("unlocked", 2))

class EqualizerCalibrationState(TextualConvention, Integer32):
    description = 'possible precorrection equalizer calibration states'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("inactive", 1), ("active", 2), ("warning", 3), ("fail", 4))

class TvStandard(TextualConvention, Integer32):
    description = "The TV standards.\n                The value 'inconsistent' cannot be written.\n                It is shown only when switching from one standard to another in between."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 100))
    namedValues = NamedValues(("atv", 1), ("dvb", 2), ("atsc", 3), ("dtmb", 4), ("mediaFLO", 5), ("test", 6), ("dab", 7), ("isdbt", 8), ("dvbt2", 9), ("inconsistent", 100))

class AtvStandard(TextualConvention, Integer32):
    description = 'The ATV standards.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("bg", 1), ("m", 2), ("m1", 3), ("n", 4), ("dk", 5), ("i", 6), ("i1", 7), ("dkfm2", 8), ("l", 9), ("k1", 10), ("h", 11), ("b", 12), ("g", 13))

class InputSource(TextualConvention, Integer32):
    description = 'input source selection type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("bnc", 1), ("rx", 2), ("sat", 3), ("ip", 4), ("reserved", 5), ("tp", 6), ("vf", 7), ("t2Mi", 8), ("iq", 9))

class Sx801AmplifierState(TextualConvention, Integer32):
    description = 'Description.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("off", 1), ("warning", 2), ("ok", 3), ("unknown", 4))

class FailDelayMode(TextualConvention, Integer32):
    description = 'The mode how fail delay is handled.\n                always(1) - the fail delay action is always carried out after\n                            the user specified fail delay time.\n                ifQualified(2) - the fail delay action is carried out after\n                            the user specified fail delay time\n                            only if the FailDelayStatus is ok(3).\n                            Otherwise (Fail DelayStatus warning(2)) 30 minutes after GPS was lost\n                            a reference fault is signaled and the input is muted.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("always", 1), ("ifQualified", 2))

class FailDelayStatus(TextualConvention, Integer32):
    description = 'The current state of time drift prediction.\n                off(1) - not used\n                warning(2) - Availability of GPS not sufficient for time drift prediction\n                ok(3) - Time drift prediction is functional.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("warning", 2), ("ok", 3))

rsXx8000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167))
if mibBuilder.loadTexts: rsXx8000.setStatus('current')
if mibBuilder.loadTexts: rsXx8000.setDescription('The subtree for all transmitters of series 8000.')
rsXx8000Common = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1))
if mibBuilder.loadTexts: rsXx8000Common.setStatus('current')
if mibBuilder.loadTexts: rsXx8000Common.setDescription('This is the subtree for values which every equipement of series 8000 suports.')
rsXx8000CommonObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1))
productInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1))
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1, 2), ReadableString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
if mibBuilder.loadTexts: serialNumber.setDescription('The serial number of the device.')
identNumberSW = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1, 3), ReadableString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: identNumberSW.setStatus('current')
if mibBuilder.loadTexts: identNumberSW.setDescription('The Rohde&Schwarz identification number of the software, for example 2094.2090.02.')
versionNumberSW = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1, 4), ReadableString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: versionNumberSW.setStatus('current')
if mibBuilder.loadTexts: versionNumberSW.setDescription('The Rohde&Schwarz revision number of the software, for example 1.2.1.')
identNumberHW = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1, 5), ReadableString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: identNumberHW.setStatus('current')
if mibBuilder.loadTexts: identNumberHW.setDescription('The Rohde&Schwarz identification number of the hardware, for example 2095.8007.02 (NetCCU).')
versionNumberHW = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1, 6), ReadableString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: versionNumberHW.setStatus('current')
if mibBuilder.loadTexts: versionNumberHW.setDescription('The Rohde&Schwarz revision number (product index) of the hardware, for example 03.03.')
snmpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2))
trapSinkTable = MibTable((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2), )
if mibBuilder.loadTexts: trapSinkTable.setStatus('current')
if mibBuilder.loadTexts: trapSinkTable.setDescription('This table is for configuration of trapsinks - the IP-addresses where traps/informs are sent to.\n                \n                This table gives you possibility for easier remote configuration of trapsinks.\n                Another way, which is predefined by IETF, is to use the MIBs SNMP-TARGET and SNMP-NOTIFICATION.')
trapSinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1), ).setIndexNames((0, "RS-XX8000-COMMON-MIB", "trapSinkNumber"))
if mibBuilder.loadTexts: trapSinkEntry.setStatus('current')
if mibBuilder.loadTexts: trapSinkEntry.setDescription('An entry for a trapsink.')
trapSinkNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)))
if mibBuilder.loadTexts: trapSinkNumber.setStatus('current')
if mibBuilder.loadTexts: trapSinkNumber.setDescription('The arbitrary number in the list.')
trapSinkVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("v1Trap", 1), ("v2Trap", 2), ("v2Inform", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSinkVersion.setStatus('current')
if mibBuilder.loadTexts: trapSinkVersion.setDescription('The SNMP-version of sent out alarm. \n                1: v1Trap\n                2: v2Trap\n                3: v2Inform')
trapSinkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSinkAddress.setStatus('current')
if mibBuilder.loadTexts: trapSinkAddress.setDescription('The IP-Address of the SNMP manager to which the alarms are sent to.')
trapSinkPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSinkPort.setStatus('current')
if mibBuilder.loadTexts: trapSinkPort.setDescription('The port of the SNMP manager to which the alarms are sent to.')
trapSinkCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 5), ReadableString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSinkCommunity.setStatus('current')
if mibBuilder.loadTexts: trapSinkCommunity.setDescription('community used in alarm')
trapSinkInformRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSinkInformRetry.setStatus('current')
if mibBuilder.loadTexts: trapSinkInformRetry.setDescription('only used for informs:\n                number of times to resend the inform')
trapSinkInformTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSinkInformTimeout.setStatus('current')
if mibBuilder.loadTexts: trapSinkInformTimeout.setDescription('only used for informs:\n                timeout between retries')
trapSinkInformUnacknowledged = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSinkInformUnacknowledged.setStatus('obsolete')
if mibBuilder.loadTexts: trapSinkInformUnacknowledged.setDescription('only used for informs:\n                maximum number of waiting informs\n                if this is reached, the oldest pending inform is discarded')
trapSinkUse = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSinkUse.setStatus('current')
if mibBuilder.loadTexts: trapSinkUse.setDescription('on/off-switch for this sink')
sendTestTrap = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 3), Trigger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sendTestTrap.setStatus('current')
if mibBuilder.loadTexts: sendTestTrap.setDescription("1: idle\n                2: Agent generates the trap 'testTrap', which is useful when checking the\n                   connection between agent (NetCCU) and your trapsink.")
irtTrapsAllOn = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 4), Trigger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irtTrapsAllOn.setStatus('current')
if mibBuilder.loadTexts: irtTrapsAllOn.setDescription('This switches all IRT-traps on - traps for all events are sent out.\n                \n                In detail, this means in the IRT-MIBs under branches *EventEnable all\n                OIDs are set to 1.\n                \n                Caution!\n                Setting this value influences remote controlling of devices.\n                Too many alarms may flood your network. Use this only for testing - for \n                operation, we suggest switch on only a few important traps.')
irtTrapsAllOff = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 5), Trigger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: irtTrapsAllOff.setStatus('current')
if mibBuilder.loadTexts: irtTrapsAllOff.setDescription("This switches all IRT-traps off - no traps are sent out.\n                \n                In detail, this means in the IRT-MIBs under branches *EventEnable all\n                OIDs are set to 2.\n                \n                Note: This is typically set when using only R&S-MIBs \n                and you don't need IRT-MIBs.")
rsTrapsAllOn = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 6), Trigger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsTrapsAllOn.setStatus('current')
if mibBuilder.loadTexts: rsTrapsAllOn.setDescription('This switches all R&S-traps on - traps for all events (info, warning, fault) are sent out.\n                \n                In detail, this means in the R&S-MIBs under *Events - Events*Table in\n                column event*Mask all OIDs are set to 1.\n                \n                Caution!\n                Enabling all traps is not recommended!\n                \n                Caution!\n                Setting this value influences remote controlling of devices!\n                Too many alarms may flood your network. Use this only for testing - for \n                operation, we suggest switch on only a few important traps.\n                \n                Caution!\n                This enables absolutely all R&S alarms!\n                Make sure you can handle it (network speed, routers, firewalls, NOC database performance etc.).')
rsTrapsAllOff = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 7), Trigger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsTrapsAllOff.setStatus('current')
if mibBuilder.loadTexts: rsTrapsAllOff.setDescription("This switches all R&S-traps off - no traps are sent out.\n                \n                In detail, this means in the R&S-MIBs under *Events - Events*Table in\n                column event*Mask all OIDs are set to 2.\n                \n                Note: This is typically set when using only IRT-MIBs \n                and you don't need R&S-MIBs.")
rsTrapsAllFaultsOn = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 8), Trigger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsTrapsAllFaultsOn.setStatus('current')
if mibBuilder.loadTexts: rsTrapsAllFaultsOn.setDescription("This switches all R&S-traps for faults on - traps for all 'faults' are sent out.\n                \n                In detail, this means in the R&S-MIBs under *Events - Events*Table in\n                column event*Mask all 'fault'-OIDs are set to '1'.\n                These traps include the value 'fault(1)' in binding 'eventAlarmClass'.\n                \n                Note: This is the recommended setting when using R&S-MIBs. It gives you an \n                overview of the device state.")
rsTrapsAllFaultsOff = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 9), Trigger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsTrapsAllFaultsOff.setStatus('current')
if mibBuilder.loadTexts: rsTrapsAllFaultsOff.setDescription("This switches all R&S-traps for faults off - no traps for 'faults' are sent out.\n                \n                In detail, this means in the R&S-MIBs under *Events - Events*Table in\n                column event*Mask all 'fault'-OIDs are set to '2'.\n                These traps include the value 'fault(1)' in binding 'eventAlarmClass'.")
rsTrapsAllWarningsOn = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 10), Trigger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsTrapsAllWarningsOn.setStatus('current')
if mibBuilder.loadTexts: rsTrapsAllWarningsOn.setDescription("This switches all R&S-traps for warnings on - traps for all 'warnings' are sent out.\n                \n                In detail, this means in the R&S-MIBs under *Events - Events*Table in\n                column event*Mask all 'warning'-OIDs are set to '1'.\n                These traps include the value 'warning(2)' in binding 'eventAlarmClass'.\n                \n                Note: This is the recommended setting when using R&S-MIBs and you want much more \n                informations from the device than only faults. \n                \n                Caution!\n                This enables lots of alarms. \n                Make sure you can handle it (network speed, NOC database performance etc.)...")
rsTrapsAllWarningsOff = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 11), Trigger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsTrapsAllWarningsOff.setStatus('current')
if mibBuilder.loadTexts: rsTrapsAllWarningsOff.setDescription("This switches all R&S-traps for warnings off - no traps for 'warnings' are sent out.\n                \n                In detail, this means in the R&S-MIBs under *Events - Events*Table in\n                column event*Mask all 'warning'-OIDs are set to '2'.\n                These traps include the value 'warning(2)' in binding 'eventAlarmClass'.")
transmitterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3))
dateTime = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dateTime.setStatus('current')
if mibBuilder.loadTexts: dateTime.setDescription('The date and time for the transmitter.\n                \n                Notes: Deci-seconds different from 0 are ignored.\n                       The range of distance from UTC is -12h..+14h.\n                       Omitting the optional UTC fields in a set-request results in keeping the \n                       old UTC offset values.')
ntp = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2))
ntpMode = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("stepAdjust", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpMode.setStatus('current')
if mibBuilder.loadTexts: ntpMode.setDescription('Configures the working mode of the NTP client.\n                disabled: no ntp synchronisation will be done\n                step: the time will synchronized every NTP sync-time\n                unknown: NTP mode is currently not determinable. This value must not be written.')
ntpSyncTimeInterval = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(6, 1440))).setUnits('minute').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpSyncTimeInterval.setStatus('current')
if mibBuilder.loadTexts: ntpSyncTimeInterval.setDescription('Set the intervall, how often the NTP client will be synchronized to the NTP server. \n                Note: this is useful in step mode only .')
ntpServerAddrTable = MibTable((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 3), )
if mibBuilder.loadTexts: ntpServerAddrTable.setStatus('current')
if mibBuilder.loadTexts: ntpServerAddrTable.setDescription('Table with server adresses.\n                Currently maximal one entry is allowed.')
ntpServerAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 3, 1), ).setIndexNames((0, "RS-XX8000-COMMON-MIB", "ntpServerAddrIdx"))
if mibBuilder.loadTexts: ntpServerAddrEntry.setStatus('current')
if mibBuilder.loadTexts: ntpServerAddrEntry.setDescription('An entry for a ntpServerAddrTable.')
ntpServerAddrIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: ntpServerAddrIdx.setStatus('current')
if mibBuilder.loadTexts: ntpServerAddrIdx.setDescription('index for table entry.')
ntpServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 3, 1, 2), ReadableString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntpServerAddress.setStatus('current')
if mibBuilder.loadTexts: ntpServerAddress.setDescription('host name or IP address of server.')
ntpState = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3), ("notRunning", 4), ("syncFailed", 5), ("synchronizing", 6), ("syncOk", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpState.setStatus('current')
if mibBuilder.loadTexts: ntpState.setDescription('Shows the actual state of the NTP synchronisation.')
ntpLastSync = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpLastSync.setStatus('current')
if mibBuilder.loadTexts: ntpLastSync.setDescription('The date/time of the last successful synchronisation.')
swMaintenance = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5))
restart = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 1), Trigger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restart.setStatus('current')
if mibBuilder.loadTexts: restart.setDescription("Restart the software of transmitter's control unit.")
swUpdate = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 5))
swUpdateStart = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 5, 2), Trigger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUpdateStart.setStatus('current')
if mibBuilder.loadTexts: swUpdateStart.setDescription("Start software update tool at transmitter side in manual mode. The PC tool can only connect\n                to transmitter's control unit if the software update tool on the transmitter is started.")
swUpdateMode = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("permanent", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUpdateMode.setStatus('current')
if mibBuilder.loadTexts: swUpdateMode.setDescription('Run mode of the software update tool at the transmitter side.\n                manual:    Software update can be started with the Start button. It will stop automaticly after\n                           an idle period of 90 seconds.\n                permanent: Software update is always running and will never stop.')
swUpdateDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 5, 4), ReadableString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUpdateDeviceName.setStatus('current')
if mibBuilder.loadTexts: swUpdateDeviceName.setDescription('The Device Name is dedicated to this control unit. It will be shown in the software update tool on the PC to differ devices.')
swUpdateDeviceGroup = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 5, 5), ReadableString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUpdateDeviceGroup.setStatus('current')
if mibBuilder.loadTexts: swUpdateDeviceGroup.setDescription('The Device Group can be used to separate devices in large networks.\n                It must match the Device Group in software update tool on the PC.')
rsXx8000CommonEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2))
rsXx8000EventsV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0))
testTrap = NotificationType((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 1)).setObjects(("RS-XX8000-COMMON-MIB", "serialNumber"), ("RS-XX8000-COMMON-MIB", "counterEvents"))
if mibBuilder.loadTexts: testTrap.setStatus('current')
if mibBuilder.loadTexts: testTrap.setDescription("This trap is sent to check whether the trapsink is receiving any traps \n                from this agent. To trigger this trap, set 'sendTestTrap' to '2'.")
eventTx = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10))
eventsTxV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 0))
if mibBuilder.loadTexts: eventsTxV2.setStatus('current')
if mibBuilder.loadTexts: eventsTxV2.setDescription('Compatibility to SMIv1.')
swUpdateStarted = NotificationType((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 0, 1)).setObjects(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"), ("RS-XX8000-COMMON-MIB", "eventAlarmClass"), ("RS-XX8000-COMMON-MIB", "eventEvent"))
if mibBuilder.loadTexts: swUpdateStarted.setStatus('current')
if mibBuilder.loadTexts: swUpdateStarted.setDescription("Software update started.\n                The PC tool can only connect to transmitter's control unit if the software\n                update tool on the transmitter is started. It uses the network 17 (TCP and UDP).")
ntpSyncFailed = NotificationType((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 0, 2)).setObjects(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"), ("RS-XX8000-COMMON-MIB", "eventAlarmClass"), ("RS-XX8000-COMMON-MIB", "eventEvent"))
if mibBuilder.loadTexts: ntpSyncFailed.setStatus('current')
if mibBuilder.loadTexts: ntpSyncFailed.setDescription('NTP synchronisation failed.')
eventsTxTable = MibTable((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1), )
if mibBuilder.loadTexts: eventsTxTable.setStatus('current')
if mibBuilder.loadTexts: eventsTxTable.setDescription('This table contains necessary information for handling alarms. \n                For each alarm you have the following information: \n                - name (get),\n                - mask to enable/disable sending out (set/get),\n                - priority (set/get) and \n                - the current state (get only).')
eventsTxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1), ).setIndexNames((0, "RS-XX8000-COMMON-MIB", "eventTxNameIdx"))
if mibBuilder.loadTexts: eventsTxEntry.setStatus('current')
if mibBuilder.loadTexts: eventsTxEntry.setDescription('An event entry always consists of 3 values:\n                - name: an enumerated list of all possible notifications\n                - mask: the corresponding mask (enable/disable)\n                - priority: the corresponding priority (value in range 0..255)\n                - event: the event itself (active/inactive)')
eventTxNameIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1, 1), EventMaxEntryNumber())
if mibBuilder.loadTexts: eventTxNameIdx.setStatus('current')
if mibBuilder.loadTexts: eventTxNameIdx.setDescription('The event number as integer.\n                This is a helper column and therefore not-accessible.')
eventTxName = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("swUpdateStarted", 1), ("ntpSyncFailed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTxName.setStatus('current')
if mibBuilder.loadTexts: eventTxName.setDescription('The event number as integer and the value as readable text.\n                The enumeration correlates with the notifications under eventsTxV2.')
eventTxMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1, 3), EventMask()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventTxMask.setStatus('current')
if mibBuilder.loadTexts: eventTxMask.setDescription('See TextualConvention for details.')
eventTxPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1, 4), EventPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventTxPriority.setStatus('current')
if mibBuilder.loadTexts: eventTxPriority.setDescription('See TextualConvention for details.')
eventTxEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1, 5), EventState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTxEvent.setStatus('current')
if mibBuilder.loadTexts: eventTxEvent.setDescription('See TextualConvention for details.')
eventHistory = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1))
if mibBuilder.loadTexts: eventHistory.setStatus('current')
if mibBuilder.loadTexts: eventHistory.setDescription('Information about sent out events.')
counterEvents = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: counterEvents.setStatus('current')
if mibBuilder.loadTexts: counterEvents.setDescription('The total number of traps sent out.\n                This is an increasing value.')
eventHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2), )
if mibBuilder.loadTexts: eventHistoryTable.setStatus('current')
if mibBuilder.loadTexts: eventHistoryTable.setDescription('The table of the last 100 messages sent out.')
eventHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1), ).setIndexNames((0, "RS-XX8000-COMMON-MIB", "eventHistoryNumber"))
if mibBuilder.loadTexts: eventHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: eventHistoryEntry.setDescription('An event entry.')
eventHistoryNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: eventHistoryNumber.setStatus('current')
if mibBuilder.loadTexts: eventHistoryNumber.setDescription('The trap number.')
eventHistoryModule = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("switchoverUnit", 1), ("netccu", 2), ("exciterA", 3), ("exciterB", 4), ("outputstageA", 5), ("outputstageB", 6), ("dvbReceiver", 7), ("pumpA", 8), ("pumpB", 9), ("antenna", 10), ("gps", 11), ("dvbRecMon", 12), ("gpParIO", 13), ("program", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventHistoryModule.setStatus('current')
if mibBuilder.loadTexts: eventHistoryModule.setDescription('This column indicates the physical module the corresponding message is for.')
eventHistoryEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventHistoryEvent.setStatus('current')
if mibBuilder.loadTexts: eventHistoryEvent.setDescription('This column indicates the event.\n                In correlation with column eventHistoryModule, you can see the name of the event here.\n                For this, you need to have a look at the event definitions of the corresponding MIB.\n                \n                Example: \n                For a DVB transmitter an entry in eventHistoryModule is netccu(2) and \n                the value in eventHistoryEvent is 1.\n                A look at eventsTxV2 of RS-XX8000-DVB-TX-MIB shows, 1 is txSummaryFault.')
eventHistoryEventState = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 4), EventState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventHistoryEventState.setStatus('current')
if mibBuilder.loadTexts: eventHistoryEventState.setDescription('See TextualConvention for details.')
eventHistoryEventDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventHistoryEventDate.setStatus('current')
if mibBuilder.loadTexts: eventHistoryEventDate.setDescription('This column indicates the date and time of the event.')
eventHistoryTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 101), IndexTransmitter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventHistoryTx.setStatus('current')
if mibBuilder.loadTexts: eventHistoryTx.setDescription('The transmitter index in case of NTx or Np1 systems.\n                For variants with one transmitter only (SingleTx) this index is always transmitterB(1).')
eventMapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3))
eventAlarmPriority = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 1), EventPriority()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventAlarmPriority.setStatus('current')
if mibBuilder.loadTexts: eventAlarmPriority.setDescription('This OID holds the value for the priority when sending out a notification.')
eventAlarmClass = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 2), EventClass()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventAlarmClass.setStatus('current')
if mibBuilder.loadTexts: eventAlarmClass.setDescription('See TextualConvention for details.')
eventEvent = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 3), EventState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventEvent.setStatus('current')
if mibBuilder.loadTexts: eventEvent.setDescription('This OID holds the value for the event itself when sending out a notification.')
indexTransmitter = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 4), IndexTransmitter()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: indexTransmitter.setStatus('current')
if mibBuilder.loadTexts: indexTransmitter.setDescription('This OID holds the value for the transmitter when sending out a notification.')
indexAB = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 5), IndexAB()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: indexAB.setStatus('current')
if mibBuilder.loadTexts: indexAB.setDescription('This OID holds the value for the module A (exciterA, outputstageA) or \n                B (exciterB, outputstageB) when sending out a notification.')
indexRack = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 6), IndexRack()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: indexRack.setStatus('current')
if mibBuilder.loadTexts: indexRack.setDescription('This OID holds the value for the rack when sending out a notification.')
indexAmplifier = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 7), IndexAmplifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: indexAmplifier.setStatus('current')
if mibBuilder.loadTexts: indexAmplifier.setDescription('This OID holds the value for the amplifier when sending out a notification.')
indexProgram = MibScalar((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 8), IndexProgram()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: indexProgram.setStatus('current')
if mibBuilder.loadTexts: indexProgram.setDescription('This object holds the value for the program when sending out a notification.')
rsXx8000CommonConf = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3))
rsXx8000CommonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1))
groupNotifyTest = NotificationGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 1)).setObjects(("RS-XX8000-COMMON-MIB", "testTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupNotifyTest = groupNotifyTest.setStatus('current')
if mibBuilder.loadTexts: groupNotifyTest.setDescription('test notifications.')
groupNotify = NotificationGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 2)).setObjects(("RS-XX8000-COMMON-MIB", "swUpdateStarted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupNotify = groupNotify.setStatus('current')
if mibBuilder.loadTexts: groupNotify.setDescription('notifications for all transmitters.')
groupEventTest = ObjectGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 6)).setObjects(("RS-XX8000-COMMON-MIB", "sendTestTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupEventTest = groupEventTest.setStatus('current')
if mibBuilder.loadTexts: groupEventTest.setDescription('The objects sent with testTrap.')
groupEventHistory = ObjectGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 8)).setObjects(("RS-XX8000-COMMON-MIB", "counterEvents"), ("RS-XX8000-COMMON-MIB", "eventHistoryModule"), ("RS-XX8000-COMMON-MIB", "eventHistoryEvent"), ("RS-XX8000-COMMON-MIB", "eventHistoryEventState"), ("RS-XX8000-COMMON-MIB", "eventHistoryEventDate"), ("RS-XX8000-COMMON-MIB", "eventHistoryTx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupEventHistory = groupEventHistory.setStatus('current')
if mibBuilder.loadTexts: groupEventHistory.setDescription("Contains all objects from 'eventHistory'.")
groupEventObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 9)).setObjects(("RS-XX8000-COMMON-MIB", "eventTxName"), ("RS-XX8000-COMMON-MIB", "eventTxMask"), ("RS-XX8000-COMMON-MIB", "eventTxPriority"), ("RS-XX8000-COMMON-MIB", "eventTxEvent"), ("RS-XX8000-COMMON-MIB", "eventAlarmPriority"), ("RS-XX8000-COMMON-MIB", "eventAlarmClass"), ("RS-XX8000-COMMON-MIB", "eventEvent"), ("RS-XX8000-COMMON-MIB", "indexTransmitter"), ("RS-XX8000-COMMON-MIB", "indexAB"), ("RS-XX8000-COMMON-MIB", "indexRack"), ("RS-XX8000-COMMON-MIB", "indexAmplifier"), ("RS-XX8000-COMMON-MIB", "indexProgram"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupEventObjects = groupEventObjects.setStatus('current')
if mibBuilder.loadTexts: groupEventObjects.setDescription("Contains all objects from 'eventMapObjects'.")
groupProductInformation = ObjectGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 11)).setObjects(("RS-XX8000-COMMON-MIB", "serialNumber"), ("RS-XX8000-COMMON-MIB", "identNumberSW"), ("RS-XX8000-COMMON-MIB", "versionNumberSW"), ("RS-XX8000-COMMON-MIB", "identNumberHW"), ("RS-XX8000-COMMON-MIB", "versionNumberHW"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupProductInformation = groupProductInformation.setStatus('current')
if mibBuilder.loadTexts: groupProductInformation.setDescription("Contains all objects from 'productInformation' (R&S typeplate).")
groupSnmpConfig = ObjectGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 12)).setObjects(("RS-XX8000-COMMON-MIB", "trapSinkVersion"), ("RS-XX8000-COMMON-MIB", "trapSinkAddress"), ("RS-XX8000-COMMON-MIB", "trapSinkPort"), ("RS-XX8000-COMMON-MIB", "trapSinkCommunity"), ("RS-XX8000-COMMON-MIB", "trapSinkInformRetry"), ("RS-XX8000-COMMON-MIB", "trapSinkInformTimeout"), ("RS-XX8000-COMMON-MIB", "trapSinkUse"), ("RS-XX8000-COMMON-MIB", "irtTrapsAllOn"), ("RS-XX8000-COMMON-MIB", "irtTrapsAllOff"), ("RS-XX8000-COMMON-MIB", "rsTrapsAllOn"), ("RS-XX8000-COMMON-MIB", "rsTrapsAllOff"), ("RS-XX8000-COMMON-MIB", "rsTrapsAllFaultsOn"), ("RS-XX8000-COMMON-MIB", "rsTrapsAllFaultsOff"), ("RS-XX8000-COMMON-MIB", "rsTrapsAllWarningsOn"), ("RS-XX8000-COMMON-MIB", "rsTrapsAllWarningsOff"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupSnmpConfig = groupSnmpConfig.setStatus('current')
if mibBuilder.loadTexts: groupSnmpConfig.setDescription("Contains all objects from 'snmpConfig'.")
groupTransmitterConfig = ObjectGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 13)).setObjects(("RS-XX8000-COMMON-MIB", "dateTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupTransmitterConfig = groupTransmitterConfig.setStatus('current')
if mibBuilder.loadTexts: groupTransmitterConfig.setDescription("objects from 'transmitterConfig'.")
groupNTP = ObjectGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 14)).setObjects(("RS-XX8000-COMMON-MIB", "ntpMode"), ("RS-XX8000-COMMON-MIB", "ntpSyncTimeInterval"), ("RS-XX8000-COMMON-MIB", "ntpServerAddress"), ("RS-XX8000-COMMON-MIB", "ntpState"), ("RS-XX8000-COMMON-MIB", "ntpLastSync"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupNTP = groupNTP.setStatus('current')
if mibBuilder.loadTexts: groupNTP.setDescription("objects from 'ntp'")
groupSwMaintenance = ObjectGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 15)).setObjects(("RS-XX8000-COMMON-MIB", "restart"), ("RS-XX8000-COMMON-MIB", "swUpdateStart"), ("RS-XX8000-COMMON-MIB", "swUpdateMode"), ("RS-XX8000-COMMON-MIB", "swUpdateDeviceName"), ("RS-XX8000-COMMON-MIB", "swUpdateDeviceGroup"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupSwMaintenance = groupSwMaintenance.setStatus('current')
if mibBuilder.loadTexts: groupSwMaintenance.setDescription("objects from 'swMaintenance'")
groupNotifyNTP = NotificationGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 16)).setObjects(("RS-XX8000-COMMON-MIB", "ntpSyncFailed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupNotifyNTP = groupNotifyNTP.setStatus('current')
if mibBuilder.loadTexts: groupNotifyNTP.setDescription('Notifications from the NTP client.')
groupObsoletedObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 17)).setObjects(("RS-XX8000-COMMON-MIB", "trapSinkInformUnacknowledged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    groupObsoletedObjects = groupObsoletedObjects.setStatus('obsolete')
if mibBuilder.loadTexts: groupObsoletedObjects.setDescription('Description.')
rsXx8000CommonCompls = MibIdentifier((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 2))
xx8000BasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 2, 1)).setObjects(("RS-XX8000-COMMON-MIB", "groupNotifyTest"), ("RS-XX8000-COMMON-MIB", "groupNotify"), ("RS-XX8000-COMMON-MIB", "groupEventTest"), ("RS-XX8000-COMMON-MIB", "groupEventHistory"), ("RS-XX8000-COMMON-MIB", "groupEventObjects"), ("RS-XX8000-COMMON-MIB", "groupProductInformation"), ("RS-XX8000-COMMON-MIB", "groupSnmpConfig"), ("RS-XX8000-COMMON-MIB", "groupTransmitterConfig"), ("RS-XX8000-COMMON-MIB", "groupSwMaintenance"), ("RS-XX8000-COMMON-MIB", "groupNTP"), ("RS-XX8000-COMMON-MIB", "groupNotifyNTP"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xx8000BasicCompliance = xx8000BasicCompliance.setStatus('current')
if mibBuilder.loadTexts: xx8000BasicCompliance.setDescription('The compliance statement for XX8000 entities which implement this MIB module.')
mibBuilder.exportSymbols("RS-XX8000-COMMON-MIB", EventPriority=EventPriority, eventTx=eventTx, sendTestTrap=sendTestTrap, eventMapObjects=eventMapObjects, InputSource=InputSource, eventsTxEntry=eventsTxEntry, eventHistoryEventState=eventHistoryEventState, TvStandard=TvStandard, testTrap=testTrap, indexTransmitter=indexTransmitter, ProdInfoModuleNameNsu=ProdInfoModuleNameNsu, indexProgram=indexProgram, eventsTxV2=eventsTxV2, rsXx8000=rsXx8000, rsTrapsAllFaultsOff=rsTrapsAllFaultsOff, AtvStandard=AtvStandard, EventMask=EventMask, ntpSyncTimeInterval=ntpSyncTimeInterval, eventHistoryEvent=eventHistoryEvent, groupSwMaintenance=groupSwMaintenance, swMaintenance=swMaintenance, swUpdate=swUpdate, trapSinkInformTimeout=trapSinkInformTimeout, ProdInfoModuleNameFm=ProdInfoModuleNameFm, LogbookEntrySlope=LogbookEntrySlope, trapSinkTable=trapSinkTable, trapSinkCommunity=trapSinkCommunity, eventAlarmPriority=eventAlarmPriority, trapSinkInformUnacknowledged=trapSinkInformUnacknowledged, ntpMode=ntpMode, groupNotifyTest=groupNotifyTest, eventHistory=eventHistory, eventHistoryTable=eventHistoryTable, IndexAmplifier=IndexAmplifier, ntpSyncFailed=ntpSyncFailed, indexAmplifier=indexAmplifier, ReadableString=ReadableString, serialNumber=serialNumber, trapSinkEntry=trapSinkEntry, indexAB=indexAB, EqualizerCalibrationState=EqualizerCalibrationState, rsTrapsAllOff=rsTrapsAllOff, transmitterConfig=transmitterConfig, eventTxPriority=eventTxPriority, rsXx8000CommonGroups=rsXx8000CommonGroups, xx8000BasicCompliance=xx8000BasicCompliance, groupTransmitterConfig=groupTransmitterConfig, eventHistoryTx=eventHistoryTx, trapSinkUse=trapSinkUse, ntpLastSync=ntpLastSync, eventTxEvent=eventTxEvent, irtTrapsAllOff=irtTrapsAllOff, IndexTransmitter=IndexTransmitter, LogbookEntryMessagesExcDVB=LogbookEntryMessagesExcDVB, groupEventObjects=groupEventObjects, eventTxNameIdx=eventTxNameIdx, ntpState=ntpState, counterEvents=counterEvents, Sx801AmplifierState=Sx801AmplifierState, versionNumberSW=versionNumberSW, FloatingPoint=FloatingPoint, ntp=ntp, LogbookEntryMessagesXV703=LogbookEntryMessagesXV703, ProdInfoModuleNameTv=ProdInfoModuleNameTv, trapSinkPort=trapSinkPort, LogbookEntryMessagesExcTv=LogbookEntryMessagesExcTv, productInformation=productInformation, swUpdateDeviceGroup=swUpdateDeviceGroup, groupProductInformation=groupProductInformation, rsTrapsAllWarningsOn=rsTrapsAllWarningsOn, identNumberHW=identNumberHW, LogbookEntryMessagesNSU=LogbookEntryMessagesNSU, swUpdateStart=swUpdateStart, rsXx8000Common=rsXx8000Common, eventTxMask=eventTxMask, versionNumberHW=versionNumberHW, eventHistoryEventDate=eventHistoryEventDate, rsTrapsAllWarningsOff=rsTrapsAllWarningsOff, rsXx8000EventsV2=rsXx8000EventsV2, eventHistoryNumber=eventHistoryNumber, FailDelayStatus=FailDelayStatus, eventsTxTable=eventsTxTable, eventHistoryModule=eventHistoryModule, trapSinkInformRetry=trapSinkInformRetry, dateTime=dateTime, LockState=LockState, groupNotify=groupNotify, IndexRack=IndexRack, swUpdateMode=swUpdateMode, LogbookEntryMessagesExcATV=LogbookEntryMessagesExcATV, LogbookEntryMessagesNetCCU=LogbookEntryMessagesNetCCU, restart=restart, groupNTP=groupNTP, snmpConfig=snmpConfig, groupEventTest=groupEventTest, rsXx8000CommonObjs=rsXx8000CommonObjs, eventEvent=eventEvent, trapSinkNumber=trapSinkNumber, FailDelayMode=FailDelayMode, rsTrapsAllOn=rsTrapsAllOn, PYSNMP_MODULE_ID=rsXx8000MibModule, groupObsoletedObjects=groupObsoletedObjects, rsTrapsAllFaultsOn=rsTrapsAllFaultsOn, LogbookMaxEntryNumber=LogbookMaxEntryNumber, groupNotifyNTP=groupNotifyNTP, rsXx8000MibModule=rsXx8000MibModule, swUpdateStarted=swUpdateStarted, eventAlarmClass=eventAlarmClass, swUpdateDeviceName=swUpdateDeviceName, EventClass=EventClass, EventState=EventState, ntpServerAddrEntry=ntpServerAddrEntry, groupEventHistory=groupEventHistory, TimeOfDay=TimeOfDay, irtTrapsAllOn=irtTrapsAllOn, LogbookEntryMessagesOST=LogbookEntryMessagesOST, ntpServerAddress=ntpServerAddress, IndexAB=IndexAB, LogbookEntryMessagesExcFM=LogbookEntryMessagesExcFM, rsXx8000CommonCompls=rsXx8000CommonCompls, groupSnmpConfig=groupSnmpConfig, eventTxName=eventTxName, trapSinkAddress=trapSinkAddress, EventMaxEntryNumber=EventMaxEntryNumber, SwitchOnOff=SwitchOnOff, ntpServerAddrTable=ntpServerAddrTable, IndexProgram=IndexProgram, rsXx8000CommonEvents=rsXx8000CommonEvents, trapSinkVersion=trapSinkVersion, Trigger=Trigger, eventHistoryEntry=eventHistoryEntry, rsXx8000CommonConf=rsXx8000CommonConf, identNumberSW=identNumberSW, ntpServerAddrIdx=ntpServerAddrIdx, indexRack=indexRack)
