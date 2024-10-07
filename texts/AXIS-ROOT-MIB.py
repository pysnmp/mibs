#
# PySNMP MIB module AXIS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/axis/AXIS-ROOT-MIB
# Produced by pysmi-1.1.12 at Mon Oct  7 02:50:30 2024
# On host fv-az775-99 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, enterprises, iso, ObjectIdentity, Counter64, TimeTicks, Bits, Integer32, Gauge32, NotificationType, Unsigned32, Counter32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "enterprises", "iso", "ObjectIdentity", "Counter64", "TimeTicks", "Bits", "Integer32", "Gauge32", "NotificationType", "Unsigned32", "Counter32", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("AXIS-ROOT-MIB", products=products, PYSNMP_MODULE_ID=axis, axis=axis)
