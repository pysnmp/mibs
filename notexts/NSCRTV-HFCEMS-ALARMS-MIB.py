#
# PySNMP MIB module NSCRTV-HFCEMS-ALARMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/glassway/NSCRTV-HFCEMS-ALARMS-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 17:47:50 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
commonPhysAddress, commonNELogicalID = mibBuilder.importSymbols("NSCRTV-HFCEMS-COMMON-MIB", "commonPhysAddress", "commonNELogicalID")
nscrtvHFCemsTree, alarmsIdent = mibBuilder.importSymbols("NSCRTV-ROOT", "nscrtvHFCemsTree", "alarmsIdent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Integer32, iso, Counter32, NotificationType, Gauge32, Counter64, Unsigned32, IpAddress, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Integer32", "iso", "Counter32", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alarmLogNumberOfEntries = MibScalar((1, 3, 6, 1, 4, 1, 17409, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogNumberOfEntries.setStatus('mandatory')
alarmLogLastIndex = MibScalar((1, 3, 6, 1, 4, 1, 17409, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogLastIndex.setStatus('mandatory')
alarmLogTable = MibTable((1, 3, 6, 1, 4, 1, 17409, 1, 2, 3), )
if mibBuilder.loadTexts: alarmLogTable.setStatus('mandatory')
alarmLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17409, 1, 2, 3, 1), ).setIndexNames((0, "NSCRTV-HFCEMS-ALARMS-MIB", "alarmLogIndex"))
if mibBuilder.loadTexts: alarmLogEntry.setStatus('mandatory')
alarmLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogIndex.setStatus('mandatory')
alarmLogInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 17409, 1, 2, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(17, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogInformation.setStatus('mandatory')
alarmText = MibScalar((1, 3, 6, 1, 4, 1, 17409, 1, 2, 4), DisplayString())
if mibBuilder.loadTexts: alarmText.setStatus('optional')
hfcAlarmEvent = NotificationType((1, 3, 6, 1, 4, 1, 17409, 1) + (0,1)).setObjects(("NSCRTV-HFCEMS-COMMON-MIB", "commonPhysAddress"), ("NSCRTV-HFCEMS-COMMON-MIB", "commonNELogicalID"), ("NSCRTV-HFCEMS-ALARMS-MIB", "alarmLogInformation"), ("NSCRTV-HFCEMS-ALARMS-MIB", "alarmText"))
mibBuilder.exportSymbols("NSCRTV-HFCEMS-ALARMS-MIB", alarmText=alarmText, alarmLogNumberOfEntries=alarmLogNumberOfEntries, hfcAlarmEvent=hfcAlarmEvent, alarmLogEntry=alarmLogEntry, alarmLogLastIndex=alarmLogLastIndex, alarmLogIndex=alarmLogIndex, alarmLogTable=alarmLogTable, alarmLogInformation=alarmLogInformation)
