#
# PySNMP MIB module BLUECOAT-SG-HEALTHCHECK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-HEALTHCHECK-MIB
# Produced by pysmi-1.1.8 at Thu Dec 15 08:19:47 2022
# On host fv-az193-683 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, iso, Unsigned32, MibIdentifier, ModuleIdentity, IpAddress, NotificationType, Integer32, TimeTicks, Gauge32, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "iso", "Unsigned32", "MibIdentifier", "ModuleIdentity", "IpAddress", "NotificationType", "Integer32", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
deviceHealthCheckMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 7))
deviceHealthCheckMIB.setRevisions(('2013-05-22 03:00', '2013-05-21 03:00', '2007-11-05 03:00', '2002-08-28 03:00',))
if mibBuilder.loadTexts: deviceHealthCheckMIB.setLastUpdated('201305220300Z')
if mibBuilder.loadTexts: deviceHealthCheckMIB.setOrganization('Blue Coat Systems, Inc.')
deviceHealthCheckMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1))
deviceHealthCheckMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 2))
deviceHealthCheckMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3))
deviceHealthCheckMIBNotifsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 2, 0))
class HealthCheckMessageString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

deviceHealthCheckStringValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 1))
deviceHealthCheckValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2))
deviceHealthCheckMessage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 1, 1), HealthCheckMessageString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthCheckMessage.setStatus('current')
deviceHealthCheckValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1), )
if mibBuilder.loadTexts: deviceHealthCheckValueTable.setStatus('current')
deviceHealthCheckValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckName"))
if mibBuilder.loadTexts: deviceHealthCheckValueEntry.setStatus('current')
class HealthCheckStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("ok", 2), ("okWithErrors", 3), ("okForSomeIPs", 4), ("okButFailing", 5), ("checkFailed", 6), ("dnsFailed", 7), ("okOnAltServer", 8))

deviceHealthCheckName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthCheckName.setStatus('current')
deviceHealthCheckState = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1, 2), HealthCheckStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthCheckState.setStatus('current')
deviceHealthCheckTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthCheckTime.setStatus('current')
deviceHealthCheckTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 7, 2, 0, 1)).setObjects(("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckMessage"))
if mibBuilder.loadTexts: deviceHealthCheckTrap.setStatus('current')
deviceHealthCheckMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 1))
deviceHealthCheckMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 2))
deviceHealthCheckMIBNotifGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 3))
deviceHealthCheckMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 1, 1)).setObjects(("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthCheckMIBCompliance = deviceHealthCheckMIBCompliance.setStatus('current')
deviceHealthCheckMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 2, 1)).setObjects(("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckName"), ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckState"), ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckTime"), ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthCheckMIBGroup = deviceHealthCheckMIBGroup.setStatus('current')
deviceHealthCheckMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 3, 1)).setObjects(("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthCheckMIBNotifGroup = deviceHealthCheckMIBNotifGroup.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-HEALTHCHECK-MIB", deviceHealthCheckMIB=deviceHealthCheckMIB, deviceHealthCheckMIBNotifs=deviceHealthCheckMIBNotifs, deviceHealthCheckMIBNotifsPrefix=deviceHealthCheckMIBNotifsPrefix, deviceHealthCheckValueEntry=deviceHealthCheckValueEntry, deviceHealthCheckTrap=deviceHealthCheckTrap, deviceHealthCheckTime=deviceHealthCheckTime, deviceHealthCheckValueTable=deviceHealthCheckValueTable, deviceHealthCheckValues=deviceHealthCheckValues, PYSNMP_MODULE_ID=deviceHealthCheckMIB, deviceHealthCheckMIBNotifGroups=deviceHealthCheckMIBNotifGroups, HealthCheckMessageString=HealthCheckMessageString, deviceHealthCheckState=deviceHealthCheckState, deviceHealthCheckMIBCompliance=deviceHealthCheckMIBCompliance, deviceHealthCheckMIBConformance=deviceHealthCheckMIBConformance, deviceHealthCheckName=deviceHealthCheckName, deviceHealthCheckMIBGroups=deviceHealthCheckMIBGroups, HealthCheckStatus=HealthCheckStatus, deviceHealthCheckMIBGroup=deviceHealthCheckMIBGroup, deviceHealthCheckMIBObjects=deviceHealthCheckMIBObjects, deviceHealthCheckStringValues=deviceHealthCheckStringValues, deviceHealthCheckMIBCompliances=deviceHealthCheckMIBCompliances, deviceHealthCheckMessage=deviceHealthCheckMessage, deviceHealthCheckMIBNotifGroup=deviceHealthCheckMIBNotifGroup)
