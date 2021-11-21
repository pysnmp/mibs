#
# PySNMP MIB module MEF-SOAM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MEF-SOAM-TC-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:25:48 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, NotificationType, Unsigned32, iso, Counter64, Integer32, TimeTicks, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "NotificationType", "Unsigned32", "iso", "Counter64", "Integer32", "TimeTicks", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mefSoamTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 15007, 1, 1))
mefSoamTcMib.setRevisions(('2012-01-10 00:00', '2010-10-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mefSoamTcMib.setRevisionsDescriptions(('Updated text to add textual conventions for the SOAM PM MIB.', 'Initial Version.',))
if mibBuilder.loadTexts: mefSoamTcMib.setLastUpdated('201201100000Z')
if mibBuilder.loadTexts: mefSoamTcMib.setOrganization('Metro Ethernet Forum')
if mibBuilder.loadTexts: mefSoamTcMib.setContactInfo('Web URL: http://metroethernetforum.org/\n        E-mail:  mibs@metroethernetforum.org\n        Postal:  Metro Ethernet Forum\n                 6033 W. Century Boulevard, Suite 830\n                 Los Angeles, CA 90045\n                 U.S.A.\n        Phone:   +1 310-642-2800\n        Fax:     +1 310-642-2808')
if mibBuilder.loadTexts: mefSoamTcMib.setDescription('This MIB module defines the textual conventions used \n        throughout the Ethernet Services Operations, Administration\n        and Maintenance MIB modules.\n        Copyright 2010 Metro Ethernet Forum.\n        All rights reserved.')
class MefSoamTcAvailabilityType(TextualConvention, Integer32):
    description = 'This enumeration data type defines the availability of a session, \n        measured by a loss measurement session.\n\n        The valid enumerated values associated with this type are:\n\n        available(1)       indicates the MEP is available.\n\n        unavailable(2)     indicates the MEP is unavailable.\n\n        unknown(3)         indicates the availability is not known, for\n                           instance because insufficient time has passed to\n                           make an availability calculation, the time has been\n                           excluded because of a maintenance interval, or because \n                           availability measurement is not enabled.\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("available", 1), ("unavailable", 2), ("unknown", 3))

class MefSoamTcConnectivityStatusType(TextualConvention, Integer32):
    reference = '[MEF17] 9.2 and [MEF7.1] III.2 Enumeration'
    description = 'This enumeration data type defines the connectivity status\n        of a Maintenance Entity (ME) or a Maintenance Entity Group (MEG).\n\n        The valid enumerated values associated with this type are:\n\n        inactive(1)        indicates an inactive connectivity state of a group\n                           and refers to the inability to exchange SOAM PDU frame\n                           among any of the entities in a group.\n\n        active(2)          indicates an active connectivity state of a group \n                           and refers to the ability to exchange SOAM PDU frames\n                           among all the entities in a group\n\n        partiallyActive(3) indicates a partially active connectivity state of a\n                           group and refers to the ability to exchange SOAM PDU\n                           frames among some entities of a group. This enumerated \n                           value is only applicable for Multipoint-to-Multipoint \n                           MEG.\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inactive", 1), ("active", 2), ("partiallyActive", 3))

class MefSoamTcDataPatternType(TextualConvention, Integer32):
    description = 'This enumeration data type indicates the type of data pattern to be\n        sent in an OAM PDU Data TLV.\n\n        The valid enumerated values associated with this type are:\n\n        zeroPattern(1)          indicates the Data TLV contains all zeros\n        onesPattern(2)          indicates the Data TLV contains all ones\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("zeroPattern", 1), ("onesPattern", 2))

class MefSoamTcDelayMeasurementBinType(TextualConvention, Integer32):
    description = 'This enumeration data type is used to distinguish between \n        measurement bins for Frame Delay, Frame Delay Range, and \n        Inter-frame Delay variation.\n\n        The valid enumerated values associated with this type are:\n\n        twoWayFrameDelay(1)        indicates a measurement bin for two-way\n                                   Frame Delay.\n        forwardFrameDelay(2)       indicates a measurement bin for one-way\n                                   Frame Delay in the forward direction.\n        backwardFrameDelay(3)      indicates a measurement bin for one-way\n                                   Frame Delay in the backward direction.\n        twoWayIfdv(4)              indicates a measurement bin for two-way\n                                   Inter-frame Delay Variation.\n        forwardIfdv(5)             indicates a measurement bin for one-way\n                                   Inter-frame Delay Variation in the forward\n                                   direction.\n        backwardIfdv(6)            indicates a measurement bin for one-way\n                                   Inter-frame Delay Variation in the backward\n                                   direction.\n        twoWayFrameDelayRange(7)   indicates a measurement bin for two-way\n                                   Frame Delay Range.\n        forwardFrameDelayRange(8)  indicates a measurement bin for one-way\n                                   Frame Delay Range in the forward direction.\n        backwardFrameDelayRange(9) indicates a measurement bin for one-way\n                                   Frame Delay Range in the backward direction.\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("twoWayFrameDelay", 1), ("forwardFrameDelay", 2), ("backwardFrameDelay", 3), ("twoWayIfdv", 4), ("forwardIfdv", 5), ("backwardIfdv", 6), ("twoWayFrameDelayRange", 7), ("forwardFrameDelayRange", 8), ("backwardFrameDelayRange", 9))

class MefSoamTcIntervalTypeAisLck(TextualConvention, Integer32):
    reference = '[MEF7.1] III.2 Enumeration, [Y.1731] 7.4, 7.6'
    description = 'This enumeration data type defines the AIS/LCK transmission time\n         interval for an Alarm Indication Signal (AIS) or LCK frame.\n\n         The valid enumerated values associated with this type are:\n\n         oneSecond(1)  indicates a one second transmission interval.\n         oneMinute(2)  indicates a one minute transmission interval.\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oneSecond", 1), ("oneMinute", 2))

class MefSoamTcMeasurementPeriodType(TextualConvention, Unsigned32):
    reference = '[MEF SOAM-PM] R56'
    description = 'Indicates the transmission time between the SOAM PM frames for a\n        PM session, in ms. \n       '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(3, 3600000)

class MefSoamTcMegIdType(TextualConvention, Integer32):
    reference = '[Y.1731] Table A-1, [CFM] 17.5, 21.6.5.1'
    description = 'This enumeration data type indicates the format of the MEG ID\n        that is sent in the OAM PDUs. Types 1-4 are more fully explained\n        in [CFM] 17.5. Type 32 is from [Y.1731] Annex A.\n\n        The valid enumerated values associated with this type are:\n\n        primaryVid(1)      Primary VLAN ID.\n                           12 bits represented in a 2-octet integer:\n                           - 4 least significant bits of the first\n                               byte contains the 4 most significant\n                               bits of the 12 bits primary VID\n                           - second byte contains the 8 least\n                             significant bits of the primary VID\n\n                              0 1 2 3 4 5 6 7 8\n                              +-+-+-+-+-+-+-+-+\n                              |0 0 0 0| (MSB) |\n                              +-+-+-+-+-+-+-+-+\n                              |  VID   LSB    |\n                              +-+-+-+-+-+-+-+-+\n\n        charString(2)      RFC2579 DisplayString, except that the\n                           character codes 0-31 (decimal) are not\n                           used. (1..45) octets\n\n        unsignedInt16 (3)  2-octet integer/big endian\n\n        rfc2865VpnId(4)    RFC 2685 VPN ID\n                           3 octet VPN authority Organizationally\n                           Unique Identifier followed by 4 octet VPN\n                           index identifying VPN according to the OUI:\n\n                               0 1 2 3 4 5 6 7 8\n                               +-+-+-+-+-+-+-+-+\n                               | VPN OUI (MSB) |\n                               +-+-+-+-+-+-+-+-+\n                               | VPN OUI |\n                               +-+-+-+-+-+-+-+-+\n                               | VPN OUI (LSB) |\n                               +-+-+-+-+-+-+-+-+\n                               |VPN Index (MSB)|\n                               +-+-+-+-+-+-+-+-+\n                               |  VPN  Index   |\n                               +-+-+-+-+-+-+-+-+\n                               |  VPN  Index   |\n                               +-+-+-+-+-+-+-+-+\n                               |VPN Index (LSB)|\n                               +-+-+-+-+-+-+-+-+\n\n        iccBased (32)      ICC-based MEG ID Format, thirteen octet field\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 32))
    namedValues = NamedValues(("primaryVid", 1), ("charString", 2), ("unsignedInt16", 3), ("rfc2865VpnId", 4), ("iccBased", 32))

class MefSoamTcOperationTimeType(TextualConvention, Integer32):
    reference = '[SOAM-PM] R2, [SOAM-FM] 8.7'
    description = 'This enumeration data type indicates the operation type start\n        or end time to indicate when an OAM operation is \n        initiated or stopped.\n\n        The valid enumerated values associated with this type are:\n\n        none(1)       The operation is never started or is stopped immediately\n                      if used to indicate a start time, or the operation never \n                      ends if it is used to indicate an end time\n        immediate(2)  The operation is to begin immediately\n        relative(3)   The operation is to begin at a relative time from the\n                      current time or stop a relative time after it has started\n        fixed(4)      The operation is to begin/stop at the given UTC time/date\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("immediate", 2), ("relative", 3), ("fixed", 4))

class MefSoamTcSessionType(TextualConvention, Integer32):
    description = 'This enumeration data type defines the status of PM session of a MEP.\n\n        The valid enumerated values associated with this type are:\n\n        proactive(1)     indicates the measurement instance is Proactive\n        onDemand(2)      indicates the measurement instance is On-demand\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("proactive", 1), ("onDemand", 2))

class MefSoamTcStatusType(TextualConvention, Integer32):
    description = 'This enumeration data type defines the status of PM session of a MEP.\n\n        The valid enumerated values associated with this type are:\n\n        active(1)        indicates the measurement instance is active\n        notActive(2)     indicates the measurement instance is not active\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("notActive", 2))

class MefSoamTcTestPatternType(TextualConvention, Integer32):
    reference = '[MEF7.1], Appendix III.2 Enumeration, [Y.1731] 7.7'
    description = 'This enumeration data type indicates the type of test pattern to be\n        sent in an OAM PDU Test TLV.\n\n        The valid enumerated values associated with this type are:\n\n        null(1)       Null signal without CRC-32\n        nullCrc32(2)  Null signal with CRC-32\n        prbs(3)       PRBS 2^31-1 without CRC-32\n        prbsCrc32(4)  PRBS 2^31-1 with CRC-32\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("null", 1), ("nullCrc32", 2), ("prbs", 3), ("prbsCrc32", 4))

mibBuilder.exportSymbols("MEF-SOAM-TC-MIB", mefSoamTcMib=mefSoamTcMib, MefSoamTcMeasurementPeriodType=MefSoamTcMeasurementPeriodType, MefSoamTcIntervalTypeAisLck=MefSoamTcIntervalTypeAisLck, MefSoamTcAvailabilityType=MefSoamTcAvailabilityType, MefSoamTcConnectivityStatusType=MefSoamTcConnectivityStatusType, MefSoamTcOperationTimeType=MefSoamTcOperationTimeType, MefSoamTcDelayMeasurementBinType=MefSoamTcDelayMeasurementBinType, MefSoamTcSessionType=MefSoamTcSessionType, MefSoamTcStatusType=MefSoamTcStatusType, MefSoamTcDataPatternType=MefSoamTcDataPatternType, MefSoamTcTestPatternType=MefSoamTcTestPatternType, MefSoamTcMegIdType=MefSoamTcMegIdType, PYSNMP_MODULE_ID=mefSoamTcMib)
