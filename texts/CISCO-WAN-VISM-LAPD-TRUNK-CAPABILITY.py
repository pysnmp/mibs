#
# PySNMP MIB module CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY
# Source digest sha256:8f7f64914ee7c34cc77f4af22d0ebd16eaed1d92e43ccab10aa470e9aa4f94b5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwVismLapdTrunkCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 336))
cwVismLapdTrunkCapability.setRevisions(('2001-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setLastUpdated('2001-08-22 00:00')
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: cwVismLapdTrunkCapability.setDescription('The Agent Capabilities for CISCO-WAN-LAPD-TRUNK-MIB.')
cwVismLapdTrunkCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 336, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismLapdTrunkCapabilityV2R00 = cwVismLapdTrunkCapabilityV2R00.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismLapdTrunkCapabilityV2R00 = cwVismLapdTrunkCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: cwVismLapdTrunkCapabilityV2R00.setDescription('CISCO-WAN-LAPD-TRUNK-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-LAPD-TRUNK-CAPABILITY", PYSNMP_MODULE_ID=cwVismLapdTrunkCapability, cwVismLapdTrunkCapability=cwVismLapdTrunkCapability, cwVismLapdTrunkCapabilityV2R00=cwVismLapdTrunkCapabilityV2R00)
