#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/PerfHist-TC-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:46:22 2021
# On host fv-az77-248 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Bits, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Integer32, Gauge32, mib_2, TimeTicks, ObjectIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Bits", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Integer32", "Gauge32", "mib-2", "TimeTicks", "ObjectIdentity", "NotificationType", "Counter64")
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

mibBuilder.exportSymbols("PerfHist-TC-MIB", PerfIntervalCount=PerfIntervalCount, PerfCurrentCount=PerfCurrentCount, PYSNMP_MODULE_ID=perfHistTCMIB, PerfTotalCount=PerfTotalCount, perfHistTCMIB=perfHistTCMIB)
