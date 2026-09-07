#
# PySNMP MIB module CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY
# Source digest sha256:c70f04747fb7dc103245b2fbd20d84a608db79be815fa477a692863492b1229c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL2L3IfConfigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 326))
ciscoL2L3IfConfigCapability.setRevisions(('2014-04-04 00:00', '2013-08-28 00:00', '2004-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setRevisionsDescriptions(('Added ciscoL2L3IfConfigCapNxOSV06R0201PMds agent\n        capability statement.', 'Added ciscoL2L3IfConfigCapNxOSV06R0202PN7K agent\n        capability statement.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setLastUpdated('2014-04-04 00:00')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapability.setDescription('The agent capabilities description of\n        CISCO-L2L3-INTERFACE-CONFIG-MIB.')
ciscoL2L3IfConfigCapV12R0119E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapV12R0119E = ciscoL2L3IfConfigCapV12R0119E.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapV12R0119E = ciscoL2L3IfConfigCapV12R0119E.setStatus('current')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapV12R0119E.setDescription('CISCO-L2L3-INTERFACE-CONFIG-MIB agent\n        capabilities.')
ciscoL2L3IfConfigCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0202PN7K = ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on \n                    Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0202PN7K = ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapNxOSV06R0202PN7K.setDescription('CISCO-L2L3-INTERFACE-CONFIG-MIB agent\n        capabilities.')
ciscoL2L3IfConfigCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 326, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0201PMds = ciscoL2L3IfConfigCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2L3IfConfigCapNxOSV06R0201PMds = ciscoL2L3IfConfigCapNxOSV06R0201PMds.setStatus('current')
if mibBuilder.loadTexts: ciscoL2L3IfConfigCapNxOSV06R0201PMds.setDescription('CISCO-L2L3-INTERFACE-CONFIG-MIB agent\n        capabilities.')
mibBuilder.exportSymbols("CISCO-L2L3-INTERFACE-CONFIG-CAPABILITY", PYSNMP_MODULE_ID=ciscoL2L3IfConfigCapability, ciscoL2L3IfConfigCapNxOSV06R0201PMds=ciscoL2L3IfConfigCapNxOSV06R0201PMds, ciscoL2L3IfConfigCapNxOSV06R0202PN7K=ciscoL2L3IfConfigCapNxOSV06R0202PN7K, ciscoL2L3IfConfigCapV12R0119E=ciscoL2L3IfConfigCapV12R0119E, ciscoL2L3IfConfigCapability=ciscoL2L3IfConfigCapability)
