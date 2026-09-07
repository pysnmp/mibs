#
# PySNMP MIB module CISCO-ATM-VIRTUAL-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-VIRTUAL-IF-CAPABILITY
# Source digest sha256:1256bfa0daf27840f790156dc2437593d4a6f4a9a791f2ea87aa08168a3495b7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmVirtualIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 279))
ciscoAtmVirtualIfCapability.setRevisions(('2005-11-14 00:00', '2003-09-10 00:00', '2003-03-24 00:00', '2002-05-14 00:00',))
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setLastUpdated('2005-11-14 00:00')
if mibBuilder.loadTexts: ciscoAtmVirtualIfCapability.setOrganization('Cisco Systems, Inc.')
cavIfCapabilityAxsmV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R00 = cavIfCapabilityAxsmV2R00.setProductRelease('MGX8850 Release 2.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R00 = cavIfCapabilityAxsmV2R00.setStatus('current')
cavIfCapabilityAxsmV2R0010 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R0010 = cavIfCapabilityAxsmV2R0010.setProductRelease('MGX8850 Release 2.0.10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmV2R0010 = cavIfCapabilityAxsmV2R0010.setStatus('current')
cavIfCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmeV2R0160 = cavIfCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityAxsmeV2R0160 = cavIfCapabilityAxsmeV2R0160.setStatus('current')
cavIfCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV4R00 = cavIfCapabilityV4R00.setProductRelease('MGX8950, MGX8850 Release 4.00.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV4R00 = cavIfCapabilityV4R00.setStatus('current')
cavIfCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 279, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV5R00 = cavIfCapabilityV5R00.setProductRelease('MGX8950, MGX8850 Release 5.00.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cavIfCapabilityV5R00 = cavIfCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-VIRTUAL-IF-CAPABILITY", PYSNMP_MODULE_ID=ciscoAtmVirtualIfCapability, cavIfCapabilityAxsmV2R0010=cavIfCapabilityAxsmV2R0010, cavIfCapabilityAxsmV2R00=cavIfCapabilityAxsmV2R00, cavIfCapabilityAxsmeV2R0160=cavIfCapabilityAxsmeV2R0160, cavIfCapabilityV4R00=cavIfCapabilityV4R00, cavIfCapabilityV5R00=cavIfCapabilityV5R00, ciscoAtmVirtualIfCapability=ciscoAtmVirtualIfCapability)
