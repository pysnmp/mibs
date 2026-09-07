#
# PySNMP MIB module CISCO-DHCP-SNOOPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DHCP-SNOOPING-CAPABILITY
# Source digest sha256:6a3123b8e1c460b890fc9519381c5c10a9565898ed34ddd99403c8f8dc7bab91
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoDhcpSnoopingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 383))
ciscoDhcpSnoopingCapability.setRevisions(('2011-09-28 00:00', '2010-10-27 00:00', '2010-03-18 00:00', '2008-03-20 00:00', '2007-07-02 09:00', '2006-06-28 00:00', '2004-03-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDhcpSnoopingCapability.setRevisionsDescriptions(('Added capability statement cdsCapV15R0001SYPCat6k.', 'Added capability statement cdsCapV12R0250SYPCat6k.', 'Added capability statement cdsCapV12R0233SXI4PCat6k.\n\n        Added VARIATION clause for cdsStaticBindingsStatus in \n        capability statement cdsCapV12R0233SXHPCat6k.', 'Added capability statements\n        cdsCapabilityV08R0701Cat6kPfc and\n        cdsCapabilityV08R0701Cat6kPfc3.', 'Added capability statements\n        cdsCapV12R0233SXHPCat6k.', 'Added capability statements\n        cdsCapabilityV08R0601Cat6kPfc and\n        cdsCapabilityV08R0601Cat6kPfc3.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDhcpSnoopingCapability.setLastUpdated('2011-09-28 00:00')
if mibBuilder.loadTexts: ciscoDhcpSnoopingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDhcpSnoopingCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoDhcpSnoopingCapability.setDescription('The capabilities description of\n        CISCO-DHCP-SNOOPING-MIB.')
cdsCapabilityV08R0301Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc = cdsCapabilityV08R0301Cat6kPfc.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC\n                          of PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc = cdsCapabilityV08R0301Cat6kPfc.setStatus('current')
if mibBuilder.loadTexts: cdsCapabilityV08R0301Cat6kPfc.setDescription('CISCO-DHCP-SNOOPING-MIB capabilities.')
cdsCapabilityV08R0301Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc3 = cdsCapabilityV08R0301Cat6kPfc3.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC3\n                          card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0301Cat6kPfc3 = cdsCapabilityV08R0301Cat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: cdsCapabilityV08R0301Cat6kPfc3.setDescription('CISCO-DHCP-SNOOPING-MIB capabilities.')
cdsCapabilityV08R0601Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc = cdsCapabilityV08R0601Cat6kPfc.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC\n                          or PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc = cdsCapabilityV08R0601Cat6kPfc.setStatus('current')
if mibBuilder.loadTexts: cdsCapabilityV08R0601Cat6kPfc.setDescription('CISCO-DHCP-SNOOPING-MIB capabilities.')
cdsCapabilityV08R0601Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc3 = cdsCapabilityV08R0601Cat6kPfc3.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC3\n                          card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0601Cat6kPfc3 = cdsCapabilityV08R0601Cat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: cdsCapabilityV08R0601Cat6kPfc3.setDescription('CISCO-DHCP-SNOOPING-MIB capabilities.')
cdsCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXHPCat6k = cdsCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXHPCat6k = cdsCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cdsCapV12R0233SXHPCat6k.setDescription('CISCO-DHCP-SNOOPING-MIB capabilities.')
cdsCapabilityV08R0701Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc = cdsCapabilityV08R0701Cat6kPfc.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC\n                          or PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc = cdsCapabilityV08R0701Cat6kPfc.setStatus('current')
if mibBuilder.loadTexts: cdsCapabilityV08R0701Cat6kPfc.setDescription('CISCO-DHCP-SNOOPING-MIB capabilities.')
cdsCapabilityV08R0701Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc3 = cdsCapabilityV08R0701Cat6kPfc3.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices with PFC3\n                          card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapabilityV08R0701Cat6kPfc3 = cdsCapabilityV08R0701Cat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: cdsCapabilityV08R0701Cat6kPfc3.setDescription('CISCO-DHCP-SNOOPING-MIB capabilities.')
cdsCapV12R0233SXI4PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXI4PCat6k = cdsCapV12R0233SXI4PCat6k.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0233SXI4PCat6k = cdsCapV12R0233SXI4PCat6k.setStatus('current')
if mibBuilder.loadTexts: cdsCapV12R0233SXI4PCat6k.setDescription('CISCO-DHCP-SNOOPING-MIB capabilities.')
cdsCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0250SYPCat6k = cdsCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV12R0250SYPCat6k = cdsCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: cdsCapV12R0250SYPCat6k.setDescription('CISCO-DHCP-SNOOPING-MIB capabilities.')
cdsCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 383, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV15R0001SYPCat6k = cdsCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdsCapV15R0001SYPCat6k = cdsCapV15R0001SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: cdsCapV15R0001SYPCat6k.setDescription('CISCO-DHCP-SNOOPING-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-DHCP-SNOOPING-CAPABILITY", PYSNMP_MODULE_ID=ciscoDhcpSnoopingCapability, cdsCapV12R0233SXHPCat6k=cdsCapV12R0233SXHPCat6k, cdsCapV12R0233SXI4PCat6k=cdsCapV12R0233SXI4PCat6k, cdsCapV12R0250SYPCat6k=cdsCapV12R0250SYPCat6k, cdsCapV15R0001SYPCat6k=cdsCapV15R0001SYPCat6k, cdsCapabilityV08R0301Cat6kPfc3=cdsCapabilityV08R0301Cat6kPfc3, cdsCapabilityV08R0301Cat6kPfc=cdsCapabilityV08R0301Cat6kPfc, cdsCapabilityV08R0601Cat6kPfc3=cdsCapabilityV08R0601Cat6kPfc3, cdsCapabilityV08R0601Cat6kPfc=cdsCapabilityV08R0601Cat6kPfc, cdsCapabilityV08R0701Cat6kPfc3=cdsCapabilityV08R0701Cat6kPfc3, cdsCapabilityV08R0701Cat6kPfc=cdsCapabilityV08R0701Cat6kPfc, ciscoDhcpSnoopingCapability=ciscoDhcpSnoopingCapability)
