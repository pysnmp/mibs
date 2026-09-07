#
# PySNMP MIB module CISCO-SWITCH-ENGINE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SWITCH-ENGINE-CAPABILITY
# Source digest sha256:34b9320dac30757146e9722220a65b2cf6ab5896c23dffe3676d6a073e6d2ead
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchEngineCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 343))
ciscoSwitchEngineCapability.setRevisions(('2013-07-25 00:00', '2012-09-10 00:00', '2011-09-28 00:00', '2010-11-11 00:00', '2010-03-22 00:00', '2008-10-30 00:00', '2007-07-16 00:00', '2005-09-16 00:00', '2005-08-24 00:00', '2004-12-22 00:00', '2004-06-14 00:00', '2004-01-15 00:00', '2003-12-04 00:00', '2003-08-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchEngineCapability.setRevisionsDescriptions(('Added capability statement cseCapNxOSV06R0104PN7k.', 'Added capability statement\n        cseCapV15R0101SYPCat6kPfc3,\n        cseCapV15R0101SYPCat6kPfc4.', 'Added capability statement\n        cseCapV15R0001SYPCat6kPfc4.', 'Added capability statement\n        cseCapV12R0250SYPCat6KPfc4.', 'Added capability statement cseCapV12R0233SXI4PCat6K.', 'Added capability statement\n        cseCapV12R0233SXIPCat6K.\n\n        Added the following missing groups to \n        previous releases:\n            cse4kVlanGroup\n            cseNDEReportGroup\n            cseCefAdjacencyEncapGroup\n            cseCefAdjacencyMTUGroup', 'Added capability statement\n        cseCapV12R0233SXHPCat6K.', 'Added capability statement\n        cseCapV12R0218SXGPCat6K.\n\n        Added variation for cseFlowIPFlowMask to\n        cseCapV12R0119ECat6KPfc,\n        cseCapV12R0119ECat6KPfc2,\n        cseCapV12R0217SXCat6KPfc3 and\n        cseCapV12R0218SXEPCat6K.', 'Added capability statement\n        cseCapCatOSV08R0501PCat6KPfc3\n\n        Added variation for cseFlowIPFlowMask to \n        cseCapCatOSV08R0101Cat6KPfc,\n        cseCapCatOSV08R0101Cat6KPfc2,\n        cseCapCatOSV08R0101Cat6KPfc3,\n        cseCapCatOSV08R0301Cat6KPfc2,\n        cseCapCatOSV08R0301Cat6KPfc3 and\n        cseCapCatOSV08R0401Cat6KPfc3.', 'Added capability statement\n        cseCapV12R0218SXEPCat6K.', 'Added capability statement\n        cseCapCatOSV08R0401Cat6KPfc3.', 'Added capability statement cseCapCatOSV08R0301Cat6KPfc2\n        and cseCapCatOSV08R0301Cat6KPfc3.', 'Fixed description for cseCapV12R0217SXCat6KPfc3\n        to match actual product release and added\n        cseTcamUsageGroup to the INCLUDES section.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchEngineCapability.setLastUpdated('2013-07-25 00:00')
if mibBuilder.loadTexts: ciscoSwitchEngineCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchEngineCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchEngineCapability.setDescription('The agent capabilities description of\n        CISCO-SWITCH-ENGINE-MIB.')
cseCapCatOSV08R0101Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc = cseCapCatOSV08R0101Cat6KPfc.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                    series devices with PFC card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc = cseCapCatOSV08R0101Cat6KPfc.setStatus('current')
if mibBuilder.loadTexts: cseCapCatOSV08R0101Cat6KPfc.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapCatOSV08R0101Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc2 = cseCapCatOSV08R0101Cat6KPfc2.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc2 = cseCapCatOSV08R0101Cat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: cseCapCatOSV08R0101Cat6KPfc2.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapCatOSV08R0101Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc3 = cseCapCatOSV08R0101Cat6KPfc3.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc3 = cseCapCatOSV08R0101Cat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: cseCapCatOSV08R0101Cat6KPfc3.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapV12R0119ECat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0119ECat6KPfc = cseCapV12R0119ECat6KPfc.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                    series devices with PFC card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0119ECat6KPfc = cseCapV12R0119ECat6KPfc.setStatus('current')
if mibBuilder.loadTexts: cseCapV12R0119ECat6KPfc.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapV12R0119ECat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0119ECat6KPfc2 = cseCapV12R0119ECat6KPfc2.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0119ECat6KPfc2 = cseCapV12R0119ECat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: cseCapV12R0119ECat6KPfc2.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapV12R0217SXCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0217SXCat6KPfc3 = cseCapV12R0217SXCat6KPfc3.setProductRelease('Cisco IOS 12.2(17SX) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0217SXCat6KPfc3 = cseCapV12R0217SXCat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: cseCapV12R0217SXCat6KPfc3.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapCatOSV08R0301Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0301Cat6KPfc2 = cseCapCatOSV08R0301Cat6KPfc2.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0301Cat6KPfc2 = cseCapCatOSV08R0301Cat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: cseCapCatOSV08R0301Cat6KPfc2.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapCatOSV08R0301Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0301Cat6KPfc3 = cseCapCatOSV08R0301Cat6KPfc3.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0301Cat6KPfc3 = cseCapCatOSV08R0301Cat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: cseCapCatOSV08R0301Cat6KPfc3.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapCatOSV08R0401Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0401Cat6KPfc3 = cseCapCatOSV08R0401Cat6KPfc3.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0401Cat6KPfc3 = cseCapCatOSV08R0401Cat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: cseCapCatOSV08R0401Cat6KPfc3.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapV12R0218SXEPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0218SXEPCat6K = cseCapV12R0218SXEPCat6K.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0218SXEPCat6K = cseCapV12R0218SXEPCat6K.setStatus('current')
if mibBuilder.loadTexts: cseCapV12R0218SXEPCat6K.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapCatOSV08R0501PCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0501PCat6KPfc3 = cseCapCatOSV08R0501PCat6KPfc3.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0501PCat6KPfc3 = cseCapCatOSV08R0501PCat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: cseCapCatOSV08R0501PCat6KPfc3.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXHPCat6K = cseCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXHPCat6K = cseCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: cseCapV12R0233SXHPCat6K.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXIPCat6K = cseCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXIPCat6K = cseCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cseCapV12R0233SXIPCat6K.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXI4PCat6K = cseCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXI4PCat6K = cseCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: cseCapV12R0233SXI4PCat6K.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapV12R0250SYPCat6KPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0250SYPCat6KPfc4 = cseCapV12R0250SYPCat6KPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices for PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0250SYPCat6KPfc4 = cseCapV12R0250SYPCat6KPfc4.setStatus('current')
if mibBuilder.loadTexts: cseCapV12R0250SYPCat6KPfc4.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapV15R0001SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0001SYPCat6kPfc4 = cseCapV15R0001SYPCat6kPfc4.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices for PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0001SYPCat6kPfc4 = cseCapV15R0001SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: cseCapV15R0001SYPCat6kPfc4.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0101SYPCat6kPfc3 = cseCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0101SYPCat6kPfc3 = cseCapV15R0101SYPCat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: cseCapV15R0101SYPCat6kPfc3.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapV15R0101SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0101SYPCat6kPfc4 = cseCapV15R0101SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices for PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0101SYPCat6kPfc4 = cseCapV15R0101SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: cseCapV15R0101SYPCat6kPfc4.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
cseCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapNxOSV06R0104PN7k = cseCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapNxOSV06R0104PN7k = cseCapNxOSV06R0104PN7k.setStatus('current')
if mibBuilder.loadTexts: cseCapNxOSV06R0104PN7k.setDescription('CISCO-SWITCH-ENGINE-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-ENGINE-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchEngineCapability, ciscoSwitchEngineCapability=ciscoSwitchEngineCapability, cseCapCatOSV08R0101Cat6KPfc2=cseCapCatOSV08R0101Cat6KPfc2, cseCapCatOSV08R0101Cat6KPfc3=cseCapCatOSV08R0101Cat6KPfc3, cseCapCatOSV08R0101Cat6KPfc=cseCapCatOSV08R0101Cat6KPfc, cseCapCatOSV08R0301Cat6KPfc2=cseCapCatOSV08R0301Cat6KPfc2, cseCapCatOSV08R0301Cat6KPfc3=cseCapCatOSV08R0301Cat6KPfc3, cseCapCatOSV08R0401Cat6KPfc3=cseCapCatOSV08R0401Cat6KPfc3, cseCapCatOSV08R0501PCat6KPfc3=cseCapCatOSV08R0501PCat6KPfc3, cseCapNxOSV06R0104PN7k=cseCapNxOSV06R0104PN7k, cseCapV12R0119ECat6KPfc2=cseCapV12R0119ECat6KPfc2, cseCapV12R0119ECat6KPfc=cseCapV12R0119ECat6KPfc, cseCapV12R0217SXCat6KPfc3=cseCapV12R0217SXCat6KPfc3, cseCapV12R0218SXEPCat6K=cseCapV12R0218SXEPCat6K, cseCapV12R0233SXHPCat6K=cseCapV12R0233SXHPCat6K, cseCapV12R0233SXI4PCat6K=cseCapV12R0233SXI4PCat6K, cseCapV12R0233SXIPCat6K=cseCapV12R0233SXIPCat6K, cseCapV12R0250SYPCat6KPfc4=cseCapV12R0250SYPCat6KPfc4, cseCapV15R0001SYPCat6kPfc4=cseCapV15R0001SYPCat6kPfc4, cseCapV15R0101SYPCat6kPfc3=cseCapV15R0101SYPCat6kPfc3, cseCapV15R0101SYPCat6kPfc4=cseCapV15R0101SYPCat6kPfc4)
