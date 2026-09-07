#
# PySNMP MIB module CISCO-WDS-IDS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WDS-IDS-CAPABILITY
# Source digest sha256:e923ce07113d6f6613e04a08011a39121154fe60ed45362df471bb63eafedebb
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWdsidsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 424))
if mibBuilder.loadTexts: ciscoWdsidsCapability.setLastUpdated('2005-01-13 00:00')
if mibBuilder.loadTexts: ciscoWdsidsCapability.setOrganization('Cisco Systems, Inc.')
ciscoWdsidsCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 424, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsidsCapabilityV1 = ciscoWdsidsCapabilityV1.setProductRelease('Cisco IOS 12.3(4) JA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWdsidsCapabilityV1 = ciscoWdsidsCapabilityV1.setStatus('current')
mibBuilder.exportSymbols("CISCO-WDS-IDS-CAPABILITY", PYSNMP_MODULE_ID=ciscoWdsidsCapability, ciscoWdsidsCapability=ciscoWdsidsCapability, ciscoWdsidsCapabilityV1=ciscoWdsidsCapabilityV1)
