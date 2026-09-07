#
# PySNMP MIB module CISCO-SWITCH-MULTICAST-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SWITCH-MULTICAST-CAPABILITY
# Source digest sha256:252a379be2c6207dfc746ae1fbbbe64c06d1f26091e7b92ea74c34b8c8a33bd8
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
ciscoSwitchMulticastCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 546))
ciscoSwitchMulticastCapability.setRevisions(('2010-11-11 00:00', '2008-10-30 00:00', '2007-07-16 00:00',))
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setLastUpdated('2010-11-11 00:00')
if mibBuilder.loadTexts: ciscoSwitchMulticastCapability.setOrganization('Cisco Systems, Inc.')
cswmCapabilityV12R0219SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0219SXHPCat6k = cswmCapabilityV12R0219SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0219SXHPCat6k = cswmCapabilityV12R0219SXHPCat6k.setStatus('current')
cswmCapabilityV12R0233SXIPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0233SXIPCat6k = cswmCapabilityV12R0233SXIPCat6k.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0233SXIPCat6k = cswmCapabilityV12R0233SXIPCat6k.setStatus('current')
cswmCapabilityV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 546, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0250SYPCat6kPfc4 = cswmCapabilityV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cswmCapabilityV12R0250SYPCat6kPfc4 = cswmCapabilityV12R0250SYPCat6kPfc4.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-MULTICAST-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchMulticastCapability, ciscoSwitchMulticastCapability=ciscoSwitchMulticastCapability, cswmCapabilityV12R0219SXHPCat6k=cswmCapabilityV12R0219SXHPCat6k, cswmCapabilityV12R0233SXIPCat6k=cswmCapabilityV12R0233SXIPCat6k, cswmCapabilityV12R0250SYPCat6kPfc4=cswmCapabilityV12R0250SYPCat6kPfc4)
