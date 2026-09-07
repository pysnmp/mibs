#
# PySNMP MIB module CISCO-HOST-RESOURCES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-HOST-RESOURCES-CAPABILITY
# Source digest sha256:a5ae47b141fe039b5a9d466351f4e2b340ef5d26212208f9f48db8dd9c0159ac
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHostResourcesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 547))
ciscoHostResourcesCapability.setRevisions(('2007-10-04 00:00', '2007-09-17 00:00',))
if mibBuilder.loadTexts: ciscoHostResourcesCapability.setLastUpdated('2007-10-04 00:00')
if mibBuilder.loadTexts: ciscoHostResourcesCapability.setOrganization('Cisco Systems, Inc.')
ciscoHostResourcesCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 547, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityV12R04 = ciscoHostResourcesCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityV12R04 = ciscoHostResourcesCapabilityV12R04.setStatus('current')
ciscoHostResourcesCapabilityCTSV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 547, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityCTSV120 = ciscoHostResourcesCapabilityCTSV120.setProductRelease('Cisco TelePresence System (CTS) 1.2.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHostResourcesCapabilityCTSV120 = ciscoHostResourcesCapabilityCTSV120.setStatus('current')
mibBuilder.exportSymbols("CISCO-HOST-RESOURCES-CAPABILITY", PYSNMP_MODULE_ID=ciscoHostResourcesCapability, ciscoHostResourcesCapability=ciscoHostResourcesCapability, ciscoHostResourcesCapabilityCTSV120=ciscoHostResourcesCapabilityCTSV120, ciscoHostResourcesCapabilityV12R04=ciscoHostResourcesCapabilityV12R04)
