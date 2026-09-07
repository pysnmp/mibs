#
# PySNMP MIB module CISCO-NETINT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-NETINT-CAPABILITY
# Source digest sha256:a661f0ffcc37fe1596c48a4e06f7c00857436111b2ee30adf3b60c301463acf7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNetintCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 452))
ciscoNetintCapability.setRevisions(('2007-07-03 00:00',))
if mibBuilder.loadTexts: ciscoNetintCapability.setLastUpdated('2007-07-03 00:00')
if mibBuilder.loadTexts: ciscoNetintCapability.setOrganization('Cisco Systems, Inc.')
ciscoNetintCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 452, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetintCapV12R0233SXHPCat6k = ciscoNetintCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetintCapV12R0233SXHPCat6k = ciscoNetintCapV12R0233SXHPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-NETINT-CAPABILITY", PYSNMP_MODULE_ID=ciscoNetintCapability, ciscoNetintCapV12R0233SXHPCat6k=ciscoNetintCapV12R0233SXHPCat6k, ciscoNetintCapability=ciscoNetintCapability)
