#
# PySNMP MIB module ALPHA-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alpha/ALPHA-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 26 02:10:03 2024
# On host fv-az1144-917 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
alarmModelDescription, alarmActiveModelPointer, alarmActiveResourceId = mibBuilder.importSymbols("ALARM-MIB", "alarmModelDescription", "alarmActiveModelPointer", "alarmActiveResourceId")
componentListStaticName, controllerInfoName, componentListReference, alpha = mibBuilder.importSymbols("ALPHA-RESOURCE-MIB", "componentListStaticName", "controllerInfoName", "componentListReference", "alpha")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, MibIdentifier, IpAddress, ModuleIdentity, ObjectIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Counter32, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "MibIdentifier", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Counter32", "Unsigned32", "NotificationType")
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
mibBuilder.exportSymbols("ALPHA-NOTIFICATION-MIB", alphaAlarmActiveState=alphaAlarmActiveState, alarmAdditionalInformation=alarmAdditionalInformation, PYSNMP_MODULE_ID=alphaAlarmNotifications, alphaAlarmNotificationCompliances=alphaAlarmNotificationCompliances, alphaAlarmNotificationsExtension=alphaAlarmNotificationsExtension, alphaAlarmNotificationCompliance=alphaAlarmNotificationCompliance, alphaAlarmNotificationGroups=alphaAlarmNotificationGroups, alarmSeverity=alarmSeverity, alphaNotificationsGroup=alphaNotificationsGroup, alarmCustomDescription=alarmCustomDescription, alarmPriority=alarmPriority, alphaAlarmNotificationConformance=alphaAlarmNotificationConformance, alphaAlarmClearState=alphaAlarmClearState, alphaAlarmNotifications=alphaAlarmNotifications, alphaParameterGroup=alphaParameterGroup)
