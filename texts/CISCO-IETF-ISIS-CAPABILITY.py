#
# PySNMP MIB module CISCO-IETF-ISIS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-ISIS-CAPABILITY
# Source digest sha256:0100b06be0c1274d1b03d1d58aa966a9aa223fe55ed93a7703ac7d5a6a47ea4c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfIsisCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 446))
ciscoIetfIsisCapability.setRevisions(('2005-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfIsisCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setLastUpdated('2005-08-18 00:00')
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-clns@cisco.com')
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setDescription('Agent capabilities for CISCO-IETF-ISIS-MIB')
ciscoIetfIsisCapV12R0225SG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 446, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfIsisCapV12R0225SG = ciscoIetfIsisCapV12R0225SG.setProductRelease('Cisco IOS 12.2(25)SG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfIsisCapV12R0225SG = ciscoIetfIsisCapV12R0225SG.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfIsisCapV12R0225SG.setDescription('Cisco IS-IS MIB Agent Capabilities for IOS 12.2S')
mibBuilder.exportSymbols("CISCO-IETF-ISIS-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfIsisCapability, ciscoIetfIsisCapV12R0225SG=ciscoIetfIsisCapV12R0225SG, ciscoIetfIsisCapability=ciscoIetfIsisCapability)
