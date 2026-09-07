#
# PySNMP MIB module CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY
# Source digest sha256:3bb8714133123e2f8d6964156b764179d7315076ebdbbfaeef6de7f569246426
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cSwitchHwCapacityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 572))
cSwitchHwCapacityCapability.setRevisions(('2014-03-03 00:01', '2013-07-26 00:01', '2013-07-16 00:01', '2011-09-28 00:01', '2008-10-29 00:00',))
if mibBuilder.loadTexts: cSwitchHwCapacityCapability.setLastUpdated('2014-03-03 00:01')
if mibBuilder.loadTexts: cSwitchHwCapacityCapability.setOrganization('Cisco Systems, Inc.')
cSwitchHwCapacityCapV12R0233SXIPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV12R0233SXIPCat6k = cSwitchHwCapacityCapV12R0233SXIPCat6k.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV12R0233SXIPCat6k = cSwitchHwCapacityCapV12R0233SXIPCat6k.setStatus('current')
cSwitchHwCapacityCapV15R0001SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV15R0001SYPCat6kSup2T = cSwitchHwCapacityCapV15R0001SYPCat6kSup2T.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                         series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapV15R0001SYPCat6kSup2T = cSwitchHwCapacityCapV15R0001SYPCat6kSup2T.setStatus('current')
cSwitchHwCapacityCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0104PN7k = cSwitchHwCapacityCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0104PN7k = cSwitchHwCapacityCapNxOSV06R0104PN7k.setStatus('current')
cSwitchHwCapacityCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0202PN7k = cSwitchHwCapacityCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0202PN7k = cSwitchHwCapacityCapNxOSV06R0202PN7k.setStatus('current')
cSwitchHwCapacityCapNxOSV06R0208PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 572, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0208PN7k = cSwitchHwCapacityCapNxOSV06R0208PN7k.setProductRelease('Cisco NX-OS 6.2(8) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSwitchHwCapacityCapNxOSV06R0208PN7k = cSwitchHwCapacityCapNxOSV06R0208PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-HARDWARE-CAPACITY-CAPABILITY", PYSNMP_MODULE_ID=cSwitchHwCapacityCapability, cSwitchHwCapacityCapNxOSV06R0104PN7k=cSwitchHwCapacityCapNxOSV06R0104PN7k, cSwitchHwCapacityCapNxOSV06R0202PN7k=cSwitchHwCapacityCapNxOSV06R0202PN7k, cSwitchHwCapacityCapNxOSV06R0208PN7k=cSwitchHwCapacityCapNxOSV06R0208PN7k, cSwitchHwCapacityCapV12R0233SXIPCat6k=cSwitchHwCapacityCapV12R0233SXIPCat6k, cSwitchHwCapacityCapV15R0001SYPCat6kSup2T=cSwitchHwCapacityCapV15R0001SYPCat6kSup2T, cSwitchHwCapacityCapability=cSwitchHwCapacityCapability)
