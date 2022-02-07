#
# PySNMP MIB module ITU-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/ITU-ALARM-TC-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 15:45:03 2022
# On host fv-az77-513 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, TimeTicks, Gauge32, Counter32, MibIdentifier, iso, ObjectIdentity, Unsigned32, Bits, IpAddress, mib_2, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "TimeTicks", "Gauge32", "Counter32", "MibIdentifier", "iso", "ObjectIdentity", "Unsigned32", "Bits", "IpAddress", "mib-2", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ituAlarmTc = ModuleIdentity((1, 3, 6, 1, 2, 1, 120))
ituAlarmTc.setRevisions(('2004-09-09 00:00',))
if mibBuilder.loadTexts: ituAlarmTc.setLastUpdated('200409090000Z')
if mibBuilder.loadTexts: ituAlarmTc.setOrganization('IETF Distributed Management Working Group')
class ItuPerceivedSeverity(TextualConvention, Integer32):
    reference = "ITU Recommendation M.3100, 'Generic Network Information Model', 1995 ITU Recommendation X.733, 'Information Technology - Open Systems Interconnection - System Management: Alarm Reporting Function', 1992"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6))

class ItuTrendIndication(TextualConvention, Integer32):
    reference = "ITU Recommendation M.3100, 'Generic Network Information Model', 1995 ITU Recommendation X.733, 'Information Technology - Open Systems Interconnection - System Management: Alarm Reporting Function', 1992"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("moreSevere", 1), ("noChange", 2), ("lessSevere", 3))

mibBuilder.exportSymbols("ITU-ALARM-TC-MIB", ituAlarmTc=ituAlarmTc, ItuTrendIndication=ItuTrendIndication, PYSNMP_MODULE_ID=ituAlarmTc, ItuPerceivedSeverity=ItuPerceivedSeverity)
