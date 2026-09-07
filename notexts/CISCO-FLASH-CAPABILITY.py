#
# PySNMP MIB module CISCO-FLASH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-FLASH-CAPABILITY
# Source digest sha256:c2ac66050fa36bd1ff1433d5b8c10e078f201470f6e9e8dab4169f948083e586
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFlashCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 222))
ciscoFlashCapability.setRevisions(('2008-01-18 00:00', '2004-04-01 00:00', '2003-10-21 00:00', '2001-09-25 12:34',))
if mibBuilder.loadTexts: ciscoFlashCapability.setLastUpdated('2008-01-18 00:00')
if mibBuilder.loadTexts: ciscoFlashCapability.setOrganization('Cisco Systems, Inc.')
ciscoFlashCapabilityV12R00S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R00S = ciscoFlashCapabilityV12R00S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R00S = ciscoFlashCapabilityV12R00S.setStatus('current')
ciscoFlashCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R01 = ciscoFlashCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R01 = ciscoFlashCapabilityV12R01.setStatus('current')
ciscoFlashCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R02 = ciscoFlashCapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashCapabilityV12R02 = ciscoFlashCapabilityV12R02.setStatus('current')
ciscoFlashMibCapCatOSV7R0501Cat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat4k = ciscoFlashMibCapCatOSV7R0501Cat4k.setProductRelease('Cisco CatOS 7.5(1) on  Catalyst 4000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat4k = ciscoFlashMibCapCatOSV7R0501Cat4k.setStatus('current')
ciscoFlashMibCapCatOSV7R0501Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat6k = ciscoFlashMibCapCatOSV7R0501Cat6k.setProductRelease('Cisco CatOS 7.5(1) on Catalyst 6000.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV7R0501Cat6k = ciscoFlashMibCapCatOSV7R0501Cat6k.setStatus('current')
ciscoFlashMibCapV12R0113ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapV12R0113ECat6K = ciscoFlashMibCapV12R0113ECat6K.setProductRelease('Cisco IOS 12.1(13E) on Catalyst 6000/6500 and Cisco\n                7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapV12R0113ECat6K = ciscoFlashMibCapV12R0113ECat6K.setStatus('current')
ciscoFlashMibCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV08R0301 = ciscoFlashMibCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1)on Catalyst 6000/6500\n                and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapCatOSV08R0301 = ciscoFlashMibCapCatOSV08R0301.setStatus('current')
ciscoFlashMibCapXRV03R06PCRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 222, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapXRV03R06PCRS1 = ciscoFlashMibCapXRV03R06PCRS1.setProductRelease('Cisco IOS XR 3.6 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlashMibCapXRV03R06PCRS1 = ciscoFlashMibCapXRV03R06PCRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-FLASH-CAPABILITY", PYSNMP_MODULE_ID=ciscoFlashCapability, ciscoFlashCapability=ciscoFlashCapability, ciscoFlashCapabilityV12R00S=ciscoFlashCapabilityV12R00S, ciscoFlashCapabilityV12R01=ciscoFlashCapabilityV12R01, ciscoFlashCapabilityV12R02=ciscoFlashCapabilityV12R02, ciscoFlashMibCapCatOSV08R0301=ciscoFlashMibCapCatOSV08R0301, ciscoFlashMibCapCatOSV7R0501Cat4k=ciscoFlashMibCapCatOSV7R0501Cat4k, ciscoFlashMibCapCatOSV7R0501Cat6k=ciscoFlashMibCapCatOSV7R0501Cat6k, ciscoFlashMibCapV12R0113ECat6K=ciscoFlashMibCapV12R0113ECat6K, ciscoFlashMibCapXRV03R06PCRS1=ciscoFlashMibCapXRV03R06PCRS1)
