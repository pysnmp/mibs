#
# PySNMP MIB module LANGTAG-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/RFC5131-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:04:42 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, IpAddress, Bits, ObjectIdentity, Integer32, mib_2, ModuleIdentity, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "IpAddress", "Bits", "ObjectIdentity", "Integer32", "mib-2", "ModuleIdentity", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
langTagTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 165))
langTagTcMIB.setRevisions(('2007-11-09 00:00',))
if mibBuilder.loadTexts: langTagTcMIB.setLastUpdated('200711090000Z')
if mibBuilder.loadTexts: langTagTcMIB.setOrganization('IETF Operations and Management (OPS) Area')
class LangTag(TextualConvention, OctetString):
    reference = 'RFC 4646 BCP 47'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 63), )
mibBuilder.exportSymbols("LANGTAG-TC-MIB", langTagTcMIB=langTagTcMIB, LangTag=LangTag, PYSNMP_MODULE_ID=langTagTcMIB)
