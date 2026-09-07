#
# PySNMP MIB module CISCO-TELEPRESENCE-CALL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-TELEPRESENCE-CALL-CAPABILITY
# Source digest sha256:c783aae618e6ac430cf08774c923ab2ad3cc6e544ea4d3f9709c1dbb618e3140
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTelepresenceCallCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 577))
ciscoTelepresenceCallCapability.setRevisions(('2011-02-02 00:00', '2008-11-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setRevisionsDescriptions(('Added capability for Cisco Telepresence System (CTS) 1.7.0.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setLastUpdated('2011-02-02 00:00')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: tsbu-snmp-dev@cisco.com')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setDescription('Agent capabilities for CISCO-TELEPRESENCE-CALL-MIB')
ciscoTelepresenceCallCapabilityCTSV150 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 577, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV150 = ciscoTelepresenceCallCapabilityCTSV150.setProductRelease('Cisco TelePresence System (CTS) 1.5.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV150 = ciscoTelepresenceCallCapabilityCTSV150.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapabilityCTSV150.setDescription('TELEPRESENCE CALL MIB capabilities')
ciscoTelepresenceCallCapabilityCTSV170 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 577, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV170 = ciscoTelepresenceCallCapabilityCTSV170.setProductRelease('Cisco TelePresence System (CTS) 1.7.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV170 = ciscoTelepresenceCallCapabilityCTSV170.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapabilityCTSV170.setDescription('TELEPRESENCE CALL MIB capabilities')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-CALL-CAPABILITY", PYSNMP_MODULE_ID=ciscoTelepresenceCallCapability, ciscoTelepresenceCallCapability=ciscoTelepresenceCallCapability, ciscoTelepresenceCallCapabilityCTSV150=ciscoTelepresenceCallCapabilityCTSV150, ciscoTelepresenceCallCapabilityCTSV170=ciscoTelepresenceCallCapabilityCTSV170)
