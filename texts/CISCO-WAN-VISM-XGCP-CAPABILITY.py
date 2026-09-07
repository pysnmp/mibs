#
# PySNMP MIB module CISCO-WAN-VISM-XGCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-VISM-XGCP-CAPABILITY
# Source digest sha256:11ccbb649e9cb133f12c6ed834adc87b654afdcbe48acedb1f9cc7c34715b109
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismXgcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 322))
ciscoWanVismXgcpCapability.setRevisions(('2002-02-27 00:00', '2002-01-21 00:00', '2001-08-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setRevisionsDescriptions(('Fix bug CSCdw32263 where xgcpRestartDelay returns illegal value', 'Changed INCLUDES fields in order to pass SMIC compiler', 'Added ciscoWanVismXgcpCapabilityV2R01 AGENT-CAPABILITIES.',))
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setLastUpdated('2002-02-27 00:00')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapability.setDescription('The Agent Capabilities for XGCP-MIB.')
ciscoWanVismXgcpCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R00 = ciscoWanVismXgcpCapabilityV2R00.setProductRelease('VISM Release1.5,VISM Release2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R00 = ciscoWanVismXgcpCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapabilityV2R00.setDescription('XGCP MIB Capabilities')
ciscoWanVismXgcpCapabilityV2R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R01 = ciscoWanVismXgcpCapabilityV2R01.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV2R01 = ciscoWanVismXgcpCapabilityV2R01.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapabilityV2R01.setDescription('XGCP MIB Capabilities')
ciscoWanVismXgcpCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 322, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV3R00 = ciscoWanVismXgcpCapabilityV3R00.setProductRelease('VISM Release3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismXgcpCapabilityV3R00 = ciscoWanVismXgcpCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismXgcpCapabilityV3R00.setDescription('XGCP MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-XGCP-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanVismXgcpCapability, ciscoWanVismXgcpCapability=ciscoWanVismXgcpCapability, ciscoWanVismXgcpCapabilityV2R00=ciscoWanVismXgcpCapabilityV2R00, ciscoWanVismXgcpCapabilityV2R01=ciscoWanVismXgcpCapabilityV2R01, ciscoWanVismXgcpCapabilityV3R00=ciscoWanVismXgcpCapabilityV3R00)
