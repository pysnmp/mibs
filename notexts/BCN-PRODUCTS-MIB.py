#
# PySNMP MIB module BCN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:20:11 2024
# On host fv-az1022-995 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
bcnModules, bcnProducts = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnModules", "bcnProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, IpAddress, NotificationType, MibIdentifier, Counter32, ModuleIdentity, Bits, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "IpAddress", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "Bits", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcnProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 4, 2))
bcnProductsMIB.setRevisions(('2010-11-30 12:00',))
if mibBuilder.loadTexts: bcnProductsMIB.setLastUpdated('201011301200Z')
if mibBuilder.loadTexts: bcnProductsMIB.setOrganization('BlueCat Networks')
bcnProductsAdonis = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 1))
bcnProductsProteus = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 2))
bcnProductsAdonis250 = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 3))
bcnProductsAdonis750 = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 4))
bcnProductsAdonis1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 5))
bcnProductsPoteus2150 = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 6))
mibBuilder.exportSymbols("BCN-PRODUCTS-MIB", bcnProductsAdonis=bcnProductsAdonis, bcnProductsAdonis250=bcnProductsAdonis250, bcnProductsAdonis1000=bcnProductsAdonis1000, bcnProductsPoteus2150=bcnProductsPoteus2150, bcnProductsAdonis750=bcnProductsAdonis750, PYSNMP_MODULE_ID=bcnProductsMIB, bcnProductsProteus=bcnProductsProteus, bcnProductsMIB=bcnProductsMIB)
