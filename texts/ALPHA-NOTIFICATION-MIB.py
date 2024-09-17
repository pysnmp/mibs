#
# PySNMP MIB module ALPHA-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alpha/ALPHA-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 11:59:16 2024
# On host fv-az888-540 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
alarmActiveResourceId, alarmModelDescription, alarmActiveModelPointer = mibBuilder.importSymbols("ALARM-MIB", "alarmActiveResourceId", "alarmModelDescription", "alarmActiveModelPointer")
componentListReference, controllerInfoName, alpha, componentListStaticName = mibBuilder.importSymbols("ALPHA-RESOURCE-MIB", "componentListReference", "controllerInfoName", "alpha", "componentListStaticName")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Integer32, MibIdentifier, ModuleIdentity, TimeTicks, Gauge32, NotificationType, Counter32, IpAddress, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Integer32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Gauge32", "NotificationType", "Counter32", "IpAddress", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alphaAlarmNotifications = ModuleIdentity((1, 3, 6, 1, 4, 1, 7309, 100))
alphaAlarmNotifications.setRevisions(('2017-07-31 00:00', '2015-07-28 00:00', '2015-07-23 00:00', '2015-06-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alphaAlarmNotifications.setRevisionsDescriptions(('\n\t\t\tAdded alarmAdditionalInformation varbinds.\n\t\t\tTested with SimpleWeb: http://www.simpleweb.org      \n\t\t\tPassed highest level of compliance.  (level 6)\n\t\t\t', '\n\t\t\tUpdated to follow MIB structure conformance rules.  Tested with \n\t\t\tSimpleWeb: http://www.simpleweb.org      \n\t\t\tPassed highest level of compliance.  (level 6)\n\t\t\t', 'Fixed MIB syntax warnings.', 'General revision.',))
if mibBuilder.loadTexts: alphaAlarmNotifications.setLastUpdated('201707310000Z')
if mibBuilder.loadTexts: alphaAlarmNotifications.setOrganization('Alpha Technologies Ltd.')
if mibBuilder.loadTexts: alphaAlarmNotifications.setContactInfo('Alpha Technologies Ltd.\n\t\t\t  7700 Riverfront Gate\n\t\t\t  Burnaby, BC  V5J 5M4\n\t\t\t  Canada\n\n\t\t\t  Tel: 1-604-436-5900\n\t\t\t  Fax: 1-604-436-1233')
if mibBuilder.loadTexts: alphaAlarmNotifications.setDescription('This MIB defines the notification block(s) available in system controllers.')
alphaAlarmNotificationsExtension = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 101))
alphaAlarmActiveState = NotificationType((1, 3, 6, 1, 4, 1, 7309, 100, 1)).setObjects(("ALARM-MIB", "alarmActiveModelPointer"), ("ALARM-MIB", "alarmActiveResourceId"), ("ALPHA-NOTIFICATION-MIB", "alarmPriority"), ("ALARM-MIB", "alarmModelDescription"), ("ALPHA-RESOURCE-MIB", "componentListStaticName"), ("ALPHA-RESOURCE-MIB", "componentListReference"), ("ALPHA-NOTIFICATION-MIB", "alarmSeverity"), ("ALPHA-RESOURCE-MIB", "controllerInfoName"), ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"), ("ALPHA-NOTIFICATION-MIB", "alarmAdditionalInformation"))
if mibBuilder.loadTexts: alphaAlarmActiveState.setStatus('current')
if mibBuilder.loadTexts: alphaAlarmActiveState.setDescription('                    \t    \n\tSNMPv2 notification varbinds start with SysUptime\n\tand Notification Oid as the first two in the list\n\tby default. The first varbind in this definition\n\twould be the third varbind in the raw output of the\n\tnotification.\n\t\n\tAn instance of the alarm indicated by\n\talarmActiveModelPointer has been raised\n\tagainst the entity indicated by\n\talarmActiveResourceId.\n\t                         \n\tThe state of the alarm is indicated by the \n\talarmModelState.\n\n\tThe description of the alarm along with its source \n\tis indicated by the alarmModelDescription and \n\tcomponentListStaticName respectively.   \n\t\n\tcomponentListSnmpId provides the Id set to the \n\tsource of the alarm.\n\t                         \n\tThe agent must throttle the generation of\n\tconsecutive alarmActiveState traps so that there is at\n\tleast a two-second gap between traps of this\n\ttype against the same alarmActiveModelPointer and\n\talarmActiveResourceId.  When traps are throttled,\n\tthey are queued for sending at a future time.\n\t\n\tA management application should periodically check\n\tthe value of alarmActiveLastChanged to detect any\n\tmissed alarmActiveState notification-events, e.g.,\n\tdue to throttling or transmission loss.\n\t')
alphaAlarmClearState = NotificationType((1, 3, 6, 1, 4, 1, 7309, 100, 2)).setObjects(("ALARM-MIB", "alarmActiveModelPointer"), ("ALARM-MIB", "alarmActiveResourceId"), ("ALPHA-NOTIFICATION-MIB", "alarmPriority"), ("ALARM-MIB", "alarmModelDescription"), ("ALPHA-RESOURCE-MIB", "componentListStaticName"), ("ALPHA-RESOURCE-MIB", "componentListReference"), ("ALPHA-NOTIFICATION-MIB", "alarmSeverity"), ("ALPHA-RESOURCE-MIB", "controllerInfoName"), ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"), ("ALPHA-NOTIFICATION-MIB", "alarmAdditionalInformation"))
if mibBuilder.loadTexts: alphaAlarmClearState.setStatus('current')
if mibBuilder.loadTexts: alphaAlarmClearState.setDescription('             \n\tSNMPv2 notification varbinds start with SysUptime\n\tand Notification Oid as the first two in the list\n\tby default. The first varbind in this definition\n\twould be the third varbind in the raw output of the\n\tnotification.\t\n\t\n\tAn instance of the alarm indicated by\n\talarmActiveModelPointer has been cleared against\n\tthe entity indicated by alarmActiveResourceId.\n\n\tThe state of the alarm is indicated by the \n\talarmModelState.\n\n\tThe description of the alarm along with its source \n\tis indicated by the alarmModelDescription and \n\tcomponentListStaticName respectively.   \n\t\t\n\tcomponentListSnmpId provides the Id set to the \n\tsource of the alarm.\n\n\tThe agent must throttle the generation of\n\tconsecutive alarmActiveClear traps so that there is at\n\tleast a two-second gap between traps of this\n\ttype against the same alarmActiveModelPointer and\n\talarmActiveResourceId.  When traps are throttled,\n\tthey are queued for sending at a future time.\n\t\n\tA management application should periodically check\n\tthe value of alarmActiveLastChanged to detect any\n\tmissed alarmClearState notification-events, e.g.,\n\tdue to throttling or transmission loss.\n\t')
alarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 7309, 101, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSeverity.setStatus('current')
if mibBuilder.loadTexts: alarmSeverity.setDescription('\n\t\tUser defined value used for filtering purposes.\n\t\t')
alarmCustomDescription = MibScalar((1, 3, 6, 1, 4, 1, 7309, 101, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmCustomDescription.setStatus('current')
if mibBuilder.loadTexts: alarmCustomDescription.setDescription('\n\t\tUser defined value used for filtering purposes.\n\t\t')
alarmPriority = MibScalar((1, 3, 6, 1, 4, 1, 7309, 101, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPriority.setStatus('current')
if mibBuilder.loadTexts: alarmPriority.setDescription('\n\t\tUser defined value used for filtering purposes.\n\t\t')
alarmAdditionalInformation = MibScalar((1, 3, 6, 1, 4, 1, 7309, 101, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmAdditionalInformation.setStatus('current')
if mibBuilder.loadTexts: alarmAdditionalInformation.setDescription('\n\t\tAdditional information about the alarm. Each piece of information is separated by 2 colons ::. The following are currently provided\n\t\t- Physical location, in the format bay-shelf-slot-channel (used by LP Module alarms)\n\t\t- What alert is producing this alarm (used by LP Module alarms)\n\t\t')
alphaAlarmNotificationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 100, 102))
alphaAlarmNotificationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1))
alphaAlarmNotificationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 1)).setObjects(("ALPHA-NOTIFICATION-MIB", "alphaParameterGroup"), ("ALPHA-NOTIFICATION-MIB", "alphaNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaAlarmNotificationCompliance = alphaAlarmNotificationCompliance.setStatus('current')
if mibBuilder.loadTexts: alphaAlarmNotificationCompliance.setDescription('The compliance statement for systems supporting\n\t          the alpha MIB.')
alphaAlarmNotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2))
alphaParameterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2, 1)).setObjects(("ALPHA-NOTIFICATION-MIB", "alarmSeverity"), ("ALPHA-NOTIFICATION-MIB", "alarmCustomDescription"), ("ALPHA-NOTIFICATION-MIB", "alarmPriority"), ("ALPHA-NOTIFICATION-MIB", "alarmAdditionalInformation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaParameterGroup = alphaParameterGroup.setStatus('current')
if mibBuilder.loadTexts: alphaParameterGroup.setDescription('Active alpha list group.')
alphaNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7309, 100, 102, 1, 2, 2)).setObjects(("ALPHA-NOTIFICATION-MIB", "alphaAlarmActiveState"), ("ALPHA-NOTIFICATION-MIB", "alphaAlarmClearState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alphaNotificationsGroup = alphaNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: alphaNotificationsGroup.setDescription('The collection of notifications that can be used to\n\t           model alarms for faults lacking pre-existing\n\t           notification definitions.')
mibBuilder.exportSymbols("ALPHA-NOTIFICATION-MIB", alphaNotificationsGroup=alphaNotificationsGroup, alphaAlarmNotificationsExtension=alphaAlarmNotificationsExtension, alphaAlarmActiveState=alphaAlarmActiveState, alarmCustomDescription=alarmCustomDescription, alphaAlarmNotificationConformance=alphaAlarmNotificationConformance, PYSNMP_MODULE_ID=alphaAlarmNotifications, alphaAlarmClearState=alphaAlarmClearState, alphaAlarmNotificationGroups=alphaAlarmNotificationGroups, alarmPriority=alarmPriority, alarmAdditionalInformation=alarmAdditionalInformation, alphaAlarmNotifications=alphaAlarmNotifications, alphaParameterGroup=alphaParameterGroup, alarmSeverity=alarmSeverity, alphaAlarmNotificationCompliances=alphaAlarmNotificationCompliances, alphaAlarmNotificationCompliance=alphaAlarmNotificationCompliance)
