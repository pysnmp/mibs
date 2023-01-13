#
# PySNMP MIB module BLUECOAT-SG-USAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-USAGE-MIB
# Produced by pysmi-1.1.8 at Fri Jan 13 11:59:03 2023
# On host fv-az218-3 platform Linux version 5.15.0-1030-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, IpAddress, NotificationType, Integer32, Unsigned32, ModuleIdentity, iso, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "IpAddress", "NotificationType", "Integer32", "Unsigned32", "ModuleIdentity", "iso", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "TimeTicks")
TextualConvention, TimeStamp, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "TruthValue", "DisplayString")
deviceUsageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 4))
deviceUsageMIB.setRevisions(('2013-07-11 03:00', '2008-01-16 03:00', '2007-12-07 03:00', '2002-11-06 03:00',))
if mibBuilder.loadTexts: deviceUsageMIB.setLastUpdated('201307110300Z')
if mibBuilder.loadTexts: deviceUsageMIB.setOrganization('Blue Coat Systems, Inc.')
deviceUsageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1))
deviceUsageMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 4, 2))
deviceUsageMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 4, 2, 0))
class Percent(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd%'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class UsageStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("high", 2))

deviceUsageTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1), )
if mibBuilder.loadTexts: deviceUsageTable.setStatus('current')
deviceUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-USAGE-MIB", "deviceUsageIndex"))
if mibBuilder.loadTexts: deviceUsageEntry.setStatus('current')
deviceUsageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceUsageIndex.setStatus('current')
deviceUsageTrapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageTrapEnabled.setStatus('current')
deviceUsageName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageName.setStatus('current')
deviceUsagePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 4), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsagePercent.setStatus('current')
deviceUsageHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 5), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageHigh.setStatus('current')
deviceUsageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 6), UsageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageStatus.setStatus('current')
deviceUsageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 7), TimeStamp()).setUnits('Hundredths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageTime.setStatus('current')
deviceUsageTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 4, 2, 0, 1)).setObjects(("BLUECOAT-SG-USAGE-MIB", "deviceUsageName"), ("BLUECOAT-SG-USAGE-MIB", "deviceUsagePercent"), ("BLUECOAT-SG-USAGE-MIB", "deviceUsageStatus"))
if mibBuilder.loadTexts: deviceUsageTrap.setStatus('deprecated')
mibBuilder.exportSymbols("BLUECOAT-SG-USAGE-MIB", deviceUsageIndex=deviceUsageIndex, deviceUsageHigh=deviceUsageHigh, deviceUsageTable=deviceUsageTable, deviceUsageMIBNotifications=deviceUsageMIBNotifications, deviceUsageMIBObjects=deviceUsageMIBObjects, PYSNMP_MODULE_ID=deviceUsageMIB, deviceUsageStatus=deviceUsageStatus, deviceUsageTime=deviceUsageTime, deviceUsageName=deviceUsageName, UsageStatus=UsageStatus, deviceUsageTrapEnabled=deviceUsageTrapEnabled, deviceUsageMIBNotificationsPrefix=deviceUsageMIBNotificationsPrefix, deviceUsageEntry=deviceUsageEntry, Percent=Percent, deviceUsageMIB=deviceUsageMIB, deviceUsageTrap=deviceUsageTrap, deviceUsagePercent=deviceUsagePercent)
