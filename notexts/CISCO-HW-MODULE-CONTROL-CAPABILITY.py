#
# PySNMP MIB module CISCO-HW-MODULE-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-HW-MODULE-CONTROL-CAPABILITY
# Source digest sha256:019b5138544594b6cd759378e09b59c955c8c7d06117c2fbd7c60f5109b75ee5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHwModuleControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 588))
ciscoHwModuleControlCapability.setRevisions(('2012-09-07 00:00', '2011-09-27 00:00', '2010-03-17 00:00',))
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setLastUpdated('2012-09-07 00:00')
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setOrganization('Cisco Systems, Inc.')
chmcCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV12R0233SXI4PCat6K = chmcCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV12R0233SXI4PCat6K = chmcCapV12R0233SXI4PCat6K.setStatus('current')
chmcCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SYPCat6K = chmcCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SYPCat6K = chmcCapV15R0001SYPCat6K.setStatus('current')
chmcCapV15R0001SY1PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SY1PCat6K = chmcCapV15R0001SY1PCat6K.setProductRelease('Cisco IOS 15.0(1)SY1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SY1PCat6K = chmcCapV15R0001SY1PCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-HW-MODULE-CONTROL-CAPABILITY", PYSNMP_MODULE_ID=ciscoHwModuleControlCapability, chmcCapV12R0233SXI4PCat6K=chmcCapV12R0233SXI4PCat6K, chmcCapV15R0001SY1PCat6K=chmcCapV15R0001SY1PCat6K, chmcCapV15R0001SYPCat6K=chmcCapV15R0001SYPCat6K, ciscoHwModuleControlCapability=ciscoHwModuleControlCapability)
