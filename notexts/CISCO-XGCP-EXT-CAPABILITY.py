#
# PySNMP MIB module CISCO-XGCP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-XGCP-EXT-CAPABILITY
# Source digest sha256:a5c3c48a1cd0a9638f5ce9ed70fade915af7028953810dfd508292e485e74779
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoXgcpExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 99999))
ciscoXgcpExtCapability.setRevisions(('2004-06-18 00:00',))
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setLastUpdated('2004-06-18 00:00')
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoXgcpExtCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpExtCapabilityV12R03 = ciscoXgcpExtCapabilityV12R03.setProductRelease('Cisco IOS 12.3.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpExtCapabilityV12R03 = ciscoXgcpExtCapabilityV12R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-XGCP-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoXgcpExtCapability, ciscoXgcpExtCapability=ciscoXgcpExtCapability, ciscoXgcpExtCapabilityV12R03=ciscoXgcpExtCapabilityV12R03)
