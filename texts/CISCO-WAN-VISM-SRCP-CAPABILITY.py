#
# PySNMP MIB module CISCO-WAN-VISM-SRCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-VISM-SRCP-CAPABILITY
# Source digest sha256:8ba6f321eefae8d20fcbbe9ac6bbfbe56ca261077383dabef86c1f6333cc2308
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismSrcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 321))
ciscoWanVismSrcpCapability.setRevisions(('2000-07-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setRevisionsDescriptions(('added ciscoWanVismSrcpCapabilityV2R01 macro\n                ',))
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setLastUpdated('2001-09-08 00:00')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapability.setDescription('The Agent Capabilities for CISCO-WAN-SRCP-MIB.')
ciscoWanVismSrcpCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 321, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R00 = ciscoWanVismSrcpCapabilityV2R00.setProductRelease('VISM Release1.5,VISM Release2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R00 = ciscoWanVismSrcpCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapabilityV2R00.setDescription('SRCP MIB Capabilities')
ciscoWanVismSrcpCapabilityV2R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 321, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R01 = ciscoWanVismSrcpCapabilityV2R01.setProductRelease('VISM release 2.0.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismSrcpCapabilityV2R01 = ciscoWanVismSrcpCapabilityV2R01.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismSrcpCapabilityV2R01.setDescription('SRCP MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-SRCP-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanVismSrcpCapability, ciscoWanVismSrcpCapability=ciscoWanVismSrcpCapability, ciscoWanVismSrcpCapabilityV2R00=ciscoWanVismSrcpCapabilityV2R00, ciscoWanVismSrcpCapabilityV2R01=ciscoWanVismSrcpCapabilityV2R01)
