#
# PySNMP MIB module GARDEROS-PRODUCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/garderos/GARDEROS-PRODUCT-MIB
# Produced by pysmi-1.1.8 at Thu Sep 15 09:41:05 2022
# On host fv-az196-500 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
garderos, = mibBuilder.importSymbols("GARDEROS-SMI-MIB", "garderos")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, ObjectIdentity, Bits, Counter64, iso, TimeTicks, Unsigned32, NotificationType, MibIdentifier, Counter32, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "ObjectIdentity", "Bits", "Counter64", "iso", "TimeTicks", "Unsigned32", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("GARDEROS-PRODUCT-MIB", productCompliances=productCompliances, productInformationGroup=productInformationGroup, productInterfaces=productInterfaces, productMIB=productMIB, productGeneral=productGeneral, productSubType=productSubType, productCasing=productCasing, productMainboard=productMainboard, productGroups=productGroups, productType=productType, productModuleCompliance=productModuleCompliance, productCasingType=productCasingType, productConformance=productConformance, product=product, PYSNMP_MODULE_ID=product)
