#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/PerfHist-TC-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:56:41 2022
# On host fv-az74-435 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Counter32, ObjectIdentity, IpAddress, Unsigned32, MibIdentifier, ModuleIdentity, NotificationType, mib_2, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Counter32", "ObjectIdentity", "IpAddress", "Unsigned32", "MibIdentifier", "ModuleIdentity", "NotificationType", "mib-2", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
perfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 58))
if mibBuilder.loadTexts: perfHistTCMIB.setLastUpdated('9811071100Z')
if mibBuilder.loadTexts: perfHistTCMIB.setOrganization('IETF AToMMIB and TrunkMIB WGs')
if mibBuilder.loadTexts: perfHistTCMIB.setContactInfo('Kaj Tesink\n              Postal:  Bellcore\n                       331 Newman Springs Road\n                       Red Bank, NJ 07701\n                       USA\n              Tel:     +1 732 758 5254\n              Fax:     +1 732 758 2269\n              E-mail:  kaj@bellcore.com')
if mibBuilder.loadTexts: perfHistTCMIB.setDescription('This MIB Module provides Textual Conventions\n             to be used by systems supporting 15 minute\n             based performance history counts.')
class PerfCurrentCount(TextualConvention, Gauge32):
    description = 'A counter associated with a\n               performance measurement in a current 15\n               minute measurement interval. The value\n               of this counter starts from zero and is\n               increased when associated events occur,\n               until the end of the 15 minute interval.\n               At that time the value of the counter is\n               stored in the first 15 minute history\n               interval, and the CurrentCount is\n               restarted at zero. In the\n               case where the agent has no valid data\n               available for the current interval the\n               corresponding object instance is not\n               available and upon a retrieval request\n               a corresponding error message shall be\n               returned to indicate that this instance\n               does not exist (for example, a noSuchName\n               error for SNMPv1 and a noSuchInstance for\n               SNMPv2 GET operation).'
    status = 'current'

class PerfIntervalCount(TextualConvention, Gauge32):
    description = 'A counter associated with a\n               performance measurement in a previous\n               15 minute measurement interval. In the\n               case where the agent has no valid data\n               available for a particular interval the\n               corresponding object instance is not\n               available and upon a retrieval request\n               a corresponding error message shall be\n               returned to indicate that this instance\n               does not exist (for example, a noSuchName\n               error for SNMPv1 and a noSuchInstance for\n               SNMPv2 GET operation).\n               In a system supporting\n               a history of n intervals with\n               IntervalCount(1) and IntervalCount(n) the\n               most and least recent intervals\n               respectively, the following applies at\n               the end of a 15 minute interval:\n               - discard the value of IntervalCount(n)\n               - the value of IntervalCount(i) becomes that\n                 of IntervalCount(i-1) for n >= i > 1\n               - the value of IntervalCount(1) becomes that\n                 of CurrentCount\n               - the TotalCount, if supported, is adjusted.'
    status = 'current'

class PerfTotalCount(TextualConvention, Gauge32):
    description = 'A counter associated with a\n               performance measurements aggregating the\n               previous valid 15 minute measurement\n               intervals. (Intervals for which no valid\n               data was available are not counted)'
    status = 'current'

mibBuilder.exportSymbols("PerfHist-TC-MIB", PYSNMP_MODULE_ID=perfHistTCMIB, PerfIntervalCount=PerfIntervalCount, perfHistTCMIB=perfHistTCMIB, PerfTotalCount=PerfTotalCount, PerfCurrentCount=PerfCurrentCount)
