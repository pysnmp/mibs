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
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setLastUpdated('2003-01-30 00:00')
if mibBuilder.loadTexts: ciscoAtmCellLayerCapability.setOrganization('Cisco Systems, Inc.')
cacLayerCapabilityAxsmV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmV2R00 = cacLayerCapabilityAxsmV2R00.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmV2R00 = cacLayerCapabilityAxsmV2R00.setStatus('current')
cacLayerCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmeV2R0160 = cacLayerCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmeV2R0160 = cacLayerCapabilityAxsmeV2R0160.setStatus('current')
cacLayerCapabilityAxsmxgV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 275, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmxgV4R00 = cacLayerCapabilityAxsmxgV4R00.setProductRelease('MGX8950 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLayerCapabilityAxsmxgV4R00 = cacLayerCapabilityAxsmxgV4R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-CELL-LAYER-CAPABILITY", PYSNMP_MODULE_ID=ciscoAtmCellLayerCapability, cacLayerCapabilityAxsmV2R00=cacLayerCapabilityAxsmV2R00, cacLayerCapabilityAxsmeV2R0160=cacLayerCapabilityAxsmeV2R0160, cacLayerCapabilityAxsmxgV4R00=cacLayerCapabilityAxsmxgV4R00, ciscoAtmCellLayerCapability=ciscoAtmCellLayerCapability)
