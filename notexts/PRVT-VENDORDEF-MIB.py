#
# PySNMP MIB module PRVT-VENDORDEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-VENDORDEF-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:57:20 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, Unsigned32, Integer32, TimeTicks, ModuleIdentity, Counter64, Counter32, IpAddress, enterprises, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Unsigned32", "Integer32", "TimeTicks", "ModuleIdentity", "Counter64", "Counter32", "IpAddress", "enterprises", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtVendorDefMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738))
prvtVendorDefMIB.setRevisions(('2007-09-29 00:00',))
if mibBuilder.loadTexts: prvtVendorDefMIB.setLastUpdated('200709290000Z')
if mibBuilder.loadTexts: prvtVendorDefMIB.setOrganization('BATM Advanced Communication')
prvt_products = ObjectIdentity((1, 3, 6, 1, 4, 1, 738, 10)).setLabel("prvt-products")
if mibBuilder.loadTexts: prvt_products.setStatus('current')
mibBuilder.exportSymbols("PRVT-VENDORDEF-MIB", prvt_products=prvt_products, prvtVendorDefMIB=prvtVendorDefMIB, PYSNMP_MODULE_ID=prvtVendorDefMIB)
