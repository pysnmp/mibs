#
# PySNMP MIB module CISCO-UDLDP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-UDLDP-CAPABILITY
# Source digest sha256:30579dfb1f8809459bc303071648d223d218d30a3180275ae1a07280f2af7aa5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoUdldpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 344))
ciscoUdldpCapability.setRevisions(('2012-09-10 00:00', '2011-03-30 00:00', '2010-03-16 09:00', '2004-04-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoUdldpCapability.setRevisionsDescriptions(('Added capability statement ciscoUdldpCapV15R0001SY1PCat6K.', 'Added capability statement ciscoUdldpCapV15R0002SGPCat4K.', 'Added capability statement ciscoUdldpCapV12R0233SXI4PCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoUdldpCapability.setLastUpdated('2012-09-10 00:00')
if mibBuilder.loadTexts: ciscoUdldpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoUdldpCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoUdldpCapability.setDescription('The capabilities description of\n        CISCO-UDLDP-MIB.')
ciscoUdldpCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV12R0214SXCat6K = ciscoUdldpCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14SX) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV12R0214SXCat6K = ciscoUdldpCapV12R0214SXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoUdldpCapV12R0214SXCat6K.setDescription('CISCO-UDLDP-MIB capabilities.')
ciscoUdldpCapCatOSV07R0604 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapCatOSV07R0604 = ciscoUdldpCapCatOSV07R0604.setProductRelease('Cisco CatOS 7.6(4).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapCatOSV07R0604 = ciscoUdldpCapCatOSV07R0604.setStatus('current')
if mibBuilder.loadTexts: ciscoUdldpCapCatOSV07R0604.setDescription('CISCO-UDLDP-MIB capabilities.')
ciscoUdldpCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapCatOSV08R0101 = ciscoUdldpCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapCatOSV08R0101 = ciscoUdldpCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoUdldpCapCatOSV08R0101.setDescription('CISCO-UDLDP-MIB capabilities.')
ciscoUdldpCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV12R0233SXI4PCat6K = ciscoUdldpCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices running IOS images.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV12R0233SXI4PCat6K = ciscoUdldpCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoUdldpCapV12R0233SXI4PCat6K.setDescription('CISCO-UDLDP-MIB capabilities.')
ciscoUdldpCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV15R0002SGPCat4K = ciscoUdldpCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Catalyst 4000 family\n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV15R0002SGPCat4K = ciscoUdldpCapV15R0002SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoUdldpCapV15R0002SGPCat4K.setDescription('CISCO-UDLDP-MIB capabilities.')
ciscoUdldpCapV15R0001SY1PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV15R0001SY1PCat6K = ciscoUdldpCapV15R0001SY1PCat6K.setProductRelease('Cisco IOS 15.0(1)SY1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV15R0001SY1PCat6K = ciscoUdldpCapV15R0001SY1PCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoUdldpCapV15R0001SY1PCat6K.setDescription('CISCO-UDLDP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-UDLDP-CAPABILITY", PYSNMP_MODULE_ID=ciscoUdldpCapability, ciscoUdldpCapCatOSV07R0604=ciscoUdldpCapCatOSV07R0604, ciscoUdldpCapCatOSV08R0101=ciscoUdldpCapCatOSV08R0101, ciscoUdldpCapV12R0214SXCat6K=ciscoUdldpCapV12R0214SXCat6K, ciscoUdldpCapV12R0233SXI4PCat6K=ciscoUdldpCapV12R0233SXI4PCat6K, ciscoUdldpCapV15R0001SY1PCat6K=ciscoUdldpCapV15R0001SY1PCat6K, ciscoUdldpCapV15R0002SGPCat4K=ciscoUdldpCapV15R0002SGPCat4K, ciscoUdldpCapability=ciscoUdldpCapability)
