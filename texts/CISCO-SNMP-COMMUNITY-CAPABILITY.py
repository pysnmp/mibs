#
# PySNMP MIB module CISCO-SNMP-COMMUNITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMP-COMMUNITY-CAPABILITY
# Source digest sha256:094608aaad98961f93b71d9d96e39fb5a704f266986e677690cda12189492fa7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpCommunityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 318))
ciscoSnmpCommunityCapability.setRevisions(('2008-08-04 00:00', '2006-03-29 00:00', '2004-01-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setRevisionsDescriptions(('Added capability statement\n        cSnmpCommunityCapc4710aceVA1R700 for ACE 4710 \n        Application Control Engine Appliance.', 'Added capability statement\n        cSnmpCommunityCapACSWV03R000 \n        for Application Control Engine (ACE).\n\n        Updated the conformance group name for \n        cSnmpCommunityCapCatOSV06R0301 from \n        snmpCommunityGroup to snmpCommunityTableGroup\n        since the new version of SNMP-COMMUNITY-MIB \n        (RFC3584) has changed the name to avoid conflicts \n        with SNMPv2-MIB.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setLastUpdated('2008-08-04 00:00')
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpCommunityCapability.setDescription('The capabilities description of\n        SNMP-COMMUNITY-MIB.')
cSnmpCommunityCapCatOSV06R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapCatOSV06R0301 = cSnmpCommunityCapCatOSV06R0301.setProductRelease('Cisco CatOS 6.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapCatOSV06R0301 = cSnmpCommunityCapCatOSV06R0301.setStatus('current')
if mibBuilder.loadTexts: cSnmpCommunityCapCatOSV06R0301.setDescription('SNMP-COMMUNITY-MIB capabilities.')
cSnmpCommunityCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapACSWV03R000 = cSnmpCommunityCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapACSWV03R000 = cSnmpCommunityCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cSnmpCommunityCapACSWV03R000.setDescription('SNMP-COMMUNITY-MIB capabilities.')
cSnmpCommunityCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 318, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapc4710aceVA1R700 = cSnmpCommunityCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpCommunityCapc4710aceVA1R700 = cSnmpCommunityCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cSnmpCommunityCapc4710aceVA1R700.setDescription('SNMP-COMMUNITY-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-COMMUNITY-CAPABILITY", PYSNMP_MODULE_ID=ciscoSnmpCommunityCapability, cSnmpCommunityCapACSWV03R000=cSnmpCommunityCapACSWV03R000, cSnmpCommunityCapCatOSV06R0301=cSnmpCommunityCapCatOSV06R0301, cSnmpCommunityCapc4710aceVA1R700=cSnmpCommunityCapc4710aceVA1R700, ciscoSnmpCommunityCapability=ciscoSnmpCommunityCapability)
