#
# PySNMP MIB module CISCO-CONTEXT-MAPPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CONTEXT-MAPPING-CAPABILITY
# Source digest sha256:bfa0e05f32deff08c5ecaeb5e408b83c66a53638403777d8e5bb0d3ed010b9f3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoContextMappingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 564))
ciscoContextMappingCapability.setRevisions(('2008-08-22 00:00', '2008-03-24 00:00', '2005-05-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoContextMappingCapability.setRevisionsDescriptions(('Added ciscoContextMappingIOSXRV3R7FCICRS1', 'Added ciscoContextMappingCapV12R02SG', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoContextMappingCapability.setLastUpdated('2008-08-22 00:00')
if mibBuilder.loadTexts: ciscoContextMappingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoContextMappingCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoContextMappingCapability.setDescription('Agent capabilities for the\n        CISCO-CONTEXT-MAPPING-MIB.')
ciscoContextMappingCapV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02S = ciscoContextMappingCapV12R02S.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02S = ciscoContextMappingCapV12R02S.setStatus('current')
if mibBuilder.loadTexts: ciscoContextMappingCapV12R02S.setDescription('CISCO-CONTEXT-MAPPING-MIB capabilities.')
ciscoContextMappingCapV12R02SG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02SG = ciscoContextMappingCapV12R02SG.setProductRelease('Cisco IOS 12.2SG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02SG = ciscoContextMappingCapV12R02SG.setStatus('current')
if mibBuilder.loadTexts: ciscoContextMappingCapV12R02SG.setDescription('CISCO-CONTEXT-MAPPING-MIB capabilities.')
ciscoContextMappingIOSXRV3R7FCICRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingIOSXRV3R7FCICRS1 = ciscoContextMappingIOSXRV3R7FCICRS1.setProductRelease('Cisco IOS XR 3.7FCI for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingIOSXRV3R7FCICRS1 = ciscoContextMappingIOSXRV3R7FCICRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoContextMappingIOSXRV3R7FCICRS1.setDescription('CISCO-CONTEXT-MAPPING-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CONTEXT-MAPPING-CAPABILITY", PYSNMP_MODULE_ID=ciscoContextMappingCapability, ciscoContextMappingCapV12R02S=ciscoContextMappingCapV12R02S, ciscoContextMappingCapV12R02SG=ciscoContextMappingCapV12R02SG, ciscoContextMappingCapability=ciscoContextMappingCapability, ciscoContextMappingIOSXRV3R7FCICRS1=ciscoContextMappingIOSXRV3R7FCICRS1)
