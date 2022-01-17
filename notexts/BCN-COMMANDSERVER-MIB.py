#
# PySNMP MIB module BCN-COMMANDSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-COMMANDSERVER-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 21:38:00 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, NotificationType, iso, Counter32, ObjectIdentity, Gauge32, MibIdentifier, TimeTicks, Counter64, Integer32, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "NotificationType", "iso", "Counter32", "ObjectIdentity", "Gauge32", "MibIdentifier", "TimeTicks", "Counter64", "Integer32", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("BCN-COMMANDSERVER-MIB", bcnCommandServerNotificationDataGroup=bcnCommandServerNotificationDataGroup, bcnCommandServerStatusCompliance=bcnCommandServerStatusCompliance, bcnCommandServer=bcnCommandServer, bcnCommandServerServiceStatus=bcnCommandServerServiceStatus, bcnCommandServerAlarmNotif=bcnCommandServerAlarmNotif, bcnCommandServerNotificationEventGroup=bcnCommandServerNotificationEventGroup, PYSNMP_MODULE_ID=bcnCommandServerMIB, bcnCommandServerAlarmSeverity=bcnCommandServerAlarmSeverity, bcnCommandServerNotification=bcnCommandServerNotification, bcnCommandServerObjects=bcnCommandServerObjects, bcnCommandServerNotificationEvents=bcnCommandServerNotificationEvents, bcnCommandServerNotificationData=bcnCommandServerNotificationData, bcnCommandServerMIB=bcnCommandServerMIB, bcnCommandServerAlarmInfo=bcnCommandServerAlarmInfo, bcnCommandServerServiceCompliances=bcnCommandServerServiceCompliances, bcnCommandServerSerOperState=bcnCommandServerSerOperState, bcnCommandServerConformance=bcnCommandServerConformance, bcnCommandServerServiceGroups=bcnCommandServerServiceGroups, bcnCommandServerServiceStatusGroup=bcnCommandServerServiceStatusGroup)
