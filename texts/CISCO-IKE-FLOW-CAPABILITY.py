#
# PySNMP MIB module CISCO-IKE-FLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IKE-FLOW-CAPABILITY
# Source digest sha256:59b5a8f944586ebfb50c0d568b3cb5ec1c32627639f0bf418115793cfc6617aa
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIkeFlowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 487))
ciscoIkeFlowCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIkeFlowCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setLastUpdated('2006-02-02 00:00')
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setDescription('Agent capabilities for\n                 CISCO-IKE-FLOW-MIB.')
ciscoIkeFlowCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 487, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIkeFlowCapSanOSV30R1MDS9000 = ciscoIkeFlowCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000 \n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIkeFlowCapSanOSV30R1MDS9000 = ciscoIkeFlowCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIkeFlowCapSanOSV30R1MDS9000.setDescription('Cisco IKE Flow Monitoring\n                     MIB capabilities')
mibBuilder.exportSymbols("CISCO-IKE-FLOW-CAPABILITY", PYSNMP_MODULE_ID=ciscoIkeFlowCapability, ciscoIkeFlowCapSanOSV30R1MDS9000=ciscoIkeFlowCapSanOSV30R1MDS9000, ciscoIkeFlowCapability=ciscoIkeFlowCapability)
