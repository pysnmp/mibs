#
# PySNMP MIB module SAF-ENTERPRISE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saf/SAF-ENTERPRISE
# Produced by pysmi-1.1.3 at Sat Nov 20 17:10:27 2021
# On host fv-az121-977 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Unsigned32, Gauge32, ObjectIdentity, Bits, Integer32, Counter64, iso, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Unsigned32", "Gauge32", "ObjectIdentity", "Bits", "Integer32", "Counter64", "iso", "Counter32", "MibIdentifier")
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
mibBuilder.exportSymbols("SAF-ENTERPRISE", pointToPoint=pointToPoint, microwaveRadio=microwaveRadio, PYSNMP_MODULE_ID=saf, microwave=microwave, saf=saf, tehnika=tehnika)
