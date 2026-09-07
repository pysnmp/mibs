#
# PySNMP MIB module CISCO-MIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MIP-CAPABILITY
# Source digest sha256:452d8bd09889c6dba4804bf1d8b00a921512bbbb47ff7c296eb5c4613be7e1d4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMIPCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 203))
ciscoMIPCapability.setRevisions(('2003-12-24 00:00', '2002-10-08 00:00', '2000-11-17 00:00',))
if mibBuilder.loadTexts: ciscoMIPCapability.setLastUpdated('2003-12-24 00:00')
if mibBuilder.loadTexts: ciscoMIPCapability.setOrganization('Cisco Systems, Inc.')
ciscoMIPCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R02 = ciscoMIPCapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R02 = ciscoMIPCapabilityV12R02.setStatus('current')
ciscoMIPCapabilityV12R0204T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0204T = ciscoMIPCapabilityV12R0204T.setProductRelease('Cisco IOS 12.2(4)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0204T = ciscoMIPCapabilityV12R0204T.setStatus('current')
ciscoMIPCapabilityV12R0304T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0304T = ciscoMIPCapabilityV12R0304T.setProductRelease('Cisco IOS 12.3(4)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0304T = ciscoMIPCapabilityV12R0304T.setStatus('current')
mibBuilder.exportSymbols("CISCO-MIP-CAPABILITY", PYSNMP_MODULE_ID=ciscoMIPCapability, ciscoMIPCapability=ciscoMIPCapability, ciscoMIPCapabilityV12R0204T=ciscoMIPCapabilityV12R0204T, ciscoMIPCapabilityV12R02=ciscoMIPCapabilityV12R02, ciscoMIPCapabilityV12R0304T=ciscoMIPCapabilityV12R0304T)
