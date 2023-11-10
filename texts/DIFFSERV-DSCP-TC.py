#
# PySNMP MIB module DIFFSERV-DSCP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/DIFFSERV-DSCP-TC
# Produced by pysmi-1.1.10 at Fri Nov 10 11:08:26 2023
# On host fv-az1251-57 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, Bits, MibIdentifier, iso, Integer32, IpAddress, mib_2, Gauge32, ModuleIdentity, ObjectIdentity, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Bits", "MibIdentifier", "iso", "Integer32", "IpAddress", "mib-2", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
diffServDSCPTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 96))
diffServDSCPTC.setRevisions(('2002-05-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: diffServDSCPTC.setRevisionsDescriptions(('Initial version, published as RFC 3289.',))
if mibBuilder.loadTexts: diffServDSCPTC.setLastUpdated('200205090000Z')
if mibBuilder.loadTexts: diffServDSCPTC.setOrganization('IETF Differentiated Services WG')
if mibBuilder.loadTexts: diffServDSCPTC.setContactInfo('       Fred Baker\n               Cisco Systems\n               1121 Via Del Rey\n               Santa Barbara, CA 93117, USA\n               E-mail: fred@cisco.com\n\n               Kwok Ho Chan\n               Nortel Networks\n               600 Technology Park Drive\n               Billerica, MA 01821, USA\n               E-mail: khchan@nortelnetworks.com\n\n               Andrew Smith\n               Harbour Networks\n               Jiuling Building\n               21 North Xisanhuan Ave.\n               Beijing, 100089, PRC\n               E-mail: ah_smith@acm.org\n\n                 Differentiated Services Working Group:\n                 diffserv@ietf.org')
if mibBuilder.loadTexts: diffServDSCPTC.setDescription('The Textual Conventions defined in this module should be used\n       whenever a Differentiated Services Code Point is used in a MIB.')
class Dscp(TextualConvention, Integer32):
    reference = 'RFC 2474, RFC 2780'
    description = 'A Differentiated Services Code-Point that may be used for\n       marking a traffic stream.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

class DscpOrAny(TextualConvention, Integer32):
    reference = 'RFC 2474, RFC 2780'
    description = 'The IP header Differentiated Services Code-Point that may be\n\n\n\n       used for discriminating among traffic streams. The value -1 is\n       used to indicate a wild card i.e. any value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 63), )
mibBuilder.exportSymbols("DIFFSERV-DSCP-TC", diffServDSCPTC=diffServDSCPTC, PYSNMP_MODULE_ID=diffServDSCPTC, DscpOrAny=DscpOrAny, Dscp=Dscp)
