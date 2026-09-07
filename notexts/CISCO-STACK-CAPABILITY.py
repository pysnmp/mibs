#
# PySNMP MIB module CISCO-STACK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-STACK-CAPABILITY
# Source digest sha256:6fe54912e4181194d59d959ac6c886927110a5cd7c146647c99dc0f7fc94c2d7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoStackCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 378))
ciscoStackCapability.setRevisions(('2008-03-19 00:00', '2006-03-15 00:00', '2005-01-19 00:00', '2003-12-17 00:00',))
if mibBuilder.loadTexts: ciscoStackCapability.setLastUpdated('2008-03-19 00:00')
if mibBuilder.loadTexts: ciscoStackCapability.setOrganization('Cisco Systems, Inc.')
ciscoStackCapCatOSV08R0101Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0101Cat6k = ciscoStackCapCatOSV08R0101Cat6k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0101Cat6k = ciscoStackCapCatOSV08R0101Cat6k.setStatus('current')
ciscoStackCapV12R0111bEXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0111bEXCat6k = ciscoStackCapV12R0111bEXCat6k.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0111bEXCat6k = ciscoStackCapV12R0111bEXCat6k.setStatus('current')
ciscoStackCapV12R0112cE01PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0112cE01PCat6k = ciscoStackCapV12R0112cE01PCat6k.setProductRelease('Cisco IOS 12.1(12c)E1 on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0112cE01PCat6k = ciscoStackCapV12R0112cE01PCat6k.setStatus('current')
ciscoStackCapCatOSV08R0701PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0701PCat6k = ciscoStackCapCatOSV08R0701PCat6k.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0701PCat6k = ciscoStackCapCatOSV08R0701PCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-STACK-CAPABILITY", PYSNMP_MODULE_ID=ciscoStackCapability, ciscoStackCapCatOSV08R0101Cat6k=ciscoStackCapCatOSV08R0101Cat6k, ciscoStackCapCatOSV08R0701PCat6k=ciscoStackCapCatOSV08R0701PCat6k, ciscoStackCapV12R0111bEXCat6k=ciscoStackCapV12R0111bEXCat6k, ciscoStackCapV12R0112cE01PCat6k=ciscoStackCapV12R0112cE01PCat6k, ciscoStackCapability=ciscoStackCapability)
