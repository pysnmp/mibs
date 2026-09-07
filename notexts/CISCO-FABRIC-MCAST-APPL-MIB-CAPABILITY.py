#
# PySNMP MIB module CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY
# Source digest sha256:34e30b1c21c0be9c1224e5760bd3a1afdd3b693d0f34e3530f6b2dd74094388b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricMcastApplCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 510))
ciscoFabricMcastApplCapability.setRevisions(('2006-06-12 00:00',))
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setLastUpdated('2006-06-12 00:00')
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setOrganization('Cisco Systems, Inc.')
cfmaCapabilityIOSXRV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 510, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmaCapabilityIOSXRV3R03 = cfmaCapabilityIOSXRV3R03.setProductRelease('Cisco IOS XR 3.3 on CRS-1 ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmaCapabilityIOSXRV3R03 = cfmaCapabilityIOSXRV3R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoFabricMcastApplCapability, cfmaCapabilityIOSXRV3R03=cfmaCapabilityIOSXRV3R03, ciscoFabricMcastApplCapability=ciscoFabricMcastApplCapability)
