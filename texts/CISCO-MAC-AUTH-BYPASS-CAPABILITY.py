#
# PySNMP MIB module CISCO-MAC-AUTH-BYPASS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MAC-AUTH-BYPASS-CAPABILITY
# Source digest sha256:3bfe73ac68d810c36783082455e79e676108b62199791d8286039b792154d695
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMacAuthBypassCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 574))
ciscoMacAuthBypassCapability.setRevisions(('2010-03-09 00:00', '2008-10-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setRevisionsDescriptions(('Added capability statement ciscoMabCapV12R0252SGPCat4K.\n\n        Added more VARIATION for ciscoMabCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setLastUpdated('2010-03-09 00:00')
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n                E-mail: cs-ibns@cisco.com,\n                        cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setDescription('The capabilities description of CISCO-MAC-AUTH-BYPASS-MIB.')
ciscoMabCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 574, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0233SXIPCat6K = ciscoMabCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0233SXIPCat6K = ciscoMabCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoMabCapV12R0233SXIPCat6K.setDescription('CISCO-MAC-AUTH-BYPASS-MIB capabilities.')
ciscoMabCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 574, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0252SGPCat4K = ciscoMabCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0252SGPCat4K = ciscoMabCapV12R0252SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoMabCapV12R0252SGPCat4K.setDescription('CISCO-MAC-AUTH-BYPASS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MAC-AUTH-BYPASS-CAPABILITY", PYSNMP_MODULE_ID=ciscoMacAuthBypassCapability, ciscoMabCapV12R0233SXIPCat6K=ciscoMabCapV12R0233SXIPCat6K, ciscoMabCapV12R0252SGPCat4K=ciscoMabCapV12R0252SGPCat4K, ciscoMacAuthBypassCapability=ciscoMacAuthBypassCapability)
