#
# PySNMP MIB module MPLS-TC-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-TC-EXT-STD-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:03:50 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, ModuleIdentity, TimeTicks, Gauge32, Counter64, Unsigned32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "ModuleIdentity", "TimeTicks", "Gauge32", "Counter64", "Unsigned32", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MPLS-TC-EXT-STD-MIB", MplsGlobalId=MplsGlobalId, MplsCcId=MplsCcId, PYSNMP_MODULE_ID=mplsTcExtStdMIB, MplsIccId=MplsIccId, mplsTcExtStdMIB=mplsTcExtStdMIB, MplsNodeId=MplsNodeId)
