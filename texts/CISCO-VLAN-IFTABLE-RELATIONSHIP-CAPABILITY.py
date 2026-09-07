#
# PySNMP MIB module CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY
# Source digest sha256:7242c5f6879f527331d904ef80d3147efbf6d99794f029579edfb0554e2a9d48
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanIfTableRelCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 369))
ciscoVlanIfTableRelCapability.setRevisions(('2013-08-08 00:00', '2006-01-18 00:00', '2004-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setRevisionsDescriptions(('Added ciscoVlanIfTableRelCapNxOSV6R0202PN7K.', 'Added ciscoVlanIfTableRelCapIOSXRV3R2CRS1\n        Agent Capabilities for IOS XR 3.2.0', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setLastUpdated('2013-08-08 00:00')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapability.setDescription('The agent capabilities description of\n        CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB.')
ciscoVlanIfTableRelCapV12R0119E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapV12R0119E = ciscoVlanIfTableRelCapV12R0119E.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapV12R0119E = ciscoVlanIfTableRelCapV12R0119E.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapV12R0119E.setDescription('CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB\n        agent capabilities.')
ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = ciscoVlanIfTableRelCapIOSXRV3R2CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapIOSXRV3R2CRS1 = ciscoVlanIfTableRelCapIOSXRV3R2CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapIOSXRV3R2CRS1.setDescription('CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB capabilities\n        for IOS XR release 3.2.0')
ciscoVlanIfTableRelCapNxOSV6R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 369, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapNxOSV6R0202PN7K = ciscoVlanIfTableRelCapNxOSV6R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanIfTableRelCapNxOSV6R0202PN7K = ciscoVlanIfTableRelCapNxOSV6R0202PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanIfTableRelCapNxOSV6R0202PN7K.setDescription('CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB\n        agent capabilities.')
mibBuilder.exportSymbols("CISCO-VLAN-IFTABLE-RELATIONSHIP-CAPABILITY", PYSNMP_MODULE_ID=ciscoVlanIfTableRelCapability, ciscoVlanIfTableRelCapIOSXRV3R2CRS1=ciscoVlanIfTableRelCapIOSXRV3R2CRS1, ciscoVlanIfTableRelCapNxOSV6R0202PN7K=ciscoVlanIfTableRelCapNxOSV6R0202PN7K, ciscoVlanIfTableRelCapV12R0119E=ciscoVlanIfTableRelCapV12R0119E, ciscoVlanIfTableRelCapability=ciscoVlanIfTableRelCapability)
