#
# PySNMP MIB module SAF-INTEGRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-INTEGRA-MIB
# Produced by pysmi-1.1.8 at Thu Jan 27 21:18:48 2022
# On host fv-az74-168 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
pointToPoint, = mibBuilder.importSymbols("SAF-ENTERPRISE", "pointToPoint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, TimeTicks, iso, Counter32, NotificationType, MibIdentifier, Bits, Unsigned32, ModuleIdentity, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "iso", "Counter32", "NotificationType", "MibIdentifier", "Bits", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress")
TextualConvention, DateAndTime, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString", "PhysAddress")
safIntegra = ModuleIdentity((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7))
safIntegra.setRevisions(('2015-01-06 00:00', '2013-09-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: safIntegra.setRevisionsDescriptions(('Public Release 1.01.\n                IntegraB module separated', 'Public Release 1.0',))
if mibBuilder.loadTexts: safIntegra.setLastUpdated('201501060000Z')
if mibBuilder.loadTexts: safIntegra.setOrganization('SAF Tehnika')
if mibBuilder.loadTexts: safIntegra.setContactInfo('SAF Tehnika technical support\n                <techsupport>')
if mibBuilder.loadTexts: safIntegra.setDescription('SAF Integra management base')
mibBuilder.exportSymbols("SAF-INTEGRA-MIB", safIntegra=safIntegra, PYSNMP_MODULE_ID=safIntegra)
