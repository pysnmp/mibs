#
# PySNMP MIB module CISCO-AUTH-FRAMEWORK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-AUTH-FRAMEWORK-CAPABILITY
# Source digest sha256:4df2c26bbd5b747e83e40a3a5fca08f8e71f2b7a60548bbe6873e488d4493a92
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAuthFrameworkCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 573))
ciscoAuthFrameworkCapability.setRevisions(('2012-09-04 00:00', '2012-04-02 00:00', '2011-03-29 00:00', '2011-03-24 00:00', '2010-05-06 00:00', '2010-04-05 00:00', '2010-03-09 00:00', '2009-05-18 00:00', '2008-10-30 00:00',))
if mibBuilder.loadTexts: ciscoAuthFrameworkCapability.setLastUpdated('2012-09-04 00:00')
if mibBuilder.loadTexts: ciscoAuthFrameworkCapability.setOrganization('Cisco Systems, Inc.')
cafCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXIPCat6K = cafCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXIPCat6K = cafCapV12R0233SXIPCat6K.setStatus('current')
cafCapV12R0233SXI2PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI2PCat6K = cafCapV12R0233SXI2PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI2 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI2PCat6K = cafCapV12R0233SXI2PCat6K.setStatus('current')
cafCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0252SGPCat4K = cafCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0252SGPCat4K = cafCapV12R0252SGPCat4K.setStatus('current')
cafCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI4PCat6K = cafCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI4PCat6K = cafCapV12R0233SXI4PCat6K.setStatus('current')
cafCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0254SGPCat4K = cafCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0254SGPCat4K = cafCapV12R0254SGPCat4K.setStatus('current')
cafCapV12R0233SXJPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXJPCat6K = cafCapV12R0233SXJPCat6K.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXJPCat6K = cafCapV12R0233SXJPCat6K.setStatus('current')
cafCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0002SGPCat4K = cafCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0002SGPCat4K = cafCapV15R0002SGPCat4K.setStatus('current')
cafCapV15R0101SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SGPCat4K = cafCapV15R0101SGPCat4K.setProductRelease('Cisco IOS 15.1(1)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SGPCat4K = cafCapV15R0101SGPCat4K.setStatus('current')
cafCapV15R0101SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SYPCat6K = cafCapV15R0101SYPCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SYPCat6K = cafCapV15R0101SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-AUTH-FRAMEWORK-CAPABILITY", PYSNMP_MODULE_ID=ciscoAuthFrameworkCapability, cafCapV12R0233SXI2PCat6K=cafCapV12R0233SXI2PCat6K, cafCapV12R0233SXI4PCat6K=cafCapV12R0233SXI4PCat6K, cafCapV12R0233SXIPCat6K=cafCapV12R0233SXIPCat6K, cafCapV12R0233SXJPCat6K=cafCapV12R0233SXJPCat6K, cafCapV12R0252SGPCat4K=cafCapV12R0252SGPCat4K, cafCapV12R0254SGPCat4K=cafCapV12R0254SGPCat4K, cafCapV15R0002SGPCat4K=cafCapV15R0002SGPCat4K, cafCapV15R0101SGPCat4K=cafCapV15R0101SGPCat4K, cafCapV15R0101SYPCat6K=cafCapV15R0101SYPCat6K, ciscoAuthFrameworkCapability=ciscoAuthFrameworkCapability)
