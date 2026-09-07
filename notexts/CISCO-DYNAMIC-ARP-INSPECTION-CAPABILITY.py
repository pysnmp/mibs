#
# PySNMP MIB module CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY
# Source digest sha256:62a1236d12b317a5cfec3ce1576b4928302f8fa724a250203415d8198e291838
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoDynamicArpInspCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 382))
ciscoDynamicArpInspCapability.setRevisions(('2011-03-24 00:00', '2010-05-07 00:00', '2007-07-02 00:00', '2004-01-13 00:00',))
if mibBuilder.loadTexts: ciscoDynamicArpInspCapability.setLastUpdated('2011-03-24 00:00')
if mibBuilder.loadTexts: ciscoDynamicArpInspCapability.setOrganization('Cisco Systems, Inc.')
cdaiCapabilityCatOSV08R0301Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapabilityCatOSV08R0301Cat6k = cdaiCapabilityCatOSV08R0301Cat6k.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapabilityCatOSV08R0301Cat6k = cdaiCapabilityCatOSV08R0301Cat6k.setStatus('current')
cdaiCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0233SXHPCat6k = cdaiCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0233SXHPCat6k = cdaiCapV12R0233SXHPCat6k.setStatus('current')
cdaiCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0254SGPCat4K = cdaiCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV12R0254SGPCat4K = cdaiCapV12R0254SGPCat4K.setStatus('current')
cdaiCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 382, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV15R0002SGPCat4K = cdaiCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdaiCapV15R0002SGPCat4K = cdaiCapV15R0002SGPCat4K.setStatus('current')
mibBuilder.exportSymbols("CISCO-DYNAMIC-ARP-INSPECTION-CAPABILITY", PYSNMP_MODULE_ID=ciscoDynamicArpInspCapability, cdaiCapV12R0233SXHPCat6k=cdaiCapV12R0233SXHPCat6k, cdaiCapV12R0254SGPCat4K=cdaiCapV12R0254SGPCat4K, cdaiCapV15R0002SGPCat4K=cdaiCapV15R0002SGPCat4K, cdaiCapabilityCatOSV08R0301Cat6k=cdaiCapabilityCatOSV08R0301Cat6k, ciscoDynamicArpInspCapability=ciscoDynamicArpInspCapability)
