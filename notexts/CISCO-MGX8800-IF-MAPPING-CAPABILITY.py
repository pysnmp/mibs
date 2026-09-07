#
# PySNMP MIB module CISCO-MGX8800-IF-MAPPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MGX8800-IF-MAPPING-CAPABILITY
# Source digest sha256:7ef320f6c99cd72106d31856d21a3ddd8bd7b0d2f37a21e08c027242c49940bf
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx8800IfMappingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 278))
ciscoMgx8800IfMappingCapability.setRevisions(('2002-08-01 00:00',))
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setLastUpdated('2002-08-01 00:00')
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setOrganization('Cisco Systems, Inc.')
cmiMappingCapabilityMgxV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 278, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityMgxV3R00 = cmiMappingCapabilityMgxV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityMgxV3R00 = cmiMappingCapabilityMgxV3R00.setStatus('current')
cmiMappingCapabilityRpmxfV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 278, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityRpmxfV12R02 = cmiMappingCapabilityRpmxfV12R02.setProductRelease('IOS Release 12.2(8)T2.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityRpmxfV12R02 = cmiMappingCapabilityRpmxfV12R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX8800-IF-MAPPING-CAPABILITY", PYSNMP_MODULE_ID=ciscoMgx8800IfMappingCapability, ciscoMgx8800IfMappingCapability=ciscoMgx8800IfMappingCapability, cmiMappingCapabilityMgxV3R00=cmiMappingCapabilityMgxV3R00, cmiMappingCapabilityRpmxfV12R02=cmiMappingCapabilityRpmxfV12R02)
