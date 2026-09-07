#
# PySNMP MIB module CISCO-IKE-FLOW-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IKE-FLOW-EXT-CAPABILITY
# Source digest sha256:4549edf2935a7c155c38e5bf690ea66d37fcab69b5634a6200e8b3d690aaf7e8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIkeFlowExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 490))
ciscoIkeFlowExtCapability.setRevisions(('2006-02-02 00:00',))
if mibBuilder.loadTexts: ciscoIkeFlowExtCapability.setLastUpdated('2006-02-02 00:00')
if mibBuilder.loadTexts: ciscoIkeFlowExtCapability.setOrganization('Cisco Systems, Inc.')
cIkeFlowExtCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 490, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIkeFlowExtCapSanOSV30R1MDS9000 = cIkeFlowExtCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIkeFlowExtCapSanOSV30R1MDS9000 = cIkeFlowExtCapSanOSV30R1MDS9000.setStatus('current')
mibBuilder.exportSymbols("CISCO-IKE-FLOW-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoIkeFlowExtCapability, cIkeFlowExtCapSanOSV30R1MDS9000=cIkeFlowExtCapSanOSV30R1MDS9000, ciscoIkeFlowExtCapability=ciscoIkeFlowExtCapability)
