#
# PySNMP MIB module BCN-COMMANDSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-COMMANDSERVER-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:18:38 2024
# On host fv-az1789-327 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, iso, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Bits, IpAddress, Gauge32, NotificationType, Integer32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Bits", "IpAddress", "Gauge32", "NotificationType", "Integer32", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BCN-COMMANDSERVER-MIB", bcnCommandServerServiceStatus=bcnCommandServerServiceStatus, bcnCommandServerConformance=bcnCommandServerConformance, bcnCommandServerAlarmSeverity=bcnCommandServerAlarmSeverity, bcnCommandServerNotificationData=bcnCommandServerNotificationData, bcnCommandServerObjects=bcnCommandServerObjects, bcnCommandServerNotificationEvents=bcnCommandServerNotificationEvents, bcnCommandServerNotificationDataGroup=bcnCommandServerNotificationDataGroup, bcnCommandServerServiceGroups=bcnCommandServerServiceGroups, bcnCommandServerServiceCompliances=bcnCommandServerServiceCompliances, bcnCommandServerAlarmInfo=bcnCommandServerAlarmInfo, bcnCommandServerNotificationEventGroup=bcnCommandServerNotificationEventGroup, bcnCommandServerAlarmNotif=bcnCommandServerAlarmNotif, bcnCommandServerStatusCompliance=bcnCommandServerStatusCompliance, bcnCommandServerServiceStatusGroup=bcnCommandServerServiceStatusGroup, bcnCommandServerMIB=bcnCommandServerMIB, bcnCommandServerSerOperState=bcnCommandServerSerOperState, PYSNMP_MODULE_ID=bcnCommandServerMIB, bcnCommandServer=bcnCommandServer, bcnCommandServerNotification=bcnCommandServerNotification)
