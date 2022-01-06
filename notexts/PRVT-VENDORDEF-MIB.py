#
# PySNMP MIB module PRVT-VENDORDEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-VENDORDEF-MIB
# Produced by pysmi-1.1.8 at Thu Jan  6 20:31:47 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Unsigned32, ObjectIdentity, Counter32, Bits, iso, TimeTicks, Counter64, Gauge32, IpAddress, ModuleIdentity, NotificationType, Integer32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Counter32", "Bits", "iso", "TimeTicks", "Counter64", "Gauge32", "IpAddress", "ModuleIdentity", "NotificationType", "Integer32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtVendorDefMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738))
prvtVendorDefMIB.setRevisions(('2007-09-29 00:00',))
if mibBuilder.loadTexts: prvtVendorDefMIB.setLastUpdated('200709290000Z')
if mibBuilder.loadTexts: prvtVendorDefMIB.setOrganization('BATM Advanced Communication')
prvt_products = ObjectIdentity((1, 3, 6, 1, 4, 1, 738, 10)).setLabel("prvt-products")
if mibBuilder.loadTexts: prvt_products.setStatus('current')
mibBuilder.exportSymbols("PRVT-VENDORDEF-MIB", prvtVendorDefMIB=prvtVendorDefMIB, prvt_products=prvt_products, PYSNMP_MODULE_ID=prvtVendorDefMIB)
