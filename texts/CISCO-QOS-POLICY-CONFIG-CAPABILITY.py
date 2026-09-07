#
# PySNMP MIB module CISCO-QOS-POLICY-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-QOS-POLICY-CONFIG-CAPABILITY
# Source digest sha256:519b89ffcc44718854b0f670abd7eab7fa80a21cb3b5649104bf6265167498e0
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoQosPolicyConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 363))
ciscoQosPolicyConfigCapability.setRevisions(('2007-06-28 00:00', '2003-10-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setRevisionsDescriptions(('Add cqpcCapabilityV12R0233SXHPCat6k statement.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setLastUpdated('2007-06-28 00:00')
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoQosPolicyConfigCapability.setDescription('The Agent capabilities for CISCO-QOS-POLICY-CONFIG-MIB')
cqpcCapabilityCatOSV08R0101Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 363, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityCatOSV08R0101Cat6k = cqpcCapabilityCatOSV08R0101Cat6k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityCatOSV08R0101Cat6k = cqpcCapabilityCatOSV08R0101Cat6k.setStatus('current')
if mibBuilder.loadTexts: cqpcCapabilityCatOSV08R0101Cat6k.setDescription('CISCO-QOS-POLICY-CONFIG-MIB capabilities.')
cqpcCapabilityV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 363, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityV12R0233SXHPCat6k = cqpcCapabilityV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cqpcCapabilityV12R0233SXHPCat6k = cqpcCapabilityV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cqpcCapabilityV12R0233SXHPCat6k.setDescription('CISCO-QOS-POLICY-CONFIG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-QOS-POLICY-CONFIG-CAPABILITY", PYSNMP_MODULE_ID=ciscoQosPolicyConfigCapability, ciscoQosPolicyConfigCapability=ciscoQosPolicyConfigCapability, cqpcCapabilityCatOSV08R0101Cat6k=cqpcCapabilityCatOSV08R0101Cat6k, cqpcCapabilityV12R0233SXHPCat6k=cqpcCapabilityV12R0233SXHPCat6k)
