#
# PySNMP MIB module ITU-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/ITU-ALARM-TC-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 10:08:58 2023
# On host fv-az732-878 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, MibIdentifier, mib_2, IpAddress, Counter32, ModuleIdentity, TimeTicks, Bits, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "MibIdentifier", "mib-2", "IpAddress", "Counter32", "ModuleIdentity", "TimeTicks", "Bits", "Unsigned32", "NotificationType")
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

mibBuilder.exportSymbols("ITU-ALARM-TC-MIB", ituAlarmTc=ituAlarmTc, ItuPerceivedSeverity=ItuPerceivedSeverity, ItuTrendIndication=ItuTrendIndication, PYSNMP_MODULE_ID=ituAlarmTc)
