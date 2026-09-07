#
# PySNMP MIB module CISCO-ENTITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-CAPABILITY
# Source digest sha256:d3e009946c718dded006c4ff8bb9525cadae8fd3c8085ba15e7bb3d3526462d8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 277))
ciscoEntityCapability.setRevisions(('2014-04-03 00:00', '2013-07-19 00:00', '2009-03-24 00:00', '2008-07-03 00:00', '2006-11-16 00:00', '2006-05-26 00:00', '2006-03-24 00:00', '2006-02-08 00:00', '2003-08-12 00:00', '2003-08-08 00:00', '2002-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoEntityCapNxOSV06R0201PMds.', 'Added capability statement\n        ciscoEntityCapNxOSV06R0202PN7k.', 'Added ciscoEntityCapabilityGssV03R01\n        agent capabilities for Global Site \n        Selector(GSS) release 3.1(0).', 'Added ciscoEntityCapc4710aceVA1R700 agent\n        capabilities for ACE 4710 Application Control Engine \n        Appliance.\n\n        Changed CISCO-ENTITY-MIB to ENTITY-MIB in the DESCRIPTION \n        clause for ciscoEntityCapability.\n\n        Changed the SUPPORT clause for ciscoEntityCapabilityV2R00,\n        ciscoEntityCapV12R0111bEXCat6K, ciscoEntityCapV12R0214SXCat6K,\n        ciscoEntityCapCatOSV08R0101, ciscoEntityCapabilityV20CRS1,\n        ciscoEntityCapabilityACSWV03R000 agent capabilities to \n        ENTITY-MIB from CISCO-ENTITY-MIB and modified the \n        DESCRIPTION clause accordingly.', 'Added ciscoEntityCapabilityIOSXRV3R4 agent\n        capabilities for IOS XR 3.4', 'Added ciscoEntityCapabilityACSWV03R000 agent\n        capabilities for Cisco Application Control \n        Engine (ACE).', 'Add VARIATION for the notification\n        entConfigChange in ciscoEntityCapCatOSV08R0101.', 'Added ciscoEntityCapabilityV20CRS1 Agent\n        capabilities for IOS XR release 2.0 CRS1', 'Updated the ciscoEntityCapability OID with the one\n        assigned by CANA.', 'Added ciscoEntityCapV12R0111bEXCat6K\n        ciscoEntityCapV12R0214SXCat6K and\n        ciscoEntityCapCatOSV08R0101.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntityCapability.setLastUpdated('2014-04-03 00:00')
if mibBuilder.loadTexts: ciscoEntityCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com\n            cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityCapability.setDescription('The Agent Capabilities for ENTITY-MIB.')
ciscoEntityCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV2R00 = ciscoEntityCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV2R00 = ciscoEntityCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapabilityV2R00.setDescription('Agent capabilities for ENTITY-MIB.')
ciscoEntityCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0111bEXCat6K = ciscoEntityCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0111bEXCat6K = ciscoEntityCapV12R0111bEXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapV12R0111bEXCat6K.setDescription('ENTITY-MIB capabilities.')
ciscoEntityCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0214SXCat6K = ciscoEntityCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapV12R0214SXCat6K = ciscoEntityCapV12R0214SXCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapV12R0214SXCat6K.setDescription('ENTITY-MIB capabilities.')
ciscoEntityCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapCatOSV08R0101 = ciscoEntityCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapCatOSV08R0101 = ciscoEntityCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapCatOSV08R0101.setDescription('ENTITY-MIB capabilities.')
ciscoEntityCapabilityV20CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV20CRS1 = ciscoEntityCapabilityV20CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityV20CRS1 = ciscoEntityCapabilityV20CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapabilityV20CRS1.setDescription('ENTITY-MIB capabilities for\n        IOS XR release 2.0')
ciscoEntityCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityACSWV03R000 = ciscoEntityCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityACSWV03R000 = ciscoEntityCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapabilityACSWV03R000.setDescription('ENTITY-MIB capabilities for ACSW 3.0')
ciscoEntityCapabilityIOSXRV3R4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityIOSXRV3R4 = ciscoEntityCapabilityIOSXRV3R4.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityIOSXRV3R4 = ciscoEntityCapabilityIOSXRV3R4.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapabilityIOSXRV3R4.setDescription('ENTITY-MIB capabilities for\n        IOS XR release 3.4')
ciscoEntityCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapc4710aceVA1R700 = ciscoEntityCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7) for \n                    ACE 4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapc4710aceVA1R700 = ciscoEntityCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapc4710aceVA1R700.setDescription('ENTITY-MIB capabilities for ACSW A1(7)')
ciscoEntityCapabilityGssV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityGssV03R01 = ciscoEntityCapabilityGssV03R01.setProductRelease('Global Site Selector(GSS) 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapabilityGssV03R01 = ciscoEntityCapabilityGssV03R01.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapabilityGssV03R01.setDescription('ENTITY-MIB capabilities for GSS 3.1(0)')
ciscoEntityCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0202PN7k = ciscoEntityCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0202PN7k = ciscoEntityCapNxOSV06R0202PN7k.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapNxOSV06R0202PN7k.setDescription('ENTITY-MIB capabilities capabilities.')
ciscoEntityCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 277, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0201PMds = ciscoEntityCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS 9000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityCapNxOSV06R0201PMds = ciscoEntityCapNxOSV06R0201PMds.setStatus('current')
if mibBuilder.loadTexts: ciscoEntityCapNxOSV06R0201PMds.setDescription('ENTITY-MIB capabilities capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-CAPABILITY", PYSNMP_MODULE_ID=ciscoEntityCapability, ciscoEntityCapCatOSV08R0101=ciscoEntityCapCatOSV08R0101, ciscoEntityCapNxOSV06R0201PMds=ciscoEntityCapNxOSV06R0201PMds, ciscoEntityCapNxOSV06R0202PN7k=ciscoEntityCapNxOSV06R0202PN7k, ciscoEntityCapV12R0111bEXCat6K=ciscoEntityCapV12R0111bEXCat6K, ciscoEntityCapV12R0214SXCat6K=ciscoEntityCapV12R0214SXCat6K, ciscoEntityCapability=ciscoEntityCapability, ciscoEntityCapabilityACSWV03R000=ciscoEntityCapabilityACSWV03R000, ciscoEntityCapabilityGssV03R01=ciscoEntityCapabilityGssV03R01, ciscoEntityCapabilityIOSXRV3R4=ciscoEntityCapabilityIOSXRV3R4, ciscoEntityCapabilityV20CRS1=ciscoEntityCapabilityV20CRS1, ciscoEntityCapabilityV2R00=ciscoEntityCapabilityV2R00, ciscoEntityCapc4710aceVA1R700=ciscoEntityCapc4710aceVA1R700)
