#
# PySNMP MIB module CISCO-WIRELESS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WIRELESS-TC-MIB
# Source digest sha256:c057bdcf0aecd80a4ec0fb9a002dbdcc5c11f75dc0742ed9ea8f9bae143749da
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWirelessTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 137))
ciscoWirelessTextualConventions.setRevisions(('2000-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setRevisionsDescriptions(('Added TEXTUAL-CONVENTIONs for\n                    CwrRfType\n                    CwrFixedPointScale\n                    CwrFixedPointPrecison\n                    CwrFixedPointValue\n                    P2mpSnapshotAttribute\n                    CwrPercentageValue\n                    CwrRfFreqRange\n                    CwrUpdateTime\n                 Modified P2mpRadioSignalAttribute',))
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setLastUpdated('2000-04-03 00:00')
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setContactInfo('       Cisco Systems\n\t\t\tCustomer Service\n\n\t\tPostal: 170 W Tasman Drive\n\t\t\tSan Jose, CA  95134\n\t\t\tUSA\n\t\t\tTel: +1 800 553-NETS\n\t\t\tE-mail: wireless-nms@cisco.com')
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setDescription('This module defines textual conventions used\n\t\tin Cisco Wireless MIBs.')
class CwrRFZeroIndex(TextualConvention, Integer32):
    description = 'This represents an index into the cwrRFTable. The valid values \n\tare from 1 onwards. The special value of 0 is used to indicate \n\tthe absence of the associated RF resource.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2)

class CwrCwErrorFreeSecond(TextualConvention, Gauge32):
    description = 'A Codeword Error Free Second (EFS) is defined as 1 second when \n\tthe radio link was synchronized and no codeword errors detected \n\ton the link.'
    status = 'current'

class CwrCwErroredSecond(TextualConvention, Gauge32):
    description = 'A Codeword Errored Second (ES) is defined as 1 second when the \n\tradio link was synchronized and 1 or more codeword errors were \n        detected on the link.'
    status = 'current'

class CwrCwSeverelyErroredSecond(TextualConvention, Gauge32):
    description = 'A Codeword Severely Errored Second (SES) is defined as 1 \n        second when the radio link was synchronized and the codeword \n        error rate (CER) was greater than the threshold specified by \n        cwrLinkHighCwErrThresh.'
    status = 'current'

class CwrCwConsecutiveSevErrSecond(TextualConvention, Gauge32):
    description = 'A Codeword Consecutively Severely Errored Seconds (CSES) is \n        defined as the metric that measures the number of times a \n\tsequence of Codeword Severely Errored Seconds(SES) crosses the \n        cwrLinkCSESThresh value.  It is independent of the length of \n        the SES sequence.  In other words this counter is incremented by\n        one and only one for every such occurrence.'
    status = 'current'

class CwrCwDegradedSecond(TextualConvention, Gauge32):
    description = 'A Codeword Degraded Second (DS) is defined as a 1 second \n\tinterval during which the CER was between cwrLinkLowCwErrThresh\n\tand cwrLinkHighCwErrThresh.'
    status = 'current'

class CwrCwDegradedMinute(TextualConvention, Gauge32):
    description = 'A Codeword Degraded Minute (DM) is defined as a 60 Codeword \n        Degraded Seconds.'
    status = 'current'

class CwrCollectionAction(TextualConvention, Integer32):
    description = 'The action to perform on the identified specification.\n\tIt can be:\n\tStop: Stop the collection specification from continuing.\n\tStart: Start the collection specification.\n\tClear: Clear the current collection data. A collection in \n\t       progress must be stopped before it can be cleared.\n\tRestart: Identical to Clear followed by a Start.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("actionStop", 1), ("actionStart", 2), ("actionClear", 3), ("actionRestart", 4))

class CwrCollectionStatus(TextualConvention, Integer32):
    description = 'This indicates the current status of the collection \n        specification. It can be:\n\tIdle: No action in progress.\n\tIn_progress: Collection specification is currently being \n                     executed\n\tStopped: The collection specification has been stopped before\n\t\t it completed successfully.\n\tCaptured: The collection is complete and data is available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("statusIdle", 1), ("statusInProgress", 2), ("statusStopped", 3), ("statusCaptured", 4))

class CwrdBm(TextualConvention, Integer32):
    description = 'This is a unit of power measurement. It is measured in decibels\n\tof milliwatts (dBm). dBm = 10 * log(millwatts of power).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-80, 33)

class CwrdB(TextualConvention, Integer32):
    description = 'This is a unit of measurement defined as decibels (dB).\n\tdB = 10 * log(measured_value).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 16)

class CwrThreshLimitType(TextualConvention, Integer32):
    description = 'This object represents the kind of change that needs to be \n        monitored for a thresholdable attribute . An event is generated \n        when the following condition is met.\n\tThe kinds of change that may be setup in the radio hardware are:\n\t\n\tupChange   : Monitored value changes by a positive amount.\n\tdownChange : Monitored value changes by a negative amount.\n\thighThresh : Monitored value exceeds specified threshold.\n\tlowThresh  : Monitored value receeds below a threshold.\n\tupLimit    : Monitored value crosses the specified threshold \n                     when increasing in value.\n\tlowLimit   : Monitored value crosses the specified threshold \n\t\t     when decreasing in value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("upChange", 1), ("downChange", 2), ("highThresh", 3), ("lowThresh", 4), ("upLimit", 5), ("lowLimit", 6))

class CwrRadioSignalAttribute(TextualConvention, Integer32):
    description = 'This represents the set of radio signal attributes that may be\n\tmonitored by using histograms, timelines, and thresholds.\n\n\tThe  attributes are:\n\n\trsaIN(1) -\n\t\tThis is the Interference + Noise power levels computed \n\t\tby the hardware on a burst by burst basis. This is \n                available for a dual antenna system only.\n\t\t\t    \n\trsaINR(2) -\n\t\tThis is the ratio of the interference+noise power levels\n\t\tcaptured by first antenna to that captured by the second\n\t\tantenna on a burst by burst basis.\n\t\tThe values reported are in log to base 2.\n\t\n        rsaConstellationVariance(3) - \n\t\tConstellation variance(CV) is the average energy of the\n\t\tconstellation error signal. The constellation error\n\t\tsignal is the error between the received (noisy) \n                constellation symbol and the nearest ideal constellation\n                symbol.  CV is a measure of the Signal to \n                Interference+noise ratio, (SINR) for that tone.\n\t\tOn a Single antenna system it represents (1/SINR).\n\t\tOn a Dual antenna system it represents a \n\t\tcomposite histogram providing (1/SINR).\n\t\t\t\t\n\trsaTimingOffset(4) -\n\t\tThis represents the histogram of timing delay variations\n\t\tdetected in radio link.\n\t\t       \n\trsaReceivedPower(5) -\n\t\tThis is a measure of the analog signal power received\n\t \tby the radio system on a burst by burst basis.\n\t\n        rsaGainSettingsIF(6) -\n\t\tThis represents the change in the automatic gain control\n\t\tloop maintained by the hardware. This may be captured\n\t\tfor each antenna and at the intermediate frequency (IF)\n\t\tmodule.\n\t\tUnits: Integral values\n\t\t       \n\trsaGainSettingsRF(7) -\n\t\tThis represents the change in the automatic gain control\n\t\tloop maintained by the hardware. This may be\n\t\tcaptured for each antenna and at both the intermediate\n\t\tfrequency (IF) and radio frequency (RF) modules.\n\t\tUnits: Integral values\n\t\t       \n\trsaFreqOffset(8) -\n\t\tThis represents the frequency offset calculations\n\t\tmade to keep the receive frequency on a slave radio in\n\t\tsync with the master radio.\n\t\tUnits: Integral values.\n\t\n        rsaTotalGain(9) -\n\t\tThis represents the change in the automatic gain control\n\t\tloop maintained by the hardware. This may be\n\t\tcaptured for each antenna.\n\t\tUnits: Integral values\n\t\n\trsaSyncStatus(10) -\n\t\tThis represents the sync status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("rsaIN", 1), ("rsaINR", 2), ("rsaConstellationVariance", 3), ("rsaTimingOffset", 4), ("rsaReceivedPower", 5), ("rsaGainSettingsIF", 6), ("rsaGainSettingsRF", 7), ("rsaFreqOffset", 8), ("rsaTotalGain", 9), ("rsaSyncStatus", 10))

class CwrOscState(TextualConvention, Integer32):
    description = 'The current state of the oscillator.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oscillatorOk", 1), ("osccillatorBad", 2))

class P2mpRadioSignalAttribute(TextualConvention, Integer32):
    description = 'This represents the set of radio signal attributes that may be\n        monitored in a point to multipoint system by using histograms, \n        timelines, and thresholds.  Some of these attributes are common \n        to the head end (HE) and the subscriber unit (SU) whereas some \n        are specific to either the HE or the SU.\n  \n        The  attributes are:\n\n        none(0) -\n               This is a special value reserved to indicate that there \n               is no threshold associated with a timeline.  This \n               attribute cannot be used to create a histogram, timeline,\n               or threshold.\n \n        rsaSinrMainAnt(1) -\n                This is the Interference + Noise power level computed by\n                the hardware at the main antenna on a burst by burst  \n                basis\n \n        rsaSinrDiversityAnt(2) -\n                This is the Interference + Noise power level computed by\n                the hardware at the diversity antenna on a burst by \n                burst basis.\n \n        rsaSinrRatio(3) -\n                Ratio of (Interference + Noise) in main antenna to \n                diversity antenna \n \n        rsaTimingOffset(4) -\n                This represents the timing delay variations detected on \n                a radio link.\n \n        rsaRxPowerMainAnt(5) -\n                This is a measure of the analog signal power received at \n                the main antenna RF head on a burst by burst basis.\n        \n        rsaRxPowerDiversityAnt(6) -\n                This is a measure of the analog signal power received at \n                the diversity antenna RF head on a burst by burst basis.\n        \n        rsaChDelaySpreadMainAnt(7) -\n                Number of samples that the channel response remains \n                within (TBD) db of the manimun TAP in the channel \n                response at the main antenna.\n \n        rsaChDelaySpreadDiversityAnt(8) -\n                Number of samples that the channel response remains \n                within (TBD) db of the manimun TAP in the channel \n                response at the diversity antenna.\n \n        rsaHeAmbientNoise(19) -\n                The ambient noise (in dB) is measured when there is no \n                signal being received at the Headend\n \n        rsaSuRxPowerDeltaMainAnt(10) -\n                Change in received power (dB) at the main antenna of the\n                subscriber unit on a burst by burst basis.\n \n        rsaSuRxPowerDeltaDiversityAnt(11) -\n                Change in received power (dB) at the diversity antenna \n                of the subscriber unit on a burst by burst basis.\n \n        rsaSuTotalTxPower(12) - \n                The sum of -20 dBm (reference level out of the DAC) +\n                Tx IF transmit gain - 13 dBm (cable compensation) + Tx \n                RF transmit gain.  This parameter does not include \n                antenna gains.  \n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("none", 0), ("rsaSinrMainAnt", 1), ("rsaSinrDiversityAnt", 2), ("rsaSinrRatio", 3), ("rsaTimingOffset", 4), ("rsaRxPowerMainAnt", 5), ("rsaRxPowerDiversityAnt", 6), ("rsaChDelaySpreadMainAnt", 7), ("rsaChDelaySpreadDiversityAnt", 8), ("rsaHeAmbientNoise", 9), ("rsaSuRxPowerDeltaMainAnt", 10), ("rsaSuRxPowerDeltaDiversityAnt", 11), ("rsaSuTotalTxPower", 12))

class CwrRfType(TextualConvention, Integer32):
    description = 'Indicates if the outdoor RF unit is being used as the main RF \n        unit or the diversity RF unit.  The main RF unit is used to \n        receive and transmit data whereas the diversity unit is used to \n        receive only.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("main", 0), ("diversity", 1))

class CwrFixedPointScale(TextualConvention, Integer32):
    description = 'International System of Units (SI) prefixes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class CwrFixedPointPrecision(TextualConvention, Integer32):
    description = 'When in the range 1 to 9, CwrFixedPointPrecision is the number\n        of decimal places in the fractional part of a fixed-point\n        number.\n \n        CwrFixedPointPrecision is 0 for non-fixed-point numbers.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 9)

class CwrFixedPointValue(TextualConvention, Integer32):
    description = 'This represents a fixed point number. Use values -2147483648\n        and +2147483647 to indicate underflow and overflow \n        respectively. Use CwrFixedPointPrecision to indicate how \n        many fractional digits the CwrFixedPointValue has.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 2147483647)

class P2mpSnapshotAttribute(TextualConvention, OctetString):
    description = 'This represents the set of radio signal attributes that may be\n        monitored by using a snapshot.  The user can capture upto 4 \n        radio signal attributes simultaneously, by picking at most one\n        signal from each of the sets below and setting the bit\n        corresponding to each selected signal.\n \n        When a snapshot request is issued up to four radio signal \n        attributes may be requested at once, one from each set:\n        ===============================================\n        Type   Set1               Set2\n        ===============================================\n        RX     y1n(x1)            y2n(x2)\n               H2k(x80)           H1k(x40)\n        ===============================================\n \n        ===============================================\n        Type   Set3                Set4\n        ===============================================\n        RX     Y2k(x8)             Y1k(x4)\n               h1n(x10)            h2n(x20)\n               zhat(x100)          -\n        ===============================================\n \n        The attributes are:\n \n        rxRawBurstAnt1Y1n(0) -\n                This represents a snapshot of the received signal for \n                the main RF resource. For every sample, the real and \n                imaginary components are captured.\n                Units: (I, q)\n                Value: 32 bit quantities.\n \n        rxRawBurstAnt2Y2n(1) -\n                This represents a snapshot of the received signal for \n                the diversity RF resource. For every sample, the real \n                and imaginary components are captured.\n                Units: (I, q)\n                Value: 32 bit quantities.\n \n        rxSpectrumAnt1Y1k(2) -\n                This represents a snapshot of the spectrum of the \n                received signal for the main RF resource. For every \n                sample, the real and imaginary components are captured.\n                Units: (I, q)\n                Value: 32 bit quantities.\n \n        rxSpectrumAnt2Y2k(3) -\n                This represents a snapshot of the spectrum of the \n                received signal for the diversity RF resource. For every\n                sample the real and imaginary components are captured.\n                Units: (I, q)\n                Value: 32 bit quantities.\n \n        rxTimeDomainChannelAnt1H1n(4) -\n                This represents a snapshot of the time domain channel\n                for the main RF resource. For every sample the real and\n                imaginary components are captured.\n                Units: (I, q)\n                Value: 32 bit quantities.\n \n        rxTimeDomainChannelAnt2H2n(5) -\n                This represents a snapshot of the time domain channel\n                for the diversity RF resource. For every sample, the \n                real and imaginary components are captured.\n                Units: (I, q)\n                Value: 32 bit quantities.\n \n        rxFreqDomainChannelAnt1H1k(6) -\n                This represents a snapshot of the frequency domain \n                channel for the main RF resource. For every sample the \n                real and imaginary components are captured.\n                Units: (I, q)\n                Value: 32 bit quantities.\n \n        rxFreqDomainChannelAnt2H2k(7) -\n                This represents a snapshot of the frequency domain \n                channel for the diversity RF resource. For every sample,\n                the real and imaginary components are captured.\n                Units: (I, q)\n                Value: 32 bit quantities.\n \n        rxConstellationZHatk(8) -\n                This represents a snapshot of the soft decisions.\n                For every sample, the real and imaginary components are \n                captured.\n                Units: (I, q)\n                Value: 32 bit quantities.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class CwrPercentageValue(TextualConvention, Gauge32):
    description = 'This object can be used to represent percentage values for \n        codeword errors, available seconds, etc. The UNITS clause \n        associated with each object will indicate the degree of \n        precison.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 10000000)

class CwrUpdateTime(TextualConvention, Integer32):
    description = 'This is used to report statistics values measured on the \n        wireless link with a 1 second granularity insted of timeTicks. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CwrRfFreqRange(TextualConvention, Integer32):
    description = 'This represents the entire radio frequency range for a wireless\n        radio product.  The lower limit is assumed to be zero.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 60000000)

class WirelessGauge64(TextualConvention, Counter64):
    description = "This is a temporary textual convention that will be deleted\n        from this MIB when all references to this TC have been changed\n        to use 'CounterBasedGauge64' defined in RFC 2856"
    status = 'current'

mibBuilder.exportSymbols("CISCO-WIRELESS-TC-MIB", CwrCollectionAction=CwrCollectionAction, CwrCollectionStatus=CwrCollectionStatus, CwrCwConsecutiveSevErrSecond=CwrCwConsecutiveSevErrSecond, CwrCwDegradedMinute=CwrCwDegradedMinute, CwrCwDegradedSecond=CwrCwDegradedSecond, CwrCwErrorFreeSecond=CwrCwErrorFreeSecond, CwrCwErroredSecond=CwrCwErroredSecond, CwrCwSeverelyErroredSecond=CwrCwSeverelyErroredSecond, CwrFixedPointPrecision=CwrFixedPointPrecision, CwrFixedPointScale=CwrFixedPointScale, CwrFixedPointValue=CwrFixedPointValue, CwrOscState=CwrOscState, CwrPercentageValue=CwrPercentageValue, CwrRFZeroIndex=CwrRFZeroIndex, CwrRadioSignalAttribute=CwrRadioSignalAttribute, CwrRfFreqRange=CwrRfFreqRange, CwrRfType=CwrRfType, CwrThreshLimitType=CwrThreshLimitType, CwrUpdateTime=CwrUpdateTime, CwrdB=CwrdB, CwrdBm=CwrdBm, P2mpRadioSignalAttribute=P2mpRadioSignalAttribute, P2mpSnapshotAttribute=P2mpSnapshotAttribute, PYSNMP_MODULE_ID=ciscoWirelessTextualConventions, WirelessGauge64=WirelessGauge64, ciscoWirelessTextualConventions=ciscoWirelessTextualConventions)
