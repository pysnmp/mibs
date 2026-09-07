#
# PySNMP MIB module CISCO-SNMPv2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMPv2-CAPABILITY
# Source digest sha256:3f0439ac3834bd768864733fadc587fe2e5a68c5a55583b362f46eb60800b103
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpV2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 113))
ciscoSnmpV2Capability.setRevisions(('2007-11-12 00:00', '2006-05-30 00:00', '2006-04-24 00:00', '2004-03-18 00:00', '2002-02-07 00:00', '2002-01-31 00:00', '1994-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpV2Capability.setRevisionsDescriptions(('Added capability statement\n        ciscoSnmpV2Capc4710aceVA1R700 for ACE \n        4710 Application Control Engine Appliance.', 'Added capability statement\n        ciscoSnmpV2CapACSWV03R000 for Application\n        Control Engine (ACE).\n\n        For ciscoSnmpV2CapabilityV10R02 commented\n        out references to object groups \n        snmpStatsGroup, snmpV1Group, snmpORGroup,\n        snmpTrapGroup because they are defined only \n        in the original RFC 1450, not in the latest\n        RFC 3418.', 'Added the VARIATION for the notification\n        authenticationFailure in \n        ciscoSnmpV2CapCatOSV08R0301.\n\n        Added capability statement\n        ciscoSnmpV2CapCatOSV08R0601.', 'Added ciscoSnmpV2CapCatOSV08R0301.', 'Added following agent capabilities:\n        - ciscoMgxSnmpV2CapabilityV20 for\n          MGX8850 series\n        - ciscoBpxSesSnmpV2CapabilityV10 for\n           BPX SES.', "Added 'ciscoRpmsSnmpV2CapabilityV20' for\n        Cisco Resource Policy Management Server\n        (RPMS) 2.0.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpV2Capability.setLastUpdated('2007-11-12 00:00')
if mibBuilder.loadTexts: ciscoSnmpV2Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpV2Capability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpV2Capability.setDescription('Agent capabilities for SNMPv2-MIB')
ciscoSnmpV2CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapabilityV10R02 = ciscoSnmpV2CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapabilityV10R02 = ciscoSnmpV2CapabilityV10R02.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpV2CapabilityV10R02.setDescription('IOS 10.2 SNMPv2 MIB capabilities')
ciscoRpmsSnmpV2CapabilityV20 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRpmsSnmpV2CapabilityV20 = ciscoRpmsSnmpV2CapabilityV20.setProductRelease('Cisco Resource Policy Management Server (RPMS) 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRpmsSnmpV2CapabilityV20 = ciscoRpmsSnmpV2CapabilityV20.setStatus('current')
if mibBuilder.loadTexts: ciscoRpmsSnmpV2CapabilityV20.setDescription('Cisco RPMS 2.0 SNMPv2 MIB capabilities.')
ciscoMgxSnmpV2CapabilityV20 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgxSnmpV2CapabilityV20 = ciscoMgxSnmpV2CapabilityV20.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgxSnmpV2CapabilityV20 = ciscoMgxSnmpV2CapabilityV20.setStatus('current')
if mibBuilder.loadTexts: ciscoMgxSnmpV2CapabilityV20.setDescription('SNMPv2-MIB capabilities in MGX Series.')
ciscoBpxSesSnmpV2CapabilityV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBpxSesSnmpV2CapabilityV10 = ciscoBpxSesSnmpV2CapabilityV10.setProductRelease('Cisco BPX SES Release 1.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBpxSesSnmpV2CapabilityV10 = ciscoBpxSesSnmpV2CapabilityV10.setStatus('current')
if mibBuilder.loadTexts: ciscoBpxSesSnmpV2CapabilityV10.setDescription('SNMPv2-MIB capabilities.')
ciscoSnmpV2CapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0301 = ciscoSnmpV2CapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) for Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0301 = ciscoSnmpV2CapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpV2CapCatOSV08R0301.setDescription('SNMPv2-MIB capabilities.')
ciscoSnmpV2CapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0601 = ciscoSnmpV2CapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1) for Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0601 = ciscoSnmpV2CapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpV2CapCatOSV08R0601.setDescription('SNMPv2-MIB capabilities.')
ciscoSnmpV2CapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapACSWV03R000 = ciscoSnmpV2CapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                          for Application Control Engine (ACE) \n                          Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapACSWV03R000 = ciscoSnmpV2CapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpV2CapACSWV03R000.setDescription('SNMPv2-MIB capabilities.')
ciscoSnmpV2Capc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2Capc4710aceVA1R700 = ciscoSnmpV2Capc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2Capc4710aceVA1R700 = ciscoSnmpV2Capc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpV2Capc4710aceVA1R700.setDescription('SNMPv2-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMPv2-CAPABILITY", PYSNMP_MODULE_ID=ciscoSnmpV2Capability, ciscoBpxSesSnmpV2CapabilityV10=ciscoBpxSesSnmpV2CapabilityV10, ciscoMgxSnmpV2CapabilityV20=ciscoMgxSnmpV2CapabilityV20, ciscoRpmsSnmpV2CapabilityV20=ciscoRpmsSnmpV2CapabilityV20, ciscoSnmpV2CapACSWV03R000=ciscoSnmpV2CapACSWV03R000, ciscoSnmpV2CapCatOSV08R0301=ciscoSnmpV2CapCatOSV08R0301, ciscoSnmpV2CapCatOSV08R0601=ciscoSnmpV2CapCatOSV08R0601, ciscoSnmpV2Capability=ciscoSnmpV2Capability, ciscoSnmpV2CapabilityV10R02=ciscoSnmpV2CapabilityV10R02, ciscoSnmpV2Capc4710aceVA1R700=ciscoSnmpV2Capc4710aceVA1R700)
