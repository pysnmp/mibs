#
# PySNMP MIB module ITU-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/ITU-ALARM-TC-MIB
# Produced by pysmi-1.1.8 at Thu Sep  8 09:47:35 2022
# On host fv-az173-382 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, TimeTicks, mib_2, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Gauge32, Counter32, ModuleIdentity, MibIdentifier, Counter64, Integer32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "mib-2", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Gauge32", "Counter32", "ModuleIdentity", "MibIdentifier", "Counter64", "Integer32", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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

mibBuilder.exportSymbols("ITU-ALARM-TC-MIB", ItuPerceivedSeverity=ItuPerceivedSeverity, PYSNMP_MODULE_ID=ituAlarmTc, ituAlarmTc=ituAlarmTc, ItuTrendIndication=ItuTrendIndication)
