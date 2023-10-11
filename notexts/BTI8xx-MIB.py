#
# PySNMP MIB module BTI8xx-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-MIB
# Produced by pysmi-1.1.8 at Wed Oct 11 11:21:08 2023
# On host fv-az456-991 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, Gauge32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Bits, Counter64, TimeTicks, ModuleIdentity, IpAddress, MibIdentifier, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "Gauge32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Bits", "Counter64", "TimeTicks", "ModuleIdentity", "IpAddress", "MibIdentifier", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bti8xx = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7))
bti8xx.setRevisions(('2013-12-26 12:00',))
if mibBuilder.loadTexts: bti8xx.setLastUpdated('201312261200Z')
if mibBuilder.loadTexts: bti8xx.setOrganization('Actus Networks Inc.')
btiSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 30005))
btiProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1))
mibBuilder.exportSymbols("BTI8xx-MIB", bti8xx=bti8xx, PYSNMP_MODULE_ID=bti8xx, btiSystems=btiSystems, btiProducts=btiProducts)
