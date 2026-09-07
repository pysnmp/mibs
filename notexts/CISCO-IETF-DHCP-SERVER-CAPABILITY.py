#
# PySNMP MIB module CISCO-IETF-DHCP-SERVER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-DHCP-SERVER-CAPABILITY
# Source digest sha256:7ca524bda214e9d6d6a3e8896db5c6309cbb7a924d6cbe4a55781267a80c0ee9
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfDhcpSrvCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 439))
ciscoIetfDhcpSrvCapability.setRevisions(('2007-02-14 12:00', '2005-05-24 00:00',))
if mibBuilder.loadTexts: ciscoIetfDhcpSrvCapability.setLastUpdated('2007-02-14 12:00')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfDhcpServerCapabilityV62R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 439, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV62R00 = ciscoIetfDhcpServerCapabilityV62R00.setProductRelease('Cisco CNS Network Registrar 6.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV62R00 = ciscoIetfDhcpServerCapabilityV62R00.setStatus('current')
ciscoIetfDhcpServerCapabilityV12R02SRC = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 439, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV12R02SRC = ciscoIetfDhcpServerCapabilityV12R02SRC.setProductRelease('Cisco IOS 12.2SRC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerCapabilityV12R02SRC = ciscoIetfDhcpServerCapabilityV12R02SRC.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-DHCP-SERVER-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfDhcpSrvCapability, ciscoIetfDhcpServerCapabilityV12R02SRC=ciscoIetfDhcpServerCapabilityV12R02SRC, ciscoIetfDhcpServerCapabilityV62R00=ciscoIetfDhcpServerCapabilityV62R00, ciscoIetfDhcpSrvCapability=ciscoIetfDhcpSrvCapability)
