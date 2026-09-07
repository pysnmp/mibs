#
# PySNMP MIB module CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY
# Source digest sha256:8a908ca871145f7c63d8414d122c609466ae401f1da68b48aa43aaed73cf5412
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfDhcpSrvExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 438))
ciscoIetfDhcpSrvExtCapability.setRevisions(('2007-02-14 12:00', '2005-05-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setRevisionsDescriptions(('Added capability definition ciscoIetfDhcpServerExtCapabilityV12R02SRC\n        for 12.2SRC.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setLastUpdated('2007-02-14 12:00')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-dhcp-mib@cisco.com')
if mibBuilder.loadTexts: ciscoIetfDhcpSrvExtCapability.setDescription('Agent capabilities for the CISCO-IETF-DHCP-SERVER-EXT-MIB.')
ciscoIetfDhcpServerExtCapabilityV62R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 438, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV62R00 = ciscoIetfDhcpServerExtCapabilityV62R00.setProductRelease('Cisco CNS Network Registrar 6.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV62R00 = ciscoIetfDhcpServerExtCapabilityV62R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfDhcpServerExtCapabilityV62R00.setDescription('CISCO-IETF-DHCP-SERVER-EXT-MIB capabilities for\n        Cisco CNS Network Registrar 6.2')
ciscoIetfDhcpServerExtCapabilityV12R02SRC = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 438, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV12R02SRC = ciscoIetfDhcpServerExtCapabilityV12R02SRC.setProductRelease('Cisco IOS 12.2SRC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfDhcpServerExtCapabilityV12R02SRC = ciscoIetfDhcpServerExtCapabilityV12R02SRC.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfDhcpServerExtCapabilityV12R02SRC.setDescription('CISCO-IETF-DHCP-SERVER-EXT-MIB capabilities for\n        Cisco IOS 12.2SRC')
mibBuilder.exportSymbols("CISCO-IETF-DHCP-SERVER-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfDhcpSrvExtCapability, ciscoIetfDhcpServerExtCapabilityV12R02SRC=ciscoIetfDhcpServerExtCapabilityV12R02SRC, ciscoIetfDhcpServerExtCapabilityV62R00=ciscoIetfDhcpServerExtCapabilityV62R00, ciscoIetfDhcpSrvExtCapability=ciscoIetfDhcpSrvExtCapability)
