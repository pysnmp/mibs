#
# PySNMP MIB module CISCO-IF-EXTENSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IF-EXTENSION-CAPABILITY
# Source digest sha256:511828583d7e3a861baab3b85baee3c3683883f96c489ed6c8f4fe2ec63a87c7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIfExtensionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 395))
ciscoIfExtensionCapability.setRevisions(('2015-06-03 00:00', '2013-09-05 00:00', '2012-03-01 00:00', '2011-03-21 00:00', '2008-03-24 00:00', '2007-11-05 00:00', '2007-08-30 00:00', '2007-04-19 00:00', '2006-02-21 00:00', '2005-04-14 00:00', '2005-03-04 00:00', '2004-01-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIfExtensionCapability.setRevisionsDescriptions(('Added ciscoIfExtensionTableIntfGroup3SupR02 and\n        VARIATIONs for cieIfTransceiverFrequencyConfig,\n        cieIfFillPatternConfig, cieIfIgnoreBitErrorsConfig and\n        cieIfIgnoreInterruptThresholdConfig\n        in capability statement ciscoIfExtCapNxOSV06R0201PMDS9000\n        and ciscoIfExtCapNxOSV06R0202PN7K.', 'Added agent capability statement\n        ciscoIfExtCapNxOSV06R0201PMDS9000 and \n        ciscoIfExtCapNxOSV06R0202PN7K.', 'Added ciscoIfExtCapV15R0002SGPCat4K agent\n        capability statement.', 'Added ciscoIfExtCapNXOSV52R1MDS9000 agent\n        capability statement.', 'Added ciscoIfExtCapCatOSV08R0701PCat6K agent\n        capability statement.', 'Added ciscoIfExtCapc4710aceVA1R700\n        agent capabilities for ACE 4710 Application \n        Control Engine Appliance.', 'Added ciscoIfExtCapV12R0233SXHPCat6K\n        capability statement.', 'Added ciscoIfExtCapV12R0229SM1 and\n        ciscoIfExtCapV12R0412MR1 capability statements.', 'Added capability statement\n        ciscoIfExtCapabilityACSWV03R000 for \n        Application Control Engine (ACE).', 'Added capability statement\n        ciscoIfExtCapSanOSV30R1MDS9000.', 'Added capability statement\n        ciscoIfExtCapV12R0217bSXAPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIfExtensionCapability.setLastUpdated('2015-06-03 00:00')
if mibBuilder.loadTexts: ciscoIfExtensionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIfExtensionCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIfExtensionCapability.setDescription('The capabilities description of\n        CISCO-IF-EXTENSION-MIB.')
ciscoIfExtensionCapV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionCapV08R0301 = ciscoIfExtensionCapV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtensionCapV08R0301 = ciscoIfExtensionCapV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtensionCapV08R0301.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapV12R0217bSXAPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0217bSXAPCat6K = ciscoIfExtCapV12R0217bSXAPCat6K.setProductRelease('Cisco IOS 12.2(17b)SXA on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0217bSXAPCat6K = ciscoIfExtCapV12R0217bSXAPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapV12R0217bSXAPCat6K.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapSanOSV30R1MDS9000 = ciscoIfExtCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0 on Cisco MDS 9000\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapSanOSV30R1MDS9000 = ciscoIfExtCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapSanOSV30R1MDS9000.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapabilityACSWV03R000 = ciscoIfExtCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapabilityACSWV03R000 = ciscoIfExtCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapabilityACSWV03R000.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapV12R0229SM1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0229SM1 = ciscoIfExtCapV12R0229SM1.setProductRelease('Cisco IOS 12.2(29)SM1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0229SM1 = ciscoIfExtCapV12R0229SM1.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapV12R0229SM1.setDescription('IOS 12.2(29)SM1 Cisco CISCO-IF-EXTENSION-MIB User Agent MIB\n        capabilities.')
ciscoIfExtCapV12R0412MR1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0412MR1 = ciscoIfExtCapV12R0412MR1.setProductRelease('Cisco IOS 12.4(2)MR1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0412MR1 = ciscoIfExtCapV12R0412MR1.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapV12R0412MR1.setDescription('IOS 12.4(2)MR1 Cisco CISCO-IF-EXTENSION-MIB User Agent MIB\n        capabilities.')
ciscoIfExtCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0233SXHPCat6K = ciscoIfExtCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV12R0233SXHPCat6K = ciscoIfExtCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapV12R0233SXHPCat6K.setDescription('CISCO-IF-EXTENSION-MIB agent capabilities.')
ciscoIfExtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapc4710aceVA1R700 = ciscoIfExtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapc4710aceVA1R700 = ciscoIfExtCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapc4710aceVA1R700.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapCatOSV08R0701PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapCatOSV08R0701PCat6K = ciscoIfExtCapCatOSV08R0701PCat6K.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500 and\n                     Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapCatOSV08R0701PCat6K = ciscoIfExtCapCatOSV08R0701PCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapCatOSV08R0701PCat6K.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapNXOSV52R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNXOSV52R1MDS9000 = ciscoIfExtCapNXOSV52R1MDS9000.setProductRelease('Cisco NXOS 5.2(1) on MDS 9000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNXOSV52R1MDS9000 = ciscoIfExtCapNXOSV52R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapNXOSV52R1MDS9000.setDescription('CISCO-IF-EXTENSION-MIB capabilities.')
ciscoIfExtCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV15R0002SGPCat4K = ciscoIfExtCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Catalyst 4000 family\n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapV15R0002SGPCat4K = ciscoIfExtCapV15R0002SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapV15R0002SGPCat4K.setDescription('CISCO-IF-EXTENSION-MIB agent capabilities.')
ciscoIfExtCapNxOSV06R0201PMDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0201PMDS9000 = ciscoIfExtCapNxOSV06R0201PMDS9000.setProductRelease('Cisco NX-OS 6.2(1) on MDS 9000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0201PMDS9000 = ciscoIfExtCapNxOSV06R0201PMDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapNxOSV06R0201PMDS9000.setDescription('CISCO-IF-EXTENSION-MIB agent capabilities.')
ciscoIfExtCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 395, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0202PN7K = ciscoIfExtCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfExtCapNxOSV06R0202PN7K = ciscoIfExtCapNxOSV06R0202PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoIfExtCapNxOSV06R0202PN7K.setDescription('CISCO-IF-EXTENSION-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-IF-EXTENSION-CAPABILITY", PYSNMP_MODULE_ID=ciscoIfExtensionCapability, ciscoIfExtCapCatOSV08R0701PCat6K=ciscoIfExtCapCatOSV08R0701PCat6K, ciscoIfExtCapNXOSV52R1MDS9000=ciscoIfExtCapNXOSV52R1MDS9000, ciscoIfExtCapNxOSV06R0201PMDS9000=ciscoIfExtCapNxOSV06R0201PMDS9000, ciscoIfExtCapNxOSV06R0202PN7K=ciscoIfExtCapNxOSV06R0202PN7K, ciscoIfExtCapSanOSV30R1MDS9000=ciscoIfExtCapSanOSV30R1MDS9000, ciscoIfExtCapV12R0217bSXAPCat6K=ciscoIfExtCapV12R0217bSXAPCat6K, ciscoIfExtCapV12R0229SM1=ciscoIfExtCapV12R0229SM1, ciscoIfExtCapV12R0233SXHPCat6K=ciscoIfExtCapV12R0233SXHPCat6K, ciscoIfExtCapV12R0412MR1=ciscoIfExtCapV12R0412MR1, ciscoIfExtCapV15R0002SGPCat4K=ciscoIfExtCapV15R0002SGPCat4K, ciscoIfExtCapabilityACSWV03R000=ciscoIfExtCapabilityACSWV03R000, ciscoIfExtCapc4710aceVA1R700=ciscoIfExtCapc4710aceVA1R700, ciscoIfExtensionCapV08R0301=ciscoIfExtensionCapV08R0301, ciscoIfExtensionCapability=ciscoIfExtensionCapability)
