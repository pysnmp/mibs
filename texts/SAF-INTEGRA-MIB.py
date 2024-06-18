#
# PySNMP MIB module SAF-INTEGRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-INTEGRA-MIB
# Produced by pysmi-1.1.12 at Tue Jun 18 01:43:44 2024
# On host fv-az1446-447 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
pointToPoint, = mibBuilder.importSymbols("SAF-ENTERPRISE", "pointToPoint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, Gauge32, Unsigned32, ObjectIdentity, MibIdentifier, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, TimeTicks, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "Gauge32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "TimeTicks", "IpAddress", "ModuleIdentity")
DisplayString, DateAndTime, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention", "PhysAddress")
safIntegra = ModuleIdentity((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7))
safIntegra.setRevisions(('2015-01-06 00:00', '2013-09-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: safIntegra.setRevisionsDescriptions(('Public Release 1.01.\n                IntegraB module separated', 'Public Release 1.0',))
if mibBuilder.loadTexts: safIntegra.setLastUpdated('201501060000Z')
if mibBuilder.loadTexts: safIntegra.setOrganization('SAF Tehnika')
if mibBuilder.loadTexts: safIntegra.setContactInfo('SAF Tehnika technical support\n                <techsupport>')
if mibBuilder.loadTexts: safIntegra.setDescription('SAF Integra management base')
mibBuilder.exportSymbols("SAF-INTEGRA-MIB", safIntegra=safIntegra, PYSNMP_MODULE_ID=safIntegra)
