#
# PySNMP MIB module CISCO-SNMP-NOTIFICATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMP-NOTIFICATION-CAPABILITY
# Source digest sha256:50ba4bc0f41c45fa4da42c0920773b35793b6fd3470b4ed73ef524d6abd1a98c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpNotificationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 330))
ciscoSnmpNotificationCapability.setRevisions(('2008-06-25 00:00', '2006-03-29 00:00', '2004-07-28 00:00', '2003-08-28 00:00',))
if mibBuilder.loadTexts: ciscoSnmpNotificationCapability.setLastUpdated('2008-06-25 00:00')
if mibBuilder.loadTexts: ciscoSnmpNotificationCapability.setOrganization('Cisco Systems, Inc.')
cSnmpNotifCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapCatOSV05R0501 = cSnmpNotifCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapCatOSV05R0501 = cSnmpNotifCapCatOSV05R0501.setStatus('current')
cSnmpNotifCapVISM33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapVISM33 = cSnmpNotifCapVISM33.setProductRelease('Cisco VISM Release 3.3.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapVISM33 = cSnmpNotifCapVISM33.setStatus('current')
cSnmpNotifCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapACSWV03R000 = cSnmpNotifCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapACSWV03R000 = cSnmpNotifCapACSWV03R000.setStatus('current')
cSnmpNotifCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapc4710aceVA1R700 = cSnmpNotifCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapc4710aceVA1R700 = cSnmpNotifCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-NOTIFICATION-CAPABILITY", PYSNMP_MODULE_ID=ciscoSnmpNotificationCapability, cSnmpNotifCapACSWV03R000=cSnmpNotifCapACSWV03R000, cSnmpNotifCapCatOSV05R0501=cSnmpNotifCapCatOSV05R0501, cSnmpNotifCapVISM33=cSnmpNotifCapVISM33, cSnmpNotifCapc4710aceVA1R700=cSnmpNotifCapc4710aceVA1R700, ciscoSnmpNotificationCapability=ciscoSnmpNotificationCapability)
