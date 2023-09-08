#
# PySNMP MIB module AXIS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/axis/AXIS-ROOT-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 07:29:45 2023
# On host fv-az437-489 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier, Integer32, ModuleIdentity, NotificationType, Counter32, TimeTicks, enterprises, Counter64, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier", "Integer32", "ModuleIdentity", "NotificationType", "Counter32", "TimeTicks", "enterprises", "Counter64", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
axis = ModuleIdentity((1, 3, 6, 1, 4, 1, 368))
axis.setRevisions(('2012-06-08 10:00',))
if mibBuilder.loadTexts: axis.setLastUpdated('201206081000Z')
if mibBuilder.loadTexts: axis.setOrganization('Axis Communications AB')
products = ObjectIdentity((1, 3, 6, 1, 4, 1, 368, 1))
if mibBuilder.loadTexts: products.setStatus('current')
mibBuilder.exportSymbols("AXIS-ROOT-MIB", products=products, axis=axis, PYSNMP_MODULE_ID=axis)
