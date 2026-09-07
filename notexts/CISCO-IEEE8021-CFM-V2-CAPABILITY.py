#
# PySNMP MIB module CISCO-IEEE8021-CFM-V2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IEEE8021-CFM-V2-CAPABILITY
# Source digest sha256:fafae44a0bec1e6c144d212d411fb37964a3cc0eff7ca5a3967df5a7860f681b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIeee8021CfmV2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 579))
ciscoIeee8021CfmV2Capability.setRevisions(('2010-02-15 00:00', '2009-02-06 00:00',))
if mibBuilder.loadTexts: ciscoIeee8021CfmV2Capability.setLastUpdated('2010-02-15 00:00')
if mibBuilder.loadTexts: ciscoIeee8021CfmV2Capability.setOrganization('Cisco Systems, Inc.')
ciscoIeee8021CfmV2CapCatOSV08R0702 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 579, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapCatOSV08R0702 = ciscoIeee8021CfmV2CapCatOSV08R0702.setProductRelease('Cisco CatOS 8.7(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapCatOSV08R0702 = ciscoIeee8021CfmV2CapCatOSV08R0702.setStatus('current')
ciscoIeee8021CfmV2CapV12R0254SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 579, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapV12R0254SE = ciscoIeee8021CfmV2CapV12R0254SE.setProductRelease('Cisco IOS 12.2(54)SE.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmV2CapV12R0254SE = ciscoIeee8021CfmV2CapV12R0254SE.setStatus('current')
mibBuilder.exportSymbols("CISCO-IEEE8021-CFM-V2-CAPABILITY", PYSNMP_MODULE_ID=ciscoIeee8021CfmV2Capability, ciscoIeee8021CfmV2CapCatOSV08R0702=ciscoIeee8021CfmV2CapCatOSV08R0702, ciscoIeee8021CfmV2CapV12R0254SE=ciscoIeee8021CfmV2CapV12R0254SE, ciscoIeee8021CfmV2Capability=ciscoIeee8021CfmV2Capability)
