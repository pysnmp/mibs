#
# PySNMP MIB module BCN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-PRODUCTS-MIB
# Produced by pysmi-1.1.8 at Thu Sep 29 13:03:06 2022
# On host fv-az340-469 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
bcnModules, bcnProducts = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnModules", "bcnProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, Counter32, TimeTicks, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter64, Bits, ObjectIdentity, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Counter32", "TimeTicks", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter64", "Bits", "ObjectIdentity", "IpAddress", "iso")
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
mibBuilder.exportSymbols("BCN-PRODUCTS-MIB", PYSNMP_MODULE_ID=bcnProductsMIB, bcnProductsAdonis750=bcnProductsAdonis750, bcnProductsPoteus2150=bcnProductsPoteus2150, bcnProductsAdonis=bcnProductsAdonis, bcnProductsAdonis250=bcnProductsAdonis250, bcnProductsMIB=bcnProductsMIB, bcnProductsProteus=bcnProductsProteus, bcnProductsAdonis1000=bcnProductsAdonis1000)
