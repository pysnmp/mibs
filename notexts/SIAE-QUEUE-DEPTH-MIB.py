#
# PySNMP MIB module SIAE-QUEUE-DEPTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-QUEUE-DEPTH-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:28:16 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, Bits, ModuleIdentity, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, iso, ObjectIdentity, Counter32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "Bits", "ModuleIdentity", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "iso", "ObjectIdentity", "Counter32", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
queueDepth = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 84))
queueDepth.setRevisions(('2014-05-20 00:00',))
if mibBuilder.loadTexts: queueDepth.setLastUpdated('201405200000Z')
if mibBuilder.loadTexts: queueDepth.setOrganization('SIAE MICROELETTRONICA spa')
class DisplayString1024(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

queueDepthMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queueDepthMibVersion.setStatus('current')
qdProfileTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2), )
if mibBuilder.loadTexts: qdProfileTable.setStatus('current')
qdProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1), ).setIndexNames((0, "SIAE-QUEUE-DEPTH-MIB", "qdProfileIndex"))
if mibBuilder.loadTexts: qdProfileEntry.setStatus('current')
qdProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qdProfileIndex.setStatus('current')
qdProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qdProfileName.setStatus('current')
qdProfileDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 2, 1, 3), DisplayString1024()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qdProfileDescription.setStatus('current')
qdProfileSelect = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 3), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qdProfileSelect.setStatus('current')
qdActualProfile = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qdActualProfile.setStatus('current')
qdProfileMismatchAlarm = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qdProfileMismatchAlarm.setStatus('current')
qdProfileMismatchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 84, 6), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qdProfileMismatchAlarmSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-QUEUE-DEPTH-MIB", queueDepth=queueDepth, queueDepthMibVersion=queueDepthMibVersion, qdProfileIndex=qdProfileIndex, DisplayString1024=DisplayString1024, qdProfileEntry=qdProfileEntry, qdActualProfile=qdActualProfile, PYSNMP_MODULE_ID=queueDepth, qdProfileName=qdProfileName, qdProfileMismatchAlarm=qdProfileMismatchAlarm, qdProfileDescription=qdProfileDescription, qdProfileSelect=qdProfileSelect, qdProfileMismatchAlarmSeverityCode=qdProfileMismatchAlarmSeverityCode, qdProfileTable=qdProfileTable)
