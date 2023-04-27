#
# PySNMP MIB module BTI8xx-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 12:06:40 2023
# On host fv-az741-387 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, Unsigned32, IpAddress, MibIdentifier, Integer32, NotificationType, Counter64, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, enterprises, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "NotificationType", "Counter64", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "enterprises", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bti8xx = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7))
bti8xx.setRevisions(('2013-12-26 12:00',))
if mibBuilder.loadTexts: bti8xx.setLastUpdated('201312261200Z')
if mibBuilder.loadTexts: bti8xx.setOrganization('Actus Networks Inc.')
btiSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 30005))
btiProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1))
mibBuilder.exportSymbols("BTI8xx-MIB", btiProducts=btiProducts, bti8xx=bti8xx, PYSNMP_MODULE_ID=bti8xx, btiSystems=btiSystems)
