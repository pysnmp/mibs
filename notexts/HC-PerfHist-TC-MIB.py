#
# PySNMP MIB module HC-PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/HC-PerfHist-TC-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:53:55 2022
# On host fv-az74-933 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, Unsigned32, iso, TimeTicks, IpAddress, mib_2, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, ObjectIdentity, NotificationType, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Unsigned32", "iso", "TimeTicks", "IpAddress", "mib-2", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "ObjectIdentity", "NotificationType", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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

mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", HCPerfCurrentCount=HCPerfCurrentCount, HCPerfTotalCount=HCPerfTotalCount, HCPerfTimeElapsed=HCPerfTimeElapsed, PYSNMP_MODULE_ID=hcPerfHistTCMIB, HCPerfInvalidIntervals=HCPerfInvalidIntervals, HCPerfIntervalThreshold=HCPerfIntervalThreshold, hcPerfHistTCMIB=hcPerfHistTCMIB, HCPerfValidIntervals=HCPerfValidIntervals, HCPerfIntervalCount=HCPerfIntervalCount)
