#
# PySNMP MIB module SIAE-QUEUE-DEPTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-QUEUE-DEPTH-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 12:10:19 2023
# On host fv-az407-692 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, ObjectIdentity, Gauge32, Counter64, IpAddress, NotificationType, ModuleIdentity, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ObjectIdentity", "Gauge32", "Counter64", "IpAddress", "NotificationType", "ModuleIdentity", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
queueDepth = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 84))
queueDepth.setRevisions(('2014-05-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: queueDepth.setRevisionsDescriptions(('Initial version 01.00.00.\n            ',))
if mibBuilder.loadTexts: queueDepth.setLastUpdated('201405200000Z')
if mibBuilder.loadTexts: queueDepth.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: queueDepth.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: queueDepth.setDescription('Queue depth management for SIAE equipments.\n            ')
class DisplayString1024(TextualConvention, OctetString):
    description = "Represents textual information taken from the NVT ASCII\n            character set, as defined in pages 4, 10-11 of RFC 854.\n\n            To summarize RFC 854, the NVT ASCII repertoire specifies:\n\n              - the use of character codes 0-127 (decimal)\n\n              - the graphics characters (32-126) are interpreted as\n                US ASCII\n\n              - NUL, LF, CR, BEL, BS, HT, VT and FF have the special\n                meanings specified in RFC 854\n\n              - the other 25 codes have no standard interpretation\n\n              - the sequence 'CR LF' means newline\n\n              - the sequence 'CR NUL' means carriage-return\n\n              - an 'LF' not preceded by a 'CR' means moving to the\n                same column on the next line.\n\n              - the sequence 'CR x' for any x other than LF or NUL is\n                illegal.  (Note that this also means that a string may\n                end with either 'CR LF' or 'CR NUL', but not with CR.)\n\n            Any object defined using this syntax may not exceed 255\n            characters in length."
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

queueDepthMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueDepthMibVersion.setStatus('current')
if mibBuilder.loadTexts: queueDepthMibVersion.setDescription('Numerical version of this module.\n                 The string version of this MIB have the following format:\n                    XX.YY.ZZ\n                 so, for example, the value 1 should be interpreted as 00.00.01\n                 and the value 10001 should be interpreted as 01.00.01.')
qdProfileTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2), )
if mibBuilder.loadTexts: qdProfileTable.setStatus('current')
if mibBuilder.loadTexts: qdProfileTable.setDescription('A list of queue depth profile entries. This table is useful \n             to show to the manager available profiles and its feature.')
qdProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1), ).setIndexNames((0, "SIAE-QUEUE-DEPTH-MIB", "qdProfileIndex"))
if mibBuilder.loadTexts: qdProfileEntry.setStatus('current')
if mibBuilder.loadTexts: qdProfileEntry.setDescription('An entry containing information about each queue depth settings\n             realized by a profile.')
qdProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qdProfileIndex.setStatus('current')
if mibBuilder.loadTexts: qdProfileIndex.setDescription('A unique value, greater than zero, for each queue depth profile.\n             It is recommended that values are assigned contiguously \n             starting from 1.')
qdProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qdProfileName.setStatus('current')
if mibBuilder.loadTexts: qdProfileName.setDescription('A brief description of the settings realized by this profile.')
qdProfileDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1, 3), DisplayString1024()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qdProfileDescription.setStatus('current')
if mibBuilder.loadTexts: qdProfileDescription.setDescription('A detailed description of the settings realized by this profile.')
qdProfileSelect = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 3), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qdProfileSelect.setStatus('current')
if mibBuilder.loadTexts: qdProfileSelect.setDescription('This object selects a queue depth profile from qdProfileTable\n             to be applied after a cold restart.')
qdActualProfile = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qdActualProfile.setStatus('current')
if mibBuilder.loadTexts: qdActualProfile.setDescription('This object shows the actual queue profile in use.\n             The object content is set upon restart equal to qdProfileSelect\n             and is never changed, since a new profile will be applied after\n             a next cold restart. The value 0 means the actual profile is\n             unknown.')
qdProfileMismatchAlarm = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qdProfileMismatchAlarm.setStatus('current')
if mibBuilder.loadTexts: qdProfileMismatchAlarm.setDescription('This alarm is raise when the actual profile is not equal to the\n             selected profile.')
qdProfileMismatchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 6), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qdProfileMismatchAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: qdProfileMismatchAlarmSeverityCode.setDescription('Defines the severity associated to the qdProfileMismatchAlarm\n             and enables/disables the trap generation on status change event.')
mibBuilder.exportSymbols("SIAE-QUEUE-DEPTH-MIB", qdActualProfile=qdActualProfile, qdProfileMismatchAlarmSeverityCode=qdProfileMismatchAlarmSeverityCode, queueDepth=queueDepth, qdProfileIndex=qdProfileIndex, PYSNMP_MODULE_ID=queueDepth, qdProfileDescription=qdProfileDescription, DisplayString1024=DisplayString1024, queueDepthMibVersion=queueDepthMibVersion, qdProfileEntry=qdProfileEntry, qdProfileTable=qdProfileTable, qdProfileName=qdProfileName, qdProfileSelect=qdProfileSelect, qdProfileMismatchAlarm=qdProfileMismatchAlarm)
