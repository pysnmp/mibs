#
# PySNMP MIB module CISCO-SP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SP-CAPABILITY
# Source digest sha256:2547c18af7f94bb7eeae9eba118332b3da18a9538ab03196fa1d4086251c88a8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cSpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 189))
cSpCapability.setRevisions(('2001-06-06 00:00',))
if mibBuilder.loadTexts: cSpCapability.setLastUpdated('2001-06-06 00:00')
if mibBuilder.loadTexts: cSpCapability.setOrganization('Cisco Systems, Inc.')
cSpCapabilityV12R021MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 189, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSpCapabilityV12R021MB1 = cSpCapabilityV12R021MB1.setProductRelease('Cisco IOS 12.2(1)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSpCapabilityV12R021MB1 = cSpCapabilityV12R021MB1.setStatus('current')
mibBuilder.exportSymbols("CISCO-SP-CAPABILITY", PYSNMP_MODULE_ID=cSpCapability, cSpCapability=cSpCapability, cSpCapabilityV12R021MB1=cSpCapabilityV12R021MB1)
