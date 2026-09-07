#
# PySNMP MIB module CISCO-DS1-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DS1-CAPABILITY
# Source digest sha256:2e70592bb64a6a220de9389c5a1d7ce4a909d906bae86b1e38beb8c82ac5ceb4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDs1Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 273))
ciscoDs1Capability.setRevisions(('2007-10-31 00:00', '2007-09-10 00:00', '2007-05-11 00:00', '2006-06-16 00:00', '2005-07-11 00:00', '2003-12-22 00:00', '2002-04-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDs1Capability.setRevisionsDescriptions(('Added VARIATION for dsx1LineStatusChangeTrapEnable to\n        agent capability statement ciscoDs1CapabilityMARsV12R5T\n        and ciscoDs1CapabilityAS5xxxV12R5T', 'Added ciscoDs1CapabilityV5R500 for defining capability for\n         VXSM support in MGX8880 release 5.5.0.', 'Added ciscoDs1CapabilityMARsV12R5T for 2800, 3800, 3700 series\n        routers and IAD2430 platforms. \n        Added ciscoDs1CapabilityAS5xxxV12R5T for AS5xxx platforms.', 'Added ciscoDs1CapabilityV5R310 for VXSM support in\n        MGX8880 release 5.3.1.', 'Added ciscoDs1CapabilityV5R100 for MPSM and VXSM support in\n        MGX8880 release 5.1.0.', 'ciscoDs1CapabilityV5R00 added for MPSM and VXSM support.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDs1Capability.setLastUpdated('2007-10-31 00:00')
if mibBuilder.loadTexts: ciscoDs1Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDs1Capability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoDs1Capability.setDescription('The agent capabilities for DS1-MIB for Cisco Products Series.\n        - ciscoDs1AxsmeCapabilityV3R00 is for\n          Enhanced ATM Switch Service Module(AXSM-E), and\n          Enhanced Processor Switch Module 1(PXM1E) uplink.\n\n        - ciscoDs1CapabilityV5R00 is for Voice Switch\n          Service Module(VXSM) and MPSM Module Release 5.0.0.')
ciscoDs1AxsmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1AxsmeCapabilityV3R00 = ciscoDs1AxsmeCapabilityV3R00.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1AxsmeCapabilityV3R00 = ciscoDs1AxsmeCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1AxsmeCapabilityV3R00.setDescription('DS1-MIB Capabilities.')
ciscoDs1CapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R00 = ciscoDs1CapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R00 = ciscoDs1CapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityV5R00.setDescription('DS1 MIB capabilities for VXSM and\n        MPSM in release 5.0.0')
ciscoDs1CapabilityV5R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R100 = ciscoDs1CapabilityV5R100.setProductRelease('MGX8880 Release 5.1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R100 = ciscoDs1CapabilityV5R100.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityV5R100.setDescription('DS1 MIB capabilities for VXSM and\n        MPSM in release 5.1.0')
ciscoDs1CapabilityV5R310 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R310 = ciscoDs1CapabilityV5R310.setProductRelease('MGX8880 Release 5.3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R310 = ciscoDs1CapabilityV5R310.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityV5R310.setDescription('DS1 MIB capabilities for VXSM\n        in release 5.3.1')
ciscoDs1CapabilityMARsV12R5T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityMARsV12R5T = ciscoDs1CapabilityMARsV12R5T.setProductRelease('IOS 12.5T for Cisco Access Routers and ISRs')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityMARsV12R5T = ciscoDs1CapabilityMARsV12R5T.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityMARsV12R5T.setDescription('Agent capabilities for Cisco 3700 series routers, IAD2430\n        and 2800, 3800 Series Integrated Services Routers.')
ciscoDs1CapabilityAS5xxxV12R5T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityAS5xxxV12R5T = ciscoDs1CapabilityAS5xxxV12R5T.setProductRelease('IOS 12.5T for Cisco Access Servers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityAS5xxxV12R5T = ciscoDs1CapabilityAS5xxxV12R5T.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityAS5xxxV12R5T.setDescription('Agent capabilities for Cisco AS5xxx routers.')
ciscoDs1CapabilityV5R500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R500 = ciscoDs1CapabilityV5R500.setProductRelease('MGX8880 Release 5.5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R500 = ciscoDs1CapabilityV5R500.setStatus('current')
if mibBuilder.loadTexts: ciscoDs1CapabilityV5R500.setDescription('DS1 MIB capabilities for VXSM\n        in release 5.5.0.')
mibBuilder.exportSymbols("CISCO-DS1-CAPABILITY", PYSNMP_MODULE_ID=ciscoDs1Capability, ciscoDs1AxsmeCapabilityV3R00=ciscoDs1AxsmeCapabilityV3R00, ciscoDs1Capability=ciscoDs1Capability, ciscoDs1CapabilityAS5xxxV12R5T=ciscoDs1CapabilityAS5xxxV12R5T, ciscoDs1CapabilityMARsV12R5T=ciscoDs1CapabilityMARsV12R5T, ciscoDs1CapabilityV5R00=ciscoDs1CapabilityV5R00, ciscoDs1CapabilityV5R100=ciscoDs1CapabilityV5R100, ciscoDs1CapabilityV5R310=ciscoDs1CapabilityV5R310, ciscoDs1CapabilityV5R500=ciscoDs1CapabilityV5R500)
