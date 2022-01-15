#
# PySNMP MIB module SAF-INTEGRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-INTEGRA-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:18:54 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
pointToPoint, = mibBuilder.importSymbols("SAF-ENTERPRISE", "pointToPoint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, Integer32, Counter32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, IpAddress, Counter64, ObjectIdentity, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Integer32", "Counter32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "IpAddress", "Counter64", "ObjectIdentity", "Gauge32", "ModuleIdentity")
DateAndTime, PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "PhysAddress", "DisplayString", "TextualConvention")
safIntegra = ModuleIdentity((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7))
safIntegra.setRevisions(('2015-01-06 00:00', '2013-09-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: safIntegra.setRevisionsDescriptions(('Public Release 1.01.\n                IntegraB module separated', 'Public Release 1.0',))
if mibBuilder.loadTexts: safIntegra.setLastUpdated('201501060000Z')
if mibBuilder.loadTexts: safIntegra.setOrganization('SAF Tehnika')
if mibBuilder.loadTexts: safIntegra.setContactInfo('SAF Tehnika technical support\n                <techsupport>')
if mibBuilder.loadTexts: safIntegra.setDescription('SAF Integra management base')
mibBuilder.exportSymbols("SAF-INTEGRA-MIB", PYSNMP_MODULE_ID=safIntegra, safIntegra=safIntegra)
