#
# PySNMP MIB module CISCO-ENTITY-DISPLAY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-DISPLAY-CAPABILITY
# Source digest sha256:6b0308e53983806b3182834bb7ea400b7bf2fec6ccdf3bfb7dd85a3a659cbb1b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityDisplayCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 379))
ciscoEntityDisplayCapability.setRevisions(('2010-11-09 00:00', '2007-07-16 00:00', '2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setLastUpdated('2010-11-09 00:00')
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setOrganization('Cisco Systems, Inc.')
cEntDisplayCapCatOSV08R0301Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapCatOSV08R0301Cat6k = cEntDisplayCapCatOSV08R0301Cat6k.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapCatOSV08R0301Cat6k = cEntDisplayCapCatOSV08R0301Cat6k.setStatus('current')
cEntDisplayCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0233SXHPCat6k = cEntDisplayCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0233SXHPCat6k = cEntDisplayCapV12R0233SXHPCat6k.setStatus('current')
cEntDisplayCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0250SYPCat6k = cEntDisplayCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0250SYPCat6k = cEntDisplayCapV12R0250SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-DISPLAY-CAPABILITY", PYSNMP_MODULE_ID=ciscoEntityDisplayCapability, cEntDisplayCapCatOSV08R0301Cat6k=cEntDisplayCapCatOSV08R0301Cat6k, cEntDisplayCapV12R0233SXHPCat6k=cEntDisplayCapV12R0233SXHPCat6k, cEntDisplayCapV12R0250SYPCat6k=cEntDisplayCapV12R0250SYPCat6k, ciscoEntityDisplayCapability=ciscoEntityDisplayCapability)
