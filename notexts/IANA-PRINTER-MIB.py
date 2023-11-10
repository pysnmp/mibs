#
# PySNMP MIB module IANA-PRINTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-PRINTER-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 10:07:24 2023
# On host fv-az732-878 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Bits, ModuleIdentity, iso, NotificationType, mib_2, TimeTicks, Integer32, Counter32, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "ModuleIdentity", "iso", "NotificationType", "mib-2", "TimeTicks", "Integer32", "Counter32", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaPrinterMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 109))
ianaPrinterMIB.setRevisions(('2004-06-02 00:00',))
if mibBuilder.loadTexts: ianaPrinterMIB.setLastUpdated('200406020000Z')
if mibBuilder.loadTexts: ianaPrinterMIB.setOrganization('IANA')
class PrtCoverStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("coverOpen", 3), ("coverClosed", 4), ("interlockOpen", 5), ("interlockClosed", 6))

class PrtGeneralResetTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 5, 6))
    namedValues = NamedValues(("notResetting", 3), ("powerCycleReset", 4), ("resetToNVRAM", 5), ("resetToFactoryDefaults", 6))

class PrtChannelTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45))
    namedValues = NamedValues(("other", 1), ("chSerialPort", 3), ("chParallelPort", 4), ("chIEEE1284Port", 5), ("chSCSIPort", 6), ("chAppleTalkPAP", 7), ("chLPDServer", 8), ("chNetwareRPrinter", 9), ("chNetwarePServer", 10), ("chPort9100", 11), ("chAppSocket", 12), ("chFTP", 13), ("chTFTP", 14), ("chDLCLLCPort", 15), ("chIBM3270", 16), ("chIBM5250", 17), ("chFax", 18), ("chIEEE1394", 19), ("chTransport1", 20), ("chCPAP", 21), ("chDCERemoteProcCall", 22), ("chONCRemoteProcCall", 23), ("chOLE", 24), ("chNamedPipe", 25), ("chPCPrint", 26), ("chServerMessageBlock", 27), ("chDPMF", 28), ("chDLLAPI", 29), ("chVxDAPI", 30), ("chSystemObjectManager", 31), ("chDECLAT", 32), ("chNPAP", 33), ("chUSB", 34), ("chIRDA", 35), ("chPrintXChange", 36), ("chPortTCP", 37), ("chBidirPortTCP", 38), ("chUNPP", 39), ("chAppleTalkADSP", 40), ("chPortSPX", 41), ("chPortHTTP", 42), ("chNDPS", 43), ("chIPP", 44), ("chSMTP", 45))

class PrtInterpreterLangFamilyTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("langPCL", 3), ("langHPGL", 4), ("langPJL", 5), ("langPS", 6), ("langIPDS", 7), ("langPPDS", 8), ("langEscapeP", 9), ("langEpson", 10), ("langDDIF", 11), ("langInterpress", 12), ("langISO6429", 13), ("langLineData", 14), ("langMODCA", 15), ("langREGIS", 16), ("langSCS", 17), ("langSPDL", 18), ("langTEK4014", 19), ("langPDS", 20), ("langIGP", 21), ("langCodeV", 22), ("langDSCDSE", 23), ("langWPS", 24), ("langLN03", 25), ("langCCITT", 26), ("langQUIC", 27), ("langCPAP", 28), ("langDecPPL", 29), ("langSimpleText", 30), ("langNPAP", 31), ("langDOC", 32), ("langimPress", 33), ("langPinwriter", 34), ("langNPDL", 35), ("langNEC201PL", 36), ("langAutomatic", 37), ("langPages", 38), ("langLIPS", 39), ("langTIFF", 40), ("langDiagnostic", 41), ("langPSPrinter", 42), ("langCaPSL", 43), ("langEXCL", 44), ("langLCDS", 45), ("langXES", 46), ("langPCLXL", 47), ("langART", 48), ("langTIPSI", 49), ("langPrescribe", 50), ("langLinePrinter", 51), ("langIDP", 52), ("langXJCL", 53), ("langPDF", 54), ("langRPDL", 55), ("langIntermecIPL", 56), ("langUBIFingerprint", 57), ("langUBIDirectProtocol", 58), ("langFujitsu", 59), ("langCGM", 60), ("langJPEG", 61), ("langCALS1", 62), ("langCALS2", 63), ("langNIRS", 64), ("langC4", 65))

class PrtInputTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("sheetFeedAutoRemovableTray", 3), ("sheetFeedAutoNonRemovableTray", 4), ("sheetFeedManual", 5), ("continuousRoll", 6), ("continuousFanFold", 7))

class PrtOutputTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("removableBin", 3), ("unRemovableBin", 4), ("continuousRollDevice", 5), ("mailBox", 6), ("continuousFanFold", 7))

class PrtMarkerMarkTechTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("electrophotographicLED", 3), ("electrophotographicLaser", 4), ("electrophotographicOther", 5), ("impactMovingHeadDotMatrix9pin", 6), ("impactMovingHeadDotMatrix24pin", 7), ("impactMovingHeadDotMatrixOther", 8), ("impactMovingHeadFullyFormed", 9), ("impactBand", 10), ("impactOther", 11), ("inkjetAqueous", 12), ("inkjetSolid", 13), ("inkjetOther", 14), ("pen", 15), ("thermalTransfer", 16), ("thermalSensitive", 17), ("thermalDiffusion", 18), ("thermalOther", 19), ("electroerosion", 20), ("electrostatic", 21), ("photographicMicrofiche", 22), ("photographicImagesetter", 23), ("photographicOther", 24), ("ionDeposition", 25), ("eBeam", 26), ("typesetter", 27))

class PrtMarkerSuppliesTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("toner", 3), ("wasteToner", 4), ("ink", 5), ("inkCartridge", 6), ("inkRibbon", 7), ("wasteInk", 8), ("opc", 9), ("developer", 10), ("fuserOil", 11), ("solidWax", 12), ("ribbonWax", 13), ("wasteWax", 14), ("fuser", 15), ("coronaWire", 16), ("fuserOilWick", 17), ("cleanerUnit", 18), ("fuserCleaningPad", 19), ("transferUnit", 20), ("tonerCartridge", 21), ("fuserOiler", 22), ("water", 23), ("wasteWater", 24), ("glueWaterAdditive", 25), ("wastePaper", 26), ("bindingSupply", 27), ("bandingSupply", 28), ("stitchingWire", 29), ("shrinkWrap", 30), ("paperWrap", 31), ("staples", 32), ("inserts", 33), ("covers", 34))

class PrtMediaPathTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("longEdgeBindingDuplex", 3), ("shortEdgeBindingDuplex", 4), ("simplex", 5))

class PrtConsoleColorTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("white", 3), ("red", 4), ("green", 5), ("blue", 6), ("cyan", 7), ("magenta", 8), ("yellow", 9), ("orange", 10))

class PrtConsoleDisableTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4))
    namedValues = NamedValues(("enabled", 3), ("disabled", 4))

class PrtAlertTrainingLevelTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("untrained", 3), ("trained", 4), ("fieldService", 5), ("management", 6), ("noInterventionRequired", 7))

class PrtAlertGroupTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 30, 31, 32, 33))
    namedValues = NamedValues(("other", 1), ("hostResourcesMIBStorageTable", 3), ("hostResourcesMIBDeviceTable", 4), ("generalPrinter", 5), ("cover", 6), ("localization", 7), ("input", 8), ("output", 9), ("marker", 10), ("markerSupplies", 11), ("markerColorant", 12), ("mediaPath", 13), ("channel", 14), ("interpreter", 15), ("consoleDisplayBuffer", 16), ("consoleLights", 17), ("alert", 18), ("finDevice", 30), ("finSupply", 31), ("finSupplyMediaInput", 32), ("finAttribute", 33))

class PrtAlertCodeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 501, 502, 503, 504, 505, 506, 507, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 901, 902, 903, 904, 1001, 1002, 1003, 1004, 1005, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1301, 1302, 1303, 1304, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1509, 1801))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("coverOpen", 3), ("coverClosed", 4), ("interlockOpen", 5), ("interlockClosed", 6), ("configurationChange", 7), ("jam", 8), ("subunitMissing", 9), ("subunitLifeAlmostOver", 10), ("subunitLifeOver", 11), ("subunitAlmostEmpty", 12), ("subunitEmpty", 13), ("subunitAlmostFull", 14), ("subunitFull", 15), ("subunitNearLimit", 16), ("subunitAtLimit", 17), ("subunitOpened", 18), ("subunitClosed", 19), ("subunitTurnedOn", 20), ("subunitTurnedOff", 21), ("subunitOffline", 22), ("subunitPowerSaver", 23), ("subunitWarmingUp", 24), ("subunitAdded", 25), ("subunitRemoved", 26), ("subunitResourceAdded", 27), ("subunitResourceRemoved", 28), ("subunitRecoverableFailure", 29), ("subunitUnrecoverableFailure", 30), ("subunitRecoverableStorageError", 31), ("subunitUnrecoverableStorageError", 32), ("subunitMotorFailure", 33), ("subunitMemoryExhausted", 34), ("subunitUnderTemperature", 35), ("subunitOverTemperature", 36), ("subunitTimingFailure", 37), ("subunitThermistorFailure", 38), ("doorOpen", 501), ("doorClosed", 502), ("powerUp", 503), ("powerDown", 504), ("printerNMSReset", 505), ("printerManualReset", 506), ("printerReadyToPrint", 507), ("inputMediaTrayMissing", 801), ("inputMediaSizeChange", 802), ("inputMediaWeightChange", 803), ("inputMediaTypeChange", 804), ("inputMediaColorChange", 805), ("inputMediaFormPartsChange", 806), ("inputMediaSupplyLow", 807), ("inputMediaSupplyEmpty", 808), ("inputMediaChangeRequest", 809), ("inputManualInputRequest", 810), ("inputTrayPositionFailure", 811), ("inputTrayElevationFailure", 812), ("inputCannotFeedSizeSelected", 813), ("outputMediaTrayMissing", 901), ("outputMediaTrayAlmostFull", 902), ("outputMediaTrayFull", 903), ("outputMailboxSelectFailure", 904), ("markerFuserUnderTemperature", 1001), ("markerFuserOverTemperature", 1002), ("markerFuserTimingFailure", 1003), ("markerFuserThermistorFailure", 1004), ("markerAdjustingPrintQuality", 1005), ("markerTonerEmpty", 1101), ("markerInkEmpty", 1102), ("markerPrintRibbonEmpty", 1103), ("markerTonerAlmostEmpty", 1104), ("markerInkAlmostEmpty", 1105), ("markerPrintRibbonAlmostEmpty", 1106), ("markerWasteTonerReceptacleAlmostFull", 1107), ("markerWasteInkReceptacleAlmostFull", 1108), ("markerWasteTonerReceptacleFull", 1109), ("markerWasteInkReceptacleFull", 1110), ("markerOpcLifeAlmostOver", 1111), ("markerOpcLifeOver", 1112), ("markerDeveloperAlmostEmpty", 1113), ("markerDeveloperEmpty", 1114), ("markerTonerCartridgeMissing", 1115), ("mediaPathMediaTrayMissing", 1301), ("mediaPathMediaTrayAlmostFull", 1302), ("mediaPathMediaTrayFull", 1303), ("mediaPathCannotDuplexMediaSelected", 1304), ("interpreterMemoryIncrease", 1501), ("interpreterMemoryDecrease", 1502), ("interpreterCartridgeAdded", 1503), ("interpreterCartridgeDeleted", 1504), ("interpreterResourceAdded", 1505), ("interpreterResourceDeleted", 1506), ("interpreterResourceUnavailable", 1507), ("interpreterComplexPageEncountered", 1509), ("alertRemovalOfBinaryChangeEntry", 1801))

mibBuilder.exportSymbols("IANA-PRINTER-MIB", PrtInputTypeTC=PrtInputTypeTC, PYSNMP_MODULE_ID=ianaPrinterMIB, PrtGeneralResetTC=PrtGeneralResetTC, PrtChannelTypeTC=PrtChannelTypeTC, PrtConsoleColorTC=PrtConsoleColorTC, PrtConsoleDisableTC=PrtConsoleDisableTC, PrtOutputTypeTC=PrtOutputTypeTC, PrtAlertGroupTC=PrtAlertGroupTC, PrtMarkerMarkTechTC=PrtMarkerMarkTechTC, PrtInterpreterLangFamilyTC=PrtInterpreterLangFamilyTC, PrtAlertCodeTC=PrtAlertCodeTC, PrtAlertTrainingLevelTC=PrtAlertTrainingLevelTC, PrtMediaPathTypeTC=PrtMediaPathTypeTC, ianaPrinterMIB=ianaPrinterMIB, PrtCoverStatusTC=PrtCoverStatusTC, PrtMarkerSuppliesTypeTC=PrtMarkerSuppliesTypeTC)
