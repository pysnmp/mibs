#
# PySNMP MIB module SAF-INTEGRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-INTEGRA-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:07:38 2024
# On host fv-az888-540 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
pointToPoint, = mibBuilder.importSymbols("SAF-ENTERPRISE", "pointToPoint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, ModuleIdentity, NotificationType, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, TimeTicks, Counter64, iso, Counter32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "TimeTicks", "Counter64", "iso", "Counter32", "Gauge32", "ObjectIdentity")
DateAndTime, PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "PhysAddress", "TextualConvention", "DisplayString")
safIntegra = ModuleIdentity((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7))
safIntegra.setRevisions(('2015-01-06 00:00', '2013-09-19 00:00',))
if mibBuilder.loadTexts: safIntegra.setLastUpdated('201501060000Z')
if mibBuilder.loadTexts: safIntegra.setOrganization('SAF Tehnika')
mibBuilder.exportSymbols("SAF-INTEGRA-MIB", PYSNMP_MODULE_ID=safIntegra, safIntegra=safIntegra)
