#
# PySNMP MIB module CISCO-POLICY-GROUP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-POLICY-GROUP-CAPABILITY
# Source digest sha256:085f9926b999a96aaa198337f79758eb91f96b4a8791a8c3d65ca3a6dc17e770
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPolicyGroupCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 512))
ciscoPolicyGroupCapability.setRevisions(('2006-06-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setLastUpdated('2006-06-26 00:00')
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setDescription('The capabilities description of\n                 CISCO-POLICY-GROUP-MIB.')
ciscoPolicyGroupCapV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 512, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPolicyGroupCapV08R0601 = ciscoPolicyGroupCapV08R0601.setProductRelease('Cisco CatOS 8.6(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPolicyGroupCapV08R0601 = ciscoPolicyGroupCapV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoPolicyGroupCapV08R0601.setDescription('CISCO-POLICY-GROUP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-POLICY-GROUP-CAPABILITY", PYSNMP_MODULE_ID=ciscoPolicyGroupCapability, ciscoPolicyGroupCapV08R0601=ciscoPolicyGroupCapV08R0601, ciscoPolicyGroupCapability=ciscoPolicyGroupCapability)
