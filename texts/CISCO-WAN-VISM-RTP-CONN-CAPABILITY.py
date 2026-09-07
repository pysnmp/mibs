#
# PySNMP MIB module CISCO-WAN-VISM-RTP-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-VISM-RTP-CONN-CAPABILITY
# Source digest sha256:a699a4e666c48a8ad0b40d42f8f046de26a2da8b8279191a470025b77b34337e
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwVismRtpConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 337))
cwVismRtpConnCapability.setRevisions(('2001-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cwVismRtpConnCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: cwVismRtpConnCapability.setLastUpdated('2001-08-22 00:00')
if mibBuilder.loadTexts: cwVismRtpConnCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cwVismRtpConnCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: cwVismRtpConnCapability.setDescription('The Agent Capabilities for CISCO-WAN-RTP-CONN-MIB.')
cwVismRtpConnCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 337, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismRtpConnCapabilityV2R00 = cwVismRtpConnCapabilityV2R00.setProductRelease('VISM Release2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismRtpConnCapabilityV2R00 = cwVismRtpConnCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: cwVismRtpConnCapabilityV2R00.setDescription('CISCO-WAN-RTP-CONN-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-RTP-CONN-CAPABILITY", PYSNMP_MODULE_ID=cwVismRtpConnCapability, cwVismRtpConnCapability=cwVismRtpConnCapability, cwVismRtpConnCapabilityV2R00=cwVismRtpConnCapabilityV2R00)
