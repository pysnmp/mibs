#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/PerfHist-TC-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 15:50:15 2021
# On host fv-az74-277 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, Integer32, Unsigned32, MibIdentifier, Gauge32, Counter32, iso, ModuleIdentity, IpAddress, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Integer32", "Unsigned32", "MibIdentifier", "Gauge32", "Counter32", "iso", "ModuleIdentity", "IpAddress", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
perfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 58))
if mibBuilder.loadTexts: perfHistTCMIB.setLastUpdated('9811071100Z')
if mibBuilder.loadTexts: perfHistTCMIB.setOrganization('IETF AToMMIB and TrunkMIB WGs')
if mibBuilder.loadTexts: perfHistTCMIB.setContactInfo('Kaj Tesink\n\t      Postal:  Bellcore\n\t\t       331 Newman Springs Road\n\t\t       Red Bank, NJ 07701\n\t\t       USA\n\t      Tel:     +1 732 758 5254\n\t      Fax:     +1 732 758 2269\n\t      E-mail:  kaj@bellcore.com')
if mibBuilder.loadTexts: perfHistTCMIB.setDescription('This MIB Module provides Textual Conventions\n\t     to\tbe used\tby systems supporting 15 minute\n\t     based performance history counts.')
class PerfCurrentCount(TextualConvention, Gauge32):
    description = 'A counter associated with a\n\t       performance measurement in a current 15\n\t       minute measurement interval. The\tvalue\n\t       of this counter starts from zero\tand is\n\n\n\n\n\n\t       increased when associated events\toccur,\n\t       until the end of\tthe 15 minute interval.\n\t       At that time the\tvalue of the counter is\n\t       stored in the first 15 minute history\n\t       interval, and the CurrentCount is\n\t       restarted at zero. In the\n\t       case where the agent has\tno valid data\n\t       available for the current interval the\n\t       corresponding object instance is\tnot\n\t       available and upon a retrieval request\n\t       a corresponding error message shall be\n\t       returned\tto indicate that this instance\n\t       does not\texist (for example, a noSuchName\n\t       error for SNMPv1\tand a noSuchInstance for\n\t       SNMPv2 GET operation).'
    status = 'current'

class PerfIntervalCount(TextualConvention, Gauge32):
    description = 'A counter associated with a\n\t       performance measurement in a previous\n\t       15 minute measurement interval. In the\n\t       case where the agent has\tno valid data\n\t       available for a particular interval the\n\t       corresponding object instance is\tnot\n\t       available and upon a retrieval request\n\t       a corresponding error message shall be\n\t       returned\tto indicate that this instance\n\t       does not\texist (for example, a noSuchName\n\t       error for SNMPv1\tand a noSuchInstance for\n\t       SNMPv2 GET operation).\n\t       In a system supporting\n\t       a history of n intervals\twith\n\t       IntervalCount(1)\tand IntervalCount(n) the\n\t       most and\tleast recent intervals\n\t       respectively, the following applies at\n\t       the end of a 15 minute interval:\n\t       - discard the value of IntervalCount(n)\n\t       - the value of IntervalCount(i) becomes that\n\t\t of IntervalCount(i-1) for n >=\ti > 1\n\t       - the value of IntervalCount(1) becomes that\n\t\t of CurrentCount\n\t       - the TotalCount, if supported, is adjusted.'
    status = 'current'

class PerfTotalCount(TextualConvention, Gauge32):
    description = 'A counter associated with a\n\t       performance measurements\taggregating the\n\t       previous\tvalid 15 minute\tmeasurement\n\t       intervals. (Intervals for which no valid\n\t       data was\tavailable are not counted)'
    status = 'current'

mibBuilder.exportSymbols("PerfHist-TC-MIB", perfHistTCMIB=perfHistTCMIB, PYSNMP_MODULE_ID=perfHistTCMIB, PerfCurrentCount=PerfCurrentCount, PerfIntervalCount=PerfIntervalCount, PerfTotalCount=PerfTotalCount)
