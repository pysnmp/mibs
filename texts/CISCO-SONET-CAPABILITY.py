#
# PySNMP MIB module CISCO-SONET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SONET-CAPABILITY
# Source digest sha256:f516dea0e1f32f64ea8b90f967305c41b607b8113320ae7e77be92c8c16ff849
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSonetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 266))
ciscoSonetCapability.setRevisions(('2004-02-19 00:00', '2003-03-11 00:00', '2002-03-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSonetCapability.setRevisionsDescriptions(('Added ciscoSonetCapabilityV5R00.', 'Added ciscoSonetCapabilityV4R00 for modules:\n         10 Gig. ATM Switch Service Module(AXSM-XG),\n         AXSM Service Module Enhanced(AXSM-E) and \n         Processor Switch Module Enhanced(PXM1E)\n         controller card.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSonetCapability.setLastUpdated('2004-02-19 00:00')
if mibBuilder.loadTexts: ciscoSonetCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSonetCapability.setContactInfo('   Cisco Systems\n                        Customer Service\n                        \n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                        \n                           Tel: +1 800 553-NETS\n                        \n                        E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSonetCapability.setDescription('Agent capabilities for SONET-MIB(RFC 2558).\n \n          ciscoSonetCapabilityAxsmV2R01 for AXSM module.\n\n          ciscoSonetCapabilitySrmeV3R00 for SRME module.\n\n          ciscoSonetCapabilityAxsmxgV4R00 for AXSM-XG module.\n\n          ciscoSonetCapabilityV5R00 for VXSM, SRME and MPSM module.')
ciscoSonetCapabilityAxsmV2R0100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityAxsmV2R0100 = ciscoSonetCapabilityAxsmV2R0100.setProductRelease('MGX8850 Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityAxsmV2R0100 = ciscoSonetCapabilityAxsmV2R0100.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetCapabilityAxsmV2R0100.setDescription('Sonet MIB Capabilities for Following Service\n                      Modules:\n                        ATM Switch Service Module(AXSM)\n                        AXSM Enhanced(AXSM-E).')
ciscoSonetCapabilitySrmeV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilitySrmeV3R00 = ciscoSonetCapabilitySrmeV3R00.setProductRelease('MGX8850 Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilitySrmeV3R00 = ciscoSonetCapabilitySrmeV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetCapabilitySrmeV3R00.setDescription('Sonet MIB Capabilities for Service\n                         Resource Module Enhanced(SRME) module.')
ciscoSonetCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV4R00 = ciscoSonetCapabilityV4R00.setProductRelease('MGX8950  and MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV4R00 = ciscoSonetCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetCapabilityV4R00.setDescription('Sonet MIB Capabilities for Service Module:\n                      10 Gig. ATM Switch Service Module(AXSM-XG),\n                      AXSM Service Module Enhanced(AXSM-E) and \n                      Processor Switch Module Enhanced(PXM1E)\n                      controller card.')
ciscoSonetCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 266, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV5R00 = ciscoSonetCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetCapabilityV5R00 = ciscoSonetCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetCapabilityV5R00.setDescription('Sonet MIB capabilities for Voice Switch \n                          Service Module(VXSM), SRME and MPSM in \n                          release 5.0.0')
mibBuilder.exportSymbols("CISCO-SONET-CAPABILITY", PYSNMP_MODULE_ID=ciscoSonetCapability, ciscoSonetCapability=ciscoSonetCapability, ciscoSonetCapabilityAxsmV2R0100=ciscoSonetCapabilityAxsmV2R0100, ciscoSonetCapabilitySrmeV3R00=ciscoSonetCapabilitySrmeV3R00, ciscoSonetCapabilityV4R00=ciscoSonetCapabilityV4R00, ciscoSonetCapabilityV5R00=ciscoSonetCapabilityV5R00)
