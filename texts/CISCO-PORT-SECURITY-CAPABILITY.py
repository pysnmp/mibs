#
# PySNMP MIB module CISCO-PORT-SECURITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PORT-SECURITY-CAPABILITY
# Source digest sha256:4edd9f005576d09c03c4ff3e6ac57d1c0e040ba5a3e1052849b27a34d16afc03
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPortSecurityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 393))
ciscoPortSecurityCapability.setRevisions(('2005-07-14 00:00', '2004-03-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPortSecurityCapability.setRevisionsDescriptions(('Added capability statement \n                 ciscoPSecureCapV12R0218SXFPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPortSecurityCapability.setLastUpdated('2005-07-14 00:00')
if mibBuilder.loadTexts: ciscoPortSecurityCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPortSecurityCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPortSecurityCapability.setDescription('The capabilities description of \n                 CISCO-PORT-SECURITY-MIB.')
ciscoPortSecurityC6kCapV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 393, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortSecurityC6kCapV08R0301 = ciscoPortSecurityC6kCapV08R0301.setProductRelease('Cisco CatOS 8.3(1) for Catalyst 6500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPortSecurityC6kCapV08R0301 = ciscoPortSecurityC6kCapV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoPortSecurityC6kCapV08R0301.setDescription('CISCO-PORT-SECURITY-MIB capabilities.')
ciscoPSecureCapV12R0218SXFPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 393, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPSecureCapV12R0218SXFPCat6K = ciscoPSecureCapV12R0218SXFPCat6K.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPSecureCapV12R0218SXFPCat6K = ciscoPSecureCapV12R0218SXFPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoPSecureCapV12R0218SXFPCat6K.setDescription('CISCO-PORT-SECURITY-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PORT-SECURITY-CAPABILITY", PYSNMP_MODULE_ID=ciscoPortSecurityCapability, ciscoPSecureCapV12R0218SXFPCat6K=ciscoPSecureCapV12R0218SXFPCat6K, ciscoPortSecurityC6kCapV08R0301=ciscoPortSecurityC6kCapV08R0301, ciscoPortSecurityCapability=ciscoPortSecurityCapability)
