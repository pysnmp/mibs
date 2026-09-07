#
# PySNMP MIB module CISCO-CALLHOME-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CALLHOME-CAPABILITY
# Source digest sha256:b414738e8a7ac659fa277b4df86d8254579e34241531210f98ac9c2d9eaffeec
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
CallHomeTransportMethod, = mibBuilder.importSymbols("CISCO-CALLHOME-MIB", "CallHomeTransportMethod")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoURLString, = mibBuilder.importSymbols("CISCO-TC", "CiscoURLString")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoCallHomeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 355))
ciscoCallHomeCapability.setRevisions(('2012-12-05 00:00', '2011-04-14 00:00', '2010-11-10 00:00', '2009-07-10 00:00', '2009-06-17 00:00', '2009-05-07 00:00', '2008-10-27 00:00', '2007-07-30 00:00', '2006-05-10 00:00', '2004-09-20 00:00', '2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoCallHomeCapability.setLastUpdated('2012-12-05 00:00')
if mibBuilder.loadTexts: ciscoCallHomeCapability.setOrganization('Cisco Systems, Inc.')
cCallHomeCapCatOSV08R0101Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapCatOSV08R0101Cat6k = cCallHomeCapCatOSV08R0101Cat6k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapCatOSV08R0101Cat6k = cCallHomeCapCatOSV08R0101Cat6k.setStatus('current')
cCallHomeCapSanOSV20R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapSanOSV20R1MDS9000 = cCallHomeCapSanOSV20R1MDS9000.setProductRelease('Cisco SanOS 2.0(1) on Cisco MDS 9000 series \n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapSanOSV20R1MDS9000 = cCallHomeCapSanOSV20R1MDS9000.setStatus('current')
cCallHomeCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapSanOSV30R1MDS9000 = cCallHomeCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000 series \n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapSanOSV30R1MDS9000 = cCallHomeCapSanOSV30R1MDS9000.setStatus('current')
cCallHomeCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXHPCat6k = cCallHomeCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXHPCat6k = cCallHomeCapV12R0233SXHPCat6k.setStatus('current')
cCallHomeCapV12R0233SXIPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXIPCat6k = cCallHomeCapV12R0233SXIPCat6k.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXIPCat6k = cCallHomeCapV12R0233SXIPCat6k.setStatus('current')
cCallHomeCapV12R0252SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0252SGPCat4k = cCallHomeCapV12R0252SGPCat4k.setProductRelease('Cisco IOS 12.2(52)SG on Catalyst 4000 family\n                    switches, except LAN Base images.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0252SGPCat4k = cCallHomeCapV12R0252SGPCat4k.setStatus('current')
cCallHomeCapV12R0233SXI2PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXI2PCat6k = cCallHomeCapV12R0233SXI2PCat6k.setProductRelease('Cisco IOS 12.2(33)SXI2 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0233SXI2PCat6k = cCallHomeCapV12R0233SXI2PCat6k.setStatus('current')
cCallHomeCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0250SYPCat6k = cCallHomeCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV12R0250SYPCat6k = cCallHomeCapV12R0250SYPCat6k.setStatus('current')
cCallHomeCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV15R0002SGPCat4K = cCallHomeCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Catalyst 4000 family\n                    switches, except LAN Base images.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV15R0002SGPCat4K = cCallHomeCapV15R0002SGPCat4K.setStatus('current')
cCallHomeCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 355, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV15R0101SYPCat6k = cCallHomeCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCallHomeCapV15R0101SYPCat6k = cCallHomeCapV15R0101SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-CALLHOME-CAPABILITY", PYSNMP_MODULE_ID=ciscoCallHomeCapability, cCallHomeCapCatOSV08R0101Cat6k=cCallHomeCapCatOSV08R0101Cat6k, cCallHomeCapSanOSV20R1MDS9000=cCallHomeCapSanOSV20R1MDS9000, cCallHomeCapSanOSV30R1MDS9000=cCallHomeCapSanOSV30R1MDS9000, cCallHomeCapV12R0233SXHPCat6k=cCallHomeCapV12R0233SXHPCat6k, cCallHomeCapV12R0233SXI2PCat6k=cCallHomeCapV12R0233SXI2PCat6k, cCallHomeCapV12R0233SXIPCat6k=cCallHomeCapV12R0233SXIPCat6k, cCallHomeCapV12R0250SYPCat6k=cCallHomeCapV12R0250SYPCat6k, cCallHomeCapV12R0252SGPCat4k=cCallHomeCapV12R0252SGPCat4k, cCallHomeCapV15R0002SGPCat4K=cCallHomeCapV15R0002SGPCat4K, cCallHomeCapV15R0101SYPCat6k=cCallHomeCapV15R0101SYPCat6k, ciscoCallHomeCapability=ciscoCallHomeCapability)
