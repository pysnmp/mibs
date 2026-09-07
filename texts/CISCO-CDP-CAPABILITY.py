#
# PySNMP MIB module CISCO-CDP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CDP-CAPABILITY
# Source digest sha256:fb32eac50eab107cf7275f644a6764ad3a3f76e9ed7e9770c575c7450c8c5fe2
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCdpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 43))
ciscoCdpCapability.setRevisions(('2007-07-18 00:00', '2006-10-26 00:00', '2006-02-06 00:00', '2005-05-24 00:00', '2003-09-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCdpCapability.setRevisionsDescriptions(('Added capability statement ciscoCdpCapV12R0233SXHPCat6K.', 'Added capability for Cisco TelePresence System (CTS) and\n        Cisco TelePresence Manager (CTM) platforms.', 'Added capability for IOS-XR 2.0 CRS-1.', 'Added capability for MDS platform.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCdpCapability.setLastUpdated('2007-07-18 00:00')
if mibBuilder.loadTexts: ciscoCdpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCdpCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCdpCapability.setDescription('The capabilities description of CISCO-CDP-MIB.')
ciscoCdpCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0111bEXCat6K = ciscoCdpCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0111bEXCat6K = ciscoCdpCapV12R0111bEXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapV12R0111bEXCat6K.setDescription('CISCO-CDP-MIB capabilities.')
ciscoCdpCapV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0217SXCat6K = ciscoCdpCapV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n\n                     and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0217SXCat6K = ciscoCdpCapV12R0217SXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapV12R0217SXCat6K.setDescription('CISCO-CDP-MIB capabilities.')
ciscoCdpCapCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat6K = ciscoCdpCapCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n\n                     and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat6K = ciscoCdpCapCatOSV08R0101Cat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapCatOSV08R0101Cat6K.setDescription('CISCO-CDP-MIB capabilities.')
ciscoCdpCapCatOSV08R0101Cat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat4K = ciscoCdpCapCatOSV08R0101Cat4K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 4000 series\n\n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCatOSV08R0101Cat4K = ciscoCdpCapCatOSV08R0101Cat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapCatOSV08R0101Cat4K.setDescription('CISCO-CDP-MIB capabilities.')
ciscoCdpCapSanOSV03R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapSanOSV03R0001 = ciscoCdpCapSanOSV03R0001.setProductRelease('Cisco SAN-OS 3.0(1) on MDS platform.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapSanOSV03R0001 = ciscoCdpCapSanOSV03R0001.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapSanOSV03R0001.setDescription('CISCO-CDP-MIB capabilities.')
ciscoCdpCapIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapIOSXRV2R0CRS1 = ciscoCdpCapIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapIOSXRV2R0CRS1 = ciscoCdpCapIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapIOSXRV2R0CRS1.setDescription('CISCO-CDP-MIB capabilities for\n        IOS XR release 2.0')
ciscoCdpCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTSV100 = ciscoCdpCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTSV100 = ciscoCdpCapCTSV100.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapCTSV100.setDescription('CISCO-CDP-MIB capabilities for CTS 1.0.0')
ciscoCdpCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTMV1000 = ciscoCdpCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapCTMV1000 = ciscoCdpCapCTMV1000.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapCTMV1000.setDescription('CISCO-CDP-MIB capabilities for CTM 1.0.0.0')
ciscoCdpCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 43, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0233SXHPCat6K = ciscoCdpCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500 \n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCapV12R0233SXHPCat6K = ciscoCdpCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoCdpCapV12R0233SXHPCat6K.setDescription('CISCO-CDP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CDP-CAPABILITY", PYSNMP_MODULE_ID=ciscoCdpCapability, ciscoCdpCapCTMV1000=ciscoCdpCapCTMV1000, ciscoCdpCapCTSV100=ciscoCdpCapCTSV100, ciscoCdpCapCatOSV08R0101Cat4K=ciscoCdpCapCatOSV08R0101Cat4K, ciscoCdpCapCatOSV08R0101Cat6K=ciscoCdpCapCatOSV08R0101Cat6K, ciscoCdpCapIOSXRV2R0CRS1=ciscoCdpCapIOSXRV2R0CRS1, ciscoCdpCapSanOSV03R0001=ciscoCdpCapSanOSV03R0001, ciscoCdpCapV12R0111bEXCat6K=ciscoCdpCapV12R0111bEXCat6K, ciscoCdpCapV12R0217SXCat6K=ciscoCdpCapV12R0217SXCat6K, ciscoCdpCapV12R0233SXHPCat6K=ciscoCdpCapV12R0233SXHPCat6K, ciscoCdpCapability=ciscoCdpCapability)
