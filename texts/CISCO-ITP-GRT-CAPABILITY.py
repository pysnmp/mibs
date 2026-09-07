#
# PySNMP MIB module CISCO-ITP-GRT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-GRT-CAPABILITY
# Source digest sha256:a643459bd5a877d0dcad38d6ab542ab751e29ca003f1d6d32dcecfe814ce9ea7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpGrtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 309))
ciscoItpGrtCapability.setRevisions(('2007-04-25 00:00', '2006-10-13 00:00', '2003-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpGrtCapability.setRevisionsDescriptions(('Added ciscoGrtCapabilityV12R0411SW capability statements.', 'Added ciscoGrtCapabilityV12R0218IXA capability statement. Added\n        cosmetic changes to MIB sections.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpGrtCapability.setLastUpdated('2007-04-25 00:00')
if mibBuilder.loadTexts: ciscoItpGrtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpGrtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpGrtCapability.setDescription('Agent capabilities for the CISCO-ITP-GRT-MIB.')
ciscoGrtCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0204MB10 = ciscoGrtCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0204MB10 = ciscoGrtCapabilityV12R0204MB10.setStatus('current')
if mibBuilder.loadTexts: ciscoGrtCapabilityV12R0204MB10.setDescription('IOS 12.2(4)MB10 Cisco CISCO-ITP-GRT-MIB.my\n        User Agent MIB capabilities.')
ciscoGrtCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0218IXA = ciscoGrtCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0218IXA = ciscoGrtCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoGrtCapabilityV12R0218IXA.setDescription('IOS 12.2(18)IXA Cisco CISCO-ITP-GRT-MIB.my\n        User Agent MIB capabilities.')
ciscoGrtCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0411SW = ciscoGrtCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0411SW = ciscoGrtCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoGrtCapabilityV12R0411SW.setDescription('Cisco IOS 12.4(11)SW Cisco CISCO-ITP-GRT-MIB.my User Agent MIB\n        capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-GRT-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpGrtCapability, ciscoGrtCapabilityV12R0204MB10=ciscoGrtCapabilityV12R0204MB10, ciscoGrtCapabilityV12R0218IXA=ciscoGrtCapabilityV12R0218IXA, ciscoGrtCapabilityV12R0411SW=ciscoGrtCapabilityV12R0411SW, ciscoItpGrtCapability=ciscoItpGrtCapability)
