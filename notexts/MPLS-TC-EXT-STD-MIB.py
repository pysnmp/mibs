#
# PySNMP MIB module MPLS-TC-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-TC-EXT-STD-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:50:53 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Gauge32, ObjectIdentity, iso, Integer32, Unsigned32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Gauge32", "ObjectIdentity", "iso", "Integer32", "Unsigned32", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mplsTcExtStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 17))
mplsTcExtStdMIB.setRevisions(('2015-02-02 00:00',))
if mibBuilder.loadTexts: mplsTcExtStdMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: mplsTcExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
class MplsGlobalId(TextualConvention, OctetString):
    reference = 'MPLS Transport Profile (MPLS-TP) Identifiers, RFC 6370, Section 3'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MplsCcId(TextualConvention, OctetString):
    reference = 'MPLS-TP Identifiers Following ITU-T Conventions, RFC 6923, Section 3. International Reference Alphabet (IRA) (Formerly International Alphabet No. 5 or IA5) - Information technology - 7-bit coded character set for information exchange, ITU-T Recommendation T.50, September 1992.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class MplsIccId(TextualConvention, OctetString):
    reference = 'MPLS-TP Identifiers Following ITU-T Conventions, RFC 6923, Section 3. International Reference Alphabet (IRA) (Formerly International Alphabet No. 5 or IA5) - Information technology - 7-bit coded character set for information exchange, ITU-T Recommendation T.50, September 1992.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 6), )
class MplsNodeId(TextualConvention, Unsigned32):
    reference = 'MPLS Transport Profile (MPLS-TP) Identifiers, RFC 6370, Section 4'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
mibBuilder.exportSymbols("MPLS-TC-EXT-STD-MIB", MplsGlobalId=MplsGlobalId, MplsNodeId=MplsNodeId, MplsCcId=MplsCcId, MplsIccId=MplsIccId, mplsTcExtStdMIB=mplsTcExtStdMIB, PYSNMP_MODULE_ID=mplsTcExtStdMIB)
