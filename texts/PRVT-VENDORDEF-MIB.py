#
# PySNMP MIB module PRVT-VENDORDEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-VENDORDEF-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 18:06:37 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, IpAddress, Gauge32, Bits, Counter64, enterprises, MibIdentifier, ObjectIdentity, NotificationType, Unsigned32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "IpAddress", "Gauge32", "Bits", "Counter64", "enterprises", "MibIdentifier", "ObjectIdentity", "NotificationType", "Unsigned32", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PRVT-VENDORDEF-MIB", prvt_products=prvt_products, prvtVendorDefMIB=prvtVendorDefMIB, PYSNMP_MODULE_ID=prvtVendorDefMIB)
