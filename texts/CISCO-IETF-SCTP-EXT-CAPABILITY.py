#
# PySNMP MIB module CISCO-IETF-SCTP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-SCTP-EXT-CAPABILITY
# Source digest sha256:1d312b8737ef84c1e65ed314ea5c9ca92661b4483259b5f570b3c1294801511f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSctpExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 220))
ciscoSctpExtCapability.setRevisions(('2002-01-21 00:00', '2001-11-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSctpExtCapability.setRevisionsDescriptions(('Updated capabilities to support additional objects\n                 and a new notification.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSctpExtCapability.setLastUpdated('2002-01-21 00:00')
if mibBuilder.loadTexts: ciscoSctpExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSctpExtCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n                \n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n                \n                   Tel: +1 800 553-NETS\n                \n                E-mail: cs-sctp@cisco.com')
if mibBuilder.loadTexts: ciscoSctpExtCapability.setDescription('Agent capabilities for the CISCO-IETF-SCTP-EXT-MIB.')
ciscoSctpExtCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 220, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R024MB1 = ciscoSctpExtCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R024MB1 = ciscoSctpExtCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoSctpExtCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-IETF-SCTP-EXT-MIB.my\n                      User Agent MIB capabilities.')
ciscoSctpExtCapabilityV12R0204MB3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 220, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R0204MB3 = ciscoSctpExtCapabilityV12R0204MB3.setProductRelease('Cisco IOS 12.2(4)MB3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSctpExtCapabilityV12R0204MB3 = ciscoSctpExtCapabilityV12R0204MB3.setStatus('current')
if mibBuilder.loadTexts: ciscoSctpExtCapabilityV12R0204MB3.setDescription('IOS 12.2(4)MB3 Cisco CISCO-IETF-SCTP-EXT-MIB.my\n                     User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IETF-SCTP-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoSctpExtCapability, ciscoSctpExtCapability=ciscoSctpExtCapability, ciscoSctpExtCapabilityV12R0204MB3=ciscoSctpExtCapabilityV12R0204MB3, ciscoSctpExtCapabilityV12R024MB1=ciscoSctpExtCapabilityV12R024MB1)
