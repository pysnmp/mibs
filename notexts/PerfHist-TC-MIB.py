#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/PerfHist-TC-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:15:10 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Unsigned32, IpAddress, Bits, ObjectIdentity, TimeTicks, ModuleIdentity, Counter64, mib_2, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Unsigned32", "IpAddress", "Bits", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Counter64", "mib-2", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
perfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 58))
if mibBuilder.loadTexts: perfHistTCMIB.setLastUpdated('9811071100Z')
if mibBuilder.loadTexts: perfHistTCMIB.setOrganization('IETF AToMMIB and TrunkMIB WGs')
class PerfCurrentCount(TextualConvention, Gauge32):
    status = 'current'

class PerfIntervalCount(TextualConvention, Gauge32):
    status = 'current'

class PerfTotalCount(TextualConvention, Gauge32):
    status = 'current'

mibBuilder.exportSymbols("PerfHist-TC-MIB", PYSNMP_MODULE_ID=perfHistTCMIB, PerfCurrentCount=PerfCurrentCount, PerfTotalCount=PerfTotalCount, perfHistTCMIB=perfHistTCMIB, PerfIntervalCount=PerfIntervalCount)
