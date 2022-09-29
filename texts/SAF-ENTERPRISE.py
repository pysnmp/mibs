#
# PySNMP MIB module SAF-ENTERPRISE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-ENTERPRISE
# Produced by pysmi-1.1.8 at Thu Sep 29 13:14:52 2022
# On host fv-az340-469 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, Integer32, TimeTicks, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, Counter32, Bits, Gauge32, NotificationType, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "Integer32", "TimeTicks", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "Counter32", "Bits", "Gauge32", "NotificationType", "ModuleIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
saf = ModuleIdentity((1, 3, 6, 1, 4, 1, 7571))
saf.setRevisions(('2007-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: saf.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: saf.setLastUpdated('201511120000Z')
if mibBuilder.loadTexts: saf.setOrganization('SAF Tehnika')
if mibBuilder.loadTexts: saf.setContactInfo('SAF Tehnika technical support\n                <techsupport>')
if mibBuilder.loadTexts: saf.setDescription('microwave subtree added')
tehnika = ObjectIdentity((1, 3, 6, 1, 4, 1, 7571, 100))
if mibBuilder.loadTexts: tehnika.setStatus('current')
if mibBuilder.loadTexts: tehnika.setDescription('Subtree to register SAF tehnika modules')
microwaveRadio = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1))
microwave = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 2))
pointToPoint = MibIdentifier((1, 3, 6, 1, 4, 1, 7571, 100, 1, 1))
mibBuilder.exportSymbols("SAF-ENTERPRISE", tehnika=tehnika, saf=saf, pointToPoint=pointToPoint, PYSNMP_MODULE_ID=saf, microwave=microwave, microwaveRadio=microwaveRadio)
