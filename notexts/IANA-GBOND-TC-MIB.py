#
# PySNMP MIB module IANA-GBOND-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source IANA-GBOND-TC-MIB
# Source digest sha256:22dd0afde0bb64a33c6eae2f94c950e1787a539cef7f5ebc87de80bc15d6e4b8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaGBondTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 215))
ianaGBondTcMIB.setRevisions(('2013-02-20 00:00',))
if mibBuilder.loadTexts: ianaGBondTcMIB.setLastUpdated('2017-06-23 00:00')
if mibBuilder.loadTexts: ianaGBondTcMIB.setOrganization('IANA')
class IANAgBondSchemeList(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("none", 0), ("g9981", 1), ("g9982", 2), ("g9983", 3))

class IANAgBondScheme(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("g9981", 1), ("g9982", 2), ("g9983", 3))

mibBuilder.exportSymbols("IANA-GBOND-TC-MIB", IANAgBondScheme=IANAgBondScheme, IANAgBondSchemeList=IANAgBondSchemeList, PYSNMP_MODULE_ID=ianaGBondTcMIB, ianaGBondTcMIB=ianaGBondTcMIB)
