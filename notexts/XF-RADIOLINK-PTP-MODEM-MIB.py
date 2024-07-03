#
# PySNMP MIB module XF-RADIOLINK-PTP-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/XF-RADIOLINK-PTP-MODEM-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 10:45:43 2024
# On host fv-az1251-584 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Unsigned32, Gauge32, Bits, Integer32, IpAddress, Counter32, Counter64, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Unsigned32", "Gauge32", "Bits", "Integer32", "IpAddress", "Counter32", "Counter64", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xfTermRowIndex, = mibBuilder.importSymbols("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRowIndex")
xfRadioLink, = mibBuilder.importSymbols("XF-TOP-MIB", "xfRadioLink")
xfRadioLinkPtpModemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2))
xfRadioLinkPtpModemMIB.setRevisions(('2012-06-24 00:00', '2012-05-29 00:00', '2011-05-23 00:00', '2011-04-06 00:00', '2011-02-01 00:00', '2010-12-13 00:00', '2010-01-19 00:00', '2009-11-30 00:00', '2009-11-26 00:00', '2009-11-18 00:00', '2009-09-18 00:00', '2009-06-26 00:00', '2009-06-24 00:00', '2009-04-20 00:00', '2009-04-14 00:00', '2009-03-04 00:00', '2008-10-02 00:00', '2008-09-16 00:00', '2008-08-15 00:00', '2008-06-25 00:00', '2008-06-24 00:00', '2008-06-18 00:00', '2008-06-04 00:00', '2008-06-03 00:00', '2008-04-09 00:00', '2008-03-03 00:00', '2008-02-26 00:00', '2007-11-12 00:00', '2007-10-24 00:00', '2007-08-14 00:00', '2007-07-03 00:00', '2007-06-04 00:00', '2007-01-17 00:00', '2006-11-14 00:00', '2006-09-19 13:25', '2006-03-20 00:00', '2006-02-24 00:00', '2006-01-31 00:00', '2005-03-02 00:00', '2004-12-13 00:00', '2004-07-02 00:00', '2004-06-16 00:00', '2004-05-25 00:00', '2004-04-26 00:00', '2004-01-20 00:00', '2003-12-17 00:00',))
if mibBuilder.loadTexts: xfRadioLinkPtpModemMIB.setLastUpdated('201205290000Z')
if mibBuilder.loadTexts: xfRadioLinkPtpModemMIB.setOrganization('Ericsson AB')
class MMUAlarmStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rcc0", 0), ("rcc1", 1), ("rcc2", 2), ("icc0", 3), ("icc1", 4), ("icc2", 5), ("atpcCapabilityAlarmFarEnd0", 6), ("atpcCapabilityAlarmFarEnd1", 7), ("atpcCapabilityAlarmFarEnd2", 8), ("hcc0", 9), ("hcc1", 10), ("hcc2", 11), ("xpicCable0", 12), ("xpicCable1", 13), ("xpicCable2", 14), ("xpicLos0", 15), ("xpicLos1", 16), ("xpicLos2", 17), ("interMMUChannelFailure0", 18), ("interMMUChannelFailure1", 19), ("interMMUChannelFailure2", 20), ("runningConfigNotAccepted0", 21), ("runningConfigNotAccepted1", 22), ("runningConfigNotAccepted2", 23), ("defaultConfigNotAccepted0", 24), ("defaultConfigNotAccepted1", 25), ("defaultConfigNotAccepted2", 26), ("syncOverRLNotSupported0", 27), ("syncOverRLNotSupported1", 28), ("syncOverRLNotSupported2", 29), ("rauPowerSupplyChanged0", 30), ("rauPowerSupplyChanged1", 31), ("rauPowerSupplyChanged2", 32), ("congestionControlNotSupported0", 33), ("congestionControlNotSupported1", 34), ("congestionControlNotSupported2", 35))

class MMUModIndexStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("modIndexValid", 2), ("modIndexNotValid", 3))

class MMUAtpcCapability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("noAtpcSupport", 2), ("doesNotExist", 3), ("atpcCapabilityUnknown", 4), ("supportsAtpc", 5), ("supportsAtpcFallback", 6), ("supportsAtpcFallbackTimer", 7))

class MMUModCapability(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("cqpsk", 0), ("qam16", 1), ("qam128", 2), ("qam32", 3), ("qam64", 4))

class MMUCapCapability(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("oneE1", 0), ("twoE1", 1), ("fourE1", 2), ("oneE2", 3), ("twoE2", 4), ("oneE3oneE1", 5), ("twoE3", 6), ("fourE3", 7), ("fourDS1", 8), ("eightDS1", 9), ("sixteenDS1", 10), ("seventeenDS1", 11), ("stm0", 12), ("stm1", 13), ("thirtytwoDS1", 14), ("stm1DS1", 15), ("stm150MHz", 16), ("twentytwoE1", 17), ("thirtyfiveE1", 18), ("fortysixE1", 19), ("seventyfiveE1", 20), ("oneStm1OneJ1", 21), ("sixtynineDS1", 22), ("eightyDS1", 23))

class MMUChannelSpacingCapability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("chspUnknown", 0), ("chsp7MHz", 1), ("chsp14MHz", 2), ("chsp20MHz", 3), ("chsp28MHz", 4), ("chsp30MHz", 5), ("chsp40MHz", 6), ("chsp50MHz", 7), ("chsp56MHz", 8), ("chsp10MHz", 9), ("chsp3500kHz", 10))

class MMUFrameFormatType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("fftUnknown", 0), ("fftStatic", 1), ("fftAdMod", 2), ("fftXpic", 3), ("fftXpicAdmod", 4), ("fftLegacy", 5), ("fftStaticLH", 6), ("fftAdmodLH", 7), ("fftXpicLH", 8), ("fftXpicAdmodLH", 9))

class ModemModulation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("cqpsk", 2), ("qam16", 3), ("qam128", 4), ("qam32", 5), ("qam64", 6), ("qam4", 7), ("qam8", 8), ("qam256", 9), ("qam512", 10), ("qam1024", 11))

xfRadioLinkPtpModemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1))
xfRadioLinkPtpModemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2))
xfModemTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1), )
if mibBuilder.loadTexts: xfModemTable.setStatus('current')
xfModemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: xfModemEntry.setStatus('current')
xfMMUAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 1), MMUAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUAlarmStatus.setStatus('current')
xfMMUModIndexNotValid = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 2), MMUModIndexStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUModIndexNotValid.setStatus('obsolete')
xfMMUAtpcCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 3), MMUAtpcCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUAtpcCapability.setStatus('current')
xfMMUModCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 4), MMUModCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUModCapability.setStatus('current')
xfMMUCapacityCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 5), MMUCapCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUCapacityCapability.setStatus('current')
xfMMUProtectionPath = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("mmuRa1", 2), ("mmuRa2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUProtectionPath.setStatus('current')
xfMMUSlotPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUSlotPosition.setStatus('current')
xfMMUChannelModeCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 8), Bits().clone(namedValues=NamedValues(("ccdp", 0), ("accp", 1), ("acap", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUChannelModeCapability.setStatus('current')
xfMMUChannelCompanionSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfMMUChannelCompanionSlot.setStatus('current')
xfMMUChannelCompanionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUChannelCompanionIndex.setStatus('current')
xfMMUInterfaceCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 11), Bits().clone(namedValues=NamedValues(("pdhToTdmHier", 0), ("pdhToTdmFlat", 1), ("pdhToTdmFlatAndBitpipeToPtp", 2), ("pdhToTdmAndSDHToSFP", 3), ("pdhToTdmAndSDHToPtp", 4), ("pdhToTdmAndSDHToSFPHAndSDHToPtP", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUInterfaceCapability.setStatus('current')
xfMMURAUSupplyVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("p55V", 2), ("m48V", 3), ("p24V", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMURAUSupplyVoltage.setStatus('current')
xfRAUIFTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2), )
if mibBuilder.loadTexts: xfRAUIFTable.setStatus('current')
xfRAUIFEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xfRAUIFEntry.setStatus('current')
xfRAUIFLoopEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfRAUIFLoopEnable.setStatus('current')
xfRAUIFRxLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfRAUIFRxLoop.setStatus('current')
xfRAUIFAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 3), Bits().clone(namedValues=NamedValues(("dmodClock0", 0), ("dmodClock1", 1), ("dmodClock2", 2), ("los0", 3), ("los1", 4), ("los2", 5), ("rxIfInput0", 6), ("rxIfInput1", 7), ("rxIfInput2", 8), ("txIfInput0", 9), ("txIfInput1", 10), ("txIfInput2", 11), ("radioFrame0", 12), ("radioFrame1", 13), ("radioFrame2", 14), ("ber0", 15), ("ber1", 16), ("ber2", 17), ("radioId0", 18), ("radioId1", 19), ("radioId2", 20), ("modIndex0", 21), ("modIndex1", 22), ("modIndex2", 23), ("aisReceived0", 24), ("aisReceived1", 25), ("aisReceived2", 26), ("carrierRecoveryLoss0", 27), ("carrierRecoveryLoss1", 28), ("carrierRecoveryLoss2", 29), ("wstLosL2R0", 30), ("wstLosL2R1", 31), ("wstLosL2R2", 32), ("wstLosR2L0", 33), ("wstLosR2L1", 34), ("wstLosR2L2", 35), ("lofR2L0", 36), ("lofR2L1", 37), ("lofR2L2", 38), ("notused0", 39), ("notused1", 40), ("notused2", 41), ("ifLosR2L0", 42), ("ifLosR2L1", 43), ("ifLosR2L2", 44), ("earlyWarning0", 45), ("earlyWarning1", 46), ("earlyWarning2", 47), ("lber0", 48), ("lber1", 49), ("lber2", 50), ("hber0", 51), ("hber1", 52), ("hber2", 53)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfRAUIFAlarms.setStatus('current')
xfRAUIFStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 4), Bits().clone(namedValues=NamedValues(("rxLoop0", 0), ("rxLoop1", 1), ("rxLoop2", 2), ("ifLoop0", 3), ("ifLoop1", 4), ("ifLoop2", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfRAUIFStatus.setStatus('current')
xfLINERSTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 3), )
if mibBuilder.loadTexts: xfLINERSTable.setStatus('current')
xfLINERSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xfLINERSEntry.setStatus('current')
xfLINERSAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 3, 1, 1), Bits().clone(namedValues=NamedValues(("timLineSide0", 0), ("timLineSide1", 1), ("timLineSide2", 2), ("lofL2R0", 3), ("lofL2R1", 4), ("lofL2R2", 5), ("losL2R0", 6), ("losL2R1", 7), ("losL2R2", 8), ("sfpLos0", 9), ("sfpLos1", 10), ("sfpLos2", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfLINERSAlarms.setStatus('current')
xfModemCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4), )
if mibBuilder.loadTexts: xfModemCapabilityTable.setStatus('current')
xfModemCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRowIndex"))
if mibBuilder.loadTexts: xfModemCapabilityEntry.setStatus('current')
xfMMUChannelSpacing = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 1), MMUChannelSpacingCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUChannelSpacing.setStatus('current')
xfMMUChannelModulation = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 2), ModemModulation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUChannelModulation.setStatus('current')
xfMMUMaxTribCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUMaxTribCapacity.setStatus('current')
xfMMUDCNCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUDCNCapacity.setStatus('current')
xfMMUMaxCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUMaxCapacity.setStatus('current')
xfMMUFrameFormatType = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 6), MMUFrameFormatType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUFrameFormatType.setStatus('current')
xfMMUFrameFormatRev = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("ffOther", 1), ("ffVersion0", 2), ("ffVersion1", 3), ("ffVersion2", 4), ("ffVersion3", 5), ("ffVersion4", 6), ("ffVersion5", 7), ("ffVersion6", 8), ("ffVersion7", 9), ("ffVersion8", 10), ("ffVersion9", 11), ("ffVersion10", 12), ("ffVersion11", 13), ("ffVersion12", 14), ("ffVersion13", 15), ("ffVersion14", 16), ("ffVersion15", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUFrameFormatRev.setStatus('current')
xfMMUBerAlarmThresholdCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 8), Bits().clone(namedValues=NamedValues(("berThrCap1e3", 0), ("berThrCap1e4", 1), ("berThrCap1e5", 2), ("berThrCap1e6", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUBerAlarmThresholdCapability.setStatus('current')
xfRadioLinkPtpModemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 1))
xfRadioLinkPtpModemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 2))
xfRadioLinkPtpModemFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 1, 1)).setObjects(("XF-RADIOLINK-PTP-MODEM-MIB", "xfRadioLinkPtpModemCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xfRadioLinkPtpModemFullCompliance = xfRadioLinkPtpModemFullCompliance.setStatus('current')
xfRadioLinkPtpModemCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 2, 1)).setObjects(("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUAlarmStatus"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUModIndexNotValid"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUAtpcCapability"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUModCapability"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUCapacityCapability"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUProtectionPath"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUSlotPosition"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelModeCapability"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelCompanionSlot"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelCompanionIndex"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUInterfaceCapability"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFLoopEnable"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFRxLoop"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFAlarms"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFStatus"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfLINERSAlarms"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelSpacing"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelModulation"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUMaxTribCapacity"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUDCNCapacity"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUMaxCapacity"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUFrameFormatType"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUFrameFormatRev"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMURAUSupplyVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xfRadioLinkPtpModemCompleteGroup = xfRadioLinkPtpModemCompleteGroup.setStatus('current')
mibBuilder.exportSymbols("XF-RADIOLINK-PTP-MODEM-MIB", xfLINERSEntry=xfLINERSEntry, xfRadioLinkPtpModemFullCompliance=xfRadioLinkPtpModemFullCompliance, xfMMURAUSupplyVoltage=xfMMURAUSupplyVoltage, xfMMUChannelCompanionSlot=xfMMUChannelCompanionSlot, xfMMUMaxTribCapacity=xfMMUMaxTribCapacity, MMUChannelSpacingCapability=MMUChannelSpacingCapability, xfRadioLinkPtpModemGroups=xfRadioLinkPtpModemGroups, xfMMUChannelCompanionIndex=xfMMUChannelCompanionIndex, xfRAUIFLoopEnable=xfRAUIFLoopEnable, MMUModIndexStatus=MMUModIndexStatus, xfMMUInterfaceCapability=xfMMUInterfaceCapability, xfRadioLinkPtpModemMIB=xfRadioLinkPtpModemMIB, xfRAUIFAlarms=xfRAUIFAlarms, xfMMUMaxCapacity=xfMMUMaxCapacity, xfMMUAlarmStatus=xfMMUAlarmStatus, xfModemCapabilityEntry=xfModemCapabilityEntry, PYSNMP_MODULE_ID=xfRadioLinkPtpModemMIB, xfMMUModCapability=xfMMUModCapability, xfMMUChannelModulation=xfMMUChannelModulation, xfLINERSTable=xfLINERSTable, xfMMUFrameFormatRev=xfMMUFrameFormatRev, xfRAUIFStatus=xfRAUIFStatus, xfMMUFrameFormatType=xfMMUFrameFormatType, xfRadioLinkPtpModemCompliances=xfRadioLinkPtpModemCompliances, ModemModulation=ModemModulation, xfMMUModIndexNotValid=xfMMUModIndexNotValid, MMUCapCapability=MMUCapCapability, xfMMUProtectionPath=xfMMUProtectionPath, xfMMUDCNCapacity=xfMMUDCNCapacity, MMUModCapability=MMUModCapability, MMUAlarmStatus=MMUAlarmStatus, xfMMUAtpcCapability=xfMMUAtpcCapability, xfMMUSlotPosition=xfMMUSlotPosition, xfModemTable=xfModemTable, MMUFrameFormatType=MMUFrameFormatType, xfMMUChannelSpacing=xfMMUChannelSpacing, xfRAUIFEntry=xfRAUIFEntry, xfRadioLinkPtpModemObjects=xfRadioLinkPtpModemObjects, xfMMUCapacityCapability=xfMMUCapacityCapability, xfRAUIFRxLoop=xfRAUIFRxLoop, xfModemCapabilityTable=xfModemCapabilityTable, xfMMUChannelModeCapability=xfMMUChannelModeCapability, xfRadioLinkPtpModemConformance=xfRadioLinkPtpModemConformance, xfModemEntry=xfModemEntry, xfRAUIFTable=xfRAUIFTable, xfLINERSAlarms=xfLINERSAlarms, xfMMUBerAlarmThresholdCapability=xfMMUBerAlarmThresholdCapability, xfRadioLinkPtpModemCompleteGroup=xfRadioLinkPtpModemCompleteGroup, MMUAtpcCapability=MMUAtpcCapability)
