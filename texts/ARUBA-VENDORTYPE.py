#
# PySNMP MIB module ARUBA-VENDORTYPE (http://snmplabs.com/pysmi)
# ASN.1 source ARUBA-VENDORTYPE
# Source digest sha256:c1e19f4df401588442cd69cb1fada91fca72395daa93f4f79f20f7110eb42ba2
# Produced by pysmi-2.3.0
#
arubaMIBModules, = mibBuilder.importSymbols("ARUBA-MIB", "arubaMIBModules")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaVendorTypeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1))
arubaVendorTypeMIB.setRevisions(('2012-08-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arubaVendorTypeMIB.setRevisionsDescriptions(('The initial revision of vendortype-oid MIB.',))
if mibBuilder.loadTexts: arubaVendorTypeMIB.setLastUpdated('2012-08-27 00:00')
if mibBuilder.loadTexts: arubaVendorTypeMIB.setOrganization('Aruba Wireless Networks')
if mibBuilder.loadTexts: arubaVendorTypeMIB.setContactInfo('Postal:    1322 Crossman Avenue\n                    Sunnyvale, CA 94089\n        E-mail:     dl-support@arubanetworks.com\n        Phone:      +1 408 227 4500')
if mibBuilder.loadTexts: arubaVendorTypeMIB.setDescription('This module describes the object identifiers that are assigned to\n        various components on aruba products.')
arubaVendorTypeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1))
arubaSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1))
aSystemUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 1))
aSystemChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 2))
aSystemBackplane = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 3))
aSystemModule = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 4))
aSystemPSU = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 5))
aSystemFAN = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 6))
aSystemContainer = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 7))
aSystemPort = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 8))
aSystemSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 9))
mibBuilder.exportSymbols("ARUBA-VENDORTYPE", PYSNMP_MODULE_ID=arubaVendorTypeMIB, aSystemBackplane=aSystemBackplane, aSystemChassis=aSystemChassis, aSystemContainer=aSystemContainer, aSystemFAN=aSystemFAN, aSystemModule=aSystemModule, aSystemPSU=aSystemPSU, aSystemPort=aSystemPort, aSystemSensor=aSystemSensor, aSystemUnknown=aSystemUnknown, arubaSystem=arubaSystem, arubaVendorTypeMIB=arubaVendorTypeMIB, arubaVendorTypeMIBObjects=arubaVendorTypeMIBObjects)
