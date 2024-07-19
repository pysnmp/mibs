#
# PySNMP MIB module SAF-INTEGRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-INTEGRA-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 10:07:00 2024
# On host fv-az1251-884 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
pointToPoint, = mibBuilder.importSymbols("SAF-ENTERPRISE", "pointToPoint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Unsigned32, Counter64, Counter32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, TimeTicks, Bits, IpAddress, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Counter64", "Counter32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "TimeTicks", "Bits", "IpAddress", "Integer32", "Gauge32")
DisplayString, DateAndTime, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention", "PhysAddress")
safIntegra = ModuleIdentity((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7))
safIntegra.setRevisions(('2015-01-06 00:00', '2013-09-19 00:00',))
if mibBuilder.loadTexts: safIntegra.setLastUpdated('201501060000Z')
if mibBuilder.loadTexts: safIntegra.setOrganization('SAF Tehnika')
mibBuilder.exportSymbols("SAF-INTEGRA-MIB", PYSNMP_MODULE_ID=safIntegra, safIntegra=safIntegra)
