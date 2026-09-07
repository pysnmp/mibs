#
# PySNMP MIB module CISCO-ITP-GSCCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-GSCCP-CAPABILITY
# Source digest sha256:10354fa53b023abd53cc57d01a810c2d7bc2d8960fbf18fa6446fa187ea03e0b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGsccpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 539))
ciscoGsccpCapability.setRevisions(('2007-05-17 00:00', '2005-01-14 00:00', '2004-10-07 00:00', '2003-12-08 00:00', '2003-10-28 00:00', '2003-05-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGsccpCapability.setRevisionsDescriptions(('Added ciscoGsccpCapabilityV12R0218IXA and\n        ciscoGsccpCapabilityV12R0411SW capability\n        statements.  Corrected all capability statements\n        to indicate that cgsccpGttConPcRowStatus was\n        implemented as read-only rather than\n        cgsccpGttConPcTable.', 'Added ciscoGsccpCapabilityV12R025000SW1\n        capability statement.  Added\n        ciscoGsccpNotificationsGroupSup1,\n        ciscoGsccpGttErrorsGroup and\n        ciscoGsccpGttPrefGroupSup1 object goups.', 'Added ciscoGsccpCapabilityV12R023000SW1\n        capability statement.  Replaced\n        ciscoGsccpGttAppGroupRev2 object group with\n        ciscoGsccpGttAppGroupRev3.', 'Support for cross instance global title\n        translation.\n\n         Added ciscoGsccpCapabilityV12R022004SW\n         capability statement.  Replaced\n         ciscoGsccpGttAppGroup object group with\n         ciscoGsccpGttAppGroupRev2.  Replaced\n         ciscoGsccpGttGtaGroup with\n         ciscoGsccpGttGtaGroupRev2.', 'Changes to allow GTT prefix conversion\n        to be specified per instance.\n\n        Added ciscoGsccpCapabilityV12R0204MB13\n        capability statement.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGsccpCapability.setLastUpdated('2007-05-17 00:00')
if mibBuilder.loadTexts: ciscoGsccpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGsccpCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoGsccpCapability.setDescription('Agent capabilities for the CISCO-ITP-GSCCP-MIB.')
ciscoGsccpCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB10 = ciscoGsccpCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB10 = ciscoGsccpCapabilityV12R0204MB10.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R0204MB10.setDescription('IOS 12.2(4)MB10 Cisco CISCO-ITP-GSCCP-MIB.my User\n        Agent MIB capabilities.')
ciscoGsccpCapabilityV12R0204MB13 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB13 = ciscoGsccpCapabilityV12R0204MB13.setProductRelease('Cisco IOS 12.2(4)MB13')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB13 = ciscoGsccpCapabilityV12R0204MB13.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R0204MB13.setDescription('IOS 12.2(4)MB13 Cisco CISCO-ITP-GSCCP-MIB.my User\n        Agent MIB capabilities.')
ciscoGsccpCapabilityV12R022004SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R022004SW = ciscoGsccpCapabilityV12R022004SW.setProductRelease('Cisco IOS 12.2(20.4)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R022004SW = ciscoGsccpCapabilityV12R022004SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R022004SW.setDescription('IOS 12.2(20.4)SW Cisco CISCO-ITP-GSCCP-MIB.my User\n        Agent MIB capabilities.')
ciscoGsccpCapabilityV12R023000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R023000SW1 = ciscoGsccpCapabilityV12R023000SW1.setProductRelease('Cisco IOS 12.2(23)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R023000SW1 = ciscoGsccpCapabilityV12R023000SW1.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R023000SW1.setDescription('IOS 12.2(23)SW1 Cisco CISCO-ITP-GSCCP-MIB.my User\n        Agent MIB capabilities.')
ciscoGsccpCapabilityV12R025000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R025000SW1 = ciscoGsccpCapabilityV12R025000SW1.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R025000SW1 = ciscoGsccpCapabilityV12R025000SW1.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R025000SW1.setDescription('IOS 12.2(25)SW1 Cisco CISCO-ITP-GSCCP-MIB.my User\n        Agent MIB capabilities.')
ciscoGsccpCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0218IXA = ciscoGsccpCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0218IXA = ciscoGsccpCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R0218IXA.setDescription('IOS 12.2(18)IXA Cisco CISCO-ITP-GSCCP-MIB.my User Agent MIB\n        capabilities.')
ciscoGsccpCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0411SW = ciscoGsccpCapabilityV12R0411SW.setProductRelease('Cisco IOS IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0411SW = ciscoGsccpCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGsccpCapabilityV12R0411SW.setDescription('Cisco IOS IOS 12.4(11)SW Cisco CISCO-ITP-GSCCP-MIB.my\n        User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-GSCCP-CAPABILITY", PYSNMP_MODULE_ID=ciscoGsccpCapability, ciscoGsccpCapability=ciscoGsccpCapability, ciscoGsccpCapabilityV12R0204MB10=ciscoGsccpCapabilityV12R0204MB10, ciscoGsccpCapabilityV12R0204MB13=ciscoGsccpCapabilityV12R0204MB13, ciscoGsccpCapabilityV12R0218IXA=ciscoGsccpCapabilityV12R0218IXA, ciscoGsccpCapabilityV12R022004SW=ciscoGsccpCapabilityV12R022004SW, ciscoGsccpCapabilityV12R023000SW1=ciscoGsccpCapabilityV12R023000SW1, ciscoGsccpCapabilityV12R025000SW1=ciscoGsccpCapabilityV12R025000SW1, ciscoGsccpCapabilityV12R0411SW=ciscoGsccpCapabilityV12R0411SW)
