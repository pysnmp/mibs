#
# PySNMP MIB module ADVA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/ADVA-MIB
# Produced by pysmi-1.1.10 at Thu Apr  4 02:54:02 2024
# On host fv-az768-708 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, NotificationType, enterprises, ModuleIdentity, iso, Integer32, mib_2, Unsigned32, snmpModules, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "NotificationType", "enterprises", "ModuleIdentity", "iso", "Integer32", "mib-2", "Unsigned32", "snmpModules", "MibIdentifier", "Counter32")
DateAndTime, DisplayString, RowStatus, MacAddress, TextualConvention, TimeStamp, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "RowStatus", "MacAddress", "TextualConvention", "TimeStamp", "TestAndIncr")
advaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544))
advaMIB.setRevisions(('2018-12-14 00:00', '2017-12-07 00:00', '2017-03-23 00:00', '2016-04-01 00:00', '2015-12-10 00:00', '2015-09-03 00:00', '2015-03-20 00:00', '2014-09-29 00:00', '2012-02-07 00:00', '2008-02-21 00:00', '2004-12-14 00:00', '2004-02-20 00:00', '2003-12-12 00:00', '2003-10-07 00:00', '2003-06-27 00:00', '2002-07-22 00:00',))
if mibBuilder.loadTexts: advaMIB.setLastUpdated('201812140000Z')
if mibBuilder.loadTexts: advaMIB.setOrganization('ADVA AG Optical Networking')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2))
fsp3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 4))
fsp1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 6))
fsp2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 7))
fsp1000adm = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 8))
fsp1500 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 9))
fsp150 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 10))
fspR7 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 11))
fsp150cm = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12))
fspNm = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 13))
fsp3000alm = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 14))
fsp3000c = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 15))
aos = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20))
aosCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1))
aosProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2))
neInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 1))
admin = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 2))
events = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 3))
software = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 4))
config = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5))
transportStandards = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4))
inventoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5))
updateBackupRestoreMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6))
snmpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7))
sonet = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1))
otn = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2))
sonetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1))
otuConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1))
oduConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2))
swAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1))
dbAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2))
class OnOff(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class AvailState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("available", 1), ("notAvailable", 2))

class EnableState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("stateNotApplicable", 0), ("stateEnabled", 1), ("stateDisabled", 2))

class ArcState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("alm", 1), ("nalm", 2))

class TrapAlarmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("indeterminate", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("cleared", 6), ("notReported", 7))

class ServiceImpairment(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("serviceAffecting", 1), ("nonServiceAffecting", 2), ("serviceAffectingInstall", 3), ("serviceAffectingActivate", 4))

class TrapCounter(TextualConvention, Counter32):
    status = 'current'

class Counter64String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

class KBytes(TextualConvention, Gauge32):
    status = 'current'

class IdentityTranslation(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class NeSwUpgradeStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39))
    namedValues = NamedValues(("none", 1), ("downloading", 2), ("downloadLoginFailed", 3), ("downloadFileNotFound", 4), ("downloadFileNoAccess", 5), ("downloadFailure", 6), ("downloadReadyForInstallation", 7), ("installingSoftware", 8), ("installationFailed", 9), ("softwareReadyForActivation", 10), ("activatingSoftware", 11), ("activationFailed", 12), ("softwareActivated", 13), ("rebooting", 14), ("downloadServerUnreachable", 15), ("noSpaceLeft", 16), ("internalError", 17), ("downloadFileProtocolFailed", 18), ("downloadFileCheckFailed", 19), ("downloadSSHHostkeyFailed", 20), ("uploading", 21), ("uploadLoginFailed", 22), ("uploadFileNotFound", 23), ("uploadFileNoAccess", 24), ("uploadFailure", 25), ("uploadServerUnreachable", 26), ("uploadFileProtocolFailed", 27), ("uploadFileCheckFailed", 28), ("uploadSSHHostkeyFailed", 29), ("installationFailedDeny", 30), ("installationFailedWrongCrc", 31), ("installationFailedVersionMismatch", 32), ("installationFailedStbyInWrongState", 33), ("installationFailedDamagedConfFile", 34), ("installationFailedFsckFailed", 35), ("installationFailedNotExist", 36), ("downloadFileFailedProtocolDisabled", 37), ("uploadFileFailedProtocolDisabled", 38), ("backupFailedGeneration", 39))

class NeSwInstallStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("undefined", 0), ("idle", 1), ("downloadingCon", 2), ("installingCon", 3), ("downloadingNcu", 4), ("installingNcu", 5), ("downloadingFwp", 6), ("installingFwp", 7), ("downloadingPgm", 8), ("installingPgm", 9))

class FileTransferProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5))
    namedValues = NamedValues(("ftp", 2), ("scp", 3), ("http", 4), ("sftp", 5))

class SourceIpAddress(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("sysIp", 1), ("defaultIp", 2))

class F7FileTimeStamp(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("add", 1), ("omit", 2))

class F7AutoBackupInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("every1Day", 2), ("every2Day", 3), ("every3Day", 4), ("every4Day", 5), ("every5Day", 6), ("every6Day", 7), ("every1Week", 8), ("every2Week", 9), ("every3Week", 10), ("every1Month", 11), ("every2Month", 12), ("every3Month", 13))

class F7AutoBackupRunState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("no", 1), ("yes", 2))

class PartitionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("empty", 1), ("configFileInstalled", 2), ("ncuFileInstalled", 3), ("softwareReadyForActivation", 4), ("fwpsInstalled", 5))

class FspDate(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class FspTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class ApsDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("bidirectional", 1), ("unidirectional", 2))

class ApsDirectionCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capBidirectional", 1), ("capUnidirectional", 2))

class ApsHoldoffTime(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("e20ms", 2), ("e100ms", 3), ("e200ms", 4), ("e300ms", 5), ("e400ms", 6), ("e500ms", 7), ("e600ms", 8), ("e700ms", 9), ("e800ms", 10), ("e900ms", 11), ("e1000ms", 12), ("e1100ms", 13), ("e1200ms", 14), ("e1300ms", 15), ("e1400ms", 16), ("e1500ms", 17), ("e1600ms", 18), ("e1700ms", 19), ("e1800ms", 20), ("e1900ms", 21), ("e2000ms", 22), ("e2100ms", 23), ("e2200ms", 24), ("e2300ms", 25), ("e2400ms", 26), ("e2500ms", 27), ("e2600ms", 28), ("e2700ms", 29), ("e2800ms", 30), ("e2900ms", 31), ("e3000ms", 32), ("e3100ms", 33), ("e3200ms", 34), ("e3300ms", 35), ("e3400ms", 36), ("e3500ms", 37), ("e3600ms", 38), ("e3700ms", 39), ("e3800ms", 40), ("e3900ms", 41), ("e4000ms", 42), ("e4100ms", 43), ("e4200ms", 44), ("e4300ms", 45), ("e4400ms", 46), ("e4500ms", 47), ("e4600ms", 48), ("e4700ms", 49), ("e4800ms", 50), ("e4900ms", 51), ("e5000ms", 52), ("e5100ms", 53), ("e5200ms", 54), ("e5300ms", 55), ("e5400ms", 56), ("e5500ms", 57), ("e5600ms", 58), ("e5700ms", 59), ("e5800ms", 60), ("e5900ms", 61), ("e6000ms", 62), ("e6100ms", 63), ("e6200ms", 64), ("e6300ms", 65), ("e6400ms", 66), ("e6500ms", 67), ("e6600ms", 68), ("e6700ms", 69), ("e6800ms", 70), ("e6900ms", 71), ("e7000ms", 72), ("e7100ms", 73), ("e7200ms", 74), ("e7300ms", 75), ("e7400ms", 76), ("e7500ms", 77), ("e7600ms", 78), ("e7700ms", 79), ("e7800ms", 80), ("e7900ms", 81), ("e8000ms", 82), ("e8100ms", 83), ("e8200ms", 84), ("e8300ms", 85), ("e8400ms", 86), ("e8500ms", 87), ("e8600ms", 88), ("e8700ms", 89), ("e8800ms", 90), ("e8900ms", 91), ("e9000ms", 92), ("e9100ms", 93), ("e9200ms", 94), ("e9300ms", 95), ("e9400ms", 96), ("e9500ms", 97), ("e9600ms", 98), ("e9700ms", 99), ("e9800ms", 100), ("e9900ms", 101), ("e10000ms", 102))

class ApsHoldoffTimeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNone", 1), ("capE20ms", 2), ("capE100ms", 3), ("capE200ms", 4), ("capE300ms", 5), ("capE400ms", 6), ("capE500ms", 7), ("capE600ms", 8), ("capE700ms", 9), ("capE800ms", 10), ("capE900ms", 11), ("capE1000ms", 12), ("capE1100ms", 13), ("capE1200ms", 14), ("capE1300ms", 15), ("capE1400ms", 16), ("capE1500ms", 17), ("capE1600ms", 18), ("capE1700ms", 19), ("capE1800ms", 20), ("capE1900ms", 21), ("capE2000ms", 22), ("capE2100ms", 23), ("capE2200ms", 24), ("capE2300ms", 25), ("capE2400ms", 26), ("capE2500ms", 27), ("capE2600ms", 28), ("capE2700ms", 29), ("capE2800ms", 30), ("capE2900ms", 31), ("capE3000ms", 32), ("capE3100ms", 33), ("capE3200ms", 34), ("capE3300ms", 35), ("capE3400ms", 36), ("capE3500ms", 37), ("capE3600ms", 38), ("capE3700ms", 39), ("capE3800ms", 40), ("capE3900ms", 41), ("capE4000ms", 42), ("capE4100ms", 43), ("capE4200ms", 44), ("capE4300ms", 45), ("capE4400ms", 46), ("capE4500ms", 47), ("capE4600ms", 48), ("capE4700ms", 49), ("capE4800ms", 50), ("capE4900ms", 51), ("capE5000ms", 52), ("capE5100ms", 53), ("capE5200ms", 54), ("capE5300ms", 55), ("capE5400ms", 56), ("capE5500ms", 57), ("capE5600ms", 58), ("capE5700ms", 59), ("capE5800ms", 60), ("capE5900ms", 61), ("capE6000ms", 62), ("capE6100ms", 63), ("capE6200ms", 64), ("capE6300ms", 65), ("capE6400ms", 66), ("capE6500ms", 67), ("capE6600ms", 68), ("capE6700ms", 69), ("capE6800ms", 70), ("capE6900ms", 71), ("capE7000ms", 72), ("capE7100ms", 73), ("capE7200ms", 74), ("capE7300ms", 75), ("capE7400ms", 76), ("capE7500ms", 77), ("capE7600ms", 78), ("capE7700ms", 79), ("capE7800ms", 80), ("capE7900ms", 81), ("capE8000ms", 82), ("capE8100ms", 83), ("capE8200ms", 84), ("capE8300ms", 85), ("capE8400ms", 86), ("capE8500ms", 87), ("capE8600ms", 88), ("capE8700ms", 89), ("capE8800ms", 90), ("capE8900ms", 91), ("capE9000ms", 92), ("capE9100ms", 93), ("capE9200ms", 94), ("capE9300ms", 95), ("capE9400ms", 96), ("capE9500ms", 97), ("capE9600ms", 98), ("capE9700ms", 99), ("capE9800ms", 100), ("capE9900ms", 101), ("capE10000ms", 102))

class AssignmentState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("assigned", 1), ("unassigned", 2), ("notassignable", 3))

class BootState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("undefined", 0), ("complete", 1), ("started", 2), ("failed", 3), ("reject", 4), ("install", 5), ("installFail", 6), ("installComplete", 7), ("activate", 8), ("activateFail", 9), ("activateReject", 10), ("activateComplete", 11))

class CommandEqpt(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("install", 2), ("reboot", 3), ("activate", 4), ("update", 5), ("installFromStby", 6), ("forceInstall", 7))

class CpWdmEntityClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("undefined", 0), ("cp", 1), ("tunnel", 2), ("connection", 3), ("path", 4), ("pathElement", 5), ("logicalInterface", 6), ("remoteAlarm", 7), ("portBinding", 8), ("reservation", 9), ("diversity", 10))

class EnableStateCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capStateEnabled", 1), ("capStateDisabled", 2))

class EntityClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88))
    namedValues = NamedValues(("undefined", 0), ("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("plug", 10), ("stack", 11), ("group", 12), ("clientPort", 13), ("networkPort", 14), ("virtualChannel", 15), ("connection", 16), ("vc4Container", 17), ("vc3sts1Container", 18), ("vc12vt15Container", 19), ("dcnChannel", 20), ("routerConfig", 21), ("environmentPort", 22), ("internalPort", 23), ("upgradePort", 24), ("midstagePort", 25), ("serialPort", 26), ("pppIpInterface", 27), ("lanIp", 28), ("vs1Container", 29), ("sts3cContainer", 30), ("payloadChannel", 31), ("passiveShelf", 32), ("sts24cContainer", 33), ("sts48cContainer", 34), ("vs2cContainer", 35), ("vs4cContainer", 36), ("tifInputPort", 37), ("tifOutputPort", 38), ("opticalLink", 39), ("virtualOpticalChannel", 40), ("logicalInterface", 41), ("physicalTerminationPoint", 42), ("ethClient", 43), ("ethNetwork", 44), ("veth", 45), ("flow", 47), ("ctrans", 48), ("policerOnFlow", 50), ("queueOnPort", 51), ("queueOnFlow", 52), ("farEndPlug", 53), ("farEndChannel", 54), ("vc4c8Container", 55), ("vc4c16Container", 56), ("vs0Container", 57), ("virtualSubChannel", 58), ("bridge", 59), ("queueOnBridge", 60), ("backwardVirtualOptMux", 61), ("forwardVirtualOptMux", 62), ("optChannelTransportLane", 63), ("virtualChannelN", 64), ("externalChannel", 65), ("virtualTerminationPoint", 66), ("virtualConnection", 67), ("virtualOptMux", 68), ("optTransportLaneGroup", 69), ("optWaveLengthGroup", 70), ("crossConnectionChannel", 71), ("crossOpticalLineChannel", 72), ("versatilePort", 73), ("system", 74), ("crossConnectionDcn", 75), ("protectionFfp", 76), ("protectionCable", 77), ("unidirectionalChannel", 78), ("filterCable", 79), ("groupTerminationPoint", 80), ("externalOm", 81), ("externalVch", 82), ("virtualModule", 83), ("virtualMap", 84), ("lldp", 85), ("managementPort", 86), ("licenseManager", 87), ("license", 88))

class EntityIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class EntityType(TextualConvention, Integer32):
    status = 'current'

class EquipmentState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("equipped", 1), ("unequipped", 2))

class EthDuplexMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("ethHalfDuplex", 1), ("ethFullDuplex", 2))

class EthDuplexModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capEthHalfDuplex", 1), ("capEthFullDuplex", 2))

class FileArea(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("undefined", 0), ("activeArea", 1), ("standbyArea", 2), ("rDisk", 3), ("backupDisk", 4), ("alpDisk", 5), ("pDisk", 6), ("cfDisk", 7), ("paDisk", 8))

class FileType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("undefined", 0), ("pgm", 1), ("dbs", 2), ("unknown", 3), ("alp", 4), ("ncu", 5), ("fwps", 6), ("con", 7), ("prf", 8), ("paf", 9), ("dbx", 10), ("alm", 11), ("pak", 12), ("map", 13))

class FspR7AdminStateSnmpProxy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 6))
    namedValues = NamedValues(("undefined", 0), ("is", 2), ("dsbld", 6))

class FspR7AdminStateSnmpProxyCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capIs", 2), ("capDsbld", 6))

class FspR7Date(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class FspR7EnableDisable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("enable", 1), ("disable", 2))

class FspR7EquipmentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 137, 138, 140, 141, 142, 143, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 180, 182, 183, 185, 186, 187, 188, 190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 234, 235, 236, 237, 239, 240, 241, 242, 243, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 264, 267, 268, 269, 270, 272, 273, 274, 280, 282, 283, 284, 285, 286, 289, 290, 291, 292, 293, 294, 295, 297, 298, 300, 303, 304, 305, 307, 308, 309, 311, 312, 314), SingleValueConstraint(317, 318, 319, 320, 321, 323, 324, 450, 453, 454, 455, 456, 457, 458, 459, 461, 462, 463, 464, 465, 466, 467, 468, 472, 473, 474, 475, 476, 478, 479, 480, 481, 482, 483, 485, 486, 487, 488, 489, 490, 491, 499))
    namedValues = NamedValues(("undefined", 0), ("eqpSh1hu", 1), ("eqpSh1huDc", 2), ("eqpSh3hu", 3), ("eqpSh7hu", 4), ("eqpF2kSh5hu", 5), ("eqpF2kSh6hu", 6), ("eqpDcm", 7), ("eqpSh9hu", 8), ("eqpUnknown", 19), ("eqpNcu", 20), ("eqpNcutif", 21), ("eqpScu", 22), ("eqpScue", 23), ("eqpR6cu", 24), ("eqpPsu1huac", 25), ("eqpPsu7huac", 26), ("eqpPsu7hudc", 27), ("eqpFcu7hu", 28), ("eqp2clsmd", 29), ("eqp2absmc", 30), ("eqp2bsmd", 31), ("eqp1Gsmud", 32), ("eqp4gsmd", 33), ("eqp8gsmd", 34), ("eqp1csmuc", 35), ("eqp1csmuewc", 36), ("eqp4csmd", 37), ("eqp4csmud", 38), ("eqp4csmc", 39), ("eqpOsfm", 40), ("eqp1pm", 41), ("eqp2pm", 42), ("eqp40csmd", 43), ("eqpDcf", 44), ("eqpEdfas", 45), ("eqpEdfasgc", 46), ("eqpEdfadgc", 47), ("eqpRaman", 48), ("eqp4tcc2g5", 49), ("eqp4tcc2g5d", 50), ("eqp4tcc10gd", 51), ("eqp4tcc10gc", 52), ("eqpWcc10gd", 53), ("eqpWcc10gc", 54), ("eqpWcc2g71N", 55), ("eqpWcc2g7d", 56), ("eqp2tcm2g5", 57), ("eqp2tca2g5", 58), ("eqp8tca10gd", 59), ("eqp8tca10gc", 60), ("eqpWca10gd", 61), ("eqpWca10gc", 62), ("eqp4tca4gd", 63), ("eqp4tca4gc", 64), ("eqpwca2g5", 65), ("eqp4tca1g3d", 66), ("eqp4tca1g3c", 67), ("eqp8tce2g5d", 68), ("eqp8tce2g5c", 69), ("eqpWcelsd", 70), ("eqpWcelsc", 71), ("eqpVsm", 72), ("eqpRsmolm", 73), ("eqpRsmsf", 74), ("eqpOscm", 75), ("eqp2oscm", 76), ("eqpDrm", 77), ("eqpXfpG", 78), ("eqpsfpd", 79), ("eqpSfpc", 80), ("eqpSfpg", 81), ("eqpSfpe", 82), ("eqpSh1hudcm", 83), ("eqpCustomc", 84), ("eqpCustomd", 85), ("eqpPsu1hudc", 86), ("eqpWcc2g7c", 87), ("eqp1csmuEwD", 88), ("eqp1csmuG", 89), ("eqp3BsmC", 90), ("eqp2Tca2g5s", 91), ("eqp8Csmuc", 92), ("eqpEdfaDgcb", 93), ("eqpOscmPn", 94), ("eqp4Tcc10gtd", 95), ("eqp4Tca4g", 96), ("eqpDcg", 97), ("eqp2Tcm2g5d", 98), ("eqp2Tcm2g5c", 99), ("eqpWcm2g5d", 100), ("eqpWcm2g5c", 101), ("eqpEdfmSgc", 102), ("eqpF2kDemiV2", 103), ("eqpPsm", 104), ("eqpNcu2e", 105), ("eqp8TceGl2g5d", 106), ("eqp8TceGl2g5c", 107), ("eqpDcf1hu", 108), ("eqp10tcc10gtd", 109), ("eqp10tcc10gd", 110), ("eqp10tcc10gc", 111), ("eqp16csmSfd", 112), ("eqpOsfmSf", 113), ("eqp2clsmSfd", 114), ("eqp3bsmEwc", 115), ("eqpEdfaSgcb", 116), ("eqpEdfaDgcv", 117), ("eqpWcc10gtd", 118), ("eqp2csmuEwc", 119), ("eqpEroadmDc", 120), ("eqpScuS", 122), ("eqp4opcm", 123), ("eqpUtm", 124), ("eqpPscu", 125), ("eqp40Csm2hu", 126), ("eqp2Twcc2g7", 127), ("eqp2Wca10g", 130), ("eqpNcuHp", 131), ("eqpNcu20085hu", 132), ("eqp20Pca10G", 133), ("eqpXfpC", 137), ("eqpXfpD", 138), ("eqpWcc40gtd", 140), ("eqpIlm", 141), ("eqpNcuII", 142), ("eqpCem9hu", 143), ("eqp8roadmC40", 148), ("eqp4Tcc40gtd", 149), ("eqp2pca10g", 150), ("eqp10pca10g", 151), ("eqp1csmuD", 152), ("eqpSfpOsC", 153), ("eqpSfpOdC", 154), ("eqpSfpOsG", 155), ("eqpSfpOdG", 156), ("eqpRoadmC80", 157), ("eqpccm8", 158), ("eqpPsu9hudc", 159), ("eqp4tca4gus", 160), ("eqp40Csm3huD", 161), ("eqp5psm", 162), ("eqpFan9hu", 163), ("eqp5tce10gtd", 164), ("eqp10tccs10gtd", 165), ("eqp40Csm3hudcD", 166), ("eqp40Csm3hudcDi", 167), ("eqp5gsmD", 169), ("eqp8csmD", 170), ("eqp2otfm", 171), ("eqp8otdr3hu", 172), ("eqpXfptD", 173), ("eqp40Csm3huDi", 174), ("eqp8CcmC80", 175), ("eqpEdfaD27", 176), ("eqp2Wcc10g", 177), ("eqp8RoadmC80", 178), ("eqp2Wcc10gAes", 180), ("eqp5tce10gtaesd", 182), ("eqpSh1hupf", 183), ("eqpFan1hu", 185), ("eqp10tcc10g", 186), ("eqpXfpOtnD", 187), ("eqpNcu2p", 188), ("eqpPsu9huac", 190), ("eqp2Raman", 192), ("eqpEdfaS26", 193), ("eqp5tces10gtd", 194), ("eqpScuII", 195), ("eqp11RoadmC96", 196), ("eqp8AdmC96", 197), ("eqp8CxmC96", 198), ("eqp8Shm", 199), ("eqpAmpShgcv", 200), ("eqpAmpSlgcv", 201), ("eqp2RamanC15", 202), ("eqpWcc100gtD", 203), ("eqpCfp4g", 204), ("eqpCfp10g", 205), ("eqpXfpTlnD", 213), ("eqp5tces10gtaesd", 214), ("eqp10tce100g", 215), ("eqp96Csm4HuD", 216), ("eqp4CfptD", 217), ("eqp2psm", 218), ("eqpWce100G", 219), ("eqp10Wxc10g", 220), ("eqpShx9hu", 221), ("eqpFanXhu", 222), ("eqp10tcc100gtbD", 223), ("eqp9RoadmC96", 224), ("eqp4Wce16g", 225), ("eqpSfpBG", 226), ("eqpSfpCdrG", 227), ("eqp10tce100gGf", 228), ("eqpSfpCdrC", 229), ("eqp5tce10gaes", 234), ("eqp5tce10g", 235), ("eqp5tces10gaes", 236), ("eqp5tces10g", 237), ("eqp4roadmC96", 239), ("eqpWcc100gtbD", 240), ("eqpEdfaS20", 241), ("eqp10tccSdi10g", 242), ("eqp4roadmEC96", 243), ("eqpSfptD", 245), ("eqpSfp2TxG", 246), ("eqpSfp2RxG", 247), ("eqpSfp2Txe", 248), ("eqpSfp2Rxe", 249), ("eqp2EdfaS20S10", 250), ("eqp10Tce100Gb", 251), ("eqp10Tce100gAes", 252), ("eqpSfpCdrD", 253), ("eqpSh1huDcEtemp", 254), ("eqp8psm", 255), ("eqp9ccmC96", 256), ("eqpWce100GB", 257), ("eqp16tcc10G", 258), ("eqp4Wcc10g", 259), ("eqp5wca16G", 260), ("eqpCfptCd", 261), ("eqpWccPcn100g", 264), ("eqpOppm", 267), ("eqp4cfpd", 268), ("eqpNcuS", 269), ("eqp10csmuD", 270), ("eqpUtmS", 272), ("eqpSfpBC", 273), ("eqp10Tce100gAesBsi", 274), ("eqpWccPcn100gAes", 280), ("eqpSfpRxTxG", 282), ("eqpSfpTlnD", 283), ("eqpCfpTfCd", 284), ("eqpXfpBG", 285), ("eqpFd128D", 286), ("eqpSfpBCdrG", 289), ("eqpMroadmC96", 290), ("eqpPsm40Mroadm", 291), ("eqpOsfma", 292), ("eqp10tcc100g", 293), ("eqpCfpTgCd", 294), ("eqpPsm80Mroadm", 295), ("eqp10Tce100gbAes", 297), ("eqpL3CmSina", 298), ("eqp9Tce10gAesG", 300), ("eqp9RoadmRs", 303), ("eqp16psm4", 304), ("eqp96Csm2HuD", 305), ("eqp9Tce10gAesF", 307), ("eqp10Tce100gAesF", 308), ("eqpMtpOscC", 309), ("eqpWcc100gAesF", 311), ("eqpCfpTrCd", 312), ("eqpWcc100gAesB", 314)) + NamedValues(("eqpMapOscC", 317), ("eqpMtpbOscC", 318), ("eqpMapbOscC", 319), ("eqpWccPcn100gB", 320), ("eqp4psmS", 321), ("eqpWcc100gAesG", 323), ("eqpHdScm", 324), ("eqpCfp2tgCd", 450), ("eqpMaB2C3LtA", 453), ("eqpMaB5Lt", 454), ("eqpCfp2tCd", 455), ("eqpMp2B4CtS", 456), ("eqpPsmdc3", 457), ("eqpQSfpNotApproved", 458), ("eqpQSfp10g", 459), ("eqpMa2C2C3LtA", 461), ("eqpQSfpDacCr", 462), ("eqpCem3", 463), ("eqpFtm3", 464), ("eqpPsmac3", 465), ("eqpSh1R", 466), ("eqpEcm3", 467), ("eqp4QsfpG", 468), ("eqpScm2", 472), ("eqpMa2C5Lt", 473), ("eqpPsmac6", 474), ("eqpQSfpDac", 475), ("eqpQSfpAoc", 476), ("eqpPsmdc4", 478), ("eqpPsmac5", 479), ("eqpFtm4", 480), ("eqpFtm2", 481), ("eqpPsmac4", 482), ("eqpPsmdc", 483), ("eqpCem2", 485), ("eqpCem4", 486), ("eqpEcm2", 487), ("eqpQSfp4g", 488), ("eqpMp2B4Ct", 489), ("eqpSh12", 490), ("eqpSh4R", 491), ("eqpPtp", 499))

class FspR7EquipmentTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capEqpSh1hu", 1), ("capEqpSh1huDc", 2), ("capEqpSh3hu", 3), ("capEqpSh7hu", 4), ("capEqpF2kSh5hu", 5), ("capEqpF2kSh6hu", 6), ("capEqpDcm", 7), ("capEqpSh9hu", 8), ("capEqpUnknown", 19), ("capEqpNcu", 20), ("capEqpNcutif", 21), ("capEqpScu", 22), ("capEqpScue", 23), ("capEqpR6cu", 24), ("capEqpPsu1huac", 25), ("capEqpPsu7huac", 26), ("capEqpPsu7hudc", 27), ("capEqpFcu7hu", 28), ("capEqp2clsmd", 29), ("capEqp2absmc", 30), ("capEqp2bsmd", 31), ("capEqp1Gsmud", 32), ("capEqp4gsmd", 33), ("capEqp8gsmd", 34), ("capEqp1csmuc", 35), ("capEqp1csmuewc", 36), ("capEqp4csmd", 37), ("capEqp4csmud", 38), ("capEqp4csmc", 39), ("capEqpOsfm", 40), ("capEqp1pm", 41), ("capEqp2pm", 42), ("capEqp40csmd", 43), ("capEqpDcf", 44), ("capEqpEdfas", 45), ("capEqpEdfasgc", 46), ("capEqpEdfadgc", 47), ("capEqpRaman", 48), ("capEqp4tcc2g5", 49), ("capEqp4tcc2g5d", 50), ("capEqp4tcc10gd", 51), ("capEqp4tcc10gc", 52), ("capEqpWcc10gd", 53), ("capEqpWcc10gc", 54), ("capEqpWcc2g71N", 55), ("capEqpWcc2g7d", 56), ("capEqp2tcm2g5", 57), ("capEqp2tca2g5", 58), ("capEqp8tca10gd", 59), ("capEqp8tca10gc", 60), ("capEqpWca10gd", 61), ("capEqpWca10gc", 62), ("capEqp4tca4gd", 63), ("capEqp4tca4gc", 64), ("capEqpwca2g5", 65), ("capEqp4tca1g3d", 66), ("capEqp4tca1g3c", 67), ("capEqp8tce2g5d", 68), ("capEqp8tce2g5c", 69), ("capEqpWcelsd", 70), ("capEqpWcelsc", 71), ("capEqpVsm", 72), ("capEqpRsmolm", 73), ("capEqpRsmsf", 74), ("capEqpOscm", 75), ("capEqp2oscm", 76), ("capEqpDrm", 77), ("capEqpXfpG", 78), ("capEqpsfpd", 79), ("capEqpSfpc", 80), ("capEqpSfpg", 81), ("capEqpSfpe", 82), ("capEqpSh1hudcm", 83), ("capEqpCustomc", 84), ("capEqpCustomd", 85), ("capEqpPsu1hudc", 86), ("capEqpWcc2g7c", 87), ("capEqp1csmuEwD", 88), ("capEqp1csmuG", 89), ("capEqp3BsmC", 90), ("capEqp2Tca2g5s", 91), ("capEqp8Csmuc", 92), ("capEqpEdfaDgcb", 93), ("capEqpOscmPn", 94), ("capEqp4Tcc10gtd", 95), ("capEqp4Tca4g", 96), ("capEqpDcg", 97), ("capEqp2Tcm2g5d", 98), ("capEqp2Tcm2g5c", 99), ("capEqpWcm2g5d", 100), ("capEqpWcm2g5c", 101), ("capEqpEdfmSgc", 102), ("capEqpF2kDemiV2", 103), ("capEqpPsm", 104), ("capEqpNcu2e", 105), ("capEqp8TceGl2g5d", 106), ("capEqp8TceGl2g5c", 107), ("capEqpDcf1hu", 108), ("capEqp10tcc10gtd", 109), ("capEqp10tcc10gd", 110), ("capEqp10tcc10gc", 111), ("capEqp16csmSfd", 112), ("capEqpOsfmSf", 113), ("capEqp2clsmSfd", 114), ("capEqp3bsmEwc", 115), ("capEqpEdfaSgcb", 116), ("capEqpEdfaDgcv", 117), ("capEqpWcc10gtd", 118), ("capEqp2csmuEwc", 119), ("capEqpEroadmDc", 120), ("capEqpScuS", 122), ("capEqp4opcm", 123), ("capEqpUtm", 124), ("capEqpPscu", 125), ("capEqp40Csm2hu", 126), ("capEqp2Twcc2g7", 127), ("capEqp2Wca10g", 130), ("capEqpNcuHp", 131), ("capEqpNcu20085hu", 132), ("capEqp20Pca10G", 133), ("capEqpXfpC", 137), ("capEqpXfpD", 138), ("capEqpWcc40gtd", 140), ("capEqpIlm", 141), ("capEqpNcuII", 142), ("capEqpCem9hu", 143), ("capEqp8roadmC40", 148), ("capEqp4Tcc40gtd", 149), ("capEqp2pca10g", 150), ("capEqp10pca10g", 151), ("capEqp1csmuD", 152), ("capEqpSfpOsC", 153), ("capEqpSfpOdC", 154), ("capEqpSfpOsG", 155), ("capEqpSfpOdG", 156), ("capEqpRoadmC80", 157), ("capEqpccm8", 158), ("capEqpPsu9hudc", 159), ("capEqp4tca4gus", 160), ("capEqp40Csm3huD", 161), ("capEqp5psm", 162), ("capEqpFan9hu", 163), ("capEqp5tce10gtd", 164), ("capEqp10tccs10gtd", 165), ("capEqp40Csm3hudcD", 166), ("capEqp40Csm3hudcDi", 167), ("capEqp5gsmD", 169), ("capEqp8csmD", 170), ("capEqp2otfm", 171), ("capEqp8otdr3hu", 172), ("capEqpXfptD", 173), ("capEqp40Csm3huDi", 174), ("capEqp8CcmC80", 175), ("capEqpEdfaD27", 176), ("capEqp2Wcc10g", 177), ("capEqp8RoadmC80", 178), ("capEqp2Wcc10gAes", 180), ("capEqp5tce10gtaesd", 182), ("capEqpSh1hupf", 183), ("capEqpFan1hu", 185), ("capEqp10tcc10g", 186), ("capEqpXfpOtnD", 187), ("capEqpNcu2p", 188), ("capEqpPsu9huac", 190), ("capEqp2Raman", 192), ("capEqpEdfaS26", 193), ("capEqp5tces10gtd", 194), ("capEqpScuII", 195), ("capEqp11RoadmC96", 196), ("capEqp8AdmC96", 197), ("capEqp8CxmC96", 198), ("capEqp8Shm", 199), ("capEqpAmpShgcv", 200), ("capEqpAmpSlgcv", 201), ("capEqp2RamanC15", 202), ("capEqpWcc100gtD", 203), ("capEqpCfp4g", 204), ("capEqpCfp10g", 205), ("capEqpXfpTlnD", 213), ("capEqp5tces10gtaesd", 214), ("capEqp10tce100g", 215), ("capEqp96Csm4HuD", 216), ("capEqp4CfptD", 217), ("capEqp2psm", 218), ("capEqpWce100G", 219), ("capEqp10Wxc10g", 220), ("capEqpShx9hu", 221), ("capEqpFanXhu", 222), ("capEqp10tcc100gtbD", 223), ("capEqp9RoadmC96", 224), ("capEqp4Wce16g", 225), ("capEqpSfpBG", 226), ("capEqpSfpCdrG", 227), ("capEqp10tce100gGf", 228), ("capEqpSfpCdrC", 229), ("capEqp5tce10gaes", 234), ("capEqp5tce10g", 235), ("capEqp5tces10gaes", 236), ("capEqp5tces10g", 237), ("capEqp4roadmC96", 239), ("capEqpWcc100gtbD", 240), ("capEqpEdfaS20", 241), ("capEqp10tccSdi10g", 242), ("capEqp4roadmEC96", 243), ("capEqpSfptD", 245), ("capEqpSfp2TxG", 246), ("capEqpSfp2RxG", 247), ("capEqpSfp2Txe", 248), ("capEqpSfp2Rxe", 249), ("capEqp2EdfaS20S10", 250), ("capEqp10Tce100Gb", 251), ("capEqp10Tce100gAes", 252), ("capEqpSfpCdrD", 253), ("capEqpSh1huDcEtemp", 254), ("capEqp8psm", 255), ("capEqp9ccmC96", 256), ("capEqpWce100GB", 257), ("capEqp16tcc10G", 258), ("capEqp4Wcc10g", 259), ("capEqp5wca16G", 260), ("capEqpCfptCd", 261), ("capEqpWccPcn100g", 264), ("capEqpOppm", 267), ("capEqp4cfpd", 268), ("capEqpNcuS", 269), ("capEqp10csmuD", 270), ("capEqpUtmS", 272), ("capEqpSfpBC", 273), ("capEqp10Tce100gAesBsi", 274), ("capEqpWccPcn100gAes", 280), ("capEqpSfpRxTxG", 282), ("capEqpSfpTlnD", 283), ("capEqpCfpTfCd", 284), ("capEqpXfpBG", 285), ("capEqpFd128D", 286), ("capEqpSfpBCdrG", 289), ("capEqpMroadmC96", 290), ("capEqpPsm40Mroadm", 291), ("capEqpOsfma", 292), ("capEqp10tcc100g", 293), ("capEqpCfpTgCd", 294), ("capEqpPsm80Mroadm", 295), ("capEqp10Tce100gbAes", 297), ("capEqpL3CmSina", 298), ("capEqp9Tce10gAesG", 300), ("capEqp9RoadmRs", 303), ("capEqp16psm4", 304), ("capEqp96Csm2HuD", 305), ("capEqp9Tce10gAesF", 307), ("capEqp10Tce100gAesF", 308), ("capEqpMtpOscC", 309), ("capEqpWcc100gAesF", 311), ("capEqpCfpTrCd", 312), ("capEqpWcc100gAesB", 314)) + NamedValues(("capEqpMapOscC", 317), ("capEqpMtpbOscC", 318), ("capEqpMapbOscC", 319), ("capEqpWccPcn100gB", 320), ("capEqp4psmS", 321), ("capEqpWcc100gAesG", 323), ("capEqpHdScm", 324), ("capEqpCfp2tgCd", 450), ("capEqpMaB2C3LtA", 453), ("capEqpMaB5Lt", 454), ("capEqpCfp2tCd", 455), ("capEqpMp2B4CtS", 456), ("capEqpPsmdc3", 457), ("capEqpQSfpNotApproved", 458), ("capEqpQSfp10g", 459), ("capEqpMa2C2C3LtA", 461), ("capEqpQSfpDacCr", 462), ("capEqpCem3", 463), ("capEqpFtm3", 464), ("capEqpPsmac3", 465), ("capEqpSh1R", 466), ("capEqpEcm3", 467), ("capEqp4QsfpG", 468), ("capEqpScm2", 472), ("capEqpMa2C5Lt", 473), ("capEqpPsmac6", 474), ("capEqpQSfpDac", 475), ("capEqpQSfpAoc", 476), ("capEqpPsmdc4", 478), ("capEqpPsmac5", 479), ("capEqpFtm4", 480), ("capEqpFtm2", 481), ("capEqpPsmac4", 482), ("capEqpPsmdc", 483), ("capEqpCem2", 485), ("capEqpCem4", 486), ("capEqpEcm2", 487), ("capEqpQSfp4g", 488), ("capEqpMp2B4Ct", 489), ("capEqpSh12", 490), ("capEqpSh4R", 491), ("capEqpPtp", 499))

class FspR7FalseTrue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("false", 1), ("true", 2))

class FspR7Time(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class FspR7YesNo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2))

class FspR7UsersDb(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2), ("keepCurrent", 3))

class Grade(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("gradeA", 1), ("gradeB", 2), ("gradeGdps", 3), ("gradeC", 4))

class LoopConfig(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("noLoop", 1), ("lineLoop", 2), ("inwardLoop", 3))

class LoopConfigCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNoLoop", 1), ("capLineLoop", 2), ("capInwardLoop", 3))

class DestinationNodeOrAgentState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("undefined", 0), ("inactive", 1))

class NcuAutoActivation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("no", 1), ("yes", 2))

class NoYesNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("no", 1), ("yes", 2), ("notApplicable", 3))

class OhTerminationLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("undefined", 0), ("phys", 1), ("otnOtu", 2), ("otnOdu", 3), ("otnOpu", 4), ("sonetSection", 5), ("sonetLine", 6), ("sonetPath", 7), ("none", 8), ("pcs", 9), ("if10GbE", 10))

class OhTerminationLevelCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capPhys", 1), ("capOtnOtu", 2), ("capOtnOdu", 3), ("capOtnOpu", 4), ("capSonetSection", 5), ("capSonetLine", 6), ("capSonetPath", 7), ("capNone", 8), ("capPcs", 9), ("capIf10GbE", 10))

class OtnPayloadType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 3, 4, 5, 6, 7, 8, 12, 15, 16, 17, 18, 39, 41, 52, 54, 55, 56, 85, 86, 87, 88, 110, 129, 150, 178, 192, 194, 195, 200, 206, 212, 58, 127, 196, 36, 214, 215, 499))
    namedValues = NamedValues(("undefined", 0), ("ifType10GbE", 3), ("ifTypeOc192", 4), ("ifTypeOc48", 5), ("ifTypeStm16", 6), ("ifTypeStm64", 7), ("ifType10GFC", 8), ("ifType1GFC", 12), ("ifTypeF9953", 15), ("ifTypeF10312", 16), ("ifTypeF10518", 17), ("ifTypeF2488", 18), ("ifType2GFC", 39), ("ifType1GbE", 41), ("ifTypeF4250", 52), ("ifTypeF10709", 54), ("ifTypeF11095", 55), ("ifTypeF11318", 56), ("ifTypeStm1", 85), ("ifTypeStm4", 86), ("ifTypeOc3", 87), ("ifTypeOc12", 88), ("ifTypeF8500", 110), ("ifTypeF10000", 129), ("ifTypeF5000", 150), ("ifTypeF14025", 178), ("ifType40GbE", 192), ("ifTypeF41250", 194), ("ifTypeF103125", 195), ("ifTypeF2457", 200), ("ifTypeFe", 206), ("ifTypeE10to1000t", 212), ("ifType4GFC", 58), ("ifType8GFC", 127), ("ifType16GFC", 196), ("ifTypeE10or100bt", 36), ("ifType25GbE", 214), ("ifType32GFC", 215), ("ifTypeNotDefined", 499))

class OtnPayloadTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capIfType10GbE", 3), ("capIfTypeOc192", 4), ("capIfTypeOc48", 5), ("capIfTypeStm16", 6), ("capIfTypeStm64", 7), ("capIfType10GFC", 8), ("capIfType1GFC", 12), ("capIfTypeF9953", 15), ("capIfTypeF10312", 16), ("capIfTypeF10518", 17), ("capIfTypeF2488", 18), ("capIfType2GFC", 39), ("capIfType1GbE", 41), ("capIfTypeF4250", 52), ("capIfTypeF10709", 54), ("capIfTypeF11095", 55), ("capIfTypeF11318", 56), ("capIfTypeStm1", 85), ("capIfTypeStm4", 86), ("capIfTypeOc3", 87), ("capIfTypeOc12", 88), ("capIfTypeF8500", 110), ("capIfTypeF10000", 129), ("capIfTypeF5000", 150), ("capIfTypeF14025", 178), ("capIfType40GbE", 192), ("capIfTypeF41250", 194), ("capIfTypeF103125", 195), ("capIfTypeF2457", 200), ("capIfTypeFe", 206), ("capIfTypeE10to1000t", 212), ("capIfType4GFC", 58), ("capIfType8GFC", 127), ("capIfType16GFC", 196), ("capIfTypeE10or100bt", 36), ("capIfType25GbE", 214), ("capIfType32GFC", 215), ("capIfTypeNotDefined", 499))

class OtnTcmLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("tcm1", 1), ("tcm2", 2), ("tcm3", 3), ("tcm4", 4), ("tcm5", 5), ("tcm6", 6), ("disabled", 7))

class OtnTcmLevelCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capTcm1", 1), ("capTcm2", 2), ("capTcm3", 3), ("capTcm4", 4), ("capTcm5", 5), ("capTcm6", 6), ("capDisabled", 7))

class PgmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("null", 1), ("ncu", 2), ("ncuHp", 3), ("fwps", 4), ("legacy", 5), ("nscuS", 6), ("fwpe", 7))

class ProtectionMech(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("undefined", 0), ("pathProtection", 1), ("channelCardProtection", 2), ("channelProtection", 3), ("versatileSwitchedProtection", 4), ("flowProtection", 5), ("clientCardProtection", 6), ("controller", 7), ("none", 8))

class ProtectionMechCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capPathProtection", 1), ("capChannelCardProtection", 2), ("capChannelProtection", 3), ("capVersatileSwitchedProtection", 4), ("capFlowProtection", 5), ("capClientCardProtection", 6), ("capController", 7), ("capNone", 8))

class RestoreActivation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("notRestore", 1), ("restoreFromStdBy", 2), ("restoreToFactory", 3), ("restoreFromEqpt", 4), ("acceptDatabase", 5))

class RestoreActivationCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNotRestore", 1), ("capRestoreFromStdBy", 2), ("capRestoreToFactory", 3), ("capRestoreFromEqpt", 4), ("capAcceptDatabase", 5))

class ServiceAffecting(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("nsa", 1), ("sa", 2), ("saActivate", 3), ("saInstall", 4), ("none", 5))

class ServiceAffectingCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNsa", 1), ("capSa", 2), ("capSaActivate", 3), ("capSaInstall", 4), ("capNone", 5))

class StandbyServiceAffecting(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("nsa", 1), ("sa", 2), ("saActivate", 3), ("saInstall", 4), ("none", 5))

class SnmpProxySynchronizationState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("inactive", 1), ("active", 2))

class SnmpProxySynchronizationStage(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("started", 1), ("finished", 2))

class SonetSectSigDegThres(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("ber10exp5", 1), ("ber10exp6", 2), ("ber10exp7", 3), ("ber10exp8", 4), ("ber10exp9", 5))

class SonetSectSigDegThresCaps(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("capBer10exp5", 1), ("capBer10exp6", 2), ("capBer10exp7", 3), ("capBer10exp8", 4), ("capBer10exp9", 5))

class SonetTimingSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("loopTiming", 1), ("internal", 2))

class SonetTimingSourceCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capLoopTiming", 1), ("capInternal", 2))

class SonetTraceForm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("form64CRLF", 1), ("form16CRC7", 2), ("form1Byte", 3))

class SonetTraceFormCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capForm64CRLF", 1), ("capForm16CRC7", 2), ("capForm1Byte", 3))

class SonetVcBundleAllocation(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class SonetVcBundleAllocationCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("vc1", 0), ("vc2", 1), ("vc3", 2), ("vc4", 3), ("vc5", 4), ("vc6", 5), ("vc7", 6), ("vc8", 7), ("vc9", 8), ("vc10", 9), ("vc11", 10), ("vc12", 11), ("vc13", 12), ("vc14", 13), ("vc15", 14), ("vc16", 15), ("vc17", 16), ("vc18", 17), ("vc19", 18), ("vc20", 19), ("vc21", 20), ("vc22", 21), ("vc23", 22), ("vc24", 23), ("vc25", 24), ("vc26", 25), ("vc27", 26), ("vc28", 27), ("vc29", 28), ("vc30", 29), ("vc31", 30), ("vc32", 31), ("vc33", 32), ("vc34", 33), ("vc35", 34), ("vc36", 35), ("vc37", 36), ("vc38", 37), ("vc39", 38), ("vc40", 39), ("vc41", 40), ("vc42", 41), ("vc43", 42), ("vc44", 43), ("vc45", 44), ("vc46", 45), ("vc47", 46), ("vc48", 47), ("vc49", 48), ("vc50", 49), ("vc51", 50), ("vc52", 51), ("vc53", 52), ("vc54", 53), ("vc55", 54), ("vc56", 55), ("vc57", 56), ("vc58", 57), ("vc59", 58), ("vc60", 59), ("vc61", 60), ("vc62", 61), ("vc63", 62), ("vc64", 63))

class TimMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("disabled", 1), ("enableAisDisabled", 2), ("enableAisEnabled", 3))

class TimModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capDisabled", 1), ("capEnableAisDisabled", 2), ("capEnableAisEnabled", 3))

class FspR7TrapsinkLifetime(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 0), ("duration1hour", 1), ("duration1day", 2), ("duration3days", 3), ("duration1week", 4), ("duration1month", 5), ("unlimited", 6))

class VirtualContainerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("undefined", 0), ("vc4Type", 1), ("vc3Au4Type", 2), ("sts1", 3), ("sts3c", 4), ("vs1", 5), ("vs2c", 6), ("sts24c", 7), ("sts48c", 8), ("vs4c", 9), ("vc4c8", 10), ("vc4c16", 11), ("vs0", 12), ("vs3c", 13), ("vs5c", 14), ("vs8c", 15), ("vs6c", 16), ("odu0", 17), ("odu1", 18), ("oduFlex", 19), ("vs7c", 20))

class VirtualContainerTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capVc4Type", 1), ("capVc3Au4Type", 2), ("capSts1", 3), ("capSts3c", 4), ("capVs1", 5), ("capVs2c", 6), ("capSts24c", 7), ("capSts48c", 8), ("capVs4c", 9), ("capVc4c8", 10), ("capVc4c16", 11), ("capVs0", 12), ("capVs3c", 13), ("capVs5c", 14), ("capVs8c", 15), ("capVs6c", 16), ("capOdu0", 17), ("capOdu1", 18), ("capOduFlex", 19), ("capVs7c", 20))

class YesNoNA(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2), ("notApplicable", 3))

class LogicalIfTransport(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class LogicalIfTransportCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lif1", 0), ("lif2", 1), ("lif3", 2), ("lif4", 3), ("lif5", 4), ("lif6", 5), ("lif7", 6), ("lif8", 7), ("lif9", 8), ("lif10", 9), ("lif11", 10), ("lif12", 11), ("lif13", 12), ("lif14", 13), ("lif15", 14), ("lif16", 15))

class ModuleForm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("native", 1), ("legacy", 2), ("compatible", 3), ("cloudConnect", 4))

neMibVariant = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neMibVariant.setStatus('current')
neManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neManufacturer.setStatus('current')
neDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 3), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neDateAndTime.setStatus('current')
neMemorySizeTotal = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 4), KBytes()).setUnits('kBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: neMemorySizeTotal.setStatus('current')
neMemorySizeFree = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 5), KBytes()).setUnits('kBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: neMemorySizeFree.setStatus('current')
neStorageTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6), )
if mibBuilder.loadTexts: neStorageTable.setStatus('current')
neStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1), ).setIndexNames((0, "ADVA-MIB", "neStorageIndex"))
if mibBuilder.loadTexts: neStorageEntry.setStatus('current')
neStorageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: neStorageIndex.setStatus('current')
neStorageDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStorageDescr.setStatus('current')
neStorageCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 3), KBytes()).setUnits('kBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: neStorageCapacity.setStatus('current')
neStorageAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 4), KBytes()).setUnits('kBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: neStorageAvailable.setStatus('current')
neAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 7), TrapAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmStatus.setStatus('current')
snmpWriteAccessRestriction = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 2, 1), EnableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpWriteAccessRestriction.setStatus('current')
snmpWriteAccessTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 2, 2), )
if mibBuilder.loadTexts: snmpWriteAccessTable.setStatus('current')
snmpWriteAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 2, 2, 1), ).setIndexNames((0, "ADVA-MIB", "snmpWriteAccessNmsAddress"))
if mibBuilder.loadTexts: snmpWriteAccessEntry.setStatus('current')
snmpWriteAccessNmsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 2, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: snmpWriteAccessNmsAddress.setStatus('current')
snmpWriteAccessNmsName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 2, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpWriteAccessNmsName.setStatus('current')
neEventsLogged = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 3, 1), TrapCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventsLogged.setStatus('current')
neEventLogTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2), )
if mibBuilder.loadTexts: neEventLogTable.setStatus('current')
neEventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1), ).setIndexNames((0, "ADVA-MIB", "neEventLogIndex"))
if mibBuilder.loadTexts: neEventLogEntry.setStatus('current')
neEventLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 1), TrapCounter())
if mibBuilder.loadTexts: neEventLogIndex.setStatus('current')
neEventLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogTimeStamp.setStatus('current')
neEventLogNotificationOID = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogNotificationOID.setStatus('current')
neEventLogIdentityTranslation = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 4), IdentityTranslation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogIdentityTranslation.setStatus('current')
neEventLogVarTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3), )
if mibBuilder.loadTexts: neEventLogVarTable.setStatus('current')
neEventLogVarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1), ).setIndexNames((0, "ADVA-MIB", "neEventLogIndex"), (0, "ADVA-MIB", "neEventLogVarIndex"))
if mibBuilder.loadTexts: neEventLogVarEntry.setStatus('current')
neEventLogVarIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: neEventLogVarIndex.setStatus('current')
neEventLogVarId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarId.setStatus('current')
neEventLogVarType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 7))).clone(namedValues=NamedValues(("integer32", 1), ("ipAddress", 2), ("octetString", 3), ("objectId", 4), ("counter64", 5), ("unsigned32", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarType.setStatus('current')
neEventLogVarInteger32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarInteger32Val.setStatus('current')
neEventLogVarIpAddressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarIpAddressVal.setStatus('current')
neEventLogVarOctetStringVal = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarOctetStringVal.setStatus('current')
neEventLogVarOidVal = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarOidVal.setStatus('current')
neEventLogVarCounter64Val = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarCounter64Val.setStatus('current')
neEventLogVarUnsigned32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarUnsigned32Val.setStatus('current')
neTrapsinkTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4), )
if mibBuilder.loadTexts: neTrapsinkTable.setStatus('current')
neTrapsinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1), ).setIndexNames((0, "ADVA-MIB", "neTrapsinkAddress"), (0, "ADVA-MIB", "neTrapsinkPort"))
if mibBuilder.loadTexts: neTrapsinkEntry.setStatus('current')
neTrapsinkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: neTrapsinkAddress.setStatus('current')
neTrapsinkPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: neTrapsinkPort.setStatus('current')
neTrapsinkCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neTrapsinkCommunity.setStatus('current')
neTrapsinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neTrapsinkRowStatus.setStatus('current')
neTrapsinkVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 5), Unsigned32()).setUnits('').setMaxAccess("readwrite")
if mibBuilder.loadTexts: neTrapsinkVersion.setStatus('current')
neTrapsinkUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neTrapsinkUserName.setStatus('current')
neTrapsinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 7), FspR7TrapsinkLifetime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neTrapsinkType.setStatus('current')
swVersionTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1), )
if mibBuilder.loadTexts: swVersionTable.setStatus('current')
swVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: swVersionEntry.setStatus('current')
swVersionActiveApplSw = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionActiveApplSw.setStatus('current')
swVersionInactiveApplSw = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionInactiveApplSw.setStatus('current')
swVersionActiveOperatingSw = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionActiveOperatingSw.setStatus('current')
swVersionInactiveOperatingSw = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionInactiveOperatingSw.setStatus('current')
swVersionNextBoot = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("activeVersion", 1), ("inactiveVersion", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionNextBoot.setStatus('current')
neSoftwareUpgrade = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2))
neSwUpgradeRequest = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("none", 1), ("download", 2), ("install", 3), ("activate", 4), ("revertToPrevious", 5), ("reboot", 6), ("downloadInstallActivateReboot", 7), ("installActivateReboot", 8), ("revertToPreviousReboot", 9), ("activateAlp", 10), ("activateDefaultAlp", 11), ("upload", 12), ("autoDownloadInstall", 13), ("autoInstall", 14), ("fwpInstall", 15), ("fwpDownloadInstall", 16), ("downloadCf", 17), ("uploadCf", 18), ("installCf", 19), ("autoInstallCf", 20), ("uploadPa", 21), ("activateWithFwp", 22), ("forceReboot", 23), ("stbyFwpInstall", 24)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeRequest.setStatus('current')
neSwUpgradeState = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 2), NeSwUpgradeStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neSwUpgradeState.setStatus('current')
neSwUpgradeServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeServerAddress.setStatus('current')
neSwUpgradeServerLogin = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 4), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeServerLogin.setStatus('current')
neSwUpgradeServerPasswd = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 5), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeServerPasswd.setStatus('current')
neSwUpgradeServerDirectory = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 6), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeServerDirectory.setStatus('current')
neSwUpgradeFileName = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 7), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeFileName.setStatus('current')
neSwUpgradeNeDirectory = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neSwUpgradeNeDirectory.setStatus('current')
neSwUpgradeTransferProtocol = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 9), FileTransferProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeTransferProtocol.setStatus('current')
sourceIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 10), SourceIpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sourceIpAddress.setStatus('current')
neSwInstallState = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 11), NeSwInstallStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neSwInstallState.setStatus('current')
neSwUpgradeType = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("undefined", 0), ("legacy", 1), ("revised", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeType.setStatus('current')
neSwDownloadProgress = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%')
if mibBuilder.loadTexts: neSwDownloadProgress.setStatus('current')
neSwUpgradeCommonIpSrv = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 14), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeCommonIpSrv.setStatus('current')
provContainerTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 1), )
if mibBuilder.loadTexts: provContainerTable.setStatus('current')
provContainerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: provContainerEntry.setStatus('current')
provAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("assigned", 1), ("unassigned", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provAssignmentState.setStatus('current')
provEquipmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("equipped", 1), ("unequipped", 2), ("invalid", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provEquipmentState.setStatus('current')
neBackupRestore = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2))
neBackupRestoreRequest = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("none", 1), ("runBackup", 2), ("runRestore", 3), ("dBdownload", 4), ("dBupload", 5), ("dbDownloadScu", 6), ("dbUploadScu", 7), ("alpDownload", 8), ("alpUpload", 9), ("runBackupScu", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neBackupRestoreRequest.setStatus('current')
neBackupRestoreState = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("noBackupAvailable", 1), ("backupInProgress", 2), ("backupAvailable", 3), ("restoreInProgress", 4), ("backupRestoreFail", 5), ("backupRestoreIdle", 6), ("backupRestoreCompleted", 7), ("dbActivationFailed", 8), ("dbActivationInProgress", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neBackupRestoreState.setStatus('current')
neBackupRestoreFile = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neBackupRestoreFile.setStatus('current')
neRestoreFileBackupDate = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neRestoreFileBackupDate.setStatus('current')
neF7AutomaticRemoteBackupSrvIp = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvIp.setStatus('current')
neF7AutomaticRemoteBackupSrvDir = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 6), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvDir.setStatus('current')
neF7AutomaticRemoteBackupSrvLogin = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 7), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvLogin.setStatus('current')
neF7AutomaticRemoteBackupSrvPass = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 8), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvPass.setStatus('current')
neF7AutomaticRemoteBackupProtocol = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 10), FileTransferProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupProtocol.setStatus('current')
neF7AutomaticRemoteBackupSrcIp = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 11), SourceIpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrcIp.setStatus('current')
neF7AutomaticRemoteBackupTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 12), F7FileTimeStamp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupTimeStamp.setStatus('deprecated')
neF7AutomaticRemoteBackupCommonIpSrv = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 13), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupCommonIpSrv.setStatus('current')
neF7AutomaticBackupTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20), )
if mibBuilder.loadTexts: neF7AutomaticBackupTable.setStatus('current')
neF7AutomaticBackupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1), ).setIndexNames((0, "ADVA-MIB", "neF7AutomaticBackupIndex"))
if mibBuilder.loadTexts: neF7AutomaticBackupEntry.setStatus('current')
neF7AutomaticBackupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 1), EntityIndex())
if mibBuilder.loadTexts: neF7AutomaticBackupIndex.setStatus('current')
neF7AutomaticBackupInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 2), F7AutoBackupInterval()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticBackupInterval.setStatus('current')
neF7AutomaticBackupStartDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 3), FspDate()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticBackupStartDate.setStatus('current')
neF7AutomaticBackupStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 4), FspTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticBackupStartTime.setStatus('current')
neF7AutomaticBackupNextDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 5), FspDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neF7AutomaticBackupNextDate.setStatus('current')
neF7AutomaticBackupRunState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 6), F7AutoBackupRunState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticBackupRunState.setStatus('current')
neF7AutomaticBackupTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 7), F7FileTimeStamp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticBackupTimeStamp.setStatus('current')
neAutoBackup = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3))
neAutoBackupConfig = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("autoBackup", 2), ("autoBackupAndUpload", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupConfig.setStatus('current')
neAutoBackupInterval = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 2), Unsigned32()).setUnits('hours').setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupInterval.setStatus('current')
neAutoBackupNextActionAt = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 3), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupNextActionAt.setStatus('current')
neAutoBackupServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupServerAddress.setStatus('current')
neAutoBackupServerLogin = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 5), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupServerLogin.setStatus('current')
neAutoBackupServerPasswd = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 6), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupServerPasswd.setStatus('current')
neAutoBackupServerDirectory = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 7), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupServerDirectory.setStatus('current')
sonetSectionConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1), )
if mibBuilder.loadTexts: sonetSectionConfigTable.setStatus('current')
sonetSectionConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: sonetSectionConfigEntry.setStatus('current')
sonetSectionConfigTimingSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 1), SonetTimingSource()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigTimingSource.setStatus('current')
sonetSectionConfigSignalDegradeThreshhold = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigSignalDegradeThreshhold.setStatus('current')
sonetSectionConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigSignalDegradePeriod.setStatus('current')
sonetSectionConfigTraceForm = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 4), SonetTraceForm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigTraceForm.setStatus('current')
sonetSectionConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigTraceExpected.setStatus('current')
sonetSectionConfigTraceTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigTraceTransmit.setStatus('current')
sonetSectionConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 7), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigTimMode.setStatus('current')
sonetSectionDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3), )
if mibBuilder.loadTexts: sonetSectionDataTable.setStatus('current')
sonetSectionDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: sonetSectionDataEntry.setStatus('current')
sonetSectionDataTraceReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetSectionDataTraceReceived.setStatus('current')
otuSectionConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1), )
if mibBuilder.loadTexts: otuSectionConfigTable.setStatus('current')
otuSectionConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: otuSectionConfigEntry.setStatus('current')
otuSectionConfigSignalDegradeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigSignalDegradeThreshold.setStatus('current')
otuSectionConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigSignalDegradePeriod.setStatus('current')
otuSectionConfigPayload = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 3), OtnPayloadType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigPayload.setStatus('current')
otuSectionConfigStuffing = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 4), EnableState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigStuffing.setStatus('current')
otuSectionConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigTraceExpected.setStatus('current')
otuSectionConfigTraceTransmitSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigTraceTransmitSapi.setStatus('current')
otuSectionConfigTraceTransmitDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigTraceTransmitDapi.setStatus('current')
otuSectionConfigTraceTransmitOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigTraceTransmitOpsp.setStatus('current')
otuSectionConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 9), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigTimMode.setStatus('current')
otuSectionDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2), )
if mibBuilder.loadTexts: otuSectionDataTable.setStatus('current')
otuSectionDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: otuSectionDataEntry.setStatus('current')
otuSectionDataResultingTotalBitrate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 1), Unsigned32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: otuSectionDataResultingTotalBitrate.setStatus('current')
otuSectionDataTraceReceivedSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: otuSectionDataTraceReceivedSapi.setStatus('current')
otuSectionDataTraceReceivedDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: otuSectionDataTraceReceivedDapi.setStatus('current')
otuSectionDataTraceReceivedOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: otuSectionDataTraceReceivedOpsp.setStatus('current')
oduSectionConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1), )
if mibBuilder.loadTexts: oduSectionConfigTable.setStatus('current')
oduSectionConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduSectionConfigEntry.setStatus('current')
oduSectionConfigSignalDegradeThres = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigSignalDegradeThres.setStatus('current')
oduSectionConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigSignalDegradePeriod.setStatus('current')
oduSectionConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigTraceExpected.setStatus('current')
oduSectionConfigTraceTransmitSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigTraceTransmitSapi.setStatus('current')
oduSectionConfigTraceTransmitDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigTraceTransmitDapi.setStatus('current')
oduSectionConfigTraceTransmitOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigTraceTransmitOpsp.setStatus('current')
oduSectionConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 7), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigTimMode.setStatus('current')
oduSectionDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2), )
if mibBuilder.loadTexts: oduSectionDataTable.setStatus('current')
oduSectionDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduSectionDataEntry.setStatus('current')
oduSectionDataTraceReceivedSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduSectionDataTraceReceivedSapi.setStatus('current')
oduSectionDataTraceReceivedDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduSectionDataTraceReceivedDapi.setStatus('current')
oduSectionDataTraceReceivedOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduSectionDataTraceReceivedOpsp.setStatus('current')
oduTcmAConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3), )
if mibBuilder.loadTexts: oduTcmAConfigTable.setStatus('current')
oduTcmAConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmAConfigEntry.setStatus('current')
oduTcmAConfigSignalDegradeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigSignalDegradeThreshold.setStatus('current')
oduTcmAConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigSignalDegradePeriod.setStatus('current')
oduTcmAConfigTcmLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 3), OtnTcmLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTcmLevel.setStatus('current')
oduTcmAConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTraceExpected.setStatus('current')
oduTcmAConfigTraceTransmitSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTraceTransmitSapi.setStatus('current')
oduTcmAConfigTraceTransmitDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTraceTransmitDapi.setStatus('current')
oduTcmAConfigTraceTransmitOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTraceTransmitOpsp.setStatus('current')
oduTcmAConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 8), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTimMode.setStatus('current')
oduTcmBConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4), )
if mibBuilder.loadTexts: oduTcmBConfigTable.setStatus('current')
oduTcmBConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmBConfigEntry.setStatus('current')
oduTcmBConfigSignalDegradeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigSignalDegradeThreshold.setStatus('current')
oduTcmBConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigSignalDegradePeriod.setStatus('current')
oduTcmBConfigTcmLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 3), OtnTcmLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTcmLevel.setStatus('current')
oduTcmBConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTraceExpected.setStatus('current')
oduTcmBConfigTraceTransmitSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTraceTransmitSapi.setStatus('current')
oduTcmBConfigTraceTransmitDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTraceTransmitDapi.setStatus('current')
oduTcmBConfigTraceTransmitOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTraceTransmitOpsp.setStatus('current')
oduTcmBConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 8), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTimMode.setStatus('current')
oduTcmCConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5), )
if mibBuilder.loadTexts: oduTcmCConfigTable.setStatus('current')
oduTcmCConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmCConfigEntry.setStatus('current')
oduTcmCConfigSignalDegradeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigSignalDegradeThreshold.setStatus('current')
oduTcmCConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigSignalDegradePeriod.setStatus('current')
oduTcmCConfigTcmLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 3), OtnTcmLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTcmLevel.setStatus('current')
oduTcmCConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTraceExpected.setStatus('current')
oduTcmCConfigTraceTransmitSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTraceTransmitSapi.setStatus('current')
oduTcmCConfigTraceTransmitDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTraceTransmitDapi.setStatus('current')
oduTcmCConfigTraceTransmitOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTraceTransmitOpsp.setStatus('current')
oduTcmCConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 8), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTimMode.setStatus('current')
oduTcmADataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6), )
if mibBuilder.loadTexts: oduTcmADataTable.setStatus('current')
oduTcmADataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmADataEntry.setStatus('current')
oduTcmADataTraceReceivedSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmADataTraceReceivedSapi.setStatus('current')
oduTcmADataTraceReceivedDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmADataTraceReceivedDapi.setStatus('current')
oduTcmADataTraceReceivedOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmADataTraceReceivedOpsp.setStatus('current')
oduTcmBDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7), )
if mibBuilder.loadTexts: oduTcmBDataTable.setStatus('current')
oduTcmBDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmBDataEntry.setStatus('current')
oduTcmBDataTraceReceivedSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmBDataTraceReceivedSapi.setStatus('current')
oduTcmBDataTraceReceivedDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmBDataTraceReceivedDapi.setStatus('current')
oduTcmBDataTraceReceivedOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmBDataTraceReceivedOpsp.setStatus('current')
oduTcmCDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8), )
if mibBuilder.loadTexts: oduTcmCDataTable.setStatus('current')
oduTcmCDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmCDataEntry.setStatus('current')
oduTcmCDataTraceReceivedSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmCDataTraceReceivedSapi.setStatus('current')
oduTcmCDataTraceReceivedDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmCDataTraceReceivedDapi.setStatus('current')
oduTcmCDataTraceReceivedOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmCDataTraceReceivedOpsp.setStatus('current')
inventoryTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1), )
if mibBuilder.loadTexts: inventoryTable.setStatus('current')
inventoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: inventoryEntry.setStatus('current')
inventoryUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryUnitName.setStatus('current')
inventoryFirmwarePackageRev = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryFirmwarePackageRev.setStatus('current')
inventoryHardwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryHardwareRev.setStatus('current')
inventorySoftwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventorySoftwareRev.setStatus('current')
inventoryFpgaRev = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryFpgaRev.setStatus('current')
inventorySerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventorySerialNum.setStatus('current')
inventoryPartnumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryPartnumber.setStatus('current')
inventoryCleiCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryCleiCode.setStatus('current')
inventoryVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryVendorId.setStatus('current')
inventoryType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 10), EntityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryType.setStatus('current')
inventoryUniversalSerialIdent = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryUniversalSerialIdent.setStatus('current')
inventoryMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryMacAddress.setStatus('current')
inventoryGradeInventory = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 13), Grade()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryGradeInventory.setStatus('current')
inventoryCfSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 14), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryCfSerialNum.setStatus('current')
inventoryCfModel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 15), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryCfModel.setStatus('current')
entityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2), )
if mibBuilder.loadTexts: entityTable.setStatus('current')
entityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: entityEntry.setStatus('current')
entityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: entityIndex.setStatus('current')
entityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityContainedIn.setStatus('current')
entityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 3), EntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityClass.setStatus('current')
entityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityClassInstanceNumber.setStatus('current')
entityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityIndexAid.setStatus('current')
entityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 6), EntityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityType.setStatus('current')
entityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 7), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityAssignmentState.setStatus('current')
entityEquipmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 8), EquipmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityEquipmentState.setStatus('current')
containsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3), )
if mibBuilder.loadTexts: containsTable.setStatus('current')
containsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"), (0, "ADVA-MIB", "containsIndex"))
if mibBuilder.loadTexts: containsEntry.setStatus('current')
containsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3, 1, 1), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: containsIndex.setStatus('current')
controlPlaneWdmEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4), )
if mibBuilder.loadTexts: controlPlaneWdmEntityTable.setStatus('current')
controlPlaneWdmEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneWdmEntityIndex"))
if mibBuilder.loadTexts: controlPlaneWdmEntityEntry.setStatus('current')
controlPlaneWdmEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: controlPlaneWdmEntityIndex.setStatus('current')
controlPlaneWdmEntityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmEntityContainedIn.setStatus('current')
controlPlaneWdmEntityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 3), CpWdmEntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmEntityClass.setStatus('current')
controlPlaneWdmEntityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmEntityClassInstanceNumber.setStatus('current')
controlPlaneWdmEntityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmEntityIndexAid.setStatus('current')
controlPlaneWdmEntityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 6), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmEntityAssignmentState.setStatus('current')
controlPlaneWdmContainsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 5), )
if mibBuilder.loadTexts: controlPlaneWdmContainsTable.setStatus('current')
controlPlaneWdmContainsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 5, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneWdmEntityIndex"), (0, "ADVA-MIB", "controlPlaneWdmContainsIndex"))
if mibBuilder.loadTexts: controlPlaneWdmContainsEntry.setStatus('current')
controlPlaneWdmContainsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 5, 1, 1), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmContainsIndex.setStatus('current')
controlPlaneEthEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6), )
if mibBuilder.loadTexts: controlPlaneEthEntityTable.setStatus('current')
controlPlaneEthEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneEthEntityIndex"))
if mibBuilder.loadTexts: controlPlaneEthEntityEntry.setStatus('current')
controlPlaneEthEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: controlPlaneEthEntityIndex.setStatus('current')
controlPlaneEthEntityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthEntityContainedIn.setStatus('current')
controlPlaneEthEntityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 3), CpWdmEntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthEntityClass.setStatus('current')
controlPlaneEthEntityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthEntityClassInstanceNumber.setStatus('current')
controlPlaneEthEntityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthEntityIndexAid.setStatus('current')
controlPlaneEthEntityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 6), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthEntityAssignmentState.setStatus('current')
controlPlaneEthContainsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 7), )
if mibBuilder.loadTexts: controlPlaneEthContainsTable.setStatus('current')
controlPlaneEthContainsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 7, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneEthEntityIndex"), (0, "ADVA-MIB", "controlPlaneEthContainsIndex"))
if mibBuilder.loadTexts: controlPlaneEthContainsEntry.setStatus('current')
controlPlaneEthContainsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 7, 1, 1), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthContainsIndex.setStatus('current')
ptpEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10), )
if mibBuilder.loadTexts: ptpEntityTable.setStatus('current')
ptpEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1), ).setIndexNames((0, "ADVA-MIB", "ptpEntityIndex"))
if mibBuilder.loadTexts: ptpEntityEntry.setStatus('current')
ptpEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ptpEntityIndex.setStatus('current')
ptpEntityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityContainedIn.setStatus('current')
ptpEntityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 3), EntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityClass.setStatus('current')
ptpEntityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityClassInstanceNumber.setStatus('current')
ptpEntityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityIndexAid.setStatus('current')
ptpEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 6), EntityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityType.setStatus('current')
ptpEntityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 7), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityAssignmentState.setStatus('current')
ptpEntityEquipmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 8), EquipmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityEquipmentState.setStatus('current')
ptpEntityReferencedTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 9), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityReferencedTo.setStatus('current')
vtpEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11), )
if mibBuilder.loadTexts: vtpEntityTable.setStatus('current')
vtpEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1), ).setIndexNames((0, "ADVA-MIB", "vtpEntityIndex"))
if mibBuilder.loadTexts: vtpEntityEntry.setStatus('current')
vtpEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vtpEntityIndex.setStatus('current')
vtpEntityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityContainedIn.setStatus('current')
vtpEntityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 3), EntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityClass.setStatus('current')
vtpEntityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityClassInstanceNumber.setStatus('current')
vtpEntityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityIndexAid.setStatus('current')
vtpEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 6), EntityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityType.setStatus('current')
vtpEntityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 7), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityAssignmentState.setStatus('current')
vtpEntityEquipmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 8), EquipmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityEquipmentState.setStatus('current')
vtpEntityReferencedTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 9), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityReferencedTo.setStatus('current')
controlPlaneOtnEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12), )
if mibBuilder.loadTexts: controlPlaneOtnEntityTable.setStatus('current')
controlPlaneOtnEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneOtnEntityIndex"))
if mibBuilder.loadTexts: controlPlaneOtnEntityEntry.setStatus('current')
controlPlaneOtnEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: controlPlaneOtnEntityIndex.setStatus('current')
controlPlaneOtnEntityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnEntityContainedIn.setStatus('current')
controlPlaneOtnEntityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 3), CpWdmEntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnEntityClass.setStatus('current')
controlPlaneOtnEntityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnEntityClassInstanceNumber.setStatus('current')
controlPlaneOtnEntityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnEntityIndexAid.setStatus('current')
controlPlaneOtnEntityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 6), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnEntityAssignmentState.setStatus('current')
controlPlaneOtnContainsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 13), )
if mibBuilder.loadTexts: controlPlaneOtnContainsTable.setStatus('current')
controlPlaneOtnContainsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 13, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneOtnEntityIndex"), (0, "ADVA-MIB", "controlPlaneOtnContainsIndex"))
if mibBuilder.loadTexts: controlPlaneOtnContainsEntry.setStatus('current')
controlPlaneOtnContainsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 13, 1, 1), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnContainsIndex.setStatus('current')
swDbFileTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1), )
if mibBuilder.loadTexts: swDbFileTable.setStatus('current')
swDbFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1), ).setIndexNames((0, "ADVA-MIB", "swDbFileIndex"))
if mibBuilder.loadTexts: swDbFileEntry.setStatus('current')
swDbFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 1), EntityIndex())
if mibBuilder.loadTexts: swDbFileIndex.setStatus('current')
swDbFileArea = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 2), FileArea()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileArea.setStatus('current')
swDbFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 3), FileType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileType.setStatus('current')
swDbFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 4), Unsigned32()).setUnits('Byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileSize.setStatus('current')
swDbFileCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileCreationTime.setStatus('current')
swDbFileVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileVersion.setStatus('current')
swDbFileGrade = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 7), Grade()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileGrade.setStatus('current')
swDbFileComment = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDbFileComment.setStatus('current')
swDbFileFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileFileName.setStatus('current')
swDbFileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDbFileRowStatus.setStatus('current')
swDbFilePgmType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 11), PgmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFilePgmType.setStatus('current')
fwDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2), )
if mibBuilder.loadTexts: fwDataTable.setStatus('current')
fwDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: fwDataEntry.setStatus('current')
fwDataNewVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataNewVersion.setStatus('current')
fwDataStandbyVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataStandbyVersion.setStatus('current')
fwDataServiceImpairment = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 3), ServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataServiceImpairment.setStatus('current')
fwDataBootStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 4), BootState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataBootStatus.setStatus('current')
fwDataFirmwarePackageRev = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataFirmwarePackageRev.setStatus('current')
fwDataStandbyServiceImpairment = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 6), StandbyServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataStandbyServiceImpairment.setStatus('current')
fwDataFirmwareAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 7), NoYesNA()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataFirmwareAvailable.setStatus('current')
fwDataFirmwareApproved = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 8), NoYesNA()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataFirmwareApproved.setStatus('current')
fwDataFirmwarePackageRevBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataFirmwarePackageRevBackup.setStatus('current')
fwDataReadyForActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 10), YesNoNA()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataReadyForActivation.setStatus('current')
fwDataActivationReadyOnStandby = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 11), YesNoNA()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataActivationReadyOnStandby.setStatus('current')
fwDataProtectionPart = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 12), FspR7YesNo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataProtectionPart.setStatus('current')
fwDataForm = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 13), ModuleForm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataForm.setStatus('current')
fwDataStandbyFirmwareAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 14), NoYesNA()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataStandbyFirmwareAvailable.setStatus('current')
coldRestartCapTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 3), )
if mibBuilder.loadTexts: coldRestartCapTable.setStatus('current')
coldRestartCapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 3, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: coldRestartCapEntry.setStatus('current')
coldRestartCapServiceAffectingCap = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 3, 1, 1), ServiceAffectingCaps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coldRestartCapServiceAffectingCap.setStatus('current')
eqpFwUpgradeRequest = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 10), CommandEqpt()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqpFwUpgradeRequest.setStatus('current')
eqpFwServiceImpairment = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 11), ServiceAffecting()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqpFwServiceImpairment.setStatus('current')
eqpFwNextEqpForUpdate = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 12), EntityIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqpFwNextEqpForUpdate.setStatus('current')
eqpFwEqpType = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 13), FspR7EquipmentType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqpFwEqpType.setStatus('current')
eqpFwNcuServerBusy = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 14), FspR7FalseTrue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqpFwNcuServerBusy.setStatus('current')
eqpFwEqpServerBusy = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 15), FspR7FalseTrue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqpFwEqpServerBusy.setStatus('current')
updateEqpt = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: updateEqpt.setStatus('current')
installedEqpt = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedEqpt.setStatus('current')
selectedFile = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 18), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: selectedFile.setStatus('current')
ncuActivationDate = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 19), FspR7Date()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuActivationDate.setStatus('current')
ncuActivationTime = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 20), FspR7Time()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuActivationTime.setStatus('current')
ncuScheduledActivation = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 21), NcuAutoActivation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuScheduledActivation.setStatus('current')
ncuScheduledDbRestore = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 22), RestoreActivation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuScheduledDbRestore.setStatus('current')
encryptionFwpFile = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 23), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: encryptionFwpFile.setStatus('current')
clearRdiskRequest = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("undefined", 0), ("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearRdiskRequest.setStatus('current')
ncuActivationDateUtc = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 25), FspR7Date()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuActivationDateUtc.setStatus('current')
ncuActivationTimeUtc = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 26), FspR7Time()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuActivationTimeUtc.setStatus('current')
neBackupEncryption = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 38), EnableState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neBackupEncryption.setStatus('current')
neBackupPassword = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 39), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neBackupPassword.setStatus('current')
neF7AutomaticRemoteBackupEncryption = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 40), EnableState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupEncryption.setStatus('current')
neF7AutomaticRemoteBackupPassword = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 41), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupPassword.setStatus('current')
neBackupUsers = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 42), FspR7UsersDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neBackupUsers.setStatus('current')
neInitialConnectionMode = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 43), FspR7EnableDisable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neInitialConnectionMode.setStatus('current')
neF7AutomaticRemoteBackupUsers = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 44), FspR7UsersDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupUsers.setStatus('current')
neRestoreConfig = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 1), RestoreActivation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neRestoreConfig.setStatus('current')
swDbDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2), )
if mibBuilder.loadTexts: swDbDataTable.setStatus('current')
swDbDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1), ).setIndexNames((0, "ADVA-MIB", "swDbDataIndex"))
if mibBuilder.loadTexts: swDbDataEntry.setStatus('current')
swDbDataIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 1), EntityIndex())
if mibBuilder.loadTexts: swDbDataIndex.setStatus('current')
swDbDataArea = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 2), FileArea()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataArea.setStatus('current')
swDbDataProgramVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataProgramVersion.setStatus('current')
swDbDataDatabaseVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataDatabaseVersion.setStatus('current')
swDbDataActivationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataActivationTime.setStatus('current')
swDbDataRestoreConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 6), RestoreActivation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataRestoreConfig.setStatus('current')
swDbDataFirmwareSetVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataFirmwareSetVersion.setStatus('current')
swDbDataNcuSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNcuSoftwareVersion.setStatus('current')
swDbDataStandbyPartitionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 9), PartitionStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataStandbyPartitionStatus.setStatus('current')
swDbDataNumEqpt = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumEqpt.setStatus('current')
swDbDataNumLegacyEqpt = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumLegacyEqpt.setStatus('current')
swDbDataNumNativeSaUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumNativeSaUpdate.setStatus('current')
swDbDataNumNativeNsaUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumNativeNsaUpdate.setStatus('current')
swDbDataNumLegacyUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumLegacyUpdate.setStatus('current')
swDbDataNumSaNotReady = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumSaNotReady.setStatus('current')
swDbDataNumNsaNotReady = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumNsaNotReady.setStatus('current')
swDbDataCapTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3), )
if mibBuilder.loadTexts: swDbDataCapTable.setStatus('current')
swDbDataCapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3, 1), ).setIndexNames((0, "ADVA-MIB", "swDbDataCapUpgradeRequest"))
if mibBuilder.loadTexts: swDbDataCapEntry.setStatus('current')
swDbDataCapUpgradeRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("undefined", 0), ("none", 1), ("download", 2), ("install", 3), ("activate", 4), ("revertToPrevious", 5), ("reboot", 6), ("downloadInstallActivateReboot", 7), ("installActivateReboot", 8), ("revertToPreviousReboot", 9), ("activateAlp", 10), ("activateDefaultAlp", 11), ("upload", 12), ("autoDownloadInstall", 13), ("autoInstall", 14), ("fwpInstall", 15), ("fwpDownloadInstall", 16), ("downloadCf", 17), ("uploadCf", 18), ("installCf", 19), ("autoInstallCf", 20), ("uploadPa", 21), ("activateWithFwp", 22), ("forceReboot", 23), ("stbyFwpInstall", 24))))
if mibBuilder.loadTexts: swDbDataCapUpgradeRequest.setStatus('current')
swDbDataCapRestoreConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3, 1, 2), RestoreActivationCaps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataCapRestoreConfig.setStatus('current')
swDbDataDefaultsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4), )
if mibBuilder.loadTexts: swDbDataDefaultsTable.setStatus('current')
swDbDataDefaultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4, 1), ).setIndexNames((0, "ADVA-MIB", "swDbDataDefaultsUpgradeRequest"))
if mibBuilder.loadTexts: swDbDataDefaultsEntry.setStatus('current')
swDbDataDefaultsUpgradeRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("undefined", 0), ("none", 1), ("download", 2), ("install", 3), ("activate", 4), ("revertToPrevious", 5), ("reboot", 6), ("downloadInstallActivateReboot", 7), ("installActivateReboot", 8), ("revertToPreviousReboot", 9), ("activateAlp", 10), ("activateDefaultAlp", 11), ("upload", 12), ("autoDownloadInstall", 13), ("autoInstall", 14), ("fwpInstall", 15), ("fwpDownloadInstall", 16), ("downloadCf", 17), ("uploadCf", 18), ("installCf", 19), ("autoInstallCf", 20), ("uploadPa", 21), ("activateWithFwp", 22), ("forceReboot", 23), ("stbyFwpInstall", 24))))
if mibBuilder.loadTexts: swDbDataDefaultsUpgradeRequest.setStatus('current')
swDbDataDefaultsRestoreConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4, 1, 2), RestoreActivation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataDefaultsRestoreConfig.setStatus('current')
snmpServerPort = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpServerPort.setStatus('current')
snmpProxyServerAdminState = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 3), FspR7AdminStateSnmpProxy()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpProxyServerAdminState.setStatus('current')
snmpProxyServerPort = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpProxyServerPort.setStatus('current')
snmpProxyServerSynchroState = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 5), SnmpProxySynchronizationState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpProxyServerSynchroState.setStatus('current')
snmpProxyServerSynchroStage = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 6), SnmpProxySynchronizationStage()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: snmpProxyServerSynchroStage.setStatus('current')
snmpProxyEntrySingleTargetOutTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10), )
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutTable.setStatus('current')
snmpProxyEntrySingleTargetOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1), ).setIndexNames((0, "ADVA-MIB", "snmpProxyEntrySingleTargetOutAddress"), (0, "ADVA-MIB", "snmpProxyEntrySingleTargetOutPort"))
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutEntry.setStatus('current')
snmpProxyEntrySingleTargetOutAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 1), IpAddress())
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutAddress.setStatus('current')
snmpProxyEntrySingleTargetOutPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutPort.setStatus('current')
snmpProxyEntrySingleTargetOutNodeAgentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 3), DestinationNodeOrAgentState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutNodeAgentStatus.setStatus('current')
snmpProxyEntrySingleTargetOutContext = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutContext.setStatus('current')
snmpProxyEntrySingleTargetOutRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutRowStatus.setStatus('current')
snmpProxyEntrySingleTargetOutAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 6), FspR7AdminStateSnmpProxy()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutAdminState.setStatus('current')
snmpProxyEntrySingleTargetOutUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 7), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutUserName.setStatus('current')
mibBuilder.exportSymbols("ADVA-MIB", neRestoreFileBackupDate=neRestoreFileBackupDate, FspDate=FspDate, aosCommon=aosCommon, eqpFwEqpType=eqpFwEqpType, inventoryCfModel=inventoryCfModel, swDbDataProgramVersion=swDbDataProgramVersion, oduTcmBDataTraceReceivedDapi=oduTcmBDataTraceReceivedDapi, neF7AutomaticRemoteBackupUsers=neF7AutomaticRemoteBackupUsers, FspR7FalseTrue=FspR7FalseTrue, entityEntry=entityEntry, oduTcmCConfigEntry=oduTcmCConfigEntry, BootState=BootState, OtnTcmLevelCaps=OtnTcmLevelCaps, controlPlaneWdmEntityTable=controlPlaneWdmEntityTable, neMibVariant=neMibVariant, neSwUpgradeServerPasswd=neSwUpgradeServerPasswd, oduTcmCConfigTable=oduTcmCConfigTable, controlPlaneOtnEntityEntry=controlPlaneOtnEntityEntry, swDbDataFirmwareSetVersion=swDbDataFirmwareSetVersion, DestinationNodeOrAgentState=DestinationNodeOrAgentState, AssignmentState=AssignmentState, vtpEntityContainedIn=vtpEntityContainedIn, IdentityTranslation=IdentityTranslation, neF7AutomaticBackupEntry=neF7AutomaticBackupEntry, ncuActivationTime=ncuActivationTime, oduTcmAConfigSignalDegradeThreshold=oduTcmAConfigSignalDegradeThreshold, inventoryUniversalSerialIdent=inventoryUniversalSerialIdent, oduTcmBDataTraceReceivedSapi=oduTcmBDataTraceReceivedSapi, neSwUpgradeState=neSwUpgradeState, PartitionStatus=PartitionStatus, PYSNMP_MODULE_ID=advaMIB, oduTcmBConfigSignalDegradePeriod=oduTcmBConfigSignalDegradePeriod, ptpEntityReferencedTo=ptpEntityReferencedTo, fwDataStandbyVersion=fwDataStandbyVersion, KBytes=KBytes, otuSectionConfigEntry=otuSectionConfigEntry, controlPlaneEthEntityClass=controlPlaneEthEntityClass, NeSwUpgradeStatusType=NeSwUpgradeStatusType, fwDataFirmwareApproved=fwDataFirmwareApproved, ApsHoldoffTime=ApsHoldoffTime, neManufacturer=neManufacturer, swDbFileType=swDbFileType, sonetSectionConfigTraceTransmit=sonetSectionConfigTraceTransmit, oduTcmCDataEntry=oduTcmCDataEntry, swDbFilePgmType=swDbFilePgmType, otuSectionConfigTraceExpected=otuSectionConfigTraceExpected, snmpProxyEntrySingleTargetOutEntry=snmpProxyEntrySingleTargetOutEntry, controlPlaneWdmEntityIndex=controlPlaneWdmEntityIndex, oduTcmBConfigTraceTransmitOpsp=oduTcmBConfigTraceTransmitOpsp, neSwUpgradeServerDirectory=neSwUpgradeServerDirectory, controlPlaneOtnEntityTable=controlPlaneOtnEntityTable, FspR7AdminStateSnmpProxy=FspR7AdminStateSnmpProxy, neF7AutomaticBackupTable=neF7AutomaticBackupTable, controlPlaneEthEntityIndex=controlPlaneEthEntityIndex, snmpProxyServerAdminState=snmpProxyServerAdminState, controlPlaneEthEntityEntry=controlPlaneEthEntityEntry, Counter64String=Counter64String, snmpServerPort=snmpServerPort, coldRestartCapTable=coldRestartCapTable, ncuScheduledActivation=ncuScheduledActivation, neStorageIndex=neStorageIndex, neBackupRestore=neBackupRestore, neAutoBackupInterval=neAutoBackupInterval, swDbDataArea=swDbDataArea, OtnPayloadType=OtnPayloadType, aos=aos, FspR7EquipmentType=FspR7EquipmentType, FileArea=FileArea, provAssignmentState=provAssignmentState, neBackupPassword=neBackupPassword, ncuActivationTimeUtc=ncuActivationTimeUtc, ApsDirection=ApsDirection, neTrapsinkAddress=neTrapsinkAddress, FspR7Date=FspR7Date, snmpAgent=snmpAgent, fsp1000adm=fsp1000adm, oduTcmAConfigEntry=oduTcmAConfigEntry, oduTcmADataTable=oduTcmADataTable, snmpWriteAccessRestriction=snmpWriteAccessRestriction, controlPlaneOtnEntityClassInstanceNumber=controlPlaneOtnEntityClassInstanceNumber, products=products, F7AutoBackupRunState=F7AutoBackupRunState, containsIndex=containsIndex, snmpWriteAccessTable=snmpWriteAccessTable, inventoryFpgaRev=inventoryFpgaRev, neBackupRestoreRequest=neBackupRestoreRequest, swDbDataNumNsaNotReady=swDbDataNumNsaNotReady, entityClassInstanceNumber=entityClassInstanceNumber, otuSectionDataTable=otuSectionDataTable, EntityIndex=EntityIndex, neF7AutomaticRemoteBackupTimeStamp=neF7AutomaticRemoteBackupTimeStamp, advaMIB=advaMIB, oduSectionConfigSignalDegradeThres=oduSectionConfigSignalDegradeThres, EthDuplexModeCaps=EthDuplexModeCaps, oduTcmADataEntry=oduTcmADataEntry, inventoryFirmwarePackageRev=inventoryFirmwarePackageRev, inventoryPartnumber=inventoryPartnumber, oduTcmBConfigTraceTransmitSapi=oduTcmBConfigTraceTransmitSapi, Grade=Grade, neSwUpgradeNeDirectory=neSwUpgradeNeDirectory, sonetSectionConfigTraceExpected=sonetSectionConfigTraceExpected, neF7AutomaticBackupStartDate=neF7AutomaticBackupStartDate, snmpProxyServerPort=snmpProxyServerPort, swVersionInactiveApplSw=swVersionInactiveApplSw, neTrapsinkRowStatus=neTrapsinkRowStatus, oduTcmAConfigTimMode=oduTcmAConfigTimMode, SonetVcBundleAllocation=SonetVcBundleAllocation, neSwUpgradeFileName=neSwUpgradeFileName, sonet=sonet, entityClass=entityClass, sonetSectionConfigTimingSource=sonetSectionConfigTimingSource, provContainerTable=provContainerTable, otuSectionConfigStuffing=otuSectionConfigStuffing, controlPlaneWdmEntityIndexAid=controlPlaneWdmEntityIndexAid, OnOff=OnOff, inventoryTable=inventoryTable, ptpEntityAssignmentState=ptpEntityAssignmentState, software=software, vtpEntityAssignmentState=vtpEntityAssignmentState, oduTcmADataTraceReceivedDapi=oduTcmADataTraceReceivedDapi, ncuActivationDateUtc=ncuActivationDateUtc, sonetConfig=sonetConfig, fwDataServiceImpairment=fwDataServiceImpairment, otuSectionDataTraceReceivedDapi=otuSectionDataTraceReceivedDapi, swDbDataCapRestoreConfig=swDbDataCapRestoreConfig, oduTcmCConfigTraceTransmitSapi=oduTcmCConfigTraceTransmitSapi, neBackupUsers=neBackupUsers, fwDataForm=fwDataForm, controlPlaneOtnContainsEntry=controlPlaneOtnContainsEntry, neEventLogVarCounter64Val=neEventLogVarCounter64Val, swDbFileTable=swDbFileTable, OtnTcmLevel=OtnTcmLevel, swDbFileRowStatus=swDbFileRowStatus, otuSectionConfigSignalDegradeThreshold=otuSectionConfigSignalDegradeThreshold, oduSectionDataEntry=oduSectionDataEntry, neF7AutomaticBackupIndex=neF7AutomaticBackupIndex, vtpEntityTable=vtpEntityTable, oduTcmBDataEntry=oduTcmBDataEntry, oduTcmBConfigTimMode=oduTcmBConfigTimMode, controlPlaneOtnEntityIndexAid=controlPlaneOtnEntityIndexAid, neEventLogVarTable=neEventLogVarTable, sonetSectionDataEntry=sonetSectionDataEntry, oduTcmAConfigTraceExpected=oduTcmAConfigTraceExpected, NcuAutoActivation=NcuAutoActivation, containsTable=containsTable, entityEquipmentState=entityEquipmentState, swDbDataNumEqpt=swDbDataNumEqpt, NeSwInstallStatusType=NeSwInstallStatusType, vtpEntityIndex=vtpEntityIndex, controlPlaneEthContainsIndex=controlPlaneEthContainsIndex, fspR7=fspR7, sonetSectionConfigSignalDegradeThreshhold=sonetSectionConfigSignalDegradeThreshhold, SnmpProxySynchronizationStage=SnmpProxySynchronizationStage, inventoryCleiCode=inventoryCleiCode, neEventLogVarId=neEventLogVarId, neEventsLogged=neEventsLogged, TrapCounter=TrapCounter, neEventLogIndex=neEventLogIndex, neF7AutomaticRemoteBackupSrvPass=neF7AutomaticRemoteBackupSrvPass, SonetTraceFormCaps=SonetTraceFormCaps, PgmType=PgmType, controlPlaneEthEntityAssignmentState=controlPlaneEthEntityAssignmentState, neSwInstallState=neSwInstallState, controlPlaneOtnEntityAssignmentState=controlPlaneOtnEntityAssignmentState, snmpProxyServerSynchroStage=snmpProxyServerSynchroStage, ApsDirectionCaps=ApsDirectionCaps, neStorageTable=neStorageTable, oduTcmCDataTraceReceivedOpsp=oduTcmCDataTraceReceivedOpsp, FspR7TrapsinkLifetime=FspR7TrapsinkLifetime, oduSectionConfigTable=oduSectionConfigTable, entityType=entityType, neTrapsinkEntry=neTrapsinkEntry, neEventLogVarIpAddressVal=neEventLogVarIpAddressVal, ServiceAffecting=ServiceAffecting, containsEntry=containsEntry, otuSectionConfigTable=otuSectionConfigTable, vtpEntityEntry=vtpEntityEntry, FspTime=FspTime, inventorySerialNum=inventorySerialNum, otuSectionDataTraceReceivedSapi=otuSectionDataTraceReceivedSapi, updateBackupRestoreMib=updateBackupRestoreMib, controlPlaneWdmContainsEntry=controlPlaneWdmContainsEntry, ptpEntityType=ptpEntityType, CommandEqpt=CommandEqpt, config=config, swVersionNextBoot=swVersionNextBoot, neF7AutomaticRemoteBackupSrvLogin=neF7AutomaticRemoteBackupSrvLogin, otuSectionDataTraceReceivedOpsp=otuSectionDataTraceReceivedOpsp, StandbyServiceAffecting=StandbyServiceAffecting, vtpEntityType=vtpEntityType, fsp1500=fsp1500, controlPlaneWdmContainsTable=controlPlaneWdmContainsTable, swDbDataDefaultsEntry=swDbDataDefaultsEntry, snmpWriteAccessNmsName=snmpWriteAccessNmsName, sonetSectionConfigTimMode=sonetSectionConfigTimMode, encryptionFwpFile=encryptionFwpFile, FileTransferProtocol=FileTransferProtocol, snmpProxyEntrySingleTargetOutContext=snmpProxyEntrySingleTargetOutContext, eqpFwNcuServerBusy=eqpFwNcuServerBusy, neSwUpgradeRequest=neSwUpgradeRequest, otuSectionConfigPayload=otuSectionConfigPayload, controlPlaneOtnContainsTable=controlPlaneOtnContainsTable, oduTcmAConfigTcmLevel=oduTcmAConfigTcmLevel, neSwUpgradeServerLogin=neSwUpgradeServerLogin, ptpEntityContainedIn=ptpEntityContainedIn, LoopConfigCaps=LoopConfigCaps, fsp1000=fsp1000, fsp3000alm=fsp3000alm, neAutoBackupServerAddress=neAutoBackupServerAddress, LogicalIfTransport=LogicalIfTransport, vtpEntityClass=vtpEntityClass, vtpEntityIndexAid=vtpEntityIndexAid, vtpEntityReferencedTo=vtpEntityReferencedTo, controlPlaneOtnEntityIndex=controlPlaneOtnEntityIndex, snmpProxyEntrySingleTargetOutAddress=snmpProxyEntrySingleTargetOutAddress, neMemorySizeTotal=neMemorySizeTotal, SonetSectSigDegThresCaps=SonetSectSigDegThresCaps, RestoreActivation=RestoreActivation, neF7AutomaticBackupStartTime=neF7AutomaticBackupStartTime, neMemorySizeFree=neMemorySizeFree, neSwUpgradeCommonIpSrv=neSwUpgradeCommonIpSrv, entityContainedIn=entityContainedIn, ProtectionMechCaps=ProtectionMechCaps, swDbDataNumNativeSaUpdate=swDbDataNumNativeSaUpdate, oduTcmADataTraceReceivedOpsp=oduTcmADataTraceReceivedOpsp, otuSectionDataEntry=otuSectionDataEntry, otn=otn, neF7AutomaticBackupTimeStamp=neF7AutomaticBackupTimeStamp, inventoryGradeInventory=inventoryGradeInventory, otuSectionConfigSignalDegradePeriod=otuSectionConfigSignalDegradePeriod, neF7AutomaticBackupInterval=neF7AutomaticBackupInterval, FspR7AdminStateSnmpProxyCaps=FspR7AdminStateSnmpProxyCaps, snmpProxyEntrySingleTargetOutNodeAgentStatus=snmpProxyEntrySingleTargetOutNodeAgentStatus, neEventLogEntry=neEventLogEntry, neAutoBackupNextActionAt=neAutoBackupNextActionAt, swDbDataCapUpgradeRequest=swDbDataCapUpgradeRequest, neSwUpgradeType=neSwUpgradeType, fsp150cm=fsp150cm, ptpEntityIndex=ptpEntityIndex, snmpProxyEntrySingleTargetOutUserName=snmpProxyEntrySingleTargetOutUserName, neBackupRestoreState=neBackupRestoreState, neF7AutomaticRemoteBackupEncryption=neF7AutomaticRemoteBackupEncryption, vtpEntityClassInstanceNumber=vtpEntityClassInstanceNumber, snmpWriteAccessNmsAddress=snmpWriteAccessNmsAddress, neEventLogVarInteger32Val=neEventLogVarInteger32Val, sonetSectionConfigTable=sonetSectionConfigTable, FileType=FileType, oduSectionDataTraceReceivedOpsp=oduSectionDataTraceReceivedOpsp, oduTcmBDataTable=oduTcmBDataTable, fwDataActivationReadyOnStandby=fwDataActivationReadyOnStandby, neRestoreConfig=neRestoreConfig, EnableState=EnableState, FspR7EquipmentTypeCaps=FspR7EquipmentTypeCaps, neTrapsinkCommunity=neTrapsinkCommunity)
mibBuilder.exportSymbols("ADVA-MIB", swDbFileVersion=swDbFileVersion, oduTcmCConfigSignalDegradePeriod=oduTcmCConfigSignalDegradePeriod, LoopConfig=LoopConfig, neAutoBackupConfig=neAutoBackupConfig, fspNm=fspNm, swDbFileComment=swDbFileComment, oduTcmCConfigTimMode=oduTcmCConfigTimMode, aosProducts=aosProducts, OhTerminationLevel=OhTerminationLevel, LogicalIfTransportCaps=LogicalIfTransportCaps, swDbDataEntry=swDbDataEntry, ptpEntityClassInstanceNumber=ptpEntityClassInstanceNumber, EnableStateCaps=EnableStateCaps, inventoryCfSerialNum=inventoryCfSerialNum, swDbFileCreationTime=swDbFileCreationTime, neAutoBackup=neAutoBackup, events=events, swDbDataNumLegacyUpdate=swDbDataNumLegacyUpdate, snmpProxyEntrySingleTargetOutAdminState=snmpProxyEntrySingleTargetOutAdminState, neTrapsinkPort=neTrapsinkPort, controlPlaneOtnEntityClass=controlPlaneOtnEntityClass, neSwUpgradeTransferProtocol=neSwUpgradeTransferProtocol, swDbDataDefaultsRestoreConfig=swDbDataDefaultsRestoreConfig, swDbDataDatabaseVersion=swDbDataDatabaseVersion, neBackupRestoreFile=neBackupRestoreFile, controlPlaneWdmEntityClass=controlPlaneWdmEntityClass, neInitialConnectionMode=neInitialConnectionMode, ApsHoldoffTimeCaps=ApsHoldoffTimeCaps, swDbDataRestoreConfig=swDbDataRestoreConfig, provContainerEntry=provContainerEntry, controlPlaneEthEntityClassInstanceNumber=controlPlaneEthEntityClassInstanceNumber, oduTcmAConfigTraceTransmitSapi=oduTcmAConfigTraceTransmitSapi, OtnPayloadTypeCaps=OtnPayloadTypeCaps, inventoryEntry=inventoryEntry, neEventLogNotificationOID=neEventLogNotificationOID, ptpEntityIndexAid=ptpEntityIndexAid, oduTcmBConfigEntry=oduTcmBConfigEntry, SnmpProxySynchronizationState=SnmpProxySynchronizationState, oduTcmAConfigTraceTransmitOpsp=oduTcmAConfigTraceTransmitOpsp, controlPlaneEthEntityTable=controlPlaneEthEntityTable, controlPlaneOtnEntityContainedIn=controlPlaneOtnEntityContainedIn, oduTcmCConfigTraceTransmitOpsp=oduTcmCConfigTraceTransmitOpsp, coldRestartCapEntry=coldRestartCapEntry, ArcState=ArcState, otuSectionConfigTraceTransmitOpsp=otuSectionConfigTraceTransmitOpsp, TimModeCaps=TimModeCaps, ptpEntityEquipmentState=ptpEntityEquipmentState, neEventLogVarEntry=neEventLogVarEntry, neF7AutomaticRemoteBackupPassword=neF7AutomaticRemoteBackupPassword, ptpEntityEntry=ptpEntityEntry, neF7AutomaticRemoteBackupSrvDir=neF7AutomaticRemoteBackupSrvDir, controlPlaneEthEntityContainedIn=controlPlaneEthEntityContainedIn, oduSectionDataTable=oduSectionDataTable, fwDataFirmwarePackageRevBackup=fwDataFirmwarePackageRevBackup, otuSectionConfigTimMode=otuSectionConfigTimMode, transportStandards=transportStandards, oduTcmCDataTable=oduTcmCDataTable, oduTcmBConfigTable=oduTcmBConfigTable, provEquipmentState=provEquipmentState, eqpFwServiceImpairment=eqpFwServiceImpairment, oduSectionConfigTraceExpected=oduSectionConfigTraceExpected, inventoryType=inventoryType, neF7AutomaticRemoteBackupSrcIp=neF7AutomaticRemoteBackupSrcIp, VirtualContainerType=VirtualContainerType, ncuScheduledDbRestore=ncuScheduledDbRestore, fwDataTable=fwDataTable, neStorageDescr=neStorageDescr, controlPlaneOtnContainsIndex=controlPlaneOtnContainsIndex, swDbDataNumNativeNsaUpdate=swDbDataNumNativeNsaUpdate, swDbFileIndex=swDbFileIndex, oduSectionConfigTraceTransmitOpsp=oduSectionConfigTraceTransmitOpsp, oduTcmBConfigTraceExpected=oduTcmBConfigTraceExpected, swDbFileFileName=swDbFileFileName, swVersionTable=swVersionTable, neSwUpgradeServerAddress=neSwUpgradeServerAddress, neEventLogVarOctetStringVal=neEventLogVarOctetStringVal, FspR7YesNo=FspR7YesNo, updateEqpt=updateEqpt, inventoryVendorId=inventoryVendorId, EntityType=EntityType, fsp150=fsp150, snmpProxyEntrySingleTargetOutTable=snmpProxyEntrySingleTargetOutTable, VirtualContainerTypeCaps=VirtualContainerTypeCaps, SourceIpAddress=SourceIpAddress, ncuActivationDate=ncuActivationDate, inventoryHardwareRev=inventoryHardwareRev, entityIndexAid=entityIndexAid, neStorageEntry=neStorageEntry, EntityClass=EntityClass, installedEqpt=installedEqpt, fsp3000c=fsp3000c, ModuleForm=ModuleForm, controlPlaneWdmEntityClassInstanceNumber=controlPlaneWdmEntityClassInstanceNumber, controlPlaneEthContainsTable=controlPlaneEthContainsTable, neStorageCapacity=neStorageCapacity, oduTcmBConfigSignalDegradeThreshold=oduTcmBConfigSignalDegradeThreshold, swDbDataIndex=swDbDataIndex, FspR7EnableDisable=FspR7EnableDisable, neAutoBackupServerPasswd=neAutoBackupServerPasswd, swDbDataTable=swDbDataTable, neEventLogVarIndex=neEventLogVarIndex, neEventLogVarType=neEventLogVarType, swDbDataDefaultsUpgradeRequest=swDbDataDefaultsUpgradeRequest, fwDataBootStatus=fwDataBootStatus, swAdmin=swAdmin, controlPlaneEthContainsEntry=controlPlaneEthContainsEntry, ProtectionMech=ProtectionMech, oduSectionConfigEntry=oduSectionConfigEntry, neF7AutomaticRemoteBackupCommonIpSrv=neF7AutomaticRemoteBackupCommonIpSrv, swVersionEntry=swVersionEntry, neTrapsinkVersion=neTrapsinkVersion, neAutoBackupServerDirectory=neAutoBackupServerDirectory, oduSectionConfigTraceTransmitSapi=oduSectionConfigTraceTransmitSapi, entityAssignmentState=entityAssignmentState, fwDataStandbyServiceImpairment=fwDataStandbyServiceImpairment, swVersionActiveApplSw=swVersionActiveApplSw, fwDataStandbyFirmwareAvailable=fwDataStandbyFirmwareAvailable, AvailState=AvailState, neF7AutomaticRemoteBackupSrvIp=neF7AutomaticRemoteBackupSrvIp, oduTcmCConfigTraceExpected=oduTcmCConfigTraceExpected, neEventLogIdentityTranslation=neEventLogIdentityTranslation, OhTerminationLevelCaps=OhTerminationLevelCaps, swDbFileSize=swDbFileSize, oduTcmCConfigTcmLevel=oduTcmCConfigTcmLevel, oduTcmCConfigSignalDegradeThreshold=oduTcmCConfigSignalDegradeThreshold, neEventLogTimeStamp=neEventLogTimeStamp, dbAdmin=dbAdmin, ServiceImpairment=ServiceImpairment, fsp2000=fsp2000, fwDataEntry=fwDataEntry, YesNoNA=YesNoNA, vtpEntityEquipmentState=vtpEntityEquipmentState, F7FileTimeStamp=F7FileTimeStamp, inventoryMib=inventoryMib, swDbDataDefaultsTable=swDbDataDefaultsTable, SonetTimingSourceCaps=SonetTimingSourceCaps, neTrapsinkType=neTrapsinkType, oduTcmAConfigSignalDegradePeriod=oduTcmAConfigSignalDegradePeriod, oduTcmCDataTraceReceivedDapi=oduTcmCDataTraceReceivedDapi, ptpEntityClass=ptpEntityClass, oduSectionConfigTimMode=oduSectionConfigTimMode, fwDataProtectionPart=fwDataProtectionPart, RestoreActivationCaps=RestoreActivationCaps, neEventLogTable=neEventLogTable, eqpFwUpgradeRequest=eqpFwUpgradeRequest, swDbDataActivationTime=swDbDataActivationTime, oduTcmAConfigTraceTransmitDapi=oduTcmAConfigTraceTransmitDapi, fwDataFirmwarePackageRev=fwDataFirmwarePackageRev, SonetSectSigDegThres=SonetSectSigDegThres, oduSectionConfigSignalDegradePeriod=oduSectionConfigSignalDegradePeriod, swDbDataStandbyPartitionStatus=swDbDataStandbyPartitionStatus, controlPlaneEthEntityIndexAid=controlPlaneEthEntityIndexAid, snmpProxyEntrySingleTargetOutPort=snmpProxyEntrySingleTargetOutPort, neStorageAvailable=neStorageAvailable, oduTcmCConfigTraceTransmitDapi=oduTcmCConfigTraceTransmitDapi, swDbDataNumSaNotReady=swDbDataNumSaNotReady, otuSectionConfigTraceTransmitSapi=otuSectionConfigTraceTransmitSapi, SonetTraceForm=SonetTraceForm, otuSectionConfigTraceTransmitDapi=otuSectionConfigTraceTransmitDapi, swDbDataNumLegacyEqpt=swDbDataNumLegacyEqpt, swDbDataCapTable=swDbDataCapTable, common=common, neBackupEncryption=neBackupEncryption, coldRestartCapServiceAffectingCap=coldRestartCapServiceAffectingCap, otuSectionDataResultingTotalBitrate=otuSectionDataResultingTotalBitrate, swDbFileGrade=swDbFileGrade, sonetSectionConfigTraceForm=sonetSectionConfigTraceForm, neInfo=neInfo, CpWdmEntityClass=CpWdmEntityClass, swVersionActiveOperatingSw=swVersionActiveOperatingSw, oduConfig=oduConfig, neDateAndTime=neDateAndTime, neEventLogVarOidVal=neEventLogVarOidVal, inventoryUnitName=inventoryUnitName, sonetSectionDataTable=sonetSectionDataTable, swDbFileArea=swDbFileArea, inventorySoftwareRev=inventorySoftwareRev, NoYesNA=NoYesNA, entityIndex=entityIndex, otuConfig=otuConfig, controlPlaneWdmContainsIndex=controlPlaneWdmContainsIndex, neAutoBackupServerLogin=neAutoBackupServerLogin, neSoftwareUpgrade=neSoftwareUpgrade, fwDataReadyForActivation=fwDataReadyForActivation, eqpFwEqpServerBusy=eqpFwEqpServerBusy, controlPlaneWdmEntityEntry=controlPlaneWdmEntityEntry, EthDuplexMode=EthDuplexMode, sonetSectionConfigSignalDegradePeriod=sonetSectionConfigSignalDegradePeriod, sonetSectionDataTraceReceived=sonetSectionDataTraceReceived, ServiceAffectingCaps=ServiceAffectingCaps, fwDataFirmwareAvailable=fwDataFirmwareAvailable, neEventLogVarUnsigned32Val=neEventLogVarUnsigned32Val, entityTable=entityTable, neAlarmStatus=neAlarmStatus, neF7AutomaticBackupNextDate=neF7AutomaticBackupNextDate, selectedFile=selectedFile, oduTcmBConfigTraceTransmitDapi=oduTcmBConfigTraceTransmitDapi, swDbDataNcuSoftwareVersion=swDbDataNcuSoftwareVersion, neSwDownloadProgress=neSwDownloadProgress, snmpProxyEntrySingleTargetOutRowStatus=snmpProxyEntrySingleTargetOutRowStatus, sourceIpAddress=sourceIpAddress, swDbDataCapEntry=swDbDataCapEntry, TrapAlarmSeverity=TrapAlarmSeverity, controlPlaneWdmEntityAssignmentState=controlPlaneWdmEntityAssignmentState, fsp3000=fsp3000, oduTcmCDataTraceReceivedSapi=oduTcmCDataTraceReceivedSapi, SonetTimingSource=SonetTimingSource, TimMode=TimMode, neF7AutomaticRemoteBackupProtocol=neF7AutomaticRemoteBackupProtocol, controlPlaneWdmEntityContainedIn=controlPlaneWdmEntityContainedIn, neF7AutomaticBackupRunState=neF7AutomaticBackupRunState, neTrapsinkTable=neTrapsinkTable, swDbFileEntry=swDbFileEntry, sonetSectionConfigEntry=sonetSectionConfigEntry, admin=admin, EquipmentState=EquipmentState, oduTcmBConfigTcmLevel=oduTcmBConfigTcmLevel, oduSectionDataTraceReceivedDapi=oduSectionDataTraceReceivedDapi, snmpProxyServerSynchroState=snmpProxyServerSynchroState, F7AutoBackupInterval=F7AutoBackupInterval, swVersionInactiveOperatingSw=swVersionInactiveOperatingSw, oduSectionDataTraceReceivedSapi=oduSectionDataTraceReceivedSapi, clearRdiskRequest=clearRdiskRequest, fwDataNewVersion=fwDataNewVersion, oduSectionConfigTraceTransmitDapi=oduSectionConfigTraceTransmitDapi, oduTcmADataTraceReceivedSapi=oduTcmADataTraceReceivedSapi, oduTcmAConfigTable=oduTcmAConfigTable, FspR7UsersDb=FspR7UsersDb, SonetVcBundleAllocationCaps=SonetVcBundleAllocationCaps, ptpEntityTable=ptpEntityTable, eqpFwNextEqpForUpdate=eqpFwNextEqpForUpdate, snmpWriteAccessEntry=snmpWriteAccessEntry, FspR7Time=FspR7Time, neTrapsinkUserName=neTrapsinkUserName, oduTcmBDataTraceReceivedOpsp=oduTcmBDataTraceReceivedOpsp, inventoryMacAddress=inventoryMacAddress)
