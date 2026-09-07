#
# PySNMP MIB module CISCO-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IF-CAPABILITY
# Source digest sha256:9aa1a214c0304ee901eb0b5853505775686e26a9a87dddae369388e014f9473f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 125))
ciscoIfCapability.setRevisions(('2008-03-17 00:00', '2006-11-03 00:00', '2006-10-30 00:00', '2006-07-17 00:00', '2006-02-02 00:00', '2004-08-09 00:00', '2004-02-21 00:00', '2004-02-20 00:00', '2003-03-14 00:00', '2002-06-12 00:00', '2000-02-09 00:00', '1998-11-16 00:00',))
if mibBuilder.loadTexts: ciscoIfCapability.setLastUpdated('2008-03-17 00:00')
if mibBuilder.loadTexts: ciscoIfCapability.setOrganization('Cisco Systems, Inc.')
ciscoIfCapabilityV11R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV11R03 = ciscoIfCapabilityV11R03.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV11R03 = ciscoIfCapabilityV11R03.setStatus('current')
ciscoIfCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R00 = ciscoIfCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R00 = ciscoIfCapabilityV12R00.setStatus('current')
ciscoIfCapabilityV12R01T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R01T = ciscoIfCapabilityV12R01T.setProductRelease('Cisco IOS 12.1T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV12R01T = ciscoIfCapabilityV12R01T.setStatus('current')
ciscoIfCapabilityPxmVR200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityPxmVR200 = ciscoIfCapabilityPxmVR200.setProductRelease('MGX8850 Release 2.00,BPX SES Release 1.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityPxmVR200 = ciscoIfCapabilityPxmVR200.setStatus('current')
ciscoIfCapabilityAxsmVR200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmVR200 = ciscoIfCapabilityAxsmVR200.setProductRelease('MGX8850 Release 2.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmVR200 = ciscoIfCapabilityAxsmVR200.setStatus('current')
ciscoIfCapabilityAxsmeV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmeV21R60 = ciscoIfCapabilityAxsmeV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityAxsmeV21R60 = ciscoIfCapabilityAxsmeV21R60.setStatus('current')
ciscoIfCapabilityFrsm12V3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityFrsm12V3R00 = ciscoIfCapabilityFrsm12V3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityFrsm12V3R00 = ciscoIfCapabilityFrsm12V3R00.setStatus('current')
ciscoIfCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV4R00 = ciscoIfCapabilityV4R00.setProductRelease('MGX8950, MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV4R00 = ciscoIfCapabilityV4R00.setStatus('current')
ciscoIfCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R00 = ciscoIfCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R00 = ciscoIfCapabilityV5R00.setStatus('current')
ciscoIfCapabilityCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0101 = ciscoIfCapabilityCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0101 = ciscoIfCapabilityCatOSV08R0101.setStatus('current')
ciscoIfCapabilityCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0301 = ciscoIfCapabilityCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCatOSV08R0301 = ciscoIfCapabilityCatOSV08R0301.setStatus('current')
ciscoIfCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R015 = ciscoIfCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityV5R015 = ciscoIfCapabilityV5R015.setStatus('current')
ciscoIfCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV2R0CRS1 = ciscoIfCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV2R0CRS1 = ciscoIfCapabilityIOSXRV2R0CRS1.setStatus('current')
ciscoIfCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityACSWV03R000 = ciscoIfCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine (ACE) \n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityACSWV03R000 = ciscoIfCapabilityACSWV03R000.setStatus('current')
ciscoIfCapabilityCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTSV100 = ciscoIfCapabilityCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTSV100 = ciscoIfCapabilityCTSV100.setStatus('current')
ciscoIfCapabilityCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTMV1000 = ciscoIfCapabilityCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityCTMV1000 = ciscoIfCapabilityCTMV1000.setStatus('current')
ciscoIfCapabilityIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV3R4CRS1 = ciscoIfCapabilityIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityIOSXRV3R4CRS1 = ciscoIfCapabilityIOSXRV3R4CRS1.setStatus('current')
ciscoIfCapabilityc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 125, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityc4710aceVA1R700 = ciscoIfCapabilityc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityc4710aceVA1R700 = ciscoIfCapabilityc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-CAPABILITY", PYSNMP_MODULE_ID=ciscoIfCapability, ciscoIfCapability=ciscoIfCapability, ciscoIfCapabilityACSWV03R000=ciscoIfCapabilityACSWV03R000, ciscoIfCapabilityAxsmVR200=ciscoIfCapabilityAxsmVR200, ciscoIfCapabilityAxsmeV21R60=ciscoIfCapabilityAxsmeV21R60, ciscoIfCapabilityCTMV1000=ciscoIfCapabilityCTMV1000, ciscoIfCapabilityCTSV100=ciscoIfCapabilityCTSV100, ciscoIfCapabilityCatOSV08R0101=ciscoIfCapabilityCatOSV08R0101, ciscoIfCapabilityCatOSV08R0301=ciscoIfCapabilityCatOSV08R0301, ciscoIfCapabilityFrsm12V3R00=ciscoIfCapabilityFrsm12V3R00, ciscoIfCapabilityIOSXRV2R0CRS1=ciscoIfCapabilityIOSXRV2R0CRS1, ciscoIfCapabilityIOSXRV3R4CRS1=ciscoIfCapabilityIOSXRV3R4CRS1, ciscoIfCapabilityPxmVR200=ciscoIfCapabilityPxmVR200, ciscoIfCapabilityV11R03=ciscoIfCapabilityV11R03, ciscoIfCapabilityV12R00=ciscoIfCapabilityV12R00, ciscoIfCapabilityV12R01T=ciscoIfCapabilityV12R01T, ciscoIfCapabilityV4R00=ciscoIfCapabilityV4R00, ciscoIfCapabilityV5R00=ciscoIfCapabilityV5R00, ciscoIfCapabilityV5R015=ciscoIfCapabilityV5R015, ciscoIfCapabilityc4710aceVA1R700=ciscoIfCapabilityc4710aceVA1R700)
