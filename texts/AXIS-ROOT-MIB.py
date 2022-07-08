#
# PySNMP MIB module AXIS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/axis/AXIS-ROOT-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:17:49 2022
# On host fv-az206-808 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, NotificationType, MibIdentifier, enterprises, Integer32, Counter64, iso, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "NotificationType", "MibIdentifier", "enterprises", "Integer32", "Counter64", "iso", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "TimeTicks", "Bits")
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
mibBuilder.exportSymbols("AXIS-ROOT-MIB", products=products, axis=axis, PYSNMP_MODULE_ID=axis)
