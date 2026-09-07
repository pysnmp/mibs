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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setLastUpdated('2005-08-27 00:00')
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoCommonMgmtCapability.setDescription('Agent capabilities for CISCO-COMMON-MGMT-MIB')
ciscoCommonMgmtCapMDS30R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 448, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonMgmtCapMDS30R1 = ciscoCommonMgmtCapMDS30R1.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonMgmtCapMDS30R1 = ciscoCommonMgmtCapMDS30R1.setStatus('current')
if mibBuilder.loadTexts: ciscoCommonMgmtCapMDS30R1.setDescription('Cisco Common Management MIB capabilities')
mibBuilder.exportSymbols("CISCO-COMMON-MGMT-CAPABILITY", PYSNMP_MODULE_ID=ciscoCommonMgmtCapability, ciscoCommonMgmtCapMDS30R1=ciscoCommonMgmtCapMDS30R1, ciscoCommonMgmtCapability=ciscoCommonMgmtCapability)
