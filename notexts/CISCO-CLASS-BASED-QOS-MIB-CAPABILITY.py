#
# PySNMP MIB module CISCO-CLASS-BASED-QOS-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CLASS-BASED-QOS-MIB-CAPABILITY
# Source digest sha256:44f5e6514f39ec5fc9f8ad4702101f8ed043651e44f051998fd3b419eac413cd
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCBQosMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 525))
ciscoCBQosMibCapability.setRevisions(('2007-07-17 00:00', '2006-11-08 00:00', '2005-06-22 00:00', '2004-09-01 00:00', '2003-01-24 00:00', '2001-06-13 00:00', '2000-12-01 00:00', '2000-07-13 00:00',))
if mibBuilder.loadTexts: ciscoCBQosMibCapability.setLastUpdated('2007-07-17 00:00')
if mibBuilder.loadTexts: ciscoCBQosMibCapability.setOrganization('Cisco Systems, Inc.')
ciscoCBQosMibCapabilityV121R02E7500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R02E7500 = ciscoCBQosMibCapabilityV121R02E7500.setProductRelease('Cisco IOS 12.1(2)E on 7500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R02E7500 = ciscoCBQosMibCapabilityV121R02E7500.setStatus('current')
ciscoCBQosMibCapabilityV120R12S7500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV120R12S7500 = ciscoCBQosMibCapabilityV120R12S7500.setProductRelease('Cisco IOS 12.0(12)S on 7500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV120R12S7500 = ciscoCBQosMibCapabilityV120R12S7500.setStatus('current')
ciscoCBQosMibCapabilityV121R05T7200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R05T7200 = ciscoCBQosMibCapabilityV121R05T7200.setProductRelease('Cisco IOS 12.1(5)T for 7200/lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R05T7200 = ciscoCBQosMibCapabilityV121R05T7200.setStatus('current')
ciscoCBQosMibCapabilityV122R01T7200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV122R01T7200 = ciscoCBQosMibCapabilityV122R01T7200.setProductRelease('Cisco IOS 12.2(2)T on 7200 and lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV122R01T7200 = ciscoCBQosMibCapabilityV122R01T7200.setStatus('current')
ciscoCBQosMibCapabilityV123R01T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV123R01T = ciscoCBQosMibCapabilityV123R01T.setProductRelease('Cisco IOS 12.3(1)T on 7500, 7200 and \n                 lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV123R01T = ciscoCBQosMibCapabilityV123R01T.setStatus('current')
ciscoCBQosMibCapabilityV121R14EB = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R14EB = ciscoCBQosMibCapabilityV121R14EB.setProductRelease('Cisco IOS 12.1(14)EB on Catalyst 8540MSR platform.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R14EB = ciscoCBQosMibCapabilityV121R14EB.setStatus('current')
ciscoCBQosMibCapabilityV12R0306T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R0306T = ciscoCBQosMibCapabilityV12R0306T.setProductRelease('Cisco IOS 12.3(6)T on 7200 and \n                 lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R0306T = ciscoCBQosMibCapabilityV12R0306T.setStatus('current')
ciscoCBQosMibCapabilityV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R02S = ciscoCBQosMibCapabilityV12R02S.setProductRelease('Cisco IOS 12.2S for 7500/7200/lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R02S = ciscoCBQosMibCapabilityV12R02S.setStatus('current')
ciscoCBQosMibCapabilityV12R00S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R00S = ciscoCBQosMibCapabilityV12R00S.setProductRelease('Cisco IOS 12.0S for 7500/7200/lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R00S = ciscoCBQosMibCapabilityV12R00S.setStatus('current')
ciscoCBQosMibCapabilityV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV320CRS1 = ciscoCBQosMibCapabilityV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV320CRS1 = ciscoCBQosMibCapabilityV320CRS1.setStatus('current')
ciscoCBQosMibCapabilityV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV3R4CRS1 = ciscoCBQosMibCapabilityV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV3R4CRS1 = ciscoCBQosMibCapabilityV3R4CRS1.setStatus('current')
ciscoCBQosMibCapV12R0218SXFPCat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc2 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc2.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                     and Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc2 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc2.setStatus('current')
ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc3.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                     and Cisco 7600 series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc3.setStatus('current')
ciscoCBQosMibCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0233SXHPCat6K = ciscoCBQosMibCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0233SXHPCat6K = ciscoCBQosMibCapV12R0233SXHPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-CLASS-BASED-QOS-MIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoCBQosMibCapability, ciscoCBQosMibCapV12R0218SXFPCat6KPfc2=ciscoCBQosMibCapV12R0218SXFPCat6KPfc2, ciscoCBQosMibCapV12R0218SXFPCat6KPfc3=ciscoCBQosMibCapV12R0218SXFPCat6KPfc3, ciscoCBQosMibCapV12R0233SXHPCat6K=ciscoCBQosMibCapV12R0233SXHPCat6K, ciscoCBQosMibCapability=ciscoCBQosMibCapability, ciscoCBQosMibCapabilityV120R12S7500=ciscoCBQosMibCapabilityV120R12S7500, ciscoCBQosMibCapabilityV121R02E7500=ciscoCBQosMibCapabilityV121R02E7500, ciscoCBQosMibCapabilityV121R05T7200=ciscoCBQosMibCapabilityV121R05T7200, ciscoCBQosMibCapabilityV121R14EB=ciscoCBQosMibCapabilityV121R14EB, ciscoCBQosMibCapabilityV122R01T7200=ciscoCBQosMibCapabilityV122R01T7200, ciscoCBQosMibCapabilityV123R01T=ciscoCBQosMibCapabilityV123R01T, ciscoCBQosMibCapabilityV12R00S=ciscoCBQosMibCapabilityV12R00S, ciscoCBQosMibCapabilityV12R02S=ciscoCBQosMibCapabilityV12R02S, ciscoCBQosMibCapabilityV12R0306T=ciscoCBQosMibCapabilityV12R0306T, ciscoCBQosMibCapabilityV320CRS1=ciscoCBQosMibCapabilityV320CRS1, ciscoCBQosMibCapabilityV3R4CRS1=ciscoCBQosMibCapabilityV3R4CRS1)
