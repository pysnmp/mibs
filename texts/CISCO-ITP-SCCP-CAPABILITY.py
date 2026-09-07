#
# PySNMP MIB module CISCO-ITP-SCCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-SCCP-CAPABILITY
# Source digest sha256:9c1196e929d337d66251b7274a09a9b10b441a5966fdd5dc0174076b784e200a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpSccpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 221))
ciscoItpSccpCapability.setRevisions(('2002-03-04 00:00', '2001-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpSccpCapability.setRevisionsDescriptions(('Changes required for the following modifications\n                    to the CISCO-ITP-SCCP-MIB.\n                    \n                    Added the following objects:\n                       CItpSccpGttPrefName\n                       cItpSccpPrefConfigLastChanged\n                       cItpSccpGttPrePrefConv\n                       cItpSccpGttPostPrefConv\n                       cItpSccpGttGtaAddrDispZB\n                       cItpSccpGttGtaAddrLenZB\n                       cItpSccpGttGtaAsName\n\n                    Added the following Tables:\n                       cItpSccpGttAppGrTable\n                       cItpSccpGttPrefTable\n\n                    Updated the following Textual Conventions:\n                       CItpSccpGttAppType\n                       CItpSccpGttGtaResType\n\n                    Deprecated the following objects:\n                       CItpSccpGttGtaAddrLen\n                       cItpSccpGttGtaAddrDisp\n                       cItpSccpGttGtaAddrLen\n\n                    Deprecated the following Tables:\n                       cItpSccpGttAppTable', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpSccpCapability.setLastUpdated('2002-03-04 00:00')
if mibBuilder.loadTexts: ciscoItpSccpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpSccpCapability.setContactInfo('       Cisco Systems\n                                Customer Service\n                        \n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                        \n                           Tel: +1 800 553-NETS\n                        \n                        E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpSccpCapability.setDescription('Agent capabilities for the CISCO-ITP-SCCP-MIB.')
ciscoItpSccpCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 221, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R024MB1 = ciscoItpSccpCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R024MB1 = ciscoItpSccpCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoItpSccpCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-ITP-SCCP-MIB.my User Agent\n                   MIB capabilities.')
ciscoItpSccpCapabilityV12R0204MB4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 221, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R0204MB4 = ciscoItpSccpCapabilityV12R0204MB4.setProductRelease('Cisco IOS 12.2(4)MB4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R0204MB4 = ciscoItpSccpCapabilityV12R0204MB4.setStatus('current')
if mibBuilder.loadTexts: ciscoItpSccpCapabilityV12R0204MB4.setDescription('IOS 12.2(4)MB4 Cisco CISCO-ITP-SCCP-MIB.my User Agent\n                   MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-SCCP-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpSccpCapability, ciscoItpSccpCapability=ciscoItpSccpCapability, ciscoItpSccpCapabilityV12R0204MB4=ciscoItpSccpCapabilityV12R0204MB4, ciscoItpSccpCapabilityV12R024MB1=ciscoItpSccpCapabilityV12R024MB1)
