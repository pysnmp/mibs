#
# PySNMP MIB module CISCO-IPSLA-ETHERNET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IPSLA-ETHERNET-CAPABILITY
# Source digest sha256:b0c1ae8cd53f21871f6b7a92ef029ea8c49a96b0db9639d0f3a9f549dd590491
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpSlaEthernetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 498))
ciscoIpSlaEthernetCapability.setRevisions(('2006-02-08 00:00',))
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setLastUpdated('2006-02-08 00:00')
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setOrganization('Cisco Systems, Inc.')
ciscoIpSlaEthernetCapabilityRev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 498, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaEthernetCapabilityRev1 = ciscoIpSlaEthernetCapabilityRev1.setProductRelease('Cisco IOS 12.2(01)SRB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaEthernetCapabilityRev1 = ciscoIpSlaEthernetCapabilityRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPSLA-ETHERNET-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpSlaEthernetCapability, ciscoIpSlaEthernetCapability=ciscoIpSlaEthernetCapability, ciscoIpSlaEthernetCapabilityRev1=ciscoIpSlaEthernetCapabilityRev1)
