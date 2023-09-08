#
# PySNMP MIB module XF-RADIOLINK-PTP-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/XF-RADIOLINK-PTP-MODEM-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 11:07:18 2023
# On host fv-az590-991 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, Bits, Unsigned32, IpAddress, ObjectIdentity, MibIdentifier, iso, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32", "IpAddress", "ObjectIdentity", "MibIdentifier", "iso", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xfTermRowIndex, = mibBuilder.importSymbols("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRowIndex")
xfRadioLink, = mibBuilder.importSymbols("XF-TOP-MIB", "xfRadioLink")
xfRadioLinkPtpModemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2))
xfRadioLinkPtpModemMIB.setRevisions(('2012-06-24 00:00', '2012-05-29 00:00', '2011-05-23 00:00', '2011-04-06 00:00', '2011-02-01 00:00', '2010-12-13 00:00', '2010-01-19 00:00', '2009-11-30 00:00', '2009-11-26 00:00', '2009-11-18 00:00', '2009-09-18 00:00', '2009-06-26 00:00', '2009-06-24 00:00', '2009-04-20 00:00', '2009-04-14 00:00', '2009-03-04 00:00', '2008-10-02 00:00', '2008-09-16 00:00', '2008-08-15 00:00', '2008-06-25 00:00', '2008-06-24 00:00', '2008-06-18 00:00', '2008-06-04 00:00', '2008-06-03 00:00', '2008-04-09 00:00', '2008-03-03 00:00', '2008-02-26 00:00', '2007-11-12 00:00', '2007-10-24 00:00', '2007-08-14 00:00', '2007-07-03 00:00', '2007-06-04 00:00', '2007-01-17 00:00', '2006-11-14 00:00', '2006-09-19 13:25', '2006-03-20 00:00', '2006-02-24 00:00', '2006-01-31 00:00', '2005-03-02 00:00', '2004-12-13 00:00', '2004-07-02 00:00', '2004-06-16 00:00', '2004-05-25 00:00', '2004-04-26 00:00', '2004-01-20 00:00', '2003-12-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: xfRadioLinkPtpModemMIB.setRevisionsDescriptions(('\n\t\t\t    Rev PK2\n\t\t\t    * pdhToTdmAndSDHToSFPHAndSDHToPtP added to xfMMUInterfaceCapability\n\t\t\t    * Adjusted values in xfMMUBerAlarmThresholdCapability\n\t\t\t    ', '\n\t\t\t\tRev PK1\n\t\t\t\tAdded xfMMUBerAlarmThresholdCapability for MMU3A\n\t\t\t\t', '\n\t\t\t    Rev Y\n\t\t\t    Official R-State for TN 4.4 FP\n\t\t\t    ', '\n\t\t\t    Rev PY3\n\t\t\t    Changes for Mini Link LH 1.0.\n\t\t\t    Added fftStaticLH(6), fftAdmodLH(7),\n                fftXpicLH(8) and fftXpicAdmodLH(9)to xfTermFrameFormatType\n\t\t\t    ', '\n\t\t\t    Rev PY2\n\t\t\t    New value for xfMMUChannelModulation:\n\t\t\t      qam1024(11)\n\t\t\t    ', '\n\t\t\t    Rev PY1\n\t\t\t    Added new enum value supportsAtpcFallbackTimer to MMUAtpcCapability\n\t\t\t    ', '\n\t\t\t    Rev X\n\t\t\t    Official R-State for TN 4.3\n\t\t\t    ', '\n\t\t\t    Rev PX4\n\t\t\t    Updated MMUAlarmStatus with tree alarms.\n\t\t\t    New alarms:\n\t\t\t    \t syncOverRLNotSupported\n\t\t\t    \t rauPowerSupplyChanged\n\t\t\t    \t congestionControlNotSupported\n\t\t\t    ', '\n\t\t\t    Rev PX3\n\t\t\t    Change type of xfMMURAUSupplyVoltage from Integer32 to INTEGER.\n\t\t\t    Values:\n\t\t\t    \tother(1)\n\t\t\t    \tp55V(2)\n\t\t\t    \tm48V(3)\n\t\t\t    \tp24V(4)\n\t\t\t    ', '\n\t\t\t    Rev PX2\n\t\t\t    Added supportsAtpcFallback in MMUAtpcCapability.\n\t\t\t    ', '\n\t\t\t    Rev PX\n\t\t\t    Added xfMMURAUSupplyVoltage in xfModemTable.\n\t\t\t    ', '\n\t\t\t    Rev V\n\t\t\t    Update revision histry.\n\t\t\t    The Revision U is lost due to human errors.\n\t\t\t    ', '\n\t\t\t    Rev V\n\t\t\t    Official Rev for TN 4.2\n\t\t\t    ', '\n\t\t\t    Rev T\n\t\t\t    Official Rev for TN 4.1 FP.\n\t\t\t    ', '\n\t\t\t    Rev PT9\n\t\t\t    Changes for TN 4.2\n\n\t\t\t    Added channelspacing chsp3500kHz(10).\n\t\t\t    ', '\n\t\t\t    Rev PT8\n\t\t\t    Changed name on MMUFrameFormatType->fftAdaptive to fftAdmod\n\t\t\t    ', '\n\t\t\t    Rev PT7\n\t\t\t    Changed object in xfModemCapabilityTable:\n\t\t\t      from xfMMUDCHNCapacity to xfMMUDCNCapacity.\n\n\t\t\t    Fixed double index issue in xfRLPtpTerminalXTable\n\t\t\t    ', '\n\t\t\t    Rev PT6\n\t\t\t    Changes for TN 4.1,\n\t\t\t    Added new vaules in MMUFrameFormatType.\n\t\t\t    ', '\n\t\t\t    Rev PT5\n\t\t\t    Changes for TN 4.1,\n\t\t\t    Fixed wrong values in xfTermFrameFormatRev for xfModemCapabilityTable\n\t\t\t    ', '\n\t\t\t    Rev PT4\n\t\t\t    Changes for TN 4.1,\n\t\t\t    Changes in table: xfModemCapabilityTable\n\t\t\t    ', '\n\t\t\t    Rev PT3\n\t\t\t    Changes for TN 4.1,\n\t\t\t    Changes in table: xfModemCapabilityTable (xfMMUChannelModulation)\n\t\t\t    ', '\n\t\t\t    Rev PT2\n\t\t\t    Changes for TN 4.1,\n\t\t\t    Changes in table: xfModemCapabilityTable\n\t\t\t    ', '\n\t\t\t    Rev PT1\n\t\t\t    Changes for TN 4.1\n\t\t\t      New table: xfModemCapabilityTable\n\t\t\t    ', '\n\t\t\t    Rev S\n\t\t\t    Ordinary revision. No other changes.\n\t\t\t    ', '\n\t\t\t    Rev PS7\n\t\t\t    Changes for TN4.0:\n\t\t\t      incompatibleUnitMMU renamed to runningConfigNotAccepted in MMUAlarmStatus\n\n\t\t\t    ', '\n\t\t\t    Rev PS6\n\t\t\t    Changes for TN4.0:\n\t\t\t      MMUCapCapability extended with two new values: sixtynineDS1 and eightyDS1\n\t\t\t      xfModemTable extended with one new MO: xfMMUInterfaceCapability\n\n\t\t\t    ', '\n\t\t\t    Rev T\n\t\t\t        Added defaultConfigNotAccepted in MMUAlarmStatus.\n\t\t\t\t  ', '\n\t\t\t    Rev S\n\t\t\t        Error correction:\n\t\t\t           incompatibleUnitMMU ->\n\t\t\t             incompatibleUnitMMU0\n\t\t\t             incompatibleUnitMMU1\n\t\t\t             incompatibleUnitMMU2\n\t\t\t\t  ', '\n\t\t\t    Rev N.\n\t\t\t        Ordinary revision, for TN 3.3 - according to 1/155 19-CRH 109 625/1 Uae Rev V.\n\t\t\t        Added incompatibleUnitMMU in MMUAlarmStatus.\n\t\t\t\t  ', '\n\t\t\t    Rev PN2.\n\t\t\t\t\tNew value for MMUCapCapability:\n\t\t\t\t\t  oneStm1OneJ1\n\t\t\t\t  ', '\n\t\t\t    Rev PN1.\n\t\t\t\t\tNew values for MMUCapCapability:\n\t\t\t\t\t\tstm1DS1(15),\n\t\t\t\t\t\tstm150MHz(16),\n\t\t\t\t\t\ttwentytwoE1(17),\n\t\t\t\t\t\tthirtyfiveE1(18),\n\t\t\t\t\t\tfortysixE1(19),\n\t\t\t\t\t\tseventyfiveE1(20)\n\t\t\t\t  ', '\n\t\t\t    Rev M\n\t\t\t\t  Changes according to 1/15519-CRH109625/1 Uae Rev U\n  \t\t\t\t- xfMMUChannelCompanionSlot: Changed comment regarding access limitation at far end.\n  \t\t\t\t- xfRAUIFLoopEnable: Changed comment regarding access limitation at far end.\n\t\t\t\t  ', '\n\t\t\t    Rev L\n\t\t\t\t  Changes according to 1/15519-CRH109625/1 Uae Rev S\n  \t\t\t\t- xfRAUIFAlarms: ifLosL2R --> notused\n  \t\t\t\t- xfLINERSAlarms : removed laserFailure and laserDegraded\n  \t\t\t\t                   added sfpLos\n  \t\t\t  -\n\t\t\t\t  ', '\n\t\t\t    Rev K: Changes according to 1/15519-CRH109625/1 Uae Rev N\n  \t\t\t\t- interMMUChannelFailure added in MMUAlarmStatus\n  \t\t\t\t- wstClockLossR2L replaced by lofR2L in xfRAUIFAlarms\n  \t\t\t\t- xfRADIORSTable moved to XF-RADIOLINK-PTP-TERMINAL-MIB\n  \t\t\t\t- xfRADIORSPerformanceTable moved to XF-RADIOLINK-PTP-TERMINAL-MIB\n          ', '\n\t\t\t    Rev J: Changes according to 1/15519-CRH109625/1 Uae Rev M, plus errata\n  \t\t\t\t- xfModemTable and xfRAUIFTable updated\n  \t\t\t\t- New tables: xfRADIORSTable, xfRADIORSPerformanceTable and xfLINERSTable\n          ', '\n\t\t\t    Rev. H.\n\t\t\t\t- Changes according to 1/15519-CRH109625/1 Uae Rev K\n\t\t\t\t- Addition of Enum values for MMUModCapability and MMUCapCapability to support ANSI.\n                            ', '\n\t\t\t    Rev. G.\n\t\t\t\t- Access restrictions explained in the description field for each MO.\n        - Default value declarations in the description fields also includes the numerical value.\n\t\t\t    ', '\n\t\t\t    Rev. F.\n\t\t\t\t- xfMMUSlotPosition (integer, read-only) added in xfModemTable\n\t\t\t    ', '\n\t\t\t    Rev. E.\n\t\t\t\t- Changes according to 1/15519-CRH109625/1 Uae Rev E and corrections:\n\t\t\t\t- Correction: Alarm bits for dmodClock restored in MO xfRAUIFAlarms (xfRAUIFTable).\n\t\t\t\t- Alarm bits for unknown removed in MO xfRAUIFAlarms (xfRAUIFTable).\n\t\t\t\t- Status for MO xfMMUModIndexNotValid in xfModemTable set obsolete.\n\t\t\t\t- farEndRxLoop changed to rxLoop, in xfRAUIFStatus\n\t\t\t    ', '\n\t\t\t    Rev. D\n\t\t\t    \t- Changes according to 1/15519-CRH109625/1 Uae Rev D\n\t\t     - MO xfRAUIFCapacity removed from xfRAUIFTable\n\t\t     - MO xfRAUIFFarEndRxLoop renamed to xfRAUIFRxLoop in xfRAUIFTable\n\t\t     - Alarm bits for dmodClock removed in MO xfRAUIFAlarms (xfRAUIFTable)\n\t\t     - Alarm bits for aisReceived and Unknown added in MO xfRAUIFAlarms (xfRAUIFTable)\n\t\t        -DEFVAL removed. Default values declared in corresponding description fields.\n\t\t\t    ', '\n\t\t\t    Rev. C\n\t\t\t    \t- All config alarms are removed\n\t\t\t    \t- xfRAUIFConnectionLoop changed to xfRAUIFFarEndRxLoop\n\t\t\t    ', '\n\t\t\t    Rev. B\n\t\t\t    \t- All config alarms are defined\n\t\t\t    \t- Alarms are updated with new names\n                    -\n\t\t\t    ', '\n\t\t\t    Rev. PB2\n\t\t\t    \t- Some minor changes\n\t\t\t    ', "\n\t\t\t\tRev. PB1  \tCapacity and loop handling MO's are added.\n\t\t\t\t\t\tAlarms are defined.\n\t\t\t\t", '\n\t\t\t\tRev. A  \tOther is added to integer enumerations.\n\t\t\t\t', '\n\t\t\t\tRev. PA1  \tInitial revision\n\t\t\t\t',))
if mibBuilder.loadTexts: xfRadioLinkPtpModemMIB.setLastUpdated('201205290000Z')
if mibBuilder.loadTexts: xfRadioLinkPtpModemMIB.setOrganization('Ericsson AB')
if mibBuilder.loadTexts: xfRadioLinkPtpModemMIB.setContactInfo('\n\t\t\t\tEricsson AB\n\t\t\t\tBU Networks\n\t\t\t\tSE-431 84  Molndal\n\t\t\t\tSweden\n\t\t\t\t')
if mibBuilder.loadTexts: xfRadioLinkPtpModemMIB.setDescription('\n\t\t\t\tThis MIB defines objects for point-to-point Radiolink modems ().\n\t\t\t\t')
class MMUAlarmStatus(TextualConvention, Bits):
    description = '\n          This TC enumerates the the alarm status.\n          RCC - Communication is lost on the Radio Communication Channel,\n                between the MMU and RAU. RCC alarm for the modem will generate hardware\n                error for the radio (which will lead to radio operational status out of service).\n          ICC - Communication is lost on the Internal Communication Channel,\n                between two MMU2B or between the MMU2 and SMU2, in the same\n                terminal.\n          ATPCCapabilityAlarmFarEnd - The terminal on the far end is configured\n                for ATPC, but at least one of the indoor units does not support\n                ATPC.\n          HCC - Communication is lost on the Hop Communication Channel,\n                between the MMU and the far end MMU.\n\n          XPICCable - Disconnection of the XPIC cross-cable carrying the baseband signal\n                      received in one polarization, e.g. V, to the XPU board of the other\n                      polarization, i.e. H if the other is V.\n\n          XPICLos   - The loss of the XPIC baseband cross-signal with cross-cable connected.\n\n          interMMUChannelFailure - High level fault on inter MMU communication of RS.\n                                   Only valid in protection.\n\n          runningConfigNotAccepted - The MMU/RAU/SFP couldn.t accept the running configuration;\n                                     the service LED is flashing.\n\n          defaultConfigNotAccepted - Default config not accepted.\n\n          syncOverRLNotSupported - Current MMU, once provisioned as having sync over RL, does not support sync over RL.\n\n          rauPowerSupplyChanged - RAU power supply has changed automatically due to undervoltage or bad grounding detection.\n\n          congestionControlNotSupported - Far-end (i.e. CN) congestion control is not supported by modem; the service LED is flashing.\n\n\n\t   \t  Alarm status is indicated by 24 bits'
    status = 'current'
    namedValues = NamedValues(("rcc0", 0), ("rcc1", 1), ("rcc2", 2), ("icc0", 3), ("icc1", 4), ("icc2", 5), ("atpcCapabilityAlarmFarEnd0", 6), ("atpcCapabilityAlarmFarEnd1", 7), ("atpcCapabilityAlarmFarEnd2", 8), ("hcc0", 9), ("hcc1", 10), ("hcc2", 11), ("xpicCable0", 12), ("xpicCable1", 13), ("xpicCable2", 14), ("xpicLos0", 15), ("xpicLos1", 16), ("xpicLos2", 17), ("interMMUChannelFailure0", 18), ("interMMUChannelFailure1", 19), ("interMMUChannelFailure2", 20), ("runningConfigNotAccepted0", 21), ("runningConfigNotAccepted1", 22), ("runningConfigNotAccepted2", 23), ("defaultConfigNotAccepted0", 24), ("defaultConfigNotAccepted1", 25), ("defaultConfigNotAccepted2", 26), ("syncOverRLNotSupported0", 27), ("syncOverRLNotSupported1", 28), ("syncOverRLNotSupported2", 29), ("rauPowerSupplyChanged0", 30), ("rauPowerSupplyChanged1", 31), ("rauPowerSupplyChanged2", 32), ("congestionControlNotSupported0", 33), ("congestionControlNotSupported1", 34), ("congestionControlNotSupported2", 35))

class MMUModIndexStatus(TextualConvention, Integer32):
    description = 'This TC enumerates modulation index status values\n            codes'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("modIndexValid", 2), ("modIndexNotValid", 3))

class MMUAtpcCapability(TextualConvention, Integer32):
    description = 'This TC enumerates atpc capabilities values\n            codes'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("noAtpcSupport", 2), ("doesNotExist", 3), ("atpcCapabilityUnknown", 4), ("supportsAtpc", 5), ("supportsAtpcFallback", 6), ("supportsAtpcFallbackTimer", 7))

class MMUModCapability(TextualConvention, Bits):
    description = 'This TC enumerates the modulation capabilities.\n          Modulation capabilities is indicated by 5 bits:\n            bits 01234\n             00000 undetermined\n             00001 C-QPSK\n             00010 16-QAM\n             00011 C-QPSK & 16-QAM\n             00100 128-QAM\n             01000  32-QAM\n             10000  64-QAM\n             ...\n             11111 C-QPSK & 16-QAM & 128-QAM & 32-QAM & 64-QAM\n\t\t      '
    status = 'current'
    namedValues = NamedValues(("cqpsk", 0), ("qam16", 1), ("qam128", 2), ("qam32", 3), ("qam64", 4))

class MMUCapCapability(TextualConvention, Bits):
    description = 'This TC enumerates capacity capabilities values. Capacity\n\t    \tcapabilities is indicated by 15 bits'
    status = 'current'
    namedValues = NamedValues(("oneE1", 0), ("twoE1", 1), ("fourE1", 2), ("oneE2", 3), ("twoE2", 4), ("oneE3oneE1", 5), ("twoE3", 6), ("fourE3", 7), ("fourDS1", 8), ("eightDS1", 9), ("sixteenDS1", 10), ("seventeenDS1", 11), ("stm0", 12), ("stm1", 13), ("thirtytwoDS1", 14), ("stm1DS1", 15), ("stm150MHz", 16), ("twentytwoE1", 17), ("thirtyfiveE1", 18), ("fortysixE1", 19), ("seventyfiveE1", 20), ("oneStm1OneJ1", 21), ("sixtynineDS1", 22), ("eightyDS1", 23))

class MMUChannelSpacingCapability(TextualConvention, Integer32):
    description = 'Channel spacing capability'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("chspUnknown", 0), ("chsp7MHz", 1), ("chsp14MHz", 2), ("chsp20MHz", 3), ("chsp28MHz", 4), ("chsp30MHz", 5), ("chsp40MHz", 6), ("chsp50MHz", 7), ("chsp56MHz", 8), ("chsp10MHz", 9), ("chsp3500kHz", 10))

class MMUFrameFormatType(TextualConvention, Integer32):
    description = 'Frame format type.\n\n            Values:\n              fftUnknown(0)\n              fftStatic(1)\n              fftAdmod(2)\n              fftXpic(3)\n              fftXpicAdmod(4)\n              fftLegacy(5)\n              fftStaticLH(6)\n              fftAdmodLH(7)\n              fftXpicLH(8)\n              fftXpicAdmodLH(9)\n\n           '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("fftUnknown", 0), ("fftStatic", 1), ("fftAdMod", 2), ("fftXpic", 3), ("fftXpicAdmod", 4), ("fftLegacy", 5), ("fftStaticLH", 6), ("fftAdmodLH", 7), ("fftXpicLH", 8), ("fftXpicAdmodLH", 9))

class ModemModulation(TextualConvention, Integer32):
    description = 'Type of modulation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("cqpsk", 2), ("qam16", 3), ("qam128", 4), ("qam32", 5), ("qam64", 6), ("qam4", 7), ("qam8", 8), ("qam256", 9), ("qam512", 10), ("qam1024", 11))

xfRadioLinkPtpModemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1))
xfRadioLinkPtpModemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2))
xfModemTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1), )
if mibBuilder.loadTexts: xfModemTable.setStatus('current')
if mibBuilder.loadTexts: xfModemTable.setDescription('\n\t\t\tTable for Radiolink point-to-points modem managed objects.\n\t\t\tThe tabled is indexed with entPhysicalIndex.\n\t\t\t')
xfModemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: xfModemEntry.setStatus('current')
if mibBuilder.loadTexts: xfModemEntry.setDescription('An entry in the xfModemTable')
xfMMUAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 1), MMUAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: xfMMUAlarmStatus.setDescription('\n\t\t\tThis object shows the alarm status of the modem.\n\t\t\t')
xfMMUModIndexNotValid = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 2), MMUModIndexStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUModIndexNotValid.setStatus('obsolete')
if mibBuilder.loadTexts: xfMMUModIndexNotValid.setDescription('\n\t\t\tThis object shows if modulation index is valid. OBSOLETE.\n\t\t\t')
xfMMUAtpcCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 3), MMUAtpcCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUAtpcCapability.setStatus('current')
if mibBuilder.loadTexts: xfMMUAtpcCapability.setDescription('\n\t\t\tThis object shows the atpc capability.\n\t\t\t')
xfMMUModCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 4), MMUModCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUModCapability.setStatus('current')
if mibBuilder.loadTexts: xfMMUModCapability.setDescription('\n\t\t\tThis object shows the modulation capability.\n\t\t\t')
xfMMUCapacityCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 5), MMUCapCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUCapacityCapability.setStatus('current')
if mibBuilder.loadTexts: xfMMUCapacityCapability.setDescription('\n\t\t\tThis object shows the capacity capability.\n\t\t\t')
xfMMUProtectionPath = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("mmuRa1", 2), ("mmuRa2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUProtectionPath.setStatus('current')
if mibBuilder.loadTexts: xfMMUProtectionPath.setDescription('\n\t\t\tThis object indicates what radio path the modem\n\t\t\tbelongs to.\n\t\t\t')
xfMMUSlotPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUSlotPosition.setStatus('current')
if mibBuilder.loadTexts: xfMMUSlotPosition.setDescription('\n\t\t\tThe AMM slot position in which the MMU2 X is inserted in.\n\t\t\t0 = Unknown, 1-20 = slot position.\n\t\t\t')
xfMMUChannelModeCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 8), Bits().clone(namedValues=NamedValues(("ccdp", 0), ("accp", 1), ("acap", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUChannelModeCapability.setStatus('current')
if mibBuilder.loadTexts: xfMMUChannelModeCapability.setDescription('\n\t\t\tChannel capability.\n\t\t\t')
xfMMUChannelCompanionSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfMMUChannelCompanionSlot.setStatus('current')
if mibBuilder.loadTexts: xfMMUChannelCompanionSlot.setDescription('\n\t\t\tSlot number of companion channel MMU (XPIC/CCDP).\n\t\t\tDefault value: 0\n\t\t\tNear end access: read-write\n\t\t\tFar end access: read-only (Traffic Node only)\n\t\t\t')
xfMMUChannelCompanionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUChannelCompanionIndex.setStatus('current')
if mibBuilder.loadTexts: xfMMUChannelCompanionIndex.setDescription('\n\t\t\t0 if CCDP not selected\n      entPhysicalIndex of companion channel MMU (XPIC/CCDP) according to\n      xfMMUChannelCompanionSlot setting.\n\t\t\t')
xfMMUInterfaceCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 11), Bits().clone(namedValues=NamedValues(("pdhToTdmHier", 0), ("pdhToTdmFlat", 1), ("pdhToTdmFlatAndBitpipeToPtp", 2), ("pdhToTdmAndSDHToSFP", 3), ("pdhToTdmAndSDHToPtp", 4), ("pdhToTdmAndSDHToSFPHAndSDHToPtP", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUInterfaceCapability.setStatus('current')
if mibBuilder.loadTexts: xfMMUInterfaceCapability.setDescription('\n\t\t\tInterface capability for MMU.\n\t\t\t')
xfMMURAUSupplyVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("p55V", 2), ("m48V", 3), ("p24V", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMURAUSupplyVoltage.setStatus('current')
if mibBuilder.loadTexts: xfMMURAUSupplyVoltage.setDescription('\n\t\t\tThe radio nominal supply voltage.\n\n\t\t\tValues:\n\t\t\tother(1)\n\t\t\tp55V(2) default\n\t\t\tm48V(3)\n\t\t\tp24V(4)\n\t\t\t')
xfRAUIFTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2), )
if mibBuilder.loadTexts: xfRAUIFTable.setStatus('current')
if mibBuilder.loadTexts: xfRAUIFTable.setDescription('\n\t\t\tTable for rau interface objects. The tabled is indexed with\n\t\t\tifIndex.\n\t\t\t')
xfRAUIFEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xfRAUIFEntry.setStatus('current')
if mibBuilder.loadTexts: xfRAUIFEntry.setDescription('An entry in the xfRAUIFTable')
xfRAUIFLoopEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfRAUIFLoopEnable.setStatus('current')
if mibBuilder.loadTexts: xfRAUIFLoopEnable.setDescription('\n\t\t\tThis object manage the IF loop.\n\t\t\tDefault value: disable(3)\n\t\t\tNear end access: read-write\n\t\t\tFar end access: no access\n\t\t\t')
xfRAUIFRxLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xfRAUIFRxLoop.setStatus('current')
if mibBuilder.loadTexts: xfRAUIFRxLoop.setDescription('\n\t\t\tThis object manage the Far end rx loop.\n\t\t\tDefault value: disable(3)\n\t\t\t')
xfRAUIFAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 3), Bits().clone(namedValues=NamedValues(("dmodClock0", 0), ("dmodClock1", 1), ("dmodClock2", 2), ("los0", 3), ("los1", 4), ("los2", 5), ("rxIfInput0", 6), ("rxIfInput1", 7), ("rxIfInput2", 8), ("txIfInput0", 9), ("txIfInput1", 10), ("txIfInput2", 11), ("radioFrame0", 12), ("radioFrame1", 13), ("radioFrame2", 14), ("ber0", 15), ("ber1", 16), ("ber2", 17), ("radioId0", 18), ("radioId1", 19), ("radioId2", 20), ("modIndex0", 21), ("modIndex1", 22), ("modIndex2", 23), ("aisReceived0", 24), ("aisReceived1", 25), ("aisReceived2", 26), ("carrierRecoveryLoss0", 27), ("carrierRecoveryLoss1", 28), ("carrierRecoveryLoss2", 29), ("wstLosL2R0", 30), ("wstLosL2R1", 31), ("wstLosL2R2", 32), ("wstLosR2L0", 33), ("wstLosR2L1", 34), ("wstLosR2L2", 35), ("lofR2L0", 36), ("lofR2L1", 37), ("lofR2L2", 38), ("notused0", 39), ("notused1", 40), ("notused2", 41), ("ifLosR2L0", 42), ("ifLosR2L1", 43), ("ifLosR2L2", 44), ("earlyWarning0", 45), ("earlyWarning1", 46), ("earlyWarning2", 47), ("lber0", 48), ("lber1", 49), ("lber2", 50), ("hber0", 51), ("hber1", 52), ("hber2", 53)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfRAUIFAlarms.setStatus('current')
if mibBuilder.loadTexts: xfRAUIFAlarms.setDescription('\n\t\t\tThis object shows rau if related alarms.\n\t\t\t')
xfRAUIFStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 4), Bits().clone(namedValues=NamedValues(("rxLoop0", 0), ("rxLoop1", 1), ("rxLoop2", 2), ("ifLoop0", 3), ("ifLoop1", 4), ("ifLoop2", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfRAUIFStatus.setStatus('current')
if mibBuilder.loadTexts: xfRAUIFStatus.setDescription('\n\t\t\tThis object shows test loop status.\n\t\t\t')
xfLINERSTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 3), )
if mibBuilder.loadTexts: xfLINERSTable.setStatus('current')
if mibBuilder.loadTexts: xfLINERSTable.setDescription('\n\t\t\tTraffic node extension of ifTable. The tabled is indexed with\n\t\t\tifIndex.\n\t\t\t')
xfLINERSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xfLINERSEntry.setStatus('current')
if mibBuilder.loadTexts: xfLINERSEntry.setDescription('An entry in the xfLINERSTable')
xfLINERSAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 3, 1, 1), Bits().clone(namedValues=NamedValues(("timLineSide0", 0), ("timLineSide1", 1), ("timLineSide2", 2), ("lofL2R0", 3), ("lofL2R1", 4), ("lofL2R2", 5), ("losL2R0", 6), ("losL2R1", 7), ("losL2R2", 8), ("sfpLos0", 9), ("sfpLos1", 10), ("sfpLos2", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfLINERSAlarms.setStatus('current')
if mibBuilder.loadTexts: xfLINERSAlarms.setDescription('\n\t\t\tThis object shows line rs related alarms.\n\t\t\t')
xfModemCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4), )
if mibBuilder.loadTexts: xfModemCapabilityTable.setStatus('current')
if mibBuilder.loadTexts: xfModemCapabilityTable.setDescription('\n\t\t\tTable for misc. modem capability information.\n\t\t\t')
xfModemCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRowIndex"))
if mibBuilder.loadTexts: xfModemCapabilityEntry.setStatus('current')
if mibBuilder.loadTexts: xfModemCapabilityEntry.setDescription('An entry in the xfModemCapabilityTable')
xfMMUChannelSpacing = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 1), MMUChannelSpacingCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUChannelSpacing.setStatus('current')
if mibBuilder.loadTexts: xfMMUChannelSpacing.setDescription('Channel spacing.\n                    ETSI: 3.5, 7, 14, 28, 40, 56 MHz\n                    ANSI: 10, 20, 30, 40, 50 MHz\n                ')
xfMMUChannelModulation = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 2), ModemModulation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUChannelModulation.setStatus('current')
if mibBuilder.loadTexts: xfMMUChannelModulation.setDescription('This object shows the channel modulation.\n                Values:\n\n          cqpsk(2)    CQPSK\n          qam16(3)    16-QAM\n          qam128(4)   128-QAM\n          qam32(5)    32-QAM\n          qam64(6)    64-QAM\n          qam4(7)     4-QAM\n          qam8(8)     8-QAM\n          qam256(9)   256-QAM\n          qam512(10)  512-QAM\n          qam1024(11) 1024-QAM\n          ')
xfMMUMaxTribCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUMaxTribCapacity.setStatus('current')
if mibBuilder.loadTexts: xfMMUMaxTribCapacity.setDescription('Max tributaries.')
xfMMUDCNCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUDCNCapacity.setStatus('current')
if mibBuilder.loadTexts: xfMMUDCNCapacity.setDescription('DCN Hop Capacity.')
xfMMUMaxCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUMaxCapacity.setStatus('current')
if mibBuilder.loadTexts: xfMMUMaxCapacity.setDescription('Max Capacity.')
xfMMUFrameFormatType = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 6), MMUFrameFormatType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUFrameFormatType.setStatus('current')
if mibBuilder.loadTexts: xfMMUFrameFormatType.setDescription('Frame format type.\n\n            Values:\n              fftUnknown(0)\n              fftStatic(1)\n              fftAdMod(2)\n              fftXpic(3)\n              fftXpicAdmod(4)\n              fftLegacy(5)')
xfMMUFrameFormatRev = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("ffOther", 1), ("ffVersion0", 2), ("ffVersion1", 3), ("ffVersion2", 4), ("ffVersion3", 5), ("ffVersion4", 6), ("ffVersion5", 7), ("ffVersion6", 8), ("ffVersion7", 9), ("ffVersion8", 10), ("ffVersion9", 11), ("ffVersion10", 12), ("ffVersion11", 13), ("ffVersion12", 14), ("ffVersion13", 15), ("ffVersion14", 16), ("ffVersion15", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUFrameFormatRev.setStatus('current')
if mibBuilder.loadTexts: xfMMUFrameFormatRev.setDescription('Frame format revision.')
xfMMUBerAlarmThresholdCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 8), Bits().clone(namedValues=NamedValues(("berThrCap1e3", 0), ("berThrCap1e4", 1), ("berThrCap1e5", 2), ("berThrCap1e6", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xfMMUBerAlarmThresholdCapability.setStatus('current')
if mibBuilder.loadTexts: xfMMUBerAlarmThresholdCapability.setDescription('List of the allowed BER thresholds.')
xfRadioLinkPtpModemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 1))
xfRadioLinkPtpModemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 2))
xfRadioLinkPtpModemFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 1, 1)).setObjects(("XF-RADIOLINK-PTP-MODEM-MIB", "xfRadioLinkPtpModemCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xfRadioLinkPtpModemFullCompliance = xfRadioLinkPtpModemFullCompliance.setStatus('current')
if mibBuilder.loadTexts: xfRadioLinkPtpModemFullCompliance.setDescription('The compliance statement for SNMP entities which\n            \t\timplement everything.')
xfRadioLinkPtpModemCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 2, 1)).setObjects(("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUAlarmStatus"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUModIndexNotValid"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUAtpcCapability"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUModCapability"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUCapacityCapability"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUProtectionPath"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUSlotPosition"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelModeCapability"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelCompanionSlot"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelCompanionIndex"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUInterfaceCapability"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFLoopEnable"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFRxLoop"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFAlarms"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFStatus"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfLINERSAlarms"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelSpacing"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelModulation"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUMaxTribCapacity"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUDCNCapacity"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUMaxCapacity"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUFrameFormatType"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUFrameFormatRev"), ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMURAUSupplyVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xfRadioLinkPtpModemCompleteGroup = xfRadioLinkPtpModemCompleteGroup.setStatus('current')
if mibBuilder.loadTexts: xfRadioLinkPtpModemCompleteGroup.setDescription('A collection of all current objects in this MIB\n           \t\tmodule.')
mibBuilder.exportSymbols("XF-RADIOLINK-PTP-MODEM-MIB", xfRadioLinkPtpModemMIB=xfRadioLinkPtpModemMIB, xfRAUIFAlarms=xfRAUIFAlarms, xfRadioLinkPtpModemGroups=xfRadioLinkPtpModemGroups, xfMMUChannelCompanionIndex=xfMMUChannelCompanionIndex, xfModemTable=xfModemTable, xfRAUIFEntry=xfRAUIFEntry, xfMMUChannelModulation=xfMMUChannelModulation, MMUModCapability=MMUModCapability, xfRadioLinkPtpModemConformance=xfRadioLinkPtpModemConformance, xfMMUAlarmStatus=xfMMUAlarmStatus, xfMMUSlotPosition=xfMMUSlotPosition, xfMMUInterfaceCapability=xfMMUInterfaceCapability, xfMMUFrameFormatType=xfMMUFrameFormatType, MMUAlarmStatus=MMUAlarmStatus, xfMMUBerAlarmThresholdCapability=xfMMUBerAlarmThresholdCapability, xfMMUChannelModeCapability=xfMMUChannelModeCapability, xfRAUIFStatus=xfRAUIFStatus, xfMMUChannelSpacing=xfMMUChannelSpacing, xfRadioLinkPtpModemObjects=xfRadioLinkPtpModemObjects, xfModemCapabilityTable=xfModemCapabilityTable, xfMMUCapacityCapability=xfMMUCapacityCapability, xfRAUIFLoopEnable=xfRAUIFLoopEnable, xfMMUFrameFormatRev=xfMMUFrameFormatRev, ModemModulation=ModemModulation, MMUFrameFormatType=MMUFrameFormatType, xfMMUModCapability=xfMMUModCapability, MMUModIndexStatus=MMUModIndexStatus, PYSNMP_MODULE_ID=xfRadioLinkPtpModemMIB, xfMMUAtpcCapability=xfMMUAtpcCapability, xfMMUDCNCapacity=xfMMUDCNCapacity, xfMMUProtectionPath=xfMMUProtectionPath, xfRAUIFTable=xfRAUIFTable, xfMMUMaxTribCapacity=xfMMUMaxTribCapacity, xfRadioLinkPtpModemCompleteGroup=xfRadioLinkPtpModemCompleteGroup, xfMMUChannelCompanionSlot=xfMMUChannelCompanionSlot, xfLINERSEntry=xfLINERSEntry, xfModemCapabilityEntry=xfModemCapabilityEntry, xfMMURAUSupplyVoltage=xfMMURAUSupplyVoltage, xfRadioLinkPtpModemCompliances=xfRadioLinkPtpModemCompliances, xfLINERSAlarms=xfLINERSAlarms, MMUCapCapability=MMUCapCapability, xfLINERSTable=xfLINERSTable, xfModemEntry=xfModemEntry, xfRadioLinkPtpModemFullCompliance=xfRadioLinkPtpModemFullCompliance, MMUChannelSpacingCapability=MMUChannelSpacingCapability, MMUAtpcCapability=MMUAtpcCapability, xfMMUMaxCapacity=xfMMUMaxCapacity, xfMMUModIndexNotValid=xfMMUModIndexNotValid, xfRAUIFRxLoop=xfRAUIFRxLoop)
