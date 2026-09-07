#
# PySNMP MIB module CISCO-ETHERLIKE-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ETHERLIKE-EXT-CAPABILITY
# Source digest sha256:9f912a5b48532e7d021ad75e10bef610a11fd99a35eaa25b2c98bf213a519052
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEtherlikeExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 587))
ciscoEtherlikeExtCapability.setRevisions(('2011-04-01 00:00', '2010-10-29 00:00', '2010-03-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setRevisionsDescriptions(('Add capability statement ceeCapV15R0002SGPCat4K.', 'Add capability statement ceeCapV12R0250SYPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setLastUpdated('2011-04-01 00:00')
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEtherlikeExtCapability.setDescription('Agent capabilities for CISCO-ETHERLIKE-EXT-MIB.')
ceeCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0233SXI4PCat6K = ceeCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0233SXI4PCat6K = ceeCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: ceeCapV12R0233SXI4PCat6K.setDescription('CISCO-ETHERLIKE-EXT-MIB agent capabilities.')
ceeCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0250SYPCat6K = ceeCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV12R0250SYPCat6K = ceeCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ceeCapV12R0250SYPCat6K.setDescription('CISCO-ETHERLIKE-EXT-MIB agent capabilities.')
ceeCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 587, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV15R0002SGPCat4K = ceeCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeCapV15R0002SGPCat4K = ceeCapV15R0002SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ceeCapV15R0002SGPCat4K.setDescription('CISCO-ETHERLIKE-EXT-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-ETHERLIKE-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoEtherlikeExtCapability, ceeCapV12R0233SXI4PCat6K=ceeCapV12R0233SXI4PCat6K, ceeCapV12R0250SYPCat6K=ceeCapV12R0250SYPCat6K, ceeCapV15R0002SGPCat4K=ceeCapV15R0002SGPCat4K, ciscoEtherlikeExtCapability=ciscoEtherlikeExtCapability)
