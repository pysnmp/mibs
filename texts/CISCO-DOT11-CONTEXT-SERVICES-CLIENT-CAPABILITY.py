#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY
# Source digest sha256:2b4738331268fc53d17bab01250901266f9ba108cb2be78e1f30515ebf045ab5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDot11CscCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 336))
ciscoDot11CscCapability.setRevisions(('2004-07-24 00:00', '2003-08-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDot11CscCapability.setRevisionsDescriptions(('Added ciscoDot11CscCapabilityV2 for IOS \n                 12.3(2).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDot11CscCapability.setLastUpdated('2004-07-24 00:00')
if mibBuilder.loadTexts: ciscoDot11CscCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDot11CscCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoDot11CscCapability.setDescription('Agent capabilities for CISCO-CONTEXT-SERVICES-\n                 CLIENT-MIB')
ciscoDot11CscCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 336, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV1 = ciscoDot11CscCapabilityV1.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV1 = ciscoDot11CscCapabilityV1.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11CscCapabilityV1.setDescription('Cisco Dot11 CONTEXT SERVICES CLIENT\n                           MIB capabilities')
ciscoDot11CscCapabilityV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 336, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV2 = ciscoDot11CscCapabilityV2.setProductRelease('Cisco IOS 12.3(2) JA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscCapabilityV2 = ciscoDot11CscCapabilityV2.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11CscCapabilityV2.setDescription('Cisco Dot11 CONTEXT SERVICES CLIENT\n                         MIB capabilities for IOS 12.3(2).')
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-CAPABILITY", PYSNMP_MODULE_ID=ciscoDot11CscCapability, ciscoDot11CscCapability=ciscoDot11CscCapability, ciscoDot11CscCapabilityV1=ciscoDot11CscCapabilityV1, ciscoDot11CscCapabilityV2=ciscoDot11CscCapabilityV2)
