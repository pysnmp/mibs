#
# PySNMP MIB module CISCO-ETHER-CFM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ETHER-CFM-CAPABILITY
# Source digest sha256:eefdcad15c47cad52e8a4c4f1ebe4f5c1acf604b954b852c2f3b83ca3e5d5d0a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEtherCfmMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 431))
ciscoEtherCfmMibCapability.setRevisions(('2005-02-11 00:00',))
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setLastUpdated('2005-02-11 00:00')
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setOrganization('Cisco Systems, Inc.')
ciscoEtherCfmMibCapabilityV122 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 431, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMibCapabilityV122 = ciscoEtherCfmMibCapabilityV122.setProductRelease('Cisco IOS 12.2X (exact rev TBD)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMibCapabilityV122 = ciscoEtherCfmMibCapabilityV122.setStatus('current')
mibBuilder.exportSymbols("CISCO-ETHER-CFM-CAPABILITY", PYSNMP_MODULE_ID=ciscoEtherCfmMibCapability, ciscoEtherCfmMibCapability=ciscoEtherCfmMibCapability, ciscoEtherCfmMibCapabilityV122=ciscoEtherCfmMibCapabilityV122)
