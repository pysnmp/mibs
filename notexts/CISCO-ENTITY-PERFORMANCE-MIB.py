#
# PySNMP MIB module CISCO-ENTITY-PERFORMANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-PERFORMANCE-MIB
# Source digest sha256:5afb08d4eebc86475c7102008bce41e9f2b72b5dbce76b574e42db5a0288a118
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DateAndTime, DisplayString, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "TimeStamp", "TruthValue")
ciscoEntityPerformanceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 756))
ciscoEntityPerformanceMIB.setRevisions(('2014-06-18 00:00', '2010-09-09 00:00',))
if mibBuilder.loadTexts: ciscoEntityPerformanceMIB.setLastUpdated('2014-06-18 00:00')
if mibBuilder.loadTexts: ciscoEntityPerformanceMIB.setOrganization('Cisco Systems, Inc.')
class CiscoEntPerfMeasurement(TextualConvention, Counter64):
    status = 'current'

class CiscoEntPerfRange(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rangePercentage", 1), ("rangeInt32", 2), ("rangeInt64", 3))

class CiscoEntPerfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("utilization", 1), ("bitInputRate", 2), ("bitOutputRate", 3), ("bitDropRate", 4), ("packetInputRate", 5), ("packetOutputRate", 6), ("packetDropRate", 7))

class CiscoEntPerfInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("current", 1), ("oneMinute", 2), ("fiveMinutes", 3), ("fifteenMinutes", 4))

class CiscoEntPerfHistInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("oneMinute", 1), ("fiveMinutes", 2), ("fifteenMinutes", 3))

class CiscoEntPerfIntervalAlgo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("current", 3), ("algoSMA", 4))

ciscoEntityPerformanceMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 0))
ciscoEntityPerformanceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 1))
ciscoEntityPerformanceMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 2))
cepEntityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cepEntityTable.setStatus('current')
cepEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cepEntityEntry.setStatus('current')
cepEntityNumReloads = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1, 1, 1), Counter32()).setUnits('reloads').setMaxAccess("readonly")
if mibBuilder.loadTexts: cepEntityNumReloads.setStatus('current')
cepEntityLastReloadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepEntityLastReloadTime.setStatus('current')
cepConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cepConfigTable.setStatus('current')
cepConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigInterval"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfType"))
if mibBuilder.loadTexts: cepConfigEntry.setStatus('current')
cepConfigInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 1), CiscoEntPerfInterval()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cepConfigInterval.setStatus('current')
cepConfigPerfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 2), CiscoEntPerfType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cepConfigPerfType.setStatus('current')
cepConfigPerfRange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 3), CiscoEntPerfRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepConfigPerfRange.setStatus('current')
cepConfigRisingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 4), CiscoEntPerfMeasurement()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepConfigRisingThreshold.setStatus('current')
cepConfigFallingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 5), CiscoEntPerfMeasurement()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepConfigFallingThreshold.setStatus('current')
cepConfigThresholdNotifEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepConfigThresholdNotifEnabled.setStatus('current')
cepStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cepStatsTable.setStatus('current')
cepStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigInterval"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfType"))
if mibBuilder.loadTexts: cepStatsEntry.setStatus('current')
cepStatsAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3, 1, 1), CiscoEntPerfIntervalAlgo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepStatsAlgorithm.setStatus('current')
cepStatsMeasurement = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3, 1, 2), CiscoEntPerfMeasurement()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepStatsMeasurement.setStatus('current')
cepEntityIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cepEntityIntervalTable.setStatus('current')
cepEntityIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepHistInterval"))
if mibBuilder.loadTexts: cepEntityIntervalEntry.setStatus('current')
cepHistInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1, 1), CiscoEntPerfHistInterval()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cepHistInterval.setStatus('current')
cepIntervalTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cepIntervalTimeElapsed.setStatus('current')
cepValidIntervalCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepValidIntervalCount.setStatus('current')
cepIntervalStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cepIntervalStatsTable.setStatus('current')
cepIntervalStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepHistInterval"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfType"), (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalNumber"))
if mibBuilder.loadTexts: cepIntervalStatsEntry.setStatus('current')
cepIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cepIntervalNumber.setStatus('current')
cepIntervalStatsValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepIntervalStatsValidData.setStatus('current')
cepIntervalStatsRange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 3), CiscoEntPerfRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepIntervalStatsRange.setStatus('current')
cepIntervalStatsMeasurement = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 4), CiscoEntPerfMeasurement()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepIntervalStatsMeasurement.setStatus('current')
cepIntervalStatsCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepIntervalStatsCreateTime.setStatus('current')
ciscoEntityPerformanceMIBNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 6))
cepThroughputTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cepThroughputTable.setStatus('current')
cepThroughputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cepThroughputEntry.setStatus('current')
cepThroughputLicensedBW = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 1), Counter64()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cepThroughputLicensedBW.setStatus('current')
cepThroughputLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("exceed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cepThroughputLevel.setStatus('current')
cepThroughputInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepThroughputInterval.setStatus('current')
cepThroughputThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(75, 95))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepThroughputThreshold.setStatus('current')
cepThroughputAvgRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 5), Counter64()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cepThroughputAvgRate.setStatus('current')
cepThresholdNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 6, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepThresholdNotifEnabled.setStatus('current')
cepThroughputNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 6, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cepThroughputNotifEnabled.setStatus('current')
cepPerfThreshRisingEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 756, 0, 1)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfRange"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigRisingThreshold"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsMeasurement"))
if mibBuilder.loadTexts: cepPerfThreshRisingEvent.setStatus('current')
cepPerfThreshFallingEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 756, 0, 2)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfRange"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigFallingThreshold"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsMeasurement"))
if mibBuilder.loadTexts: cepPerfThreshFallingEvent.setStatus('current')
cepThroughputNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 756, 0, 3)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLicensedBW"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLevel"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputAvgRate"))
if mibBuilder.loadTexts: cepThroughputNotif.setStatus('current')
ciscoEntityPerformanceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 1))
ciscoEntityPerformanceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2))
ciscoEntityPerformanceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 1, 1)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBEntityGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBConfigGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBNotificationGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBPerfStatsGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBIntervalStatsGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBNotifControlGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBEntityIntervalGroup"), ("CISCO-ENTITY-PERFORMANCE-MIB", "ciscoEntityPerformanceMIBThroughputGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBCompliance = ciscoEntityPerformanceMIBCompliance.setStatus('current')
ciscoEntityPerformanceMIBEntityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 1)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepEntityNumReloads"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepEntityLastReloadTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBEntityGroup = ciscoEntityPerformanceMIBEntityGroup.setStatus('current')
ciscoEntityPerformanceMIBConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 2)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigRisingThreshold"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigFallingThreshold"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfRange"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigThresholdNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBConfigGroup = ciscoEntityPerformanceMIBConfigGroup.setStatus('current')
ciscoEntityPerformanceMIBPerfStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 3)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsAlgorithm"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsMeasurement"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBPerfStatsGroup = ciscoEntityPerformanceMIBPerfStatsGroup.setStatus('current')
ciscoEntityPerformanceMIBEntityIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 4)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalTimeElapsed"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepValidIntervalCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBEntityIntervalGroup = ciscoEntityPerformanceMIBEntityIntervalGroup.setStatus('current')
ciscoEntityPerformanceMIBIntervalStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 5)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsValidData"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsMeasurement"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsCreateTime"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsRange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBIntervalStatsGroup = ciscoEntityPerformanceMIBIntervalStatsGroup.setStatus('current')
ciscoEntityPerformanceMIBNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 6)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepThresholdNotifEnabled"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBNotifControlGroup = ciscoEntityPerformanceMIBNotifControlGroup.setStatus('current')
ciscoEntityPerformanceMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 7)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepPerfThreshRisingEvent"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepPerfThreshFallingEvent"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBNotificationGroup = ciscoEntityPerformanceMIBNotificationGroup.setStatus('current')
ciscoEntityPerformanceMIBThroughputGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 8)).setObjects(("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLicensedBW"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLevel"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputInterval"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputThreshold"), ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputAvgRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityPerformanceMIBThroughputGroup = ciscoEntityPerformanceMIBThroughputGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-PERFORMANCE-MIB", CiscoEntPerfHistInterval=CiscoEntPerfHistInterval, CiscoEntPerfInterval=CiscoEntPerfInterval, CiscoEntPerfIntervalAlgo=CiscoEntPerfIntervalAlgo, CiscoEntPerfMeasurement=CiscoEntPerfMeasurement, CiscoEntPerfRange=CiscoEntPerfRange, CiscoEntPerfType=CiscoEntPerfType, PYSNMP_MODULE_ID=ciscoEntityPerformanceMIB, cepConfigEntry=cepConfigEntry, cepConfigFallingThreshold=cepConfigFallingThreshold, cepConfigInterval=cepConfigInterval, cepConfigPerfRange=cepConfigPerfRange, cepConfigPerfType=cepConfigPerfType, cepConfigRisingThreshold=cepConfigRisingThreshold, cepConfigTable=cepConfigTable, cepConfigThresholdNotifEnabled=cepConfigThresholdNotifEnabled, cepEntityEntry=cepEntityEntry, cepEntityIntervalEntry=cepEntityIntervalEntry, cepEntityIntervalTable=cepEntityIntervalTable, cepEntityLastReloadTime=cepEntityLastReloadTime, cepEntityNumReloads=cepEntityNumReloads, cepEntityTable=cepEntityTable, cepHistInterval=cepHistInterval, cepIntervalNumber=cepIntervalNumber, cepIntervalStatsCreateTime=cepIntervalStatsCreateTime, cepIntervalStatsEntry=cepIntervalStatsEntry, cepIntervalStatsMeasurement=cepIntervalStatsMeasurement, cepIntervalStatsRange=cepIntervalStatsRange, cepIntervalStatsTable=cepIntervalStatsTable, cepIntervalStatsValidData=cepIntervalStatsValidData, cepIntervalTimeElapsed=cepIntervalTimeElapsed, cepPerfThreshFallingEvent=cepPerfThreshFallingEvent, cepPerfThreshRisingEvent=cepPerfThreshRisingEvent, cepStatsAlgorithm=cepStatsAlgorithm, cepStatsEntry=cepStatsEntry, cepStatsMeasurement=cepStatsMeasurement, cepStatsTable=cepStatsTable, cepThresholdNotifEnabled=cepThresholdNotifEnabled, cepThroughputAvgRate=cepThroughputAvgRate, cepThroughputEntry=cepThroughputEntry, cepThroughputInterval=cepThroughputInterval, cepThroughputLevel=cepThroughputLevel, cepThroughputLicensedBW=cepThroughputLicensedBW, cepThroughputNotif=cepThroughputNotif, cepThroughputNotifEnabled=cepThroughputNotifEnabled, cepThroughputTable=cepThroughputTable, cepThroughputThreshold=cepThroughputThreshold, cepValidIntervalCount=cepValidIntervalCount, ciscoEntityPerformanceMIB=ciscoEntityPerformanceMIB, ciscoEntityPerformanceMIBCompliance=ciscoEntityPerformanceMIBCompliance, ciscoEntityPerformanceMIBCompliances=ciscoEntityPerformanceMIBCompliances, ciscoEntityPerformanceMIBConfigGroup=ciscoEntityPerformanceMIBConfigGroup, ciscoEntityPerformanceMIBConform=ciscoEntityPerformanceMIBConform, ciscoEntityPerformanceMIBEntityGroup=ciscoEntityPerformanceMIBEntityGroup, ciscoEntityPerformanceMIBEntityIntervalGroup=ciscoEntityPerformanceMIBEntityIntervalGroup, ciscoEntityPerformanceMIBGroups=ciscoEntityPerformanceMIBGroups, ciscoEntityPerformanceMIBIntervalStatsGroup=ciscoEntityPerformanceMIBIntervalStatsGroup, ciscoEntityPerformanceMIBNotifControlGroup=ciscoEntityPerformanceMIBNotifControlGroup, ciscoEntityPerformanceMIBNotifObjects=ciscoEntityPerformanceMIBNotifObjects, ciscoEntityPerformanceMIBNotificationGroup=ciscoEntityPerformanceMIBNotificationGroup, ciscoEntityPerformanceMIBNotifs=ciscoEntityPerformanceMIBNotifs, ciscoEntityPerformanceMIBObjects=ciscoEntityPerformanceMIBObjects, ciscoEntityPerformanceMIBPerfStatsGroup=ciscoEntityPerformanceMIBPerfStatsGroup, ciscoEntityPerformanceMIBThroughputGroup=ciscoEntityPerformanceMIBThroughputGroup)
