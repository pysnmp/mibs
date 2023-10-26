#
# PySNMP MIB module ITU-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/ITU-ALARM-TC-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 11:00:10 2023
# On host fv-az552-338 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, iso, Gauge32, ObjectIdentity, MibIdentifier, Integer32, mib_2, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "iso", "Gauge32", "ObjectIdentity", "MibIdentifier", "Integer32", "mib-2", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ituAlarmTc = ModuleIdentity((1, 3, 6, 1, 2, 1, 120))
ituAlarmTc.setRevisions(('2004-09-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ituAlarmTc.setRevisionsDescriptions(('Initial version, published as RFC 3877.',))
if mibBuilder.loadTexts: ituAlarmTc.setLastUpdated('200409090000Z')
if mibBuilder.loadTexts: ituAlarmTc.setOrganization('IETF Distributed Management Working Group')
if mibBuilder.loadTexts: ituAlarmTc.setContactInfo(' WG EMail: disman@ietf.org\n           Subscribe: disman-request@ietf.org\n           http://www.ietf.org/html.charters/disman-charter.html\n\n           Chair:     Randy Presuhn\n                      randy_presuhn@mindspring.com\n\n           Editors:   Sharon Chisholm\n                      Nortel Networks\n                      PO Box 3511 Station C\n                      Ottawa, Ont.  K1Y 4H7\n                      Canada\n                      schishol@nortelnetworks.com\n\n                      Dan Romascanu\n                      Avaya\n                      Atidim Technology Park, Bldg. #3\n                      Tel Aviv, 61131\n                      Israel\n                      Tel: +972-3-645-8414\n                      Email: dromasca@avaya.com')
if mibBuilder.loadTexts: ituAlarmTc.setDescription('This MIB module defines the ITU Alarm\n         textual convention for objects not expected to require\n         regular extension.\n\n         Copyright (C) The Internet Society (2004).  The\n         initial version of this MIB module was published\n         in RFC 3877.  For full legal notices see the RFC\n         itself.  Supplementary information may be available on:\n         http://www.ietf.org/copyrights/ianamib.html')
class ItuPerceivedSeverity(TextualConvention, Integer32):
    reference = "ITU Recommendation M.3100, 'Generic Network Information\n            Model', 1995\n            ITU Recommendation X.733, 'Information Technology - Open\n            Systems Interconnection - System Management: Alarm\n            Reporting Function', 1992"
    description = 'ITU perceived severity values'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6))

class ItuTrendIndication(TextualConvention, Integer32):
    reference = "ITU Recommendation M.3100, 'Generic Network Information\n            Model', 1995\n            ITU Recommendation X.733, 'Information Technology - Open\n            Systems Interconnection - System Management: Alarm\n            Reporting Function', 1992"
    description = 'ITU trend indication values for alarms.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("moreSevere", 1), ("noChange", 2), ("lessSevere", 3))

mibBuilder.exportSymbols("ITU-ALARM-TC-MIB", PYSNMP_MODULE_ID=ituAlarmTc, ItuTrendIndication=ItuTrendIndication, ituAlarmTc=ituAlarmTc, ItuPerceivedSeverity=ItuPerceivedSeverity)
