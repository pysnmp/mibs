#
# PySNMP MIB module BCN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-PRODUCTS-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:20:22 2023
# On host fv-az448-504 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
bcnModules, bcnProducts = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnModules", "bcnProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Gauge32, Unsigned32, Counter64, MibIdentifier, IpAddress, iso, TimeTicks, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Gauge32", "Unsigned32", "Counter64", "MibIdentifier", "IpAddress", "iso", "TimeTicks", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcnProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 4, 2))
bcnProductsMIB.setRevisions(('2010-11-30 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcnProductsMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bcnProductsMIB.setLastUpdated('201011301200Z')
if mibBuilder.loadTexts: bcnProductsMIB.setOrganization('BlueCat Networks')
if mibBuilder.loadTexts: bcnProductsMIB.setContactInfo('BlueCat Networks. Customer Care.\n\n        North America\n        Call: +1.866.491.2228\n        Europe\n        Call: +44.8081.011.306\n        Other\n        Call: +1.416.646.8433\n        \n        Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bcnProductsMIB.setDescription('This module defines the object identifiers that are assigned to\n        hardware platforms or software systems.\n        This objects are returned as sysObjectID.')
bcnProductsAdonis = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 1))
bcnProductsProteus = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 2))
bcnProductsAdonis250 = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 3))
bcnProductsAdonis750 = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 4))
bcnProductsAdonis1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 5))
bcnProductsPoteus2150 = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 2, 6))
mibBuilder.exportSymbols("BCN-PRODUCTS-MIB", bcnProductsPoteus2150=bcnProductsPoteus2150, bcnProductsAdonis250=bcnProductsAdonis250, bcnProductsProteus=bcnProductsProteus, bcnProductsAdonis=bcnProductsAdonis, bcnProductsAdonis750=bcnProductsAdonis750, PYSNMP_MODULE_ID=bcnProductsMIB, bcnProductsMIB=bcnProductsMIB, bcnProductsAdonis1000=bcnProductsAdonis1000)
