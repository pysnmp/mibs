#
# PySNMP MIB module CISCO-CATOS-ACL-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CATOS-ACL-QOS-CAPABILITY
# Source digest sha256:6acc7fbd1ed5e226c408caceec6ce414a72a2444c4e7f3f055ff074341e69f70
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCatOSAclQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 325))
ciscoCatOSAclQosCapability.setRevisions(('2008-03-17 00:00', '2006-06-29 00:00', '2005-09-06 00:00', '2004-06-24 00:00', '2004-01-27 00:00', '2003-12-19 00:00', '2003-08-25 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCatOSAclQosCapability.setRevisionsDescriptions(('Add caqCapabilityV08R0701Cat6KPfc, \n                 caqCapabilityV08R0701Cat6KPfc2,\n                 caqCapabilityV08R0701Cat6KPfc3,\n                 caqCapabilityV08R0701Cat6KPfc3b\n                 agent capability statements.', 'Add caqCapabilityV08R0601Cat6KPfc, \n                 caqCapabilityV08R0601Cat6KPfc2,\n                 caqCapabilityV08R0601Cat6KPfc3,\n                 caqCapabilityV08R0601Cat6KPfc3b\n                 agent capability statements.', 'Add caqCapabilityV08R0501Cat6KPfc, \n                 caqCapabilityV08R0501Cat6KPfc2,\n                 caqCapabilityV08R0501Cat6KPfc3,\n                 caqCapabilityV08R0501Cat6KPfc3b\n                 agent capability statements.\n\n                 Add VARIATION clauses for caqIpAceProtocolMatchCriteria\n                 object in all existing agent capability statements.', 'Add caqCapabilityV08R0401Cat6KPfc, \n                 caqCapabilityV08R0401Cat6KPfc2,\n                 caqCapabilityV08R0401Cat6KPfc3,\n                 caqCapabilityV08R0401Cat6KPfc3b\n                 agent capability statements.', 'Add caqCapabilityV08R0301Cat6KPfc, \n                 caqCapabilityV08R0301Cat6KPfc2,\n                 caqCapabilityV08R0301Cat6KPfc3\n                 agent capability statements.', 'Correct BITS syntax typo.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCatOSAclQosCapability.setLastUpdated('2008-03-17 00:00')
if mibBuilder.loadTexts: ciscoCatOSAclQosCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCatOSAclQosCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCatOSAclQosCapability.setDescription('The agent capabilities description of \n                 CISCO-CATOS-ACL-QOS-MIB.')
caqCapabilityV08R0101Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc = caqCapabilityV08R0101Cat6KPfc.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc = caqCapabilityV08R0101Cat6KPfc.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0101Cat6KPfc.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0101Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc2 = caqCapabilityV08R0101Cat6KPfc2.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc2 = caqCapabilityV08R0101Cat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0101Cat6KPfc2.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0101Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc3 = caqCapabilityV08R0101Cat6KPfc3.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc3 = caqCapabilityV08R0101Cat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0101Cat6KPfc3.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0101Cat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat4K = caqCapabilityV08R0101Cat4K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 4000 series\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat4K = caqCapabilityV08R0101Cat4K.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0101Cat4K.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0301Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc = caqCapabilityV08R0301Cat6KPfc.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc = caqCapabilityV08R0301Cat6KPfc.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0301Cat6KPfc.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0301Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc2 = caqCapabilityV08R0301Cat6KPfc2.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc2 = caqCapabilityV08R0301Cat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0301Cat6KPfc2.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0301Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc3 = caqCapabilityV08R0301Cat6KPfc3.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc3 = caqCapabilityV08R0301Cat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0301Cat6KPfc3.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0401Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc = caqCapabilityV08R0401Cat6KPfc.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc = caqCapabilityV08R0401Cat6KPfc.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0401Cat6KPfc.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0401Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc2 = caqCapabilityV08R0401Cat6KPfc2.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc2 = caqCapabilityV08R0401Cat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0401Cat6KPfc2.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0401Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3 = caqCapabilityV08R0401Cat6KPfc3.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3 = caqCapabilityV08R0401Cat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0401Cat6KPfc3.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0401Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3b = caqCapabilityV08R0401Cat6KPfc3b.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3b = caqCapabilityV08R0401Cat6KPfc3b.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0401Cat6KPfc3b.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0501Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc = caqCapabilityV08R0501Cat6KPfc.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc = caqCapabilityV08R0501Cat6KPfc.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0501Cat6KPfc.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0501Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc2 = caqCapabilityV08R0501Cat6KPfc2.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc2 = caqCapabilityV08R0501Cat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0501Cat6KPfc2.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0501Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3 = caqCapabilityV08R0501Cat6KPfc3.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3 = caqCapabilityV08R0501Cat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0501Cat6KPfc3.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0501Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3b = caqCapabilityV08R0501Cat6KPfc3b.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3b = caqCapabilityV08R0501Cat6KPfc3b.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0501Cat6KPfc3b.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0601Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc = caqCapabilityV08R0601Cat6KPfc.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc = caqCapabilityV08R0601Cat6KPfc.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0601Cat6KPfc.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0601Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc2 = caqCapabilityV08R0601Cat6KPfc2.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc2 = caqCapabilityV08R0601Cat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0601Cat6KPfc2.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0601Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3 = caqCapabilityV08R0601Cat6KPfc3.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3 = caqCapabilityV08R0601Cat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0601Cat6KPfc3.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0601Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3b = caqCapabilityV08R0601Cat6KPfc3b.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3b = caqCapabilityV08R0601Cat6KPfc3b.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0601Cat6KPfc3b.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0701Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc = caqCapabilityV08R0701Cat6KPfc.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc = caqCapabilityV08R0701Cat6KPfc.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0701Cat6KPfc.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0701Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc2 = caqCapabilityV08R0701Cat6KPfc2.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc2 = caqCapabilityV08R0701Cat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0701Cat6KPfc2.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0701Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3 = caqCapabilityV08R0701Cat6KPfc3.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3 = caqCapabilityV08R0701Cat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0701Cat6KPfc3.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
caqCapabilityV08R0701Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3b = caqCapabilityV08R0701Cat6KPfc3b.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3b = caqCapabilityV08R0701Cat6KPfc3b.setStatus('current')
if mibBuilder.loadTexts: caqCapabilityV08R0701Cat6KPfc3b.setDescription('CISCO-CATOS-ACL-QOS-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-CATOS-ACL-QOS-CAPABILITY", PYSNMP_MODULE_ID=ciscoCatOSAclQosCapability, caqCapabilityV08R0101Cat4K=caqCapabilityV08R0101Cat4K, caqCapabilityV08R0101Cat6KPfc2=caqCapabilityV08R0101Cat6KPfc2, caqCapabilityV08R0101Cat6KPfc3=caqCapabilityV08R0101Cat6KPfc3, caqCapabilityV08R0101Cat6KPfc=caqCapabilityV08R0101Cat6KPfc, caqCapabilityV08R0301Cat6KPfc2=caqCapabilityV08R0301Cat6KPfc2, caqCapabilityV08R0301Cat6KPfc3=caqCapabilityV08R0301Cat6KPfc3, caqCapabilityV08R0301Cat6KPfc=caqCapabilityV08R0301Cat6KPfc, caqCapabilityV08R0401Cat6KPfc2=caqCapabilityV08R0401Cat6KPfc2, caqCapabilityV08R0401Cat6KPfc3=caqCapabilityV08R0401Cat6KPfc3, caqCapabilityV08R0401Cat6KPfc3b=caqCapabilityV08R0401Cat6KPfc3b, caqCapabilityV08R0401Cat6KPfc=caqCapabilityV08R0401Cat6KPfc, caqCapabilityV08R0501Cat6KPfc2=caqCapabilityV08R0501Cat6KPfc2, caqCapabilityV08R0501Cat6KPfc3=caqCapabilityV08R0501Cat6KPfc3, caqCapabilityV08R0501Cat6KPfc3b=caqCapabilityV08R0501Cat6KPfc3b, caqCapabilityV08R0501Cat6KPfc=caqCapabilityV08R0501Cat6KPfc, caqCapabilityV08R0601Cat6KPfc2=caqCapabilityV08R0601Cat6KPfc2, caqCapabilityV08R0601Cat6KPfc3=caqCapabilityV08R0601Cat6KPfc3, caqCapabilityV08R0601Cat6KPfc3b=caqCapabilityV08R0601Cat6KPfc3b, caqCapabilityV08R0601Cat6KPfc=caqCapabilityV08R0601Cat6KPfc, caqCapabilityV08R0701Cat6KPfc2=caqCapabilityV08R0701Cat6KPfc2, caqCapabilityV08R0701Cat6KPfc3=caqCapabilityV08R0701Cat6KPfc3, caqCapabilityV08R0701Cat6KPfc3b=caqCapabilityV08R0701Cat6KPfc3b, caqCapabilityV08R0701Cat6KPfc=caqCapabilityV08R0701Cat6KPfc, ciscoCatOSAclQosCapability=ciscoCatOSAclQosCapability)
