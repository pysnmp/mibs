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
if mibBuilder.loadTexts: ciscoDs3Capability.setLastUpdated('2004-05-06 00:00')
if mibBuilder.loadTexts: ciscoDs3Capability.setOrganization('Cisco Systems, Inc.')
ciscoDs3CapabilityV2R0100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV2R0100 = ciscoDs3CapabilityV2R0100.setProductRelease('MGX8850 Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV2R0100 = ciscoDs3CapabilityV2R0100.setStatus('current')
ciscoDs3CapabilitySrmV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilitySrmV3R00 = ciscoDs3CapabilitySrmV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilitySrmV3R00 = ciscoDs3CapabilitySrmV3R00.setStatus('current')
ciscoDs3CapabilityPxm1eV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityPxm1eV3R00 = ciscoDs3CapabilityPxm1eV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityPxm1eV3R00 = ciscoDs3CapabilityPxm1eV3R00.setStatus('current')
ciscoDs3CapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV4R00 = ciscoDs3CapabilityV4R00.setProductRelease('MGX8950 and MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV4R00 = ciscoDs3CapabilityV4R00.setStatus('current')
ciscoDs3CapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 265, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV5R00 = ciscoDs3CapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3CapabilityV5R00 = ciscoDs3CapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS3-CAPABILITY", PYSNMP_MODULE_ID=ciscoDs3Capability, ciscoDs3Capability=ciscoDs3Capability, ciscoDs3CapabilityPxm1eV3R00=ciscoDs3CapabilityPxm1eV3R00, ciscoDs3CapabilitySrmV3R00=ciscoDs3CapabilitySrmV3R00, ciscoDs3CapabilityV2R0100=ciscoDs3CapabilityV2R0100, ciscoDs3CapabilityV4R00=ciscoDs3CapabilityV4R00, ciscoDs3CapabilityV5R00=ciscoDs3CapabilityV5R00)
