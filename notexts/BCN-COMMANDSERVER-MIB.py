#
# PySNMP MIB module BCN-COMMANDSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-COMMANDSERVER-MIB
# Produced by pysmi-1.1.3 at Tue Nov 30 13:51:57 2021
# On host fv-az77-605 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Gauge32, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, Counter32, Integer32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "Counter32", "Integer32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
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
mibBuilder.exportSymbols("BCN-COMMANDSERVER-MIB", bcnCommandServerAlarmNotif=bcnCommandServerAlarmNotif, bcnCommandServerConformance=bcnCommandServerConformance, bcnCommandServerObjects=bcnCommandServerObjects, bcnCommandServerServiceStatus=bcnCommandServerServiceStatus, bcnCommandServerServiceGroups=bcnCommandServerServiceGroups, bcnCommandServerMIB=bcnCommandServerMIB, bcnCommandServerNotificationEventGroup=bcnCommandServerNotificationEventGroup, bcnCommandServerNotificationDataGroup=bcnCommandServerNotificationDataGroup, bcnCommandServerNotificationData=bcnCommandServerNotificationData, bcnCommandServerNotification=bcnCommandServerNotification, bcnCommandServerServiceCompliances=bcnCommandServerServiceCompliances, bcnCommandServerAlarmInfo=bcnCommandServerAlarmInfo, bcnCommandServer=bcnCommandServer, bcnCommandServerAlarmSeverity=bcnCommandServerAlarmSeverity, bcnCommandServerSerOperState=bcnCommandServerSerOperState, bcnCommandServerNotificationEvents=bcnCommandServerNotificationEvents, bcnCommandServerStatusCompliance=bcnCommandServerStatusCompliance, PYSNMP_MODULE_ID=bcnCommandServerMIB, bcnCommandServerServiceStatusGroup=bcnCommandServerServiceStatusGroup)
