#
# PySNMP MIB module PT-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-MONITOR-MIB
# Produced by pysmi-1.1.12 at Wed Sep 18 06:45:22 2024
# On host fv-az1780-151 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
pt, = mibBuilder.importSymbols("PT-MIB", "pt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ObjectIdentity, Unsigned32, Bits, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Integer32, ModuleIdentity, IpAddress, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Integer32", "ModuleIdentity", "IpAddress", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ptMonitor = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2, 4))
ptMonitor.setRevisions(('2016-03-09 12:30', '2016-02-10 12:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ptMonitor.setRevisionsDescriptions(('Validated.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: ptMonitor.setLastUpdated('201603091230Z')
if mibBuilder.loadTexts: ptMonitor.setOrganization('Ericsson')
if mibBuilder.loadTexts: ptMonitor.setContactInfo('Anders Ekvall\n             Postal: Ericsson AB,\n             E-Mail: anders.ekvall@ericsson.com')
if mibBuilder.loadTexts: ptMonitor.setDescription('This is the MIB of PT specifics')
ptMonitorConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2))
class HealthStatusTC(TextualConvention, Integer32):
    description = 'hw status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("eOK", 1), ("eNOTOK", 2), ("eUNKNOWN", 3))

hwDiagnosticsTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1), )
if mibBuilder.loadTexts: hwDiagnosticsTable.setStatus('current')
if mibBuilder.loadTexts: hwDiagnosticsTable.setDescription('A list of interface entries.  The number of entries is\n            given by the value of ExampleNumber.')
hwDiagnosticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1), ).setIndexNames((0, "PT-MONITOR-MIB", "hwIndex"))
if mibBuilder.loadTexts: hwDiagnosticsEntry.setStatus('current')
if mibBuilder.loadTexts: hwDiagnosticsEntry.setDescription('An entry containing management information applicable to a\n            particular interface.')
hwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hwIndex.setStatus('current')
if mibBuilder.loadTexts: hwIndex.setDescription('a unique index for hw that we diagnose, here it is the slotId')
temperatureStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureStatus.setStatus('current')
if mibBuilder.loadTexts: temperatureStatus.setDescription('The temperature in degree Celsius.')
healthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 1, 1, 3), HealthStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: healthStatus.setStatus('current')
if mibBuilder.loadTexts: healthStatus.setDescription('This is the hw running status, it has the following value:\n\t     eOK       (1),\n\t     eNOT_OK   (2),\n\t     eUNKNOWN  (3)            \n            ')
ptMonitorCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 1))
ptMonitorGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 2))
ptMonitorFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 1, 1)).setObjects(("PT-MONITOR-MIB", "ptMonitorCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptMonitorFullCompliance = ptMonitorFullCompliance.setStatus('current')
if mibBuilder.loadTexts: ptMonitorFullCompliance.setDescription('The compliance statement for SNMP entities which implement everything.')
ptMonitorCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 4, 2, 2, 1)).setObjects(("PT-MONITOR-MIB", "temperatureStatus"), ("PT-MONITOR-MIB", "healthStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptMonitorCompleteGroup = ptMonitorCompleteGroup.setStatus('current')
if mibBuilder.loadTexts: ptMonitorCompleteGroup.setDescription('A collection of all current objects in this MIB module.')
mibBuilder.exportSymbols("PT-MONITOR-MIB", ptMonitorGroups=ptMonitorGroups, hwDiagnosticsEntry=hwDiagnosticsEntry, healthStatus=healthStatus, hwDiagnosticsTable=hwDiagnosticsTable, hwIndex=hwIndex, ptMonitorCompliances=ptMonitorCompliances, HealthStatusTC=HealthStatusTC, ptMonitorFullCompliance=ptMonitorFullCompliance, PYSNMP_MODULE_ID=ptMonitor, temperatureStatus=temperatureStatus, ptMonitorConformance=ptMonitorConformance, ptMonitorCompleteGroup=ptMonitorCompleteGroup, ptMonitor=ptMonitor)
