#
# PySNMP MIB module CISCO-SYSLOG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SYSLOG-CAPABILITY
# Source digest sha256:807bf246b77b0f4b5c90170822599fbdcc191e2cb4b81ae5b6e409b0456ff914
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSyslogCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 61))
ciscoSyslogCapability.setRevisions(('2010-01-22 14:32', '2008-08-11 00:00', '2008-06-08 00:00', '2006-10-26 00:00', '2006-05-25 00:00', '2004-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSyslogCapability.setRevisionsDescriptions(('Added capability for Visual Quality Experience Server (VQE-S)\n        and Visual Quality Experience Tools (VQE-TOOLS) platforms.', 'Adding newlines at the end of the MIB file.', 'Added Agent capability for ACE 4710 Application\n        Control Engine Appliance.', 'Added capability for Cisco TelePresence System (CTS) and\n        Cisco TelePresence Manager (CTM) platforms.', 'Added Agent capability\n        ciscoSyslogCapACSWV03R000 for\n        Application Control Engine (ACE).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSyslogCapability.setLastUpdated('2010-01-22 14:32')
if mibBuilder.loadTexts: ciscoSyslogCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSyslogCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com\n            cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSyslogCapability.setDescription('The capabilities description of CISCO-SYSLOG-MIB.')
ciscoSyslogCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCatOSV08R0101 = ciscoSyslogCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCatOSV08R0101 = ciscoSyslogCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapCatOSV08R0101.setDescription('CISCO-SYSLOG-MIB capabilities.')
ciscoSyslogCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapACSWV03R000 = ciscoSyslogCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n \n                   for Application Control Engine(ACE)\n\n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapACSWV03R000 = ciscoSyslogCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapACSWV03R000.setDescription('CISCO-SYSLOG-MIB capabilities.')
ciscoSyslogCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTSV100 = ciscoSyslogCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTSV100 = ciscoSyslogCapCTSV100.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapCTSV100.setDescription('CISCO-SYSLOG-MIB capabilities.')
ciscoSyslogCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTMV1000 = ciscoSyslogCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTMV1000 = ciscoSyslogCapCTMV1000.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapCTMV1000.setDescription('CISCO-SYSLOG-MIB capabilities.')
ciscoSyslogCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapc4710aceVA1R70 = ciscoSyslogCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapc4710aceVA1R70 = ciscoSyslogCapc4710aceVA1R70.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapc4710aceVA1R70.setDescription('CISCO-SYSLOG-MIB capabilities.')
ciscoSyslogCapVqe = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapVqe = ciscoSyslogCapVqe.setProductRelease('VQE 3.5 release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapVqe = ciscoSyslogCapVqe.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapVqe.setDescription('CISCO-SYSLOG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SYSLOG-CAPABILITY", PYSNMP_MODULE_ID=ciscoSyslogCapability, ciscoSyslogCapACSWV03R000=ciscoSyslogCapACSWV03R000, ciscoSyslogCapCTMV1000=ciscoSyslogCapCTMV1000, ciscoSyslogCapCTSV100=ciscoSyslogCapCTSV100, ciscoSyslogCapCatOSV08R0101=ciscoSyslogCapCatOSV08R0101, ciscoSyslogCapVqe=ciscoSyslogCapVqe, ciscoSyslogCapability=ciscoSyslogCapability, ciscoSyslogCapc4710aceVA1R70=ciscoSyslogCapc4710aceVA1R70)
