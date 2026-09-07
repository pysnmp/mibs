#
# PySNMP MIB module CISCO-COMMON-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-COMMON-MGMT-CAPABILITY
# Source digest sha256:9f47967da9403cedfc846ebbed9276ddd3eda5444dc61ce3cb66d40915448828
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCommonMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 448))
ciscoCommonMgmtCapability.setRevisions(('2005-08-27 00:00',))
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setLastUpdated('2005-08-27 00:00')
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setOrganization('Cisco Systems, Inc.')
ciscoCommonMgmtCapMDS30R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 448, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonMgmtCapMDS30R1 = ciscoCommonMgmtCapMDS30R1.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonMgmtCapMDS30R1 = ciscoCommonMgmtCapMDS30R1.setStatus('current')
mibBuilder.exportSymbols("CISCO-COMMON-MGMT-CAPABILITY", PYSNMP_MODULE_ID=ciscoCommonMgmtCapability, ciscoCommonMgmtCapMDS30R1=ciscoCommonMgmtCapMDS30R1, ciscoCommonMgmtCapability=ciscoCommonMgmtCapability)
