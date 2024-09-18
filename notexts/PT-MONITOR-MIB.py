#
# PySNMP MIB module PT-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-MONITOR-MIB
# Produced by pysmi-1.1.12 at Wed Sep 18 06:45:19 2024
# On host fv-az1780-151 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
pt, = mibBuilder.importSymbols("PT-MIB", "pt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, iso, IpAddress, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter64, Integer32, ObjectIdentity, Counter32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "IpAddress", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter64", "Integer32", "ObjectIdentity", "Counter32", "Bits", "ModuleIdentity")
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
mibBuilder.exportSymbols("PT-MONITOR-MIB", PYSNMP_MODULE_ID=ptMonitor, hwIndex=hwIndex, ptMonitorConformance=ptMonitorConformance, hwDiagnosticsEntry=hwDiagnosticsEntry, HealthStatusTC=HealthStatusTC, temperatureStatus=temperatureStatus, healthStatus=healthStatus, ptMonitor=ptMonitor, ptMonitorFullCompliance=ptMonitorFullCompliance, ptMonitorGroups=ptMonitorGroups, ptMonitorCompleteGroup=ptMonitorCompleteGroup, ptMonitorCompliances=ptMonitorCompliances, hwDiagnosticsTable=hwDiagnosticsTable)
