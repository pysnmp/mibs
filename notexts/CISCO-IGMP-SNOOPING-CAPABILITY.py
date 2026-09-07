#
# PySNMP MIB module CISCO-IGMP-SNOOPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IGMP-SNOOPING-CAPABILITY
# Source digest sha256:56d4601cd4b59677968dc1534499590899021d59591964770f4ce4f24ad94a56
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoIgmpSnoopingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 320))
ciscoIgmpSnoopingCapability.setRevisions(('2012-09-12 00:00', '2010-11-16 00:00', '2008-10-31 00:00', '2004-03-10 00:00', '2003-08-13 00:00',))
if mibBuilder.loadTexts: ciscoIgmpSnoopingCapability.setLastUpdated('2012-09-12 00:00')
if mibBuilder.loadTexts: ciscoIgmpSnoopingCapability.setOrganization('Cisco Systems, Inc.')
cisCapCatOSV08R0101Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc = cisCapCatOSV08R0101Cat6kPfc.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc = cisCapCatOSV08R0101Cat6kPfc.setStatus('current')
cisCapCatOSV08R0101Cat6kPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc2 = cisCapCatOSV08R0101Cat6kPfc2.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc2 = cisCapCatOSV08R0101Cat6kPfc2.setStatus('current')
cisCapCatOSV08R0101Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc3 = cisCapCatOSV08R0101Cat6kPfc3.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc3 = cisCapCatOSV08R0101Cat6kPfc3.setStatus('current')
cisCapCatOSV08R0301Cat6kPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc2 = cisCapCatOSV08R0301Cat6kPfc2.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc2 = cisCapCatOSV08R0301Cat6kPfc2.setStatus('current')
cisCapCatOSV08R0301Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc3 = cisCapCatOSV08R0301Cat6kPfc3.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc3 = cisCapCatOSV08R0301Cat6kPfc3.setStatus('current')
cisCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0233SXIPCat6K = cisCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0233SXIPCat6K = cisCapV12R0233SXIPCat6K.setStatus('current')
cisCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0250SYPCat6K = cisCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0250SYPCat6K = cisCapV12R0250SYPCat6K.setStatus('current')
cisCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc3 = cisCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc3 = cisCapV15R0101SYPCat6kPfc3.setStatus('current')
cisCapV15R0101SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc4 = cisCapV15R0101SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc4 = cisCapV15R0101SYPCat6kPfc4.setStatus('current')
mibBuilder.exportSymbols("CISCO-IGMP-SNOOPING-CAPABILITY", PYSNMP_MODULE_ID=ciscoIgmpSnoopingCapability, cisCapCatOSV08R0101Cat6kPfc2=cisCapCatOSV08R0101Cat6kPfc2, cisCapCatOSV08R0101Cat6kPfc3=cisCapCatOSV08R0101Cat6kPfc3, cisCapCatOSV08R0101Cat6kPfc=cisCapCatOSV08R0101Cat6kPfc, cisCapCatOSV08R0301Cat6kPfc2=cisCapCatOSV08R0301Cat6kPfc2, cisCapCatOSV08R0301Cat6kPfc3=cisCapCatOSV08R0301Cat6kPfc3, cisCapV12R0233SXIPCat6K=cisCapV12R0233SXIPCat6K, cisCapV12R0250SYPCat6K=cisCapV12R0250SYPCat6K, cisCapV15R0101SYPCat6kPfc3=cisCapV15R0101SYPCat6kPfc3, cisCapV15R0101SYPCat6kPfc4=cisCapV15R0101SYPCat6kPfc4, ciscoIgmpSnoopingCapability=ciscoIgmpSnoopingCapability)
