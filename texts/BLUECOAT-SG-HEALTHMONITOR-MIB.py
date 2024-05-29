#
# PySNMP MIB module BLUECOAT-SG-HEALTHMONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-HEALTHMONITOR-MIB
# Produced by pysmi-1.1.12 at Wed May 29 06:43:17 2024
# On host fv-az1776-875 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Counter64, NotificationType, TimeTicks, Unsigned32, ModuleIdentity, ObjectIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "NotificationType", "TimeTicks", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bluecoatSGHealthMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 12))
bluecoatSGHealthMonMIB.setRevisions(('2013-06-10 03:00', '2007-11-05 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bluecoatSGHealthMonMIB.setRevisionsDescriptions(("1. Introduced individual traps for states.\n                         2. The overall health monitoring state is made pollable.\n                         3. Renamed 'bluecoatSgHealthMonitor' prefix as 'deviceHealthMon'.\n                         4. Added comformance and compliance statements.", 'Initial revision of this MIB.',))
if mibBuilder.loadTexts: bluecoatSGHealthMonMIB.setLastUpdated('201306100300Z')
if mibBuilder.loadTexts: bluecoatSGHealthMonMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: bluecoatSGHealthMonMIB.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: bluecoatSGHealthMonMIB.setDescription('The health monitoring MIB is used to monitor\n                         changes in the health of the SG appliance.')
deviceHealthMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 1))
deviceHealthMonMIBNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 2))
deviceHealthMonMIBNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0))
deviceHealthMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3))
class HealthMonMessageString(TextualConvention, OctetString):
    description = 'The message describing a change in the health\n                          of the SG system.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

deviceHealthMonValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 1, 1))
deviceHealthMonMessage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 12, 1, 1, 1), HealthMonMessageString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthMonMessage.setStatus('current')
if mibBuilder.loadTexts: deviceHealthMonMessage.setDescription('The custom message generated for this change in health.')
class HealthMonStatus(TextualConvention, Integer32):
    description = 'Indicates the current state of the health monitor.\n                (1) - ok\n                (2) - warning\n                (3) - critical\n                (4) - unknown'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ok", 1), ("warning", 2), ("critical", 3), ("unknown", 4))

deviceHealthMonStatus = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 12, 1, 1, 2), HealthMonStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthMonStatus.setStatus('current')
if mibBuilder.loadTexts: deviceHealthMonStatus.setDescription('This shows the current state of health monitor.')
deviceHealthMonOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0, 1)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage"))
if mibBuilder.loadTexts: deviceHealthMonOkTrap.setStatus('current')
if mibBuilder.loadTexts: deviceHealthMonOkTrap.setDescription('This notifies that the health monitor status changed to OK.')
deviceHealthMonWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0, 2)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage"))
if mibBuilder.loadTexts: deviceHealthMonWarningTrap.setStatus('current')
if mibBuilder.loadTexts: deviceHealthMonWarningTrap.setDescription('This notifies that the health monitor status changed to Warning.')
deviceHealthMonCriticalTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0, 3)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage"))
if mibBuilder.loadTexts: deviceHealthMonCriticalTrap.setStatus('current')
if mibBuilder.loadTexts: deviceHealthMonCriticalTrap.setDescription('This notifies that the health monitor status changed to Critical.')
deviceHealthMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 1))
deviceHealthMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 2))
deviceHealthMonMIBNotifGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 3))
deviceHealthMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 1, 1)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthMonMIBCompliance = deviceHealthMonMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: deviceHealthMonMIBCompliance.setDescription('The compliance statement for the health monitoring module. ')
deviceHealthMonMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 2, 1)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonStatus"), ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthMonMIBGroup = deviceHealthMonMIBGroup.setStatus('current')
if mibBuilder.loadTexts: deviceHealthMonMIBGroup.setDescription('Group of Health Monitoring-related objects implemented in ProxySG appliances.')
deviceHealthMonMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 3, 1)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonOkTrap"), ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonWarningTrap"), ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonCriticalTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthMonMIBNotifGroup = deviceHealthMonMIBNotifGroup.setStatus('current')
if mibBuilder.loadTexts: deviceHealthMonMIBNotifGroup.setDescription('Group of Health Monitoring notifications implemented in ProxySG appliances.')
mibBuilder.exportSymbols("BLUECOAT-SG-HEALTHMONITOR-MIB", deviceHealthMonOkTrap=deviceHealthMonOkTrap, deviceHealthMonMIBNotification=deviceHealthMonMIBNotification, deviceHealthMonMIBCompliances=deviceHealthMonMIBCompliances, HealthMonStatus=HealthMonStatus, deviceHealthMonMIBConformance=deviceHealthMonMIBConformance, deviceHealthMonMessage=deviceHealthMonMessage, deviceHealthMonWarningTrap=deviceHealthMonWarningTrap, deviceHealthMonMIBNotifPrefix=deviceHealthMonMIBNotifPrefix, deviceHealthMonValues=deviceHealthMonValues, deviceHealthMonMIBCompliance=deviceHealthMonMIBCompliance, bluecoatSGHealthMonMIB=bluecoatSGHealthMonMIB, deviceHealthMonStatus=deviceHealthMonStatus, PYSNMP_MODULE_ID=bluecoatSGHealthMonMIB, deviceHealthMonCriticalTrap=deviceHealthMonCriticalTrap, deviceHealthMonMIBGroup=deviceHealthMonMIBGroup, HealthMonMessageString=HealthMonMessageString, deviceHealthMonMIBObjects=deviceHealthMonMIBObjects, deviceHealthMonMIBNotifGroup=deviceHealthMonMIBNotifGroup, deviceHealthMonMIBGroups=deviceHealthMonMIBGroups, deviceHealthMonMIBNotifGroups=deviceHealthMonMIBNotifGroups)
