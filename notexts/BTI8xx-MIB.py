#
# PySNMP MIB module BTI8xx-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 19:00:14 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Integer32, Unsigned32, Counter64, ObjectIdentity, IpAddress, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, NotificationType, TimeTicks, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Integer32", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "NotificationType", "TimeTicks", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bti8xx = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7))
bti8xx.setRevisions(('2013-12-26 12:00',))
if mibBuilder.loadTexts: bti8xx.setLastUpdated('201312261200Z')
if mibBuilder.loadTexts: bti8xx.setOrganization('Actus Networks Inc.')
btiSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 30005))
btiProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1))
mibBuilder.exportSymbols("BTI8xx-MIB", btiSystems=btiSystems, bti8xx=bti8xx, btiProducts=btiProducts, PYSNMP_MODULE_ID=bti8xx)
