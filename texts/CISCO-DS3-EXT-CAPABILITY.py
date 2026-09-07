#
# PySNMP MIB module CISCO-DS3-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DS3-EXT-CAPABILITY
# Source digest sha256:e842d42a0a53831c253034ca1cffb78ff3352272f68ad89110702efd42103f53
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDs3ExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 262))
ciscoDs3ExtCapability.setRevisions(('2003-12-23 00:00', '2003-03-20 00:00', '2002-03-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDs3ExtCapability.setRevisionsDescriptions(('Added ciscoDs3Ext155CapabilityV5R00.', 'Added ciscoDs3ExtCapabilityV4R00 for \n             10 Gig. AXSM Module (AXSM-XG) and \n             Processor Switch Module Enhanced(PXM1E)\n             controller card.', 'Initial version of the MIB Module.',))
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setLastUpdated('2003-12-23 00:00')
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setDescription('The Agent Capabilities for CISCO-DS3-MIB.\n            \n             - The ciscoDs3ExtAxsmCapabilityV2R00 is for\n               ATM Switch Service Module(AXSM).\n\n             - The ciscoDs3ExtAxsmeCapabilityV21R60 is for\n               Enhanced AXSM(AXSM-E) Module.\n\n             - The ciscoDs3ExtSrmCapabilityV3R00 is for\n               Service Resource Module(SRM).\n\n             - The ciscoDs3ExtFrsm12CapabilityV3R00 is for\n               Frame Relay Service Module(FRSM-12).\n\n             - The ciscoDs3ExtAxsmxgCapabilityV4R00 is for\n               10 Gig. AXSM Module (AXSM-XG).\n\n             - The ciscoDs3ExtCapabilityV5R00 is for\n               Voice Switch Service (VXSM) and MPSM Modules.')
ciscoDs3ExtAxsmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmCapabilityV2R00 = ciscoDs3ExtAxsmCapabilityV2R00.setProductRelease('MGX8850 Release 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmCapabilityV2R00 = ciscoDs3ExtAxsmCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtAxsmCapabilityV2R00.setDescription('CISCO-DS3-MIB Capabilities for\n                         ATM Switch Service Module(AXSM).')
ciscoDs3ExtAxsmeCapabilityV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmeCapabilityV21R60 = ciscoDs3ExtAxsmeCapabilityV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmeCapabilityV21R60 = ciscoDs3ExtAxsmeCapabilityV21R60.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtAxsmeCapabilityV21R60.setDescription('CISCO-DS3-MIB Capabilities for\n                         Enhanced AXSM Module(AXSM-E).')
ciscoDs3ExtSrmCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtSrmCapabilityV3R00 = ciscoDs3ExtSrmCapabilityV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtSrmCapabilityV3R00 = ciscoDs3ExtSrmCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtSrmCapabilityV3R00.setDescription('CISCO-DS3-MIB Capabilities for\n                         Service Resource Module(SRM).')
ciscoDs3ExtFrsm12CapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtFrsm12CapabilityV3R00 = ciscoDs3ExtFrsm12CapabilityV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtFrsm12CapabilityV3R00 = ciscoDs3ExtFrsm12CapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtFrsm12CapabilityV3R00.setDescription('CISCO-DS3-MIB Capabilities for\n                         Frame Relay Service Module(FRSM-12).')
ciscoDs3ExtCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV4R00 = ciscoDs3ExtCapabilityV4R00.setProductRelease('MGX8950 and MGX8850 Release \n                         4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV4R00 = ciscoDs3ExtCapabilityV4R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtCapabilityV4R00.setDescription('CISCO-DS3-MIB Capabilities for\n                         10 Gig. AXSM Module(AXSM-XG) and\n                         Processor Switch Module Enhanced-\n                         (PXM1E) controller card.')
ciscoDs3ExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV5R00 = ciscoDs3ExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV5R00 = ciscoDs3ExtCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDs3ExtCapabilityV5R00.setDescription('CISCO-DS3-MIB capabilities Voice Switch\n                          Service Module(VXSM) and MPSM \n                          in release 5.0.0')
mibBuilder.exportSymbols("CISCO-DS3-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoDs3ExtCapability, ciscoDs3ExtAxsmCapabilityV2R00=ciscoDs3ExtAxsmCapabilityV2R00, ciscoDs3ExtAxsmeCapabilityV21R60=ciscoDs3ExtAxsmeCapabilityV21R60, ciscoDs3ExtCapability=ciscoDs3ExtCapability, ciscoDs3ExtCapabilityV4R00=ciscoDs3ExtCapabilityV4R00, ciscoDs3ExtCapabilityV5R00=ciscoDs3ExtCapabilityV5R00, ciscoDs3ExtFrsm12CapabilityV3R00=ciscoDs3ExtFrsm12CapabilityV3R00, ciscoDs3ExtSrmCapabilityV3R00=ciscoDs3ExtSrmCapabilityV3R00)
