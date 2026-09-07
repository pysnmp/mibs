#
# PySNMP MIB module CISCO-IMAGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IMAGE-CAPABILITY
# Source digest sha256:9043296d94c36e8ba9584cac5682c9cb2f9271c07e8204255a8e400afa611f29
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImageMIBCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 580))
ciscoImageMIBCapability.setRevisions(('2009-03-26 00:00', '2003-09-15 00:00', '1995-01-25 00:00',))
if mibBuilder.loadTexts: ciscoImageMIBCapability.setLastUpdated('2009-03-26 00:00')
if mibBuilder.loadTexts: ciscoImageMIBCapability.setOrganization('Cisco Systems, Inc.')
ciscoImageMIBCapabilityV10R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCapabilityV10R01 = ciscoImageMIBCapabilityV10R01.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCapabilityV10R01 = ciscoImageMIBCapabilityV10R01.setStatus('current')
ciscoImageCapabilityV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0119ECat6K = ciscoImageCapabilityV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0119ECat6K = ciscoImageCapabilityV12R0119ECat6K.setStatus('current')
ciscoImageCapabilityV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0217SXCat6K = ciscoImageCapabilityV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17SX) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0217SXCat6K = ciscoImageCapabilityV12R0217SXCat6K.setStatus('current')
ciscoImageCapabilityCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityCatOSV08R0101 = ciscoImageCapabilityCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityCatOSV08R0101 = ciscoImageCapabilityCatOSV08R0101.setStatus('current')
ciscoImageCapabilityGssV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityGssV03R01 = ciscoImageCapabilityGssV03R01.setProductRelease('Global Site Selector(GSS) 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityGssV03R01 = ciscoImageCapabilityGssV03R01.setStatus('current')
mibBuilder.exportSymbols("CISCO-IMAGE-CAPABILITY", PYSNMP_MODULE_ID=ciscoImageMIBCapability, ciscoImageCapabilityCatOSV08R0101=ciscoImageCapabilityCatOSV08R0101, ciscoImageCapabilityGssV03R01=ciscoImageCapabilityGssV03R01, ciscoImageCapabilityV12R0119ECat6K=ciscoImageCapabilityV12R0119ECat6K, ciscoImageCapabilityV12R0217SXCat6K=ciscoImageCapabilityV12R0217SXCat6K, ciscoImageMIBCapability=ciscoImageMIBCapability, ciscoImageMIBCapabilityV10R01=ciscoImageMIBCapabilityV10R01)
