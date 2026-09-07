#
# PySNMP MIB module CISCO-VLAN-BRIDGING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VLAN-BRIDGING-CAPABILITY
# Source digest sha256:ef6150492cef18f8b6d122b8cb50c04e186c95375aec2e86f22149890839c076
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanBridgingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 339))
ciscoVlanBridgingCapability.setRevisions(('2004-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setLastUpdated('2004-06-11 00:00')
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com\n                        cs-vlans@cisco.com')
if mibBuilder.loadTexts: ciscoVlanBridgingCapability.setDescription('The agent capabilities description of \n                 CISCO-VLAN-BRIDGING-MIB.')
cVlanBridgingCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 339, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0101 = cVlanBridgingCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0101 = cVlanBridgingCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: cVlanBridgingCapCatOSV08R0101.setDescription('CISCO-VLAN-BRIDGING-MIB capabilities.')
cVlanBridgingCapCatOSV08R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 339, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0201 = cVlanBridgingCapCatOSV08R0201.setProductRelease('Cisco CatOS 8.2(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanBridgingCapCatOSV08R0201 = cVlanBridgingCapCatOSV08R0201.setStatus('current')
if mibBuilder.loadTexts: cVlanBridgingCapCatOSV08R0201.setDescription('CISCO-VLAN-BRIDGING-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VLAN-BRIDGING-CAPABILITY", PYSNMP_MODULE_ID=ciscoVlanBridgingCapability, cVlanBridgingCapCatOSV08R0101=cVlanBridgingCapCatOSV08R0101, cVlanBridgingCapCatOSV08R0201=cVlanBridgingCapCatOSV08R0201, ciscoVlanBridgingCapability=ciscoVlanBridgingCapability)
