#
# PySNMP MIB module CISCO-ENTITY-ASSET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-ASSET-CAPABILITY
# Source digest sha256:70282ebd79fca85c374d3f71e1a67d5c29ddc05bab6419292ad953fe1eb1f648
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityAssetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 300))
ciscoEntityAssetCapability.setRevisions(('2003-09-04 00:00', '2003-04-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityAssetCapability.setRevisionsDescriptions(('Added ceAssetCapV12R0214SXCat6K and\n             ceAssetCapCatOSV08R0101Cat6K.', 'Initial version of this MIB Module.',))
if mibBuilder.loadTexts: ciscoEntityAssetCapability.setLastUpdated('2003-09-04 00:00')
if mibBuilder.loadTexts: ciscoEntityAssetCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityAssetCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com\n                        cs-lan-switch-snmp@cisco.com\n                        cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityAssetCapability.setDescription('The capabilities description of\n             CISCO-ENTITY-ASSET-MIB.')
ceAssetCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 300, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapabilityV4R00 = ceAssetCapabilityV4R00.setProductRelease('MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapabilityV4R00 = ceAssetCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ceAssetCapabilityV4R00.setDescription('Entity Asset Agent capabilities for\n                          monitoring the asset information of items\n                          in the ENTITY-MIB (RFC 2737) entPhysical\n                          Table.')
ceAssetCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 300, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapV12R0214SXCat6K = ceAssetCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapV12R0214SXCat6K = ceAssetCapV12R0214SXCat6K.setStatus('current')
if mibBuilder.loadTexts: ceAssetCapV12R0214SXCat6K.setDescription('CISCO-ENTITY-ASSET-MIB capabilities.')
ceAssetCapCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 300, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapCatOSV08R0101Cat6K = ceAssetCapCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceAssetCapCatOSV08R0101Cat6K = ceAssetCapCatOSV08R0101Cat6K.setStatus('current')
if mibBuilder.loadTexts: ceAssetCapCatOSV08R0101Cat6K.setDescription('CISCO-ENTITY-ASSET-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-ASSET-CAPABILITY", PYSNMP_MODULE_ID=ciscoEntityAssetCapability, ceAssetCapCatOSV08R0101Cat6K=ceAssetCapCatOSV08R0101Cat6K, ceAssetCapV12R0214SXCat6K=ceAssetCapV12R0214SXCat6K, ceAssetCapabilityV4R00=ceAssetCapabilityV4R00, ciscoEntityAssetCapability=ciscoEntityAssetCapability)
