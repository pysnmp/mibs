#
# PySNMP MIB module BLUECOAT-SG-HEALTHMONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-HEALTHMONITOR-MIB
# Produced by pysmi-1.1.8 at Thu Oct 12 09:02:33 2023
# On host fv-az245-3 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Unsigned32, iso, NotificationType, Integer32, TimeTicks, Gauge32, Counter32, Bits, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "iso", "NotificationType", "Integer32", "TimeTicks", "Gauge32", "Counter32", "Bits", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bluecoatSGHealthMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 12))
bluecoatSGHealthMonMIB.setRevisions(('2013-06-10 03:00', '2007-11-05 03:00',))
if mibBuilder.loadTexts: bluecoatSGHealthMonMIB.setLastUpdated('201306100300Z')
if mibBuilder.loadTexts: bluecoatSGHealthMonMIB.setOrganization('Blue Coat Systems, Inc.')
deviceHealthMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 1))
deviceHealthMonMIBNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 2))
deviceHealthMonMIBNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0))
deviceHealthMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3))
class HealthMonMessageString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

deviceHealthMonValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 1, 1))
deviceHealthMonMessage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 12, 1, 1, 1), HealthMonMessageString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthMonMessage.setStatus('current')
class HealthMonStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ok", 1), ("warning", 2), ("critical", 3), ("unknown", 4))

deviceHealthMonStatus = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 12, 1, 1, 2), HealthMonStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthMonStatus.setStatus('current')
deviceHealthMonOkTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0, 1)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage"))
if mibBuilder.loadTexts: deviceHealthMonOkTrap.setStatus('current')
deviceHealthMonWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0, 2)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage"))
if mibBuilder.loadTexts: deviceHealthMonWarningTrap.setStatus('current')
deviceHealthMonCriticalTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 12, 2, 0, 3)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage"))
if mibBuilder.loadTexts: deviceHealthMonCriticalTrap.setStatus('current')
deviceHealthMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 1))
deviceHealthMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 2))
deviceHealthMonMIBNotifGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 3))
deviceHealthMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 1, 1)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthMonMIBCompliance = deviceHealthMonMIBCompliance.setStatus('current')
deviceHealthMonMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 2, 1)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonStatus"), ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthMonMIBGroup = deviceHealthMonMIBGroup.setStatus('current')
deviceHealthMonMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3417, 2, 12, 3, 3, 1)).setObjects(("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonOkTrap"), ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonWarningTrap"), ("BLUECOAT-SG-HEALTHMONITOR-MIB", "deviceHealthMonCriticalTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthMonMIBNotifGroup = deviceHealthMonMIBNotifGroup.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-HEALTHMONITOR-MIB", HealthMonMessageString=HealthMonMessageString, deviceHealthMonMIBCompliance=deviceHealthMonMIBCompliance, deviceHealthMonMIBGroups=deviceHealthMonMIBGroups, deviceHealthMonWarningTrap=deviceHealthMonWarningTrap, deviceHealthMonCriticalTrap=deviceHealthMonCriticalTrap, deviceHealthMonMessage=deviceHealthMonMessage, PYSNMP_MODULE_ID=bluecoatSGHealthMonMIB, deviceHealthMonValues=deviceHealthMonValues, deviceHealthMonOkTrap=deviceHealthMonOkTrap, HealthMonStatus=HealthMonStatus, deviceHealthMonMIBObjects=deviceHealthMonMIBObjects, deviceHealthMonMIBCompliances=deviceHealthMonMIBCompliances, deviceHealthMonStatus=deviceHealthMonStatus, deviceHealthMonMIBNotifPrefix=deviceHealthMonMIBNotifPrefix, deviceHealthMonMIBNotifGroups=deviceHealthMonMIBNotifGroups, deviceHealthMonMIBConformance=deviceHealthMonMIBConformance, bluecoatSGHealthMonMIB=bluecoatSGHealthMonMIB, deviceHealthMonMIBNotification=deviceHealthMonMIBNotification, deviceHealthMonMIBGroup=deviceHealthMonMIBGroup, deviceHealthMonMIBNotifGroup=deviceHealthMonMIBNotifGroup)
