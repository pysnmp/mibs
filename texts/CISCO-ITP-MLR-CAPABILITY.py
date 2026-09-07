#
# PySNMP MIB module CISCO-ITP-MLR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-MLR-CAPABILITY
# Source digest sha256:1db201c2a634cb27ed529871850f9be5f31af0f372cf1c535a6b77380606d20b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMlrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 423))
ciscoMlrCapability.setRevisions(('2007-05-18 00:00', '2006-10-05 00:00', '2005-02-18 00:00', '2004-04-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMlrCapability.setRevisionsDescriptions(('Added ciscoMlrCapabilityV12R0411SW capabilities statement.', 'Added ciscoMlrCapabilityV12R0218IXA capabilities statement.', 'Added ciscoMlrCapabilityV12R0225SW01 capability\n        statement. Replace the ciscoMlrRuleSetGroup\n        group with ciscoMlrRuleSetGroupRev2 to support\n        additional rule parameters.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMlrCapability.setLastUpdated('2007-05-18 00:00')
if mibBuilder.loadTexts: ciscoMlrCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMlrCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoMlrCapability.setDescription('Agent capabilities for the CISCO-ITP-MLR-MIB.')
ciscoMlrCapabilityV12R0221SW01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0221SW01 = ciscoMlrCapabilityV12R0221SW01.setProductRelease('Cisco IOS 12.2(21)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0221SW01 = ciscoMlrCapabilityV12R0221SW01.setStatus('current')
if mibBuilder.loadTexts: ciscoMlrCapabilityV12R0221SW01.setDescription('IOS 12.2(21)SW1 Cisco CISCO-ITP-MLR-MIB.my\n        User Agent MIB capabilities.')
ciscoMlrCapabilityV12R0225SW01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0225SW01 = ciscoMlrCapabilityV12R0225SW01.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0225SW01 = ciscoMlrCapabilityV12R0225SW01.setStatus('current')
if mibBuilder.loadTexts: ciscoMlrCapabilityV12R0225SW01.setDescription('IOS 12.2(25)SW1 Cisco CISCO-ITP-MLR-MIB.my\n        User Agent MIB capabilities.')
ciscoMlrCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0218IXA = ciscoMlrCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0218IXA = ciscoMlrCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoMlrCapabilityV12R0218IXA.setDescription('IOS 12.2(18)IXA Cisco CISCO-ITP-MLR-MIB.my\n        User Agent MIB capabilities.')
ciscoMlrCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0411SW = ciscoMlrCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0411SW = ciscoMlrCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoMlrCapabilityV12R0411SW.setDescription('Cisco IOS 12.4(11)SW CISCO-ITP-MLR-MIB.my\n        User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-MLR-CAPABILITY", PYSNMP_MODULE_ID=ciscoMlrCapability, ciscoMlrCapability=ciscoMlrCapability, ciscoMlrCapabilityV12R0218IXA=ciscoMlrCapabilityV12R0218IXA, ciscoMlrCapabilityV12R0221SW01=ciscoMlrCapabilityV12R0221SW01, ciscoMlrCapabilityV12R0225SW01=ciscoMlrCapabilityV12R0225SW01, ciscoMlrCapabilityV12R0411SW=ciscoMlrCapabilityV12R0411SW)
