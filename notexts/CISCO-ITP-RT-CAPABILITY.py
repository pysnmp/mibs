#
# PySNMP MIB module CISCO-ITP-RT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-RT-CAPABILITY
# Source digest sha256:0ff643c267a8340c8a8083491dfad974064e9e9b8b9e93cfe747be7e55ea3a54
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpRtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 216))
ciscoItpRtCapability.setRevisions(('2002-01-21 00:00', '2001-10-24 00:00',))
if mibBuilder.loadTexts: ciscoItpRtCapability.setLastUpdated('2002-01-21 00:00')
if mibBuilder.loadTexts: ciscoItpRtCapability.setOrganization('Cisco Systems, Inc.')
ciscoItpRtCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 216, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R024MB1 = ciscoItpRtCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R024MB1 = ciscoItpRtCapabilityV12R024MB1.setStatus('current')
ciscoItpRtCapabilityV12R0204MB3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 216, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R0204MB3 = ciscoItpRtCapabilityV12R0204MB3.setProductRelease('Cisco IOS 12.2(4)MB3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpRtCapabilityV12R0204MB3 = ciscoItpRtCapabilityV12R0204MB3.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-RT-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpRtCapability, ciscoItpRtCapability=ciscoItpRtCapability, ciscoItpRtCapabilityV12R0204MB3=ciscoItpRtCapabilityV12R0204MB3, ciscoItpRtCapabilityV12R024MB1=ciscoItpRtCapabilityV12R024MB1)
