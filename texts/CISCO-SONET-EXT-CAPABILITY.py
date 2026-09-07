#
# PySNMP MIB module CISCO-SONET-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SONET-EXT-CAPABILITY
# Source digest sha256:9df359fbda643a82880d996e63dc6950280e43028cbf44bf2ac1fc21b762438b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSonetExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 261))
ciscoSonetExtCapability.setRevisions(('2003-12-23 00:00', '2003-03-13 00:00', '2002-02-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSonetExtCapability.setRevisionsDescriptions(('Added ciscoSonetExtCapabilityV5R00.', 'Added ciscoSonetExtCapabilityV4R00 for modules:\n      ATM Switch Service Module(AXSM),\n      10 Gig. ATM Switch Service Module(AXSM-XG),\n      Enhanced ATM Switch Service Module(AXSM-E) and\n      Processor Switch Module Enhanced (PXM1E).', 'Initial Version of the MIB module.',))
if mibBuilder.loadTexts: ciscoSonetExtCapability.setLastUpdated('2003-12-23 00:00')
if mibBuilder.loadTexts: ciscoSonetExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSonetExtCapability.setContactInfo('    Cisco Systems\n             Customer Service\n\n        Postal: 170 W Tasman Drive\n             San Jose, CA  95134\n             USA\n\n             Tel: +1 800 553-NETS\n\n        E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSonetExtCapability.setDescription('The Agent Capabilities for CISCO-SONET-MIB.\n\n      - ciscoSonetExtAxsmCapabilityV2R00 is for \n        ATM Switch Service Module(AXSM).\n\n      - ciscoSonetExtAxsmCapabilityV2R11 is for \n        ATM Switch Service Module(AXSM).\n\n      - ciscoSonetExtAxsmeCapabilityV21R60 is for\n        Enhanced ATM Switch Service Module(AXSM-E).\n\n      - ciscoSonetExtCapabilityV5R000 is for\n        Service Resource Module(SRM-E).\n\n      - ciscoSonetExtSrmeCapabilityV3R00 is for\n        Voice Switch Service Module(VXSM)\n\n      - ciscoSonetExtSrmeCapabilityV3R00 is for\n        Service Resource Module(SRM-E).\n\n      - ciscoSonetExtCapabilityV4R00 is for\n        10 Gig. ATM Switch Service Module(AXSM-XG) and\n        Enhanced ATM Switch Service Module(AXSM-E).\n\n      - ciscoSonetExtCapabilityV5R000 is for\n        Voice Switch Service Module(VXSM) and MPSM.')
ciscoSonetExtAxsmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R00 = ciscoSonetExtAxsmCapabilityV2R00.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R00 = ciscoSonetExtAxsmCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtAxsmCapabilityV2R00.setDescription('CISCO-SONET-MIB Capabilities for\n                     ATM Switch Service Module(AXSM).')
ciscoSonetExtAxsmCapabilityV2R11 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R11 = ciscoSonetExtAxsmCapabilityV2R11.setProductRelease('MGX8850 Release 2.0.11')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmCapabilityV2R11 = ciscoSonetExtAxsmCapabilityV2R11.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtAxsmCapabilityV2R11.setDescription('CISCO-SONET-MIB Capabilities for\n                  ATM Switch Service Module(AXSM).')
ciscoSonetExtAxsmeCapabilityV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmeCapabilityV21R60 = ciscoSonetExtAxsmeCapabilityV21R60.setProductRelease('MGX8850 Release 2.1.60.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtAxsmeCapabilityV21R60 = ciscoSonetExtAxsmeCapabilityV21R60.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtAxsmeCapabilityV21R60.setDescription('CISCO-SONET-MIB Capabilities for\n                  AXSM-E Service Modules.')
ciscoSonetExtSrmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtSrmeCapabilityV3R00 = ciscoSonetExtSrmeCapabilityV3R00.setProductRelease('MGX8800 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtSrmeCapabilityV3R00 = ciscoSonetExtSrmeCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtSrmeCapabilityV3R00.setDescription('CISCO-SONET-MIB Capabilities of \n                  Enhanced Service Resource Module(SRM-E).')
ciscoSonetExtCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV4R00 = ciscoSonetExtCapabilityV4R00.setProductRelease('MGX8850, MGX8950 Release 4.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV4R00 = ciscoSonetExtCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtCapabilityV4R00.setDescription('CISCO-SONET-MIB Capabilities for\n                     AXSM, AXSM-E, AXSM-XG and PXM1E \n                     Modules.')
ciscoSonetExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 261, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV5R00 = ciscoSonetExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSonetExtCapabilityV5R00 = ciscoSonetExtCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSonetExtCapabilityV5R00.setDescription('Cisco Sonet Ext MIB capabilities for Voice \n                      Switch Service Module(VXSM) and \n                      MPSM in release 5.0.0.')
mibBuilder.exportSymbols("CISCO-SONET-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoSonetExtCapability, ciscoSonetExtAxsmCapabilityV2R00=ciscoSonetExtAxsmCapabilityV2R00, ciscoSonetExtAxsmCapabilityV2R11=ciscoSonetExtAxsmCapabilityV2R11, ciscoSonetExtAxsmeCapabilityV21R60=ciscoSonetExtAxsmeCapabilityV21R60, ciscoSonetExtCapability=ciscoSonetExtCapability, ciscoSonetExtCapabilityV4R00=ciscoSonetExtCapabilityV4R00, ciscoSonetExtCapabilityV5R00=ciscoSonetExtCapabilityV5R00, ciscoSonetExtSrmeCapabilityV3R00=ciscoSonetExtSrmeCapabilityV3R00)
