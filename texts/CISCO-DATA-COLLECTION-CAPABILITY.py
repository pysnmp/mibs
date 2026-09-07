#
# PySNMP MIB module CISCO-DATA-COLLECTION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DATA-COLLECTION-CAPABILITY
# Source digest sha256:1f3456be39e4d4bc2d26aa620ca0d5a30cad63d3eb01c9f569e276115a5b3b24
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cDataCollectionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 425))
cDataCollectionCapability.setRevisions(('2007-08-07 00:00', '2005-01-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cDataCollectionCapability.setRevisionsDescriptions(('Added Agent-Capability support for IOS 12.2SR.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cDataCollectionCapability.setLastUpdated('2007-08-07 00:00')
if mibBuilder.loadTexts: cDataCollectionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cDataCollectionCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n                   San Jose, CA  95134\n                    USA\n\n                Tel:+1 800 553-NETS\n\n                    E-mail:        cs-snmp@cisco.com')
if mibBuilder.loadTexts: cDataCollectionCapability.setDescription('Agent capabilities for CISCO-DATA-COLLECTION-MIB')
cDataCollectionCapabilityV12R0S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 425, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R0S = cDataCollectionCapabilityV12R0S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R0S = cDataCollectionCapabilityV12R0S.setStatus('current')
if mibBuilder.loadTexts: cDataCollectionCapabilityV12R0S.setDescription('cisco-data-collection mib capabilities')
cDataCollectionCapabilityV12R1S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 425, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R1S = cDataCollectionCapabilityV12R1S.setProductRelease('Cisco IOS 12.2SR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDataCollectionCapabilityV12R1S = cDataCollectionCapabilityV12R1S.setStatus('current')
if mibBuilder.loadTexts: cDataCollectionCapabilityV12R1S.setDescription('cisco-data-collection mib capabilities')
mibBuilder.exportSymbols("CISCO-DATA-COLLECTION-CAPABILITY", PYSNMP_MODULE_ID=cDataCollectionCapability, cDataCollectionCapability=cDataCollectionCapability, cDataCollectionCapabilityV12R0S=cDataCollectionCapabilityV12R0S, cDataCollectionCapabilityV12R1S=cDataCollectionCapabilityV12R1S)
