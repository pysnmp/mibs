#
# PySNMP MIB module BCN-COMMANDSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-COMMANDSERVER-MIB
# Produced by pysmi-1.1.12 at Wed May 29 06:42:13 2024
# On host fv-az1019-850 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, ObjectIdentity, NotificationType, Unsigned32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, ModuleIdentity, Integer32, iso, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "NotificationType", "Unsigned32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "ModuleIdentity", "Integer32", "iso", "Gauge32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcnCommandServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 1))
bcnCommandServerMIB.setRevisions(('2011-06-30 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcnCommandServerMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bcnCommandServerMIB.setLastUpdated('201106301200Z')
if mibBuilder.loadTexts: bcnCommandServerMIB.setOrganization('BlueCat Networks')
if mibBuilder.loadTexts: bcnCommandServerMIB.setContactInfo('BlueCat Networks. Customer Care.\n\n        North America\n        Call: +1.866.491.2228\n        Europe\n        Call: +44.8081.011.306\n        Other\n        Call: +1.416.646.8433\n        \n        Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bcnCommandServerMIB.setDescription('This module provides status as well as statistical information\n        about the COMMANDSERVER service.')
bcnCommandServer = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7))
bcnCommandServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 2))
bcnCommandServerNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3))
bcnCommandServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4))
bcnCommandServerServiceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 2, 1))
if mibBuilder.loadTexts: bcnCommandServerServiceStatus.setStatus('current')
if mibBuilder.loadTexts: bcnCommandServerServiceStatus.setDescription('General state of the COMMANDSERVER Service.')
bcnCommandServerSerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("running", 1), ("notRunning", 2), ("starting", 3), ("stopping", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnCommandServerSerOperState.setStatus('current')
if mibBuilder.loadTexts: bcnCommandServerSerOperState.setDescription('Operational state of the Service. The possible states are:\n        running(1)    The service is running normally.\n        notRunning(2) The service is stopped either intentionally (i.e.:\n                      the service is not supposed to run on this node) or\n                      unintentionally (a problem has occurred).\n        starting(3)   The service is in the process of starting, either\n                      for the first time of after an event occurred.\n        stopping(4)   The service is in the process of stopping. Stopping\n                      a service might be necessary after a configuration\n                      change.\n        fault(5)      An error has been detected and the state is undefined.\n        ')
bcnCommandServerNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 0))
bcnCommandServerNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 1))
bcnCommandServerAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnCommandServerAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: bcnCommandServerAlarmSeverity.setDescription('Severity classification for the alarm.')
bcnCommandServerAlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnCommandServerAlarmInfo.setStatus('current')
if mibBuilder.loadTexts: bcnCommandServerAlarmInfo.setDescription('Descriptive information about the alarm event.')
bcnCommandServerAlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 0, 1)).setObjects(("BCN-COMMANDSERVER-MIB", "bcnCommandServerSerOperState"), ("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmSeverity"), ("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmInfo"))
if mibBuilder.loadTexts: bcnCommandServerAlarmNotif.setStatus('current')
if mibBuilder.loadTexts: bcnCommandServerAlarmNotif.setDescription('A bcnCommandServerAlarmNotif signifies that the COMMANDSERVER service has transitioned\n        state or a particular event has been detected on the service.')
bcnCommandServerServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 1))
bcnCommandServerServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2))
bcnCommandServerServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2, 1)).setObjects(("BCN-COMMANDSERVER-MIB", "bcnCommandServerSerOperState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnCommandServerServiceStatusGroup = bcnCommandServerServiceStatusGroup.setStatus('current')
if mibBuilder.loadTexts: bcnCommandServerServiceStatusGroup.setDescription('Status conformance.')
bcnCommandServerNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2, 2)).setObjects(("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnCommandServerNotificationEventGroup = bcnCommandServerNotificationEventGroup.setStatus('current')
if mibBuilder.loadTexts: bcnCommandServerNotificationEventGroup.setDescription('Server statistics conformance.')
bcnCommandServerNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2, 3)).setObjects(("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmSeverity"), ("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnCommandServerNotificationDataGroup = bcnCommandServerNotificationDataGroup.setStatus('current')
if mibBuilder.loadTexts: bcnCommandServerNotificationDataGroup.setDescription('Server statistics conformance.')
bcnCommandServerStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 1, 1)).setObjects(("BCN-COMMANDSERVER-MIB", "bcnCommandServerServiceStatusGroup"), ("BCN-COMMANDSERVER-MIB", "bcnCommandServerNotificationEventGroup"), ("BCN-COMMANDSERVER-MIB", "bcnCommandServerNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnCommandServerStatusCompliance = bcnCommandServerStatusCompliance.setStatus('current')
if mibBuilder.loadTexts: bcnCommandServerStatusCompliance.setDescription('Basic conformance')
mibBuilder.exportSymbols("BCN-COMMANDSERVER-MIB", bcnCommandServerNotification=bcnCommandServerNotification, bcnCommandServerStatusCompliance=bcnCommandServerStatusCompliance, bcnCommandServerNotificationData=bcnCommandServerNotificationData, bcnCommandServer=bcnCommandServer, bcnCommandServerAlarmSeverity=bcnCommandServerAlarmSeverity, bcnCommandServerAlarmNotif=bcnCommandServerAlarmNotif, bcnCommandServerMIB=bcnCommandServerMIB, bcnCommandServerServiceStatus=bcnCommandServerServiceStatus, bcnCommandServerServiceGroups=bcnCommandServerServiceGroups, bcnCommandServerServiceCompliances=bcnCommandServerServiceCompliances, bcnCommandServerAlarmInfo=bcnCommandServerAlarmInfo, bcnCommandServerNotificationEventGroup=bcnCommandServerNotificationEventGroup, bcnCommandServerServiceStatusGroup=bcnCommandServerServiceStatusGroup, bcnCommandServerSerOperState=bcnCommandServerSerOperState, PYSNMP_MODULE_ID=bcnCommandServerMIB, bcnCommandServerConformance=bcnCommandServerConformance, bcnCommandServerObjects=bcnCommandServerObjects, bcnCommandServerNotificationEvents=bcnCommandServerNotificationEvents, bcnCommandServerNotificationDataGroup=bcnCommandServerNotificationDataGroup)
