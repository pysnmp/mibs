#
# PySNMP MIB module CISCO-TCP-STD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-TCP-STD-CAPABILITY
# Source digest sha256:bd63963f7672d4b0b050f0a4cc300ada7aa93b9a183e3233afc5a66f09a87d5e
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTcpStdCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 481))
ciscoTcpStdCapability.setRevisions(('2008-08-11 00:00', '2008-02-08 00:00', '2006-11-08 00:00', '2006-10-25 00:00', '2006-05-26 00:00', '2006-02-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTcpStdCapability.setRevisionsDescriptions(('Added newlines at the end of the MIB file.', 'Added ciscoTcpStdCapc4710aceVA1R700 agent\n        capability for ACE 4710 Application Control Engine\n        Appliance.', 'Added ciscoTcpStdCapIOSXRV3R4CRS1 agent\n        capability for IOS XR 3.4', 'Added capability for Cisco TelePresence System (CTS) and\n        Cisco TelePresence Manager (CTM) platforms.', 'Added capability statement\n        ciscoTcpStdCapACSWV03R000', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTcpStdCapability.setLastUpdated('2008-08-11 00:00')
if mibBuilder.loadTexts: ciscoTcpStdCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTcpStdCapability.setContactInfo('Cisco Systems\n            Customer Service\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTcpStdCapability.setDescription('Agent capabilities for TCP-MIB')
ciscoTcpStdCapIOSXRV3R2CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R2CRS1 = ciscoTcpStdCapIOSXRV3R2CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R2CRS1 = ciscoTcpStdCapIOSXRV3R2CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapIOSXRV3R2CRS1.setDescription('TCP-MIB capabilities\n        for IOS XR release 3.2.0')
ciscoTcpStdCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapACSWV03R000 = ciscoTcpStdCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n\n                    for Application Control Engine(ACE)\n\n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapACSWV03R000 = ciscoTcpStdCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapACSWV03R000.setDescription('TCP-MIB capabilities for ACSW 3.0')
ciscoTcpStdCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTSV100 = ciscoTcpStdCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTSV100 = ciscoTcpStdCapCTSV100.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapCTSV100.setDescription('TCP-MIB capabilities for CTS 1.0.0')
ciscoTcpStdCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTMV1000 = ciscoTcpStdCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapCTMV1000 = ciscoTcpStdCapCTMV1000.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapCTMV1000.setDescription('TCP-MIB capabilities for CTM 1.0.0.0')
ciscoTcpStdCapIOSXRV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R4CRS1 = ciscoTcpStdCapIOSXRV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapIOSXRV3R4CRS1 = ciscoTcpStdCapIOSXRV3R4CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapIOSXRV3R4CRS1.setDescription('TCP-MIB capabilities\n        for IOS XR release 3.4')
ciscoTcpStdCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 481, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapc4710aceVA1R700 = ciscoTcpStdCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpStdCapc4710aceVA1R700 = ciscoTcpStdCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoTcpStdCapc4710aceVA1R700.setDescription('TCP-MIB capabilities for ACSW A1(7)')
mibBuilder.exportSymbols("CISCO-TCP-STD-CAPABILITY", PYSNMP_MODULE_ID=ciscoTcpStdCapability, ciscoTcpStdCapACSWV03R000=ciscoTcpStdCapACSWV03R000, ciscoTcpStdCapCTMV1000=ciscoTcpStdCapCTMV1000, ciscoTcpStdCapCTSV100=ciscoTcpStdCapCTSV100, ciscoTcpStdCapIOSXRV3R2CRS1=ciscoTcpStdCapIOSXRV3R2CRS1, ciscoTcpStdCapIOSXRV3R4CRS1=ciscoTcpStdCapIOSXRV3R4CRS1, ciscoTcpStdCapability=ciscoTcpStdCapability, ciscoTcpStdCapc4710aceVA1R700=ciscoTcpStdCapc4710aceVA1R700)
