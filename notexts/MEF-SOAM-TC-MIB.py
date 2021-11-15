#
# PySNMP MIB module MEF-SOAM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MEF-SOAM-TC-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:46:22 2021
# On host fv-az77-248 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, enterprises, Unsigned32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Integer32, Counter32, Counter64, TimeTicks, ObjectIdentity, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "Unsigned32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Integer32", "Counter32", "Counter64", "TimeTicks", "ObjectIdentity", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mefSoamTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 15007, 1, 1))
mefSoamTcMib.setRevisions(('2012-01-10 00:00', '2010-10-11 00:00',))
if mibBuilder.loadTexts: mefSoamTcMib.setLastUpdated('201201100000Z')
if mibBuilder.loadTexts: mefSoamTcMib.setOrganization('Metro Ethernet Forum')
class MefSoamTcAvailabilityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("available", 1), ("unavailable", 2), ("unknown", 3))

class MefSoamTcConnectivityStatusType(TextualConvention, Integer32):
    reference = '[MEF17] 9.2 and [MEF7.1] III.2 Enumeration'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inactive", 1), ("active", 2), ("partiallyActive", 3))

class MefSoamTcDataPatternType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("zeroPattern", 1), ("onesPattern", 2))

class MefSoamTcDelayMeasurementBinType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("twoWayFrameDelay", 1), ("forwardFrameDelay", 2), ("backwardFrameDelay", 3), ("twoWayIfdv", 4), ("forwardIfdv", 5), ("backwardIfdv", 6), ("twoWayFrameDelayRange", 7), ("forwardFrameDelayRange", 8), ("backwardFrameDelayRange", 9))

class MefSoamTcIntervalTypeAisLck(TextualConvention, Integer32):
    reference = '[MEF7.1] III.2 Enumeration, [Y.1731] 7.4, 7.6'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oneSecond", 1), ("oneMinute", 2))

class MefSoamTcMeasurementPeriodType(TextualConvention, Unsigned32):
    reference = '[MEF SOAM-PM] R56'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(3, 3600000)

class MefSoamTcMegIdType(TextualConvention, Integer32):
    reference = '[Y.1731] Table A-1, [CFM] 17.5, 21.6.5.1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 32))
    namedValues = NamedValues(("primaryVid", 1), ("charString", 2), ("unsignedInt16", 3), ("rfc2865VpnId", 4), ("iccBased", 32))

class MefSoamTcOperationTimeType(TextualConvention, Integer32):
    reference = '[SOAM-PM] R2, [SOAM-FM] 8.7'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("immediate", 2), ("relative", 3), ("fixed", 4))

class MefSoamTcSessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("proactive", 1), ("onDemand", 2))

class MefSoamTcStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("notActive", 2))

class MefSoamTcTestPatternType(TextualConvention, Integer32):
    reference = '[MEF7.1], Appendix III.2 Enumeration, [Y.1731] 7.7'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("null", 1), ("nullCrc32", 2), ("prbs", 3), ("prbsCrc32", 4))

mibBuilder.exportSymbols("MEF-SOAM-TC-MIB", MefSoamTcDataPatternType=MefSoamTcDataPatternType, MefSoamTcAvailabilityType=MefSoamTcAvailabilityType, PYSNMP_MODULE_ID=mefSoamTcMib, MefSoamTcMegIdType=MefSoamTcMegIdType, MefSoamTcOperationTimeType=MefSoamTcOperationTimeType, MefSoamTcTestPatternType=MefSoamTcTestPatternType, MefSoamTcConnectivityStatusType=MefSoamTcConnectivityStatusType, MefSoamTcSessionType=MefSoamTcSessionType, MefSoamTcMeasurementPeriodType=MefSoamTcMeasurementPeriodType, MefSoamTcStatusType=MefSoamTcStatusType, mefSoamTcMib=mefSoamTcMib, MefSoamTcIntervalTypeAisLck=MefSoamTcIntervalTypeAisLck, MefSoamTcDelayMeasurementBinType=MefSoamTcDelayMeasurementBinType)
