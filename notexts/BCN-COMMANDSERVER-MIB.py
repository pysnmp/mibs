#
# PySNMP MIB module BCN-COMMANDSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-COMMANDSERVER-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 08:50:36 2024
# On host fv-az2028-26 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, MibIdentifier, Integer32, ObjectIdentity, Gauge32, ModuleIdentity, Bits, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Integer32", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Bits", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "IpAddress", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bcnCommandServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 1))
bcnCommandServerMIB.setRevisions(('2011-06-30 12:00',))
if mibBuilder.loadTexts: bcnCommandServerMIB.setLastUpdated('201106301200Z')
if mibBuilder.loadTexts: bcnCommandServerMIB.setOrganization('BlueCat Networks')
bcnCommandServer = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7))
bcnCommandServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 2))
bcnCommandServerNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3))
bcnCommandServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4))
bcnCommandServerServiceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 2, 1))
if mibBuilder.loadTexts: bcnCommandServerServiceStatus.setStatus('current')
bcnCommandServerSerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("running", 1), ("notRunning", 2), ("starting", 3), ("stopping", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnCommandServerSerOperState.setStatus('current')
bcnCommandServerNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 0))
bcnCommandServerNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 1))
bcnCommandServerAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnCommandServerAlarmSeverity.setStatus('current')
bcnCommandServerAlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnCommandServerAlarmInfo.setStatus('current')
bcnCommandServerAlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 0, 1)).setObjects(("BCN-COMMANDSERVER-MIB", "bcnCommandServerSerOperState"), ("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmSeverity"), ("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmInfo"))
if mibBuilder.loadTexts: bcnCommandServerAlarmNotif.setStatus('current')
bcnCommandServerServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 1))
bcnCommandServerServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2))
bcnCommandServerServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2, 1)).setObjects(("BCN-COMMANDSERVER-MIB", "bcnCommandServerSerOperState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnCommandServerServiceStatusGroup = bcnCommandServerServiceStatusGroup.setStatus('current')
bcnCommandServerNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2, 2)).setObjects(("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnCommandServerNotificationEventGroup = bcnCommandServerNotificationEventGroup.setStatus('current')
bcnCommandServerNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2, 3)).setObjects(("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmSeverity"), ("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnCommandServerNotificationDataGroup = bcnCommandServerNotificationDataGroup.setStatus('current')
bcnCommandServerStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 1, 1)).setObjects(("BCN-COMMANDSERVER-MIB", "bcnCommandServerServiceStatusGroup"), ("BCN-COMMANDSERVER-MIB", "bcnCommandServerNotificationEventGroup"), ("BCN-COMMANDSERVER-MIB", "bcnCommandServerNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnCommandServerStatusCompliance = bcnCommandServerStatusCompliance.setStatus('current')
mibBuilder.exportSymbols("BCN-COMMANDSERVER-MIB", bcnCommandServerNotificationEvents=bcnCommandServerNotificationEvents, PYSNMP_MODULE_ID=bcnCommandServerMIB, bcnCommandServerObjects=bcnCommandServerObjects, bcnCommandServerNotificationDataGroup=bcnCommandServerNotificationDataGroup, bcnCommandServerSerOperState=bcnCommandServerSerOperState, bcnCommandServerAlarmInfo=bcnCommandServerAlarmInfo, bcnCommandServerServiceStatusGroup=bcnCommandServerServiceStatusGroup, bcnCommandServerNotificationData=bcnCommandServerNotificationData, bcnCommandServerMIB=bcnCommandServerMIB, bcnCommandServerNotification=bcnCommandServerNotification, bcnCommandServerAlarmSeverity=bcnCommandServerAlarmSeverity, bcnCommandServerConformance=bcnCommandServerConformance, bcnCommandServerAlarmNotif=bcnCommandServerAlarmNotif, bcnCommandServerNotificationEventGroup=bcnCommandServerNotificationEventGroup, bcnCommandServerServiceCompliances=bcnCommandServerServiceCompliances, bcnCommandServer=bcnCommandServer, bcnCommandServerServiceGroups=bcnCommandServerServiceGroups, bcnCommandServerServiceStatus=bcnCommandServerServiceStatus, bcnCommandServerStatusCompliance=bcnCommandServerStatusCompliance)
