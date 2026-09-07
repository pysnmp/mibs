#
# PySNMP MIB module CISCO-ITP-ACT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-ACT-CAPABILITY
# Source digest sha256:4df5f0351e685e3d89c84e22813f83f2334bc8e3bee65ab5980142b2cef96ca5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpActCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 219))
ciscoItpActCapability.setRevisions(('2001-10-24 00:00',))
if mibBuilder.loadTexts: ciscoItpActCapability.setLastUpdated('2001-10-24 00:00')
if mibBuilder.loadTexts: ciscoItpActCapability.setOrganization('Cisco Systems, Inc.')
ciscoItpActCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 219, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpActCapabilityV12R024MB1 = ciscoItpActCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpActCapabilityV12R024MB1 = ciscoItpActCapabilityV12R024MB1.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-ACT-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpActCapability, ciscoItpActCapability=ciscoItpActCapability, ciscoItpActCapabilityV12R024MB1=ciscoItpActCapabilityV12R024MB1)
