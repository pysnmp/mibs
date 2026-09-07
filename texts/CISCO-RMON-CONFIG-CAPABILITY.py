#
# PySNMP MIB module CISCO-RMON-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-RMON-CONFIG-CAPABILITY
# Source digest sha256:0b4235dc8d65d4187ac400789fbb8d61b21f2fb72cf349c7387f785f35cca65b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRmonConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 346))
ciscoRmonConfigCapability.setRevisions(('2008-10-28 00:00', '2008-05-09 00:00', '2007-06-28 00:00', '2006-01-18 00:00', '2005-08-24 10:00', '2004-03-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRmonConfigCapability.setRevisionsDescriptions(('Added capability statement\n        crcCapV12R0233SXIPCat6K.', 'Added capability statement\n        ciscoRmonConfigCapDCOS.', 'Added capability statement\n        crcCapV12R0233SXHPCat6k.', 'Added capability statements\n        crcCapV12R0218SXDPCat6k and\n        crcCapV12R0218SXEPCat6k.', 'Added capability statement\n        ciscoRmonConfigCapCatOSV08R0501.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRmonConfigCapability.setLastUpdated('2008-10-28 00:00')
if mibBuilder.loadTexts: ciscoRmonConfigCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRmonConfigCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRmonConfigCapability.setDescription('The capabilities description of CISCO-RMON-CONFIG-MIB.')
ciscoRmonConfigCapV12R0111ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapV12R0111ECat6K = ciscoRmonConfigCapV12R0111ECat6K.setProductRelease('Cisco IOS 12.1(11E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapV12R0111ECat6K = ciscoRmonConfigCapV12R0111ECat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoRmonConfigCapV12R0111ECat6K.setDescription('CISCO-RMON-CONFIG-MIB capabilities.')
ciscoRmonConfigCapCatOSV6R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV6R0301 = ciscoRmonConfigCapCatOSV6R0301.setProductRelease('Cisco CatOS 6.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV6R0301 = ciscoRmonConfigCapCatOSV6R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoRmonConfigCapCatOSV6R0301.setDescription('CISCO-RMON-CONFIG-MIB capabilities.')
ciscoRmonConfigCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV08R0501 = ciscoRmonConfigCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapCatOSV08R0501 = ciscoRmonConfigCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoRmonConfigCapCatOSV08R0501.setDescription('CISCO-RMON-CONFIG-MIB capabilities.')
crcCapV12R0218SXDPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXDPCat6k = crcCapV12R0218SXDPCat6k.setProductRelease('Cisco IOS 12.2(18)SXD on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXDPCat6k = crcCapV12R0218SXDPCat6k.setStatus('current')
if mibBuilder.loadTexts: crcCapV12R0218SXDPCat6k.setDescription('CISCO-RMON-CONFIG-MIB capabilities.')
crcCapV12R0218SXEPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXEPCat6k = crcCapV12R0218SXEPCat6k.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0218SXEPCat6k = crcCapV12R0218SXEPCat6k.setStatus('current')
if mibBuilder.loadTexts: crcCapV12R0218SXEPCat6k.setDescription('CISCO-RMON-CONFIG-MIB capabilities.')
crcCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXHPCat6k = crcCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXHPCat6k = crcCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: crcCapV12R0233SXHPCat6k.setDescription('CISCO-RMON-CONFIG-MIB capabilities.')
ciscoRmonConfigCapSanOSV34R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapSanOSV34R1 = ciscoRmonConfigCapSanOSV34R1.setProductRelease('Cisco SanOS 3.4(1) on MDS9000 Storage Switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonConfigCapSanOSV34R1 = ciscoRmonConfigCapSanOSV34R1.setStatus('current')
if mibBuilder.loadTexts: ciscoRmonConfigCapSanOSV34R1.setDescription('CISCO-RMON-CONFIG-MIB capabilities.')
crcCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 346, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXIPCat6K = crcCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crcCapV12R0233SXIPCat6K = crcCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: crcCapV12R0233SXIPCat6K.setDescription('CISCO-RMON-CONFIG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RMON-CONFIG-CAPABILITY", PYSNMP_MODULE_ID=ciscoRmonConfigCapability, ciscoRmonConfigCapCatOSV08R0501=ciscoRmonConfigCapCatOSV08R0501, ciscoRmonConfigCapCatOSV6R0301=ciscoRmonConfigCapCatOSV6R0301, ciscoRmonConfigCapSanOSV34R1=ciscoRmonConfigCapSanOSV34R1, ciscoRmonConfigCapV12R0111ECat6K=ciscoRmonConfigCapV12R0111ECat6K, ciscoRmonConfigCapability=ciscoRmonConfigCapability, crcCapV12R0218SXDPCat6k=crcCapV12R0218SXDPCat6k, crcCapV12R0218SXEPCat6k=crcCapV12R0218SXEPCat6k, crcCapV12R0233SXHPCat6k=crcCapV12R0233SXHPCat6k, crcCapV12R0233SXIPCat6K=crcCapV12R0233SXIPCat6K)
