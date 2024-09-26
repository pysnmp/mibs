#
# PySNMP MIB module BCN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 26 02:10:54 2024
# On host fv-az1144-917 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
bcnProducts, bcnModules = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnProducts", "bcnModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, Gauge32, MibIdentifier, iso, TimeTicks, Counter32, Integer32, ModuleIdentity, Counter64, Unsigned32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Gauge32", "MibIdentifier", "iso", "TimeTicks", "Counter32", "Integer32", "ModuleIdentity", "Counter64", "Unsigned32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("BCN-PRODUCTS-MIB", bcnProductsAdonis250=bcnProductsAdonis250, bcnProductsAdonis=bcnProductsAdonis, PYSNMP_MODULE_ID=bcnProductsMIB, bcnProductsAdonis750=bcnProductsAdonis750, bcnProductsAdonis1000=bcnProductsAdonis1000, bcnProductsPoteus2150=bcnProductsPoteus2150, bcnProductsProteus=bcnProductsProteus, bcnProductsMIB=bcnProductsMIB)
