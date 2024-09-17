#
# PySNMP MIB module ALPHA-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alpha/ALPHA-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 11:59:14 2024
# On host fv-az888-540 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
alarmModelDescription, alarmActiveModelPointer, alarmActiveResourceId = mibBuilder.importSymbols("ALARM-MIB", "alarmModelDescription", "alarmActiveModelPointer", "alarmActiveResourceId")
alpha, componentListStaticName, componentListReference, controllerInfoName = mibBuilder.importSymbols("ALPHA-RESOURCE-MIB", "alpha", "componentListStaticName", "componentListReference", "controllerInfoName")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Counter64, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Counter32, IpAddress, Unsigned32, Bits, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Counter32", "IpAddress", "Unsigned32", "Bits", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alphaAlarmNotifications = ModuleIdentity((1, 3, 6, 1, 4, 1, 7309, 100))
alphaAlarmNotifications.setRevisions(('2017-07-31 00:00', '2015-07-28 00:00', '2015-07-23 00:00', '2015-06-23 00:00',))
if mibBuilder.loadTexts: alphaAlarmNotifications.setLastUpdated('201707310000Z')
if mibBuilder.loadTexts: alphaAlarmNotifications.setOrganization('Alpha Technologies Ltd.')
alphaAlarmNotificationsExtension = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 101))
alphaAlarmActiveState = NotificationType((1, 3, 6, 1, 4, 1, 7309, 100, 1)).setObjects(("ALARM-MIB", "alarmActiveModelPointer"), ("ALARM-MIB", "alarmActiveResourceId"), ("ALPHA-NOTIFICATION-MIB", "alarmPriority"), ("ALARM-MIB", "alarmModelDescription"), ("ALPHA-RESOURCE-MIB", "componentListStaticName"), ("ALPHA-RESOURCE-MIB", "componentListReference"), ("ALPHA-NOTIFICATION-MIB", "alarmSeverity"), ("ALPHA-RESOURCE-MIB", "controllerInfoName"), ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"), ("ALPHA-NOTIFICATION-MIB", "alarmAdditionalInformation"))
if mibBuilder.loadTexts: alphaAlarmActiveState.setStatus('current')
alphaAlarmClearState = NotificationType((1, 3, 6, 1, 4, 1, 7309, 100, 2)).setObjects(("ALARM-MIB", "alarmActiveModelPointer"), ("ALARM-MIB", "alarmActiveResourceId"), ("ALPHA-NOTIFICATION-MIB", "alarmPriority"), ("ALARM-MIB", "alarmModelDescription"), ("ALPHA-RESOURCE-MIB", "componentListStaticName"), ("ALPHA-RESOURCE-MIB", "componentListReference"), ("ALPHA-NOTIFICATION-MIB", "alarmSeverity"), ("ALPHA-RESOURCE-MIB", "controllerInfoName"), ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"), ("ALPHA-NOTIFICATION-MIB", "alarmAdditionalInformation"))
if mibBuilder.loadTexts: alphaAlarmClearState.setStatus('current')
alarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 7309, 101, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSeverity.setStatus('current')
alarmCustomDescription = MibScalar((1, 3, 6, 1, 4, 1, 7309, 101, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmCustomDescription.setStatus('current')
alarmPriority = MibScalar((1, 3, 6, 1, 4, 1, 7309, 101, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPriority.setStatus('current')
alarmAdditionalInformation = MibScalar((1, 3, 6, 1, 4, 1, 7309, 101, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmAdditionalInformation.setStatus('current')
alphaAlarmNotificationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 100, 102))
alphaAlarmNotificationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1))
alphaAlarmNotificationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 1)).setObjects(("ALPHA-NOTIFICATION-MIB", "alphaParameterGroup"), ("ALPHA-NOTIFICATION-MIB", "alphaNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaAlarmNotificationCompliance = alphaAlarmNotificationCompliance.setStatus('current')
alphaAlarmNotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2))
alphaParameterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2, 1)).setObjects(("ALPHA-NOTIFICATION-MIB", "alarmSeverity"), ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"), ("ALPHA-NOTIFICATION-MIB", "alarmPriority"), ("ALPHA-NOTIFICATION-MIB", "alarmAdditionalInformation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaParameterGroup = alphaParameterGroup.setStatus('current')
alphaNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2, 2)).setObjects(("ALPHA-NOTIFICATION-MIB", "alphaAlarmActiveState"), ("ALPHA-NOTIFICATION-MIB", "alphaAlarmClearState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaNotificationsGroup = alphaNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ALPHA-NOTIFICATION-MIB", alphaAlarmNotificationCompliances=alphaAlarmNotificationCompliances, alphaAlarmNotificationCompliance=alphaAlarmNotificationCompliance, alarmCustomDescription=alarmCustomDescription, alphaAlarmNotifications=alphaAlarmNotifications, alphaAlarmClearState=alphaAlarmClearState, alphaAlarmNotificationConformance=alphaAlarmNotificationConformance, alarmAdditionalInformation=alarmAdditionalInformation, alphaParameterGroup=alphaParameterGroup, alphaAlarmNotificationGroups=alphaAlarmNotificationGroups, alphaAlarmNotificationsExtension=alphaAlarmNotificationsExtension, PYSNMP_MODULE_ID=alphaAlarmNotifications, alarmSeverity=alarmSeverity, alphaNotificationsGroup=alphaNotificationsGroup, alarmPriority=alarmPriority, alphaAlarmActiveState=alphaAlarmActiveState)
