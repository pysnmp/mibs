#
# PySNMP MIB module F3-CAPABILITIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-CAPABILITIES-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 22:26:08 2022
# On host fv-az36-646 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
f3Capabilities, = mibBuilder.importSymbols("CM-COMMON-MIB", "f3Capabilities")
VlanIdOrAnyOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrAnyOrNone")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, MibIdentifier, Bits, ObjectIdentity, NotificationType, Counter64, iso, Gauge32, ModuleIdentity, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "MibIdentifier", "Bits", "ObjectIdentity", "NotificationType", "Counter64", "iso", "Gauge32", "ModuleIdentity", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
f3CapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1))
f3CapabilityMIB.setRevisions(('2020-02-18 00:00',))
if mibBuilder.loadTexts: f3CapabilityMIB.setLastUpdated('202002180000Z')
if mibBuilder.loadTexts: f3CapabilityMIB.setOrganization('ADVA Optical Networking SE')
f3CapabilityDefinitions = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1))
f3BaseStandardsCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BaseStandardsCapabilities = f3BaseStandardsCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BaseStandardsCapabilities = f3BaseStandardsCapabilities.setStatus('current')
f3StandardIfEntityCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardIfEntityCapabilities = f3StandardIfEntityCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardIfEntityCapabilities = f3StandardIfEntityCapabilities.setStatus('current')
f3StandardTargetNotifCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardTargetNotifCapabilities = f3StandardTargetNotifCapabilities.setProductRelease('F3 - Standard Interface and Entity capabilities ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardTargetNotifCapabilities = f3StandardTargetNotifCapabilities.setStatus('current')
f3StandardSecurityCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardSecurityCapabilities = f3StandardSecurityCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardSecurityCapabilities = f3StandardSecurityCapabilities.setStatus('current')
f3StandardRMONCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardRMONCapabilities = f3StandardRMONCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardRMONCapabilities = f3StandardRMONCapabilities.setStatus('current')
f3StandardCfmCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardCfmCapabilities = f3StandardCfmCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardCfmCapabilities = f3StandardCfmCapabilities.setStatus('current')
f3StandardBridgeCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardBridgeCapabilities = f3StandardBridgeCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardBridgeCapabilities = f3StandardBridgeCapabilities.setStatus('current')
f3StandardLAGCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardLAGCapabilities = f3StandardLAGCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3StandardLAGCapabilities = f3StandardLAGCapabilities.setStatus('current')
f3CommonVendorSpecificCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CommonVendorSpecificCapabilities = f3CommonVendorSpecificCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CommonVendorSpecificCapabilities = f3CommonVendorSpecificCapabilities.setStatus('current')
f3FacilityCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilities = f3FacilityCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilities = f3FacilityCapabilities.setStatus('current')
f3Nid206Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206Capabilities = f3Nid206Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206Capabilities = f3Nid206Capabilities.setStatus('current')
f3Nid201SyncECapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid201SyncECapabilities = f3Nid201SyncECapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid201SyncECapabilities = f3Nid201SyncECapabilities.setStatus('current')
f3Nid201NonSyncECapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid201NonSyncECapabilities = f3Nid201NonSyncECapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid201NonSyncECapabilities = f3Nid201NonSyncECapabilities.setStatus('current')
f3Nid206FCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206FCapabilities = f3Nid206FCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206FCapabilities = f3Nid206FCapabilities.setStatus('current')
f3Nid112Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112Capabilities = f3Nid112Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112Capabilities = f3Nid112Capabilities.setStatus('current')
f3Nid114Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114Capabilities = f3Nid114Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114Capabilities = f3Nid114Capabilities.setStatus('current')
f3EcpaCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EcpaCapabilities = f3EcpaCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EcpaCapabilities = f3EcpaCapabilities.setStatus('current')
f3EsaCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EsaCapabilities = f3EsaCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EsaCapabilities = f3EsaCapabilities.setStatus('current')
f3BridgeCapabilitiesCmHub = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BridgeCapabilitiesCmHub = f3BridgeCapabilitiesCmHub.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BridgeCapabilitiesCmHub = f3BridgeCapabilitiesCmHub.setStatus('current')
f3CommonVendorSpecificCapabilitiesCmHub = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CommonVendorSpecificCapabilitiesCmHub = f3CommonVendorSpecificCapabilitiesCmHub.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CommonVendorSpecificCapabilitiesCmHub = f3CommonVendorSpecificCapabilitiesCmHub.setStatus('current')
f3FacilityCapabilitiesCmHub = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilitiesCmHub = f3FacilityCapabilitiesCmHub.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilitiesCmHub = f3FacilityCapabilitiesCmHub.setStatus('current')
f3EntityCmHubCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EntityCmHubCapabilities = f3EntityCmHubCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EntityCmHubCapabilities = f3EntityCmHubCapabilities.setStatus('current')
f3Nid206VCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206VCapabilities = f3Nid206VCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid206VCapabilities = f3Nid206VCapabilities.setStatus('current')
f3NidXG210Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 24))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG210Capabilities = f3NidXG210Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG210Capabilities = f3NidXG210Capabilities.setStatus('current')
f3PtpCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 25))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PtpCapabilities = f3PtpCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PtpCapabilities = f3PtpCapabilities.setStatus('current')
f3PseudoWireCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 26))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PseudoWireCapabilities = f3PseudoWireCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PseudoWireCapabilities = f3PseudoWireCapabilities.setStatus('current')
f3DS1Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 27))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3DS1Capabilities = f3DS1Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3DS1Capabilities = f3DS1Capabilities.setStatus('current')
f3SonetCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 28))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SonetCapabilities = f3SonetCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SonetCapabilities = f3SonetCapabilities.setStatus('current')
f3SyncECapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 29))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SyncECapabilities = f3SyncECapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SyncECapabilities = f3SyncECapabilities.setStatus('current')
f3CfmCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 30))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CfmCapabilities = f3CfmCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3CfmCapabilities = f3CfmCapabilities.setStatus('current')
f3LAGCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 31))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3LAGCapabilities = f3LAGCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3LAGCapabilities = f3LAGCapabilities.setStatus('current')
f3PBBCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 32))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PBBCapabilities = f3PBBCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PBBCapabilities = f3PBBCapabilities.setStatus('current')
f3Nid1804Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 33))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid1804Capabilities = f3Nid1804Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid1804Capabilities = f3Nid1804Capabilities.setStatus('current')
f3Nid3204Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 34))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid3204Capabilities = f3Nid3204Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid3204Capabilities = f3Nid3204Capabilities.setStatus('current')
f3BertCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 35))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BertCapabilities = f3BertCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BertCapabilities = f3BertCapabilities.setStatus('current')
f3NidSyncProbeCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 36))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidSyncProbeCapabilities = f3NidSyncProbeCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidSyncProbeCapabilities = f3NidSyncProbeCapabilities.setStatus('current')
f3SyncJackCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 37))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SyncJackCapabilities = f3SyncJackCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SyncJackCapabilities = f3SyncJackCapabilities.setStatus('current')
f3EsmCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 38))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EsmCapabilities = f3EsmCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EsmCapabilities = f3EsmCapabilities.setStatus('current')
f3AMPClientCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 39))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AMPClientCapabilities = f3AMPClientCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AMPClientCapabilities = f3AMPClientCapabilities.setStatus('current')
f3AMPServerCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 40))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AMPServerCapabilities = f3AMPServerCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3AMPServerCapabilities = f3AMPServerCapabilities.setStatus('current')
f3Nid114HCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 41))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114HCapabilities = f3Nid114HCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114HCapabilities = f3Nid114HCapabilities.setStatus('current')
f3Nid114PHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 42))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114PHCapabilities = f3Nid114PHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114PHCapabilities = f3Nid114PHCapabilities.setStatus('current')
f3ERPCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 43))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ERPCapabilities = f3ERPCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ERPCapabilities = f3ERPCapabilities.setStatus('current')
f3ShgCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 44))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ShgCapabilities = f3ShgCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ShgCapabilities = f3ShgCapabilities.setStatus('current')
f3Nid114SCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 45))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114SCapabilities = f3Nid114SCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114SCapabilities = f3Nid114SCapabilities.setStatus('current')
f3Nid114SHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 46))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114SHCapabilities = f3Nid114SHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114SHCapabilities = f3Nid114SHCapabilities.setStatus('current')
f3Ipv6Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 47))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Ipv6Capabilities = f3Ipv6Capabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Ipv6Capabilities = f3Ipv6Capabilities.setStatus('current')
f3SatCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 48))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SatCapabilities = f3SatCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SatCapabilities = f3SatCapabilities.setStatus('current')
f3JdsuCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 49))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3JdsuCapabilities = f3JdsuCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3JdsuCapabilities = f3JdsuCapabilities.setStatus('current')
f3PortMirrorCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 50))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PortMirrorCapabilities = f3PortMirrorCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PortMirrorCapabilities = f3PortMirrorCapabilities.setStatus('current')
f3JdsuGeneratorCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 51))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3JdsuGeneratorCapabilities = f3JdsuGeneratorCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3JdsuGeneratorCapabilities = f3JdsuGeneratorCapabilities.setStatus('current')
f3TwampCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 52))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3TwampCapabilities = f3TwampCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3TwampCapabilities = f3TwampCapabilities.setStatus('current')
f3OspfCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 53))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OspfCapabilities = f3OspfCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OspfCapabilities = f3OspfCapabilities.setStatus('current')
f3Mef35Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 54))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Mef35Capabilities = f3Mef35Capabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Mef35Capabilities = f3Mef35Capabilities.setStatus('current')
f3Nid112ProCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 55))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProCapabilities = f3Nid112ProCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProCapabilities = f3Nid112ProCapabilities.setStatus('current')
f3Nid112ProMCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 56))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProMCapabilities = f3Nid112ProMCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProMCapabilities = f3Nid112ProMCapabilities.setStatus('current')
f3Nid114ProCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 57))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCapabilities = f3Nid114ProCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCapabilities = f3Nid114ProCapabilities.setStatus('current')
f3Nid114ProCCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 58))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCCapabilities = f3Nid114ProCCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCCapabilities = f3Nid114ProCCapabilities.setStatus('current')
f3Nid114ProSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 59))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProSHCapabilities = f3Nid114ProSHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProSHCapabilities = f3Nid114ProSHCapabilities.setStatus('current')
f3Nid114ProCSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 60))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCSHCapabilities = f3Nid114ProCSHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProCSHCapabilities = f3Nid114ProCSHCapabilities.setStatus('current')
f3Nid114ProHECapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 61))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProHECapabilities = f3Nid114ProHECapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProHECapabilities = f3Nid114ProHECapabilities.setStatus('current')
f3Nid112ProHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 62))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProHCapabilities = f3Nid112ProHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProHCapabilities = f3Nid112ProHCapabilities.setStatus('current')
f3ConnectGuardCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 63))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ConnectGuardCapabilities = f3ConnectGuardCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ConnectGuardCapabilities = f3ConnectGuardCapabilities.setStatus('current')
f3L3Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 64))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3Capabilities = f3L3Capabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3Capabilities = f3L3Capabilities.setStatus('current')
f3Nid114GCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 65))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114GCapabilities = f3Nid114GCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114GCapabilities = f3Nid114GCapabilities.setStatus('current')
f3BfdCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 66))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BfdCapabilities = f3BfdCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3BfdCapabilities = f3BfdCapabilities.setStatus('current')
f3EoMplsCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 67))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EoMplsCapabilities = f3EoMplsCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EoMplsCapabilities = f3EoMplsCapabilities.setStatus('current')
f3FpmCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 68))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FpmCapabilities = f3FpmCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FpmCapabilities = f3FpmCapabilities.setStatus('current')
f3Nid114ProVMHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 69))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMHCapabilities = f3Nid114ProVMHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMHCapabilities = f3Nid114ProVMHCapabilities.setStatus('current')
f3Nid114ProVMCHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 70))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMCHCapabilities = f3Nid114ProVMCHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMCHCapabilities = f3Nid114ProVMCHCapabilities.setStatus('current')
f3Nid114ProVMCSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 71))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMCSHCapabilities = f3Nid114ProVMCSHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMCSHCapabilities = f3Nid114ProVMCSHCapabilities.setStatus('current')
f3NidGe101ProCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 72))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGe101ProCapabilities = f3NidGe101ProCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGe101ProCapabilities = f3NidGe101ProCapabilities.setStatus('current')
f3NidGo102ProSCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 73))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSCapabilities = f3NidGo102ProSCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSCapabilities = f3NidGo102ProSCapabilities.setStatus('current')
f3NidGo102ProSPCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 74))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSPCapabilities = f3NidGo102ProSPCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSPCapabilities = f3NidGo102ProSPCapabilities.setStatus('current')
f3NidCx101Pro30ACapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 75))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidCx101Pro30ACapabilities = f3NidCx101Pro30ACapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidCx101Pro30ACapabilities = f3NidCx101Pro30ACapabilities.setStatus('current')
f3NidCx102Pro30ACapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 76))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidCx102Pro30ACapabilities = f3NidCx102Pro30ACapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidCx102Pro30ACapabilities = f3NidCx102Pro30ACapabilities.setStatus('current')
f3IpfixCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 77))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3IpfixCapabilities = f3IpfixCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3IpfixCapabilities = f3IpfixCapabilities.setStatus('current')
f3VxlanCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 78))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3VxlanCapabilities = f3VxlanCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3VxlanCapabilities = f3VxlanCapabilities.setStatus('current')
f3GreCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 79))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3GreCapabilities = f3GreCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3GreCapabilities = f3GreCapabilities.setStatus('current')
f3NtpCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 80))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NtpCapabilities = f3NtpCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NtpCapabilities = f3NtpCapabilities.setStatus('current')
f3ElpCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 81))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ElpCapabilities = f3ElpCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ElpCapabilities = f3ElpCapabilities.setStatus('current')
f3NidXG116PROCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 82))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG116PROCapabilities = f3NidXG116PROCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG116PROCapabilities = f3NidXG116PROCapabilities.setStatus('current')
f3NidXG120PROCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 83))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG120PROCapabilities = f3NidXG120PROCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG120PROCapabilities = f3NidXG120PROCapabilities.setStatus('current')
f3FacilityCapabilitiesXGPRO = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 84))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilitiesXGPRO = f3FacilityCapabilitiesXGPRO.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3FacilityCapabilitiesXGPRO = f3FacilityCapabilitiesXGPRO.setStatus('current')
f3EoMplsCapabilitiesXG = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 85))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EoMplsCapabilitiesXG = f3EoMplsCapabilitiesXG.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EoMplsCapabilitiesXG = f3EoMplsCapabilitiesXG.setStatus('current')
f3Nid112ProVMCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 86))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProVMCapabilities = f3Nid112ProVMCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid112ProVMCapabilities = f3Nid112ProVMCapabilities.setStatus('current')
f3SystemCommonCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 87))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SystemCommonCapabilities = f3SystemCommonCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3SystemCommonCapabilities = f3SystemCommonCapabilities.setStatus('current')
f3NidXG116PROHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 88))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG116PROHCapabilities = f3NidXG116PROHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG116PROHCapabilities = f3NidXG116PROHCapabilities.setStatus('current')
f3NidGo102ProSMCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 89))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSMCapabilities = f3NidGo102ProSMCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGo102ProSMCapabilities = f3NidGo102ProSMCapabilities.setStatus('current')
f3NidXG118PROSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 90))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG118PROSHCapabilities = f3NidXG118PROSHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG118PROSHCapabilities = f3NidXG118PROSHCapabilities.setStatus('current')
f3L3CapabilitiesGE = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 91))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3CapabilitiesGE = f3L3CapabilitiesGE.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3CapabilitiesGE = f3L3CapabilitiesGE.setStatus('current')
f3L3TrafficOSPFCapabilties = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 92))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficOSPFCapabilties = f3L3TrafficOSPFCapabilties.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficOSPFCapabilties = f3L3TrafficOSPFCapabilties.setStatus('current')
f3L3TrafficBGPCapabilties = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 93))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficBGPCapabilties = f3L3TrafficBGPCapabilties.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficBGPCapabilties = f3L3TrafficBGPCapabilties.setStatus('current')
f3L3TrafficIPv6Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 94))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficIPv6Capabilities = f3L3TrafficIPv6Capabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3L3TrafficIPv6Capabilities = f3L3TrafficIPv6Capabilities.setStatus('current')
f3NidXG118PROACSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 95))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG118PROACSHCapabilities = f3NidXG118PROACSHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG118PROACSHCapabilities = f3NidXG118PROACSHCapabilities.setStatus('current')
f3Nid114ProVMSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 96))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMSHCapabilities = f3Nid114ProVMSHCapabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Nid114ProVMSHCapabilities = f3Nid114ProVMSHCapabilities.setStatus('current')
f3NidGe104Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 97))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGe104Capabilities = f3NidGe104Capabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidGe104Capabilities = f3NidGe104Capabilities.setStatus('current')
f3NidXG120PROSHCapabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 98))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG120PROSHCapabilities = f3NidXG120PROSHCapabilities.setProductRelease('F3 - family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3NidXG120PROSHCapabilities = f3NidXG120PROSHCapabilities.setStatus('current')
f3Rfc2544Capabilities = AgentCapabilities((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 99))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Rfc2544Capabilities = f3Rfc2544Capabilities.setProductRelease('F3- family of products')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3Rfc2544Capabilities = f3Rfc2544Capabilities.setStatus('current')
mibBuilder.exportSymbols("F3-CAPABILITIES-MIB", f3TwampCapabilities=f3TwampCapabilities, f3Nid114SHCapabilities=f3Nid114SHCapabilities, f3Nid112Capabilities=f3Nid112Capabilities, f3NidXG118PROSHCapabilities=f3NidXG118PROSHCapabilities, f3VxlanCapabilities=f3VxlanCapabilities, f3NidXG118PROACSHCapabilities=f3NidXG118PROACSHCapabilities, f3SatCapabilities=f3SatCapabilities, f3BaseStandardsCapabilities=f3BaseStandardsCapabilities, f3ShgCapabilities=f3ShgCapabilities, f3SyncECapabilities=f3SyncECapabilities, f3Nid114ProVMCHCapabilities=f3Nid114ProVMCHCapabilities, f3NidGe101ProCapabilities=f3NidGe101ProCapabilities, f3Nid3204Capabilities=f3Nid3204Capabilities, f3Nid206FCapabilities=f3Nid206FCapabilities, f3PortMirrorCapabilities=f3PortMirrorCapabilities, f3Ipv6Capabilities=f3Ipv6Capabilities, f3Nid114ProCapabilities=f3Nid114ProCapabilities, f3LAGCapabilities=f3LAGCapabilities, f3Nid114ProHECapabilities=f3Nid114ProHECapabilities, f3SystemCommonCapabilities=f3SystemCommonCapabilities, f3BertCapabilities=f3BertCapabilities, f3EoMplsCapabilitiesXG=f3EoMplsCapabilitiesXG, f3BfdCapabilities=f3BfdCapabilities, f3StandardBridgeCapabilities=f3StandardBridgeCapabilities, f3Rfc2544Capabilities=f3Rfc2544Capabilities, f3PBBCapabilities=f3PBBCapabilities, f3Nid201SyncECapabilities=f3Nid201SyncECapabilities, f3CapabilityDefinitions=f3CapabilityDefinitions, f3EntityCmHubCapabilities=f3EntityCmHubCapabilities, f3ERPCapabilities=f3ERPCapabilities, f3PseudoWireCapabilities=f3PseudoWireCapabilities, f3NidGe104Capabilities=f3NidGe104Capabilities, f3StandardCfmCapabilities=f3StandardCfmCapabilities, f3L3Capabilities=f3L3Capabilities, f3Nid112ProVMCapabilities=f3Nid112ProVMCapabilities, f3Nid201NonSyncECapabilities=f3Nid201NonSyncECapabilities, f3NidXG210Capabilities=f3NidXG210Capabilities, f3NidGo102ProSPCapabilities=f3NidGo102ProSPCapabilities, f3ElpCapabilities=f3ElpCapabilities, f3Nid206VCapabilities=f3Nid206VCapabilities, f3Nid114ProCSHCapabilities=f3Nid114ProCSHCapabilities, f3AMPServerCapabilities=f3AMPServerCapabilities, f3Mef35Capabilities=f3Mef35Capabilities, f3FacilityCapabilitiesXGPRO=f3FacilityCapabilitiesXGPRO, f3Nid206Capabilities=f3Nid206Capabilities, f3L3TrafficOSPFCapabilties=f3L3TrafficOSPFCapabilties, f3NidGo102ProSCapabilities=f3NidGo102ProSCapabilities, f3CfmCapabilities=f3CfmCapabilities, f3AMPClientCapabilities=f3AMPClientCapabilities, f3IpfixCapabilities=f3IpfixCapabilities, f3CommonVendorSpecificCapabilities=f3CommonVendorSpecificCapabilities, f3NidXG116PROCapabilities=f3NidXG116PROCapabilities, f3GreCapabilities=f3GreCapabilities, f3Nid114ProVMHCapabilities=f3Nid114ProVMHCapabilities, f3Nid114ProVMSHCapabilities=f3Nid114ProVMSHCapabilities, f3L3TrafficIPv6Capabilities=f3L3TrafficIPv6Capabilities, f3Nid114ProCCapabilities=f3Nid114ProCCapabilities, f3Nid114Capabilities=f3Nid114Capabilities, f3Nid114HCapabilities=f3Nid114HCapabilities, f3CommonVendorSpecificCapabilitiesCmHub=f3CommonVendorSpecificCapabilitiesCmHub, f3SonetCapabilities=f3SonetCapabilities, f3L3CapabilitiesGE=f3L3CapabilitiesGE, f3OspfCapabilities=f3OspfCapabilities, f3NidCx101Pro30ACapabilities=f3NidCx101Pro30ACapabilities, f3Nid112ProMCapabilities=f3Nid112ProMCapabilities, f3CapabilityMIB=f3CapabilityMIB, f3Nid112ProHCapabilities=f3Nid112ProHCapabilities, f3FpmCapabilities=f3FpmCapabilities, f3Nid1804Capabilities=f3Nid1804Capabilities, f3JdsuCapabilities=f3JdsuCapabilities, f3NidXG120PROSHCapabilities=f3NidXG120PROSHCapabilities, f3Nid114ProVMCSHCapabilities=f3Nid114ProVMCSHCapabilities, f3SyncJackCapabilities=f3SyncJackCapabilities, f3NtpCapabilities=f3NtpCapabilities, f3Nid112ProCapabilities=f3Nid112ProCapabilities, f3PtpCapabilities=f3PtpCapabilities, f3Nid114ProSHCapabilities=f3Nid114ProSHCapabilities, f3EsmCapabilities=f3EsmCapabilities, f3EsaCapabilities=f3EsaCapabilities, f3DS1Capabilities=f3DS1Capabilities, f3Nid114SCapabilities=f3Nid114SCapabilities, f3Nid114PHCapabilities=f3Nid114PHCapabilities, f3JdsuGeneratorCapabilities=f3JdsuGeneratorCapabilities, f3L3TrafficBGPCapabilties=f3L3TrafficBGPCapabilties, f3FacilityCapabilitiesCmHub=f3FacilityCapabilitiesCmHub, f3FacilityCapabilities=f3FacilityCapabilities, PYSNMP_MODULE_ID=f3CapabilityMIB, f3ConnectGuardCapabilities=f3ConnectGuardCapabilities, f3NidXG116PROHCapabilities=f3NidXG116PROHCapabilities, f3Nid114GCapabilities=f3Nid114GCapabilities, f3EoMplsCapabilities=f3EoMplsCapabilities, f3StandardTargetNotifCapabilities=f3StandardTargetNotifCapabilities, f3NidGo102ProSMCapabilities=f3NidGo102ProSMCapabilities, f3EcpaCapabilities=f3EcpaCapabilities, f3StandardRMONCapabilities=f3StandardRMONCapabilities, f3NidCx102Pro30ACapabilities=f3NidCx102Pro30ACapabilities, f3StandardSecurityCapabilities=f3StandardSecurityCapabilities, f3NidXG120PROCapabilities=f3NidXG120PROCapabilities, f3StandardLAGCapabilities=f3StandardLAGCapabilities, f3StandardIfEntityCapabilities=f3StandardIfEntityCapabilities, f3NidSyncProbeCapabilities=f3NidSyncProbeCapabilities, f3BridgeCapabilitiesCmHub=f3BridgeCapabilitiesCmHub)
