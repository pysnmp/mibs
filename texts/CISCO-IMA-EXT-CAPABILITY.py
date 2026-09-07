#
# PySNMP MIB module CISCO-IMA-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IMA-EXT-CAPABILITY
# Source digest sha256:df4beb63551891bcd5b63c5f2a1a13d92157b451058bc4e45dd08ce01c477c24
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
MilliSeconds, = mibBuilder.importSymbols("IMA-MIB", "MilliSeconds")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImaExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 524))
ciscoImaExtCapability.setRevisions(('2006-11-24 00:00', '2006-09-26 00:00', '2002-03-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoImaExtCapability.setRevisionsDescriptions(('Added ciscoImaExtCapabilityV12R05 for\n        Cisco 2800, 3700 and 3800 Series Routers.', 'Added ciscoImaExtAxsmeCapabilityV5R320 and\n        ciscoImaExtCapabilityV5R320.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoImaExtCapability.setLastUpdated('2006-11-24 00:00')
if mibBuilder.loadTexts: ciscoImaExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoImaExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoImaExtCapability.setDescription('Agent Capabilities for CISCO-IMA-MIB.')
ciscoImaExtAxsmeCapabilityV3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV3R0 = ciscoImaExtAxsmeCapabilityV3R0.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV3R0 = ciscoImaExtAxsmeCapabilityV3R0.setStatus('current')
if mibBuilder.loadTexts: ciscoImaExtAxsmeCapabilityV3R0.setDescription('Agent capabilities for CISCO-IMA-MIB\n        for AXSME Service Module in MGX8850 Series.')
ciscoImaExtAxsmeCapabilityV5R320 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV5R320 = ciscoImaExtAxsmeCapabilityV5R320.setProductRelease('MGX8850 Release 5.3.20')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtAxsmeCapabilityV5R320 = ciscoImaExtAxsmeCapabilityV5R320.setStatus('current')
if mibBuilder.loadTexts: ciscoImaExtAxsmeCapabilityV5R320.setDescription('Agent capabilities for CISCO-IMA-MIB\n        for AXSME Service Module in MGX8850 Series.')
ciscoImaExtCapabilityV5R320 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV5R320 = ciscoImaExtCapabilityV5R320.setProductRelease('MGX8950  and MGX8850 Release 5.3.20')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV5R320 = ciscoImaExtCapabilityV5R320.setStatus('current')
if mibBuilder.loadTexts: ciscoImaExtCapabilityV5R320.setDescription('CISCO-IMA-MIB Capabilities for Service Module:\n        MPSM155,MPSM16T1E1 and Processor Switch Module\n        Enhanced (PXM1E) controller card.')
ciscoImaExtCapabilityV12R05 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 524, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV12R05 = ciscoImaExtCapabilityV12R05.setProductRelease('IOS 12.5 for Cisco Access Routers and ISRs')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaExtCapabilityV12R05 = ciscoImaExtCapabilityV12R05.setStatus('current')
if mibBuilder.loadTexts: ciscoImaExtCapabilityV12R05.setDescription('Agent capabilities for Cisco 3700 Series Access\n        Routers and 2800, 3800 Series Integrated Services Routers.')
mibBuilder.exportSymbols("CISCO-IMA-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoImaExtCapability, ciscoImaExtAxsmeCapabilityV3R0=ciscoImaExtAxsmeCapabilityV3R0, ciscoImaExtAxsmeCapabilityV5R320=ciscoImaExtAxsmeCapabilityV5R320, ciscoImaExtCapability=ciscoImaExtCapability, ciscoImaExtCapabilityV12R05=ciscoImaExtCapabilityV12R05, ciscoImaExtCapabilityV5R320=ciscoImaExtCapabilityV5R320)
