#
# PySNMP MIB module CISCO-ENTITY-DIAG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-DIAG-CAPABILITY
# Source digest sha256:0f4603b1808486e9055da7f44de9e1da7806df0702d8400a2943312e05af87b5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityDiagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 529))
ciscoEntityDiagCapability.setRevisions(('2010-11-03 00:00', '2009-07-02 00:00', '2009-06-01 00:00', '2008-10-30 00:00', '2008-02-29 00:00', '2007-07-23 00:00', '2007-01-12 00:00',))
if mibBuilder.loadTexts: ciscoEntityDiagCapability.setLastUpdated('2010-11-03 00:00')
if mibBuilder.loadTexts: ciscoEntityDiagCapability.setOrganization('Cisco Systems, Inc.')
ceDiagCapCatOSV08R0601Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapCatOSV08R0601Cat6K = ceDiagCapCatOSV08R0601Cat6K.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500 series \n                     devices with Supervisor 720 or Supervisor 32 \n                     present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapCatOSV08R0601Cat6K = ceDiagCapCatOSV08R0601Cat6K.setStatus('current')
ceDiagCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXHPCat6K = ceDiagCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXHPCat6K = ceDiagCapV12R0233SXHPCat6K.setStatus('current')
ceDiagCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXIPCat6K = ceDiagCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXIPCat6K = ceDiagCapV12R0233SXIPCat6K.setStatus('current')
ceDiagCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0252SGPCat4K = ceDiagCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on CAT4K family \n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0252SGPCat4K = ceDiagCapV12R0252SGPCat4K.setStatus('current')
ceDiagCapV12R0233SXI2PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXI2PCat6K = ceDiagCapV12R0233SXI2PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI2 on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXI2PCat6K = ceDiagCapV12R0233SXI2PCat6K.setStatus('current')
ceDiagCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0250SYPCat6K = ceDiagCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0250SYPCat6K = ceDiagCapV12R0250SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-DIAG-CAPABILITY", PYSNMP_MODULE_ID=ciscoEntityDiagCapability, ceDiagCapCatOSV08R0601Cat6K=ceDiagCapCatOSV08R0601Cat6K, ceDiagCapV12R0233SXHPCat6K=ceDiagCapV12R0233SXHPCat6K, ceDiagCapV12R0233SXI2PCat6K=ceDiagCapV12R0233SXI2PCat6K, ceDiagCapV12R0233SXIPCat6K=ceDiagCapV12R0233SXIPCat6K, ceDiagCapV12R0250SYPCat6K=ceDiagCapV12R0250SYPCat6K, ceDiagCapV12R0252SGPCat4K=ceDiagCapV12R0252SGPCat4K, ciscoEntityDiagCapability=ciscoEntityDiagCapability)
