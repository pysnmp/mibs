#
# PySNMP MIB module CISCO-MODEM-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MODEM-MGMT-CAPABILITY
# Source digest sha256:f04b315fe9224621d8bdba0bc49303117faef9f15307338378a9a985a180d250
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoModemMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoModemMgmtCapability.setRevisions(('2006-07-31 00:00',))
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setLastUpdated('2006-07-31 00:00')
if mibBuilder.loadTexts: ciscoModemMgmtCapability.setOrganization('Cisco Systems, Inc.')
ciscoModemMgmtCapV12R4TISR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModemMgmtCapV12R4TISR = ciscoModemMgmtCapV12R4TISR.setProductRelease('Cisco IOS 12.4 for ATG Platform Devices')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModemMgmtCapV12R4TISR = ciscoModemMgmtCapV12R4TISR.setStatus('current')
mibBuilder.exportSymbols("CISCO-MODEM-MGMT-CAPABILITY", PYSNMP_MODULE_ID=ciscoModemMgmtCapability, ciscoModemMgmtCapV12R4TISR=ciscoModemMgmtCapV12R4TISR, ciscoModemMgmtCapability=ciscoModemMgmtCapability)
