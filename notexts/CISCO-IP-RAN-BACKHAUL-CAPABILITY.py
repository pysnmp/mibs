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
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setLastUpdated('2010-07-14 00:00')
if mibBuilder.loadTexts: ciscoIpRanBhCapability.setOrganization('Cisco Systems, Inc.')
ciscoIpRanBhCapabilityV12R0402MR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 461, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0402MR = ciscoIpRanBhCapabilityV12R0402MR.setProductRelease('Cisco IOS 12.4(2)MR1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0402MR = ciscoIpRanBhCapabilityV12R0402MR.setStatus('current')
ciscoIpRanBhCapabilityV12R0412MR1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 461, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0412MR1 = ciscoIpRanBhCapabilityV12R0412MR1.setProductRelease('Cisco IOS 12.4(12)MR1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpRanBhCapabilityV12R0412MR1 = ciscoIpRanBhCapabilityV12R0412MR1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-RAN-BACKHAUL-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpRanBhCapability, ciscoIpRanBhCapability=ciscoIpRanBhCapability, ciscoIpRanBhCapabilityV12R0402MR=ciscoIpRanBhCapabilityV12R0402MR, ciscoIpRanBhCapabilityV12R0412MR1=ciscoIpRanBhCapabilityV12R0412MR1)
