#
# PySNMP MIB module ALPHA-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alpha/ALPHA-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:18:41 2024
# On host fv-az1019-803 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
alarmActiveModelPointer, alarmModelDescription, alarmActiveResourceId = mibBuilder.importSymbols("ALARM-MIB", "alarmActiveModelPointer", "alarmModelDescription", "alarmActiveResourceId")
componentListReference, componentListStaticName, alpha, controllerInfoName = mibBuilder.importSymbols("ALPHA-RESOURCE-MIB", "componentListReference", "componentListStaticName", "alpha", "controllerInfoName")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, TimeTicks, MibIdentifier, Counter64, IpAddress, Integer32, ModuleIdentity, iso, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "TimeTicks", "MibIdentifier", "Counter64", "IpAddress", "Integer32", "ModuleIdentity", "iso", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ALPHA-NOTIFICATION-MIB", alphaAlarmActiveState=alphaAlarmActiveState, alarmSeverity=alarmSeverity, PYSNMP_MODULE_ID=alphaAlarmNotifications, alarmCustomDescription=alarmCustomDescription, alphaNotificationsGroup=alphaNotificationsGroup, alphaAlarmNotificationsExtension=alphaAlarmNotificationsExtension, alphaAlarmNotificationConformance=alphaAlarmNotificationConformance, alarmAdditionalInformation=alarmAdditionalInformation, alphaAlarmNotificationCompliance=alphaAlarmNotificationCompliance, alphaAlarmClearState=alphaAlarmClearState, alarmPriority=alarmPriority, alphaAlarmNotifications=alphaAlarmNotifications, alphaAlarmNotificationCompliances=alphaAlarmNotificationCompliances, alphaAlarmNotificationGroups=alphaAlarmNotificationGroups, alphaParameterGroup=alphaParameterGroup)
