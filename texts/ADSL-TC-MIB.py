#
# PySNMP MIB module ADSL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ADSL-TC-MIB
# Produced by pysmi-1.1.3 at Tue Nov 30 02:48:21 2021
# On host fv-az77-605 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, transmission, Counter64, MibIdentifier, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Unsigned32, Integer32, IpAddress, iso, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "transmission", "Counter64", "MibIdentifier", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Unsigned32", "Integer32", "IpAddress", "iso", "ObjectIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adsltcmib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 94, 2))
adsltcmib.setRevisions(('1999-08-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adsltcmib.setRevisionsDescriptions(('Initial Version, published as RFC 2662',))
if mibBuilder.loadTexts: adsltcmib.setLastUpdated('9908190000Z')
if mibBuilder.loadTexts: adsltcmib.setOrganization('IETF ADSL MIB Working Group')
if mibBuilder.loadTexts: adsltcmib.setContactInfo('\n       Gregory Bathrick\n       AG Communication Systems\n       A Subsidiary of Lucent Technologies\n       2500 W Utopia Rd.\n       Phoenix, AZ 85027 USA\n       Tel: +1 602-582-7679\n       Fax: +1 602-582-7697\n       E-mail: bathricg@agcs.com\n\n       Faye Ly\n       Copper Mountain Networks\n       Norcal Office\n       2470 Embarcadero Way\n       Palo Alto, CA 94303\n       Tel: +1 650-858-8500\n       Fax: +1 650-858-8085\n       E-Mail: faye@coppermountain.com\n       IETF ADSL MIB Working Group (adsl@xlist.agcs.com)\n       ')
if mibBuilder.loadTexts: adsltcmib.setDescription('The MIB module which provides a ADSL\n           Line Coding Textual Convention to be used\n           by ADSL Lines.')
class AdslLineCodingType(TextualConvention, Integer32):
    description = 'This data type is used as the syntax for the ADSL\n               Line Code.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("dmt", 2), ("cap", 3), ("qam", 4))

class AdslPerfCurrDayCount(TextualConvention, Gauge32):
    description = 'A counter associated with interface performance\n               measurements in a current 1-day (24 hour) measurement\n               interval.\n\n               The value of this counter starts at zero at the\n               beginning of an interval and is increased when\n               associated events occur, until the end of the\n               1-day interval.  At that time the value of the\n               counter is stored in the previous 1-day history\n               interval, if available, and the current interval\n               counter is restarted at zero.\n\n               In the case where the agent has no valid data available\n               for this interval the corresponding object\n               instance is not available and upon a retrieval\n               request a corresponding error message shall be\n               returned to indicate that this instance does\n               not exist (for example, a noSuchName error for\n               SNMPv1 and a noSuchInstance for SNMPv2 GET\n               operation).'
    status = 'current'

class AdslPerfPrevDayCount(TextualConvention, Gauge32):
    description = 'A counter associated with interface performance\n               measurements during the most previous 1-day (24 hour)\n               measurement interval.  The value of this counter is\n               equal to the value of the current day counter at\n               the end of its most recent interval.\n\n               In the case where the agent has no valid data available\n               for this interval the corresponding object\n               instance is not available and upon a retrieval\n               request a corresponding error message shall be\n               returned to indicate that this instance does\n               not exist (for example, a noSuchName error for\n               SNMPv1 and a noSuchInstance for SNMPv2 GET\n               operation).'
    status = 'current'

class AdslPerfTimeElapsed(TextualConvention, Gauge32):
    description = "The number of seconds that have elapsed since\n               the beginning of the current measurement period.\n               If, for some reason, such as an adjustment in the\n               system's time-of-day clock, the current interval\n               exceeds the maximum value, the agent will return\n               the maximum value."
    status = 'current'

mibBuilder.exportSymbols("ADSL-TC-MIB", AdslPerfCurrDayCount=AdslPerfCurrDayCount, AdslLineCodingType=AdslLineCodingType, PYSNMP_MODULE_ID=adsltcmib, AdslPerfPrevDayCount=AdslPerfPrevDayCount, AdslPerfTimeElapsed=AdslPerfTimeElapsed, adsltcmib=adsltcmib)
