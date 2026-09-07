#
# PySNMP MIB module CISCO-L2-TUNNEL-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-L2-TUNNEL-CONFIG-CAPABILITY
# Source digest sha256:97ec5d38827443586bd3a3679d7a79ac3b84d5c2c03531b3fe9cbed80c371eb4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL2TunnelConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 334))
ciscoL2TunnelConfigCapability.setRevisions(('2010-05-14 00:00', '2008-10-27 00:00', '2007-07-09 00:00', '2005-07-05 00:00', '2004-06-21 00:00', '2003-08-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL2TunnelConfigCapability.setRevisionsDescriptions(('Added capability statement\n        cL2TunnelConfigCapV12R0254SGPCat4K.', 'Added capability statement\n        cL2TunnelConfigCapV12R0233SXIPCat6K.', 'Added capability statement\n        cL2TunnelConfigCapV12R0233SXHPCat6k.', 'Added capability statement\n        cL2TunConfCapCatOSV08R0501.', 'Added capability statement\n        cL2TunConfCapCatOSV08R0401Cat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoL2TunnelConfigCapability.setLastUpdated('2010-05-14 00:00')
if mibBuilder.loadTexts: ciscoL2TunnelConfigCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoL2TunnelConfigCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com,\n            cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoL2TunnelConfigCapability.setDescription('The capabilities description of\n        CISCO-L2-TUNNEL-CONFIG-MIB.')
cL2TunConfCapCatOSV07R0501Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV07R0501Cat6k = cL2TunConfCapCatOSV07R0501Cat6k.setProductRelease('Cisco CatOS 7.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV07R0501Cat6k = cL2TunConfCapCatOSV07R0501Cat6k.setStatus('current')
if mibBuilder.loadTexts: cL2TunConfCapCatOSV07R0501Cat6k.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunnelConfigCapV12R0214SX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0214SX = cL2TunnelConfigCapV12R0214SX.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0214SX = cL2TunnelConfigCapV12R0214SX.setStatus('current')
if mibBuilder.loadTexts: cL2TunnelConfigCapV12R0214SX.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunConfCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV08R0401 = cL2TunConfCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV08R0401 = cL2TunConfCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: cL2TunConfCapCatOSV08R0401.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunConfCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV08R0501 = cL2TunConfCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunConfCapCatOSV08R0501 = cL2TunConfCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: cL2TunConfCapCatOSV08R0501.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunnelConfigCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0233SXHPCat6k = cL2TunnelConfigCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0233SXHPCat6k = cL2TunnelConfigCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cL2TunnelConfigCapV12R0233SXHPCat6k.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunnelConfigCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0233SXIPCat6K = cL2TunnelConfigCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0233SXIPCat6K = cL2TunnelConfigCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cL2TunnelConfigCapV12R0233SXIPCat6K.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
cL2TunnelConfigCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 334, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0254SGPCat4K = cL2TunnelConfigCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches,\n                    except LAN Base images.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL2TunnelConfigCapV12R0254SGPCat4K = cL2TunnelConfigCapV12R0254SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cL2TunnelConfigCapV12R0254SGPCat4K.setDescription('CISCO-L2-TUNNEL-CONFIG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-L2-TUNNEL-CONFIG-CAPABILITY", PYSNMP_MODULE_ID=ciscoL2TunnelConfigCapability, cL2TunConfCapCatOSV07R0501Cat6k=cL2TunConfCapCatOSV07R0501Cat6k, cL2TunConfCapCatOSV08R0401=cL2TunConfCapCatOSV08R0401, cL2TunConfCapCatOSV08R0501=cL2TunConfCapCatOSV08R0501, cL2TunnelConfigCapV12R0214SX=cL2TunnelConfigCapV12R0214SX, cL2TunnelConfigCapV12R0233SXHPCat6k=cL2TunnelConfigCapV12R0233SXHPCat6k, cL2TunnelConfigCapV12R0233SXIPCat6K=cL2TunnelConfigCapV12R0233SXIPCat6K, cL2TunnelConfigCapV12R0254SGPCat4K=cL2TunnelConfigCapV12R0254SGPCat4K, ciscoL2TunnelConfigCapability=ciscoL2TunnelConfigCapability)
