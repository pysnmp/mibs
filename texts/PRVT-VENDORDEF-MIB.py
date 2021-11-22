#
# PySNMP MIB module PRVT-VENDORDEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-VENDORDEF-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:35:14 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, ObjectIdentity, Bits, iso, Integer32, ModuleIdentity, enterprises, NotificationType, Unsigned32, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "ObjectIdentity", "Bits", "iso", "Integer32", "ModuleIdentity", "enterprises", "NotificationType", "Unsigned32", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtVendorDefMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738))
prvtVendorDefMIB.setRevisions(('2007-09-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtVendorDefMIB.setRevisionsDescriptions(('Initial.',))
if mibBuilder.loadTexts: prvtVendorDefMIB.setLastUpdated('200709290000Z')
if mibBuilder.loadTexts: prvtVendorDefMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtVendorDefMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtVendorDefMIB.setDescription('Vendor Id Definition')
prvt_products = ObjectIdentity((1, 3, 6, 1, 4, 1, 738, 10)).setLabel("prvt-products")
if mibBuilder.loadTexts: prvt_products.setStatus('current')
if mibBuilder.loadTexts: prvt_products.setDescription('prvt-product')
mibBuilder.exportSymbols("PRVT-VENDORDEF-MIB", prvtVendorDefMIB=prvtVendorDefMIB, prvt_products=prvt_products, PYSNMP_MODULE_ID=prvtVendorDefMIB)
