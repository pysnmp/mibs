#
# PySNMP MIB module CISCO-PORT-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PORT-QOS-CAPABILITY
# Source digest sha256:419263430bdfa161ba8aea3e2bed5756f12b31513f7595751bae5a16b85aa7bd
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPortQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 209))
ciscoPortQosCapability.setRevisions(('2008-09-25 00:00', '2001-02-05 00:00',))
if mibBuilder.loadTexts: ciscoPortQosCapability.setLastUpdated('2008-09-25 00:00')
if mibBuilder.loadTexts: ciscoPortQosCapability.setOrganization('Cisco Systems, Inc.')
ciscoPortQosCapabilityCat2948gL3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 209, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityCat2948gL3 = ciscoPortQosCapabilityCat2948gL3.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityCat2948gL3 = ciscoPortQosCapabilityCat2948gL3.setStatus('current')
ciscoPortQosCapabilityV12R0250SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 209, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityV12R0250SE = ciscoPortQosCapabilityV12R0250SE.setProductRelease('Cisco IOS 12.2(50)SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortQosCapabilityV12R0250SE = ciscoPortQosCapabilityV12R0250SE.setStatus('current')
mibBuilder.exportSymbols("CISCO-PORT-QOS-CAPABILITY", PYSNMP_MODULE_ID=ciscoPortQosCapability, ciscoPortQosCapability=ciscoPortQosCapability, ciscoPortQosCapabilityCat2948gL3=ciscoPortQosCapabilityCat2948gL3, ciscoPortQosCapabilityV12R0250SE=ciscoPortQosCapabilityV12R0250SE)
