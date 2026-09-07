#
# PySNMP MIB module CISCO-MODULE-AUTO-SHUTDOWN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MODULE-AUTO-SHUTDOWN-MIB
# Source digest sha256:df0892ad61831cbb29e99b973c5f2a34726ce2ff12cdc4bf22e42593891c40ea
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, entPhysicalModelName, entPhysicalName = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalModelName", "entPhysicalName")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DateAndTime, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "TruthValue")
ciscoModuleAutoShutdownMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 386))
ciscoModuleAutoShutdownMIB.setRevisions(('2008-03-12 00:00', '2003-12-29 00:00',))
if mibBuilder.loadTexts: ciscoModuleAutoShutdownMIB.setLastUpdated('2008-03-12 00:00')
if mibBuilder.loadTexts: ciscoModuleAutoShutdownMIB.setOrganization('Cisco Systems, Inc.')
cmasMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 0))
cmasMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1))
cmasMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2))
cmasGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1))
cmasNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2))
cmasModule = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3))
cmasModuleSysActionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4))
class CiscoModuleAutoShutSysAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("reset", 2), ("powerCycle", 3), ("powerDown", 4))

cmasFrequency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasFrequency.setStatus('current')
cmasPeriod = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 1, 2), Unsigned32()).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasPeriod.setStatus('current')
cmasMIBEnableNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasMIBEnableNotification.setStatus('current')
cmasModuleSysActionNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasModuleSysActionNotifEnable.setStatus('current')
cmasModuleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cmasModuleTable.setStatus('current')
cmasModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cmasModuleEntry.setStatus('current')
cmasModuleEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmasModuleEnable.setStatus('current')
cmasModuleNumResets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleNumResets.setStatus('current')
cmasModuleLastResetReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleLastResetReason.setStatus('current')
cmasModuleLastResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 3, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmasModuleLastResetTime.setStatus('current')
cmasModuleSysAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4, 1), CiscoModuleAutoShutSysAction()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmasModuleSysAction.setStatus('current')
cmasModuleSysActionReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 386, 1, 4, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cmasModuleSysActionReason.setStatus('current')
cmasModuleAutoShutdown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 386, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleNumResets"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetReason"))
if mibBuilder.loadTexts: cmasModuleAutoShutdown.setStatus('current')
cmasModuleSysActionNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 386, 0, 2)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysAction"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionReason"))
if mibBuilder.loadTexts: cmasModuleSysActionNotif.setStatus('current')
cmasMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1))
cmasMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2))
cmasMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1, 1)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationEnableGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasMIBCompliance = cmasMIBCompliance.setStatus('deprecated')
cmasMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 1, 2)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationEnableGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionGroup"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasNotificationsGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasMIBCompliance2 = cmasMIBCompliance2.setStatus('current')
cmasModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 1)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasFrequency"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasPeriod"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleEnable"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleNumResets"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetReason"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleLastResetTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasModuleGroup = cmasModuleGroup.setStatus('current')
cmasNotificationEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 2)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasMIBEnableNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationEnableGroup = cmasNotificationEnableGroup.setStatus('current')
cmasNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 3)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleAutoShutdown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationsGroup = cmasNotificationsGroup.setStatus('current')
cmasModuleSysActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 4)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionNotifEnable"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysAction"), ("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasModuleSysActionGroup = cmasModuleSysActionGroup.setStatus('current')
cmasNotificationsGroup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 386, 2, 2, 5)).setObjects(("CISCO-MODULE-AUTO-SHUTDOWN-MIB", "cmasModuleSysActionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmasNotificationsGroup2 = cmasNotificationsGroup2.setStatus('current')
mibBuilder.exportSymbols("CISCO-MODULE-AUTO-SHUTDOWN-MIB", CiscoModuleAutoShutSysAction=CiscoModuleAutoShutSysAction, PYSNMP_MODULE_ID=ciscoModuleAutoShutdownMIB, ciscoModuleAutoShutdownMIB=ciscoModuleAutoShutdownMIB, cmasFrequency=cmasFrequency, cmasGlobal=cmasGlobal, cmasMIBCompliance2=cmasMIBCompliance2, cmasMIBCompliance=cmasMIBCompliance, cmasMIBCompliances=cmasMIBCompliances, cmasMIBConformance=cmasMIBConformance, cmasMIBEnableNotification=cmasMIBEnableNotification, cmasMIBGroups=cmasMIBGroups, cmasMIBNotifs=cmasMIBNotifs, cmasMIBObjects=cmasMIBObjects, cmasModule=cmasModule, cmasModuleAutoShutdown=cmasModuleAutoShutdown, cmasModuleEnable=cmasModuleEnable, cmasModuleEntry=cmasModuleEntry, cmasModuleGroup=cmasModuleGroup, cmasModuleLastResetReason=cmasModuleLastResetReason, cmasModuleLastResetTime=cmasModuleLastResetTime, cmasModuleNumResets=cmasModuleNumResets, cmasModuleSysAction=cmasModuleSysAction, cmasModuleSysActionGroup=cmasModuleSysActionGroup, cmasModuleSysActionNotif=cmasModuleSysActionNotif, cmasModuleSysActionNotifEnable=cmasModuleSysActionNotifEnable, cmasModuleSysActionObjects=cmasModuleSysActionObjects, cmasModuleSysActionReason=cmasModuleSysActionReason, cmasModuleTable=cmasModuleTable, cmasNotifObjects=cmasNotifObjects, cmasNotificationEnableGroup=cmasNotificationEnableGroup, cmasNotificationsGroup2=cmasNotificationsGroup2, cmasNotificationsGroup=cmasNotificationsGroup, cmasPeriod=cmasPeriod)
