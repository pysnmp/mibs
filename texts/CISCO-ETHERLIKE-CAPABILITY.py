#
# PySNMP MIB module CISCO-ETHERLIKE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ETHERLIKE-CAPABILITY
# Source digest sha256:57e0c80446b060267c4acbb74e747ce50db93f98dab958a12362b319a052fe77
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEtherlikeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 130))
ciscoEtherlikeCapability.setRevisions(('2011-04-01 00:00', '2010-10-29 00:00', '2010-03-17 00:00', '2007-07-03 00:00', '2003-09-08 00:00', '2000-01-21 14:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEtherlikeCapability.setRevisionsDescriptions(('Added capability statement\n        cEtherlikeCapV15R0002SGPCat4K', 'Added capability statement\n        cEtherlikeCapV12R0250SYPCat6K.', 'Added capability statement\n        cEtherlikeCapV12R0233SXI4PCat6K.', 'Added capability statement\n        cEtherlikeCapV12R0233SXHPCat6k.', 'Added ciscoEtherlikeCapV12R0111bEX\n        for IOS 12.1(11b)EX on Catalyst 6000/6500 and\n        Cisco 7600 series devices.\n\n        Added ciscoEtherlikeCapV12R0214SX \n        for IOS 12.2(14)SX on Catalyst 6000/6500 and\n        Cisco 7600 series devices.\n\n        Added ciscoEtherlikeCapV08R0101 for Cisco CatOS\n        8.1(1).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEtherlikeCapability.setLastUpdated('2011-04-01 00:00')
if mibBuilder.loadTexts: ciscoEtherlikeCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEtherlikeCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ethermibs@cisco.com\n            cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEtherlikeCapability.setDescription('Agent capabilities for EtherLike-MIB.')
ciscoEtherlikeCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 130, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherlikeCapabilityV12R01 = ciscoEtherlikeCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherlikeCapabilityV12R01 = ciscoEtherlikeCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoEtherlikeCapabilityV12R01.setDescription('IOS 12.1 Ethernet MIB capabilities.')
ciscoEtherlikeCapV12R0111bEX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 130, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherlikeCapV12R0111bEX = ciscoEtherlikeCapV12R0111bEX.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherlikeCapV12R0111bEX = ciscoEtherlikeCapV12R0111bEX.setStatus('current')
if mibBuilder.loadTexts: ciscoEtherlikeCapV12R0111bEX.setDescription('EtherLike-MIB capabilities')
ciscoEtherlikeCapV12R0214SX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 130, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherlikeCapV12R0214SX = ciscoEtherlikeCapV12R0214SX.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherlikeCapV12R0214SX = ciscoEtherlikeCapV12R0214SX.setStatus('current')
if mibBuilder.loadTexts: ciscoEtherlikeCapV12R0214SX.setDescription('EtherLike-MIB capabilities.')
ciscoEtherlikeCapV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 130, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherlikeCapV08R0101 = ciscoEtherlikeCapV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherlikeCapV08R0101 = ciscoEtherlikeCapV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoEtherlikeCapV08R0101.setDescription('EtherLike-MIB capabilities')
cEtherlikeCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 130, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEtherlikeCapV12R0233SXHPCat6k = cEtherlikeCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEtherlikeCapV12R0233SXHPCat6k = cEtherlikeCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cEtherlikeCapV12R0233SXHPCat6k.setDescription('EtherLike-MIB capabilities.')
cEtherlikeCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 130, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEtherlikeCapV12R0233SXI4PCat6K = cEtherlikeCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEtherlikeCapV12R0233SXI4PCat6K = cEtherlikeCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: cEtherlikeCapV12R0233SXI4PCat6K.setDescription('EtherLike-MIB capabilities.')
cEtherlikeCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 130, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEtherlikeCapV12R0250SYPCat6K = cEtherlikeCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEtherlikeCapV12R0250SYPCat6K = cEtherlikeCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cEtherlikeCapV12R0250SYPCat6K.setDescription('EtherLike-MIB capabilities.')
cEtherlikeCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 130, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEtherlikeCapV15R0002SGPCat4K = cEtherlikeCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEtherlikeCapV15R0002SGPCat4K = cEtherlikeCapV15R0002SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cEtherlikeCapV15R0002SGPCat4K.setDescription('EtherLike-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ETHERLIKE-CAPABILITY", PYSNMP_MODULE_ID=ciscoEtherlikeCapability, cEtherlikeCapV12R0233SXHPCat6k=cEtherlikeCapV12R0233SXHPCat6k, cEtherlikeCapV12R0233SXI4PCat6K=cEtherlikeCapV12R0233SXI4PCat6K, cEtherlikeCapV12R0250SYPCat6K=cEtherlikeCapV12R0250SYPCat6K, cEtherlikeCapV15R0002SGPCat4K=cEtherlikeCapV15R0002SGPCat4K, ciscoEtherlikeCapV08R0101=ciscoEtherlikeCapV08R0101, ciscoEtherlikeCapV12R0111bEX=ciscoEtherlikeCapV12R0111bEX, ciscoEtherlikeCapV12R0214SX=ciscoEtherlikeCapV12R0214SX, ciscoEtherlikeCapability=ciscoEtherlikeCapability, ciscoEtherlikeCapabilityV12R01=ciscoEtherlikeCapabilityV12R01)
