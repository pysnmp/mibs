#
# PySNMP MIB module CISCO-MAC-NOTIFICATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MAC-NOTIFICATION-CAPABILITY
# Source digest sha256:209c4579ddade539e70326f013dfa46fed63d6da82a83a135961f935118e6356
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMacNotificationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 327))
ciscoMacNotificationCapability.setRevisions(('2007-07-09 00:00', '2004-02-05 00:00', '2003-11-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMacNotificationCapability.setRevisionsDescriptions(('Add capability statement \n                 cmnCapabilityV12R0233SXHPCat6K.', 'Add capability statement \n                 cmnCapabilityCatOSV08R0301Cat6K and add\n                 VARIATION for cmnCapabilityV12R0217SXCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMacNotificationCapability.setLastUpdated('2007-07-09 00:00')
if mibBuilder.loadTexts: ciscoMacNotificationCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMacNotificationCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoMacNotificationCapability.setDescription('The capabilities description of \n                 CISCO-MAC-NOTIFICATION-MIB.')
cmnCapabilityCatOSV08R0101Cat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat4K = cmnCapabilityCatOSV08R0101Cat4K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 4000 series\n                        devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat4K = cmnCapabilityCatOSV08R0101Cat4K.setStatus('current')
if mibBuilder.loadTexts: cmnCapabilityCatOSV08R0101Cat4K.setDescription('CISCO-MAC-NOTIFICATION-MIB agent capabilities.')
cmnCapabilityCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat6K = cmnCapabilityCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat6K = cmnCapabilityCatOSV08R0101Cat6K.setStatus('current')
if mibBuilder.loadTexts: cmnCapabilityCatOSV08R0101Cat6K.setDescription('CISCO-MAC-NOTIFICATION-MIB agent capabilities.')
cmnCapabilityV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0217SXCat6K = cmnCapabilityV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0217SXCat6K = cmnCapabilityV12R0217SXCat6K.setStatus('current')
if mibBuilder.loadTexts: cmnCapabilityV12R0217SXCat6K.setDescription('CISCO-MAC-NOTIFICATION-MIB agent capabilities.')
cmnCapabilityCatOSV08R0301Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0301Cat6K = cmnCapabilityCatOSV08R0301Cat6K.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0301Cat6K = cmnCapabilityCatOSV08R0301Cat6K.setStatus('current')
if mibBuilder.loadTexts: cmnCapabilityCatOSV08R0301Cat6K.setDescription('CISCO-MAC-NOTIFICATION-MIB agent capabilities.')
cmnCapabilityV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0233SXHPCat6K = cmnCapabilityV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0233SXHPCat6K = cmnCapabilityV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: cmnCapabilityV12R0233SXHPCat6K.setDescription('CISCO-MAC-NOTIFICATION-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-MAC-NOTIFICATION-CAPABILITY", PYSNMP_MODULE_ID=ciscoMacNotificationCapability, ciscoMacNotificationCapability=ciscoMacNotificationCapability, cmnCapabilityCatOSV08R0101Cat4K=cmnCapabilityCatOSV08R0101Cat4K, cmnCapabilityCatOSV08R0101Cat6K=cmnCapabilityCatOSV08R0101Cat6K, cmnCapabilityCatOSV08R0301Cat6K=cmnCapabilityCatOSV08R0301Cat6K, cmnCapabilityV12R0217SXCat6K=cmnCapabilityV12R0217SXCat6K, cmnCapabilityV12R0233SXHPCat6K=cmnCapabilityV12R0233SXHPCat6K)
