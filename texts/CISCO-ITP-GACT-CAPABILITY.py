#
# PySNMP MIB module CISCO-ITP-GACT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-GACT-CAPABILITY
# Source digest sha256:4202c270b923aa9e2d9b6a2274d6f3d2142892f8b3a3ff3f7cfad33e5dfb9d6f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGactCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 304))
ciscoGactCapability.setRevisions(('2007-04-26 00:00', '2003-12-08 00:00', '2003-07-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGactCapability.setRevisionsDescriptions(('Added ciscoGactCapabilityV12R0218IXA and\n        ciscoGactCapabilityV12R0411SW capability statements.', 'Support for cross instance global title\n        translation.  Added agent capability\n        ciscoGactCapabilityV12R022004SW statement for \n        IOS 12.2(20.4) and replaced \n        ciscoGactGttGroup object group with\n        ciscoGactGttGroupRev1.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGactCapability.setLastUpdated('2007-04-26 00:00')
if mibBuilder.loadTexts: ciscoGactCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGactCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoGactCapability.setDescription('Agent capabilities for the CISCO-ITP-GACT-MIB.')
ciscoGactCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0204MB10 = ciscoGactCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0204MB10 = ciscoGactCapabilityV12R0204MB10.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R0204MB10.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
ciscoGactCapabilityV12R022004SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R022004SW = ciscoGactCapabilityV12R022004SW.setProductRelease('Cisco IOS 12.2(20.4)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R022004SW = ciscoGactCapabilityV12R022004SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R022004SW.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
ciscoGactCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0218IXA = ciscoGactCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0218IXA = ciscoGactCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R0218IXA.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
ciscoGactCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 304, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0411SW = ciscoGactCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGactCapabilityV12R0411SW = ciscoGactCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGactCapabilityV12R0411SW.setDescription('CISCO-ITP-GACT-MIB.my agent capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-GACT-CAPABILITY", PYSNMP_MODULE_ID=ciscoGactCapability, ciscoGactCapability=ciscoGactCapability, ciscoGactCapabilityV12R0204MB10=ciscoGactCapabilityV12R0204MB10, ciscoGactCapabilityV12R0218IXA=ciscoGactCapabilityV12R0218IXA, ciscoGactCapabilityV12R022004SW=ciscoGactCapabilityV12R022004SW, ciscoGactCapabilityV12R0411SW=ciscoGactCapabilityV12R0411SW)
