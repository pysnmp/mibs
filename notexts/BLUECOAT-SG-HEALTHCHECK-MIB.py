#
# PySNMP MIB module BLUECOAT-SG-HEALTHCHECK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-HEALTHCHECK-MIB
# Produced by pysmi-1.1.8 at Wed Oct 11 08:25:25 2023
# On host fv-az791-264 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, TimeTicks, ModuleIdentity, Gauge32, iso, Counter64, MibIdentifier, NotificationType, ObjectIdentity, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "ModuleIdentity", "Gauge32", "iso", "Counter64", "MibIdentifier", "NotificationType", "ObjectIdentity", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32")
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
mibBuilder.exportSymbols("BLUECOAT-SG-HEALTHCHECK-MIB", HealthCheckMessageString=HealthCheckMessageString, deviceHealthCheckStringValues=deviceHealthCheckStringValues, deviceHealthCheckMIBNotifGroup=deviceHealthCheckMIBNotifGroup, deviceHealthCheckValueTable=deviceHealthCheckValueTable, deviceHealthCheckMIBCompliances=deviceHealthCheckMIBCompliances, deviceHealthCheckMIBCompliance=deviceHealthCheckMIBCompliance, deviceHealthCheckMIBGroups=deviceHealthCheckMIBGroups, deviceHealthCheckMIBGroup=deviceHealthCheckMIBGroup, deviceHealthCheckValueEntry=deviceHealthCheckValueEntry, deviceHealthCheckMIBObjects=deviceHealthCheckMIBObjects, deviceHealthCheckMIB=deviceHealthCheckMIB, deviceHealthCheckTime=deviceHealthCheckTime, deviceHealthCheckMIBConformance=deviceHealthCheckMIBConformance, HealthCheckStatus=HealthCheckStatus, deviceHealthCheckMIBNotifGroups=deviceHealthCheckMIBNotifGroups, deviceHealthCheckMIBNotifsPrefix=deviceHealthCheckMIBNotifsPrefix, PYSNMP_MODULE_ID=deviceHealthCheckMIB, deviceHealthCheckTrap=deviceHealthCheckTrap, deviceHealthCheckValues=deviceHealthCheckValues, deviceHealthCheckMessage=deviceHealthCheckMessage, deviceHealthCheckMIBNotifs=deviceHealthCheckMIBNotifs, deviceHealthCheckName=deviceHealthCheckName, deviceHealthCheckState=deviceHealthCheckState)
