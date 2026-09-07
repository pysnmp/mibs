#
# PySNMP MIB module CISCO-ENTITY-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-EXT-CAPABILITY
# Source digest sha256:66af8f9c818cb7d5eddbeb0af05115f60565fe49fdbba25f713c47be7cc0059a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 392))
ciscoEntityExtCapability.setRevisions(('2007-09-06 00:00', '2004-03-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityExtCapability.setRevisionsDescriptions(('Addition of ceExtCapV12R0217SXPCat6k and\n                ceExtCapV12R0233SXHPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntityExtCapability.setLastUpdated('2007-09-06 00:00')
if mibBuilder.loadTexts: ciscoEntityExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityExtCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityExtCapability.setDescription('The agent capabilities description of \n                CISCO-ENTITY-EXT-MIB.')
ciscoEntityExtCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 392, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtCapCatOSV08R0301 = ciscoEntityExtCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtCapCatOSV08R0301 = ciscoEntityExtCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityExtCapCatOSV08R0301.setDescription('CISCO-ENTITY-EXT-MIB agent capabilities.')
ceExtCapV12R0217SXPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 392, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0217SXPCat6k = ceExtCapV12R0217SXPCat6k.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0217SXPCat6k = ceExtCapV12R0217SXPCat6k.setStatus('current')
if mibBuilder.loadTexts: ceExtCapV12R0217SXPCat6k.setDescription('CISCO-ENTITY-EXT-MIB capabilities.')
ceExtCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 392, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0233SXHPCat6k = ceExtCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtCapV12R0233SXHPCat6k = ceExtCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: ceExtCapV12R0233SXHPCat6k.setDescription('CISCO-ENTITY-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoEntityExtCapability, ceExtCapV12R0217SXPCat6k=ceExtCapV12R0217SXPCat6k, ceExtCapV12R0233SXHPCat6k=ceExtCapV12R0233SXHPCat6k, ciscoEntityExtCapCatOSV08R0301=ciscoEntityExtCapCatOSV08R0301, ciscoEntityExtCapability=ciscoEntityExtCapability)
