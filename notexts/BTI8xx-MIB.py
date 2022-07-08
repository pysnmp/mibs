#
# PySNMP MIB module BTI8xx-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:18:04 2022
# On host fv-az206-808 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, MibIdentifier, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Unsigned32, iso, TimeTicks, ModuleIdentity, Counter64, Gauge32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "MibIdentifier", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Unsigned32", "iso", "TimeTicks", "ModuleIdentity", "Counter64", "Gauge32", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bti8xx = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7))
bti8xx.setRevisions(('2013-12-26 12:00',))
if mibBuilder.loadTexts: bti8xx.setLastUpdated('201312261200Z')
if mibBuilder.loadTexts: bti8xx.setOrganization('Actus Networks Inc.')
btiSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 30005))
btiProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1))
mibBuilder.exportSymbols("BTI8xx-MIB", btiProducts=btiProducts, PYSNMP_MODULE_ID=bti8xx, bti8xx=bti8xx, btiSystems=btiSystems)
