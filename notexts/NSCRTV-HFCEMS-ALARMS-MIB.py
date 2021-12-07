#
# PySNMP MIB module NSCRTV-HFCEMS-ALARMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/glassway/NSCRTV-HFCEMS-ALARMS-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 16:31:19 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
commonNELogicalID, commonPhysAddress = mibBuilder.importSymbols("NSCRTV-HFCEMS-COMMON-MIB", "commonNELogicalID", "commonPhysAddress")
alarmsIdent, nscrtvHFCemsTree = mibBuilder.importSymbols("NSCRTV-ROOT", "alarmsIdent", "nscrtvHFCemsTree")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, Bits, ModuleIdentity, NotificationType, ObjectIdentity, Unsigned32, MibIdentifier, NotificationType, IpAddress, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Bits", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Unsigned32", "MibIdentifier", "NotificationType", "IpAddress", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("NSCRTV-HFCEMS-ALARMS-MIB", alarmLogNumberOfEntries=alarmLogNumberOfEntries, alarmLogEntry=alarmLogEntry, alarmLogIndex=alarmLogIndex, alarmLogTable=alarmLogTable, alarmLogInformation=alarmLogInformation, hfcAlarmEvent=hfcAlarmEvent, alarmText=alarmText, alarmLogLastIndex=alarmLogLastIndex)
