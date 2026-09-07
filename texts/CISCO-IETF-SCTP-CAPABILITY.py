#
# PySNMP MIB module CISCO-IETF-SCTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-SCTP-CAPABILITY
# Source digest sha256:eb0882cc1b94a34e10ad1939b99d4e905db02bcaa11e40b670029f7317fed4a5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSctpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 215))
ciscoSctpCapability.setRevisions(('2001-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSctpCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSctpCapability.setLastUpdated('2001-10-24 00:00')
if mibBuilder.loadTexts: ciscoSctpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSctpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n                \n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n                \n                   Tel: +1 800 553-NETS\n                \n                E-mail: cs-sctp@cisco.com')
if mibBuilder.loadTexts: ciscoSctpCapability.setDescription('Agent capabilities for the CISCO-IETF-SCTP-MIB.')
ciscoSctpCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 215, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpCapabilityV12R024MB1 = ciscoSctpCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpCapabilityV12R024MB1 = ciscoSctpCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoSctpCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-IETF-SCTP-MIB.my User Agent\n                   MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IETF-SCTP-CAPABILITY", PYSNMP_MODULE_ID=ciscoSctpCapability, ciscoSctpCapability=ciscoSctpCapability, ciscoSctpCapabilityV12R024MB1=ciscoSctpCapabilityV12R024MB1)
