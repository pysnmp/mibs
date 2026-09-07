#
# PySNMP MIB module CISCO-SNMP-NOTIFICATION-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMP-NOTIFICATION-EXT-MIB
# Source digest sha256:168469d2bebd448c328c6b08fe1dae09f32a02819a2ec8327b852fd98eb23e80
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
snmpNotifyFilterEntry, = mibBuilder.importSymbols("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpNotificationExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 408))
ciscoSnmpNotificationExtMIB.setRevisions(('2004-05-12 00:00',))
if mibBuilder.loadTexts: ciscoSnmpNotificationExtMIB.setLastUpdated('2004-05-12 00:00')
if mibBuilder.loadTexts: ciscoSnmpNotificationExtMIB.setOrganization('Cisco Systems, Inc.')
csneMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 0))
csneMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 1))
csneMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 2))
csneNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1))
csneSnmpNotifyFilterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: csneSnmpNotifyFilterTable.setStatus('current')
csneSnmpNotifyFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1), ).setMaxAccess("notaccessible")
snmpNotifyFilterEntry.registerAugmentions(("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneSnmpNotifyFilterEntry"))
csneSnmpNotifyFilterEntry.setIndexNames(*snmpNotifyFilterEntry.getIndexNames())
if mibBuilder.loadTexts: csneSnmpNotifyFilterEntry.setStatus('current')
csneFilterAdminTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 1), Unsigned32().clone(15)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csneFilterAdminTimer.setStatus('current')
csneFilterOperTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csneFilterOperTimer.setStatus('current')
csneFilterTimerUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 408, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("seconds", 1), ("minutes", 2), ("hours", 3))).clone('minutes')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csneFilterTimerUnit.setStatus('current')
csneMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 1))
csneMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 2))
csneMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 1, 1)).setObjects(("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneNotifyFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csneMIBCompliance = csneMIBCompliance.setStatus('current')
csneNotifyFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 408, 2, 2, 1)).setObjects(("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterOperTimer"), ("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterAdminTimer"), ("CISCO-SNMP-NOTIFICATION-EXT-MIB", "csneFilterTimerUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csneNotifyFilterGroup = csneNotifyFilterGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-NOTIFICATION-EXT-MIB", PYSNMP_MODULE_ID=ciscoSnmpNotificationExtMIB, ciscoSnmpNotificationExtMIB=ciscoSnmpNotificationExtMIB, csneFilterAdminTimer=csneFilterAdminTimer, csneFilterOperTimer=csneFilterOperTimer, csneFilterTimerUnit=csneFilterTimerUnit, csneMIBCompliance=csneMIBCompliance, csneMIBCompliances=csneMIBCompliances, csneMIBConform=csneMIBConform, csneMIBGroups=csneMIBGroups, csneMIBNotifs=csneMIBNotifs, csneMIBObjects=csneMIBObjects, csneNotifyFilterGroup=csneNotifyFilterGroup, csneNotifyObjects=csneNotifyObjects, csneSnmpNotifyFilterEntry=csneSnmpNotifyFilterEntry, csneSnmpNotifyFilterTable=csneSnmpNotifyFilterTable)
