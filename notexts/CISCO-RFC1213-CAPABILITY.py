#
# PySNMP MIB module CISCO-RFC1213-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-RFC1213-CAPABILITY
# Source digest sha256:9ce82d261a7b315b00c8287f1d213b336645cfacf0f10002df0004fefa995614
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRFC1213Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 101))
ciscoRFC1213Capability.setRevisions(('2003-10-27 16:00', '2001-09-08 16:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRFC1213Capability.setLastUpdated('2003-10-27 16:00')
if mibBuilder.loadTexts: ciscoRFC1213Capability.setOrganization('Cisco Systems, Inc.')
ciscoRFC1213CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV10R02 = ciscoRFC1213CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV10R02 = ciscoRFC1213CapabilityV10R02.setStatus('current')
ciscoRFC1213CapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R02 = ciscoRFC1213CapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R02 = ciscoRFC1213CapabilityV12R02.setStatus('current')
ciscoRFC1213CapabilityV12R00S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R00S = ciscoRFC1213CapabilityV12R00S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R00S = ciscoRFC1213CapabilityV12R00S.setStatus('current')
ciscoRFC1213CapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R01 = ciscoRFC1213CapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R01 = ciscoRFC1213CapabilityV12R01.setStatus('current')
ciscoRFC1213CapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapCatOSV08R0101 = ciscoRFC1213CapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapCatOSV08R0101 = ciscoRFC1213CapCatOSV08R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-RFC1213-CAPABILITY", PYSNMP_MODULE_ID=ciscoRFC1213Capability, ciscoRFC1213CapCatOSV08R0101=ciscoRFC1213CapCatOSV08R0101, ciscoRFC1213Capability=ciscoRFC1213Capability, ciscoRFC1213CapabilityV10R02=ciscoRFC1213CapabilityV10R02, ciscoRFC1213CapabilityV12R00S=ciscoRFC1213CapabilityV12R00S, ciscoRFC1213CapabilityV12R01=ciscoRFC1213CapabilityV12R01, ciscoRFC1213CapabilityV12R02=ciscoRFC1213CapabilityV12R02)
