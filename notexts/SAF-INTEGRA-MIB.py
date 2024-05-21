#
# PySNMP MIB module SAF-INTEGRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-INTEGRA-MIB
# Produced by pysmi-1.1.12 at Tue May 21 07:00:51 2024
# On host fv-az1501-253 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
pointToPoint, = mibBuilder.importSymbols("SAF-ENTERPRISE", "pointToPoint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, TimeTicks, Integer32, NotificationType, Gauge32, Counter32, IpAddress, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "TimeTicks", "Integer32", "NotificationType", "Gauge32", "Counter32", "IpAddress", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "iso")
PhysAddress, DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "DateAndTime", "TextualConvention")
safIntegra = ModuleIdentity((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7))
safIntegra.setRevisions(('2015-01-06 00:00', '2013-09-19 00:00',))
if mibBuilder.loadTexts: safIntegra.setLastUpdated('201501060000Z')
if mibBuilder.loadTexts: safIntegra.setOrganization('SAF Tehnika')
mibBuilder.exportSymbols("SAF-INTEGRA-MIB", safIntegra=safIntegra, PYSNMP_MODULE_ID=safIntegra)
