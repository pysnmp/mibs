#
# PySNMP MIB module HC-PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/HC-PerfHist-TC-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 11:58:52 2024
# On host fv-az888-540 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, MibIdentifier, mib_2, NotificationType, Gauge32, Unsigned32, Bits, Counter32, Counter64, IpAddress, iso, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "MibIdentifier", "mib-2", "NotificationType", "Gauge32", "Unsigned32", "Bits", "Counter32", "Counter64", "IpAddress", "iso", "TimeTicks", "ModuleIdentity")
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

mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", HCPerfInvalidIntervals=HCPerfInvalidIntervals, HCPerfValidIntervals=HCPerfValidIntervals, hcPerfHistTCMIB=hcPerfHistTCMIB, HCPerfIntervalCount=HCPerfIntervalCount, PYSNMP_MODULE_ID=hcPerfHistTCMIB, HCPerfIntervalThreshold=HCPerfIntervalThreshold, HCPerfTotalCount=HCPerfTotalCount, HCPerfCurrentCount=HCPerfCurrentCount, HCPerfTimeElapsed=HCPerfTimeElapsed)
