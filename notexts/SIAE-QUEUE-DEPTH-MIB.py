#
# PySNMP MIB module SIAE-QUEUE-DEPTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-QUEUE-DEPTH-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 13:13:22 2024
# On host fv-az883-299 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
AlarmSeverityCode, AlarmStatus = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Integer32, iso, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, ObjectIdentity, Counter32, MibIdentifier, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Integer32", "iso", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "ObjectIdentity", "Counter32", "MibIdentifier", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SIAE-QUEUE-DEPTH-MIB", PYSNMP_MODULE_ID=queueDepth, qdProfileMismatchAlarm=qdProfileMismatchAlarm, DisplayString1024=DisplayString1024, qdProfileEntry=qdProfileEntry, qdProfileName=qdProfileName, qdActualProfile=qdActualProfile, qdProfileDescription=qdProfileDescription, qdProfileTable=qdProfileTable, qdProfileIndex=qdProfileIndex, queueDepth=queueDepth, queueDepthMibVersion=queueDepthMibVersion, qdProfileMismatchAlarmSeverityCode=qdProfileMismatchAlarmSeverityCode, qdProfileSelect=qdProfileSelect)
