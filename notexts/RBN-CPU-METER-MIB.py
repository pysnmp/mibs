#
# PySNMP MIB module RBN-CPU-METER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/RBN-CPU-METER-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 14:33:50 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnPercentage, = mibBuilder.importSymbols("RBN-TC", "RbnPercentage")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, Gauge32, Bits, Integer32, MibIdentifier, Counter64, Counter32, iso, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Bits", "Integer32", "MibIdentifier", "Counter64", "Counter32", "iso", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnCpuMeterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 6))
rbnCpuMeterMIB.setRevisions(('2011-12-13 18:00', '2011-01-19 18:00', '2002-12-16 00:00', '2002-06-26 00:00', '2002-05-29 00:00', '1999-06-16 23:00',))
if mibBuilder.loadTexts: rbnCpuMeterMIB.setLastUpdated('201112131800Z')
if mibBuilder.loadTexts: rbnCpuMeterMIB.setOrganization('Ericsson AB.')
rbnCpuMeterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1))
rbnCpuMeterMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2))
rbnCpuProcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3))
class Percentage(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

rbnCpuMeterFiveSecondAvg = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 1), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterFiveSecondAvg.setStatus('current')
rbnCpuMeterOneMinuteAvg = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 2), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterOneMinuteAvg.setStatus('current')
rbnCpuMeterFiveMinuteAvg = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 3), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterFiveMinuteAvg.setStatus('current')
rbnCpuMeterFiveSecondPeak = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 4), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterFiveSecondPeak.setStatus('current')
rbnCpuMeterOneMinutePeak = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 5), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterOneMinutePeak.setStatus('current')
rbnCpuMeterFiveMinutePeak = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 6), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuMeterFiveMinutePeak.setStatus('current')
rbnCpuProcTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1), )
if mibBuilder.loadTexts: rbnCpuProcTable.setStatus('current')
rbnCpuProcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1), ).setIndexNames((1, "RBN-CPU-METER-MIB", "rbnCpuProcName"))
if mibBuilder.loadTexts: rbnCpuProcEntry.setStatus('current')
rbnCpuProcName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 114))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProcName.setStatus('current')
rbnCpuProcPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProcPriority.setStatus('current')
rbnCpuProcTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProcTime.setStatus('current')
rbnCpuProcCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProcCalls.setStatus('current')
rbnCpuProc5Sec = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 5), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProc5Sec.setStatus('current')
rbnCpuProc1Min = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 6), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProc1Min.setStatus('current')
rbnCpuProc5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 7), RbnPercentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProc5Min.setStatus('current')
rbnCpuProcLongest = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuProcLongest.setStatus('current')
rbnCpuMeterMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 1))
rbnCpuMeterMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2))
rbnCpuProcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 3))
rbnCpuMeterMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2, 1)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuMeterStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterMIBCompliance = rbnCpuMeterMIBCompliance.setStatus('deprecated')
rbnCpuMeterMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2, 2)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuMeterStatsGroup"), ("RBN-CPU-METER-MIB", "rbnCpuProcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterMIBCompliance1 = rbnCpuMeterMIBCompliance1.setStatus('deprecated')
rbnCpuMeterMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2, 3)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuMeterStatsGroup2"), ("RBN-CPU-METER-MIB", "rbnCpuProcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterMIBCompliance2 = rbnCpuMeterMIBCompliance2.setStatus('current')
rbnCpuMeterStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 1, 1)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuMeterFiveSecondAvg"), ("RBN-CPU-METER-MIB", "rbnCpuMeterOneMinuteAvg"), ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveMinuteAvg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterStatsGroup = rbnCpuMeterStatsGroup.setStatus('deprecated')
rbnCpuProcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 3, 1)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuProcName"), ("RBN-CPU-METER-MIB", "rbnCpuProcPriority"), ("RBN-CPU-METER-MIB", "rbnCpuProcTime"), ("RBN-CPU-METER-MIB", "rbnCpuProcCalls"), ("RBN-CPU-METER-MIB", "rbnCpuProc5Sec"), ("RBN-CPU-METER-MIB", "rbnCpuProc1Min"), ("RBN-CPU-METER-MIB", "rbnCpuProc5Min"), ("RBN-CPU-METER-MIB", "rbnCpuProcLongest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuProcGroup = rbnCpuProcGroup.setStatus('current')
rbnCpuMeterStatsGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 1, 2)).setObjects(("RBN-CPU-METER-MIB", "rbnCpuMeterFiveSecondAvg"), ("RBN-CPU-METER-MIB", "rbnCpuMeterOneMinuteAvg"), ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveMinuteAvg"), ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveSecondPeak"), ("RBN-CPU-METER-MIB", "rbnCpuMeterOneMinutePeak"), ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveMinutePeak"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnCpuMeterStatsGroup2 = rbnCpuMeterStatsGroup2.setStatus('current')
mibBuilder.exportSymbols("RBN-CPU-METER-MIB", rbnCpuMeterMIBCompliances=rbnCpuMeterMIBCompliances, Percentage=Percentage, rbnCpuMeterMIBCompliance=rbnCpuMeterMIBCompliance, rbnCpuMeterFiveMinuteAvg=rbnCpuMeterFiveMinuteAvg, rbnCpuMeterMIBConformance=rbnCpuMeterMIBConformance, rbnCpuProc5Sec=rbnCpuProc5Sec, rbnCpuProcPriority=rbnCpuProcPriority, rbnCpuProc1Min=rbnCpuProc1Min, rbnCpuProcName=rbnCpuProcName, rbnCpuProcCalls=rbnCpuProcCalls, rbnCpuMeterMIBObjects=rbnCpuMeterMIBObjects, rbnCpuMeterOneMinuteAvg=rbnCpuMeterOneMinuteAvg, rbnCpuMeterOneMinutePeak=rbnCpuMeterOneMinutePeak, rbnCpuProcTime=rbnCpuProcTime, rbnCpuMeterMIBGroups=rbnCpuMeterMIBGroups, rbnCpuMeterMIB=rbnCpuMeterMIB, PYSNMP_MODULE_ID=rbnCpuMeterMIB, rbnCpuMeterFiveMinutePeak=rbnCpuMeterFiveMinutePeak, rbnCpuProc5Min=rbnCpuProc5Min, rbnCpuProcLongest=rbnCpuProcLongest, rbnCpuMeterStatsGroup=rbnCpuMeterStatsGroup, rbnCpuProcMIBObjects=rbnCpuProcMIBObjects, rbnCpuMeterFiveSecondPeak=rbnCpuMeterFiveSecondPeak, rbnCpuMeterStatsGroup2=rbnCpuMeterStatsGroup2, rbnCpuMeterMIBCompliance1=rbnCpuMeterMIBCompliance1, rbnCpuProcEntry=rbnCpuProcEntry, rbnCpuProcTable=rbnCpuProcTable, rbnCpuProcGroup=rbnCpuProcGroup, rbnCpuMeterFiveSecondAvg=rbnCpuMeterFiveSecondAvg, rbnCpuProcGroups=rbnCpuProcGroups, rbnCpuMeterMIBCompliance2=rbnCpuMeterMIBCompliance2)
