#
# PySNMP MIB module CISCO-RF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-RF-CAPABILITY
# Source digest sha256:e5ae73e0d7b78cf7b8c0ed58d4c23ea870f43c9b4159e45440c47d1da03b23fe
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRFCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoRFCapability.setRevisions(('2003-08-20 00:00', '2001-01-04 10:00',))
if mibBuilder.loadTexts: ciscoRFCapability.setLastUpdated('2003-08-20 00:00')
if mibBuilder.loadTexts: ciscoRFCapability.setOrganization('Cisco Systems, Inc.')
ciscoRFCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R01 = ciscoRFCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R01 = ciscoRFCapabilityV12R01.setStatus('current')
ciscoRFCapabilityV12R0111bEXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0111bEXCat6k = ciscoRFCapabilityV12R0111bEXCat6k.setProductRelease('Cisco IOS 12.1(11bEX) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0111bEXCat6k = ciscoRFCapabilityV12R0111bEXCat6k.setStatus('current')
ciscoRFCapabilityV12R0113ECat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0113ECat6k = ciscoRFCapabilityV12R0113ECat6k.setProductRelease('Cisco IOS 12.1(13E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityV12R0113ECat6k = ciscoRFCapabilityV12R0113ECat6k.setStatus('current')
ciscoRFCapabilityCatOSV8R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityCatOSV8R0101Cat6K = ciscoRFCapabilityCatOSV8R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFCapabilityCatOSV8R0101Cat6K = ciscoRFCapabilityCatOSV8R0101Cat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-RF-CAPABILITY", PYSNMP_MODULE_ID=ciscoRFCapability, ciscoRFCapability=ciscoRFCapability, ciscoRFCapabilityCatOSV8R0101Cat6K=ciscoRFCapabilityCatOSV8R0101Cat6K, ciscoRFCapabilityV12R0111bEXCat6k=ciscoRFCapabilityV12R0111bEXCat6k, ciscoRFCapabilityV12R0113ECat6k=ciscoRFCapabilityV12R0113ECat6k, ciscoRFCapabilityV12R01=ciscoRFCapabilityV12R01)
