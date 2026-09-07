#
# PySNMP MIB module CISCO-CONTENT-SERVICES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CONTENT-SERVICES-CAPABILITY
# Source digest sha256:f1890e1f45aaa0ac40c063439b6fb3d2d6db155ab848166dc1351a283d2beb17
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoContentServicesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 581))
ciscoContentServicesCapability.setRevisions(('2010-12-23 00:00', '2010-02-11 00:00', '2009-08-21 00:00', '2009-05-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoContentServicesCapability.setRevisionsDescriptions(('Added following object groups:\n        ciscoContentServicesLoadStatRadiusGroupSup1\n        ciscoContentServicesLoadStatUserDBGroupSup1\n        ciscoContentServicesLoadStatSessionGroupSup1\n        ciscoContentServicesLoadStatBMAGroupSup1\n        ciscoContentServicesLoadStatQuotaMgrGroupSup1\n        ciscoContentServicesLoadStatGxEventGroupSup1', 'Added following object group:\n        ciscoContentServicesBillingPlanStatsGroup', 'Added following object groups:\n        ciscoContentServiceProtocolStatsGroup\n        ciscoContentServicesLoadStatGxEventGroup', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoContentServicesCapability.setLastUpdated('2010-12-23 00:00')
if mibBuilder.loadTexts: ciscoContentServicesCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoContentServicesCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-csg@cisco.com')
if mibBuilder.loadTexts: ciscoContentServicesCapability.setDescription('Agent capabilities for CISCO-CONTENT-SERVICES-MIB')
ciscoContentServicesCapabilityAdcV01R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityAdcV01R00 = ciscoContentServicesCapabilityAdcV01R00.setProductRelease('Cisco IOS 12.4MF')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityAdcV01R00 = ciscoContentServicesCapabilityAdcV01R00.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityAdcV01R00.setDescription('Cisco Content Services MIB for AdControl capabilities')
ciscoContentServicesCapabilityCSG2R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R03 = ciscoContentServicesCapabilityCSG2R03.setProductRelease('Cisco IOS 12.4(22)MD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R03 = ciscoContentServicesCapabilityCSG2R03.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R03.setDescription('Cisco Content Services MIB for CSG2 R3 capabilities')
ciscoContentServicesCapabilityCSG2R0305 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R0305 = ciscoContentServicesCapabilityCSG2R0305.setProductRelease('Cisco IOS 12.4(22)MDA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R0305 = ciscoContentServicesCapabilityCSG2R0305.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R0305.setDescription('Added ciscoContentServicesCapabilityCSG2R0305 agent capabilities \n        for Content Service Gateway version 3.5. This verion contains \n        the statistics for Layer 7 protocols including Nbar protocol. \n        Also added load statistical information related to Gx Events.')
ciscoContentServicesCapabilityCSG2R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R04 = ciscoContentServicesCapabilityCSG2R04.setProductRelease('Cisco IOS 12.4(24)MD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R04 = ciscoContentServicesCapabilityCSG2R04.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R04.setDescription('Added ciscoContentServicesCapabilityCSG2R04 agent capabilities\n        for Content Service Gateway 2 release 4. In addition to existing \n        features, the release also provides the statistics of associated\n        subscribers per billing plan.')
ciscoContentServicesCapabilityCSG2R06 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R06 = ciscoContentServicesCapabilityCSG2R06.setProductRelease('Cisco IOS R6')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R06 = ciscoContentServicesCapabilityCSG2R06.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R06.setDescription('Added ciscoContentServicesCapabilityCSG2R06 agent capabilities\n        for Content Service Gateway 2 release 6. In addition to existing \n        features, the release also provides 64 bit version of allowed\n        and denial rate for load statistics.')
mibBuilder.exportSymbols("CISCO-CONTENT-SERVICES-CAPABILITY", PYSNMP_MODULE_ID=ciscoContentServicesCapability, ciscoContentServicesCapability=ciscoContentServicesCapability, ciscoContentServicesCapabilityAdcV01R00=ciscoContentServicesCapabilityAdcV01R00, ciscoContentServicesCapabilityCSG2R0305=ciscoContentServicesCapabilityCSG2R0305, ciscoContentServicesCapabilityCSG2R03=ciscoContentServicesCapabilityCSG2R03, ciscoContentServicesCapabilityCSG2R04=ciscoContentServicesCapabilityCSG2R04, ciscoContentServicesCapabilityCSG2R06=ciscoContentServicesCapabilityCSG2R06)
