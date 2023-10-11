#
# PySNMP MIB module GREENBONE-PRODUCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/greenbone/GREENBONE-PRODUCT-MIB
# Produced by pysmi-1.1.8 at Wed Oct 11 08:32:38 2023
# On host fv-az791-264 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, MibIdentifier, TimeTicks, Counter64, Integer32, Unsigned32, enterprises, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, Counter32, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "TimeTicks", "Counter64", "Integer32", "Unsigned32", "enterprises", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "Counter32", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("GREENBONE-PRODUCT-MIB", swVersionPatch=swVersionPatch, greenboneProduct=greenboneProduct, greenboneProductHWGroup=greenboneProductHWGroup, PYSNMP_MODULE_ID=greenboneProduct, swVersion=swVersion, greenboneProductSWGroup=greenboneProductSWGroup, swVersionMinor=swVersionMinor, greenboneProductGroup=greenboneProductGroup, swName=swName, productGroups=productGroups, productHardware=productHardware, productName=productName, hwName=hwName, swVersionString=swVersionString, swVersionRevision=swVersionRevision, swVersionMajor=swVersionMajor, productSoftware=productSoftware)
