#
# PySNMP MIB module AXIS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source AXIS-ROOT-MIB
# Source digest sha256:37c5590d45ffee80f9ebca5a58b709862a52136fa18ef5de838aee08b53ae438
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
axis = ModuleIdentity((1, 3, 6, 1, 4, 1, 368))
axis.setRevisions(('2012-06-08 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: axis.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: axis.setLastUpdated('2012-06-08 10:00')
if mibBuilder.loadTexts: axis.setOrganization('Axis Communications AB')
if mibBuilder.loadTexts: axis.setContactInfo('Postal: Axis Communications AB\n                  Emdalavagen 14\n                  SE-223 69 Lund\n                  Sweden\n                  Phone: +46 (0)46 272 18 00\n                  Fax:   +46 (0)46 13 61 30\n                  E-Mail: info@axis.com\n                  Web: www.axis.com')
if mibBuilder.loadTexts: axis.setDescription('The AXIS root MIB.')
products = ObjectIdentity((1, 3, 6, 1, 4, 1, 368, 1))
if mibBuilder.loadTexts: products.setStatus('current')
if mibBuilder.loadTexts: products.setDescription('products is the root OBJECT IDENTIFIER from which\n         sysObjectID values are assigned. Actual values and\n         respectively products sub-tree are defined in:\n         AXIS-PRINTSERVER-MIB\n         AXIS-VIDEO-MIB')
mibBuilder.exportSymbols("AXIS-ROOT-MIB", PYSNMP_MODULE_ID=axis, axis=axis, products=products)
