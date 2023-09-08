#
# PySNMP MIB module GARDEROS-PRODUCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-PRODUCT-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 07:34:06 2023
# On host fv-az362-181 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
garderos, = mibBuilder.importSymbols("GARDEROS-SMI-MIB", "garderos")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, TimeTicks, NotificationType, Unsigned32, MibIdentifier, Counter32, Gauge32, ObjectIdentity, IpAddress, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "TimeTicks", "NotificationType", "Unsigned32", "MibIdentifier", "Counter32", "Gauge32", "ObjectIdentity", "IpAddress", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
product = ModuleIdentity((1, 3, 6, 1, 4, 1, 16108, 1))
product.setRevisions(('2017-03-06 13:59',))
if mibBuilder.loadTexts: product.setLastUpdated('201703061359Z')
if mibBuilder.loadTexts: product.setOrganization('Garderos GmbH')
productMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1))
if mibBuilder.loadTexts: productMIB.setStatus('current')
productConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2))
if mibBuilder.loadTexts: productConformance.setStatus('current')
productGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 1))
if mibBuilder.loadTexts: productGroups.setStatus('current')
productCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 2))
if mibBuilder.loadTexts: productCompliances.setStatus('current')
productModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 2, 1)).setObjects(("GARDEROS-PRODUCT-MIB", "productInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    productModuleCompliance = productModuleCompliance.setStatus('current')
productInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 16108, 1, 1, 2, 1, 2)).setObjects(("GARDEROS-PRODUCT-MIB", "productType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    productInformationGroup = productInformationGroup.setStatus('current')
productCasingType = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17))
if mibBuilder.loadTexts: productCasingType.setStatus('current')
productCasing = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33))
if mibBuilder.loadTexts: productCasing.setStatus('current')
productMainboard = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31))
if mibBuilder.loadTexts: productMainboard.setStatus('current')
productInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36))
if mibBuilder.loadTexts: productInterfaces.setStatus('current')
productSubType = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36, 255))
if mibBuilder.loadTexts: productSubType.setStatus('current')
productGeneral = ObjectIdentity((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36, 255, 1))
if mibBuilder.loadTexts: productGeneral.setStatus('current')
productType = MibScalar((1, 3, 6, 1, 4, 1, 16108, 1, 17, 33, 31, 36, 255, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productType.setStatus('current')
mibBuilder.exportSymbols("GARDEROS-PRODUCT-MIB", productGeneral=productGeneral, productCompliances=productCompliances, product=product, productCasingType=productCasingType, productSubType=productSubType, productCasing=productCasing, productConformance=productConformance, productModuleCompliance=productModuleCompliance, productInformationGroup=productInformationGroup, productMainboard=productMainboard, PYSNMP_MODULE_ID=product, productType=productType, productGroups=productGroups, productMIB=productMIB, productInterfaces=productInterfaces)
