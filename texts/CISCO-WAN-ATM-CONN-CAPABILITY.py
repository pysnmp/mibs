#
# PySNMP MIB module CISCO-WAN-ATM-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-ATM-CONN-CAPABILITY
# Source digest sha256:d4333d7aeb92229ddf5e819ab0f47626d65db169d936c241d4521b475366c1a1
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanAtmConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 380))
ciscoWanAtmConnCapability.setRevisions(('2004-02-07 00:00', '2002-03-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanAtmConnCapability.setRevisionsDescriptions(('Added cwAtmConnCapabilityV5R00 for MPSM155 & VXSM cards', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWanAtmConnCapability.setLastUpdated('2004-02-07 00:00')
if mibBuilder.loadTexts: ciscoWanAtmConnCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanAtmConnCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanAtmConnCapability.setDescription('The agent capabilities for CISCO-WAN-ATM-CONN-MIB\n\t\t in MGX8800 Series.\n                 - The capability cwAtmConnCapabilityAxsmV2R0160\n                   is for AXSM in MGX Release 2.1.60.\n                 - The capability cwAtmConnCapabilityAxsmeV2R0160\n                   is for AXSM-E in MGX Release 2.1.60.\n                 - The capability cwAtmConnCapabilityRpmprV2R0160\n                   is for RPM-PR in MGX Release 2.1.60.\n                 - The capability cwAtmConnCapabilityBpxsesV3R00 \n                   is for AXSM in MGX Release 3.0.00.\n                 - The capability cwAtmConnCapabilityAxsmV3R00 \n                   is for AXSM in MGX Release 3.0.00.\n                 - The capability cwAtmConnCapabilityAxsmeV3R00 \n                   is for AXSM-E in MGX Release 3.0.00.\n                 - The capability cwAtmConnCapabilityPxm1eV3R00 \n                   is for AXSM-E in MGX Release 3.0.00.\n                 - The capability cwAtmConnCapabilityRpmprV3R00\n                   is for RPM-PR in MGX Release 3.0.00.\n                 - The capability cwAtmConnCapabilityRpmxfV12R02\n                   is for RPM-XF in MGX Release 3.0.00.\n                 - The capability cwAtmConnCapabilityV5R00\n                   is for MPSM155 & VXSM in MGX Release 5.0.00.')
cwAtmConnCapabilityAxsmV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV2R0160 = cwAtmConnCapabilityAxsmV2R0160.setProductRelease('MGX8850 Release 2.1.60.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV2R0160 = cwAtmConnCapabilityAxsmV2R0160.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnCapabilityAxsmV2R0160.setDescription('Agent capabilities for ATM Switch\n                         Service Module(AXSM).')
cwAtmConnCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV2R0160 = cwAtmConnCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV2R0160 = cwAtmConnCapabilityAxsmeV2R0160.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnCapabilityAxsmeV2R0160.setDescription('Agent capabilities for Enhanced AXSM(AXSM-E).')
cwAtmConnCapabilityRpmprV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV2R0160 = cwAtmConnCapabilityRpmprV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV2R0160 = cwAtmConnCapabilityRpmprV2R0160.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnCapabilityRpmprV2R0160.setDescription('Agent capabilities for RPM-PR module.')
cwAtmConnCapabilityBpxsesV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityBpxsesV3R00 = cwAtmConnCapabilityBpxsesV3R00.setProductRelease('BPX SES Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityBpxsesV3R00 = cwAtmConnCapabilityBpxsesV3R00.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnCapabilityBpxsesV3R00.setDescription('Agent capabilities for BPX SES.')
cwAtmConnCapabilityAxsmV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV3R00 = cwAtmConnCapabilityAxsmV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV3R00 = cwAtmConnCapabilityAxsmV3R00.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnCapabilityAxsmV3R00.setDescription('Agent capabilities for AXSM module.')
cwAtmConnCapabilityAxsmeV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV3R00 = cwAtmConnCapabilityAxsmeV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV3R00 = cwAtmConnCapabilityAxsmeV3R00.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnCapabilityAxsmeV3R00.setDescription('Agent capabilities for AXSM-E module.')
cwAtmConnCapabilityPxm1eV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityPxm1eV3R00 = cwAtmConnCapabilityPxm1eV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityPxm1eV3R00 = cwAtmConnCapabilityPxm1eV3R00.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnCapabilityPxm1eV3R00.setDescription('Agent capabilities for PXM1-E module.')
cwAtmConnCapabilityRpmprV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV3R00 = cwAtmConnCapabilityRpmprV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV3R00 = cwAtmConnCapabilityRpmprV3R00.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnCapabilityRpmprV3R00.setDescription('Agent capabilities for RPM-PR module.')
cwAtmConnCapabilityRpmxfV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmxfV12R02 = cwAtmConnCapabilityRpmxfV12R02.setProductRelease('IOS Release 12.2\n                          in MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmxfV12R02 = cwAtmConnCapabilityRpmxfV12R02.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnCapabilityRpmxfV12R02.setDescription('Agent capabilities for RPM-XF module.')
cwAtmConnCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityV5R00 = cwAtmConnCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityV5R00 = cwAtmConnCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: cwAtmConnCapabilityV5R00.setDescription('Agent capabilities for MPSM155 and\n                          Voice Switch Service Module - VXSM')
mibBuilder.exportSymbols("CISCO-WAN-ATM-CONN-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanAtmConnCapability, ciscoWanAtmConnCapability=ciscoWanAtmConnCapability, cwAtmConnCapabilityAxsmV2R0160=cwAtmConnCapabilityAxsmV2R0160, cwAtmConnCapabilityAxsmV3R00=cwAtmConnCapabilityAxsmV3R00, cwAtmConnCapabilityAxsmeV2R0160=cwAtmConnCapabilityAxsmeV2R0160, cwAtmConnCapabilityAxsmeV3R00=cwAtmConnCapabilityAxsmeV3R00, cwAtmConnCapabilityBpxsesV3R00=cwAtmConnCapabilityBpxsesV3R00, cwAtmConnCapabilityPxm1eV3R00=cwAtmConnCapabilityPxm1eV3R00, cwAtmConnCapabilityRpmprV2R0160=cwAtmConnCapabilityRpmprV2R0160, cwAtmConnCapabilityRpmprV3R00=cwAtmConnCapabilityRpmprV3R00, cwAtmConnCapabilityRpmxfV12R02=cwAtmConnCapabilityRpmxfV12R02, cwAtmConnCapabilityV5R00=cwAtmConnCapabilityV5R00)
