#
# PySNMP MIB module GREENBONE-PRODUCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/greenbone/GREENBONE-PRODUCT-MIB
# Produced by pysmi-1.1.8 at Thu Sep  8 09:19:06 2022
# On host fv-az447-161 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Unsigned32, NotificationType, IpAddress, iso, ObjectIdentity, ModuleIdentity, Gauge32, MibIdentifier, enterprises, TimeTicks, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "NotificationType", "IpAddress", "iso", "ObjectIdentity", "ModuleIdentity", "Gauge32", "MibIdentifier", "enterprises", "TimeTicks", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
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
mibBuilder.exportSymbols("GREENBONE-PRODUCT-MIB", greenboneProduct=greenboneProduct, swVersionMinor=swVersionMinor, swVersionRevision=swVersionRevision, productGroups=productGroups, greenboneProductSWGroup=greenboneProductSWGroup, productHardware=productHardware, hwName=hwName, productName=productName, productSoftware=productSoftware, swName=swName, swVersionPatch=swVersionPatch, greenboneProductHWGroup=greenboneProductHWGroup, swVersionMajor=swVersionMajor, swVersion=swVersion, swVersionString=swVersionString, PYSNMP_MODULE_ID=greenboneProduct, greenboneProductGroup=greenboneProductGroup)
