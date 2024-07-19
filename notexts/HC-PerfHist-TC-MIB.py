#
# PySNMP MIB module HC-PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/HC-PerfHist-TC-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 12:37:47 2024
# On host fv-az1247-562 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, mib_2, Unsigned32, Bits, TimeTicks, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Counter32, ModuleIdentity, MibIdentifier, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "mib-2", "Unsigned32", "Bits", "TimeTicks", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Counter32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Counter64")
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

mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", HCPerfTimeElapsed=HCPerfTimeElapsed, HCPerfTotalCount=HCPerfTotalCount, HCPerfCurrentCount=HCPerfCurrentCount, HCPerfValidIntervals=HCPerfValidIntervals, HCPerfIntervalCount=HCPerfIntervalCount, PYSNMP_MODULE_ID=hcPerfHistTCMIB, HCPerfIntervalThreshold=HCPerfIntervalThreshold, hcPerfHistTCMIB=hcPerfHistTCMIB, HCPerfInvalidIntervals=HCPerfInvalidIntervals)
