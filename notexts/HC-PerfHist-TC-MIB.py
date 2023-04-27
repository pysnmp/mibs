#
# PySNMP MIB module HC-PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/HC-PerfHist-TC-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 09:15:27 2023
# On host fv-az590-874 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, MibIdentifier, mib_2, TimeTicks, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Bits, Counter64, ObjectIdentity, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "MibIdentifier", "mib-2", "TimeTicks", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Bits", "Counter64", "ObjectIdentity", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hcPerfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 107))
hcPerfHistTCMIB.setRevisions(('2004-02-03 00:00',))
if mibBuilder.loadTexts: hcPerfHistTCMIB.setLastUpdated('200402030000Z')
if mibBuilder.loadTexts: hcPerfHistTCMIB.setOrganization('ADSLMIB Working Group')
class HCPerfValidIntervals(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 96)

class HCPerfInvalidIntervals(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 96)

class HCPerfTimeElapsed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 86399)

class HCPerfIntervalThreshold(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 900)

class HCPerfCurrentCount(TextualConvention, Counter64):
    status = 'current'

class HCPerfIntervalCount(TextualConvention, Counter64):
    status = 'current'

class HCPerfTotalCount(TextualConvention, Counter64):
    status = 'current'

mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", PYSNMP_MODULE_ID=hcPerfHistTCMIB, HCPerfInvalidIntervals=HCPerfInvalidIntervals, HCPerfTotalCount=HCPerfTotalCount, HCPerfIntervalCount=HCPerfIntervalCount, hcPerfHistTCMIB=hcPerfHistTCMIB, HCPerfIntervalThreshold=HCPerfIntervalThreshold, HCPerfCurrentCount=HCPerfCurrentCount, HCPerfTimeElapsed=HCPerfTimeElapsed, HCPerfValidIntervals=HCPerfValidIntervals)
