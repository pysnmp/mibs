#
# PySNMP MIB module CISCO-IP-RAN-BACKHAUL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IP-RAN-BACKHAUL-CAPABILITY
# Source digest sha256:00bbeb174c647cd8aa6a289ae8c7cb6ef185f150bdf715ac03d8775656dea3ad
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpRanBhCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 461))
ciscoIpRanBhCapability.setRevisions(('2010-07-14 00:00', '2005-09-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpRanBhCapability.setRevisionsDescriptions(('Changes to indicate conversion to cirbhShortHaulBulkTable.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setLastUpdated('2010-07-14 00:00')
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ran-o@cisco.com')
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setDescription('Agent capabilities for the\n        CISCO-IP-RAN-BACKHAUL-MIB.')
ciscoIpRanBhCapabilityV12R0402MR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 461, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0402MR = ciscoIpRanBhCapabilityV12R0402MR.setProductRelease('Cisco IOS 12.4(2)MR1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0402MR = ciscoIpRanBhCapabilityV12R0402MR.setStatus('current')
if mibBuilder.loadTexts: ciscoIpRanBhCapabilityV12R0402MR.setDescription('IOS 12.4(2)MR1 Cisco CISCO-IP-RAN-BACKHAUL-MIB\n        User Agent MIB capabilities.')
ciscoIpRanBhCapabilityV12R0412MR1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 461, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0412MR1 = ciscoIpRanBhCapabilityV12R0412MR1.setProductRelease('Cisco IOS 12.4(12)MR1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0412MR1 = ciscoIpRanBhCapabilityV12R0412MR1.setStatus('current')
if mibBuilder.loadTexts: ciscoIpRanBhCapabilityV12R0412MR1.setDescription('IOS 12.4(12)MR1 Cisco CISCO-IP-RAN-BACKHAUL-MIB\n        User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IP-RAN-BACKHAUL-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpRanBhCapability, ciscoIpRanBhCapability=ciscoIpRanBhCapability, ciscoIpRanBhCapabilityV12R0402MR=ciscoIpRanBhCapabilityV12R0402MR, ciscoIpRanBhCapabilityV12R0412MR1=ciscoIpRanBhCapabilityV12R0412MR1)
