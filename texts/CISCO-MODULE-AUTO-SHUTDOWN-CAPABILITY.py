#
# PySNMP MIB module CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY
# Source digest sha256:96b151cb538f2b3518debb292dadcf060a75467b3f7b3c94fbfb286acd9bf70a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cmAutoShutdownCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 386))
cmAutoShutdownCapability.setRevisions(('2008-10-29 00:00', '2004-01-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmAutoShutdownCapability.setRevisionsDescriptions(('Add the capability statements\n        cmAutoShutdownCapV12R0233SXH3PCat6K and\n        cmAutoShutdownCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cmAutoShutdownCapability.setLastUpdated('2008-10-29 00:00')
if mibBuilder.loadTexts: cmAutoShutdownCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cmAutoShutdownCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cmAutoShutdownCapability.setDescription('The capabilities description of\n        CISCO-MODULE-AUTO-SHUTDOWN-MIB.')
cmAutoShutdownCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapCatOSV08R0301 = cmAutoShutdownCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapCatOSV08R0301 = cmAutoShutdownCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: cmAutoShutdownCapCatOSV08R0301.setDescription('CISCO-MODULE-AUTO-SHUTDOWN-MIB capabilities.')
cmAutoShutdownCapV12R0233SXH3PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXH3PCat6K = cmAutoShutdownCapV12R0233SXH3PCat6K.setProductRelease('Cisco IOS 12.2(33)SXH3 on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXH3PCat6K = cmAutoShutdownCapV12R0233SXH3PCat6K.setStatus('current')
if mibBuilder.loadTexts: cmAutoShutdownCapV12R0233SXH3PCat6K.setDescription('CISCO-MODULE-AUTO-SHUTDOWN-MIB capabilities.')
cmAutoShutdownCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXIPCat6K = cmAutoShutdownCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXIPCat6K = cmAutoShutdownCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cmAutoShutdownCapV12R0233SXIPCat6K.setDescription('CISCO-MODULE-AUTO-SHUTDOWN-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY", PYSNMP_MODULE_ID=cmAutoShutdownCapability, cmAutoShutdownCapCatOSV08R0301=cmAutoShutdownCapCatOSV08R0301, cmAutoShutdownCapV12R0233SXH3PCat6K=cmAutoShutdownCapV12R0233SXH3PCat6K, cmAutoShutdownCapV12R0233SXIPCat6K=cmAutoShutdownCapV12R0233SXIPCat6K, cmAutoShutdownCapability=cmAutoShutdownCapability)
