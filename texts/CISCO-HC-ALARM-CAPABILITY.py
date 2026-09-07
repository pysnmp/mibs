#
# PySNMP MIB module CISCO-HC-ALARM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-HC-ALARM-CAPABILITY
# Source digest sha256:978af2067a446668bd28ace6a84587df0b3f44d5a8ba8adb7842193f49994606
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TextualConvention")
ciscoHcAlarmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 398))
ciscoHcAlarmCapability.setRevisions(('2008-08-05 00:00', '2004-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHcAlarmCapability.setRevisionsDescriptions(('Added capability statement ciscoHcAlarmCapNXOSV04R0101.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setLastUpdated('2008-08-05 00:00')
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setDescription('The capabilities description of HC-ALARM-MIB.')
ciscoHcAlarmCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 398, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapCatOSV08R0401 = ciscoHcAlarmCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapCatOSV08R0401 = ciscoHcAlarmCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoHcAlarmCapCatOSV08R0401.setDescription('HC-ALARM-MIB capabilities.')
ciscoHcAlarmCapNXOSV04R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 398, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapNXOSV04R0101 = ciscoHcAlarmCapNXOSV04R0101.setProductRelease('Cisco NX-OS 4.1(1) on MDS9000 Storage Switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapNXOSV04R0101 = ciscoHcAlarmCapNXOSV04R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoHcAlarmCapNXOSV04R0101.setDescription('HC-RMON-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-HC-ALARM-CAPABILITY", PYSNMP_MODULE_ID=ciscoHcAlarmCapability, ciscoHcAlarmCapCatOSV08R0401=ciscoHcAlarmCapCatOSV08R0401, ciscoHcAlarmCapNXOSV04R0101=ciscoHcAlarmCapNXOSV04R0101, ciscoHcAlarmCapability=ciscoHcAlarmCapability)
