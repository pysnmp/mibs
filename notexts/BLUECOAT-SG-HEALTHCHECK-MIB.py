#
# PySNMP MIB module BLUECOAT-SG-HEALTHCHECK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-HEALTHCHECK-MIB
# Produced by pysmi-1.1.8 at Thu Feb  9 13:53:30 2023
# On host fv-az565-495 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, IpAddress, ModuleIdentity, TimeTicks, Counter64, Gauge32, Integer32, MibIdentifier, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "IpAddress", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "Integer32", "MibIdentifier", "Unsigned32", "NotificationType")
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
mibBuilder.exportSymbols("BLUECOAT-SG-HEALTHCHECK-MIB", deviceHealthCheckMIBCompliances=deviceHealthCheckMIBCompliances, deviceHealthCheckMIB=deviceHealthCheckMIB, deviceHealthCheckMIBNotifsPrefix=deviceHealthCheckMIBNotifsPrefix, deviceHealthCheckMIBGroups=deviceHealthCheckMIBGroups, deviceHealthCheckMIBNotifGroups=deviceHealthCheckMIBNotifGroups, deviceHealthCheckName=deviceHealthCheckName, deviceHealthCheckTime=deviceHealthCheckTime, deviceHealthCheckStringValues=deviceHealthCheckStringValues, deviceHealthCheckMIBCompliance=deviceHealthCheckMIBCompliance, deviceHealthCheckMIBNotifGroup=deviceHealthCheckMIBNotifGroup, deviceHealthCheckValues=deviceHealthCheckValues, HealthCheckMessageString=HealthCheckMessageString, deviceHealthCheckValueTable=deviceHealthCheckValueTable, HealthCheckStatus=HealthCheckStatus, deviceHealthCheckMIBObjects=deviceHealthCheckMIBObjects, deviceHealthCheckMessage=deviceHealthCheckMessage, deviceHealthCheckValueEntry=deviceHealthCheckValueEntry, deviceHealthCheckTrap=deviceHealthCheckTrap, deviceHealthCheckState=deviceHealthCheckState, deviceHealthCheckMIBNotifs=deviceHealthCheckMIBNotifs, deviceHealthCheckMIBGroup=deviceHealthCheckMIBGroup, PYSNMP_MODULE_ID=deviceHealthCheckMIB, deviceHealthCheckMIBConformance=deviceHealthCheckMIBConformance)
