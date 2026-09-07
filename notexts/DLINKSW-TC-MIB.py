#
# PySNMP MIB module DLINKSW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLINKSW-TC-MIB
# Source digest sha256:dbcd6bb235398f77ab11747716550e1280a4a647ecec56411847a61966a364e2
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkSwTextualConvention = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 1))
dlinkSwTextualConvention.setRevisions(('2012-11-19 00:00',))
if mibBuilder.loadTexts: dlinkSwTextualConvention.setLastUpdated('2012-11-19 00:00')
if mibBuilder.loadTexts: dlinkSwTextualConvention.setOrganization('D-Link Corp.')
class DlinkTrigger(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("action", 2))

class Dlink2kVlanList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

mibBuilder.exportSymbols("DLINKSW-TC-MIB", Dlink2kVlanList=Dlink2kVlanList, DlinkTrigger=DlinkTrigger, PYSNMP_MODULE_ID=dlinkSwTextualConvention, dlinkSwTextualConvention=dlinkSwTextualConvention)
