#
# PySNMP MIB module DATA-DOMAIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/datadomain/DATA-DOMAIN-MIB
# Produced by pysmi-1.1.8 at Mon Feb  6 14:28:03 2023
# On host fv-az216-339 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, NotificationType, Counter32, enterprises, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, IpAddress, Counter64, iso, Bits, MibIdentifier, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Counter32", "enterprises", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "IpAddress", "Counter64", "iso", "Bits", "MibIdentifier", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dataDomainMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 19746))
dataDomainMib.setRevisions(('2017-05-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dataDomainMib.setRevisionsDescriptions(('Updated mib on 16 may, 2017. Please refer to Release Guide for list of changes.',))
if mibBuilder.loadTexts: dataDomainMib.setLastUpdated('201705160000Z')
if mibBuilder.loadTexts: dataDomainMib.setOrganization('Data Domain, Inc')
if mibBuilder.loadTexts: dataDomainMib.setContactInfo('Phone: +1-408-980-4800 \n\t     Fax:   +1-408-980-8620')
if mibBuilder.loadTexts: dataDomainMib.setDescription('This MIB is used for managing the suite of Data Domain Products.')
dataDomainMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 0))
dataDomainMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1))
dataDomainMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 2))
dataDomainMibProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3))
dataDomainMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 0, 2))
environmentals = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1))
nvram = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2))
fileSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3))
alerts = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 4))
statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 5))
diskStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6))
replication = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8))
nfs = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 9))
cifs = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 10))
vtl = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11))
ddboost = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12))
dataDomainSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13))
art = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 14))
mtree = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 15))
storage = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 16))
enclosure = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 17))
network = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 18))
ddms = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 19))
smt = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20))
quota = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 21))
highAvailability = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 22))
scsitarget = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23))
class EnclosureID(TextualConvention, Integer32):
    description = 'unique Enclosure ID, used as index in several tables'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Temperature(TextualConvention, Integer32):
    description = 'Temperature value in Celsius'
    status = 'current'
    displayHint = 'd'

class Minutes(TextualConvention, Integer32):
    description = 'Minutes'
    status = 'current'
    displayHint = 'd'

class Percentage(TextualConvention, Integer32):
    description = 'Percentage'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class PercentageStr(TextualConvention, OctetString):
    description = 'Percentage string'
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class KBytesPerSecond(TextualConvention, Counter32):
    description = 'Number of KBytes transferred per second'
    status = 'current'
    displayHint = 'd'

class OpsPerSecond(TextualConvention, Counter32):
    description = 'Number of Operations performed per second'
    status = 'current'
    displayHint = 'd'

class ErrorCount(TextualConvention, Counter32):
    description = 'Number of Errors Encountered'
    status = 'current'
    displayHint = 'd'

class DDMibTableIndexTC(TextualConvention, Integer32):
    description = 'Index for Any Data Domain MIB table'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DDMibTableString32TC(TextualConvention, OctetString):
    description = 'DD Mib Table String 32'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class DDMibTableString64TC(TextualConvention, OctetString):
    description = 'DD Mib Table String 64'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DDMibTableString128TC(TextualConvention, OctetString):
    description = 'DD Mib Table String 128'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class DDMibTableString256TC(TextualConvention, OctetString):
    description = 'DD Mib Table String 256'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class DDMibTableString512TC(TextualConvention, OctetString):
    description = 'DD Mib Table String 512'
    status = 'current'
    displayHint = '512a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 512)

class DDMibTableString1024TC(TextualConvention, OctetString):
    description = 'DD Mib Table String 1024'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class DDMibString96TC(TextualConvention, OctetString):
    description = 'DD Mib String 96'
    status = 'current'
    displayHint = '96a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 96)

class DDMibTableSizeGibTC(TextualConvention, OctetString):
    description = 'Data Domain Compression size in GiB'
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class DDMibTableSizeMiBTC(TextualConvention, OctetString):
    description = 'Data Domain size in MiB'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class DDMibDateTC(TextualConvention, OctetString):
    description = 'Data Domain Mib Date in the yyyy-mm-dd hh:mm format'
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class DDMibMemorySizeTC(TextualConvention, Integer32):
    description = 'Data Domain Mib Memory Size of  in bytes.'
    status = 'current'
    displayHint = 'd'

class DDMibTimeStampTC(TextualConvention, OctetString):
    description = 'DD Mib Timestamp'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DDMibVersionTC(TextualConvention, OctetString):
    description = 'Data Domain Mib version'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DDMibTableEnabledTC(TextualConvention, Integer32):
    description = 'DD Mib Table  Enabled'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class DDMibInteger32TC(TextualConvention, Integer32):
    description = 'Data Domain Mib Integer 32.'
    status = 'current'
    displayHint = 'd'

class DDMibCompressionFactorTC(TextualConvention, OctetString):
    description = 'Data Domain compression factor'
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class DDMibAlertSeverityTC(TextualConvention, OctetString):
    description = 'Data Domain Alert Severity'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DDMibTrafficBytesTC(TextualConvention, Counter64):
    description = 'measurement of bytes being transferred'
    status = 'current'
    displayHint = 'd'

class DDMibStatusTC(TextualConvention, Integer32):
    description = 'DD Mib Status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class PowerModuleIndexTC(TextualConvention, Integer32):
    description = 'Number of Power Module present in the DDR'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PowerModuleDescriptionTC(TextualConvention, OctetString):
    description = 'Power Module Description'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class PowerModuleStatusTC(TextualConvention, Integer32):
    description = 'Current Power Module Status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 99))
    namedValues = NamedValues(("absent", 0), ("ok", 1), ("failed", 2), ("faulty", 3), ("acnone", 4), ("unknown", 99))

class TempSensorIndexTC(TextualConvention, Integer32):
    description = 'Number of Temperature Sensor present in the DDR'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class TempSensorDescriptionTC(TextualConvention, OctetString):
    description = 'Temperature Sensor Description'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TempSensorStatusTC(TextualConvention, Integer32):
    description = 'Current Temperature Sensor Status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("failed", 0), ("ok", 1), ("notfound", 2), ("overheatWarning", 3), ("overheatCritical", 4))

class FanIndexTC(TextualConvention, Integer32):
    description = 'Fan Number of fan that is present in DDR'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FanDescriptionTC(TextualConvention, OctetString):
    description = 'Fan Description'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class FanLevelTC(TextualConvention, Integer32):
    description = 'Current Fan level'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("low", 1), ("medium", 2), ("high", 3))

class FanStatusTC(TextualConvention, Integer32):
    description = 'Current Fan Status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notfound", 0), ("ok", 1), ("fail", 2))

class NvramIndexTC(TextualConvention, Integer32):
    description = 'Index of NVRAM card present in the DDR'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NvramMemorySizeTC(TextualConvention, Integer32):
    description = 'Memory Size of NVRAM in bytes.'
    status = 'current'
    displayHint = 'd'

class NvramHCPropertyBytesTC(TextualConvention, Counter64):
    description = 'Value of an NVRAM high capacity property in bytes.'
    status = 'current'
    displayHint = 'd'

class NvramWindowSizeTC(TextualConvention, Integer32):
    description = 'Window Size of NVRAM in bytes.'
    status = 'current'
    displayHint = 'd'

class NvramBatteryIndexTC(TextualConvention, Integer32):
    description = 'Number of NVRAM Battery present in the DDR'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NvramBatteryStatusTC(TextualConvention, Integer32):
    description = 'Current NVRAM Battery Status\n                Status      Description\n                --------------------------------\n                ok          charged and enabled\n                discharged  charging and enabled'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ok", 0), ("disabled", 1), ("discharged", 2), ("softdisabled", 3))

class DiskIndexTC(TextualConvention, Integer32):
    description = 'Disk Number of disk that is present in the DDR'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DiskModelTC(TextualConvention, OctetString):
    description = 'Manufacture & Model Number of disk'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DiskFirmwareVersionTC(TextualConvention, OctetString):
    description = 'Firmware version of disk'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DiskSerialNumberTC(TextualConvention, OctetString):
    description = 'Serial Number of disk'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DiskCapacityTC(TextualConvention, OctetString):
    description = 'Capacity of disk'
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class DiskStateTC(TextualConvention, Integer32):
    description = 'Current Disk State'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ok", 1), ("unknown", 2), ("absent", 3), ("failed", 4), ("spare", 5), ("available", 6))

class DiskPackTC(TextualConvention, Integer32):
    description = 'Pack number for disks of ES60.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notapplicable", 0), ("pack1", 1), ("pack2", 2), ("pack3", 3), ("pack4", 4))

class DiskSectorsPerSecondTC(TextualConvention, Counter32):
    description = 'Number of disk sectors being transferred per second'
    status = 'current'
    displayHint = 'd'

class FileSystemStatusTC(TextualConvention, Integer32):
    description = 'Current File System Status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("running", 3), ("unknown", 4), ("error", 5), ("cleaning", 6))

class FileSystemResourceIndexTC(TextualConvention, Integer32):
    description = 'Resource Number of file system resource'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FileSystemResourceNameTC(TextualConvention, OctetString):
    description = 'File System resource name'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class FileSystemSpaceUnitTC(TextualConvention, OctetString):
    description = 'Units of space in the file System represented in Gigabytes'
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class FileSystemCompressionSizeTC(TextualConvention, OctetString):
    description = 'File Systems Compression size in GiB'
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class FileSystemCompressionFactorTC(TextualConvention, OctetString):
    description = 'File System compression factor'
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class FileSystemCompressionPeriodTC(TextualConvention, OctetString):
    description = 'File System compression period: last 24 hours, last 7 days'
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class DateTC(TextualConvention, OctetString):
    description = 'Date in the yyyy-mm-dd hh:mm format'
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class FileSystemOptionsIndexTC(TextualConvention, Integer32):
    description = 'Index of File System Option Table Index'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FileSystemOptionsNameTC(TextualConvention, OctetString):
    description = 'Index of File Systems Option Name '
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class FileSystemOptionsValueTC(TextualConvention, OctetString):
    description = 'Index of File Systems Option Value '
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class FileSystemCleanIndexTC(TextualConvention, Integer32):
    description = 'File System Clean Index'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FileSystemCleanStatusTC(TextualConvention, OctetString):
    description = 'File System Clean Status '
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class FileSystemCleanScheduleTC(TextualConvention, OctetString):
    description = 'File System Clean Schedule '
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class FileSystemCleanThrottleTC(TextualConvention, OctetString):
    description = 'File System Clean throttle'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class AlertIndexTC(TextualConvention, Integer32):
    description = 'Alert Row Index'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AlertTimestampTC(TextualConvention, OctetString):
    description = 'Alert Timestamp'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class AlertDescriptionTC(TextualConvention, OctetString):
    description = 'Alert Description'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SystemStatsIndexTC(TextualConvention, Integer32):
    description = 'Statistics Row Index'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class RaidDiskStateTC(TextualConvention, Integer32):
    description = 'Raid Disk State'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 99))
    namedValues = NamedValues(("inuse", 1), ("notinuse", 2), ("spare", 3), ("absent", 4), ("failed", 5), ("invalid", 6), ("foreign", 7), ("known", 8), ("available", 9), ("unknown", 99))

class ReplicationStateTC(TextualConvention, Integer32):
    description = 'Current Replication status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("initializing", 1), ("normal", 2), ("recovering", 3), ("uninitialized", 4))

class ReplicationStatusTC(TextualConvention, Integer32):
    description = 'Current Replication connection status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("connected", 1), ("disconnected", 2), ("migrating", 3), ("suspended", 4), ("neverConnected", 5), ("idle", 6))

class ReplicationConnectTimeTC(TextualConvention, Integer32):
    description = 'timestamp when connection was established, or 0 if there is no Replication connection'
    status = 'current'
    displayHint = 'd'

class ReplicationPathTC(TextualConvention, OctetString):
    description = 'source or destination path for replication'
    status = 'current'
    displayHint = '254a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 254)

class ReplicationTrafficTC(TextualConvention, Counter64):
    description = 'measurement of bytes being replicated'
    status = 'current'
    displayHint = 'd'

class ReplicationThrottleTC(TextualConvention, Integer32):
    description = 'measurement of replication throttle in bps'
    status = 'current'
    displayHint = 'd'

class ReplicationSyncedTimeTC(TextualConvention, Integer32):
    description = 'timestamp when replication source and destination were in sync, or 0 if unknown'
    status = 'current'
    displayHint = 'd'

class ReplicationContextTC(TextualConvention, Integer32):
    description = '0 for collection replication contexts, > 0 for directory replication contexts'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ReplicationConfigIndexTC(TextualConvention, Integer32):
    description = 'Replication Config Row Index'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ReplicationConfigContextIdTC(TextualConvention, OctetString):
    description = 'Replicaton Configuration Context Id'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class ReplicationConfigSourceTC(TextualConvention, OctetString):
    description = 'Replicaton Configuration Connection Source'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class ReplicationConfigDestTC(TextualConvention, OctetString):
    description = 'Replicaton Configuration Destination'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class ReplicationConfigConnHostTC(TextualConvention, OctetString):
    description = 'Replicaton Configuration Connection Host'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class ReplicationConfigConnPortTC(TextualConvention, OctetString):
    description = 'Replicaton Configuration Connection Port'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class ReplicationConfigLowBWOptimTC(TextualConvention, Integer32):
    description = 'Replication Low BW Optimization Status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class ReplicationConfigEnabledTC(TextualConvention, Integer32):
    description = 'Replication Configuration Enabled'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class NfsStatusTC(TextualConvention, Integer32):
    description = 'Current Network File System Status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class NfsClientIndexTC(TextualConvention, Integer32):
    description = 'Index of NFS clients'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NfsClientPathTC(TextualConvention, OctetString):
    description = 'NFS path'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class NfsClientClientsTC(TextualConvention, OctetString):
    description = 'NFS Clients'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class NfsClientOptionsTC(TextualConvention, OctetString):
    description = 'NFS options'
    status = 'current'
    displayHint = '254a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 254)

class NfsStatsIndexTC(TextualConvention, Integer32):
    description = 'Index of NFS stats'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NfsStatsExportPointTC(TextualConvention, OctetString):
    description = 'NFS export point'
    status = 'current'
    displayHint = '254a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 254)

class NfsStatsFilesystemTypeTC(TextualConvention, OctetString):
    description = 'NFS file system type'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class NfsStatsCacheEntryTC(TextualConvention, Counter32):
    description = 'Number of cache entries'
    status = 'current'
    displayHint = 'd'

class NfsStatsFileHandleLookupTC(TextualConvention, Counter32):
    description = 'Number of file handle lookup'
    status = 'current'
    displayHint = 'd'

class NfsStatsMaxCacheSizeTC(TextualConvention, Counter32):
    description = 'Max cache size'
    status = 'current'
    displayHint = 'd'

class NfsStatsCurrentOpenStreamsTC(TextualConvention, Counter32):
    description = 'Number of current open streams'
    status = 'current'
    displayHint = 'd'

class VtlAdminStateTC(TextualConvention, Integer32):
    description = 'Current VTL administration state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("enabled", 1), ("disabled", 2), ("failed", 3))

class VtlProcessStateTC(TextualConvention, Integer32):
    description = 'Current VTL process state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("stopped", 1), ("starting", 2), ("running", 3), ("timingout", 4), ("stopping", 5), ("stuck", 6))

class VtlLibraryIndexTC(TextualConvention, Integer32):
    description = 'Index of VTL library'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 64)

class VtlLibraryNameTC(TextualConvention, OctetString):
    description = 'VTL library name'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlLibraryVendorTC(TextualConvention, OctetString):
    description = 'VTL library vendor'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlLibraryModelTC(TextualConvention, OctetString):
    description = 'VTL library model'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlLibraryRevisionTC(TextualConvention, OctetString):
    description = 'VTL library revision'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlLibrarySerialTC(TextualConvention, OctetString):
    description = 'VTL library serial'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlLibraryTotalDrivesTC(TextualConvention, Counter32):
    description = 'Number of VTL drives'
    status = 'current'
    displayHint = 'd'

class VtlLibraryTotalSlotsTC(TextualConvention, Counter32):
    description = 'Number of VTL slots'
    status = 'current'
    displayHint = 'd'

class VtlLibraryTotalCapsTC(TextualConvention, Counter32):
    description = 'Number of VTL caps'
    status = 'current'
    displayHint = 'd'

class VtlLibraryStatusTC(TextualConvention, Integer32):
    description = 'Current VTL library status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("online", 1), ("offline", 2))

class VtlDriveIndexTC(TextualConvention, Integer32):
    description = 'Index of VTL drive'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 512)

class VtlDriveNameTC(TextualConvention, OctetString):
    description = 'VTL drive name'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlDriveVendorTC(TextualConvention, OctetString):
    description = 'VTL drive vendor'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlDriveModelTC(TextualConvention, OctetString):
    description = 'VTL drive model'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlDriveRevisionTC(TextualConvention, OctetString):
    description = 'VTL drive revision'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlDriveSerialTC(TextualConvention, OctetString):
    description = 'VTL drive serial'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlDriveStatusTC(TextualConvention, Integer32):
    description = 'Current VTL drive status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("online", 1), ("offline", 2))

class VtlDriveTapeVolumeTC(TextualConvention, OctetString):
    description = 'VTL drive tape volume'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlPortIndexTC(TextualConvention, Integer32):
    description = 'VTL Port Table Index'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10)

class VtlPortNameTC(TextualConvention, OctetString):
    description = 'VTL Port Name '
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlPortIDTC(TextualConvention, Counter32):
    description = 'VTL Port Id'
    status = 'current'
    displayHint = 'd'

class VtlPortModelTC(TextualConvention, OctetString):
    description = 'VTL Port MODEL'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlPortFirmwareTC(TextualConvention, OctetString):
    description = 'VTL Port Firmware'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlPortWWNNTC(TextualConvention, OctetString):
    description = 'VTL WWNN Address'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlPortWWPNTC(TextualConvention, OctetString):
    description = 'VTL WWPN Address'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlPortConnectionTypeTC(TextualConvention, Integer32):
    description = 'VTL Port Connection Type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("nPORT", 0), ("loop", 1), ("pointToPoint", 2), ("fabricLoop", 3), ("unknown", 4))

class VtlPortSpeedTC(TextualConvention, Integer32):
    description = 'VTL Port Speed '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 6))
    namedValues = NamedValues(("zeroGBPS", 0), ("oneGBPS", 1), ("twoGBPS", 2), ("fourGBPS", 3), ("eightGBPS", 4), ("unknown", 6))

class VtlPortEnabledTC(TextualConvention, Integer32):
    description = 'VTL Port Enabled'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1), ("unknown", 2))

class VtlPortStatusTC(TextualConvention, Integer32):
    description = 'VTL Port State'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("offline", 0), ("online", 1), ("unknown", 2))

class VtlTapeIndexTC(TextualConvention, Integer32):
    description = 'VTL Tape Table Index'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 250000)

class VtlTapeBarCodeTC(TextualConvention, OctetString):
    description = 'VTL Tape Bar Code '
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlTapePoolTC(TextualConvention, OctetString):
    description = 'VTL Tape Pool '
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeLocationTC(TextualConvention, OctetString):
    description = 'VTL Tape Location '
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeStateTC(TextualConvention, OctetString):
    description = 'VTL Tape State '
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeSizeTC(TextualConvention, OctetString):
    description = 'VTL Tape Size '
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeUsedTC(TextualConvention, OctetString):
    description = 'VTL Tape Used '
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeCompTC(TextualConvention, OctetString):
    description = 'VTL Tape Compression '
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeModTimeTC(TextualConvention, OctetString):
    description = 'VTL Tape Mod Time '
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlStatsIndexTC(TextualConvention, Integer32):
    description = 'VTL Stats Table Index'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class VtlStatsPortTC(TextualConvention, OctetString):
    description = 'VTL Tape Bar Code '
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlStatsConrolCommandsTC(TextualConvention, Counter64):
    description = 'VTL Stats Table Control Commands'
    status = 'current'
    displayHint = 'd'

class VtlStatsWriteCommandsTC(TextualConvention, Counter64):
    description = 'VTL Stats Table write commands'
    status = 'current'
    displayHint = 'd'

class VtlStatsReadCommandsTC(TextualConvention, Counter64):
    description = 'VTL Stats Table Read Commands'
    status = 'current'
    displayHint = 'd'

class VtlStatsInTC(TextualConvention, Counter64):
    description = 'VTL Stats Table Stats In'
    status = 'current'
    displayHint = 'd'

class VtlStatsOutTC(TextualConvention, Counter64):
    description = 'VTL Stats Table Stats Out'
    status = 'current'
    displayHint = 'd'

class VtlStatsLinkFailuresTC(TextualConvention, Counter64):
    description = 'VTL Stats Table Link failures'
    status = 'current'
    displayHint = 'd'

class VtlStatsLIPCountTC(TextualConvention, Counter64):
    description = 'VTL Stats Table LIP count'
    status = 'current'
    displayHint = 'd'

class VtlStatsSyncLossesTC(TextualConvention, Counter64):
    description = 'VTL Stats Table Sync Losses'
    status = 'current'
    displayHint = 'd'

class VtlStatsSignalLossesTC(TextualConvention, Counter64):
    description = 'VTL Stats Table Signal Losses'
    status = 'current'
    displayHint = 'd'

class VtlStatsPrimSeqProtoErrorsTC(TextualConvention, Counter64):
    description = 'VTL Stats Table Prim Seq Protocol Errors'
    status = 'current'
    displayHint = 'd'

class VtlStatsInvalidTxWordsTC(TextualConvention, Counter64):
    description = 'VTL Stats Table Invalid Tx Words'
    status = 'current'
    displayHint = 'd'

class VtlStatsInvalidCRCsTC(TextualConvention, Counter64):
    description = 'VTL Stats Table Invalid CRCs'
    status = 'current'
    displayHint = 'd'

class CifsStatusTC(TextualConvention, Integer32):
    description = 'Current CIFS status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("enabled", 1), ("enabledRunning", 2), ("enabledNotRunning", 3), ("enabledWindbindNotRun", 4), ("disabled", 5))

class CifsConfigModeTC(TextualConvention, OctetString):
    description = 'Current CIFS mode'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CifsConfigWINSServerTC(TextualConvention, OctetString):
    description = 'CIFS WINS servers'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsConfigNetBIOSHostnameTC(TextualConvention, OctetString):
    description = 'CIFS NetBIOS hostname'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CifsConfigDomainControllerTC(TextualConvention, OctetString):
    description = 'CIFS Domain Controller'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsConfigDNSTC(TextualConvention, OctetString):
    description = 'CIFS DNS server'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsConfigGroupNameTC(TextualConvention, OctetString):
    description = 'CIFS group name'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CifsConfigMaxConnectionTC(TextualConvention, Counter32):
    description = 'CIFS configuration maximum connection'
    status = 'current'
    displayHint = 'd'

class CifsConfigMaxOpenFilesPerConnectionTC(TextualConvention, Counter32):
    description = 'CIFS configuration maximum open files per connection'
    status = 'current'
    displayHint = 'd'

class CifsShareIndexTC(TextualConvention, Integer32):
    description = 'Index of CIFS share'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CifsShareNameTC(TextualConvention, OctetString):
    description = 'CIFS share name'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CifsSharePathTC(TextualConvention, OctetString):
    description = 'CIFS share path'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsShareMaxConnectionTC(TextualConvention, Counter32):
    description = 'CIFS maximum connection'
    status = 'current'
    displayHint = 'd'

class CifsShareClientsTC(TextualConvention, OctetString):
    description = 'CIFS share clients'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsShareBrowsingTC(TextualConvention, Integer32):
    description = 'Current CIFS browsing'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CifsShareWriteableTC(TextualConvention, Integer32):
    description = 'Current CIFS writeable'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CifsShareUserTC(TextualConvention, OctetString):
    description = 'CIFS share user'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsShareCommentTC(TextualConvention, OctetString):
    description = 'CIFS share comment'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CifsStatsSummaryIndexTC(TextualConvention, Integer32):
    description = 'Index of Cifs Stats Summary Table'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CifsStatsDetailsIndexTC(TextualConvention, Integer32):
    description = 'Index of CIFS Stats Details Table'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CifsOptionsIndexTC(TextualConvention, Integer32):
    description = 'Index of CIFS Option Table Index'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class CifsOptionsNameTC(TextualConvention, OctetString):
    description = 'Index of CIFS Option Name '
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CifsOptionsValueTC(TextualConvention, OctetString):
    description = 'Index of CIFS Option Value '
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class DDboostStatsIndexTC(TextualConvention, Integer32):
    description = 'Index of ddboost Stats Table'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DDboostStatusTC(TextualConvention, Integer32):
    description = 'DDboost Status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class DDboostUserTC(TextualConvention, OctetString):
    description = 'DDboost user'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class SystemSerialNumberTC(TextualConvention, OctetString):
    description = 'System Serial Number'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class SystemTimeZoneNameTC(TextualConvention, OctetString):
    description = "DDR system's time zone name"
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class SystemNotesTC(TextualConvention, OctetString):
    description = 'System notes'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class FileSystemArchiveUnitStateTC(TextualConvention, Integer32):
    description = 'File System Archive Unit State'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("new", 1), ("target", 2), ("sealed", 3))

class FileSystemArchiveUnitStatusTC(TextualConvention, Integer32):
    description = 'File System Archive Unit Status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ready", 1), ("disabled", 2))

class MtreeListStatusTC(TextualConvention, Integer32):
    description = 'Mtree List  Status TC'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("deleted", 1), ("readOnly", 2), ("readWrite", 3), ("replicationDestination", 4), ("retentionLockEnabled", 5), ("retentionLockDisabled", 6))

class MtreeRetentionLockStatusTC(TextualConvention, Integer32):
    description = 'Mtree Retention Lock'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class TenantUnitMgmtUserListUserRoleTC(TextualConvention, Integer32):
    description = 'The role of a Management user of a tenant-unit. It can be \n                tenant-admin (1) or tenant-user (2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tenantAdmin", 1), ("tenantUser", 2))

class TenantUnitMgmtGroupTypeTC(TextualConvention, Integer32):
    description = 'The type of a Management group of a tenant-unit.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("all", 0), ("unknown", 1), ("local", 2), ("ad", 3), ("nis", 4), ("ldap", 5))

class SmtStatusTC(TextualConvention, Integer32):
    description = 'Status of the SMT feature components. They may be enabled or \n                disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class TenantUnitSecurityModeTC(TextualConvention, Integer32):
    description = 'The security mode of a tenant-unit. It can be \n                strict (1) or default (2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("strict", 1), ("default", 2))

class DDStatusTC(TextualConvention, Integer32):
    description = 'DD feature Status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class DdboostAccessClientsEncryStrengthTC(TextualConvention, Integer32):
    description = 'The types of Ddboost access clients encryption strength level'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3))
    namedValues = NamedValues(("none", 0), ("medium", 2), ("high", 3))

class DdboostAccessClientsAuthModeTC(TextualConvention, Integer32):
    description = 'The types of Ddboost access clients authentication mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("oneWay", 1), ("twoWay", 2), ("anonymous", 3))

class HaSystemStatusTC(TextualConvention, Integer32):
    description = 'The status of the high availabiilty system.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("highlyAvailable", 1), ("degraded", 2))

class HaStatusTC(TextualConvention, Integer32):
    description = 'The status of a high availabiilty component.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("notOk", 2), ("notApplicable", 3))

power = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1))
powerModules = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1))
powerModuleTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1), )
if mibBuilder.loadTexts: powerModuleTable.setStatus('current')
if mibBuilder.loadTexts: powerModuleTable.setDescription('A table containing entries of PowerModuleEntry.')
powerModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "powerEnclosureID"), (0, "DATA-DOMAIN-MIB", "powerModuleIndex"))
if mibBuilder.loadTexts: powerModuleEntry.setStatus('current')
if mibBuilder.loadTexts: powerModuleEntry.setDescription('powerModuleTable Row Description')
powerEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: powerEnclosureID.setStatus('current')
if mibBuilder.loadTexts: powerEnclosureID.setDescription('Power Module Enclosure ID')
powerModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 2), PowerModuleIndexTC())
if mibBuilder.loadTexts: powerModuleIndex.setStatus('current')
if mibBuilder.loadTexts: powerModuleIndex.setDescription('Power Module index')
powerModuleDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 3), PowerModuleDescriptionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerModuleDescription.setStatus('current')
if mibBuilder.loadTexts: powerModuleDescription.setDescription('Power Module Description')
powerModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 4), PowerModuleStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerModuleStatus.setStatus('current')
if mibBuilder.loadTexts: powerModuleStatus.setDescription('current enclosure Power Module status')
temperatures = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2))
temperatureSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1))
temperatureSensorTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1), )
if mibBuilder.loadTexts: temperatureSensorTable.setStatus('current')
if mibBuilder.loadTexts: temperatureSensorTable.setDescription('A table containing entries of TemperatureSensorEntry.')
temperatureSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tempEnclosureID"), (0, "DATA-DOMAIN-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: temperatureSensorEntry.setStatus('current')
if mibBuilder.loadTexts: temperatureSensorEntry.setDescription('temperatureSensorTable Row Description')
tempEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: tempEnclosureID.setStatus('current')
if mibBuilder.loadTexts: tempEnclosureID.setDescription('Temperature Sensor Enclosure ID')
tempSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 2), TempSensorIndexTC())
if mibBuilder.loadTexts: tempSensorIndex.setStatus('current')
if mibBuilder.loadTexts: tempSensorIndex.setDescription('Temperature Sensor Number')
tempSensorTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 3), TempSensorIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorTrapIndex.setStatus('current')
if mibBuilder.loadTexts: tempSensorTrapIndex.setDescription('Temperature Sensor Number Used for Traps')
tempSensorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 4), TempSensorDescriptionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorDescription.setStatus('current')
if mibBuilder.loadTexts: tempSensorDescription.setDescription('Temperature Sensor Description')
tempSensorCurrentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 5), Temperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorCurrentValue.setStatus('current')
if mibBuilder.loadTexts: tempSensorCurrentValue.setDescription('Current Temperature Value of the sensor')
tempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 6), TempSensorStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorStatus.setStatus('current')
if mibBuilder.loadTexts: tempSensorStatus.setDescription('Current status of the sensor')
fans = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3))
fanProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1))
fanPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1), )
if mibBuilder.loadTexts: fanPropertiesTable.setStatus('current')
if mibBuilder.loadTexts: fanPropertiesTable.setDescription('A table containing entries of FanPropertiesEntry.')
fanPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fanEnclosureID"), (0, "DATA-DOMAIN-MIB", "fanIndex"))
if mibBuilder.loadTexts: fanPropertiesEntry.setStatus('current')
if mibBuilder.loadTexts: fanPropertiesEntry.setDescription('fanPropertiesTable Row Description')
fanEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: fanEnclosureID.setStatus('current')
if mibBuilder.loadTexts: fanEnclosureID.setDescription('Enclosure ID of fan')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 2), FanIndexTC())
if mibBuilder.loadTexts: fanIndex.setStatus('current')
if mibBuilder.loadTexts: fanIndex.setDescription('Fan Number Index of the fan')
fanTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 3), FanIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanTrapIndex.setStatus('current')
if mibBuilder.loadTexts: fanTrapIndex.setDescription('Fan Number trap index, used for trap notifications')
fanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 4), FanDescriptionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanDescription.setStatus('current')
if mibBuilder.loadTexts: fanDescription.setDescription('Vendor supplied description of the fan')
fanLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 5), FanLevelTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanLevel.setStatus('current')
if mibBuilder.loadTexts: fanLevel.setDescription('current run level of fan')
fanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 6), FanStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStatus.setStatus('current')
if mibBuilder.loadTexts: fanStatus.setDescription('Current status of the fan')
nvramBatteries = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3))
nvramBatteryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1), )
if mibBuilder.loadTexts: nvramBatteryTable.setStatus('current')
if mibBuilder.loadTexts: nvramBatteryTable.setDescription('A table containing entries of NvramBatteryEntry.')
nvramBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nvramBatteriesIndex"), (0, "DATA-DOMAIN-MIB", "nvramBatteryIndex"))
if mibBuilder.loadTexts: nvramBatteryEntry.setStatus('current')
if mibBuilder.loadTexts: nvramBatteryEntry.setDescription('nvramBatteryTable Row Description')
nvramBatteriesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 1), NvramIndexTC())
if mibBuilder.loadTexts: nvramBatteriesIndex.setStatus('current')
if mibBuilder.loadTexts: nvramBatteriesIndex.setDescription('NVRAM card index')
nvramBatteryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 2), NvramBatteryIndexTC())
if mibBuilder.loadTexts: nvramBatteryIndex.setStatus('current')
if mibBuilder.loadTexts: nvramBatteryIndex.setDescription('NVRAM Battery Number')
nvramBatteryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 3), NvramBatteryStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramBatteryStatus.setStatus('current')
if mibBuilder.loadTexts: nvramBatteryStatus.setDescription('NVRAM Battery Status')
nvramBatteryCharge = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 4), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramBatteryCharge.setStatus('current')
if mibBuilder.loadTexts: nvramBatteryCharge.setDescription('NVRAM Battery charge percentage')
nvramProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1))
nvramPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1), )
if mibBuilder.loadTexts: nvramPropertiesTable.setStatus('current')
if mibBuilder.loadTexts: nvramPropertiesTable.setDescription('A table containing entries of NvramPropertiesEntry.')
nvramPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nvramPropertiesIndex"))
if mibBuilder.loadTexts: nvramPropertiesEntry.setStatus('current')
if mibBuilder.loadTexts: nvramPropertiesEntry.setDescription('nvramPropertiesTable Row Description')
nvramPropertiesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 1), NvramIndexTC())
if mibBuilder.loadTexts: nvramPropertiesIndex.setStatus('current')
if mibBuilder.loadTexts: nvramPropertiesIndex.setDescription('NVRAM card index')
nvramMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 2), NvramMemorySizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramMemorySize.setStatus('current')
if mibBuilder.loadTexts: nvramMemorySize.setDescription('Size of NVRAM Memory in bytes')
nvramWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 3), NvramWindowSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramWindowSize.setStatus('current')
if mibBuilder.loadTexts: nvramWindowSize.setDescription('Window size of NVRAM in bytes')
nvramHCMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 4), NvramHCPropertyBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramHCMemorySize.setStatus('current')
if mibBuilder.loadTexts: nvramHCMemorySize.setDescription("The size of an NVRAM entity's memory in bytes, with support for\n             high capacity modules. This entry may be used in place of \n             nvramMemorySize.")
nvramStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2))
nvramStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1), )
if mibBuilder.loadTexts: nvramStatsTable.setStatus('current')
if mibBuilder.loadTexts: nvramStatsTable.setDescription('A table containing entries of NvramStatsEntry.')
nvramStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nvramStatsIndex"))
if mibBuilder.loadTexts: nvramStatsEntry.setStatus('current')
if mibBuilder.loadTexts: nvramStatsEntry.setDescription('nvramStatsTable Row Description')
nvramStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1, 1), NvramIndexTC())
if mibBuilder.loadTexts: nvramStatsIndex.setStatus('current')
if mibBuilder.loadTexts: nvramStatsIndex.setDescription('NVRAM card index')
nvramPCIErrorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1, 2), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramPCIErrorCount.setStatus('current')
if mibBuilder.loadTexts: nvramPCIErrorCount.setDescription('Number of PCI Errors Encountered on NVRAM Card')
nvramMemoryErrorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1, 3), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramMemoryErrorCount.setStatus('current')
if mibBuilder.loadTexts: nvramMemoryErrorCount.setDescription('Number of Memory Errors  Encountered on NVRAM Card')
fileSystemArchiveUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6))
fileSystemArchiveUnitTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1), )
if mibBuilder.loadTexts: fileSystemArchiveUnitTable.setStatus('current')
if mibBuilder.loadTexts: fileSystemArchiveUnitTable.setDescription('A table containing entries of fileSystemArchiveUnitEntry.')
fileSystemArchiveUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemArchiveUnitIndex"))
if mibBuilder.loadTexts: fileSystemArchiveUnitEntry.setStatus('current')
if mibBuilder.loadTexts: fileSystemArchiveUnitEntry.setDescription('fileSystemArchiveUnitTable Row Description')
fileSystemArchiveUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: fileSystemArchiveUnitIndex.setStatus('current')
if mibBuilder.loadTexts: fileSystemArchiveUnitIndex.setDescription('fileSystem ArchiveUnit index')
fileSystemArchiveUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitName.setStatus('current')
if mibBuilder.loadTexts: fileSystemArchiveUnitName.setDescription('fileSystem ArchiveUnit Name')
fileSystemArchiveUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 3), FileSystemArchiveUnitStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitState.setStatus('current')
if mibBuilder.loadTexts: fileSystemArchiveUnitState.setDescription('fileSystem ArchiveUnit State')
fileSystemArchiveUnitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 4), FileSystemArchiveUnitStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitStatus.setStatus('current')
if mibBuilder.loadTexts: fileSystemArchiveUnitStatus.setDescription('fileSystem ArchiveUnit Status')
fileSystemArchiveUnitStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 5), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitStartTime.setStatus('current')
if mibBuilder.loadTexts: fileSystemArchiveUnitStartTime.setDescription('fileSystem ArchiveUnit start Time')
fileSystemArchiveUnitEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 6), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitEndTime.setStatus('current')
if mibBuilder.loadTexts: fileSystemArchiveUnitEndTime.setDescription('fileSystem ArchiveUnit End Time')
fileSystemArchiveUnitSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 7), DDMibTableSizeGibTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitSize.setStatus('current')
if mibBuilder.loadTexts: fileSystemArchiveUnitSize.setDescription('fileSystem ArchiveUnit Size in Gib')
fileSystemArchiveUnitDiskGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 8), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitDiskGroups.setStatus('current')
if mibBuilder.loadTexts: fileSystemArchiveUnitDiskGroups.setDescription('fileSystem ArchiveUnit DiskGroups')
fileSystemClean = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5))
fileSystemCleanTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1), )
if mibBuilder.loadTexts: fileSystemCleanTable.setStatus('current')
if mibBuilder.loadTexts: fileSystemCleanTable.setDescription('A table containing entries of fileSystemCleanEntry.')
fileSystemCleanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemCleanIndex"))
if mibBuilder.loadTexts: fileSystemCleanEntry.setStatus('current')
if mibBuilder.loadTexts: fileSystemCleanEntry.setDescription('fileSystemCleanTable Row Description')
fileSystemCleanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 1), FileSystemCleanIndexTC())
if mibBuilder.loadTexts: fileSystemCleanIndex.setStatus('current')
if mibBuilder.loadTexts: fileSystemCleanIndex.setDescription('fileSystem Clean index')
fileSystemCleanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 2), FileSystemCleanStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCleanStatus.setStatus('current')
if mibBuilder.loadTexts: fileSystemCleanStatus.setDescription('fileSystem Clean Status')
fileSystemCleanSchedule = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 3), FileSystemCleanScheduleTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCleanSchedule.setStatus('current')
if mibBuilder.loadTexts: fileSystemCleanSchedule.setDescription('fileSystem Clean Schedule')
fileSystemCleanThrottle = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 4), FileSystemCleanThrottleTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCleanThrottle.setStatus('current')
if mibBuilder.loadTexts: fileSystemCleanThrottle.setDescription('fileSystem Clean Throttle')
fileSystemCompression = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3))
fileSystemCompressionTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1), )
if mibBuilder.loadTexts: fileSystemCompressionTable.setStatus('current')
if mibBuilder.loadTexts: fileSystemCompressionTable.setDescription('A table containing entries of FileSystemCompressionEntry.')
fileSystemCompressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemCompressionIndex"))
if mibBuilder.loadTexts: fileSystemCompressionEntry.setStatus('current')
if mibBuilder.loadTexts: fileSystemCompressionEntry.setDescription('fileSystemCompressionTable Row Description')
fileSystemCompressionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 1), FileSystemResourceIndexTC())
if mibBuilder.loadTexts: fileSystemCompressionIndex.setStatus('current')
if mibBuilder.loadTexts: fileSystemCompressionIndex.setDescription('File system compression index')
fileSystemCompressionPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 2), FileSystemCompressionPeriodTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCompressionPeriod.setStatus('current')
if mibBuilder.loadTexts: fileSystemCompressionPeriod.setDescription('File system compression period')
fileSystemCompressionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 3), DateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCompressionStartTime.setStatus('current')
if mibBuilder.loadTexts: fileSystemCompressionStartTime.setDescription('File system compression start time')
fileSystemCompressionEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 4), DateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCompressionEndTime.setStatus('current')
if mibBuilder.loadTexts: fileSystemCompressionEndTime.setDescription('File system compression end time')
fileSystemPreCompressionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 5), FileSystemCompressionSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemPreCompressionSize.setStatus('current')
if mibBuilder.loadTexts: fileSystemPreCompressionSize.setDescription('Size of the file system pre compression in gigabytes')
fileSystemPostCompressionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 6), FileSystemCompressionSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemPostCompressionSize.setStatus('current')
if mibBuilder.loadTexts: fileSystemPostCompressionSize.setDescription('Size of the file system post compression in gigabytes')
fileSystemGlobalCompressionFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 7), FileSystemCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemGlobalCompressionFactor.setStatus('current')
if mibBuilder.loadTexts: fileSystemGlobalCompressionFactor.setDescription('File system global compression factor')
fileSystemLocalCompressionFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 8), FileSystemCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemLocalCompressionFactor.setStatus('current')
if mibBuilder.loadTexts: fileSystemLocalCompressionFactor.setDescription('File system local compression factor')
fileSystemTotalCompressionFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 9), FileSystemCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemTotalCompressionFactor.setStatus('current')
if mibBuilder.loadTexts: fileSystemTotalCompressionFactor.setDescription('File system Total compression factor')
fileSystemReductionPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 10), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemReductionPercent.setStatus('deprecated')
if mibBuilder.loadTexts: fileSystemReductionPercent.setDescription('File system Reduction Percent')
fileSystemReductionPercent1 = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 11), PercentageStr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemReductionPercent1.setStatus('current')
if mibBuilder.loadTexts: fileSystemReductionPercent1.setDescription('File system Reduction Percent')
fileSystemOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4))
fileSystemOptionsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1), )
if mibBuilder.loadTexts: fileSystemOptionsTable.setStatus('current')
if mibBuilder.loadTexts: fileSystemOptionsTable.setDescription('A table containing entries of fileSystemOptionsEntry.')
fileSystemOptionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemOptionsIndex"))
if mibBuilder.loadTexts: fileSystemOptionsEntry.setStatus('current')
if mibBuilder.loadTexts: fileSystemOptionsEntry.setDescription('fileSystemOptionsTable Row Description')
fileSystemOptionsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1, 1), FileSystemOptionsIndexTC())
if mibBuilder.loadTexts: fileSystemOptionsIndex.setStatus('current')
if mibBuilder.loadTexts: fileSystemOptionsIndex.setDescription('fileSystem Options index')
fileSystemOptionsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1, 2), FileSystemOptionsNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemOptionsName.setStatus('current')
if mibBuilder.loadTexts: fileSystemOptionsName.setDescription('This object represents the fileSystem Options type in text format.\n             Below lists the possible options and their representations.\n             --------------------------------   --------------------------\n             Option Name                        Representation in text\n             --------------------------------   --------------------------\n\t     Local compression type             gz/gzfast/lz\n\t     Marker-type                        auto/cv1\n\t     Report-replica-as-writable         enabled/disabled\n\t     Low-bw-optim replication support   enabled/disabled\n\t     Current global compression type    1/9\n\t     Staging reserve                    % of the total space/disabled\n\t     Staging clean                      % of staging reserve space\n\t     Staging delete suspend             % of staging reserve space \n\t     --------------------------------   ---------------------------\n            ')
fileSystemOptionsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1, 3), FileSystemOptionsValueTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemOptionsValue.setStatus('current')
if mibBuilder.loadTexts: fileSystemOptionsValue.setDescription('fileSystem Options Value')
fileSystemProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1))
fileSystemStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 1), FileSystemStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemStatus.setStatus('current')
if mibBuilder.loadTexts: fileSystemStatus.setDescription('Status of the file system')
fileSystemVirtualSpace = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 2), FileSystemSpaceUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemVirtualSpace.setStatus('current')
if mibBuilder.loadTexts: fileSystemVirtualSpace.setDescription('Amount of Uncompressed data that has been backed up by the system')
fileSystemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 3), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemUpTime.setStatus('current')
if mibBuilder.loadTexts: fileSystemUpTime.setDescription('File System Up time')
fileSystemStatusMessage = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 4), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemStatusMessage.setStatus('current')
if mibBuilder.loadTexts: fileSystemStatusMessage.setDescription('file system status message')
fileSystemSpace = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2))
fileSystemSpaceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1), )
if mibBuilder.loadTexts: fileSystemSpaceTable.setStatus('current')
if mibBuilder.loadTexts: fileSystemSpaceTable.setDescription('A table containing entries of FileSystemSpaceEntry.')
fileSystemSpaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSystemSpaceEntry.setStatus('current')
if mibBuilder.loadTexts: fileSystemSpaceEntry.setDescription('fileSystemSpaceTable Row Description')
fileSystemResourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 1), FileSystemResourceIndexTC())
if mibBuilder.loadTexts: fileSystemResourceIndex.setStatus('current')
if mibBuilder.loadTexts: fileSystemResourceIndex.setDescription('File system resource index')
fileSystemResourceTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 2), FileSystemResourceIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemResourceTrapIndex.setStatus('current')
if mibBuilder.loadTexts: fileSystemResourceTrapIndex.setDescription('File system resource trap index')
fileSystemResourceName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 3), FileSystemResourceNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemResourceName.setStatus('current')
if mibBuilder.loadTexts: fileSystemResourceName.setDescription('File system resource name')
fileSystemSpaceSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 4), FileSystemSpaceUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceSize.setStatus('current')
if mibBuilder.loadTexts: fileSystemSpaceSize.setDescription('Size of the file system resource in gigabytes')
fileSystemSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 5), FileSystemSpaceUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceUsed.setStatus('current')
if mibBuilder.loadTexts: fileSystemSpaceUsed.setDescription('Amount of used space within the file system resource in gigabytes')
fileSystemSpaceAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 6), FileSystemSpaceUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceAvail.setStatus('current')
if mibBuilder.loadTexts: fileSystemSpaceAvail.setDescription('Amount of available space within the file system resource in gigabytes')
fileSystemPercentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 7), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemPercentUsed.setStatus('current')
if mibBuilder.loadTexts: fileSystemPercentUsed.setDescription('Percentage of used space within the file system resource')
fileSystemSpaceCleanable = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 8), FileSystemSpaceUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceCleanable.setStatus('current')
if mibBuilder.loadTexts: fileSystemSpaceCleanable.setDescription('Amount of cleanable space within the file system resource')
fileSystemResourceTier = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 9), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemResourceTier.setStatus('current')
if mibBuilder.loadTexts: fileSystemResourceTier.setDescription('The tier that a resource belongs to, such as active or archive.')
currentAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1))
currentAlertTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1), )
if mibBuilder.loadTexts: currentAlertTable.setStatus('current')
if mibBuilder.loadTexts: currentAlertTable.setDescription('A table containing entries of CurrentAlertEntry.')
currentAlertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "currentAlertIndex"))
if mibBuilder.loadTexts: currentAlertEntry.setStatus('current')
if mibBuilder.loadTexts: currentAlertEntry.setDescription('currentAlertTable Row Description')
currentAlertIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 1), AlertIndexTC())
if mibBuilder.loadTexts: currentAlertIndex.setStatus('current')
if mibBuilder.loadTexts: currentAlertIndex.setDescription('Current Alert Row index')
currentAlertTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 2), AlertTimestampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertTimestamp.setStatus('current')
if mibBuilder.loadTexts: currentAlertTimestamp.setDescription('Timestamp of current alert')
currentAlertDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 3), AlertDescriptionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertDescription.setStatus('current')
if mibBuilder.loadTexts: currentAlertDescription.setDescription('Alert Description')
currentAlertSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 4), DDMibAlertSeverityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertSeverity.setStatus('current')
if mibBuilder.loadTexts: currentAlertSeverity.setDescription('Alert Severity')
currentAlertID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertID.setStatus('current')
if mibBuilder.loadTexts: currentAlertID.setDescription('Alert ID')
alertHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2))
alertHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1), )
if mibBuilder.loadTexts: alertHistoryTable.setStatus('current')
if mibBuilder.loadTexts: alertHistoryTable.setDescription('A table containing entries of Alert History Entries.')
alertHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "alertHistoryIndex"))
if mibBuilder.loadTexts: alertHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: alertHistoryEntry.setDescription('alertHistoryTable Row Description')
alertHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: alertHistoryIndex.setStatus('current')
if mibBuilder.loadTexts: alertHistoryIndex.setDescription('Alert History Row index')
alertHistoryTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 2), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertHistoryTimestamp.setStatus('current')
if mibBuilder.loadTexts: alertHistoryTimestamp.setDescription('Timestamp of  alert')
alertHistoryDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 3), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertHistoryDescription.setStatus('current')
if mibBuilder.loadTexts: alertHistoryDescription.setDescription('Alert history Description')
alertHistorySeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 4), DDMibAlertSeverityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertHistorySeverity.setStatus('current')
if mibBuilder.loadTexts: alertHistorySeverity.setDescription('Alert history Severity')
alertHistoryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 5), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertHistoryStatus.setStatus('current')
if mibBuilder.loadTexts: alertHistoryStatus.setDescription('Alert history Status (Post or Cleared)')
alertInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 4, 3))
alertInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1), )
if mibBuilder.loadTexts: alertInfoTable.setStatus('current')
if mibBuilder.loadTexts: alertInfoTable.setDescription('A table containing entries of Alert Information.')
alertInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "alertInfoIndex"))
if mibBuilder.loadTexts: alertInfoEntry.setStatus('current')
if mibBuilder.loadTexts: alertInfoEntry.setDescription('alertInfoTable Row Description')
alertInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: alertInfoIndex.setStatus('current')
if mibBuilder.loadTexts: alertInfoIndex.setDescription('Alert Info Row index')
alertInfoDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertInfoDescription.setStatus('current')
if mibBuilder.loadTexts: alertInfoDescription.setDescription('Alert Info Description')
systemStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1))
systemStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1), )
if mibBuilder.loadTexts: systemStatsTable.setStatus('current')
if mibBuilder.loadTexts: systemStatsTable.setDescription('A table containing entries of SystemStatsEntry.')
systemStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemStatsIndex"))
if mibBuilder.loadTexts: systemStatsEntry.setStatus('current')
if mibBuilder.loadTexts: systemStatsEntry.setDescription('systemStatsTable Row Description')
systemStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 1), SystemStatsIndexTC())
if mibBuilder.loadTexts: systemStatsIndex.setStatus('current')
if mibBuilder.loadTexts: systemStatsIndex.setDescription('System Stats Row index')
cpuAvgPercentageBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 2), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuAvgPercentageBusy.setStatus('current')
if mibBuilder.loadTexts: cpuAvgPercentageBusy.setDescription('CPU Average Percentage Busy')
cpuMaxPercentageBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 3), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuMaxPercentageBusy.setStatus('current')
if mibBuilder.loadTexts: cpuMaxPercentageBusy.setDescription('CPU Max Percentage Busy')
nfsOpsPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 4), OpsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsOpsPerSecond.setStatus('current')
if mibBuilder.loadTexts: nfsOpsPerSecond.setDescription('Number of NFS Operations performed per second')
nfsIdlePercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 5), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsIdlePercentage.setStatus('current')
if mibBuilder.loadTexts: nfsIdlePercentage.setDescription('Percentage of time NFS was Idle')
nfsProcPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsProcPercentage.setStatus('current')
if mibBuilder.loadTexts: nfsProcPercentage.setDescription('Percentage of time NFS was processing')
nfsSendPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 7), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsSendPercentage.setStatus('current')
if mibBuilder.loadTexts: nfsSendPercentage.setDescription('Percentage of time NFS was sending requests')
nfsReceivePercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 8), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsReceivePercentage.setStatus('current')
if mibBuilder.loadTexts: nfsReceivePercentage.setDescription('Percentage of time NFS was receiving requests')
cifsOpsPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 9), OpsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsOpsPerSecond.setStatus('current')
if mibBuilder.loadTexts: cifsOpsPerSecond.setDescription('Number of CIFS Operations performed per second')
diskReadKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 10), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadKBytesPerSecond.setStatus('current')
if mibBuilder.loadTexts: diskReadKBytesPerSecond.setDescription('Number of KBytes per second read from disk')
diskWriteKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 11), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteKBytesPerSecond.setStatus('current')
if mibBuilder.loadTexts: diskWriteKBytesPerSecond.setDescription('Number of KBytes per second written on disk')
diskBusyPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 12), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskBusyPercentage.setStatus('current')
if mibBuilder.loadTexts: diskBusyPercentage.setDescription('Percentage of Time Disks were busy')
nvramReadKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 13), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramReadKBytesPerSecond.setStatus('current')
if mibBuilder.loadTexts: nvramReadKBytesPerSecond.setDescription('Number of KBytes read per second from NVRAM')
nvramWriteKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 14), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramWriteKBytesPerSecond.setStatus('current')
if mibBuilder.loadTexts: nvramWriteKBytesPerSecond.setDescription('Number of KBytes written per second on NVRAM')
replInKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 15), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replInKBytesPerSecond.setStatus('current')
if mibBuilder.loadTexts: replInKBytesPerSecond.setDescription('Number of KBytes per second received for Replication')
replOutKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 16), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replOutKBytesPerSecond.setStatus('current')
if mibBuilder.loadTexts: replOutKBytesPerSecond.setDescription('Number of KBytes per second sent for Replication')
diskPerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2))
diskPerformanceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1), )
if mibBuilder.loadTexts: diskPerformanceTable.setStatus('current')
if mibBuilder.loadTexts: diskPerformanceTable.setDescription('A table containing entries of DiskPerformanceEntry.')
diskPerformanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskPerfEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskPerfIndex"))
if mibBuilder.loadTexts: diskPerformanceEntry.setStatus('current')
if mibBuilder.loadTexts: diskPerformanceEntry.setDescription('diskPerformanceTable Row Description')
diskPerfEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: diskPerfEnclosureID.setStatus('current')
if mibBuilder.loadTexts: diskPerfEnclosureID.setDescription('Enclosure ID of disk')
diskPerfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 2), DiskIndexTC())
if mibBuilder.loadTexts: diskPerfIndex.setStatus('current')
if mibBuilder.loadTexts: diskPerfIndex.setDescription('Disk Number')
diskSectorsRead = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 3), DiskSectorsPerSecondTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSectorsRead.setStatus('current')
if mibBuilder.loadTexts: diskSectorsRead.setDescription('Number of disk sectors read per second')
diskSectorsWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 4), DiskSectorsPerSecondTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSectorsWritten.setStatus('current')
if mibBuilder.loadTexts: diskSectorsWritten.setDescription('Number of disk sectors written per second')
diskTotalKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 5), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTotalKBytes.setStatus('current')
if mibBuilder.loadTexts: diskTotalKBytes.setDescription('Total Number of Kilo-bytes read/written per second')
diskBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskBusy.setStatus('current')
if mibBuilder.loadTexts: diskBusy.setDescription('Percentage of time disk is busy')
diskPerfState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 7), DiskStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPerfState.setStatus('current')
if mibBuilder.loadTexts: diskPerfState.setDescription('Current State of the disk')
diskProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1))
diskPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1), )
if mibBuilder.loadTexts: diskPropertiesTable.setStatus('current')
if mibBuilder.loadTexts: diskPropertiesTable.setDescription('A table containing entries of DiskPropertiesEntry.')
diskPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskPropEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskPropIndex"))
if mibBuilder.loadTexts: diskPropertiesEntry.setStatus('current')
if mibBuilder.loadTexts: diskPropertiesEntry.setDescription('diskPropertiesTable Row Description')
diskPropEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: diskPropEnclosureID.setStatus('current')
if mibBuilder.loadTexts: diskPropEnclosureID.setDescription('Enclosure ID of disk')
diskPropIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 2), DiskIndexTC())
if mibBuilder.loadTexts: diskPropIndex.setStatus('current')
if mibBuilder.loadTexts: diskPropIndex.setDescription('Disk Number')
diskPropTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 3), DiskIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPropTrapIndex.setStatus('current')
if mibBuilder.loadTexts: diskPropTrapIndex.setDescription('Disk Number for Traps')
diskModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 4), DiskModelTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskModel.setStatus('current')
if mibBuilder.loadTexts: diskModel.setDescription('Manufacture and model of the disk')
diskFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 5), DiskFirmwareVersionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: diskFirmwareVersion.setDescription('Firmware version of the disk')
diskSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 6), DiskSerialNumberTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSerialNumber.setStatus('current')
if mibBuilder.loadTexts: diskSerialNumber.setDescription('Serial Number of the disk')
diskCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 7), DiskCapacityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskCapacity.setStatus('current')
if mibBuilder.loadTexts: diskCapacity.setDescription('Capacity of the disk')
diskPropState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 8), DiskStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPropState.setStatus('current')
if mibBuilder.loadTexts: diskPropState.setDescription('Current State of the disk')
diskPack = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 9), DiskPackTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPack.setStatus('current')
if mibBuilder.loadTexts: diskPack.setDescription('Pack information of the disk.\n\t     Applicable to enclosures with packs such as ES60, and not for ES20 or ES30.')
diskReliability = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3))
diskReliabilityTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1), )
if mibBuilder.loadTexts: diskReliabilityTable.setStatus('current')
if mibBuilder.loadTexts: diskReliabilityTable.setDescription('A table containing entries of DiskReliabilityEntry.')
diskReliabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskErrEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskErrIndex"))
if mibBuilder.loadTexts: diskReliabilityEntry.setStatus('current')
if mibBuilder.loadTexts: diskReliabilityEntry.setDescription('diskReliabilityTable Row Description')
diskErrEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: diskErrEnclosureID.setStatus('current')
if mibBuilder.loadTexts: diskErrEnclosureID.setDescription('Enclosure ID of disk')
diskErrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 2), DiskIndexTC())
if mibBuilder.loadTexts: diskErrIndex.setStatus('current')
if mibBuilder.loadTexts: diskErrIndex.setDescription('Disk Number')
diskErrTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 3), DiskIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrTrapIndex.setStatus('current')
if mibBuilder.loadTexts: diskErrTrapIndex.setDescription('Disk Number for Traps')
diskTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 4), Temperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTemperature.setStatus('current')
if mibBuilder.loadTexts: diskTemperature.setDescription('Current Disk Temperature in Celsius')
diskTimeoutCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 5), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTimeoutCount.setStatus('current')
if mibBuilder.loadTexts: diskTimeoutCount.setDescription('Number of command timeouts')
diskReadFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 6), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadFailCount.setStatus('current')
if mibBuilder.loadTexts: diskReadFailCount.setDescription('Number of read failures')
diskWriteFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 7), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteFailCount.setStatus('current')
if mibBuilder.loadTexts: diskWriteFailCount.setDescription('Number of write failures')
diskMiscFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 8), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskMiscFailCount.setStatus('current')
if mibBuilder.loadTexts: diskMiscFailCount.setDescription('Number of miscellaneous failures')
diskOffTrackErrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 9), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskOffTrackErrCount.setStatus('current')
if mibBuilder.loadTexts: diskOffTrackErrCount.setDescription('Number of offtrack errors')
diskSoftEccCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 10), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSoftEccCount.setStatus('current')
if mibBuilder.loadTexts: diskSoftEccCount.setDescription('Number of soft ecc errors')
diskCrcErrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 11), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskCrcErrCount.setStatus('current')
if mibBuilder.loadTexts: diskCrcErrCount.setDescription('Number of crc errors')
diskProbationalCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 12), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskProbationalCount.setStatus('current')
if mibBuilder.loadTexts: diskProbationalCount.setDescription('Number of probational errors')
diskReallocCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 13), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReallocCount.setStatus('current')
if mibBuilder.loadTexts: diskReallocCount.setDescription('Number of reallocation errors')
diskErrState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 14), DiskStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrState.setStatus('current')
if mibBuilder.loadTexts: diskErrState.setDescription('Current State of the disk')
replicationConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2))
replicationConfigTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1), )
if mibBuilder.loadTexts: replicationConfigTable.setStatus('current')
if mibBuilder.loadTexts: replicationConfigTable.setDescription('A table containing entries of ReplicationConfigEntry.')
replicationConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "replConfigIndex"))
if mibBuilder.loadTexts: replicationConfigEntry.setStatus('current')
if mibBuilder.loadTexts: replicationConfigEntry.setDescription('replicationConfigTable Row Description')
replConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 1), ReplicationConfigIndexTC())
if mibBuilder.loadTexts: replConfigIndex.setStatus('current')
if mibBuilder.loadTexts: replConfigIndex.setDescription('ConfigIndex ID of replication source/dest pair')
replConfigContextId = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 2), ReplicationConfigContextIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigContextId.setStatus('current')
if mibBuilder.loadTexts: replConfigContextId.setDescription('ConfigContextId of replication source/dest pair')
replConfigSource = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 3), ReplicationConfigSourceTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigSource.setStatus('current')
if mibBuilder.loadTexts: replConfigSource.setDescription('Source for replication source/dest pair connection')
replConfigDest = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 4), ReplicationConfigDestTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigDest.setStatus('current')
if mibBuilder.loadTexts: replConfigDest.setDescription('Destination for replication connection')
replConfigConnHost = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 5), ReplicationConfigConnHostTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigConnHost.setStatus('current')
if mibBuilder.loadTexts: replConfigConnHost.setDescription('Host for a replication connection')
replConfigConnPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 6), ReplicationConfigConnPortTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigConnPort.setStatus('current')
if mibBuilder.loadTexts: replConfigConnPort.setDescription('Replication Configuration port for the connection')
replConfigLowBWOptim = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 7), ReplicationConfigLowBWOptimTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigLowBWOptim.setStatus('current')
if mibBuilder.loadTexts: replConfigLowBWOptim.setDescription('Replication configuration Low BW optim')
replConfigEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 8), ReplicationConfigEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigEnabled.setStatus('current')
if mibBuilder.loadTexts: replConfigEnabled.setDescription('Replication config Enabled')
replConfigTenantUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 9), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigTenantUnit.setStatus('current')
if mibBuilder.loadTexts: replConfigTenantUnit.setDescription('The name of the tenant-unit of a particular replication context.\n             ')
replicationHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3))
replicationHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1), )
if mibBuilder.loadTexts: replicationHistoryTable.setStatus('current')
if mibBuilder.loadTexts: replicationHistoryTable.setDescription('A table containing entries of replicationHistoryEntry.')
replicationHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "replHistoryContext"))
if mibBuilder.loadTexts: replicationHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: replicationHistoryEntry.setDescription('replicationHistoryTable Row Description')
replHistoryContext = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: replHistoryContext.setStatus('current')
if mibBuilder.loadTexts: replHistoryContext.setDescription('context ID of replication History source/dest pair')
replHistoryDate = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 2), DDMibDateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryDate.setStatus('current')
if mibBuilder.loadTexts: replHistoryDate.setDescription('replication History Date')
replHistoryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 3), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryTime.setStatus('current')
if mibBuilder.loadTexts: replHistoryTime.setDescription('replication History Time')
replHistoryPreCompWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 4), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPreCompWritten.setStatus('current')
if mibBuilder.loadTexts: replHistoryPreCompWritten.setDescription('Replication History Pre comp bytes written')
replHistoryPreCompRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 5), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPreCompRemaining.setStatus('current')
if mibBuilder.loadTexts: replHistoryPreCompRemaining.setDescription('Replication History Byte remaining')
replHistoryPreCompressed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 6), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPreCompressed.setStatus('current')
if mibBuilder.loadTexts: replHistoryPreCompressed.setDescription('Replication History Precompressed bytes')
replHistoryPostFiltered = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 7), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPostFiltered.setStatus('current')
if mibBuilder.loadTexts: replHistoryPostFiltered.setDescription('replication history post filtered bytes')
replHistoryPostLowBwOptim = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 8), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPostLowBwOptim.setStatus('current')
if mibBuilder.loadTexts: replHistoryPostLowBwOptim.setDescription('Replication history Post Low BW Optimum')
replHistoryPostLocalComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 9), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPostLocalComp.setStatus('current')
if mibBuilder.loadTexts: replHistoryPostLocalComp.setDescription('Replication History Post Local Comp')
replHistoryBytesNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 10), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryBytesNetwork.setStatus('current')
if mibBuilder.loadTexts: replHistoryBytesNetwork.setDescription('Replication History network bytes')
replHistorySyncedAsOfTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 11), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistorySyncedAsOfTime.setStatus('current')
if mibBuilder.loadTexts: replHistorySyncedAsOfTime.setDescription('Time when the source and destination were in sync,\n             or 0 if the time is unknown')
replicationInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1))
replicationInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1), )
if mibBuilder.loadTexts: replicationInfoTable.setStatus('current')
if mibBuilder.loadTexts: replicationInfoTable.setDescription('A table containing entries of ReplicationInfoEntry.')
replicationInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "replContext"))
if mibBuilder.loadTexts: replicationInfoEntry.setStatus('current')
if mibBuilder.loadTexts: replicationInfoEntry.setDescription('replicationInfoTable Row Description')
replContext = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 1), ReplicationContextTC())
if mibBuilder.loadTexts: replContext.setStatus('current')
if mibBuilder.loadTexts: replContext.setDescription('context ID of replication source/dest pair')
replTrapContext = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 2), ReplicationContextTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replTrapContext.setStatus('current')
if mibBuilder.loadTexts: replTrapContext.setDescription('context ID of replication source/dest pair for traps')
replState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 3), ReplicationStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replState.setStatus('current')
if mibBuilder.loadTexts: replState.setDescription('state of replication source/dest pair')
replStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 4), ReplicationStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replStatus.setStatus('current')
if mibBuilder.loadTexts: replStatus.setDescription('status of replication source/dest pair connection')
replFileSysStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 5), FileSystemStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replFileSysStatus.setStatus('current')
if mibBuilder.loadTexts: replFileSysStatus.setDescription('status of filesystem')
replConnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 6), ReplicationConnectTimeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConnTime.setStatus('current')
if mibBuilder.loadTexts: replConnTime.setDescription("time of connection established between source and dest,\n             or time since disconnect if status is 'disconnected'")
replSource = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 7), ReplicationPathTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replSource.setStatus('current')
if mibBuilder.loadTexts: replSource.setDescription('network path to replication source directory')
replDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 8), ReplicationPathTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replDestination.setStatus('current')
if mibBuilder.loadTexts: replDestination.setDescription('network path to replication destination directory')
replPreCompBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 9), ReplicationTrafficTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPreCompBytesSent.setStatus('current')
if mibBuilder.loadTexts: replPreCompBytesSent.setDescription('pre compression bytes sent')
replPostCompBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 10), ReplicationTrafficTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPostCompBytesSent.setStatus('current')
if mibBuilder.loadTexts: replPostCompBytesSent.setDescription('post compression bytes sent')
replPreCompBytesRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 11), ReplicationTrafficTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPreCompBytesRemaining.setStatus('current')
if mibBuilder.loadTexts: replPreCompBytesRemaining.setDescription('pre compression bytes remaining')
replPostCompBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 12), ReplicationTrafficTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPostCompBytesReceived.setStatus('current')
if mibBuilder.loadTexts: replPostCompBytesReceived.setDescription('post compression bytes received')
replThrottle = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 13), ReplicationThrottleTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replThrottle.setStatus('current')
if mibBuilder.loadTexts: replThrottle.setDescription('replication throttle in bps -- -1 is disabled, 0 unlimited')
replSyncedAsOfTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 14), ReplicationSyncedTimeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replSyncedAsOfTime.setStatus('current')
if mibBuilder.loadTexts: replSyncedAsOfTime.setDescription('time when the source and destination were in sync,\n             or 0 if the time is unknown')
replicationPerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4))
replicationPerformanceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1), )
if mibBuilder.loadTexts: replicationPerformanceTable.setStatus('current')
if mibBuilder.loadTexts: replicationPerformanceTable.setDescription('A table containing entries of replicationPerformanceEntry.')
replicationPerformanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "replContext"))
if mibBuilder.loadTexts: replicationPerformanceEntry.setStatus('current')
if mibBuilder.loadTexts: replicationPerformanceEntry.setDescription('replicationPerformanceTable Row Description')
replPerformancePreCompKBPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 1), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformancePreCompKBPerSec.setStatus('current')
if mibBuilder.loadTexts: replPerformancePreCompKBPerSec.setDescription("Network (KB/s): The size value before compression is applied. Sometimes referred to as 'logical size.'")
replPerformanceNetworkKBPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 2), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceNetworkKBPerSec.setStatus('current')
if mibBuilder.loadTexts: replPerformanceNetworkKBPerSec.setDescription('Network (KB/s): The amount of compressed data transferred over the network per second.')
replPerformanceStreams = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceStreams.setStatus('current')
if mibBuilder.loadTexts: replPerformanceStreams.setDescription('An internal system resource associated with reads and writes.\n             One replication context can use multiple streams for better performance.')
replPerformanceBusyReading = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceBusyReading.setStatus('current')
if mibBuilder.loadTexts: replPerformanceBusyReading.setDescription('The time spent reading filesystem data from the local filesystem.\n             Typically this number is the second highest number after Network.\n             On a deployment with high network bandwidth, Reading may be the largest column.')
replPerformanceBusyMeta = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceBusyMeta.setStatus('current')
if mibBuilder.loadTexts: replPerformanceBusyMeta.setDescription('The time spent on miscellaneous bookkeeping activities and replicating filesystem\n            namespace operations. Typically this value is under 50. If this value exceeds 50 on a\n            sustained basis, it may indicate an unusual workload (a large number of file attribute\n            updates, for example).')
replPerformanceWaitingDest = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 6), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceWaitingDest.setStatus('current')
if mibBuilder.loadTexts: replPerformanceWaitingDest.setDescription('The time spent waiting due to the receiver not providing the sender enough information\n            on what data to send. Typically this value is low. Exceptions include systems on\n            high-speed networks where the sender is a more powerful Data Domain system than the\n            replica, or where the replica has a higher workload than the sender because the replica\n            is the destination for a multiple replication contexts.')
replPerformanceWaitingNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 7), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceWaitingNetwork.setStatus('current')
if mibBuilder.loadTexts: replPerformanceWaitingNetwork.setDescription('The time spent waiting due to the receiver not providing the sender enough information\n            on what data to send. Typically this value is low. Exceptions include systems on\n            high-speed networks where the sender is a more powerful Data Domain system than the\n            replica, or where the replica has a higher workload than the sender because the replica\n            is the destination for a multiple replication contexts.')
nfsActive = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4))
nfsActiveTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1), )
if mibBuilder.loadTexts: nfsActiveTable.setStatus('current')
if mibBuilder.loadTexts: nfsActiveTable.setDescription('A table containing entries of Nfs Active Clients.')
nfsActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nfsActiveIndex"))
if mibBuilder.loadTexts: nfsActiveEntry.setStatus('current')
if mibBuilder.loadTexts: nfsActiveEntry.setDescription('nfsActiveTable Row Description')
nfsActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: nfsActiveIndex.setStatus('current')
if mibBuilder.loadTexts: nfsActiveIndex.setDescription('NFS Active index')
nfsActivePath = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1, 2), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsActivePath.setStatus('current')
if mibBuilder.loadTexts: nfsActivePath.setDescription('NFS Active client path')
nfsActiveClients = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1, 3), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsActiveClients.setStatus('current')
if mibBuilder.loadTexts: nfsActiveClients.setDescription('NFS Active Client')
nfsClient = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2))
nfsClientTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1), )
if mibBuilder.loadTexts: nfsClientTable.setStatus('current')
if mibBuilder.loadTexts: nfsClientTable.setDescription('A table containing entries of NfsClientEntry.')
nfsClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nfsClientIndex"))
if mibBuilder.loadTexts: nfsClientEntry.setStatus('current')
if mibBuilder.loadTexts: nfsClientEntry.setDescription('nfsClientTable Row Description')
nfsClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 1), NfsClientIndexTC())
if mibBuilder.loadTexts: nfsClientIndex.setStatus('current')
if mibBuilder.loadTexts: nfsClientIndex.setDescription('NFS client index')
nfsClientPath = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 2), NfsClientPathTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsClientPath.setStatus('current')
if mibBuilder.loadTexts: nfsClientPath.setDescription('NFS client path')
nfsClientClients = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 3), NfsClientClientsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsClientClients.setStatus('current')
if mibBuilder.loadTexts: nfsClientClients.setDescription('List of NFS clients')
nfsClientOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 4), NfsClientOptionsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsClientOptions.setStatus('current')
if mibBuilder.loadTexts: nfsClientOptions.setDescription("NFS client's options")
nfsPort = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5))
nfsPortTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1), )
if mibBuilder.loadTexts: nfsPortTable.setStatus('current')
if mibBuilder.loadTexts: nfsPortTable.setDescription('A table containing entries of NfsPortEntry.')
nfsPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nfsPortIndex"))
if mibBuilder.loadTexts: nfsPortEntry.setStatus('current')
if mibBuilder.loadTexts: nfsPortEntry.setDescription('nfsPortTable Row Description')
nfsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: nfsPortIndex.setStatus('current')
if mibBuilder.loadTexts: nfsPortIndex.setDescription('NFS Port index')
nfsPortService = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsPortService.setStatus('current')
if mibBuilder.loadTexts: nfsPortService.setDescription('NFS Port Service Name')
nfsPortPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1, 3), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsPortPort.setStatus('current')
if mibBuilder.loadTexts: nfsPortPort.setDescription('NFS Service Port')
nfsProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 9, 1))
nfsStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 9, 1, 1), NfsStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatus.setStatus('current')
if mibBuilder.loadTexts: nfsStatus.setDescription('Status of the network file system')
nfsStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3))
nfsStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1), )
if mibBuilder.loadTexts: nfsStatsTable.setStatus('current')
if mibBuilder.loadTexts: nfsStatsTable.setDescription('A table containing entries of NfsStatsEntry.')
nfsStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nfsStatsIndex"))
if mibBuilder.loadTexts: nfsStatsEntry.setStatus('current')
if mibBuilder.loadTexts: nfsStatsEntry.setDescription('nfsStatsTable Row Description')
nfsStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 1), NfsStatsIndexTC())
if mibBuilder.loadTexts: nfsStatsIndex.setStatus('current')
if mibBuilder.loadTexts: nfsStatsIndex.setDescription('NFS resource index')
nfsStatsExportPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 2), NfsStatsExportPointTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsExportPoint.setStatus('current')
if mibBuilder.loadTexts: nfsStatsExportPoint.setDescription('NFS export point')
nfsStatsFilesystemType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 3), NfsStatsFilesystemTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsFilesystemType.setStatus('current')
if mibBuilder.loadTexts: nfsStatsFilesystemType.setDescription('File system type')
nfsStatsCacheEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 4), NfsStatsCacheEntryTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsCacheEntry.setStatus('current')
if mibBuilder.loadTexts: nfsStatsCacheEntry.setDescription('Number of cache entries')
nfsStatsFileHandleLookup = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 5), NfsStatsFileHandleLookupTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsFileHandleLookup.setStatus('current')
if mibBuilder.loadTexts: nfsStatsFileHandleLookup.setDescription('File handle lookup count')
nfsStatsMaxCacheSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 6), NfsStatsMaxCacheSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsMaxCacheSize.setStatus('current')
if mibBuilder.loadTexts: nfsStatsMaxCacheSize.setDescription('Max cache size')
nfsStatsCurrentOpenStreams = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 7), NfsStatsCurrentOpenStreamsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsCurrentOpenStreams.setStatus('current')
if mibBuilder.loadTexts: nfsStatsCurrentOpenStreams.setDescription('Current open stream count')
cifsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2))
cifsConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 1), CifsConfigModeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigMode.setStatus('current')
if mibBuilder.loadTexts: cifsConfigMode.setDescription('CIFS configuration mode')
cifsConfigWINSServer = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 2), CifsConfigWINSServerTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigWINSServer.setStatus('current')
if mibBuilder.loadTexts: cifsConfigWINSServer.setDescription('CIFS WINS server')
cifsConfigNetBIOSHostname = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 3), CifsConfigNetBIOSHostnameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigNetBIOSHostname.setStatus('current')
if mibBuilder.loadTexts: cifsConfigNetBIOSHostname.setDescription('CIFS Net BIOS hostname')
cifsConfigDomainController = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 4), CifsConfigDomainControllerTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigDomainController.setStatus('current')
if mibBuilder.loadTexts: cifsConfigDomainController.setDescription('CIFS domain controller')
cifsConfigDNS = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 5), CifsConfigDNSTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigDNS.setStatus('current')
if mibBuilder.loadTexts: cifsConfigDNS.setDescription('CIFS DNS server')
cifsConfigGroupName = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 6), CifsConfigGroupNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigGroupName.setStatus('current')
if mibBuilder.loadTexts: cifsConfigGroupName.setDescription('CIFS configuration group name')
cifsConfigMaxConnection = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 7), CifsConfigMaxConnectionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigMaxConnection.setStatus('current')
if mibBuilder.loadTexts: cifsConfigMaxConnection.setDescription('CIFS configuration maximum connection')
cifsConfigMaxOpenFilesPerConnection = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 8), CifsConfigMaxOpenFilesPerConnectionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigMaxOpenFilesPerConnection.setStatus('deprecated')
if mibBuilder.loadTexts: cifsConfigMaxOpenFilesPerConnection.setDescription('CIFS configuration maximum open files per connection')
cifsConfigMaxOpenFiles = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigMaxOpenFiles.setStatus('current')
if mibBuilder.loadTexts: cifsConfigMaxOpenFiles.setDescription('CIFS configuration maximum open files')
cifsOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5))
cifsOptionsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1), )
if mibBuilder.loadTexts: cifsOptionsTable.setStatus('current')
if mibBuilder.loadTexts: cifsOptionsTable.setDescription('A table containing entries of CifsOptionsEntry.')
cifsOptionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "cifsOptionsIndex"))
if mibBuilder.loadTexts: cifsOptionsEntry.setStatus('current')
if mibBuilder.loadTexts: cifsOptionsEntry.setDescription('cifsOptionsTable Row Description')
cifsOptionsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1, 1), CifsOptionsIndexTC())
if mibBuilder.loadTexts: cifsOptionsIndex.setStatus('current')
if mibBuilder.loadTexts: cifsOptionsIndex.setDescription('CIFS Options index')
cifsOptionsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1, 2), CifsOptionsNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsOptionsName.setStatus('current')
if mibBuilder.loadTexts: cifsOptionsName.setDescription('CIFS Options name')
cifsOptionsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1, 3), CifsOptionsValueTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsOptionsValue.setStatus('current')
if mibBuilder.loadTexts: cifsOptionsValue.setDescription('CIFS Options Value')
cifsProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 10, 1))
cifsStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 1, 1), CifsStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsStatus.setStatus('current')
if mibBuilder.loadTexts: cifsStatus.setDescription('CIFS status')
cifsShare = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3))
cifsShareTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1), )
if mibBuilder.loadTexts: cifsShareTable.setStatus('current')
if mibBuilder.loadTexts: cifsShareTable.setDescription('A table containing entries of CifsShareEntry.')
cifsShareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "cifsShareIndex"))
if mibBuilder.loadTexts: cifsShareEntry.setStatus('current')
if mibBuilder.loadTexts: cifsShareEntry.setDescription('cifsShareTable Row Description')
cifsShareIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 1), CifsShareIndexTC())
if mibBuilder.loadTexts: cifsShareIndex.setStatus('current')
if mibBuilder.loadTexts: cifsShareIndex.setDescription('CIFS share index')
cifsShareName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 2), CifsShareNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareName.setStatus('current')
if mibBuilder.loadTexts: cifsShareName.setDescription('CIFS share name')
cifsSharePath = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 3), CifsSharePathTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsSharePath.setStatus('current')
if mibBuilder.loadTexts: cifsSharePath.setDescription('CIFS share path')
cifsShareClients = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 4), CifsShareClientsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareClients.setStatus('current')
if mibBuilder.loadTexts: cifsShareClients.setDescription('CIFS share clients')
cifsShareUser = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 5), CifsShareUserTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareUser.setStatus('current')
if mibBuilder.loadTexts: cifsShareUser.setDescription('CIFS share user')
cifsShareComment = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 6), CifsShareCommentTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareComment.setStatus('current')
if mibBuilder.loadTexts: cifsShareComment.setDescription('CIFS share comment')
cifsShareBrowsing = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 7), CifsShareBrowsingTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareBrowsing.setStatus('current')
if mibBuilder.loadTexts: cifsShareBrowsing.setDescription('CIFS share browsing')
cifsShareWriteable = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 8), CifsShareWriteableTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareWriteable.setStatus('current')
if mibBuilder.loadTexts: cifsShareWriteable.setDescription('CIFS share writeable')
cifsShareMaxConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 9), CifsShareMaxConnectionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareMaxConnection.setStatus('current')
if mibBuilder.loadTexts: cifsShareMaxConnection.setDescription('CIFS share maximum connection')
vtlConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2))
vtlLibrary = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1))
vtlLibraryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1), )
if mibBuilder.loadTexts: vtlLibraryTable.setStatus('current')
if mibBuilder.loadTexts: vtlLibraryTable.setDescription('A table containing entries of VtlLibraryEntry.')
vtlLibraryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlLibraryIndex"))
if mibBuilder.loadTexts: vtlLibraryEntry.setStatus('current')
if mibBuilder.loadTexts: vtlLibraryEntry.setDescription('vtlLibraryTable Row Description')
vtlLibraryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 1), VtlLibraryIndexTC())
if mibBuilder.loadTexts: vtlLibraryIndex.setStatus('current')
if mibBuilder.loadTexts: vtlLibraryIndex.setDescription('VTL Library index')
vtlLibraryName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 2), VtlLibraryNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryName.setStatus('current')
if mibBuilder.loadTexts: vtlLibraryName.setDescription('VTL library name')
vtlLibraryVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 3), VtlLibraryVendorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryVendor.setStatus('current')
if mibBuilder.loadTexts: vtlLibraryVendor.setDescription('VTL library vendor')
vtlLibraryModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 4), VtlLibraryModelTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryModel.setStatus('current')
if mibBuilder.loadTexts: vtlLibraryModel.setDescription('VTL library model')
vtlLibraryRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 5), VtlLibraryRevisionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryRevision.setStatus('current')
if mibBuilder.loadTexts: vtlLibraryRevision.setDescription('VTL library revision')
vtlLibrarySerial = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 6), VtlLibrarySerialTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibrarySerial.setStatus('current')
if mibBuilder.loadTexts: vtlLibrarySerial.setDescription('VTL library serial')
vtlLibraryTotalDrives = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 7), VtlLibraryTotalDrivesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryTotalDrives.setStatus('current')
if mibBuilder.loadTexts: vtlLibraryTotalDrives.setDescription('VTL library total drives')
vtlLibraryTotalSlots = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 8), VtlLibraryTotalSlotsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryTotalSlots.setStatus('current')
if mibBuilder.loadTexts: vtlLibraryTotalSlots.setDescription('VTL library total slots')
vtlLibraryTotalCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 9), VtlLibraryTotalCapsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryTotalCaps.setStatus('current')
if mibBuilder.loadTexts: vtlLibraryTotalCaps.setDescription('VTL library total caps')
vtlLibraryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 10), VtlLibraryStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryStatus.setStatus('current')
if mibBuilder.loadTexts: vtlLibraryStatus.setDescription('VTL library status')
vtlDrive = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2))
vtlDriveTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1), )
if mibBuilder.loadTexts: vtlDriveTable.setStatus('current')
if mibBuilder.loadTexts: vtlDriveTable.setDescription('A table containing entries of VtlDriveEntry.')
vtlDriveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlDriveIndex"))
if mibBuilder.loadTexts: vtlDriveEntry.setStatus('current')
if mibBuilder.loadTexts: vtlDriveEntry.setDescription('vtlDriveTable Row Description')
vtlDriveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 1), VtlDriveIndexTC())
if mibBuilder.loadTexts: vtlDriveIndex.setStatus('current')
if mibBuilder.loadTexts: vtlDriveIndex.setDescription('VTL drive index')
vtlDriveName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 2), VtlDriveNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveName.setStatus('current')
if mibBuilder.loadTexts: vtlDriveName.setDescription('VTL drive name')
vtlDriveVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 3), VtlDriveVendorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveVendor.setStatus('current')
if mibBuilder.loadTexts: vtlDriveVendor.setDescription('VTL drive vendor')
vtlDriveModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 4), VtlDriveModelTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveModel.setStatus('current')
if mibBuilder.loadTexts: vtlDriveModel.setDescription('VTL drive model')
vtlDriveRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 5), VtlDriveRevisionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveRevision.setStatus('current')
if mibBuilder.loadTexts: vtlDriveRevision.setDescription('VTL drive revision')
vtlDriveSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 6), VtlDriveSerialTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveSerial.setStatus('current')
if mibBuilder.loadTexts: vtlDriveSerial.setDescription('VTL drive serial')
vtlDriveLibraryName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 7), VtlLibraryNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveLibraryName.setStatus('current')
if mibBuilder.loadTexts: vtlDriveLibraryName.setDescription('VTL drive library name')
vtlDriveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 8), VtlDriveStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveStatus.setStatus('current')
if mibBuilder.loadTexts: vtlDriveStatus.setDescription('VTL drive status')
vtlDriveTapeVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 9), VtlDriveTapeVolumeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveTapeVolume.setStatus('current')
if mibBuilder.loadTexts: vtlDriveTapeVolume.setDescription('VTL drive tape volume')
vtlGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7))
vtlGroupTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1), )
if mibBuilder.loadTexts: vtlGroupTable.setStatus('current')
if mibBuilder.loadTexts: vtlGroupTable.setDescription('A table containing entries of VtlGroupEntry.')
vtlGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlGroupIndex"))
if mibBuilder.loadTexts: vtlGroupEntry.setStatus('current')
if mibBuilder.loadTexts: vtlGroupEntry.setDescription('vtlGroupTable Row Description')
vtlGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: vtlGroupIndex.setStatus('current')
if mibBuilder.loadTexts: vtlGroupIndex.setDescription('VTL Group index')
vtlGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupName.setStatus('current')
if mibBuilder.loadTexts: vtlGroupName.setDescription('VTL Group Name')
vtlGroupInitiaterCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupInitiaterCount.setStatus('current')
if mibBuilder.loadTexts: vtlGroupInitiaterCount.setDescription('VTL Group Initiater Count')
vtlGroupDeviceCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceCount.setStatus('current')
if mibBuilder.loadTexts: vtlGroupDeviceCount.setDescription('VTL Group Device Count')
vtlGroupDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2), )
if mibBuilder.loadTexts: vtlGroupDeviceTable.setStatus('current')
if mibBuilder.loadTexts: vtlGroupDeviceTable.setDescription('This table contains information about the devices in VTL groups.\n            It provides information such as the Device Name, the Device LUN,\n            the Primary Ports, Secondary Ports, In-Use Ports, and Group Name.\n            It is comprised of entries of VtlGroupDeviceEntry.')
vtlGroupDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlGroupIndex"), (0, "DATA-DOMAIN-MIB", "vtlGroupDeviceIndex"))
if mibBuilder.loadTexts: vtlGroupDeviceEntry.setStatus('current')
if mibBuilder.loadTexts: vtlGroupDeviceEntry.setDescription('Information about the devices in a VTL group.')
vtlGroupDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 2), DDMibTableIndexTC())
if mibBuilder.loadTexts: vtlGroupDeviceIndex.setStatus('current')
if mibBuilder.loadTexts: vtlGroupDeviceIndex.setDescription('The index of a VTL Device.')
vtlGroupDeviceGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 3), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceGroupName.setStatus('current')
if mibBuilder.loadTexts: vtlGroupDeviceGroupName.setDescription('The name of a VTL Group.')
vtlGroupDeviceDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 4), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceDeviceName.setStatus('current')
if mibBuilder.loadTexts: vtlGroupDeviceDeviceName.setDescription('The name of a VTL Device.')
vtlGroupDeviceLun = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceLun.setStatus('current')
if mibBuilder.loadTexts: vtlGroupDeviceLun.setDescription('The LUN (Logical Unit Number) of a VTL Device.')
vtlGroupDevicePrimaryPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDevicePrimaryPorts.setStatus('current')
if mibBuilder.loadTexts: vtlGroupDevicePrimaryPorts.setDescription("The Primary Ports of a VTL Device. This entry specifies a set of\n            ports that the device will be visible on. If 'all' is provided the\n            device is visible on all ports. If 'none' is provided the device \n            is visible on none of the ports.")
vtlGroupDeviceSecondaryPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceSecondaryPorts.setStatus('current')
if mibBuilder.loadTexts: vtlGroupDeviceSecondaryPorts.setDescription('The Secondary Ports of a VTL Device. This entry specifies a second\n            set of ports that the device will be visible on. The administrator\n            can switch the ports in use in a group to the primary or secondary\n            port list.')
vtlGroupDeviceInUsePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 8), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceInUsePorts.setStatus('current')
if mibBuilder.loadTexts: vtlGroupDeviceInUsePorts.setDescription('The In-Use Ports of a VTL Device. The port list that the device is\n            visible on is the in-use port list, which can be the primary or\n            secondary port list.')
vtlInitiator = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8))
vtlInitiatorTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1), )
if mibBuilder.loadTexts: vtlInitiatorTable.setStatus('current')
if mibBuilder.loadTexts: vtlInitiatorTable.setDescription('A table containing entries of VtlInitiatorEntry.')
vtlInitiatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlInitiatorIndex"))
if mibBuilder.loadTexts: vtlInitiatorEntry.setStatus('current')
if mibBuilder.loadTexts: vtlInitiatorEntry.setDescription('vtlInitiatorTable Row Description')
vtlInitiatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: vtlInitiatorIndex.setStatus('current')
if mibBuilder.loadTexts: vtlInitiatorIndex.setDescription('VTL Initiator index')
vtlInitiatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorName.setStatus('current')
if mibBuilder.loadTexts: vtlInitiatorName.setDescription('VTL Initiator Name')
vtlInitiatorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 3), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorStatus.setStatus('current')
if mibBuilder.loadTexts: vtlInitiatorStatus.setDescription('VTL Initiator Status')
vtlInitiatorGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorGroup.setStatus('current')
if mibBuilder.loadTexts: vtlInitiatorGroup.setDescription('VTL Initiator Group')
vtlInitiatorWWNN = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 5), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorWWNN.setStatus('current')
if mibBuilder.loadTexts: vtlInitiatorWWNN.setDescription('VTL Initiator WWNN')
vtlInitiatorWWPN = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorWWPN.setStatus('current')
if mibBuilder.loadTexts: vtlInitiatorWWPN.setDescription('VTL Initiator WWPN')
vtlInitiatorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 7), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorPort.setStatus('current')
if mibBuilder.loadTexts: vtlInitiatorPort.setDescription('VTL Initiator Port')
vtlPool = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6))
vtlPoolTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1), )
if mibBuilder.loadTexts: vtlPoolTable.setStatus('current')
if mibBuilder.loadTexts: vtlPoolTable.setDescription('A table containing entries of VtlPoolEntry.')
vtlPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlPoolIndex"))
if mibBuilder.loadTexts: vtlPoolEntry.setStatus('current')
if mibBuilder.loadTexts: vtlPoolEntry.setDescription('vtlPoolTable Row Description')
vtlPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: vtlPoolIndex.setStatus('current')
if mibBuilder.loadTexts: vtlPoolIndex.setDescription('VTL Pool index')
vtlPoolPool = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolPool.setStatus('current')
if mibBuilder.loadTexts: vtlPoolPool.setDescription('VTL Pool Pool')
vtlPoolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolStatus.setStatus('current')
if mibBuilder.loadTexts: vtlPoolStatus.setDescription('VTL Pool Status')
vtlPoolTapes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 4), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolTapes.setStatus('current')
if mibBuilder.loadTexts: vtlPoolTapes.setDescription('VTL Pool Tapes')
vtlPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 5), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolSize.setStatus('current')
if mibBuilder.loadTexts: vtlPoolSize.setDescription('VTL Pool Size')
vtlPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolUsed.setStatus('current')
if mibBuilder.loadTexts: vtlPoolUsed.setDescription('VTL Pool Used')
vtlPoolComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolComp.setStatus('current')
if mibBuilder.loadTexts: vtlPoolComp.setDescription('VTL Pool Compression')
vtlPort = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3))
vtlPortTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1), )
if mibBuilder.loadTexts: vtlPortTable.setStatus('current')
if mibBuilder.loadTexts: vtlPortTable.setDescription('A table containing entries of VtlPortEntry.')
vtlPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlPortIndex"))
if mibBuilder.loadTexts: vtlPortEntry.setStatus('current')
if mibBuilder.loadTexts: vtlPortEntry.setDescription('vtlPortTable Row Description')
vtlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 1), VtlPortIndexTC())
if mibBuilder.loadTexts: vtlPortIndex.setStatus('current')
if mibBuilder.loadTexts: vtlPortIndex.setDescription('VTL Port index')
vtlPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 2), VtlPortNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortName.setStatus('current')
if mibBuilder.loadTexts: vtlPortName.setDescription('VTL Port name')
vtlPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 3), VtlPortIDTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortID.setStatus('current')
if mibBuilder.loadTexts: vtlPortID.setDescription('VTL Port ID')
vtlPortModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 4), VtlPortModelTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortModel.setStatus('current')
if mibBuilder.loadTexts: vtlPortModel.setDescription('VTL Port model')
vtlPortFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 5), VtlPortFirmwareTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortFirmware.setStatus('current')
if mibBuilder.loadTexts: vtlPortFirmware.setDescription('VTL Port Firmware Version')
vtlPortWWNN = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 6), VtlPortWWNNTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortWWNN.setStatus('current')
if mibBuilder.loadTexts: vtlPortWWNN.setDescription('VTL Port WWNN address')
vtlPortWWPN = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 7), VtlPortWWPNTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortWWPN.setStatus('current')
if mibBuilder.loadTexts: vtlPortWWPN.setDescription('VTL Port WWPN Address')
vtlPortConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 8), VtlPortConnectionTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortConnectionType.setStatus('current')
if mibBuilder.loadTexts: vtlPortConnectionType.setDescription('VTL Port Connection Type')
vtlPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 9), VtlPortSpeedTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortSpeed.setStatus('current')
if mibBuilder.loadTexts: vtlPortSpeed.setDescription('VTL Port Speed in Gibs')
vtlPortEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 10), VtlPortEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortEnabled.setStatus('current')
if mibBuilder.loadTexts: vtlPortEnabled.setDescription('VTL Port Enabled')
vtlPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 11), VtlPortStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortStatus.setStatus('current')
if mibBuilder.loadTexts: vtlPortStatus.setDescription('VTL Port Status')
vtlPortTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 12), VtlPortIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortTrapIndex.setStatus('current')
if mibBuilder.loadTexts: vtlPortTrapIndex.setDescription('VTL Port index')
vtlProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 1))
vtlAdminState = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 11, 1, 1), VtlAdminStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlAdminState.setStatus('current')
if mibBuilder.loadTexts: vtlAdminState.setDescription('State of VTL administration')
vtlProcessState = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 11, 1, 2), VtlProcessStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlProcessState.setStatus('current')
if mibBuilder.loadTexts: vtlProcessState.setDescription('State of VTL process')
vtlStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3))
vtlStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1), )
if mibBuilder.loadTexts: vtlStatsTable.setStatus('current')
if mibBuilder.loadTexts: vtlStatsTable.setDescription('This table contains detailed statistical information about the \n            individual VTL Ports on a Data Domain System. It includes the \n            count of Control Commands, Write Commands, and Read Commands. The\n            amount of data In, and Out. The count of Link Failures, LIP count,\n            Sync Losses, Signal Losses, Prim Seq Proto Errors, Invalid Tx \n            Words, and Invalid CRCs. It is comprised of entries of \n            VtlStatsEntry.')
vtlStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlStatsIndex"))
if mibBuilder.loadTexts: vtlStatsEntry.setStatus('current')
if mibBuilder.loadTexts: vtlStatsEntry.setDescription('vtlStatsTable Row Description')
vtlStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 1), VtlStatsIndexTC())
if mibBuilder.loadTexts: vtlStatsIndex.setStatus('current')
if mibBuilder.loadTexts: vtlStatsIndex.setDescription('VTL Stats Index. The index of the VTL Per-Port Statistical entry.')
vtlStatsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 2), VtlStatsPortTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsPort.setStatus('current')
if mibBuilder.loadTexts: vtlStatsPort.setDescription('VTL Stats Port. The physical VTL port number.')
vtlStatsConrolCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 3), VtlStatsConrolCommandsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsConrolCommands.setStatus('current')
if mibBuilder.loadTexts: vtlStatsConrolCommands.setDescription('VTL Stats Control Commands. The number of non read/write \n            commands.')
vtlStatsWriteCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 4), VtlStatsWriteCommandsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsWriteCommands.setStatus('current')
if mibBuilder.loadTexts: vtlStatsWriteCommands.setDescription('VTL Stats Write Commands. The number of WRITE commands.')
vtlStatsReadCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 5), VtlStatsReadCommandsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsReadCommands.setStatus('current')
if mibBuilder.loadTexts: vtlStatsReadCommands.setDescription('VTL Stats Read Commands. The number of READ commands.')
vtlStatsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 6), VtlStatsInTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsIn.setStatus('current')
if mibBuilder.loadTexts: vtlStatsIn.setDescription('VTL Stats In. The number of megabytes written to the specific \n            port.')
vtlStatsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 7), VtlStatsOutTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsOut.setStatus('current')
if mibBuilder.loadTexts: vtlStatsOut.setDescription('VTL Stats Out. The number of megabytes read from the specific\n            port.')
vtlStatsLinkFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 8), VtlStatsLinkFailuresTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsLinkFailures.setStatus('current')
if mibBuilder.loadTexts: vtlStatsLinkFailures.setDescription('VTL Stats Link Failures. The count of Link Failures.')
vtlStatsLIPCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 9), VtlStatsLIPCountTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsLIPCount.setStatus('current')
if mibBuilder.loadTexts: vtlStatsLIPCount.setDescription('VTL Stats LIP Count. The number of LIPs.')
vtlStatsSyncLosses = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 10), VtlStatsSyncLossesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsSyncLosses.setStatus('current')
if mibBuilder.loadTexts: vtlStatsSyncLosses.setDescription('VTL Stats Sync Losses. The number of times sync loss was \n            detected.')
vtlStatsSignalLosses = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 11), VtlStatsSignalLossesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsSignalLosses.setStatus('current')
if mibBuilder.loadTexts: vtlStatsSignalLosses.setDescription('VTL Stats Signal Losses. The number of times loss of signal was\n            detected.')
vtlStatsPrimSeqProtoErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 12), VtlStatsPrimSeqProtoErrorsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsPrimSeqProtoErrors.setStatus('current')
if mibBuilder.loadTexts: vtlStatsPrimSeqProtoErrors.setDescription('VTL Stats Prim Seq Proto Errors. The count of errors in the \n            Primitive Sequence Protocol.')
vtlStatsInvalidTxWords = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 13), VtlStatsInvalidTxWordsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsInvalidTxWords.setStatus('current')
if mibBuilder.loadTexts: vtlStatsInvalidTxWords.setDescription('VTL Stats Invalid Tx Words. The number of invalid TX words.')
vtlStatsInvalidCRCs = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 14), VtlStatsInvalidCRCsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsInvalidCRCs.setStatus('current')
if mibBuilder.loadTexts: vtlStatsInvalidCRCs.setDescription('VTL Stats Invalid CRCs. The number of frames received with bad \n            CRC.')
vtlTape = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4))
vtlTapeTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1), )
if mibBuilder.loadTexts: vtlTapeTable.setStatus('current')
if mibBuilder.loadTexts: vtlTapeTable.setDescription('A table containing entries of VtlTapeEntry.')
vtlTapeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlTapeIndex"))
if mibBuilder.loadTexts: vtlTapeEntry.setStatus('current')
if mibBuilder.loadTexts: vtlTapeEntry.setDescription('vtlTapeTable Row Description')
vtlTapeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 1), VtlTapeIndexTC())
if mibBuilder.loadTexts: vtlTapeIndex.setStatus('current')
if mibBuilder.loadTexts: vtlTapeIndex.setDescription('VTL Tape index')
vtlTapeBarCode = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 2), VtlTapeBarCodeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeBarCode.setStatus('current')
if mibBuilder.loadTexts: vtlTapeBarCode.setDescription('VTL Tape BarCode')
vtlTapePool = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 3), VtlTapePoolTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapePool.setStatus('current')
if mibBuilder.loadTexts: vtlTapePool.setDescription('VTL Tape Pool')
vtlTapeLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 4), VtlTapeLocationTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeLocation.setStatus('current')
if mibBuilder.loadTexts: vtlTapeLocation.setDescription('VTL Tape Location')
vtlTapeState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 5), VtlTapeStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeState.setStatus('current')
if mibBuilder.loadTexts: vtlTapeState.setDescription('VTL Tape State')
vtlTapeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 6), VtlTapeSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeSize.setStatus('current')
if mibBuilder.loadTexts: vtlTapeSize.setDescription('VTL Tape Size')
vtlTapeUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 7), VtlTapeUsedTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeUsed.setStatus('current')
if mibBuilder.loadTexts: vtlTapeUsed.setDescription('VTL Tape Used')
vtlTapeComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 8), VtlTapeCompTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeComp.setStatus('current')
if mibBuilder.loadTexts: vtlTapeComp.setDescription('VTL Tape Compression')
vtlTapeModTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 9), VtlTapeModTimeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeModTime.setStatus('current')
if mibBuilder.loadTexts: vtlTapeModTime.setDescription('VTL Tape status')
ddboostAccessClients = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8))
ddboostAccessClientsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1), )
if mibBuilder.loadTexts: ddboostAccessClientsTable.setStatus('current')
if mibBuilder.loadTexts: ddboostAccessClientsTable.setDescription('DDBOOST AccessClients table information for DDBOOST Access Client Configuration')
ddboostAccessClientsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostAccessClientsIndex"))
if mibBuilder.loadTexts: ddboostAccessClientsEntry.setStatus('current')
if mibBuilder.loadTexts: ddboostAccessClientsEntry.setDescription('ddboostAccessClientsTable Row Entry')
ddboostAccessClientsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostAccessClientsIndex.setStatus('current')
if mibBuilder.loadTexts: ddboostAccessClientsIndex.setDescription('ddboost AccessClients Table index')
ddboostAccessClientsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostAccessClientsName.setStatus('current')
if mibBuilder.loadTexts: ddboostAccessClientsName.setDescription('The DDboost Access clients Name')
ddboostAccessClientsEncryStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 3), DdboostAccessClientsEncryStrengthTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostAccessClientsEncryStrength.setStatus('current')
if mibBuilder.loadTexts: ddboostAccessClientsEncryStrength.setDescription('The encryption strength that the DDboost Access client is using, possible values are\n             none, medium and high')
ddboostAccessClientsAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 4), DdboostAccessClientsAuthModeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostAccessClientsAuthMode.setStatus('current')
if mibBuilder.loadTexts: ddboostAccessClientsAuthMode.setDescription('The Authentication mode that the DDboost Access client is using, possible values are\n             none, one-way, two-way and anonymous')
ddboostConnections = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3))
ddboostConnectionsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1), )
if mibBuilder.loadTexts: ddboostConnectionsTable.setStatus('current')
if mibBuilder.loadTexts: ddboostConnectionsTable.setDescription('DDBOOST connections table information for DDBOOST Client Connections')
ddboostConnectionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostConnectionsIndex"))
if mibBuilder.loadTexts: ddboostConnectionsEntry.setStatus('current')
if mibBuilder.loadTexts: ddboostConnectionsEntry.setDescription('ddboostConnectionsTable Row Entry')
ddboostConnectionsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostConnectionsIndex.setStatus('current')
if mibBuilder.loadTexts: ddboostConnectionsIndex.setDescription('ddboost connections Table index')
ddboostInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostInterface.setStatus('current')
if mibBuilder.loadTexts: ddboostInterface.setDescription('DDboost Interface Name')
ddboostifGroupMember = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 3), DDMibTableEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostifGroupMember.setStatus('current')
if mibBuilder.loadTexts: ddboostifGroupMember.setDescription('If Member of ifGroup')
ddboostBackupConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostBackupConnections.setStatus('current')
if mibBuilder.loadTexts: ddboostBackupConnections.setDescription('DDboost backup connections')
ddboostRestoreConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostRestoreConnections.setStatus('current')
if mibBuilder.loadTexts: ddboostRestoreConnections.setDescription('DDboost Restore connections')
ddboostControlConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 6), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostControlConnections.setStatus('current')
if mibBuilder.loadTexts: ddboostControlConnections.setDescription('DDboost control connections')
ddboostTotalConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 7), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostTotalConnections.setStatus('current')
if mibBuilder.loadTexts: ddboostTotalConnections.setDescription('DDboost Total connections')
ddboostFileReplicationHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6))
ddboostFileReplicationHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1), )
if mibBuilder.loadTexts: ddboostFileReplicationHistoryTable.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplicationHistoryTable.setDescription('DDBOOST FileReplicationHistory table contains information for File Replication History')
ddboostFileReplicationHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostFileReplHistoryIndex"))
if mibBuilder.loadTexts: ddboostFileReplicationHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplicationHistoryEntry.setDescription('ddboostFileReplicationHistoryTable Row Entry')
ddboostFileReplHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostFileReplHistoryIndex.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplHistoryIndex.setDescription('ddboost FileReplicationHistory Table index')
ddboostFileReplHistoryDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryDirection.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplHistoryDirection.setDescription('DDboost File ReplHistory History Direction')
ddboostFileReplHistoryNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 3), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryNetwork.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplHistoryNetwork.setDescription('DDBoost File Replication History Network KBytes Sent')
ddboostFileReplHistoryPreComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 4), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryPreComp.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplHistoryPreComp.setDescription('DDBoost File ReplHistory Pre Compressed Kbytes sent')
ddboostFileReplHistoryPostComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 5), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryPostComp.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplHistoryPostComp.setDescription('DDBoost File ReplHistory Post Compressed KBytes')
ddboostFileReplHistoryLowBWOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 6), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryLowBWOpt.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplHistoryLowBWOpt.setDescription('DDBoost File ReplHistory KBytes after Low Bandwidth optimization')
ddboostFileReplHistoryErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 7), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryErrors.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplHistoryErrors.setDescription('DDBoost File ReplHistory Errors')
ddboostFileReplHistoryDate = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 8), DDMibDateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryDate.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplHistoryDate.setDescription('DDboost File ReplHistory Date')
ddboostFileReplHistoryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 9), DDMibDateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryTime.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplHistoryTime.setDescription('DDboost File ReplHistory Time')
ddboostFileReplicationStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5))
ddboostFileReplicationStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1), )
if mibBuilder.loadTexts: ddboostFileReplicationStatsTable.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplicationStatsTable.setDescription('DDBOOST FileReplicationStats table contains information for File Replication Stats')
ddboostFileReplicationStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostFileReplStatsIndex"))
if mibBuilder.loadTexts: ddboostFileReplicationStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplicationStatsEntry.setDescription('ddboostFileReplicationStatsTable Row Entry')
ddboostFileReplStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostFileReplStatsIndex.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplStatsIndex.setDescription('ddboost FileReplicationStats Table index')
ddboostFileReplStatsDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsDirection.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplStatsDirection.setDescription('DDboost File Replication Direction')
ddboostFileReplStatsNetworkSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 3), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsNetworkSent.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplStatsNetworkSent.setDescription('DDBoost File Replication Network Bytes Sent')
ddboostFileReplStatsPreCompSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 4), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsPreCompSent.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplStatsPreCompSent.setDescription('DDBoost File Replication Pre Compressed bytes sent')
ddboostFileReplStatsFiltered = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 5), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsFiltered.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplStatsFiltered.setDescription('DDBoost File Replication Bytes after Filtering')
ddboostFileReplStatsLowBWOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 6), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsLowBWOpt.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplStatsLowBWOpt.setDescription('DDBoost File Replication Bytes after Low Bandwidth optimization')
ddboostFileReplStatsLocalComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 7), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsLocalComp.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplStatsLocalComp.setDescription('DDBoost File Replication Bytes after local compression')
ddboostFileReplStatsCompRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 8), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsCompRatio.setStatus('current')
if mibBuilder.loadTexts: ddboostFileReplStatsCompRatio.setDescription('DDboost File Replication Compressed Ratio')
ddboostFileReplicationPerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 10))
ddboostFileRepliPerfInPreCompKBPerSec = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 1), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileRepliPerfInPreCompKBPerSec.setStatus('current')
if mibBuilder.loadTexts: ddboostFileRepliPerfInPreCompKBPerSec.setDescription('DDBOOST File Replication Performance Inbound pre-comp kilobytes per second')
ddboostFileRepliPerfInNetworkKBPerSec = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 2), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileRepliPerfInNetworkKBPerSec.setStatus('current')
if mibBuilder.loadTexts: ddboostFileRepliPerfInNetworkKBPerSec.setDescription('DDBOOST File Replication Performance Inbound network kilobytes per second')
ddboostFileRepliPerfOutPreCompKBPerSec = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileRepliPerfOutPreCompKBPerSec.setStatus('current')
if mibBuilder.loadTexts: ddboostFileRepliPerfOutPreCompKBPerSec.setDescription('DDBOOST File Replication Performance Outbound pre-comp kilobytes per second')
ddboostFileRepliPerfOutNetworkKBPerSec = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileRepliPerfOutNetworkKBPerSec.setStatus('current')
if mibBuilder.loadTexts: ddboostFileRepliPerfOutNetworkKBPerSec.setDescription('DDBOOST File Replication Performance Outbound network kilobytes per second')
ddboostIfGroupConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 7))
ddboostIfGroupConfigTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1), )
if mibBuilder.loadTexts: ddboostIfGroupConfigTable.setStatus('current')
if mibBuilder.loadTexts: ddboostIfGroupConfigTable.setDescription('DDBOOST IfGroupConfig table information for DDBOOST ifGroup Configuration')
ddboostIfGroupConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostIfGroupConfigIndex"))
if mibBuilder.loadTexts: ddboostIfGroupConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ddboostIfGroupConfigEntry.setDescription('ddboostIfGroupConfigTable Row Entry')
ddboostIfGroupConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostIfGroupConfigIndex.setStatus('current')
if mibBuilder.loadTexts: ddboostIfGroupConfigIndex.setDescription('ddboost IfGroupConfig Table index')
ddboostIfGroupInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostIfGroupInterface.setStatus('current')
if mibBuilder.loadTexts: ddboostIfGroupInterface.setDescription('DDboost ifGroup Interface Name')
ddboostOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9))
ddboostOptionsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1), )
if mibBuilder.loadTexts: ddboostOptionsTable.setStatus('current')
if mibBuilder.loadTexts: ddboostOptionsTable.setDescription('DDBOOST Options table')
ddboostOptionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostOptionsIndex"))
if mibBuilder.loadTexts: ddboostOptionsEntry.setStatus('current')
if mibBuilder.loadTexts: ddboostOptionsEntry.setDescription('ddboostOptionsTable Row Entry')
ddboostOptionsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostOptionsIndex.setStatus('current')
if mibBuilder.loadTexts: ddboostOptionsIndex.setDescription('ddboost Option Table index')
ddboostOptionsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostOptionsName.setStatus('current')
if mibBuilder.loadTexts: ddboostOptionsName.setDescription('DDboost Option Value Name ')
ddboostOptionsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1, 3), DDMibStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostOptionsStatus.setStatus('current')
if mibBuilder.loadTexts: ddboostOptionsStatus.setDescription('DDboost Option Status Enabled/Disabled ')
ddboostProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1))
ddboostStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 1), DDboostStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatus.setStatus('current')
if mibBuilder.loadTexts: ddboostStatus.setDescription('The status of the DDBoost interface group on a DD system.')
ddboostUser = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 2), DDboostUserTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostUser.setStatus('deprecated')
if mibBuilder.loadTexts: ddboostUser.setDescription('DDBoost User.')
ddboostIfGroupStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 3), DDMibStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostIfGroupStatus.setStatus('deprecated')
if mibBuilder.loadTexts: ddboostIfGroupStatus.setDescription('DDBoost IfGroup Status.')
ddboostUserTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4), )
if mibBuilder.loadTexts: ddboostUserTable.setStatus('current')
if mibBuilder.loadTexts: ddboostUserTable.setDescription('This table contains information about DDBoost users.')
ddboostUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostUserIdx"))
if mibBuilder.loadTexts: ddboostUserEntry.setStatus('current')
if mibBuilder.loadTexts: ddboostUserEntry.setDescription('ddboostUserTable Row Entry.')
ddboostUserIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1, 1), DDboostStatsIndexTC())
if mibBuilder.loadTexts: ddboostUserIdx.setStatus('current')
if mibBuilder.loadTexts: ddboostUserIdx.setDescription('DDBoost users table index.')
ddboostUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostUserName.setStatus('current')
if mibBuilder.loadTexts: ddboostUserName.setDescription('The name of a Ddboost user.')
ddboostUserDefaultTenantUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1, 3), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostUserDefaultTenantUnit.setStatus('current')
if mibBuilder.loadTexts: ddboostUserDefaultTenantUnit.setDescription('The default tenant unit that is associated with a specific DDBoost user.')
ddboostIfGroupTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5), )
if mibBuilder.loadTexts: ddboostIfGroupTable.setStatus('current')
if mibBuilder.loadTexts: ddboostIfGroupTable.setDescription('DDBoost IfGroup table containing interface group information.')
ddboostIfGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostIfGroupIdx"))
if mibBuilder.loadTexts: ddboostIfGroupEntry.setStatus('current')
if mibBuilder.loadTexts: ddboostIfGroupEntry.setDescription('ddboostIfGroupTable Row Entry.')
ddboostIfGroupIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1, 1), DDboostStatsIndexTC())
if mibBuilder.loadTexts: ddboostIfGroupIdx.setStatus('current')
if mibBuilder.loadTexts: ddboostIfGroupIdx.setDescription('DDBoost IfGroup table index.')
ddboostIfGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostIfGroupName.setStatus('current')
if mibBuilder.loadTexts: ddboostIfGroupName.setDescription('The name of DDBoost IfGroup.')
ddboostIfGroupCurrentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1, 3), DDMibStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostIfGroupCurrentStatus.setStatus('current')
if mibBuilder.loadTexts: ddboostIfGroupCurrentStatus.setDescription("The status of a DDBoost IfGroup. Possible values are: 'enabled' or 'disabled'.")
ddboostStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2))
ddboostStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1), )
if mibBuilder.loadTexts: ddboostStatsTable.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsTable.setDescription('DDBOOST stats table containing byte statistics information for DDBOOST')
ddboostStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostStatsIndex"))
if mibBuilder.loadTexts: ddboostStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsEntry.setDescription('ddboostStatsTable Row Entry')
ddboostStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 1), DDboostStatsIndexTC())
if mibBuilder.loadTexts: ddboostStatsIndex.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsIndex.setDescription('ddboost Stats Table index')
ddboostPreCompKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 2), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostPreCompKBytesPerSecond.setStatus('current')
if mibBuilder.loadTexts: ddboostPreCompKBytesPerSecond.setDescription('Number of pre-compressed (logical) bytes received per second')
ddboostPostCompKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 3), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostPostCompKBytesPerSecond.setStatus('current')
if mibBuilder.loadTexts: ddboostPostCompKBytesPerSecond.setDescription('number of pddboost local compression bytes received per second')
ddboostNetworkKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 4), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostNetworkKBytesPerSecond.setStatus('current')
if mibBuilder.loadTexts: ddboostNetworkKBytesPerSecond.setDescription('Number of physical network bytes received per second')
ddboostReadKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 5), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostReadKBytesPerSecond.setStatus('current')
if mibBuilder.loadTexts: ddboostReadKBytesPerSecond.setDescription('Number of bytes read per second')
ddboostStatsBackupConn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsBackupConn.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsBackupConn.setDescription('Number of backup connections')
ddboostStatsRestoreConn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsRestoreConn.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsRestoreConn.setDescription('Number of restore connections')
ddboostStatsImageCreatesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsImageCreatesCount.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsImageCreatesCount.setDescription('Number of image creates')
ddboostStatsImageCreatesErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsImageCreatesErrors.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsImageCreatesErrors.setDescription('Number of image creates errors')
ddboostStatsImageDeletesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsImageDeletesCount.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsImageDeletesCount.setDescription('Number of image deletes')
ddboostStatsImageDeletesErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsImageDeletesErrors.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsImageDeletesErrors.setDescription('Number of image deletes errors')
ddboostStatsPrecompBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 12), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsPrecompBytesReceived.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsPrecompBytesReceived.setDescription('Number of pre-compressed (logical) bytes received')
ddboostStatsBytesAfterFiltering = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 13), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsBytesAfterFiltering.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsBytesAfterFiltering.setDescription('Number of bytes after filtering')
ddboostStatsBytesAfterLc = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 14), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsBytesAfterLc.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsBytesAfterLc.setDescription('Number of bytes after local compression')
ddboostStatsNetworkBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 15), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsNetworkBytesReceived.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsNetworkBytesReceived.setDescription('Number of network bytes received')
ddboostStatsCompressionRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 16), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsCompressionRatio.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsCompressionRatio.setDescription('Compression ratio')
ddboostStatsTotalBytesReadCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 17), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsTotalBytesReadCount.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsTotalBytesReadCount.setDescription('Total bytes read count')
ddboostStatsTotalBytesReadErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 18), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsTotalBytesReadErrors.setStatus('current')
if mibBuilder.loadTexts: ddboostStatsTotalBytesReadErrors.setDescription('Total bytes read errors')
ddboostStorageUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4))
ddboostStorageUnitTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1), )
if mibBuilder.loadTexts: ddboostStorageUnitTable.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitTable.setDescription('DDBOOST StorageUnit table information for DDBOOST Storage Units')
ddboostStorageUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostStorageUnitIndex"))
if mibBuilder.loadTexts: ddboostStorageUnitEntry.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitEntry.setDescription('ddboostStorageUnitTable Row Entry')
ddboostStorageUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostStorageUnitIndex.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitIndex.setDescription('ddboost StorageUnit Table index')
ddboostStorageUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitName.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitName.setDescription('DDboost Storage Unit Name')
ddboostStorageUnitBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitBytes.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitBytes.setDescription('DDboost Storage Unit Original MiB.')
ddboostStorageUnitGlobalComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitGlobalComp.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitGlobalComp.setDescription('DDboost Storage Unit Globally Compressed MiB.')
ddboostStorageUnitLocalComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitLocalComp.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitLocalComp.setDescription('DDboost Storage Unit Locally Compressed MiB.')
ddboostStorageUnitMetaData = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 6), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitMetaData.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitMetaData.setDescription('DDboost Storage Unit Meta Data MiB.')
ddboostStorageUnitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitStatus.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitStatus.setDescription('DDboost Storage Unit Status.')
ddboostStorageUnitPreComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 8), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitPreComp.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitPreComp.setDescription('DDboost Storage Unit Pre-Compression Rate.')
ddboostStorageUnitUser = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 9), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitUser.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitUser.setDescription('The User of the DDboost Storage Unit.')
ddboostStorageUnitReportPhysicalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 10), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitReportPhysicalSize.setStatus('current')
if mibBuilder.loadTexts: ddboostStorageUnitReportPhysicalSize.setDescription('DDboost Storage Unit Report Physical Size.')
systemLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4))
systemLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1), )
if mibBuilder.loadTexts: systemLicenseTable.setStatus('current')
if mibBuilder.loadTexts: systemLicenseTable.setDescription('A table containing entries of SystemLicenseEntry.')
systemLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemLicenseIndex"))
if mibBuilder.loadTexts: systemLicenseEntry.setStatus('current')
if mibBuilder.loadTexts: systemLicenseEntry.setDescription('systemLicenseTable Row Description')
systemLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemLicenseIndex.setStatus('current')
if mibBuilder.loadTexts: systemLicenseIndex.setDescription('System License Row index')
systemLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemLicenseKey.setStatus('current')
if mibBuilder.loadTexts: systemLicenseKey.setDescription('System License Key')
systemLicenseFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemLicenseFeature.setStatus('current')
if mibBuilder.loadTexts: systemLicenseFeature.setDescription('Feature for the license')
systemCapacityLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2))
systemCapacityLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1), )
if mibBuilder.loadTexts: systemCapacityLicenseTable.setStatus('current')
if mibBuilder.loadTexts: systemCapacityLicenseTable.setDescription('A table containing entries of systemCapacityLicenseEntry.')
systemCapacityLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemCapacityLicenseIndex"))
if mibBuilder.loadTexts: systemCapacityLicenseEntry.setStatus('current')
if mibBuilder.loadTexts: systemCapacityLicenseEntry.setDescription('systemCapacityLicenseTable Row Description')
systemCapacityLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemCapacityLicenseIndex.setStatus('current')
if mibBuilder.loadTexts: systemCapacityLicenseIndex.setDescription('systemCapacity License Row index')
systemCapacityLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemCapacityLicenseKey.setStatus('current')
if mibBuilder.loadTexts: systemCapacityLicenseKey.setDescription('systemCapacity License Key')
systemCapacityLicenseFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemCapacityLicenseFeature.setStatus('current')
if mibBuilder.loadTexts: systemCapacityLicenseFeature.setDescription('Capacity Feature for the license')
systemCapacityLicenseModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemCapacityLicenseModel.setStatus('current')
if mibBuilder.loadTexts: systemCapacityLicenseModel.setDescription('Model for Feature of the license')
systemCapacityLicenseCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemCapacityLicenseCapacity.setStatus('current')
if mibBuilder.loadTexts: systemCapacityLicenseCapacity.setDescription('Capacity of the model')
systemHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2))
systemHardwareTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1), )
if mibBuilder.loadTexts: systemHardwareTable.setStatus('current')
if mibBuilder.loadTexts: systemHardwareTable.setDescription('A table containing entries of SystemHardwareEntry.')
systemHardwareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemHardwareIndex"))
if mibBuilder.loadTexts: systemHardwareEntry.setStatus('current')
if mibBuilder.loadTexts: systemHardwareEntry.setDescription('systemHardwareTable Row Description')
systemHardwareIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemHardwareIndex.setStatus('current')
if mibBuilder.loadTexts: systemHardwareIndex.setDescription('System Hardware Row index')
systemHardwareSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 2), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwareSlot.setStatus('deprecated')
if mibBuilder.loadTexts: systemHardwareSlot.setDescription('System Hardware Slot')
systemHardwareVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwareVendor.setStatus('current')
if mibBuilder.loadTexts: systemHardwareVendor.setDescription('Slot Device Vendor')
systemHardwareDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 4), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwareDevice.setStatus('current')
if mibBuilder.loadTexts: systemHardwareDevice.setDescription('Slot Device')
systemHardwarePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 5), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwarePorts.setStatus('current')
if mibBuilder.loadTexts: systemHardwarePorts.setDescription('Slot Ports')
systemHardwareSlotName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwareSlotName.setStatus('current')
if mibBuilder.loadTexts: systemHardwareSlotName.setDescription('System Hardware Slot Name')
systemPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3))
systemPortsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1), )
if mibBuilder.loadTexts: systemPortsTable.setStatus('current')
if mibBuilder.loadTexts: systemPortsTable.setDescription('A table containing entries of SystemPortsEntry.')
systemPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemPortsIndex"))
if mibBuilder.loadTexts: systemPortsEntry.setStatus('current')
if mibBuilder.loadTexts: systemPortsEntry.setDescription('systemPortsTable Row Description')
systemPortsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemPortsIndex.setStatus('current')
if mibBuilder.loadTexts: systemPortsIndex.setDescription('System Ports Row index')
systemPortsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemPortsPort.setStatus('current')
if mibBuilder.loadTexts: systemPortsPort.setDescription('System Ports Port name')
systemPortsConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemPortsConnectionType.setStatus('current')
if mibBuilder.loadTexts: systemPortsConnectionType.setDescription('Port LinkSpeed ConnectionType')
systemPortsLinkSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 4), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemPortsLinkSpeed.setStatus('current')
if mibBuilder.loadTexts: systemPortsLinkSpeed.setDescription('system Port LinkSpeed')
systemPortsFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 5), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemPortsFirmware.setStatus('current')
if mibBuilder.loadTexts: systemPortsFirmware.setDescription('system ports firmware version')
systemPortsHardwareAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemPortsHardwareAddress.setStatus('current')
if mibBuilder.loadTexts: systemPortsHardwareAddress.setDescription('System Port Hardware Address.')
systemProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1))
systemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 1), SystemSerialNumberTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSerialNumber.setStatus('current')
if mibBuilder.loadTexts: systemSerialNumber.setDescription('Serial Number of the System')
systemCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 2), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemCurrentTime.setStatus('current')
if mibBuilder.loadTexts: systemCurrentTime.setDescription("DDR system's current time")
systemVersion = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 3), DDMibVersionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemVersion.setStatus('current')
if mibBuilder.loadTexts: systemVersion.setDescription('DD Version of the System')
systemModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 4), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemModelNumber.setStatus('current')
if mibBuilder.loadTexts: systemModelNumber.setDescription('Model Number of the System')
systemTimeZoneName = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 5), SystemTimeZoneNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTimeZoneName.setStatus('current')
if mibBuilder.loadTexts: systemTimeZoneName.setDescription("DDR system's time zone name")
sysNotes = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 6), SystemNotesTC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNotes.setStatus('current')
if mibBuilder.loadTexts: sysNotes.setDescription('Customer defined notes associated with this DD System.')
systemUser = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5))
systemUserTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1), )
if mibBuilder.loadTexts: systemUserTable.setStatus('current')
if mibBuilder.loadTexts: systemUserTable.setDescription('A table containing entries of SystemUsers.')
systemUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemUserIndex"))
if mibBuilder.loadTexts: systemUserEntry.setStatus('current')
if mibBuilder.loadTexts: systemUserEntry.setDescription('SystemUserTable Row Description')
systemUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemUserIndex.setStatus('current')
if mibBuilder.loadTexts: systemUserIndex.setDescription('SystemUser Row index')
systemUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 2), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUserName.setStatus('current')
if mibBuilder.loadTexts: systemUserName.setDescription('SystemUser Name ')
systemUserUID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUserUID.setStatus('current')
if mibBuilder.loadTexts: systemUserUID.setDescription('SystemUser UID')
systemUserRole = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUserRole.setStatus('current')
if mibBuilder.loadTexts: systemUserRole.setDescription('SystemUser Role')
systemUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUserStatus.setStatus('current')
if mibBuilder.loadTexts: systemUserStatus.setDescription('SystemUsers Status ')
systemActiveUserTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2), )
if mibBuilder.loadTexts: systemActiveUserTable.setStatus('current')
if mibBuilder.loadTexts: systemActiveUserTable.setDescription('A table containing entries of SystemActiveUsers.')
systemActiveUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemActiveUserIndex"))
if mibBuilder.loadTexts: systemActiveUserEntry.setStatus('current')
if mibBuilder.loadTexts: systemActiveUserEntry.setDescription('SystemActiveUserTable Row Description')
systemActiveUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemActiveUserIndex.setStatus('current')
if mibBuilder.loadTexts: systemActiveUserIndex.setDescription('SystemActiveUser Row index')
systemActiveUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 2), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemActiveUserName.setStatus('current')
if mibBuilder.loadTexts: systemActiveUserName.setDescription('SystemActiveUser Name ')
systemActiveUserIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 3), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemActiveUserIdleTime.setStatus('current')
if mibBuilder.loadTexts: systemActiveUserIdleTime.setDescription('SystemActiveUser idle time')
systemActiveUserLoginTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemActiveUserLoginTime.setStatus('current')
if mibBuilder.loadTexts: systemActiveUserLoginTime.setDescription('SystemActiveUser login time')
systemActiveUserLoginFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemActiveUserLoginFrom.setStatus('current')
if mibBuilder.loadTexts: systemActiveUserLoginFrom.setDescription('SystemActiveUser login from')
systemActiveUserTty = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 6), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemActiveUserTty.setStatus('current')
if mibBuilder.loadTexts: systemActiveUserTty.setDescription('SystemActiveUsers Tty')
taskHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2))
taskHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1), )
if mibBuilder.loadTexts: taskHistoryTable.setStatus('current')
if mibBuilder.loadTexts: taskHistoryTable.setDescription('A table containing entries of TaskHistoryEntry.')
taskHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "taskHistoryIndex"))
if mibBuilder.loadTexts: taskHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: taskHistoryEntry.setDescription('taskHistoryEntry Row Description')
taskHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: taskHistoryIndex.setStatus('current')
if mibBuilder.loadTexts: taskHistoryIndex.setDescription('Task History Row index')
taskHistoryUser = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryUser.setStatus('current')
if mibBuilder.loadTexts: taskHistoryUser.setDescription('Task History User')
taskHistoryID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryID.setStatus('current')
if mibBuilder.loadTexts: taskHistoryID.setDescription('Task History ID')
taskHistoryParent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 4), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryParent.setStatus('current')
if mibBuilder.loadTexts: taskHistoryParent.setDescription('Task History Parent')
taskHistoryName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 5), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryName.setStatus('current')
if mibBuilder.loadTexts: taskHistoryName.setDescription('Task History Name')
taskHistoryState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryState.setStatus('current')
if mibBuilder.loadTexts: taskHistoryState.setDescription('Task History State')
taskHistoryStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryStartTime.setStatus('current')
if mibBuilder.loadTexts: taskHistoryStartTime.setDescription('Task History Start Time')
taskHistoryDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 8), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryDuration.setStatus('current')
if mibBuilder.loadTexts: taskHistoryDuration.setDescription('Task History Duration')
taskActive = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3))
taskActiveTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1), )
if mibBuilder.loadTexts: taskActiveTable.setStatus('current')
if mibBuilder.loadTexts: taskActiveTable.setDescription('A table containing entries of TaskActiveEntry.')
taskActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "taskActiveIndex"))
if mibBuilder.loadTexts: taskActiveEntry.setStatus('current')
if mibBuilder.loadTexts: taskActiveEntry.setDescription('taskActiveEntry Row Description')
taskActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: taskActiveIndex.setStatus('current')
if mibBuilder.loadTexts: taskActiveIndex.setDescription('Task Active Row index')
taskActiveUser = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveUser.setStatus('current')
if mibBuilder.loadTexts: taskActiveUser.setDescription('Task Active User')
taskActiveID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveID.setStatus('current')
if mibBuilder.loadTexts: taskActiveID.setDescription('Task Active ID')
taskActiveParent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 4), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveParent.setStatus('current')
if mibBuilder.loadTexts: taskActiveParent.setDescription('Task Active Parent')
taskActiveName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 5), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveName.setStatus('current')
if mibBuilder.loadTexts: taskActiveName.setDescription('Task Active Name')
taskActiveState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveState.setStatus('current')
if mibBuilder.loadTexts: taskActiveState.setDescription('Task Active State')
taskActiveStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveStartTime.setStatus('current')
if mibBuilder.loadTexts: taskActiveStartTime.setDescription('Task Active Start Time')
taskActiveDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 8), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveDuration.setStatus('current')
if mibBuilder.loadTexts: taskActiveDuration.setDescription('Task Active Duration')
artConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1))
artConfigTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1), )
if mibBuilder.loadTexts: artConfigTable.setStatus('current')
if mibBuilder.loadTexts: artConfigTable.setDescription('A table containing entries of artConfigEntry.')
artConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "artConfigIndex"))
if mibBuilder.loadTexts: artConfigEntry.setStatus('current')
if mibBuilder.loadTexts: artConfigEntry.setDescription('artConfigTable Row Description')
artConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: artConfigIndex.setStatus('current')
if mibBuilder.loadTexts: artConfigIndex.setDescription('art Config index')
artConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 2), DDMibTableEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artConfigStatus.setStatus('current')
if mibBuilder.loadTexts: artConfigStatus.setDescription('art Config Status')
artConfigMigrationSchedule = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 3), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artConfigMigrationSchedule.setStatus('current')
if mibBuilder.loadTexts: artConfigMigrationSchedule.setDescription('art Config Migration Schedule')
artConfigDefaultAge = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artConfigDefaultAge.setStatus('current')
if mibBuilder.loadTexts: artConfigDefaultAge.setDescription('art Config Default Age threshold migration policy')
artConfigFileSystemClean = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 5), DDMibTableEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artConfigFileSystemClean.setStatus('current')
if mibBuilder.loadTexts: artConfigFileSystemClean.setDescription('art Config file System Clean Required')
artConfigCompression = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 6), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artConfigCompression.setStatus('current')
if mibBuilder.loadTexts: artConfigCompression.setDescription('art Config local compression')
artMigrationPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3))
artMigrationPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1), )
if mibBuilder.loadTexts: artMigrationPolicyTable.setStatus('current')
if mibBuilder.loadTexts: artMigrationPolicyTable.setDescription('A table containing entries of artMigrationPolicyEntry.')
artMigrationPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "artMigrationPolicyIndex"))
if mibBuilder.loadTexts: artMigrationPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: artMigrationPolicyEntry.setDescription('artMigrationPolicyTable Row Description')
artMigrationPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: artMigrationPolicyIndex.setStatus('current')
if mibBuilder.loadTexts: artMigrationPolicyIndex.setDescription('art MigrationPolicy index')
artMigrationPolicyMtreeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artMigrationPolicyMtreeName.setStatus('current')
if mibBuilder.loadTexts: artMigrationPolicyMtreeName.setDescription('art MigrationPolicy Mtree Name')
artMigrationPolicyDefaultAge = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artMigrationPolicyDefaultAge.setStatus('current')
if mibBuilder.loadTexts: artMigrationPolicyDefaultAge.setDescription('art MigrationPolicy Default Age')
artMigrationSchedule = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2))
artMigrationScheduleTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1), )
if mibBuilder.loadTexts: artMigrationScheduleTable.setStatus('current')
if mibBuilder.loadTexts: artMigrationScheduleTable.setDescription('A table containing entries of artMigrationScheduleEntry.')
artMigrationScheduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "artMigrationScheduleIndex"))
if mibBuilder.loadTexts: artMigrationScheduleEntry.setStatus('current')
if mibBuilder.loadTexts: artMigrationScheduleEntry.setDescription('artMigrationScheduleTable Row Description')
artMigrationScheduleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: artMigrationScheduleIndex.setStatus('current')
if mibBuilder.loadTexts: artMigrationScheduleIndex.setDescription('art MigrationScheduleindex')
artMigrationScheduleSchedule = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artMigrationScheduleSchedule.setStatus('current')
if mibBuilder.loadTexts: artMigrationScheduleSchedule.setDescription('art MigrationSchedule Schedule')
artMigrationScheduleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1, 3), DDMibStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artMigrationScheduleStatus.setStatus('current')
if mibBuilder.loadTexts: artMigrationScheduleStatus.setDescription('art MigrationSchedule Status')
mtreeCompression = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1))
mtreeCompressionTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1), )
if mibBuilder.loadTexts: mtreeCompressionTable.setStatus('current')
if mibBuilder.loadTexts: mtreeCompressionTable.setDescription('A table containing entries of mtreeCompressionEntry.')
mtreeCompressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "mtreeCompressionIndex"))
if mibBuilder.loadTexts: mtreeCompressionEntry.setStatus('current')
if mibBuilder.loadTexts: mtreeCompressionEntry.setDescription('mtreeCompressionTable Row Description')
mtreeCompressionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: mtreeCompressionIndex.setStatus('current')
if mibBuilder.loadTexts: mtreeCompressionIndex.setDescription('mtree Compression index')
mtreeCompressionMtreePath = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionMtreePath.setStatus('current')
if mibBuilder.loadTexts: mtreeCompressionMtreePath.setDescription('mtree Compression Mtree Path')
mtreeCompressionPreCompGib = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 3), DDMibTableSizeGibTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionPreCompGib.setStatus('current')
if mibBuilder.loadTexts: mtreeCompressionPreCompGib.setDescription('mtree Compression Pre comp giga bytes')
mtreeCompressionPostCompGib = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 4), DDMibTableSizeGibTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionPostCompGib.setStatus('current')
if mibBuilder.loadTexts: mtreeCompressionPostCompGib.setDescription('mtree Compression Post Comp Giga Bytes')
mtreeCompressionGlobalCompFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 5), DDMibCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionGlobalCompFactor.setStatus('current')
if mibBuilder.loadTexts: mtreeCompressionGlobalCompFactor.setDescription('mtree Compression Global Comp Factor')
mtreeCompressionLocalCompFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 6), DDMibCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionLocalCompFactor.setStatus('current')
if mibBuilder.loadTexts: mtreeCompressionLocalCompFactor.setDescription('mtree Compression Local Comp Factor')
mtreeCompressionPostTotalCompFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 7), DDMibCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionPostTotalCompFactor.setStatus('current')
if mibBuilder.loadTexts: mtreeCompressionPostTotalCompFactor.setDescription('mtree Compression Total Comp Factor')
mtreeCompressionTimePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 8), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionTimePeriod.setStatus('current')
if mibBuilder.loadTexts: mtreeCompressionTimePeriod.setDescription('mtree Compression Time Period')
mtreeList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2))
mtreeListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1), )
if mibBuilder.loadTexts: mtreeListTable.setStatus('current')
if mibBuilder.loadTexts: mtreeListTable.setDescription('A table containing entries of mtreeListEntry.')
mtreeListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "mtreeListIndex"))
if mibBuilder.loadTexts: mtreeListEntry.setStatus('current')
if mibBuilder.loadTexts: mtreeListEntry.setDescription('mtreeListTable Row Description')
mtreeListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: mtreeListIndex.setStatus('current')
if mibBuilder.loadTexts: mtreeListIndex.setDescription('mtree List index')
mtreeListMtreeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeListMtreeName.setStatus('current')
if mibBuilder.loadTexts: mtreeListMtreeName.setDescription('mtree List Mtree Name')
mtreeListPreCompGib = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 3), DDMibTableSizeGibTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeListPreCompGib.setStatus('current')
if mibBuilder.loadTexts: mtreeListPreCompGib.setDescription('mtree List Pre comp giga bytes')
mtreeListStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 4), MtreeListStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeListStatus.setStatus('current')
if mibBuilder.loadTexts: mtreeListStatus.setDescription('mtree List Status')
mtreeRetentionLock = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4))
mtreeRetentionLockTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1), )
if mibBuilder.loadTexts: mtreeRetentionLockTable.setStatus('current')
if mibBuilder.loadTexts: mtreeRetentionLockTable.setDescription('A table containing entries of mtreeRetentionLockEntry.')
mtreeRetentionLockEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "mtreeRetentionLockIndex"))
if mibBuilder.loadTexts: mtreeRetentionLockEntry.setStatus('current')
if mibBuilder.loadTexts: mtreeRetentionLockEntry.setDescription('mtreeRetentionLockTable Row Description')
mtreeRetentionLockIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: mtreeRetentionLockIndex.setStatus('current')
if mibBuilder.loadTexts: mtreeRetentionLockIndex.setDescription('mtree RetentionLock index')
mtreeRetentionLockMtreeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeRetentionLockMtreeName.setStatus('current')
if mibBuilder.loadTexts: mtreeRetentionLockMtreeName.setDescription('mtree RetentionLock Mtree Name')
mtreeRetentionLockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 3), MtreeRetentionLockStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeRetentionLockStatus.setStatus('current')
if mibBuilder.loadTexts: mtreeRetentionLockStatus.setDescription('mtree RetentionLock Status')
mtreeRetentionLockUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeRetentionLockUUID.setStatus('current')
if mibBuilder.loadTexts: mtreeRetentionLockUUID.setDescription('mtree RetentionLock UUID')
mtreeRetentionLockMinRetentionPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeRetentionLockMinRetentionPeriod.setStatus('current')
if mibBuilder.loadTexts: mtreeRetentionLockMinRetentionPeriod.setDescription('mtree RetentionLock Minimum Retention Period')
mtreeRetentionLockMaxRetentionPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 6), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeRetentionLockMaxRetentionPeriod.setStatus('current')
if mibBuilder.loadTexts: mtreeRetentionLockMaxRetentionPeriod.setDescription('mtree RetentionLock Maximum Retention Period')
enclosureList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1))
enclosureListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1), )
if mibBuilder.loadTexts: enclosureListTable.setStatus('current')
if mibBuilder.loadTexts: enclosureListTable.setDescription('A table containing entries of EnclosureListEntry.')
enclosureListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "enclosureListIndex"))
if mibBuilder.loadTexts: enclosureListEntry.setStatus('current')
if mibBuilder.loadTexts: enclosureListEntry.setDescription('enclosure List Row Description')
enclosureListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: enclosureListIndex.setStatus('current')
if mibBuilder.loadTexts: enclosureListIndex.setDescription('enclosure List Row index')
enclosureListNum = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 2), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListNum.setStatus('current')
if mibBuilder.loadTexts: enclosureListNum.setDescription('enclosure Number')
enclosureListModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListModel.setStatus('current')
if mibBuilder.loadTexts: enclosureListModel.setDescription('enclosure model')
enclosureListSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 4), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListSerialNum.setStatus('current')
if mibBuilder.loadTexts: enclosureListSerialNum.setDescription('enclosure serial number')
enclosureListOemName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 5), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListOemName.setStatus('current')
if mibBuilder.loadTexts: enclosureListOemName.setDescription('enclosure oem name')
enclosureListOemValue = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 6), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListOemValue.setStatus('current')
if mibBuilder.loadTexts: enclosureListOemValue.setDescription('enclosure oem value')
enclosureListCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListCapacity.setStatus('current')
if mibBuilder.loadTexts: enclosureListCapacity.setDescription('enclosure Capacity')
enclosurePack = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 17, 2))
enclosurePackTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 17, 2, 1), )
if mibBuilder.loadTexts: enclosurePackTable.setStatus('current')
if mibBuilder.loadTexts: enclosurePackTable.setDescription('A table containing entries of EnclosurePackEntry.')
enclosurePackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 17, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "enclosureListIndex"), (0, "DATA-DOMAIN-MIB", "enclosurePackID"))
if mibBuilder.loadTexts: enclosurePackEntry.setStatus('current')
if mibBuilder.loadTexts: enclosurePackEntry.setDescription('enclosure Pack Row Description')
enclosurePackID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 2, 1, 1, 1), DDMibTableIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosurePackID.setStatus('current')
if mibBuilder.loadTexts: enclosurePackID.setDescription('Pack information for the enclosure.\n\t    Applicable to enclosures with packs such as ES60, and not for ES20 or ES30.')
restorer = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1))
unknown = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 0))
dd200 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 1))
dd200Proto = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 2))
dd410 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 3))
dd430 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 4))
dd460 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 5))
dd400g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 6))
dd460g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 7))
dd560 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 8))
dd560g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 9))
dd580 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 10))
dd580g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 11))
dd565 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 12))
dd530 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 13))
dd510 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 14))
dd120 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 15))
dd690 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 16))
dd690g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 17))
dd660 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 18))
dd880 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 19))
dd880g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 20))
dd610 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 21))
dd630 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 22))
dd140 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 23))
dd670 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 24))
dd860 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 25))
dd860g = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 26))
dd890 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 27))
dd640 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 28))
dd620 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 29))
dd160 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 30))
ddintrepid = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 31))
dd4500 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 32))
dd7200 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 33))
ddve = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 34))
dd990 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 35))
dd2500 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 36))
dd4200 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 37))
ddkoalam1 = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 38))
apollo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 39))
unset = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 3, 1, 9999))
dns = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 18, 1))
dnsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 18, 1, 1), )
if mibBuilder.loadTexts: dnsTable.setStatus('current')
if mibBuilder.loadTexts: dnsTable.setDescription('A table containing entries of dnsEntry.')
dnsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 18, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "dnsIndex"))
if mibBuilder.loadTexts: dnsEntry.setStatus('current')
if mibBuilder.loadTexts: dnsEntry.setDescription('DNS Table Row Description')
dnsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 1, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: dnsIndex.setStatus('current')
if mibBuilder.loadTexts: dnsIndex.setDescription('DNS Table Row index')
dnsServer = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 1, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServer.setStatus('current')
if mibBuilder.loadTexts: dnsServer.setDescription('DNS Server')
searchDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 18, 2))
searchDomainsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1), )
if mibBuilder.loadTexts: searchDomainsTable.setStatus('current')
if mibBuilder.loadTexts: searchDomainsTable.setDescription('A table containing entries of searchDomainsEntry.')
searchDomainsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "searchDomainsIndex"))
if mibBuilder.loadTexts: searchDomainsEntry.setStatus('current')
if mibBuilder.loadTexts: searchDomainsEntry.setDescription('searchDomains Table Row Description')
searchDomainsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: searchDomainsIndex.setStatus('current')
if mibBuilder.loadTexts: searchDomainsIndex.setDescription('searchDomains Table Row index')
searchDomainsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1, 1, 2), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: searchDomainsName.setStatus('current')
if mibBuilder.loadTexts: searchDomainsName.setDescription('searchDomains Name')
snmpTrapHosts = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3))
snmpTrapHostsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1), )
if mibBuilder.loadTexts: snmpTrapHostsTable.setStatus('current')
if mibBuilder.loadTexts: snmpTrapHostsTable.setDescription('A table containing entries of snmp Trap Hosts.')
snmpTrapHostsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "snmpTrapHostsIndex"))
if mibBuilder.loadTexts: snmpTrapHostsEntry.setStatus('current')
if mibBuilder.loadTexts: snmpTrapHostsEntry.setDescription('snmpTrapHosts Table Row Description')
snmpTrapHostsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: snmpTrapHostsIndex.setStatus('current')
if mibBuilder.loadTexts: snmpTrapHostsIndex.setDescription('snmpTrapHosts Table Row index')
snmpTrapHostsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTrapHostsName.setStatus('current')
if mibBuilder.loadTexts: snmpTrapHostsName.setDescription('snmp Trap Hosts Name')
snmpTrapHostsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1, 3), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTrapHostsVersion.setStatus('current')
if mibBuilder.loadTexts: snmpTrapHostsVersion.setDescription('snmp Trap Hosts Version')
nis = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4))
nisDomain = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 1), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisDomain.setStatus('current')
if mibBuilder.loadTexts: nisDomain.setDescription('NIS domain')
nisServers = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 2), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisServers.setStatus('current')
if mibBuilder.loadTexts: nisServers.setDescription('NIS servers')
nisAdminGroups = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 3), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisAdminGroups.setStatus('current')
if mibBuilder.loadTexts: nisAdminGroups.setDescription('NIS admin groups')
nisUserGroups = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 4), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisUserGroups.setStatus('current')
if mibBuilder.loadTexts: nisUserGroups.setDescription('NIS user groups')
nisBackupOperatorGroups = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 5), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisBackupOperatorGroups.setStatus('current')
if mibBuilder.loadTexts: nisBackupOperatorGroups.setDescription('NIS backup operator groups')
nisEnabled = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 6), DDMibTableEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisEnabled.setStatus('current')
if mibBuilder.loadTexts: nisEnabled.setDescription('NIS enabled or not')
nisStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 7), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisStatus.setStatus('current')
if mibBuilder.loadTexts: nisStatus.setDescription('NIS status')
managedSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1))
managedSystemTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1), )
if mibBuilder.loadTexts: managedSystemTable.setStatus('current')
if mibBuilder.loadTexts: managedSystemTable.setDescription('A table containing entries of managed systems.')
managedSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "managedSystemIndex"))
if mibBuilder.loadTexts: managedSystemEntry.setStatus('current')
if mibBuilder.loadTexts: managedSystemEntry.setDescription('managedSystemTable Row Description')
managedSystemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: managedSystemIndex.setStatus('current')
if mibBuilder.loadTexts: managedSystemIndex.setDescription('managed system Row index')
managedSystemHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemHostname.setStatus('current')
if mibBuilder.loadTexts: managedSystemHostname.setDescription('managed system hostname')
managedSystemSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 3), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemSerial.setStatus('current')
if mibBuilder.loadTexts: managedSystemSerial.setDescription('managed system serial number')
managedSystemState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemState.setStatus('current')
if mibBuilder.loadTexts: managedSystemState.setDescription('managed system state')
managedSystemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemStatus.setStatus('current')
if mibBuilder.loadTexts: managedSystemStatus.setDescription('managed system status')
managedSystemDDOSVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 6), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemDDOSVersion.setStatus('current')
if mibBuilder.loadTexts: managedSystemDDOSVersion.setDescription('managed system DDOS version')
managedSystemHDSyncTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemHDSyncTime.setStatus('current')
if mibBuilder.loadTexts: managedSystemHDSyncTime.setDescription('managed system historial data last sync time')
managedSystemCDSyncTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 8), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemCDSyncTime.setStatus('current')
if mibBuilder.loadTexts: managedSystemCDSyncTime.setDescription('managed system system current data last sync time')
smtProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 1))
smtStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 20, 1, 1), SmtStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smtStatus.setStatus('current')
if mibBuilder.loadTexts: smtStatus.setDescription('The status of the Secure Multi-Tenancy (SMT) feature on a DD \n            System, which enables storage consolidation for multiple tenants on\n            the same appliance. Through this feature, data and control paths on\n            the DD System are logically secured, isolated and confined, \n            creating secure and isolated logical partitions for each tenant-\n            unit within the same appliance.')
tenantUnitList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2))
tenantUnitListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1), )
if mibBuilder.loadTexts: tenantUnitListTable.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListTable.setDescription('This table contains information about the tenant-units within a \n            DD System that has the Secure Multi-Tenancy (SMT) feature enabled.\n            It includes the tenant-unit name, the number of tenant specific \n            Management users that have been added, the number of Mtree(s)/\n            DDBoost Storage Units assigned, and whether Tenant-self-service \n            mode is enabled.')
tenantUnitListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"))
if mibBuilder.loadTexts: tenantUnitListEntry.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListEntry.setDescription('Information about a tenant-unit within a DD System.')
tenantUnitListIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: tenantUnitListIdx.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListIdx.setDescription('The index of a tenant-unit (SMT management object). This index \n            uniquely identifies the tenant-unit at a given time.')
tenantUnitListName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListName.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListName.setDescription('The name of a tenant-unit. A tenant-unit name consists of letters,\n            numbers, no special characters and can have a length of 254\n            characters.')
tenantUnitListNumberOfMgmtUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListNumberOfMgmtUsers.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListNumberOfMgmtUsers.setDescription('The number of Tenant specific Management users which have been \n            added to a tenant-unit.')
tenantUnitListNumberOfMtrees = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListNumberOfMtrees.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListNumberOfMtrees.setDescription('The number of Mtree(s) which have been assigned to a tenant-unit.')
tenantUnitListNumberOfDdboostStus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListNumberOfDdboostStus.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListNumberOfDdboostStus.setDescription('The number of DDBoost Storage Units which have been assigned to a\n            tenant-unit.')
tenantUnitListTenantSelfServiceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 6), SmtStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListTenantSelfServiceMode.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListTenantSelfServiceMode.setDescription('Status of Tenant Self Service Mode. If enabled, administrative\n            access to each tenant is allowed, so that they can monitor and\n            configure their data protection implementation, within the bounds\n            of their allocated objects and features.')
tenantUnitListParentTenantName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 7), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListParentTenantName.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListParentTenantName.setDescription('The tenant name that a tenant-unit is associated with.\n\t    ')
tenantUnitListType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 8), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListType.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListType.setDescription('The Mtree type of a tenant-unit.\n\t     ')
tenantUnitListSecurityMode = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 9), TenantUnitSecurityModeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListSecurityMode.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListSecurityMode.setDescription('The security mode of a tenant-unit.\n\t     ')
tenantUnitListNumberOfMgmtGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 10), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListNumberOfMgmtGroups.setStatus('current')
if mibBuilder.loadTexts: tenantUnitListNumberOfMgmtGroups.setDescription('The number of Tenant specific Management groups which have been \n            added to a tenant-unit.')
tenantUnitMgmtUserList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 3))
tenantUnitMgmtUserListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1), )
if mibBuilder.loadTexts: tenantUnitMgmtUserListTable.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMgmtUserListTable.setDescription('This table contains information about the tenant specific\n            management users that have been added to a tenant-unit. Such users\n            may be limited by their role and scope to operate a limited set of\n            operations only on the objects which are assigned-to/associated\n            with their tenant-units. Tenant specific management users may have \n            limited administrative and management capabilities.')
tenantUnitMgmtUserListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"), (0, "DATA-DOMAIN-MIB", "tenantUnitMgmtUserListUserName"))
if mibBuilder.loadTexts: tenantUnitMgmtUserListEntry.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMgmtUserListEntry.setDescription('Information about the management users that have been added to a\n            tenant-unit.')
tenantUnitMgmtUserListUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1, 1, 2), DDMibString96TC())
if mibBuilder.loadTexts: tenantUnitMgmtUserListUserName.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMgmtUserListUserName.setDescription('The name of a management user which has been added to a tenant-\n            unit. Users may be limited by their roles and may have limited\n            administrative and management capabilities.')
tenantUnitMgmtUserListUserRole = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1, 1, 3), TenantUnitMgmtUserListUserRoleTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitMgmtUserListUserRole.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMgmtUserListUserRole.setDescription('The role of a management user. Roles include tenant-admin and\n            tenant-user.')
tenantUnitMtreeList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 4))
tenantUnitMtreeListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 4, 1), )
if mibBuilder.loadTexts: tenantUnitMtreeListTable.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMtreeListTable.setDescription('This table contains information about the mtree(s) which have been\n            assigned to a tenant-unit. Mtree logical quotas for soft-limit and\n            hard-limit may be imposed on a tenant-unit and will allow \n            provisioning space for each tenant on a DD System. Data access may\n            be contained within the mtrees belonging to an tenant-unit.')
tenantUnitMtreeListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"), (0, "DATA-DOMAIN-MIB", "tenantUnitMtreeListMtreeName"))
if mibBuilder.loadTexts: tenantUnitMtreeListEntry.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMtreeListEntry.setDescription('Information about an mtree associated with a tenant-unit within a \n            DD System.')
tenantUnitMtreeListMtreeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 4, 1, 1, 2), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitMtreeListMtreeName.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMtreeListMtreeName.setDescription('The name of an mtree that has been assigned to a particular \n            tenant-unit. One tenant-unit (SMT management object) may have \n            multiple mtrees associated with it.')
tenantUnitDdboostStuList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 5))
tenantUnitDdboostStuListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 5, 1), )
if mibBuilder.loadTexts: tenantUnitDdboostStuListTable.setStatus('current')
if mibBuilder.loadTexts: tenantUnitDdboostStuListTable.setDescription('This table contains information about the DDBoost Storage Units\n            that have been assigned to a tenant-unit. Logical quotas for soft-\n            limit and hard-limit may be imposed on a tenant-unit and will allow\n            provisioning space for each tenant on a DD System. Data access\n            may be contained within the DDBoost Storage Units belonging to a\n            tenant-unit.')
tenantUnitDdboostStuListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"), (0, "DATA-DOMAIN-MIB", "tenantUnitDdboostStuListStuName"))
if mibBuilder.loadTexts: tenantUnitDdboostStuListEntry.setStatus('current')
if mibBuilder.loadTexts: tenantUnitDdboostStuListEntry.setDescription('Information about a DDBoost Storage Unit associated with a tenant-\n            unit.')
tenantUnitDdboostStuListStuName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 5, 1, 1, 2), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitDdboostStuListStuName.setStatus('current')
if mibBuilder.loadTexts: tenantUnitDdboostStuListStuName.setDescription('The name of a DDBoost Storage Unit associated with a tenant-unit.\n            One tenant-unit (SMT management object) may have multiple DDBoost \n            Storage Units associated with it.')
tenantUnitAdminIpInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 6))
tenantUnitAdminIpInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1), )
if mibBuilder.loadTexts: tenantUnitAdminIpInfoTable.setStatus('current')
if mibBuilder.loadTexts: tenantUnitAdminIpInfoTable.setDescription('This table provides IP address related information\n\t    about a tenant-unit administrator.')
tenantUnitAdminIpInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"), (0, "DATA-DOMAIN-MIB", "tenantUnitAdminIpInfoAddr"))
if mibBuilder.loadTexts: tenantUnitAdminIpInfoEntry.setStatus('current')
if mibBuilder.loadTexts: tenantUnitAdminIpInfoEntry.setDescription('An entry of this table represents one set of \n\t    IP information about a tenant-unit administrator.')
tenantUnitAdminIpInfoAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1, 1, 2), DDMibString96TC())
if mibBuilder.loadTexts: tenantUnitAdminIpInfoAddr.setStatus('current')
if mibBuilder.loadTexts: tenantUnitAdminIpInfoAddr.setDescription('The IP address (IPv4/IPv6) of a tenant-unit administrator.')
tenantUnitAdminIpInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1, 1, 3), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitAdminIpInfoType.setStatus('current')
if mibBuilder.loadTexts: tenantUnitAdminIpInfoType.setDescription('The IP addresss type of a tenant-unit administrator.\n\t    Possible values: local or remote.')
tenantInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7))
tenantInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1), )
if mibBuilder.loadTexts: tenantInfoTable.setStatus('current')
if mibBuilder.loadTexts: tenantInfoTable.setDescription('This table provides tenant information\n\t    for the Secure Multi-Tenancy (SMT) feature.\n            ')
tenantInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantInfoIdx"))
if mibBuilder.loadTexts: tenantInfoEntry.setStatus('current')
if mibBuilder.loadTexts: tenantInfoEntry.setDescription('An entry represents one instance about a tenant\n\t     that is configured on DD system.')
tenantInfoIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: tenantInfoIdx.setStatus('current')
if mibBuilder.loadTexts: tenantInfoIdx.setDescription('The index into this table indentifying a particular tenant object.')
tenantInfoTenantName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1, 1, 2), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantInfoTenantName.setStatus('current')
if mibBuilder.loadTexts: tenantInfoTenantName.setDescription('The name of this tenant.')
tenantInfoTenantUnitTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 2), )
if mibBuilder.loadTexts: tenantInfoTenantUnitTable.setStatus('current')
if mibBuilder.loadTexts: tenantInfoTenantUnitTable.setDescription('This table provides information about the tenant-unit(s) that\n\t    are associated with this tenant.')
tenantInfoTenantUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantInfoIdx"), (0, "DATA-DOMAIN-MIB", "tenantInfoTenantUnitName"))
if mibBuilder.loadTexts: tenantInfoTenantUnitEntry.setStatus('current')
if mibBuilder.loadTexts: tenantInfoTenantUnitEntry.setDescription('An entry represents information about one tenant-unit\n\t    that is associated with a particular tenant.')
tenantInfoTenantUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 2, 1, 2), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantInfoTenantUnitName.setStatus('current')
if mibBuilder.loadTexts: tenantInfoTenantUnitName.setDescription('The name of tenant-unit that is associated with this tenant.')
tenantUnitMgmtGroupList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8))
tenantUnitMgmtGroupListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1), )
if mibBuilder.loadTexts: tenantUnitMgmtGroupListTable.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMgmtGroupListTable.setDescription('This table contains information about the tenant specific\n            management groups that have been added to a tenant-unit. Such groups\n            may be limited by their role and scope to operate a limited set of\n            operations only on the objects which are assigned-to/associated\n            with their tenant-units. Tenant specific management groups may have \n            limited administrative and management capabilities.')
tenantUnitMgmtGroupListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"), (0, "DATA-DOMAIN-MIB", "tenantUnitMgmtGroupListGroupName"))
if mibBuilder.loadTexts: tenantUnitMgmtGroupListEntry.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMgmtGroupListEntry.setDescription('Information about the management groups that have been added to a\n            tenant-unit.')
tenantUnitMgmtGroupListGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1, 2), DDMibString96TC())
if mibBuilder.loadTexts: tenantUnitMgmtGroupListGroupName.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMgmtGroupListGroupName.setDescription('The name of a management group which has been added to a tenant-\n            unit. Groups may be limited by their roles and may have limited\n            administrative and management capabilities.')
tenantUnitMgmtGroupListGroupRole = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1, 3), TenantUnitMgmtUserListUserRoleTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitMgmtGroupListGroupRole.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMgmtGroupListGroupRole.setDescription('The role of a management group. Roles include tenant-admin and\n            tenant-group.')
tenantUnitMgmtGroupListGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1, 4), TenantUnitMgmtGroupTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitMgmtGroupListGroupType.setStatus('current')
if mibBuilder.loadTexts: tenantUnitMgmtGroupListGroupType.setDescription('The type of a management group.  Types include all, local, ad,\n\t     nis and ldap.')
quotaProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 21, 1))
quotaCapacityStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 21, 1, 1), DDStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacityStatus.setStatus('current')
if mibBuilder.loadTexts: quotaCapacityStatus.setDescription('The status of the quota capacity property on a Data Domain System.\n            If enabled quota limits are enforced and administrators can control\n            the logical space consumed on a per-Mtree basis.')
quotaCapacity = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2))
quotaCapacityTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1), )
if mibBuilder.loadTexts: quotaCapacityTable.setStatus('current')
if mibBuilder.loadTexts: quotaCapacityTable.setDescription('This table lists quota capacities for Mtrees and Storage-units. It \n            provides information such as the Mtree name, the Pre-Comp (MiB) \n            size, Soft-Limit (MiB), and Hard-Limit (MiB). It is comprised of \n            entries of quotaCapacityEntry.')
quotaCapacityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "quotaCapacityIndex"))
if mibBuilder.loadTexts: quotaCapacityEntry.setStatus('current')
if mibBuilder.loadTexts: quotaCapacityEntry.setDescription('An entry containing quota information for Mtrees and Storage-units on\n        the DD System.')
quotaCapacityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: quotaCapacityIndex.setStatus('current')
if mibBuilder.loadTexts: quotaCapacityIndex.setDescription('The index of an Mtree or Storage-unit. This index uniquely \n            identifies the entry at a given time.')
quotaCapacityMtreeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacityMtreeName.setStatus('current')
if mibBuilder.loadTexts: quotaCapacityMtreeName.setDescription('The name of the Mtree or Storage-unit for which quota capacity\n            information is provided.')
quotaCapacityPreCompMiB = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 3), DDMibTableSizeMiBTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacityPreCompMiB.setStatus('current')
if mibBuilder.loadTexts: quotaCapacityPreCompMiB.setDescription('The Pre-Comp (MiB) size of the Mtree or Storage-unit. This is the\n            amount of data written before compression.')
quotaCapacitySoftLimitMiB = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 4), DDMibTableSizeMiBTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacitySoftLimitMiB.setStatus('current')
if mibBuilder.loadTexts: quotaCapacitySoftLimitMiB.setDescription('The Soft-Limit (MiB) quota for the Mtree or Storage-unit. Soft\n            quotas provide only an alert when quota limits are reached, and the\n            backup job is allowed to complete so that the administrator can\n            take corrective actions that are convenient to the organization.')
quotaCapacityHardLimitMiB = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 5), DDMibTableSizeMiBTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacityHardLimitMiB.setStatus('current')
if mibBuilder.loadTexts: quotaCapacityHardLimitMiB.setDescription('The Hard-Limit (MiB) quota for the Mtree or Storage-unit. Hard\n            quotas provide a stricter enforcement model than soft quotas by\n            failing the backup jobs or I/O when quota limits are reached.')
quotaCapacityTenantUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 6), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacityTenantUnit.setStatus('current')
if mibBuilder.loadTexts: quotaCapacityTenantUnit.setDescription('The Tenant-unit to which this Mtree or Storage-unit is assigned.\n            Tenant-units allow for secure and isolated logical partitions \n            within an appliance and are part of the Secure Multi-Tenancy (SMT)\n            feature.')
highAvailabilityStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1))
haSystemName = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 1), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haSystemName.setStatus('current')
if mibBuilder.loadTexts: haSystemName.setDescription('High Availability System Name')
haSystemStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 2), HaSystemStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haSystemStatus.setStatus('current')
if mibBuilder.loadTexts: haSystemStatus.setDescription('High Availability System Status')
haInterconnectStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 3), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haInterconnectStatus.setStatus('current')
if mibBuilder.loadTexts: haInterconnectStatus.setDescription('High Availability Interconnect Status')
haPrimaryHeartbeatStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 4), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haPrimaryHeartbeatStatus.setStatus('current')
if mibBuilder.loadTexts: haPrimaryHeartbeatStatus.setDescription('High Availability Primary Heartbeat Status')
haExternalLanHeartbeatStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 5), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haExternalLanHeartbeatStatus.setStatus('current')
if mibBuilder.loadTexts: haExternalLanHeartbeatStatus.setDescription('High Availability External LAN Heartbeat Status')
haHardwareCompatibilityCheck = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 6), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haHardwareCompatibilityCheck.setStatus('current')
if mibBuilder.loadTexts: haHardwareCompatibilityCheck.setDescription('High Availability Hardware Compatibility Check')
haSoftwareVersionCheck = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 7), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haSoftwareVersionCheck.setStatus('current')
if mibBuilder.loadTexts: haSoftwareVersionCheck.setDescription('High Availability Software Version Check')
highAvailabilityNode = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2))
highAvailabilityNodeTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1), )
if mibBuilder.loadTexts: highAvailabilityNodeTable.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityNodeTable.setDescription('This table provides high availability node information.\n            ')
highAvailabilityNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "highAvailabilityNodeIdx"))
if mibBuilder.loadTexts: highAvailabilityNodeEntry.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityNodeEntry.setDescription('An entry represents one instance about a high availability node.\n\t    ')
highAvailabilityNodeIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: highAvailabilityNodeIdx.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityNodeIdx.setDescription('The index into this table indentifying a particular node.')
highAvailabilityNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 2), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityNodeName.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityNodeName.setDescription('The name of a high availability node.')
highAvailabilityNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 3), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityNodeId.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityNodeId.setDescription('The ID of a high availability node.')
highAvailabilityNodeRole = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 4), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityNodeRole.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityNodeRole.setDescription('The role of a high availability node.')
highAvailabilityNodeState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 5), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityNodeState.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityNodeState.setDescription('The state of a high availability node.')
highAvailabilityNodeHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 6), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityNodeHealth.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityNodeHealth.setDescription("The health of the high availability node's resources.")
highAvailabilityComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3))
highAvailabilityComponentTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3, 1), )
if mibBuilder.loadTexts: highAvailabilityComponentTable.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityComponentTable.setDescription('This table provides high availability component information.\n            ')
highAvailabilityComponentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "highAvailabilityComponentIdx"))
if mibBuilder.loadTexts: highAvailabilityComponentEntry.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityComponentEntry.setDescription('An entry represents one instance about a high availability component.\n\t    ')
highAvailabilityComponentIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: highAvailabilityComponentIdx.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityComponentIdx.setDescription('The index into this table indentifying a particular component.')
highAvailabilityComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3, 1, 1, 2), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityComponentName.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityComponentName.setDescription('The name of the component.')
highAvailabilityComponentState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3, 1, 1, 3), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityComponentState.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityComponentState.setDescription('The status of the component.')
scsitargetProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 1))
scsitargetAdminState = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 23, 1, 1), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetAdminState.setStatus('current')
if mibBuilder.loadTexts: scsitargetAdminState.setDescription('Scsitarget Admin State')
scsitargetProcessState = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 23, 1, 2), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetProcessState.setStatus('current')
if mibBuilder.loadTexts: scsitargetProcessState.setDescription('Scsitarget Process State')
scsitargetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2))
scsitargetGroupTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1), )
if mibBuilder.loadTexts: scsitargetGroupTable.setStatus('current')
if mibBuilder.loadTexts: scsitargetGroupTable.setDescription('Scsitarget Group Table')
scsitargetGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetGroupIndex"))
if mibBuilder.loadTexts: scsitargetGroupEntry.setStatus('current')
if mibBuilder.loadTexts: scsitargetGroupEntry.setDescription('scsitargetGroupEntry')
scsitargetGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetGroupIndex.setStatus('current')
if mibBuilder.loadTexts: scsitargetGroupIndex.setDescription('Scsitarget Group Index')
scsitargetGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetGroupName.setStatus('current')
if mibBuilder.loadTexts: scsitargetGroupName.setDescription('Scsitarget Group Name')
scsitargetGroupService = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetGroupService.setStatus('current')
if mibBuilder.loadTexts: scsitargetGroupService.setDescription('Scsitarget Group Service')
scsitargetGroupActiveState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 4), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetGroupActiveState.setStatus('current')
if mibBuilder.loadTexts: scsitargetGroupActiveState.setDescription('Scsitarget Group Active State')
scsitargetGroupNumInitiators = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetGroupNumInitiators.setStatus('current')
if mibBuilder.loadTexts: scsitargetGroupNumInitiators.setDescription('Scsitarget Group Number of Initiators')
scsitargetGroupNumDevices = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 6), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetGroupNumDevices.setStatus('current')
if mibBuilder.loadTexts: scsitargetGroupNumDevices.setDescription('Scsitarget Group Number of Devices')
scsitargetInitiator = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3))
scsitargetInitiatorTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1), )
if mibBuilder.loadTexts: scsitargetInitiatorTable.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorTable.setDescription('Scsitarget Initiator Table')
scsitargetInitiatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetInitiatorIndex"))
if mibBuilder.loadTexts: scsitargetInitiatorEntry.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorEntry.setDescription('scsitargetInitiatorEntry')
scsitargetInitiatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetInitiatorIndex.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorIndex.setDescription('Scsitarget Initiator Index')
scsitargetInitiatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorName.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorName.setDescription('Scsitarget Initiator Name')
scsitargetInitiatorSystemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorSystemAddress.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorSystemAddress.setDescription('Scsitarget Initiator System Address')
scsitargetInitiatorGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 4), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorGroup.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorGroup.setDescription('Scsitarget Initiator Group')
scsitargetInitiatorService = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 5), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorService.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorService.setDescription('Scsitarget Initiator Service')
scsitargetInitiatorAddressMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 6), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorAddressMethod.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorAddressMethod.setDescription('Scsitarget Initiator Address Method')
scsitargetInitiatorTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 7), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorTransport.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorTransport.setDescription('Scsitarget Initiator Transport')
scsitargetInitiatorFcWwpn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 8), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorFcWwpn.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorFcWwpn.setDescription('Scsitarget Initiator Fc Wwpn')
scsitargetInitiatorFcWwnn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 9), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorFcWwnn.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorFcWwnn.setDescription('Scsitarget Initiator Fc Wwnn')
scsitargetInitiatorFcSymbolicPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 10), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorFcSymbolicPortName.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorFcSymbolicPortName.setDescription('Scsitarget Initiator Fc Symbolic Port Name')
scsitargetInitiatorEndpTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2), )
if mibBuilder.loadTexts: scsitargetInitiatorEndpTable.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorEndpTable.setDescription('Scsitarget Initiator Endpoint Table')
scsitargetInitiatorEndpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetInitiatorEndpIndex"))
if mibBuilder.loadTexts: scsitargetInitiatorEndpEntry.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorEndpEntry.setDescription('scsitargetInitiatorEndpEntry')
scsitargetInitiatorEndpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetInitiatorEndpIndex.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorEndpIndex.setDescription('Scsitarget Initiator Endpoint Index')
scsitargetInitiatorEndpInitiator = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorEndpInitiator.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorEndpInitiator.setDescription('Scsitarget Initiator')
scsitargetInitiatorEndpEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorEndpEndpoint.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorEndpEndpoint.setDescription('Scsitarget Initiator Endpoint')
scsitargetInitiatorEndpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 4), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorEndpStatus.setStatus('current')
if mibBuilder.loadTexts: scsitargetInitiatorEndpStatus.setDescription('Scsitarget Initiator Endpoint Status')
scsitargetEndpoint = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4))
scsitargetEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1), )
if mibBuilder.loadTexts: scsitargetEndpointTable.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointTable.setDescription('Scsitarget Endpoint Table')
scsitargetEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetEndpointIndex"))
if mibBuilder.loadTexts: scsitargetEndpointEntry.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointEntry.setDescription('scsitargetEndpointEntry')
scsitargetEndpointIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetEndpointIndex.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointIndex.setDescription('Scsitarget Endpoint Index')
scsitargetEndpointName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointName.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointName.setDescription('Scsitarget Endpoint Name')
scsitargetEndpointCurrentSystemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointCurrentSystemAddress.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointCurrentSystemAddress.setDescription('Scsitarget Endpoint Current System Address')
scsitargetEndpointPrimarySystemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 4), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointPrimarySystemAddress.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointPrimarySystemAddress.setDescription('Scsitarget Endpoint Primary System Address')
scsitargetEndpointSecondarySystemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 5), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointSecondarySystemAddress.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointSecondarySystemAddress.setDescription('Scsitarget Endpoint Secondary System Address')
scsitargetEndpointEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 6), DDStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointEnabled.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointEnabled.setDescription('Scsitarget Endpoint Enabled')
scsitargetEndpointStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 7), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointStatus.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointStatus.setDescription('Scsitarget Endpoint Status')
scsitargetEndpointTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 8), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointTransport.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointTransport.setDescription('Scsitarget Endpoint Transport')
scsitargetEndpointFcWwnn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 9), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointFcWwnn.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointFcWwnn.setDescription('Scsitarget Endpoint Fc Wwnn')
scsitargetEndpointFcWwpn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 10), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointFcWwpn.setStatus('current')
if mibBuilder.loadTexts: scsitargetEndpointFcWwpn.setDescription('Scsitarget Endpoint Fc Wwpn')
scsitargetPort = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5))
scsitargetPortTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1), )
if mibBuilder.loadTexts: scsitargetPortTable.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortTable.setDescription('Scsitarget Port Table')
scsitargetPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetPortIndex"))
if mibBuilder.loadTexts: scsitargetPortEntry.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortEntry.setDescription('scsitargetPortEntry')
scsitargetPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetPortIndex.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortIndex.setDescription('Scsitarget Port Index')
scsitargetPortSystemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortSystemAddress.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortSystemAddress.setDescription('Scsitarget Port System Address')
scsitargetPortEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 3), DDStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEnabled.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortEnabled.setDescription('Scsitarget Port Enabled')
scsitargetPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 4), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortStatus.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortStatus.setDescription('Scsitarget Port Status')
scsitargetPortTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 5), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortTransport.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortTransport.setDescription('Scsitarget Port Transport')
scsitargetPortOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 6), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortOperationalStatus.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortOperationalStatus.setDescription('Scsitarget Port Operational Status')
scsitargetPortFcNpiv = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 7), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcNpiv.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortFcNpiv.setDescription('Scsitarget Port Fc Npiv')
scsitargetPortPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 8), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortPortId.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortPortId.setDescription('Scsitarget Port Port Id')
scsitargetPortModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 9), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortModel.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortModel.setDescription('Scsitarget Port Model')
scsitargetPortFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 10), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFirmware.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortFirmware.setDescription('Scsitarget Port Firmware')
scsitargetPortFcBaseWwnn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 11), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcBaseWwnn.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortFcBaseWwnn.setDescription('Scsitarget Port Fc Base Wwnn')
scsitargetPortFcBaseWwpn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 12), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcBaseWwpn.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortFcBaseWwpn.setDescription('Scsitarget Port Fc Base Wwpn')
scsitargetPortFcCurrentWwnn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 13), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcCurrentWwnn.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortFcCurrentWwnn.setDescription('Scsitarget Port Fc Current Wwnn')
scsitargetPortFcCurrentWwpn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 14), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcCurrentWwpn.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortFcCurrentWwpn.setDescription('Scsitarget Port Fc Current Wwpn')
scsitargetPortFcp2Retry = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 15), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcp2Retry.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortFcp2Retry.setDescription('Scsitarget Port Fcp2 Retry')
scsitargetPortConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 16), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortConnectionType.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortConnectionType.setDescription('scsitarget Port Connection Type')
scsitargetPortLinkSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 17), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortLinkSpeed.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortLinkSpeed.setDescription('Scsitarget Port Link Speed')
scsitargetPortFcTopology = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 18), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcTopology.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortFcTopology.setDescription('Scsitarget Port Fc Topology')
scsitargetPortEndpTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2), )
if mibBuilder.loadTexts: scsitargetPortEndpTable.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortEndpTable.setDescription('Scsitarget Port Endpoint Table')
scsitargetPortEndpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetPortEndpIndex"))
if mibBuilder.loadTexts: scsitargetPortEndpEntry.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortEndpEntry.setDescription('scsitargetPortEndpEntry')
scsitargetPortEndpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetPortEndpIndex.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortEndpIndex.setDescription('Scsitarget Port Endpoint Index')
scsitargetPortEndpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEndpPort.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortEndpPort.setDescription('Scsitarget Port')
scsitargetPortEndpEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEndpEndpoint.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortEndpEndpoint.setDescription('Scsitarget Port Endpoint')
scsitargetPortEndpEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 4), DDStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEndpEnabled.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortEndpEnabled.setDescription('Scsitarget Port Endpoint Enabled')
scsitargetPortEndpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 5), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEndpStatus.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortEndpStatus.setDescription('Scsitarget Port Endpoint Status')
scsitargetPortEndpCurrentInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 6), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEndpCurrentInstance.setStatus('current')
if mibBuilder.loadTexts: scsitargetPortEndpCurrentInstance.setDescription('Scsitarget Port Endpoint Current Instance')
scsitargetDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6))
scsitargetDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1), )
if mibBuilder.loadTexts: scsitargetDeviceTable.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceTable.setDescription('Scsitarget Device Table')
scsitargetDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetDeviceIndex"))
if mibBuilder.loadTexts: scsitargetDeviceEntry.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceEntry.setDescription('scsitargetDeviceEntry')
scsitargetDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetDeviceIndex.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceIndex.setDescription('Scsitarget Device Index')
scsitargetDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceName.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceName.setDescription('Scsitarget Device Name')
scsitargetDeviceService = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceService.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceService.setDescription('Scsitarget Device Service')
scsitargetDeviceActiveState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 4), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceActiveState.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceActiveState.setDescription('Scsitarget Device Active State')
scsitargetDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 5), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceAddress.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceAddress.setDescription('Scsitarget Device Address')
scsitargetDeviceGrpTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2), )
if mibBuilder.loadTexts: scsitargetDeviceGrpTable.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceGrpTable.setDescription('Scsitarget Device Group Table')
scsitargetDeviceGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetDeviceGrpIndex"))
if mibBuilder.loadTexts: scsitargetDeviceGrpEntry.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceGrpEntry.setDescription('scsitargetDeviceGrpEntry')
scsitargetDeviceGrpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetDeviceGrpIndex.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceGrpIndex.setDescription('Scsitarget Device Group Index')
scsitargetDeviceGrpDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpDevice.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceGrpDevice.setDescription('Scsitarget Device')
scsitargetDeviceGrpGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpGroupName.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceGrpGroupName.setDescription('Scsitarget Device Group Name')
scsitargetDeviceGrpLun = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 4), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpLun.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceGrpLun.setDescription('Scsitarget Device Group Lun')
scsitargetDeviceGrpPrimaryEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 5), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpPrimaryEndpoints.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceGrpPrimaryEndpoints.setDescription('Scsitarget Device Group Primary Endpoints')
scsitargetDeviceGrpSecondaryEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 6), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpSecondaryEndpoints.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceGrpSecondaryEndpoints.setDescription('Scsitarget Device Group Secondary Endpoints')
scsitargetDeviceGrpInUseEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 7), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpInUseEndpoints.setStatus('current')
if mibBuilder.loadTexts: scsitargetDeviceGrpInUseEndpoints.setDescription('Scsitarget Device Group In Use Endpoints')
dataDomainMibTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 2, 0))
powerSupplyFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 1))
if mibBuilder.loadTexts: powerSupplyFailedAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: powerSupplyFailedAlarm.setDescription('Meaning: Power Supply failed\n             What to do: replace the power supply')
systemOverheatWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 2)).setObjects(("DATA-DOMAIN-MIB", "tempSensorDescription"))
if mibBuilder.loadTexts: systemOverheatWarningAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: systemOverheatWarningAlarm.setDescription("Meaning: the temperature reading of one of the thermometers in the Chassis  has exceeded \n\t     the 'warning' temperature level.  If it continues to rise, it may eventually trigger a \n\t     shutdown of the DDR.  The index value of the alarm indicates the thermometer index that\n\t     may be looked up in the environmentals table 'temperatures' for more information about\n\t     the actual thermometer reading the high value.\n\t     What to do: check the Fan status, temperatures of the environment in which the DDR is,\n\t     and other factors which may increase the temperature.")
systemOverheatAlertAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 3)).setObjects(("DATA-DOMAIN-MIB", "tempSensorDescription"))
if mibBuilder.loadTexts: systemOverheatAlertAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: systemOverheatAlertAlarm.setDescription("Meaning: the temperature reading of one of the thermometers in the Chassis is more than\n\t     halfway between the 'warning' and 'shutdown' temperature levels.  If it continues to rise, \n\t     it may eventually trigger a shutdown of the DDR.  The index value of the alarm indicates \n\t     the thermometer index that may be looked up in the environmentals table 'temperatures' \n\t     for more information about the actual thermometer reading the high value.\n\t     What to do: check the Fan status, temperatures of the environment in which the DDR is,\n\t     and other factors which may increase the system temperature.")
systemOverheatShutdownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 4)).setObjects(("DATA-DOMAIN-MIB", "tempSensorDescription"))
if mibBuilder.loadTexts: systemOverheatShutdownAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: systemOverheatShutdownAlarm.setDescription("Meaning: the temperature reading of one of the thermometers in the Chassis has reached\n\t     or exceeded the 'shutdown' temperature level. The DDR will be shutdown to prevent damage\n\t     to the system.  The index value of the alarm indicates the thermometer index that may be\n\t     looked up in the environmentals table 'temperatures' for more information about the actual \n\t     thermometer reading the high value.\n\t     What to do: Once the system has been brought back up, after checking for high environment\n\t     temperatures or other factors which may increase the system temperature, check other \n\t     environmental values, such as Fan Status, Disk Temperatures, etc...")
fanModuleFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5)).setObjects(("DATA-DOMAIN-MIB", "fanDescription"))
if mibBuilder.loadTexts: fanModuleFailedAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: fanModuleFailedAlarm.setDescription("Meaning: a Fan Module in the enclosure has failed.  The index of the fan is given\n             as the index of the alarm.  This same index can be looked up in the environmentals\n             table 'fanProperies' for more information about which fan has failed.\n             What to do: replace the fan")
nvramFailingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6))
if mibBuilder.loadTexts: nvramFailingAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: nvramFailingAlarm.setDescription("Meaning: The system has detected that the NVRAM is potentially failing.  There has\n            been an excessive amount of PCI or Memory errors. The nvram tables 'nvramProperties'\n            and 'nvramStats' may provide for information on why the NVRAM is failing.\n            What to do: check the status of the NVRAM after reboot, and replace if the\n            errors continue.")
fileSystemFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7))
if mibBuilder.loadTexts: fileSystemFailedAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: fileSystemFailedAlarm.setDescription('Meaning: The File System process on the DDR has had a serious problem and has had\n             to restart.\n             What to do: check the system logs for conditions that may be triggering the failure.\n             Other alarms may also indicate why the File System is having problems.')
fileSpaceMaintenanceAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 8)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceName"))
if mibBuilder.loadTexts: fileSpaceMaintenanceAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: fileSpaceMaintenanceAlarm.setDescription('Meaning: DDVAR File System Resource Space is running low for system maintenance activities.  The\n\t     system may not have enough space for the routine system activities to run without error.\n\t     What to do: Delete unneeded files, such as old log files, support bundles, core files,\n\t     upgrade rpm files stored in the /ddvar file system.')
fileSpacePreWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 9)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceName"))
if mibBuilder.loadTexts: fileSpacePreWarningAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: fileSpacePreWarningAlarm.setDescription("Meaning: A File System Resource space is 80-85% utilized.  While not critical, the space usage\n\t     should be monitored.  The index value of the alarm indicates the file system index that may be \n\t     looked up in the fileSystem table 'fileSystemSpace' for more information about the actual FS \n\t     that is getting full. \n\t     What to do: no action is necessary, but the file system should be monitored more closely as it\n\t     grows more full.  Further alarms will be sent when and if the file system space is approaching very full.")
fileSpaceWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceName"))
if mibBuilder.loadTexts: fileSpaceWarningAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: fileSpaceWarningAlarm.setDescription("Meaning: A File System Resource space is 90% utilized.  The index value of the alarm indicates \n\t     the file system index that may be looked up in the fileSystem table 'fileSystemSpace' \n\t     for more information about the actual FS that is getting full. \n\t     What to do: Delete unneeded files, such as old log files, support bundles, core files,\n\t     upgrade rpm files stored in the /ddvar file system.  Consider upgrading the hardware or adding\n\t     shelves to high-end units.  Reducing the retention times for backup data can also help. When \n\t     files are deleted from outside of the /ddvar space, filesys clean will have to be done before \n\t     the space is recovered.")
fileSpaceSevereAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 11)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceName"))
if mibBuilder.loadTexts: fileSpaceSevereAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: fileSpaceSevereAlarm.setDescription("Meaning: A File System Resource space is 95% utilized.  The index value of the alarm indicates \n\t     the file system index that may be looked up in the fileSystem table 'fileSystemSpace' \n\t     for more information about the actual FS that is getting full. \n\t     What to do: Delete unneeded files, such as old log files, support bundles, core files,\n\t     upgrade rpm files stored in the /ddvar file system.  Consider upgrading the hardware or adding\n\t     shelves to high-end units.  Reducing the retention times for backup data can also help. When \n\t     files are deleted from outside of the /ddvar space, filesys clean will have to be done before \n\t     the space is recovered.")
fileSpaceCriticalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 12)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceName"))
if mibBuilder.loadTexts: fileSpaceCriticalAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: fileSpaceCriticalAlarm.setDescription("Meaning: A File System Resource space is 100% utilized.  The index value of the alarm indicates \n\t     the file system index that may be looked up in the fileSystem table 'fileSystemSpace' \n\t     for more information about the actual FS that is full. \n\t     What to do: Delete unneeded files, such as old log files, support bundles, core files,\n\t     upgrade rpm files stored in the /ddvar file system.  Consider upgrading the hardware or adding\n\t     shelves to high-end units.  Reducing the retention times for backup data can also help. When \n\t     files are deleted from outside of the /ddvar space, filesys clean will have to be done before \n\t     the space is recovered.")
diskFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 14)).setObjects(("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskFailedAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: diskFailedAlarm.setDescription("Meaning: some problem has been detected about the indicated disk.  The index value \n             of the alarm indicates the disk index that may be looked up in the disk tables \n             'diskProperties', 'diskPerformance', and 'diskReliability' for more information \n             about the actual disk that has failed.\n             What to do: replace the disk.")
diskOverheatWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 15)).setObjects(("DATA-DOMAIN-MIB", "diskTemperature"))
if mibBuilder.loadTexts: diskOverheatWarningAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: diskOverheatWarningAlarm.setDescription("Meaning: the temperature reading of the indicated disk has exceeded the 'warning' \n\t     temperature level.  If it continues to rise, it may eventually trigger a \n\t     shutdown of the DDR.  The index value of the alarm indicates the disk index that\n\t     may be looked up in the disk tables 'diskProperties', 'diskPerformance', and \n\t     'diskReliability' for more information about the actual disk reading the high value.\n\t     What to do: check the disk status, temperatures of the environment in which the DDR is,\n\t     and other factors which may increase the temperature.")
diskOverheatAlertAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 16)).setObjects(("DATA-DOMAIN-MIB", "diskTemperature"))
if mibBuilder.loadTexts: diskOverheatAlertAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: diskOverheatAlertAlarm.setDescription("Meaning: the temperature reading of the indicated disk is more than halfway between\n\t     the 'warning' and 'shutdown' temperature levels. If it continues to rise, it will \n\t     trigger a shutdown of the DDR.  The index value of the alarm indicates the disk index that\n\t     may be looked up in the disk tables 'diskProperties', 'diskPerformance', and \n\t     'diskReliability' for more information about the actual disk reading the high value.\n\t     What to do: check the disk status, temperatures of the environment in which the DDR is,\n\t     and other factors which may increase the temperature.  If the temperature continues stays\n\t     at this level or rises, and no other disks are reading this trouble, consider 'failing'\n\t     the disk, and get a replacement.")
diskOverheatShutdownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 17)).setObjects(("DATA-DOMAIN-MIB", "diskTemperature"))
if mibBuilder.loadTexts: diskOverheatShutdownAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: diskOverheatShutdownAlarm.setDescription("Meaning: the temperature reading of the indicated disk has surpassed the 'shutdown' \n\t     temperature level. The DDR will be shutdown.  The index value of the alarm indicates \n\t     the disk index that may be looked up in the disk tables 'diskProperties', 'diskPerformance', \n\t     and 'diskReliability' for more information about the actual disk reading the high value.\n\t     What to do: Boot the DDR and monitor the status and temperatures.  If the same disk has\n\t     continued problems, consider 'failing' it and get a replacement disk.")
raidReconSevereAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 18))
if mibBuilder.loadTexts: raidReconSevereAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: raidReconSevereAlarm.setDescription('Meaning: A raid group is MAX degraded with no reconstruction after less than 71 hours or \n             A disk group is degraded with none max degraded with no reconstruction. This alarm is sent \n             every 1 hour until 71 hours after which raidReconCriticalAlarm or raidReconCriticalShutdown\n             alarm is generated. This can happen due to a disk failing at run-time or boot-time.\n\t     What to do: while it is still possible that the reconstruction could succeed, the disk\n\t     should be replaced to ensure data safety.')
raidReconCriticalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 19))
if mibBuilder.loadTexts: raidReconCriticalAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: raidReconCriticalAlarm.setDescription('Meaning: Raid group is MAX degraded with no reconstruction after 71 hours. This can\n\t     happen due to a disk failing at run-time or boot-up.\n\t     What to do: the disk should be replaced to ensure data safety.')
raidReconCriticalShutdownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 20))
if mibBuilder.loadTexts: raidReconCriticalShutdownAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: raidReconCriticalShutdownAlarm.setDescription('Meaning: Raid group is MAX degraded with no reconstruction after 71 hours. This can\n             happen due to a disk failing at run-time or boot-up.\n\t     What to do: the disk must be replaced.')
raidGroupMissingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 21))
if mibBuilder.loadTexts: raidGroupMissingAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: raidGroupMissingAlarm.setDescription('Meaning: one or more raid groups are missing.\n\t     What to do: disk may need replacement, or raid administration may be necessary.')
diskNoSpareAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 22))
if mibBuilder.loadTexts: diskNoSpareAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: diskNoSpareAlarm.setDescription('Meaning: there is no spare available for the raid group.\n\t     What to do: disk may need replacement, or raid administration may be necessary.')
diskPathAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 23)).setObjects(("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskPathAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: diskPathAlarm.setDescription('Meaning: multipath configuration is experiencing a problem.  The number of paths set up is less than \n\t    the required number of paths.  Disk index is the first disk in the enclosure with multipath.\n\t     What to do: multipath disk administration may be necessary.')
diskSASAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 24))
if mibBuilder.loadTexts: diskSASAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: diskSASAlarm.setDescription('Meaning: SAS configuration error.  Maximum enclosures has been reached, or there\n\t    is a topology problem.\n\t     What to do: SAS configuration documentation should be consulted.  administration may be necessary.')
diskSASHBAAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 25)).setObjects(("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskSASHBAAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: diskSASHBAAlarm.setDescription('Meaning: Unsupported multi-path setting is enabled in the hba firmware.\n\t     What to do: contact Data Domain support.')
snapshotFullAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 26))
if mibBuilder.loadTexts: snapshotFullAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: snapshotFullAlarm.setDescription('Meaning: maximum number of snapshots has been reached.\n\t     What to do: expire some old snapshots to make room.')
snapshotHWMAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 27))
if mibBuilder.loadTexts: snapshotHWMAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: snapshotHWMAlarm.setDescription('Meaning: the number of snapshots has exceeded a predefined percentage (current 90%) of the maximum.\n\t     What to do: begin expiring snapshots so that the maximum is not reached.')
clusterNodeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 28))
if mibBuilder.loadTexts: clusterNodeAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: clusterNodeAlarm.setDescription('Meaning: node is not reachable on any network interface.\n\t     What to do: check status of network and wiring.  if that fails, try \n\t     rebooting the node.')
clusterInterfaceAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 29))
if mibBuilder.loadTexts: clusterInterfaceAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: clusterInterfaceAlarm.setDescription('Meaning: one interface of the cluster node is down.\n\t     What to do: check status of network and wiring.  if that fails, try \n\t     rebooting the node.')
replSyncAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 30)).setObjects(("DATA-DOMAIN-MIB", "replStatus"))
if mibBuilder.loadTexts: replSyncAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: replSyncAlarm.setDescription('Meaning: a replication context is disabled due to nvram loss.\n\t     What to do: break replication on source and destination, then reconfigure\n\t     them and run replication sync.')
systemStartupAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 31))
if mibBuilder.loadTexts: systemStartupAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: systemStartupAlarm.setDescription('Meaning: system has rebooted or started.  this does not indicate any abnormal activity.\n\t     What to do: nothing, unless reboot was triggered by other abnormal conditions, such as\n\t     temperature, fan or power problems.')
filesysRelaunchAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 32))
if mibBuilder.loadTexts: filesysRelaunchAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: filesysRelaunchAlarm.setDescription('Meaning: file system has undergone too many relaunches.  it is probably unstable.\n\t     What to do: consult system logs.  software or hardware restart may fix the malfunction.')
filesysDDGCFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 33))
if mibBuilder.loadTexts: filesysDDGCFailedAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: filesysDDGCFailedAlarm.setDescription('Meaning: DDGC cleaning process has failed.\n\t     What to do: consult system logs.  software or hardware restart may fix the malfunction.')
filesysGeneralProblemAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 34))
if mibBuilder.loadTexts: filesysGeneralProblemAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: filesysGeneralProblemAlarm.setDescription('Meaning: a general problem has occurred with the file system.\n\t     What to do: consult system logs.  software or hardware restart may fix the malfunction.')
diskUnsupportedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 35)).setObjects(("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskUnsupportedAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: diskUnsupportedAlarm.setDescription("Meaning: the model of the disk is unsupported by current DD platform.  The index value \n             of the alarm indicates the disk index that may be looked up in the disk tables \n             'diskProperties', 'diskPerformance', and 'diskReliability' for more information \n             about the actual disk.\n             What to do: replace the disk.")
eventIPMIUnmanageAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 36))
if mibBuilder.loadTexts: eventIPMIUnmanageAlarm.setStatus('deprecated')
if mibBuilder.loadTexts: eventIPMIUnmanageAlarm.setDescription('Meaning: IPMI unmanaged alert detected.\n             What to do: check alert message')
generatedNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 5000)).setObjects(("DATA-DOMAIN-MIB", "cpismissing"), ("DATA-DOMAIN-MIB", "controllerUnreachableAlert"), ("DATA-DOMAIN-MIB", "controllerIfaceUnreachableAlert"), ("DATA-DOMAIN-MIB", "containerMarkedInvalid"), ("DATA-DOMAIN-MIB", "cMTaskEnded"), ("DATA-DOMAIN-MIB", "correctableECCLimitReached"), ("DATA-DOMAIN-MIB", "uncorrectableECCerror"), ("DATA-DOMAIN-MIB", "dIMMFailure"), ("DATA-DOMAIN-MIB", "compromisedEncryptionKeys"), ("DATA-DOMAIN-MIB", "newEncryptionKey"), ("DATA-DOMAIN-MIB", "encryptionKeyTableFull"), ("DATA-DOMAIN-MIB", "encryptionKeyExportFailed"), ("DATA-DOMAIN-MIB", "insufficientSpaceForEncryption"), ("DATA-DOMAIN-MIB", "corruptEncryptionKeys"), ("DATA-DOMAIN-MIB", "legacyChassisTempWarning"), ("DATA-DOMAIN-MIB", "legacyChassisTempCritical"), ("DATA-DOMAIN-MIB", "legacyPowerSupplyWarning"), ("DATA-DOMAIN-MIB", "legacyFanWarning"), ("DATA-DOMAIN-MIB", "powerSupplyWarning"), ("DATA-DOMAIN-MIB", "fanWarning"), ("DATA-DOMAIN-MIB", "voltageWarning"), ("DATA-DOMAIN-MIB", "powerWarning"), ("DATA-DOMAIN-MIB", "correctECCWarning"), ("DATA-DOMAIN-MIB", "processorWarning"), ("DATA-DOMAIN-MIB", "powerUnitWarning"), ("DATA-DOMAIN-MIB", "unCorrectECCWarning"), ("DATA-DOMAIN-MIB", "chassisSensorCritical"), ("DATA-DOMAIN-MIB", "chassisTempWarning"), ("DATA-DOMAIN-MIB", "chassisTempCritical"), ("DATA-DOMAIN-MIB", "cPUFailureWarning"), ("DATA-DOMAIN-MIB", "legacyBMCHangCritical"), ("DATA-DOMAIN-MIB", "bMCHangCritical"), ("DATA-DOMAIN-MIB", "abnormalShutdown"), ("DATA-DOMAIN-MIB", "smiMrc"), ("DATA-DOMAIN-MIB", "bMCPartialHang"), ("DATA-DOMAIN-MIB", "fanFault"), ("DATA-DOMAIN-MIB", "powerSupplyInputFault"), ("DATA-DOMAIN-MIB", "powerSupplyFailure"), ("DATA-DOMAIN-MIB", "powerSupplyAbsent"), ("DATA-DOMAIN-MIB", "unsupportedACVoltage"), ("DATA-DOMAIN-MIB", "iOModuleFault"), ("DATA-DOMAIN-MIB", "iOModuleInserted"), ("DATA-DOMAIN-MIB", "mgmtModuleFault"), ("DATA-DOMAIN-MIB", "sPFault"), ("DATA-DOMAIN-MIB", "chassisFailure"), ("DATA-DOMAIN-MIB", "forcedControllerShutdown"), ("DATA-DOMAIN-MIB", "systemReset"), ("DATA-DOMAIN-MIB", "enclosureHighTemp"), ("DATA-DOMAIN-MIB", "unsupportedSystemType"), ("DATA-DOMAIN-MIB", "bMCHangShutdown"), ("DATA-DOMAIN-MIB", "bMCFailure"), ("DATA-DOMAIN-MIB", "unsupportedHardwareConfig"), ("DATA-DOMAIN-MIB", "unsupportedVirtualCPU"), ("DATA-DOMAIN-MIB", "unsupportedPowerSupply"), ("DATA-DOMAIN-MIB", "openFanDrawer"), ("DATA-DOMAIN-MIB", "memoryRiserFault"), ("DATA-DOMAIN-MIB", "bMCFailureSysBBU"), ("DATA-DOMAIN-MIB", "unsupportedEnclosurePSU"), ("DATA-DOMAIN-MIB", "pCILinkDegraded"), ("DATA-DOMAIN-MIB", "invalidHardwareCritical"), ("DATA-DOMAIN-MIB", "invalidHardwareWarning"), ("DATA-DOMAIN-MIB", "correctableErrorWarning"), ("DATA-DOMAIN-MIB", "generalHardwareFailure"), ("DATA-DOMAIN-MIB", "targetDriverPortOffline"), ("DATA-DOMAIN-MIB", "targetDriverPortOnline"), ("DATA-DOMAIN-MIB", "targetDriverPortCore"), ("DATA-DOMAIN-MIB", "targetDriverPortMultipleCore"), ("DATA-DOMAIN-MIB", "targetDriverPortFWLoadFailed"), ("DATA-DOMAIN-MIB", "targetDriverPortUnreadable"), ("DATA-DOMAIN-MIB", "targetDriverPortTooManyOsc"), ("DATA-DOMAIN-MIB", "tooManyRelaunches"), ("DATA-DOMAIN-MIB", "filesystemProblem"), ("DATA-DOMAIN-MIB", "dDFSFailedInShutdown"), ("DATA-DOMAIN-MIB", "dDFSNoHeartbeat"), ("DATA-DOMAIN-MIB", "dDFSDiedAfterReboot"), ("DATA-DOMAIN-MIB", "dDFSDied"), ("DATA-DOMAIN-MIB", "dDFSRebooted"), ("DATA-DOMAIN-MIB", "dDFSRebootedDisabled"), ("DATA-DOMAIN-MIB", "indexRebuildComplete"), ("DATA-DOMAIN-MIB", "filesystemNVRAMDataLoss"), ("DATA-DOMAIN-MIB", "recoverFromNVRAMFailed"), ("DATA-DOMAIN-MIB", "dDFSRequiresReboot"), ("DATA-DOMAIN-MIB", "metadataWarningThreshold"), ("DATA-DOMAIN-MIB", "filesystemCorruption"), ("DATA-DOMAIN-MIB", "physicalCapacityMeasurementTasksLost"), ("DATA-DOMAIN-MIB", "physicalCapacityMeasurementTasksLostMTree"), ("DATA-DOMAIN-MIB", "physicalCapacityMeasurementScheduleFailed"), ("DATA-DOMAIN-MIB", "uncertifiedFirmware"), ("DATA-DOMAIN-MIB", "fileMigrationError"), ("DATA-DOMAIN-MIB", "cleaningError"), ("DATA-DOMAIN-MIB", "hAdegraded"), ("DATA-DOMAIN-MIB", "hAofflineErrors"), ("DATA-DOMAIN-MIB", "hATimeOutOfSync"), ("DATA-DOMAIN-MIB", "historicalDatabaseRecoverError"), ("DATA-DOMAIN-MIB", "historicalDatabaseBackupError"), ("DATA-DOMAIN-MIB", "historicalDatabaseUpgradeError"), ("DATA-DOMAIN-MIB", "historicalDatabasePruneError"), ("DATA-DOMAIN-MIB", "noHistoricalDatabaseError"), ("DATA-DOMAIN-MIB", "historicalDatabaseFailoverError"), ("DATA-DOMAIN-MIB", "hDTFileTransferFailed"), ("DATA-DOMAIN-MIB", "hDTSystemError"), ("DATA-DOMAIN-MIB", "spuriousInterruptDisabled"), ("DATA-DOMAIN-MIB", "licenseExpiring"), ("DATA-DOMAIN-MIB", "licenseExpired"), ("DATA-DOMAIN-MIB", "dIMMFailureAlert"), ("DATA-DOMAIN-MIB", "memoryAlert"), ("DATA-DOMAIN-MIB", "portPathDisabled"), ("DATA-DOMAIN-MIB", "diskPathRedundancy"), ("DATA-DOMAIN-MIB", "missingPortConnection"), ("DATA-DOMAIN-MIB", "missingLunPath"), ("DATA-DOMAIN-MIB", "missingDiskPath"), ("DATA-DOMAIN-MIB", "missingEnclosurePath"), ("DATA-DOMAIN-MIB", "interfaceConnectivityDown"), ("DATA-DOMAIN-MIB", "interfaceConnectivityIntermittent"), ("DATA-DOMAIN-MIB", "interfaceMisconfiguration"), ("DATA-DOMAIN-MIB", "interfaceConnectivityUpAndRunning"), ("DATA-DOMAIN-MIB", "duplicateAddressDetection"), ("DATA-DOMAIN-MIB", "invalidNICSlot"), ("DATA-DOMAIN-MIB", "unsupportedNIC"), ("DATA-DOMAIN-MIB", "tcpZeroWindowAlert"), ("DATA-DOMAIN-MIB", "dNSUnresponsive"), ("DATA-DOMAIN-MIB", "nISCommFailure"), ("DATA-DOMAIN-MIB", "iOModuleMacFault"), ("DATA-DOMAIN-MIB", "missingSlaveInterface"), ("DATA-DOMAIN-MIB", "nTPDFailed"), ("DATA-DOMAIN-MIB", "nvramWarning"), ("DATA-DOMAIN-MIB", "nvramBatteryAlert"), ("DATA-DOMAIN-MIB", "nvramErrorAlert"), ("DATA-DOMAIN-MIB", "nvramBatteryLowChargeAlert"), ("DATA-DOMAIN-MIB", "ext3NvlogDisabled"), ("DATA-DOMAIN-MIB", "nvramHWAlert"), ("DATA-DOMAIN-MIB", "nvramBattAlert"), ("DATA-DOMAIN-MIB", "nvramEnvAlert"), ("DATA-DOMAIN-MIB", "nvramCondAlert"), ("DATA-DOMAIN-MIB", "nvramEventHWAlert"), ("DATA-DOMAIN-MIB", "nvramBattEndOfLife"), ("DATA-DOMAIN-MIB", "phyalert"), ("DATA-DOMAIN-MIB", "mtreeQuotaSoftLimit"), ("DATA-DOMAIN-MIB", "mtreeQuotaHardLimit"), ("DATA-DOMAIN-MIB", "storageUnitStreamSoftLimit"), ("DATA-DOMAIN-MIB", "replProgressThreshholdReached"), ("DATA-DOMAIN-MIB", "replNeedResync"), ("DATA-DOMAIN-MIB", "replLogFull"), ("DATA-DOMAIN-MIB", "replIncompatibleWorm"), ("DATA-DOMAIN-MIB", "replDestNotConfigured"), ("DATA-DOMAIN-MIB", "replLagThreshholdReached"), ("DATA-DOMAIN-MIB", "replPathTooLong"), ("DATA-DOMAIN-MIB", "missingCreplUnits"), ("DATA-DOMAIN-MIB", "mtreeCascadeNeedResync"), ("DATA-DOMAIN-MIB", "insecureEncryptedReplication"), ("DATA-DOMAIN-MIB", "suspendedMReplMissingUnits"), ("DATA-DOMAIN-MIB", "sASEnclosureCheck"), ("DATA-DOMAIN-MIB", "sASTopologyCheck"), ("DATA-DOMAIN-MIB", "sASPortDisabled"), ("DATA-DOMAIN-MIB", "sASHBAFailure"), ("DATA-DOMAIN-MIB", "sASHBAErrors"), ("DATA-DOMAIN-MIB", "unsupportedSASDevice"), ("DATA-DOMAIN-MIB", "invalidEnclosureTopology"), ("DATA-DOMAIN-MIB", "diskPathSpeedDegraded"), ("DATA-DOMAIN-MIB", "enclosureMixType"), ("DATA-DOMAIN-MIB", "enclosureMixDriveType"), ("DATA-DOMAIN-MIB", "sCSITGTInvalidRegistry"), ("DATA-DOMAIN-MIB", "sSLCertificateCorrupted"), ("DATA-DOMAIN-MIB", "unusableHostCertificate"), ("DATA-DOMAIN-MIB", "missingHostCertificate"), ("DATA-DOMAIN-MIB", "expiredHostCertificate"), ("DATA-DOMAIN-MIB", "sMSUnresponsive"), ("DATA-DOMAIN-MIB", "mailserverError"), ("DATA-DOMAIN-MIB", "snapshotOver90Percent"), ("DATA-DOMAIN-MIB", "snapshotLimitReached"), ("DATA-DOMAIN-MIB", "sNTZMultipleIterations"), ("DATA-DOMAIN-MIB", "coredumpWarning"), ("DATA-DOMAIN-MIB", "coredumpDisabled"), ("DATA-DOMAIN-MIB", "spaceOver80Percent"), ("DATA-DOMAIN-MIB", "spaceOver90Percent"), ("DATA-DOMAIN-MIB", "spaceReclRestartFailed"), ("DATA-DOMAIN-MIB", "spaceReclMissingUnit"), ("DATA-DOMAIN-MIB", "spaceReclUnitReclaimed"), ("DATA-DOMAIN-MIB", "spaceReclError"), ("DATA-DOMAIN-MIB", "spaceReclSuspended"), ("DATA-DOMAIN-MIB", "spaceReclUnitError"), ("DATA-DOMAIN-MIB", "diskAccessError"), ("DATA-DOMAIN-MIB", "diskFailure"), ("DATA-DOMAIN-MIB", "diskTemperatureWarning"), ("DATA-DOMAIN-MIB", "diskTemperatureShutdown"), ("DATA-DOMAIN-MIB", "unsupportedHardwareSpareSize"), ("DATA-DOMAIN-MIB", "missingDiskGroup"), ("DATA-DOMAIN-MIB", "diskGroupReconstructionNoProgress"), ("DATA-DOMAIN-MIB", "diskGroupReconstruction"), ("DATA-DOMAIN-MIB", "diskGroupReconstructionShutdown"), ("DATA-DOMAIN-MIB", "diskGroupReconstructionCritical"), ("DATA-DOMAIN-MIB", "diskUnknown"), ("DATA-DOMAIN-MIB", "lowSpares"), ("DATA-DOMAIN-MIB", "unsupportedConfigurationROL"), ("DATA-DOMAIN-MIB", "foreignEnclosure"), ("DATA-DOMAIN-MIB", "sSDEndOfLife"), ("DATA-DOMAIN-MIB", "multipleDiskReadErrors"), ("DATA-DOMAIN-MIB", "unsupportedDriveModel"), ("DATA-DOMAIN-MIB", "driveMixType"), ("DATA-DOMAIN-MIB", "missingTierStorage"), ("DATA-DOMAIN-MIB", "storageMigrationCopyComplete"), ("DATA-DOMAIN-MIB", "storageMigrationCannotResume"), ("DATA-DOMAIN-MIB", "storageMigrationUserSuspend"), ("DATA-DOMAIN-MIB", "foreignPack"), ("DATA-DOMAIN-MIB", "upgradeFailure"), ("DATA-DOMAIN-MIB", "upgradeCompleted"), ("DATA-DOMAIN-MIB", "upgradeInProgress"), ("DATA-DOMAIN-MIB", "vDiskSCSITargetMismatch"), ("DATA-DOMAIN-MIB", "tapeReposition"), ("DATA-DOMAIN-MIB", "duplicateVTLPoolNames"), ("DATA-DOMAIN-MIB", "vTLEnabled"), ("DATA-DOMAIN-MIB", "vTLDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    generatedNotificationsGroup = generatedNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: generatedNotificationsGroup.setDescription('A collection of objects providing  notifications, automatically generated by build.')
cpismissing = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5500)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: cpismissing.setStatus('current')
if mibBuilder.loadTexts: cpismissing.setDescription('Description: \n        An archive unit is missing which could result in failure to access files in that unit.\n    \n   Action: \n        - check power connection of each shelf.\n        - check data cables of each shelf.\n        - if a hardware problem is found and fixed, restart the files system and verify that the archive unit is online.\n        - If the problem persists,  contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
controllerUnreachableAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5002)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: controllerUnreachableAlert.setStatus('current')
if mibBuilder.loadTexts: controllerUnreachableAlert.setDescription('Description: \n        This is a GDA event raised by the Master controller when it fails to reach a Worker\n        controller for more than 5 minutes. An unreachable Worker controller implies none of the Worker\n        controller interfaces are pingable from the Master controller.\n    \n   Action: \n        Check the status of network interfaces on both controllers.\n        Check network connectivity between the Master and Worker controller.\n        Make sure all cables are securely connected.\n    ')
controllerIfaceUnreachableAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5003)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: controllerIfaceUnreachableAlert.setStatus('current')
if mibBuilder.loadTexts: controllerIfaceUnreachableAlert.setDescription('Description: \n        This is a GDA event raised by the Master controller when it fails to reach a particular\n        Worker controller interface for more than 5 minutes. An unreachable interface implies that\n        it is not pingable from its Master controller equivalent interface.\n    \n   Action: \n        Check network interface status on both controllers.\n        Check network connectivity between the Master and Worker controller.\n        Make sure all cables are securely connected.\n    ')
containerMarkedInvalid = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5501)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: containerMarkedInvalid.setStatus('current')
if mibBuilder.loadTexts: containerMarkedInvalid.setDescription('Description: \n        The restorer filesystem has detected a data integrity check failure\n        due to hardware/software problems. There is potential for data loss or\n        corruption and needs immediate attention.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
cMTaskEnded = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10503)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: cMTaskEnded.setStatus('current')
if mibBuilder.loadTexts: cMTaskEnded.setDescription('Description: \n        A long running task has ended.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
correctableECCLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5004)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: correctableECCLimitReached.setStatus('current')
if mibBuilder.loadTexts: correctableECCLimitReached.setDescription('Description: \n      Single bit correctable ECC limit reached.\n    \n   Action: \n      Replace the failed DIMM(s).\n      Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
uncorrectableECCerror = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5005)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: uncorrectableECCerror.setStatus('current')
if mibBuilder.loadTexts: uncorrectableECCerror.setDescription('Description: \n      Multi bit uncorrectable ECC error.\n    \n   Action: \n      Replace the failed DIMM(s).\n      Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
dIMMFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6525)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dIMMFailure.setStatus('current')
if mibBuilder.loadTexts: dIMMFailure.setDescription('Description: \n        A fault has been detected on a memory card. The memory may no longer be usable by the system and the system may not function with the reduced memory capacity.\n    \n   Action: \n        The failing memory card must be replaced.Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
compromisedEncryptionKeys = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6001)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: compromisedEncryptionKeys.setStatus('current')
if mibBuilder.loadTexts: compromisedEncryptionKeys.setDescription('Description: \n    Data on disk may be at risk of disclosure. Data encrypted with\n    the compromised keys should be re-encrypted before shipping the disks.\n    One can get the list of compromised keys either from CLI or Enterprise Manager.\n    \n   Action: \n    Start file system cleaning to re-encrypt the affected data. \n    For extended retention systems, run space reclamation to re-encrypt affected data in the archive tier.\n    Note, these operations will take a long time to complete.\n    ')
newEncryptionKey = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6002)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: newEncryptionKey.setStatus('current')
if mibBuilder.loadTexts: newEncryptionKey.setDescription('Description: \n    Old key is still used for encrypting new data.\n    The file system needs to be restarted to activate the new key.\n    \n   Action: \n    Restart the filesystem.\n    ')
encryptionKeyTableFull = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6003)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: encryptionKeyTableFull.setStatus('current')
if mibBuilder.loadTexts: encryptionKeyTableFull.setDescription('Description: \n        Encryption key table is full. No new keys can be added until some keys are\n        deleted.\n    \n   Action: \n        Free up key table space by deleting an unused key and then add the new key.\n    ')
encryptionKeyExportFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6540)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: encryptionKeyExportFailed.setStatus('current')
if mibBuilder.loadTexts: encryptionKeyExportFailed.setDescription('Description: \n        The automatic export of the encryption keys failed.\n        This could result in encrypted data being inaccessible.\n    \n   Action: \n        Manually export the encryption keys.\n    ')
insufficientSpaceForEncryption = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7515)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: insufficientSpaceForEncryption.setStatus('current')
if mibBuilder.loadTexts: insufficientSpaceForEncryption.setDescription('Description: \n    Additional space is needed on the archive tier to encrypt the existing data.\n    Free space up to 1% of data size may be required.\n    Un-encrypted data will not get encrypted until sufficient space is available.\n    \n   Action: \n    Make free space available in the archive tier by doing one or all of the following:\n    1. Delete any unwanted data in archive tier and run space-reclamation to reclaim free space.\n    2. Expand the archive unit by adding some storage, and run space-reclamation. \n    ')
corruptEncryptionKeys = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10009)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: corruptEncryptionKeys.setStatus('current')
if mibBuilder.loadTexts: corruptEncryptionKeys.setDescription('Description: \n    File system was locked as the encryption keys cannot not be validated. One or more \n    encryption keys could be corrupt.\n  \n   Action: \n    Contact your contracted support provider or visit us online at https://support.emc.com\n  ')
legacyChassisTempWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5006)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: legacyChassisTempWarning.setStatus('current')
if mibBuilder.loadTexts: legacyChassisTempWarning.setDescription('Description: \n        Current temperature sensor reading exceeds warning threshold.\n    \n   Action: \n        Monitor temperature readings. If alert persists, check ambient room temperature and for blocked air flow.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
legacyChassisTempCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5007)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: legacyChassisTempCritical.setStatus('current')
if mibBuilder.loadTexts: legacyChassisTempCritical.setDescription('Description: \n        Current temperature sensor reading exceeds critical threshold.\n    \n   Action: \n        Check ambient room temperature and for blocked air flow.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
legacyPowerSupplyWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5008)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "powerModuleDescription"))
if mibBuilder.loadTexts: legacyPowerSupplyWarning.setStatus('current')
if mibBuilder.loadTexts: legacyPowerSupplyWarning.setDescription('Description: \n        A power supply has failed, is unplugged, or absent.\n    \n   Action: \n        Check power supply cables and LED. Replace with other working power supply.\n        If there are outstanding alerts for all power supplies in an enclosure, the\n        system must be shutdown before replacing any power supply. \n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
legacyFanWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5009)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: legacyFanWarning.setStatus('current')
if mibBuilder.loadTexts: legacyFanWarning.setDescription('Description: \n        A fan has failed.\n    \n   Action: \n        Check for any failed fan. If failed, replace with new fan.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
powerSupplyWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5010)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerSupplyWarning.setStatus('current')
if mibBuilder.loadTexts: powerSupplyWarning.setDescription('Description: \n        A power supply has failed, is unplugged, or absent.\n    \n   Action: \n        Check power supply cables and LED. Replace with other working power supply.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
fanWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5011)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: fanWarning.setStatus('current')
if mibBuilder.loadTexts: fanWarning.setDescription('Description: \n        A fan has failed or is missing.\n    \n   Action: \n        Check for any failed or missing fan. Reseat the fan.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
voltageWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5012)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: voltageWarning.setStatus('current')
if mibBuilder.loadTexts: voltageWarning.setDescription('Description: \n        Voltage sensor reading exceeds warning threshold.\n    \n   Action: \n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
powerWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5013)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerWarning.setStatus('current')
if mibBuilder.loadTexts: powerWarning.setDescription('Description: \n        Current power consumption reading exceeds warning threshold.\n    \n   Action: \n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
correctECCWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5014)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: correctECCWarning.setStatus('current')
if mibBuilder.loadTexts: correctECCWarning.setDescription('Description: \n        Memory correctable ECC errors exceed warning threshold.\n    \n   Action: \n        These memory errors are automatically corrected by the system. \n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
processorWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5016)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: processorWarning.setStatus('current')
if mibBuilder.loadTexts: processorWarning.setDescription('Description: \n        Processor status sensor alert.\n    \n   Action: \n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
powerUnitWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5017)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerUnitWarning.setStatus('current')
if mibBuilder.loadTexts: powerUnitWarning.setDescription('Description: \n        This event is expected after power off, power cycle, or AC power loss event.\n    \n   Action: \n        If this alert is not expected, check power cords and AC power.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
unCorrectECCWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5018)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unCorrectECCWarning.setStatus('current')
if mibBuilder.loadTexts: unCorrectECCWarning.setDescription('Description: \n        Memory uncorrectable ECC error alert.\n    \n   Action: \n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
chassisSensorCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5020)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: chassisSensorCritical.setStatus('current')
if mibBuilder.loadTexts: chassisSensorCritical.setDescription('Description: \n        Current sensor reading or state exceeds critical condition.\n    \n   Action: \n        Check the specific alert message for information.\n        Monitor temperature readings. If alert persists, check ambient room temperature \n        and for blocked air flow. \n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
chassisTempWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5021)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: chassisTempWarning.setStatus('current')
if mibBuilder.loadTexts: chassisTempWarning.setDescription('Description: \n        Current temperature sensor reading exceeds warning threshold.\n    \n   Action: \n        Monitor temperature readings. If alert persists, check ambient room temperature \n        and for blocked air flow. \n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
chassisTempCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5022)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: chassisTempCritical.setStatus('current')
if mibBuilder.loadTexts: chassisTempCritical.setDescription('Description: \n        Current temperature sensor reading exceeds critical threshold.\n    \n   Action: \n        Check ambient room temperature and for blocked air flow. \n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
cPUFailureWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5023)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: cPUFailureWarning.setStatus('current')
if mibBuilder.loadTexts: cPUFailureWarning.setDescription('Description: \n        DDOS has detected a fault with the indicated CPU.\n    \n   Action: \n         Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
legacyBMCHangCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5024)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: legacyBMCHangCritical.setStatus('current')
if mibBuilder.loadTexts: legacyBMCHangCritical.setDescription('Description: \n        While BMC is unresponsive, environmental monitoring and remote access via IPMI is not operational.\n        This could mask serious problems such as overheating.\n    \n   Action: \n        Use CLI or Enterprise Manager to check fan, voltage, and power supply readings.\n        If the system fails to fetch the readings, gracefully shut down the system and pull out all power cables to reset BMC.\n        Wait until all LEDS are off. Reinsert the power cables and then power the system up.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
bMCHangCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5025)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: bMCHangCritical.setStatus('current')
if mibBuilder.loadTexts: bMCHangCritical.setDescription('Description: \n        While BMC is unresponsive, environmental monitoring and remote access via IPMI is not operational.\n        This could mask serious problems such as overheating.\n    \n   Action: \n        Use CLI or Enterprise Manager to check fan, voltage, and power supply readings.\n        If the system fails to fetch the readings, gracefully shut down the system and pull out all power cables to reset BMC.\n        Wait until all LEDS are off. Reinsert the power cables and then power the system up.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
abnormalShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5026)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: abnormalShutdown.setStatus('current')
if mibBuilder.loadTexts: abnormalShutdown.setDescription('Description: \n        The system has been shutdown by abnormal method, i.e. not by one of the following: \n        1) Via IPMI chassis control command \n        2) Via power button\n        3) Via OS shutdown\n    \n   Action: \n        This alert is expected after loss of AC (main power) event.\n        If this shutdown is not expected and persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
smiMrc = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5502)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: smiMrc.setStatus('current')
if mibBuilder.loadTexts: smiMrc.setDescription('Description: \n        BIOS SMI MRC interrupt\n    \n   Action: \n        Check if system memory size has been decreased due to a DIMM has been disabled.\n        If yes, replace the bad DIMM.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
bMCPartialHang = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6015)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: bMCPartialHang.setStatus('current')
if mibBuilder.loadTexts: bMCPartialHang.setDescription('Description: \n        BMC firmware is not responsive.\n    \n   Action: \n        Use CLI or Enterprise Manager to check fan, voltage, and power supply readings.\n        If the system fails to fetch the readings, gracefully shut down the system and pull out all power cables to reset BMC.\n        Wait until all LEDS are off. Reinsert the power cables and then power the system up.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
fanFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6517)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: fanFault.setStatus('current')
if mibBuilder.loadTexts: fanFault.setDescription('Description: \n        A hardware fault has been detected in an enclosure cooling fan. This may allow the enclosure to overheat.\n    \n   Action: \n        The fan must be replaced. Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
powerSupplyInputFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6518)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerSupplyInputFault.setStatus('current')
if mibBuilder.loadTexts: powerSupplyInputFault.setDescription('Description: \n        A power loss has been detected in an enclosure power supply.  This can be caused by a loss of AC power to one power supply.\n    \n   Action: \n        Check if AC main power is available to the system. \n        Check if power supply cables are properly connected.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com to replace the power supply. \n    ')
powerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6519)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerSupplyFailure.setStatus('current')
if mibBuilder.loadTexts: powerSupplyFailure.setDescription('Description: \n        A power loss has been detected in an enclosure power supply.  This can be caused by a failure in the power supply.\n    \n   Action: \n        Power supply needs to be replaced. Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
powerSupplyAbsent = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6520)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerSupplyAbsent.setStatus('current')
if mibBuilder.loadTexts: powerSupplyAbsent.setDescription('Description: \n        An enclosure power supply is absent.\n    \n   Action: \n        Power supply needs to be replaced. Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
unsupportedACVoltage = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6521)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedACVoltage.setStatus('current')
if mibBuilder.loadTexts: unsupportedACVoltage.setDescription('Description: \n        The power supply for this enclosure is connected to an unsupported AC voltage. \n        The system may operate at a reduced capacity or unexpectedly shut down.\n    \n   Action: \n         Replace the input power with the supported voltage.\n    ')
iOModuleFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6522)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: iOModuleFault.setStatus('current')
if mibBuilder.loadTexts: iOModuleFault.setDescription('Description: \n        A fault has been detected with an I/O module and it will not function correctly.\n    \n   Action: \n        The I/O module must be replaced.Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
iOModuleInserted = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6523)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: iOModuleInserted.setStatus('current')
if mibBuilder.loadTexts: iOModuleInserted.setDescription('Description: \n        An I/O module has been inserted during system runtime. The I/O module will not be powered on until the system is restarted.\n    \n   Action: \n        Restart the system to activate this module.\n    ')
mgmtModuleFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6524)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: mgmtModuleFault.setStatus('current')
if mibBuilder.loadTexts: mgmtModuleFault.setDescription('Description: \n        A fault has been detected in the management I/O module. Management functions requiring the I/O module will not work.\n    \n   Action: \n        The management I/O module must be replaced.Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
sPFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6526)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sPFault.setStatus('current')
if mibBuilder.loadTexts: sPFault.setDescription('Description: \n        A fault has been detected on the storage processor. The system may experience unexpected behavior.\n    \n   Action: \n        The failed storage processor must be replaced.Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
chassisFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6527)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: chassisFailure.setStatus('current')
if mibBuilder.loadTexts: chassisFailure.setDescription('Description: \n        A fault has been detected in one of the chassis components. The system may experience unexpected behavior. \n    \n   Action: \n        The chassis must be replaced.Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
forcedControllerShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6528)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: forcedControllerShutdown.setStatus('current')
if mibBuilder.loadTexts: forcedControllerShutdown.setDescription('Description: \n        An environmental condition or hardware fault has been detected that may cause significant damage to the hardware or possible data loss, and the system unit is being shut down.\n    \n   Action: \n        Check the environment, If the system environment is at a normal state, restart the system and review the alert history to determine the source of the problem.\n        Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
systemReset = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6529)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: systemReset.setStatus('current')
if mibBuilder.loadTexts: systemReset.setDescription('Description: \n        A critical failure caused the system to unexpectedly shut down.\n        The system was able to boot successfully either because the fault was corrected, the fault was transient, or the system was able to boot without the component causing the fault.\n    \n   Action: \n        Review the system for earlier alerts to determine the cause of the unexpected shut down.\n        Check the system inventory to verify all components are configured as expected. \n        If this alert is issued again, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
enclosureHighTemp = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6535)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: enclosureHighTemp.setStatus('current')
if mibBuilder.loadTexts: enclosureHighTemp.setDescription('Description: \n        The temperature inside the enclosure is high and has exceeded the warning threshold.If no action is taken and the temperature continue to increase, the system will shut down.\n    \n   Action: \n        If the temperature around the system unit is within the documented operating limits and the air flow is not blocked,\n        Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
unsupportedSystemType = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6536)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedSystemType.setStatus('current')
if mibBuilder.loadTexts: unsupportedSystemType.setDescription('Description: \n            An unsupported system type has been detected and needs \n            to be modified or replaced.\n        \n   Action: \n            Contact your contracted support provider or visit us online at https://support.emc.com\n        ')
bMCHangShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6537)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: bMCHangShutdown.setStatus('current')
if mibBuilder.loadTexts: bMCHangShutdown.setDescription('Description: \n       While BMC is unresponsive, environmental monitoring and remote access via IPMI is not operational.  This could mask serious problems such as overheating.\n    \n   Action: \n        After the system is shut down, pull out all power cables from the controller to reset BMC.\n        Wait until all LEDs are off, reinsert the power cables, and then power the system up.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
bMCFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7000)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: bMCFailure.setStatus('current')
if mibBuilder.loadTexts: bMCFailure.setDescription('Description: \n        BMC is unresponsive or unable to access some required information. This may be corrected by a BMC reset procedure. If the condition is serious, the file system will be disabled.\n    \n   Action: \n        Shut the system down and pull out all power cables from the controller to reset BMC.\n        Wait until all LEDs are off, reinsert the power cables, and then power the system up.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
unsupportedHardwareConfig = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7502)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedHardwareConfig.setStatus('current')
if mibBuilder.loadTexts: unsupportedHardwareConfig.setDescription('Description: \n        Unsupported virtual machine hardware configuration was detected.  \n        This configuration may cause unexpected behavior.\n    \n   Action: \n        Fix the hardware configuration to resolve the problem.\n        If problem persists, restart the system.\n    ')
unsupportedVirtualCPU = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7503)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedVirtualCPU.setStatus('current')
if mibBuilder.loadTexts: unsupportedVirtualCPU.setDescription('Description: \n            The current number of CPU sockets and cores in the \n            virtual machine configuration is not valid for the \n            current storage capacity. The file system will not \n            be enabled.\n        \n   Action: \n            Power off this virtual machine instance and change \n            the virtual machine configuration to match the supported values. \n            If you made this change to add storage capacity, you must \n            add the additional capacity before enabling the file system.\n        ')
unsupportedPowerSupply = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10001)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedPowerSupply.setStatus('current')
if mibBuilder.loadTexts: unsupportedPowerSupply.setDescription('Description: \n        The installed power supply is an unsupported model.\n        The system may exhibit unexpected behavior.\n    \n   Action: \n        Replace the power supply with a supported model.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
openFanDrawer = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10002)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: openFanDrawer.setStatus('current')
if mibBuilder.loadTexts: openFanDrawer.setDescription('Description: \n        Fan drawer is not closed securely.\n        Failure to secure the fan drawer may allow the system to overheat and shut down.\n    \n   Action: \n        Close and secure the fan drawer.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
memoryRiserFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10003)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: memoryRiserFault.setStatus('current')
if mibBuilder.loadTexts: memoryRiserFault.setDescription('Description: \n        A critical failure has been detected in a memory riser.\n        Memory attached to this riser may disappear from the system inventory.\n        The system may exhibit unexpected behavior.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com to replace the memory riser.\n    ')
bMCFailureSysBBU = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7524)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: bMCFailureSysBBU.setStatus('current')
if mibBuilder.loadTexts: bMCFailureSysBBU.setDescription('Description: \n        BMC is unresponsive or unable to access some required information. This may be corrected by a BMC reset procedure. If the condition is serious, the file system will be disabled.\n    \n   Action: \n        Shut the system down and remove all external power sources from the controller.\n        Remove the system battery backup unit (BBU).\n        Wait until all LEDs are off, reinsert the BBU, connect external power, and then power the system up.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
unsupportedEnclosurePSU = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10000)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedEnclosurePSU.setStatus('current')
if mibBuilder.loadTexts: unsupportedEnclosurePSU.setDescription('Description: \n        A power supply has been detected in an enclosure which does not provide complete environmental information. \n        This will not affect normal operations but should be replaced as soon as convenient.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
pCILinkDegraded = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10004)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: pCILinkDegraded.setStatus('current')
if mibBuilder.loadTexts: pCILinkDegraded.setDescription('Description: \n        The system has detected that PCI communication speed is degraded.\n        This will not cause the system to fail but may impact performance of affected components.\n    \n   Action: \n        Reboot the system.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
invalidHardwareCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10005)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: invalidHardwareCritical.setStatus('current')
if mibBuilder.loadTexts: invalidHardwareCritical.setDescription('Description: \n        During device inventory verification, the system found missing or invalid hardware, or devices installed in the wrong location. \n        The filesystem cannot be enabled with the current hardware configuration.\n        \n   Action: \n        View enclosure misconfiguration to determine the problem.\n        For assistance, contact your contracted support provider or visit us online at https://support.emc.com.\n        ')
invalidHardwareWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10006)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: invalidHardwareWarning.setStatus('current')
if mibBuilder.loadTexts: invalidHardwareWarning.setDescription('Description: \n        During device inventory verification, the system found missing or invalid hardware, or devices installed in the wrong location. \n        Some components may not operate as expected.\n        \n   Action: \n        View enclosure misconfiguration to determine the problem.\n        For assistance, contact your contracted support provider or visit us online at https://support.emc.com.\n        ')
correctableErrorWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10007)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: correctableErrorWarning.setStatus('current')
if mibBuilder.loadTexts: correctableErrorWarning.setDescription('Description: \n        The system has detected excessive correctable errors on a component that may indicate a hardware failure.\n    \n   Action: \n         Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
generalHardwareFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10011)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: generalHardwareFailure.setStatus('current')
if mibBuilder.loadTexts: generalHardwareFailure.setDescription('Description: \n        A critical failure has been detected in one or more chassis components.\n        The system may exhibit unexpected behavior.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
targetDriverPortOffline = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7508)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortOffline.setStatus('current')
if mibBuilder.loadTexts: targetDriverPortOffline.setDescription('Description: \n        No connection is detected on the Fibre Channel Port. \n    \n   Action: \n        If this port is not in use, please disable it. If port is being\n        used, please restore Fibre Channel Port connectivity. Alert will be cleared\n        when port is disabled or online.\n    ')
targetDriverPortOnline = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7509)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortOnline.setStatus('current')
if mibBuilder.loadTexts: targetDriverPortOnline.setDescription('Description: \n        Fibre Channel Port is online. \n    \n   Action: \n        No action required\n    ')
targetDriverPortCore = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7510)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortCore.setStatus('current')
if mibBuilder.loadTexts: targetDriverPortCore.setDescription('Description: \n        An error occurred on the Fibre Channel Port that resulted in a HBA core. \n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com to extract and analyze the HBA core.\n    ')
targetDriverPortMultipleCore = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7511)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortMultipleCore.setStatus('current')
if mibBuilder.loadTexts: targetDriverPortMultipleCore.setDescription('Description: \n        An error occurred on the Fibre Channel Port that caused multiple HBA core attempts. The Fibre Channel Port is disabled. \n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com to replace Fibre Channel HBA.\n    ')
targetDriverPortFWLoadFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7512)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortFWLoadFailed.setStatus('current')
if mibBuilder.loadTexts: targetDriverPortFWLoadFailed.setDescription('Description: \n        The Fibre Channel Port is unable to load required firmware. The Fibre Channel Port is disabled. \n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com to replace Fibre Channel HBA.\n    ')
targetDriverPortUnreadable = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7513)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortUnreadable.setStatus('current')
if mibBuilder.loadTexts: targetDriverPortUnreadable.setDescription('Description: \n        Unable to access one or more resources on the HBA. The Fibre Channel Port is disabled. \n    \n   Action: \n        Contact contact your contracted support provider or visit us online at https://support.emc.com to replace Fibre Channel HBA.\n    ')
targetDriverPortTooManyOsc = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7514)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortTooManyOsc.setStatus('current')
if mibBuilder.loadTexts: targetDriverPortTooManyOsc.setDescription('Description: \n        The system has detected a Fibre Channel Port has been transitioning\n        between online and offline too frequently. This may cause disruption in i/o.\n    \n   Action: \n        Please ensure stable port connectivity. Disable the port if it is not in use.\n    ')
tooManyRelaunches = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5027)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: tooManyRelaunches.setStatus('current')
if mibBuilder.loadTexts: tooManyRelaunches.setDescription('Description: \n    The filesystem has failed to restart after multiple attempts.  Backup and restore services are unavailable.\n    \n   Action: \n    Contact your contracted support provider or visit us online at https://support.emc.com to diagnose the failure.\n    ')
filesystemProblem = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5028)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: filesystemProblem.setStatus('current')
if mibBuilder.loadTexts: filesystemProblem.setDescription('Description: \n    A problem is preventing the filesystem from running. This usually \n    involves the storage being unavailable.\n    \n   Action: \n    Check disk shelf cabling.  If problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
dDFSFailedInShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5030)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dDFSFailedInShutdown.setStatus('current')
if mibBuilder.loadTexts: dDFSFailedInShutdown.setDescription('Description: \n    The filesystem shut down encountered an error. This can potentially leave data in the NVRAM \n    which would be normally flushed to the disk.  Failed shutdown can leave the filesystem in a \n    state that can prevent certain operations from being performed (i.e. system upgrade,\n    filesys destroy, etc.) and may cause data loss.\n    \n   Action: \n    Re-enable the filesystem and try shutting it down again. If the problem persists, \n    Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
dDFSNoHeartbeat = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5034)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dDFSNoHeartbeat.setStatus('current')
if mibBuilder.loadTexts: dDFSNoHeartbeat.setDescription('Description: \n    Filesystem has encountered an error and is forced to restart.\n    \n   Action: \n    If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
dDFSDiedAfterReboot = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5036)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dDFSDiedAfterReboot.setStatus('current')
if mibBuilder.loadTexts: dDFSDiedAfterReboot.setDescription('Description: \n    The filesystem failed to startup immediately after system reboot.\n    \n   Action: \n    Contact your contracted support provider or visit us online at https://support.emc.com for diagnosis of the cause of failure. No other \n    action required if filesystem successfully restarts.\n    ')
dDFSDied = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5037)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dDFSDied.setStatus('current')
if mibBuilder.loadTexts: dDFSDied.setDescription('Description: \n    The filesystem process failed and is restarting.\n    \n   Action: \n    Contact your contracted support provider or visit us online at https://support.emc.com for diagnosis of the cause of failure. No other \n    action required if filesystem successfully restarts.\n    ')
dDFSRebooted = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5038)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: dDFSRebooted.setStatus('current')
if mibBuilder.loadTexts: dDFSRebooted.setDescription('Description: \n    This is just a notification alert that the system has been rebooted.\n    \n   Action: \n    No action required.\n    ')
dDFSRebootedDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5039)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: dDFSRebootedDisabled.setStatus('current')
if mibBuilder.loadTexts: dDFSRebootedDisabled.setDescription("Description: \n    This is a notification alert sent out during system startup following a \n    reboot. The system is rebooted with the filesystem in disabled state.\n    \n   Action: \n    No action is required unless the intent is to have the filesystem enabled. \n    In that case, invoke the 'filesys enable' command.\n    ")
indexRebuildComplete = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5040)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: indexRebuildComplete.setStatus('current')
if mibBuilder.loadTexts: indexRebuildComplete.setDescription('Description: \n        The metadata rebuild operation that was started by support has completed. The system is ready for the next action. \n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com to perform the next operation on your system. \n    ')
filesystemNVRAMDataLoss = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6005)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: filesystemNVRAMDataLoss.setStatus('current')
if mibBuilder.loadTexts: filesystemNVRAMDataLoss.setDescription('Description: \n       Filesystem cannot be enabled because of NVRAM mismatch. This can happen because of an improper headswap or NVRAM card replacement operation.\n    \n   Action: \n      Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
recoverFromNVRAMFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6013)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: recoverFromNVRAMFailed.setStatus('current')
if mibBuilder.loadTexts: recoverFromNVRAMFailed.setDescription('Description: \n        Due to NVRAM issues, filesystem has been disabled in order to maintain data integrity.\n        No backups will run until this problem is resolved.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
dDFSRequiresReboot = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7516)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dDFSRequiresReboot.setStatus('current')
if mibBuilder.loadTexts: dDFSRequiresReboot.setDescription('Description: \n    File system was unable to start because an abnormal internal\n    condition was detected.\n    \n   Action: \n    Reboot the system. If problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
metadataWarningThreshold = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7519)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: metadataWarningThreshold.setStatus('current')
if mibBuilder.loadTexts: metadataWarningThreshold.setDescription('Description: \n        Large amount of metadata has been created by the filesystem.\n        Continuing without cleaning would cause the filesystem to enter into read-only mode.\n    \n   Action: \n        Clean the filesystem as soon as possible.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
filesystemCorruption = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7521)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: filesystemCorruption.setStatus('current')
if mibBuilder.loadTexts: filesystemCorruption.setDescription('Description: \n        Filesystem processing detected some corruption.\n        This may be isolated to a single file or multiple files, \n        preventing you from reading the corrupted files. \n        If a system file is affected, the filesystem could be disabled.\n        Until this corruption is fixed, you will not be able to run cleaning,\n        data-movement or space reclamation on the affected tier.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
physicalCapacityMeasurementTasksLost = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10504)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: physicalCapacityMeasurementTasksLost.setStatus('current')
if mibBuilder.loadTexts: physicalCapacityMeasurementTasksLost.setDescription('Description: \n        File system has been disabled either by a failure or user action.\n        Physical-capacity-measurement samples for these tasks are no longer available.\n    \n   Action: \n        Restart physical-capacity-measurement sample tasks that have not completed.\n    ')
physicalCapacityMeasurementTasksLostMTree = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10505)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: physicalCapacityMeasurementTasksLostMTree.setStatus('current')
if mibBuilder.loadTexts: physicalCapacityMeasurementTasksLostMTree.setDescription('Description: \n        MTree replication was broken or resynced causing one or more physical-capacity-measurement sample tasks to be cancelled.\n        Physical-capacity-measurement samples for these tasks are no longer available.\n    \n   Action: \n        Restart physical-capacity-measurement sample tasks that have not completed for this MTree.\n    ')
physicalCapacityMeasurementScheduleFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10506)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: physicalCapacityMeasurementScheduleFailed.setStatus('current')
if mibBuilder.loadTexts: physicalCapacityMeasurementScheduleFailed.setDescription('Description: \n        A physical-capacity-measurement sample task that was scheduled to run was unable to start due to an error.\n        Some or all of the physical-capacity-measurement samples for these tasks are not available.\n    \n   Action: \n        Review scheduled physical-capacity-measurement sample task errors to determine the reason for the failure.\n        Resubmit failed tasks if needed.\n    ')
uncertifiedFirmware = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6004)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: uncertifiedFirmware.setStatus('current')
if mibBuilder.loadTexts: uncertifiedFirmware.setDescription('Description: \n    Firmware version is not compatible with this version of DDOS and may cause unexpected behavior.\n    \n   Action: \n    The firmware must be updated as soon as possible, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
fileMigrationError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6016)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: fileMigrationError.setStatus('current')
if mibBuilder.loadTexts: fileMigrationError.setDescription('Description: \n        File migration is suspended until this problem is resolved.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
cleaningError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6014)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: cleaningError.setStatus('current')
if mibBuilder.loadTexts: cleaningError.setDescription('Description: \n        Unable to reclaim unused space and this may impact the ability to backup.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
hAdegraded = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10508)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: hAdegraded.setStatus('current')
if mibBuilder.loadTexts: hAdegraded.setDescription('Description: \n       A condition has been detected causing the configured HA system to be degraded.\n       Any failover attempt will not succeed.\n    \n   Action: \n       Display the HA detailed status to determine the failed component.\n       Repairing the failed component can return the HA system to available state.\n    ')
hAofflineErrors = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10510)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: hAofflineErrors.setStatus('current')
if mibBuilder.loadTexts: hAofflineErrors.setDescription('Description: \n       Critical system errors have been detected causing the configured HA system to be in offline state.\n       Access to system services may be unavailable.\n    \n   Action: \n       Review exisiting alerts.\n       Fixing issues identified by these alerts may resolve this alert.\n       If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
hATimeOutOfSync = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10514)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: hATimeOutOfSync.setStatus('current')
if mibBuilder.loadTexts: hATimeOutOfSync.setDescription('Description: \n       Timestamps of logs and system events will not match between the HA nodes.\n       This condition will not have an effect on HA functionality or system operation.\n    \n   Action: \n       Set the time on the standby node to match the active node.\n       If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
historicalDatabaseRecoverError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5041)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: historicalDatabaseRecoverError.setStatus('current')
if mibBuilder.loadTexts: historicalDatabaseRecoverError.setDescription('Description: \n        All existing historical data has been lost. Data in the historical\n        database is used for some system reports, but it is not required for proper\n        system functioning. This failure may occur during head swap processing if\n        recovery to create the new head primary historical database from the shelf\n        database files fails or historical database may be corrupted.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com\n        to debug this problem and possibly attempt recovery of the lost historical data.\n    ')
historicalDatabaseBackupError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5042)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: historicalDatabaseBackupError.setStatus('current')
if mibBuilder.loadTexts: historicalDatabaseBackupError.setDescription('Description: \n        Historical database backup failed. If the primary historical\n        database fails without a recent backup present, some or all of the historical\n        data can be lost when the primary historical database is restored from its\n        backup and log files. Data in the historical database is used for some system\n        reports, but it is not required for proper system functioning.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com\n        to help debug the problem.\n    ')
historicalDatabaseUpgradeError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5043)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: historicalDatabaseUpgradeError.setStatus('current')
if mibBuilder.loadTexts: historicalDatabaseUpgradeError.setDescription('Description: \n            Historical database upgrade failed during software upgrade.  New historical\n            data fields will not be saved.  Some UI reports might be unavailable, or\n            be missing data. Otherwise, this should not affect the system.\n        \n   Action: \n            Contact your contracted support provider or visit us online at https://support.emc.com\n            to help debug the problem and upgrade the historical database.\n        ')
historicalDatabasePruneError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5044)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: historicalDatabasePruneError.setStatus('current')
if mibBuilder.loadTexts: historicalDatabasePruneError.setDescription('Description: \n            Historical database pruning failed.  Pruning ensures the historical database\n            does not consume more than its allocated disk space.\n        \n   Action: \n            Contact your contracted support provider or visit us online at https://support.emc.com\n            to help debug the problem.\n        ')
noHistoricalDatabaseError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5045)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: noHistoricalDatabaseError.setStatus('current')
if mibBuilder.loadTexts: noHistoricalDatabaseError.setDescription('Description: \n        Data in the historical database is used for some system reports,\n        but it is not required for proper system functioning. This failure may occur\n        during head swap processing if recovery to create the new head primary\n        historical database from the shelf database files fails or the database has\n        been corrupted. The system is running without historical database after failing\n        to create a new one.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com\n        to debug this problem and possibly attempt recovery of the lost historical data.\n    ')
historicalDatabaseFailoverError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10507)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: historicalDatabaseFailoverError.setStatus('current')
if mibBuilder.loadTexts: historicalDatabaseFailoverError.setDescription('Description: \n            Historical database failover failed.\n        \n   Action: \n            Contact your contracted support provider or visit us online at https://support.emc.com\n            to help debug the problem.\n        ')
hDTFileTransferFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5046)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: hDTFileTransferFailed.setStatus('current')
if mibBuilder.loadTexts: hDTFileTransferFailed.setDescription('Description: \n\t\tUnable to send historical data update file to Data Domain Management Center.\n    \n   Action: \n\t\tCheck DNS settings and network connection between the Data Domain\n\t\tSystem and Data Domain Management Center.  If the problem persists,\n\t\tcontact your contracted support provider or visit us online at https://support.emc.com.\n    ')
hDTSystemError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5047)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: hDTSystemError.setStatus('current')
if mibBuilder.loadTexts: hDTSystemError.setDescription('Description: \n\t\tSystem Error occurred while sending historical data to Data Domain Management Center.\n    \n   Action: \n\t\tCheck configuration and system status, messages logs for indicative problems.\n\t\tIf the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
spuriousInterruptDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10008)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spuriousInterruptDisabled.setStatus('current')
if mibBuilder.loadTexts: spuriousInterruptDisabled.setDescription('Description: \n       Excessive spurious hardware messages have been detected that may indicate a hardware failure.\n    \n   Action: \n       Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
licenseExpiring = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 8001)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: licenseExpiring.setStatus('current')
if mibBuilder.loadTexts: licenseExpiring.setDescription('Description: \n        The temporary license indicated is about to expire. The function provided by this license will cease to operate.\n    \n   Action: \n        Contact your [account team] to purchase a license if you wish to continue to use this feature.\n    ')
licenseExpired = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 8002)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: licenseExpired.setStatus('current')
if mibBuilder.loadTexts: licenseExpired.setDescription('Description: \n        The temporary license indicated has expired. The function provided by this license has stopped operating.\n    \n   Action: \n        Contact your [account team] to purchase a license if you wish to use this feature.\n    ')
dIMMFailureAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5048)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dIMMFailureAlert.setStatus('current')
if mibBuilder.loadTexts: dIMMFailureAlert.setDescription("Description: \n            DIMM failure detected. DDFS can't be enabled.\n        \n   Action: \n            Replace the bad DIMMS.\n        ")
memoryAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5049)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: memoryAlert.setStatus('current')
if mibBuilder.loadTexts: memoryAlert.setDescription("Description: \n            Current memory is less than configured. DDFS can't be enabled.\n        \n   Action: \n            Check the DIMMS in DDR. Add new DIMMS and/or replace the bad DIMMS.\n        ")
portPathDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5050)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: portPathDisabled.setStatus('current')
if mibBuilder.loadTexts: portPathDisabled.setDescription('Description: \n        A path is disabled. Multipath failover will not work correctly until the port is enabled.\n    \n   Action: \n        Verify all storage cabling is connected correctly.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com. \n    ')
diskPathRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5051)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskPathRedundancy.setStatus('current')
if mibBuilder.loadTexts: diskPathRedundancy.setDescription("Description: \n        Since only one HBA controller has been detected, disk path redundancy is lost.\n    \n   Action: \n        If the HBA configuration is correct, disable multipath configuration. Otherwise: 1)Use \n        'disk multipath status' to examine connection status; 2)Verify all storage cabling is connected \n        correctly; 3)Use 'enclosure' commands to verify that HBA controllers are functional.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ")
missingPortConnection = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5052)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingPortConnection.setStatus('current')
if mibBuilder.loadTexts: missingPortConnection.setDescription('Description: \n        A port and the attached storage have disappeared.\n    \n   Action: \n        Verify the connection and any external storage connected to the missing port.\n    ')
missingLunPath = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5053)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingLunPath.setStatus('current')
if mibBuilder.loadTexts: missingLunPath.setDescription('Description: \n        The number of active paths to a LUN has changed.\n    \n   Action: \n        If this is due to reconfiguration, verify the topology and disable then re-enable\n        multipath monitoring to reset the monitoring. If not, verify the storage cabling and that\n        all paths are connected.\n    ')
missingDiskPath = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5054)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: missingDiskPath.setStatus('current')
if mibBuilder.loadTexts: missingDiskPath.setDescription('Description: \n        The number of active paths to a disk has decreased. Multipath redundancy has been lost\n        unless there are more than one connection paths.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
missingEnclosurePath = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5055)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingEnclosurePath.setStatus('current')
if mibBuilder.loadTexts: missingEnclosurePath.setDescription("Description: \n        The number of active paths to a disk has decreased. Multipath redundancy has been lost\n        unless there are more than one connection paths.\n    \n   Action: \n        Use 'enclosure' commands to verify that HBAs are functional.\n        If this condition is due to configuration change: verify the topology, and then disable and \n        re-enable disk multipath monitoring to reset connection counts.\n        If not, verify the storage cabling is connected correctly.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ")
interfaceConnectivityDown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6009)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: interfaceConnectivityDown.setStatus('current')
if mibBuilder.loadTexts: interfaceConnectivityDown.setDescription("Description: \n        Network connectivity on this interface is down.\n        This interface is not pingable and cannot be used to send or receive any data.\n        All data transfers using this interface will fail.  \n    \n   Action: \n       Please view the Hardware->Network GUI page, or use the 'net show settings' and 'net show config' CLIs to check the current configuration.\n       Make sure that the cable is securely connected to both endpoints and that the interfaces on both ends are properly configured.\n       Otherwise the cable or network hardware could be faulty and may need to be replaced.\n    ")
interfaceConnectivityIntermittent = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6010)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: interfaceConnectivityIntermittent.setStatus('current')
if mibBuilder.loadTexts: interfaceConnectivityIntermittent.setDescription("Description: \n        Network connectivity on this interface is intermittent. Data may not be sent or received successfully. \n        Data transfers using this interface may experience performance degradation or intermittent failures.\n    \n   Action: \n        Please view the Hardware->Network GUI page, or use the 'net show settings' and 'net show config' CLIs to check the current configuration.\n        Make sure that the cable is securely connected to both endpoints and that the interfaces on both ends are properly configured.\n        Otherwise the cable or network hardware could be faulty and may need to be replaced.\n        If the network is configured properly and the problem still persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ")
interfaceMisconfiguration = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6011)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: interfaceMisconfiguration.setStatus('current')
if mibBuilder.loadTexts: interfaceMisconfiguration.setDescription("Description: \n        Network interface configuration problem detected. This may be a result of changing the NIC hardware without reconfiguring the interface.\n        This could indicate an unsupported configuration, network environment or hardware problem.\n        A misconfigured interface can potentially cause connectivity problems on subsequent reboots.\n    \n   Action: \n        Please view the Hardware->Network GUI page, or use 'net show settings', 'net config' and 'net show hardware' to check network configuration.\n        Try to fix the problem by reconfiguring the interface with 'net config'.\n    ")
interfaceConnectivityUpAndRunning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6020)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: interfaceConnectivityUpAndRunning.setStatus('current')
if mibBuilder.loadTexts: interfaceConnectivityUpAndRunning.setDescription('Description: \n        Network interface is up and running for a period of time after experiencing instability.\n    \n   Action: \n        No action needed.\n    ')
duplicateAddressDetection = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6530)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: duplicateAddressDetection.setStatus('current')
if mibBuilder.loadTexts: duplicateAddressDetection.setDescription('Description: \n        This IP address has been detected on the network. Connections to this IP address will be adversely impacted.\n    \n   Action: \n        Make sure the local and remote systems are using different IP addresses. Clear the alert once the problem is resolved.\n    ')
invalidNICSlot = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6512)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: invalidNICSlot.setStatus('current')
if mibBuilder.loadTexts: invalidNICSlot.setDescription('Description: \n        Network interface cards must be installed in their designated slots.\n        The network card may not function correctly when installed in the wrong slot.\n    \n   Action: \n        Please make sure that the Network interface card is installed in a valid slot.\n    ')
unsupportedNIC = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6513)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedNIC.setStatus('current')
if mibBuilder.loadTexts: unsupportedNIC.setDescription('Description: \n        An unsupported network interface card is installed in the system.\n        Having an unsupported card installed in the system can cause unexpected errors.\n    \n   Action: \n        Remove the card from system.\n    ')
tcpZeroWindowAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6101)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: tcpZeroWindowAlert.setStatus('current')
if mibBuilder.loadTexts: tcpZeroWindowAlert.setDescription('Description: \n        The TCP connection is active but data is not being transferred.\n        This may cause other communication failures.\n    \n   Action: \n        Check the remote application that uses this TCP connection.\n        Check the network path between the local and remote systems.\n        If problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
dNSUnresponsive = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7504)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dNSUnresponsive.setStatus('current')
if mibBuilder.loadTexts: dNSUnresponsive.setDescription('Description: \n        No DNS servers responded to a DNS query. This may be caused by a network failure or a DNS server problem.\n        System functions that require name address resolution will fail.\n    \n   Action: \n        Check the network path and the DNS server to establish communication or remove the DNS entries and add host entries to the hosts table.\n        If this problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
nISCommFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7501)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nISCommFailure.setStatus('current')
if mibBuilder.loadTexts: nISCommFailure.setDescription('Description: \n        Unable to query information from the NIS server. \n        This could be a network problem or an authentication failure with the NIS server.\n        This could prevent NIS servers from completing backups or restoring existing backups.\n        This alert will clear when communication is established with the NIS server.\n    \n   Action: \n        Verify network connection to the NIS server and verify NIS configurations for both systems.\n        If this problem persists, contact your contracted support provider or visit us online at https://support.emc.com .\n    ')
iOModuleMacFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10013)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: iOModuleMacFault.setStatus('current')
if mibBuilder.loadTexts: iOModuleMacFault.setDescription('Description: \n        A Mac fault has been detected with an I/O module and it will not function correctly.\n    \n   Action: \n        The I/O module must be replaced.Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
missingSlaveInterface = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10523)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingSlaveInterface.setStatus('current')
if mibBuilder.loadTexts: missingSlaveInterface.setDescription('Description: \n        The bonded interface has been created with the remaining interfaces and\n        may experience degraded performance or reduced failover capability.\n    \n   Action: \n        Replace the network interface or reconfigure the bonded interface to\n        restore functionality. If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
nTPDFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7505)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nTPDFailed.setStatus('current')
if mibBuilder.loadTexts: nTPDFailed.setDescription('Description: \n      Network Time Protocol (NTP) daemon is not running. NTP daemon has detected a\n      time difference between this system and the configured network time server\n      (drift) greater than the configured maximum and has shut down.\n    \n   Action: \n      Disable NTP. Verify time on the NTP server. Set system date/time to match the\n      time on the NTP server. Enable NTP. If this problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
nvramWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5059)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramWarning.setStatus('current')
if mibBuilder.loadTexts: nvramWarning.setDescription('Description: \n\t\t\tDDFS is disabled due to a problem with the NVRAM subsystem.\n        \n   Action: \n\t\t\tCheck for other NVRAM-related alerts and follow the action described in those alerts.\n        ')
nvramBatteryAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5060)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "nvramBatteryStatus"))
if mibBuilder.loadTexts: nvramBatteryAlert.setStatus('current')
if mibBuilder.loadTexts: nvramBatteryAlert.setDescription("Description: \n\t\tDD OS detected an NVRAM card Battery Unit hardware fault.\n\t\tProbable causes:  1) Battery charging is disabled, or  2) One or more batteries are not charging.\n    \n   Action: \n\t\tRun CLI command 'system show nvram' to check battery status.\n\t\tIf the problem persists,   contact your contracted support provider or visit us online at https://support.emc.com.\n    ")
nvramErrorAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5061)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramErrorAlert.setStatus('current')
if mibBuilder.loadTexts: nvramErrorAlert.setDescription('Description: \n        DD OS detected an NVRAM card fault.\n        Probable cause: Excessive correctable errors exceed the warning threshold number.\n    \n   Action: \n        The NVRAM card may need to be replaced.\n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
nvramBatteryLowChargeAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5508)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramBatteryLowChargeAlert.setStatus('current')
if mibBuilder.loadTexts: nvramBatteryLowChargeAlert.setDescription('Description: \n        The NVRAM battery is charging, but is below the threshold.  \n        The filesystem will not start until the battery charge reaches the threshold.\n    \n   Action: \n        Wait for the battery charge to reach threshold.\n        If the battery does not reach threshold within 3 hours, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
ext3NvlogDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5527)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: ext3NvlogDisabled.setStatus('current')
if mibBuilder.loadTexts: ext3NvlogDisabled.setDescription('Description: \n\t\tDDOS RAID log is disabled due to a problem with the NVRAM subsystem.\n        \n   Action: \n\t\tCheck for other NVRAM-related alerts and follow the action described in those alerts.\n        ')
nvramHWAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6504)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramHWAlert.setStatus('current')
if mibBuilder.loadTexts: nvramHWAlert.setDescription('Description: \n        The NVRAM card is not in a usable state.\n        The file system cannot be accessed until the fault is corrected or the NVRAM card is replaced.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
nvramBattAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6507)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramBattAlert.setStatus('current')
if mibBuilder.loadTexts: nvramBattAlert.setDescription('Description: \n        The remote battery for an NVRAM card is not in a usable state.\n        The file system cannot be accessed until the fault is corrected or the NVRAM remote battery is replaced.\n    \n   Action: \n        Check NVRAM battery status.\n        Check the cables between the remote battery and the power source, and between the remote battery \n        and the NVRAM card. If the cables are correctly connected and the problem persists, \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
nvramEnvAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6505)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramEnvAlert.setStatus('current')
if mibBuilder.loadTexts: nvramEnvAlert.setDescription('Description: \n\tThe temperature sensor on the NVRAM card or the remote battery detected a temperature \n        that is higher than the warning threshold.  If there are other environmental alerts, \n        this may indicate a cooling problem where the system is installed.  \n        If there are no other environmental alerts, this may indicate a problem with this component.  \n        When the temperature is reduced, this alert will clear.\n    \n   Action: \n        Check cooling and airflow around the system unit.  Remove any blockage, or ensure \n        the environmental systems are operating correctly, and the environment is at a normal \n        temperature.  If there is no problem in the environment, or if only the NVRAM or \n        remote battery are reporting this problem, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
nvramCondAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6508)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramCondAlert.setStatus('current')
if mibBuilder.loadTexts: nvramCondAlert.setDescription('Description: \n        The NVRAM battery power or charging has been set as disabled. \n        This condition is either the result of an explicit setting, or indicates a fault \n        in the NVRAM card or battery unit. \n    \n   Action: \n        If the NVRAM battery power was explicitly disabled, enable it using \n        the reverse of the procedure used to disable it.  If not, reboot the system.  \n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
nvramEventHWAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6506)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramEventHWAlert.setStatus('current')
if mibBuilder.loadTexts: nvramEventHWAlert.setDescription('Description: \n        NVRAM firmware detects an NVRAM card hardware fault.\n    \n   Action: \n        The NVRAM card may need to be replaced. Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
nvramBattEndOfLife = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6545)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramBattEndOfLife.setStatus('current')
if mibBuilder.loadTexts: nvramBattEndOfLife.setDescription('Description: \n        The remote battery for NVRAM us currently usable but is approaching the end of its life.\n        If the battery is not replaced before it reaches end of its life, the filesystem will be disabled.\n    \n   Action: \n        To schedule a replacement, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
phyalert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5062)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: phyalert.setStatus('current')
if mibBuilder.loadTexts: phyalert.setDescription("Description: \n        Enclosure slot has been disabled due to continuous discovery caused by a failed drive.\n    \n   Action: \n        Replace the failed drive.\n        Use 'disk rescan' command specifying the disk and enclosure id to re-enable the slot.\n    ")
mtreeQuotaSoftLimit = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6007)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: mtreeQuotaSoftLimit.setStatus('current')
if mibBuilder.loadTexts: mtreeQuotaSoftLimit.setDescription('Description: \n\tThe Soft Limit Quota for this MTree has been reached.  This will not affect the operation of the system and is only a warning.\n    If a Quota Hard Limit is set for this MTree, you are approaching that limit and operations writing data to this MTree may fail if the hard limit is reached.\n    \n   Action: \n     To clear this alert, either raise the quota limits or reduce the data in the MTree by deleting files. \n    ')
mtreeQuotaHardLimit = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6008)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: mtreeQuotaHardLimit.setStatus('current')
if mibBuilder.loadTexts: mtreeQuotaHardLimit.setDescription('Description: \n\tThe Hard Limit Quota for this MTree has been reached. No more data will be written to this MTree.\n    If a backup operation was running, it probably failed and must be restarted after clearing this condition.\n    \n   Action: \n\tTo clear this alert, either raise the Quota Hard Limit for this MTree, or reduce the data in the MTree by deleting files.\n    ')
storageUnitStreamSoftLimit = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7517)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: storageUnitStreamSoftLimit.setStatus('current')
if mibBuilder.loadTexts: storageUnitStreamSoftLimit.setDescription('Description: \n        Stream soft limit quota for this storage-unit and type of stream has been exceeded.\n        Crossing this limit may cause reduced performance as the system hard limits are reached.\n    \n   Action: \n        To clear this alert, configure the backup application to use fewer concurrent streams.\n        Otherwise, increase the soft limit quota on this storage-unit for this stream type.\n    ')
replProgressThreshholdReached = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5063)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "replStatus"))
if mibBuilder.loadTexts: replProgressThreshholdReached.setStatus('current')
if mibBuilder.loadTexts: replProgressThreshholdReached.setDescription("Description: \n       Collection replication has not made progress and there is data waiting to be replicated.\n       This means your replica is not up to date.\n    \n   Action: \n        - check the 'replication status' or the GUI for errors\n        - check the replica filesystem\n        - check the network\n        - if problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ")
replNeedResync = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5064)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "replStatus"))
if mibBuilder.loadTexts: replNeedResync.setStatus('current')
if mibBuilder.loadTexts: replNeedResync.setDescription('Description: \n        Replication will not proceed until this context is resynced. \n    \n   Action: \n        To re-establish replication\n            - Note the context information\n            - break the context\n            - reconfigure contexts on both source and destination\n            - resync context on the source\n    ')
replLogFull = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5065)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: replLogFull.setStatus('current')
if mibBuilder.loadTexts: replLogFull.setDescription('Description: \n        No data can be written to the filesystem. Too much data remains to be replicated.\n        This can be caused by disabled contexts or slow replication.\n        When the condition is resolved, the filesystem will be writable again.\n    \n   Action: \n        Refer to knowledge base for articles discussing ways to reduce replication lag.\n    ')
replIncompatibleWorm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5066)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: replIncompatibleWorm.setStatus('current')
if mibBuilder.loadTexts: replIncompatibleWorm.setDescription('Description: \n        New retention-locked files detected on destination during replication resync. Resync cannot proceed.\n    \n   Action: \n        Break the existing context and resync to a new destination.\n    ')
replDestNotConfigured = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5067)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "replConfigDest"))
if mibBuilder.loadTexts: replDestNotConfigured.setStatus('current')
if mibBuilder.loadTexts: replDestNotConfigured.setDescription('Description: \n        Replication context on the destination is missing or mis-matched. Cannot initialize context.\n    \n   Action: \n        - Check both the source and destination configured context URL pair. The context is identified by the destination URL.\n        - Make sure the destination has a matching configuration for this context.\n    ')
replLagThreshholdReached = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5068)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: replLagThreshholdReached.setStatus('current')
if mibBuilder.loadTexts: replLagThreshholdReached.setDescription('Description: \n        Replication lag threshold has been exceeded.\n    \n   Action: \n        Refer to the knowledge base on ways to resolve the replication lag.\n    ')
replPathTooLong = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5531)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: replPathTooLong.setStatus('current')
if mibBuilder.loadTexts: replPathTooLong.setDescription('Description: \n       Path is too long\n    \n   Action: \n        Shorten the path.\n    ')
missingCreplUnits = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6544)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingCreplUnits.setStatus('current')
if mibBuilder.loadTexts: missingCreplUnits.setDescription('Description: \n        The collection replication destination is not in a consistent state and will not be usable until matching retention units are added to the destination.\n    \n   Action: \n        Add the required retention units to the collection replication destination.\n    ')
mtreeCascadeNeedResync = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7520)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "replStatus"))
if mibBuilder.loadTexts: mtreeCascadeNeedResync.setStatus('current')
if mibBuilder.loadTexts: mtreeCascadeNeedResync.setDescription('Description: \n       This Mtree is now a cascaded source.  Since this mtree already has data, this replication context requires a resync to proceed. \n    \n   Action: \n        To re-establish replication\n            - Note the context information\n            - break the context\n            - reconfigure contexts on both source and destination\n            - resync context on the source\n    ')
insecureEncryptedReplication = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6102)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: insecureEncryptedReplication.setStatus('current')
if mibBuilder.loadTexts: insecureEncryptedReplication.setDescription('Description: \n       Encrypted replication is configured between this system and the remote host.\n       The remote host is running a DDOS version that does not support a fully secure communication protocol.\n       Unauthorized individuals may be able to intercept and decrypt the replicated data.\n    \n   Action: \n       Upgrade the remote system to a release that supports the desired communication protocol.\n       Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
suspendedMReplMissingUnits = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10511)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: suspendedMReplMissingUnits.setStatus('current')
if mibBuilder.loadTexts: suspendedMReplMissingUnits.setDescription('Description: \n        Mtree replication on this context cannot continue until all archive units used by this Mtree are online.\n        Replication will resume automatically once all archive units come online.\n    \n   Action: \n        Return missing archive units to the system to resume MTree replication for this context.\n        If the archive units cannot be restored, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
sASEnclosureCheck = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5069)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sASEnclosureCheck.setStatus('current')
if mibBuilder.loadTexts: sASEnclosureCheck.setDescription('Description: \n        The number of enclosures connected to the port has exceeded the maximum supported limit.\n        This may cause an unexpected behavior.\n    \n   Action: \n        Reduce the number of enclosures down to the limit for the system.\n    ')
sASTopologyCheck = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5070)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sASTopologyCheck.setStatus('current')
if mibBuilder.loadTexts: sASTopologyCheck.setDescription("Description: \n        Invalid cabling has been detected. This may cause unexpected behavior.\n    \n   Action: \n        Refer to the cabling guide. Verify the connectivity of the SAS enclosures by using command\n         'enclosure show topology'.\n    ")
sASPortDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5071)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sASPortDisabled.setStatus('current')
if mibBuilder.loadTexts: sASPortDisabled.setDescription('Description: \n        Excessive errors have caused this port to be disabled. This could be caused by faulty cables or shelf controllers.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com .\n    ')
sASHBAFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6514)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sASHBAFailure.setStatus('current')
if mibBuilder.loadTexts: sASHBAFailure.setDescription('Description: \n        Storage is no longer accessible through this HBA.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
sASHBAErrors = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6515)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sASHBAErrors.setStatus('current')
if mibBuilder.loadTexts: sASHBAErrors.setDescription('Description: \n        A SAS HBA has detected correctable errors exceeding the warning threshold.\n        This will reduce throughput and may indicate a failing HBA.\n    \n   Action: \n        If this condition persists for more than 24 hours, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
unsupportedSASDevice = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6516)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedSASDevice.setStatus('current')
if mibBuilder.loadTexts: unsupportedSASDevice.setDescription('Description: \n        A SAS HBA has reported a device that is not recognized.\n        This device is not usable and may adversely affect the system.\n    \n   Action: \n        Identify the device and remove it from the topology.\n        If you believe it is a supported device, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
invalidEnclosureTopology = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7506)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: invalidEnclosureTopology.setStatus('current')
if mibBuilder.loadTexts: invalidEnclosureTopology.setDescription('Description: \n        The cables connecting enclosures to the controller are not installed correctly. This can cause unpredictable system behavior. Recable the enclosures immediately.\n    \n   Action: \n        Display the topology to identify the invalid path(s). Power down the system and cable the enclosures according to the cabling guide for your system.\n    ')
diskPathSpeedDegraded = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7507)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskPathSpeedDegraded.setStatus('current')
if mibBuilder.loadTexts: diskPathSpeedDegraded.setDescription('Description: \n        SAS connection speed is degraded and could reduce disk performance.\n    \n   Action: \n        Check cable seating and replace if needed.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
enclosureMixType = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5528)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: enclosureMixType.setStatus('current')
if mibBuilder.loadTexts: enclosureMixType.setDescription('Description: \n        An unsupported mix of enclosure models have been detected. For example, a mixture of ES30s and ES20s.\n    \n   Action: \n        Refer to the configuration guide for valid cabling configurations.\n    ')
enclosureMixDriveType = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10515)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: enclosureMixDriveType.setStatus('current')
if mibBuilder.loadTexts: enclosureMixDriveType.setDescription('Description: \n        An unsupported mix of enclosures with different drive types may impact performance and lead to unexpected system behavior.\n    \n   Action: \n        Recable the enclosures to eliminate the unsupported mix. Refer to the configuration guide for valid cabling configurations.\n    ')
sCSITGTInvalidRegistry = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6539)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sCSITGTInvalidRegistry.setStatus('current')
if mibBuilder.loadTexts: sCSITGTInvalidRegistry.setDescription('Description: \n        A registry entry used in the SCSI Target system is invalid.\n        The SCSI Target services, including VTL, DD-BOOST FC and VDISK will be\n        inaccessible until this problem is resolved.\n    \n   Action: \n        The registry entry must be corrected.  \n        Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
sSLCertificateCorrupted = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5072)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sSLCertificateCorrupted.setStatus('current')
if mibBuilder.loadTexts: sSLCertificateCorrupted.setDescription('Description: \n            The SSL certificate used to establish mutual trust between Data Domain systems is broken.        \n        \n   Action: \n            Contact your contracted support provider or visit us online at https://support.emc.com\n        ')
unusableHostCertificate = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6017)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: unusableHostCertificate.setStatus('current')
if mibBuilder.loadTexts: unusableHostCertificate.setDescription('Description: \n            Enterprise Manager will not start up using the imported certificate. However, it will start up using the default self-signed certificate. \n Following is the list of possible causes of this alert,\n    - the file system is locked\n    - the system passphrase is missing\n    - the imported certificate is corrupted\n        \n   Action: \n            Unlock the file system if it is locked.\n            Enter the system passphrase if it is missing.\n            Delete and reimport the current host certificate if it is corrupted.\n            In all cases, the Enterprise Manager needs to be restarted.\n            If the condition persists, contact your contracted support provider or visit us online at https://support.emc.com\n        ')
missingHostCertificate = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6018)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: missingHostCertificate.setStatus('current')
if mibBuilder.loadTexts: missingHostCertificate.setDescription('Description: \n            The imported certificate is missing. However, the Enterprise Manager will start up using the default self-signed certificate.\n        \n   Action: \n            If you want to use your own certificate, import it again.\n        ')
expiredHostCertificate = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6538)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: expiredHostCertificate.setStatus('current')
if mibBuilder.loadTexts: expiredHostCertificate.setDescription('Description: \n            Communication using this certificate is vulnerable to disclosure.\n        \n   Action: \n            Replace the host certificate with a valid certificate.\n        ')
sMSUnresponsive = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7500)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sMSUnresponsive.setStatus('current')
if mibBuilder.loadTexts: sMSUnresponsive.setDescription('Description: \n        The System Management Service has reached the maximum number of concurrent \n        requests and has been unresponsive for over five minutes. This may indicate \n        a serious condition that may need to be addressed by support. The system is \n        unable to accept additional commands.\n    \n   Action: \n        If this condition persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
mailserverError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6511)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: mailserverError.setStatus('current')
if mibBuilder.loadTexts: mailserverError.setDescription('Description: \n            There is a problem communicating with the configured mail server.\n            The system will not be able to send out any email notifications that includes alerts, autosupports and daily summary emails.\n        \n   Action: \n            Make sure that the mail server is configured correctly.\n            Verify the configured mail server by sending out a test email from the system.\n            If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n        ')
snapshotOver90Percent = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5075)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: snapshotOver90Percent.setStatus('current')
if mibBuilder.loadTexts: snapshotOver90Percent.setDescription("Description: \n        Current number of snapshots for an Mtree is at 90% or more of the maximum number of snapshots allowed.\n    \n   Action: \n        Consider expiring existing snapshots of that Mtree with the 'snapshot expire' command or \n        adjusting scheduled snapshot retention periods with the 'snapshot schedule modify' command.\n    ")
snapshotLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5076)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: snapshotLimitReached.setStatus('current')
if mibBuilder.loadTexts: snapshotLimitReached.setDescription("Description: \n        Data Domain system has a limit on the number of existing snapshots held at once for a single Mtree.\n        Once this limit is reached no more snapshots can be created of that Mtree.\n    \n   Action: \n        Consider expiring existing snapshots of that Mtree with 'snapshot expire' command to make room for newer ones.\n    ")
sNTZMultipleIterations = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5077)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sNTZMultipleIterations.setStatus('current')
if mibBuilder.loadTexts: sNTZMultipleIterations.setDescription('Description: \n    Indicates that sanitization will be run in multiple iterations.\n    In the worst case this can take 15-20 days for 280 TBs. It means \n    that the system will not run at full speed for that period of \n    time and that GC will not be run to reclaim space. However, \n    sanitization will also reclaim space back but it might not be \n    as efficient as GC is.\n\n   Action: \n    Make sure that you have enough space to not run out of space and\n    that you can wait that many days in the worst case. You should have\n    at least 20% of physical space available. Other option is\n    to abort sanitization, delete a bunch of files and try again. You can\n    do this process iteratively until you do not get this alert anymore. \n')
coredumpWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5078)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: coredumpWarning.setStatus('current')
if mibBuilder.loadTexts: coredumpWarning.setDescription('Description: \n        /ddvar might soon run out of space to save system core dumps.\n    \n   Action: \n        Remove unwanted files from /ddvar to free up some space.\n        Lack of space can result in missing core dumps that will hamper debugging operations.\n    ')
coredumpDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5079)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: coredumpDisabled.setStatus('current')
if mibBuilder.loadTexts: coredumpDisabled.setDescription('Description: \n        Space in /ddvar is not sufficient enough for saving system core dumps.\n    \n   Action: \n        Remove unwanted files from /ddvar to free up some space.\n        Lack of space can result in missing core dumps that will hamper debugging operations.\n    ')
spaceOver80Percent = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5080)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"))
if mibBuilder.loadTexts: spaceOver80Percent.setStatus('current')
if mibBuilder.loadTexts: spaceOver80Percent.setDescription('Description: \n        Space usage has exceeded 80% of the total capacity.\n        Lack of space can result in missing important logs or loss of file system functionality.\n    \n   Action: \n        If it is in root, contact your contracted support provider or visit us online at https://support.emc.com to free up some space.\n        If it is in /ddvar, remove unwanted files to free up some space.\n        If it is in active tier, remove unwanted files and start file system cleaning or add storage.\n        If it is in archive tier, remove unwanted files or add more archive units to the filesystem.\n    ')
spaceOver90Percent = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5081)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"))
if mibBuilder.loadTexts: spaceOver90Percent.setStatus('current')
if mibBuilder.loadTexts: spaceOver90Percent.setDescription('Description: \n        Space usage has exceeded 90% of the total capacity.\n        Lack of space can result in missing important logs or loss of file system functionality.\n    \n   Action: \n        If it is in root, contact your contracted support provider or visit us online at https://support.emc.com to free up some space.\n        If it is in /ddvar, remove unwanted files to free up some space.\n        If it is in active tier, remove unwanted files and start file system cleaning or add storage.\n        If it is in archive tier, remove unwanted files or add more archive units to the filesystem.\n    ')
spaceReclRestartFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6531)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclRestartFailed.setStatus('current')
if mibBuilder.loadTexts: spaceReclRestartFailed.setDescription('Description: \n        Archive space reclamation was running before the last shutdown of the filesystem and could not be restarted automatically.\n        Space will not be reclaimed in the archive tier until space reclamation is restarted.\n    \n   Action: \n        Start space reclamation.\n    ')
spaceReclMissingUnit = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6532)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclMissingUnit.setStatus('current')
if mibBuilder.loadTexts: spaceReclMissingUnit.setDescription('Description: \n        Archive units are missing. Space reclamation cannot run unless all configured units are attached.\n        Space will not be reclaimed in the archive tier until space reclamation is restarted.\n    \n   Action: \n        Return missing archive units to the system and start space reclamation.\n    ')
spaceReclUnitReclaimed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6533)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclUnitReclaimed.setStatus('current')
if mibBuilder.loadTexts: spaceReclUnitReclaimed.setDescription('Description: \n        All space on the archive unit has been reclaimed. This unit is available to reuse.\n    \n   Action: \n        No action is required.\n    ')
spaceReclError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6534)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclError.setStatus('current')
if mibBuilder.loadTexts: spaceReclError.setDescription('Description: \n        Archive space reclamation has stopped due to the specified error.\n        Space will not be reclaimed in the archive tier until the error condition is resolved and space reclamation is restarted.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
spaceReclSuspended = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7518)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclSuspended.setStatus('current')
if mibBuilder.loadTexts: spaceReclSuspended.setDescription('Description: \n        Archive space reclamation has suspended due to the specified error.\n        Space will not be reclaimed in the archive tier until the error condition is resolved and space reclamation is resumed.\n    \n   Action: \n         Resume space reclamation after the underlying error condition is corrected. If problem persists,\n         Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
spaceReclUnitError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7523)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclUnitError.setStatus('current')
if mibBuilder.loadTexts: spaceReclUnitError.setDescription('Description: \n        Space reclamation encountered an error and cannot proceed on the specified archive unit. \n        If you have more than one archive unit, space reclamation will continue on the next unit. \n        Space will not be reclaimed in this archive unit until the error condition is resolved \n        and space reclamation finishes successfully on this unit.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
diskAccessError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5082)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskAccessError.setStatus('current')
if mibBuilder.loadTexts: diskAccessError.setDescription('Description: \n        A hardware fault has been detected for this drive. The drive or the cabling to it may have a problem.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
diskFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5083)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskFailure.setStatus('current')
if mibBuilder.loadTexts: diskFailure.setDescription('Description: \n        Unable to communicate with a disk. This disk cannot be used at this time.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
diskTemperatureWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5084)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskTemperature"))
if mibBuilder.loadTexts: diskTemperatureWarning.setStatus('current')
if mibBuilder.loadTexts: diskTemperatureWarning.setDescription('Description: \n        The disk temperature has exceeded a specified threshold. If the temperature continues to increase,\n        the system could fail or the system could be shut down.\n    \n   Action: \n        If the temperature is high due to high activity for a short period, it should return to normal in a short time.\n        Verify the environment is at its normal temperature. If not, correct this condition.\n        Check for fan failures and free air flow.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
diskTemperatureShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5085)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: diskTemperatureShutdown.setStatus('current')
if mibBuilder.loadTexts: diskTemperatureShutdown.setDescription('Description: \n        One or more disks have exceeded the shut down temperature threshold. The system is shutting down.\n    \n   Action: \n        Verify the environment is at its normal temperature. If not, correct this condition.\n        Check for fan failures and free air flow.\n    ')
unsupportedHardwareSpareSize = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5086)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: unsupportedHardwareSpareSize.setStatus('current')
if mibBuilder.loadTexts: unsupportedHardwareSpareSize.setDescription('Description: \n        The disk capacity is too small for it to be of any use in the system.\n    \n   Action: \n        Replace with a larger capacity disk.\n    ')
missingDiskGroup = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5087)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingDiskGroup.setStatus('current')
if mibBuilder.loadTexts: missingDiskGroup.setDescription('Description: \n        One or more critical disks/LUNs are unavailable.\n    \n   Action: \n        Make sure all storage is securely connected.\n        Look at alert history for any path failures.\n        Check for any core files, a critical layer may be unavailable.\n        Verify that all storage is working and recognized correctly.\n    ')
diskGroupReconstructionNoProgress = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5088)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskGroupReconstructionNoProgress.setStatus('current')
if mibBuilder.loadTexts: diskGroupReconstructionNoProgress.setDescription('Description: \n        One or more disks are failed and the RAID reconstruction is not running.\n    \n   Action: \n        Make sure there is/are spare disk(s) in the system.\n    ')
diskGroupReconstruction = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5089)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskGroupReconstruction.setStatus('current')
if mibBuilder.loadTexts: diskGroupReconstruction.setDescription('Description: \n        Two or more disks are failed and the RAID protection is in critical state.\n        If an additional disk fails, there might be permanent loss of data.\n        The system will shut down if the problem is not fixed.\n    \n   Action: \n        Make sure there is/are spare disk(s) in the system.\n    ')
diskGroupReconstructionShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5090)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskGroupReconstructionShutdown.setStatus('current')
if mibBuilder.loadTexts: diskGroupReconstructionShutdown.setDescription('Description: \n        Two or more disks are failed and the RAID protection is in critical state for over a\n        considerable period of time. If an additional disk fails, there might be permanent loss of\n        data. The system will shut down.\n    \n   Action: \n        Restart the system and make sure there is/are spare disk(s) in the system.\n    ')
diskGroupReconstructionCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5091)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskGroupReconstructionCritical.setStatus('current')
if mibBuilder.loadTexts: diskGroupReconstructionCritical.setDescription('Description: \n        Two or more disks are failed and the RAID protection is in critical state for over a\n        considerable period of time. If an additional disk fails, there might be permanent loss of\n        data.\n    \n   Action: \n        Make sure there is/are spare disk(s) in the system.\n    ')
diskUnknown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5092)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskUnknown.setStatus('current')
if mibBuilder.loadTexts: diskUnknown.setDescription('Description: \n        Disk is unknown.\n    \n   Action: \n        Add disk to the system.\n    ')
lowSpares = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5094)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: lowSpares.setStatus('current')
if mibBuilder.loadTexts: lowSpares.setDescription('Description: \n        Not enough spare disks can be detected for this tier.\n        There may be failed disks or connectivity issues with disks or enclosures.\n    \n   Action: \n        Replace any failed or absent disks. Check enclosure connectivity.\n    ')
unsupportedConfigurationROL = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5095)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedConfigurationROL.setStatus('current')
if mibBuilder.loadTexts: unsupportedConfigurationROL.setDescription('Description: \n        Raid on LUN from 4.8 is no longer supported.  Please follow instruction on how to increase \n        usable space in your filesystem. \n    \n   Action: \n                1) migrate data away \n                2) do a filesystem destroy\n                3) add your LUN\n                4) migrate data back  \n    ')
foreignEnclosure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6019)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "enclosureListNum"))
if mibBuilder.loadTexts: foreignEnclosure.setStatus('current')
if mibBuilder.loadTexts: foreignEnclosure.setDescription('Description: \n        The enclosure is unusable by the filesystem.\n        Storage configuration can not be modified while a foreign device is present.\n    \n   Action: \n        If this is expected as part of a chassis swap or chassis upgrade, proceed with\n        the headswap operation to make the foreign filesystem available.\n        Otherwise contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
sSDEndOfLife = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6541)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: sSDEndOfLife.setStatus('current')
if mibBuilder.loadTexts: sSDEndOfLife.setDescription('Description: \n        The SSD has reached end of life and could fail at any time.\n        The system may shut down unexpectedly if the drive is not replaced.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
multipleDiskReadErrors = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6543)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: multipleDiskReadErrors.setStatus('current')
if mibBuilder.loadTexts: multipleDiskReadErrors.setDescription('Description: \n        There are too many disks reporting read errors in the same RAID group.\n        As each of these disks completes reconstruction it will be failed.\n        If the ongoing RAID reconstruction fails, there might be permanent loss of data.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com to determine the number of drives that need to be replaced.\n    ')
unsupportedDriveModel = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7001)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedDriveModel.setStatus('current')
if mibBuilder.loadTexts: unsupportedDriveModel.setDescription('Description: \n        This system only supports certain drive models.\n        The unsupported drives are unusable and must be replaced for proper system operation.\n    \n   Action: \n        Identify and remove/replace the unsupported drives.\n        For assistance, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
driveMixType = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7002)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: driveMixType.setStatus('current')
if mibBuilder.loadTexts: driveMixType.setDescription('Description: \n        Mixing drive types within an enclosure is not supported and may cause unexpected system behavior.\n    \n   Action: \n        Ensure that all drives within the enclosure are of the same type.\n        For assistance, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
missingTierStorage = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7522)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingTierStorage.setStatus('current')
if mibBuilder.loadTexts: missingTierStorage.setDescription('Description: \n        Critical storage resources are unavailable, preventing the tier from functioning.\n    \n   Action: \n        Verify all storage is functional and configured correctly.\n        If the problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n    ')
storageMigrationCopyComplete = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10501)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: storageMigrationCopyComplete.setStatus('current')
if mibBuilder.loadTexts: storageMigrationCopyComplete.setDescription('Description:                                                                                                                                                                         \n        All data has been moved from old enclosures to the new enclosures.\n        Storage migration must be finalized to decommission old enclosures and\n        add new capacity to the file system.\n    \n   Action:  \n        Finalize the storage migration.\n    ')
storageMigrationCannotResume = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10500)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: storageMigrationCannotResume.setStatus('current')
if mibBuilder.loadTexts: storageMigrationCannotResume.setDescription('Description: \n        The system has detected a condition which prevented the storage\n        migration from continuing and has suspended the data copy phase.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
storageMigrationUserSuspend = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10502)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: storageMigrationUserSuspend.setStatus('current')
if mibBuilder.loadTexts: storageMigrationUserSuspend.setDescription('Description: \n        An administrator has suspended the data copy phase of storage migration.\n        Data copy cannot proceed until it is manually resumed.\n    \n   Action: \n        Resume the storage migration.\n    ')
foreignPack = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10512)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "enclosurePackID"))
if mibBuilder.loadTexts: foreignPack.setStatus('current')
if mibBuilder.loadTexts: foreignPack.setDescription('Description: \n        The enclosure pack is unusable by the file system.\n        Storage configuration can not be modified while a foreign device is present.\n    \n   Action: \n        If this is expected as part of a chassis swap or chassis upgrade, proceed with\n        the headswap operation to make the foreign filesystem available.\n        Otherwise contact your contracted support provider or visit us online at https://support.emc.com.\n    ')
upgradeFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6509)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: upgradeFailure.setStatus('current')
if mibBuilder.loadTexts: upgradeFailure.setDescription('Description: \n            During the upgrade process, there was an error that requires manual intervention. The system is not usable.\n        \n   Action: \n            Contact your contracted support provider or visit us online at https://support.emc.com.\n        ')
upgradeCompleted = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6510)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: upgradeCompleted.setStatus('current')
if mibBuilder.loadTexts: upgradeCompleted.setDescription('Description: \n            The DD OS upgrade is completed successfully. The system will be ready to use when the filesystem is enabled.\n        \n   Action: \n            No action required.\n        ')
upgradeInProgress = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10509)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: upgradeInProgress.setStatus('current')
if mibBuilder.loadTexts: upgradeInProgress.setDescription('Description: \n            DD OS upgrade is in progress.\n            The system will not be available for backup and restore operations.\n            The alert will be cleared after the upgrade operation is complete.\n        \n   Action: \n            Allow the upgrade operation to complete. If the upgrade takes longer than usual, contact your contracted support provider or visit us online at https://support.emc.com\n        ')
vDiskSCSITargetMismatch = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10513)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: vDiskSCSITargetMismatch.setStatus('current')
if mibBuilder.loadTexts: vDiskSCSITargetMismatch.setDescription('Description: \n        VDisk configuration does not match SCSI Target configuration.\n        Non-matching devices are not available and must be deleted or repaired.\n    \n   Action: \n        Contact your contracted support provider or visit us online at https://support.emc.com\n    ')
tapeReposition = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6542)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: tapeReposition.setStatus('current')
if mibBuilder.loadTexts: tapeReposition.setDescription('Description: \n        The tape volume was adjusted to the last consistent data position during\n        VTL recovery. Recent pending updates to the volume may have been discarded.\n    \n   Action: \n        Verify that any backup sent to the affected tape at the time of this alert\n        completed successfully. Reissue the backup if necessary.\n    ')
duplicateVTLPoolNames = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10010)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: duplicateVTLPoolNames.setStatus('current')
if mibBuilder.loadTexts: duplicateVTLPoolNames.setDescription('Description: \n        VTL directory pool and a VTL mtree pool have been detected with the same name.\n        Viewing pool information will only retrieve tapes from the mtree pool. Tapes in the\n        directory pool will not be visible to DataDomain system administration interfaces.\n        Backups and restores using the directory pool will operate normally.\n    \n   Action: \n        Rename one of the pools to make the name unique. The duplicate pool name may have been created as\n        part of a replication pair.If problem persists, contact your contracted support provider or visit us online at https://support.emc.com\n')
vTLEnabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 11105)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: vTLEnabled.setStatus('current')
if mibBuilder.loadTexts: vTLEnabled.setDescription('Description: \n        VTL is enabled. VTL functionality is available to the user.\n    \n   Action: \n        Some backup applications may need manual rescanning for devices.\n    ')
vTLDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 11106)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: vTLDisabled.setStatus('current')
if mibBuilder.loadTexts: vTLDisabled.setDescription('Description: \n        VTL is disabled. VTL functionality is unavailable to the user.\n    \n   Action: \n        No Action required.\n    ')
dataDomainMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 0, 1))
dataDomainMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 1)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroup"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "basicNotificationsGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroup"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageNotificationsGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibCompliance = dataDomainMibCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: dataDomainMibCompliance.setDescription('The compliance statement for SNMP entities which\n            implement this MIB module.')
dataDomainMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 2)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroup"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "ddboostGroup"), ("DATA-DOMAIN-MIB", "ddsystemGroup"), ("DATA-DOMAIN-MIB", "artGroup"), ("DATA-DOMAIN-MIB", "mtreeGroup"), ("DATA-DOMAIN-MIB", "enclosureGroup"), ("DATA-DOMAIN-MIB", "networkGroup"), ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"), ("DATA-DOMAIN-MIB", "managedObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibComplianceRev1 = dataDomainMibComplianceRev1.setStatus('deprecated')
if mibBuilder.loadTexts: dataDomainMibComplianceRev1.setDescription('The compliance statement for SNMP entities which\n            implement this MIB module.')
dataDomainMibComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 3)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroup"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "ddboostGroup"), ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"), ("DATA-DOMAIN-MIB", "artGroup"), ("DATA-DOMAIN-MIB", "mtreeGroup"), ("DATA-DOMAIN-MIB", "enclosureGroup"), ("DATA-DOMAIN-MIB", "networkGroup"), ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"), ("DATA-DOMAIN-MIB", "managedObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibComplianceRev2 = dataDomainMibComplianceRev2.setStatus('deprecated')
if mibBuilder.loadTexts: dataDomainMibComplianceRev2.setDescription('The compliance statement for SNMP entities which\n            implement this MIB module.')
dataDomainMibComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 4)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroup"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "ddboostGroupRev1"), ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"), ("DATA-DOMAIN-MIB", "artGroup"), ("DATA-DOMAIN-MIB", "mtreeGroup"), ("DATA-DOMAIN-MIB", "enclosureGroup"), ("DATA-DOMAIN-MIB", "networkGroup"), ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"), ("DATA-DOMAIN-MIB", "smtGroup"), ("DATA-DOMAIN-MIB", "quotaGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"), ("DATA-DOMAIN-MIB", "managedObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibComplianceRev3 = dataDomainMibComplianceRev3.setStatus('deprecated')
if mibBuilder.loadTexts: dataDomainMibComplianceRev3.setDescription('The compliance statement for SNMP entities which\n            implement this MIB module.')
dataDomainMibComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 5)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroup"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "ddboostGroupRev2"), ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"), ("DATA-DOMAIN-MIB", "artGroup"), ("DATA-DOMAIN-MIB", "mtreeGroup"), ("DATA-DOMAIN-MIB", "enclosureGroup"), ("DATA-DOMAIN-MIB", "networkGroup"), ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"), ("DATA-DOMAIN-MIB", "smtGroup"), ("DATA-DOMAIN-MIB", "quotaGroup"), ("DATA-DOMAIN-MIB", "highAvailabilityGroup"), ("DATA-DOMAIN-MIB", "scsitargetObjectGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"), ("DATA-DOMAIN-MIB", "managedObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibComplianceRev4 = dataDomainMibComplianceRev4.setStatus('deprecated')
if mibBuilder.loadTexts: dataDomainMibComplianceRev4.setDescription('The compliance statement for SNMP entities which\n            implement this MIB module.')
dataDomainMibComplianceRev5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 6)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroupRev1"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "ddboostGroupRev2"), ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"), ("DATA-DOMAIN-MIB", "artGroup"), ("DATA-DOMAIN-MIB", "mtreeGroup"), ("DATA-DOMAIN-MIB", "enclosureGroup"), ("DATA-DOMAIN-MIB", "networkGroup"), ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"), ("DATA-DOMAIN-MIB", "smtGroup"), ("DATA-DOMAIN-MIB", "quotaGroup"), ("DATA-DOMAIN-MIB", "highAvailabilityGroup"), ("DATA-DOMAIN-MIB", "scsitargetObjectGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"), ("DATA-DOMAIN-MIB", "managedObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibComplianceRev5 = dataDomainMibComplianceRev5.setStatus('current')
if mibBuilder.loadTexts: dataDomainMibComplianceRev5.setDescription('The compliance statement for SNMP entities which\n            implement this MIB module.')
environmentalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 1)).setObjects(("DATA-DOMAIN-MIB", "powerModuleDescription"), ("DATA-DOMAIN-MIB", "powerModuleStatus"), ("DATA-DOMAIN-MIB", "tempSensorDescription"), ("DATA-DOMAIN-MIB", "tempSensorCurrentValue"), ("DATA-DOMAIN-MIB", "tempSensorStatus"), ("DATA-DOMAIN-MIB", "fanDescription"), ("DATA-DOMAIN-MIB", "fanLevel"), ("DATA-DOMAIN-MIB", "fanStatus"), ("DATA-DOMAIN-MIB", "tempSensorTrapIndex"), ("DATA-DOMAIN-MIB", "fanTrapIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    environmentalsGroup = environmentalsGroup.setStatus('current')
if mibBuilder.loadTexts: environmentalsGroup.setDescription('A collection of objects providing environmental monitoring information.')
nvramGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 2)).setObjects(("DATA-DOMAIN-MIB", "nvramMemorySize"), ("DATA-DOMAIN-MIB", "nvramWindowSize"), ("DATA-DOMAIN-MIB", "nvramPCIErrorCount"), ("DATA-DOMAIN-MIB", "nvramMemoryErrorCount"), ("DATA-DOMAIN-MIB", "nvramBatteryStatus"), ("DATA-DOMAIN-MIB", "nvramBatteryCharge"), ("DATA-DOMAIN-MIB", "nvramHCMemorySize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nvramGroup = nvramGroup.setStatus('current')
if mibBuilder.loadTexts: nvramGroup.setDescription('A collection of objects providing nvram monitoring information.')
fileSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 3)).setObjects(("DATA-DOMAIN-MIB", "fileSystemStatus"), ("DATA-DOMAIN-MIB", "fileSystemVirtualSpace"), ("DATA-DOMAIN-MIB", "fileSystemResourceName"), ("DATA-DOMAIN-MIB", "fileSystemSpaceSize"), ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"), ("DATA-DOMAIN-MIB", "fileSystemSpaceAvail"), ("DATA-DOMAIN-MIB", "fileSystemPercentUsed"), ("DATA-DOMAIN-MIB", "fileSystemSpaceCleanable"), ("DATA-DOMAIN-MIB", "fileSystemCompressionPeriod"), ("DATA-DOMAIN-MIB", "fileSystemCompressionStartTime"), ("DATA-DOMAIN-MIB", "fileSystemCompressionEndTime"), ("DATA-DOMAIN-MIB", "fileSystemPreCompressionSize"), ("DATA-DOMAIN-MIB", "fileSystemPostCompressionSize"), ("DATA-DOMAIN-MIB", "fileSystemGlobalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemLocalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemTotalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemReductionPercent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fileSystemGroup = fileSystemGroup.setStatus('deprecated')
if mibBuilder.loadTexts: fileSystemGroup.setDescription('A collection of objects providing file system monitoring information.')
alertsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 4)).setObjects(("DATA-DOMAIN-MIB", "currentAlertTimestamp"), ("DATA-DOMAIN-MIB", "currentAlertDescription"), ("DATA-DOMAIN-MIB", "currentAlertSeverity"), ("DATA-DOMAIN-MIB", "currentAlertID"), ("DATA-DOMAIN-MIB", "alertHistoryTimestamp"), ("DATA-DOMAIN-MIB", "alertHistoryDescription"), ("DATA-DOMAIN-MIB", "alertHistorySeverity"), ("DATA-DOMAIN-MIB", "alertHistoryStatus"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alertsGroup = alertsGroup.setStatus('current')
if mibBuilder.loadTexts: alertsGroup.setDescription('A collection of objects providing alert monitoring information.')
statisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 5)).setObjects(("DATA-DOMAIN-MIB", "cpuAvgPercentageBusy"), ("DATA-DOMAIN-MIB", "cpuMaxPercentageBusy"), ("DATA-DOMAIN-MIB", "nfsOpsPerSecond"), ("DATA-DOMAIN-MIB", "nfsIdlePercentage"), ("DATA-DOMAIN-MIB", "nfsProcPercentage"), ("DATA-DOMAIN-MIB", "nfsSendPercentage"), ("DATA-DOMAIN-MIB", "nfsReceivePercentage"), ("DATA-DOMAIN-MIB", "cifsOpsPerSecond"), ("DATA-DOMAIN-MIB", "diskReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "diskWriteKBytesPerSecond"), ("DATA-DOMAIN-MIB", "diskBusyPercentage"), ("DATA-DOMAIN-MIB", "nvramReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "nvramWriteKBytesPerSecond"), ("DATA-DOMAIN-MIB", "replInKBytesPerSecond"), ("DATA-DOMAIN-MIB", "replOutKBytesPerSecond"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    statisticsGroup = statisticsGroup.setStatus('current')
if mibBuilder.loadTexts: statisticsGroup.setDescription('A collection of objects providing statistics information.')
internalDiskStorageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 7)).setObjects(("DATA-DOMAIN-MIB", "diskModel"), ("DATA-DOMAIN-MIB", "diskFirmwareVersion"), ("DATA-DOMAIN-MIB", "diskSerialNumber"), ("DATA-DOMAIN-MIB", "diskCapacity"), ("DATA-DOMAIN-MIB", "diskPropState"), ("DATA-DOMAIN-MIB", "diskPack"), ("DATA-DOMAIN-MIB", "diskSectorsRead"), ("DATA-DOMAIN-MIB", "diskSectorsWritten"), ("DATA-DOMAIN-MIB", "diskTotalKBytes"), ("DATA-DOMAIN-MIB", "diskBusy"), ("DATA-DOMAIN-MIB", "diskPerfState"), ("DATA-DOMAIN-MIB", "diskTemperature"), ("DATA-DOMAIN-MIB", "diskTimeoutCount"), ("DATA-DOMAIN-MIB", "diskReadFailCount"), ("DATA-DOMAIN-MIB", "diskWriteFailCount"), ("DATA-DOMAIN-MIB", "diskMiscFailCount"), ("DATA-DOMAIN-MIB", "diskOffTrackErrCount"), ("DATA-DOMAIN-MIB", "diskSoftEccCount"), ("DATA-DOMAIN-MIB", "diskCrcErrCount"), ("DATA-DOMAIN-MIB", "diskProbationalCount"), ("DATA-DOMAIN-MIB", "diskReallocCount"), ("DATA-DOMAIN-MIB", "diskErrState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    internalDiskStorageGroup = internalDiskStorageGroup.setStatus('current')
if mibBuilder.loadTexts: internalDiskStorageGroup.setDescription('A collection of objects providing internal disk monitoring information.')
externalUnmanagedDiskStorageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 8)).setObjects(("DATA-DOMAIN-MIB", "diskModel"), ("DATA-DOMAIN-MIB", "diskFirmwareVersion"), ("DATA-DOMAIN-MIB", "diskSerialNumber"), ("DATA-DOMAIN-MIB", "diskCapacity"), ("DATA-DOMAIN-MIB", "diskPropState"), ("DATA-DOMAIN-MIB", "diskSectorsRead"), ("DATA-DOMAIN-MIB", "diskSectorsWritten"), ("DATA-DOMAIN-MIB", "diskTotalKBytes"), ("DATA-DOMAIN-MIB", "diskBusy"), ("DATA-DOMAIN-MIB", "diskPerfState"), ("DATA-DOMAIN-MIB", "diskPropTrapIndex"), ("DATA-DOMAIN-MIB", "diskErrTrapIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    externalUnmanagedDiskStorageGroup = externalUnmanagedDiskStorageGroup.setStatus('current')
if mibBuilder.loadTexts: externalUnmanagedDiskStorageGroup.setDescription('A collection of objects providing external unmanaged disk monitoring information.')
basicNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 9)).setObjects(("DATA-DOMAIN-MIB", "powerSupplyFailedAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatWarningAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatAlertAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatShutdownAlarm"), ("DATA-DOMAIN-MIB", "fanModuleFailedAlarm"), ("DATA-DOMAIN-MIB", "nvramFailingAlarm"), ("DATA-DOMAIN-MIB", "fileSystemFailedAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceMaintenanceAlarm"), ("DATA-DOMAIN-MIB", "fileSpacePreWarningAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceWarningAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceSevereAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceCriticalAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatWarningAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatAlertAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatShutdownAlarm"), ("DATA-DOMAIN-MIB", "diskFailedAlarm"), ("DATA-DOMAIN-MIB", "diskNoSpareAlarm"), ("DATA-DOMAIN-MIB", "diskPathAlarm"), ("DATA-DOMAIN-MIB", "diskSASAlarm"), ("DATA-DOMAIN-MIB", "diskSASHBAAlarm"), ("DATA-DOMAIN-MIB", "snapshotFullAlarm"), ("DATA-DOMAIN-MIB", "snapshotHWMAlarm"), ("DATA-DOMAIN-MIB", "clusterNodeAlarm"), ("DATA-DOMAIN-MIB", "clusterInterfaceAlarm"), ("DATA-DOMAIN-MIB", "replSyncAlarm"), ("DATA-DOMAIN-MIB", "systemStartupAlarm"), ("DATA-DOMAIN-MIB", "filesysRelaunchAlarm"), ("DATA-DOMAIN-MIB", "filesysDDGCFailedAlarm"), ("DATA-DOMAIN-MIB", "filesysGeneralProblemAlarm"), ("DATA-DOMAIN-MIB", "diskUnsupportedAlarm"), ("DATA-DOMAIN-MIB", "eventIPMIUnmanageAlarm"), ("DATA-DOMAIN-MIB", "raidReconSevereAlarm"), ("DATA-DOMAIN-MIB", "raidReconCriticalAlarm"), ("DATA-DOMAIN-MIB", "raidReconCriticalShutdownAlarm"), ("DATA-DOMAIN-MIB", "raidGroupMissingAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basicNotificationsGroup = basicNotificationsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: basicNotificationsGroup.setDescription('A collection of objects providing basic notifications.')
internalDiskStorageNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 10)).setObjects(("DATA-DOMAIN-MIB", "diskFailedAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatWarningAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatAlertAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatShutdownAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    internalDiskStorageNotificationsGroup = internalDiskStorageNotificationsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: internalDiskStorageNotificationsGroup.setDescription('A collection of objects providing internal disk storage notifications.')
replGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 11)).setObjects(("DATA-DOMAIN-MIB", "replState"), ("DATA-DOMAIN-MIB", "replStatus"), ("DATA-DOMAIN-MIB", "replFileSysStatus"), ("DATA-DOMAIN-MIB", "replConnTime"), ("DATA-DOMAIN-MIB", "replSource"), ("DATA-DOMAIN-MIB", "replDestination"), ("DATA-DOMAIN-MIB", "replPreCompBytesSent"), ("DATA-DOMAIN-MIB", "replPostCompBytesSent"), ("DATA-DOMAIN-MIB", "replPreCompBytesRemaining"), ("DATA-DOMAIN-MIB", "replPostCompBytesReceived"), ("DATA-DOMAIN-MIB", "replThrottle"), ("DATA-DOMAIN-MIB", "replSyncedAsOfTime"), ("DATA-DOMAIN-MIB", "replConfigContextId"), ("DATA-DOMAIN-MIB", "replConfigSource"), ("DATA-DOMAIN-MIB", "replConfigDest"), ("DATA-DOMAIN-MIB", "replConfigConnHost"), ("DATA-DOMAIN-MIB", "replConfigConnPort"), ("DATA-DOMAIN-MIB", "replConfigLowBWOptim"), ("DATA-DOMAIN-MIB", "replConfigEnabled"), ("DATA-DOMAIN-MIB", "replConfigTenantUnit"), ("DATA-DOMAIN-MIB", "replHistoryDate"), ("DATA-DOMAIN-MIB", "replHistoryTime"), ("DATA-DOMAIN-MIB", "replHistoryPreCompWritten"), ("DATA-DOMAIN-MIB", "replHistoryPreCompRemaining"), ("DATA-DOMAIN-MIB", "replHistoryPreCompressed"), ("DATA-DOMAIN-MIB", "replHistoryPostFiltered"), ("DATA-DOMAIN-MIB", "replHistoryPostLowBwOptim"), ("DATA-DOMAIN-MIB", "replHistoryPostLocalComp"), ("DATA-DOMAIN-MIB", "replHistoryBytesNetwork"), ("DATA-DOMAIN-MIB", "replHistorySyncedAsOfTime"), ("DATA-DOMAIN-MIB", "replTrapContext"), ("DATA-DOMAIN-MIB", "replPerformancePreCompKBPerSec"), ("DATA-DOMAIN-MIB", "replPerformanceNetworkKBPerSec"), ("DATA-DOMAIN-MIB", "replPerformanceStreams"), ("DATA-DOMAIN-MIB", "replPerformanceBusyReading"), ("DATA-DOMAIN-MIB", "replPerformanceBusyMeta"), ("DATA-DOMAIN-MIB", "replPerformanceWaitingDest"), ("DATA-DOMAIN-MIB", "replPerformanceWaitingNetwork"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    replGroup = replGroup.setStatus('current')
if mibBuilder.loadTexts: replGroup.setDescription('a collection of objects providing replication pair config and monitoring information.')
nfsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 12)).setObjects(("DATA-DOMAIN-MIB", "nfsStatus"), ("DATA-DOMAIN-MIB", "nfsClientPath"), ("DATA-DOMAIN-MIB", "nfsClientClients"), ("DATA-DOMAIN-MIB", "nfsClientOptions"), ("DATA-DOMAIN-MIB", "nfsStatsExportPoint"), ("DATA-DOMAIN-MIB", "nfsStatsFilesystemType"), ("DATA-DOMAIN-MIB", "nfsStatsCacheEntry"), ("DATA-DOMAIN-MIB", "nfsStatsFileHandleLookup"), ("DATA-DOMAIN-MIB", "nfsStatsMaxCacheSize"), ("DATA-DOMAIN-MIB", "nfsStatsCurrentOpenStreams"), ("DATA-DOMAIN-MIB", "nfsActivePath"), ("DATA-DOMAIN-MIB", "nfsActiveClients"), ("DATA-DOMAIN-MIB", "nfsPortService"), ("DATA-DOMAIN-MIB", "nfsPortPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nfsGroup = nfsGroup.setStatus('current')
if mibBuilder.loadTexts: nfsGroup.setDescription('A collection of objects providing NFS monitoring information.')
cifsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 13)).setObjects(("DATA-DOMAIN-MIB", "cifsStatus"), ("DATA-DOMAIN-MIB", "cifsConfigMode"), ("DATA-DOMAIN-MIB", "cifsConfigWINSServer"), ("DATA-DOMAIN-MIB", "cifsConfigNetBIOSHostname"), ("DATA-DOMAIN-MIB", "cifsConfigDomainController"), ("DATA-DOMAIN-MIB", "cifsConfigDNS"), ("DATA-DOMAIN-MIB", "cifsConfigGroupName"), ("DATA-DOMAIN-MIB", "cifsConfigMaxConnection"), ("DATA-DOMAIN-MIB", "cifsConfigMaxOpenFilesPerConnection"), ("DATA-DOMAIN-MIB", "cifsShareName"), ("DATA-DOMAIN-MIB", "cifsSharePath"), ("DATA-DOMAIN-MIB", "cifsShareClients"), ("DATA-DOMAIN-MIB", "cifsShareUser"), ("DATA-DOMAIN-MIB", "cifsShareComment"), ("DATA-DOMAIN-MIB", "cifsShareBrowsing"), ("DATA-DOMAIN-MIB", "cifsShareWriteable"), ("DATA-DOMAIN-MIB", "cifsShareMaxConnection"), ("DATA-DOMAIN-MIB", "cifsOptionsName"), ("DATA-DOMAIN-MIB", "cifsOptionsValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifsGroup = cifsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cifsGroup.setDescription('A collection of objects providing CIFS monitoring information.')
vtlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 14)).setObjects(("DATA-DOMAIN-MIB", "vtlAdminState"), ("DATA-DOMAIN-MIB", "vtlProcessState"), ("DATA-DOMAIN-MIB", "vtlLibraryName"), ("DATA-DOMAIN-MIB", "vtlLibraryVendor"), ("DATA-DOMAIN-MIB", "vtlLibraryModel"), ("DATA-DOMAIN-MIB", "vtlLibraryRevision"), ("DATA-DOMAIN-MIB", "vtlLibrarySerial"), ("DATA-DOMAIN-MIB", "vtlLibraryTotalDrives"), ("DATA-DOMAIN-MIB", "vtlLibraryTotalSlots"), ("DATA-DOMAIN-MIB", "vtlLibraryTotalCaps"), ("DATA-DOMAIN-MIB", "vtlLibraryStatus"), ("DATA-DOMAIN-MIB", "vtlDriveName"), ("DATA-DOMAIN-MIB", "vtlDriveVendor"), ("DATA-DOMAIN-MIB", "vtlDriveModel"), ("DATA-DOMAIN-MIB", "vtlDriveRevision"), ("DATA-DOMAIN-MIB", "vtlDriveSerial"), ("DATA-DOMAIN-MIB", "vtlDriveLibraryName"), ("DATA-DOMAIN-MIB", "vtlDriveStatus"), ("DATA-DOMAIN-MIB", "vtlDriveTapeVolume"), ("DATA-DOMAIN-MIB", "vtlGroupName"), ("DATA-DOMAIN-MIB", "vtlGroupInitiaterCount"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceCount"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceGroupName"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceDeviceName"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceLun"), ("DATA-DOMAIN-MIB", "vtlGroupDevicePrimaryPorts"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceSecondaryPorts"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceInUsePorts"), ("DATA-DOMAIN-MIB", "vtlInitiatorName"), ("DATA-DOMAIN-MIB", "vtlInitiatorStatus"), ("DATA-DOMAIN-MIB", "vtlInitiatorGroup"), ("DATA-DOMAIN-MIB", "vtlInitiatorWWNN"), ("DATA-DOMAIN-MIB", "vtlInitiatorWWPN"), ("DATA-DOMAIN-MIB", "vtlInitiatorPort"), ("DATA-DOMAIN-MIB", "vtlPoolPool"), ("DATA-DOMAIN-MIB", "vtlPoolStatus"), ("DATA-DOMAIN-MIB", "vtlPoolTapes"), ("DATA-DOMAIN-MIB", "vtlPoolSize"), ("DATA-DOMAIN-MIB", "vtlPoolUsed"), ("DATA-DOMAIN-MIB", "vtlPoolComp"), ("DATA-DOMAIN-MIB", "vtlPortName"), ("DATA-DOMAIN-MIB", "vtlPortID"), ("DATA-DOMAIN-MIB", "vtlPortModel"), ("DATA-DOMAIN-MIB", "vtlPortFirmware"), ("DATA-DOMAIN-MIB", "vtlPortWWNN"), ("DATA-DOMAIN-MIB", "vtlPortWWPN"), ("DATA-DOMAIN-MIB", "vtlPortConnectionType"), ("DATA-DOMAIN-MIB", "vtlPortSpeed"), ("DATA-DOMAIN-MIB", "vtlPortEnabled"), ("DATA-DOMAIN-MIB", "vtlPortStatus"), ("DATA-DOMAIN-MIB", "vtlPortTrapIndex"), ("DATA-DOMAIN-MIB", "vtlStatsPort"), ("DATA-DOMAIN-MIB", "vtlStatsConrolCommands"), ("DATA-DOMAIN-MIB", "vtlStatsWriteCommands"), ("DATA-DOMAIN-MIB", "vtlStatsReadCommands"), ("DATA-DOMAIN-MIB", "vtlStatsIn"), ("DATA-DOMAIN-MIB", "vtlStatsOut"), ("DATA-DOMAIN-MIB", "vtlStatsLinkFailures"), ("DATA-DOMAIN-MIB", "vtlStatsLIPCount"), ("DATA-DOMAIN-MIB", "vtlStatsSyncLosses"), ("DATA-DOMAIN-MIB", "vtlStatsSignalLosses"), ("DATA-DOMAIN-MIB", "vtlStatsPrimSeqProtoErrors"), ("DATA-DOMAIN-MIB", "vtlStatsInvalidTxWords"), ("DATA-DOMAIN-MIB", "vtlStatsInvalidCRCs"), ("DATA-DOMAIN-MIB", "vtlTapeBarCode"), ("DATA-DOMAIN-MIB", "vtlTapePool"), ("DATA-DOMAIN-MIB", "vtlTapeLocation"), ("DATA-DOMAIN-MIB", "vtlTapeState"), ("DATA-DOMAIN-MIB", "vtlTapeSize"), ("DATA-DOMAIN-MIB", "vtlTapeUsed"), ("DATA-DOMAIN-MIB", "vtlTapeComp"), ("DATA-DOMAIN-MIB", "vtlTapeModTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vtlGroup = vtlGroup.setStatus('current')
if mibBuilder.loadTexts: vtlGroup.setDescription('A collection of objects providing VTL monitoring information.')
ddboostGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 15)).setObjects(("DATA-DOMAIN-MIB", "ddboostAccessClientsName"), ("DATA-DOMAIN-MIB", "ddboostAccessClientsEncryStrength"), ("DATA-DOMAIN-MIB", "ddboostAccessClientsAuthMode"), ("DATA-DOMAIN-MIB", "ddboostInterface"), ("DATA-DOMAIN-MIB", "ddboostifGroupMember"), ("DATA-DOMAIN-MIB", "ddboostBackupConnections"), ("DATA-DOMAIN-MIB", "ddboostRestoreConnections"), ("DATA-DOMAIN-MIB", "ddboostControlConnections"), ("DATA-DOMAIN-MIB", "ddboostTotalConnections"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryNetwork"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPreComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPostComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryErrors"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDate"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryTime"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsNetworkSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsPreCompSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsFiltered"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLocalComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsCompRatio"), ("DATA-DOMAIN-MIB", "ddboostIfGroupInterface"), ("DATA-DOMAIN-MIB", "ddboostOptionsName"), ("DATA-DOMAIN-MIB", "ddboostOptionsStatus"), ("DATA-DOMAIN-MIB", "ddboostStatus"), ("DATA-DOMAIN-MIB", "ddboostUser"), ("DATA-DOMAIN-MIB", "ddboostIfGroupStatus"), ("DATA-DOMAIN-MIB", "ddboostPreCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostPostCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostNetworkKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostStatsBackupConn"), ("DATA-DOMAIN-MIB", "ddboostStatsRestoreConn"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsPrecompBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterFiltering"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterLc"), ("DATA-DOMAIN-MIB", "ddboostStatsNetworkBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsCompressionRatio"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadCount"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadErrors"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitName"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitBytes"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitGlobalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitLocalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitMetaData"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInNetworkKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutNetworkKBPerSec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddboostGroup = ddboostGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ddboostGroup.setDescription('A collection of objects providing DDBoost monitoring information.')
ddsystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 16)).setObjects(("DATA-DOMAIN-MIB", "systemLicenseKey"), ("DATA-DOMAIN-MIB", "systemLicenseFeature"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseKey"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseFeature"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseModel"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseCapacity"), ("DATA-DOMAIN-MIB", "systemHardwareSlot"), ("DATA-DOMAIN-MIB", "systemHardwareVendor"), ("DATA-DOMAIN-MIB", "systemHardwareDevice"), ("DATA-DOMAIN-MIB", "systemHardwarePorts"), ("DATA-DOMAIN-MIB", "systemPortsPort"), ("DATA-DOMAIN-MIB", "systemPortsConnectionType"), ("DATA-DOMAIN-MIB", "systemPortsLinkSpeed"), ("DATA-DOMAIN-MIB", "systemPortsFirmware"), ("DATA-DOMAIN-MIB", "systemPortsHardwareAddress"), ("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "systemCurrentTime"), ("DATA-DOMAIN-MIB", "systemVersion"), ("DATA-DOMAIN-MIB", "systemModelNumber"), ("DATA-DOMAIN-MIB", "sysNotes"), ("DATA-DOMAIN-MIB", "systemTimeZoneName"), ("DATA-DOMAIN-MIB", "systemUserName"), ("DATA-DOMAIN-MIB", "systemUserUID"), ("DATA-DOMAIN-MIB", "systemUserRole"), ("DATA-DOMAIN-MIB", "systemUserStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddsystemGroup = ddsystemGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ddsystemGroup.setDescription('A collection of objects providing system monitoring information.')
artGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 17)).setObjects(("DATA-DOMAIN-MIB", "artConfigStatus"), ("DATA-DOMAIN-MIB", "artConfigMigrationSchedule"), ("DATA-DOMAIN-MIB", "artConfigDefaultAge"), ("DATA-DOMAIN-MIB", "artConfigFileSystemClean"), ("DATA-DOMAIN-MIB", "artConfigCompression"), ("DATA-DOMAIN-MIB", "artMigrationPolicyMtreeName"), ("DATA-DOMAIN-MIB", "artMigrationPolicyDefaultAge"), ("DATA-DOMAIN-MIB", "artMigrationScheduleSchedule"), ("DATA-DOMAIN-MIB", "artMigrationScheduleStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    artGroup = artGroup.setStatus('current')
if mibBuilder.loadTexts: artGroup.setDescription('A collection of objects providing art monitoring information.')
mtreeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 18)).setObjects(("DATA-DOMAIN-MIB", "mtreeCompressionMtreePath"), ("DATA-DOMAIN-MIB", "mtreeCompressionPreCompGib"), ("DATA-DOMAIN-MIB", "mtreeCompressionPostCompGib"), ("DATA-DOMAIN-MIB", "mtreeCompressionGlobalCompFactor"), ("DATA-DOMAIN-MIB", "mtreeCompressionLocalCompFactor"), ("DATA-DOMAIN-MIB", "mtreeCompressionPostTotalCompFactor"), ("DATA-DOMAIN-MIB", "mtreeCompressionTimePeriod"), ("DATA-DOMAIN-MIB", "mtreeListMtreeName"), ("DATA-DOMAIN-MIB", "mtreeListPreCompGib"), ("DATA-DOMAIN-MIB", "mtreeListStatus"), ("DATA-DOMAIN-MIB", "mtreeRetentionLockMtreeName"), ("DATA-DOMAIN-MIB", "mtreeRetentionLockStatus"), ("DATA-DOMAIN-MIB", "mtreeRetentionLockUUID"), ("DATA-DOMAIN-MIB", "mtreeRetentionLockMinRetentionPeriod"), ("DATA-DOMAIN-MIB", "mtreeRetentionLockMaxRetentionPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mtreeGroup = mtreeGroup.setStatus('current')
if mibBuilder.loadTexts: mtreeGroup.setDescription('A collection of objects providing mtree monitoring information.')
enclosureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 19)).setObjects(("DATA-DOMAIN-MIB", "enclosureListNum"), ("DATA-DOMAIN-MIB", "enclosureListModel"), ("DATA-DOMAIN-MIB", "enclosureListSerialNum"), ("DATA-DOMAIN-MIB", "enclosureListOemName"), ("DATA-DOMAIN-MIB", "enclosureListOemValue"), ("DATA-DOMAIN-MIB", "enclosureListCapacity"), ("DATA-DOMAIN-MIB", "enclosurePackID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    enclosureGroup = enclosureGroup.setStatus('current')
if mibBuilder.loadTexts: enclosureGroup.setDescription('A collection of objects providing enclousure information.')
managedObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 20)).setObjects(("DATA-DOMAIN-MIB", "managedSystemHostname"), ("DATA-DOMAIN-MIB", "managedSystemSerial"), ("DATA-DOMAIN-MIB", "managedSystemState"), ("DATA-DOMAIN-MIB", "managedSystemStatus"), ("DATA-DOMAIN-MIB", "managedSystemDDOSVersion"), ("DATA-DOMAIN-MIB", "managedSystemHDSyncTime"), ("DATA-DOMAIN-MIB", "managedSystemCDSyncTime"), ("DATA-DOMAIN-MIB", "taskHistoryUser"), ("DATA-DOMAIN-MIB", "taskHistoryID"), ("DATA-DOMAIN-MIB", "taskHistoryParent"), ("DATA-DOMAIN-MIB", "taskHistoryName"), ("DATA-DOMAIN-MIB", "taskHistoryState"), ("DATA-DOMAIN-MIB", "taskHistoryStartTime"), ("DATA-DOMAIN-MIB", "taskHistoryDuration"), ("DATA-DOMAIN-MIB", "taskActiveUser"), ("DATA-DOMAIN-MIB", "taskActiveID"), ("DATA-DOMAIN-MIB", "taskActiveParent"), ("DATA-DOMAIN-MIB", "taskActiveName"), ("DATA-DOMAIN-MIB", "taskActiveState"), ("DATA-DOMAIN-MIB", "taskActiveStartTime"), ("DATA-DOMAIN-MIB", "taskActiveDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    managedObjectsGroup = managedObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: managedObjectsGroup.setDescription('A collection of objects providing ddms system information.')
networkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 21)).setObjects(("DATA-DOMAIN-MIB", "dnsServer"), ("DATA-DOMAIN-MIB", "searchDomainsName"), ("DATA-DOMAIN-MIB", "snmpTrapHostsName"), ("DATA-DOMAIN-MIB", "snmpTrapHostsVersion"), ("DATA-DOMAIN-MIB", "nisDomain"), ("DATA-DOMAIN-MIB", "nisServers"), ("DATA-DOMAIN-MIB", "nisAdminGroups"), ("DATA-DOMAIN-MIB", "nisUserGroups"), ("DATA-DOMAIN-MIB", "nisBackupOperatorGroups"), ("DATA-DOMAIN-MIB", "nisEnabled"), ("DATA-DOMAIN-MIB", "nisStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    networkGroup = networkGroup.setStatus('current')
if mibBuilder.loadTexts: networkGroup.setDescription('A collection of objects providing network information.')
fileSystemGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 22)).setObjects(("DATA-DOMAIN-MIB", "fileSystemStatus"), ("DATA-DOMAIN-MIB", "fileSystemVirtualSpace"), ("DATA-DOMAIN-MIB", "fileSystemResourceName"), ("DATA-DOMAIN-MIB", "fileSystemSpaceSize"), ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"), ("DATA-DOMAIN-MIB", "fileSystemSpaceAvail"), ("DATA-DOMAIN-MIB", "fileSystemPercentUsed"), ("DATA-DOMAIN-MIB", "fileSystemSpaceCleanable"), ("DATA-DOMAIN-MIB", "fileSystemResourceTier"), ("DATA-DOMAIN-MIB", "fileSystemCompressionPeriod"), ("DATA-DOMAIN-MIB", "fileSystemCompressionStartTime"), ("DATA-DOMAIN-MIB", "fileSystemCompressionEndTime"), ("DATA-DOMAIN-MIB", "fileSystemPreCompressionSize"), ("DATA-DOMAIN-MIB", "fileSystemPostCompressionSize"), ("DATA-DOMAIN-MIB", "fileSystemGlobalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemLocalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemTotalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitName"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitState"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitStatus"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitStartTime"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitEndTime"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitSize"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitDiskGroups"), ("DATA-DOMAIN-MIB", "fileSystemCleanStatus"), ("DATA-DOMAIN-MIB", "fileSystemCleanSchedule"), ("DATA-DOMAIN-MIB", "fileSystemCleanThrottle"), ("DATA-DOMAIN-MIB", "fileSystemReductionPercent1"), ("DATA-DOMAIN-MIB", "fileSystemOptionsName"), ("DATA-DOMAIN-MIB", "fileSystemOptionsValue"), ("DATA-DOMAIN-MIB", "fileSystemUpTime"), ("DATA-DOMAIN-MIB", "fileSystemStatusMessage"), ("DATA-DOMAIN-MIB", "fileSystemResourceTrapIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fileSystemGroupRev1 = fileSystemGroupRev1.setStatus('current')
if mibBuilder.loadTexts: fileSystemGroupRev1.setDescription('A collection of objects providing file system monitoring information.')
ddsystemGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 23)).setObjects(("DATA-DOMAIN-MIB", "systemLicenseKey"), ("DATA-DOMAIN-MIB", "systemLicenseFeature"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseKey"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseFeature"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseModel"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseCapacity"), ("DATA-DOMAIN-MIB", "systemHardwareVendor"), ("DATA-DOMAIN-MIB", "systemHardwareDevice"), ("DATA-DOMAIN-MIB", "systemHardwarePorts"), ("DATA-DOMAIN-MIB", "systemHardwareSlotName"), ("DATA-DOMAIN-MIB", "systemPortsPort"), ("DATA-DOMAIN-MIB", "systemPortsConnectionType"), ("DATA-DOMAIN-MIB", "systemPortsLinkSpeed"), ("DATA-DOMAIN-MIB", "systemPortsFirmware"), ("DATA-DOMAIN-MIB", "systemPortsHardwareAddress"), ("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "systemCurrentTime"), ("DATA-DOMAIN-MIB", "systemVersion"), ("DATA-DOMAIN-MIB", "systemModelNumber"), ("DATA-DOMAIN-MIB", "systemTimeZoneName"), ("DATA-DOMAIN-MIB", "systemUserName"), ("DATA-DOMAIN-MIB", "systemUserUID"), ("DATA-DOMAIN-MIB", "systemUserRole"), ("DATA-DOMAIN-MIB", "systemUserStatus"), ("DATA-DOMAIN-MIB", "systemActiveUserName"), ("DATA-DOMAIN-MIB", "systemActiveUserIdleTime"), ("DATA-DOMAIN-MIB", "systemActiveUserLoginTime"), ("DATA-DOMAIN-MIB", "systemActiveUserLoginFrom"), ("DATA-DOMAIN-MIB", "systemActiveUserTty"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddsystemGroupRev1 = ddsystemGroupRev1.setStatus('current')
if mibBuilder.loadTexts: ddsystemGroupRev1.setDescription('A collection of objects providing system monitoring information.')
smtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 24)).setObjects(("DATA-DOMAIN-MIB", "smtStatus"), ("DATA-DOMAIN-MIB", "tenantUnitListName"), ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfMgmtUsers"), ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfMtrees"), ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfDdboostStus"), ("DATA-DOMAIN-MIB", "tenantUnitListTenantSelfServiceMode"), ("DATA-DOMAIN-MIB", "tenantUnitListParentTenantName"), ("DATA-DOMAIN-MIB", "tenantUnitListType"), ("DATA-DOMAIN-MIB", "tenantUnitListSecurityMode"), ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfMgmtGroups"), ("DATA-DOMAIN-MIB", "tenantUnitMgmtUserListUserRole"), ("DATA-DOMAIN-MIB", "tenantUnitMtreeListMtreeName"), ("DATA-DOMAIN-MIB", "tenantUnitDdboostStuListStuName"), ("DATA-DOMAIN-MIB", "tenantUnitAdminIpInfoType"), ("DATA-DOMAIN-MIB", "tenantInfoTenantName"), ("DATA-DOMAIN-MIB", "tenantInfoTenantUnitName"), ("DATA-DOMAIN-MIB", "tenantUnitMgmtGroupListGroupRole"), ("DATA-DOMAIN-MIB", "tenantUnitMgmtGroupListGroupType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smtGroup = smtGroup.setStatus('current')
if mibBuilder.loadTexts: smtGroup.setDescription('A collection of objects providing Secure Multi-Tenancy (SMT) information.')
quotaGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 25)).setObjects(("DATA-DOMAIN-MIB", "quotaCapacityStatus"), ("DATA-DOMAIN-MIB", "quotaCapacityMtreeName"), ("DATA-DOMAIN-MIB", "quotaCapacityPreCompMiB"), ("DATA-DOMAIN-MIB", "quotaCapacitySoftLimitMiB"), ("DATA-DOMAIN-MIB", "quotaCapacityHardLimitMiB"), ("DATA-DOMAIN-MIB", "quotaCapacityTenantUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    quotaGroup = quotaGroup.setStatus('current')
if mibBuilder.loadTexts: quotaGroup.setDescription('A collection of objects providing quota information.')
ddboostGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 26)).setObjects(("DATA-DOMAIN-MIB", "ddboostAccessClientsName"), ("DATA-DOMAIN-MIB", "ddboostInterface"), ("DATA-DOMAIN-MIB", "ddboostifGroupMember"), ("DATA-DOMAIN-MIB", "ddboostBackupConnections"), ("DATA-DOMAIN-MIB", "ddboostRestoreConnections"), ("DATA-DOMAIN-MIB", "ddboostControlConnections"), ("DATA-DOMAIN-MIB", "ddboostTotalConnections"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryNetwork"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPreComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPostComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryErrors"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDate"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryTime"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsNetworkSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsPreCompSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsFiltered"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLocalComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsCompRatio"), ("DATA-DOMAIN-MIB", "ddboostIfGroupInterface"), ("DATA-DOMAIN-MIB", "ddboostOptionsName"), ("DATA-DOMAIN-MIB", "ddboostOptionsStatus"), ("DATA-DOMAIN-MIB", "ddboostStatus"), ("DATA-DOMAIN-MIB", "ddboostUserName"), ("DATA-DOMAIN-MIB", "ddboostIfGroupStatus"), ("DATA-DOMAIN-MIB", "ddboostPreCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostPostCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostNetworkKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostStatsBackupConn"), ("DATA-DOMAIN-MIB", "ddboostStatsRestoreConn"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsPrecompBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterFiltering"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterLc"), ("DATA-DOMAIN-MIB", "ddboostStatsNetworkBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsCompressionRatio"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadCount"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadErrors"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitName"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitBytes"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitGlobalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitLocalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitMetaData"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInNetworkKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutNetworkKBPerSec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddboostGroupRev1 = ddboostGroupRev1.setStatus('deprecated')
if mibBuilder.loadTexts: ddboostGroupRev1.setDescription('A collection of objects providing DDBoost monitoring information.')
ddboostGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 27)).setObjects(("DATA-DOMAIN-MIB", "ddboostAccessClientsName"), ("DATA-DOMAIN-MIB", "ddboostInterface"), ("DATA-DOMAIN-MIB", "ddboostifGroupMember"), ("DATA-DOMAIN-MIB", "ddboostBackupConnections"), ("DATA-DOMAIN-MIB", "ddboostRestoreConnections"), ("DATA-DOMAIN-MIB", "ddboostControlConnections"), ("DATA-DOMAIN-MIB", "ddboostTotalConnections"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryNetwork"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPreComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPostComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryErrors"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDate"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryTime"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsNetworkSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsPreCompSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsFiltered"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLocalComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsCompRatio"), ("DATA-DOMAIN-MIB", "ddboostIfGroupInterface"), ("DATA-DOMAIN-MIB", "ddboostOptionsName"), ("DATA-DOMAIN-MIB", "ddboostOptionsStatus"), ("DATA-DOMAIN-MIB", "ddboostStatus"), ("DATA-DOMAIN-MIB", "ddboostUserName"), ("DATA-DOMAIN-MIB", "ddboostUserDefaultTenantUnit"), ("DATA-DOMAIN-MIB", "ddboostIfGroupName"), ("DATA-DOMAIN-MIB", "ddboostIfGroupCurrentStatus"), ("DATA-DOMAIN-MIB", "ddboostPreCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostPostCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostNetworkKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostStatsBackupConn"), ("DATA-DOMAIN-MIB", "ddboostStatsRestoreConn"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsPrecompBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterFiltering"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterLc"), ("DATA-DOMAIN-MIB", "ddboostStatsNetworkBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsCompressionRatio"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadCount"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadErrors"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitName"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitBytes"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitGlobalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitLocalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitMetaData"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitStatus"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitPreComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitUser"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitReportPhysicalSize"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInNetworkKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutNetworkKBPerSec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddboostGroupRev2 = ddboostGroupRev2.setStatus('current')
if mibBuilder.loadTexts: ddboostGroupRev2.setDescription('A collection of objects providing DDBoost monitoring information.')
highAvailabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 28)).setObjects(("DATA-DOMAIN-MIB", "haSystemName"), ("DATA-DOMAIN-MIB", "haSystemStatus"), ("DATA-DOMAIN-MIB", "haInterconnectStatus"), ("DATA-DOMAIN-MIB", "haPrimaryHeartbeatStatus"), ("DATA-DOMAIN-MIB", "haExternalLanHeartbeatStatus"), ("DATA-DOMAIN-MIB", "haHardwareCompatibilityCheck"), ("DATA-DOMAIN-MIB", "haSoftwareVersionCheck"), ("DATA-DOMAIN-MIB", "highAvailabilityNodeName"), ("DATA-DOMAIN-MIB", "highAvailabilityNodeId"), ("DATA-DOMAIN-MIB", "highAvailabilityNodeRole"), ("DATA-DOMAIN-MIB", "highAvailabilityNodeState"), ("DATA-DOMAIN-MIB", "highAvailabilityNodeHealth"), ("DATA-DOMAIN-MIB", "highAvailabilityComponentName"), ("DATA-DOMAIN-MIB", "highAvailabilityComponentState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    highAvailabilityGroup = highAvailabilityGroup.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityGroup.setDescription('A collection of objects providing High Availability information.')
scsitargetObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 29)).setObjects(("DATA-DOMAIN-MIB", "scsitargetAdminState"), ("DATA-DOMAIN-MIB", "scsitargetProcessState"), ("DATA-DOMAIN-MIB", "scsitargetGroupName"), ("DATA-DOMAIN-MIB", "scsitargetGroupService"), ("DATA-DOMAIN-MIB", "scsitargetGroupActiveState"), ("DATA-DOMAIN-MIB", "scsitargetGroupNumInitiators"), ("DATA-DOMAIN-MIB", "scsitargetGroupNumDevices"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorName"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorSystemAddress"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorGroup"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorService"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorAddressMethod"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorTransport"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorFcWwpn"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorFcWwnn"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorFcSymbolicPortName"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorEndpInitiator"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorEndpEndpoint"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorEndpStatus"), ("DATA-DOMAIN-MIB", "scsitargetEndpointName"), ("DATA-DOMAIN-MIB", "scsitargetEndpointCurrentSystemAddress"), ("DATA-DOMAIN-MIB", "scsitargetEndpointPrimarySystemAddress"), ("DATA-DOMAIN-MIB", "scsitargetEndpointSecondarySystemAddress"), ("DATA-DOMAIN-MIB", "scsitargetEndpointEnabled"), ("DATA-DOMAIN-MIB", "scsitargetEndpointStatus"), ("DATA-DOMAIN-MIB", "scsitargetEndpointTransport"), ("DATA-DOMAIN-MIB", "scsitargetEndpointFcWwnn"), ("DATA-DOMAIN-MIB", "scsitargetEndpointFcWwpn"), ("DATA-DOMAIN-MIB", "scsitargetPortSystemAddress"), ("DATA-DOMAIN-MIB", "scsitargetPortEnabled"), ("DATA-DOMAIN-MIB", "scsitargetPortStatus"), ("DATA-DOMAIN-MIB", "scsitargetPortTransport"), ("DATA-DOMAIN-MIB", "scsitargetPortOperationalStatus"), ("DATA-DOMAIN-MIB", "scsitargetPortFcNpiv"), ("DATA-DOMAIN-MIB", "scsitargetPortPortId"), ("DATA-DOMAIN-MIB", "scsitargetPortModel"), ("DATA-DOMAIN-MIB", "scsitargetPortFirmware"), ("DATA-DOMAIN-MIB", "scsitargetPortFcBaseWwnn"), ("DATA-DOMAIN-MIB", "scsitargetPortFcBaseWwpn"), ("DATA-DOMAIN-MIB", "scsitargetPortFcCurrentWwnn"), ("DATA-DOMAIN-MIB", "scsitargetPortFcCurrentWwpn"), ("DATA-DOMAIN-MIB", "scsitargetPortFcp2Retry"), ("DATA-DOMAIN-MIB", "scsitargetPortConnectionType"), ("DATA-DOMAIN-MIB", "scsitargetPortLinkSpeed"), ("DATA-DOMAIN-MIB", "scsitargetPortFcTopology"), ("DATA-DOMAIN-MIB", "scsitargetPortEndpPort"), ("DATA-DOMAIN-MIB", "scsitargetPortEndpEndpoint"), ("DATA-DOMAIN-MIB", "scsitargetPortEndpEnabled"), ("DATA-DOMAIN-MIB", "scsitargetPortEndpStatus"), ("DATA-DOMAIN-MIB", "scsitargetPortEndpCurrentInstance"), ("DATA-DOMAIN-MIB", "scsitargetDeviceName"), ("DATA-DOMAIN-MIB", "scsitargetDeviceService"), ("DATA-DOMAIN-MIB", "scsitargetDeviceActiveState"), ("DATA-DOMAIN-MIB", "scsitargetDeviceAddress"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpDevice"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpGroupName"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpLun"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpPrimaryEndpoints"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpSecondaryEndpoints"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpInUseEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    scsitargetObjectGroup = scsitargetObjectGroup.setStatus('current')
if mibBuilder.loadTexts: scsitargetObjectGroup.setDescription('A collection of objects providing Scsitarget information.')
cifsGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 30)).setObjects(("DATA-DOMAIN-MIB", "cifsStatus"), ("DATA-DOMAIN-MIB", "cifsConfigMode"), ("DATA-DOMAIN-MIB", "cifsConfigWINSServer"), ("DATA-DOMAIN-MIB", "cifsConfigNetBIOSHostname"), ("DATA-DOMAIN-MIB", "cifsConfigDomainController"), ("DATA-DOMAIN-MIB", "cifsConfigDNS"), ("DATA-DOMAIN-MIB", "cifsConfigGroupName"), ("DATA-DOMAIN-MIB", "cifsConfigMaxConnection"), ("DATA-DOMAIN-MIB", "cifsConfigMaxOpenFiles"), ("DATA-DOMAIN-MIB", "cifsShareName"), ("DATA-DOMAIN-MIB", "cifsSharePath"), ("DATA-DOMAIN-MIB", "cifsShareClients"), ("DATA-DOMAIN-MIB", "cifsShareUser"), ("DATA-DOMAIN-MIB", "cifsShareComment"), ("DATA-DOMAIN-MIB", "cifsShareBrowsing"), ("DATA-DOMAIN-MIB", "cifsShareWriteable"), ("DATA-DOMAIN-MIB", "cifsShareMaxConnection"), ("DATA-DOMAIN-MIB", "cifsOptionsName"), ("DATA-DOMAIN-MIB", "cifsOptionsValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifsGroupRev1 = cifsGroupRev1.setStatus('current')
if mibBuilder.loadTexts: cifsGroupRev1.setDescription('A collection of objects providing CIFS monitoring information.')
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", VtlLibraryTotalSlotsTC=VtlLibraryTotalSlotsTC, scsitargetDeviceGrpGroupName=scsitargetDeviceGrpGroupName, NfsStatsCurrentOpenStreamsTC=NfsStatsCurrentOpenStreamsTC, sASHBAFailure=sASHBAFailure, nvramWriteKBytesPerSecond=nvramWriteKBytesPerSecond, abnormalShutdown=abnormalShutdown, ddboostStatsImageDeletesCount=ddboostStatsImageDeletesCount, scsitargetPortEndpEntry=scsitargetPortEndpEntry, ddboostStorageUnitGlobalComp=ddboostStorageUnitGlobalComp, nfsActiveEntry=nfsActiveEntry, DiskIndexTC=DiskIndexTC, nfsStatsEntry=nfsStatsEntry, artConfigCompression=artConfigCompression, ddboostStatsIndex=ddboostStatsIndex, nfsClientClients=nfsClientClients, artMigrationPolicyTable=artMigrationPolicyTable, mtreeCompressionGlobalCompFactor=mtreeCompressionGlobalCompFactor, diskFailedAlarm=diskFailedAlarm, nfsStatsCurrentOpenStreams=nfsStatsCurrentOpenStreams, scsitargetPortStatus=scsitargetPortStatus, replicationInfoEntry=replicationInfoEntry, replicationHistory=replicationHistory, vtlStatsWriteCommands=vtlStatsWriteCommands, ddboostIfGroupCurrentStatus=ddboostIfGroupCurrentStatus, systemCurrentTime=systemCurrentTime, vtlTape=vtlTape, dDFSFailedInShutdown=dDFSFailedInShutdown, vtlAdminState=vtlAdminState, fileSystemCleanThrottle=fileSystemCleanThrottle, scsitargetInitiatorAddressMethod=scsitargetInitiatorAddressMethod, diskPerformanceTable=diskPerformanceTable, NvramIndexTC=NvramIndexTC, fileSystemPercentUsed=fileSystemPercentUsed, missingSlaveInterface=missingSlaveInterface, tenantUnitListTable=tenantUnitListTable, FileSystemOptionsNameTC=FileSystemOptionsNameTC, fileSystemLocalCompressionFactor=fileSystemLocalCompressionFactor, replHistoryPreCompWritten=replHistoryPreCompWritten, CifsOptionsIndexTC=CifsOptionsIndexTC, tenantInfoTenantUnitName=tenantInfoTenantUnitName, dd890=dd890, physicalCapacityMeasurementTasksLost=physicalCapacityMeasurementTasksLost, foreignPack=foreignPack, nvramEventHWAlert=nvramEventHWAlert, dDFSRebootedDisabled=dDFSRebootedDisabled, fileSystemCompressionStartTime=fileSystemCompressionStartTime, vtlConfiguration=vtlConfiguration, vtlStatsLinkFailures=vtlStatsLinkFailures, ddboostStatsNetworkBytesReceived=ddboostStatsNetworkBytesReceived, haExternalLanHeartbeatStatus=haExternalLanHeartbeatStatus, lowSpares=lowSpares, replConfigEnabled=replConfigEnabled, sSLCertificateCorrupted=sSLCertificateCorrupted, haSystemStatus=haSystemStatus, dd530=dd530, fileSystemCleanStatus=fileSystemCleanStatus, driveMixType=driveMixType, artConfigDefaultAge=artConfigDefaultAge, DDMibTableSizeGibTC=DDMibTableSizeGibTC, systemCapacityLicenseEntry=systemCapacityLicenseEntry, dataDomainMibNotifications=dataDomainMibNotifications, vtlTapeUsed=vtlTapeUsed, licenseExpiring=licenseExpiring, tenantInfoTable=tenantInfoTable, artConfigFileSystemClean=artConfigFileSystemClean, vtlDriveLibraryName=vtlDriveLibraryName, quotaCapacityStatus=quotaCapacityStatus, physicalCapacityMeasurementScheduleFailed=physicalCapacityMeasurementScheduleFailed, FanDescriptionTC=FanDescriptionTC, mtreeRetentionLock=mtreeRetentionLock, haSystemName=haSystemName, dDFSDied=dDFSDied, replPostCompBytesReceived=replPostCompBytesReceived, dIMMFailureAlert=dIMMFailureAlert, managedSystemIndex=managedSystemIndex, ddboostIfGroupConfigTable=ddboostIfGroupConfigTable, vtlTapeTable=vtlTapeTable, mtreeCompressionTable=mtreeCompressionTable, powerSupplyWarning=powerSupplyWarning, nfsStatsIndex=nfsStatsIndex, vtlTapeBarCode=vtlTapeBarCode, DDMibTimeStampTC=DDMibTimeStampTC, FileSystemCleanIndexTC=FileSystemCleanIndexTC, scsitargetPortFcTopology=scsitargetPortFcTopology, ddboostFileReplStatsCompRatio=ddboostFileReplStatsCompRatio, voltageWarning=voltageWarning, controllerUnreachableAlert=controllerUnreachableAlert, VtlLibraryStatusTC=VtlLibraryStatusTC, diskPerfIndex=diskPerfIndex, ddboostGroupRev2=ddboostGroupRev2, diskGroupReconstructionCritical=diskGroupReconstructionCritical, vtlStatsIn=vtlStatsIn, TempSensorDescriptionTC=TempSensorDescriptionTC, ReplicationConfigIndexTC=ReplicationConfigIndexTC, ddboostUserIdx=ddboostUserIdx, tenantUnitDdboostStuListEntry=tenantUnitDdboostStuListEntry, tempEnclosureID=tempEnclosureID, ddboostFileReplicationStatsEntry=ddboostFileReplicationStatsEntry, nfsClientPath=nfsClientPath, mtreeCompressionPreCompGib=mtreeCompressionPreCompGib, quotaCapacityIndex=quotaCapacityIndex, nfsStatsFilesystemType=nfsStatsFilesystemType, fanLevel=fanLevel, tenantUnitMgmtGroupListTable=tenantUnitMgmtGroupListTable, systemActiveUserIndex=systemActiveUserIndex, vtl=vtl, powerModuleTable=powerModuleTable, FileSystemArchiveUnitStateTC=FileSystemArchiveUnitStateTC, vtlPortModel=vtlPortModel, highAvailabilityStatus=highAvailabilityStatus, FileSystemOptionsIndexTC=FileSystemOptionsIndexTC, VtlTapeIndexTC=VtlTapeIndexTC, ddboostStorageUnitIndex=ddboostStorageUnitIndex, systemUserName=systemUserName, unsupportedDriveModel=unsupportedDriveModel, systemStatsEntry=systemStatsEntry, sASHBAErrors=sASHBAErrors, scsitarget=scsitarget, nfsPortPort=nfsPortPort, spaceReclError=spaceReclError, fanProperties=fanProperties, sMSUnresponsive=sMSUnresponsive, alertInfoTable=alertInfoTable, systemUserStatus=systemUserStatus, replHistorySyncedAsOfTime=replHistorySyncedAsOfTime, taskHistoryName=taskHistoryName, ddboostStorageUnitLocalComp=ddboostStorageUnitLocalComp, fileSystemTotalCompressionFactor=fileSystemTotalCompressionFactor, upgradeCompleted=upgradeCompleted, replNeedResync=replNeedResync, scsitargetInitiatorTable=scsitargetInitiatorTable, dd4500=dd4500, VtlStatsPrimSeqProtoErrorsTC=VtlStatsPrimSeqProtoErrorsTC, diskOverheatShutdownAlarm=diskOverheatShutdownAlarm, ddboostControlConnections=ddboostControlConnections, vtlLibraryModel=vtlLibraryModel, scsitargetInitiatorTransport=scsitargetInitiatorTransport, HaStatusTC=HaStatusTC, ddboostStorageUnitPreComp=ddboostStorageUnitPreComp, DDMibCompressionFactorTC=DDMibCompressionFactorTC, powerModuleStatus=powerModuleStatus, ddboostConnectionsTable=ddboostConnectionsTable, fileSystemFailedAlarm=fileSystemFailedAlarm, ReplicationPathTC=ReplicationPathTC, VtlLibraryTotalCapsTC=VtlLibraryTotalCapsTC, controllerIfaceUnreachableAlert=controllerIfaceUnreachableAlert, systemCapacityLicenseCapacity=systemCapacityLicenseCapacity, ddboostStatsBytesAfterLc=ddboostStatsBytesAfterLc, historicalDatabaseUpgradeError=historicalDatabaseUpgradeError, vtlGroupDeviceDeviceName=vtlGroupDeviceDeviceName, fileSystemVirtualSpace=fileSystemVirtualSpace, taskHistoryParent=taskHistoryParent, replPreCompBytesRemaining=replPreCompBytesRemaining, VtlLibraryIndexTC=VtlLibraryIndexTC, nfsStatus=nfsStatus, nfsStatsExportPoint=nfsStatsExportPoint, enclosurePackID=enclosurePackID, managedSystem=managedSystem, diskReliability=diskReliability, fileSystemSpaceCleanable=fileSystemSpaceCleanable, snapshotOver90Percent=snapshotOver90Percent, fileSystemArchiveUnit=fileSystemArchiveUnit, ddboostUserName=ddboostUserName, DDMibTableString32TC=DDMibTableString32TC, scsitargetPortEndpTable=scsitargetPortEndpTable, nvramFailingAlarm=nvramFailingAlarm, diskOverheatAlertAlarm=diskOverheatAlertAlarm, mtreeCompressionTimePeriod=mtreeCompressionTimePeriod, vtlDriveStatus=vtlDriveStatus, managedSystemCDSyncTime=managedSystemCDSyncTime, KBytesPerSecond=KBytesPerSecond, fileSystemStatus=fileSystemStatus, VtlPortConnectionTypeTC=VtlPortConnectionTypeTC, quotaCapacityTable=quotaCapacityTable, scsitargetDeviceGrpInUseEndpoints=scsitargetDeviceGrpInUseEndpoints, missingLunPath=missingLunPath, fileSpacePreWarningAlarm=fileSpacePreWarningAlarm, PYSNMP_MODULE_ID=dataDomainMib, ddboostTotalConnections=ddboostTotalConnections, tenantUnitMgmtGroupListEntry=tenantUnitMgmtGroupListEntry, generatedNotificationsGroup=generatedNotificationsGroup, invalidHardwareCritical=invalidHardwareCritical, dd565=dd565, enclosureListIndex=enclosureListIndex, DDMibAlertSeverityTC=DDMibAlertSeverityTC, nvramBatteryCharge=nvramBatteryCharge, CifsConfigMaxOpenFilesPerConnectionTC=CifsConfigMaxOpenFilesPerConnectionTC, cifsShareName=cifsShareName, tenantUnitMgmtUserListTable=tenantUnitMgmtUserListTable, unsupportedEnclosurePSU=unsupportedEnclosurePSU, systemHardwareDevice=systemHardwareDevice, storageUnitStreamSoftLimit=storageUnitStreamSoftLimit, diskReallocCount=diskReallocCount, tenantUnitMgmtUserListEntry=tenantUnitMgmtUserListEntry, scsitargetGroupService=scsitargetGroupService, nfsProperties=nfsProperties, FileSystemResourceNameTC=FileSystemResourceNameTC, raidReconCriticalShutdownAlarm=raidReconCriticalShutdownAlarm, tenantUnitMgmtGroupListGroupName=tenantUnitMgmtGroupListGroupName, ddboostOptionsStatus=ddboostOptionsStatus, iOModuleMacFault=iOModuleMacFault, newEncryptionKey=newEncryptionKey, diskOverheatWarningAlarm=diskOverheatWarningAlarm, systemLicenseTable=systemLicenseTable, fileSpaceWarningAlarm=fileSpaceWarningAlarm, ddintrepid=ddintrepid, NfsClientClientsTC=NfsClientClientsTC, currentAlertSeverity=currentAlertSeverity, tenantUnitMtreeListTable=tenantUnitMtreeListTable, nfsGroup=nfsGroup, searchDomainsTable=searchDomainsTable, mtreeCompressionEntry=mtreeCompressionEntry, scsitargetInitiatorFcSymbolicPortName=scsitargetInitiatorFcSymbolicPortName, containerMarkedInvalid=containerMarkedInvalid, tenantUnitListType=tenantUnitListType, SystemTimeZoneNameTC=SystemTimeZoneNameTC, cifsConfigNetBIOSHostname=cifsConfigNetBIOSHostname, vtlProperties=vtlProperties, ddboostConnectionsIndex=ddboostConnectionsIndex, scsitargetPortSystemAddress=scsitargetPortSystemAddress, replPerformanceWaitingDest=replPerformanceWaitingDest, nfsActiveTable=nfsActiveTable, scsitargetProperties=scsitargetProperties, DDMibTableSizeMiBTC=DDMibTableSizeMiBTC, ReplicationThrottleTC=ReplicationThrottleTC, tenantUnitMgmtUserListUserRole=tenantUnitMgmtUserListUserRole, systemActiveUserTty=systemActiveUserTty, tenantInfo=tenantInfo, diskErrTrapIndex=diskErrTrapIndex, fanDescription=fanDescription, CifsShareNameTC=CifsShareNameTC, environmentals=environmentals, tenantUnitDdboostStuListTable=tenantUnitDdboostStuListTable, fileSystem=fileSystem, DDboostStatsIndexTC=DDboostStatsIndexTC, FileSystemArchiveUnitStatusTC=FileSystemArchiveUnitStatusTC, haPrimaryHeartbeatStatus=haPrimaryHeartbeatStatus, TempSensorStatusTC=TempSensorStatusTC, diskAccessError=diskAccessError, unsupportedConfigurationROL=unsupportedConfigurationROL, vtlStatsPort=vtlStatsPort, VtlTapeStateTC=VtlTapeStateTC, ddboostIfGroupIdx=ddboostIfGroupIdx, VtlTapeSizeTC=VtlTapeSizeTC, replContext=replContext, ddboostFileReplHistoryNetwork=ddboostFileReplHistoryNetwork, ddms=ddms, ddboostFileReplicationHistoryEntry=ddboostFileReplicationHistoryEntry, systemOverheatWarningAlarm=systemOverheatWarningAlarm, systemPortsTable=systemPortsTable, dd430=dd430, ddsystemGroupRev1=ddsystemGroupRev1, artConfig=artConfig, cifsOptionsIndex=cifsOptionsIndex)
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", systemStats=systemStats, systemUserIndex=systemUserIndex, alertHistoryIndex=alertHistoryIndex, vtlLibraryTotalDrives=vtlLibraryTotalDrives, vtlLibraryTotalCaps=vtlLibraryTotalCaps, cifs=cifs, ddboostFileReplStatsDirection=ddboostFileReplStatsDirection, targetDriverPortFWLoadFailed=targetDriverPortFWLoadFailed, haSoftwareVersionCheck=haSoftwareVersionCheck, scsitargetEndpointEnabled=scsitargetEndpointEnabled, alertHistoryStatus=alertHistoryStatus, systemLicenseFeature=systemLicenseFeature, artConfigTable=artConfigTable, dd560=dd560, scsitargetDeviceGrpEntry=scsitargetDeviceGrpEntry, vtlLibrary=vtlLibrary, vtlStatsSyncLosses=vtlStatsSyncLosses, artMigrationPolicyIndex=artMigrationPolicyIndex, cifsOptionsValue=cifsOptionsValue, mtreeRetentionLockEntry=mtreeRetentionLockEntry, vtlTapeModTime=vtlTapeModTime, systemOverheatShutdownAlarm=systemOverheatShutdownAlarm, chassisTempWarning=chassisTempWarning, vtlGroupTable=vtlGroupTable, filesysDDGCFailedAlarm=filesysDDGCFailedAlarm, interfaceConnectivityDown=interfaceConnectivityDown, replStatus=replStatus, diskSerialNumber=diskSerialNumber, dd460g=dd460g, dd510=dd510, nfsClientTable=nfsClientTable, FileSystemSpaceUnitTC=FileSystemSpaceUnitTC, cifsConfigWINSServer=cifsConfigWINSServer, VtlStatsConrolCommandsTC=VtlStatsConrolCommandsTC, artConfigEntry=artConfigEntry, VtlPortFirmwareTC=VtlPortFirmwareTC, TenantUnitMgmtUserListUserRoleTC=TenantUnitMgmtUserListUserRoleTC, VtlDriveModelTC=VtlDriveModelTC, cifsShare=cifsShare, enclosurePackEntry=enclosurePackEntry, alertHistorySeverity=alertHistorySeverity, replHistoryContext=replHistoryContext, NfsStatusTC=NfsStatusTC, vtlPortIndex=vtlPortIndex, fileSpaceSevereAlarm=fileSpaceSevereAlarm, diskReliabilityTable=diskReliabilityTable, spaceReclMissingUnit=spaceReclMissingUnit, nvramStats=nvramStats, scsitargetInitiatorIndex=scsitargetInitiatorIndex, vtlDrive=vtlDrive, replHistoryTime=replHistoryTime, quotaCapacity=quotaCapacity, nvramEnvAlert=nvramEnvAlert, nfsOpsPerSecond=nfsOpsPerSecond, recoverFromNVRAMFailed=recoverFromNVRAMFailed, replPerformanceBusyMeta=replPerformanceBusyMeta, systemPortsIndex=systemPortsIndex, systemOverheatAlertAlarm=systemOverheatAlertAlarm, tenantUnitMgmtUserListUserName=tenantUnitMgmtUserListUserName, fileSystemArchiveUnitStatus=fileSystemArchiveUnitStatus, ddboostFileReplHistoryPostComp=ddboostFileReplHistoryPostComp, vtlGroupName=vtlGroupName, replHistoryPreCompRemaining=replHistoryPreCompRemaining, filesysRelaunchAlarm=filesysRelaunchAlarm, dataDomainMibComplianceRev4=dataDomainMibComplianceRev4, dnsIndex=dnsIndex, cifsShareBrowsing=cifsShareBrowsing, nfsClientEntry=nfsClientEntry, scsitargetInitiator=scsitargetInitiator, vtlPortTable=vtlPortTable, spaceOver90Percent=spaceOver90Percent, systemLicense=systemLicense, fanWarning=fanWarning, ddboostFileRepliPerfOutPreCompKBPerSec=ddboostFileRepliPerfOutPreCompKBPerSec, nvramCondAlert=nvramCondAlert, scsitargetPortEndpPort=scsitargetPortEndpPort, vtlTapePool=vtlTapePool, nvramStatsIndex=nvramStatsIndex, taskHistoryUser=taskHistoryUser, snmpTrapHosts=snmpTrapHosts, nfsClientOptions=nfsClientOptions, snapshotHWMAlarm=snapshotHWMAlarm, tempSensorDescription=tempSensorDescription, spaceReclUnitError=spaceReclUnitError, replHistoryPostFiltered=replHistoryPostFiltered, tenantUnitAdminIpInfo=tenantUnitAdminIpInfo, replSyncAlarm=replSyncAlarm, targetDriverPortCore=targetDriverPortCore, DDMibTableString64TC=DDMibTableString64TC, nisAdminGroups=nisAdminGroups, nvramErrorAlert=nvramErrorAlert, cifsShareComment=cifsShareComment, PowerModuleIndexTC=PowerModuleIndexTC, historicalDatabaseRecoverError=historicalDatabaseRecoverError, scsitargetEndpointPrimarySystemAddress=scsitargetEndpointPrimarySystemAddress, vtlPortStatus=vtlPortStatus, scsitargetInitiatorEndpTable=scsitargetInitiatorEndpTable, taskHistoryTable=taskHistoryTable, restorer=restorer, DdboostAccessClientsAuthModeTC=DdboostAccessClientsAuthModeTC, systemActiveUserLoginFrom=systemActiveUserLoginFrom, mtreeRetentionLockMinRetentionPeriod=mtreeRetentionLockMinRetentionPeriod, scsitargetPortEndpStatus=scsitargetPortEndpStatus, snmpTrapHostsTable=snmpTrapHostsTable, vtlGroupDeviceGroupName=vtlGroupDeviceGroupName, ddboostProperties=ddboostProperties, Minutes=Minutes, highAvailabilityNodeRole=highAvailabilityNodeRole, ddboostStorageUnitStatus=ddboostStorageUnitStatus, cifsConfigGroupName=cifsConfigGroupName, cpismissing=cpismissing, alertsGroup=alertsGroup, enclosureMixDriveType=enclosureMixDriveType, mtreeQuotaHardLimit=mtreeQuotaHardLimit, dd580=dd580, fileSystemArchiveUnitName=fileSystemArchiveUnitName, dataDomainMibProducts=dataDomainMibProducts, nfsPort=nfsPort, ddboostAccessClientsIndex=ddboostAccessClientsIndex, nfs=nfs, spaceReclSuspended=spaceReclSuspended, CifsOptionsValueTC=CifsOptionsValueTC, dd160=dd160, FileSystemCompressionFactorTC=FileSystemCompressionFactorTC, fileSystemResourceName=fileSystemResourceName, systemProperties=systemProperties, dataDomainMib=dataDomainMib, coredumpWarning=coredumpWarning, diskPathAlarm=diskPathAlarm, ReplicationConfigContextIdTC=ReplicationConfigContextIdTC, vtlLibraryStatus=vtlLibraryStatus, vtlDriveRevision=vtlDriveRevision, nvramBattAlert=nvramBattAlert, nISCommFailure=nISCommFailure, powerModules=powerModules, ddboostStatsImageCreatesErrors=ddboostStatsImageCreatesErrors, ddboostStorageUnitName=ddboostStorageUnitName, invalidHardwareWarning=invalidHardwareWarning, VtlStatsInvalidCRCsTC=VtlStatsInvalidCRCsTC, fileSystemArchiveUnitStartTime=fileSystemArchiveUnitStartTime, FileSystemCompressionPeriodTC=FileSystemCompressionPeriodTC, dataDomainMibComplianceRev2=dataDomainMibComplianceRev2, ddboostUser=ddboostUser, interfaceMisconfiguration=interfaceMisconfiguration, diskProbationalCount=diskProbationalCount, missingDiskGroup=missingDiskGroup, taskActiveState=taskActiveState, ReplicationTrafficTC=ReplicationTrafficTC, haHardwareCompatibilityCheck=haHardwareCompatibilityCheck, historicalDatabaseBackupError=historicalDatabaseBackupError, nisUserGroups=nisUserGroups, nTPDFailed=nTPDFailed, ddboostStatsTotalBytesReadErrors=ddboostStatsTotalBytesReadErrors, dd200Proto=dd200Proto, FanIndexTC=FanIndexTC, CifsShareMaxConnectionTC=CifsShareMaxConnectionTC, VtlStatsWriteCommandsTC=VtlStatsWriteCommandsTC, SystemStatsIndexTC=SystemStatsIndexTC, TempSensorIndexTC=TempSensorIndexTC, FileSystemCleanStatusTC=FileSystemCleanStatusTC, VtlPortSpeedTC=VtlPortSpeedTC, scsitargetDeviceGrpPrimaryEndpoints=scsitargetDeviceGrpPrimaryEndpoints, scsitargetEndpointStatus=scsitargetEndpointStatus, replicationPerformance=replicationPerformance, fileSystemSpace=fileSystemSpace, systemCapacityLicenseModel=systemCapacityLicenseModel, mtreeQuotaSoftLimit=mtreeQuotaSoftLimit, scsitargetPortEnabled=scsitargetPortEnabled, unsupportedNIC=unsupportedNIC, vtlPortName=vtlPortName, cifsShareUser=cifsShareUser, cpuMaxPercentageBusy=cpuMaxPercentageBusy, VtlStatsSyncLossesTC=VtlStatsSyncLossesTC, diskPathRedundancy=diskPathRedundancy, dataDomainSystem=dataDomainSystem, ddboostAccessClientsTable=ddboostAccessClientsTable, systemPortsHardwareAddress=systemPortsHardwareAddress, ddve=ddve, vtlPortSpeed=vtlPortSpeed, uncorrectableECCerror=uncorrectableECCerror, VtlLibraryVendorTC=VtlLibraryVendorTC, CifsSharePathTC=CifsSharePathTC, scsitargetDevice=scsitargetDevice, mtreeCompressionLocalCompFactor=mtreeCompressionLocalCompFactor, DDStatusTC=DDStatusTC, NfsClientPathTC=NfsClientPathTC, VtlPortIDTC=VtlPortIDTC, multipleDiskReadErrors=multipleDiskReadErrors, replPostCompBytesSent=replPostCompBytesSent, alertInfoIndex=alertInfoIndex, artMigrationPolicyDefaultAge=artMigrationPolicyDefaultAge, ddboostFileReplicationHistoryTable=ddboostFileReplicationHistoryTable, iOModuleInserted=iOModuleInserted, vtlPortEnabled=vtlPortEnabled, dataDomainMibConformance=dataDomainMibConformance, VtlDriveNameTC=VtlDriveNameTC, ddboostStorageUnitMetaData=ddboostStorageUnitMetaData, diskSASHBAAlarm=diskSASHBAAlarm, powerUnitWarning=powerUnitWarning, diskPerformanceEntry=diskPerformanceEntry, unsupportedPowerSupply=unsupportedPowerSupply, replHistoryPreCompressed=replHistoryPreCompressed, vtlGroupInitiaterCount=vtlGroupInitiaterCount, diskTemperatureShutdown=diskTemperatureShutdown, DiskFirmwareVersionTC=DiskFirmwareVersionTC, mtreeListTable=mtreeListTable, replConfigSource=replConfigSource, VtlStatsOutTC=VtlStatsOutTC, vtlInitiatorEntry=vtlInitiatorEntry, vtlInitiatorGroup=vtlInitiatorGroup, iOModuleFault=iOModuleFault, legacyBMCHangCritical=legacyBMCHangCritical, vtlTapeSize=vtlTapeSize, vtlStatsTable=vtlStatsTable, scsitargetInitiatorEntry=scsitargetInitiatorEntry, targetDriverPortOffline=targetDriverPortOffline, taskActiveIndex=taskActiveIndex, phyalert=phyalert, mtreeRetentionLockIndex=mtreeRetentionLockIndex, mtreeListMtreeName=mtreeListMtreeName, CifsShareBrowsingTC=CifsShareBrowsingTC, unsupportedHardwareSpareSize=unsupportedHardwareSpareSize, vtlPoolIndex=vtlPoolIndex, ReplicationSyncedTimeTC=ReplicationSyncedTimeTC, VtlStatsLIPCountTC=VtlStatsLIPCountTC, quotaProperties=quotaProperties, memoryAlert=memoryAlert, CifsShareWriteableTC=CifsShareWriteableTC, vtlGroupDeviceEntry=vtlGroupDeviceEntry, artMigrationScheduleSchedule=artMigrationScheduleSchedule, correctECCWarning=correctECCWarning, scsitargetEndpointName=scsitargetEndpointName, scsitargetPortIndex=scsitargetPortIndex, scsitargetInitiatorSystemAddress=scsitargetInitiatorSystemAddress, fileSystemCleanTable=fileSystemCleanTable, nfsActive=nfsActive, ddboostStorageUnitReportPhysicalSize=ddboostStorageUnitReportPhysicalSize, fileSystemOptionsTable=fileSystemOptionsTable, nfsSendPercentage=nfsSendPercentage, replConnTime=replConnTime, highAvailability=highAvailability, scsitargetObjectGroup=scsitargetObjectGroup, fileSystemCleanSchedule=fileSystemCleanSchedule, ddboostStatsPrecompBytesReceived=ddboostStatsPrecompBytesReceived, VtlStatsIndexTC=VtlStatsIndexTC, vtlStatsInvalidCRCs=vtlStatsInvalidCRCs, vtlPort=vtlPort, fileSystemCompressionTable=fileSystemCompressionTable, DiskStateTC=DiskStateTC, smiMrc=smiMrc, DDMibTableIndexTC=DDMibTableIndexTC, bMCFailureSysBBU=bMCFailureSysBBU, diskTimeoutCount=diskTimeoutCount, MtreeRetentionLockStatusTC=MtreeRetentionLockStatusTC)
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", ddboostFileReplStatsLocalComp=ddboostFileReplStatsLocalComp, hAdegraded=hAdegraded, scsitargetGroupTable=scsitargetGroupTable, diskPerformance=diskPerformance, diskWriteFailCount=diskWriteFailCount, ddboostIfGroupEntry=ddboostIfGroupEntry, forcedControllerShutdown=forcedControllerShutdown, scsitargetPortFcBaseWwnn=scsitargetPortFcBaseWwnn, taskActiveID=taskActiveID, replicationHistoryEntry=replicationHistoryEntry, sASPortDisabled=sASPortDisabled, systemActiveUserIdleTime=systemActiveUserIdleTime, CifsOptionsNameTC=CifsOptionsNameTC, vtlInitiatorPort=vtlInitiatorPort, powerSupplyAbsent=powerSupplyAbsent, ddboostConnections=ddboostConnections, replIncompatibleWorm=replIncompatibleWorm, replConfigConnPort=replConfigConnPort, physicalCapacityMeasurementTasksLostMTree=physicalCapacityMeasurementTasksLostMTree, chassisSensorCritical=chassisSensorCritical, scsitargetEndpointIndex=scsitargetEndpointIndex, diskSectorsRead=diskSectorsRead, dataDomainMibComplianceRev5=dataDomainMibComplianceRev5, scsitargetDeviceService=scsitargetDeviceService, tenantInfoTenantName=tenantInfoTenantName, diskErrState=diskErrState, ddboostFileReplStatsFiltered=ddboostFileReplStatsFiltered, indexRebuildComplete=indexRebuildComplete, NfsStatsMaxCacheSizeTC=NfsStatsMaxCacheSizeTC, nfsStatsTable=nfsStatsTable, statistics=statistics, ddboostFileReplHistoryErrors=ddboostFileReplHistoryErrors, taskActiveUser=taskActiveUser, fileSystemArchiveUnitTable=fileSystemArchiveUnitTable, ddboostOptionsName=ddboostOptionsName, diskPropEnclosureID=diskPropEnclosureID, scsitargetDeviceAddress=scsitargetDeviceAddress, replicationConfigEntry=replicationConfigEntry, vtlInitiatorTable=vtlInitiatorTable, vtlLibrarySerial=vtlLibrarySerial, highAvailabilityComponentIdx=highAvailabilityComponentIdx, ddboostFileReplicationStatsTable=ddboostFileReplicationStatsTable, DDMibTableEnabledTC=DDMibTableEnabledTC, dd860g=dd860g, missingEnclosurePath=missingEnclosurePath, unCorrectECCWarning=unCorrectECCWarning, scsitargetGroupName=scsitargetGroupName, diskPack=diskPack, fileSystemResourceTrapIndex=fileSystemResourceTrapIndex, tenantUnitListNumberOfMgmtUsers=tenantUnitListNumberOfMgmtUsers, CifsConfigWINSServerTC=CifsConfigWINSServerTC, smt=smt, vtlTapeState=vtlTapeState, fileSystemOptionsName=fileSystemOptionsName, duplicateAddressDetection=duplicateAddressDetection, unsupportedSASDevice=unsupportedSASDevice, snapshotLimitReached=snapshotLimitReached, ddboostGroup=ddboostGroup, VtlStatsPortTC=VtlStatsPortTC, ddboostFileReplicationStats=ddboostFileReplicationStats, alerts=alerts, vtlInitiatorIndex=vtlInitiatorIndex, FileSystemCompressionSizeTC=FileSystemCompressionSizeTC, DdboostAccessClientsEncryStrengthTC=DdboostAccessClientsEncryStrengthTC, DateTC=DateTC, ddboostFileReplStatsIndex=ddboostFileReplStatsIndex, chassisFailure=chassisFailure, replOutKBytesPerSecond=replOutKBytesPerSecond, FileSystemResourceIndexTC=FileSystemResourceIndexTC, replHistoryPostLocalComp=replHistoryPostLocalComp, Percentage=Percentage, vtlInitiatorWWPN=vtlInitiatorWWPN, networkGroup=networkGroup, systemUserEntry=systemUserEntry, ddboostStorageUnitBytes=ddboostStorageUnitBytes, fileSystemOptionsIndex=fileSystemOptionsIndex, nvramReadKBytesPerSecond=nvramReadKBytesPerSecond, systemUserUID=systemUserUID, Temperature=Temperature, replPerformanceWaitingNetwork=replPerformanceWaitingNetwork, mtreeList=mtreeList, enclosureList=enclosureList, mtree=mtree, systemSerialNumber=systemSerialNumber, highAvailabilityNodeEntry=highAvailabilityNodeEntry, dns=dns, scsitargetDeviceGrpIndex=scsitargetDeviceGrpIndex, fileSystemReductionPercent1=fileSystemReductionPercent1, targetDriverPortTooManyOsc=targetDriverPortTooManyOsc, ddboostInterface=ddboostInterface, art=art, ddboostAccessClientsAuthMode=ddboostAccessClientsAuthMode, diskNoSpareAlarm=diskNoSpareAlarm, mtreeCompressionPostCompGib=mtreeCompressionPostCompGib, VtlLibraryRevisionTC=VtlLibraryRevisionTC, nfsActiveIndex=nfsActiveIndex, scsitargetInitiatorName=scsitargetInitiatorName, scsitargetDeviceActiveState=scsitargetDeviceActiveState, mtreeRetentionLockMaxRetentionPeriod=mtreeRetentionLockMaxRetentionPeriod, ddboostPreCompKBytesPerSecond=ddboostPreCompKBytesPerSecond, artMigrationScheduleStatus=artMigrationScheduleStatus, tenantUnitMgmtGroupListGroupType=tenantUnitMgmtGroupListGroupType, DDMibTrafficBytesTC=DDMibTrafficBytesTC, fileSystemOptionsEntry=fileSystemOptionsEntry, ddboostifGroupMember=ddboostifGroupMember, nvramBatteryTable=nvramBatteryTable, ReplicationContextTC=ReplicationContextTC, vtlDriveVendor=vtlDriveVendor, ddboostIfGroupConfigIndex=ddboostIfGroupConfigIndex, invalidNICSlot=invalidNICSlot, diskPropertiesTable=diskPropertiesTable, NfsStatsCacheEntryTC=NfsStatsCacheEntryTC, ddboostFileReplicationPerformance=ddboostFileReplicationPerformance, fileSystemArchiveUnitDiskGroups=fileSystemArchiveUnitDiskGroups, managedSystemHDSyncTime=managedSystemHDSyncTime, ReplicationConfigLowBWOptimTC=ReplicationConfigLowBWOptimTC, nfsClientIndex=nfsClientIndex, legacyChassisTempCritical=legacyChassisTempCritical, pCILinkDegraded=pCILinkDegraded, systemModelNumber=systemModelNumber, FileSystemOptionsValueTC=FileSystemOptionsValueTC, diskProperties=diskProperties, hAofflineErrors=hAofflineErrors, vtlGroupDeviceSecondaryPorts=vtlGroupDeviceSecondaryPorts, VtlPortIndexTC=VtlPortIndexTC, AlertIndexTC=AlertIndexTC, fileSystemArchiveUnitState=fileSystemArchiveUnitState, clusterInterfaceAlarm=clusterInterfaceAlarm, NvramMemorySizeTC=NvramMemorySizeTC, fanFault=fanFault, highAvailabilityNodeId=highAvailabilityNodeId, replHistoryBytesNetwork=replHistoryBytesNetwork, vtlDriveTable=vtlDriveTable, systemStartupAlarm=systemStartupAlarm, interfaceConnectivityIntermittent=interfaceConnectivityIntermittent, unsupportedSystemType=unsupportedSystemType, cifsShareTable=cifsShareTable, managedSystemTable=managedSystemTable, mtreeCascadeNeedResync=mtreeCascadeNeedResync, nisEnabled=nisEnabled, scsitargetInitiatorService=scsitargetInitiatorService, tenantUnitListNumberOfMgmtGroups=tenantUnitListNumberOfMgmtGroups, sNTZMultipleIterations=sNTZMultipleIterations, nvramBatteries=nvramBatteries, nisBackupOperatorGroups=nisBackupOperatorGroups, dd400g=dd400g, dataDomainMibCompliance=dataDomainMibCompliance, eventIPMIUnmanageAlarm=eventIPMIUnmanageAlarm, processorWarning=processorWarning, mtreeCompressionPostTotalCompFactor=mtreeCompressionPostTotalCompFactor, storageMigrationCannotResume=storageMigrationCannotResume, diskMiscFailCount=diskMiscFailCount, raidGroupMissingAlarm=raidGroupMissingAlarm, nfsPortService=nfsPortService, systemCapacityLicenseIndex=systemCapacityLicenseIndex, managedSystemDDOSVersion=managedSystemDDOSVersion, CifsConfigModeTC=CifsConfigModeTC, scsitargetInitiatorEndpEndpoint=scsitargetInitiatorEndpEndpoint, nis=nis, replFileSysStatus=replFileSysStatus, ReplicationConfigConnPortTC=ReplicationConfigConnPortTC, ddboostIfGroupTable=ddboostIfGroupTable, replState=replState, tcpZeroWindowAlert=tcpZeroWindowAlert, alertHistoryTimestamp=alertHistoryTimestamp, cMTaskEnded=cMTaskEnded, scsitargetDeviceTable=scsitargetDeviceTable, mtreeCompressionMtreePath=mtreeCompressionMtreePath, dd670=dd670, metadataWarningThreshold=metadataWarningThreshold, ddboostStorageUnitTable=ddboostStorageUnitTable, ddsystemGroup=ddsystemGroup, temperatureSensorEntry=temperatureSensorEntry, ddboostStatsImageCreatesCount=ddboostStatsImageCreatesCount, temperatureSensors=temperatureSensors, ddboostFileReplStatsNetworkSent=ddboostFileReplStatsNetworkSent, CifsShareUserTC=CifsShareUserTC, vtlStatsLIPCount=vtlStatsLIPCount, vtlStatsInvalidTxWords=vtlStatsInvalidTxWords, VtlStatsSignalLossesTC=VtlStatsSignalLossesTC, fans=fans, cifsOptionsEntry=cifsOptionsEntry, vtlDriveEntry=vtlDriveEntry, fileMigrationError=fileMigrationError, diskErrIndex=diskErrIndex, tenantUnitListEntry=tenantUnitListEntry, vtlPoolTable=vtlPoolTable, scsitargetEndpointSecondarySystemAddress=scsitargetEndpointSecondarySystemAddress, mtreeGroup=mtreeGroup, tenantUnitMgmtUserList=tenantUnitMgmtUserList, fileSystemSpaceEntry=fileSystemSpaceEntry, dd4200=dd4200, cifsShareMaxConnection=cifsShareMaxConnection, filesystemProblem=filesystemProblem, nvramWarning=nvramWarning, cifsShareEntry=cifsShareEntry, VtlDriveRevisionTC=VtlDriveRevisionTC, scsitargetDeviceIndex=scsitargetDeviceIndex, dnsTable=dnsTable, smtStatus=smtStatus, artGroup=artGroup, vtlGroupDeviceLun=vtlGroupDeviceLun, VtlAdminStateTC=VtlAdminStateTC, replProgressThreshholdReached=replProgressThreshholdReached, VtlPortWWPNTC=VtlPortWWPNTC, vtlStatsIndex=vtlStatsIndex, highAvailabilityNodeName=highAvailabilityNodeName, scsitargetPortLinkSpeed=scsitargetPortLinkSpeed, sASTopologyCheck=sASTopologyCheck, nvramStatsTable=nvramStatsTable, tenantUnitListNumberOfMtrees=tenantUnitListNumberOfMtrees, VtlDriveStatusTC=VtlDriveStatusTC, systemHardwareVendor=systemHardwareVendor, alertHistoryEntry=alertHistoryEntry, ddboostAccessClientsName=ddboostAccessClientsName, tenantUnitAdminIpInfoEntry=tenantUnitAdminIpInfoEntry, mtreeRetentionLockMtreeName=mtreeRetentionLockMtreeName, ddboostStatsBackupConn=ddboostStatsBackupConn, ddboostStatsRestoreConn=ddboostStatsRestoreConn, searchDomainsEntry=searchDomainsEntry, scsitargetDeviceEntry=scsitargetDeviceEntry, scsitargetGroupActiveState=scsitargetGroupActiveState, DDMibTableString1024TC=DDMibTableString1024TC, nfsPortEntry=nfsPortEntry, managedObjectsGroup=managedObjectsGroup, fanTrapIndex=fanTrapIndex, legacyChassisTempWarning=legacyChassisTempWarning, taskHistoryIndex=taskHistoryIndex, fileSystemCompressionPeriod=fileSystemCompressionPeriod, interfaceConnectivityUpAndRunning=interfaceConnectivityUpAndRunning, AlertTimestampTC=AlertTimestampTC, taskActiveDuration=taskActiveDuration, tenantInfoEntry=tenantInfoEntry, memoryRiserFault=memoryRiserFault, dDFSRequiresReboot=dDFSRequiresReboot, systemCapacityLicenseTable=systemCapacityLicenseTable, ddboostOptionsEntry=ddboostOptionsEntry, missingTierStorage=missingTierStorage, nfsPortIndex=nfsPortIndex, replPerformanceBusyReading=replPerformanceBusyReading, systemActiveUserLoginTime=systemActiveUserLoginTime, diskPropState=diskPropState, scsitargetPortFcCurrentWwpn=scsitargetPortFcCurrentWwpn, sCSITGTInvalidRegistry=sCSITGTInvalidRegistry, diskGroupReconstruction=diskGroupReconstruction, network=network, nvramPropertiesIndex=nvramPropertiesIndex, vtlGroupDevicePrimaryPorts=vtlGroupDevicePrimaryPorts, highAvailabilityNodeIdx=highAvailabilityNodeIdx, cifsShareWriteable=cifsShareWriteable, fileSystemStatusMessage=fileSystemStatusMessage, fileSystemArchiveUnitIndex=fileSystemArchiveUnitIndex, nisDomain=nisDomain, scsitargetPortModel=scsitargetPortModel)
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", nvramMemorySize=nvramMemorySize, diskSectorsWritten=diskSectorsWritten, systemActiveUserTable=systemActiveUserTable, ddboostFileReplicationHistory=ddboostFileReplicationHistory, dDFSNoHeartbeat=dDFSNoHeartbeat, tenantInfoIdx=tenantInfoIdx, replicationPerformanceEntry=replicationPerformanceEntry, vtlTapeIndex=vtlTapeIndex, vtlPortWWNN=vtlPortWWNN, NfsStatsFileHandleLookupTC=NfsStatsFileHandleLookupTC, ddboostOptions=ddboostOptions, NvramWindowSizeTC=NvramWindowSizeTC, NfsStatsIndexTC=NfsStatsIndexTC, ReplicationConfigSourceTC=ReplicationConfigSourceTC, ddboostIfGroupStatus=ddboostIfGroupStatus, enclosureListModel=enclosureListModel, DDMibStatusTC=DDMibStatusTC, cifsGroup=cifsGroup, scsitargetAdminState=scsitargetAdminState, tenantUnitList=tenantUnitList, diskWriteKBytesPerSecond=diskWriteKBytesPerSecond, cifsStatus=cifsStatus, tenantUnitMgmtGroupList=tenantUnitMgmtGroupList, CifsStatsSummaryIndexTC=CifsStatsSummaryIndexTC, upgradeInProgress=upgradeInProgress, ddboostStats=ddboostStats, bMCHangShutdown=bMCHangShutdown, tenantUnitListParentTenantName=tenantUnitListParentTenantName, ddboostStatsBytesAfterFiltering=ddboostStatsBytesAfterFiltering, ReplicationConnectTimeTC=ReplicationConnectTimeTC, fileSystemCompressionIndex=fileSystemCompressionIndex, artMigrationSchedule=artMigrationSchedule, cifsShareIndex=cifsShareIndex, fanStatus=fanStatus, smtGroup=smtGroup, replicationInfo=replicationInfo, alertHistoryDescription=alertHistoryDescription, systemCapacityLicenseKey=systemCapacityLicenseKey, taskHistoryDuration=taskHistoryDuration, highAvailabilityNodeHealth=highAvailabilityNodeHealth, quotaCapacityMtreeName=quotaCapacityMtreeName, systemLicenseKey=systemLicenseKey, replThrottle=replThrottle, RaidDiskStateTC=RaidDiskStateTC, tenantUnitListIdx=tenantUnitListIdx, ddboostAccessClients=ddboostAccessClients, dd990=dd990, nfsActiveClients=nfsActiveClients, hATimeOutOfSync=hATimeOutOfSync, quotaCapacitySoftLimitMiB=quotaCapacitySoftLimitMiB, temperatures=temperatures, nvramPropertiesTable=nvramPropertiesTable, nvramBatteryLowChargeAlert=nvramBatteryLowChargeAlert, nfsClient=nfsClient, tempSensorTrapIndex=tempSensorTrapIndex, vtlProcessState=vtlProcessState, bMCPartialHang=bMCPartialHang, replicationConfigTable=replicationConfigTable, clusterNodeAlarm=clusterNodeAlarm, tenantUnitListSecurityMode=tenantUnitListSecurityMode, legacyFanWarning=legacyFanWarning, raidReconCriticalAlarm=raidReconCriticalAlarm, EnclosureID=EnclosureID, dd690=dd690, fileSystemReductionPercent=fileSystemReductionPercent, ddkoalam1=ddkoalam1, replicationPerformanceTable=replicationPerformanceTable, DiskSectorsPerSecondTC=DiskSectorsPerSecondTC, ddboostStatus=ddboostStatus, nfsStatsCacheEntry=nfsStatsCacheEntry, vtlPool=vtlPool, highAvailabilityComponentEntry=highAvailabilityComponentEntry, scsitargetPortFcCurrentWwnn=scsitargetPortFcCurrentWwnn, systemTimeZoneName=systemTimeZoneName, scsitargetDeviceGrpSecondaryEndpoints=scsitargetDeviceGrpSecondaryEndpoints, systemStatsTable=systemStatsTable, currentAlertEntry=currentAlertEntry, ddboostIfGroupConfig=ddboostIfGroupConfig, ddboostPostCompKBytesPerSecond=ddboostPostCompKBytesPerSecond, nvramBattEndOfLife=nvramBattEndOfLife, vtlPoolSize=vtlPoolSize, scsitargetInitiatorEndpIndex=scsitargetInitiatorEndpIndex, diskPropIndex=diskPropIndex, nvramPCIErrorCount=nvramPCIErrorCount, diskPropertiesEntry=diskPropertiesEntry, systemPortsEntry=systemPortsEntry, nfsStatsMaxCacheSize=nfsStatsMaxCacheSize, diskReadKBytesPerSecond=diskReadKBytesPerSecond, scsitargetPortTransport=scsitargetPortTransport, dd620=dd620, insecureEncryptedReplication=insecureEncryptedReplication, ddboostRestoreConnections=ddboostRestoreConnections, systemUserRole=systemUserRole, ddboostStatsEntry=ddboostStatsEntry, mtreeCompressionIndex=mtreeCompressionIndex, correctableErrorWarning=correctableErrorWarning, hDTFileTransferFailed=hDTFileTransferFailed, dNSUnresponsive=dNSUnresponsive, fileSystemCleanEntry=fileSystemCleanEntry, scsitargetInitiatorFcWwpn=scsitargetInitiatorFcWwpn, ddboostStatsImageDeletesErrors=ddboostStatsImageDeletesErrors, vtlDriveIndex=vtlDriveIndex, highAvailabilityComponentState=highAvailabilityComponentState, VtlPortStatusTC=VtlPortStatusTC, cifsConfigMaxConnection=cifsConfigMaxConnection, ddboostStatsTotalBytesReadCount=ddboostStatsTotalBytesReadCount, missingDiskPath=missingDiskPath, cifsGroupRev1=cifsGroupRev1, systemHardwareIndex=systemHardwareIndex, powerModuleIndex=powerModuleIndex, scsitargetPortFcp2Retry=scsitargetPortFcp2Retry, fileSystemUpTime=fileSystemUpTime, snmpTrapHostsEntry=snmpTrapHostsEntry, dd880g=dd880g, vtlPoolUsed=vtlPoolUsed, scsitargetPortPortId=scsitargetPortPortId, sysNotes=sysNotes, VtlLibraryModelTC=VtlLibraryModelTC, vtlDriveSerial=vtlDriveSerial, currentAlerts=currentAlerts, replConfigContextId=replConfigContextId, cifsShareClients=cifsShareClients, scsitargetEndpointTransport=scsitargetEndpointTransport, fileSystemArchiveUnitEntry=fileSystemArchiveUnitEntry, diskOffTrackErrCount=diskOffTrackErrCount, ddboostIfGroupInterface=ddboostIfGroupInterface, NvramBatteryStatusTC=NvramBatteryStatusTC, taskHistoryEntry=taskHistoryEntry, tempSensorCurrentValue=tempSensorCurrentValue, DiskCapacityTC=DiskCapacityTC, searchDomainsIndex=searchDomainsIndex, HaSystemStatusTC=HaSystemStatusTC, enclosurePackTable=enclosurePackTable, replicationHistoryTable=replicationHistoryTable, vtlDriveName=vtlDriveName, fileSpaceMaintenanceAlarm=fileSpaceMaintenanceAlarm, replication=replication, noHistoricalDatabaseError=noHistoricalDatabaseError, currentAlertDescription=currentAlertDescription, snmpTrapHostsIndex=snmpTrapHostsIndex, ddboostFileReplHistoryDate=ddboostFileReplHistoryDate, ddboostUserDefaultTenantUnit=ddboostUserDefaultTenantUnit, taskActiveParent=taskActiveParent, PercentageStr=PercentageStr, tenantUnitListNumberOfDdboostStus=tenantUnitListNumberOfDdboostStus, DiskSerialNumberTC=DiskSerialNumberTC, mtreeListEntry=mtreeListEntry, haInterconnectStatus=haInterconnectStatus, systemHardwareEntry=systemHardwareEntry, scsitargetEndpointFcWwpn=scsitargetEndpointFcWwpn, replConfigDest=replConfigDest, vTLEnabled=vTLEnabled, nisStatus=nisStatus, DDboostStatusTC=DDboostStatusTC, tenantInfoTenantUnitEntry=tenantInfoTenantUnitEntry, enclosureListOemName=enclosureListOemName, vtlTapeEntry=vtlTapeEntry, VtlDriveTapeVolumeTC=VtlDriveTapeVolumeTC, replHistoryDate=replHistoryDate, powerEnclosureID=powerEnclosureID, CifsShareIndexTC=CifsShareIndexTC, ext3NvlogDisabled=ext3NvlogDisabled, apollo=apollo, fileSystemResourceIndex=fileSystemResourceIndex, diskGroupReconstructionShutdown=diskGroupReconstructionShutdown, ddboostStorageUnit=ddboostStorageUnit, mtreeListStatus=mtreeListStatus, CifsStatusTC=CifsStatusTC, fileSystemArchiveUnitEndTime=fileSystemArchiveUnitEndTime, tapeReposition=tapeReposition, replDestination=replDestination, CifsShareCommentTC=CifsShareCommentTC, replHistoryPostLowBwOptim=replHistoryPostLowBwOptim, scsitargetPortEndpIndex=scsitargetPortEndpIndex, ddboostIfGroupName=ddboostIfGroupName, diskErrEnclosureID=diskErrEnclosureID, nvramBatteryIndex=nvramBatteryIndex, searchDomains=searchDomains, nvramWindowSize=nvramWindowSize, diskModel=diskModel, cPUFailureWarning=cPUFailureWarning, systemLicenseEntry=systemLicenseEntry, spaceOver80Percent=spaceOver80Percent, nvramMemoryErrorCount=nvramMemoryErrorCount, currentAlertIndex=currentAlertIndex, powerSupplyFailure=powerSupplyFailure, fileSystemCompressionEndTime=fileSystemCompressionEndTime, dd860=dd860, tenantUnitListName=tenantUnitListName, diskBusy=diskBusy, replConfigIndex=replConfigIndex, fanIndex=fanIndex, NvramBatteryIndexTC=NvramBatteryIndexTC, fileSystemOptionsValue=fileSystemOptionsValue, dd640=dd640, diskPathSpeedDegraded=diskPathSpeedDegraded, VtlTapeLocationTC=VtlTapeLocationTC, managedSystemSerial=managedSystemSerial, DDMibTableString128TC=DDMibTableString128TC, targetDriverPortOnline=targetDriverPortOnline, systemHardwareSlot=systemHardwareSlot, spaceReclUnitReclaimed=spaceReclUnitReclaimed, scsitargetInitiatorEndpInitiator=scsitargetInitiatorEndpInitiator, dnsEntry=dnsEntry, environmentalsGroup=environmentalsGroup, ddboostIfGroupConfigEntry=ddboostIfGroupConfigEntry, temperatureSensorTable=temperatureSensorTable, artMigrationPolicyMtreeName=artMigrationPolicyMtreeName, enclosureMixType=enclosureMixType, encryptionKeyTableFull=encryptionKeyTableFull, fileSystemGlobalCompressionFactor=fileSystemGlobalCompressionFactor, VtlLibraryTotalDrivesTC=VtlLibraryTotalDrivesTC, dd560g=dd560g, ddboostStatsTable=ddboostStatsTable, managedSystemStatus=managedSystemStatus, TenantUnitMgmtGroupTypeTC=TenantUnitMgmtGroupTypeTC, diskSoftEccCount=diskSoftEccCount, fileSystemPostCompressionSize=fileSystemPostCompressionSize, externalUnmanagedDiskStorageGroup=externalUnmanagedDiskStorageGroup, quota=quota, dd2500=dd2500, snmpTrapHostsVersion=snmpTrapHostsVersion, enclosureListSerialNum=enclosureListSerialNum, highAvailabilityNodeTable=highAvailabilityNodeTable, diskGroupReconstructionNoProgress=diskGroupReconstructionNoProgress, VtlTapeUsedTC=VtlTapeUsedTC, dd690g=dd690g, vtlLibraryEntry=vtlLibraryEntry, vtlDriveModel=vtlDriveModel, dataDomainMibTraps=dataDomainMibTraps, ReplicationStatusTC=ReplicationStatusTC, systemCapacityLicense=systemCapacityLicense, ddboostConnectionsEntry=ddboostConnectionsEntry, systemHardware=systemHardware, invalidEnclosureTopology=invalidEnclosureTopology, insufficientSpaceForEncryption=insufficientSpaceForEncryption, powerModuleEntry=powerModuleEntry, vtlGroupDeviceInUsePorts=vtlGroupDeviceInUsePorts, vtlInitiator=vtlInitiator, replConfigLowBWOptim=replConfigLowBWOptim, nvramBatteryEntry=nvramBatteryEntry, tempSensorStatus=tempSensorStatus, fileSystemSpaceSize=fileSystemSpaceSize, filesystemCorruption=filesystemCorruption, artMigrationScheduleEntry=artMigrationScheduleEntry, systemHardwareTable=systemHardwareTable, cifsOptionsTable=cifsOptionsTable, systemPortsConnectionType=systemPortsConnectionType, correctableECCLimitReached=correctableECCLimitReached, ddboostFileReplStatsLowBWOpt=ddboostFileReplStatsLowBWOpt, systemPortsPort=systemPortsPort, nfsPortTable=nfsPortTable, basicNotificationsGroup=basicNotificationsGroup, ddboostOptionsIndex=ddboostOptionsIndex)
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", ddboostOptionsTable=ddboostOptionsTable, VtlProcessStateTC=VtlProcessStateTC, scsitargetPortTable=scsitargetPortTable, powerWarning=powerWarning, enclosureListTable=enclosureListTable, targetDriverPortMultipleCore=targetDriverPortMultipleCore, FileSystemCleanThrottleTC=FileSystemCleanThrottleTC, currentAlertTimestamp=currentAlertTimestamp, taskActiveName=taskActiveName, VtlStatsReadCommandsTC=VtlStatsReadCommandsTC, vtlGroupIndex=vtlGroupIndex, systemHardwarePorts=systemHardwarePorts, vtlPoolPool=vtlPoolPool, statisticsGroup=statisticsGroup, systemReset=systemReset, currentAlertID=currentAlertID, scsitargetInitiatorEndpStatus=scsitargetInitiatorEndpStatus, dd120=dd120, cifsConfigDomainController=cifsConfigDomainController, diskUnknown=diskUnknown, ddboostFileReplHistoryLowBWOpt=ddboostFileReplHistoryLowBWOpt, taskActiveEntry=taskActiveEntry, vtlPoolEntry=vtlPoolEntry, replInKBytesPerSecond=replInKBytesPerSecond, sPFault=sPFault, artMigrationPolicyEntry=artMigrationPolicyEntry, scsitargetGroupIndex=scsitargetGroupIndex, quotaCapacityHardLimitMiB=quotaCapacityHardLimitMiB, systemUserTable=systemUserTable, nvram=nvram, nvramBatteryStatus=nvramBatteryStatus, nfsProcPercentage=nfsProcPercentage, dd610=dd610, cifsOptions=cifsOptions, filesysGeneralProblemAlarm=filesysGeneralProblemAlarm, currentAlertTable=currentAlertTable, diskTotalKBytes=diskTotalKBytes, mtreeRetentionLockTable=mtreeRetentionLockTable, enclosureListOemValue=enclosureListOemValue, cifsOptionsName=cifsOptionsName, vtlDriveTapeVolume=vtlDriveTapeVolume, vtlStats=vtlStats, SmtStatusTC=SmtStatusTC, vtlGroupEntry=vtlGroupEntry, power=power, nfsStatsFileHandleLookup=nfsStatsFileHandleLookup, fanModuleFailedAlarm=fanModuleFailedAlarm, scsitargetEndpointFcWwnn=scsitargetEndpointFcWwnn, systemUser=systemUser, vtlStatsEntry=vtlStatsEntry, quotaCapacityPreCompMiB=quotaCapacityPreCompMiB, replPreCompBytesSent=replPreCompBytesSent, DDMibMemorySizeTC=DDMibMemorySizeTC, sSDEndOfLife=sSDEndOfLife, vtlPortWWPN=vtlPortWWPN, targetDriverPortUnreadable=targetDriverPortUnreadable, VtlDriveSerialTC=VtlDriveSerialTC, TenantUnitSecurityModeTC=TenantUnitSecurityModeTC, vtlLibraryIndex=vtlLibraryIndex, vtlPortConnectionType=vtlPortConnectionType, filesystemNVRAMDataLoss=filesystemNVRAMDataLoss, tempSensorIndex=tempSensorIndex, diskBusyPercentage=diskBusyPercentage, dd410=dd410, mtreeCompression=mtreeCompression, nisServers=nisServers, FanLevelTC=FanLevelTC, mtreeListIndex=mtreeListIndex, tenantUnitAdminIpInfoAddr=tenantUnitAdminIpInfoAddr, corruptEncryptionKeys=corruptEncryptionKeys, DDMibTableString256TC=DDMibTableString256TC, tenantUnitMtreeListEntry=tenantUnitMtreeListEntry, CifsConfigDNSTC=CifsConfigDNSTC, quotaGroup=quotaGroup, vtlLibraryTable=vtlLibraryTable, scsitargetPortOperationalStatus=scsitargetPortOperationalStatus, vtlStatsConrolCommands=vtlStatsConrolCommands, fileSystemSpaceTable=fileSystemSpaceTable, vtlPortTrapIndex=vtlPortTrapIndex, mtreeListPreCompGib=mtreeListPreCompGib, powerModuleDescription=powerModuleDescription, replLagThreshholdReached=replLagThreshholdReached, cifsConfig=cifsConfig, taskActive=taskActive, scsitargetPortFcBaseWwpn=scsitargetPortFcBaseWwpn, hDTSystemError=hDTSystemError, ddboostFileRepliPerfOutNetworkKBPerSec=ddboostFileRepliPerfOutNetworkKBPerSec, ddboostNetworkKBytesPerSecond=ddboostNetworkKBytesPerSecond, vtlLibraryVendor=vtlLibraryVendor, PowerModuleStatusTC=PowerModuleStatusTC, fileSystemProperties=fileSystemProperties, scsitargetInitiatorEndpEntry=scsitargetInitiatorEndpEntry, nfsActivePath=nfsActivePath, replConfigTenantUnit=replConfigTenantUnit, legacyPowerSupplyWarning=legacyPowerSupplyWarning, vtlLibraryName=vtlLibraryName, diskCapacity=diskCapacity, systemStatsIndex=systemStatsIndex, nvramProperties=nvramProperties, vDiskSCSITargetMismatch=vDiskSCSITargetMismatch, portPathDisabled=portPathDisabled, vtlStatsPrimSeqProtoErrors=vtlStatsPrimSeqProtoErrors, vtlPoolStatus=vtlPoolStatus, nvramHCMemorySize=nvramHCMemorySize, ddboostFileReplStatsPreCompSent=ddboostFileReplStatsPreCompSent, vtlStatsReadCommands=vtlStatsReadCommands, scsitargetEndpoint=scsitargetEndpoint, mtreeRetentionLockStatus=mtreeRetentionLockStatus, taskHistoryStartTime=taskHistoryStartTime, ddboostGroupRev1=ddboostGroupRev1, ddboostAccessClientsEncryStrength=ddboostAccessClientsEncryStrength, spuriousInterruptDisabled=spuriousInterruptDisabled, dd140=dd140, highAvailabilityGroup=highAvailabilityGroup, ddboostUserTable=ddboostUserTable, vtlInitiatorWWNN=vtlInitiatorWWNN, cifsProperties=cifsProperties, nfsReceivePercentage=nfsReceivePercentage, tenantUnitDdboostStuList=tenantUnitDdboostStuList, scsitargetEndpointEntry=scsitargetEndpointEntry, fileSystemSpaceUsed=fileSystemSpaceUsed, CifsStatsDetailsIndexTC=CifsStatsDetailsIndexTC, internalDiskStorageGroup=internalDiskStorageGroup, fileSystemSpaceAvail=fileSystemSpaceAvail, tenantUnitMgmtGroupListGroupRole=tenantUnitMgmtGroupListGroupRole, unknown=unknown, fileSystemCompression=fileSystemCompression, nvramStatsEntry=nvramStatsEntry, VtlPortWWNNTC=VtlPortWWNNTC, ReplicationStateTC=ReplicationStateTC, DDboostUserTC=DDboostUserTC, vtlInitiatorName=vtlInitiatorName, scsitargetGroup=scsitargetGroup, ddboostFileReplHistoryDirection=ddboostFileReplHistoryDirection, replPerformancePreCompKBPerSec=replPerformancePreCompKBPerSec, alertHistory=alertHistory, artConfigStatus=artConfigStatus, SystemNotesTC=SystemNotesTC, fanEnclosureID=fanEnclosureID, cifsOpsPerSecond=cifsOpsPerSecond, dDFSDiedAfterReboot=dDFSDiedAfterReboot, diskStorage=diskStorage, SystemSerialNumberTC=SystemSerialNumberTC, PowerModuleDescriptionTC=PowerModuleDescriptionTC, diskFailure=diskFailure, taskHistory=taskHistory, nvramBatteryAlert=nvramBatteryAlert, duplicateVTLPoolNames=duplicateVTLPoolNames, enclosureListNum=enclosureListNum, mailserverError=mailserverError, highAvailabilityNode=highAvailabilityNode, quotaCapacityEntry=quotaCapacityEntry, systemHardwareSlotName=systemHardwareSlotName, DDMibVersionTC=DDMibVersionTC, ddboostFileReplHistoryPreComp=ddboostFileReplHistoryPreComp, dd880=dd880, CifsConfigMaxConnectionTC=CifsConfigMaxConnectionTC, unsupportedHardwareConfig=unsupportedHardwareConfig, systemVersion=systemVersion, CifsConfigGroupNameTC=CifsConfigGroupNameTC, openFanDrawer=openFanDrawer, cpuAvgPercentageBusy=cpuAvgPercentageBusy, enclosure=enclosure, systemActiveUserName=systemActiveUserName, unsupportedACVoltage=unsupportedACVoltage, vtlPoolTapes=vtlPoolTapes, diskTemperature=diskTemperature, powerSupplyFailedAlarm=powerSupplyFailedAlarm, diskFirmwareVersion=diskFirmwareVersion, systemCapacityLicenseFeature=systemCapacityLicenseFeature, VtlTapePoolTC=VtlTapePoolTC, dd200=dd200, diskSASAlarm=diskSASAlarm, tenantUnitMtreeList=tenantUnitMtreeList, diskPropTrapIndex=diskPropTrapIndex, dataDomainMibObjects=dataDomainMibObjects, diskCrcErrCount=diskCrcErrCount, sASEnclosureCheck=sASEnclosureCheck, compromisedEncryptionKeys=compromisedEncryptionKeys, replSyncedAsOfTime=replSyncedAsOfTime, artMigrationScheduleIndex=artMigrationScheduleIndex, suspendedMReplMissingUnits=suspendedMReplMissingUnits, replSource=replSource, mtreeRetentionLockUUID=mtreeRetentionLockUUID, scsitargetPortEntry=scsitargetPortEntry, tenantUnitListTenantSelfServiceMode=tenantUnitListTenantSelfServiceMode, VtlTapeModTimeTC=VtlTapeModTimeTC, dd580g=dd580g, historicalDatabasePruneError=historicalDatabasePruneError, dataDomainMibCompliances=dataDomainMibCompliances, systemActiveUserEntry=systemActiveUserEntry, unset=unset, expiredHostCertificate=expiredHostCertificate, tenantUnitMtreeListMtreeName=tenantUnitMtreeListMtreeName, alertHistoryTable=alertHistoryTable, scsitargetPortEndpEndpoint=scsitargetPortEndpEndpoint, highAvailabilityNodeState=highAvailabilityNodeState, cifsSharePath=cifsSharePath, artConfigMigrationSchedule=artConfigMigrationSchedule, replLogFull=replLogFull, replGroup=replGroup, artMigrationScheduleTable=artMigrationScheduleTable, DDMibTableString512TC=DDMibTableString512TC, CifsConfigNetBIOSHostnameTC=CifsConfigNetBIOSHostnameTC, cifsConfigMode=cifsConfigMode, vtlPortID=vtlPortID, scsitargetPortConnectionType=scsitargetPortConnectionType, vtlStatsSignalLosses=vtlStatsSignalLosses, replDestNotConfigured=replDestNotConfigured, FileSystemStatusTC=FileSystemStatusTC, CifsConfigDomainControllerTC=CifsConfigDomainControllerTC, NfsStatsExportPointTC=NfsStatsExportPointTC, taskHistoryState=taskHistoryState, mgmtModuleFault=mgmtModuleFault, scsitargetDeviceName=scsitargetDeviceName, encryptionKeyExportFailed=encryptionKeyExportFailed, VtlTapeBarCodeTC=VtlTapeBarCodeTC, scsitargetEndpointTable=scsitargetEndpointTable, ddboostBackupConnections=ddboostBackupConnections, cifsConfigDNS=cifsConfigDNS, dataDomainMibComplianceRev1=dataDomainMibComplianceRev1, scsitargetPortEndpCurrentInstance=scsitargetPortEndpCurrentInstance, scsitargetGroupNumDevices=scsitargetGroupNumDevices, fileSystemOptions=fileSystemOptions, highAvailabilityComponent=highAvailabilityComponent, scsitargetPortFcNpiv=scsitargetPortFcNpiv, dnsServer=dnsServer, enclosureGroup=enclosureGroup, ddboostStatsCompressionRatio=ddboostStatsCompressionRatio, missingPortConnection=missingPortConnection, vtlGroupDeviceIndex=vtlGroupDeviceIndex, vTLDisabled=vTLDisabled, foreignEnclosure=foreignEnclosure, ReplicationConfigDestTC=ReplicationConfigDestTC, FileSystemCleanScheduleTC=FileSystemCleanScheduleTC, vtlStatsOut=vtlStatsOut, generalHardwareFailure=generalHardwareFailure, systemPortsFirmware=systemPortsFirmware, NfsClientIndexTC=NfsClientIndexTC, MtreeListStatusTC=MtreeListStatusTC, dd7200=dd7200, enclosureHighTemp=enclosureHighTemp, fileSystemCleanIndex=fileSystemCleanIndex, replPerformanceNetworkKBPerSec=replPerformanceNetworkKBPerSec, diskReadFailCount=diskReadFailCount, VtlStatsInTC=VtlStatsInTC, VtlLibrarySerialTC=VtlLibrarySerialTC, VtlStatsLinkFailuresTC=VtlStatsLinkFailuresTC, highAvailabilityComponentName=highAvailabilityComponentName, vtlTapeLocation=vtlTapeLocation, missingHostCertificate=missingHostCertificate, raidReconSevereAlarm=raidReconSevereAlarm, systemPortsLinkSpeed=systemPortsLinkSpeed, powerSupplyInputFault=powerSupplyInputFault)
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", tenantInfoTenantUnitTable=tenantInfoTenantUnitTable, fileSystemClean=fileSystemClean, replPerformanceStreams=replPerformanceStreams, spaceReclRestartFailed=spaceReclRestartFailed, fanPropertiesTable=fanPropertiesTable, dd460=dd460, NfsStatsFilesystemTypeTC=NfsStatsFilesystemTypeTC, ReplicationConfigConnHostTC=ReplicationConfigConnHostTC, fileSystemCompressionEntry=fileSystemCompressionEntry, tenantUnitDdboostStuListStuName=tenantUnitDdboostStuListStuName, fileSpaceCriticalAlarm=fileSpaceCriticalAlarm, storageMigrationCopyComplete=storageMigrationCopyComplete, diskTemperatureWarning=diskTemperatureWarning, ddboostStorageUnitUser=ddboostStorageUnitUser, ddboostFileRepliPerfInNetworkKBPerSec=ddboostFileRepliPerfInNetworkKBPerSec, dDFSRebooted=dDFSRebooted, fileSystemGroupRev1=fileSystemGroupRev1, diskPerfEnclosureID=diskPerfEnclosureID, cleaningError=cleaningError, cifsConfigMaxOpenFiles=cifsConfigMaxOpenFiles, dd630=dd630, replTrapContext=replTrapContext, VtlDriveVendorTC=VtlDriveVendorTC, ddboostReadKBytesPerSecond=ddboostReadKBytesPerSecond, OpsPerSecond=OpsPerSecond, storage=storage, scsitargetInitiatorGroup=scsitargetInitiatorGroup, diskUnsupportedAlarm=diskUnsupportedAlarm, ddboost=ddboost, dIMMFailure=dIMMFailure, bMCHangCritical=bMCHangCritical, snapshotFullAlarm=snapshotFullAlarm, NfsClientOptionsTC=NfsClientOptionsTC, highAvailabilityComponentTable=highAvailabilityComponentTable, nvramHWAlert=nvramHWAlert, cifsConfigMaxOpenFilesPerConnection=cifsConfigMaxOpenFilesPerConnection, VtlPortNameTC=VtlPortNameTC, vtlLibraryTotalSlots=vtlLibraryTotalSlots, DDMibDateTC=DDMibDateTC, VtlLibraryNameTC=VtlLibraryNameTC, vtlTapeComp=vtlTapeComp, scsitargetGroupNumInitiators=scsitargetGroupNumInitiators, storageMigrationUserSuspend=storageMigrationUserSuspend, diskPerfState=diskPerfState, DDMibInteger32TC=DDMibInteger32TC, alertInfoDescription=alertInfoDescription, enclosurePack=enclosurePack, FanStatusTC=FanStatusTC, internalDiskStorageNotificationsGroup=internalDiskStorageNotificationsGroup, scsitargetPortFirmware=scsitargetPortFirmware, coredumpDisabled=coredumpDisabled, tenantUnitAdminIpInfoType=tenantUnitAdminIpInfoType, scsitargetDeviceGrpLun=scsitargetDeviceGrpLun, VtlPortEnabledTC=VtlPortEnabledTC, diskReliabilityEntry=diskReliabilityEntry, systemPorts=systemPorts, ErrorCount=ErrorCount, historicalDatabaseFailoverError=historicalDatabaseFailoverError, scsitargetDeviceGrpTable=scsitargetDeviceGrpTable, scsitargetEndpointCurrentSystemAddress=scsitargetEndpointCurrentSystemAddress, nvramBatteriesIndex=nvramBatteriesIndex, taskActiveStartTime=taskActiveStartTime, vtlPoolComp=vtlPoolComp, NvramHCPropertyBytesTC=NvramHCPropertyBytesTC, ddboostAccessClientsEntry=ddboostAccessClientsEntry, DiskPackTC=DiskPackTC, vtlGroup=vtlGroup, unusableHostCertificate=unusableHostCertificate, artConfigIndex=artConfigIndex, replicationInfoTable=replicationInfoTable, alertInfo=alertInfo, scsitargetDeviceGrpDevice=scsitargetDeviceGrpDevice, VtlPortModelTC=VtlPortModelTC, dataDomainMibComplianceRev3=dataDomainMibComplianceRev3, missingCreplUnits=missingCreplUnits, taskActiveTable=taskActiveTable, tooManyRelaunches=tooManyRelaunches, alertInfoEntry=alertInfoEntry, fileSystemPreCompressionSize=fileSystemPreCompressionSize, replConfigConnHost=replConfigConnHost, dataDomainMibGroups=dataDomainMibGroups, replPathTooLong=replPathTooLong, VtlStatsInvalidTxWordsTC=VtlStatsInvalidTxWordsTC, nfsStats=nfsStats, ddboostFileReplHistoryTime=ddboostFileReplHistoryTime, smtProperties=smtProperties, fanPropertiesEntry=fanPropertiesEntry, vtlGroupDeviceCount=vtlGroupDeviceCount, AlertDescriptionTC=AlertDescriptionTC, ddboostStorageUnitEntry=ddboostStorageUnitEntry, vtlLibraryRevision=vtlLibraryRevision, vtlInitiatorStatus=vtlInitiatorStatus, vtlGroups=vtlGroups, scsitargetPort=scsitargetPort, DDMibString96TC=DDMibString96TC, VtlTapeCompTC=VtlTapeCompTC, fileSystemGroup=fileSystemGroup, bMCFailure=bMCFailure, dd660=dd660, nvramGroup=nvramGroup, vtlPortEntry=vtlPortEntry, DiskModelTC=DiskModelTC, scsitargetProcessState=scsitargetProcessState, scsitargetInitiatorFcWwnn=scsitargetInitiatorFcWwnn, enclosureListCapacity=enclosureListCapacity, upgradeFailure=upgradeFailure, unsupportedVirtualCPU=unsupportedVirtualCPU, searchDomainsName=searchDomainsName, replicationConfig=replicationConfig, artMigrationPolicy=artMigrationPolicy, vtlGroupDeviceTable=vtlGroupDeviceTable, ddboostUserEntry=ddboostUserEntry, CifsShareClientsTC=CifsShareClientsTC, scsitargetGroupEntry=scsitargetGroupEntry, ReplicationConfigEnabledTC=ReplicationConfigEnabledTC, tenantUnitAdminIpInfoTable=tenantUnitAdminIpInfoTable, ddboostFileReplHistoryIndex=ddboostFileReplHistoryIndex, scsitargetPortEndpEnabled=scsitargetPortEndpEnabled, managedSystemState=managedSystemState, fileSystemResourceTier=fileSystemResourceTier, fileSystemArchiveUnitSize=fileSystemArchiveUnitSize, managedSystemHostname=managedSystemHostname, snmpTrapHostsName=snmpTrapHostsName, uncertifiedFirmware=uncertifiedFirmware, vtlPortFirmware=vtlPortFirmware, VtlDriveIndexTC=VtlDriveIndexTC, nfsIdlePercentage=nfsIdlePercentage, licenseExpired=licenseExpired, quotaCapacityTenantUnit=quotaCapacityTenantUnit, ddboostFileRepliPerfInPreCompKBPerSec=ddboostFileRepliPerfInPreCompKBPerSec, managedSystemEntry=managedSystemEntry, chassisTempCritical=chassisTempCritical, systemLicenseIndex=systemLicenseIndex, nvramPropertiesEntry=nvramPropertiesEntry, taskHistoryID=taskHistoryID, enclosureListEntry=enclosureListEntry)
