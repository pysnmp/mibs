#
# PySNMP MIB module CISCO-SWITCH-CEF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SWITCH-CEF-CAPABILITY
# Source digest sha256:9386be2181e2be7fa3a067daf6979acbb604458d98de744c2abaa0a6118c58f9
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchCefCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 614))
ciscoSwitchCefCapability.setRevisions(('2012-09-07 00:00',))
if mibBuilder.loadTexts: ciscoSwitchCefCapability.setLastUpdated('2012-09-07 00:00')
if mibBuilder.loadTexts: ciscoSwitchCefCapability.setOrganization('Cisco Systems, Inc.')
ciscoSwitchCefCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 614, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc3 = ciscoSwitchCefCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc3 = ciscoSwitchCefCapV15R0101SYPCat6kPfc3.setStatus('current')
ciscoSwitchCefCapV15R0101SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 614, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc4 = ciscoSwitchCefCapV15R0101SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc4 = ciscoSwitchCefCapV15R0101SYPCat6kPfc4.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-CEF-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchCefCapability, ciscoSwitchCefCapV15R0101SYPCat6kPfc3=ciscoSwitchCefCapV15R0101SYPCat6kPfc3, ciscoSwitchCefCapV15R0101SYPCat6kPfc4=ciscoSwitchCefCapV15R0101SYPCat6kPfc4, ciscoSwitchCefCapability=ciscoSwitchCefCapability)
