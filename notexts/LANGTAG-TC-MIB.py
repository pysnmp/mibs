#
# PySNMP MIB module LANGTAG-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/RFC5131-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:26 2022
# On host fv-az77-149 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, ObjectIdentity, TimeTicks, Gauge32, Integer32, MibIdentifier, NotificationType, Unsigned32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "ObjectIdentity", "TimeTicks", "Gauge32", "Integer32", "MibIdentifier", "NotificationType", "Unsigned32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
langTagTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 165))
langTagTcMIB.setRevisions(('2007-11-09 00:00',))
if mibBuilder.loadTexts: langTagTcMIB.setLastUpdated('200711090000Z')
if mibBuilder.loadTexts: langTagTcMIB.setOrganization('IETF Operations and Management (OPS) Area')
class LangTag(TextualConvention, OctetString):
    reference = 'RFC 4646 BCP 47'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 63), )
mibBuilder.exportSymbols("LANGTAG-TC-MIB", PYSNMP_MODULE_ID=langTagTcMIB, langTagTcMIB=langTagTcMIB, LangTag=LangTag)
