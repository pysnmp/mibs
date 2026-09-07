#
# PySNMP MIB module CISCO-SNMP-USM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMP-USM-CAPABILITY
# Source digest sha256:3167938b3b8c4d9077c614840de8860142970c719867cb015b6c17e54d44e216
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpUsmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 323))
ciscoSnmpUsmCapability.setRevisions(('2008-08-01 00:00', '2006-05-22 00:00', '2003-08-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setRevisionsDescriptions(('Added the correct mib name under the\n        SUPPORTS clause for ciscoSnmpUsmCapCatOSV05R0501\n        and ciscoSnmpUsmCapACSWV03R000.\n        Added terminating quotes for \n        ciscoSnmpUsmCapACSWV03R000 PRODUCT-RELEASE clause.\n        Added capability statement \n        ciscoSnmpUsmCapc4710aceVA1R700 for ACE 4710 Application\n        Control Engine Appliance.', 'Added capability statement\n        ciscoSnmpUsmCapACSWV03R000 for \n        Application Control Engine (ACE).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setLastUpdated('2008-08-01 00:00')
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setDescription('The capabilities description of SNMP-USER-BASED-SM-MIB.')
ciscoSnmpUsmCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapCatOSV05R0501 = ciscoSnmpUsmCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapCatOSV05R0501 = ciscoSnmpUsmCapCatOSV05R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpUsmCapCatOSV05R0501.setDescription('SNMP-USER-BASED-SM-MIB capabilities.')
ciscoSnmpUsmCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapACSWV03R000 = ciscoSnmpUsmCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapACSWV03R000 = ciscoSnmpUsmCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpUsmCapACSWV03R000.setDescription('SNMP-USER-BASED-SM-MIB capabilities.')
ciscoSnmpUsmCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapc4710aceVA1R700 = ciscoSnmpUsmCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapc4710aceVA1R700 = ciscoSnmpUsmCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpUsmCapc4710aceVA1R700.setDescription('SNMP-USER-BASED-SM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-USM-CAPABILITY", PYSNMP_MODULE_ID=ciscoSnmpUsmCapability, ciscoSnmpUsmCapACSWV03R000=ciscoSnmpUsmCapACSWV03R000, ciscoSnmpUsmCapCatOSV05R0501=ciscoSnmpUsmCapCatOSV05R0501, ciscoSnmpUsmCapability=ciscoSnmpUsmCapability, ciscoSnmpUsmCapc4710aceVA1R700=ciscoSnmpUsmCapc4710aceVA1R700)
