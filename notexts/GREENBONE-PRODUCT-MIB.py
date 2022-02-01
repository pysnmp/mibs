#
# PySNMP MIB module GREENBONE-PRODUCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/greenbone/GREENBONE-PRODUCT-MIB
# Produced by pysmi-1.1.8 at Tue Feb  1 21:03:46 2022
# On host fv-az121-510 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, enterprises, NotificationType, TimeTicks, Counter64, iso, Integer32, ModuleIdentity, Unsigned32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "enterprises", "NotificationType", "TimeTicks", "Counter64", "iso", "Integer32", "ModuleIdentity", "Unsigned32", "Bits", "MibIdentifier")
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
mibBuilder.exportSymbols("GREENBONE-PRODUCT-MIB", productGroups=productGroups, productHardware=productHardware, PYSNMP_MODULE_ID=greenboneProduct, hwName=hwName, swVersionPatch=swVersionPatch, swName=swName, productName=productName, swVersionString=swVersionString, swVersionMajor=swVersionMajor, swVersionRevision=swVersionRevision, greenboneProduct=greenboneProduct, greenboneProductGroup=greenboneProductGroup, greenboneProductHWGroup=greenboneProductHWGroup, greenboneProductSWGroup=greenboneProductSWGroup, swVersionMinor=swVersionMinor, swVersion=swVersion, productSoftware=productSoftware)
