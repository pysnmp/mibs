#
# PySNMP MIB module CISCO-PROCESS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PROCESS-CAPABILITY
# Source digest sha256:3af9f14276c940b3094b5d6dba9f9f1aacf39b131fd41d9b3edeeb581a8ab317
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoProcessCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 256))
ciscoProcessCapability.setRevisions(('2013-08-29 00:00', '2009-03-18 00:00', '2008-09-15 00:00', '2007-11-27 00:00', '2007-11-22 00:00', '2006-03-22 00:00', '2006-02-21 00:00', '2005-12-12 00:00', '2004-11-05 00:00', '2003-08-06 00:00', '2001-11-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoProcessCapability.setRevisionsDescriptions(('Added the capabilities for CISCO WAAS 5.3.0.', 'Added ciscoProcessCapabilityGssV03R01 agent\n        capabilities for Global Site Selector(GSS)\n        release 3.1(0).', 'Added ciscoProcessCapabilityGssV03R00 agent\n        capabilities for Global Site Selector(GSS)\n        release 3.0.', 'Added ciscoProcessCapabilityIONV12R02SXH33\n        for Cisco Modular IOS(ION) release 12.2SXH33.\n        -Added ciscoProcessCapabilityIOSV12R02SXH33\n        for Cisco IOS release 12.2SXH33', 'Added ciscoProcessCapc4710aceVA1R700 agent\n        capabilities for ACE 4710 Application \n        Control Engine Appliance.', 'Added ciscoProcessCapIOSXRV2R0CRS1 agent\n        capabilities for IOS XR release 2.0 CRS1', '-Added Agent capabilities\n        ciscoProcessCapabilityACSWV03R000 for \n        Cisco Application Control Engine (ACE).', '-Added ciscoProcessCapabilitySANOSV3R0001 for\n        SAN-OS 3.0(1).', '-Added ciscoProcessCapabilityV12R02S for\n        Cisco IOS 12.2(S).\n        -Added ciscoProcessCapabilityV12R03 for\n        Cisco IOS 12.3.\n        -Added ciscoProcessCapabilityV12R03T for\n        Cisco IOS 12.3(T)', 'Added ciscoProcessCapCatOSV07R0201 for\n        Cisco CatOS 7.2(1).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoProcessCapability.setLastUpdated('2013-08-29 00:00')
if mibBuilder.loadTexts: ciscoProcessCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoProcessCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com\n            cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoProcessCapability.setDescription('Agent capabilities for CISCO-PROCESS-MIB')
ciscoProcessCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R00 = ciscoProcessCapabilityV12R00.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R00 = ciscoProcessCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityV12R00.setDescription('IOS 12.0S CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R01 = ciscoProcessCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R01 = ciscoProcessCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityV12R01.setDescription('IOS 12.1 CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02 = ciscoProcessCapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02 = ciscoProcessCapabilityV12R02.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityV12R02.setDescription('IOS 12.2 CISCO-PROCESS-MIB capabilities')
ciscoProcessCapCatOSV07R0201 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapCatOSV07R0201 = ciscoProcessCapCatOSV07R0201.setProductRelease('Cisco CatOS 7.2(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapCatOSV07R0201 = ciscoProcessCapCatOSV07R0201.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapCatOSV07R0201.setDescription('CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilityV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02S = ciscoProcessCapabilityV12R02S.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R02S = ciscoProcessCapabilityV12R02S.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityV12R02S.setDescription('IOS 12.2 CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03 = ciscoProcessCapabilityV12R03.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03 = ciscoProcessCapabilityV12R03.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityV12R03.setDescription('IOS 12.3 CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilityV12R03T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03T = ciscoProcessCapabilityV12R03T.setProductRelease('Cisco IOS 12.3T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityV12R03T = ciscoProcessCapabilityV12R03T.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityV12R03T.setDescription('IOS 12.3T CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilitySAN3R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilitySAN3R0001 = ciscoProcessCapabilitySAN3R0001.setProductRelease('SAN-OS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilitySAN3R0001 = ciscoProcessCapabilitySAN3R0001.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilitySAN3R0001.setDescription('SAN-OS 3.0(1) CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityACSWV03R000 = ciscoProcessCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityACSWV03R000 = ciscoProcessCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityACSWV03R000.setDescription('ACSW 3.0 CISCO-PROCESS-MIB capabilities')
ciscoProcessCapIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapIOSXRV2R0CRS1 = ciscoProcessCapIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapIOSXRV2R0CRS1 = ciscoProcessCapIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapIOSXRV2R0CRS1.setDescription('CISCO-PROCESS-MIB capabilities for\n        IOS XR release 2.0')
ciscoProcessCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapc4710aceVA1R700 = ciscoProcessCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                for ACE 4710 Application Control Engine \n                Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapc4710aceVA1R700 = ciscoProcessCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapc4710aceVA1R700.setDescription('ACSW A1(7) CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilityIONV12R02SXH33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIONV12R02SXH33 = ciscoProcessCapabilityIONV12R02SXH33.setProductRelease('Modular IOS(ION) 12.2SXH33')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIONV12R02SXH33 = ciscoProcessCapabilityIONV12R02SXH33.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityIONV12R02SXH33.setDescription('ION 12.2SXH33 CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilityIOSV12R02SXH33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIOSV12R02SXH33 = ciscoProcessCapabilityIOSV12R02SXH33.setProductRelease('Cisco IOS 12.2SXH33')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityIOSV12R02SXH33 = ciscoProcessCapabilityIOSV12R02SXH33.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityIOSV12R02SXH33.setDescription('IOS 12.2SXH33 CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilityGssV03R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R00 = ciscoProcessCapabilityGssV03R00.setProductRelease('Global Site Selector(GSS) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R00 = ciscoProcessCapabilityGssV03R00.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityGssV03R00.setDescription('GSS 3.0 CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilityGssV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R01 = ciscoProcessCapabilityGssV03R01.setProductRelease('Global Site Selector(GSS) 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityGssV03R01 = ciscoProcessCapabilityGssV03R01.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityGssV03R01.setDescription('GSS 3.1(0) CISCO-PROCESS-MIB capabilities')
ciscoProcessCapabilityWAASV05R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 256, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityWAASV05R03 = ciscoProcessCapabilityWAASV05R03.setProductRelease('OS=WAAS\n                     OSVERSION=5.3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoProcessCapabilityWAASV05R03 = ciscoProcessCapabilityWAASV05R03.setStatus('current')
if mibBuilder.loadTexts: ciscoProcessCapabilityWAASV05R03.setDescription('Cisco WAAS 5.3.0 CISCO-PROCESS-MIB Capabilities.')
mibBuilder.exportSymbols("CISCO-PROCESS-CAPABILITY", PYSNMP_MODULE_ID=ciscoProcessCapability, ciscoProcessCapCatOSV07R0201=ciscoProcessCapCatOSV07R0201, ciscoProcessCapIOSXRV2R0CRS1=ciscoProcessCapIOSXRV2R0CRS1, ciscoProcessCapability=ciscoProcessCapability, ciscoProcessCapabilityACSWV03R000=ciscoProcessCapabilityACSWV03R000, ciscoProcessCapabilityGssV03R00=ciscoProcessCapabilityGssV03R00, ciscoProcessCapabilityGssV03R01=ciscoProcessCapabilityGssV03R01, ciscoProcessCapabilityIONV12R02SXH33=ciscoProcessCapabilityIONV12R02SXH33, ciscoProcessCapabilityIOSV12R02SXH33=ciscoProcessCapabilityIOSV12R02SXH33, ciscoProcessCapabilitySAN3R0001=ciscoProcessCapabilitySAN3R0001, ciscoProcessCapabilityV12R00=ciscoProcessCapabilityV12R00, ciscoProcessCapabilityV12R01=ciscoProcessCapabilityV12R01, ciscoProcessCapabilityV12R02=ciscoProcessCapabilityV12R02, ciscoProcessCapabilityV12R02S=ciscoProcessCapabilityV12R02S, ciscoProcessCapabilityV12R03=ciscoProcessCapabilityV12R03, ciscoProcessCapabilityV12R03T=ciscoProcessCapabilityV12R03T, ciscoProcessCapabilityWAASV05R03=ciscoProcessCapabilityWAASV05R03, ciscoProcessCapc4710aceVA1R700=ciscoProcessCapc4710aceVA1R700)
