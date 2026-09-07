#
# PySNMP MIB module CISCO-INTERFACETOPN-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-INTERFACETOPN-EXT-CAPABILITY
# Source digest sha256:7d85b35c82152435fd21a785bbbfb71e867a76ad4fbb29e04cb5cd61afcbba0f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTopNExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 543))
ciscoTopNExtCapability.setRevisions(('2012-09-07 01:00', '2007-07-06 00:00',))
if mibBuilder.loadTexts: ciscoTopNExtCapability.setLastUpdated('2012-09-07 01:00')
if mibBuilder.loadTexts: ciscoTopNExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoTopNExtCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 543, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV12R0233SXHPCat6k = ciscoTopNExtCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV12R0233SXHPCat6k = ciscoTopNExtCapV12R0233SXHPCat6k.setStatus('current')
ciscoTopNExtCapV15R0001SY1PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 543, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV15R0001SY1PCat6K = ciscoTopNExtCapV15R0001SY1PCat6K.setProductRelease('Cisco IOS 15.0(1)SY1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTopNExtCapV15R0001SY1PCat6K = ciscoTopNExtCapV15R0001SY1PCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-INTERFACETOPN-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoTopNExtCapability, ciscoTopNExtCapV12R0233SXHPCat6k=ciscoTopNExtCapV12R0233SXHPCat6k, ciscoTopNExtCapV15R0001SY1PCat6K=ciscoTopNExtCapV15R0001SY1PCat6K, ciscoTopNExtCapability=ciscoTopNExtCapability)
