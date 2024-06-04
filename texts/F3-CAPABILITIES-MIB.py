#
# PySNMP MIB module F3-CAPABILITIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-CAPABILITIES-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 09:26:54 2024
# On host fv-az1146-179 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
f3Capabilities, = mibBuilder.importSymbols("CM-COMMON-MIB", "f3Capabilities")
VlanIdOrAnyOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrAnyOrNone")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, Integer32, IpAddress, TimeTicks, NotificationType, ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibIdentifier, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "IpAddress", "TimeTicks", "NotificationType", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibIdentifier", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
f3CapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1))
f3CapabilityMIB.setRevisions(('2020-02-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f3CapabilityMIB.setRevisionsDescriptions(('\n         Notes from release 202002180000Z\n              - Added f3Rfc2544Capabilities\n\n         Notes from release 201903110000Z\n              - Added f3NidXG118PROACSHCapabilities\n \n         Notes from release 201809240000Z\n              - Added f3NidXG118PROSHCapabilities\n \n         Notes from release 201804190000Z\n              - Added f3NidXG116PROHCapabilities\n \n         Notes from release 201107080000Z\n               -Added capabilities for \n                    ethernetNTEGE206CardFineGrainedPmInterval,\n                    ethernetNTEGE201SyncECardFineGrainedPmInterval,\n                    ethernetNTEGE201CardFineGrainedPmInterval,\n                    ethernetNTEGE206FCardFineGrainedPmInterval\n\n         Notes from release 201106010000Z\n               -First release of the agent capabilities with R5.2.1CC.',))
if mibBuilder.loadTexts: f3CapabilityMIB.setLastUpdated('202002180000Z')
if mibBuilder.loadTexts: f3CapabilityMIB.setOrganization('ADVA Optical Networking SE')
if mibBuilder.loadTexts: f3CapabilityMIB.setContactInfo('Web URL: http://adva.com/\n        E-mail:  support@adva.com\n        Postal:  ADVA Optical Networking SE\n             Campus Martinsried\n             Fraunhoferstrasse 9a\n             82152 Martinsried/Munich\n             Germany\n        Phone: +49 089 89 06 65 0\n        Fax:  +49 089 89 06 65 199 ')
if mibBuilder.loadTexts: f3CapabilityMIB.setDescription('This module defines the Capabilities MIB definitions used by \n             the F3 (FSP150CC) product lines.\n             Copyright (C) ADVA.')
f3CapabilityDefinitions = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1))
f3BaseStandardsCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BaseStandardsCapabilities = f3BaseStandardsCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BaseStandardsCapabilities = f3BaseStandardsCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3BaseStandardsCapabilities.setDescription('SNMP Standard/Framework Capabilities for the F3 product family')
f3StandardIfEntityCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardIfEntityCapabilities = f3StandardIfEntityCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardIfEntityCapabilities = f3StandardIfEntityCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3StandardIfEntityCapabilities.setDescription('SNMP Standard IF and ENTITY Capabilities for the F3 product family')
f3StandardTargetNotifCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardTargetNotifCapabilities = f3StandardTargetNotifCapabilities.setProductRelease('F3 - Standard Interface and Entity capabilities ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardTargetNotifCapabilities = f3StandardTargetNotifCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3StandardTargetNotifCapabilities.setDescription('SNMP Target/Notification Capabilities for the F3 product family')
f3StandardSecurityCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardSecurityCapabilities = f3StandardSecurityCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardSecurityCapabilities = f3StandardSecurityCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3StandardSecurityCapabilities.setDescription('SNMP Security Capabilities for the F3 product family')
f3StandardRMONCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardRMONCapabilities = f3StandardRMONCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardRMONCapabilities = f3StandardRMONCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3StandardRMONCapabilities.setDescription('SNMP RMON Capabilities for the F3  product family')
f3StandardCfmCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardCfmCapabilities = f3StandardCfmCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardCfmCapabilities = f3StandardCfmCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3StandardCfmCapabilities.setDescription('SNMP Standard 8021.ag Capabilities for the F3 product family')
f3StandardBridgeCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardBridgeCapabilities = f3StandardBridgeCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardBridgeCapabilities = f3StandardBridgeCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3StandardBridgeCapabilities.setDescription('SNMP Standard Bridging Capabilities for the F3 product family')
f3StandardLAGCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardLAGCapabilities = f3StandardLAGCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardLAGCapabilities = f3StandardLAGCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3StandardLAGCapabilities.setDescription('SNMP Standard Link Aggregation Capabilities for the F3 product family')
f3CommonVendorSpecificCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CommonVendorSpecificCapabilities = f3CommonVendorSpecificCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CommonVendorSpecificCapabilities = f3CommonVendorSpecificCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3CommonVendorSpecificCapabilities.setDescription('SNMP Common vendor specific capabilities for the F3 products')
f3FacilityCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilities = f3FacilityCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilities = f3FacilityCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3FacilityCapabilities.setDescription('SNMP vendor specific Facility capabilities for the F3 products')
f3Nid206Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206Capabilities = f3Nid206Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206Capabilities = f3Nid206Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid206Capabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - GE206')
f3Nid201SyncECapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid201SyncECapabilities = f3Nid201SyncECapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid201SyncECapabilities = f3Nid201SyncECapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid201SyncECapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - GE201 SyncE')
f3Nid201NonSyncECapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid201NonSyncECapabilities = f3Nid201NonSyncECapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid201NonSyncECapabilities = f3Nid201NonSyncECapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid201NonSyncECapabilities.setDescription('SNMP vendor specific Entity capabilities for \n                      F3 product - GE201 Non-SyncE')
f3Nid206FCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206FCapabilities = f3Nid206FCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206FCapabilities = f3Nid206FCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid206FCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - GE206F')
f3Nid112Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112Capabilities = f3Nid112Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112Capabilities = f3Nid112Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid112Capabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - GE112')
f3Nid114Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114Capabilities = f3Nid114Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114Capabilities = f3Nid114Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114Capabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - GE114')
f3EcpaCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EcpaCapabilities = f3EcpaCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EcpaCapabilities = f3EcpaCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3EcpaCapabilities.setDescription('SNMP Ecpa capabilities for F3 product')
f3EsaCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EsaCapabilities = f3EsaCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EsaCapabilities = f3EsaCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3EsaCapabilities.setDescription('SNMP Esa capabilities for F3 product')
f3BridgeCapabilitiesCmHub = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BridgeCapabilitiesCmHub = f3BridgeCapabilitiesCmHub.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BridgeCapabilitiesCmHub = f3BridgeCapabilitiesCmHub.setStatus('current')
if mibBuilder.loadTexts: f3BridgeCapabilitiesCmHub.setDescription('SNMP Bridging Capabilities for the F3 product family - CMHUB')
f3CommonVendorSpecificCapabilitiesCmHub = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CommonVendorSpecificCapabilitiesCmHub = f3CommonVendorSpecificCapabilitiesCmHub.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CommonVendorSpecificCapabilitiesCmHub = f3CommonVendorSpecificCapabilitiesCmHub.setStatus('current')
if mibBuilder.loadTexts: f3CommonVendorSpecificCapabilitiesCmHub.setDescription('SNMP Common vendor specific capabilities for the F3 products')
f3FacilityCapabilitiesCmHub = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilitiesCmHub = f3FacilityCapabilitiesCmHub.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilitiesCmHub = f3FacilityCapabilitiesCmHub.setStatus('current')
if mibBuilder.loadTexts: f3FacilityCapabilitiesCmHub.setDescription('SNMP vendor specific Facility capabilities for the F3 products')
f3EntityCmHubCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EntityCmHubCapabilities = f3EntityCmHubCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EntityCmHubCapabilities = f3EntityCmHubCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3EntityCmHubCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - HUBSHELF')
f3Nid206VCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206VCapabilities = f3Nid206VCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206VCapabilities = f3Nid206VCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid206VCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - GE206V')
f3NidXG210Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 24))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG210Capabilities = f3NidXG210Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG210Capabilities = f3NidXG210Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidXG210Capabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - XG210')
f3PtpCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 25))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PtpCapabilities = f3PtpCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PtpCapabilities = f3PtpCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3PtpCapabilities.setDescription('SNMP vendor specific PTP capabilities for F3 product')
f3PseudoWireCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 26))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PseudoWireCapabilities = f3PseudoWireCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PseudoWireCapabilities = f3PseudoWireCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3PseudoWireCapabilities.setDescription('SNMP vendor specific PWE capabilities for F3 product')
f3DS1Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 27))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3DS1Capabilities = f3DS1Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3DS1Capabilities = f3DS1Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3DS1Capabilities.setDescription('SNMP vendor specific DS1 capabilities for F3 product')
f3SonetCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 28))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SonetCapabilities = f3SonetCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SonetCapabilities = f3SonetCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3SonetCapabilities.setDescription('SNMP vendor specific Sonet capabilities for F3 product')
f3SyncECapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 29))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SyncECapabilities = f3SyncECapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SyncECapabilities = f3SyncECapabilities.setStatus('current')
if mibBuilder.loadTexts: f3SyncECapabilities.setDescription('SNMP vendor specific Synchronous Ethernet capabilities for F3 product family.')
f3CfmCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 30))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CfmCapabilities = f3CfmCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CfmCapabilities = f3CfmCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3CfmCapabilities.setDescription('SNMP vendor specific CFM capabilities for F3 product family.')
f3LAGCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 31))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3LAGCapabilities = f3LAGCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3LAGCapabilities = f3LAGCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3LAGCapabilities.setDescription('SNMP vendor specific LAG capabilities for F3 product family.')
f3PBBCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 32))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PBBCapabilities = f3PBBCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PBBCapabilities = f3PBBCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3PBBCapabilities.setDescription('SNMP vendor specific PBB capabilities for F3 product family.')
f3Nid1804Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 33))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid1804Capabilities = f3Nid1804Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid1804Capabilities = f3Nid1804Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid1804Capabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - T1804')
f3Nid3204Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 34))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid3204Capabilities = f3Nid3204Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid3204Capabilities = f3Nid3204Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid3204Capabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - T3204')
f3BertCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 35))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BertCapabilities = f3BertCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BertCapabilities = f3BertCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3BertCapabilities.setDescription('SNMP vendor specific Bert capabilities for F3 product family.')
f3NidSyncProbeCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 36))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidSyncProbeCapabilities = f3NidSyncProbeCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidSyncProbeCapabilities = f3NidSyncProbeCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidSyncProbeCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - SyncProbe')
f3SyncJackCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 37))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SyncJackCapabilities = f3SyncJackCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SyncJackCapabilities = f3SyncJackCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3SyncJackCapabilities.setDescription('SNMP vendor specific SyncJack capabilities for F3 product family.')
f3EsmCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 38))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EsmCapabilities = f3EsmCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EsmCapabilities = f3EsmCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3EsmCapabilities.setDescription('SNMP vendor specific ESM Breadcrumbs capabilities for F3 product family.')
f3AMPClientCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 39))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AMPClientCapabilities = f3AMPClientCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AMPClientCapabilities = f3AMPClientCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3AMPClientCapabilities.setDescription('SNMP vendor specific AMP Client capabilities for F3 product family.')
f3AMPServerCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 40))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AMPServerCapabilities = f3AMPServerCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AMPServerCapabilities = f3AMPServerCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3AMPServerCapabilities.setDescription('SNMP vendor specific AMP Server capabilities for F3 product family.')
f3Nid114HCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 41))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114HCapabilities = f3Nid114HCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114HCapabilities = f3Nid114HCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114HCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - GE114H')
f3Nid114PHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 42))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114PHCapabilities = f3Nid114PHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114PHCapabilities = f3Nid114PHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114PHCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - GE114PH')
f3ERPCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 43))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ERPCapabilities = f3ERPCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ERPCapabilities = f3ERPCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3ERPCapabilities.setDescription('SNMP vendor specific ERP capabilities for F3 product family.')
f3ShgCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 44))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ShgCapabilities = f3ShgCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ShgCapabilities = f3ShgCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3ShgCapabilities.setDescription('SNMP vendor specific SHG capabilities for F3 product family.')
f3Nid114SCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 45))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114SCapabilities = f3Nid114SCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114SCapabilities = f3Nid114SCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114SCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - GE114S')
f3Nid114SHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 46))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114SHCapabilities = f3Nid114SHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114SHCapabilities = f3Nid114SHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114SHCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - GE114SH')
f3Ipv6Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 47))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Ipv6Capabilities = f3Ipv6Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Ipv6Capabilities = f3Ipv6Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3Ipv6Capabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - family')
f3SatCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 48))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SatCapabilities = f3SatCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SatCapabilities = f3SatCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3SatCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 product - family')
f3JdsuCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 49))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3JdsuCapabilities = f3JdsuCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3JdsuCapabilities = f3JdsuCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3JdsuCapabilities.setDescription('SNMP vendor specific JDSU loopback capabilities for F3 product family.')
f3PortMirrorCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 50))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PortMirrorCapabilities = f3PortMirrorCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PortMirrorCapabilities = f3PortMirrorCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3PortMirrorCapabilities.setDescription('SNMP vendor specific Port Mirror capabilities for F3 product family.')
f3JdsuGeneratorCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 51))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3JdsuGeneratorCapabilities = f3JdsuGeneratorCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3JdsuGeneratorCapabilities = f3JdsuGeneratorCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3JdsuGeneratorCapabilities.setDescription('SNMP vendor specific JDSU Generator capabilities for F3 product family.')
f3TwampCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 52))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3TwampCapabilities = f3TwampCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3TwampCapabilities = f3TwampCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3TwampCapabilities.setDescription('SNMP vendor specific TWAMP capabilities for F3 product family.')
f3OspfCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 53))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OspfCapabilities = f3OspfCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OspfCapabilities = f3OspfCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3OspfCapabilities.setDescription('SNMP vendor specific OSPF capabilities for F3 product family.')
f3Mef35Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 54))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Mef35Capabilities = f3Mef35Capabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Mef35Capabilities = f3Mef35Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3Mef35Capabilities.setDescription('SNMP vendor specific MEF 35/36 capabilities for F3 product family.')
f3Nid112ProCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 55))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProCapabilities = f3Nid112ProCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProCapabilities = f3Nid112ProCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid112ProCapabilities.setDescription('SNMP vendor specific GE112Pro for F3 product family.')
f3Nid112ProMCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 56))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProMCapabilities = f3Nid112ProMCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProMCapabilities = f3Nid112ProMCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid112ProMCapabilities.setDescription('SNMP vendor specific GE112ProM for F3 product family.')
f3Nid114ProCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 57))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCapabilities = f3Nid114ProCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCapabilities = f3Nid114ProCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114ProCapabilities.setDescription('SNMP vendor specific GE114Pro for F3 product family.')
f3Nid114ProCCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 58))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCCapabilities = f3Nid114ProCCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCCapabilities = f3Nid114ProCCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114ProCCapabilities.setDescription('SNMP vendor specific GE114ProC for F3 product family.')
f3Nid114ProSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 59))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProSHCapabilities = f3Nid114ProSHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProSHCapabilities = f3Nid114ProSHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114ProSHCapabilities.setDescription('SNMP vendor specific GE114ProSH for F3 product family.')
f3Nid114ProCSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 60))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCSHCapabilities = f3Nid114ProCSHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCSHCapabilities = f3Nid114ProCSHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114ProCSHCapabilities.setDescription('SNMP vendor specific GE114ProCSH for F3 product family.')
f3Nid114ProHECapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 61))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProHECapabilities = f3Nid114ProHECapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProHECapabilities = f3Nid114ProHECapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114ProHECapabilities.setDescription('SNMP vendor specific GE114ProHE for F3 product family.')
f3Nid112ProHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 62))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProHCapabilities = f3Nid112ProHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProHCapabilities = f3Nid112ProHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid112ProHCapabilities.setDescription('SNMP vendor specific GE112ProH for F3 product family.')
f3ConnectGuardCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 63))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ConnectGuardCapabilities = f3ConnectGuardCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ConnectGuardCapabilities = f3ConnectGuardCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3ConnectGuardCapabilities.setDescription('SNMP vendor specific Connect Guard capabilities for F3 product')
f3L3Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 64))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3Capabilities = f3L3Capabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3Capabilities = f3L3Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3L3Capabilities.setDescription('SNMP vendor specific L3 Service Model capabilities for F3 XG products')
f3Nid114GCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 65))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114GCapabilities = f3Nid114GCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114GCapabilities = f3Nid114GCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114GCapabilities.setDescription('SNMP vendor specific GE114G for F3 product family.')
f3BfdCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 66))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BfdCapabilities = f3BfdCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BfdCapabilities = f3BfdCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3BfdCapabilities.setDescription('SNMP vendor specific BFD for F3 product family.')
f3EoMplsCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 67))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EoMplsCapabilities = f3EoMplsCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EoMplsCapabilities = f3EoMplsCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3EoMplsCapabilities.setDescription('SNMP vendor specific EoMpls for F3 product family.')
f3FpmCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 68))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FpmCapabilities = f3FpmCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FpmCapabilities = f3FpmCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3FpmCapabilities.setDescription('SNMP vendor specific Flowpoint Model capabilities for F3 product')
f3Nid114ProVMHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 69))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMHCapabilities = f3Nid114ProVMHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMHCapabilities = f3Nid114ProVMHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114ProVMHCapabilities.setDescription('SNMP vendor specific GE114ProVMH for F3 product family.')
f3Nid114ProVMCHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 70))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMCHCapabilities = f3Nid114ProVMCHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMCHCapabilities = f3Nid114ProVMCHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114ProVMCHCapabilities.setDescription('SNMP vendor specific GE114ProVMCH for F3 product family.')
f3Nid114ProVMCSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 71))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMCSHCapabilities = f3Nid114ProVMCSHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMCSHCapabilities = f3Nid114ProVMCSHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114ProVMCSHCapabilities.setDescription('SNMP vendor specific GE114ProVMCSH for F3 product family.')
f3NidGe101ProCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 72))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGe101ProCapabilities = f3NidGe101ProCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGe101ProCapabilities = f3NidGe101ProCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidGe101ProCapabilities.setDescription('SNMP vendor specific GE101Pro for F3 product family.')
f3NidGo102ProSCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 73))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSCapabilities = f3NidGo102ProSCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSCapabilities = f3NidGo102ProSCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidGo102ProSCapabilities.setDescription('SNMP vendor specific Go102ProS for F3 product family.')
f3NidGo102ProSPCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 74))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSPCapabilities = f3NidGo102ProSPCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSPCapabilities = f3NidGo102ProSPCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidGo102ProSPCapabilities.setDescription('SNMP vendor specific Go102ProSP for F3 product family.')
f3NidCx101Pro30ACapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 75))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidCx101Pro30ACapabilities = f3NidCx101Pro30ACapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidCx101Pro30ACapabilities = f3NidCx101Pro30ACapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidCx101Pro30ACapabilities.setDescription('SNMP vendor specific Pro Cx101Pro30a for F3 product family.')
f3NidCx102Pro30ACapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 76))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidCx102Pro30ACapabilities = f3NidCx102Pro30ACapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidCx102Pro30ACapabilities = f3NidCx102Pro30ACapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidCx102Pro30ACapabilities.setDescription('SNMP vendor specific Cx102Pro30a for F3 product family.')
f3IpfixCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 77))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3IpfixCapabilities = f3IpfixCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3IpfixCapabilities = f3IpfixCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3IpfixCapabilities.setDescription('SNMP vendor specific IPFIX for F3 product family.')
f3VxlanCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 78))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3VxlanCapabilities = f3VxlanCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3VxlanCapabilities = f3VxlanCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3VxlanCapabilities.setDescription('SNMP vendor specific Vxlan for F3 product family.')
f3GreCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 79))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3GreCapabilities = f3GreCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3GreCapabilities = f3GreCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3GreCapabilities.setDescription('SNMP vendor specific GRE for F3 product family.')
f3NtpCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 80))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NtpCapabilities = f3NtpCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NtpCapabilities = f3NtpCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NtpCapabilities.setDescription('SNMP vendor specific NTP capabilities for F3 product')
f3ElpCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 81))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ElpCapabilities = f3ElpCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ElpCapabilities = f3ElpCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3ElpCapabilities.setDescription('SNMP vendor specific ELP capabilities for F3 product')
f3NidXG116PROCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 82))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG116PROCapabilities = f3NidXG116PROCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG116PROCapabilities = f3NidXG116PROCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidXG116PROCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 products - XG116PRO')
f3NidXG120PROCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 83))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG120PROCapabilities = f3NidXG120PROCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG120PROCapabilities = f3NidXG120PROCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidXG120PROCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 products - XG120PRO')
f3FacilityCapabilitiesXGPRO = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 84))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilitiesXGPRO = f3FacilityCapabilitiesXGPRO.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilitiesXGPRO = f3FacilityCapabilitiesXGPRO.setStatus('current')
if mibBuilder.loadTexts: f3FacilityCapabilitiesXGPRO.setDescription('SNMP vendor specific Facility capabilities for the F3 XGPRO products')
f3EoMplsCapabilitiesXG = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 85))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EoMplsCapabilitiesXG = f3EoMplsCapabilitiesXG.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EoMplsCapabilitiesXG = f3EoMplsCapabilitiesXG.setStatus('current')
if mibBuilder.loadTexts: f3EoMplsCapabilitiesXG.setDescription('SNMP vendor specific EoMpls for the F3 XG products.')
f3Nid112ProVMCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 86))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProVMCapabilities = f3Nid112ProVMCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProVMCapabilities = f3Nid112ProVMCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid112ProVMCapabilities.setDescription('SNMP vendor specific GE112ProVM for F3 product family.')
f3SystemCommonCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 87))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SystemCommonCapabilities = f3SystemCommonCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SystemCommonCapabilities = f3SystemCommonCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3SystemCommonCapabilities.setDescription('SNMP vendor specific System capabilities for the F3 products')
f3NidXG116PROHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 88))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG116PROHCapabilities = f3NidXG116PROHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG116PROHCapabilities = f3NidXG116PROHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidXG116PROHCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 products - XG116PRO (H)')
f3NidGo102ProSMCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 89))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSMCapabilities = f3NidGo102ProSMCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSMCapabilities = f3NidGo102ProSMCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidGo102ProSMCapabilities.setDescription('SNMP vendor specific Go102ProSM for F3 product family.')
f3NidXG118PROSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 90))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG118PROSHCapabilities = f3NidXG118PROSHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG118PROSHCapabilities = f3NidXG118PROSHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidXG118PROSHCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 products - XG118PRO (SH)')
f3L3CapabilitiesGE = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 91))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3CapabilitiesGE = f3L3CapabilitiesGE.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3CapabilitiesGE = f3L3CapabilitiesGE.setStatus('current')
if mibBuilder.loadTexts: f3L3CapabilitiesGE.setDescription('SNMP vendor specific L3 Service Model capabilities for F3 GE products')
f3L3TrafficOSPFCapabilties = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 92))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficOSPFCapabilties = f3L3TrafficOSPFCapabilties.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficOSPFCapabilties = f3L3TrafficOSPFCapabilties.setStatus('current')
if mibBuilder.loadTexts: f3L3TrafficOSPFCapabilties.setDescription('SNMP vendor specific Traffic OSPF for the F3 product family.')
f3L3TrafficBGPCapabilties = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 93))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficBGPCapabilties = f3L3TrafficBGPCapabilties.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficBGPCapabilties = f3L3TrafficBGPCapabilties.setStatus('current')
if mibBuilder.loadTexts: f3L3TrafficBGPCapabilties.setDescription('SNMP vendor specific Traffic BGP for the F3 product family.')
f3L3TrafficIPv6Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 94))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficIPv6Capabilities = f3L3TrafficIPv6Capabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficIPv6Capabilities = f3L3TrafficIPv6Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3L3TrafficIPv6Capabilities.setDescription('SNMP vendor specific Traffic IPv6 for the F3 product family.')
f3NidXG118PROACSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 95))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG118PROACSHCapabilities = f3NidXG118PROACSHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG118PROACSHCapabilities = f3NidXG118PROACSHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidXG118PROACSHCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 products - XG118PROAC (SH)')
f3Nid114ProVMSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 96))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMSHCapabilities = f3Nid114ProVMSHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMSHCapabilities = f3Nid114ProVMSHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3Nid114ProVMSHCapabilities.setDescription('SNMP vendor specific GE114ProVMSH for F3 product family.')
f3NidGe104Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 97))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGe104Capabilities = f3NidGe104Capabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGe104Capabilities = f3NidGe104Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidGe104Capabilities.setDescription('SNMP vendor specific GE104 for F3 product family.')
f3NidXG120PROSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 98))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG120PROSHCapabilities = f3NidXG120PROSHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG120PROSHCapabilities = f3NidXG120PROSHCapabilities.setStatus('current')
if mibBuilder.loadTexts: f3NidXG120PROSHCapabilities.setDescription('SNMP vendor specific Entity capabilities for F3 products - XG120PROSH')
f3Rfc2544Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 99))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Rfc2544Capabilities = f3Rfc2544Capabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Rfc2544Capabilities = f3Rfc2544Capabilities.setStatus('current')
if mibBuilder.loadTexts: f3Rfc2544Capabilities.setDescription('SNMP vendor specific Rfc2544 capabilities for F3 product family.')
mibBuilder.exportSymbols("F3-CAPABILITIES-MIB", f3CapabilityDefinitions=f3CapabilityDefinitions, f3StandardTargetNotifCapabilities=f3StandardTargetNotifCapabilities, f3EsmCapabilities=f3EsmCapabilities, f3ElpCapabilities=f3ElpCapabilities, f3FacilityCapabilitiesXGPRO=f3FacilityCapabilitiesXGPRO, f3Nid112ProCapabilities=f3Nid112ProCapabilities, f3NidGo102ProSMCapabilities=f3NidGo102ProSMCapabilities, f3BfdCapabilities=f3BfdCapabilities, f3FpmCapabilities=f3FpmCapabilities, f3NidCx102Pro30ACapabilities=f3NidCx102Pro30ACapabilities, f3DS1Capabilities=f3DS1Capabilities, f3L3CapabilitiesGE=f3L3CapabilitiesGE, f3NidGo102ProSCapabilities=f3NidGo102ProSCapabilities, f3NidXG118PROSHCapabilities=f3NidXG118PROSHCapabilities, f3NidGo102ProSPCapabilities=f3NidGo102ProSPCapabilities, f3BridgeCapabilitiesCmHub=f3BridgeCapabilitiesCmHub, f3NidCx101Pro30ACapabilities=f3NidCx101Pro30ACapabilities, f3BertCapabilities=f3BertCapabilities, f3Nid206VCapabilities=f3Nid206VCapabilities, f3IpfixCapabilities=f3IpfixCapabilities, f3GreCapabilities=f3GreCapabilities, f3Nid112ProVMCapabilities=f3Nid112ProVMCapabilities, f3StandardRMONCapabilities=f3StandardRMONCapabilities, f3StandardCfmCapabilities=f3StandardCfmCapabilities, f3NidXG116PROHCapabilities=f3NidXG116PROHCapabilities, f3CfmCapabilities=f3CfmCapabilities, f3Nid114ProVMHCapabilities=f3Nid114ProVMHCapabilities, f3Nid3204Capabilities=f3Nid3204Capabilities, f3NidXG116PROCapabilities=f3NidXG116PROCapabilities, f3Nid114ProSHCapabilities=f3Nid114ProSHCapabilities, f3StandardSecurityCapabilities=f3StandardSecurityCapabilities, f3PtpCapabilities=f3PtpCapabilities, f3Nid114ProVMSHCapabilities=f3Nid114ProVMSHCapabilities, f3LAGCapabilities=f3LAGCapabilities, f3EcpaCapabilities=f3EcpaCapabilities, f3Nid112ProHCapabilities=f3Nid112ProHCapabilities, f3SystemCommonCapabilities=f3SystemCommonCapabilities, f3StandardBridgeCapabilities=f3StandardBridgeCapabilities, f3Nid1804Capabilities=f3Nid1804Capabilities, f3Nid114PHCapabilities=f3Nid114PHCapabilities, f3Nid114SHCapabilities=f3Nid114SHCapabilities, f3Nid114ProHECapabilities=f3Nid114ProHECapabilities, f3NidXG120PROCapabilities=f3NidXG120PROCapabilities, f3ERPCapabilities=f3ERPCapabilities, f3AMPClientCapabilities=f3AMPClientCapabilities, f3Nid201NonSyncECapabilities=f3Nid201NonSyncECapabilities, f3PBBCapabilities=f3PBBCapabilities, f3CapabilityMIB=f3CapabilityMIB, f3Nid112ProMCapabilities=f3Nid112ProMCapabilities, f3FacilityCapabilitiesCmHub=f3FacilityCapabilitiesCmHub, f3SonetCapabilities=f3SonetCapabilities, f3NtpCapabilities=f3NtpCapabilities, f3EoMplsCapabilitiesXG=f3EoMplsCapabilitiesXG, f3Nid201SyncECapabilities=f3Nid201SyncECapabilities, f3AMPServerCapabilities=f3AMPServerCapabilities, f3SatCapabilities=f3SatCapabilities, f3Nid206Capabilities=f3Nid206Capabilities, f3Nid114ProVMCHCapabilities=f3Nid114ProVMCHCapabilities, f3NidGe104Capabilities=f3NidGe104Capabilities, f3Nid114ProVMCSHCapabilities=f3Nid114ProVMCSHCapabilities, f3NidGe101ProCapabilities=f3NidGe101ProCapabilities, f3Nid114HCapabilities=f3Nid114HCapabilities, f3Mef35Capabilities=f3Mef35Capabilities, f3L3TrafficIPv6Capabilities=f3L3TrafficIPv6Capabilities, f3PseudoWireCapabilities=f3PseudoWireCapabilities, f3L3TrafficBGPCapabilties=f3L3TrafficBGPCapabilties, f3Nid114ProCCapabilities=f3Nid114ProCCapabilities, f3ConnectGuardCapabilities=f3ConnectGuardCapabilities, f3NidSyncProbeCapabilities=f3NidSyncProbeCapabilities, f3Nid114SCapabilities=f3Nid114SCapabilities, f3SyncJackCapabilities=f3SyncJackCapabilities, f3EoMplsCapabilities=f3EoMplsCapabilities, PYSNMP_MODULE_ID=f3CapabilityMIB, f3Nid114GCapabilities=f3Nid114GCapabilities, f3OspfCapabilities=f3OspfCapabilities, f3Ipv6Capabilities=f3Ipv6Capabilities, f3TwampCapabilities=f3TwampCapabilities, f3SyncECapabilities=f3SyncECapabilities, f3VxlanCapabilities=f3VxlanCapabilities, f3NidXG120PROSHCapabilities=f3NidXG120PROSHCapabilities, f3Nid114Capabilities=f3Nid114Capabilities, f3JdsuGeneratorCapabilities=f3JdsuGeneratorCapabilities, f3PortMirrorCapabilities=f3PortMirrorCapabilities, f3NidXG210Capabilities=f3NidXG210Capabilities, f3CommonVendorSpecificCapabilitiesCmHub=f3CommonVendorSpecificCapabilitiesCmHub, f3Nid114ProCapabilities=f3Nid114ProCapabilities, f3JdsuCapabilities=f3JdsuCapabilities, f3Nid206FCapabilities=f3Nid206FCapabilities, f3BaseStandardsCapabilities=f3BaseStandardsCapabilities, f3Rfc2544Capabilities=f3Rfc2544Capabilities, f3CommonVendorSpecificCapabilities=f3CommonVendorSpecificCapabilities, f3EsaCapabilities=f3EsaCapabilities, f3ShgCapabilities=f3ShgCapabilities, f3Nid114ProCSHCapabilities=f3Nid114ProCSHCapabilities, f3L3TrafficOSPFCapabilties=f3L3TrafficOSPFCapabilties, f3StandardIfEntityCapabilities=f3StandardIfEntityCapabilities, f3StandardLAGCapabilities=f3StandardLAGCapabilities, f3EntityCmHubCapabilities=f3EntityCmHubCapabilities, f3FacilityCapabilities=f3FacilityCapabilities, f3NidXG118PROACSHCapabilities=f3NidXG118PROACSHCapabilities, f3L3Capabilities=f3L3Capabilities, f3Nid112Capabilities=f3Nid112Capabilities)
