#
# PySNMP MIB module HC-PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/HC-PerfHist-TC-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 15:54:12 2024
# On host fv-az1205-935 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, MibIdentifier, TimeTicks, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Counter64, iso, Unsigned32, Bits, Gauge32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "MibIdentifier", "TimeTicks", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Counter64", "iso", "Unsigned32", "Bits", "Gauge32", "ModuleIdentity", "IpAddress")
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

mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", HCPerfInvalidIntervals=HCPerfInvalidIntervals, HCPerfValidIntervals=HCPerfValidIntervals, HCPerfCurrentCount=HCPerfCurrentCount, HCPerfTimeElapsed=HCPerfTimeElapsed, hcPerfHistTCMIB=hcPerfHistTCMIB, HCPerfIntervalThreshold=HCPerfIntervalThreshold, HCPerfTotalCount=HCPerfTotalCount, PYSNMP_MODULE_ID=hcPerfHistTCMIB, HCPerfIntervalCount=HCPerfIntervalCount)
