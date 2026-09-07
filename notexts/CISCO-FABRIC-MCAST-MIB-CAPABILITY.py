#
# PySNMP MIB module CISCO-FABRIC-MCAST-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-FABRIC-MCAST-MIB-CAPABILITY
# Source digest sha256:79086fa60af2c292e3eca91574ab7048b8d8b4ff1e8f438c663f426c7c6a1815
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricMcastCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 509))
ciscoFabricMcastCapability.setRevisions(('2006-06-12 00:00',))
if mibBuilder.loadTexts: ciscoFabricMcastCapability.setLastUpdated('2006-06-12 00:00')
if mibBuilder.loadTexts: ciscoFabricMcastCapability.setOrganization('Cisco Systems, Inc.')
cfmCapabilityIOSXRV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 509, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmCapabilityIOSXRV3R03 = cfmCapabilityIOSXRV3R03.setProductRelease('Cisco IOS XR 3.3 on CRS-1 ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmCapabilityIOSXRV3R03 = cfmCapabilityIOSXRV3R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-FABRIC-MCAST-MIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoFabricMcastCapability, cfmCapabilityIOSXRV3R03=cfmCapabilityIOSXRV3R03, ciscoFabricMcastCapability=ciscoFabricMcastCapability)
