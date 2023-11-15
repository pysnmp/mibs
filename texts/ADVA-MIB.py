#
# PySNMP MIB module ADVA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/ADVA-MIB
# Produced by pysmi-1.1.10 at Wed Nov 15 02:34:12 2023
# On host fv-az661-425 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, Unsigned32, MibIdentifier, NotificationType, enterprises, Integer32, ObjectIdentity, Counter64, TimeTicks, iso, Bits, snmpModules, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, mib_2, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibIdentifier", "NotificationType", "enterprises", "Integer32", "ObjectIdentity", "Counter64", "TimeTicks", "iso", "Bits", "snmpModules", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "mib-2", "Counter32", "IpAddress")
TimeStamp, DateAndTime, RowStatus, MacAddress, TextualConvention, DisplayString, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DateAndTime", "RowStatus", "MacAddress", "TextualConvention", "DisplayString", "TestAndIncr")
advaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544))
advaMIB.setRevisions(('2018-12-14 00:00', '2017-12-07 00:00', '2017-03-23 00:00', '2016-04-01 00:00', '2015-12-10 00:00', '2015-09-03 00:00', '2015-03-20 00:00', '2014-09-29 00:00', '2012-02-07 00:00', '2008-02-21 00:00', '2004-12-14 00:00', '2004-02-20 00:00', '2003-12-12 00:00', '2003-10-07 00:00', '2003-06-27 00:00', '2002-07-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: advaMIB.setRevisionsDescriptions(('Revised ADVA Common MIB version 2.10.', 'Revised ADVA Common MIB version 2.9.', 'Revised ADVA Common MIB version 2.8.', 'Revised ADVA Common MIB version 2.7.', 'Revised ADVA Common MIB version 2.6.', 'Revised ADVA Common MIB version 2.5.', 'Revised ADVA Common MIB version 2.4.', 'Revised ADVA Common MIB version 2.3.', 'Revised ADVA Common MIB version 2.1.', 'Revised ADVA Common MIB version 2.0.', 'The ADVA Common MIB version 1.7.', 'The ADVA Common MIB version 1.6.', 'The ADVA Common MIB version 1.5.', 'The ADVA Common MIB version 1.4.', 'The ADVA Common MIB version 1.3', 'The ADVA MIB version 1.3.',))
if mibBuilder.loadTexts: advaMIB.setLastUpdated('201812140000Z')
if mibBuilder.loadTexts: advaMIB.setOrganization('ADVA AG Optical Networking')
if mibBuilder.loadTexts: advaMIB.setContactInfo('ADVA AG Optical Networking\n        Justus-von-Liebig-Str. 7\n        12489 Berlin, Germany\n\n        Support Europe:\n        Phone:  +49 89 89 0665 848\n        Fax:    +49 89 89 0665 22848\n        e-mail: support@advaoptical.com\n\n        Support USA:\n        Phone:  +1 201 995 0080\n        Fax:    +1 201 995 0081\n        e-mail: support-usa@advaoptical.com\n\n        Support Asia:\n        Phone:  +81 3 5408 5891\n        Fax:    +81 3 5408 5899\n        e-mail: support-asia@advaoptical.com')
if mibBuilder.loadTexts: advaMIB.setDescription('The ADVA Optical Networking base MIB.')
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
    description = 'Variable for representing a state and is for general use.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class AvailState(TextualConvention, Integer32):
    description = 'Variable for representing availability state and is for\n        general use.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("available", 1), ("notAvailable", 2))

class EnableState(TextualConvention, Integer32):
    description = 'Describes whether a feature is enabled or disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("stateNotApplicable", 0), ("stateEnabled", 1), ("stateDisabled", 2))

class ArcState(TextualConvention, Integer32):
    description = 'Variable for representing the Alarm Report Control (ARC)\n        state for an entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("alm", 1), ("nalm", 2))

class TrapAlarmSeverity(TextualConvention, Integer32):
    description = "This object identifies the severity of an alarm. The state\n        'cleared' is not a severity, but is used for reporting that\n        an alarm condition is no longer present. The state\n        'notReported' is used for current alarms which are not\n        reported because of ARC.\n        The state 'indeterminate' is used when the severity value\n        cannot be determined due to an internal error."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("indeterminate", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("cleared", 6), ("notReported", 7))

class ServiceImpairment(TextualConvention, Integer32):
    description = 'This object identifies the potential service impairment of\n        an alarm.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("serviceAffecting", 1), ("nonServiceAffecting", 2), ("serviceAffectingInstall", 3), ("serviceAffectingActivate", 4))

class TrapCounter(TextualConvention, Counter32):
    description = 'The sequence number of sent notifications (traps).'
    status = 'current'

class Counter64String(TextualConvention, OctetString):
    description = 'A string representation of a 64 bit counter.\n        This TC is provided solely for SNMPv1 compliance.'
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

class KBytes(TextualConvention, Gauge32):
    description = 'A memory size, expressed in units of 1024 bytes.'
    status = 'current'

class IdentityTranslation(TextualConvention, OctetString):
    description = 'Translation of an index (entPhysicalIndex, ifIndex etc.)\n        to a string.\n            Slot/Module/Port location (product specific notation)\n            Service/Bundle Name\n\n        If no index available a string with:\n            IP address (for neTrapsinkTable etc.)\n\n        If nothing appropriate available\n            zero length string\n\n        Further info in product documentation.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class NeSwUpgradeStatusType(TextualConvention, Integer32):
    description = 'The status of a NE software upgrade command. The states 2 - 7 and 15, 18-29  are only used\n         when the NE is used as FTP client. States from 30 to 36 are used for reporting the\n         installation failure in case of revised F7 upgrade procedure, 37-28 are introduce for F7\n         schedule backup.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39))
    namedValues = NamedValues(("none", 1), ("downloading", 2), ("downloadLoginFailed", 3), ("downloadFileNotFound", 4), ("downloadFileNoAccess", 5), ("downloadFailure", 6), ("downloadReadyForInstallation", 7), ("installingSoftware", 8), ("installationFailed", 9), ("softwareReadyForActivation", 10), ("activatingSoftware", 11), ("activationFailed", 12), ("softwareActivated", 13), ("rebooting", 14), ("downloadServerUnreachable", 15), ("noSpaceLeft", 16), ("internalError", 17), ("downloadFileProtocolFailed", 18), ("downloadFileCheckFailed", 19), ("downloadSSHHostkeyFailed", 20), ("uploading", 21), ("uploadLoginFailed", 22), ("uploadFileNotFound", 23), ("uploadFileNoAccess", 24), ("uploadFailure", 25), ("uploadServerUnreachable", 26), ("uploadFileProtocolFailed", 27), ("uploadFileCheckFailed", 28), ("uploadSSHHostkeyFailed", 29), ("installationFailedDeny", 30), ("installationFailedWrongCrc", 31), ("installationFailedVersionMismatch", 32), ("installationFailedStbyInWrongState", 33), ("installationFailedDamagedConfFile", 34), ("installationFailedFsckFailed", 35), ("installationFailedNotExist", 36), ("downloadFileFailedProtocolDisabled", 37), ("uploadFileFailedProtocolDisabled", 38), ("backupFailedGeneration", 39))

class NeSwInstallStatusType(TextualConvention, Integer32):
    description = 'Software installation status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("undefined", 0), ("idle", 1), ("downloadingCon", 2), ("installingCon", 3), ("downloadingNcu", 4), ("installingNcu", 5), ("downloadingFwp", 6), ("installingFwp", 7), ("downloadingPgm", 8), ("installingPgm", 9))

class FileTransferProtocol(TextualConvention, Integer32):
    description = 'The protocol used for a file transfer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5))
    namedValues = NamedValues(("ftp", 2), ("scp", 3), ("http", 4), ("sftp", 5))

class SourceIpAddress(TextualConvention, Integer32):
    description = 'IP address used as source IP address in FTP Client session'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("sysIp", 1), ("defaultIp", 2))

class F7FileTimeStamp(TextualConvention, Integer32):
    description = 'Add Timestamp to File Name'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("add", 1), ("omit", 2))

class F7AutoBackupInterval(TextualConvention, Integer32):
    description = 'Scheduled Database Backup Interval'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("every1Day", 2), ("every2Day", 3), ("every3Day", 4), ("every4Day", 5), ("every5Day", 6), ("every6Day", 7), ("every1Week", 8), ("every2Week", 9), ("every3Week", 10), ("every1Month", 11), ("every2Month", 12), ("every3Month", 13))

class F7AutoBackupRunState(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("no", 1), ("yes", 2))

class PartitionStatus(TextualConvention, Integer32):
    description = 'Partition State'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("empty", 1), ("configFileInstalled", 2), ("ncuFileInstalled", 3), ("softwareReadyForActivation", 4), ("fwpsInstalled", 5))

class FspDate(TextualConvention, OctetString):
    description = 'A date specification.\n         field octets contents range\n         ----- ------ -------- -----\n         1 1-2 year* 0..65536\n         2 3 month 1..12\n         3 4 day 1..31\n         * Notes: - the value of year is in network-byte order\n         For example, Tuesday May 26, 1992 would be\n         displayed as:\n         1992-5-26'
    status = 'current'
    displayHint = '2d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class FspTime(TextualConvention, OctetString):
    description = 'A time specification.\n         field octets contents range\n         ----- ------ -------- -----\n         1 1 hour 0..23\n         2 2 minutes 0..59\n         3 3 seconds 0..60\n         (use 60 for leap-second)\n         For example: 13-10-26'
    status = 'current'
    displayHint = '1d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class ApsDirection(TextualConvention, Integer32):
    description = 'Bi-Directional | Unidirectional setup used in protection setup: Not to be used by others'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("bidirectional", 1), ("unidirectional", 2))

class ApsDirectionCaps(TextualConvention, Bits):
    description = 'Bi-Directional | Unidirectional setup used in protection setup: Not to be used by others'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capBidirectional", 1), ("capUnidirectional", 2))

class ApsHoldoffTime(TextualConvention, Integer32):
    description = 'Soak period before switch after trigger.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("e20ms", 2), ("e100ms", 3), ("e200ms", 4), ("e300ms", 5), ("e400ms", 6), ("e500ms", 7), ("e600ms", 8), ("e700ms", 9), ("e800ms", 10), ("e900ms", 11), ("e1000ms", 12), ("e1100ms", 13), ("e1200ms", 14), ("e1300ms", 15), ("e1400ms", 16), ("e1500ms", 17), ("e1600ms", 18), ("e1700ms", 19), ("e1800ms", 20), ("e1900ms", 21), ("e2000ms", 22), ("e2100ms", 23), ("e2200ms", 24), ("e2300ms", 25), ("e2400ms", 26), ("e2500ms", 27), ("e2600ms", 28), ("e2700ms", 29), ("e2800ms", 30), ("e2900ms", 31), ("e3000ms", 32), ("e3100ms", 33), ("e3200ms", 34), ("e3300ms", 35), ("e3400ms", 36), ("e3500ms", 37), ("e3600ms", 38), ("e3700ms", 39), ("e3800ms", 40), ("e3900ms", 41), ("e4000ms", 42), ("e4100ms", 43), ("e4200ms", 44), ("e4300ms", 45), ("e4400ms", 46), ("e4500ms", 47), ("e4600ms", 48), ("e4700ms", 49), ("e4800ms", 50), ("e4900ms", 51), ("e5000ms", 52), ("e5100ms", 53), ("e5200ms", 54), ("e5300ms", 55), ("e5400ms", 56), ("e5500ms", 57), ("e5600ms", 58), ("e5700ms", 59), ("e5800ms", 60), ("e5900ms", 61), ("e6000ms", 62), ("e6100ms", 63), ("e6200ms", 64), ("e6300ms", 65), ("e6400ms", 66), ("e6500ms", 67), ("e6600ms", 68), ("e6700ms", 69), ("e6800ms", 70), ("e6900ms", 71), ("e7000ms", 72), ("e7100ms", 73), ("e7200ms", 74), ("e7300ms", 75), ("e7400ms", 76), ("e7500ms", 77), ("e7600ms", 78), ("e7700ms", 79), ("e7800ms", 80), ("e7900ms", 81), ("e8000ms", 82), ("e8100ms", 83), ("e8200ms", 84), ("e8300ms", 85), ("e8400ms", 86), ("e8500ms", 87), ("e8600ms", 88), ("e8700ms", 89), ("e8800ms", 90), ("e8900ms", 91), ("e9000ms", 92), ("e9100ms", 93), ("e9200ms", 94), ("e9300ms", 95), ("e9400ms", 96), ("e9500ms", 97), ("e9600ms", 98), ("e9700ms", 99), ("e9800ms", 100), ("e9900ms", 101), ("e10000ms", 102))

class ApsHoldoffTimeCaps(TextualConvention, Bits):
    description = 'Soak period before switch after trigger.'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNone", 1), ("capE20ms", 2), ("capE100ms", 3), ("capE200ms", 4), ("capE300ms", 5), ("capE400ms", 6), ("capE500ms", 7), ("capE600ms", 8), ("capE700ms", 9), ("capE800ms", 10), ("capE900ms", 11), ("capE1000ms", 12), ("capE1100ms", 13), ("capE1200ms", 14), ("capE1300ms", 15), ("capE1400ms", 16), ("capE1500ms", 17), ("capE1600ms", 18), ("capE1700ms", 19), ("capE1800ms", 20), ("capE1900ms", 21), ("capE2000ms", 22), ("capE2100ms", 23), ("capE2200ms", 24), ("capE2300ms", 25), ("capE2400ms", 26), ("capE2500ms", 27), ("capE2600ms", 28), ("capE2700ms", 29), ("capE2800ms", 30), ("capE2900ms", 31), ("capE3000ms", 32), ("capE3100ms", 33), ("capE3200ms", 34), ("capE3300ms", 35), ("capE3400ms", 36), ("capE3500ms", 37), ("capE3600ms", 38), ("capE3700ms", 39), ("capE3800ms", 40), ("capE3900ms", 41), ("capE4000ms", 42), ("capE4100ms", 43), ("capE4200ms", 44), ("capE4300ms", 45), ("capE4400ms", 46), ("capE4500ms", 47), ("capE4600ms", 48), ("capE4700ms", 49), ("capE4800ms", 50), ("capE4900ms", 51), ("capE5000ms", 52), ("capE5100ms", 53), ("capE5200ms", 54), ("capE5300ms", 55), ("capE5400ms", 56), ("capE5500ms", 57), ("capE5600ms", 58), ("capE5700ms", 59), ("capE5800ms", 60), ("capE5900ms", 61), ("capE6000ms", 62), ("capE6100ms", 63), ("capE6200ms", 64), ("capE6300ms", 65), ("capE6400ms", 66), ("capE6500ms", 67), ("capE6600ms", 68), ("capE6700ms", 69), ("capE6800ms", 70), ("capE6900ms", 71), ("capE7000ms", 72), ("capE7100ms", 73), ("capE7200ms", 74), ("capE7300ms", 75), ("capE7400ms", 76), ("capE7500ms", 77), ("capE7600ms", 78), ("capE7700ms", 79), ("capE7800ms", 80), ("capE7900ms", 81), ("capE8000ms", 82), ("capE8100ms", 83), ("capE8200ms", 84), ("capE8300ms", 85), ("capE8400ms", 86), ("capE8500ms", 87), ("capE8600ms", 88), ("capE8700ms", 89), ("capE8800ms", 90), ("capE8900ms", 91), ("capE9000ms", 92), ("capE9100ms", 93), ("capE9200ms", 94), ("capE9300ms", 95), ("capE9400ms", 96), ("capE9500ms", 97), ("capE9600ms", 98), ("capE9700ms", 99), ("capE9800ms", 100), ("capE9900ms", 101), ("capE10000ms", 102))

class AssignmentState(TextualConvention, Integer32):
    description = "Assignment State. Describes an entity' state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("assigned", 1), ("unassigned", 2), ("notassignable", 3))

class BootState(TextualConvention, Integer32):
    description = 'Boot State. Every state change (excluding IDLE) does generate a corresponding transient condition.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("undefined", 0), ("complete", 1), ("started", 2), ("failed", 3), ("reject", 4), ("install", 5), ("installFail", 6), ("installComplete", 7), ("activate", 8), ("activateFail", 9), ("activateReject", 10), ("activateComplete", 11))

class CommandEqpt(TextualConvention, Integer32):
    description = 'Update, Install and Reboot commands.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("install", 2), ("reboot", 3), ("activate", 4), ("update", 5), ("installFromStby", 6), ("forceInstall", 7))

class CpWdmEntityClass(TextualConvention, Integer32):
    description = 'Control Plane WDM Entity Class'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("undefined", 0), ("cp", 1), ("tunnel", 2), ("connection", 3), ("path", 4), ("pathElement", 5), ("logicalInterface", 6), ("remoteAlarm", 7), ("portBinding", 8), ("reservation", 9), ("diversity", 10))

class EnableStateCaps(TextualConvention, Bits):
    description = 'Usage of 3rd Party Plugs'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capStateEnabled", 1), ("capStateDisabled", 2))

class EntityClass(TextualConvention, Integer32):
    description = 'Entity Class'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88))
    namedValues = NamedValues(("undefined", 0), ("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("plug", 10), ("stack", 11), ("group", 12), ("clientPort", 13), ("networkPort", 14), ("virtualChannel", 15), ("connection", 16), ("vc4Container", 17), ("vc3sts1Container", 18), ("vc12vt15Container", 19), ("dcnChannel", 20), ("routerConfig", 21), ("environmentPort", 22), ("internalPort", 23), ("upgradePort", 24), ("midstagePort", 25), ("serialPort", 26), ("pppIpInterface", 27), ("lanIp", 28), ("vs1Container", 29), ("sts3cContainer", 30), ("payloadChannel", 31), ("passiveShelf", 32), ("sts24cContainer", 33), ("sts48cContainer", 34), ("vs2cContainer", 35), ("vs4cContainer", 36), ("tifInputPort", 37), ("tifOutputPort", 38), ("opticalLink", 39), ("virtualOpticalChannel", 40), ("logicalInterface", 41), ("physicalTerminationPoint", 42), ("ethClient", 43), ("ethNetwork", 44), ("veth", 45), ("flow", 47), ("ctrans", 48), ("policerOnFlow", 50), ("queueOnPort", 51), ("queueOnFlow", 52), ("farEndPlug", 53), ("farEndChannel", 54), ("vc4c8Container", 55), ("vc4c16Container", 56), ("vs0Container", 57), ("virtualSubChannel", 58), ("bridge", 59), ("queueOnBridge", 60), ("backwardVirtualOptMux", 61), ("forwardVirtualOptMux", 62), ("optChannelTransportLane", 63), ("virtualChannelN", 64), ("externalChannel", 65), ("virtualTerminationPoint", 66), ("virtualConnection", 67), ("virtualOptMux", 68), ("optTransportLaneGroup", 69), ("optWaveLengthGroup", 70), ("crossConnectionChannel", 71), ("crossOpticalLineChannel", 72), ("versatilePort", 73), ("system", 74), ("crossConnectionDcn", 75), ("protectionFfp", 76), ("protectionCable", 77), ("unidirectionalChannel", 78), ("filterCable", 79), ("groupTerminationPoint", 80), ("externalOm", 81), ("externalVch", 82), ("virtualModule", 83), ("virtualMap", 84), ("lldp", 85), ("managementPort", 86), ("licenseManager", 87), ("license", 88))

class EntityIndex(TextualConvention, Integer32):
    description = 'The index of an entity. EntityIndex is used to index the following:\n        Entities which are provisioned but unequipped (existing in the database but\n        not physically present),\n        Entities which are equipped but non-provisioned (physically present but not in\n        the database),\n        Entities which are both provisioned and equipped (existing in the database and\n        physically present),\n        Entities which are non-provisioned and unequipped (not existing in the database\n        and not physically present).\n        These will have an entry in the entityTable, but their EntityType will\n        be undefined.\n        The EntityIndex is used similarly to how the entPhysicalIndex in\n        RFC2737 (Entity MIB) is used to address entities and containers of entities.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class EntityType(TextualConvention, Integer32):
    description = 'Identifies the entity type. Each NE may have their own use of\n        this INTEGER value, which will defined in the conformance document\n        for each individual NE MIB.'
    status = 'current'

class EquipmentState(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("equipped", 1), ("unequipped", 2))

class EthDuplexMode(TextualConvention, Integer32):
    description = 'Duplex Mode (provision), available when Auto Negoiation is Disable (AUTONEG=DISABLE)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("ethHalfDuplex", 1), ("ethFullDuplex", 2))

class EthDuplexModeCaps(TextualConvention, Bits):
    description = 'Duplex Mode (provision), available when Auto Negoiation is Disable (AUTONEG=DISABLE)'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capEthHalfDuplex", 1), ("capEthFullDuplex", 2))

class FileArea(TextualConvention, Integer32):
    description = 'Type of Area'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("undefined", 0), ("activeArea", 1), ("standbyArea", 2), ("rDisk", 3), ("backupDisk", 4), ("alpDisk", 5), ("pDisk", 6), ("cfDisk", 7), ("paDisk", 8))

class FileType(TextualConvention, Integer32):
    description = 'Type of File'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("undefined", 0), ("pgm", 1), ("dbs", 2), ("unknown", 3), ("alp", 4), ("ncu", 5), ("fwps", 6), ("con", 7), ("prf", 8), ("paf", 9), ("dbx", 10), ("alm", 11), ("pak", 12), ("map", 13))

class FspR7AdminStateSnmpProxy(TextualConvention, Integer32):
    description = 'Administrative State is displayed in the GUI and Craft. Transition to Unassigend requires the entity to be deleted.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 6))
    namedValues = NamedValues(("undefined", 0), ("is", 2), ("dsbld", 6))

class FspR7AdminStateSnmpProxyCaps(TextualConvention, Bits):
    description = 'Administrative State is displayed in the GUI and Craft. Transition to Unassigend requires the entity to be deleted.'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capIs", 2), ("capDsbld", 6))

class FspR7Date(TextualConvention, OctetString):
    description = 'A date specification.\n        field  octets  contents                  range\n        -----  ------  --------                  -----\n        1      1-2   year*                     0..65536\n        2       3    month                     1..12\n        3       4    day                       1..31\n        * Notes:             - the value of year is in network-byte order\n        For example, Tuesday May 26, 1992 would be\n        displayed as:\n        1992-5-26'
    status = 'current'
    displayHint = '2d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class FspR7EnableDisable(TextualConvention, Integer32):
    description = 'Enable/Disable variable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("enable", 1), ("disable", 2))

class FspR7EquipmentType(TextualConvention, Integer32):
    description = "The TYPE of Equipment and the MODE setting determine uniquely\n        the number and allowed TYPE's of the provisionable dependent\n        entities (plugs, interfaces, modules)"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 137, 138, 140, 141, 142, 143, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 180, 182, 183, 185, 186, 187, 188, 190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 234, 235, 236, 237, 239, 240, 241, 242, 243, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 264, 267, 268, 269, 270, 272, 273, 274, 280, 282, 283, 284, 285, 286, 289, 290, 291, 292, 293, 294, 295, 297, 298, 300, 303, 304, 305, 307, 308, 309, 311, 312, 314), SingleValueConstraint(317, 318, 319, 320, 321, 323, 324, 450, 453, 454, 455, 456, 457, 458, 459, 461, 462, 463, 464, 465, 466, 467, 468, 472, 473, 474, 475, 476, 478, 479, 480, 481, 482, 483, 485, 486, 487, 488, 489, 490, 491, 499))
    namedValues = NamedValues(("undefined", 0), ("eqpSh1hu", 1), ("eqpSh1huDc", 2), ("eqpSh3hu", 3), ("eqpSh7hu", 4), ("eqpF2kSh5hu", 5), ("eqpF2kSh6hu", 6), ("eqpDcm", 7), ("eqpSh9hu", 8), ("eqpUnknown", 19), ("eqpNcu", 20), ("eqpNcutif", 21), ("eqpScu", 22), ("eqpScue", 23), ("eqpR6cu", 24), ("eqpPsu1huac", 25), ("eqpPsu7huac", 26), ("eqpPsu7hudc", 27), ("eqpFcu7hu", 28), ("eqp2clsmd", 29), ("eqp2absmc", 30), ("eqp2bsmd", 31), ("eqp1Gsmud", 32), ("eqp4gsmd", 33), ("eqp8gsmd", 34), ("eqp1csmuc", 35), ("eqp1csmuewc", 36), ("eqp4csmd", 37), ("eqp4csmud", 38), ("eqp4csmc", 39), ("eqpOsfm", 40), ("eqp1pm", 41), ("eqp2pm", 42), ("eqp40csmd", 43), ("eqpDcf", 44), ("eqpEdfas", 45), ("eqpEdfasgc", 46), ("eqpEdfadgc", 47), ("eqpRaman", 48), ("eqp4tcc2g5", 49), ("eqp4tcc2g5d", 50), ("eqp4tcc10gd", 51), ("eqp4tcc10gc", 52), ("eqpWcc10gd", 53), ("eqpWcc10gc", 54), ("eqpWcc2g71N", 55), ("eqpWcc2g7d", 56), ("eqp2tcm2g5", 57), ("eqp2tca2g5", 58), ("eqp8tca10gd", 59), ("eqp8tca10gc", 60), ("eqpWca10gd", 61), ("eqpWca10gc", 62), ("eqp4tca4gd", 63), ("eqp4tca4gc", 64), ("eqpwca2g5", 65), ("eqp4tca1g3d", 66), ("eqp4tca1g3c", 67), ("eqp8tce2g5d", 68), ("eqp8tce2g5c", 69), ("eqpWcelsd", 70), ("eqpWcelsc", 71), ("eqpVsm", 72), ("eqpRsmolm", 73), ("eqpRsmsf", 74), ("eqpOscm", 75), ("eqp2oscm", 76), ("eqpDrm", 77), ("eqpXfpG", 78), ("eqpsfpd", 79), ("eqpSfpc", 80), ("eqpSfpg", 81), ("eqpSfpe", 82), ("eqpSh1hudcm", 83), ("eqpCustomc", 84), ("eqpCustomd", 85), ("eqpPsu1hudc", 86), ("eqpWcc2g7c", 87), ("eqp1csmuEwD", 88), ("eqp1csmuG", 89), ("eqp3BsmC", 90), ("eqp2Tca2g5s", 91), ("eqp8Csmuc", 92), ("eqpEdfaDgcb", 93), ("eqpOscmPn", 94), ("eqp4Tcc10gtd", 95), ("eqp4Tca4g", 96), ("eqpDcg", 97), ("eqp2Tcm2g5d", 98), ("eqp2Tcm2g5c", 99), ("eqpWcm2g5d", 100), ("eqpWcm2g5c", 101), ("eqpEdfmSgc", 102), ("eqpF2kDemiV2", 103), ("eqpPsm", 104), ("eqpNcu2e", 105), ("eqp8TceGl2g5d", 106), ("eqp8TceGl2g5c", 107), ("eqpDcf1hu", 108), ("eqp10tcc10gtd", 109), ("eqp10tcc10gd", 110), ("eqp10tcc10gc", 111), ("eqp16csmSfd", 112), ("eqpOsfmSf", 113), ("eqp2clsmSfd", 114), ("eqp3bsmEwc", 115), ("eqpEdfaSgcb", 116), ("eqpEdfaDgcv", 117), ("eqpWcc10gtd", 118), ("eqp2csmuEwc", 119), ("eqpEroadmDc", 120), ("eqpScuS", 122), ("eqp4opcm", 123), ("eqpUtm", 124), ("eqpPscu", 125), ("eqp40Csm2hu", 126), ("eqp2Twcc2g7", 127), ("eqp2Wca10g", 130), ("eqpNcuHp", 131), ("eqpNcu20085hu", 132), ("eqp20Pca10G", 133), ("eqpXfpC", 137), ("eqpXfpD", 138), ("eqpWcc40gtd", 140), ("eqpIlm", 141), ("eqpNcuII", 142), ("eqpCem9hu", 143), ("eqp8roadmC40", 148), ("eqp4Tcc40gtd", 149), ("eqp2pca10g", 150), ("eqp10pca10g", 151), ("eqp1csmuD", 152), ("eqpSfpOsC", 153), ("eqpSfpOdC", 154), ("eqpSfpOsG", 155), ("eqpSfpOdG", 156), ("eqpRoadmC80", 157), ("eqpccm8", 158), ("eqpPsu9hudc", 159), ("eqp4tca4gus", 160), ("eqp40Csm3huD", 161), ("eqp5psm", 162), ("eqpFan9hu", 163), ("eqp5tce10gtd", 164), ("eqp10tccs10gtd", 165), ("eqp40Csm3hudcD", 166), ("eqp40Csm3hudcDi", 167), ("eqp5gsmD", 169), ("eqp8csmD", 170), ("eqp2otfm", 171), ("eqp8otdr3hu", 172), ("eqpXfptD", 173), ("eqp40Csm3huDi", 174), ("eqp8CcmC80", 175), ("eqpEdfaD27", 176), ("eqp2Wcc10g", 177), ("eqp8RoadmC80", 178), ("eqp2Wcc10gAes", 180), ("eqp5tce10gtaesd", 182), ("eqpSh1hupf", 183), ("eqpFan1hu", 185), ("eqp10tcc10g", 186), ("eqpXfpOtnD", 187), ("eqpNcu2p", 188), ("eqpPsu9huac", 190), ("eqp2Raman", 192), ("eqpEdfaS26", 193), ("eqp5tces10gtd", 194), ("eqpScuII", 195), ("eqp11RoadmC96", 196), ("eqp8AdmC96", 197), ("eqp8CxmC96", 198), ("eqp8Shm", 199), ("eqpAmpShgcv", 200), ("eqpAmpSlgcv", 201), ("eqp2RamanC15", 202), ("eqpWcc100gtD", 203), ("eqpCfp4g", 204), ("eqpCfp10g", 205), ("eqpXfpTlnD", 213), ("eqp5tces10gtaesd", 214), ("eqp10tce100g", 215), ("eqp96Csm4HuD", 216), ("eqp4CfptD", 217), ("eqp2psm", 218), ("eqpWce100G", 219), ("eqp10Wxc10g", 220), ("eqpShx9hu", 221), ("eqpFanXhu", 222), ("eqp10tcc100gtbD", 223), ("eqp9RoadmC96", 224), ("eqp4Wce16g", 225), ("eqpSfpBG", 226), ("eqpSfpCdrG", 227), ("eqp10tce100gGf", 228), ("eqpSfpCdrC", 229), ("eqp5tce10gaes", 234), ("eqp5tce10g", 235), ("eqp5tces10gaes", 236), ("eqp5tces10g", 237), ("eqp4roadmC96", 239), ("eqpWcc100gtbD", 240), ("eqpEdfaS20", 241), ("eqp10tccSdi10g", 242), ("eqp4roadmEC96", 243), ("eqpSfptD", 245), ("eqpSfp2TxG", 246), ("eqpSfp2RxG", 247), ("eqpSfp2Txe", 248), ("eqpSfp2Rxe", 249), ("eqp2EdfaS20S10", 250), ("eqp10Tce100Gb", 251), ("eqp10Tce100gAes", 252), ("eqpSfpCdrD", 253), ("eqpSh1huDcEtemp", 254), ("eqp8psm", 255), ("eqp9ccmC96", 256), ("eqpWce100GB", 257), ("eqp16tcc10G", 258), ("eqp4Wcc10g", 259), ("eqp5wca16G", 260), ("eqpCfptCd", 261), ("eqpWccPcn100g", 264), ("eqpOppm", 267), ("eqp4cfpd", 268), ("eqpNcuS", 269), ("eqp10csmuD", 270), ("eqpUtmS", 272), ("eqpSfpBC", 273), ("eqp10Tce100gAesBsi", 274), ("eqpWccPcn100gAes", 280), ("eqpSfpRxTxG", 282), ("eqpSfpTlnD", 283), ("eqpCfpTfCd", 284), ("eqpXfpBG", 285), ("eqpFd128D", 286), ("eqpSfpBCdrG", 289), ("eqpMroadmC96", 290), ("eqpPsm40Mroadm", 291), ("eqpOsfma", 292), ("eqp10tcc100g", 293), ("eqpCfpTgCd", 294), ("eqpPsm80Mroadm", 295), ("eqp10Tce100gbAes", 297), ("eqpL3CmSina", 298), ("eqp9Tce10gAesG", 300), ("eqp9RoadmRs", 303), ("eqp16psm4", 304), ("eqp96Csm2HuD", 305), ("eqp9Tce10gAesF", 307), ("eqp10Tce100gAesF", 308), ("eqpMtpOscC", 309), ("eqpWcc100gAesF", 311), ("eqpCfpTrCd", 312), ("eqpWcc100gAesB", 314)) + NamedValues(("eqpMapOscC", 317), ("eqpMtpbOscC", 318), ("eqpMapbOscC", 319), ("eqpWccPcn100gB", 320), ("eqp4psmS", 321), ("eqpWcc100gAesG", 323), ("eqpHdScm", 324), ("eqpCfp2tgCd", 450), ("eqpMaB2C3LtA", 453), ("eqpMaB5Lt", 454), ("eqpCfp2tCd", 455), ("eqpMp2B4CtS", 456), ("eqpPsmdc3", 457), ("eqpQSfpNotApproved", 458), ("eqpQSfp10g", 459), ("eqpMa2C2C3LtA", 461), ("eqpQSfpDacCr", 462), ("eqpCem3", 463), ("eqpFtm3", 464), ("eqpPsmac3", 465), ("eqpSh1R", 466), ("eqpEcm3", 467), ("eqp4QsfpG", 468), ("eqpScm2", 472), ("eqpMa2C5Lt", 473), ("eqpPsmac6", 474), ("eqpQSfpDac", 475), ("eqpQSfpAoc", 476), ("eqpPsmdc4", 478), ("eqpPsmac5", 479), ("eqpFtm4", 480), ("eqpFtm2", 481), ("eqpPsmac4", 482), ("eqpPsmdc", 483), ("eqpCem2", 485), ("eqpCem4", 486), ("eqpEcm2", 487), ("eqpQSfp4g", 488), ("eqpMp2B4Ct", 489), ("eqpSh12", 490), ("eqpSh4R", 491), ("eqpPtp", 499))

class FspR7EquipmentTypeCaps(TextualConvention, Bits):
    description = "The TYPE of Equipment and the MODE setting determine uniquely\n        the number and allowed TYPE's of the provisionable dependent\n        entities (plugs, interfaces, modules)"
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capEqpSh1hu", 1), ("capEqpSh1huDc", 2), ("capEqpSh3hu", 3), ("capEqpSh7hu", 4), ("capEqpF2kSh5hu", 5), ("capEqpF2kSh6hu", 6), ("capEqpDcm", 7), ("capEqpSh9hu", 8), ("capEqpUnknown", 19), ("capEqpNcu", 20), ("capEqpNcutif", 21), ("capEqpScu", 22), ("capEqpScue", 23), ("capEqpR6cu", 24), ("capEqpPsu1huac", 25), ("capEqpPsu7huac", 26), ("capEqpPsu7hudc", 27), ("capEqpFcu7hu", 28), ("capEqp2clsmd", 29), ("capEqp2absmc", 30), ("capEqp2bsmd", 31), ("capEqp1Gsmud", 32), ("capEqp4gsmd", 33), ("capEqp8gsmd", 34), ("capEqp1csmuc", 35), ("capEqp1csmuewc", 36), ("capEqp4csmd", 37), ("capEqp4csmud", 38), ("capEqp4csmc", 39), ("capEqpOsfm", 40), ("capEqp1pm", 41), ("capEqp2pm", 42), ("capEqp40csmd", 43), ("capEqpDcf", 44), ("capEqpEdfas", 45), ("capEqpEdfasgc", 46), ("capEqpEdfadgc", 47), ("capEqpRaman", 48), ("capEqp4tcc2g5", 49), ("capEqp4tcc2g5d", 50), ("capEqp4tcc10gd", 51), ("capEqp4tcc10gc", 52), ("capEqpWcc10gd", 53), ("capEqpWcc10gc", 54), ("capEqpWcc2g71N", 55), ("capEqpWcc2g7d", 56), ("capEqp2tcm2g5", 57), ("capEqp2tca2g5", 58), ("capEqp8tca10gd", 59), ("capEqp8tca10gc", 60), ("capEqpWca10gd", 61), ("capEqpWca10gc", 62), ("capEqp4tca4gd", 63), ("capEqp4tca4gc", 64), ("capEqpwca2g5", 65), ("capEqp4tca1g3d", 66), ("capEqp4tca1g3c", 67), ("capEqp8tce2g5d", 68), ("capEqp8tce2g5c", 69), ("capEqpWcelsd", 70), ("capEqpWcelsc", 71), ("capEqpVsm", 72), ("capEqpRsmolm", 73), ("capEqpRsmsf", 74), ("capEqpOscm", 75), ("capEqp2oscm", 76), ("capEqpDrm", 77), ("capEqpXfpG", 78), ("capEqpsfpd", 79), ("capEqpSfpc", 80), ("capEqpSfpg", 81), ("capEqpSfpe", 82), ("capEqpSh1hudcm", 83), ("capEqpCustomc", 84), ("capEqpCustomd", 85), ("capEqpPsu1hudc", 86), ("capEqpWcc2g7c", 87), ("capEqp1csmuEwD", 88), ("capEqp1csmuG", 89), ("capEqp3BsmC", 90), ("capEqp2Tca2g5s", 91), ("capEqp8Csmuc", 92), ("capEqpEdfaDgcb", 93), ("capEqpOscmPn", 94), ("capEqp4Tcc10gtd", 95), ("capEqp4Tca4g", 96), ("capEqpDcg", 97), ("capEqp2Tcm2g5d", 98), ("capEqp2Tcm2g5c", 99), ("capEqpWcm2g5d", 100), ("capEqpWcm2g5c", 101), ("capEqpEdfmSgc", 102), ("capEqpF2kDemiV2", 103), ("capEqpPsm", 104), ("capEqpNcu2e", 105), ("capEqp8TceGl2g5d", 106), ("capEqp8TceGl2g5c", 107), ("capEqpDcf1hu", 108), ("capEqp10tcc10gtd", 109), ("capEqp10tcc10gd", 110), ("capEqp10tcc10gc", 111), ("capEqp16csmSfd", 112), ("capEqpOsfmSf", 113), ("capEqp2clsmSfd", 114), ("capEqp3bsmEwc", 115), ("capEqpEdfaSgcb", 116), ("capEqpEdfaDgcv", 117), ("capEqpWcc10gtd", 118), ("capEqp2csmuEwc", 119), ("capEqpEroadmDc", 120), ("capEqpScuS", 122), ("capEqp4opcm", 123), ("capEqpUtm", 124), ("capEqpPscu", 125), ("capEqp40Csm2hu", 126), ("capEqp2Twcc2g7", 127), ("capEqp2Wca10g", 130), ("capEqpNcuHp", 131), ("capEqpNcu20085hu", 132), ("capEqp20Pca10G", 133), ("capEqpXfpC", 137), ("capEqpXfpD", 138), ("capEqpWcc40gtd", 140), ("capEqpIlm", 141), ("capEqpNcuII", 142), ("capEqpCem9hu", 143), ("capEqp8roadmC40", 148), ("capEqp4Tcc40gtd", 149), ("capEqp2pca10g", 150), ("capEqp10pca10g", 151), ("capEqp1csmuD", 152), ("capEqpSfpOsC", 153), ("capEqpSfpOdC", 154), ("capEqpSfpOsG", 155), ("capEqpSfpOdG", 156), ("capEqpRoadmC80", 157), ("capEqpccm8", 158), ("capEqpPsu9hudc", 159), ("capEqp4tca4gus", 160), ("capEqp40Csm3huD", 161), ("capEqp5psm", 162), ("capEqpFan9hu", 163), ("capEqp5tce10gtd", 164), ("capEqp10tccs10gtd", 165), ("capEqp40Csm3hudcD", 166), ("capEqp40Csm3hudcDi", 167), ("capEqp5gsmD", 169), ("capEqp8csmD", 170), ("capEqp2otfm", 171), ("capEqp8otdr3hu", 172), ("capEqpXfptD", 173), ("capEqp40Csm3huDi", 174), ("capEqp8CcmC80", 175), ("capEqpEdfaD27", 176), ("capEqp2Wcc10g", 177), ("capEqp8RoadmC80", 178), ("capEqp2Wcc10gAes", 180), ("capEqp5tce10gtaesd", 182), ("capEqpSh1hupf", 183), ("capEqpFan1hu", 185), ("capEqp10tcc10g", 186), ("capEqpXfpOtnD", 187), ("capEqpNcu2p", 188), ("capEqpPsu9huac", 190), ("capEqp2Raman", 192), ("capEqpEdfaS26", 193), ("capEqp5tces10gtd", 194), ("capEqpScuII", 195), ("capEqp11RoadmC96", 196), ("capEqp8AdmC96", 197), ("capEqp8CxmC96", 198), ("capEqp8Shm", 199), ("capEqpAmpShgcv", 200), ("capEqpAmpSlgcv", 201), ("capEqp2RamanC15", 202), ("capEqpWcc100gtD", 203), ("capEqpCfp4g", 204), ("capEqpCfp10g", 205), ("capEqpXfpTlnD", 213), ("capEqp5tces10gtaesd", 214), ("capEqp10tce100g", 215), ("capEqp96Csm4HuD", 216), ("capEqp4CfptD", 217), ("capEqp2psm", 218), ("capEqpWce100G", 219), ("capEqp10Wxc10g", 220), ("capEqpShx9hu", 221), ("capEqpFanXhu", 222), ("capEqp10tcc100gtbD", 223), ("capEqp9RoadmC96", 224), ("capEqp4Wce16g", 225), ("capEqpSfpBG", 226), ("capEqpSfpCdrG", 227), ("capEqp10tce100gGf", 228), ("capEqpSfpCdrC", 229), ("capEqp5tce10gaes", 234), ("capEqp5tce10g", 235), ("capEqp5tces10gaes", 236), ("capEqp5tces10g", 237), ("capEqp4roadmC96", 239), ("capEqpWcc100gtbD", 240), ("capEqpEdfaS20", 241), ("capEqp10tccSdi10g", 242), ("capEqp4roadmEC96", 243), ("capEqpSfptD", 245), ("capEqpSfp2TxG", 246), ("capEqpSfp2RxG", 247), ("capEqpSfp2Txe", 248), ("capEqpSfp2Rxe", 249), ("capEqp2EdfaS20S10", 250), ("capEqp10Tce100Gb", 251), ("capEqp10Tce100gAes", 252), ("capEqpSfpCdrD", 253), ("capEqpSh1huDcEtemp", 254), ("capEqp8psm", 255), ("capEqp9ccmC96", 256), ("capEqpWce100GB", 257), ("capEqp16tcc10G", 258), ("capEqp4Wcc10g", 259), ("capEqp5wca16G", 260), ("capEqpCfptCd", 261), ("capEqpWccPcn100g", 264), ("capEqpOppm", 267), ("capEqp4cfpd", 268), ("capEqpNcuS", 269), ("capEqp10csmuD", 270), ("capEqpUtmS", 272), ("capEqpSfpBC", 273), ("capEqp10Tce100gAesBsi", 274), ("capEqpWccPcn100gAes", 280), ("capEqpSfpRxTxG", 282), ("capEqpSfpTlnD", 283), ("capEqpCfpTfCd", 284), ("capEqpXfpBG", 285), ("capEqpFd128D", 286), ("capEqpSfpBCdrG", 289), ("capEqpMroadmC96", 290), ("capEqpPsm40Mroadm", 291), ("capEqpOsfma", 292), ("capEqp10tcc100g", 293), ("capEqpCfpTgCd", 294), ("capEqpPsm80Mroadm", 295), ("capEqp10Tce100gbAes", 297), ("capEqpL3CmSina", 298), ("capEqp9Tce10gAesG", 300), ("capEqp9RoadmRs", 303), ("capEqp16psm4", 304), ("capEqp96Csm2HuD", 305), ("capEqp9Tce10gAesF", 307), ("capEqp10Tce100gAesF", 308), ("capEqpMtpOscC", 309), ("capEqpWcc100gAesF", 311), ("capEqpCfpTrCd", 312), ("capEqpWcc100gAesB", 314)) + NamedValues(("capEqpMapOscC", 317), ("capEqpMtpbOscC", 318), ("capEqpMapbOscC", 319), ("capEqpWccPcn100gB", 320), ("capEqp4psmS", 321), ("capEqpWcc100gAesG", 323), ("capEqpHdScm", 324), ("capEqpCfp2tgCd", 450), ("capEqpMaB2C3LtA", 453), ("capEqpMaB5Lt", 454), ("capEqpCfp2tCd", 455), ("capEqpMp2B4CtS", 456), ("capEqpPsmdc3", 457), ("capEqpQSfpNotApproved", 458), ("capEqpQSfp10g", 459), ("capEqpMa2C2C3LtA", 461), ("capEqpQSfpDacCr", 462), ("capEqpCem3", 463), ("capEqpFtm3", 464), ("capEqpPsmac3", 465), ("capEqpSh1R", 466), ("capEqpEcm3", 467), ("capEqp4QsfpG", 468), ("capEqpScm2", 472), ("capEqpMa2C5Lt", 473), ("capEqpPsmac6", 474), ("capEqpQSfpDac", 475), ("capEqpQSfpAoc", 476), ("capEqpPsmdc4", 478), ("capEqpPsmac5", 479), ("capEqpFtm4", 480), ("capEqpFtm2", 481), ("capEqpPsmac4", 482), ("capEqpPsmdc", 483), ("capEqpCem2", 485), ("capEqpCem4", 486), ("capEqpEcm2", 487), ("capEqpQSfp4g", 488), ("capEqpMp2B4Ct", 489), ("capEqpSh12", 490), ("capEqpSh4R", 491), ("capEqpPtp", 499))

class FspR7FalseTrue(TextualConvention, Integer32):
    description = 'False True variable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("false", 1), ("true", 2))

class FspR7Time(TextualConvention, OctetString):
    description = 'A time specification.\n        field  octets  contents  range\n        -----  ------  --------  -----\n        1      1       hour    0..23\n        2      2     minutes   0..59\n        3      3     seconds   0..60\n        (use 60 for leap-second)\n        For example: 13-10-26'
    status = 'current'
    displayHint = '1d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class FspR7YesNo(TextualConvention, Integer32):
    description = 'YesNo variable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2))

class FspR7UsersDb(TextualConvention, Integer32):
    description = 'Specifies how user accounts are handled for database operations'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2), ("keepCurrent", 3))

class Grade(TextualConvention, Integer32):
    description = 'Used to distinguish between NCU capabilities (range of supported services or applications)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("gradeA", 1), ("gradeB", 2), ("gradeGdps", 3), ("gradeC", 4))

class LoopConfig(TextualConvention, Integer32):
    description = 'External or Facility Loopback'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("noLoop", 1), ("lineLoop", 2), ("inwardLoop", 3))

class LoopConfigCaps(TextualConvention, Bits):
    description = 'External or Facility Loopback'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNoLoop", 1), ("capLineLoop", 2), ("capInwardLoop", 3))

class DestinationNodeOrAgentState(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("undefined", 0), ("inactive", 1))

class NcuAutoActivation(TextualConvention, Integer32):
    description = 'Enable scheduled activation of the standby PGM partition.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("no", 1), ("yes", 2))

class NoYesNA(TextualConvention, Integer32):
    description = 'Enumerator values no(1), yes(2), notApplicable(3).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("no", 1), ("yes", 2), ("notApplicable", 3))

class OhTerminationLevel(TextualConvention, Integer32):
    description = 'Highest signal level hardware removes then generates for transmission.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("undefined", 0), ("phys", 1), ("otnOtu", 2), ("otnOdu", 3), ("otnOpu", 4), ("sonetSection", 5), ("sonetLine", 6), ("sonetPath", 7), ("none", 8), ("pcs", 9), ("if10GbE", 10))

class OhTerminationLevelCaps(TextualConvention, Bits):
    description = 'Highest signal level hardware removes then generates for transmission.'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capPhys", 1), ("capOtnOtu", 2), ("capOtnOdu", 3), ("capOtnOpu", 4), ("capSonetSection", 5), ("capSonetLine", 6), ("capSonetPath", 7), ("capNone", 8), ("capPcs", 9), ("capIf10GbE", 10))

class OtnPayloadType(TextualConvention, Integer32):
    description = 'The PAYLOAD defines the transport service type of the payload'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 3, 4, 5, 6, 7, 8, 12, 15, 16, 17, 18, 39, 41, 52, 54, 55, 56, 85, 86, 87, 88, 110, 129, 150, 178, 192, 194, 195, 200, 206, 212, 58, 127, 196, 36, 214, 215, 499))
    namedValues = NamedValues(("undefined", 0), ("ifType10GbE", 3), ("ifTypeOc192", 4), ("ifTypeOc48", 5), ("ifTypeStm16", 6), ("ifTypeStm64", 7), ("ifType10GFC", 8), ("ifType1GFC", 12), ("ifTypeF9953", 15), ("ifTypeF10312", 16), ("ifTypeF10518", 17), ("ifTypeF2488", 18), ("ifType2GFC", 39), ("ifType1GbE", 41), ("ifTypeF4250", 52), ("ifTypeF10709", 54), ("ifTypeF11095", 55), ("ifTypeF11318", 56), ("ifTypeStm1", 85), ("ifTypeStm4", 86), ("ifTypeOc3", 87), ("ifTypeOc12", 88), ("ifTypeF8500", 110), ("ifTypeF10000", 129), ("ifTypeF5000", 150), ("ifTypeF14025", 178), ("ifType40GbE", 192), ("ifTypeF41250", 194), ("ifTypeF103125", 195), ("ifTypeF2457", 200), ("ifTypeFe", 206), ("ifTypeE10to1000t", 212), ("ifType4GFC", 58), ("ifType8GFC", 127), ("ifType16GFC", 196), ("ifTypeE10or100bt", 36), ("ifType25GbE", 214), ("ifType32GFC", 215), ("ifTypeNotDefined", 499))

class OtnPayloadTypeCaps(TextualConvention, Bits):
    description = 'The PAYLOAD defines the transport service type of the payload'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capIfType10GbE", 3), ("capIfTypeOc192", 4), ("capIfTypeOc48", 5), ("capIfTypeStm16", 6), ("capIfTypeStm64", 7), ("capIfType10GFC", 8), ("capIfType1GFC", 12), ("capIfTypeF9953", 15), ("capIfTypeF10312", 16), ("capIfTypeF10518", 17), ("capIfTypeF2488", 18), ("capIfType2GFC", 39), ("capIfType1GbE", 41), ("capIfTypeF4250", 52), ("capIfTypeF10709", 54), ("capIfTypeF11095", 55), ("capIfTypeF11318", 56), ("capIfTypeStm1", 85), ("capIfTypeStm4", 86), ("capIfTypeOc3", 87), ("capIfTypeOc12", 88), ("capIfTypeF8500", 110), ("capIfTypeF10000", 129), ("capIfTypeF5000", 150), ("capIfTypeF14025", 178), ("capIfType40GbE", 192), ("capIfTypeF41250", 194), ("capIfTypeF103125", 195), ("capIfTypeF2457", 200), ("capIfTypeFe", 206), ("capIfTypeE10to1000t", 212), ("capIfType4GFC", 58), ("capIfType8GFC", 127), ("capIfType16GFC", 196), ("capIfTypeE10or100bt", 36), ("capIfType25GbE", 214), ("capIfType32GFC", 215), ("capIfTypeNotDefined", 499))

class OtnTcmLevel(TextualConvention, Integer32):
    description = 'Activation of Tandem Connection Monitoring Instance A. 6 Tandem Connection Monitoring levels are available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("tcm1", 1), ("tcm2", 2), ("tcm3", 3), ("tcm4", 4), ("tcm5", 5), ("tcm6", 6), ("disabled", 7))

class OtnTcmLevelCaps(TextualConvention, Bits):
    description = 'Activation of Tandem Connection Monitoring Instance A. 6 Tandem Connection Monitoring levels are available.'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capTcm1", 1), ("capTcm2", 2), ("capTcm3", 3), ("capTcm4", 4), ("capTcm5", 5), ("capTcm6", 6), ("capDisabled", 7))

class PgmType(TextualConvention, Integer32):
    description = 'Program Type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("null", 1), ("ncu", 2), ("ncuHp", 3), ("fwps", 4), ("legacy", 5), ("nscuS", 6), ("fwpe", 7))

class ProtectionMech(TextualConvention, Integer32):
    description = 'Port Based refers to HST Cards and Switches: Card Based refers to additional equipment protection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("undefined", 0), ("pathProtection", 1), ("channelCardProtection", 2), ("channelProtection", 3), ("versatileSwitchedProtection", 4), ("flowProtection", 5), ("clientCardProtection", 6), ("controller", 7), ("none", 8))

class ProtectionMechCaps(TextualConvention, Bits):
    description = 'Port Based refers to HST Cards and Switches: Card Based refers to additional equipment protection'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capPathProtection", 1), ("capChannelCardProtection", 2), ("capChannelProtection", 3), ("capVersatileSwitchedProtection", 4), ("capFlowProtection", 5), ("capClientCardProtection", 6), ("capController", 7), ("capNone", 8))

class RestoreActivation(TextualConvention, Integer32):
    description = 'Shows whether the last activation was(will be) a database restore or a new software activation'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("notRestore", 1), ("restoreFromStdBy", 2), ("restoreToFactory", 3), ("restoreFromEqpt", 4), ("acceptDatabase", 5))

class RestoreActivationCaps(TextualConvention, Bits):
    description = 'Shows whether the last activation was(will be) a database restore or a new software activation'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNotRestore", 1), ("capRestoreFromStdBy", 2), ("capRestoreToFactory", 3), ("capRestoreFromEqpt", 4), ("capAcceptDatabase", 5))

class ServiceAffecting(TextualConvention, Integer32):
    description = 'Service Affecting Change during FWP upgrade and Restart operation'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("nsa", 1), ("sa", 2), ("saActivate", 3), ("saInstall", 4), ("none", 5))

class ServiceAffectingCaps(TextualConvention, Bits):
    description = 'Service Affecting Change during FWP upgrade and Restart operation'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNsa", 1), ("capSa", 2), ("capSaActivate", 3), ("capSaInstall", 4), ("capNone", 5))

class StandbyServiceAffecting(TextualConvention, Integer32):
    description = 'Service Affecting Change during FWP upgrade after activation of STBY PGM partition.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("nsa", 1), ("sa", 2), ("saActivate", 3), ("saInstall", 4), ("none", 5))

class SnmpProxySynchronizationState(TextualConvention, Integer32):
    description = "This parameter is used to synchronize proxy table on GNE with destination NE's\n        availability."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("inactive", 1), ("active", 2))

class SnmpProxySynchronizationStage(TextualConvention, Integer32):
    description = 'This parameter is used to indicate stage of synchronization process.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("started", 1), ("finished", 2))

class SonetSectSigDegThres(TextualConvention, Integer32):
    description = 'The SONET signal degrade threshold as a bit error rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("ber10exp5", 1), ("ber10exp6", 2), ("ber10exp7", 3), ("ber10exp8", 4), ("ber10exp9", 5))

class SonetSectSigDegThresCaps(TextualConvention, Integer32):
    description = 'The SONET signal degrade threshold as a bit error rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("capBer10exp5", 1), ("capBer10exp6", 2), ("capBer10exp7", 3), ("capBer10exp8", 4), ("capBer10exp9", 5))

class SonetTimingSource(TextualConvention, Integer32):
    description = 'Interface Timing Source Selection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("loopTiming", 1), ("internal", 2))

class SonetTimingSourceCaps(TextualConvention, Bits):
    description = 'Interface Timing Source Selection'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capLoopTiming", 1), ("capInternal", 2))

class SonetTraceForm(TextualConvention, Integer32):
    description = 'Byte-Length of Trace Compared to Expected'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("form64CRLF", 1), ("form16CRC7", 2), ("form1Byte", 3))

class SonetTraceFormCaps(TextualConvention, Bits):
    description = 'Byte-Length of Trace Compared to Expected'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capForm64CRLF", 1), ("capForm16CRC7", 2), ("capForm1Byte", 3))

class SonetVcBundleAllocation(TextualConvention, OctetString):
    description = 'Each byte represents one sequence position in the VC bundle, always assigned\n        consecutively. The sequence identifies the order in which the individual VCs are combined\n        within the VC-4-Xv/VC-3-Xv. Each VC has a fixed unique sequence number in the range of 0\n        to (X-1): byte 0: VC4/VC3 transporting the first container of the VC-4-Xv/VC-3-Xv is\n        assigned sequence number 0, byte 1: VC4/VC3 transporting the second container of the\n        VC-4-Xv/VC-3-Xv is assigned sequence number 1, etc. byte (X-1): VC4/VC3 transporting\n        container X of the VC-4-Xv/VC-3-Xv is assigned sequence number (X-1).'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class SonetVcBundleAllocationCaps(TextualConvention, Bits):
    description = 'Each bit set in the bitmask represents the number\n        of a free VC. Bit 0 = VC #1, and so on.'
    status = 'current'
    namedValues = NamedValues(("vc1", 0), ("vc2", 1), ("vc3", 2), ("vc4", 3), ("vc5", 4), ("vc6", 5), ("vc7", 6), ("vc8", 7), ("vc9", 8), ("vc10", 9), ("vc11", 10), ("vc12", 11), ("vc13", 12), ("vc14", 13), ("vc15", 14), ("vc16", 15), ("vc17", 16), ("vc18", 17), ("vc19", 18), ("vc20", 19), ("vc21", 20), ("vc22", 21), ("vc23", 22), ("vc24", 23), ("vc25", 24), ("vc26", 25), ("vc27", 26), ("vc28", 27), ("vc29", 28), ("vc30", 29), ("vc31", 30), ("vc32", 31), ("vc33", 32), ("vc34", 33), ("vc35", 34), ("vc36", 35), ("vc37", 36), ("vc38", 37), ("vc39", 38), ("vc40", 39), ("vc41", 40), ("vc42", 41), ("vc43", 42), ("vc44", 43), ("vc45", 44), ("vc46", 45), ("vc47", 46), ("vc48", 47), ("vc49", 48), ("vc50", 49), ("vc51", 50), ("vc52", 51), ("vc53", 52), ("vc54", 53), ("vc55", 54), ("vc56", 55), ("vc57", 56), ("vc58", 57), ("vc59", 58), ("vc60", 59), ("vc61", 60), ("vc62", 61), ("vc63", 62), ("vc64", 63))

class TimMode(TextualConvention, Integer32):
    description = 'OTU Trace Identifier Mismatch (TIM) detection/action for TIM defect.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("disabled", 1), ("enableAisDisabled", 2), ("enableAisEnabled", 3))

class TimModeCaps(TextualConvention, Bits):
    description = 'OTU Trace Identifier Mismatch (TIM) detection/action for TIM defect.'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capDisabled", 1), ("capEnableAisDisabled", 2), ("capEnableAisEnabled", 3))

class FspR7TrapsinkLifetime(TextualConvention, Integer32):
    description = 'Lifetime of Trapsink'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 0), ("duration1hour", 1), ("duration1day", 2), ("duration3days", 3), ("duration1week", 4), ("duration1month", 5), ("unlimited", 6))

class VirtualContainerType(TextualConvention, Integer32):
    description = 'Virtual Container Group Type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("undefined", 0), ("vc4Type", 1), ("vc3Au4Type", 2), ("sts1", 3), ("sts3c", 4), ("vs1", 5), ("vs2c", 6), ("sts24c", 7), ("sts48c", 8), ("vs4c", 9), ("vc4c8", 10), ("vc4c16", 11), ("vs0", 12), ("vs3c", 13), ("vs5c", 14), ("vs8c", 15), ("vs6c", 16), ("odu0", 17), ("odu1", 18), ("oduFlex", 19), ("vs7c", 20))

class VirtualContainerTypeCaps(TextualConvention, Bits):
    description = 'Virtual Container Group Type'
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capVc4Type", 1), ("capVc3Au4Type", 2), ("capSts1", 3), ("capSts3c", 4), ("capVs1", 5), ("capVs2c", 6), ("capSts24c", 7), ("capSts48c", 8), ("capVs4c", 9), ("capVc4c8", 10), ("capVc4c16", 11), ("capVs0", 12), ("capVs3c", 13), ("capVs5c", 14), ("capVs8c", 15), ("capVs6c", 16), ("capOdu0", 17), ("capOdu1", 18), ("capOduFlex", 19), ("capVs7c", 20))

class YesNoNA(TextualConvention, Integer32):
    description = 'Enumerator values yes(1), no(2), notApplicable(3).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2), ("notApplicable", 3))

class LogicalIfTransport(TextualConvention, OctetString):
    description = ''
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class LogicalIfTransportCaps(TextualConvention, Bits):
    description = ''
    status = 'current'
    namedValues = NamedValues(("lif1", 0), ("lif2", 1), ("lif3", 2), ("lif4", 3), ("lif5", 4), ("lif6", 5), ("lif7", 6), ("lif8", 7), ("lif9", 8), ("lif10", 9), ("lif11", 10), ("lif12", 11), ("lif13", 12), ("lif14", 13), ("lif15", 14), ("lif16", 15))

class ModuleForm(TextualConvention, Integer32):
    description = 'Form of module'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("native", 1), ("legacy", 2), ("compatible", 3), ("cloudConnect", 4))

neMibVariant = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neMibVariant.setStatus('current')
if mibBuilder.loadTexts: neMibVariant.setDescription('The variant of the SNMP enterprise MIB. This object will\n        together with sysObjectID [RFC1213] uniquely identify the\n        revision and variant of the enterprise MIB used by the NE.')
neManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neManufacturer.setStatus('current')
if mibBuilder.loadTexts: neManufacturer.setDescription('Manufacturer of the system. This value is used to present\n        in clear text the manufacturer of the system.')
neDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 3), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neDateAndTime.setStatus('current')
if mibBuilder.loadTexts: neDateAndTime.setDescription('Reports the current local time on the Network Element.\n        It also allows to set the local time. However, SET\n        requests may not be supported by all products.')
neMemorySizeTotal = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 4), KBytes()).setUnits('kBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: neMemorySizeTotal.setStatus('current')
if mibBuilder.loadTexts: neMemorySizeTotal.setDescription('The total amount of physical main memory contained in\n        the NEMI.')
neMemorySizeFree = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 5), KBytes()).setUnits('kBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: neMemorySizeFree.setStatus('current')
if mibBuilder.loadTexts: neMemorySizeFree.setDescription('The amount of unused physical main memory contained in\n        the NEMI.')
neStorageTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6), )
if mibBuilder.loadTexts: neStorageTable.setStatus('current')
if mibBuilder.loadTexts: neStorageTable.setDescription('The table of long-term storage partitions contained in\n        the NE.')
neStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1), ).setIndexNames((0, "ADVA-MIB", "neStorageIndex"))
if mibBuilder.loadTexts: neStorageEntry.setStatus('current')
if mibBuilder.loadTexts: neStorageEntry.setDescription('An entry for one long-term storage partition contained in\n        the NE.')
neStorageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: neStorageIndex.setStatus('current')
if mibBuilder.loadTexts: neStorageIndex.setDescription('The index of the NE storage partition.')
neStorageDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStorageDescr.setStatus('current')
if mibBuilder.loadTexts: neStorageDescr.setDescription('The product specific description of the NE storage\n        partition.')
neStorageCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 3), KBytes()).setUnits('kBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: neStorageCapacity.setStatus('current')
if mibBuilder.loadTexts: neStorageCapacity.setDescription('The total capacity of the NE storage partition.')
neStorageAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 1, 6, 1, 4), KBytes()).setUnits('kBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: neStorageAvailable.setStatus('current')
if mibBuilder.loadTexts: neStorageAvailable.setDescription('The free space on the NE storage partition.')
neAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 1, 7), TrapAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: neAlarmStatus.setDescription('The highest severity of all currently active alarms on the\n        NE. Alarms that are not reported because of Alarm Report\n        Control (ARC) or any other administrative state are not\n        considered active. The values indeterminate(1) and\n        notReported(7) are not applicable for this object. The value\n        cleared(6) indicates that the NE reports no alarm\n        (i.e. Alarm LED(s) off).')
snmpWriteAccessRestriction = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 2, 1), EnableState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpWriteAccessRestriction.setStatus('current')
if mibBuilder.loadTexts: snmpWriteAccessRestriction.setDescription('This value is used in combination with the\n        snmpWriteAccessTable for additional security for SNMP set\n        requests. When the status is Disabled, SNMP set requests\n        from any NMS (using the correct write community) are\n        accepted (ie, the snmpWriteAccessTable entries do not\n        apply).\n        When the status is Enabled, however, only SNMP set requests\n        from NMSs (using the correct write community) which are\n        listed in the snmpWriteAccessTable are accepted.\n        This object is read-only, meaning that it cannot be updated\n        via the SNMP interface. The operator must configure SNMP\n        write access permissions via a non-SNMP interface.')
snmpWriteAccessTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 2, 2), )
if mibBuilder.loadTexts: snmpWriteAccessTable.setStatus('current')
if mibBuilder.loadTexts: snmpWriteAccessTable.setDescription('Table of authorized NMSs (identified by IP address) for\n        SNMP set requests.\n        This table is not relevant if snmpWriteAccessRestriction is\n        set to Disabled.\n        The entries of this table are read-only. This means\n        that the SNMP write access permissions cannot be updated via\n        the SNMP interface. The operator must configure them via a\n        non-SNMP interface.')
snmpWriteAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 2, 2, 1), ).setIndexNames((0, "ADVA-MIB", "snmpWriteAccessNmsAddress"))
if mibBuilder.loadTexts: snmpWriteAccessEntry.setStatus('current')
if mibBuilder.loadTexts: snmpWriteAccessEntry.setDescription('Entries in the SNMP Write Access Table.\n        The maximum of rows in this table is product specific,\n        typically 10.')
snmpWriteAccessNmsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 2, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: snmpWriteAccessNmsAddress.setStatus('current')
if mibBuilder.loadTexts: snmpWriteAccessNmsAddress.setDescription('IP Address of the NMS which has SNMP write permission.')
snmpWriteAccessNmsName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 2, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpWriteAccessNmsName.setStatus('current')
if mibBuilder.loadTexts: snmpWriteAccessNmsName.setDescription('Name of the NMS.')
neEventsLogged = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 3, 1), TrapCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventsLogged.setStatus('current')
if mibBuilder.loadTexts: neEventsLogged.setDescription('This value is the sum of all notified events (trap counter).\n        It is also the event number of the most recent event\n        (neEventLogIndex) found in the neEventLog tables. It can,\n        for example, be used to check if a notification (trap) is\n        lost.\n        The value is reset to 0 after a cold start. The counter is\n        increased even if no trap sinks are specified.')
neEventLogTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2), )
if mibBuilder.loadTexts: neEventLogTable.setStatus('current')
if mibBuilder.loadTexts: neEventLogTable.setDescription("Table of events issued by the NE's SNMP agent. The eventLog\n        entries are read-only.")
neEventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1), ).setIndexNames((0, "ADVA-MIB", "neEventLogIndex"))
if mibBuilder.loadTexts: neEventLogEntry.setStatus('current')
if mibBuilder.loadTexts: neEventLogEntry.setDescription('Entries in the neEventLog Table. Enterprise traps are\n        always logged; logging of Generic traps is product specific.')
neEventLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 1), TrapCounter())
if mibBuilder.loadTexts: neEventLogIndex.setStatus('current')
if mibBuilder.loadTexts: neEventLogIndex.setDescription('The associated neEventsLogged counter for the logged\n        event (trap).')
neEventLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogTimeStamp.setStatus('current')
if mibBuilder.loadTexts: neEventLogTimeStamp.setDescription('The NE Date and Time when the event (trap) occurred. This\n        object is used in the trap varbind.')
neEventLogNotificationOID = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogNotificationOID.setStatus('current')
if mibBuilder.loadTexts: neEventLogNotificationOID.setDescription('The NOTIFICATION-TYPE object identifier of the event that\n        occurred. The last part of the OID corresponds to the\n        specific trap type value in the trap PDU.')
neEventLogIdentityTranslation = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 2, 1, 4), IdentityTranslation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogIdentityTranslation.setStatus('current')
if mibBuilder.loadTexts: neEventLogIdentityTranslation.setDescription('Translation of entPhysicalIndex/ifIndex or other identifier\n        to a string used in the trap varbind following the timestamp\n        varbind.')
neEventLogVarTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3), )
if mibBuilder.loadTexts: neEventLogVarTable.setStatus('current')
if mibBuilder.loadTexts: neEventLogVarTable.setDescription('Table of variables corresponding to events logged in the\n        neEventLog.')
neEventLogVarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1), ).setIndexNames((0, "ADVA-MIB", "neEventLogIndex"), (0, "ADVA-MIB", "neEventLogVarIndex"))
if mibBuilder.loadTexts: neEventLogVarEntry.setStatus('current')
if mibBuilder.loadTexts: neEventLogVarEntry.setDescription('Entries in the neEventLogVar Table. An entry appears in\n        this table for each variable in the varbind list of an entry\n        in the neEventLogTable. For an event having no variables,\n        no entries are found in this table.')
neEventLogVarIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: neEventLogVarIndex.setStatus('current')
if mibBuilder.loadTexts: neEventLogVarIndex.setDescription('A monotonically increasing integer, starting at 1 for a\n        given neEventLogIndex, for indexing a variable contained in\n        the varbind list of a logged event.')
neEventLogVarId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarId.setStatus('current')
if mibBuilder.loadTexts: neEventLogVarId.setDescription('The object identifier of the variable in the varbind list.')
neEventLogVarType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 7))).clone(namedValues=NamedValues(("integer32", 1), ("ipAddress", 2), ("octetString", 3), ("objectId", 4), ("counter64", 5), ("unsigned32", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarType.setStatus('current')
if mibBuilder.loadTexts: neEventLogVarType.setDescription('The type of variable. One and only one of the value objects\n        that follow must be instantiated, based on this type. The\n        used types depend on the enterprise traps defined for the\n        specific product.')
neEventLogVarInteger32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarInteger32Val.setStatus('current')
if mibBuilder.loadTexts: neEventLogVarInteger32Val.setDescription("The value when neEventLogVarType is 'integer32'. Integer32\n        is also used to represent INTEGER types.\n        Otherwise, 0 is returned.")
neEventLogVarIpAddressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarIpAddressVal.setStatus('current')
if mibBuilder.loadTexts: neEventLogVarIpAddressVal.setDescription("The value when neEventLogVarType is 'ipAddress'.\n        Otherwise, an empty address is returned.")
neEventLogVarOctetStringVal = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarOctetStringVal.setStatus('current')
if mibBuilder.loadTexts: neEventLogVarOctetStringVal.setDescription("The value when neEventLogVarType is 'octetString'.\n        OctetString is used for all string types, including\n        DisplayString, SnmpAdminString and DateAndTime.\n        Otherwise, an empty string is returned.")
neEventLogVarOidVal = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarOidVal.setStatus('current')
if mibBuilder.loadTexts: neEventLogVarOidVal.setDescription("The value when neEventLogVarType is 'objectId'.\n        Otherwise, an objectId { 0.0 } is returned.")
neEventLogVarCounter64Val = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarCounter64Val.setStatus('current')
if mibBuilder.loadTexts: neEventLogVarCounter64Val.setDescription("The value when neEventLogVarType is 'counter64'.")
neEventLogVarUnsigned32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neEventLogVarUnsigned32Val.setStatus('current')
if mibBuilder.loadTexts: neEventLogVarUnsigned32Val.setDescription("The value when neEventLogVarType is 'unsigned32'.")
neTrapsinkTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4), )
if mibBuilder.loadTexts: neTrapsinkTable.setStatus('current')
if mibBuilder.loadTexts: neTrapsinkTable.setDescription('Table of Trapsinks. A neTrapsinkTable entry can be created,\n        deleted or modified via the SNMP interface for a specific\n        address and port.')
neTrapsinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1), ).setIndexNames((0, "ADVA-MIB", "neTrapsinkAddress"), (0, "ADVA-MIB", "neTrapsinkPort"))
if mibBuilder.loadTexts: neTrapsinkEntry.setStatus('current')
if mibBuilder.loadTexts: neTrapsinkEntry.setDescription('Entries in the Trapsink Table. Entries are created and\n        deleted using the neTrapsinkRowStatus object. The maximum of\n        rows in this table is product specific.')
neTrapsinkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: neTrapsinkAddress.setStatus('current')
if mibBuilder.loadTexts: neTrapsinkAddress.setDescription('IP Address of the Management System which should receive\n        SNMP Traps.')
neTrapsinkPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: neTrapsinkPort.setStatus('current')
if mibBuilder.loadTexts: neTrapsinkPort.setDescription('The port number where the specified trap sink will receive\n        SNMP traps.')
neTrapsinkCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neTrapsinkCommunity.setStatus('current')
if mibBuilder.loadTexts: neTrapsinkCommunity.setDescription('Community String which is sent with an SNMP Trap to the\n        Management Station. If no community is specified, the\n        default (public) is used.')
neTrapsinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neTrapsinkRowStatus.setStatus('current')
if mibBuilder.loadTexts: neTrapsinkRowStatus.setDescription('The status of this conceptual row. To create a row in this\n        table, set this object to createAndGo(4). To remove a row,\n        set this object to destroy(6).')
neTrapsinkVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 5), Unsigned32()).setUnits('').setMaxAccess("readwrite")
if mibBuilder.loadTexts: neTrapsinkVersion.setStatus('current')
if mibBuilder.loadTexts: neTrapsinkVersion.setDescription('')
neTrapsinkUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neTrapsinkUserName.setStatus('current')
if mibBuilder.loadTexts: neTrapsinkUserName.setDescription('A human readable string representing the name of the user.')
neTrapsinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 3, 4, 1, 7), FspR7TrapsinkLifetime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neTrapsinkType.setStatus('current')
if mibBuilder.loadTexts: neTrapsinkType.setDescription('Lifetime of Trapsink.')
swVersionTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1), )
if mibBuilder.loadTexts: swVersionTable.setStatus('current')
if mibBuilder.loadTexts: swVersionTable.setDescription('Software version information table for units/modules which\n        run a management Operating System. This includes the\n        Application software and Operating System software.')
swVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: swVersionEntry.setStatus('current')
if mibBuilder.loadTexts: swVersionEntry.setDescription('Entries in the swVersion Table.')
swVersionActiveApplSw = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionActiveApplSw.setStatus('current')
if mibBuilder.loadTexts: swVersionActiveApplSw.setDescription('Reports the active Application software version on the\n        unit/module.')
swVersionInactiveApplSw = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionInactiveApplSw.setStatus('current')
if mibBuilder.loadTexts: swVersionInactiveApplSw.setDescription('Reports the inactive Application software version available\n        on the unit/module.')
swVersionActiveOperatingSw = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionActiveOperatingSw.setStatus('current')
if mibBuilder.loadTexts: swVersionActiveOperatingSw.setDescription('Reports the active Operating System software version on the\n        unit/module.')
swVersionInactiveOperatingSw = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionInactiveOperatingSw.setStatus('current')
if mibBuilder.loadTexts: swVersionInactiveOperatingSw.setDescription('Reports the inactive Operating System software version\n        available on the unit/module.')
swVersionNextBoot = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("activeVersion", 1), ("inactiveVersion", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersionNextBoot.setStatus('current')
if mibBuilder.loadTexts: swVersionNextBoot.setDescription('Reports which software will be run at next\n        boot, either the currently active one again\n        or the alternative (currently inactive) one.')
neSoftwareUpgrade = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2))
neSwUpgradeRequest = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("none", 1), ("download", 2), ("install", 3), ("activate", 4), ("revertToPrevious", 5), ("reboot", 6), ("downloadInstallActivateReboot", 7), ("installActivateReboot", 8), ("revertToPreviousReboot", 9), ("activateAlp", 10), ("activateDefaultAlp", 11), ("upload", 12), ("autoDownloadInstall", 13), ("autoInstall", 14), ("fwpInstall", 15), ("fwpDownloadInstall", 16), ("downloadCf", 17), ("uploadCf", 18), ("installCf", 19), ("autoInstallCf", 20), ("uploadPa", 21), ("activateWithFwp", 22), ("forceReboot", 23), ("stbyFwpInstall", 24)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeRequest.setStatus('current')
if mibBuilder.loadTexts: neSwUpgradeRequest.setDescription("The request to the software upgrade function.\n        Request 2..6 are single step requests while requests 7..9\n        are batch commands for common upgrade scenarios. Requests 13,14\n        are defined for automatic install process for F7 platform.\n\n        If the NE is the FTP server, the file must then have been\n        downloaded to the neSwUpgradeNeDirectory on the NE using the\n        'netadmin' account.")
neSwUpgradeState = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 2), NeSwUpgradeStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neSwUpgradeState.setStatus('current')
if mibBuilder.loadTexts: neSwUpgradeState.setDescription('The current status of the SW upgrade process.\n        NOTE: All failures that are caused by malfunctioning\n              hardware are reported as internalError(17).')
neSwUpgradeServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeServerAddress.setStatus('current')
if mibBuilder.loadTexts: neSwUpgradeServerAddress.setDescription('The IP address of the external FTP server.')
neSwUpgradeServerLogin = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 4), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeServerLogin.setStatus('current')
if mibBuilder.loadTexts: neSwUpgradeServerLogin.setDescription('The login name on the external FTP server.')
neSwUpgradeServerPasswd = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 5), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeServerPasswd.setStatus('current')
if mibBuilder.loadTexts: neSwUpgradeServerPasswd.setDescription('The password on the external FTP server. Read requests on\n        this object will return a zero-length string.')
neSwUpgradeServerDirectory = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 6), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeServerDirectory.setStatus('current')
if mibBuilder.loadTexts: neSwUpgradeServerDirectory.setDescription('The SW file location (path) on the external FTP server.')
neSwUpgradeFileName = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 7), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeFileName.setStatus('current')
if mibBuilder.loadTexts: neSwUpgradeFileName.setDescription('The SW file name (without path) on the external FTP server\n        or the name of the file which has been downloaded to the NE.')
neSwUpgradeNeDirectory = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neSwUpgradeNeDirectory.setStatus('current')
if mibBuilder.loadTexts: neSwUpgradeNeDirectory.setDescription('The SW file location (path) on the NE.')
neSwUpgradeTransferProtocol = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 9), FileTransferProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeTransferProtocol.setStatus('current')
if mibBuilder.loadTexts: neSwUpgradeTransferProtocol.setDescription('The transfer protocol to be used.')
sourceIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 10), SourceIpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sourceIpAddress.setStatus('current')
if mibBuilder.loadTexts: sourceIpAddress.setDescription('IP address used as source IP address in FTP Client session')
neSwInstallState = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 11), NeSwInstallStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neSwInstallState.setStatus('current')
if mibBuilder.loadTexts: neSwInstallState.setDescription('Software installation state.')
neSwUpgradeType = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("undefined", 0), ("legacy", 1), ("revised", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeType.setStatus('current')
if mibBuilder.loadTexts: neSwUpgradeType.setDescription('Required procedure type to be used for software download. legacy(1) is the default value.\n         This parameter MUST be set before any other parameters will be set for software upgrade\n         procedure (for example IP address, user name, password etc.). revised(2) value corresponds\n         to Revised Upgrade Procedure which uses new PGM format. This parameter is NOT stored in the\n         database and will be reset to default after SNMP Agent restart.\n        ')
neSwDownloadProgress = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%')
if mibBuilder.loadTexts: neSwDownloadProgress.setStatus('current')
if mibBuilder.loadTexts: neSwDownloadProgress.setDescription('Operational progress in % i.e. file transfer')
neSwUpgradeCommonIpSrv = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 4, 2, 14), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neSwUpgradeCommonIpSrv.setStatus('current')
if mibBuilder.loadTexts: neSwUpgradeCommonIpSrv.setDescription('IPv4/v6 Server Address')
provContainerTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 1), )
if mibBuilder.loadTexts: provContainerTable.setStatus('current')
if mibBuilder.loadTexts: provContainerTable.setDescription("This table defines the objects that support provisioning of\n        'container' class physical entities.  Provisioning sets up a\n        'container' to hold a specified physical entity.  This allows\n        a management client to configure the specified physical entity,\n        including all of its subordinates physical entities, before\n        installation.\n\n        Provisioning allows the network manager to 'create' the\n        physical entities that represent the new modules. In\n        essence, the device simulates the installation of the new\n        modules into the system.  This has the effect of creating all\n        conceptual rows in all the necessary tables that support the\n        physical entity and all its subordinate physical entities (e.g.,\n        entPhysicalTable, and ifTable).\n\n        The table extends some entries in the entPhysicalTable\n        (see ENTITY-MIB for further details). A entry appears in\n        this table for a physical entity matching the following\n        criteria:\n\n        1)  Its entPhysicalClass object has a value of 'container';\n\n        2)  It can contain one (but not multiple) physical entity;\n            and,\n\n        3)  It supports provisioning.\n\n\n        The following states cause an alarm to be raised at the level\n        of the containing module:\n\n        IF  provAssignmentState = assigned(1)\n              AND\n            provEquipmentState = unequipped(2)\n        THEN  'eqMissing' alarm\n\n        IF    provEquipmentState = invalid(3)\n        THEN  'eqNotAccepted' alarm\n        ")
provContainerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: provContainerEntry.setStatus('current')
if mibBuilder.loadTexts: provContainerEntry.setDescription('Entries in the provContainer Table.')
provAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("assigned", 1), ("unassigned", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provAssignmentState.setStatus('current')
if mibBuilder.loadTexts: provAssignmentState.setDescription('This status indicates the assignment (provisioning) of a\n        module type to the container.')
provEquipmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("equipped", 1), ("unequipped", 2), ("invalid", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provEquipmentState.setStatus('current')
if mibBuilder.loadTexts: provEquipmentState.setDescription("This status indicates how the container is equipped:\n\n        'equipped'      The container holds a module that fits to the\n                        container.\n\n        'unequipped'    The container does not hold any hardware.\n\n        'invalid'       The container holds a recognized module that\n                        the container is not capable of supporting,\n                        or the container holds an unrecognized\n                        module.\n        ")
neBackupRestore = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2))
neBackupRestoreRequest = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("none", 1), ("runBackup", 2), ("runRestore", 3), ("dBdownload", 4), ("dBupload", 5), ("dbDownloadScu", 6), ("dbUploadScu", 7), ("alpDownload", 8), ("alpUpload", 9), ("runBackupScu", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neBackupRestoreRequest.setStatus('current')
if mibBuilder.loadTexts: neBackupRestoreRequest.setDescription('Run network element configuration Backup/Restore operation:\n\n        - none(1):       No action (read only)\n\n        - runBackup(2):  Save the network element configuration to\n                         a file (write only)\n\n        - runRestore(3): Restore the network element configuration\n                         from a file (write only)\n\n        The Restore operation does not overwrite settings which are\n        required to reestablish contact to the NE via SNMP and\n        Telnet.')
neBackupRestoreState = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("noBackupAvailable", 1), ("backupInProgress", 2), ("backupAvailable", 3), ("restoreInProgress", 4), ("backupRestoreFail", 5), ("backupRestoreIdle", 6), ("backupRestoreCompleted", 7), ("dbActivationFailed", 8), ("dbActivationInProgress", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neBackupRestoreState.setStatus('current')
if mibBuilder.loadTexts: neBackupRestoreState.setDescription("The status of the current NE configuration backup/restore\n        operation activated by 'neBackupRestoreRequest'.")
neBackupRestoreFile = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neBackupRestoreFile.setStatus('current')
if mibBuilder.loadTexts: neBackupRestoreFile.setDescription('The full local path of the network element configuration\n        backup file.\n        This file is generated during the Backup operation and is\n        also used for the Restore operation.')
neRestoreFileBackupDate = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neRestoreFileBackupDate.setStatus('current')
if mibBuilder.loadTexts: neRestoreFileBackupDate.setDescription('The backup time of the current file to be used for Restore.\n        If no backup is available, this object reports 8 zero-octets.')
neF7AutomaticRemoteBackupSrvIp = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvIp.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvIp.setDescription('Remote server IP as a backup destination address.')
neF7AutomaticRemoteBackupSrvDir = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 6), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvDir.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvDir.setDescription('Remote server directory.')
neF7AutomaticRemoteBackupSrvLogin = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 7), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvLogin.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvLogin.setDescription('Remote user login.')
neF7AutomaticRemoteBackupSrvPass = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 8), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvPass.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrvPass.setDescription('Remote user password.')
neF7AutomaticRemoteBackupProtocol = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 10), FileTransferProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupProtocol.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupProtocol.setDescription('Connection protocol to be used for remote backup.')
neF7AutomaticRemoteBackupSrcIp = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 11), SourceIpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrcIp.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupSrcIp.setDescription('Source IP address to be used for remote backup.')
neF7AutomaticRemoteBackupTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 12), F7FileTimeStamp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupTimeStamp.setStatus('deprecated')
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupTimeStamp.setDescription('Add or omit the time stamp in the backuped filename.')
neF7AutomaticRemoteBackupCommonIpSrv = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 13), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupCommonIpSrv.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupCommonIpSrv.setDescription('Remote server IPv4/IPv6 as a backup destination address.')
neF7AutomaticBackupTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20), )
if mibBuilder.loadTexts: neF7AutomaticBackupTable.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticBackupTable.setDescription('Table releated to SCU/Remote backup.')
neF7AutomaticBackupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1), ).setIndexNames((0, "ADVA-MIB", "neF7AutomaticBackupIndex"))
if mibBuilder.loadTexts: neF7AutomaticBackupEntry.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticBackupEntry.setDescription('Entry releated to SCU/Remote backup.')
neF7AutomaticBackupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 1), EntityIndex())
if mibBuilder.loadTexts: neF7AutomaticBackupIndex.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticBackupIndex.setDescription('Index of the backup entity. May be the Backup SCU\n         entity index or Backup Remote entity index.')
neF7AutomaticBackupInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 2), F7AutoBackupInterval()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticBackupInterval.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticBackupInterval.setDescription('Schedule database backup interval.')
neF7AutomaticBackupStartDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 3), FspDate()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticBackupStartDate.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticBackupStartDate.setDescription('Schedule database backup start date.')
neF7AutomaticBackupStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 4), FspTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticBackupStartTime.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticBackupStartTime.setDescription('Schedule database backup start time.')
neF7AutomaticBackupNextDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 5), FspDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neF7AutomaticBackupNextDate.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticBackupNextDate.setDescription('Next schedule database backup date.')
neF7AutomaticBackupRunState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 6), F7AutoBackupRunState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticBackupRunState.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticBackupRunState.setDescription('Automatic Backup running state.')
neF7AutomaticBackupTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 2, 20, 1, 7), F7FileTimeStamp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticBackupTimeStamp.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticBackupTimeStamp.setDescription('Add or omit the time stamp in the backuped filename.')
neAutoBackup = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3))
neAutoBackupConfig = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("autoBackup", 2), ("autoBackupAndUpload", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupConfig.setStatus('current')
if mibBuilder.loadTexts: neAutoBackupConfig.setDescription('The configuration of the regular network element\n        configuration Backup/Restore:\n\n        - disabled(1):            No regular backup\n\n        - autoBackup(2):          Regular backup to a local file\n                                  is active\n\n        - autoBackupAndUpload(3): Regular backup and upload to\n                                  external FTP server is active\n\n        The default is autoBackup(2).\n\n        If this object is not disabled(1) all other auto-backup\n        objects are read-only. I.e., all neAutoBackupServerXxx\n        objects must be set before changing this object to\n        autoBackupAndUpload(3).')
neAutoBackupInterval = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 2), Unsigned32()).setUnits('hours').setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupInterval.setStatus('current')
if mibBuilder.loadTexts: neAutoBackupInterval.setDescription('The interval between two subsequent backup actions in\n        hours (default: 24 hours).')
neAutoBackupNextActionAt = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 3), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupNextActionAt.setStatus('current')
if mibBuilder.loadTexts: neAutoBackupNextActionAt.setDescription('The sliding time of the next backup action (default:\n        midnight local NE time).')
neAutoBackupServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupServerAddress.setStatus('current')
if mibBuilder.loadTexts: neAutoBackupServerAddress.setDescription('The IP address of the external FTP server for backup files.')
neAutoBackupServerLogin = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 5), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupServerLogin.setStatus('current')
if mibBuilder.loadTexts: neAutoBackupServerLogin.setDescription('The login name on the external FTP server for backup files.')
neAutoBackupServerPasswd = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 6), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupServerPasswd.setStatus('current')
if mibBuilder.loadTexts: neAutoBackupServerPasswd.setDescription('The password on the external FTP server for backup files.\n        Read requests on this object will return a zero-length\n        string.')
neAutoBackupServerDirectory = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 3, 7), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neAutoBackupServerDirectory.setStatus('current')
if mibBuilder.loadTexts: neAutoBackupServerDirectory.setDescription('The directory on the external FTP server to which the\n        backup files will be uploaded. The file name will be\n        generated automatically (containing NE IP addres and backup\n        time).')
sonetSectionConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1), )
if mibBuilder.loadTexts: sonetSectionConfigTable.setStatus('current')
if mibBuilder.loadTexts: sonetSectionConfigTable.setDescription('Contains entries for the configuration of SONET interfaces.  In the naming of\n        parameters, only sonet (and not sdh) is used for simplification.\n        This table extends the entries in\n        the ifTable (RFC 2863).')
sonetSectionConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: sonetSectionConfigEntry.setStatus('current')
if mibBuilder.loadTexts: sonetSectionConfigEntry.setDescription('SDH/SONET interfaces will have an entry\n        in this table.')
sonetSectionConfigTimingSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 1), SonetTimingSource()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigTimingSource.setStatus('current')
if mibBuilder.loadTexts: sonetSectionConfigTimingSource.setDescription('The SDH/SONET timing source for this interface.\n        - internal: used in stand-alone, point-to-point topologies\n        stand-alone (dedicated fiber operation)\n        - loopTiming: used in point-to-point via SDH network and\n        feeder topologies. The default is internal(1).')
sonetSectionConfigSignalDegradeThreshhold = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigSignalDegradeThreshhold.setStatus('current')
if mibBuilder.loadTexts: sonetSectionConfigSignalDegradeThreshhold.setDescription('Block-Error-Based Degradation Definition for SDH (standard integration period).\n        Defined as percentage Background Block Errors (30% default) evaluated\n        over a defined period (SDPER-RS).')
sonetSectionConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigSignalDegradePeriod.setStatus('current')
if mibBuilder.loadTexts: sonetSectionConfigSignalDegradePeriod.setDescription('The measurement period in seconds used together with\n        the sonetSectionConfigSignalDegradeThreshold based on the\n        block error counting method.\n        The valid range is 2..10, The default being 7.')
sonetSectionConfigTraceForm = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 4), SonetTraceForm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigTraceForm.setStatus('current')
if mibBuilder.loadTexts: sonetSectionConfigTraceForm.setDescription('Byte-Length of Trace Compared to Expected')
sonetSectionConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigTraceExpected.setStatus('current')
if mibBuilder.loadTexts: sonetSectionConfigTraceExpected.setDescription('Expected Sec/RS trace. NULL TRACE implies that no trace comparison is made.')
sonetSectionConfigTraceTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigTraceTransmit.setStatus('current')
if mibBuilder.loadTexts: sonetSectionConfigTraceTransmit.setDescription('Sec/RS Trace to be Transmitted')
sonetSectionConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 1, 1, 7), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonetSectionConfigTimMode.setStatus('current')
if mibBuilder.loadTexts: sonetSectionConfigTimMode.setDescription('SONET Section  Trace Identifier Mismatch (TIM) detection/action for TIM defect.')
sonetSectionDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3), )
if mibBuilder.loadTexts: sonetSectionDataTable.setStatus('current')
if mibBuilder.loadTexts: sonetSectionDataTable.setDescription('Contains entries for the status of SONET interfaces.  In the naming of\n        parameters, only sonet (and not sdh) is used for simplification.\n        This table extends the entries in\n        the ifTable (RFC 2863).')
sonetSectionDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: sonetSectionDataEntry.setStatus('current')
if mibBuilder.loadTexts: sonetSectionDataEntry.setDescription('SDH/SONET interfaces will have an entry\n        in this table.')
sonetSectionDataTraceReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 1, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonetSectionDataTraceReceived.setStatus('current')
if mibBuilder.loadTexts: sonetSectionDataTraceReceived.setDescription('The received Sec/RS Trace')
otuSectionConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1), )
if mibBuilder.loadTexts: otuSectionConfigTable.setStatus('current')
if mibBuilder.loadTexts: otuSectionConfigTable.setDescription('Contains entries for the configuration of OTU interfaces.\n        This table extends the entries in\n        the ifTable (RFC 2863).')
otuSectionConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: otuSectionConfigEntry.setStatus('current')
if mibBuilder.loadTexts: otuSectionConfigEntry.setDescription('OTU interfaces will have an entry\n        in this table.')
otuSectionConfigSignalDegradeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigSignalDegradeThreshold.setStatus('current')
if mibBuilder.loadTexts: otuSectionConfigSignalDegradeThreshold.setDescription('Threshold for OTU SM-SD alarm (threshold level 0..100%, default value 15 %).\n        Ref. table 24/G.7710.')
otuSectionConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigSignalDegradePeriod.setStatus('current')
if mibBuilder.loadTexts: otuSectionConfigSignalDegradePeriod.setDescription('Measuring period for OTU SM-SD alarm: 2..10 sec) (bursty)\n        Ref. table 24/G.7710.  Default value: 7.')
otuSectionConfigPayload = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 3), OtnPayloadType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigPayload.setStatus('current')
if mibBuilder.loadTexts: otuSectionConfigPayload.setDescription('The payload of the interface (inside a transport overhead).\n        Relevant e. g. for OTN cards which wrap a payload into an OTU1/2 wrapper.')
otuSectionConfigStuffing = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 4), EnableState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigStuffing.setStatus('current')
if mibBuilder.loadTexts: otuSectionConfigStuffing.setDescription('Indicates if bit/byte stuffing is used in the transport signal.')
otuSectionConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigTraceExpected.setStatus('current')
if mibBuilder.loadTexts: otuSectionConfigTraceExpected.setDescription('Expected SAPI part of the OTU trace (15 character). NULL TRACE implies that no trace comparison is made.')
otuSectionConfigTraceTransmitSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigTraceTransmitSapi.setStatus('current')
if mibBuilder.loadTexts: otuSectionConfigTraceTransmitSapi.setDescription('The transmitted SAPI part of the OTU trace (15 character)')
otuSectionConfigTraceTransmitDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigTraceTransmitDapi.setStatus('current')
if mibBuilder.loadTexts: otuSectionConfigTraceTransmitDapi.setDescription('The transmitted DAPI part of the OTU trace (15 character)')
otuSectionConfigTraceTransmitOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigTraceTransmitOpsp.setStatus('current')
if mibBuilder.loadTexts: otuSectionConfigTraceTransmitOpsp.setDescription('The transmitted Operator Specific part of the OTU trace (32 character)')
otuSectionConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 1, 1, 9), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: otuSectionConfigTimMode.setStatus('current')
if mibBuilder.loadTexts: otuSectionConfigTimMode.setDescription('OTU Trace Identifier Mismatch (TIM) detection/action for TIM defect.')
otuSectionDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2), )
if mibBuilder.loadTexts: otuSectionDataTable.setStatus('current')
if mibBuilder.loadTexts: otuSectionDataTable.setDescription('Contains entries for the status of OTU interfaces.\n        This table extends the entries in\n        the ifTable (RFC 2863).')
otuSectionDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: otuSectionDataEntry.setStatus('current')
if mibBuilder.loadTexts: otuSectionDataEntry.setDescription('OTU interfaces will have an entry\n        in this table.')
otuSectionDataResultingTotalBitrate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 1), Unsigned32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: otuSectionDataResultingTotalBitrate.setStatus('current')
if mibBuilder.loadTexts: otuSectionDataResultingTotalBitrate.setDescription('This interface bitrate is dependent on the type and the payload of the interface.\n        Relevant e. g. for OTN cards which wrap a payload into an OTU1/2 wrapper.')
otuSectionDataTraceReceivedSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: otuSectionDataTraceReceivedSapi.setStatus('current')
if mibBuilder.loadTexts: otuSectionDataTraceReceivedSapi.setDescription('The received SAPI part of the OTU trace (15 character)')
otuSectionDataTraceReceivedDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: otuSectionDataTraceReceivedDapi.setStatus('current')
if mibBuilder.loadTexts: otuSectionDataTraceReceivedDapi.setDescription('The received DAPI part of the OTU trace (15 character)')
otuSectionDataTraceReceivedOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: otuSectionDataTraceReceivedOpsp.setStatus('current')
if mibBuilder.loadTexts: otuSectionDataTraceReceivedOpsp.setDescription('The received Operator Specific part of the OTU trace (32 character)')
oduSectionConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1), )
if mibBuilder.loadTexts: oduSectionConfigTable.setStatus('current')
if mibBuilder.loadTexts: oduSectionConfigTable.setDescription('Contains entries for the configuration of ODU interfaces.\n        This table extends the entries in\n        the ifTable (RFC 2863).')
oduSectionConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduSectionConfigEntry.setStatus('current')
if mibBuilder.loadTexts: oduSectionConfigEntry.setDescription('ODU interfaces will have an entry\n        in this table.')
oduSectionConfigSignalDegradeThres = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigSignalDegradeThres.setStatus('current')
if mibBuilder.loadTexts: oduSectionConfigSignalDegradeThres.setDescription('Threshold for ODU SM-SD alarm (threshold level 0..100%,\n        default value 15 %. Ref. table 24/G.7710.')
oduSectionConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigSignalDegradePeriod.setStatus('current')
if mibBuilder.loadTexts: oduSectionConfigSignalDegradePeriod.setDescription('Measuring period for ODU SM-SD alarm: 2..10 sec) (bursty)\n        Ref. table 24/G.7710.  Default value: 7.')
oduSectionConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigTraceExpected.setStatus('current')
if mibBuilder.loadTexts: oduSectionConfigTraceExpected.setDescription('Expected SAPI part of the ODU trace (15 character). NULL TRACE implies that no trace comparison is made.')
oduSectionConfigTraceTransmitSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigTraceTransmitSapi.setStatus('current')
if mibBuilder.loadTexts: oduSectionConfigTraceTransmitSapi.setDescription('The transmitted SAPI part of the ODU trace (15 character)')
oduSectionConfigTraceTransmitDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigTraceTransmitDapi.setStatus('current')
if mibBuilder.loadTexts: oduSectionConfigTraceTransmitDapi.setDescription('The transmitted DAPI part of the ODU trace (15 character)')
oduSectionConfigTraceTransmitOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigTraceTransmitOpsp.setStatus('current')
if mibBuilder.loadTexts: oduSectionConfigTraceTransmitOpsp.setDescription('The transmitted Operator Specific part of the ODU trace (32 character)')
oduSectionConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 1, 1, 7), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduSectionConfigTimMode.setStatus('current')
if mibBuilder.loadTexts: oduSectionConfigTimMode.setDescription('Detection of TIM-ODU Condition can be configured')
oduSectionDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2), )
if mibBuilder.loadTexts: oduSectionDataTable.setStatus('current')
if mibBuilder.loadTexts: oduSectionDataTable.setDescription('Contains entries for the status of ODU interfaces.\n        This table extends the entries in\n        the ifTable (RFC 2863).')
oduSectionDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduSectionDataEntry.setStatus('current')
if mibBuilder.loadTexts: oduSectionDataEntry.setDescription('ODU interfaces will have an entry\n        in this table.')
oduSectionDataTraceReceivedSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduSectionDataTraceReceivedSapi.setStatus('current')
if mibBuilder.loadTexts: oduSectionDataTraceReceivedSapi.setDescription('The received SAPI part of the ODU trace (15 character)')
oduSectionDataTraceReceivedDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduSectionDataTraceReceivedDapi.setStatus('current')
if mibBuilder.loadTexts: oduSectionDataTraceReceivedDapi.setDescription('The received DAPI part of the ODU trace (15 character)')
oduSectionDataTraceReceivedOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduSectionDataTraceReceivedOpsp.setStatus('current')
if mibBuilder.loadTexts: oduSectionDataTraceReceivedOpsp.setDescription('The received Operator Specific part of the ODU trace (32 character)')
oduTcmAConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3), )
if mibBuilder.loadTexts: oduTcmAConfigTable.setStatus('current')
if mibBuilder.loadTexts: oduTcmAConfigTable.setDescription('Contains entries for the configuration of ODU interfaces.\n        This table extends the entries in\n        the ifTable (RFC 2863).')
oduTcmAConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmAConfigEntry.setStatus('current')
if mibBuilder.loadTexts: oduTcmAConfigEntry.setDescription('ODU interfaces will have an entry in this table.')
oduTcmAConfigSignalDegradeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigSignalDegradeThreshold.setStatus('current')
if mibBuilder.loadTexts: oduTcmAConfigSignalDegradeThreshold.setDescription('Threshold for ODU SM-SD alarm (threshold level 0..100%, default value 15 %).\n        Ref. table 24/G.7710.')
oduTcmAConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigSignalDegradePeriod.setStatus('current')
if mibBuilder.loadTexts: oduTcmAConfigSignalDegradePeriod.setDescription('Measuring period for ODU SM-SD alarm: 2..10 sec) (bursty)\n        Ref. table 24/G.7710.  Default value: 7.')
oduTcmAConfigTcmLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 3), OtnTcmLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTcmLevel.setStatus('current')
if mibBuilder.loadTexts: oduTcmAConfigTcmLevel.setDescription('Activation of Tandem Connection Monitoring Instance A')
oduTcmAConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTraceExpected.setStatus('current')
if mibBuilder.loadTexts: oduTcmAConfigTraceExpected.setDescription('Expected SAPI part of the TCMA trace (15 character). NULL TRACE-TCM implies that no trace comparison is made.')
oduTcmAConfigTraceTransmitSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTraceTransmitSapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmAConfigTraceTransmitSapi.setDescription('The transmitted SAPI part of the TCMA trace (15 character)')
oduTcmAConfigTraceTransmitDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTraceTransmitDapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmAConfigTraceTransmitDapi.setDescription('The transmitted DAPI part of the TCMA trace (15 character)')
oduTcmAConfigTraceTransmitOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTraceTransmitOpsp.setStatus('current')
if mibBuilder.loadTexts: oduTcmAConfigTraceTransmitOpsp.setDescription('The transmitted Operator Specific part of the TCMA trace (32 character)')
oduTcmAConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 3, 1, 8), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmAConfigTimMode.setStatus('current')
if mibBuilder.loadTexts: oduTcmAConfigTimMode.setDescription('TCM_A Trace Identifier Mismatch (TIM) detection/action for TIM defect.')
oduTcmBConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4), )
if mibBuilder.loadTexts: oduTcmBConfigTable.setStatus('current')
if mibBuilder.loadTexts: oduTcmBConfigTable.setDescription('Contains entries for the configuration of ODU interfaces.\n        This table extends the entries in the ifTable (RFC 2863).')
oduTcmBConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmBConfigEntry.setStatus('current')
if mibBuilder.loadTexts: oduTcmBConfigEntry.setDescription('ODU interfaces will have an entry in this table.')
oduTcmBConfigSignalDegradeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigSignalDegradeThreshold.setStatus('current')
if mibBuilder.loadTexts: oduTcmBConfigSignalDegradeThreshold.setDescription('Threshold for ODU SM-SD alarm (threshold level 0..100%, default value 15 %).\n        Ref. table 24/G.7710.')
oduTcmBConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigSignalDegradePeriod.setStatus('current')
if mibBuilder.loadTexts: oduTcmBConfigSignalDegradePeriod.setDescription('Measuring period for ODU SM-SD alarm: 2..10 sec) (bursty)\n        Ref. table 24/G.7710.  Default value: 7.')
oduTcmBConfigTcmLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 3), OtnTcmLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTcmLevel.setStatus('current')
if mibBuilder.loadTexts: oduTcmBConfigTcmLevel.setDescription('Activation of Tandem Connection Monitoring Instance B')
oduTcmBConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTraceExpected.setStatus('current')
if mibBuilder.loadTexts: oduTcmBConfigTraceExpected.setDescription('Expected SAPI part of the TCMB trace (15 character). NULL TRACE-TCM implies that no trace comparison is made.')
oduTcmBConfigTraceTransmitSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTraceTransmitSapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmBConfigTraceTransmitSapi.setDescription('The transmitted SAPI part of the TCMB trace (15 character)')
oduTcmBConfigTraceTransmitDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTraceTransmitDapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmBConfigTraceTransmitDapi.setDescription('The transmitted DAPI part of the TCMB trace (15 character)')
oduTcmBConfigTraceTransmitOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTraceTransmitOpsp.setStatus('current')
if mibBuilder.loadTexts: oduTcmBConfigTraceTransmitOpsp.setDescription('The transmitted Operator Specific part of the TCMB trace (32 character)')
oduTcmBConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 4, 1, 8), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmBConfigTimMode.setStatus('current')
if mibBuilder.loadTexts: oduTcmBConfigTimMode.setDescription('TCM_B Trace Identifier Mismatch (TIM) detection/action for TIM defect.')
oduTcmCConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5), )
if mibBuilder.loadTexts: oduTcmCConfigTable.setStatus('current')
if mibBuilder.loadTexts: oduTcmCConfigTable.setDescription('Contains entries for the configuration of ODU interfaces.\n        This table extends the entries in the ifTable (RFC 2863).')
oduTcmCConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmCConfigEntry.setStatus('current')
if mibBuilder.loadTexts: oduTcmCConfigEntry.setDescription('ODU interfaces will have an entry in this table.')
oduTcmCConfigSignalDegradeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 100), ValueRangeConstraint(-2147483648, -2147483648), ))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigSignalDegradeThreshold.setStatus('current')
if mibBuilder.loadTexts: oduTcmCConfigSignalDegradeThreshold.setDescription('Threshold for ODU SM-SD alarm (threshold level 0..100%, default value 15 %).\n        Ref. table 24/G.7710.')
oduTcmCConfigSignalDegradePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 10), ValueRangeConstraint(4294967295, 4294967295), ))).setUnits('s').setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigSignalDegradePeriod.setStatus('current')
if mibBuilder.loadTexts: oduTcmCConfigSignalDegradePeriod.setDescription('Measuring period for ODU SM-SD alarm: 2..10 sec) (bursty)\n        Ref. table 24/G.7710.  Default value: 7.')
oduTcmCConfigTcmLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 3), OtnTcmLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTcmLevel.setStatus('current')
if mibBuilder.loadTexts: oduTcmCConfigTcmLevel.setDescription('Activation of Tandem Connection Monitoring Instance C')
oduTcmCConfigTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTraceExpected.setStatus('current')
if mibBuilder.loadTexts: oduTcmCConfigTraceExpected.setDescription('Expected SAPI part of the TCMC trace (15 character). NULL TRACE-TCM implies that no trace comparison is made.')
oduTcmCConfigTraceTransmitSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTraceTransmitSapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmCConfigTraceTransmitSapi.setDescription('The transmitted SAPI part of the TCMC trace (15 character)')
oduTcmCConfigTraceTransmitDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTraceTransmitDapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmCConfigTraceTransmitDapi.setDescription('The transmitted DAPI part of the TCMC trace (15 character)')
oduTcmCConfigTraceTransmitOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTraceTransmitOpsp.setStatus('current')
if mibBuilder.loadTexts: oduTcmCConfigTraceTransmitOpsp.setDescription('The transmitted Operator Specific part of the TCMC trace (32 character)')
oduTcmCConfigTimMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 5, 1, 8), TimMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oduTcmCConfigTimMode.setStatus('current')
if mibBuilder.loadTexts: oduTcmCConfigTimMode.setDescription('TCM_C Trace Identifier Mismatch (TIM) detection/action for TIM defect.')
oduTcmADataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6), )
if mibBuilder.loadTexts: oduTcmADataTable.setStatus('current')
if mibBuilder.loadTexts: oduTcmADataTable.setDescription('Contains entries for the status of ODU interfaces.\n        This table extends the entries in the ifTable (RFC 2863).')
oduTcmADataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmADataEntry.setStatus('current')
if mibBuilder.loadTexts: oduTcmADataEntry.setDescription('ODU interfaces will have an entry in this table.')
oduTcmADataTraceReceivedSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmADataTraceReceivedSapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmADataTraceReceivedSapi.setDescription('The received SAPI part of the TCMA trace (15 character)')
oduTcmADataTraceReceivedDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmADataTraceReceivedDapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmADataTraceReceivedDapi.setDescription('The received DAPI part of the TCMA trace (15 character)')
oduTcmADataTraceReceivedOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmADataTraceReceivedOpsp.setStatus('current')
if mibBuilder.loadTexts: oduTcmADataTraceReceivedOpsp.setDescription('The received Operator Specific part of the TCMA trace (32 character)')
oduTcmBDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7), )
if mibBuilder.loadTexts: oduTcmBDataTable.setStatus('current')
if mibBuilder.loadTexts: oduTcmBDataTable.setDescription('Contains entries for the status of ODU interfaces.\n        This table extends the entries in the ifTable (RFC 2863).')
oduTcmBDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmBDataEntry.setStatus('current')
if mibBuilder.loadTexts: oduTcmBDataEntry.setDescription('ODU interfaces will have an entry in this table.')
oduTcmBDataTraceReceivedSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmBDataTraceReceivedSapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmBDataTraceReceivedSapi.setDescription('The received SAPI part of the TCMB trace (15 character)')
oduTcmBDataTraceReceivedDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmBDataTraceReceivedDapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmBDataTraceReceivedDapi.setDescription('The received DAPI part of the TCMB trace (15 character)')
oduTcmBDataTraceReceivedOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmBDataTraceReceivedOpsp.setStatus('current')
if mibBuilder.loadTexts: oduTcmBDataTraceReceivedOpsp.setDescription('The received Operator Specific part of the TCMB trace (32 character)')
oduTcmCDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8), )
if mibBuilder.loadTexts: oduTcmCDataTable.setStatus('current')
if mibBuilder.loadTexts: oduTcmCDataTable.setDescription('Contains entries for the status of ODU interfaces.\n        This table extends the entries in the ifTable (RFC 2863).')
oduTcmCDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: oduTcmCDataEntry.setStatus('current')
if mibBuilder.loadTexts: oduTcmCDataEntry.setDescription('ODU interfaces will have an entry in this table.')
oduTcmCDataTraceReceivedSapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmCDataTraceReceivedSapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmCDataTraceReceivedSapi.setDescription('The received SAPI part of the TCMC trace (15 character)')
oduTcmCDataTraceReceivedDapi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmCDataTraceReceivedDapi.setStatus('current')
if mibBuilder.loadTexts: oduTcmCDataTraceReceivedDapi.setDescription('The received DAPI part of the TCMC trace (15 character)')
oduTcmCDataTraceReceivedOpsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 4, 2, 2, 8, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oduTcmCDataTraceReceivedOpsp.setStatus('current')
if mibBuilder.loadTexts: oduTcmCDataTraceReceivedOpsp.setDescription('The received Operator Specific part of the TCMC trace (32 character)')
inventoryTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1), )
if mibBuilder.loadTexts: inventoryTable.setStatus('current')
if mibBuilder.loadTexts: inventoryTable.setDescription('This table lists all physically present (equipped) equipment in the NE')
inventoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: inventoryEntry.setStatus('current')
if mibBuilder.loadTexts: inventoryEntry.setDescription('')
inventoryUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryUnitName.setStatus('current')
if mibBuilder.loadTexts: inventoryUnitName.setDescription('ADVA Official Equipment Name')
inventoryFirmwarePackageRev = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryFirmwarePackageRev.setStatus('current')
if mibBuilder.loadTexts: inventoryFirmwarePackageRev.setDescription('Firmware Package Revision Number')
inventoryHardwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryHardwareRev.setStatus('current')
if mibBuilder.loadTexts: inventoryHardwareRev.setDescription('Equipment Revision Number')
inventorySoftwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventorySoftwareRev.setStatus('current')
if mibBuilder.loadTexts: inventorySoftwareRev.setDescription('The active Application software version on the unit/module.')
inventoryFpgaRev = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryFpgaRev.setStatus('current')
if mibBuilder.loadTexts: inventoryFpgaRev.setDescription('The active FPGA version on the unit/module.')
inventorySerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventorySerialNum.setStatus('current')
if mibBuilder.loadTexts: inventorySerialNum.setDescription('Equipment Serial Number')
inventoryPartnumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryPartnumber.setStatus('current')
if mibBuilder.loadTexts: inventoryPartnumber.setDescription('ADVA Part Number')
inventoryCleiCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryCleiCode.setStatus('current')
if mibBuilder.loadTexts: inventoryCleiCode.setDescription('Common Language Equipment Identifier')
inventoryVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryVendorId.setStatus('current')
if mibBuilder.loadTexts: inventoryVendorId.setDescription('OEM Vendor Code')
inventoryType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 10), EntityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryType.setStatus('current')
if mibBuilder.loadTexts: inventoryType.setDescription('Type of a physical entity: shelf/module/plug')
inventoryUniversalSerialIdent = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryUniversalSerialIdent.setStatus('current')
if mibBuilder.loadTexts: inventoryUniversalSerialIdent.setDescription('Unique Serial Identifier')
inventoryMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryMacAddress.setStatus('current')
if mibBuilder.loadTexts: inventoryMacAddress.setDescription('Ethernet MAC address')
inventoryGradeInventory = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 13), Grade()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryGradeInventory.setStatus('current')
if mibBuilder.loadTexts: inventoryGradeInventory.setDescription('Used to distinguish between NCU capabilities (range of supported services or applications)')
inventoryCfSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 14), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryCfSerialNum.setStatus('current')
if mibBuilder.loadTexts: inventoryCfSerialNum.setDescription('Compact Flash Serial Number')
inventoryCfModel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 1, 1, 15), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inventoryCfModel.setStatus('current')
if mibBuilder.loadTexts: inventoryCfModel.setDescription('Compact Flash Model Number')
entityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2), )
if mibBuilder.loadTexts: entityTable.setStatus('current')
if mibBuilder.loadTexts: entityTable.setDescription('Table for all existing addresses. Entities in this table are either\n        provisioned, equipped, both of these or neither of these. Containers\n        are always present in the table as long as their supporting entity\n        is provisioned or equipped.')
entityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: entityEntry.setStatus('current')
if mibBuilder.loadTexts: entityEntry.setDescription('Entry for all existing addresses.')
entityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: entityIndex.setStatus('current')
if mibBuilder.loadTexts: entityIndex.setDescription('Existing adress index')
entityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityContainedIn.setStatus('current')
if mibBuilder.loadTexts: entityContainedIn.setDescription('Contained in')
entityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 3), EntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityClass.setStatus('current')
if mibBuilder.loadTexts: entityClass.setDescription('See EntityClass')
entityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityClassInstanceNumber.setStatus('current')
if mibBuilder.loadTexts: entityClassInstanceNumber.setDescription('The class instance number of this entity within the module(card)')
entityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityIndexAid.setStatus('current')
if mibBuilder.loadTexts: entityIndexAid.setDescription('Name')
entityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 6), EntityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityType.setStatus('current')
if mibBuilder.loadTexts: entityType.setDescription('The type of FspR7 entity.  Please refer to EntityType for further deails.')
entityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 7), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityAssignmentState.setStatus('current')
if mibBuilder.loadTexts: entityAssignmentState.setDescription('See AssignmentState.')
entityEquipmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 2, 1, 8), EquipmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityEquipmentState.setStatus('current')
if mibBuilder.loadTexts: entityEquipmentState.setDescription('See EquipmentState.')
containsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3), )
if mibBuilder.loadTexts: containsTable.setStatus('current')
if mibBuilder.loadTexts: containsTable.setDescription('Table for all existing addresses. Gives the index of the subtending\n        entity in the containment.')
containsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"), (0, "ADVA-MIB", "containsIndex"))
if mibBuilder.loadTexts: containsEntry.setStatus('current')
if mibBuilder.loadTexts: containsEntry.setDescription('')
containsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 3, 1, 1), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: containsIndex.setStatus('current')
if mibBuilder.loadTexts: containsIndex.setDescription('')
controlPlaneWdmEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4), )
if mibBuilder.loadTexts: controlPlaneWdmEntityTable.setStatus('current')
if mibBuilder.loadTexts: controlPlaneWdmEntityTable.setDescription('Table for all existing addresses. Entities in this table are either\n        provisioned, equipped, both of these or neither of these. Containers\n        are always present in the table as long as their supporting entity\n        is provisioned or equipped.')
controlPlaneWdmEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneWdmEntityIndex"))
if mibBuilder.loadTexts: controlPlaneWdmEntityEntry.setStatus('current')
if mibBuilder.loadTexts: controlPlaneWdmEntityEntry.setDescription('Entry for all existing addresses.')
controlPlaneWdmEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: controlPlaneWdmEntityIndex.setStatus('current')
if mibBuilder.loadTexts: controlPlaneWdmEntityIndex.setDescription('Existing adress index')
controlPlaneWdmEntityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmEntityContainedIn.setStatus('current')
if mibBuilder.loadTexts: controlPlaneWdmEntityContainedIn.setDescription('Contained in')
controlPlaneWdmEntityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 3), CpWdmEntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmEntityClass.setStatus('current')
if mibBuilder.loadTexts: controlPlaneWdmEntityClass.setDescription('See EntityClass')
controlPlaneWdmEntityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmEntityClassInstanceNumber.setStatus('current')
if mibBuilder.loadTexts: controlPlaneWdmEntityClassInstanceNumber.setDescription('The class instance number of this entity within the module(card)')
controlPlaneWdmEntityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmEntityIndexAid.setStatus('current')
if mibBuilder.loadTexts: controlPlaneWdmEntityIndexAid.setDescription('Name')
controlPlaneWdmEntityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 4, 1, 6), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmEntityAssignmentState.setStatus('current')
if mibBuilder.loadTexts: controlPlaneWdmEntityAssignmentState.setDescription('See AssignmentState.')
controlPlaneWdmContainsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 5), )
if mibBuilder.loadTexts: controlPlaneWdmContainsTable.setStatus('current')
if mibBuilder.loadTexts: controlPlaneWdmContainsTable.setDescription('Table for all existing addresses. Gives the index of the subtending\n        entity in the containment.')
controlPlaneWdmContainsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 5, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneWdmEntityIndex"), (0, "ADVA-MIB", "controlPlaneWdmContainsIndex"))
if mibBuilder.loadTexts: controlPlaneWdmContainsEntry.setStatus('current')
if mibBuilder.loadTexts: controlPlaneWdmContainsEntry.setDescription('')
controlPlaneWdmContainsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 5, 1, 1), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneWdmContainsIndex.setStatus('current')
if mibBuilder.loadTexts: controlPlaneWdmContainsIndex.setDescription('')
controlPlaneEthEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6), )
if mibBuilder.loadTexts: controlPlaneEthEntityTable.setStatus('current')
if mibBuilder.loadTexts: controlPlaneEthEntityTable.setDescription('Table for all existing addresses. Entities in this table are either\n        provisioned, equipped, both of these or neither of these. Containers\n        are always present in the table as long as their supporting entity\n        is provisioned or equipped.')
controlPlaneEthEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneEthEntityIndex"))
if mibBuilder.loadTexts: controlPlaneEthEntityEntry.setStatus('current')
if mibBuilder.loadTexts: controlPlaneEthEntityEntry.setDescription('Entry for all existing addresses.')
controlPlaneEthEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: controlPlaneEthEntityIndex.setStatus('current')
if mibBuilder.loadTexts: controlPlaneEthEntityIndex.setDescription('Existing adress index')
controlPlaneEthEntityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthEntityContainedIn.setStatus('current')
if mibBuilder.loadTexts: controlPlaneEthEntityContainedIn.setDescription('Contained in')
controlPlaneEthEntityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 3), CpWdmEntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthEntityClass.setStatus('current')
if mibBuilder.loadTexts: controlPlaneEthEntityClass.setDescription('See EntityClass')
controlPlaneEthEntityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthEntityClassInstanceNumber.setStatus('current')
if mibBuilder.loadTexts: controlPlaneEthEntityClassInstanceNumber.setDescription('The class instance number of this entity within the module(card)')
controlPlaneEthEntityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthEntityIndexAid.setStatus('current')
if mibBuilder.loadTexts: controlPlaneEthEntityIndexAid.setDescription('Name')
controlPlaneEthEntityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 6, 1, 6), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthEntityAssignmentState.setStatus('current')
if mibBuilder.loadTexts: controlPlaneEthEntityAssignmentState.setDescription('See AssignmentState.')
controlPlaneEthContainsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 7), )
if mibBuilder.loadTexts: controlPlaneEthContainsTable.setStatus('current')
if mibBuilder.loadTexts: controlPlaneEthContainsTable.setDescription('Table for all existing addresses. Gives the index of the subtending\n        entity in the containment.')
controlPlaneEthContainsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 7, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneEthEntityIndex"), (0, "ADVA-MIB", "controlPlaneEthContainsIndex"))
if mibBuilder.loadTexts: controlPlaneEthContainsEntry.setStatus('current')
if mibBuilder.loadTexts: controlPlaneEthContainsEntry.setDescription('')
controlPlaneEthContainsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 7, 1, 1), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneEthContainsIndex.setStatus('current')
if mibBuilder.loadTexts: controlPlaneEthContainsIndex.setDescription('')
ptpEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10), )
if mibBuilder.loadTexts: ptpEntityTable.setStatus('current')
if mibBuilder.loadTexts: ptpEntityTable.setDescription('Table for PTP existing addresses. Entities in this table are either\n        provisioned, equipped, both of these or neither of these. Containers\n        are always present in the table as long as their supporting entity\n        is provisioned or equipped.')
ptpEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1), ).setIndexNames((0, "ADVA-MIB", "ptpEntityIndex"))
if mibBuilder.loadTexts: ptpEntityEntry.setStatus('current')
if mibBuilder.loadTexts: ptpEntityEntry.setDescription('')
ptpEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ptpEntityIndex.setStatus('current')
if mibBuilder.loadTexts: ptpEntityIndex.setDescription('Existing adress index')
ptpEntityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityContainedIn.setStatus('current')
if mibBuilder.loadTexts: ptpEntityContainedIn.setDescription('Contained in')
ptpEntityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 3), EntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityClass.setStatus('current')
if mibBuilder.loadTexts: ptpEntityClass.setDescription('See EntityClass')
ptpEntityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityClassInstanceNumber.setStatus('current')
if mibBuilder.loadTexts: ptpEntityClassInstanceNumber.setDescription('The class instance number of this entity within the module(card)')
ptpEntityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityIndexAid.setStatus('current')
if mibBuilder.loadTexts: ptpEntityIndexAid.setDescription('Name')
ptpEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 6), EntityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityType.setStatus('current')
if mibBuilder.loadTexts: ptpEntityType.setDescription('The type of FspR7 entity.  Please refer to EntityType for further deails.')
ptpEntityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 7), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityAssignmentState.setStatus('current')
if mibBuilder.loadTexts: ptpEntityAssignmentState.setDescription('See AssignmentState.')
ptpEntityEquipmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 8), EquipmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityEquipmentState.setStatus('current')
if mibBuilder.loadTexts: ptpEntityEquipmentState.setDescription('See EquipmentState.')
ptpEntityReferencedTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 10, 1, 9), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptpEntityReferencedTo.setStatus('current')
if mibBuilder.loadTexts: ptpEntityReferencedTo.setDescription('')
vtpEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11), )
if mibBuilder.loadTexts: vtpEntityTable.setStatus('current')
if mibBuilder.loadTexts: vtpEntityTable.setDescription('Table for VTP existing addresses. Entities in this table are either\n        provisioned, equipped, both of these or neither of these. Containers\n        are always present in the table as long as their supporting entity\n        is provisioned or equipped.')
vtpEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1), ).setIndexNames((0, "ADVA-MIB", "vtpEntityIndex"))
if mibBuilder.loadTexts: vtpEntityEntry.setStatus('current')
if mibBuilder.loadTexts: vtpEntityEntry.setDescription('')
vtpEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vtpEntityIndex.setStatus('current')
if mibBuilder.loadTexts: vtpEntityIndex.setDescription('Existing adress index')
vtpEntityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityContainedIn.setStatus('current')
if mibBuilder.loadTexts: vtpEntityContainedIn.setDescription('Contained in')
vtpEntityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 3), EntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityClass.setStatus('current')
if mibBuilder.loadTexts: vtpEntityClass.setDescription('See EntityClass')
vtpEntityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityClassInstanceNumber.setStatus('current')
if mibBuilder.loadTexts: vtpEntityClassInstanceNumber.setDescription('The class instance number of this entity within the module(card)')
vtpEntityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityIndexAid.setStatus('current')
if mibBuilder.loadTexts: vtpEntityIndexAid.setDescription('Name')
vtpEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 6), EntityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityType.setStatus('current')
if mibBuilder.loadTexts: vtpEntityType.setDescription('The type of FspR7 entity.  Please refer to EntityType for further deails.')
vtpEntityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 7), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityAssignmentState.setStatus('current')
if mibBuilder.loadTexts: vtpEntityAssignmentState.setDescription('See AssignmentState.')
vtpEntityEquipmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 8), EquipmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityEquipmentState.setStatus('current')
if mibBuilder.loadTexts: vtpEntityEquipmentState.setDescription('See EquipmentState.')
vtpEntityReferencedTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 11, 1, 9), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vtpEntityReferencedTo.setStatus('current')
if mibBuilder.loadTexts: vtpEntityReferencedTo.setDescription('')
controlPlaneOtnEntityTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12), )
if mibBuilder.loadTexts: controlPlaneOtnEntityTable.setStatus('current')
if mibBuilder.loadTexts: controlPlaneOtnEntityTable.setDescription('Table for all existing addresses. Entities in this table are either\n        provisioned, equipped, both of these or neither of these. Containers\n        are always present in the table as long as their supporting entity\n        is provisioned or equipped.')
controlPlaneOtnEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneOtnEntityIndex"))
if mibBuilder.loadTexts: controlPlaneOtnEntityEntry.setStatus('current')
if mibBuilder.loadTexts: controlPlaneOtnEntityEntry.setDescription('Entry for all existing addresses.')
controlPlaneOtnEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 1), EntityIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: controlPlaneOtnEntityIndex.setStatus('current')
if mibBuilder.loadTexts: controlPlaneOtnEntityIndex.setDescription('Existing adress index')
controlPlaneOtnEntityContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 2), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnEntityContainedIn.setStatus('current')
if mibBuilder.loadTexts: controlPlaneOtnEntityContainedIn.setDescription('Contained in')
controlPlaneOtnEntityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 3), CpWdmEntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnEntityClass.setStatus('current')
if mibBuilder.loadTexts: controlPlaneOtnEntityClass.setDescription('See EntityClass')
controlPlaneOtnEntityClassInstanceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 32000), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnEntityClassInstanceNumber.setStatus('current')
if mibBuilder.loadTexts: controlPlaneOtnEntityClassInstanceNumber.setDescription('The class instance number of this entity within the module(card)')
controlPlaneOtnEntityIndexAid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnEntityIndexAid.setStatus('current')
if mibBuilder.loadTexts: controlPlaneOtnEntityIndexAid.setDescription('Name')
controlPlaneOtnEntityAssignmentState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 12, 1, 6), AssignmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnEntityAssignmentState.setStatus('current')
if mibBuilder.loadTexts: controlPlaneOtnEntityAssignmentState.setDescription('See AssignmentState.')
controlPlaneOtnContainsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 13), )
if mibBuilder.loadTexts: controlPlaneOtnContainsTable.setStatus('current')
if mibBuilder.loadTexts: controlPlaneOtnContainsTable.setDescription('Table for all existing addresses. Gives the index of the subtending\n        entity in the containment.')
controlPlaneOtnContainsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 13, 1), ).setIndexNames((0, "ADVA-MIB", "controlPlaneOtnEntityIndex"), (0, "ADVA-MIB", "controlPlaneOtnContainsIndex"))
if mibBuilder.loadTexts: controlPlaneOtnContainsEntry.setStatus('current')
if mibBuilder.loadTexts: controlPlaneOtnContainsEntry.setDescription('')
controlPlaneOtnContainsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 5, 13, 1, 1), EntityIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: controlPlaneOtnContainsIndex.setStatus('current')
if mibBuilder.loadTexts: controlPlaneOtnContainsIndex.setDescription('')
swDbFileTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1), )
if mibBuilder.loadTexts: swDbFileTable.setStatus('current')
if mibBuilder.loadTexts: swDbFileTable.setDescription('')
swDbFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1), ).setIndexNames((0, "ADVA-MIB", "swDbFileIndex"))
if mibBuilder.loadTexts: swDbFileEntry.setStatus('current')
if mibBuilder.loadTexts: swDbFileEntry.setDescription('')
swDbFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 1), EntityIndex())
if mibBuilder.loadTexts: swDbFileIndex.setStatus('current')
if mibBuilder.loadTexts: swDbFileIndex.setDescription('Index')
swDbFileArea = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 2), FileArea()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileArea.setStatus('current')
if mibBuilder.loadTexts: swDbFileArea.setDescription('Type of Area')
swDbFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 3), FileType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileType.setStatus('current')
if mibBuilder.loadTexts: swDbFileType.setDescription('Type of File')
swDbFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 4), Unsigned32()).setUnits('Byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileSize.setStatus('current')
if mibBuilder.loadTexts: swDbFileSize.setDescription('Size of Memory = USED + AVAILABLE')
swDbFileCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileCreationTime.setStatus('current')
if mibBuilder.loadTexts: swDbFileCreationTime.setDescription('Creation Time')
swDbFileVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileVersion.setStatus('current')
if mibBuilder.loadTexts: swDbFileVersion.setDescription('General Release Issue Number of software in the ACT or STBY memory location. Format: XX-YY-Z')
swDbFileGrade = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 7), Grade()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileGrade.setStatus('current')
if mibBuilder.loadTexts: swDbFileGrade.setDescription('Used to distinguish between NCU capabilities (range of supported services or applications)')
swDbFileComment = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDbFileComment.setStatus('current')
if mibBuilder.loadTexts: swDbFileComment.setDescription('Comment of PGM or DBS files.')
swDbFileFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFileFileName.setStatus('current')
if mibBuilder.loadTexts: swDbFileFileName.setDescription('File Name')
swDbFileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDbFileRowStatus.setStatus('current')
if mibBuilder.loadTexts: swDbFileRowStatus.setDescription('RowStatus')
swDbFilePgmType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 1, 1, 11), PgmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbFilePgmType.setStatus('current')
if mibBuilder.loadTexts: swDbFilePgmType.setDescription('Program Type')
fwDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2), )
if mibBuilder.loadTexts: fwDataTable.setStatus('current')
if mibBuilder.loadTexts: fwDataTable.setDescription('')
fwDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: fwDataEntry.setStatus('current')
if mibBuilder.loadTexts: fwDataEntry.setDescription('')
fwDataNewVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataNewVersion.setStatus('current')
if mibBuilder.loadTexts: fwDataNewVersion.setDescription('New Firmware Package Revision Number of file which resides on ACT PGM partition.')
fwDataStandbyVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataStandbyVersion.setStatus('current')
if mibBuilder.loadTexts: fwDataStandbyVersion.setDescription('New Firmware Package Revision Number of file which resides on STBY PGM partition.')
fwDataServiceImpairment = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 3), ServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataServiceImpairment.setStatus('current')
if mibBuilder.loadTexts: fwDataServiceImpairment.setDescription('Service Affecting Change during FWP upgrade and Restart operation')
fwDataBootStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 4), BootState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataBootStatus.setStatus('current')
if mibBuilder.loadTexts: fwDataBootStatus.setDescription('Boot State. Every state change (excluding IDLE) does generate a corresponding transient condition.')
fwDataFirmwarePackageRev = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataFirmwarePackageRev.setStatus('current')
if mibBuilder.loadTexts: fwDataFirmwarePackageRev.setDescription('Active Firmware Package Revision Number of module software.')
fwDataStandbyServiceImpairment = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 6), StandbyServiceAffecting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataStandbyServiceImpairment.setStatus('current')
if mibBuilder.loadTexts: fwDataStandbyServiceImpairment.setDescription('Service Affecting Change during FWP upgrade after activation of STBY PGM partition.')
fwDataFirmwareAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 7), NoYesNA()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataFirmwareAvailable.setStatus('current')
if mibBuilder.loadTexts: fwDataFirmwareAvailable.setDescription('Firmware package for module available for ACT-PGM')
fwDataFirmwareApproved = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 8), NoYesNA()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataFirmwareApproved.setStatus('current')
if mibBuilder.loadTexts: fwDataFirmwareApproved.setDescription('Firmware package update for Encryption module is approved by Crypto Officer')
fwDataFirmwarePackageRevBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataFirmwarePackageRevBackup.setStatus('current')
if mibBuilder.loadTexts: fwDataFirmwarePackageRevBackup.setDescription('Standby Firmware Package Revision Number, Format XX.YY.ZZ (X,Y,Z are decimal characters, leading 0 are omitted).')
fwDataReadyForActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 10), YesNoNA()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataReadyForActivation.setStatus('current')
if mibBuilder.loadTexts: fwDataReadyForActivation.setDescription('FWPREV-STBY == FWPREV-SYS-ACT')
fwDataActivationReadyOnStandby = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 11), YesNoNA()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataActivationReadyOnStandby.setStatus('current')
if mibBuilder.loadTexts: fwDataActivationReadyOnStandby.setDescription('FWPREV-STBY == FWPREV-SYS-STBY')
fwDataProtectionPart = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 12), FspR7YesNo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataProtectionPart.setStatus('current')
if mibBuilder.loadTexts: fwDataProtectionPart.setDescription('Module is active part of Channel Card Protection Group.')
fwDataForm = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 13), ModuleForm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataForm.setStatus('current')
if mibBuilder.loadTexts: fwDataForm.setDescription('Form of module')
fwDataStandbyFirmwareAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 2, 1, 14), NoYesNA()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fwDataStandbyFirmwareAvailable.setStatus('current')
if mibBuilder.loadTexts: fwDataStandbyFirmwareAvailable.setDescription('Firmware package for module available for STBY-PGM')
coldRestartCapTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 3), )
if mibBuilder.loadTexts: coldRestartCapTable.setStatus('current')
if mibBuilder.loadTexts: coldRestartCapTable.setDescription('')
coldRestartCapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 3, 1), ).setIndexNames((0, "ADVA-MIB", "entityIndex"))
if mibBuilder.loadTexts: coldRestartCapEntry.setStatus('current')
if mibBuilder.loadTexts: coldRestartCapEntry.setDescription('')
coldRestartCapServiceAffectingCap = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 3, 1, 1), ServiceAffectingCaps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coldRestartCapServiceAffectingCap.setStatus('current')
if mibBuilder.loadTexts: coldRestartCapServiceAffectingCap.setDescription('Service Affecting Change during FWP upgrade and Restart operation')
eqpFwUpgradeRequest = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 10), CommandEqpt()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqpFwUpgradeRequest.setStatus('current')
if mibBuilder.loadTexts: eqpFwUpgradeRequest.setDescription('Update, Install and Reboot commands.')
eqpFwServiceImpairment = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 11), ServiceAffecting()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqpFwServiceImpairment.setStatus('current')
if mibBuilder.loadTexts: eqpFwServiceImpairment.setDescription('Service Affecting Change during FWP upgrade and Restart operation')
eqpFwNextEqpForUpdate = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 12), EntityIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqpFwNextEqpForUpdate.setStatus('current')
if mibBuilder.loadTexts: eqpFwNextEqpForUpdate.setDescription('The valid address of physically available Equipment part.')
eqpFwEqpType = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 13), FspR7EquipmentType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqpFwEqpType.setStatus('current')
if mibBuilder.loadTexts: eqpFwEqpType.setDescription("The TYPE of Equipment and the MODE setting determine uniquely the number and allowed TYPE's of the provisionable dependent entities (plugs, interfaces, modules)")
eqpFwNcuServerBusy = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 14), FspR7FalseTrue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqpFwNcuServerBusy.setStatus('current')
if mibBuilder.loadTexts: eqpFwNcuServerBusy.setDescription('NCU SW download busy')
eqpFwEqpServerBusy = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 15), FspR7FalseTrue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqpFwEqpServerBusy.setStatus('current')
if mibBuilder.loadTexts: eqpFwEqpServerBusy.setDescription('Firmware package download busy')
updateEqpt = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: updateEqpt.setStatus('current')
if mibBuilder.loadTexts: updateEqpt.setDescription('Number of equipment which have to be updated')
installedEqpt = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedEqpt.setStatus('current')
if mibBuilder.loadTexts: installedEqpt.setDescription('Number of equipment is already installed')
selectedFile = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 18), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: selectedFile.setStatus('current')
if mibBuilder.loadTexts: selectedFile.setDescription('File Name')
ncuActivationDate = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 19), FspR7Date()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuActivationDate.setStatus('current')
if mibBuilder.loadTexts: ncuActivationDate.setDescription('Activation Date in local time. Format: YY-MM-DD')
ncuActivationTime = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 20), FspR7Time()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuActivationTime.setStatus('current')
if mibBuilder.loadTexts: ncuActivationTime.setDescription('Activation Time in local time. Format HH-MM-SS')
ncuScheduledActivation = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 21), NcuAutoActivation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuScheduledActivation.setStatus('current')
if mibBuilder.loadTexts: ncuScheduledActivation.setDescription('Enable scheduled activation of the standby PGM partition.')
ncuScheduledDbRestore = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 22), RestoreActivation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuScheduledDbRestore.setStatus('current')
if mibBuilder.loadTexts: ncuScheduledDbRestore.setDescription('Shows whether scheduled activtion will be a database restore or a new software activation')
encryptionFwpFile = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 23), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: encryptionFwpFile.setStatus('current')
if mibBuilder.loadTexts: encryptionFwpFile.setDescription('The name FWP for encryption capable modules.')
clearRdiskRequest = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("undefined", 0), ("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearRdiskRequest.setStatus('current')
if mibBuilder.loadTexts: clearRdiskRequest.setDescription('This object initiate RDISK clearance.')
ncuActivationDateUtc = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 25), FspR7Date()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuActivationDateUtc.setStatus('current')
if mibBuilder.loadTexts: ncuActivationDateUtc.setDescription('Activation Date Format: YY-MM-DD')
ncuActivationTimeUtc = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 26), FspR7Time()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncuActivationTimeUtc.setStatus('current')
if mibBuilder.loadTexts: ncuActivationTimeUtc.setDescription('Activation Time Format: HH-MM-SS')
neBackupEncryption = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 38), EnableState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neBackupEncryption.setStatus('current')
if mibBuilder.loadTexts: neBackupEncryption.setDescription('Allows the database backup file to be encrypted with a user specified password.')
neBackupPassword = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 39), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neBackupPassword.setStatus('current')
if mibBuilder.loadTexts: neBackupPassword.setDescription('Secret, case-sensitive password to for encryption')
neF7AutomaticRemoteBackupEncryption = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 40), EnableState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupEncryption.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupEncryption.setDescription('Allows the database backup file to be encrypted with a user specified password.')
neF7AutomaticRemoteBackupPassword = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 41), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupPassword.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupPassword.setDescription('Secret, case-sensitive password to for encryption')
neBackupUsers = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 42), FspR7UsersDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neBackupUsers.setStatus('current')
if mibBuilder.loadTexts: neBackupUsers.setDescription('Specifies how user accounts are handled for database operations')
neInitialConnectionMode = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 43), FspR7EnableDisable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neInitialConnectionMode.setStatus('current')
if mibBuilder.loadTexts: neInitialConnectionMode.setDescription("NCU C1 Auto Connect/DHCP Mode will offer DHCP leases to the user's device.")
neF7AutomaticRemoteBackupUsers = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 1, 44), FspR7UsersDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupUsers.setStatus('current')
if mibBuilder.loadTexts: neF7AutomaticRemoteBackupUsers.setDescription('Specifies how user accounts are handled for database operations')
neRestoreConfig = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 1), RestoreActivation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neRestoreConfig.setStatus('current')
if mibBuilder.loadTexts: neRestoreConfig.setDescription('Shows whether the last activation was(will be) a database restore or a new software activation')
swDbDataTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2), )
if mibBuilder.loadTexts: swDbDataTable.setStatus('current')
if mibBuilder.loadTexts: swDbDataTable.setDescription('')
swDbDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1), ).setIndexNames((0, "ADVA-MIB", "swDbDataIndex"))
if mibBuilder.loadTexts: swDbDataEntry.setStatus('current')
if mibBuilder.loadTexts: swDbDataEntry.setDescription('')
swDbDataIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 1), EntityIndex())
if mibBuilder.loadTexts: swDbDataIndex.setStatus('current')
if mibBuilder.loadTexts: swDbDataIndex.setDescription('Index')
swDbDataArea = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 2), FileArea()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataArea.setStatus('current')
if mibBuilder.loadTexts: swDbDataArea.setDescription('Type of Area')
swDbDataProgramVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataProgramVersion.setStatus('current')
if mibBuilder.loadTexts: swDbDataProgramVersion.setDescription('General Release Issue Number of software in the ACT or STBY memory location. Format: XX-YY-Z')
swDbDataDatabaseVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataDatabaseVersion.setStatus('current')
if mibBuilder.loadTexts: swDbDataDatabaseVersion.setDescription('General Release Issue Number of Database in the ACT or STBY memory location. Typically this will be the same as the GISSUE.')
swDbDataActivationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataActivationTime.setStatus('current')
if mibBuilder.loadTexts: swDbDataActivationTime.setDescription('Activation Time')
swDbDataRestoreConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 6), RestoreActivation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataRestoreConfig.setStatus('current')
if mibBuilder.loadTexts: swDbDataRestoreConfig.setDescription('Shows whether the last activation was(will be) a database restore or a new software activation')
swDbDataFirmwareSetVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataFirmwareSetVersion.setStatus('current')
if mibBuilder.loadTexts: swDbDataFirmwareSetVersion.setDescription('Firmware Package Set Version')
swDbDataNcuSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNcuSoftwareVersion.setStatus('current')
if mibBuilder.loadTexts: swDbDataNcuSoftwareVersion.setDescription('NCU Software Version ACT or STBY memory location. Format: XX-YY-Z')
swDbDataStandbyPartitionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 9), PartitionStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataStandbyPartitionStatus.setStatus('current')
if mibBuilder.loadTexts: swDbDataStandbyPartitionStatus.setDescription('Partition State')
swDbDataNumEqpt = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumEqpt.setStatus('current')
if mibBuilder.loadTexts: swDbDataNumEqpt.setDescription('Number of all provisioned and equipped equipment in system')
swDbDataNumLegacyEqpt = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumLegacyEqpt.setStatus('current')
if mibBuilder.loadTexts: swDbDataNumLegacyEqpt.setDescription('Number of all legacy provisioned and equipped modules in system,')
swDbDataNumNativeSaUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumNativeSaUpdate.setStatus('current')
if mibBuilder.loadTexts: swDbDataNumNativeSaUpdate.setDescription('Number of all native modules which have to be updated (SA), both with already properly installed pak on standby image and those which need installation.')
swDbDataNumNativeNsaUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumNativeNsaUpdate.setStatus('current')
if mibBuilder.loadTexts: swDbDataNumNativeNsaUpdate.setDescription('Number of all modules which have to be updated (NSA),both with already properly installed pak on standby image and those which need installation.')
swDbDataNumLegacyUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumLegacyUpdate.setStatus('current')
if mibBuilder.loadTexts: swDbDataNumLegacyUpdate.setDescription('Number of all legacy modules which have to be updated.')
swDbDataNumSaNotReady = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumSaNotReady.setStatus('current')
if mibBuilder.loadTexts: swDbDataNumSaNotReady.setDescription('Number of modules which can be updated with a service affecting (SA) firmware package.')
swDbDataNumNsaNotReady = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 2, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataNumNsaNotReady.setStatus('current')
if mibBuilder.loadTexts: swDbDataNumNsaNotReady.setDescription('Number of modules which can be updated with a non-service affecting (NSA) firmware package.')
swDbDataCapTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3), )
if mibBuilder.loadTexts: swDbDataCapTable.setStatus('current')
if mibBuilder.loadTexts: swDbDataCapTable.setDescription('')
swDbDataCapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3, 1), ).setIndexNames((0, "ADVA-MIB", "swDbDataCapUpgradeRequest"))
if mibBuilder.loadTexts: swDbDataCapEntry.setStatus('current')
if mibBuilder.loadTexts: swDbDataCapEntry.setDescription('')
swDbDataCapUpgradeRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("undefined", 0), ("none", 1), ("download", 2), ("install", 3), ("activate", 4), ("revertToPrevious", 5), ("reboot", 6), ("downloadInstallActivateReboot", 7), ("installActivateReboot", 8), ("revertToPreviousReboot", 9), ("activateAlp", 10), ("activateDefaultAlp", 11), ("upload", 12), ("autoDownloadInstall", 13), ("autoInstall", 14), ("fwpInstall", 15), ("fwpDownloadInstall", 16), ("downloadCf", 17), ("uploadCf", 18), ("installCf", 19), ("autoInstallCf", 20), ("uploadPa", 21), ("activateWithFwp", 22), ("forceReboot", 23), ("stbyFwpInstall", 24))))
if mibBuilder.loadTexts: swDbDataCapUpgradeRequest.setStatus('current')
if mibBuilder.loadTexts: swDbDataCapUpgradeRequest.setDescription('Index value is a requested upgrade type from neSwUpgradeRequest object,\n        where following values are applicable:\n        - install(3)\n        - activate(4)\n        - reboot(6)\n        - activateAlp(10)\n        - activateDefaultAlp(11)')
swDbDataCapRestoreConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 3, 1, 2), RestoreActivationCaps()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataCapRestoreConfig.setStatus('current')
if mibBuilder.loadTexts: swDbDataCapRestoreConfig.setDescription('Shows whether the last activation was(will be) a database restore or a new software activation')
swDbDataDefaultsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4), )
if mibBuilder.loadTexts: swDbDataDefaultsTable.setStatus('current')
if mibBuilder.loadTexts: swDbDataDefaultsTable.setDescription('')
swDbDataDefaultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4, 1), ).setIndexNames((0, "ADVA-MIB", "swDbDataDefaultsUpgradeRequest"))
if mibBuilder.loadTexts: swDbDataDefaultsEntry.setStatus('current')
if mibBuilder.loadTexts: swDbDataDefaultsEntry.setDescription('')
swDbDataDefaultsUpgradeRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("undefined", 0), ("none", 1), ("download", 2), ("install", 3), ("activate", 4), ("revertToPrevious", 5), ("reboot", 6), ("downloadInstallActivateReboot", 7), ("installActivateReboot", 8), ("revertToPreviousReboot", 9), ("activateAlp", 10), ("activateDefaultAlp", 11), ("upload", 12), ("autoDownloadInstall", 13), ("autoInstall", 14), ("fwpInstall", 15), ("fwpDownloadInstall", 16), ("downloadCf", 17), ("uploadCf", 18), ("installCf", 19), ("autoInstallCf", 20), ("uploadPa", 21), ("activateWithFwp", 22), ("forceReboot", 23), ("stbyFwpInstall", 24))))
if mibBuilder.loadTexts: swDbDataDefaultsUpgradeRequest.setStatus('current')
if mibBuilder.loadTexts: swDbDataDefaultsUpgradeRequest.setDescription('Index value is a requested upgrade type from neSwUpgradeRequest object,\n        where following values are applicable:\n        - install(3)\n        - activate(4)\n        - reboot(6)\n        - activateAlp(10)\n        - activateDefaultAlp(11)')
swDbDataDefaultsRestoreConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 6, 2, 4, 1, 2), RestoreActivation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDbDataDefaultsRestoreConfig.setStatus('current')
if mibBuilder.loadTexts: swDbDataDefaultsRestoreConfig.setDescription('Shows whether the last activation was(will be) a database restore or a new software activation')
snmpServerPort = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpServerPort.setStatus('current')
if mibBuilder.loadTexts: snmpServerPort.setDescription('The TCP or UDP port on which a server is listening')
snmpProxyServerAdminState = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 3), FspR7AdminStateSnmpProxy()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpProxyServerAdminState.setStatus('current')
if mibBuilder.loadTexts: snmpProxyServerAdminState.setDescription('Administrative State is displayed in the GUI and Craft. Transition to Unassigend requires the entity to be deleted.')
snmpProxyServerPort = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpProxyServerPort.setStatus('current')
if mibBuilder.loadTexts: snmpProxyServerPort.setDescription('The TCP or UDP port on which a server is listening')
snmpProxyServerSynchroState = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 5), SnmpProxySynchronizationState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpProxyServerSynchroState.setStatus('current')
if mibBuilder.loadTexts: snmpProxyServerSynchroState.setDescription("This parameter is used to synchronize proxy table on GNE with destination NE's\n        availability.")
snmpProxyServerSynchroStage = MibScalar((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 6), SnmpProxySynchronizationStage()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: snmpProxyServerSynchroStage.setStatus('current')
if mibBuilder.loadTexts: snmpProxyServerSynchroStage.setDescription('This parameter is used to indicate stage of synchronization process.')
snmpProxyEntrySingleTargetOutTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10), )
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutTable.setStatus('current')
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutTable.setDescription('')
snmpProxyEntrySingleTargetOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1), ).setIndexNames((0, "ADVA-MIB", "snmpProxyEntrySingleTargetOutAddress"), (0, "ADVA-MIB", "snmpProxyEntrySingleTargetOutPort"))
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutEntry.setStatus('current')
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutEntry.setDescription('')
snmpProxyEntrySingleTargetOutAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 1), IpAddress())
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutAddress.setStatus('current')
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutAddress.setDescription('IP Address assigned to LAN IP Interface')
snmpProxyEntrySingleTargetOutPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutPort.setStatus('current')
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutPort.setDescription('The destination port')
snmpProxyEntrySingleTargetOutNodeAgentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 3), DestinationNodeOrAgentState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutNodeAgentStatus.setStatus('current')
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutNodeAgentStatus.setDescription('')
snmpProxyEntrySingleTargetOutContext = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutContext.setStatus('current')
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutContext.setDescription('The contextName used in SNMP messages to an SNMP Proxy Forwarder to indicate for which SNMP Proxy Client the SNMP messages is meant')
snmpProxyEntrySingleTargetOutRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutRowStatus.setStatus('current')
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutRowStatus.setDescription('RowStatus')
snmpProxyEntrySingleTargetOutAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 6), FspR7AdminStateSnmpProxy()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutAdminState.setStatus('current')
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutAdminState.setDescription('Administrative State is displayed in the GUI and Craft. Transition to Unassigend requires the entity to be deleted.')
snmpProxyEntrySingleTargetOutUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 2, 5, 7, 10, 1, 7), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutUserName.setStatus('current')
if mibBuilder.loadTexts: snmpProxyEntrySingleTargetOutUserName.setDescription('The name string for user authentication purposes')
mibBuilder.exportSymbols("ADVA-MIB", SourceIpAddress=SourceIpAddress, admin=admin, neMibVariant=neMibVariant, snmpWriteAccessNmsAddress=snmpWriteAccessNmsAddress, neInfo=neInfo, fwDataStandbyFirmwareAvailable=fwDataStandbyFirmwareAvailable, EthDuplexMode=EthDuplexMode, swDbDataNumNsaNotReady=swDbDataNumNsaNotReady, neF7AutomaticBackupInterval=neF7AutomaticBackupInterval, swDbDataRestoreConfig=swDbDataRestoreConfig, config=config, neF7AutomaticBackupNextDate=neF7AutomaticBackupNextDate, neEventLogVarEntry=neEventLogVarEntry, vtpEntityIndex=vtpEntityIndex, swDbDataStandbyPartitionStatus=swDbDataStandbyPartitionStatus, controlPlaneEthEntityContainedIn=controlPlaneEthEntityContainedIn, neTrapsinkCommunity=neTrapsinkCommunity, sonetSectionConfigTimingSource=sonetSectionConfigTimingSource, neSwUpgradeFileName=neSwUpgradeFileName, neEventLogVarOctetStringVal=neEventLogVarOctetStringVal, swDbDataDefaultsUpgradeRequest=swDbDataDefaultsUpgradeRequest, neF7AutomaticBackupRunState=neF7AutomaticBackupRunState, StandbyServiceAffecting=StandbyServiceAffecting, swDbFileIndex=swDbFileIndex, oduTcmBConfigTimMode=oduTcmBConfigTimMode, snmpProxyServerSynchroStage=snmpProxyServerSynchroStage, fspNm=fspNm, oduSectionConfigTraceTransmitDapi=oduSectionConfigTraceTransmitDapi, oduSectionConfigTraceExpected=oduSectionConfigTraceExpected, neTrapsinkVersion=neTrapsinkVersion, neEventLogVarIpAddressVal=neEventLogVarIpAddressVal, oduTcmCConfigTraceTransmitOpsp=oduTcmCConfigTraceTransmitOpsp, NcuAutoActivation=NcuAutoActivation, containsIndex=containsIndex, swVersionActiveApplSw=swVersionActiveApplSw, swDbFileType=swDbFileType, vtpEntityReferencedTo=vtpEntityReferencedTo, swDbFileComment=swDbFileComment, neF7AutomaticRemoteBackupSrvPass=neF7AutomaticRemoteBackupSrvPass, controlPlaneOtnEntityIndex=controlPlaneOtnEntityIndex, controlPlaneOtnEntityIndexAid=controlPlaneOtnEntityIndexAid, SnmpProxySynchronizationStage=SnmpProxySynchronizationStage, controlPlaneOtnEntityContainedIn=controlPlaneOtnEntityContainedIn, vtpEntityTable=vtpEntityTable, ServiceAffecting=ServiceAffecting, fwDataActivationReadyOnStandby=fwDataActivationReadyOnStandby, sonetSectionConfigTimMode=sonetSectionConfigTimMode, sonetSectionConfigSignalDegradePeriod=sonetSectionConfigSignalDegradePeriod, oduTcmAConfigTraceExpected=oduTcmAConfigTraceExpected, entityContainedIn=entityContainedIn, neStorageDescr=neStorageDescr, RestoreActivationCaps=RestoreActivationCaps, inventoryFirmwarePackageRev=inventoryFirmwarePackageRev, oduTcmAConfigSignalDegradePeriod=oduTcmAConfigSignalDegradePeriod, swVersionActiveOperatingSw=swVersionActiveOperatingSw, fsp3000=fsp3000, OtnPayloadType=OtnPayloadType, controlPlaneEthEntityTable=controlPlaneEthEntityTable, snmpProxyServerSynchroState=snmpProxyServerSynchroState, transportStandards=transportStandards, controlPlaneEthEntityClass=controlPlaneEthEntityClass, snmpWriteAccessNmsName=snmpWriteAccessNmsName, oduSectionConfigTraceTransmitOpsp=oduSectionConfigTraceTransmitOpsp, ApsHoldoffTimeCaps=ApsHoldoffTimeCaps, software=software, PYSNMP_MODULE_ID=advaMIB, neRestoreConfig=neRestoreConfig, controlPlaneWdmEntityClass=controlPlaneWdmEntityClass, AssignmentState=AssignmentState, neStorageTable=neStorageTable, oduTcmBConfigTraceTransmitSapi=oduTcmBConfigTraceTransmitSapi, snmpServerPort=snmpServerPort, oduTcmAConfigSignalDegradeThreshold=oduTcmAConfigSignalDegradeThreshold, controlPlaneWdmEntityContainedIn=controlPlaneWdmEntityContainedIn, oduConfig=oduConfig, otuSectionDataResultingTotalBitrate=otuSectionDataResultingTotalBitrate, ptpEntityContainedIn=ptpEntityContainedIn, neAutoBackupServerAddress=neAutoBackupServerAddress, FileArea=FileArea, PgmType=PgmType, vtpEntityIndexAid=vtpEntityIndexAid, otuSectionDataTraceReceivedDapi=otuSectionDataTraceReceivedDapi, oduTcmADataTraceReceivedSapi=oduTcmADataTraceReceivedSapi, controlPlaneEthContainsIndex=controlPlaneEthContainsIndex, eqpFwNcuServerBusy=eqpFwNcuServerBusy, controlPlaneOtnEntityAssignmentState=controlPlaneOtnEntityAssignmentState, oduTcmBConfigTraceExpected=oduTcmBConfigTraceExpected, TrapCounter=TrapCounter, neStorageCapacity=neStorageCapacity, EnableState=EnableState, fwDataNewVersion=fwDataNewVersion, containsTable=containsTable, SonetSectSigDegThresCaps=SonetSectSigDegThresCaps, EntityClass=EntityClass, neEventLogVarCounter64Val=neEventLogVarCounter64Val, swDbDataNumNativeSaUpdate=swDbDataNumNativeSaUpdate, controlPlaneEthContainsEntry=controlPlaneEthContainsEntry, SnmpProxySynchronizationState=SnmpProxySynchronizationState, neEventLogVarId=neEventLogVarId, oduTcmAConfigTable=oduTcmAConfigTable, swDbFileFileName=swDbFileFileName, F7FileTimeStamp=F7FileTimeStamp, fwDataFirmwarePackageRevBackup=fwDataFirmwarePackageRevBackup, sonetSectionConfigTraceTransmit=sonetSectionConfigTraceTransmit, FspR7AdminStateSnmpProxyCaps=FspR7AdminStateSnmpProxyCaps, vtpEntityContainedIn=vtpEntityContainedIn, ncuScheduledActivation=ncuScheduledActivation, snmpProxyServerAdminState=snmpProxyServerAdminState, NeSwUpgradeStatusType=NeSwUpgradeStatusType, oduTcmCConfigEntry=oduTcmCConfigEntry, neBackupRestore=neBackupRestore, otuSectionConfigTable=otuSectionConfigTable, RestoreActivation=RestoreActivation, otuSectionDataTraceReceivedSapi=otuSectionDataTraceReceivedSapi, ModuleForm=ModuleForm, swDbDataDefaultsTable=swDbDataDefaultsTable, EntityIndex=EntityIndex, neF7AutomaticRemoteBackupUsers=neF7AutomaticRemoteBackupUsers, snmpProxyEntrySingleTargetOutEntry=snmpProxyEntrySingleTargetOutEntry, oduTcmADataTraceReceivedOpsp=oduTcmADataTraceReceivedOpsp, neSwUpgradeType=neSwUpgradeType, DestinationNodeOrAgentState=DestinationNodeOrAgentState, snmpProxyEntrySingleTargetOutPort=snmpProxyEntrySingleTargetOutPort, neStorageIndex=neStorageIndex, oduTcmBConfigSignalDegradeThreshold=oduTcmBConfigSignalDegradeThreshold, neStorageEntry=neStorageEntry, FspTime=FspTime, fwDataForm=fwDataForm, otuSectionConfigPayload=otuSectionConfigPayload, neAutoBackupConfig=neAutoBackupConfig, ptpEntityReferencedTo=ptpEntityReferencedTo, YesNoNA=YesNoNA, entityIndex=entityIndex, Grade=Grade, neMemorySizeTotal=neMemorySizeTotal, common=common, oduTcmADataTraceReceivedDapi=oduTcmADataTraceReceivedDapi, fsp2000=fsp2000, sonetSectionDataEntry=sonetSectionDataEntry, updateEqpt=updateEqpt, swVersionTable=swVersionTable, oduTcmCConfigTraceExpected=oduTcmCConfigTraceExpected, swDbFileVersion=swDbFileVersion, neAlarmStatus=neAlarmStatus, fwDataFirmwareAvailable=fwDataFirmwareAvailable, OtnTcmLevel=OtnTcmLevel, SonetTimingSource=SonetTimingSource, neSwUpgradeTransferProtocol=neSwUpgradeTransferProtocol, ncuActivationTimeUtc=ncuActivationTimeUtc, oduTcmAConfigTraceTransmitSapi=oduTcmAConfigTraceTransmitSapi, oduSectionDataTraceReceivedOpsp=oduSectionDataTraceReceivedOpsp, swDbDataEntry=swDbDataEntry, oduTcmAConfigTimMode=oduTcmAConfigTimMode, oduTcmCConfigTraceTransmitSapi=oduTcmCConfigTraceTransmitSapi, controlPlaneOtnContainsTable=controlPlaneOtnContainsTable, fwDataBootStatus=fwDataBootStatus, oduTcmBDataTraceReceivedOpsp=oduTcmBDataTraceReceivedOpsp, aos=aos, controlPlaneWdmEntityClassInstanceNumber=controlPlaneWdmEntityClassInstanceNumber, oduTcmBConfigEntry=oduTcmBConfigEntry, neEventLogTimeStamp=neEventLogTimeStamp, snmpProxyEntrySingleTargetOutTable=snmpProxyEntrySingleTargetOutTable, SonetTraceFormCaps=SonetTraceFormCaps, inventoryGradeInventory=inventoryGradeInventory, snmpProxyEntrySingleTargetOutAddress=snmpProxyEntrySingleTargetOutAddress, neManufacturer=neManufacturer, neF7AutomaticRemoteBackupProtocol=neF7AutomaticRemoteBackupProtocol, ProtectionMechCaps=ProtectionMechCaps, FspDate=FspDate, installedEqpt=installedEqpt, swVersionEntry=swVersionEntry, snmpProxyEntrySingleTargetOutUserName=snmpProxyEntrySingleTargetOutUserName, SonetTraceForm=SonetTraceForm, swDbFilePgmType=swDbFilePgmType, snmpProxyEntrySingleTargetOutNodeAgentStatus=snmpProxyEntrySingleTargetOutNodeAgentStatus, coldRestartCapEntry=coldRestartCapEntry, OhTerminationLevelCaps=OhTerminationLevelCaps, FspR7YesNo=FspR7YesNo, neF7AutomaticRemoteBackupSrvLogin=neF7AutomaticRemoteBackupSrvLogin, EnableStateCaps=EnableStateCaps, controlPlaneOtnEntityClass=controlPlaneOtnEntityClass, snmpWriteAccessEntry=snmpWriteAccessEntry, fwDataProtectionPart=fwDataProtectionPart, selectedFile=selectedFile, neF7AutomaticRemoteBackupSrvDir=neF7AutomaticRemoteBackupSrvDir, controlPlaneOtnEntityTable=controlPlaneOtnEntityTable, oduTcmBConfigSignalDegradePeriod=oduTcmBConfigSignalDegradePeriod, neSwUpgradeServerAddress=neSwUpgradeServerAddress, ptpEntityClassInstanceNumber=ptpEntityClassInstanceNumber, neAutoBackupServerPasswd=neAutoBackupServerPasswd, neAutoBackup=neAutoBackup, snmpProxyServerPort=snmpProxyServerPort, swDbDataCapRestoreConfig=swDbDataCapRestoreConfig, provContainerEntry=provContainerEntry, neDateAndTime=neDateAndTime, neEventLogVarUnsigned32Val=neEventLogVarUnsigned32Val, LogicalIfTransport=LogicalIfTransport, neF7AutomaticRemoteBackupSrvIp=neF7AutomaticRemoteBackupSrvIp, LoopConfig=LoopConfig, sonetSectionDataTraceReceived=sonetSectionDataTraceReceived, swDbDataCapUpgradeRequest=swDbDataCapUpgradeRequest, oduTcmBDataEntry=oduTcmBDataEntry, neTrapsinkType=neTrapsinkType, otuSectionConfigTraceTransmitSapi=otuSectionConfigTraceTransmitSapi, oduTcmBDataTraceReceivedDapi=oduTcmBDataTraceReceivedDapi, sonet=sonet, ApsHoldoffTime=ApsHoldoffTime, entityEntry=entityEntry, neRestoreFileBackupDate=neRestoreFileBackupDate, fsp150=fsp150, vtpEntityClass=vtpEntityClass, CommandEqpt=CommandEqpt, swDbDataIndex=swDbDataIndex, fsp1000=fsp1000, neAutoBackupServerDirectory=neAutoBackupServerDirectory, oduSectionDataEntry=oduSectionDataEntry, swDbDataCapTable=swDbDataCapTable, neTrapsinkUserName=neTrapsinkUserName, eqpFwUpgradeRequest=eqpFwUpgradeRequest, controlPlaneWdmContainsTable=controlPlaneWdmContainsTable, AvailState=AvailState, otuSectionDataEntry=otuSectionDataEntry, neF7AutomaticBackupEntry=neF7AutomaticBackupEntry, oduTcmCDataTraceReceivedOpsp=oduTcmCDataTraceReceivedOpsp, swAdmin=swAdmin, FspR7FalseTrue=FspR7FalseTrue, SonetVcBundleAllocationCaps=SonetVcBundleAllocationCaps, containsEntry=containsEntry, inventoryEntry=inventoryEntry, inventoryCleiCode=inventoryCleiCode, neEventLogNotificationOID=neEventLogNotificationOID, swDbDataNumLegacyUpdate=swDbDataNumLegacyUpdate, neTrapsinkEntry=neTrapsinkEntry, swDbDataNumNativeNsaUpdate=swDbDataNumNativeNsaUpdate, CpWdmEntityClass=CpWdmEntityClass, neF7AutomaticBackupTable=neF7AutomaticBackupTable, controlPlaneOtnContainsIndex=controlPlaneOtnContainsIndex, oduTcmBDataTable=oduTcmBDataTable, ncuActivationDate=ncuActivationDate, fwDataTable=fwDataTable, oduTcmBConfigTcmLevel=oduTcmBConfigTcmLevel, neF7AutomaticBackupStartTime=neF7AutomaticBackupStartTime, inventoryType=inventoryType, ncuScheduledDbRestore=ncuScheduledDbRestore, swVersionInactiveApplSw=swVersionInactiveApplSw, oduTcmBDataTraceReceivedSapi=oduTcmBDataTraceReceivedSapi, controlPlaneWdmEntityEntry=controlPlaneWdmEntityEntry, swDbDataActivationTime=swDbDataActivationTime, entityClass=entityClass, entityClassInstanceNumber=entityClassInstanceNumber, otuSectionConfigSignalDegradePeriod=otuSectionConfigSignalDegradePeriod, inventoryFpgaRev=inventoryFpgaRev, ApsDirection=ApsDirection, ptpEntityType=ptpEntityType)
mibBuilder.exportSymbols("ADVA-MIB", updateBackupRestoreMib=updateBackupRestoreMib, otuSectionDataTraceReceivedOpsp=otuSectionDataTraceReceivedOpsp, sonetSectionConfigTraceExpected=sonetSectionConfigTraceExpected, coldRestartCapServiceAffectingCap=coldRestartCapServiceAffectingCap, snmpProxyEntrySingleTargetOutAdminState=snmpProxyEntrySingleTargetOutAdminState, controlPlaneEthContainsTable=controlPlaneEthContainsTable, FspR7UsersDb=FspR7UsersDb, sonetSectionConfigTable=sonetSectionConfigTable, ptpEntityIndexAid=ptpEntityIndexAid, ptpEntityAssignmentState=ptpEntityAssignmentState, provAssignmentState=provAssignmentState, vtpEntityAssignmentState=vtpEntityAssignmentState, fwDataFirmwareApproved=fwDataFirmwareApproved, swDbDataNumSaNotReady=swDbDataNumSaNotReady, FileTransferProtocol=FileTransferProtocol, neBackupRestoreRequest=neBackupRestoreRequest, otuSectionDataTable=otuSectionDataTable, FspR7TrapsinkLifetime=FspR7TrapsinkLifetime, vtpEntityEquipmentState=vtpEntityEquipmentState, fsp3000alm=fsp3000alm, EthDuplexModeCaps=EthDuplexModeCaps, swDbDataNumLegacyEqpt=swDbDataNumLegacyEqpt, advaMIB=advaMIB, controlPlaneOtnContainsEntry=controlPlaneOtnContainsEntry, swDbDataDefaultsRestoreConfig=swDbDataDefaultsRestoreConfig, SonetSectSigDegThres=SonetSectSigDegThres, neMemorySizeFree=neMemorySizeFree, inventoryCfModel=inventoryCfModel, swDbFileRowStatus=swDbFileRowStatus, TimModeCaps=TimModeCaps, ptpEntityClass=ptpEntityClass, IdentityTranslation=IdentityTranslation, oduTcmCConfigSignalDegradeThreshold=oduTcmCConfigSignalDegradeThreshold, FileType=FileType, F7AutoBackupRunState=F7AutoBackupRunState, OtnPayloadTypeCaps=OtnPayloadTypeCaps, oduSectionDataTable=oduSectionDataTable, neBackupRestoreState=neBackupRestoreState, swDbFileTable=swDbFileTable, sonetSectionDataTable=sonetSectionDataTable, entityAssignmentState=entityAssignmentState, controlPlaneEthEntityEntry=controlPlaneEthEntityEntry, otuSectionConfigTraceTransmitDapi=otuSectionConfigTraceTransmitDapi, FspR7AdminStateSnmpProxy=FspR7AdminStateSnmpProxy, NeSwInstallStatusType=NeSwInstallStatusType, neAutoBackupInterval=neAutoBackupInterval, oduTcmCConfigTimMode=oduTcmCConfigTimMode, ApsDirectionCaps=ApsDirectionCaps, neEventLogVarIndex=neEventLogVarIndex, neEventLogVarOidVal=neEventLogVarOidVal, swDbDataTable=swDbDataTable, neBackupPassword=neBackupPassword, oduSectionConfigSignalDegradePeriod=oduSectionConfigSignalDegradePeriod, ptpEntityEntry=ptpEntityEntry, fsp150cm=fsp150cm, otuSectionConfigStuffing=otuSectionConfigStuffing, neEventLogEntry=neEventLogEntry, sourceIpAddress=sourceIpAddress, inventoryTable=inventoryTable, neEventsLogged=neEventsLogged, swDbDataNumEqpt=swDbDataNumEqpt, controlPlaneEthEntityIndexAid=controlPlaneEthEntityIndexAid, TimMode=TimMode, OtnTcmLevelCaps=OtnTcmLevelCaps, VirtualContainerTypeCaps=VirtualContainerTypeCaps, oduTcmCDataTable=oduTcmCDataTable, controlPlaneOtnEntityClassInstanceNumber=controlPlaneOtnEntityClassInstanceNumber, oduTcmBConfigTraceTransmitOpsp=oduTcmBConfigTraceTransmitOpsp, neSwUpgradeNeDirectory=neSwUpgradeNeDirectory, neEventLogVarInteger32Val=neEventLogVarInteger32Val, oduTcmAConfigTraceTransmitDapi=oduTcmAConfigTraceTransmitDapi, neF7AutomaticRemoteBackupEncryption=neF7AutomaticRemoteBackupEncryption, FspR7Date=FspR7Date, F7AutoBackupInterval=F7AutoBackupInterval, controlPlaneWdmEntityTable=controlPlaneWdmEntityTable, NoYesNA=NoYesNA, neSwUpgradeState=neSwUpgradeState, neF7AutomaticRemoteBackupSrcIp=neF7AutomaticRemoteBackupSrcIp, oduTcmBConfigTable=oduTcmBConfigTable, VirtualContainerType=VirtualContainerType, neTrapsinkPort=neTrapsinkPort, neF7AutomaticBackupStartDate=neF7AutomaticBackupStartDate, ServiceImpairment=ServiceImpairment, sonetSectionConfigTraceForm=sonetSectionConfigTraceForm, entityType=entityType, neBackupUsers=neBackupUsers, neF7AutomaticRemoteBackupPassword=neF7AutomaticRemoteBackupPassword, inventoryUniversalSerialIdent=inventoryUniversalSerialIdent, otuConfig=otuConfig, fwDataReadyForActivation=fwDataReadyForActivation, oduSectionConfigTimMode=oduSectionConfigTimMode, fsp1500=fsp1500, LoopConfigCaps=LoopConfigCaps, controlPlaneWdmEntityIndex=controlPlaneWdmEntityIndex, fwDataFirmwarePackageRev=fwDataFirmwarePackageRev, oduTcmADataEntry=oduTcmADataEntry, fsp3000c=fsp3000c, swDbDataFirmwareSetVersion=swDbDataFirmwareSetVersion, oduSectionConfigSignalDegradeThres=oduSectionConfigSignalDegradeThres, snmpAgent=snmpAgent, sonetSectionConfigEntry=sonetSectionConfigEntry, entityIndexAid=entityIndexAid, neStorageAvailable=neStorageAvailable, neEventLogIndex=neEventLogIndex, neSwUpgradeServerPasswd=neSwUpgradeServerPasswd, encryptionFwpFile=encryptionFwpFile, aosCommon=aosCommon, swDbDataArea=swDbDataArea, controlPlaneEthEntityAssignmentState=controlPlaneEthEntityAssignmentState, oduTcmCDataTraceReceivedSapi=oduTcmCDataTraceReceivedSapi, neInitialConnectionMode=neInitialConnectionMode, FspR7Time=FspR7Time, neEventLogIdentityTranslation=neEventLogIdentityTranslation, clearRdiskRequest=clearRdiskRequest, neF7AutomaticBackupIndex=neF7AutomaticBackupIndex, neF7AutomaticBackupTimeStamp=neF7AutomaticBackupTimeStamp, oduTcmAConfigTraceTransmitOpsp=oduTcmAConfigTraceTransmitOpsp, fwDataStandbyVersion=fwDataStandbyVersion, inventoryMib=inventoryMib, eqpFwNextEqpForUpdate=eqpFwNextEqpForUpdate, ProtectionMech=ProtectionMech, neBackupEncryption=neBackupEncryption, products=products, swDbDataNcuSoftwareVersion=swDbDataNcuSoftwareVersion, otuSectionConfigSignalDegradeThreshold=otuSectionConfigSignalDegradeThreshold, oduSectionConfigEntry=oduSectionConfigEntry, SonetVcBundleAllocation=SonetVcBundleAllocation, controlPlaneWdmEntityIndexAid=controlPlaneWdmEntityIndexAid, oduTcmCDataEntry=oduTcmCDataEntry, Counter64String=Counter64String, neSoftwareUpgrade=neSoftwareUpgrade, controlPlaneWdmContainsIndex=controlPlaneWdmContainsIndex, inventoryHardwareRev=inventoryHardwareRev, controlPlaneEthEntityClassInstanceNumber=controlPlaneEthEntityClassInstanceNumber, entityEquipmentState=entityEquipmentState, ServiceAffectingCaps=ServiceAffectingCaps, EntityType=EntityType, oduTcmAConfigTcmLevel=oduTcmAConfigTcmLevel, ncuActivationDateUtc=ncuActivationDateUtc, FspR7EquipmentType=FspR7EquipmentType, snmpProxyEntrySingleTargetOutRowStatus=snmpProxyEntrySingleTargetOutRowStatus, fspR7=fspR7, OhTerminationLevel=OhTerminationLevel, otuSectionConfigTraceTransmitOpsp=otuSectionConfigTraceTransmitOpsp, ptpEntityEquipmentState=ptpEntityEquipmentState, otn=otn, neSwInstallState=neSwInstallState, neSwUpgradeRequest=neSwUpgradeRequest, swDbFileEntry=swDbFileEntry, snmpProxyEntrySingleTargetOutContext=snmpProxyEntrySingleTargetOutContext, events=events, oduTcmCConfigTraceTransmitDapi=oduTcmCConfigTraceTransmitDapi, ArcState=ArcState, neAutoBackupNextActionAt=neAutoBackupNextActionAt, neSwUpgradeServerLogin=neSwUpgradeServerLogin, provContainerTable=provContainerTable, provEquipmentState=provEquipmentState, inventoryVendorId=inventoryVendorId, coldRestartCapTable=coldRestartCapTable, controlPlaneWdmContainsEntry=controlPlaneWdmContainsEntry, entityTable=entityTable, neEventLogVarTable=neEventLogVarTable, oduTcmBConfigTraceTransmitDapi=oduTcmBConfigTraceTransmitDapi, swVersionNextBoot=swVersionNextBoot, controlPlaneWdmEntityAssignmentState=controlPlaneWdmEntityAssignmentState, otuSectionConfigTraceExpected=otuSectionConfigTraceExpected, sonetConfig=sonetConfig, SonetTimingSourceCaps=SonetTimingSourceCaps, swDbFileArea=swDbFileArea, swDbDataCapEntry=swDbDataCapEntry, oduSectionDataTraceReceivedDapi=oduSectionDataTraceReceivedDapi, vtpEntityEntry=vtpEntityEntry, swDbFileCreationTime=swDbFileCreationTime, swDbDataProgramVersion=swDbDataProgramVersion, neF7AutomaticRemoteBackupCommonIpSrv=neF7AutomaticRemoteBackupCommonIpSrv, fsp1000adm=fsp1000adm, neTrapsinkRowStatus=neTrapsinkRowStatus, oduTcmCDataTraceReceivedDapi=oduTcmCDataTraceReceivedDapi, swDbFileSize=swDbFileSize, inventoryMacAddress=inventoryMacAddress, neBackupRestoreFile=neBackupRestoreFile, OnOff=OnOff, neTrapsinkTable=neTrapsinkTable, dbAdmin=dbAdmin, otuSectionConfigEntry=otuSectionConfigEntry, inventorySerialNum=inventorySerialNum, TrapAlarmSeverity=TrapAlarmSeverity, LogicalIfTransportCaps=LogicalIfTransportCaps, aosProducts=aosProducts, oduSectionDataTraceReceivedSapi=oduSectionDataTraceReceivedSapi, eqpFwEqpServerBusy=eqpFwEqpServerBusy, vtpEntityType=vtpEntityType, neSwUpgradeCommonIpSrv=neSwUpgradeCommonIpSrv, ncuActivationTime=ncuActivationTime, inventoryUnitName=inventoryUnitName, oduTcmCConfigTable=oduTcmCConfigTable, vtpEntityClassInstanceNumber=vtpEntityClassInstanceNumber, neSwUpgradeServerDirectory=neSwUpgradeServerDirectory, swDbDataDatabaseVersion=swDbDataDatabaseVersion, inventoryCfSerialNum=inventoryCfSerialNum, PartitionStatus=PartitionStatus, fwDataServiceImpairment=fwDataServiceImpairment, oduSectionConfigTable=oduSectionConfigTable, oduTcmADataTable=oduTcmADataTable, FspR7EnableDisable=FspR7EnableDisable, KBytes=KBytes, EquipmentState=EquipmentState, neTrapsinkAddress=neTrapsinkAddress, ptpEntityTable=ptpEntityTable, FspR7EquipmentTypeCaps=FspR7EquipmentTypeCaps, fwDataStandbyServiceImpairment=fwDataStandbyServiceImpairment, inventorySoftwareRev=inventorySoftwareRev, swVersionInactiveOperatingSw=swVersionInactiveOperatingSw, neF7AutomaticRemoteBackupTimeStamp=neF7AutomaticRemoteBackupTimeStamp, BootState=BootState, neEventLogTable=neEventLogTable, neEventLogVarType=neEventLogVarType, snmpWriteAccessRestriction=snmpWriteAccessRestriction, eqpFwServiceImpairment=eqpFwServiceImpairment, sonetSectionConfigSignalDegradeThreshhold=sonetSectionConfigSignalDegradeThreshhold, ptpEntityIndex=ptpEntityIndex, swDbDataDefaultsEntry=swDbDataDefaultsEntry, fwDataEntry=fwDataEntry, oduTcmAConfigEntry=oduTcmAConfigEntry, oduTcmCConfigTcmLevel=oduTcmCConfigTcmLevel, eqpFwEqpType=eqpFwEqpType, neSwDownloadProgress=neSwDownloadProgress, swDbFileGrade=swDbFileGrade, controlPlaneEthEntityIndex=controlPlaneEthEntityIndex, inventoryPartnumber=inventoryPartnumber, snmpWriteAccessTable=snmpWriteAccessTable, neAutoBackupServerLogin=neAutoBackupServerLogin, oduSectionConfigTraceTransmitSapi=oduSectionConfigTraceTransmitSapi, controlPlaneOtnEntityEntry=controlPlaneOtnEntityEntry, oduTcmCConfigSignalDegradePeriod=oduTcmCConfigSignalDegradePeriod, otuSectionConfigTimMode=otuSectionConfigTimMode)
