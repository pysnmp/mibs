#
# PySNMP MIB module CISCO-MGC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MGC-CAPABILITY
# Source digest sha256:65e1d3ee58376655e048dbf6a5bdc34c198a7201824f871d585708f905b668b0
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 370))
ciscoMgcCapability.setRevisions(('2004-02-05 00:00',))
if mibBuilder.loadTexts: ciscoMgcCapability.setLastUpdated('2004-02-05 00:00')
if mibBuilder.loadTexts: ciscoMgcCapability.setOrganization('Cisco Systems, Inc.')
ciscoMgcCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 370, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgcCapabilityV5R00 = ciscoMgcCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgcCapabilityV5R00 = ciscoMgcCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGC-CAPABILITY", PYSNMP_MODULE_ID=ciscoMgcCapability, ciscoMgcCapability=ciscoMgcCapability, ciscoMgcCapabilityV5R00=ciscoMgcCapabilityV5R00)
