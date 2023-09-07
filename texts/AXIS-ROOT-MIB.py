#
# PySNMP MIB module AXIS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/axis/AXIS-ROOT-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:20:09 2023
# On host fv-az448-504 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, Bits, iso, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, enterprises, TimeTicks, ObjectIdentity, Gauge32, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Bits", "iso", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "enterprises", "TimeTicks", "ObjectIdentity", "Gauge32", "Unsigned32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
axis = ModuleIdentity((1, 3, 6, 1, 4, 1, 368))
axis.setRevisions(('2012-06-08 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: axis.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: axis.setLastUpdated('201206081000Z')
if mibBuilder.loadTexts: axis.setOrganization('Axis Communications AB')
if mibBuilder.loadTexts: axis.setContactInfo('Postal: Axis Communications AB\n                  Emdalavagen 14\n                  SE-223 69 Lund\n                  Sweden\n                  Phone: +46 (0)46 272 18 00\n                  Fax:   +46 (0)46 13 61 30\n                  E-Mail: info@axis.com\n                  Web: www.axis.com')
if mibBuilder.loadTexts: axis.setDescription('The AXIS root MIB.')
products = ObjectIdentity((1, 3, 6, 1, 4, 1, 368, 1))
if mibBuilder.loadTexts: products.setStatus('current')
if mibBuilder.loadTexts: products.setDescription('products is the root OBJECT IDENTIFIER from which\n         sysObjectID values are assigned. Actual values and\n         respectively products sub-tree are defined in:\n         AXIS-PRINTSERVER-MIB\n         AXIS-VIDEO-MIB')
mibBuilder.exportSymbols("AXIS-ROOT-MIB", axis=axis, PYSNMP_MODULE_ID=axis, products=products)
