#
# PySNMP MIB module PT-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-MONITOR-MIB
# Produced by pysmi-1.1.12 at Tue May 28 12:34:24 2024
# On host fv-az768-311 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
pt, = mibBuilder.importSymbols("PT-MIB", "pt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, NotificationType, Bits, ObjectIdentity, Gauge32, MibIdentifier, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "NotificationType", "Bits", "ObjectIdentity", "Gauge32", "MibIdentifier", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ptMonitor = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2, 4))
ptMonitor.setRevisions(('2016-03-09 12:30', '2016-02-10 12:30',))
if mibBuilder.loadTexts: ptMonitor.setLastUpdated('201603091230Z')
if mibBuilder.loadTexts: ptMonitor.setOrganization('Ericsson')
ptMonitorConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2))
class HealthStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("eOK", 1), ("eNOTOK", 2), ("eUNKNOWN", 3))

hwDiagnosticsTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1), )
if mibBuilder.loadTexts: hwDiagnosticsTable.setStatus('current')
hwDiagnosticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1), ).setIndexNames((0, "PT-MONITOR-MIB", "hwIndex"))
if mibBuilder.loadTexts: hwDiagnosticsEntry.setStatus('current')
hwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hwIndex.setStatus('current')
temperatureStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureStatus.setStatus('current')
healthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1, 3), HealthStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: healthStatus.setStatus('current')
ptMonitorCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 1))
ptMonitorGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 2))
ptMonitorFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 1, 1)).setObjects(("PT-MONITOR-MIB", "ptMonitorCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptMonitorFullCompliance = ptMonitorFullCompliance.setStatus('current')
ptMonitorCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 2, 1)).setObjects(("PT-MONITOR-MIB", "temperatureStatus"), ("PT-MONITOR-MIB", "healthStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptMonitorCompleteGroup = ptMonitorCompleteGroup.setStatus('current')
mibBuilder.exportSymbols("PT-MONITOR-MIB", hwDiagnosticsEntry=hwDiagnosticsEntry, ptMonitorGroups=ptMonitorGroups, ptMonitorConformance=ptMonitorConformance, PYSNMP_MODULE_ID=ptMonitor, ptMonitor=ptMonitor, healthStatus=healthStatus, hwIndex=hwIndex, ptMonitorCompleteGroup=ptMonitorCompleteGroup, hwDiagnosticsTable=hwDiagnosticsTable, temperatureStatus=temperatureStatus, HealthStatusTC=HealthStatusTC, ptMonitorFullCompliance=ptMonitorFullCompliance, ptMonitorCompliances=ptMonitorCompliances)
