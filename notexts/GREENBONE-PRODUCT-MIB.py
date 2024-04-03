#
# PySNMP MIB module GREENBONE-PRODUCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/greenbone/GREENBONE-PRODUCT-MIB
# Produced by pysmi-1.1.11 at Wed Apr  3 13:59:18 2024
# On host fv-az1200-481 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, Integer32, TimeTicks, Unsigned32, Counter64, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, IpAddress, enterprises, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Integer32", "TimeTicks", "Unsigned32", "Counter64", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "IpAddress", "enterprises", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
greenboneProduct = ModuleIdentity((1, 3, 6, 1, 4, 1, 35847, 1))
greenboneProduct.setRevisions(('2017-05-15 00:01', '2015-01-06 00:01', '2014-12-31 00:01', '2012-03-26 00:01',))
if mibBuilder.loadTexts: greenboneProduct.setLastUpdated('201705150001Z')
if mibBuilder.loadTexts: greenboneProduct.setOrganization('Greenbone Networks GmbH')
productName = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productName.setStatus('current')
productHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 35847, 1, 2))
productSoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 35847, 1, 3))
productGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 35847, 1, 4))
hwName = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwName.setStatus('current')
swName = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swName.setStatus('current')
swVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2))
swVersionString = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionString.setStatus('current')
swVersionMajor = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionMajor.setStatus('current')
swVersionMinor = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionMinor.setStatus('current')
swVersionPatch = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionPatch.setStatus('current')
swVersionRevision = MibScalar((1, 3, 6, 1, 4, 1, 35847, 1, 3, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionRevision.setStatus('current')
greenboneProductGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35847, 1, 4, 1)).setObjects(("GREENBONE-PRODUCT-MIB", "productName"), ("GREENBONE-PRODUCT-MIB", "hwName"), ("GREENBONE-PRODUCT-MIB", "swName"), ("GREENBONE-PRODUCT-MIB", "swVersionString"), ("GREENBONE-PRODUCT-MIB", "swVersionMajor"), ("GREENBONE-PRODUCT-MIB", "swVersionMinor"), ("GREENBONE-PRODUCT-MIB", "swVersionPatch"), ("GREENBONE-PRODUCT-MIB", "swVersionRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    greenboneProductGroup = greenboneProductGroup.setStatus('current')
greenboneProductHWGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35847, 1, 4, 2)).setObjects(("GREENBONE-PRODUCT-MIB", "hwName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    greenboneProductHWGroup = greenboneProductHWGroup.setStatus('current')
greenboneProductSWGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 35847, 1, 4, 3)).setObjects(("GREENBONE-PRODUCT-MIB", "swName"), ("GREENBONE-PRODUCT-MIB", "swVersionString"), ("GREENBONE-PRODUCT-MIB", "swVersionMajor"), ("GREENBONE-PRODUCT-MIB", "swVersionMinor"), ("GREENBONE-PRODUCT-MIB", "swVersionPatch"), ("GREENBONE-PRODUCT-MIB", "swVersionRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    greenboneProductSWGroup = greenboneProductSWGroup.setStatus('current')
mibBuilder.exportSymbols("GREENBONE-PRODUCT-MIB", productHardware=productHardware, swVersionMajor=swVersionMajor, productName=productName, swVersionString=swVersionString, swVersionPatch=swVersionPatch, hwName=hwName, greenboneProductGroup=greenboneProductGroup, productSoftware=productSoftware, greenboneProductHWGroup=greenboneProductHWGroup, swVersionMinor=swVersionMinor, greenboneProductSWGroup=greenboneProductSWGroup, greenboneProduct=greenboneProduct, swVersion=swVersion, swVersionRevision=swVersionRevision, swName=swName, PYSNMP_MODULE_ID=greenboneProduct, productGroups=productGroups)
