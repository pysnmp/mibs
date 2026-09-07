#
# PySNMP MIB module CISCO-WAN-FR-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-FR-CONN-CAPABILITY
# Source digest sha256:8ec4e60ab04c13bcdc013905264508e5f581e65cc13f0a047200dec12f6946f7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanFrConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 358))
ciscoWanFrConnCapability.setRevisions(('2002-03-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanFrConnCapability.setRevisionsDescriptions(('Initial version of this MIB Module.',))
if mibBuilder.loadTexts: ciscoWanFrConnCapability.setLastUpdated('2002-03-27 00:00')
if mibBuilder.loadTexts: ciscoWanFrConnCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanFrConnCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanFrConnCapability.setDescription('The Agent Capabilities for Frame Relay\n            connection mib objects.\n\n            - The capability cwFrConnCapabilityFrsm12V3R00 is \n              for FRSM-12 module.')
cwFrConnCapabilityFrsm12V3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 358, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwFrConnCapabilityFrsm12V3R00 = cwFrConnCapabilityFrsm12V3R00.setProductRelease('MGX8850 Release 3.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwFrConnCapabilityFrsm12V3R00 = cwFrConnCapabilityFrsm12V3R00.setStatus('current')
if mibBuilder.loadTexts: cwFrConnCapabilityFrsm12V3R00.setDescription('Frame Relay Connection \n                         Agent Capabilities for\n                         Frame Relay Service Module(FRSM-12).')
mibBuilder.exportSymbols("CISCO-WAN-FR-CONN-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanFrConnCapability, ciscoWanFrConnCapability=ciscoWanFrConnCapability, cwFrConnCapabilityFrsm12V3R00=cwFrConnCapabilityFrsm12V3R00)
