#
# PySNMP MIB module CISCO-ITP-SP2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-SP2-CAPABILITY
# Source digest sha256:783a439f97ab435057d88d375ee657d9b3f51d4810e2b2f95c458c6061c1e2ba
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpSp2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 272))
ciscoItpSp2Capability.setRevisions(('2002-06-05 00:00',))
if mibBuilder.loadTexts: ciscoItpSp2Capability.setLastUpdated('2002-06-05 00:00')
if mibBuilder.loadTexts: ciscoItpSp2Capability.setOrganization('Cisco Systems, Inc.')
ciscoItpSp2CapabilityV12R0204MB4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 272, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSp2CapabilityV12R0204MB4 = ciscoItpSp2CapabilityV12R0204MB4.setProductRelease('Cisco IOS 12.2(4)MB4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSp2CapabilityV12R0204MB4 = ciscoItpSp2CapabilityV12R0204MB4.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-SP2-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpSp2Capability, ciscoItpSp2Capability=ciscoItpSp2Capability, ciscoItpSp2CapabilityV12R0204MB4=ciscoItpSp2CapabilityV12R0204MB4)
