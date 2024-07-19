#
# PySNMP MIB module DATA-DOMAIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/datadomain/DATA-DOMAIN-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 10:00:42 2024
# On host fv-az1251-884 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, iso, Counter64, ModuleIdentity, Gauge32, TimeTicks, ObjectIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Counter32, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Counter64", "ModuleIdentity", "Gauge32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Counter32", "IpAddress", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dataDomainMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 19746))
dataDomainMib.setRevisions(('2017-05-16 00:00',))
if mibBuilder.loadTexts: dataDomainMib.setLastUpdated('201705160000Z')
if mibBuilder.loadTexts: dataDomainMib.setOrganization('Data Domain, Inc')
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
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Temperature(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class Minutes(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class Percentage(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class PercentageStr(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class KBytesPerSecond(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class OpsPerSecond(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class ErrorCount(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class DDMibTableIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DDMibTableString32TC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class DDMibTableString64TC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DDMibTableString128TC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class DDMibTableString256TC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class DDMibTableString512TC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '512a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 512)

class DDMibTableString1024TC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class DDMibString96TC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '96a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 96)

class DDMibTableSizeGibTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class DDMibTableSizeMiBTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class DDMibDateTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class DDMibMemorySizeTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class DDMibTimeStampTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DDMibVersionTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DDMibTableEnabledTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class DDMibInteger32TC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class DDMibCompressionFactorTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class DDMibAlertSeverityTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DDMibTrafficBytesTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class DDMibStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class PowerModuleIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PowerModuleDescriptionTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class PowerModuleStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 99))
    namedValues = NamedValues(("absent", 0), ("ok", 1), ("failed", 2), ("faulty", 3), ("acnone", 4), ("unknown", 99))

class TempSensorIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class TempSensorDescriptionTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TempSensorStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("failed", 0), ("ok", 1), ("notfound", 2), ("overheatWarning", 3), ("overheatCritical", 4))

class FanIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FanDescriptionTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class FanLevelTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("low", 1), ("medium", 2), ("high", 3))

class FanStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notfound", 0), ("ok", 1), ("fail", 2))

class NvramIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NvramMemorySizeTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class NvramHCPropertyBytesTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class NvramWindowSizeTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class NvramBatteryIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NvramBatteryStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ok", 0), ("disabled", 1), ("discharged", 2), ("softdisabled", 3))

class DiskIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DiskModelTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DiskFirmwareVersionTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DiskSerialNumberTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class DiskCapacityTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class DiskStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ok", 1), ("unknown", 2), ("absent", 3), ("failed", 4), ("spare", 5), ("available", 6))

class DiskPackTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notapplicable", 0), ("pack1", 1), ("pack2", 2), ("pack3", 3), ("pack4", 4))

class DiskSectorsPerSecondTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class FileSystemStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("running", 3), ("unknown", 4), ("error", 5), ("cleaning", 6))

class FileSystemResourceIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FileSystemResourceNameTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class FileSystemSpaceUnitTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class FileSystemCompressionSizeTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class FileSystemCompressionFactorTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class FileSystemCompressionPeriodTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class DateTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class FileSystemOptionsIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FileSystemOptionsNameTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class FileSystemOptionsValueTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class FileSystemCleanIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class FileSystemCleanStatusTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class FileSystemCleanScheduleTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class FileSystemCleanThrottleTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class AlertIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AlertTimestampTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class AlertDescriptionTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SystemStatsIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class RaidDiskStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 99))
    namedValues = NamedValues(("inuse", 1), ("notinuse", 2), ("spare", 3), ("absent", 4), ("failed", 5), ("invalid", 6), ("foreign", 7), ("known", 8), ("available", 9), ("unknown", 99))

class ReplicationStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("initializing", 1), ("normal", 2), ("recovering", 3), ("uninitialized", 4))

class ReplicationStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("connected", 1), ("disconnected", 2), ("migrating", 3), ("suspended", 4), ("neverConnected", 5), ("idle", 6))

class ReplicationConnectTimeTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class ReplicationPathTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '254a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 254)

class ReplicationTrafficTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class ReplicationThrottleTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class ReplicationSyncedTimeTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class ReplicationContextTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ReplicationConfigIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ReplicationConfigContextIdTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class ReplicationConfigSourceTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class ReplicationConfigDestTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class ReplicationConfigConnHostTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class ReplicationConfigConnPortTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class ReplicationConfigLowBWOptimTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class ReplicationConfigEnabledTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class NfsStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class NfsClientIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NfsClientPathTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class NfsClientClientsTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class NfsClientOptionsTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '254a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 254)

class NfsStatsIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class NfsStatsExportPointTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '254a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 254)

class NfsStatsFilesystemTypeTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class NfsStatsCacheEntryTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class NfsStatsFileHandleLookupTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class NfsStatsMaxCacheSizeTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class NfsStatsCurrentOpenStreamsTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class VtlAdminStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("enabled", 1), ("disabled", 2), ("failed", 3))

class VtlProcessStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("stopped", 1), ("starting", 2), ("running", 3), ("timingout", 4), ("stopping", 5), ("stuck", 6))

class VtlLibraryIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 64)

class VtlLibraryNameTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlLibraryVendorTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlLibraryModelTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlLibraryRevisionTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlLibrarySerialTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlLibraryTotalDrivesTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class VtlLibraryTotalSlotsTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class VtlLibraryTotalCapsTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class VtlLibraryStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("online", 1), ("offline", 2))

class VtlDriveIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 512)

class VtlDriveNameTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlDriveVendorTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlDriveModelTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlDriveRevisionTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlDriveSerialTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlDriveStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("online", 1), ("offline", 2))

class VtlDriveTapeVolumeTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlPortIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10)

class VtlPortNameTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlPortIDTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class VtlPortModelTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlPortFirmwareTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlPortWWNNTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlPortWWPNTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlPortConnectionTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("nPORT", 0), ("loop", 1), ("pointToPoint", 2), ("fabricLoop", 3), ("unknown", 4))

class VtlPortSpeedTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 6))
    namedValues = NamedValues(("zeroGBPS", 0), ("oneGBPS", 1), ("twoGBPS", 2), ("fourGBPS", 3), ("eightGBPS", 4), ("unknown", 6))

class VtlPortEnabledTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1), ("unknown", 2))

class VtlPortStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("offline", 0), ("online", 1), ("unknown", 2))

class VtlTapeIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 250000)

class VtlTapeBarCodeTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class VtlTapePoolTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeLocationTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeStateTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeSizeTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeUsedTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeCompTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlTapeModTimeTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlStatsIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class VtlStatsPortTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class VtlStatsConrolCommandsTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VtlStatsWriteCommandsTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VtlStatsReadCommandsTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VtlStatsInTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VtlStatsOutTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VtlStatsLinkFailuresTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VtlStatsLIPCountTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VtlStatsSyncLossesTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VtlStatsSignalLossesTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VtlStatsPrimSeqProtoErrorsTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VtlStatsInvalidTxWordsTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VtlStatsInvalidCRCsTC(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class CifsStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("enabled", 1), ("enabledRunning", 2), ("enabledNotRunning", 3), ("enabledWindbindNotRun", 4), ("disabled", 5))

class CifsConfigModeTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CifsConfigWINSServerTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsConfigNetBIOSHostnameTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CifsConfigDomainControllerTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsConfigDNSTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsConfigGroupNameTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CifsConfigMaxConnectionTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class CifsConfigMaxOpenFilesPerConnectionTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class CifsShareIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CifsShareNameTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CifsSharePathTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsShareMaxConnectionTC(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class CifsShareClientsTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsShareBrowsingTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CifsShareWriteableTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CifsShareUserTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class CifsShareCommentTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CifsStatsSummaryIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CifsStatsDetailsIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CifsOptionsIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class CifsOptionsNameTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CifsOptionsValueTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class DDboostStatsIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DDboostStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class DDboostUserTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class SystemSerialNumberTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class SystemTimeZoneNameTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class SystemNotesTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class FileSystemArchiveUnitStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("new", 1), ("target", 2), ("sealed", 3))

class FileSystemArchiveUnitStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ready", 1), ("disabled", 2))

class MtreeListStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("deleted", 1), ("readOnly", 2), ("readWrite", 3), ("replicationDestination", 4), ("retentionLockEnabled", 5), ("retentionLockDisabled", 6))

class MtreeRetentionLockStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class TenantUnitMgmtUserListUserRoleTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tenantAdmin", 1), ("tenantUser", 2))

class TenantUnitMgmtGroupTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("all", 0), ("unknown", 1), ("local", 2), ("ad", 3), ("nis", 4), ("ldap", 5))

class SmtStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class TenantUnitSecurityModeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("strict", 1), ("default", 2))

class DDStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class DdboostAccessClientsEncryStrengthTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3))
    namedValues = NamedValues(("none", 0), ("medium", 2), ("high", 3))

class DdboostAccessClientsAuthModeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("oneWay", 1), ("twoWay", 2), ("anonymous", 3))

class HaSystemStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("highlyAvailable", 1), ("degraded", 2))

class HaStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("notOk", 2), ("notApplicable", 3))

power = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1))
powerModules = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1))
powerModuleTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1), )
if mibBuilder.loadTexts: powerModuleTable.setStatus('current')
powerModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "powerEnclosureID"), (0, "DATA-DOMAIN-MIB", "powerModuleIndex"))
if mibBuilder.loadTexts: powerModuleEntry.setStatus('current')
powerEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: powerEnclosureID.setStatus('current')
powerModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 2), PowerModuleIndexTC())
if mibBuilder.loadTexts: powerModuleIndex.setStatus('current')
powerModuleDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 3), PowerModuleDescriptionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerModuleDescription.setStatus('current')
powerModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 1, 1, 1, 1, 4), PowerModuleStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerModuleStatus.setStatus('current')
temperatures = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2))
temperatureSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1))
temperatureSensorTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1), )
if mibBuilder.loadTexts: temperatureSensorTable.setStatus('current')
temperatureSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tempEnclosureID"), (0, "DATA-DOMAIN-MIB", "tempSensorIndex"))
if mibBuilder.loadTexts: temperatureSensorEntry.setStatus('current')
tempEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: tempEnclosureID.setStatus('current')
tempSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 2), TempSensorIndexTC())
if mibBuilder.loadTexts: tempSensorIndex.setStatus('current')
tempSensorTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 3), TempSensorIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorTrapIndex.setStatus('current')
tempSensorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 4), TempSensorDescriptionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorDescription.setStatus('current')
tempSensorCurrentValue = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 5), Temperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorCurrentValue.setStatus('current')
tempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 2, 1, 1, 1, 6), TempSensorStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorStatus.setStatus('current')
fans = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3))
fanProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1))
fanPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1), )
if mibBuilder.loadTexts: fanPropertiesTable.setStatus('current')
fanPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fanEnclosureID"), (0, "DATA-DOMAIN-MIB", "fanIndex"))
if mibBuilder.loadTexts: fanPropertiesEntry.setStatus('current')
fanEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: fanEnclosureID.setStatus('current')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 2), FanIndexTC())
if mibBuilder.loadTexts: fanIndex.setStatus('current')
fanTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 3), FanIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanTrapIndex.setStatus('current')
fanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 4), FanDescriptionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanDescription.setStatus('current')
fanLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 5), FanLevelTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanLevel.setStatus('current')
fanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 1, 3, 1, 1, 1, 6), FanStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStatus.setStatus('current')
nvramBatteries = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3))
nvramBatteryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1), )
if mibBuilder.loadTexts: nvramBatteryTable.setStatus('current')
nvramBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nvramBatteriesIndex"), (0, "DATA-DOMAIN-MIB", "nvramBatteryIndex"))
if mibBuilder.loadTexts: nvramBatteryEntry.setStatus('current')
nvramBatteriesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 1), NvramIndexTC())
if mibBuilder.loadTexts: nvramBatteriesIndex.setStatus('current')
nvramBatteryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 2), NvramBatteryIndexTC())
if mibBuilder.loadTexts: nvramBatteryIndex.setStatus('current')
nvramBatteryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 3), NvramBatteryStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramBatteryStatus.setStatus('current')
nvramBatteryCharge = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 3, 1, 1, 4), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramBatteryCharge.setStatus('current')
nvramProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1))
nvramPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1), )
if mibBuilder.loadTexts: nvramPropertiesTable.setStatus('current')
nvramPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nvramPropertiesIndex"))
if mibBuilder.loadTexts: nvramPropertiesEntry.setStatus('current')
nvramPropertiesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 1), NvramIndexTC())
if mibBuilder.loadTexts: nvramPropertiesIndex.setStatus('current')
nvramMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 2), NvramMemorySizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramMemorySize.setStatus('current')
nvramWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 3), NvramWindowSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramWindowSize.setStatus('current')
nvramHCMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 1, 1, 1, 4), NvramHCPropertyBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramHCMemorySize.setStatus('current')
nvramStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2))
nvramStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1), )
if mibBuilder.loadTexts: nvramStatsTable.setStatus('current')
nvramStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nvramStatsIndex"))
if mibBuilder.loadTexts: nvramStatsEntry.setStatus('current')
nvramStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1, 1), NvramIndexTC())
if mibBuilder.loadTexts: nvramStatsIndex.setStatus('current')
nvramPCIErrorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1, 2), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramPCIErrorCount.setStatus('current')
nvramMemoryErrorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 2, 2, 1, 1, 3), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramMemoryErrorCount.setStatus('current')
fileSystemArchiveUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6))
fileSystemArchiveUnitTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1), )
if mibBuilder.loadTexts: fileSystemArchiveUnitTable.setStatus('current')
fileSystemArchiveUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemArchiveUnitIndex"))
if mibBuilder.loadTexts: fileSystemArchiveUnitEntry.setStatus('current')
fileSystemArchiveUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: fileSystemArchiveUnitIndex.setStatus('current')
fileSystemArchiveUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitName.setStatus('current')
fileSystemArchiveUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 3), FileSystemArchiveUnitStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitState.setStatus('current')
fileSystemArchiveUnitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 4), FileSystemArchiveUnitStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitStatus.setStatus('current')
fileSystemArchiveUnitStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 5), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitStartTime.setStatus('current')
fileSystemArchiveUnitEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 6), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitEndTime.setStatus('current')
fileSystemArchiveUnitSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 7), DDMibTableSizeGibTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitSize.setStatus('current')
fileSystemArchiveUnitDiskGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 6, 1, 1, 8), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemArchiveUnitDiskGroups.setStatus('current')
fileSystemClean = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5))
fileSystemCleanTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1), )
if mibBuilder.loadTexts: fileSystemCleanTable.setStatus('current')
fileSystemCleanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemCleanIndex"))
if mibBuilder.loadTexts: fileSystemCleanEntry.setStatus('current')
fileSystemCleanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 1), FileSystemCleanIndexTC())
if mibBuilder.loadTexts: fileSystemCleanIndex.setStatus('current')
fileSystemCleanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 2), FileSystemCleanStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCleanStatus.setStatus('current')
fileSystemCleanSchedule = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 3), FileSystemCleanScheduleTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCleanSchedule.setStatus('current')
fileSystemCleanThrottle = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 5, 1, 1, 4), FileSystemCleanThrottleTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCleanThrottle.setStatus('current')
fileSystemCompression = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3))
fileSystemCompressionTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1), )
if mibBuilder.loadTexts: fileSystemCompressionTable.setStatus('current')
fileSystemCompressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemCompressionIndex"))
if mibBuilder.loadTexts: fileSystemCompressionEntry.setStatus('current')
fileSystemCompressionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 1), FileSystemResourceIndexTC())
if mibBuilder.loadTexts: fileSystemCompressionIndex.setStatus('current')
fileSystemCompressionPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 2), FileSystemCompressionPeriodTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCompressionPeriod.setStatus('current')
fileSystemCompressionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 3), DateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCompressionStartTime.setStatus('current')
fileSystemCompressionEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 4), DateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemCompressionEndTime.setStatus('current')
fileSystemPreCompressionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 5), FileSystemCompressionSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemPreCompressionSize.setStatus('current')
fileSystemPostCompressionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 6), FileSystemCompressionSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemPostCompressionSize.setStatus('current')
fileSystemGlobalCompressionFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 7), FileSystemCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemGlobalCompressionFactor.setStatus('current')
fileSystemLocalCompressionFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 8), FileSystemCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemLocalCompressionFactor.setStatus('current')
fileSystemTotalCompressionFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 9), FileSystemCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemTotalCompressionFactor.setStatus('current')
fileSystemReductionPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 10), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemReductionPercent.setStatus('deprecated')
fileSystemReductionPercent1 = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 3, 1, 1, 11), PercentageStr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemReductionPercent1.setStatus('current')
fileSystemOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4))
fileSystemOptionsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1), )
if mibBuilder.loadTexts: fileSystemOptionsTable.setStatus('current')
fileSystemOptionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemOptionsIndex"))
if mibBuilder.loadTexts: fileSystemOptionsEntry.setStatus('current')
fileSystemOptionsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1, 1), FileSystemOptionsIndexTC())
if mibBuilder.loadTexts: fileSystemOptionsIndex.setStatus('current')
fileSystemOptionsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1, 2), FileSystemOptionsNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemOptionsName.setStatus('current')
fileSystemOptionsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 4, 1, 1, 3), FileSystemOptionsValueTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemOptionsValue.setStatus('current')
fileSystemProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1))
fileSystemStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 1), FileSystemStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemStatus.setStatus('current')
fileSystemVirtualSpace = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 2), FileSystemSpaceUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemVirtualSpace.setStatus('current')
fileSystemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 3), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemUpTime.setStatus('current')
fileSystemStatusMessage = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 3, 1, 4), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemStatusMessage.setStatus('current')
fileSystemSpace = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2))
fileSystemSpaceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1), )
if mibBuilder.loadTexts: fileSystemSpaceTable.setStatus('current')
fileSystemSpaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "fileSystemResourceIndex"))
if mibBuilder.loadTexts: fileSystemSpaceEntry.setStatus('current')
fileSystemResourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 1), FileSystemResourceIndexTC())
if mibBuilder.loadTexts: fileSystemResourceIndex.setStatus('current')
fileSystemResourceTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 2), FileSystemResourceIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemResourceTrapIndex.setStatus('current')
fileSystemResourceName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 3), FileSystemResourceNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemResourceName.setStatus('current')
fileSystemSpaceSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 4), FileSystemSpaceUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceSize.setStatus('current')
fileSystemSpaceUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 5), FileSystemSpaceUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceUsed.setStatus('current')
fileSystemSpaceAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 6), FileSystemSpaceUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceAvail.setStatus('current')
fileSystemPercentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 7), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemPercentUsed.setStatus('current')
fileSystemSpaceCleanable = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 8), FileSystemSpaceUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemSpaceCleanable.setStatus('current')
fileSystemResourceTier = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 3, 2, 1, 1, 9), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fileSystemResourceTier.setStatus('current')
currentAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1))
currentAlertTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1), )
if mibBuilder.loadTexts: currentAlertTable.setStatus('current')
currentAlertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "currentAlertIndex"))
if mibBuilder.loadTexts: currentAlertEntry.setStatus('current')
currentAlertIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 1), AlertIndexTC())
if mibBuilder.loadTexts: currentAlertIndex.setStatus('current')
currentAlertTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 2), AlertTimestampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertTimestamp.setStatus('current')
currentAlertDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 3), AlertDescriptionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertDescription.setStatus('current')
currentAlertSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 4), DDMibAlertSeverityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertSeverity.setStatus('current')
currentAlertID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 1, 1, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentAlertID.setStatus('current')
alertHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2))
alertHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1), )
if mibBuilder.loadTexts: alertHistoryTable.setStatus('current')
alertHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "alertHistoryIndex"))
if mibBuilder.loadTexts: alertHistoryEntry.setStatus('current')
alertHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: alertHistoryIndex.setStatus('current')
alertHistoryTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 2), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertHistoryTimestamp.setStatus('current')
alertHistoryDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 3), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertHistoryDescription.setStatus('current')
alertHistorySeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 4), DDMibAlertSeverityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertHistorySeverity.setStatus('current')
alertHistoryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 2, 1, 1, 5), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertHistoryStatus.setStatus('current')
alertInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 4, 3))
alertInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1), )
if mibBuilder.loadTexts: alertInfoTable.setStatus('current')
alertInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "alertInfoIndex"))
if mibBuilder.loadTexts: alertInfoEntry.setStatus('current')
alertInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: alertInfoIndex.setStatus('current')
alertInfoDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 4, 3, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertInfoDescription.setStatus('current')
systemStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1))
systemStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1), )
if mibBuilder.loadTexts: systemStatsTable.setStatus('current')
systemStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemStatsIndex"))
if mibBuilder.loadTexts: systemStatsEntry.setStatus('current')
systemStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 1), SystemStatsIndexTC())
if mibBuilder.loadTexts: systemStatsIndex.setStatus('current')
cpuAvgPercentageBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 2), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuAvgPercentageBusy.setStatus('current')
cpuMaxPercentageBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 3), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuMaxPercentageBusy.setStatus('current')
nfsOpsPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 4), OpsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsOpsPerSecond.setStatus('current')
nfsIdlePercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 5), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsIdlePercentage.setStatus('current')
nfsProcPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsProcPercentage.setStatus('current')
nfsSendPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 7), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsSendPercentage.setStatus('current')
nfsReceivePercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 8), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsReceivePercentage.setStatus('current')
cifsOpsPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 9), OpsPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsOpsPerSecond.setStatus('current')
diskReadKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 10), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadKBytesPerSecond.setStatus('current')
diskWriteKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 11), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteKBytesPerSecond.setStatus('current')
diskBusyPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 12), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskBusyPercentage.setStatus('current')
nvramReadKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 13), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramReadKBytesPerSecond.setStatus('current')
nvramWriteKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 14), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvramWriteKBytesPerSecond.setStatus('current')
replInKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 15), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replInKBytesPerSecond.setStatus('current')
replOutKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 5, 1, 1, 1, 16), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replOutKBytesPerSecond.setStatus('current')
diskPerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2))
diskPerformanceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1), )
if mibBuilder.loadTexts: diskPerformanceTable.setStatus('current')
diskPerformanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskPerfEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskPerfIndex"))
if mibBuilder.loadTexts: diskPerformanceEntry.setStatus('current')
diskPerfEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: diskPerfEnclosureID.setStatus('current')
diskPerfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 2), DiskIndexTC())
if mibBuilder.loadTexts: diskPerfIndex.setStatus('current')
diskSectorsRead = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 3), DiskSectorsPerSecondTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSectorsRead.setStatus('current')
diskSectorsWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 4), DiskSectorsPerSecondTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSectorsWritten.setStatus('current')
diskTotalKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 5), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTotalKBytes.setStatus('current')
diskBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 6), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskBusy.setStatus('current')
diskPerfState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 2, 1, 1, 7), DiskStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPerfState.setStatus('current')
diskProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1))
diskPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1), )
if mibBuilder.loadTexts: diskPropertiesTable.setStatus('current')
diskPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskPropEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskPropIndex"))
if mibBuilder.loadTexts: diskPropertiesEntry.setStatus('current')
diskPropEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: diskPropEnclosureID.setStatus('current')
diskPropIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 2), DiskIndexTC())
if mibBuilder.loadTexts: diskPropIndex.setStatus('current')
diskPropTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 3), DiskIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPropTrapIndex.setStatus('current')
diskModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 4), DiskModelTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskModel.setStatus('current')
diskFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 5), DiskFirmwareVersionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskFirmwareVersion.setStatus('current')
diskSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 6), DiskSerialNumberTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSerialNumber.setStatus('current')
diskCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 7), DiskCapacityTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskCapacity.setStatus('current')
diskPropState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 8), DiskStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPropState.setStatus('current')
diskPack = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 1, 1, 1, 9), DiskPackTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskPack.setStatus('current')
diskReliability = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3))
diskReliabilityTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1), )
if mibBuilder.loadTexts: diskReliabilityTable.setStatus('current')
diskReliabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "diskErrEnclosureID"), (0, "DATA-DOMAIN-MIB", "diskErrIndex"))
if mibBuilder.loadTexts: diskReliabilityEntry.setStatus('current')
diskErrEnclosureID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 1), EnclosureID())
if mibBuilder.loadTexts: diskErrEnclosureID.setStatus('current')
diskErrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 2), DiskIndexTC())
if mibBuilder.loadTexts: diskErrIndex.setStatus('current')
diskErrTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 3), DiskIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrTrapIndex.setStatus('current')
diskTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 4), Temperature()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTemperature.setStatus('current')
diskTimeoutCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 5), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTimeoutCount.setStatus('current')
diskReadFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 6), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReadFailCount.setStatus('current')
diskWriteFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 7), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskWriteFailCount.setStatus('current')
diskMiscFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 8), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskMiscFailCount.setStatus('current')
diskOffTrackErrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 9), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskOffTrackErrCount.setStatus('current')
diskSoftEccCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 10), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskSoftEccCount.setStatus('current')
diskCrcErrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 11), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskCrcErrCount.setStatus('current')
diskProbationalCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 12), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskProbationalCount.setStatus('current')
diskReallocCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 13), ErrorCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskReallocCount.setStatus('current')
diskErrState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 6, 3, 1, 1, 14), DiskStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskErrState.setStatus('current')
replicationConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2))
replicationConfigTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1), )
if mibBuilder.loadTexts: replicationConfigTable.setStatus('current')
replicationConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "replConfigIndex"))
if mibBuilder.loadTexts: replicationConfigEntry.setStatus('current')
replConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 1), ReplicationConfigIndexTC())
if mibBuilder.loadTexts: replConfigIndex.setStatus('current')
replConfigContextId = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 2), ReplicationConfigContextIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigContextId.setStatus('current')
replConfigSource = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 3), ReplicationConfigSourceTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigSource.setStatus('current')
replConfigDest = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 4), ReplicationConfigDestTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigDest.setStatus('current')
replConfigConnHost = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 5), ReplicationConfigConnHostTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigConnHost.setStatus('current')
replConfigConnPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 6), ReplicationConfigConnPortTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigConnPort.setStatus('current')
replConfigLowBWOptim = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 7), ReplicationConfigLowBWOptimTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigLowBWOptim.setStatus('current')
replConfigEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 8), ReplicationConfigEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigEnabled.setStatus('current')
replConfigTenantUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 2, 1, 1, 9), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConfigTenantUnit.setStatus('current')
replicationHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3))
replicationHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1), )
if mibBuilder.loadTexts: replicationHistoryTable.setStatus('current')
replicationHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "replHistoryContext"))
if mibBuilder.loadTexts: replicationHistoryEntry.setStatus('current')
replHistoryContext = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: replHistoryContext.setStatus('current')
replHistoryDate = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 2), DDMibDateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryDate.setStatus('current')
replHistoryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 3), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryTime.setStatus('current')
replHistoryPreCompWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 4), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPreCompWritten.setStatus('current')
replHistoryPreCompRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 5), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPreCompRemaining.setStatus('current')
replHistoryPreCompressed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 6), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPreCompressed.setStatus('current')
replHistoryPostFiltered = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 7), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPostFiltered.setStatus('current')
replHistoryPostLowBwOptim = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 8), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPostLowBwOptim.setStatus('current')
replHistoryPostLocalComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 9), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryPostLocalComp.setStatus('current')
replHistoryBytesNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 10), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistoryBytesNetwork.setStatus('current')
replHistorySyncedAsOfTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 3, 1, 1, 11), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replHistorySyncedAsOfTime.setStatus('current')
replicationInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1))
replicationInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1), )
if mibBuilder.loadTexts: replicationInfoTable.setStatus('current')
replicationInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "replContext"))
if mibBuilder.loadTexts: replicationInfoEntry.setStatus('current')
replContext = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 1), ReplicationContextTC())
if mibBuilder.loadTexts: replContext.setStatus('current')
replTrapContext = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 2), ReplicationContextTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replTrapContext.setStatus('current')
replState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 3), ReplicationStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replState.setStatus('current')
replStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 4), ReplicationStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replStatus.setStatus('current')
replFileSysStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 5), FileSystemStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replFileSysStatus.setStatus('current')
replConnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 6), ReplicationConnectTimeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replConnTime.setStatus('current')
replSource = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 7), ReplicationPathTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replSource.setStatus('current')
replDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 8), ReplicationPathTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replDestination.setStatus('current')
replPreCompBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 9), ReplicationTrafficTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPreCompBytesSent.setStatus('current')
replPostCompBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 10), ReplicationTrafficTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPostCompBytesSent.setStatus('current')
replPreCompBytesRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 11), ReplicationTrafficTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPreCompBytesRemaining.setStatus('current')
replPostCompBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 12), ReplicationTrafficTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPostCompBytesReceived.setStatus('current')
replThrottle = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 13), ReplicationThrottleTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replThrottle.setStatus('current')
replSyncedAsOfTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 1, 1, 1, 14), ReplicationSyncedTimeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replSyncedAsOfTime.setStatus('current')
replicationPerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4))
replicationPerformanceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1), )
if mibBuilder.loadTexts: replicationPerformanceTable.setStatus('current')
replicationPerformanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "replContext"))
if mibBuilder.loadTexts: replicationPerformanceEntry.setStatus('current')
replPerformancePreCompKBPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 1), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformancePreCompKBPerSec.setStatus('current')
replPerformanceNetworkKBPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 2), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceNetworkKBPerSec.setStatus('current')
replPerformanceStreams = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceStreams.setStatus('current')
replPerformanceBusyReading = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceBusyReading.setStatus('current')
replPerformanceBusyMeta = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceBusyMeta.setStatus('current')
replPerformanceWaitingDest = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 6), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceWaitingDest.setStatus('current')
replPerformanceWaitingNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 8, 4, 1, 1, 7), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: replPerformanceWaitingNetwork.setStatus('current')
nfsActive = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4))
nfsActiveTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1), )
if mibBuilder.loadTexts: nfsActiveTable.setStatus('current')
nfsActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nfsActiveIndex"))
if mibBuilder.loadTexts: nfsActiveEntry.setStatus('current')
nfsActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: nfsActiveIndex.setStatus('current')
nfsActivePath = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1, 2), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsActivePath.setStatus('current')
nfsActiveClients = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 4, 1, 1, 3), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsActiveClients.setStatus('current')
nfsClient = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2))
nfsClientTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1), )
if mibBuilder.loadTexts: nfsClientTable.setStatus('current')
nfsClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nfsClientIndex"))
if mibBuilder.loadTexts: nfsClientEntry.setStatus('current')
nfsClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 1), NfsClientIndexTC())
if mibBuilder.loadTexts: nfsClientIndex.setStatus('current')
nfsClientPath = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 2), NfsClientPathTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsClientPath.setStatus('current')
nfsClientClients = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 3), NfsClientClientsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsClientClients.setStatus('current')
nfsClientOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 2, 1, 1, 4), NfsClientOptionsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsClientOptions.setStatus('current')
nfsPort = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5))
nfsPortTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1), )
if mibBuilder.loadTexts: nfsPortTable.setStatus('current')
nfsPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nfsPortIndex"))
if mibBuilder.loadTexts: nfsPortEntry.setStatus('current')
nfsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: nfsPortIndex.setStatus('current')
nfsPortService = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsPortService.setStatus('current')
nfsPortPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 5, 1, 1, 3), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsPortPort.setStatus('current')
nfsProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 9, 1))
nfsStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 9, 1, 1), NfsStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatus.setStatus('current')
nfsStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3))
nfsStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1), )
if mibBuilder.loadTexts: nfsStatsTable.setStatus('current')
nfsStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "nfsStatsIndex"))
if mibBuilder.loadTexts: nfsStatsEntry.setStatus('current')
nfsStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 1), NfsStatsIndexTC())
if mibBuilder.loadTexts: nfsStatsIndex.setStatus('current')
nfsStatsExportPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 2), NfsStatsExportPointTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsExportPoint.setStatus('current')
nfsStatsFilesystemType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 3), NfsStatsFilesystemTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsFilesystemType.setStatus('current')
nfsStatsCacheEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 4), NfsStatsCacheEntryTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsCacheEntry.setStatus('current')
nfsStatsFileHandleLookup = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 5), NfsStatsFileHandleLookupTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsFileHandleLookup.setStatus('current')
nfsStatsMaxCacheSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 6), NfsStatsMaxCacheSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsMaxCacheSize.setStatus('current')
nfsStatsCurrentOpenStreams = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 9, 3, 1, 1, 7), NfsStatsCurrentOpenStreamsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfsStatsCurrentOpenStreams.setStatus('current')
cifsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2))
cifsConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 1), CifsConfigModeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigMode.setStatus('current')
cifsConfigWINSServer = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 2), CifsConfigWINSServerTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigWINSServer.setStatus('current')
cifsConfigNetBIOSHostname = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 3), CifsConfigNetBIOSHostnameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigNetBIOSHostname.setStatus('current')
cifsConfigDomainController = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 4), CifsConfigDomainControllerTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigDomainController.setStatus('current')
cifsConfigDNS = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 5), CifsConfigDNSTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigDNS.setStatus('current')
cifsConfigGroupName = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 6), CifsConfigGroupNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigGroupName.setStatus('current')
cifsConfigMaxConnection = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 7), CifsConfigMaxConnectionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigMaxConnection.setStatus('current')
cifsConfigMaxOpenFilesPerConnection = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 8), CifsConfigMaxOpenFilesPerConnectionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigMaxOpenFilesPerConnection.setStatus('deprecated')
cifsConfigMaxOpenFiles = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsConfigMaxOpenFiles.setStatus('current')
cifsOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5))
cifsOptionsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1), )
if mibBuilder.loadTexts: cifsOptionsTable.setStatus('current')
cifsOptionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "cifsOptionsIndex"))
if mibBuilder.loadTexts: cifsOptionsEntry.setStatus('current')
cifsOptionsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1, 1), CifsOptionsIndexTC())
if mibBuilder.loadTexts: cifsOptionsIndex.setStatus('current')
cifsOptionsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1, 2), CifsOptionsNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsOptionsName.setStatus('current')
cifsOptionsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 5, 1, 1, 3), CifsOptionsValueTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsOptionsValue.setStatus('current')
cifsProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 10, 1))
cifsStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 10, 1, 1), CifsStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsStatus.setStatus('current')
cifsShare = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3))
cifsShareTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1), )
if mibBuilder.loadTexts: cifsShareTable.setStatus('current')
cifsShareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "cifsShareIndex"))
if mibBuilder.loadTexts: cifsShareEntry.setStatus('current')
cifsShareIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 1), CifsShareIndexTC())
if mibBuilder.loadTexts: cifsShareIndex.setStatus('current')
cifsShareName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 2), CifsShareNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareName.setStatus('current')
cifsSharePath = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 3), CifsSharePathTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsSharePath.setStatus('current')
cifsShareClients = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 4), CifsShareClientsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareClients.setStatus('current')
cifsShareUser = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 5), CifsShareUserTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareUser.setStatus('current')
cifsShareComment = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 6), CifsShareCommentTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareComment.setStatus('current')
cifsShareBrowsing = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 7), CifsShareBrowsingTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareBrowsing.setStatus('current')
cifsShareWriteable = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 8), CifsShareWriteableTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareWriteable.setStatus('current')
cifsShareMaxConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 10, 3, 1, 1, 9), CifsShareMaxConnectionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifsShareMaxConnection.setStatus('current')
vtlConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2))
vtlLibrary = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1))
vtlLibraryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1), )
if mibBuilder.loadTexts: vtlLibraryTable.setStatus('current')
vtlLibraryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlLibraryIndex"))
if mibBuilder.loadTexts: vtlLibraryEntry.setStatus('current')
vtlLibraryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 1), VtlLibraryIndexTC())
if mibBuilder.loadTexts: vtlLibraryIndex.setStatus('current')
vtlLibraryName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 2), VtlLibraryNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryName.setStatus('current')
vtlLibraryVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 3), VtlLibraryVendorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryVendor.setStatus('current')
vtlLibraryModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 4), VtlLibraryModelTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryModel.setStatus('current')
vtlLibraryRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 5), VtlLibraryRevisionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryRevision.setStatus('current')
vtlLibrarySerial = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 6), VtlLibrarySerialTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibrarySerial.setStatus('current')
vtlLibraryTotalDrives = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 7), VtlLibraryTotalDrivesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryTotalDrives.setStatus('current')
vtlLibraryTotalSlots = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 8), VtlLibraryTotalSlotsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryTotalSlots.setStatus('current')
vtlLibraryTotalCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 9), VtlLibraryTotalCapsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryTotalCaps.setStatus('current')
vtlLibraryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 1, 1, 1, 10), VtlLibraryStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlLibraryStatus.setStatus('current')
vtlDrive = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2))
vtlDriveTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1), )
if mibBuilder.loadTexts: vtlDriveTable.setStatus('current')
vtlDriveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlDriveIndex"))
if mibBuilder.loadTexts: vtlDriveEntry.setStatus('current')
vtlDriveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 1), VtlDriveIndexTC())
if mibBuilder.loadTexts: vtlDriveIndex.setStatus('current')
vtlDriveName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 2), VtlDriveNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveName.setStatus('current')
vtlDriveVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 3), VtlDriveVendorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveVendor.setStatus('current')
vtlDriveModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 4), VtlDriveModelTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveModel.setStatus('current')
vtlDriveRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 5), VtlDriveRevisionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveRevision.setStatus('current')
vtlDriveSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 6), VtlDriveSerialTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveSerial.setStatus('current')
vtlDriveLibraryName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 7), VtlLibraryNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveLibraryName.setStatus('current')
vtlDriveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 8), VtlDriveStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveStatus.setStatus('current')
vtlDriveTapeVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 2, 1, 1, 9), VtlDriveTapeVolumeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlDriveTapeVolume.setStatus('current')
vtlGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7))
vtlGroupTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1), )
if mibBuilder.loadTexts: vtlGroupTable.setStatus('current')
vtlGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlGroupIndex"))
if mibBuilder.loadTexts: vtlGroupEntry.setStatus('current')
vtlGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: vtlGroupIndex.setStatus('current')
vtlGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupName.setStatus('current')
vtlGroupInitiaterCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupInitiaterCount.setStatus('current')
vtlGroupDeviceCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceCount.setStatus('current')
vtlGroupDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2), )
if mibBuilder.loadTexts: vtlGroupDeviceTable.setStatus('current')
vtlGroupDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlGroupIndex"), (0, "DATA-DOMAIN-MIB", "vtlGroupDeviceIndex"))
if mibBuilder.loadTexts: vtlGroupDeviceEntry.setStatus('current')
vtlGroupDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 2), DDMibTableIndexTC())
if mibBuilder.loadTexts: vtlGroupDeviceIndex.setStatus('current')
vtlGroupDeviceGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 3), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceGroupName.setStatus('current')
vtlGroupDeviceDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 4), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceDeviceName.setStatus('current')
vtlGroupDeviceLun = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceLun.setStatus('current')
vtlGroupDevicePrimaryPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDevicePrimaryPorts.setStatus('current')
vtlGroupDeviceSecondaryPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceSecondaryPorts.setStatus('current')
vtlGroupDeviceInUsePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 7, 2, 1, 8), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlGroupDeviceInUsePorts.setStatus('current')
vtlInitiator = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8))
vtlInitiatorTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1), )
if mibBuilder.loadTexts: vtlInitiatorTable.setStatus('current')
vtlInitiatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlInitiatorIndex"))
if mibBuilder.loadTexts: vtlInitiatorEntry.setStatus('current')
vtlInitiatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: vtlInitiatorIndex.setStatus('current')
vtlInitiatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorName.setStatus('current')
vtlInitiatorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 3), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorStatus.setStatus('current')
vtlInitiatorGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorGroup.setStatus('current')
vtlInitiatorWWNN = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 5), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorWWNN.setStatus('current')
vtlInitiatorWWPN = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorWWPN.setStatus('current')
vtlInitiatorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 8, 1, 1, 7), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlInitiatorPort.setStatus('current')
vtlPool = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6))
vtlPoolTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1), )
if mibBuilder.loadTexts: vtlPoolTable.setStatus('current')
vtlPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlPoolIndex"))
if mibBuilder.loadTexts: vtlPoolEntry.setStatus('current')
vtlPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: vtlPoolIndex.setStatus('current')
vtlPoolPool = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolPool.setStatus('current')
vtlPoolStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolStatus.setStatus('current')
vtlPoolTapes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 4), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolTapes.setStatus('current')
vtlPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 5), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolSize.setStatus('current')
vtlPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolUsed.setStatus('current')
vtlPoolComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 6, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPoolComp.setStatus('current')
vtlPort = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3))
vtlPortTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1), )
if mibBuilder.loadTexts: vtlPortTable.setStatus('current')
vtlPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlPortIndex"))
if mibBuilder.loadTexts: vtlPortEntry.setStatus('current')
vtlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 1), VtlPortIndexTC())
if mibBuilder.loadTexts: vtlPortIndex.setStatus('current')
vtlPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 2), VtlPortNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortName.setStatus('current')
vtlPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 3), VtlPortIDTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortID.setStatus('current')
vtlPortModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 4), VtlPortModelTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortModel.setStatus('current')
vtlPortFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 5), VtlPortFirmwareTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortFirmware.setStatus('current')
vtlPortWWNN = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 6), VtlPortWWNNTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortWWNN.setStatus('current')
vtlPortWWPN = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 7), VtlPortWWPNTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortWWPN.setStatus('current')
vtlPortConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 8), VtlPortConnectionTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortConnectionType.setStatus('current')
vtlPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 9), VtlPortSpeedTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortSpeed.setStatus('current')
vtlPortEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 10), VtlPortEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortEnabled.setStatus('current')
vtlPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 11), VtlPortStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortStatus.setStatus('current')
vtlPortTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 3, 1, 1, 12), VtlPortIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlPortTrapIndex.setStatus('current')
vtlProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 1))
vtlAdminState = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 11, 1, 1), VtlAdminStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlAdminState.setStatus('current')
vtlProcessState = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 11, 1, 2), VtlProcessStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlProcessState.setStatus('current')
vtlStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3))
vtlStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1), )
if mibBuilder.loadTexts: vtlStatsTable.setStatus('current')
vtlStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlStatsIndex"))
if mibBuilder.loadTexts: vtlStatsEntry.setStatus('current')
vtlStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 1), VtlStatsIndexTC())
if mibBuilder.loadTexts: vtlStatsIndex.setStatus('current')
vtlStatsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 2), VtlStatsPortTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsPort.setStatus('current')
vtlStatsConrolCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 3), VtlStatsConrolCommandsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsConrolCommands.setStatus('current')
vtlStatsWriteCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 4), VtlStatsWriteCommandsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsWriteCommands.setStatus('current')
vtlStatsReadCommands = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 5), VtlStatsReadCommandsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsReadCommands.setStatus('current')
vtlStatsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 6), VtlStatsInTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsIn.setStatus('current')
vtlStatsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 7), VtlStatsOutTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsOut.setStatus('current')
vtlStatsLinkFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 8), VtlStatsLinkFailuresTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsLinkFailures.setStatus('current')
vtlStatsLIPCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 9), VtlStatsLIPCountTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsLIPCount.setStatus('current')
vtlStatsSyncLosses = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 10), VtlStatsSyncLossesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsSyncLosses.setStatus('current')
vtlStatsSignalLosses = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 11), VtlStatsSignalLossesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsSignalLosses.setStatus('current')
vtlStatsPrimSeqProtoErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 12), VtlStatsPrimSeqProtoErrorsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsPrimSeqProtoErrors.setStatus('current')
vtlStatsInvalidTxWords = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 13), VtlStatsInvalidTxWordsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsInvalidTxWords.setStatus('current')
vtlStatsInvalidCRCs = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 3, 1, 1, 14), VtlStatsInvalidCRCsTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlStatsInvalidCRCs.setStatus('current')
vtlTape = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4))
vtlTapeTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1), )
if mibBuilder.loadTexts: vtlTapeTable.setStatus('current')
vtlTapeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "vtlTapeIndex"))
if mibBuilder.loadTexts: vtlTapeEntry.setStatus('current')
vtlTapeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 1), VtlTapeIndexTC())
if mibBuilder.loadTexts: vtlTapeIndex.setStatus('current')
vtlTapeBarCode = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 2), VtlTapeBarCodeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeBarCode.setStatus('current')
vtlTapePool = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 3), VtlTapePoolTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapePool.setStatus('current')
vtlTapeLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 4), VtlTapeLocationTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeLocation.setStatus('current')
vtlTapeState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 5), VtlTapeStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeState.setStatus('current')
vtlTapeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 6), VtlTapeSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeSize.setStatus('current')
vtlTapeUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 7), VtlTapeUsedTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeUsed.setStatus('current')
vtlTapeComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 8), VtlTapeCompTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeComp.setStatus('current')
vtlTapeModTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 11, 2, 4, 1, 1, 9), VtlTapeModTimeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtlTapeModTime.setStatus('current')
ddboostAccessClients = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8))
ddboostAccessClientsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1), )
if mibBuilder.loadTexts: ddboostAccessClientsTable.setStatus('current')
ddboostAccessClientsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostAccessClientsIndex"))
if mibBuilder.loadTexts: ddboostAccessClientsEntry.setStatus('current')
ddboostAccessClientsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostAccessClientsIndex.setStatus('current')
ddboostAccessClientsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostAccessClientsName.setStatus('current')
ddboostAccessClientsEncryStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 3), DdboostAccessClientsEncryStrengthTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostAccessClientsEncryStrength.setStatus('current')
ddboostAccessClientsAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 8, 1, 1, 4), DdboostAccessClientsAuthModeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostAccessClientsAuthMode.setStatus('current')
ddboostConnections = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3))
ddboostConnectionsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1), )
if mibBuilder.loadTexts: ddboostConnectionsTable.setStatus('current')
ddboostConnectionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostConnectionsIndex"))
if mibBuilder.loadTexts: ddboostConnectionsEntry.setStatus('current')
ddboostConnectionsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostConnectionsIndex.setStatus('current')
ddboostInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostInterface.setStatus('current')
ddboostifGroupMember = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 3), DDMibTableEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostifGroupMember.setStatus('current')
ddboostBackupConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostBackupConnections.setStatus('current')
ddboostRestoreConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostRestoreConnections.setStatus('current')
ddboostControlConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 6), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostControlConnections.setStatus('current')
ddboostTotalConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 3, 1, 1, 7), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostTotalConnections.setStatus('current')
ddboostFileReplicationHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6))
ddboostFileReplicationHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1), )
if mibBuilder.loadTexts: ddboostFileReplicationHistoryTable.setStatus('current')
ddboostFileReplicationHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostFileReplHistoryIndex"))
if mibBuilder.loadTexts: ddboostFileReplicationHistoryEntry.setStatus('current')
ddboostFileReplHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostFileReplHistoryIndex.setStatus('current')
ddboostFileReplHistoryDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryDirection.setStatus('current')
ddboostFileReplHistoryNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 3), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryNetwork.setStatus('current')
ddboostFileReplHistoryPreComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 4), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryPreComp.setStatus('current')
ddboostFileReplHistoryPostComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 5), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryPostComp.setStatus('current')
ddboostFileReplHistoryLowBWOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 6), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryLowBWOpt.setStatus('current')
ddboostFileReplHistoryErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 7), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryErrors.setStatus('current')
ddboostFileReplHistoryDate = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 8), DDMibDateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryDate.setStatus('current')
ddboostFileReplHistoryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 6, 1, 1, 9), DDMibDateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplHistoryTime.setStatus('current')
ddboostFileReplicationStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5))
ddboostFileReplicationStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1), )
if mibBuilder.loadTexts: ddboostFileReplicationStatsTable.setStatus('current')
ddboostFileReplicationStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostFileReplStatsIndex"))
if mibBuilder.loadTexts: ddboostFileReplicationStatsEntry.setStatus('current')
ddboostFileReplStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostFileReplStatsIndex.setStatus('current')
ddboostFileReplStatsDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsDirection.setStatus('current')
ddboostFileReplStatsNetworkSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 3), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsNetworkSent.setStatus('current')
ddboostFileReplStatsPreCompSent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 4), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsPreCompSent.setStatus('current')
ddboostFileReplStatsFiltered = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 5), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsFiltered.setStatus('current')
ddboostFileReplStatsLowBWOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 6), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsLowBWOpt.setStatus('current')
ddboostFileReplStatsLocalComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 7), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsLocalComp.setStatus('current')
ddboostFileReplStatsCompRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 5, 1, 1, 8), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileReplStatsCompRatio.setStatus('current')
ddboostFileReplicationPerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 10))
ddboostFileRepliPerfInPreCompKBPerSec = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 1), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileRepliPerfInPreCompKBPerSec.setStatus('current')
ddboostFileRepliPerfInNetworkKBPerSec = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 2), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileRepliPerfInNetworkKBPerSec.setStatus('current')
ddboostFileRepliPerfOutPreCompKBPerSec = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileRepliPerfOutPreCompKBPerSec.setStatus('current')
ddboostFileRepliPerfOutNetworkKBPerSec = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 10, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostFileRepliPerfOutNetworkKBPerSec.setStatus('current')
ddboostIfGroupConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 7))
ddboostIfGroupConfigTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1), )
if mibBuilder.loadTexts: ddboostIfGroupConfigTable.setStatus('current')
ddboostIfGroupConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostIfGroupConfigIndex"))
if mibBuilder.loadTexts: ddboostIfGroupConfigEntry.setStatus('current')
ddboostIfGroupConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostIfGroupConfigIndex.setStatus('current')
ddboostIfGroupInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 7, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostIfGroupInterface.setStatus('current')
ddboostOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9))
ddboostOptionsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1), )
if mibBuilder.loadTexts: ddboostOptionsTable.setStatus('current')
ddboostOptionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostOptionsIndex"))
if mibBuilder.loadTexts: ddboostOptionsEntry.setStatus('current')
ddboostOptionsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostOptionsIndex.setStatus('current')
ddboostOptionsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostOptionsName.setStatus('current')
ddboostOptionsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 9, 1, 1, 3), DDMibStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostOptionsStatus.setStatus('current')
ddboostProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1))
ddboostStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 1), DDboostStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatus.setStatus('current')
ddboostUser = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 2), DDboostUserTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostUser.setStatus('deprecated')
ddboostIfGroupStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 3), DDMibStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostIfGroupStatus.setStatus('deprecated')
ddboostUserTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4), )
if mibBuilder.loadTexts: ddboostUserTable.setStatus('current')
ddboostUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostUserIdx"))
if mibBuilder.loadTexts: ddboostUserEntry.setStatus('current')
ddboostUserIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1, 1), DDboostStatsIndexTC())
if mibBuilder.loadTexts: ddboostUserIdx.setStatus('current')
ddboostUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostUserName.setStatus('current')
ddboostUserDefaultTenantUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 4, 1, 3), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostUserDefaultTenantUnit.setStatus('current')
ddboostIfGroupTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5), )
if mibBuilder.loadTexts: ddboostIfGroupTable.setStatus('current')
ddboostIfGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostIfGroupIdx"))
if mibBuilder.loadTexts: ddboostIfGroupEntry.setStatus('current')
ddboostIfGroupIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1, 1), DDboostStatsIndexTC())
if mibBuilder.loadTexts: ddboostIfGroupIdx.setStatus('current')
ddboostIfGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostIfGroupName.setStatus('current')
ddboostIfGroupCurrentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 1, 5, 1, 3), DDMibStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostIfGroupCurrentStatus.setStatus('current')
ddboostStats = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2))
ddboostStatsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1), )
if mibBuilder.loadTexts: ddboostStatsTable.setStatus('current')
ddboostStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostStatsIndex"))
if mibBuilder.loadTexts: ddboostStatsEntry.setStatus('current')
ddboostStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 1), DDboostStatsIndexTC())
if mibBuilder.loadTexts: ddboostStatsIndex.setStatus('current')
ddboostPreCompKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 2), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostPreCompKBytesPerSecond.setStatus('current')
ddboostPostCompKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 3), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostPostCompKBytesPerSecond.setStatus('current')
ddboostNetworkKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 4), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostNetworkKBytesPerSecond.setStatus('current')
ddboostReadKBytesPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 5), KBytesPerSecond()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostReadKBytesPerSecond.setStatus('current')
ddboostStatsBackupConn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsBackupConn.setStatus('current')
ddboostStatsRestoreConn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsRestoreConn.setStatus('current')
ddboostStatsImageCreatesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsImageCreatesCount.setStatus('current')
ddboostStatsImageCreatesErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsImageCreatesErrors.setStatus('current')
ddboostStatsImageDeletesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsImageDeletesCount.setStatus('current')
ddboostStatsImageDeletesErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsImageDeletesErrors.setStatus('current')
ddboostStatsPrecompBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 12), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsPrecompBytesReceived.setStatus('current')
ddboostStatsBytesAfterFiltering = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 13), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsBytesAfterFiltering.setStatus('current')
ddboostStatsBytesAfterLc = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 14), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsBytesAfterLc.setStatus('current')
ddboostStatsNetworkBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 15), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsNetworkBytesReceived.setStatus('current')
ddboostStatsCompressionRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 16), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsCompressionRatio.setStatus('current')
ddboostStatsTotalBytesReadCount = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 17), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsTotalBytesReadCount.setStatus('current')
ddboostStatsTotalBytesReadErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 2, 1, 1, 18), DDMibTrafficBytesTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStatsTotalBytesReadErrors.setStatus('current')
ddboostStorageUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4))
ddboostStorageUnitTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1), )
if mibBuilder.loadTexts: ddboostStorageUnitTable.setStatus('current')
ddboostStorageUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "ddboostStorageUnitIndex"))
if mibBuilder.loadTexts: ddboostStorageUnitEntry.setStatus('current')
ddboostStorageUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: ddboostStorageUnitIndex.setStatus('current')
ddboostStorageUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitName.setStatus('current')
ddboostStorageUnitBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitBytes.setStatus('current')
ddboostStorageUnitGlobalComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitGlobalComp.setStatus('current')
ddboostStorageUnitLocalComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitLocalComp.setStatus('current')
ddboostStorageUnitMetaData = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 6), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitMetaData.setStatus('current')
ddboostStorageUnitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitStatus.setStatus('current')
ddboostStorageUnitPreComp = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 8), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitPreComp.setStatus('current')
ddboostStorageUnitUser = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 9), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitUser.setStatus('current')
ddboostStorageUnitReportPhysicalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 12, 4, 1, 1, 10), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddboostStorageUnitReportPhysicalSize.setStatus('current')
systemLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4))
systemLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1), )
if mibBuilder.loadTexts: systemLicenseTable.setStatus('current')
systemLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemLicenseIndex"))
if mibBuilder.loadTexts: systemLicenseEntry.setStatus('current')
systemLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemLicenseIndex.setStatus('current')
systemLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemLicenseKey.setStatus('current')
systemLicenseFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemLicenseFeature.setStatus('current')
systemCapacityLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2))
systemCapacityLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1), )
if mibBuilder.loadTexts: systemCapacityLicenseTable.setStatus('current')
systemCapacityLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemCapacityLicenseIndex"))
if mibBuilder.loadTexts: systemCapacityLicenseEntry.setStatus('current')
systemCapacityLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemCapacityLicenseIndex.setStatus('current')
systemCapacityLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemCapacityLicenseKey.setStatus('current')
systemCapacityLicenseFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemCapacityLicenseFeature.setStatus('current')
systemCapacityLicenseModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemCapacityLicenseModel.setStatus('current')
systemCapacityLicenseCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 4, 2, 1, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemCapacityLicenseCapacity.setStatus('current')
systemHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2))
systemHardwareTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1), )
if mibBuilder.loadTexts: systemHardwareTable.setStatus('current')
systemHardwareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemHardwareIndex"))
if mibBuilder.loadTexts: systemHardwareEntry.setStatus('current')
systemHardwareIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemHardwareIndex.setStatus('current')
systemHardwareSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 2), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwareSlot.setStatus('deprecated')
systemHardwareVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwareVendor.setStatus('current')
systemHardwareDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 4), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwareDevice.setStatus('current')
systemHardwarePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 5), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwarePorts.setStatus('current')
systemHardwareSlotName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwareSlotName.setStatus('current')
systemPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3))
systemPortsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1), )
if mibBuilder.loadTexts: systemPortsTable.setStatus('current')
systemPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemPortsIndex"))
if mibBuilder.loadTexts: systemPortsEntry.setStatus('current')
systemPortsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemPortsIndex.setStatus('current')
systemPortsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemPortsPort.setStatus('current')
systemPortsConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemPortsConnectionType.setStatus('current')
systemPortsLinkSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 4), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemPortsLinkSpeed.setStatus('current')
systemPortsFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 5), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemPortsFirmware.setStatus('current')
systemPortsHardwareAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 3, 1, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemPortsHardwareAddress.setStatus('current')
systemProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1))
systemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 1), SystemSerialNumberTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSerialNumber.setStatus('current')
systemCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 2), DDMibTimeStampTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemCurrentTime.setStatus('current')
systemVersion = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 3), DDMibVersionTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemVersion.setStatus('current')
systemModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 4), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemModelNumber.setStatus('current')
systemTimeZoneName = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 5), SystemTimeZoneNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTimeZoneName.setStatus('current')
sysNotes = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 13, 1, 6), SystemNotesTC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNotes.setStatus('current')
systemUser = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5))
systemUserTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1), )
if mibBuilder.loadTexts: systemUserTable.setStatus('current')
systemUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemUserIndex"))
if mibBuilder.loadTexts: systemUserEntry.setStatus('current')
systemUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemUserIndex.setStatus('current')
systemUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 2), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUserName.setStatus('current')
systemUserUID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUserUID.setStatus('current')
systemUserRole = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUserRole.setStatus('current')
systemUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 1, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUserStatus.setStatus('current')
systemActiveUserTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2), )
if mibBuilder.loadTexts: systemActiveUserTable.setStatus('current')
systemActiveUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "systemActiveUserIndex"))
if mibBuilder.loadTexts: systemActiveUserEntry.setStatus('current')
systemActiveUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: systemActiveUserIndex.setStatus('current')
systemActiveUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 2), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemActiveUserName.setStatus('current')
systemActiveUserIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 3), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemActiveUserIdleTime.setStatus('current')
systemActiveUserLoginTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemActiveUserLoginTime.setStatus('current')
systemActiveUserLoginFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemActiveUserLoginFrom.setStatus('current')
systemActiveUserTty = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 13, 5, 2, 1, 6), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemActiveUserTty.setStatus('current')
taskHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2))
taskHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1), )
if mibBuilder.loadTexts: taskHistoryTable.setStatus('current')
taskHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "taskHistoryIndex"))
if mibBuilder.loadTexts: taskHistoryEntry.setStatus('current')
taskHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: taskHistoryIndex.setStatus('current')
taskHistoryUser = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryUser.setStatus('current')
taskHistoryID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryID.setStatus('current')
taskHistoryParent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 4), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryParent.setStatus('current')
taskHistoryName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 5), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryName.setStatus('current')
taskHistoryState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryState.setStatus('current')
taskHistoryStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryStartTime.setStatus('current')
taskHistoryDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 2, 1, 1, 8), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskHistoryDuration.setStatus('current')
taskActive = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3))
taskActiveTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1), )
if mibBuilder.loadTexts: taskActiveTable.setStatus('current')
taskActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "taskActiveIndex"))
if mibBuilder.loadTexts: taskActiveEntry.setStatus('current')
taskActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: taskActiveIndex.setStatus('current')
taskActiveUser = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 2), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveUser.setStatus('current')
taskActiveID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveID.setStatus('current')
taskActiveParent = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 4), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveParent.setStatus('current')
taskActiveName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 5), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveName.setStatus('current')
taskActiveState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 6), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveState.setStatus('current')
taskActiveStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveStartTime.setStatus('current')
taskActiveDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 3, 1, 1, 8), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: taskActiveDuration.setStatus('current')
artConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1))
artConfigTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1), )
if mibBuilder.loadTexts: artConfigTable.setStatus('current')
artConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "artConfigIndex"))
if mibBuilder.loadTexts: artConfigEntry.setStatus('current')
artConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: artConfigIndex.setStatus('current')
artConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 2), DDMibTableEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artConfigStatus.setStatus('current')
artConfigMigrationSchedule = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 3), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artConfigMigrationSchedule.setStatus('current')
artConfigDefaultAge = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artConfigDefaultAge.setStatus('current')
artConfigFileSystemClean = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 5), DDMibTableEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artConfigFileSystemClean.setStatus('current')
artConfigCompression = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 1, 1, 1, 6), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artConfigCompression.setStatus('current')
artMigrationPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3))
artMigrationPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1), )
if mibBuilder.loadTexts: artMigrationPolicyTable.setStatus('current')
artMigrationPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "artMigrationPolicyIndex"))
if mibBuilder.loadTexts: artMigrationPolicyEntry.setStatus('current')
artMigrationPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: artMigrationPolicyIndex.setStatus('current')
artMigrationPolicyMtreeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artMigrationPolicyMtreeName.setStatus('current')
artMigrationPolicyDefaultAge = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 3, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artMigrationPolicyDefaultAge.setStatus('current')
artMigrationSchedule = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2))
artMigrationScheduleTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1), )
if mibBuilder.loadTexts: artMigrationScheduleTable.setStatus('current')
artMigrationScheduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "artMigrationScheduleIndex"))
if mibBuilder.loadTexts: artMigrationScheduleEntry.setStatus('current')
artMigrationScheduleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: artMigrationScheduleIndex.setStatus('current')
artMigrationScheduleSchedule = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artMigrationScheduleSchedule.setStatus('current')
artMigrationScheduleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 14, 2, 1, 1, 3), DDMibStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: artMigrationScheduleStatus.setStatus('current')
mtreeCompression = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1))
mtreeCompressionTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1), )
if mibBuilder.loadTexts: mtreeCompressionTable.setStatus('current')
mtreeCompressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "mtreeCompressionIndex"))
if mibBuilder.loadTexts: mtreeCompressionEntry.setStatus('current')
mtreeCompressionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: mtreeCompressionIndex.setStatus('current')
mtreeCompressionMtreePath = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionMtreePath.setStatus('current')
mtreeCompressionPreCompGib = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 3), DDMibTableSizeGibTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionPreCompGib.setStatus('current')
mtreeCompressionPostCompGib = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 4), DDMibTableSizeGibTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionPostCompGib.setStatus('current')
mtreeCompressionGlobalCompFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 5), DDMibCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionGlobalCompFactor.setStatus('current')
mtreeCompressionLocalCompFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 6), DDMibCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionLocalCompFactor.setStatus('current')
mtreeCompressionPostTotalCompFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 7), DDMibCompressionFactorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionPostTotalCompFactor.setStatus('current')
mtreeCompressionTimePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 1, 1, 1, 8), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeCompressionTimePeriod.setStatus('current')
mtreeList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2))
mtreeListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1), )
if mibBuilder.loadTexts: mtreeListTable.setStatus('current')
mtreeListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "mtreeListIndex"))
if mibBuilder.loadTexts: mtreeListEntry.setStatus('current')
mtreeListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: mtreeListIndex.setStatus('current')
mtreeListMtreeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeListMtreeName.setStatus('current')
mtreeListPreCompGib = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 3), DDMibTableSizeGibTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeListPreCompGib.setStatus('current')
mtreeListStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 2, 1, 1, 4), MtreeListStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeListStatus.setStatus('current')
mtreeRetentionLock = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4))
mtreeRetentionLockTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1), )
if mibBuilder.loadTexts: mtreeRetentionLockTable.setStatus('current')
mtreeRetentionLockEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "mtreeRetentionLockIndex"))
if mibBuilder.loadTexts: mtreeRetentionLockEntry.setStatus('current')
mtreeRetentionLockIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: mtreeRetentionLockIndex.setStatus('current')
mtreeRetentionLockMtreeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeRetentionLockMtreeName.setStatus('current')
mtreeRetentionLockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 3), MtreeRetentionLockStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeRetentionLockStatus.setStatus('current')
mtreeRetentionLockUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeRetentionLockUUID.setStatus('current')
mtreeRetentionLockMinRetentionPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeRetentionLockMinRetentionPeriod.setStatus('current')
mtreeRetentionLockMaxRetentionPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 15, 4, 1, 1, 6), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtreeRetentionLockMaxRetentionPeriod.setStatus('current')
enclosureList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1))
enclosureListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1), )
if mibBuilder.loadTexts: enclosureListTable.setStatus('current')
enclosureListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "enclosureListIndex"))
if mibBuilder.loadTexts: enclosureListEntry.setStatus('current')
enclosureListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: enclosureListIndex.setStatus('current')
enclosureListNum = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 2), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListNum.setStatus('current')
enclosureListModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 3), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListModel.setStatus('current')
enclosureListSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 4), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListSerialNum.setStatus('current')
enclosureListOemName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 5), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListOemName.setStatus('current')
enclosureListOemValue = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 6), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListOemValue.setStatus('current')
enclosureListCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 1, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosureListCapacity.setStatus('current')
enclosurePack = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 17, 2))
enclosurePackTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 17, 2, 1), )
if mibBuilder.loadTexts: enclosurePackTable.setStatus('current')
enclosurePackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 17, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "enclosureListIndex"), (0, "DATA-DOMAIN-MIB", "enclosurePackID"))
if mibBuilder.loadTexts: enclosurePackEntry.setStatus('current')
enclosurePackID = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 17, 2, 1, 1, 1), DDMibTableIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enclosurePackID.setStatus('current')
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
dnsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 18, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "dnsIndex"))
if mibBuilder.loadTexts: dnsEntry.setStatus('current')
dnsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 1, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: dnsIndex.setStatus('current')
dnsServer = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 1, 1, 1, 2), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServer.setStatus('current')
searchDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 18, 2))
searchDomainsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1), )
if mibBuilder.loadTexts: searchDomainsTable.setStatus('current')
searchDomainsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "searchDomainsIndex"))
if mibBuilder.loadTexts: searchDomainsEntry.setStatus('current')
searchDomainsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: searchDomainsIndex.setStatus('current')
searchDomainsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 2, 1, 1, 2), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: searchDomainsName.setStatus('current')
snmpTrapHosts = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3))
snmpTrapHostsTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1), )
if mibBuilder.loadTexts: snmpTrapHostsTable.setStatus('current')
snmpTrapHostsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "snmpTrapHostsIndex"))
if mibBuilder.loadTexts: snmpTrapHostsEntry.setStatus('current')
snmpTrapHostsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: snmpTrapHostsIndex.setStatus('current')
snmpTrapHostsName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTrapHostsName.setStatus('current')
snmpTrapHostsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 18, 3, 1, 1, 3), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTrapHostsVersion.setStatus('current')
nis = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4))
nisDomain = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 1), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisDomain.setStatus('current')
nisServers = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 2), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisServers.setStatus('current')
nisAdminGroups = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 3), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisAdminGroups.setStatus('current')
nisUserGroups = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 4), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisUserGroups.setStatus('current')
nisBackupOperatorGroups = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 5), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisBackupOperatorGroups.setStatus('current')
nisEnabled = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 6), DDMibTableEnabledTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisEnabled.setStatus('current')
nisStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 18, 4, 7), DDMibTableString1024TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nisStatus.setStatus('current')
managedSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1))
managedSystemTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1), )
if mibBuilder.loadTexts: managedSystemTable.setStatus('current')
managedSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "managedSystemIndex"))
if mibBuilder.loadTexts: managedSystemEntry.setStatus('current')
managedSystemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: managedSystemIndex.setStatus('current')
managedSystemHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemHostname.setStatus('current')
managedSystemSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 3), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemSerial.setStatus('current')
managedSystemState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 4), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemState.setStatus('current')
managedSystemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 5), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemStatus.setStatus('current')
managedSystemDDOSVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 6), DDMibTableString32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemDDOSVersion.setStatus('current')
managedSystemHDSyncTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 7), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemHDSyncTime.setStatus('current')
managedSystemCDSyncTime = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 19, 1, 1, 1, 8), DDMibTableString64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managedSystemCDSyncTime.setStatus('current')
smtProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 1))
smtStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 20, 1, 1), SmtStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smtStatus.setStatus('current')
tenantUnitList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2))
tenantUnitListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1), )
if mibBuilder.loadTexts: tenantUnitListTable.setStatus('current')
tenantUnitListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"))
if mibBuilder.loadTexts: tenantUnitListEntry.setStatus('current')
tenantUnitListIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: tenantUnitListIdx.setStatus('current')
tenantUnitListName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 2), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListName.setStatus('current')
tenantUnitListNumberOfMgmtUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 3), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListNumberOfMgmtUsers.setStatus('current')
tenantUnitListNumberOfMtrees = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 4), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListNumberOfMtrees.setStatus('current')
tenantUnitListNumberOfDdboostStus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListNumberOfDdboostStus.setStatus('current')
tenantUnitListTenantSelfServiceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 6), SmtStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListTenantSelfServiceMode.setStatus('current')
tenantUnitListParentTenantName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 7), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListParentTenantName.setStatus('current')
tenantUnitListType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 8), DDMibTableString256TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListType.setStatus('current')
tenantUnitListSecurityMode = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 9), TenantUnitSecurityModeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListSecurityMode.setStatus('current')
tenantUnitListNumberOfMgmtGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 2, 1, 1, 10), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitListNumberOfMgmtGroups.setStatus('current')
tenantUnitMgmtUserList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 3))
tenantUnitMgmtUserListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1), )
if mibBuilder.loadTexts: tenantUnitMgmtUserListTable.setStatus('current')
tenantUnitMgmtUserListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"), (0, "DATA-DOMAIN-MIB", "tenantUnitMgmtUserListUserName"))
if mibBuilder.loadTexts: tenantUnitMgmtUserListEntry.setStatus('current')
tenantUnitMgmtUserListUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1, 1, 2), DDMibString96TC())
if mibBuilder.loadTexts: tenantUnitMgmtUserListUserName.setStatus('current')
tenantUnitMgmtUserListUserRole = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 3, 1, 1, 3), TenantUnitMgmtUserListUserRoleTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitMgmtUserListUserRole.setStatus('current')
tenantUnitMtreeList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 4))
tenantUnitMtreeListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 4, 1), )
if mibBuilder.loadTexts: tenantUnitMtreeListTable.setStatus('current')
tenantUnitMtreeListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"), (0, "DATA-DOMAIN-MIB", "tenantUnitMtreeListMtreeName"))
if mibBuilder.loadTexts: tenantUnitMtreeListEntry.setStatus('current')
tenantUnitMtreeListMtreeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 4, 1, 1, 2), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitMtreeListMtreeName.setStatus('current')
tenantUnitDdboostStuList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 5))
tenantUnitDdboostStuListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 5, 1), )
if mibBuilder.loadTexts: tenantUnitDdboostStuListTable.setStatus('current')
tenantUnitDdboostStuListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"), (0, "DATA-DOMAIN-MIB", "tenantUnitDdboostStuListStuName"))
if mibBuilder.loadTexts: tenantUnitDdboostStuListEntry.setStatus('current')
tenantUnitDdboostStuListStuName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 5, 1, 1, 2), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitDdboostStuListStuName.setStatus('current')
tenantUnitAdminIpInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 6))
tenantUnitAdminIpInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1), )
if mibBuilder.loadTexts: tenantUnitAdminIpInfoTable.setStatus('current')
tenantUnitAdminIpInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"), (0, "DATA-DOMAIN-MIB", "tenantUnitAdminIpInfoAddr"))
if mibBuilder.loadTexts: tenantUnitAdminIpInfoEntry.setStatus('current')
tenantUnitAdminIpInfoAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1, 1, 2), DDMibString96TC())
if mibBuilder.loadTexts: tenantUnitAdminIpInfoAddr.setStatus('current')
tenantUnitAdminIpInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 6, 1, 1, 3), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitAdminIpInfoType.setStatus('current')
tenantInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7))
tenantInfoTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1), )
if mibBuilder.loadTexts: tenantInfoTable.setStatus('current')
tenantInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantInfoIdx"))
if mibBuilder.loadTexts: tenantInfoEntry.setStatus('current')
tenantInfoIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: tenantInfoIdx.setStatus('current')
tenantInfoTenantName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 1, 1, 2), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantInfoTenantName.setStatus('current')
tenantInfoTenantUnitTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 2), )
if mibBuilder.loadTexts: tenantInfoTenantUnitTable.setStatus('current')
tenantInfoTenantUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantInfoIdx"), (0, "DATA-DOMAIN-MIB", "tenantInfoTenantUnitName"))
if mibBuilder.loadTexts: tenantInfoTenantUnitEntry.setStatus('current')
tenantInfoTenantUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 7, 2, 1, 2), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantInfoTenantUnitName.setStatus('current')
tenantUnitMgmtGroupList = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8))
tenantUnitMgmtGroupListTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1), )
if mibBuilder.loadTexts: tenantUnitMgmtGroupListTable.setStatus('current')
tenantUnitMgmtGroupListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "tenantUnitListIdx"), (0, "DATA-DOMAIN-MIB", "tenantUnitMgmtGroupListGroupName"))
if mibBuilder.loadTexts: tenantUnitMgmtGroupListEntry.setStatus('current')
tenantUnitMgmtGroupListGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1, 2), DDMibString96TC())
if mibBuilder.loadTexts: tenantUnitMgmtGroupListGroupName.setStatus('current')
tenantUnitMgmtGroupListGroupRole = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1, 3), TenantUnitMgmtUserListUserRoleTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitMgmtGroupListGroupRole.setStatus('current')
tenantUnitMgmtGroupListGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 20, 8, 1, 1, 4), TenantUnitMgmtGroupTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tenantUnitMgmtGroupListGroupType.setStatus('current')
quotaProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 21, 1))
quotaCapacityStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 21, 1, 1), DDStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacityStatus.setStatus('current')
quotaCapacity = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2))
quotaCapacityTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1), )
if mibBuilder.loadTexts: quotaCapacityTable.setStatus('current')
quotaCapacityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "quotaCapacityIndex"))
if mibBuilder.loadTexts: quotaCapacityEntry.setStatus('current')
quotaCapacityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: quotaCapacityIndex.setStatus('current')
quotaCapacityMtreeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacityMtreeName.setStatus('current')
quotaCapacityPreCompMiB = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 3), DDMibTableSizeMiBTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacityPreCompMiB.setStatus('current')
quotaCapacitySoftLimitMiB = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 4), DDMibTableSizeMiBTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacitySoftLimitMiB.setStatus('current')
quotaCapacityHardLimitMiB = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 5), DDMibTableSizeMiBTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacityHardLimitMiB.setStatus('current')
quotaCapacityTenantUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 21, 2, 1, 1, 6), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quotaCapacityTenantUnit.setStatus('current')
highAvailabilityStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1))
haSystemName = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 1), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haSystemName.setStatus('current')
haSystemStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 2), HaSystemStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haSystemStatus.setStatus('current')
haInterconnectStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 3), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haInterconnectStatus.setStatus('current')
haPrimaryHeartbeatStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 4), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haPrimaryHeartbeatStatus.setStatus('current')
haExternalLanHeartbeatStatus = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 5), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haExternalLanHeartbeatStatus.setStatus('current')
haHardwareCompatibilityCheck = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 6), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haHardwareCompatibilityCheck.setStatus('current')
haSoftwareVersionCheck = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 22, 1, 7), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haSoftwareVersionCheck.setStatus('current')
highAvailabilityNode = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2))
highAvailabilityNodeTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1), )
if mibBuilder.loadTexts: highAvailabilityNodeTable.setStatus('current')
highAvailabilityNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "highAvailabilityNodeIdx"))
if mibBuilder.loadTexts: highAvailabilityNodeEntry.setStatus('current')
highAvailabilityNodeIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: highAvailabilityNodeIdx.setStatus('current')
highAvailabilityNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 2), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityNodeName.setStatus('current')
highAvailabilityNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 3), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityNodeId.setStatus('current')
highAvailabilityNodeRole = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 4), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityNodeRole.setStatus('current')
highAvailabilityNodeState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 5), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityNodeState.setStatus('current')
highAvailabilityNodeHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 2, 1, 1, 6), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityNodeHealth.setStatus('current')
highAvailabilityComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3))
highAvailabilityComponentTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3, 1), )
if mibBuilder.loadTexts: highAvailabilityComponentTable.setStatus('current')
highAvailabilityComponentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "highAvailabilityComponentIdx"))
if mibBuilder.loadTexts: highAvailabilityComponentEntry.setStatus('current')
highAvailabilityComponentIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: highAvailabilityComponentIdx.setStatus('current')
highAvailabilityComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3, 1, 1, 2), DDMibTableString128TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityComponentName.setStatus('current')
highAvailabilityComponentState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 22, 3, 1, 1, 3), HaStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityComponentState.setStatus('current')
scsitargetProperties = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 1))
scsitargetAdminState = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 23, 1, 1), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetAdminState.setStatus('current')
scsitargetProcessState = MibScalar((1, 3, 6, 1, 4, 1, 19746, 1, 23, 1, 2), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetProcessState.setStatus('current')
scsitargetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2))
scsitargetGroupTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1), )
if mibBuilder.loadTexts: scsitargetGroupTable.setStatus('current')
scsitargetGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetGroupIndex"))
if mibBuilder.loadTexts: scsitargetGroupEntry.setStatus('current')
scsitargetGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetGroupIndex.setStatus('current')
scsitargetGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetGroupName.setStatus('current')
scsitargetGroupService = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetGroupService.setStatus('current')
scsitargetGroupActiveState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 4), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetGroupActiveState.setStatus('current')
scsitargetGroupNumInitiators = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 5), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetGroupNumInitiators.setStatus('current')
scsitargetGroupNumDevices = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 2, 1, 1, 6), DDMibInteger32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetGroupNumDevices.setStatus('current')
scsitargetInitiator = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3))
scsitargetInitiatorTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1), )
if mibBuilder.loadTexts: scsitargetInitiatorTable.setStatus('current')
scsitargetInitiatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetInitiatorIndex"))
if mibBuilder.loadTexts: scsitargetInitiatorEntry.setStatus('current')
scsitargetInitiatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetInitiatorIndex.setStatus('current')
scsitargetInitiatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorName.setStatus('current')
scsitargetInitiatorSystemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorSystemAddress.setStatus('current')
scsitargetInitiatorGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 4), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorGroup.setStatus('current')
scsitargetInitiatorService = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 5), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorService.setStatus('current')
scsitargetInitiatorAddressMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 6), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorAddressMethod.setStatus('current')
scsitargetInitiatorTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 7), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorTransport.setStatus('current')
scsitargetInitiatorFcWwpn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 8), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorFcWwpn.setStatus('current')
scsitargetInitiatorFcWwnn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 9), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorFcWwnn.setStatus('current')
scsitargetInitiatorFcSymbolicPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 1, 1, 10), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorFcSymbolicPortName.setStatus('current')
scsitargetInitiatorEndpTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2), )
if mibBuilder.loadTexts: scsitargetInitiatorEndpTable.setStatus('current')
scsitargetInitiatorEndpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetInitiatorEndpIndex"))
if mibBuilder.loadTexts: scsitargetInitiatorEndpEntry.setStatus('current')
scsitargetInitiatorEndpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetInitiatorEndpIndex.setStatus('current')
scsitargetInitiatorEndpInitiator = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorEndpInitiator.setStatus('current')
scsitargetInitiatorEndpEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorEndpEndpoint.setStatus('current')
scsitargetInitiatorEndpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 3, 2, 1, 4), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetInitiatorEndpStatus.setStatus('current')
scsitargetEndpoint = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4))
scsitargetEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1), )
if mibBuilder.loadTexts: scsitargetEndpointTable.setStatus('current')
scsitargetEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetEndpointIndex"))
if mibBuilder.loadTexts: scsitargetEndpointEntry.setStatus('current')
scsitargetEndpointIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetEndpointIndex.setStatus('current')
scsitargetEndpointName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointName.setStatus('current')
scsitargetEndpointCurrentSystemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointCurrentSystemAddress.setStatus('current')
scsitargetEndpointPrimarySystemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 4), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointPrimarySystemAddress.setStatus('current')
scsitargetEndpointSecondarySystemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 5), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointSecondarySystemAddress.setStatus('current')
scsitargetEndpointEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 6), DDStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointEnabled.setStatus('current')
scsitargetEndpointStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 7), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointStatus.setStatus('current')
scsitargetEndpointTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 8), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointTransport.setStatus('current')
scsitargetEndpointFcWwnn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 9), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointFcWwnn.setStatus('current')
scsitargetEndpointFcWwpn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 4, 1, 1, 10), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetEndpointFcWwpn.setStatus('current')
scsitargetPort = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5))
scsitargetPortTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1), )
if mibBuilder.loadTexts: scsitargetPortTable.setStatus('current')
scsitargetPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetPortIndex"))
if mibBuilder.loadTexts: scsitargetPortEntry.setStatus('current')
scsitargetPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetPortIndex.setStatus('current')
scsitargetPortSystemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortSystemAddress.setStatus('current')
scsitargetPortEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 3), DDStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEnabled.setStatus('current')
scsitargetPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 4), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortStatus.setStatus('current')
scsitargetPortTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 5), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortTransport.setStatus('current')
scsitargetPortOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 6), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortOperationalStatus.setStatus('current')
scsitargetPortFcNpiv = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 7), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcNpiv.setStatus('current')
scsitargetPortPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 8), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortPortId.setStatus('current')
scsitargetPortModel = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 9), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortModel.setStatus('current')
scsitargetPortFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 10), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFirmware.setStatus('current')
scsitargetPortFcBaseWwnn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 11), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcBaseWwnn.setStatus('current')
scsitargetPortFcBaseWwpn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 12), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcBaseWwpn.setStatus('current')
scsitargetPortFcCurrentWwnn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 13), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcCurrentWwnn.setStatus('current')
scsitargetPortFcCurrentWwpn = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 14), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcCurrentWwpn.setStatus('current')
scsitargetPortFcp2Retry = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 15), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcp2Retry.setStatus('current')
scsitargetPortConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 16), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortConnectionType.setStatus('current')
scsitargetPortLinkSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 17), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortLinkSpeed.setStatus('current')
scsitargetPortFcTopology = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 1, 1, 18), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortFcTopology.setStatus('current')
scsitargetPortEndpTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2), )
if mibBuilder.loadTexts: scsitargetPortEndpTable.setStatus('current')
scsitargetPortEndpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetPortEndpIndex"))
if mibBuilder.loadTexts: scsitargetPortEndpEntry.setStatus('current')
scsitargetPortEndpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetPortEndpIndex.setStatus('current')
scsitargetPortEndpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEndpPort.setStatus('current')
scsitargetPortEndpEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEndpEndpoint.setStatus('current')
scsitargetPortEndpEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 4), DDStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEndpEnabled.setStatus('current')
scsitargetPortEndpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 5), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEndpStatus.setStatus('current')
scsitargetPortEndpCurrentInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 5, 2, 1, 6), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetPortEndpCurrentInstance.setStatus('current')
scsitargetDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6))
scsitargetDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1), )
if mibBuilder.loadTexts: scsitargetDeviceTable.setStatus('current')
scsitargetDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetDeviceIndex"))
if mibBuilder.loadTexts: scsitargetDeviceEntry.setStatus('current')
scsitargetDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetDeviceIndex.setStatus('current')
scsitargetDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceName.setStatus('current')
scsitargetDeviceService = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceService.setStatus('current')
scsitargetDeviceActiveState = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 4), DDMibString96TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceActiveState.setStatus('current')
scsitargetDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 1, 1, 5), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceAddress.setStatus('current')
scsitargetDeviceGrpTable = MibTable((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2), )
if mibBuilder.loadTexts: scsitargetDeviceGrpTable.setStatus('current')
scsitargetDeviceGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1), ).setIndexNames((0, "DATA-DOMAIN-MIB", "scsitargetDeviceGrpIndex"))
if mibBuilder.loadTexts: scsitargetDeviceGrpEntry.setStatus('current')
scsitargetDeviceGrpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 1), DDMibTableIndexTC())
if mibBuilder.loadTexts: scsitargetDeviceGrpIndex.setStatus('current')
scsitargetDeviceGrpDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 2), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpDevice.setStatus('current')
scsitargetDeviceGrpGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 3), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpGroupName.setStatus('current')
scsitargetDeviceGrpLun = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 4), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpLun.setStatus('current')
scsitargetDeviceGrpPrimaryEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 5), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpPrimaryEndpoints.setStatus('current')
scsitargetDeviceGrpSecondaryEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 6), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpSecondaryEndpoints.setStatus('current')
scsitargetDeviceGrpInUseEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 19746, 1, 23, 6, 2, 1, 7), DDMibTableString512TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scsitargetDeviceGrpInUseEndpoints.setStatus('current')
dataDomainMibTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 2, 0))
powerSupplyFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 1))
if mibBuilder.loadTexts: powerSupplyFailedAlarm.setStatus('deprecated')
systemOverheatWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 2)).setObjects(("DATA-DOMAIN-MIB", "tempSensorDescription"))
if mibBuilder.loadTexts: systemOverheatWarningAlarm.setStatus('deprecated')
systemOverheatAlertAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 3)).setObjects(("DATA-DOMAIN-MIB", "tempSensorDescription"))
if mibBuilder.loadTexts: systemOverheatAlertAlarm.setStatus('deprecated')
systemOverheatShutdownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 4)).setObjects(("DATA-DOMAIN-MIB", "tempSensorDescription"))
if mibBuilder.loadTexts: systemOverheatShutdownAlarm.setStatus('deprecated')
fanModuleFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5)).setObjects(("DATA-DOMAIN-MIB", "fanDescription"))
if mibBuilder.loadTexts: fanModuleFailedAlarm.setStatus('deprecated')
nvramFailingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6))
if mibBuilder.loadTexts: nvramFailingAlarm.setStatus('deprecated')
fileSystemFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7))
if mibBuilder.loadTexts: fileSystemFailedAlarm.setStatus('deprecated')
fileSpaceMaintenanceAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 8)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceName"))
if mibBuilder.loadTexts: fileSpaceMaintenanceAlarm.setStatus('deprecated')
fileSpacePreWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 9)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceName"))
if mibBuilder.loadTexts: fileSpacePreWarningAlarm.setStatus('deprecated')
fileSpaceWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceName"))
if mibBuilder.loadTexts: fileSpaceWarningAlarm.setStatus('deprecated')
fileSpaceSevereAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 11)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceName"))
if mibBuilder.loadTexts: fileSpaceSevereAlarm.setStatus('deprecated')
fileSpaceCriticalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 12)).setObjects(("DATA-DOMAIN-MIB", "fileSystemResourceName"))
if mibBuilder.loadTexts: fileSpaceCriticalAlarm.setStatus('deprecated')
diskFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 14)).setObjects(("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskFailedAlarm.setStatus('deprecated')
diskOverheatWarningAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 15)).setObjects(("DATA-DOMAIN-MIB", "diskTemperature"))
if mibBuilder.loadTexts: diskOverheatWarningAlarm.setStatus('deprecated')
diskOverheatAlertAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 16)).setObjects(("DATA-DOMAIN-MIB", "diskTemperature"))
if mibBuilder.loadTexts: diskOverheatAlertAlarm.setStatus('deprecated')
diskOverheatShutdownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 17)).setObjects(("DATA-DOMAIN-MIB", "diskTemperature"))
if mibBuilder.loadTexts: diskOverheatShutdownAlarm.setStatus('deprecated')
raidReconSevereAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 18))
if mibBuilder.loadTexts: raidReconSevereAlarm.setStatus('deprecated')
raidReconCriticalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 19))
if mibBuilder.loadTexts: raidReconCriticalAlarm.setStatus('deprecated')
raidReconCriticalShutdownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 20))
if mibBuilder.loadTexts: raidReconCriticalShutdownAlarm.setStatus('deprecated')
raidGroupMissingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 21))
if mibBuilder.loadTexts: raidGroupMissingAlarm.setStatus('deprecated')
diskNoSpareAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 22))
if mibBuilder.loadTexts: diskNoSpareAlarm.setStatus('deprecated')
diskPathAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 23)).setObjects(("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskPathAlarm.setStatus('deprecated')
diskSASAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 24))
if mibBuilder.loadTexts: diskSASAlarm.setStatus('deprecated')
diskSASHBAAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 25)).setObjects(("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskSASHBAAlarm.setStatus('deprecated')
snapshotFullAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 26))
if mibBuilder.loadTexts: snapshotFullAlarm.setStatus('deprecated')
snapshotHWMAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 27))
if mibBuilder.loadTexts: snapshotHWMAlarm.setStatus('deprecated')
clusterNodeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 28))
if mibBuilder.loadTexts: clusterNodeAlarm.setStatus('deprecated')
clusterInterfaceAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 29))
if mibBuilder.loadTexts: clusterInterfaceAlarm.setStatus('deprecated')
replSyncAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 30)).setObjects(("DATA-DOMAIN-MIB", "replStatus"))
if mibBuilder.loadTexts: replSyncAlarm.setStatus('deprecated')
systemStartupAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 31))
if mibBuilder.loadTexts: systemStartupAlarm.setStatus('deprecated')
filesysRelaunchAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 32))
if mibBuilder.loadTexts: filesysRelaunchAlarm.setStatus('deprecated')
filesysDDGCFailedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 33))
if mibBuilder.loadTexts: filesysDDGCFailedAlarm.setStatus('deprecated')
filesysGeneralProblemAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 34))
if mibBuilder.loadTexts: filesysGeneralProblemAlarm.setStatus('deprecated')
diskUnsupportedAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 35)).setObjects(("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskUnsupportedAlarm.setStatus('deprecated')
eventIPMIUnmanageAlarm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 36))
if mibBuilder.loadTexts: eventIPMIUnmanageAlarm.setStatus('deprecated')
generatedNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 5000)).setObjects(("DATA-DOMAIN-MIB", "cpismissing"), ("DATA-DOMAIN-MIB", "controllerUnreachableAlert"), ("DATA-DOMAIN-MIB", "controllerIfaceUnreachableAlert"), ("DATA-DOMAIN-MIB", "containerMarkedInvalid"), ("DATA-DOMAIN-MIB", "cMTaskEnded"), ("DATA-DOMAIN-MIB", "correctableECCLimitReached"), ("DATA-DOMAIN-MIB", "uncorrectableECCerror"), ("DATA-DOMAIN-MIB", "dIMMFailure"), ("DATA-DOMAIN-MIB", "compromisedEncryptionKeys"), ("DATA-DOMAIN-MIB", "newEncryptionKey"), ("DATA-DOMAIN-MIB", "encryptionKeyTableFull"), ("DATA-DOMAIN-MIB", "encryptionKeyExportFailed"), ("DATA-DOMAIN-MIB", "insufficientSpaceForEncryption"), ("DATA-DOMAIN-MIB", "corruptEncryptionKeys"), ("DATA-DOMAIN-MIB", "legacyChassisTempWarning"), ("DATA-DOMAIN-MIB", "legacyChassisTempCritical"), ("DATA-DOMAIN-MIB", "legacyPowerSupplyWarning"), ("DATA-DOMAIN-MIB", "legacyFanWarning"), ("DATA-DOMAIN-MIB", "powerSupplyWarning"), ("DATA-DOMAIN-MIB", "fanWarning"), ("DATA-DOMAIN-MIB", "voltageWarning"), ("DATA-DOMAIN-MIB", "powerWarning"), ("DATA-DOMAIN-MIB", "correctECCWarning"), ("DATA-DOMAIN-MIB", "processorWarning"), ("DATA-DOMAIN-MIB", "powerUnitWarning"), ("DATA-DOMAIN-MIB", "unCorrectECCWarning"), ("DATA-DOMAIN-MIB", "chassisSensorCritical"), ("DATA-DOMAIN-MIB", "chassisTempWarning"), ("DATA-DOMAIN-MIB", "chassisTempCritical"), ("DATA-DOMAIN-MIB", "cPUFailureWarning"), ("DATA-DOMAIN-MIB", "legacyBMCHangCritical"), ("DATA-DOMAIN-MIB", "bMCHangCritical"), ("DATA-DOMAIN-MIB", "abnormalShutdown"), ("DATA-DOMAIN-MIB", "smiMrc"), ("DATA-DOMAIN-MIB", "bMCPartialHang"), ("DATA-DOMAIN-MIB", "fanFault"), ("DATA-DOMAIN-MIB", "powerSupplyInputFault"), ("DATA-DOMAIN-MIB", "powerSupplyFailure"), ("DATA-DOMAIN-MIB", "powerSupplyAbsent"), ("DATA-DOMAIN-MIB", "unsupportedACVoltage"), ("DATA-DOMAIN-MIB", "iOModuleFault"), ("DATA-DOMAIN-MIB", "iOModuleInserted"), ("DATA-DOMAIN-MIB", "mgmtModuleFault"), ("DATA-DOMAIN-MIB", "sPFault"), ("DATA-DOMAIN-MIB", "chassisFailure"), ("DATA-DOMAIN-MIB", "forcedControllerShutdown"), ("DATA-DOMAIN-MIB", "systemReset"), ("DATA-DOMAIN-MIB", "enclosureHighTemp"), ("DATA-DOMAIN-MIB", "unsupportedSystemType"), ("DATA-DOMAIN-MIB", "bMCHangShutdown"), ("DATA-DOMAIN-MIB", "bMCFailure"), ("DATA-DOMAIN-MIB", "unsupportedHardwareConfig"), ("DATA-DOMAIN-MIB", "unsupportedVirtualCPU"), ("DATA-DOMAIN-MIB", "unsupportedPowerSupply"), ("DATA-DOMAIN-MIB", "openFanDrawer"), ("DATA-DOMAIN-MIB", "memoryRiserFault"), ("DATA-DOMAIN-MIB", "bMCFailureSysBBU"), ("DATA-DOMAIN-MIB", "unsupportedEnclosurePSU"), ("DATA-DOMAIN-MIB", "pCILinkDegraded"), ("DATA-DOMAIN-MIB", "invalidHardwareCritical"), ("DATA-DOMAIN-MIB", "invalidHardwareWarning"), ("DATA-DOMAIN-MIB", "correctableErrorWarning"), ("DATA-DOMAIN-MIB", "generalHardwareFailure"), ("DATA-DOMAIN-MIB", "targetDriverPortOffline"), ("DATA-DOMAIN-MIB", "targetDriverPortOnline"), ("DATA-DOMAIN-MIB", "targetDriverPortCore"), ("DATA-DOMAIN-MIB", "targetDriverPortMultipleCore"), ("DATA-DOMAIN-MIB", "targetDriverPortFWLoadFailed"), ("DATA-DOMAIN-MIB", "targetDriverPortUnreadable"), ("DATA-DOMAIN-MIB", "targetDriverPortTooManyOsc"), ("DATA-DOMAIN-MIB", "tooManyRelaunches"), ("DATA-DOMAIN-MIB", "filesystemProblem"), ("DATA-DOMAIN-MIB", "dDFSFailedInShutdown"), ("DATA-DOMAIN-MIB", "dDFSNoHeartbeat"), ("DATA-DOMAIN-MIB", "dDFSDiedAfterReboot"), ("DATA-DOMAIN-MIB", "dDFSDied"), ("DATA-DOMAIN-MIB", "dDFSRebooted"), ("DATA-DOMAIN-MIB", "dDFSRebootedDisabled"), ("DATA-DOMAIN-MIB", "indexRebuildComplete"), ("DATA-DOMAIN-MIB", "filesystemNVRAMDataLoss"), ("DATA-DOMAIN-MIB", "recoverFromNVRAMFailed"), ("DATA-DOMAIN-MIB", "dDFSRequiresReboot"), ("DATA-DOMAIN-MIB", "metadataWarningThreshold"), ("DATA-DOMAIN-MIB", "filesystemCorruption"), ("DATA-DOMAIN-MIB", "physicalCapacityMeasurementTasksLost"), ("DATA-DOMAIN-MIB", "physicalCapacityMeasurementTasksLostMTree"), ("DATA-DOMAIN-MIB", "physicalCapacityMeasurementScheduleFailed"), ("DATA-DOMAIN-MIB", "uncertifiedFirmware"), ("DATA-DOMAIN-MIB", "fileMigrationError"), ("DATA-DOMAIN-MIB", "cleaningError"), ("DATA-DOMAIN-MIB", "hAdegraded"), ("DATA-DOMAIN-MIB", "hAofflineErrors"), ("DATA-DOMAIN-MIB", "hATimeOutOfSync"), ("DATA-DOMAIN-MIB", "historicalDatabaseRecoverError"), ("DATA-DOMAIN-MIB", "historicalDatabaseBackupError"), ("DATA-DOMAIN-MIB", "historicalDatabaseUpgradeError"), ("DATA-DOMAIN-MIB", "historicalDatabasePruneError"), ("DATA-DOMAIN-MIB", "noHistoricalDatabaseError"), ("DATA-DOMAIN-MIB", "historicalDatabaseFailoverError"), ("DATA-DOMAIN-MIB", "hDTFileTransferFailed"), ("DATA-DOMAIN-MIB", "hDTSystemError"), ("DATA-DOMAIN-MIB", "spuriousInterruptDisabled"), ("DATA-DOMAIN-MIB", "licenseExpiring"), ("DATA-DOMAIN-MIB", "licenseExpired"), ("DATA-DOMAIN-MIB", "dIMMFailureAlert"), ("DATA-DOMAIN-MIB", "memoryAlert"), ("DATA-DOMAIN-MIB", "portPathDisabled"), ("DATA-DOMAIN-MIB", "diskPathRedundancy"), ("DATA-DOMAIN-MIB", "missingPortConnection"), ("DATA-DOMAIN-MIB", "missingLunPath"), ("DATA-DOMAIN-MIB", "missingDiskPath"), ("DATA-DOMAIN-MIB", "missingEnclosurePath"), ("DATA-DOMAIN-MIB", "interfaceConnectivityDown"), ("DATA-DOMAIN-MIB", "interfaceConnectivityIntermittent"), ("DATA-DOMAIN-MIB", "interfaceMisconfiguration"), ("DATA-DOMAIN-MIB", "interfaceConnectivityUpAndRunning"), ("DATA-DOMAIN-MIB", "duplicateAddressDetection"), ("DATA-DOMAIN-MIB", "invalidNICSlot"), ("DATA-DOMAIN-MIB", "unsupportedNIC"), ("DATA-DOMAIN-MIB", "tcpZeroWindowAlert"), ("DATA-DOMAIN-MIB", "dNSUnresponsive"), ("DATA-DOMAIN-MIB", "nISCommFailure"), ("DATA-DOMAIN-MIB", "iOModuleMacFault"), ("DATA-DOMAIN-MIB", "missingSlaveInterface"), ("DATA-DOMAIN-MIB", "nTPDFailed"), ("DATA-DOMAIN-MIB", "nvramWarning"), ("DATA-DOMAIN-MIB", "nvramBatteryAlert"), ("DATA-DOMAIN-MIB", "nvramErrorAlert"), ("DATA-DOMAIN-MIB", "nvramBatteryLowChargeAlert"), ("DATA-DOMAIN-MIB", "ext3NvlogDisabled"), ("DATA-DOMAIN-MIB", "nvramHWAlert"), ("DATA-DOMAIN-MIB", "nvramBattAlert"), ("DATA-DOMAIN-MIB", "nvramEnvAlert"), ("DATA-DOMAIN-MIB", "nvramCondAlert"), ("DATA-DOMAIN-MIB", "nvramEventHWAlert"), ("DATA-DOMAIN-MIB", "nvramBattEndOfLife"), ("DATA-DOMAIN-MIB", "phyalert"), ("DATA-DOMAIN-MIB", "mtreeQuotaSoftLimit"), ("DATA-DOMAIN-MIB", "mtreeQuotaHardLimit"), ("DATA-DOMAIN-MIB", "storageUnitStreamSoftLimit"), ("DATA-DOMAIN-MIB", "replProgressThreshholdReached"), ("DATA-DOMAIN-MIB", "replNeedResync"), ("DATA-DOMAIN-MIB", "replLogFull"), ("DATA-DOMAIN-MIB", "replIncompatibleWorm"), ("DATA-DOMAIN-MIB", "replDestNotConfigured"), ("DATA-DOMAIN-MIB", "replLagThreshholdReached"), ("DATA-DOMAIN-MIB", "replPathTooLong"), ("DATA-DOMAIN-MIB", "missingCreplUnits"), ("DATA-DOMAIN-MIB", "mtreeCascadeNeedResync"), ("DATA-DOMAIN-MIB", "insecureEncryptedReplication"), ("DATA-DOMAIN-MIB", "suspendedMReplMissingUnits"), ("DATA-DOMAIN-MIB", "sASEnclosureCheck"), ("DATA-DOMAIN-MIB", "sASTopologyCheck"), ("DATA-DOMAIN-MIB", "sASPortDisabled"), ("DATA-DOMAIN-MIB", "sASHBAFailure"), ("DATA-DOMAIN-MIB", "sASHBAErrors"), ("DATA-DOMAIN-MIB", "unsupportedSASDevice"), ("DATA-DOMAIN-MIB", "invalidEnclosureTopology"), ("DATA-DOMAIN-MIB", "diskPathSpeedDegraded"), ("DATA-DOMAIN-MIB", "enclosureMixType"), ("DATA-DOMAIN-MIB", "enclosureMixDriveType"), ("DATA-DOMAIN-MIB", "sCSITGTInvalidRegistry"), ("DATA-DOMAIN-MIB", "sSLCertificateCorrupted"), ("DATA-DOMAIN-MIB", "unusableHostCertificate"), ("DATA-DOMAIN-MIB", "missingHostCertificate"), ("DATA-DOMAIN-MIB", "expiredHostCertificate"), ("DATA-DOMAIN-MIB", "sMSUnresponsive"), ("DATA-DOMAIN-MIB", "mailserverError"), ("DATA-DOMAIN-MIB", "snapshotOver90Percent"), ("DATA-DOMAIN-MIB", "snapshotLimitReached"), ("DATA-DOMAIN-MIB", "sNTZMultipleIterations"), ("DATA-DOMAIN-MIB", "coredumpWarning"), ("DATA-DOMAIN-MIB", "coredumpDisabled"), ("DATA-DOMAIN-MIB", "spaceOver80Percent"), ("DATA-DOMAIN-MIB", "spaceOver90Percent"), ("DATA-DOMAIN-MIB", "spaceReclRestartFailed"), ("DATA-DOMAIN-MIB", "spaceReclMissingUnit"), ("DATA-DOMAIN-MIB", "spaceReclUnitReclaimed"), ("DATA-DOMAIN-MIB", "spaceReclError"), ("DATA-DOMAIN-MIB", "spaceReclSuspended"), ("DATA-DOMAIN-MIB", "spaceReclUnitError"), ("DATA-DOMAIN-MIB", "diskAccessError"), ("DATA-DOMAIN-MIB", "diskFailure"), ("DATA-DOMAIN-MIB", "diskTemperatureWarning"), ("DATA-DOMAIN-MIB", "diskTemperatureShutdown"), ("DATA-DOMAIN-MIB", "unsupportedHardwareSpareSize"), ("DATA-DOMAIN-MIB", "missingDiskGroup"), ("DATA-DOMAIN-MIB", "diskGroupReconstructionNoProgress"), ("DATA-DOMAIN-MIB", "diskGroupReconstruction"), ("DATA-DOMAIN-MIB", "diskGroupReconstructionShutdown"), ("DATA-DOMAIN-MIB", "diskGroupReconstructionCritical"), ("DATA-DOMAIN-MIB", "diskUnknown"), ("DATA-DOMAIN-MIB", "lowSpares"), ("DATA-DOMAIN-MIB", "unsupportedConfigurationROL"), ("DATA-DOMAIN-MIB", "foreignEnclosure"), ("DATA-DOMAIN-MIB", "sSDEndOfLife"), ("DATA-DOMAIN-MIB", "multipleDiskReadErrors"), ("DATA-DOMAIN-MIB", "unsupportedDriveModel"), ("DATA-DOMAIN-MIB", "driveMixType"), ("DATA-DOMAIN-MIB", "missingTierStorage"), ("DATA-DOMAIN-MIB", "storageMigrationCopyComplete"), ("DATA-DOMAIN-MIB", "storageMigrationCannotResume"), ("DATA-DOMAIN-MIB", "storageMigrationUserSuspend"), ("DATA-DOMAIN-MIB", "foreignPack"), ("DATA-DOMAIN-MIB", "upgradeFailure"), ("DATA-DOMAIN-MIB", "upgradeCompleted"), ("DATA-DOMAIN-MIB", "upgradeInProgress"), ("DATA-DOMAIN-MIB", "vDiskSCSITargetMismatch"), ("DATA-DOMAIN-MIB", "tapeReposition"), ("DATA-DOMAIN-MIB", "duplicateVTLPoolNames"), ("DATA-DOMAIN-MIB", "vTLEnabled"), ("DATA-DOMAIN-MIB", "vTLDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    generatedNotificationsGroup = generatedNotificationsGroup.setStatus('current')
cpismissing = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5500)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: cpismissing.setStatus('current')
controllerUnreachableAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5002)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: controllerUnreachableAlert.setStatus('current')
controllerIfaceUnreachableAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5003)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: controllerIfaceUnreachableAlert.setStatus('current')
containerMarkedInvalid = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5501)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: containerMarkedInvalid.setStatus('current')
cMTaskEnded = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10503)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: cMTaskEnded.setStatus('current')
correctableECCLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5004)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: correctableECCLimitReached.setStatus('current')
uncorrectableECCerror = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5005)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: uncorrectableECCerror.setStatus('current')
dIMMFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6525)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dIMMFailure.setStatus('current')
compromisedEncryptionKeys = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6001)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: compromisedEncryptionKeys.setStatus('current')
newEncryptionKey = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6002)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: newEncryptionKey.setStatus('current')
encryptionKeyTableFull = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6003)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: encryptionKeyTableFull.setStatus('current')
encryptionKeyExportFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6540)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: encryptionKeyExportFailed.setStatus('current')
insufficientSpaceForEncryption = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7515)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: insufficientSpaceForEncryption.setStatus('current')
corruptEncryptionKeys = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10009)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: corruptEncryptionKeys.setStatus('current')
legacyChassisTempWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5006)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: legacyChassisTempWarning.setStatus('current')
legacyChassisTempCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5007)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: legacyChassisTempCritical.setStatus('current')
legacyPowerSupplyWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5008)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "powerModuleDescription"))
if mibBuilder.loadTexts: legacyPowerSupplyWarning.setStatus('current')
legacyFanWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5009)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: legacyFanWarning.setStatus('current')
powerSupplyWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5010)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerSupplyWarning.setStatus('current')
fanWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5011)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: fanWarning.setStatus('current')
voltageWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5012)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: voltageWarning.setStatus('current')
powerWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5013)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerWarning.setStatus('current')
correctECCWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5014)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: correctECCWarning.setStatus('current')
processorWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5016)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: processorWarning.setStatus('current')
powerUnitWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5017)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerUnitWarning.setStatus('current')
unCorrectECCWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5018)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unCorrectECCWarning.setStatus('current')
chassisSensorCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5020)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: chassisSensorCritical.setStatus('current')
chassisTempWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5021)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: chassisTempWarning.setStatus('current')
chassisTempCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5022)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: chassisTempCritical.setStatus('current')
cPUFailureWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5023)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: cPUFailureWarning.setStatus('current')
legacyBMCHangCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5024)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: legacyBMCHangCritical.setStatus('current')
bMCHangCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5025)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: bMCHangCritical.setStatus('current')
abnormalShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5026)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: abnormalShutdown.setStatus('current')
smiMrc = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5502)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: smiMrc.setStatus('current')
bMCPartialHang = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6015)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: bMCPartialHang.setStatus('current')
fanFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6517)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: fanFault.setStatus('current')
powerSupplyInputFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6518)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerSupplyInputFault.setStatus('current')
powerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6519)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerSupplyFailure.setStatus('current')
powerSupplyAbsent = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6520)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: powerSupplyAbsent.setStatus('current')
unsupportedACVoltage = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6521)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedACVoltage.setStatus('current')
iOModuleFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6522)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: iOModuleFault.setStatus('current')
iOModuleInserted = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6523)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: iOModuleInserted.setStatus('current')
mgmtModuleFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6524)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: mgmtModuleFault.setStatus('current')
sPFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6526)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sPFault.setStatus('current')
chassisFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6527)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: chassisFailure.setStatus('current')
forcedControllerShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6528)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: forcedControllerShutdown.setStatus('current')
systemReset = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6529)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: systemReset.setStatus('current')
enclosureHighTemp = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6535)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: enclosureHighTemp.setStatus('current')
unsupportedSystemType = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6536)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedSystemType.setStatus('current')
bMCHangShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6537)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: bMCHangShutdown.setStatus('current')
bMCFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7000)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: bMCFailure.setStatus('current')
unsupportedHardwareConfig = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7502)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedHardwareConfig.setStatus('current')
unsupportedVirtualCPU = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7503)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedVirtualCPU.setStatus('current')
unsupportedPowerSupply = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10001)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedPowerSupply.setStatus('current')
openFanDrawer = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10002)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: openFanDrawer.setStatus('current')
memoryRiserFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10003)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: memoryRiserFault.setStatus('current')
bMCFailureSysBBU = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7524)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: bMCFailureSysBBU.setStatus('current')
unsupportedEnclosurePSU = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10000)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedEnclosurePSU.setStatus('current')
pCILinkDegraded = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10004)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: pCILinkDegraded.setStatus('current')
invalidHardwareCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10005)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: invalidHardwareCritical.setStatus('current')
invalidHardwareWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10006)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: invalidHardwareWarning.setStatus('current')
correctableErrorWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10007)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: correctableErrorWarning.setStatus('current')
generalHardwareFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10011)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: generalHardwareFailure.setStatus('current')
targetDriverPortOffline = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7508)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortOffline.setStatus('current')
targetDriverPortOnline = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7509)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortOnline.setStatus('current')
targetDriverPortCore = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7510)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortCore.setStatus('current')
targetDriverPortMultipleCore = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7511)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortMultipleCore.setStatus('current')
targetDriverPortFWLoadFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7512)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortFWLoadFailed.setStatus('current')
targetDriverPortUnreadable = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7513)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortUnreadable.setStatus('current')
targetDriverPortTooManyOsc = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7514)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: targetDriverPortTooManyOsc.setStatus('current')
tooManyRelaunches = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5027)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: tooManyRelaunches.setStatus('current')
filesystemProblem = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5028)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: filesystemProblem.setStatus('current')
dDFSFailedInShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5030)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dDFSFailedInShutdown.setStatus('current')
dDFSNoHeartbeat = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5034)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dDFSNoHeartbeat.setStatus('current')
dDFSDiedAfterReboot = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5036)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dDFSDiedAfterReboot.setStatus('current')
dDFSDied = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5037)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dDFSDied.setStatus('current')
dDFSRebooted = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5038)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: dDFSRebooted.setStatus('current')
dDFSRebootedDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5039)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: dDFSRebootedDisabled.setStatus('current')
indexRebuildComplete = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5040)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: indexRebuildComplete.setStatus('current')
filesystemNVRAMDataLoss = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6005)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: filesystemNVRAMDataLoss.setStatus('current')
recoverFromNVRAMFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6013)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: recoverFromNVRAMFailed.setStatus('current')
dDFSRequiresReboot = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7516)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dDFSRequiresReboot.setStatus('current')
metadataWarningThreshold = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7519)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: metadataWarningThreshold.setStatus('current')
filesystemCorruption = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7521)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: filesystemCorruption.setStatus('current')
physicalCapacityMeasurementTasksLost = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10504)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: physicalCapacityMeasurementTasksLost.setStatus('current')
physicalCapacityMeasurementTasksLostMTree = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10505)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: physicalCapacityMeasurementTasksLostMTree.setStatus('current')
physicalCapacityMeasurementScheduleFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10506)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: physicalCapacityMeasurementScheduleFailed.setStatus('current')
uncertifiedFirmware = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6004)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: uncertifiedFirmware.setStatus('current')
fileMigrationError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6016)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: fileMigrationError.setStatus('current')
cleaningError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6014)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: cleaningError.setStatus('current')
hAdegraded = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10508)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: hAdegraded.setStatus('current')
hAofflineErrors = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10510)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: hAofflineErrors.setStatus('current')
hATimeOutOfSync = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10514)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: hATimeOutOfSync.setStatus('current')
historicalDatabaseRecoverError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5041)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: historicalDatabaseRecoverError.setStatus('current')
historicalDatabaseBackupError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5042)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: historicalDatabaseBackupError.setStatus('current')
historicalDatabaseUpgradeError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5043)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: historicalDatabaseUpgradeError.setStatus('current')
historicalDatabasePruneError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5044)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: historicalDatabasePruneError.setStatus('current')
noHistoricalDatabaseError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5045)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: noHistoricalDatabaseError.setStatus('current')
historicalDatabaseFailoverError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10507)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: historicalDatabaseFailoverError.setStatus('current')
hDTFileTransferFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5046)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: hDTFileTransferFailed.setStatus('current')
hDTSystemError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5047)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: hDTSystemError.setStatus('current')
spuriousInterruptDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10008)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spuriousInterruptDisabled.setStatus('current')
licenseExpiring = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 8001)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: licenseExpiring.setStatus('current')
licenseExpired = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 8002)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: licenseExpired.setStatus('current')
dIMMFailureAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5048)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dIMMFailureAlert.setStatus('current')
memoryAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5049)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: memoryAlert.setStatus('current')
portPathDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5050)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: portPathDisabled.setStatus('current')
diskPathRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5051)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskPathRedundancy.setStatus('current')
missingPortConnection = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5052)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingPortConnection.setStatus('current')
missingLunPath = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5053)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingLunPath.setStatus('current')
missingDiskPath = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5054)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: missingDiskPath.setStatus('current')
missingEnclosurePath = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5055)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingEnclosurePath.setStatus('current')
interfaceConnectivityDown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6009)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: interfaceConnectivityDown.setStatus('current')
interfaceConnectivityIntermittent = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6010)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: interfaceConnectivityIntermittent.setStatus('current')
interfaceMisconfiguration = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6011)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: interfaceMisconfiguration.setStatus('current')
interfaceConnectivityUpAndRunning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6020)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: interfaceConnectivityUpAndRunning.setStatus('current')
duplicateAddressDetection = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6530)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: duplicateAddressDetection.setStatus('current')
invalidNICSlot = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6512)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: invalidNICSlot.setStatus('current')
unsupportedNIC = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6513)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedNIC.setStatus('current')
tcpZeroWindowAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6101)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: tcpZeroWindowAlert.setStatus('current')
dNSUnresponsive = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7504)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: dNSUnresponsive.setStatus('current')
nISCommFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7501)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nISCommFailure.setStatus('current')
iOModuleMacFault = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10013)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: iOModuleMacFault.setStatus('current')
missingSlaveInterface = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10523)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingSlaveInterface.setStatus('current')
nTPDFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7505)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nTPDFailed.setStatus('current')
nvramWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5059)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramWarning.setStatus('current')
nvramBatteryAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5060)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "nvramBatteryStatus"))
if mibBuilder.loadTexts: nvramBatteryAlert.setStatus('current')
nvramErrorAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5061)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramErrorAlert.setStatus('current')
nvramBatteryLowChargeAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5508)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramBatteryLowChargeAlert.setStatus('current')
ext3NvlogDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5527)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: ext3NvlogDisabled.setStatus('current')
nvramHWAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6504)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramHWAlert.setStatus('current')
nvramBattAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6507)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramBattAlert.setStatus('current')
nvramEnvAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6505)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramEnvAlert.setStatus('current')
nvramCondAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6508)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramCondAlert.setStatus('current')
nvramEventHWAlert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6506)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramEventHWAlert.setStatus('current')
nvramBattEndOfLife = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6545)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: nvramBattEndOfLife.setStatus('current')
phyalert = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5062)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: phyalert.setStatus('current')
mtreeQuotaSoftLimit = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6007)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: mtreeQuotaSoftLimit.setStatus('current')
mtreeQuotaHardLimit = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6008)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: mtreeQuotaHardLimit.setStatus('current')
storageUnitStreamSoftLimit = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7517)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: storageUnitStreamSoftLimit.setStatus('current')
replProgressThreshholdReached = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5063)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "replStatus"))
if mibBuilder.loadTexts: replProgressThreshholdReached.setStatus('current')
replNeedResync = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5064)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "replStatus"))
if mibBuilder.loadTexts: replNeedResync.setStatus('current')
replLogFull = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5065)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: replLogFull.setStatus('current')
replIncompatibleWorm = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5066)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: replIncompatibleWorm.setStatus('current')
replDestNotConfigured = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5067)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "replConfigDest"))
if mibBuilder.loadTexts: replDestNotConfigured.setStatus('current')
replLagThreshholdReached = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5068)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: replLagThreshholdReached.setStatus('current')
replPathTooLong = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5531)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: replPathTooLong.setStatus('current')
missingCreplUnits = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6544)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingCreplUnits.setStatus('current')
mtreeCascadeNeedResync = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7520)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "replStatus"))
if mibBuilder.loadTexts: mtreeCascadeNeedResync.setStatus('current')
insecureEncryptedReplication = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6102)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: insecureEncryptedReplication.setStatus('current')
suspendedMReplMissingUnits = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10511)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: suspendedMReplMissingUnits.setStatus('current')
sASEnclosureCheck = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5069)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sASEnclosureCheck.setStatus('current')
sASTopologyCheck = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5070)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sASTopologyCheck.setStatus('current')
sASPortDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5071)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sASPortDisabled.setStatus('current')
sASHBAFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6514)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sASHBAFailure.setStatus('current')
sASHBAErrors = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6515)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sASHBAErrors.setStatus('current')
unsupportedSASDevice = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6516)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedSASDevice.setStatus('current')
invalidEnclosureTopology = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7506)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: invalidEnclosureTopology.setStatus('current')
diskPathSpeedDegraded = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7507)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskPathSpeedDegraded.setStatus('current')
enclosureMixType = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5528)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: enclosureMixType.setStatus('current')
enclosureMixDriveType = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10515)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: enclosureMixDriveType.setStatus('current')
sCSITGTInvalidRegistry = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6539)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sCSITGTInvalidRegistry.setStatus('current')
sSLCertificateCorrupted = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5072)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sSLCertificateCorrupted.setStatus('current')
unusableHostCertificate = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6017)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: unusableHostCertificate.setStatus('current')
missingHostCertificate = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6018)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: missingHostCertificate.setStatus('current')
expiredHostCertificate = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6538)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: expiredHostCertificate.setStatus('current')
sMSUnresponsive = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7500)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sMSUnresponsive.setStatus('current')
mailserverError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6511)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: mailserverError.setStatus('current')
snapshotOver90Percent = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5075)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: snapshotOver90Percent.setStatus('current')
snapshotLimitReached = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5076)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: snapshotLimitReached.setStatus('current')
sNTZMultipleIterations = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5077)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: sNTZMultipleIterations.setStatus('current')
coredumpWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5078)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: coredumpWarning.setStatus('current')
coredumpDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5079)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: coredumpDisabled.setStatus('current')
spaceOver80Percent = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5080)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"))
if mibBuilder.loadTexts: spaceOver80Percent.setStatus('current')
spaceOver90Percent = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5081)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"))
if mibBuilder.loadTexts: spaceOver90Percent.setStatus('current')
spaceReclRestartFailed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6531)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclRestartFailed.setStatus('current')
spaceReclMissingUnit = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6532)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclMissingUnit.setStatus('current')
spaceReclUnitReclaimed = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6533)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclUnitReclaimed.setStatus('current')
spaceReclError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6534)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclError.setStatus('current')
spaceReclSuspended = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7518)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclSuspended.setStatus('current')
spaceReclUnitError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7523)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: spaceReclUnitError.setStatus('current')
diskAccessError = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5082)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskAccessError.setStatus('current')
diskFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5083)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: diskFailure.setStatus('current')
diskTemperatureWarning = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5084)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskTemperature"))
if mibBuilder.loadTexts: diskTemperatureWarning.setStatus('current')
diskTemperatureShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5085)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: diskTemperatureShutdown.setStatus('current')
unsupportedHardwareSpareSize = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5086)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: unsupportedHardwareSpareSize.setStatus('current')
missingDiskGroup = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5087)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingDiskGroup.setStatus('current')
diskGroupReconstructionNoProgress = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5088)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskGroupReconstructionNoProgress.setStatus('current')
diskGroupReconstruction = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5089)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskGroupReconstruction.setStatus('current')
diskGroupReconstructionShutdown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5090)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskGroupReconstructionShutdown.setStatus('current')
diskGroupReconstructionCritical = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5091)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskGroupReconstructionCritical.setStatus('current')
diskUnknown = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5092)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: diskUnknown.setStatus('current')
lowSpares = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5094)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: lowSpares.setStatus('current')
unsupportedConfigurationROL = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 5095)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedConfigurationROL.setStatus('current')
foreignEnclosure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6019)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "enclosureListNum"))
if mibBuilder.loadTexts: foreignEnclosure.setStatus('current')
sSDEndOfLife = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6541)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "diskSerialNumber"))
if mibBuilder.loadTexts: sSDEndOfLife.setStatus('current')
multipleDiskReadErrors = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6543)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: multipleDiskReadErrors.setStatus('current')
unsupportedDriveModel = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7001)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: unsupportedDriveModel.setStatus('current')
driveMixType = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7002)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: driveMixType.setStatus('current')
missingTierStorage = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 7522)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: missingTierStorage.setStatus('current')
storageMigrationCopyComplete = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10501)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: storageMigrationCopyComplete.setStatus('current')
storageMigrationCannotResume = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10500)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: storageMigrationCannotResume.setStatus('current')
storageMigrationUserSuspend = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10502)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: storageMigrationUserSuspend.setStatus('current')
foreignPack = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10512)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "enclosurePackID"))
if mibBuilder.loadTexts: foreignPack.setStatus('current')
upgradeFailure = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6509)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: upgradeFailure.setStatus('current')
upgradeCompleted = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6510)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: upgradeCompleted.setStatus('current')
upgradeInProgress = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10509)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: upgradeInProgress.setStatus('current')
vDiskSCSITargetMismatch = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10513)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: vDiskSCSITargetMismatch.setStatus('current')
tapeReposition = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 6542)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: tapeReposition.setStatus('current')
duplicateVTLPoolNames = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 10010)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: duplicateVTLPoolNames.setStatus('current')
vTLEnabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 11105)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: vTLEnabled.setStatus('current')
vTLDisabled = NotificationType((1, 3, 6, 1, 4, 1, 19746, 2, 0, 11106)).setObjects(("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if mibBuilder.loadTexts: vTLDisabled.setStatus('current')
dataDomainMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 19746, 0, 1))
dataDomainMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 1)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroup"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "basicNotificationsGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroup"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageNotificationsGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibCompliance = dataDomainMibCompliance.setStatus('deprecated')
dataDomainMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 2)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroup"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "ddboostGroup"), ("DATA-DOMAIN-MIB", "ddsystemGroup"), ("DATA-DOMAIN-MIB", "artGroup"), ("DATA-DOMAIN-MIB", "mtreeGroup"), ("DATA-DOMAIN-MIB", "enclosureGroup"), ("DATA-DOMAIN-MIB", "networkGroup"), ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"), ("DATA-DOMAIN-MIB", "managedObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibComplianceRev1 = dataDomainMibComplianceRev1.setStatus('deprecated')
dataDomainMibComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 3)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroup"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "ddboostGroup"), ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"), ("DATA-DOMAIN-MIB", "artGroup"), ("DATA-DOMAIN-MIB", "mtreeGroup"), ("DATA-DOMAIN-MIB", "enclosureGroup"), ("DATA-DOMAIN-MIB", "networkGroup"), ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"), ("DATA-DOMAIN-MIB", "managedObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibComplianceRev2 = dataDomainMibComplianceRev2.setStatus('deprecated')
dataDomainMibComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 4)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroup"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "ddboostGroupRev1"), ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"), ("DATA-DOMAIN-MIB", "artGroup"), ("DATA-DOMAIN-MIB", "mtreeGroup"), ("DATA-DOMAIN-MIB", "enclosureGroup"), ("DATA-DOMAIN-MIB", "networkGroup"), ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"), ("DATA-DOMAIN-MIB", "smtGroup"), ("DATA-DOMAIN-MIB", "quotaGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"), ("DATA-DOMAIN-MIB", "managedObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibComplianceRev3 = dataDomainMibComplianceRev3.setStatus('deprecated')
dataDomainMibComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 5)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroup"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "ddboostGroupRev2"), ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"), ("DATA-DOMAIN-MIB", "artGroup"), ("DATA-DOMAIN-MIB", "mtreeGroup"), ("DATA-DOMAIN-MIB", "enclosureGroup"), ("DATA-DOMAIN-MIB", "networkGroup"), ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"), ("DATA-DOMAIN-MIB", "smtGroup"), ("DATA-DOMAIN-MIB", "quotaGroup"), ("DATA-DOMAIN-MIB", "highAvailabilityGroup"), ("DATA-DOMAIN-MIB", "scsitargetObjectGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"), ("DATA-DOMAIN-MIB", "managedObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibComplianceRev4 = dataDomainMibComplianceRev4.setStatus('deprecated')
dataDomainMibComplianceRev5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 19746, 0, 1, 6)).setObjects(("DATA-DOMAIN-MIB", "environmentalsGroup"), ("DATA-DOMAIN-MIB", "nvramGroup"), ("DATA-DOMAIN-MIB", "fileSystemGroupRev1"), ("DATA-DOMAIN-MIB", "alertsGroup"), ("DATA-DOMAIN-MIB", "statisticsGroup"), ("DATA-DOMAIN-MIB", "replGroup"), ("DATA-DOMAIN-MIB", "nfsGroup"), ("DATA-DOMAIN-MIB", "cifsGroupRev1"), ("DATA-DOMAIN-MIB", "vtlGroup"), ("DATA-DOMAIN-MIB", "ddboostGroupRev2"), ("DATA-DOMAIN-MIB", "ddsystemGroupRev1"), ("DATA-DOMAIN-MIB", "artGroup"), ("DATA-DOMAIN-MIB", "mtreeGroup"), ("DATA-DOMAIN-MIB", "enclosureGroup"), ("DATA-DOMAIN-MIB", "networkGroup"), ("DATA-DOMAIN-MIB", "generatedNotificationsGroup"), ("DATA-DOMAIN-MIB", "smtGroup"), ("DATA-DOMAIN-MIB", "quotaGroup"), ("DATA-DOMAIN-MIB", "highAvailabilityGroup"), ("DATA-DOMAIN-MIB", "scsitargetObjectGroup"), ("DATA-DOMAIN-MIB", "internalDiskStorageGroup"), ("DATA-DOMAIN-MIB", "externalUnmanagedDiskStorageGroup"), ("DATA-DOMAIN-MIB", "managedObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dataDomainMibComplianceRev5 = dataDomainMibComplianceRev5.setStatus('current')
environmentalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 1)).setObjects(("DATA-DOMAIN-MIB", "powerModuleDescription"), ("DATA-DOMAIN-MIB", "powerModuleStatus"), ("DATA-DOMAIN-MIB", "tempSensorDescription"), ("DATA-DOMAIN-MIB", "tempSensorCurrentValue"), ("DATA-DOMAIN-MIB", "tempSensorStatus"), ("DATA-DOMAIN-MIB", "fanDescription"), ("DATA-DOMAIN-MIB", "fanLevel"), ("DATA-DOMAIN-MIB", "fanStatus"), ("DATA-DOMAIN-MIB", "tempSensorTrapIndex"), ("DATA-DOMAIN-MIB", "fanTrapIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    environmentalsGroup = environmentalsGroup.setStatus('current')
nvramGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 2)).setObjects(("DATA-DOMAIN-MIB", "nvramMemorySize"), ("DATA-DOMAIN-MIB", "nvramWindowSize"), ("DATA-DOMAIN-MIB", "nvramPCIErrorCount"), ("DATA-DOMAIN-MIB", "nvramMemoryErrorCount"), ("DATA-DOMAIN-MIB", "nvramBatteryStatus"), ("DATA-DOMAIN-MIB", "nvramBatteryCharge"), ("DATA-DOMAIN-MIB", "nvramHCMemorySize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nvramGroup = nvramGroup.setStatus('current')
fileSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 3)).setObjects(("DATA-DOMAIN-MIB", "fileSystemStatus"), ("DATA-DOMAIN-MIB", "fileSystemVirtualSpace"), ("DATA-DOMAIN-MIB", "fileSystemResourceName"), ("DATA-DOMAIN-MIB", "fileSystemSpaceSize"), ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"), ("DATA-DOMAIN-MIB", "fileSystemSpaceAvail"), ("DATA-DOMAIN-MIB", "fileSystemPercentUsed"), ("DATA-DOMAIN-MIB", "fileSystemSpaceCleanable"), ("DATA-DOMAIN-MIB", "fileSystemCompressionPeriod"), ("DATA-DOMAIN-MIB", "fileSystemCompressionStartTime"), ("DATA-DOMAIN-MIB", "fileSystemCompressionEndTime"), ("DATA-DOMAIN-MIB", "fileSystemPreCompressionSize"), ("DATA-DOMAIN-MIB", "fileSystemPostCompressionSize"), ("DATA-DOMAIN-MIB", "fileSystemGlobalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemLocalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemTotalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemReductionPercent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fileSystemGroup = fileSystemGroup.setStatus('deprecated')
alertsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 4)).setObjects(("DATA-DOMAIN-MIB", "currentAlertTimestamp"), ("DATA-DOMAIN-MIB", "currentAlertDescription"), ("DATA-DOMAIN-MIB", "currentAlertSeverity"), ("DATA-DOMAIN-MIB", "currentAlertID"), ("DATA-DOMAIN-MIB", "alertHistoryTimestamp"), ("DATA-DOMAIN-MIB", "alertHistoryDescription"), ("DATA-DOMAIN-MIB", "alertHistorySeverity"), ("DATA-DOMAIN-MIB", "alertHistoryStatus"), ("DATA-DOMAIN-MIB", "alertInfoDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alertsGroup = alertsGroup.setStatus('current')
statisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 5)).setObjects(("DATA-DOMAIN-MIB", "cpuAvgPercentageBusy"), ("DATA-DOMAIN-MIB", "cpuMaxPercentageBusy"), ("DATA-DOMAIN-MIB", "nfsOpsPerSecond"), ("DATA-DOMAIN-MIB", "nfsIdlePercentage"), ("DATA-DOMAIN-MIB", "nfsProcPercentage"), ("DATA-DOMAIN-MIB", "nfsSendPercentage"), ("DATA-DOMAIN-MIB", "nfsReceivePercentage"), ("DATA-DOMAIN-MIB", "cifsOpsPerSecond"), ("DATA-DOMAIN-MIB", "diskReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "diskWriteKBytesPerSecond"), ("DATA-DOMAIN-MIB", "diskBusyPercentage"), ("DATA-DOMAIN-MIB", "nvramReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "nvramWriteKBytesPerSecond"), ("DATA-DOMAIN-MIB", "replInKBytesPerSecond"), ("DATA-DOMAIN-MIB", "replOutKBytesPerSecond"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    statisticsGroup = statisticsGroup.setStatus('current')
internalDiskStorageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 7)).setObjects(("DATA-DOMAIN-MIB", "diskModel"), ("DATA-DOMAIN-MIB", "diskFirmwareVersion"), ("DATA-DOMAIN-MIB", "diskSerialNumber"), ("DATA-DOMAIN-MIB", "diskCapacity"), ("DATA-DOMAIN-MIB", "diskPropState"), ("DATA-DOMAIN-MIB", "diskPack"), ("DATA-DOMAIN-MIB", "diskSectorsRead"), ("DATA-DOMAIN-MIB", "diskSectorsWritten"), ("DATA-DOMAIN-MIB", "diskTotalKBytes"), ("DATA-DOMAIN-MIB", "diskBusy"), ("DATA-DOMAIN-MIB", "diskPerfState"), ("DATA-DOMAIN-MIB", "diskTemperature"), ("DATA-DOMAIN-MIB", "diskTimeoutCount"), ("DATA-DOMAIN-MIB", "diskReadFailCount"), ("DATA-DOMAIN-MIB", "diskWriteFailCount"), ("DATA-DOMAIN-MIB", "diskMiscFailCount"), ("DATA-DOMAIN-MIB", "diskOffTrackErrCount"), ("DATA-DOMAIN-MIB", "diskSoftEccCount"), ("DATA-DOMAIN-MIB", "diskCrcErrCount"), ("DATA-DOMAIN-MIB", "diskProbationalCount"), ("DATA-DOMAIN-MIB", "diskReallocCount"), ("DATA-DOMAIN-MIB", "diskErrState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    internalDiskStorageGroup = internalDiskStorageGroup.setStatus('current')
externalUnmanagedDiskStorageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 8)).setObjects(("DATA-DOMAIN-MIB", "diskModel"), ("DATA-DOMAIN-MIB", "diskFirmwareVersion"), ("DATA-DOMAIN-MIB", "diskSerialNumber"), ("DATA-DOMAIN-MIB", "diskCapacity"), ("DATA-DOMAIN-MIB", "diskPropState"), ("DATA-DOMAIN-MIB", "diskSectorsRead"), ("DATA-DOMAIN-MIB", "diskSectorsWritten"), ("DATA-DOMAIN-MIB", "diskTotalKBytes"), ("DATA-DOMAIN-MIB", "diskBusy"), ("DATA-DOMAIN-MIB", "diskPerfState"), ("DATA-DOMAIN-MIB", "diskPropTrapIndex"), ("DATA-DOMAIN-MIB", "diskErrTrapIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    externalUnmanagedDiskStorageGroup = externalUnmanagedDiskStorageGroup.setStatus('current')
basicNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 9)).setObjects(("DATA-DOMAIN-MIB", "powerSupplyFailedAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatWarningAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatAlertAlarm"), ("DATA-DOMAIN-MIB", "systemOverheatShutdownAlarm"), ("DATA-DOMAIN-MIB", "fanModuleFailedAlarm"), ("DATA-DOMAIN-MIB", "nvramFailingAlarm"), ("DATA-DOMAIN-MIB", "fileSystemFailedAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceMaintenanceAlarm"), ("DATA-DOMAIN-MIB", "fileSpacePreWarningAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceWarningAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceSevereAlarm"), ("DATA-DOMAIN-MIB", "fileSpaceCriticalAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatWarningAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatAlertAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatShutdownAlarm"), ("DATA-DOMAIN-MIB", "diskFailedAlarm"), ("DATA-DOMAIN-MIB", "diskNoSpareAlarm"), ("DATA-DOMAIN-MIB", "diskPathAlarm"), ("DATA-DOMAIN-MIB", "diskSASAlarm"), ("DATA-DOMAIN-MIB", "diskSASHBAAlarm"), ("DATA-DOMAIN-MIB", "snapshotFullAlarm"), ("DATA-DOMAIN-MIB", "snapshotHWMAlarm"), ("DATA-DOMAIN-MIB", "clusterNodeAlarm"), ("DATA-DOMAIN-MIB", "clusterInterfaceAlarm"), ("DATA-DOMAIN-MIB", "replSyncAlarm"), ("DATA-DOMAIN-MIB", "systemStartupAlarm"), ("DATA-DOMAIN-MIB", "filesysRelaunchAlarm"), ("DATA-DOMAIN-MIB", "filesysDDGCFailedAlarm"), ("DATA-DOMAIN-MIB", "filesysGeneralProblemAlarm"), ("DATA-DOMAIN-MIB", "diskUnsupportedAlarm"), ("DATA-DOMAIN-MIB", "eventIPMIUnmanageAlarm"), ("DATA-DOMAIN-MIB", "raidReconSevereAlarm"), ("DATA-DOMAIN-MIB", "raidReconCriticalAlarm"), ("DATA-DOMAIN-MIB", "raidReconCriticalShutdownAlarm"), ("DATA-DOMAIN-MIB", "raidGroupMissingAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basicNotificationsGroup = basicNotificationsGroup.setStatus('deprecated')
internalDiskStorageNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 10)).setObjects(("DATA-DOMAIN-MIB", "diskFailedAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatWarningAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatAlertAlarm"), ("DATA-DOMAIN-MIB", "diskOverheatShutdownAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    internalDiskStorageNotificationsGroup = internalDiskStorageNotificationsGroup.setStatus('deprecated')
replGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 11)).setObjects(("DATA-DOMAIN-MIB", "replState"), ("DATA-DOMAIN-MIB", "replStatus"), ("DATA-DOMAIN-MIB", "replFileSysStatus"), ("DATA-DOMAIN-MIB", "replConnTime"), ("DATA-DOMAIN-MIB", "replSource"), ("DATA-DOMAIN-MIB", "replDestination"), ("DATA-DOMAIN-MIB", "replPreCompBytesSent"), ("DATA-DOMAIN-MIB", "replPostCompBytesSent"), ("DATA-DOMAIN-MIB", "replPreCompBytesRemaining"), ("DATA-DOMAIN-MIB", "replPostCompBytesReceived"), ("DATA-DOMAIN-MIB", "replThrottle"), ("DATA-DOMAIN-MIB", "replSyncedAsOfTime"), ("DATA-DOMAIN-MIB", "replConfigContextId"), ("DATA-DOMAIN-MIB", "replConfigSource"), ("DATA-DOMAIN-MIB", "replConfigDest"), ("DATA-DOMAIN-MIB", "replConfigConnHost"), ("DATA-DOMAIN-MIB", "replConfigConnPort"), ("DATA-DOMAIN-MIB", "replConfigLowBWOptim"), ("DATA-DOMAIN-MIB", "replConfigEnabled"), ("DATA-DOMAIN-MIB", "replConfigTenantUnit"), ("DATA-DOMAIN-MIB", "replHistoryDate"), ("DATA-DOMAIN-MIB", "replHistoryTime"), ("DATA-DOMAIN-MIB", "replHistoryPreCompWritten"), ("DATA-DOMAIN-MIB", "replHistoryPreCompRemaining"), ("DATA-DOMAIN-MIB", "replHistoryPreCompressed"), ("DATA-DOMAIN-MIB", "replHistoryPostFiltered"), ("DATA-DOMAIN-MIB", "replHistoryPostLowBwOptim"), ("DATA-DOMAIN-MIB", "replHistoryPostLocalComp"), ("DATA-DOMAIN-MIB", "replHistoryBytesNetwork"), ("DATA-DOMAIN-MIB", "replHistorySyncedAsOfTime"), ("DATA-DOMAIN-MIB", "replTrapContext"), ("DATA-DOMAIN-MIB", "replPerformancePreCompKBPerSec"), ("DATA-DOMAIN-MIB", "replPerformanceNetworkKBPerSec"), ("DATA-DOMAIN-MIB", "replPerformanceStreams"), ("DATA-DOMAIN-MIB", "replPerformanceBusyReading"), ("DATA-DOMAIN-MIB", "replPerformanceBusyMeta"), ("DATA-DOMAIN-MIB", "replPerformanceWaitingDest"), ("DATA-DOMAIN-MIB", "replPerformanceWaitingNetwork"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    replGroup = replGroup.setStatus('current')
nfsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 12)).setObjects(("DATA-DOMAIN-MIB", "nfsStatus"), ("DATA-DOMAIN-MIB", "nfsClientPath"), ("DATA-DOMAIN-MIB", "nfsClientClients"), ("DATA-DOMAIN-MIB", "nfsClientOptions"), ("DATA-DOMAIN-MIB", "nfsStatsExportPoint"), ("DATA-DOMAIN-MIB", "nfsStatsFilesystemType"), ("DATA-DOMAIN-MIB", "nfsStatsCacheEntry"), ("DATA-DOMAIN-MIB", "nfsStatsFileHandleLookup"), ("DATA-DOMAIN-MIB", "nfsStatsMaxCacheSize"), ("DATA-DOMAIN-MIB", "nfsStatsCurrentOpenStreams"), ("DATA-DOMAIN-MIB", "nfsActivePath"), ("DATA-DOMAIN-MIB", "nfsActiveClients"), ("DATA-DOMAIN-MIB", "nfsPortService"), ("DATA-DOMAIN-MIB", "nfsPortPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nfsGroup = nfsGroup.setStatus('current')
cifsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 13)).setObjects(("DATA-DOMAIN-MIB", "cifsStatus"), ("DATA-DOMAIN-MIB", "cifsConfigMode"), ("DATA-DOMAIN-MIB", "cifsConfigWINSServer"), ("DATA-DOMAIN-MIB", "cifsConfigNetBIOSHostname"), ("DATA-DOMAIN-MIB", "cifsConfigDomainController"), ("DATA-DOMAIN-MIB", "cifsConfigDNS"), ("DATA-DOMAIN-MIB", "cifsConfigGroupName"), ("DATA-DOMAIN-MIB", "cifsConfigMaxConnection"), ("DATA-DOMAIN-MIB", "cifsConfigMaxOpenFilesPerConnection"), ("DATA-DOMAIN-MIB", "cifsShareName"), ("DATA-DOMAIN-MIB", "cifsSharePath"), ("DATA-DOMAIN-MIB", "cifsShareClients"), ("DATA-DOMAIN-MIB", "cifsShareUser"), ("DATA-DOMAIN-MIB", "cifsShareComment"), ("DATA-DOMAIN-MIB", "cifsShareBrowsing"), ("DATA-DOMAIN-MIB", "cifsShareWriteable"), ("DATA-DOMAIN-MIB", "cifsShareMaxConnection"), ("DATA-DOMAIN-MIB", "cifsOptionsName"), ("DATA-DOMAIN-MIB", "cifsOptionsValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifsGroup = cifsGroup.setStatus('deprecated')
vtlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 14)).setObjects(("DATA-DOMAIN-MIB", "vtlAdminState"), ("DATA-DOMAIN-MIB", "vtlProcessState"), ("DATA-DOMAIN-MIB", "vtlLibraryName"), ("DATA-DOMAIN-MIB", "vtlLibraryVendor"), ("DATA-DOMAIN-MIB", "vtlLibraryModel"), ("DATA-DOMAIN-MIB", "vtlLibraryRevision"), ("DATA-DOMAIN-MIB", "vtlLibrarySerial"), ("DATA-DOMAIN-MIB", "vtlLibraryTotalDrives"), ("DATA-DOMAIN-MIB", "vtlLibraryTotalSlots"), ("DATA-DOMAIN-MIB", "vtlLibraryTotalCaps"), ("DATA-DOMAIN-MIB", "vtlLibraryStatus"), ("DATA-DOMAIN-MIB", "vtlDriveName"), ("DATA-DOMAIN-MIB", "vtlDriveVendor"), ("DATA-DOMAIN-MIB", "vtlDriveModel"), ("DATA-DOMAIN-MIB", "vtlDriveRevision"), ("DATA-DOMAIN-MIB", "vtlDriveSerial"), ("DATA-DOMAIN-MIB", "vtlDriveLibraryName"), ("DATA-DOMAIN-MIB", "vtlDriveStatus"), ("DATA-DOMAIN-MIB", "vtlDriveTapeVolume"), ("DATA-DOMAIN-MIB", "vtlGroupName"), ("DATA-DOMAIN-MIB", "vtlGroupInitiaterCount"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceCount"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceGroupName"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceDeviceName"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceLun"), ("DATA-DOMAIN-MIB", "vtlGroupDevicePrimaryPorts"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceSecondaryPorts"), ("DATA-DOMAIN-MIB", "vtlGroupDeviceInUsePorts"), ("DATA-DOMAIN-MIB", "vtlInitiatorName"), ("DATA-DOMAIN-MIB", "vtlInitiatorStatus"), ("DATA-DOMAIN-MIB", "vtlInitiatorGroup"), ("DATA-DOMAIN-MIB", "vtlInitiatorWWNN"), ("DATA-DOMAIN-MIB", "vtlInitiatorWWPN"), ("DATA-DOMAIN-MIB", "vtlInitiatorPort"), ("DATA-DOMAIN-MIB", "vtlPoolPool"), ("DATA-DOMAIN-MIB", "vtlPoolStatus"), ("DATA-DOMAIN-MIB", "vtlPoolTapes"), ("DATA-DOMAIN-MIB", "vtlPoolSize"), ("DATA-DOMAIN-MIB", "vtlPoolUsed"), ("DATA-DOMAIN-MIB", "vtlPoolComp"), ("DATA-DOMAIN-MIB", "vtlPortName"), ("DATA-DOMAIN-MIB", "vtlPortID"), ("DATA-DOMAIN-MIB", "vtlPortModel"), ("DATA-DOMAIN-MIB", "vtlPortFirmware"), ("DATA-DOMAIN-MIB", "vtlPortWWNN"), ("DATA-DOMAIN-MIB", "vtlPortWWPN"), ("DATA-DOMAIN-MIB", "vtlPortConnectionType"), ("DATA-DOMAIN-MIB", "vtlPortSpeed"), ("DATA-DOMAIN-MIB", "vtlPortEnabled"), ("DATA-DOMAIN-MIB", "vtlPortStatus"), ("DATA-DOMAIN-MIB", "vtlPortTrapIndex"), ("DATA-DOMAIN-MIB", "vtlStatsPort"), ("DATA-DOMAIN-MIB", "vtlStatsConrolCommands"), ("DATA-DOMAIN-MIB", "vtlStatsWriteCommands"), ("DATA-DOMAIN-MIB", "vtlStatsReadCommands"), ("DATA-DOMAIN-MIB", "vtlStatsIn"), ("DATA-DOMAIN-MIB", "vtlStatsOut"), ("DATA-DOMAIN-MIB", "vtlStatsLinkFailures"), ("DATA-DOMAIN-MIB", "vtlStatsLIPCount"), ("DATA-DOMAIN-MIB", "vtlStatsSyncLosses"), ("DATA-DOMAIN-MIB", "vtlStatsSignalLosses"), ("DATA-DOMAIN-MIB", "vtlStatsPrimSeqProtoErrors"), ("DATA-DOMAIN-MIB", "vtlStatsInvalidTxWords"), ("DATA-DOMAIN-MIB", "vtlStatsInvalidCRCs"), ("DATA-DOMAIN-MIB", "vtlTapeBarCode"), ("DATA-DOMAIN-MIB", "vtlTapePool"), ("DATA-DOMAIN-MIB", "vtlTapeLocation"), ("DATA-DOMAIN-MIB", "vtlTapeState"), ("DATA-DOMAIN-MIB", "vtlTapeSize"), ("DATA-DOMAIN-MIB", "vtlTapeUsed"), ("DATA-DOMAIN-MIB", "vtlTapeComp"), ("DATA-DOMAIN-MIB", "vtlTapeModTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vtlGroup = vtlGroup.setStatus('current')
ddboostGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 15)).setObjects(("DATA-DOMAIN-MIB", "ddboostAccessClientsName"), ("DATA-DOMAIN-MIB", "ddboostAccessClientsEncryStrength"), ("DATA-DOMAIN-MIB", "ddboostAccessClientsAuthMode"), ("DATA-DOMAIN-MIB", "ddboostInterface"), ("DATA-DOMAIN-MIB", "ddboostifGroupMember"), ("DATA-DOMAIN-MIB", "ddboostBackupConnections"), ("DATA-DOMAIN-MIB", "ddboostRestoreConnections"), ("DATA-DOMAIN-MIB", "ddboostControlConnections"), ("DATA-DOMAIN-MIB", "ddboostTotalConnections"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryNetwork"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPreComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPostComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryErrors"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDate"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryTime"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsNetworkSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsPreCompSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsFiltered"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLocalComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsCompRatio"), ("DATA-DOMAIN-MIB", "ddboostIfGroupInterface"), ("DATA-DOMAIN-MIB", "ddboostOptionsName"), ("DATA-DOMAIN-MIB", "ddboostOptionsStatus"), ("DATA-DOMAIN-MIB", "ddboostStatus"), ("DATA-DOMAIN-MIB", "ddboostUser"), ("DATA-DOMAIN-MIB", "ddboostIfGroupStatus"), ("DATA-DOMAIN-MIB", "ddboostPreCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostPostCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostNetworkKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostStatsBackupConn"), ("DATA-DOMAIN-MIB", "ddboostStatsRestoreConn"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsPrecompBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterFiltering"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterLc"), ("DATA-DOMAIN-MIB", "ddboostStatsNetworkBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsCompressionRatio"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadCount"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadErrors"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitName"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitBytes"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitGlobalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitLocalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitMetaData"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInNetworkKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutNetworkKBPerSec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddboostGroup = ddboostGroup.setStatus('deprecated')
ddsystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 16)).setObjects(("DATA-DOMAIN-MIB", "systemLicenseKey"), ("DATA-DOMAIN-MIB", "systemLicenseFeature"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseKey"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseFeature"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseModel"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseCapacity"), ("DATA-DOMAIN-MIB", "systemHardwareSlot"), ("DATA-DOMAIN-MIB", "systemHardwareVendor"), ("DATA-DOMAIN-MIB", "systemHardwareDevice"), ("DATA-DOMAIN-MIB", "systemHardwarePorts"), ("DATA-DOMAIN-MIB", "systemPortsPort"), ("DATA-DOMAIN-MIB", "systemPortsConnectionType"), ("DATA-DOMAIN-MIB", "systemPortsLinkSpeed"), ("DATA-DOMAIN-MIB", "systemPortsFirmware"), ("DATA-DOMAIN-MIB", "systemPortsHardwareAddress"), ("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "systemCurrentTime"), ("DATA-DOMAIN-MIB", "systemVersion"), ("DATA-DOMAIN-MIB", "systemModelNumber"), ("DATA-DOMAIN-MIB", "sysNotes"), ("DATA-DOMAIN-MIB", "systemTimeZoneName"), ("DATA-DOMAIN-MIB", "systemUserName"), ("DATA-DOMAIN-MIB", "systemUserUID"), ("DATA-DOMAIN-MIB", "systemUserRole"), ("DATA-DOMAIN-MIB", "systemUserStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddsystemGroup = ddsystemGroup.setStatus('deprecated')
artGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 17)).setObjects(("DATA-DOMAIN-MIB", "artConfigStatus"), ("DATA-DOMAIN-MIB", "artConfigMigrationSchedule"), ("DATA-DOMAIN-MIB", "artConfigDefaultAge"), ("DATA-DOMAIN-MIB", "artConfigFileSystemClean"), ("DATA-DOMAIN-MIB", "artConfigCompression"), ("DATA-DOMAIN-MIB", "artMigrationPolicyMtreeName"), ("DATA-DOMAIN-MIB", "artMigrationPolicyDefaultAge"), ("DATA-DOMAIN-MIB", "artMigrationScheduleSchedule"), ("DATA-DOMAIN-MIB", "artMigrationScheduleStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    artGroup = artGroup.setStatus('current')
mtreeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 18)).setObjects(("DATA-DOMAIN-MIB", "mtreeCompressionMtreePath"), ("DATA-DOMAIN-MIB", "mtreeCompressionPreCompGib"), ("DATA-DOMAIN-MIB", "mtreeCompressionPostCompGib"), ("DATA-DOMAIN-MIB", "mtreeCompressionGlobalCompFactor"), ("DATA-DOMAIN-MIB", "mtreeCompressionLocalCompFactor"), ("DATA-DOMAIN-MIB", "mtreeCompressionPostTotalCompFactor"), ("DATA-DOMAIN-MIB", "mtreeCompressionTimePeriod"), ("DATA-DOMAIN-MIB", "mtreeListMtreeName"), ("DATA-DOMAIN-MIB", "mtreeListPreCompGib"), ("DATA-DOMAIN-MIB", "mtreeListStatus"), ("DATA-DOMAIN-MIB", "mtreeRetentionLockMtreeName"), ("DATA-DOMAIN-MIB", "mtreeRetentionLockStatus"), ("DATA-DOMAIN-MIB", "mtreeRetentionLockUUID"), ("DATA-DOMAIN-MIB", "mtreeRetentionLockMinRetentionPeriod"), ("DATA-DOMAIN-MIB", "mtreeRetentionLockMaxRetentionPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mtreeGroup = mtreeGroup.setStatus('current')
enclosureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 19)).setObjects(("DATA-DOMAIN-MIB", "enclosureListNum"), ("DATA-DOMAIN-MIB", "enclosureListModel"), ("DATA-DOMAIN-MIB", "enclosureListSerialNum"), ("DATA-DOMAIN-MIB", "enclosureListOemName"), ("DATA-DOMAIN-MIB", "enclosureListOemValue"), ("DATA-DOMAIN-MIB", "enclosureListCapacity"), ("DATA-DOMAIN-MIB", "enclosurePackID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    enclosureGroup = enclosureGroup.setStatus('current')
managedObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 20)).setObjects(("DATA-DOMAIN-MIB", "managedSystemHostname"), ("DATA-DOMAIN-MIB", "managedSystemSerial"), ("DATA-DOMAIN-MIB", "managedSystemState"), ("DATA-DOMAIN-MIB", "managedSystemStatus"), ("DATA-DOMAIN-MIB", "managedSystemDDOSVersion"), ("DATA-DOMAIN-MIB", "managedSystemHDSyncTime"), ("DATA-DOMAIN-MIB", "managedSystemCDSyncTime"), ("DATA-DOMAIN-MIB", "taskHistoryUser"), ("DATA-DOMAIN-MIB", "taskHistoryID"), ("DATA-DOMAIN-MIB", "taskHistoryParent"), ("DATA-DOMAIN-MIB", "taskHistoryName"), ("DATA-DOMAIN-MIB", "taskHistoryState"), ("DATA-DOMAIN-MIB", "taskHistoryStartTime"), ("DATA-DOMAIN-MIB", "taskHistoryDuration"), ("DATA-DOMAIN-MIB", "taskActiveUser"), ("DATA-DOMAIN-MIB", "taskActiveID"), ("DATA-DOMAIN-MIB", "taskActiveParent"), ("DATA-DOMAIN-MIB", "taskActiveName"), ("DATA-DOMAIN-MIB", "taskActiveState"), ("DATA-DOMAIN-MIB", "taskActiveStartTime"), ("DATA-DOMAIN-MIB", "taskActiveDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    managedObjectsGroup = managedObjectsGroup.setStatus('current')
networkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 21)).setObjects(("DATA-DOMAIN-MIB", "dnsServer"), ("DATA-DOMAIN-MIB", "searchDomainsName"), ("DATA-DOMAIN-MIB", "snmpTrapHostsName"), ("DATA-DOMAIN-MIB", "snmpTrapHostsVersion"), ("DATA-DOMAIN-MIB", "nisDomain"), ("DATA-DOMAIN-MIB", "nisServers"), ("DATA-DOMAIN-MIB", "nisAdminGroups"), ("DATA-DOMAIN-MIB", "nisUserGroups"), ("DATA-DOMAIN-MIB", "nisBackupOperatorGroups"), ("DATA-DOMAIN-MIB", "nisEnabled"), ("DATA-DOMAIN-MIB", "nisStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    networkGroup = networkGroup.setStatus('current')
fileSystemGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 22)).setObjects(("DATA-DOMAIN-MIB", "fileSystemStatus"), ("DATA-DOMAIN-MIB", "fileSystemVirtualSpace"), ("DATA-DOMAIN-MIB", "fileSystemResourceName"), ("DATA-DOMAIN-MIB", "fileSystemSpaceSize"), ("DATA-DOMAIN-MIB", "fileSystemSpaceUsed"), ("DATA-DOMAIN-MIB", "fileSystemSpaceAvail"), ("DATA-DOMAIN-MIB", "fileSystemPercentUsed"), ("DATA-DOMAIN-MIB", "fileSystemSpaceCleanable"), ("DATA-DOMAIN-MIB", "fileSystemResourceTier"), ("DATA-DOMAIN-MIB", "fileSystemCompressionPeriod"), ("DATA-DOMAIN-MIB", "fileSystemCompressionStartTime"), ("DATA-DOMAIN-MIB", "fileSystemCompressionEndTime"), ("DATA-DOMAIN-MIB", "fileSystemPreCompressionSize"), ("DATA-DOMAIN-MIB", "fileSystemPostCompressionSize"), ("DATA-DOMAIN-MIB", "fileSystemGlobalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemLocalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemTotalCompressionFactor"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitName"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitState"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitStatus"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitStartTime"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitEndTime"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitSize"), ("DATA-DOMAIN-MIB", "fileSystemArchiveUnitDiskGroups"), ("DATA-DOMAIN-MIB", "fileSystemCleanStatus"), ("DATA-DOMAIN-MIB", "fileSystemCleanSchedule"), ("DATA-DOMAIN-MIB", "fileSystemCleanThrottle"), ("DATA-DOMAIN-MIB", "fileSystemReductionPercent1"), ("DATA-DOMAIN-MIB", "fileSystemOptionsName"), ("DATA-DOMAIN-MIB", "fileSystemOptionsValue"), ("DATA-DOMAIN-MIB", "fileSystemUpTime"), ("DATA-DOMAIN-MIB", "fileSystemStatusMessage"), ("DATA-DOMAIN-MIB", "fileSystemResourceTrapIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fileSystemGroupRev1 = fileSystemGroupRev1.setStatus('current')
ddsystemGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 23)).setObjects(("DATA-DOMAIN-MIB", "systemLicenseKey"), ("DATA-DOMAIN-MIB", "systemLicenseFeature"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseKey"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseFeature"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseModel"), ("DATA-DOMAIN-MIB", "systemCapacityLicenseCapacity"), ("DATA-DOMAIN-MIB", "systemHardwareVendor"), ("DATA-DOMAIN-MIB", "systemHardwareDevice"), ("DATA-DOMAIN-MIB", "systemHardwarePorts"), ("DATA-DOMAIN-MIB", "systemHardwareSlotName"), ("DATA-DOMAIN-MIB", "systemPortsPort"), ("DATA-DOMAIN-MIB", "systemPortsConnectionType"), ("DATA-DOMAIN-MIB", "systemPortsLinkSpeed"), ("DATA-DOMAIN-MIB", "systemPortsFirmware"), ("DATA-DOMAIN-MIB", "systemPortsHardwareAddress"), ("DATA-DOMAIN-MIB", "systemSerialNumber"), ("DATA-DOMAIN-MIB", "systemCurrentTime"), ("DATA-DOMAIN-MIB", "systemVersion"), ("DATA-DOMAIN-MIB", "systemModelNumber"), ("DATA-DOMAIN-MIB", "systemTimeZoneName"), ("DATA-DOMAIN-MIB", "systemUserName"), ("DATA-DOMAIN-MIB", "systemUserUID"), ("DATA-DOMAIN-MIB", "systemUserRole"), ("DATA-DOMAIN-MIB", "systemUserStatus"), ("DATA-DOMAIN-MIB", "systemActiveUserName"), ("DATA-DOMAIN-MIB", "systemActiveUserIdleTime"), ("DATA-DOMAIN-MIB", "systemActiveUserLoginTime"), ("DATA-DOMAIN-MIB", "systemActiveUserLoginFrom"), ("DATA-DOMAIN-MIB", "systemActiveUserTty"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddsystemGroupRev1 = ddsystemGroupRev1.setStatus('current')
smtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 24)).setObjects(("DATA-DOMAIN-MIB", "smtStatus"), ("DATA-DOMAIN-MIB", "tenantUnitListName"), ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfMgmtUsers"), ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfMtrees"), ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfDdboostStus"), ("DATA-DOMAIN-MIB", "tenantUnitListTenantSelfServiceMode"), ("DATA-DOMAIN-MIB", "tenantUnitListParentTenantName"), ("DATA-DOMAIN-MIB", "tenantUnitListType"), ("DATA-DOMAIN-MIB", "tenantUnitListSecurityMode"), ("DATA-DOMAIN-MIB", "tenantUnitListNumberOfMgmtGroups"), ("DATA-DOMAIN-MIB", "tenantUnitMgmtUserListUserRole"), ("DATA-DOMAIN-MIB", "tenantUnitMtreeListMtreeName"), ("DATA-DOMAIN-MIB", "tenantUnitDdboostStuListStuName"), ("DATA-DOMAIN-MIB", "tenantUnitAdminIpInfoType"), ("DATA-DOMAIN-MIB", "tenantInfoTenantName"), ("DATA-DOMAIN-MIB", "tenantInfoTenantUnitName"), ("DATA-DOMAIN-MIB", "tenantUnitMgmtGroupListGroupRole"), ("DATA-DOMAIN-MIB", "tenantUnitMgmtGroupListGroupType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smtGroup = smtGroup.setStatus('current')
quotaGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 25)).setObjects(("DATA-DOMAIN-MIB", "quotaCapacityStatus"), ("DATA-DOMAIN-MIB", "quotaCapacityMtreeName"), ("DATA-DOMAIN-MIB", "quotaCapacityPreCompMiB"), ("DATA-DOMAIN-MIB", "quotaCapacitySoftLimitMiB"), ("DATA-DOMAIN-MIB", "quotaCapacityHardLimitMiB"), ("DATA-DOMAIN-MIB", "quotaCapacityTenantUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    quotaGroup = quotaGroup.setStatus('current')
ddboostGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 26)).setObjects(("DATA-DOMAIN-MIB", "ddboostAccessClientsName"), ("DATA-DOMAIN-MIB", "ddboostInterface"), ("DATA-DOMAIN-MIB", "ddboostifGroupMember"), ("DATA-DOMAIN-MIB", "ddboostBackupConnections"), ("DATA-DOMAIN-MIB", "ddboostRestoreConnections"), ("DATA-DOMAIN-MIB", "ddboostControlConnections"), ("DATA-DOMAIN-MIB", "ddboostTotalConnections"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryNetwork"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPreComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPostComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryErrors"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDate"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryTime"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsNetworkSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsPreCompSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsFiltered"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLocalComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsCompRatio"), ("DATA-DOMAIN-MIB", "ddboostIfGroupInterface"), ("DATA-DOMAIN-MIB", "ddboostOptionsName"), ("DATA-DOMAIN-MIB", "ddboostOptionsStatus"), ("DATA-DOMAIN-MIB", "ddboostStatus"), ("DATA-DOMAIN-MIB", "ddboostUserName"), ("DATA-DOMAIN-MIB", "ddboostIfGroupStatus"), ("DATA-DOMAIN-MIB", "ddboostPreCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostPostCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostNetworkKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostStatsBackupConn"), ("DATA-DOMAIN-MIB", "ddboostStatsRestoreConn"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsPrecompBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterFiltering"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterLc"), ("DATA-DOMAIN-MIB", "ddboostStatsNetworkBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsCompressionRatio"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadCount"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadErrors"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitName"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitBytes"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitGlobalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitLocalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitMetaData"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInNetworkKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutNetworkKBPerSec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddboostGroupRev1 = ddboostGroupRev1.setStatus('deprecated')
ddboostGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 27)).setObjects(("DATA-DOMAIN-MIB", "ddboostAccessClientsName"), ("DATA-DOMAIN-MIB", "ddboostInterface"), ("DATA-DOMAIN-MIB", "ddboostifGroupMember"), ("DATA-DOMAIN-MIB", "ddboostBackupConnections"), ("DATA-DOMAIN-MIB", "ddboostRestoreConnections"), ("DATA-DOMAIN-MIB", "ddboostControlConnections"), ("DATA-DOMAIN-MIB", "ddboostTotalConnections"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryNetwork"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPreComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryPostComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryErrors"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryDate"), ("DATA-DOMAIN-MIB", "ddboostFileReplHistoryTime"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsDirection"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsNetworkSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsPreCompSent"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsFiltered"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLowBWOpt"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsLocalComp"), ("DATA-DOMAIN-MIB", "ddboostFileReplStatsCompRatio"), ("DATA-DOMAIN-MIB", "ddboostIfGroupInterface"), ("DATA-DOMAIN-MIB", "ddboostOptionsName"), ("DATA-DOMAIN-MIB", "ddboostOptionsStatus"), ("DATA-DOMAIN-MIB", "ddboostStatus"), ("DATA-DOMAIN-MIB", "ddboostUserName"), ("DATA-DOMAIN-MIB", "ddboostUserDefaultTenantUnit"), ("DATA-DOMAIN-MIB", "ddboostIfGroupName"), ("DATA-DOMAIN-MIB", "ddboostIfGroupCurrentStatus"), ("DATA-DOMAIN-MIB", "ddboostPreCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostPostCompKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostNetworkKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostReadKBytesPerSecond"), ("DATA-DOMAIN-MIB", "ddboostStatsBackupConn"), ("DATA-DOMAIN-MIB", "ddboostStatsRestoreConn"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageCreatesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesCount"), ("DATA-DOMAIN-MIB", "ddboostStatsImageDeletesErrors"), ("DATA-DOMAIN-MIB", "ddboostStatsPrecompBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterFiltering"), ("DATA-DOMAIN-MIB", "ddboostStatsBytesAfterLc"), ("DATA-DOMAIN-MIB", "ddboostStatsNetworkBytesReceived"), ("DATA-DOMAIN-MIB", "ddboostStatsCompressionRatio"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadCount"), ("DATA-DOMAIN-MIB", "ddboostStatsTotalBytesReadErrors"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitName"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitBytes"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitGlobalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitLocalComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitMetaData"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitStatus"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitPreComp"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitUser"), ("DATA-DOMAIN-MIB", "ddboostStorageUnitReportPhysicalSize"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfInNetworkKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutPreCompKBPerSec"), ("DATA-DOMAIN-MIB", "ddboostFileRepliPerfOutNetworkKBPerSec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ddboostGroupRev2 = ddboostGroupRev2.setStatus('current')
highAvailabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 28)).setObjects(("DATA-DOMAIN-MIB", "haSystemName"), ("DATA-DOMAIN-MIB", "haSystemStatus"), ("DATA-DOMAIN-MIB", "haInterconnectStatus"), ("DATA-DOMAIN-MIB", "haPrimaryHeartbeatStatus"), ("DATA-DOMAIN-MIB", "haExternalLanHeartbeatStatus"), ("DATA-DOMAIN-MIB", "haHardwareCompatibilityCheck"), ("DATA-DOMAIN-MIB", "haSoftwareVersionCheck"), ("DATA-DOMAIN-MIB", "highAvailabilityNodeName"), ("DATA-DOMAIN-MIB", "highAvailabilityNodeId"), ("DATA-DOMAIN-MIB", "highAvailabilityNodeRole"), ("DATA-DOMAIN-MIB", "highAvailabilityNodeState"), ("DATA-DOMAIN-MIB", "highAvailabilityNodeHealth"), ("DATA-DOMAIN-MIB", "highAvailabilityComponentName"), ("DATA-DOMAIN-MIB", "highAvailabilityComponentState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    highAvailabilityGroup = highAvailabilityGroup.setStatus('current')
scsitargetObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 29)).setObjects(("DATA-DOMAIN-MIB", "scsitargetAdminState"), ("DATA-DOMAIN-MIB", "scsitargetProcessState"), ("DATA-DOMAIN-MIB", "scsitargetGroupName"), ("DATA-DOMAIN-MIB", "scsitargetGroupService"), ("DATA-DOMAIN-MIB", "scsitargetGroupActiveState"), ("DATA-DOMAIN-MIB", "scsitargetGroupNumInitiators"), ("DATA-DOMAIN-MIB", "scsitargetGroupNumDevices"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorName"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorSystemAddress"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorGroup"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorService"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorAddressMethod"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorTransport"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorFcWwpn"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorFcWwnn"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorFcSymbolicPortName"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorEndpInitiator"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorEndpEndpoint"), ("DATA-DOMAIN-MIB", "scsitargetInitiatorEndpStatus"), ("DATA-DOMAIN-MIB", "scsitargetEndpointName"), ("DATA-DOMAIN-MIB", "scsitargetEndpointCurrentSystemAddress"), ("DATA-DOMAIN-MIB", "scsitargetEndpointPrimarySystemAddress"), ("DATA-DOMAIN-MIB", "scsitargetEndpointSecondarySystemAddress"), ("DATA-DOMAIN-MIB", "scsitargetEndpointEnabled"), ("DATA-DOMAIN-MIB", "scsitargetEndpointStatus"), ("DATA-DOMAIN-MIB", "scsitargetEndpointTransport"), ("DATA-DOMAIN-MIB", "scsitargetEndpointFcWwnn"), ("DATA-DOMAIN-MIB", "scsitargetEndpointFcWwpn"), ("DATA-DOMAIN-MIB", "scsitargetPortSystemAddress"), ("DATA-DOMAIN-MIB", "scsitargetPortEnabled"), ("DATA-DOMAIN-MIB", "scsitargetPortStatus"), ("DATA-DOMAIN-MIB", "scsitargetPortTransport"), ("DATA-DOMAIN-MIB", "scsitargetPortOperationalStatus"), ("DATA-DOMAIN-MIB", "scsitargetPortFcNpiv"), ("DATA-DOMAIN-MIB", "scsitargetPortPortId"), ("DATA-DOMAIN-MIB", "scsitargetPortModel"), ("DATA-DOMAIN-MIB", "scsitargetPortFirmware"), ("DATA-DOMAIN-MIB", "scsitargetPortFcBaseWwnn"), ("DATA-DOMAIN-MIB", "scsitargetPortFcBaseWwpn"), ("DATA-DOMAIN-MIB", "scsitargetPortFcCurrentWwnn"), ("DATA-DOMAIN-MIB", "scsitargetPortFcCurrentWwpn"), ("DATA-DOMAIN-MIB", "scsitargetPortFcp2Retry"), ("DATA-DOMAIN-MIB", "scsitargetPortConnectionType"), ("DATA-DOMAIN-MIB", "scsitargetPortLinkSpeed"), ("DATA-DOMAIN-MIB", "scsitargetPortFcTopology"), ("DATA-DOMAIN-MIB", "scsitargetPortEndpPort"), ("DATA-DOMAIN-MIB", "scsitargetPortEndpEndpoint"), ("DATA-DOMAIN-MIB", "scsitargetPortEndpEnabled"), ("DATA-DOMAIN-MIB", "scsitargetPortEndpStatus"), ("DATA-DOMAIN-MIB", "scsitargetPortEndpCurrentInstance"), ("DATA-DOMAIN-MIB", "scsitargetDeviceName"), ("DATA-DOMAIN-MIB", "scsitargetDeviceService"), ("DATA-DOMAIN-MIB", "scsitargetDeviceActiveState"), ("DATA-DOMAIN-MIB", "scsitargetDeviceAddress"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpDevice"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpGroupName"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpLun"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpPrimaryEndpoints"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpSecondaryEndpoints"), ("DATA-DOMAIN-MIB", "scsitargetDeviceGrpInUseEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    scsitargetObjectGroup = scsitargetObjectGroup.setStatus('current')
cifsGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 19746, 0, 2, 30)).setObjects(("DATA-DOMAIN-MIB", "cifsStatus"), ("DATA-DOMAIN-MIB", "cifsConfigMode"), ("DATA-DOMAIN-MIB", "cifsConfigWINSServer"), ("DATA-DOMAIN-MIB", "cifsConfigNetBIOSHostname"), ("DATA-DOMAIN-MIB", "cifsConfigDomainController"), ("DATA-DOMAIN-MIB", "cifsConfigDNS"), ("DATA-DOMAIN-MIB", "cifsConfigGroupName"), ("DATA-DOMAIN-MIB", "cifsConfigMaxConnection"), ("DATA-DOMAIN-MIB", "cifsConfigMaxOpenFiles"), ("DATA-DOMAIN-MIB", "cifsShareName"), ("DATA-DOMAIN-MIB", "cifsSharePath"), ("DATA-DOMAIN-MIB", "cifsShareClients"), ("DATA-DOMAIN-MIB", "cifsShareUser"), ("DATA-DOMAIN-MIB", "cifsShareComment"), ("DATA-DOMAIN-MIB", "cifsShareBrowsing"), ("DATA-DOMAIN-MIB", "cifsShareWriteable"), ("DATA-DOMAIN-MIB", "cifsShareMaxConnection"), ("DATA-DOMAIN-MIB", "cifsOptionsName"), ("DATA-DOMAIN-MIB", "cifsOptionsValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifsGroupRev1 = cifsGroupRev1.setStatus('current')
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", tenantUnitMgmtGroupListGroupName=tenantUnitMgmtGroupListGroupName, systemStartupAlarm=systemStartupAlarm, fans=fans, FanLevelTC=FanLevelTC, targetDriverPortCore=targetDriverPortCore, mtreeCompressionEntry=mtreeCompressionEntry, fileSystemResourceTier=fileSystemResourceTier, scsitargetPortIndex=scsitargetPortIndex, ddsystemGroupRev1=ddsystemGroupRev1, vtlInitiatorStatus=vtlInitiatorStatus, FileSystemStatusTC=FileSystemStatusTC, quotaCapacity=quotaCapacity, historicalDatabaseUpgradeError=historicalDatabaseUpgradeError, FileSystemCleanScheduleTC=FileSystemCleanScheduleTC, RaidDiskStateTC=RaidDiskStateTC, haInterconnectStatus=haInterconnectStatus, taskActiveTable=taskActiveTable, encryptionKeyExportFailed=encryptionKeyExportFailed, ddboostTotalConnections=ddboostTotalConnections, unusableHostCertificate=unusableHostCertificate, DateTC=DateTC, currentAlertTimestamp=currentAlertTimestamp, scsitargetPortEnabled=scsitargetPortEnabled, HaStatusTC=HaStatusTC, TempSensorIndexTC=TempSensorIndexTC, scsitargetPortFirmware=scsitargetPortFirmware, vtlStatsSignalLosses=vtlStatsSignalLosses, ddboostIfGroupConfigTable=ddboostIfGroupConfigTable, systemCurrentTime=systemCurrentTime, ddboostStorageUnit=ddboostStorageUnit, foreignEnclosure=foreignEnclosure, nfsSendPercentage=nfsSendPercentage, mtreeListStatus=mtreeListStatus, enclosureListNum=enclosureListNum, vtlDriveModel=vtlDriveModel, scsitargetPortFcCurrentWwnn=scsitargetPortFcCurrentWwnn, controllerUnreachableAlert=controllerUnreachableAlert, nisEnabled=nisEnabled, replPerformanceWaitingDest=replPerformanceWaitingDest, unknown=unknown, replLogFull=replLogFull, CifsStatusTC=CifsStatusTC, scsitargetDeviceGrpPrimaryEndpoints=scsitargetDeviceGrpPrimaryEndpoints, fanProperties=fanProperties, ddboostFileReplHistoryPostComp=ddboostFileReplHistoryPostComp, nfsActive=nfsActive, scsitargetEndpointTransport=scsitargetEndpointTransport, fileSystemOptionsName=fileSystemOptionsName, highAvailabilityStatus=highAvailabilityStatus, raidReconCriticalShutdownAlarm=raidReconCriticalShutdownAlarm, fanLevel=fanLevel, tenantUnitListTable=tenantUnitListTable, ddboostIfGroupConfigIndex=ddboostIfGroupConfigIndex, FanDescriptionTC=FanDescriptionTC, nvramBatteryTable=nvramBatteryTable, VtlStatsPrimSeqProtoErrorsTC=VtlStatsPrimSeqProtoErrorsTC, nvramWarning=nvramWarning, FileSystemResourceIndexTC=FileSystemResourceIndexTC, fileSystemReductionPercent1=fileSystemReductionPercent1, ddboostStorageUnitStatus=ddboostStorageUnitStatus, tapeReposition=tapeReposition, mtreeRetentionLockMaxRetentionPeriod=mtreeRetentionLockMaxRetentionPeriod, vtlLibraryModel=vtlLibraryModel, dDFSRequiresReboot=dDFSRequiresReboot, dataDomainSystem=dataDomainSystem, replPreCompBytesRemaining=replPreCompBytesRemaining, artMigrationPolicyDefaultAge=artMigrationPolicyDefaultAge, systemStatsIndex=systemStatsIndex, vtlConfiguration=vtlConfiguration, vtlLibraryRevision=vtlLibraryRevision, tempSensorIndex=tempSensorIndex, powerModuleStatus=powerModuleStatus, systemCapacityLicenseIndex=systemCapacityLicenseIndex, haPrimaryHeartbeatStatus=haPrimaryHeartbeatStatus, sASEnclosureCheck=sASEnclosureCheck, dDFSDiedAfterReboot=dDFSDiedAfterReboot, replPathTooLong=replPathTooLong, mtreeCompressionLocalCompFactor=mtreeCompressionLocalCompFactor, replGroup=replGroup, cifsStatus=cifsStatus, SystemTimeZoneNameTC=SystemTimeZoneNameTC, smiMrc=smiMrc, highAvailabilityNodeTable=highAvailabilityNodeTable, fileSystemCleanIndex=fileSystemCleanIndex, currentAlertSeverity=currentAlertSeverity, CifsSharePathTC=CifsSharePathTC, unsupportedSystemType=unsupportedSystemType, nvramBatteryEntry=nvramBatteryEntry, dataDomainMibTraps=dataDomainMibTraps, nvramHWAlert=nvramHWAlert, quotaGroup=quotaGroup, spaceReclSuspended=spaceReclSuspended, artMigrationPolicyEntry=artMigrationPolicyEntry, nfsGroup=nfsGroup, tenantUnitMgmtGroupListEntry=tenantUnitMgmtGroupListEntry, vtlPortTable=vtlPortTable, ddboostStatsEntry=ddboostStatsEntry, storageMigrationCopyComplete=storageMigrationCopyComplete, vtlLibraryTable=vtlLibraryTable, ddboostFileRepliPerfInNetworkKBPerSec=ddboostFileRepliPerfInNetworkKBPerSec, systemUserEntry=systemUserEntry, fileSystemCleanTable=fileSystemCleanTable, vtlLibraryStatus=vtlLibraryStatus, interfaceConnectivityIntermittent=interfaceConnectivityIntermittent, compromisedEncryptionKeys=compromisedEncryptionKeys, dataDomainMibComplianceRev1=dataDomainMibComplianceRev1, vtlPool=vtlPool, cifsConfigWINSServer=cifsConfigWINSServer, diskReallocCount=diskReallocCount, DDMibInteger32TC=DDMibInteger32TC, internalDiskStorageGroup=internalDiskStorageGroup, dd990=dd990, ddsystemGroup=ddsystemGroup, vtlGroupDeviceGroupName=vtlGroupDeviceGroupName, NvramHCPropertyBytesTC=NvramHCPropertyBytesTC, cifsConfigMode=cifsConfigMode, vtlGroupDeviceSecondaryPorts=vtlGroupDeviceSecondaryPorts, ddboostFileReplStatsLowBWOpt=ddboostFileReplStatsLowBWOpt, VtlStatsInvalidTxWordsTC=VtlStatsInvalidTxWordsTC, artConfig=artConfig, tenantUnitMgmtUserListTable=tenantUnitMgmtUserListTable, systemCapacityLicenseFeature=systemCapacityLicenseFeature, snmpTrapHostsEntry=snmpTrapHostsEntry, CifsShareMaxConnectionTC=CifsShareMaxConnectionTC, legacyChassisTempWarning=legacyChassisTempWarning, dd860=dd860, scsitargetPortSystemAddress=scsitargetPortSystemAddress, snmpTrapHostsIndex=snmpTrapHostsIndex, vtlLibrary=vtlLibrary, nfsActivePath=nfsActivePath, vtlPortEntry=vtlPortEntry, powerModules=powerModules, ddboostFileReplicationHistoryTable=ddboostFileReplicationHistoryTable, ddboostConnections=ddboostConnections, DdboostAccessClientsAuthModeTC=DdboostAccessClientsAuthModeTC, targetDriverPortOnline=targetDriverPortOnline, nvramBatteryLowChargeAlert=nvramBatteryLowChargeAlert, ReplicationThrottleTC=ReplicationThrottleTC, DDMibTableIndexTC=DDMibTableIndexTC, replConfigEnabled=replConfigEnabled, FileSystemCompressionFactorTC=FileSystemCompressionFactorTC, alerts=alerts, diskPropEnclosureID=diskPropEnclosureID, unsupportedConfigurationROL=unsupportedConfigurationROL, vtlTapeState=vtlTapeState, scsitargetInitiatorAddressMethod=scsitargetInitiatorAddressMethod, systemCapacityLicenseTable=systemCapacityLicenseTable, highAvailabilityComponent=highAvailabilityComponent, DDStatusTC=DDStatusTC, diskBusyPercentage=diskBusyPercentage, diskTimeoutCount=diskTimeoutCount, upgradeCompleted=upgradeCompleted, scsitargetDeviceGrpEntry=scsitargetDeviceGrpEntry, dataDomainMibComplianceRev5=dataDomainMibComplianceRev5, vtlProperties=vtlProperties, systemPortsTable=systemPortsTable, snmpTrapHostsTable=snmpTrapHostsTable, VtlPortIndexTC=VtlPortIndexTC, vtlPoolComp=vtlPoolComp, ddboostStatsBytesAfterFiltering=ddboostStatsBytesAfterFiltering, dd670=dd670, nfsPort=nfsPort, NvramBatteryStatusTC=NvramBatteryStatusTC, replIncompatibleWorm=replIncompatibleWorm, ddboostStatsImageDeletesErrors=ddboostStatsImageDeletesErrors, tenantUnitList=tenantUnitList, NfsStatsFileHandleLookupTC=NfsStatsFileHandleLookupTC, replicationPerformanceTable=replicationPerformanceTable, interfaceConnectivityDown=interfaceConnectivityDown, targetDriverPortOffline=targetDriverPortOffline, ddboostIfGroupName=ddboostIfGroupName, powerModuleTable=powerModuleTable, cifsShareMaxConnection=cifsShareMaxConnection, DDMibTableEnabledTC=DDMibTableEnabledTC, replicationInfoEntry=replicationInfoEntry, CifsShareWriteableTC=CifsShareWriteableTC, highAvailabilityNodeHealth=highAvailabilityNodeHealth, nvramStatsEntry=nvramStatsEntry, mtreeRetentionLock=mtreeRetentionLock, CifsConfigGroupNameTC=CifsConfigGroupNameTC, scsitargetEndpointName=scsitargetEndpointName, raidGroupMissingAlarm=raidGroupMissingAlarm, nfsActiveIndex=nfsActiveIndex, nfsClient=nfsClient, dd160=dd160, diskSASHBAAlarm=diskSASHBAAlarm, scsitargetPort=scsitargetPort, diskSASAlarm=diskSASAlarm, managedSystemHDSyncTime=managedSystemHDSyncTime, fileSystemArchiveUnitStatus=fileSystemArchiveUnitStatus, fileSystemStatus=fileSystemStatus, diskAccessError=diskAccessError, VtlDriveTapeVolumeTC=VtlDriveTapeVolumeTC, mtreeCompressionTable=mtreeCompressionTable, enclosureListOemName=enclosureListOemName, searchDomains=searchDomains, invalidNICSlot=invalidNICSlot, ddboostReadKBytesPerSecond=ddboostReadKBytesPerSecond, ddboostInterface=ddboostInterface, ddboostStatsNetworkBytesReceived=ddboostStatsNetworkBytesReceived, generatedNotificationsGroup=generatedNotificationsGroup, FileSystemSpaceUnitTC=FileSystemSpaceUnitTC, dDFSFailedInShutdown=dDFSFailedInShutdown, vtlLibraryName=vtlLibraryName, scsitargetGroupName=scsitargetGroupName, vtlDriveEntry=vtlDriveEntry, ddboostUserTable=ddboostUserTable, fileSystemArchiveUnitTable=fileSystemArchiveUnitTable, cifsOptionsTable=cifsOptionsTable, currentAlertEntry=currentAlertEntry, vtlTapeEntry=vtlTapeEntry, cifsShareTable=cifsShareTable, hAdegraded=hAdegraded, powerSupplyFailedAlarm=powerSupplyFailedAlarm, hAofflineErrors=hAofflineErrors, DiskStateTC=DiskStateTC, fileSystemArchiveUnitEndTime=fileSystemArchiveUnitEndTime, ddboostUserDefaultTenantUnit=ddboostUserDefaultTenantUnit, tenantInfoTenantName=tenantInfoTenantName, diskErrTrapIndex=diskErrTrapIndex, replHistorySyncedAsOfTime=replHistorySyncedAsOfTime, fileSystemArchiveUnitIndex=fileSystemArchiveUnitIndex, scsitargetDeviceAddress=scsitargetDeviceAddress, restorer=restorer, diskFirmwareVersion=diskFirmwareVersion, enclosurePack=enclosurePack, diskPerfIndex=diskPerfIndex, vtlPoolEntry=vtlPoolEntry, tempSensorTrapIndex=tempSensorTrapIndex, enclosure=enclosure, nfsClientClients=nfsClientClients, NfsStatsMaxCacheSizeTC=NfsStatsMaxCacheSizeTC, bMCFailure=bMCFailure, cifsShareComment=cifsShareComment, nvramStats=nvramStats, vtlInitiatorTable=vtlInitiatorTable, sNTZMultipleIterations=sNTZMultipleIterations, mtreeListPreCompGib=mtreeListPreCompGib, diskGroupReconstructionCritical=diskGroupReconstructionCritical, fanDescription=fanDescription, VtlStatsLinkFailuresTC=VtlStatsLinkFailuresTC, VtlLibraryIndexTC=VtlLibraryIndexTC, nfsPortTable=nfsPortTable, dd530=dd530, powerUnitWarning=powerUnitWarning, scsitargetInitiatorIndex=scsitargetInitiatorIndex, searchDomainsIndex=searchDomainsIndex, mtreeCompressionMtreePath=mtreeCompressionMtreePath, upgradeInProgress=upgradeInProgress, scsitargetAdminState=scsitargetAdminState, scsitargetEndpointCurrentSystemAddress=scsitargetEndpointCurrentSystemAddress, scsitargetInitiatorEndpIndex=scsitargetInitiatorEndpIndex, mtreeListIndex=mtreeListIndex, vtlStatsPrimSeqProtoErrors=vtlStatsPrimSeqProtoErrors)
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", ReplicationConfigConnHostTC=ReplicationConfigConnHostTC, dd460g=dd460g, diskCrcErrCount=diskCrcErrCount, ddboostRestoreConnections=ddboostRestoreConnections, VtlLibraryTotalCapsTC=VtlLibraryTotalCapsTC, quotaCapacityPreCompMiB=quotaCapacityPreCompMiB, nvramReadKBytesPerSecond=nvramReadKBytesPerSecond, nvramStatsTable=nvramStatsTable, DDMibTableString128TC=DDMibTableString128TC, ddboostAccessClientsIndex=ddboostAccessClientsIndex, ddboostIfGroupConfig=ddboostIfGroupConfig, ddboostFileReplicationHistory=ddboostFileReplicationHistory, artConfigCompression=artConfigCompression, replicationInfo=replicationInfo, systemUserRole=systemUserRole, vtlPoolTapes=vtlPoolTapes, NfsClientOptionsTC=NfsClientOptionsTC, diskProperties=diskProperties, diskPathSpeedDegraded=diskPathSpeedDegraded, ddboostFileReplicationStatsEntry=ddboostFileReplicationStatsEntry, scsitargetPortStatus=scsitargetPortStatus, quotaCapacityMtreeName=quotaCapacityMtreeName, cifsProperties=cifsProperties, nvramBatteryIndex=nvramBatteryIndex, highAvailabilityComponentEntry=highAvailabilityComponentEntry, historicalDatabaseBackupError=historicalDatabaseBackupError, fileSystemSpaceAvail=fileSystemSpaceAvail, VtlPortConnectionTypeTC=VtlPortConnectionTypeTC, scsitargetPortTable=scsitargetPortTable, ErrorCount=ErrorCount, fileSystemCleanThrottle=fileSystemCleanThrottle, vtlInitiatorEntry=vtlInitiatorEntry, replicationHistory=replicationHistory, taskActiveParent=taskActiveParent, MtreeListStatusTC=MtreeListStatusTC, vtlGroupDeviceCount=vtlGroupDeviceCount, cifsConfigNetBIOSHostname=cifsConfigNetBIOSHostname, scsitargetEndpointIndex=scsitargetEndpointIndex, systemPortsIndex=systemPortsIndex, ddboostFileReplicationStatsTable=ddboostFileReplicationStatsTable, artMigrationScheduleTable=artMigrationScheduleTable, NfsStatusTC=NfsStatusTC, replHistoryTime=replHistoryTime, ddboostFileReplHistoryNetwork=ddboostFileReplHistoryNetwork, apollo=apollo, fileSystemPercentUsed=fileSystemPercentUsed, scsitargetInitiatorService=scsitargetInitiatorService, DDMibTableSizeGibTC=DDMibTableSizeGibTC, SystemSerialNumberTC=SystemSerialNumberTC, unsupportedNIC=unsupportedNIC, replDestination=replDestination, filesystemProblem=filesystemProblem, filesysDDGCFailedAlarm=filesysDDGCFailedAlarm, diskOverheatShutdownAlarm=diskOverheatShutdownAlarm, systemLicenseKey=systemLicenseKey, vtlDrive=vtlDrive, scsitargetPortConnectionType=scsitargetPortConnectionType, VtlPortEnabledTC=VtlPortEnabledTC, systemSerialNumber=systemSerialNumber, PowerModuleStatusTC=PowerModuleStatusTC, legacyFanWarning=legacyFanWarning, replLagThreshholdReached=replLagThreshholdReached, nfsActiveTable=nfsActiveTable, vtl=vtl, systemPortsEntry=systemPortsEntry, dnsEntry=dnsEntry, snmpTrapHostsVersion=snmpTrapHostsVersion, ddboostFileRepliPerfOutNetworkKBPerSec=ddboostFileRepliPerfOutNetworkKBPerSec, systemHardwarePorts=systemHardwarePorts, MtreeRetentionLockStatusTC=MtreeRetentionLockStatusTC, cifsShareBrowsing=cifsShareBrowsing, powerSupplyAbsent=powerSupplyAbsent, DiskCapacityTC=DiskCapacityTC, nfsStatsFilesystemType=nfsStatsFilesystemType, lowSpares=lowSpares, replSyncAlarm=replSyncAlarm, managedSystemIndex=managedSystemIndex, replicationConfigTable=replicationConfigTable, NfsClientClientsTC=NfsClientClientsTC, powerSupplyFailure=powerSupplyFailure, fileSpaceSevereAlarm=fileSpaceSevereAlarm, cifsOptionsName=cifsOptionsName, filesysRelaunchAlarm=filesysRelaunchAlarm, tenantInfoTenantUnitName=tenantInfoTenantUnitName, nfsStatsCurrentOpenStreams=nfsStatsCurrentOpenStreams, cifsOptionsIndex=cifsOptionsIndex, missingCreplUnits=missingCreplUnits, duplicateAddressDetection=duplicateAddressDetection, alertInfoDescription=alertInfoDescription, taskActiveUser=taskActiveUser, scsitargetInitiatorEndpInitiator=scsitargetInitiatorEndpInitiator, powerSupplyWarning=powerSupplyWarning, scsitargetPortTransport=scsitargetPortTransport, CifsConfigWINSServerTC=CifsConfigWINSServerTC, systemOverheatWarningAlarm=systemOverheatWarningAlarm, replicationHistoryTable=replicationHistoryTable, nfsProperties=nfsProperties, scsitargetPortFcTopology=scsitargetPortFcTopology, vtlStatsInvalidTxWords=vtlStatsInvalidTxWords, nfs=nfs, tenantUnitDdboostStuListEntry=tenantUnitDdboostStuListEntry, diskProbationalCount=diskProbationalCount, dd400g=dd400g, VtlPortIDTC=VtlPortIDTC, vtlPoolStatus=vtlPoolStatus, systemPortsFirmware=systemPortsFirmware, ddboostStatsPrecompBytesReceived=ddboostStatsPrecompBytesReceived, diskPathRedundancy=diskPathRedundancy, fileSystemResourceIndex=fileSystemResourceIndex, mtreeRetentionLockTable=mtreeRetentionLockTable, fileSystemProperties=fileSystemProperties, nvramMemoryErrorCount=nvramMemoryErrorCount, VtlLibraryNameTC=VtlLibraryNameTC, diskPropTrapIndex=diskPropTrapIndex, nfsReceivePercentage=nfsReceivePercentage, dd510=dd510, vtlLibraryEntry=vtlLibraryEntry, diskMiscFailCount=diskMiscFailCount, ddboostFileReplStatsFiltered=ddboostFileReplStatsFiltered, mtreeList=mtreeList, vtlTapeUsed=vtlTapeUsed, haSystemName=haSystemName, powerModuleIndex=powerModuleIndex, vtlDriveRevision=vtlDriveRevision, vtlGroups=vtlGroups, fanEnclosureID=fanEnclosureID, fileSystemArchiveUnitState=fileSystemArchiveUnitState, ddboostIfGroupEntry=ddboostIfGroupEntry, taskHistoryEntry=taskHistoryEntry, sASHBAErrors=sASHBAErrors, ReplicationConfigDestTC=ReplicationConfigDestTC, ddboostFileReplStatsCompRatio=ddboostFileReplStatsCompRatio, ddboostIfGroupCurrentStatus=ddboostIfGroupCurrentStatus, systemActiveUserName=systemActiveUserName, PYSNMP_MODULE_ID=dataDomainMib, vtlPortSpeed=vtlPortSpeed, snmpTrapHosts=snmpTrapHosts, tenantUnitAdminIpInfoAddr=tenantUnitAdminIpInfoAddr, newEncryptionKey=newEncryptionKey, fileSystemArchiveUnitName=fileSystemArchiveUnitName, CifsShareIndexTC=CifsShareIndexTC, highAvailabilityNodeId=highAvailabilityNodeId, nvramEnvAlert=nvramEnvAlert, systemVersion=systemVersion, VtlPortWWPNTC=VtlPortWWPNTC, expiredHostCertificate=expiredHostCertificate, fileSystemSpaceEntry=fileSystemSpaceEntry, vtlDriveTapeVolume=vtlDriveTapeVolume, multipleDiskReadErrors=multipleDiskReadErrors, DDMibTimeStampTC=DDMibTimeStampTC, vtlPortID=vtlPortID, nfsPortEntry=nfsPortEntry, coredumpWarning=coredumpWarning, mtreeCompressionTimePeriod=mtreeCompressionTimePeriod, systemHardwareIndex=systemHardwareIndex, ddboostGroupRev2=ddboostGroupRev2, pCILinkDegraded=pCILinkDegraded, scsitargetDeviceService=scsitargetDeviceService, vtlGroupDeviceEntry=vtlGroupDeviceEntry, VtlTapeStateTC=VtlTapeStateTC, openFanDrawer=openFanDrawer, NfsStatsFilesystemTypeTC=NfsStatsFilesystemTypeTC, systemHardwareVendor=systemHardwareVendor, quotaCapacityEntry=quotaCapacityEntry, memoryRiserFault=memoryRiserFault, replConfigConnPort=replConfigConnPort, scsitargetDeviceName=scsitargetDeviceName, portPathDisabled=portPathDisabled, mtreeCompressionPostTotalCompFactor=mtreeCompressionPostTotalCompFactor, diskPerformance=diskPerformance, ReplicationContextTC=ReplicationContextTC, quotaCapacityStatus=quotaCapacityStatus, systemCapacityLicenseEntry=systemCapacityLicenseEntry, vtlPoolIndex=vtlPoolIndex, replTrapContext=replTrapContext, ddboostStatsTable=ddboostStatsTable, vDiskSCSITargetMismatch=vDiskSCSITargetMismatch, vtlTapePool=vtlTapePool, mgmtModuleFault=mgmtModuleFault, missingHostCertificate=missingHostCertificate, FileSystemArchiveUnitStateTC=FileSystemArchiveUnitStateTC, artMigrationPolicyTable=artMigrationPolicyTable, systemActiveUserLoginTime=systemActiveUserLoginTime, CifsConfigMaxConnectionTC=CifsConfigMaxConnectionTC, scsitargetEndpointStatus=scsitargetEndpointStatus, raidReconSevereAlarm=raidReconSevereAlarm, vtlInitiatorWWPN=vtlInitiatorWWPN, ddboostIfGroupConfigEntry=ddboostIfGroupConfigEntry, vtlTapeComp=vtlTapeComp, ddboostPostCompKBytesPerSecond=ddboostPostCompKBytesPerSecond, nvramProperties=nvramProperties, replicationConfig=replicationConfig, spaceOver80Percent=spaceOver80Percent, nfsPortIndex=nfsPortIndex, VtlTapeUsedTC=VtlTapeUsedTC, DDboostStatsIndexTC=DDboostStatsIndexTC, scsitargetEndpointPrimarySystemAddress=scsitargetEndpointPrimarySystemAddress, uncorrectableECCerror=uncorrectableECCerror, scsitargetPortEndpTable=scsitargetPortEndpTable, mtreeRetentionLockMtreeName=mtreeRetentionLockMtreeName, abnormalShutdown=abnormalShutdown, powerSupplyInputFault=powerSupplyInputFault, containerMarkedInvalid=containerMarkedInvalid, replHistoryPostFiltered=replHistoryPostFiltered, ddms=ddms, mtreeCompressionGlobalCompFactor=mtreeCompressionGlobalCompFactor, nisStatus=nisStatus, tenantUnitDdboostStuListTable=tenantUnitDdboostStuListTable, nISCommFailure=nISCommFailure, dNSUnresponsive=dNSUnresponsive, dataDomainMibConformance=dataDomainMibConformance, mtreeCompressionPostCompGib=mtreeCompressionPostCompGib, replHistoryDate=replHistoryDate, fileSystemSpace=fileSystemSpace, scsitargetPortFcCurrentWwpn=scsitargetPortFcCurrentWwpn, nfsStats=nfsStats, replPerformanceBusyReading=replPerformanceBusyReading, VtlDriveSerialTC=VtlDriveSerialTC, scsitargetPortFcBaseWwnn=scsitargetPortFcBaseWwnn, vtlLibraryVendor=vtlLibraryVendor, ddboostIfGroupIdx=ddboostIfGroupIdx, DDMibMemorySizeTC=DDMibMemorySizeTC, nvramErrorAlert=nvramErrorAlert, CifsShareClientsTC=CifsShareClientsTC, physicalCapacityMeasurementTasksLost=physicalCapacityMeasurementTasksLost, tcpZeroWindowAlert=tcpZeroWindowAlert, mtreeListMtreeName=mtreeListMtreeName, CifsStatsDetailsIndexTC=CifsStatsDetailsIndexTC, FileSystemCleanIndexTC=FileSystemCleanIndexTC, systemCapacityLicense=systemCapacityLicense, taskActiveID=taskActiveID, diskUnsupportedAlarm=diskUnsupportedAlarm, tempEnclosureID=tempEnclosureID, vtlDriveLibraryName=vtlDriveLibraryName, systemLicenseEntry=systemLicenseEntry, tenantInfo=tenantInfo, systemStatsEntry=systemStatsEntry, spaceReclError=spaceReclError, vtlPoolUsed=vtlPoolUsed, diskSectorsRead=diskSectorsRead, VtlPortStatusTC=VtlPortStatusTC, ddboostFileReplStatsPreCompSent=ddboostFileReplStatsPreCompSent, diskErrIndex=diskErrIndex, ReplicationConfigSourceTC=ReplicationConfigSourceTC, duplicateVTLPoolNames=duplicateVTLPoolNames, ddboostStorageUnitPreComp=ddboostStorageUnitPreComp, VtlDriveVendorTC=VtlDriveVendorTC, replHistoryPostLocalComp=replHistoryPostLocalComp, cifsShareName=cifsShareName, sPFault=sPFault, smt=smt, nfsStatsMaxCacheSize=nfsStatsMaxCacheSize, insufficientSpaceForEncryption=insufficientSpaceForEncryption, temperatureSensorTable=temperatureSensorTable)
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", nfsStatsEntry=nfsStatsEntry, alertHistoryIndex=alertHistoryIndex, nfsStatsExportPoint=nfsStatsExportPoint, nis=nis, vtlStatsEntry=vtlStatsEntry, hATimeOutOfSync=hATimeOutOfSync, fileSystemCompressionTable=fileSystemCompressionTable, diskErrEnclosureID=diskErrEnclosureID, cpismissing=cpismissing, artMigrationScheduleSchedule=artMigrationScheduleSchedule, systemStatsTable=systemStatsTable, ddboostBackupConnections=ddboostBackupConnections, snapshotOver90Percent=snapshotOver90Percent, vtlInitiatorWWNN=vtlInitiatorWWNN, cifsConfigMaxConnection=cifsConfigMaxConnection, smtGroup=smtGroup, vtlPort=vtlPort, systemUserName=systemUserName, nfsClientPath=nfsClientPath, scsitargetProcessState=scsitargetProcessState, artMigrationScheduleEntry=artMigrationScheduleEntry, NfsClientPathTC=NfsClientPathTC, tenantInfoTable=tenantInfoTable, storageUnitStreamSoftLimit=storageUnitStreamSoftLimit, DDMibString96TC=DDMibString96TC, quotaProperties=quotaProperties, replPerformancePreCompKBPerSec=replPerformancePreCompKBPerSec, tenantInfoIdx=tenantInfoIdx, vtlGroupEntry=vtlGroupEntry, targetDriverPortTooManyOsc=targetDriverPortTooManyOsc, nvramPropertiesEntry=nvramPropertiesEntry, systemCapacityLicenseKey=systemCapacityLicenseKey, nvramCondAlert=nvramCondAlert, dd880g=dd880g, dd120=dd120, highAvailabilityComponentTable=highAvailabilityComponentTable, systemCapacityLicenseCapacity=systemCapacityLicenseCapacity, diskTotalKBytes=diskTotalKBytes, VtlLibraryVendorTC=VtlLibraryVendorTC, tenantUnitMgmtUserListEntry=tenantUnitMgmtUserListEntry, tenantUnitAdminIpInfoTable=tenantUnitAdminIpInfoTable, alertHistorySeverity=alertHistorySeverity, diskSectorsWritten=diskSectorsWritten, scsitargetGroupTable=scsitargetGroupTable, legacyPowerSupplyWarning=legacyPowerSupplyWarning, cMTaskEnded=cMTaskEnded, fanIndex=fanIndex, ddboostIfGroupStatus=ddboostIfGroupStatus, systemReset=systemReset, replConfigLowBWOptim=replConfigLowBWOptim, ddboost=ddboost, alertHistory=alertHistory, tenantInfoTenantUnitEntry=tenantInfoTenantUnitEntry, fileSystemVirtualSpace=fileSystemVirtualSpace, alertHistoryStatus=alertHistoryStatus, ddboostStats=ddboostStats, systemPortsConnectionType=systemPortsConnectionType, ReplicationPathTC=ReplicationPathTC, taskHistoryUser=taskHistoryUser, vtlPortFirmware=vtlPortFirmware, scsitarget=scsitarget, VtlDriveRevisionTC=VtlDriveRevisionTC, replicationConfigEntry=replicationConfigEntry, vtlPortModel=vtlPortModel, sASTopologyCheck=sASTopologyCheck, scsitargetEndpointSecondarySystemAddress=scsitargetEndpointSecondarySystemAddress, FileSystemOptionsValueTC=FileSystemOptionsValueTC, diskPropState=diskPropState, ddboostFileReplHistoryLowBWOpt=ddboostFileReplHistoryLowBWOpt, targetDriverPortFWLoadFailed=targetDriverPortFWLoadFailed, managedSystem=managedSystem, scsitargetEndpointEnabled=scsitargetEndpointEnabled, tenantUnitListSecurityMode=tenantUnitListSecurityMode, ddboostFileReplicationStats=ddboostFileReplicationStats, ddboostFileReplHistoryPreComp=ddboostFileReplHistoryPreComp, artConfigTable=artConfigTable, tenantUnitMtreeListTable=tenantUnitMtreeListTable, targetDriverPortMultipleCore=targetDriverPortMultipleCore, bMCHangShutdown=bMCHangShutdown, driveMixType=driveMixType, vtlStatsInvalidCRCs=vtlStatsInvalidCRCs, DDMibTableString64TC=DDMibTableString64TC, systemLicenseFeature=systemLicenseFeature, diskGroupReconstruction=diskGroupReconstruction, spaceOver90Percent=spaceOver90Percent, systemHardwareTable=systemHardwareTable, scsitargetInitiatorFcWwnn=scsitargetInitiatorFcWwnn, fileSystemFailedAlarm=fileSystemFailedAlarm, alertInfoTable=alertInfoTable, dataDomainMibCompliance=dataDomainMibCompliance, ReplicationTrafficTC=ReplicationTrafficTC, vtlProcessState=vtlProcessState, scsitargetPortOperationalStatus=scsitargetPortOperationalStatus, cifsOpsPerSecond=cifsOpsPerSecond, taskHistoryTable=taskHistoryTable, scsitargetDeviceGrpTable=scsitargetDeviceGrpTable, ddboostConnectionsTable=ddboostConnectionsTable, VtlStatsIndexTC=VtlStatsIndexTC, scsitargetInitiatorFcWwpn=scsitargetInitiatorFcWwpn, uncertifiedFirmware=uncertifiedFirmware, ddboostStatsTotalBytesReadErrors=ddboostStatsTotalBytesReadErrors, systemPorts=systemPorts, vtlTapeSize=vtlTapeSize, tenantUnitListEntry=tenantUnitListEntry, nvramStatsIndex=nvramStatsIndex, tenantUnitMtreeListEntry=tenantUnitMtreeListEntry, correctableErrorWarning=correctableErrorWarning, tenantUnitListNumberOfMgmtGroups=tenantUnitListNumberOfMgmtGroups, dd660=dd660, vtlAdminState=vtlAdminState, ddboostFileRepliPerfOutPreCompKBPerSec=ddboostFileRepliPerfOutPreCompKBPerSec, scsitargetDeviceEntry=scsitargetDeviceEntry, fileSystemArchiveUnit=fileSystemArchiveUnit, invalidHardwareCritical=invalidHardwareCritical, nvramBatteryAlert=nvramBatteryAlert, diskPack=diskPack, dd4200=dd4200, replSource=replSource, dataDomainMibGroups=dataDomainMibGroups, vtlStatsIndex=vtlStatsIndex, mtreeListTable=mtreeListTable, PowerModuleDescriptionTC=PowerModuleDescriptionTC, fanStatus=fanStatus, DDMibAlertSeverityTC=DDMibAlertSeverityTC, nvramFailingAlarm=nvramFailingAlarm, enclosureMixType=enclosureMixType, replInKBytesPerSecond=replInKBytesPerSecond, nvramPropertiesIndex=nvramPropertiesIndex, scsitargetDeviceGrpInUseEndpoints=scsitargetDeviceGrpInUseEndpoints, NfsStatsIndexTC=NfsStatsIndexTC, noHistoricalDatabaseError=noHistoricalDatabaseError, fileSystemPostCompressionSize=fileSystemPostCompressionSize, coredumpDisabled=coredumpDisabled, highAvailabilityNodeEntry=highAvailabilityNodeEntry, systemProperties=systemProperties, missingSlaveInterface=missingSlaveInterface, DDMibTableString1024TC=DDMibTableString1024TC, vtlLibraryTotalSlots=vtlLibraryTotalSlots, dd690=dd690, cifsShareEntry=cifsShareEntry, vtlTapeIndex=vtlTapeIndex, enclosureListEntry=enclosureListEntry, iOModuleMacFault=iOModuleMacFault, diskFailure=diskFailure, cifsConfigMaxOpenFilesPerConnection=cifsConfigMaxOpenFilesPerConnection, cifsOptionsValue=cifsOptionsValue, dd630=dd630, bMCHangCritical=bMCHangCritical, scsitargetPortEndpIndex=scsitargetPortEndpIndex, iOModuleInserted=iOModuleInserted, artMigrationScheduleStatus=artMigrationScheduleStatus, systemHardwareDevice=systemHardwareDevice, diskReadKBytesPerSecond=diskReadKBytesPerSecond, tenantUnitMtreeList=tenantUnitMtreeList, nfsActiveEntry=nfsActiveEntry, ddboostAccessClientsEntry=ddboostAccessClientsEntry, diskReliabilityEntry=diskReliabilityEntry, tenantInfoTenantUnitTable=tenantInfoTenantUnitTable, diskWriteFailCount=diskWriteFailCount, nisUserGroups=nisUserGroups, fileSystemCompressionEndTime=fileSystemCompressionEndTime, ddboostFileReplHistoryIndex=ddboostFileReplHistoryIndex, nvramBatteries=nvramBatteries, nfsIdlePercentage=nfsIdlePercentage, chassisFailure=chassisFailure, fileSystemOptionsValue=fileSystemOptionsValue, clusterInterfaceAlarm=clusterInterfaceAlarm, ddboostConnectionsEntry=ddboostConnectionsEntry, storageMigrationCannotResume=storageMigrationCannotResume, unsupportedDriveModel=unsupportedDriveModel, currentAlerts=currentAlerts, mtreeRetentionLockEntry=mtreeRetentionLockEntry, ddboostAccessClientsName=ddboostAccessClientsName, nfsPortPort=nfsPortPort, systemPortsHardwareAddress=systemPortsHardwareAddress, replFileSysStatus=replFileSysStatus, artMigrationPolicy=artMigrationPolicy, unsupportedHardwareConfig=unsupportedHardwareConfig, VtlLibraryModelTC=VtlLibraryModelTC, vtlPortConnectionType=vtlPortConnectionType, KBytesPerSecond=KBytesPerSecond, vTLDisabled=vTLDisabled, ddboostStorageUnitTable=ddboostStorageUnitTable, alertHistoryTimestamp=alertHistoryTimestamp, fileSystemArchiveUnitSize=fileSystemArchiveUnitSize, fileSystemOptionsIndex=fileSystemOptionsIndex, SystemStatsIndexTC=SystemStatsIndexTC, highAvailabilityNodeState=highAvailabilityNodeState, taskActiveState=taskActiveState, managedSystemTable=managedSystemTable, dd580=dd580, tenantUnitListTenantSelfServiceMode=tenantUnitListTenantSelfServiceMode, quota=quota, ReplicationConfigIndexTC=ReplicationConfigIndexTC, VtlTapeBarCodeTC=VtlTapeBarCodeTC, scsitargetEndpointEntry=scsitargetEndpointEntry, ddboostConnectionsIndex=ddboostConnectionsIndex, diskCapacity=diskCapacity, diskOverheatAlertAlarm=diskOverheatAlertAlarm, vTLEnabled=vTLEnabled, highAvailabilityNodeName=highAvailabilityNodeName, ddboostStatsRestoreConn=ddboostStatsRestoreConn, PowerModuleIndexTC=PowerModuleIndexTC, vtlDriveName=vtlDriveName, vtlPortEnabled=vtlPortEnabled, filesysGeneralProblemAlarm=filesysGeneralProblemAlarm, scsitargetPortFcNpiv=scsitargetPortFcNpiv, temperatureSensorEntry=temperatureSensorEntry, temperatureSensors=temperatureSensors, NvramMemorySizeTC=NvramMemorySizeTC, historicalDatabaseFailoverError=historicalDatabaseFailoverError, systemLicenseIndex=systemLicenseIndex, scsitargetPortModel=scsitargetPortModel, fileSystemSpaceUsed=fileSystemSpaceUsed, fileSystemArchiveUnitDiskGroups=fileSystemArchiveUnitDiskGroups, DDMibTrafficBytesTC=DDMibTrafficBytesTC, fileSystemArchiveUnitStartTime=fileSystemArchiveUnitStartTime, tempSensorDescription=tempSensorDescription, diskPropertiesEntry=diskPropertiesEntry, ddboostStatsTotalBytesReadCount=ddboostStatsTotalBytesReadCount, interfaceConnectivityUpAndRunning=interfaceConnectivityUpAndRunning, generalHardwareFailure=generalHardwareFailure, environmentalsGroup=environmentalsGroup, dDFSRebootedDisabled=dDFSRebootedDisabled, currentAlertDescription=currentAlertDescription, replHistoryPostLowBwOptim=replHistoryPostLowBwOptim, NfsStatsCurrentOpenStreamsTC=NfsStatsCurrentOpenStreamsTC, fileSystemGroupRev1=fileSystemGroupRev1, forcedControllerShutdown=forcedControllerShutdown, scsitargetDeviceGrpGroupName=scsitargetDeviceGrpGroupName, taskHistoryID=taskHistoryID, vtlTape=vtlTape, unsupportedEnclosurePSU=unsupportedEnclosurePSU, fanTrapIndex=fanTrapIndex, alertHistoryEntry=alertHistoryEntry, OpsPerSecond=OpsPerSecond, ddboostFileReplStatsNetworkSent=ddboostFileReplStatsNetworkSent, NfsClientIndexTC=NfsClientIndexTC, ddboostOptionsEntry=ddboostOptionsEntry, externalUnmanagedDiskStorageGroup=externalUnmanagedDiskStorageGroup, environmentals=environmentals, cpuMaxPercentageBusy=cpuMaxPercentageBusy, CifsConfigDomainControllerTC=CifsConfigDomainControllerTC, sSDEndOfLife=sSDEndOfLife, alertInfoEntry=alertInfoEntry, systemHardware=systemHardware, fanPropertiesTable=fanPropertiesTable, dd560g=dd560g, taskHistoryName=taskHistoryName, scsitargetPortEndpEndpoint=scsitargetPortEndpEndpoint, replPostCompBytesReceived=replPostCompBytesReceived, CifsConfigDNSTC=CifsConfigDNSTC, encryptionKeyTableFull=encryptionKeyTableFull, spaceReclMissingUnit=spaceReclMissingUnit)
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", snmpTrapHostsName=snmpTrapHostsName, NfsStatsCacheEntryTC=NfsStatsCacheEntryTC, nvramWindowSize=nvramWindowSize, CifsConfigMaxOpenFilesPerConnectionTC=CifsConfigMaxOpenFilesPerConnectionTC, nfsPortService=nfsPortService, nfsActiveClients=nfsActiveClients, powerModuleDescription=powerModuleDescription, tenantUnitAdminIpInfo=tenantUnitAdminIpInfo, ddboostStorageUnitLocalComp=ddboostStorageUnitLocalComp, ReplicationStatusTC=ReplicationStatusTC, managedSystemState=managedSystemState, correctableECCLimitReached=correctableECCLimitReached, diskOverheatWarningAlarm=diskOverheatWarningAlarm, enclosureListTable=enclosureListTable, enclosureListModel=enclosureListModel, fileSystemResourceName=fileSystemResourceName, vtlDriveTable=vtlDriveTable, ddboostUserIdx=ddboostUserIdx, ddboostFileReplicationHistoryEntry=ddboostFileReplicationHistoryEntry, foreignPack=foreignPack, nvramPropertiesTable=nvramPropertiesTable, fileSystemCleanSchedule=fileSystemCleanSchedule, dd200=dd200, VtlTapeSizeTC=VtlTapeSizeTC, cifsConfig=cifsConfig, systemHardwareSlotName=systemHardwareSlotName, scsitargetInitiatorFcSymbolicPortName=scsitargetInitiatorFcSymbolicPortName, correctECCWarning=correctECCWarning, nfsClientOptions=nfsClientOptions, dDFSDied=dDFSDied, systemUserTable=systemUserTable, dataDomainMibCompliances=dataDomainMibCompliances, haHardwareCompatibilityCheck=haHardwareCompatibilityCheck, artGroup=artGroup, enclosureList=enclosureList, ddboostAccessClientsEncryStrength=ddboostAccessClientsEncryStrength, replConfigSource=replConfigSource, ddboostIfGroupTable=ddboostIfGroupTable, VtlStatsConrolCommandsTC=VtlStatsConrolCommandsTC, vtlLibrarySerial=vtlLibrarySerial, ReplicationSyncedTimeTC=ReplicationSyncedTimeTC, scsitargetInitiatorName=scsitargetInitiatorName, snapshotFullAlarm=snapshotFullAlarm, VtlDriveIndexTC=VtlDriveIndexTC, basicNotificationsGroup=basicNotificationsGroup, scsitargetInitiatorGroup=scsitargetInitiatorGroup, AlertTimestampTC=AlertTimestampTC, vtlInitiator=vtlInitiator, ddboostAccessClientsAuthMode=ddboostAccessClientsAuthMode, mtreeRetentionLockUUID=mtreeRetentionLockUUID, replConnTime=replConnTime, scsitargetEndpointFcWwnn=scsitargetEndpointFcWwnn, powerEnclosureID=powerEnclosureID, nvramBatteriesIndex=nvramBatteriesIndex, scsitargetInitiatorEndpStatus=scsitargetInitiatorEndpStatus, fileSystemCompression=fileSystemCompression, systemOverheatAlertAlarm=systemOverheatAlertAlarm, vtlPortIndex=vtlPortIndex, CifsOptionsNameTC=CifsOptionsNameTC, systemStats=systemStats, cifsSharePath=cifsSharePath, quotaCapacityHardLimitMiB=quotaCapacityHardLimitMiB, physicalCapacityMeasurementScheduleFailed=physicalCapacityMeasurementScheduleFailed, dnsIndex=dnsIndex, fanModuleFailedAlarm=fanModuleFailedAlarm, voltageWarning=voltageWarning, cifsGroupRev1=cifsGroupRev1, DDMibTableSizeMiBTC=DDMibTableSizeMiBTC, fileSystemLocalCompressionFactor=fileSystemLocalCompressionFactor, tenantInfoEntry=tenantInfoEntry, replConfigIndex=replConfigIndex, fileSystemSpaceSize=fileSystemSpaceSize, dnsServer=dnsServer, diskNoSpareAlarm=diskNoSpareAlarm, nvramPCIErrorCount=nvramPCIErrorCount, vtlPortWWNN=vtlPortWWNN, taskActive=taskActive, enclosureListSerialNum=enclosureListSerialNum, diskReliabilityTable=diskReliabilityTable, FileSystemResourceNameTC=FileSystemResourceNameTC, VtlPortSpeedTC=VtlPortSpeedTC, replProgressThreshholdReached=replProgressThreshholdReached, systemUserUID=systemUserUID, storage=storage, diskReadFailCount=diskReadFailCount, VtlAdminStateTC=VtlAdminStateTC, Percentage=Percentage, bMCFailureSysBBU=bMCFailureSysBBU, systemActiveUserLoginFrom=systemActiveUserLoginFrom, snapshotLimitReached=snapshotLimitReached, smtProperties=smtProperties, enclosureListOemValue=enclosureListOemValue, ddboostFileReplicationPerformance=ddboostFileReplicationPerformance, iOModuleFault=iOModuleFault, TenantUnitMgmtGroupTypeTC=TenantUnitMgmtGroupTypeTC, tenantUnitListType=tenantUnitListType, licenseExpired=licenseExpired, ReplicationConnectTimeTC=ReplicationConnectTimeTC, dd565=dd565, fileSystem=fileSystem, dd890=dd890, taskHistoryDuration=taskHistoryDuration, ddboostFileReplHistoryErrors=ddboostFileReplHistoryErrors, ddve=ddve, dataDomainMibComplianceRev3=dataDomainMibComplianceRev3, suspendedMReplMissingUnits=suspendedMReplMissingUnits, insecureEncryptedReplication=insecureEncryptedReplication, artConfigEntry=artConfigEntry, historicalDatabaseRecoverError=historicalDatabaseRecoverError, ddboostStatsCompressionRatio=ddboostStatsCompressionRatio, ddboostOptionsName=ddboostOptionsName, DDMibTableString256TC=DDMibTableString256TC, ddboostStatsBytesAfterLc=ddboostStatsBytesAfterLc, vtlInitiatorIndex=vtlInitiatorIndex, mtreeGroup=mtreeGroup, dd560=dd560, tenantUnitListNumberOfMgmtUsers=tenantUnitListNumberOfMgmtUsers, cifsOptions=cifsOptions, VtlStatsReadCommandsTC=VtlStatsReadCommandsTC, ddboostStatsImageCreatesErrors=ddboostStatsImageCreatesErrors, FileSystemOptionsIndexTC=FileSystemOptionsIndexTC, mtreeQuotaHardLimit=mtreeQuotaHardLimit, enclosureGroup=enclosureGroup, ddboostStorageUnitUser=ddboostStorageUnitUser, dd860g=dd860g, unsupportedPowerSupply=unsupportedPowerSupply, scsitargetProperties=scsitargetProperties, nfsStatsCacheEntry=nfsStatsCacheEntry, vtlTapeModTime=vtlTapeModTime, DDboostStatusTC=DDboostStatusTC, ddintrepid=ddintrepid, scsitargetGroupNumInitiators=scsitargetGroupNumInitiators, tenantUnitListParentTenantName=tenantUnitListParentTenantName, nfsStatsFileHandleLookup=nfsStatsFileHandleLookup, vtlGroupIndex=vtlGroupIndex, artConfigDefaultAge=artConfigDefaultAge, networkGroup=networkGroup, FileSystemArchiveUnitStatusTC=FileSystemArchiveUnitStatusTC, taskHistoryIndex=taskHistoryIndex, taskHistoryStartTime=taskHistoryStartTime, scsitargetGroup=scsitargetGroup, fileSystemOptions=fileSystemOptions, artMigrationScheduleIndex=artMigrationScheduleIndex, scsitargetInitiatorSystemAddress=scsitargetInitiatorSystemAddress, diskPerformanceTable=diskPerformanceTable, systemPortsLinkSpeed=systemPortsLinkSpeed, scsitargetPortFcp2Retry=scsitargetPortFcp2Retry, taskHistoryParent=taskHistoryParent, diskSerialNumber=diskSerialNumber, scsitargetEndpoint=scsitargetEndpoint, replicationHistoryEntry=replicationHistoryEntry, vtlDriveIndex=vtlDriveIndex, VtlLibraryTotalSlotsTC=VtlLibraryTotalSlotsTC, diskPathAlarm=diskPathAlarm, vtlGroupName=vtlGroupName, dd4500=dd4500, sASHBAFailure=sASHBAFailure, ddboostStorageUnitMetaData=ddboostStorageUnitMetaData, taskActiveDuration=taskActiveDuration, highAvailability=highAvailability, fileSpaceWarningAlarm=fileSpaceWarningAlarm, nvramBatteryCharge=nvramBatteryCharge, vtlTapeBarCode=vtlTapeBarCode, vtlTapeLocation=vtlTapeLocation, highAvailabilityNodeIdx=highAvailabilityNodeIdx, invalidHardwareWarning=invalidHardwareWarning, dnsTable=dnsTable, mtreeRetentionLockIndex=mtreeRetentionLockIndex, SystemNotesTC=SystemNotesTC, vtlLibraryIndex=vtlLibraryIndex, fileSystemCleanStatus=fileSystemCleanStatus, ddboostifGroupMember=ddboostifGroupMember, mtreeCompressionIndex=mtreeCompressionIndex, Temperature=Temperature, replConfigConnHost=replConfigConnHost, chassisSensorCritical=chassisSensorCritical, DdboostAccessClientsEncryStrengthTC=DdboostAccessClientsEncryStrengthTC, nisServers=nisServers, fileSystemGroup=fileSystemGroup, fileSystemCleanEntry=fileSystemCleanEntry, DiskFirmwareVersionTC=DiskFirmwareVersionTC, systemCapacityLicenseModel=systemCapacityLicenseModel, fileSystemClean=fileSystemClean, AlertDescriptionTC=AlertDescriptionTC, diskBusy=diskBusy, ddboostFileReplStatsLocalComp=ddboostFileReplStatsLocalComp, CifsShareBrowsingTC=CifsShareBrowsingTC, systemHardwareEntry=systemHardwareEntry, artConfigIndex=artConfigIndex, scsitargetDeviceGrpSecondaryEndpoints=scsitargetDeviceGrpSecondaryEndpoints, diskStorage=diskStorage, fileSystemResourceTrapIndex=fileSystemResourceTrapIndex, systemHardwareSlot=systemHardwareSlot, legacyBMCHangCritical=legacyBMCHangCritical, mtreeCascadeNeedResync=mtreeCascadeNeedResync, VtlLibraryStatusTC=VtlLibraryStatusTC, VtlLibrarySerialTC=VtlLibrarySerialTC, quotaCapacityIndex=quotaCapacityIndex, cifs=cifs, mtreeCompressionPreCompGib=mtreeCompressionPreCompGib, sCSITGTInvalidRegistry=sCSITGTInvalidRegistry, systemLicenseTable=systemLicenseTable, taskActiveIndex=taskActiveIndex, VtlStatsInvalidCRCsTC=VtlStatsInvalidCRCsTC, taskActiveStartTime=taskActiveStartTime, processorWarning=processorWarning, fileSystemReductionPercent=fileSystemReductionPercent, DiskIndexTC=DiskIndexTC, vtlGroupDeviceLun=vtlGroupDeviceLun, TempSensorStatusTC=TempSensorStatusTC, VtlTapeModTimeTC=VtlTapeModTimeTC, cleaningError=cleaningError, DDMibTableString512TC=DDMibTableString512TC, ddboostStorageUnitBytes=ddboostStorageUnitBytes, vtlGroupDeviceIndex=vtlGroupDeviceIndex, haSystemStatus=haSystemStatus, highAvailabilityNode=highAvailabilityNode, FileSystemOptionsNameTC=FileSystemOptionsNameTC, ddboostStatsIndex=ddboostStatsIndex, fileSystemUpTime=fileSystemUpTime, tenantUnitMgmtUserListUserRole=tenantUnitMgmtUserListUserRole, replHistoryPreCompressed=replHistoryPreCompressed, VtlStatsLIPCountTC=VtlStatsLIPCountTC, vtlTapeTable=vtlTapeTable, ddboostIfGroupInterface=ddboostIfGroupInterface, missingPortConnection=missingPortConnection, TempSensorDescriptionTC=TempSensorDescriptionTC, physicalCapacityMeasurementTasksLostMTree=physicalCapacityMeasurementTasksLostMTree, DiskPackTC=DiskPackTC, sMSUnresponsive=sMSUnresponsive, vtlPortWWPN=vtlPortWWPN, currentAlertID=currentAlertID, ddboostStorageUnitGlobalComp=ddboostStorageUnitGlobalComp, scsitargetInitiatorTransport=scsitargetInitiatorTransport, vtlPoolSize=vtlPoolSize, TenantUnitMgmtUserListUserRoleTC=TenantUnitMgmtUserListUserRoleTC, FanStatusTC=FanStatusTC, VtlTapeLocationTC=VtlTapeLocationTC, hDTFileTransferFailed=hDTFileTransferFailed, diskTemperatureShutdown=diskTemperatureShutdown, CifsShareUserTC=CifsShareUserTC, nvramWriteKBytesPerSecond=nvramWriteKBytesPerSecond, tenantUnitMgmtGroupList=tenantUnitMgmtGroupList, VtlLibraryRevisionTC=VtlLibraryRevisionTC, ReplicationConfigEnabledTC=ReplicationConfigEnabledTC, replicationPerformance=replicationPerformance, missingDiskPath=missingDiskPath, nvramBattAlert=nvramBattAlert, nvramHCMemorySize=nvramHCMemorySize, systemOverheatShutdownAlarm=systemOverheatShutdownAlarm, diskPropertiesTable=diskPropertiesTable, alertsGroup=alertsGroup, tenantUnitDdboostStuListStuName=tenantUnitDdboostStuListStuName, VtlPortWWNNTC=VtlPortWWNNTC)
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", dataDomainMibObjects=dataDomainMibObjects, nfsStatsTable=nfsStatsTable, upgradeFailure=upgradeFailure, vtlStatsSyncLosses=vtlStatsSyncLosses, tempSensorCurrentValue=tempSensorCurrentValue, missingEnclosurePath=missingEnclosurePath, taskHistoryState=taskHistoryState, ddboostStorageUnitIndex=ddboostStorageUnitIndex, tenantUnitListNumberOfMtrees=tenantUnitListNumberOfMtrees, dDFSNoHeartbeat=dDFSNoHeartbeat, scsitargetPortPortId=scsitargetPortPortId, fileSystemCompressionIndex=fileSystemCompressionIndex, nvramMemorySize=nvramMemorySize, nfsClientTable=nfsClientTable, systemLicense=systemLicense, enclosurePackTable=enclosurePackTable, enclosureHighTemp=enclosureHighTemp, unsupportedHardwareSpareSize=unsupportedHardwareSpareSize, EnclosureID=EnclosureID, systemActiveUserTty=systemActiveUserTty, artConfigMigrationSchedule=artConfigMigrationSchedule, scsitargetPortEndpCurrentInstance=scsitargetPortEndpCurrentInstance, diskPropIndex=diskPropIndex, DiskModelTC=DiskModelTC, VtlDriveNameTC=VtlDriveNameTC, DDboostUserTC=DDboostUserTC, fileMigrationError=fileMigrationError, diskGroupReconstructionNoProgress=diskGroupReconstructionNoProgress, scsitargetObjectGroup=scsitargetObjectGroup, enclosurePackEntry=enclosurePackEntry, diskUnknown=diskUnknown, missingDiskGroup=missingDiskGroup, diskErrState=diskErrState, dd640=dd640, replConfigDest=replConfigDest, currentAlertIndex=currentAlertIndex, dd200Proto=dd200Proto, recoverFromNVRAMFailed=recoverFromNVRAMFailed, FileSystemCleanThrottleTC=FileSystemCleanThrottleTC, vtlStatsReadCommands=vtlStatsReadCommands, systemActiveUserTable=systemActiveUserTable, power=power, ddboostStorageUnitEntry=ddboostStorageUnitEntry, scsitargetDeviceGrpDevice=scsitargetDeviceGrpDevice, spuriousInterruptDisabled=spuriousInterruptDisabled, systemModelNumber=systemModelNumber, ReplicationStateTC=ReplicationStateTC, nvramBattEndOfLife=nvramBattEndOfLife, vtlInitiatorPort=vtlInitiatorPort, ddboostControlConnections=ddboostControlConnections, internalDiskStorageNotificationsGroup=internalDiskStorageNotificationsGroup, corruptEncryptionKeys=corruptEncryptionKeys, historicalDatabasePruneError=historicalDatabasePruneError, enclosureListIndex=enclosureListIndex, cifsConfigGroupName=cifsConfigGroupName, highAvailabilityComponentName=highAvailabilityComponentName, eventIPMIUnmanageAlarm=eventIPMIUnmanageAlarm, tenantUnitListName=tenantUnitListName, tenantUnitListNumberOfDdboostStus=tenantUnitListNumberOfDdboostStus, DDMibVersionTC=DDMibVersionTC, fileSystemSpaceTable=fileSystemSpaceTable, vtlGroupDeviceTable=vtlGroupDeviceTable, vtlStatsLIPCount=vtlStatsLIPCount, dataDomainMibProducts=dataDomainMibProducts, ddboostStorageUnitReportPhysicalSize=ddboostStorageUnitReportPhysicalSize, DDMibTableString32TC=DDMibTableString32TC, VtlLibraryTotalDrivesTC=VtlLibraryTotalDrivesTC, fileSystemOptionsEntry=fileSystemOptionsEntry, scsitargetGroupNumDevices=scsitargetGroupNumDevices, quotaCapacityTable=quotaCapacityTable, managedSystemEntry=managedSystemEntry, vtlStatsLinkFailures=vtlStatsLinkFailures, unCorrectECCWarning=unCorrectECCWarning, replPerformanceBusyMeta=replPerformanceBusyMeta, tenantUnitMgmtUserListUserName=tenantUnitMgmtUserListUserName, alertHistoryDescription=alertHistoryDescription, snapshotHWMAlarm=snapshotHWMAlarm, managedObjectsGroup=managedObjectsGroup, sysNotes=sysNotes, cpuAvgPercentageBusy=cpuAvgPercentageBusy, nfsClientEntry=nfsClientEntry, scsitargetDeviceTable=scsitargetDeviceTable, replThrottle=replThrottle, scsitargetPortEndpStatus=scsitargetPortEndpStatus, enclosureListCapacity=enclosureListCapacity, artConfigStatus=artConfigStatus, scsitargetInitiatorEndpEndpoint=scsitargetInitiatorEndpEndpoint, vtlGroupDevicePrimaryPorts=vtlGroupDevicePrimaryPorts, ddboostStatsImageDeletesCount=ddboostStatsImageDeletesCount, dd880=dd880, ddboostFileReplHistoryTime=ddboostFileReplHistoryTime, fanWarning=fanWarning, artMigrationPolicyIndex=artMigrationPolicyIndex, CifsShareCommentTC=CifsShareCommentTC, diskTemperature=diskTemperature, cifsShareIndex=cifsShareIndex, storageMigrationUserSuspend=storageMigrationUserSuspend, network=network, ddboostStatsBackupConn=ddboostStatsBackupConn, dataDomainMibComplianceRev2=dataDomainMibComplianceRev2, vtlDriveSerial=vtlDriveSerial, spaceReclUnitError=spaceReclUnitError, fileSystemCompressionEntry=fileSystemCompressionEntry, ReplicationConfigContextIdTC=ReplicationConfigContextIdTC, nisDomain=nisDomain, replHistoryContext=replHistoryContext, artMigrationSchedule=artMigrationSchedule, NfsStatsExportPointTC=NfsStatsExportPointTC, VtlDriveModelTC=VtlDriveModelTC, nisAdminGroups=nisAdminGroups, systemTimeZoneName=systemTimeZoneName, nTPDFailed=nTPDFailed, replHistoryPreCompWritten=replHistoryPreCompWritten, replPerformanceNetworkKBPerSec=replPerformanceNetworkKBPerSec, targetDriverPortUnreadable=targetDriverPortUnreadable, scsitargetInitiator=scsitargetInitiator, taskHistory=taskHistory, diskPerformanceEntry=diskPerformanceEntry, replPerformanceStreams=replPerformanceStreams, replOutKBytesPerSecond=replOutKBytesPerSecond, diskPerfEnclosureID=diskPerfEnclosureID, replicationInfoTable=replicationInfoTable, chassisTempCritical=chassisTempCritical, replStatus=replStatus, sASPortDisabled=sASPortDisabled, scsitargetInitiatorTable=scsitargetInitiatorTable, vtlInitiatorGroup=vtlInitiatorGroup, ddboostAccessClients=ddboostAccessClients, fileSpaceMaintenanceAlarm=fileSpaceMaintenanceAlarm, ddboostFileReplHistoryDate=ddboostFileReplHistoryDate, searchDomainsTable=searchDomainsTable, ddboostOptions=ddboostOptions, CifsConfigModeTC=CifsConfigModeTC, nfsStatsIndex=nfsStatsIndex, highAvailabilityGroup=highAvailabilityGroup, AlertIndexTC=AlertIndexTC, fileSpacePreWarningAlarm=fileSpacePreWarningAlarm, scsitargetPortEndpEnabled=scsitargetPortEndpEnabled, fileSystemGlobalCompressionFactor=fileSystemGlobalCompressionFactor, cifsOptionsEntry=cifsOptionsEntry, scsitargetPortLinkSpeed=scsitargetPortLinkSpeed, statisticsGroup=statisticsGroup, unsupportedACVoltage=unsupportedACVoltage, dd620=dd620, diskReliability=diskReliability, ddboostOptionsTable=ddboostOptionsTable, dataDomainMibNotifications=dataDomainMibNotifications, ddboostUser=ddboostUser, cifsShareUser=cifsShareUser, ddboostOptionsIndex=ddboostOptionsIndex, scsitargetDeviceGrpLun=scsitargetDeviceGrpLun, fileSystemStatusMessage=fileSystemStatusMessage, dns=dns, vtlDriveStatus=vtlDriveStatus, clusterNodeAlarm=clusterNodeAlarm, vtlStatsIn=vtlStatsIn, scsitargetDeviceActiveState=scsitargetDeviceActiveState, ddboostGroup=ddboostGroup, CifsStatsSummaryIndexTC=CifsStatsSummaryIndexTC, DiskSerialNumberTC=DiskSerialNumberTC, ddboostUserName=ddboostUserName, systemActiveUserIndex=systemActiveUserIndex, DDMibDateTC=DDMibDateTC, VtlStatsSignalLossesTC=VtlStatsSignalLossesTC, replPreCompBytesSent=replPreCompBytesSent, scsitargetEndpointTable=scsitargetEndpointTable, vtlDriveVendor=vtlDriveVendor, managedSystemStatus=managedSystemStatus, artConfigFileSystemClean=artConfigFileSystemClean, scsitargetInitiatorEntry=scsitargetInitiatorEntry, unsupportedVirtualCPU=unsupportedVirtualCPU, metadataWarningThreshold=metadataWarningThreshold, dd7200=dd7200, ddboostFileRepliPerfInPreCompKBPerSec=ddboostFileRepliPerfInPreCompKBPerSec, ddkoalam1=ddkoalam1, dd610=dd610, VtlTapeCompTC=VtlTapeCompTC, HaSystemStatusTC=HaSystemStatusTC, ddboostStatsImageCreatesCount=ddboostStatsImageCreatesCount, dd140=dd140, diskFailedAlarm=diskFailedAlarm, controllerIfaceUnreachableAlert=controllerIfaceUnreachableAlert, diskModel=diskModel, nvramGroup=nvramGroup, spaceReclRestartFailed=spaceReclRestartFailed, nvramBatteryStatus=nvramBatteryStatus, powerModuleEntry=powerModuleEntry, VtlStatsPortTC=VtlStatsPortTC, cifsShareClients=cifsShareClients, nisBackupOperatorGroups=nisBackupOperatorGroups, VtlTapeIndexTC=VtlTapeIndexTC, dIMMFailure=dIMMFailure, CifsOptionsIndexTC=CifsOptionsIndexTC, SmtStatusTC=SmtStatusTC, fanPropertiesEntry=fanPropertiesEntry, fileSystemArchiveUnitEntry=fileSystemArchiveUnitEntry, ddboostFileReplHistoryDirection=ddboostFileReplHistoryDirection, currentAlertTable=currentAlertTable, smtStatus=smtStatus, scsitargetEndpointFcWwpn=scsitargetEndpointFcWwpn, cPUFailureWarning=cPUFailureWarning, mtreeQuotaSoftLimit=mtreeQuotaSoftLimit, filesystemCorruption=filesystemCorruption, searchDomainsEntry=searchDomainsEntry, VtlPortModelTC=VtlPortModelTC, statistics=statistics, nvramEventHWAlert=nvramEventHWAlert, scsitargetPortEndpEntry=scsitargetPortEndpEntry, systemUserIndex=systemUserIndex, nfsStatus=nfsStatus, vtlStatsPort=vtlStatsPort, scsitargetDeviceGrpIndex=scsitargetDeviceGrpIndex, legacyChassisTempCritical=legacyChassisTempCritical, FileSystemCompressionSizeTC=FileSystemCompressionSizeTC, managedSystemHostname=managedSystemHostname, cifsShareWriteable=cifsShareWriteable, interfaceMisconfiguration=interfaceMisconfiguration, systemUserStatus=systemUserStatus, highAvailabilityComponentState=highAvailabilityComponentState, raidReconCriticalAlarm=raidReconCriticalAlarm, managedSystemCDSyncTime=managedSystemCDSyncTime, diskOffTrackErrCount=diskOffTrackErrCount, nfsOpsPerSecond=nfsOpsPerSecond, taskActiveName=taskActiveName, unset=unset, vtlGroupTable=vtlGroupTable, scsitargetDeviceIndex=scsitargetDeviceIndex, FileSystemCompressionPeriodTC=FileSystemCompressionPeriodTC, fileSystemSpaceCleanable=fileSystemSpaceCleanable, ddboostAccessClientsTable=ddboostAccessClientsTable, ddboostFileReplStatsDirection=ddboostFileReplStatsDirection, VtlStatsWriteCommandsTC=VtlStatsWriteCommandsTC, dDFSRebooted=dDFSRebooted, mtree=mtree, missingTierStorage=missingTierStorage, DDMibCompressionFactorTC=DDMibCompressionFactorTC, tenantUnitAdminIpInfoType=tenantUnitAdminIpInfoType, ddboostGroupRev1=ddboostGroupRev1, dd460=dd460, alertInfo=alertInfo, mtreeRetentionLockMinRetentionPeriod=mtreeRetentionLockMinRetentionPeriod, tenantUnitMgmtGroupListTable=tenantUnitMgmtGroupListTable, tenantUnitMgmtUserList=tenantUnitMgmtUserList, tenantUnitDdboostStuList=tenantUnitDdboostStuList, ddboostOptionsStatus=ddboostOptionsStatus, dd580g=dd580g, ddboostFileReplStatsIndex=ddboostFileReplStatsIndex, enclosurePackID=enclosurePackID, systemActiveUserEntry=systemActiveUserEntry, taskActiveEntry=taskActiveEntry, nfsClientIndex=nfsClientIndex, managedSystemSerial=managedSystemSerial, systemActiveUserIdleTime=systemActiveUserIdleTime, mtreeListEntry=mtreeListEntry)
mibBuilder.exportSymbols("DATA-DOMAIN-MIB", dIMMFailureAlert=dIMMFailureAlert, sSLCertificateCorrupted=sSLCertificateCorrupted, VtlPortFirmwareTC=VtlPortFirmwareTC, replPostCompBytesSent=replPostCompBytesSent, replication=replication, VtlPortNameTC=VtlPortNameTC, replHistoryPreCompRemaining=replHistoryPreCompRemaining, ext3NvlogDisabled=ext3NvlogDisabled, fileSystemOptionsTable=fileSystemOptionsTable, mailserverError=mailserverError, DiskSectorsPerSecondTC=DiskSectorsPerSecondTC, powerWarning=powerWarning, vtlPoolPool=vtlPoolPool, cifsConfigMaxOpenFiles=cifsConfigMaxOpenFiles, dd2500=dd2500, replicationPerformanceEntry=replicationPerformanceEntry, replPerformanceWaitingNetwork=replPerformanceWaitingNetwork, NvramIndexTC=NvramIndexTC, vtlGroupInitiaterCount=vtlGroupInitiaterCount, scsitargetInitiatorEndpTable=scsitargetInitiatorEndpTable, vtlPortStatus=vtlPortStatus, vtlPortName=vtlPortName, phyalert=phyalert, tenantUnitMgmtGroupListGroupType=tenantUnitMgmtGroupListGroupType, searchDomainsName=searchDomainsName, CifsShareNameTC=CifsShareNameTC, tenantUnitListIdx=tenantUnitListIdx, scsitargetGroupActiveState=scsitargetGroupActiveState, replNeedResync=replNeedResync, dataDomainMib=dataDomainMib, VtlDriveStatusTC=VtlDriveStatusTC, temperatures=temperatures, diskPerfState=diskPerfState, scsitargetPortFcBaseWwpn=scsitargetPortFcBaseWwpn, missingLunPath=missingLunPath, replSyncedAsOfTime=replSyncedAsOfTime, ddboostStorageUnitName=ddboostStorageUnitName, mtreeCompression=mtreeCompression, highAvailabilityComponentIdx=highAvailabilityComponentIdx, replConfigTenantUnit=replConfigTenantUnit, tenantUnitMtreeListMtreeName=tenantUnitMtreeListMtreeName, replDestNotConfigured=replDestNotConfigured, tenantUnitAdminIpInfoEntry=tenantUnitAdminIpInfoEntry, dataDomainMibComplianceRev4=dataDomainMibComplianceRev4, DDMibStatusTC=DDMibStatusTC, managedSystemDDOSVersion=managedSystemDDOSVersion, nfsProcPercentage=nfsProcPercentage, hDTSystemError=hDTSystemError, CifsOptionsValueTC=CifsOptionsValueTC, vtlGroup=vtlGroup, vtlStatsConrolCommands=vtlStatsConrolCommands, vtlInitiatorName=vtlInitiatorName, FileSystemCleanStatusTC=FileSystemCleanStatusTC, cifsShare=cifsShare, CifsConfigNetBIOSHostnameTC=CifsConfigNetBIOSHostnameTC, TenantUnitSecurityModeTC=TenantUnitSecurityModeTC, NvramBatteryIndexTC=NvramBatteryIndexTC, invalidEnclosureTopology=invalidEnclosureTopology, cifsGroup=cifsGroup, art=art, licenseExpiring=licenseExpiring, scsitargetGroupIndex=scsitargetGroupIndex, vtlStatsWriteCommands=vtlStatsWriteCommands, vtlStats=vtlStats, fanFault=fanFault, replConfigContextId=replConfigContextId, chassisTempWarning=chassisTempWarning, tooManyRelaunches=tooManyRelaunches, fileSystemCompressionPeriod=fileSystemCompressionPeriod, NvramWindowSizeTC=NvramWindowSizeTC, artMigrationPolicyMtreeName=artMigrationPolicyMtreeName, scsitargetPortEntry=scsitargetPortEntry, bMCPartialHang=bMCPartialHang, vtlStatsOut=vtlStatsOut, ddboostPreCompKBytesPerSecond=ddboostPreCompKBytesPerSecond, spaceReclUnitReclaimed=spaceReclUnitReclaimed, dd430=dd430, scsitargetInitiatorEndpEntry=scsitargetInitiatorEndpEntry, replHistoryBytesNetwork=replHistoryBytesNetwork, diskSoftEccCount=diskSoftEccCount, diskWriteKBytesPerSecond=diskWriteKBytesPerSecond, PercentageStr=PercentageStr, vtlGroupDeviceInUsePorts=vtlGroupDeviceInUsePorts, memoryAlert=memoryAlert, vtlGroupDeviceDeviceName=vtlGroupDeviceDeviceName, quotaCapacityTenantUnit=quotaCapacityTenantUnit, mtreeRetentionLockStatus=mtreeRetentionLockStatus, indexRebuildComplete=indexRebuildComplete, ReplicationConfigConnPortTC=ReplicationConfigConnPortTC, fileSystemPreCompressionSize=fileSystemPreCompressionSize, fileSpaceCriticalAlarm=fileSpaceCriticalAlarm, scsitargetGroupEntry=scsitargetGroupEntry, alertHistoryTable=alertHistoryTable, vtlStatsTable=vtlStatsTable, enclosureMixDriveType=enclosureMixDriveType, fileSystemTotalCompressionFactor=fileSystemTotalCompressionFactor, haSoftwareVersionCheck=haSoftwareVersionCheck, vtlLibraryTotalCaps=vtlLibraryTotalCaps, ReplicationConfigLowBWOptimTC=ReplicationConfigLowBWOptimTC, highAvailabilityNodeRole=highAvailabilityNodeRole, VtlTapePoolTC=VtlTapePoolTC, nvram=nvram, cifsConfigDomainController=cifsConfigDomainController, ddboostNetworkKBytesPerSecond=ddboostNetworkKBytesPerSecond, Minutes=Minutes, fileSystemCompressionStartTime=fileSystemCompressionStartTime, alertInfoIndex=alertInfoIndex, dd690g=dd690g, scsitargetDevice=scsitargetDevice, quotaCapacitySoftLimitMiB=quotaCapacitySoftLimitMiB, unsupportedSASDevice=unsupportedSASDevice, tempSensorStatus=tempSensorStatus, scsitargetGroupService=scsitargetGroupService, filesystemNVRAMDataLoss=filesystemNVRAMDataLoss, ddboostStatus=ddboostStatus, replContext=replContext, diskGroupReconstructionShutdown=diskGroupReconstructionShutdown, ddboostProperties=ddboostProperties, VtlStatsInTC=VtlStatsInTC, VtlStatsSyncLossesTC=VtlStatsSyncLossesTC, ddboostUserEntry=ddboostUserEntry, cifsConfigDNS=cifsConfigDNS, vtlPoolTable=vtlPoolTable, systemUser=systemUser, FanIndexTC=FanIndexTC, vtlPortTrapIndex=vtlPortTrapIndex, tenantUnitMgmtGroupListGroupRole=tenantUnitMgmtGroupListGroupRole, dd410=dd410, haExternalLanHeartbeatStatus=haExternalLanHeartbeatStatus, VtlProcessStateTC=VtlProcessStateTC, VtlStatsOutTC=VtlStatsOutTC, systemPortsPort=systemPortsPort, scsitargetPortEndpPort=scsitargetPortEndpPort, diskTemperatureWarning=diskTemperatureWarning, replState=replState, vtlLibraryTotalDrives=vtlLibraryTotalDrives)
