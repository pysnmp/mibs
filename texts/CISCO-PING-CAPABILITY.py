#
# PySNMP MIB module CISCO-PING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PING-CAPABILITY
# Source digest sha256:2ac4be49275655dc2f76f0d9149abf24974dd6786da0c375229c0a0454b8e84c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 36))
ciscoPingCapability.setRevisions(('2006-03-15 00:00', '2004-06-14 00:00', '2004-01-19 00:00', '1994-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPingCapability.setRevisionsDescriptions(('Add VARIATION for notification \n                 ciscoPingCompletion in \n                 ciscoPingCapabilityCatOSV08R0301.', 'Fix the typo in the supporting for the CatOS\n                 platform for this MIB module.', 'Add supporting for the CatOS platform for\n                 this MIB module.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPingCapability.setLastUpdated('2006-03-15 00:00')
if mibBuilder.loadTexts: ciscoPingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPingCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n                        \n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n                        \n                   Tel: +1 800 553-NETS\n                        \n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPingCapability.setDescription('Agent capabilities for CISCO-PING-MIB.')
ciscoPingCapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 36, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityV10R02 = ciscoPingCapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityV10R02 = ciscoPingCapabilityV10R02.setStatus('current')
if mibBuilder.loadTexts: ciscoPingCapabilityV10R02.setDescription('Cisco Ping MIB capabilities.')
ciscoPingCapabilityCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 36, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityCatOSV08R0301 = ciscoPingCapabilityCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPingCapabilityCatOSV08R0301 = ciscoPingCapabilityCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoPingCapabilityCatOSV08R0301.setDescription('CISCO-PING-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PING-CAPABILITY", PYSNMP_MODULE_ID=ciscoPingCapability, ciscoPingCapability=ciscoPingCapability, ciscoPingCapabilityCatOSV08R0301=ciscoPingCapabilityCatOSV08R0301, ciscoPingCapabilityV10R02=ciscoPingCapabilityV10R02)
