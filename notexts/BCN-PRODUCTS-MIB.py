#
# PySNMP MIB module BCN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-PRODUCTS-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:35:04 2021
# On host fv-az83-627 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
bcnProducts, bcnModules = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnProducts", "bcnModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, Counter32, IpAddress, ObjectIdentity, iso, Unsigned32, Integer32, MibIdentifier, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter32", "IpAddress", "ObjectIdentity", "iso", "Unsigned32", "Integer32", "MibIdentifier", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("BCN-PRODUCTS-MIB", bcnProductsProteus=bcnProductsProteus, bcnProductsPoteus2150=bcnProductsPoteus2150, bcnProductsMIB=bcnProductsMIB, bcnProductsAdonis250=bcnProductsAdonis250, bcnProductsAdonis1000=bcnProductsAdonis1000, PYSNMP_MODULE_ID=bcnProductsMIB, bcnProductsAdonis=bcnProductsAdonis, bcnProductsAdonis750=bcnProductsAdonis750)
