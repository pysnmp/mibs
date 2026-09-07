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
if mibBuilder.loadTexts: ciscoContextMappingCapability.setLastUpdated('2008-08-22 00:00')
if mibBuilder.loadTexts: ciscoContextMappingCapability.setOrganization('Cisco Systems, Inc.')
ciscoContextMappingCapV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02S = ciscoContextMappingCapV12R02S.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02S = ciscoContextMappingCapV12R02S.setStatus('current')
ciscoContextMappingCapV12R02SG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02SG = ciscoContextMappingCapV12R02SG.setProductRelease('Cisco IOS 12.2SG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02SG = ciscoContextMappingCapV12R02SG.setStatus('current')
ciscoContextMappingIOSXRV3R7FCICRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingIOSXRV3R7FCICRS1 = ciscoContextMappingIOSXRV3R7FCICRS1.setProductRelease('Cisco IOS XR 3.7FCI for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingIOSXRV3R7FCICRS1 = ciscoContextMappingIOSXRV3R7FCICRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-CONTEXT-MAPPING-CAPABILITY", PYSNMP_MODULE_ID=ciscoContextMappingCapability, ciscoContextMappingCapV12R02S=ciscoContextMappingCapV12R02S, ciscoContextMappingCapV12R02SG=ciscoContextMappingCapV12R02SG, ciscoContextMappingCapability=ciscoContextMappingCapability, ciscoContextMappingIOSXRV3R7FCICRS1=ciscoContextMappingIOSXRV3R7FCICRS1)
