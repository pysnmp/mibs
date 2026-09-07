#
# PySNMP MIB module CISCO-SWITCH-STATS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SWITCH-STATS-CAPABILITY
# Source digest sha256:7247d48279d14db71d1f2eae97105c89db5264fbd53597a1cfef0aec19a84a36
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchStatsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 600))
ciscoSwitchStatsCapability.setRevisions(('2013-09-25 00:00', '2013-07-26 00:00', '2010-11-11 00:00',))
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setLastUpdated('2013-09-25 00:00')
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setOrganization('Cisco Systems, Inc.')
csstCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV12R0250SYPCat6kPfc4 = csstCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV12R0250SYPCat6kPfc4 = csstCapV12R0250SYPCat6kPfc4.setStatus('current')
csstCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0104PN7k = csstCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0104PN7k = csstCapNxOSV06R0104PN7k.setStatus('current')
csstCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0201PMds = csstCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0201PMds = csstCapNxOSV06R0201PMds.setStatus('current')
csstCapV15R0102SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc4 = csstCapV15R0102SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc4 = csstCapV15R0102SYPCat6kPfc4.setStatus('current')
csstCapV15R0102SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc3 = csstCapV15R0102SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc3 = csstCapV15R0102SYPCat6kPfc3.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-STATS-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchStatsCapability, ciscoSwitchStatsCapability=ciscoSwitchStatsCapability, csstCapNxOSV06R0104PN7k=csstCapNxOSV06R0104PN7k, csstCapNxOSV06R0201PMds=csstCapNxOSV06R0201PMds, csstCapV12R0250SYPCat6kPfc4=csstCapV12R0250SYPCat6kPfc4, csstCapV15R0102SYPCat6kPfc3=csstCapV15R0102SYPCat6kPfc3, csstCapV15R0102SYPCat6kPfc4=csstCapV15R0102SYPCat6kPfc4)
