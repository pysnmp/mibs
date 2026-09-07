#
# PySNMP MIB module CISCO-ATM-CELL-LAYER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-CELL-LAYER-CAPABILITY
# Source digest sha256:a9bca09477c386db91099c2ee95d7ab8be515b262352d2d9c4ce1e7b2991e2c8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmCellLayerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 275))
ciscoAtmCellLayerCapability.setRevisions(('2003-01-30 00:00', '2002-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setRevisionsDescriptions(('Added cacLayerCapabilityAxsmxgV4R00.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setLastUpdated('2003-01-30 00:00')
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setDescription('The Agent Capabilities for \n            CISCO-ATM-CELL-LAYER-MIB.\n\n            - cacLayerCapabilityAxsmV2R00 is for\n              ATM Switch Service Module(AXSM).\n\n            - cacLayerCapabilityAxsmeV2R0160 is for\n              Enhanced AXSM(AXSM-E).\n\n            - cacLayerCapabilityAxsmxgV4R00 is for\n              10 Gig. AXSM(AXSM-XG).')
cacLayerCapabilityAxsmV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmV2R00 = cacLayerCapabilityAxsmV2R00.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmV2R00 = cacLayerCapabilityAxsmV2R00.setStatus('current')
if mibBuilder.loadTexts: cacLayerCapabilityAxsmV2R00.setDescription('CISCO-ATM-CELL-LAYER-MIB Capabilities for\n                AXSM Service Module.')
cacLayerCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmeV2R0160 = cacLayerCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmeV2R0160 = cacLayerCapabilityAxsmeV2R0160.setStatus('current')
if mibBuilder.loadTexts: cacLayerCapabilityAxsmeV2R0160.setDescription('CISCO-ATM-CELL-LAYER-MIB Capabilities for\n                Enhanced AXSM(AXSM-E) Service Module.')
cacLayerCapabilityAxsmxgV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmxgV4R00 = cacLayerCapabilityAxsmxgV4R00.setProductRelease('MGX8950 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmxgV4R00 = cacLayerCapabilityAxsmxgV4R00.setStatus('current')
if mibBuilder.loadTexts: cacLayerCapabilityAxsmxgV4R00.setDescription('CISCO-ATM-CELL-LAYER-MIB Capabilities for\n                10 Gig. AXSM Service Module (AXSM-XG).')
mibBuilder.exportSymbols("CISCO-ATM-CELL-LAYER-CAPABILITY", PYSNMP_MODULE_ID=ciscoAtmCellLayerCapability, cacLayerCapabilityAxsmV2R00=cacLayerCapabilityAxsmV2R00, cacLayerCapabilityAxsmeV2R0160=cacLayerCapabilityAxsmeV2R0160, cacLayerCapabilityAxsmxgV4R00=cacLayerCapabilityAxsmxgV4R00, ciscoAtmCellLayerCapability=ciscoAtmCellLayerCapability)
