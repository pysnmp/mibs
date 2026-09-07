#
# PySNMP MIB module CISCO-FABRICPATH-TOPOLOGY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-FABRICPATH-TOPOLOGY-CAPABILITY
# Source digest sha256:e50ceee1bce23f17aea6c471c6b0a2264b62590c08d5496d4a84701ab1101899
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricPathTopologyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 620))
ciscoFabricPathTopologyCapability.setRevisions(('2013-07-16 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFabricPathTopologyCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFabricPathTopologyCapability.setLastUpdated('2013-07-16 12:00')
if mibBuilder.loadTexts: ciscoFabricPathTopologyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFabricPathTopologyCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoFabricPathTopologyCapability.setDescription('The capabilities description of\n        CISCO-FABRICPATH-TOPOLOGY-MIB.')
ciscoFabricPathTopologyCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 620, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFabricPathTopologyCapNxOSV06R0202PN7k = ciscoFabricPathTopologyCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFabricPathTopologyCapNxOSV06R0202PN7k = ciscoFabricPathTopologyCapNxOSV06R0202PN7k.setStatus('current')
if mibBuilder.loadTexts: ciscoFabricPathTopologyCapNxOSV06R0202PN7k.setDescription('CISCO-FABRICPATH-TOPOLOGY-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-FABRICPATH-TOPOLOGY-CAPABILITY", PYSNMP_MODULE_ID=ciscoFabricPathTopologyCapability, ciscoFabricPathTopologyCapNxOSV06R0202PN7k=ciscoFabricPathTopologyCapNxOSV06R0202PN7k, ciscoFabricPathTopologyCapability=ciscoFabricPathTopologyCapability)
