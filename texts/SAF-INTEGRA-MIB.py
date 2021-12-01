#
# PySNMP MIB module SAF-INTEGRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-INTEGRA-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 16:55:06 2021
# On host fv-az83-424 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
pointToPoint, = mibBuilder.importSymbols("SAF-ENTERPRISE", "pointToPoint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, iso, ObjectIdentity, MibIdentifier, Counter64, Counter32, Unsigned32, TimeTicks, IpAddress, NotificationType, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "iso", "ObjectIdentity", "MibIdentifier", "Counter64", "Counter32", "Unsigned32", "TimeTicks", "IpAddress", "NotificationType", "Bits", "Integer32")
DisplayString, PhysAddress, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "DateAndTime", "TextualConvention")
safIntegra = ModuleIdentity((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 7))
safIntegra.setRevisions(('2015-01-06 00:00', '2013-09-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: safIntegra.setRevisionsDescriptions(('Public Release 1.01.\n                IntegraB module separated', 'Public Release 1.0',))
if mibBuilder.loadTexts: safIntegra.setLastUpdated('201501060000Z')
if mibBuilder.loadTexts: safIntegra.setOrganization('SAF Tehnika')
if mibBuilder.loadTexts: safIntegra.setContactInfo('SAF Tehnika technical support\n                <techsupport>')
if mibBuilder.loadTexts: safIntegra.setDescription('SAF Integra management base')
mibBuilder.exportSymbols("SAF-INTEGRA-MIB", PYSNMP_MODULE_ID=safIntegra, safIntegra=safIntegra)
