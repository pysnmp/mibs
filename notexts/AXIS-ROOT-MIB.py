#
# PySNMP MIB module AXIS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/axis/AXIS-ROOT-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 12:07:54 2023
# On host fv-az1234-823 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, Gauge32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, ObjectIdentity, enterprises, TimeTicks, Unsigned32, Counter64, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Gauge32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "ObjectIdentity", "enterprises", "TimeTicks", "Unsigned32", "Counter64", "NotificationType", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
axis = ModuleIdentity((1, 3, 6, 1, 4, 1, 368))
axis.setRevisions(('2012-06-08 10:00',))
if mibBuilder.loadTexts: axis.setLastUpdated('201206081000Z')
if mibBuilder.loadTexts: axis.setOrganization('Axis Communications AB')
products = ObjectIdentity((1, 3, 6, 1, 4, 1, 368, 1))
if mibBuilder.loadTexts: products.setStatus('current')
mibBuilder.exportSymbols("AXIS-ROOT-MIB", products=products, PYSNMP_MODULE_ID=axis, axis=axis)
