#
# PySNMP MIB module CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY
# Source digest sha256:71b4af96b457a3d227fbfad6e2d7197cb70e79b5660130e23f3c366e30f3346c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoThreatMitigationServiceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 532))
ciscoThreatMitigationServiceCapability.setRevisions(('2007-05-17 00:00', '2007-01-29 00:00',))
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setLastUpdated('2007-05-17 00:00')
if mibBuilder.loadTexts: ciscoThreatMitigationServiceCapability.setOrganization('Cisco Systems, Inc.')
ciscoTmsCapIOSV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 532, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R02S = ciscoTmsCapIOSV12R02S.setProductRelease('Cisco IOS 12.2S ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R02S = ciscoTmsCapIOSV12R02S.setStatus('current')
ciscoTmsCapIOSV12R05T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 532, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R05T = ciscoTmsCapIOSV12R05T.setProductRelease('Cisco IOS 12.5T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTmsCapIOSV12R05T = ciscoTmsCapIOSV12R05T.setStatus('current')
mibBuilder.exportSymbols("CISCO-THREAT-MITIGATION-SERVICE-CAPABILITY", PYSNMP_MODULE_ID=ciscoThreatMitigationServiceCapability, ciscoThreatMitigationServiceCapability=ciscoThreatMitigationServiceCapability, ciscoTmsCapIOSV12R02S=ciscoTmsCapIOSV12R02S, ciscoTmsCapIOSV12R05T=ciscoTmsCapIOSV12R05T)
