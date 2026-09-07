#
# PySNMP MIB module CISCO-DS3-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DS3-CAPABILITY
# Source digest sha256:ac42ef0b308a0a96c398debcbb24e9af8e9e288ecb499cc66f6666e1a8eb6814
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDs3Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 265))
ciscoDs3Capability.setRevisions(('2004-05-06 00:00', '2003-12-22 00:00', '2003-03-12 00:00', '2002-05-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDs3Capability.setRevisionsDescriptions(('Modified MPSM agent capability description.', 'Added ciscoDs3CapabilityV5R00.', 'Added ciscoDs3CapabilityV4R00 for modules:\n             10 Gig. ATM Switch Service Module(AXSM-XG),\n             AXSM Service Module Enhanced(AXSM-E) and \n             Processor Switch Module Enhanced(PXM1E)\n             controller card.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDs3Capability.setLastUpdated('2004-05-06 00:00')
if mibBuilder.loadTexts: ciscoDs3Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDs3Capability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoDs3Capability.setDescription('The Agent Capabilities for DS3-MIB(RFC 2496).')
ciscoDs3CapabilityV2R0100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV2R0100 = ciscoDs3CapabilityV2R0100.setProductRelease('MGX8850 Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV2R0100 = ciscoDs3CapabilityV2R0100.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3CapabilityV2R0100.setDescription('DS3 MIB Capabilities for Following Modules:\n                ATM Switch Service Module(AXSM).\n                AXSM-E(AXSM Enhanced).')
ciscoDs3CapabilitySrmV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilitySrmV3R00 = ciscoDs3CapabilitySrmV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilitySrmV3R00 = ciscoDs3CapabilitySrmV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3CapabilitySrmV3R00.setDescription('DS3 MIB Capabilities for\n                Service Resource Module(SRM).')
ciscoDs3CapabilityPxm1eV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityPxm1eV3R00 = ciscoDs3CapabilityPxm1eV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityPxm1eV3R00 = ciscoDs3CapabilityPxm1eV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3CapabilityPxm1eV3R00.setDescription('DS3 MIB Capabilities for\n                 Processor Switch Module Enhanced (PXM1E)\n                 controller card.')
ciscoDs3CapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV4R00 = ciscoDs3CapabilityV4R00.setProductRelease('MGX8950 and MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV4R00 = ciscoDs3CapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3CapabilityV4R00.setDescription('DS3 MIB Capabilities for Modules:\n                10 Gig. ATM Switch Service Module(AXSM-XG),\n                AXSM Service Module Enhanced(AXSM-E) and \n                Processor Switch Module Enhanced(PXM1E)\n                controller card.')
ciscoDs3CapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV5R00 = ciscoDs3CapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV5R00 = ciscoDs3CapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3CapabilityV5R00.setDescription('DS3 MIB capabilities for Voice Switch \n                 Service Module(VXSM) and MPSM in release\n                 5.0.0')
mibBuilder.exportSymbols("CISCO-DS3-CAPABILITY", PYSNMP_MODULE_ID=ciscoDs3Capability, ciscoDs3Capability=ciscoDs3Capability, ciscoDs3CapabilityPxm1eV3R00=ciscoDs3CapabilityPxm1eV3R00, ciscoDs3CapabilitySrmV3R00=ciscoDs3CapabilitySrmV3R00, ciscoDs3CapabilityV2R0100=ciscoDs3CapabilityV2R0100, ciscoDs3CapabilityV4R00=ciscoDs3CapabilityV4R00, ciscoDs3CapabilityV5R00=ciscoDs3CapabilityV5R00)
