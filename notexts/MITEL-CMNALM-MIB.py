#
# PySNMP MIB module MITEL-CMNALM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mitel/MITEL-CMNALM-MIB
# Produced by pysmi-1.1.8 at Fri Jan 27 15:51:00 2023
# On host fv-az551-95 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
mitelConfGroups, mitelConfCompliances, mitelIdentification, mitelPropCommon = mibBuilder.importSymbols("MITEL-MIB", "mitelConfGroups", "mitelConfCompliances", "mitelIdentification", "mitelPropCommon")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Unsigned32, ObjectIdentity, Integer32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, MibIdentifier, Counter64, TimeTicks, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "ObjectIdentity", "Integer32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "MibIdentifier", "Counter64", "TimeTicks", "ModuleIdentity", "Bits")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
mitelCmnAlarms = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1))
mitelCmnAlarms.setRevisions(('2014-02-11 12:00', '2005-02-21 21:34', '2004-02-23 00:00',))
if mibBuilder.loadTexts: mitelCmnAlarms.setLastUpdated('201402111200Z')
if mibBuilder.loadTexts: mitelCmnAlarms.setOrganization('MITEL Networks Corporation')
class ItuPerceivedSeverity(TextualConvention, Integer32):
    reference = "ITU Recommendation M.3100, 'Generic Network Information Model', 1995 ITU Recommendation X.733, 'Information Technology - Open Systems Interconnection - System Management: Alarm Reporting Function', 1992"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6))

class MitelCmnAlarmThresholdType(TextualConvention, Integer32):
    reference = 'Mitel SNMP MIB Support Guide - DK113065'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("percentage", 1), ("absoluteValue", 2), ("indeterminate", 3))

mitelCmnAlmObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1))
if mibBuilder.loadTexts: mitelCmnAlmObjects.setStatus('current')
mitelCmnAlmNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 2))
if mibBuilder.loadTexts: mitelCmnAlmNotifications.setStatus('current')
mitelCmnAlmConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 3))
if mibBuilder.loadTexts: mitelCmnAlmConformance.setStatus('current')
mitelAlmSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1))
if mibBuilder.loadTexts: mitelAlmSystem.setStatus('current')
mitelAlmSysSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1, 1), ItuPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmSysSeverity.setStatus('current')
mitelAlmSysSeverityDetectTime = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmSysSeverityDetectTime.setStatus('current')
mitelAlmSysSeverityDescr = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmSysSeverityDescr.setStatus('current')
mitelAlmActiveTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2), )
if mibBuilder.loadTexts: mitelAlmActiveTable.setStatus('current')
mitelAlmActiveTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1), ).setIndexNames((0, "MITEL-CMNALM-MIB", "mitelAlmActiveTblIndex"))
if mibBuilder.loadTexts: mitelAlmActiveTableEntry.setStatus('current')
mitelAlmActiveTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblIndex.setStatus('current')
mitelAlmActiveTblClass = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblClass.setStatus('current')
mitelAlmActiveTblType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblType.setStatus('current')
mitelAlmActiveTblTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblTypeName.setStatus('current')
mitelAlmActiveTblSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 5), ItuPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblSeverity.setStatus('current')
mitelAlmActiveTblSeverityDetectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblSeverityDetectTime.setStatus('current')
mitelAlmActiveTblThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 7), MitelCmnAlarmThresholdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblThresholdType.setStatus('current')
mitelAlmActiveTblThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblThresholdValue.setStatus('current')
mitelAlmActiveTblDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 1, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAlmActiveTblDescr.setStatus('current')
mitelNotifActiveAlarm = NotificationType((1, 3, 6, 1, 4, 1, 1027, 4, 9, 1, 2, 1)).setObjects(("MITEL-CMNALM-MIB", "mitelAlmSysSeverity"), ("MITEL-CMNALM-MIB", "mitelAlmSysSeverityDetectTime"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblIndex"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblClass"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblType"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblTypeName"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblSeverity"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblThresholdType"), ("MITEL-CMNALM-MIB", "mitelAlmActiveTblThresholdValue"))
if mibBuilder.loadTexts: mitelNotifActiveAlarm.setStatus('current')
mibBuilder.exportSymbols("MITEL-CMNALM-MIB", mitelAlmActiveTblThresholdType=mitelAlmActiveTblThresholdType, mitelAlmActiveTblType=mitelAlmActiveTblType, mitelAlmSysSeverityDetectTime=mitelAlmSysSeverityDetectTime, ItuPerceivedSeverity=ItuPerceivedSeverity, mitelAlmActiveTableEntry=mitelAlmActiveTableEntry, mitelAlmSysSeverityDescr=mitelAlmSysSeverityDescr, mitelAlmSysSeverity=mitelAlmSysSeverity, mitelAlmSystem=mitelAlmSystem, mitelAlmActiveTblClass=mitelAlmActiveTblClass, PYSNMP_MODULE_ID=mitelCmnAlarms, mitelAlmActiveTblDescr=mitelAlmActiveTblDescr, mitelCmnAlarms=mitelCmnAlarms, mitelAlmActiveTblThresholdValue=mitelAlmActiveTblThresholdValue, MitelCmnAlarmThresholdType=MitelCmnAlarmThresholdType, mitelAlmActiveTable=mitelAlmActiveTable, mitelCmnAlmObjects=mitelCmnAlmObjects, mitelAlmActiveTblIndex=mitelAlmActiveTblIndex, mitelCmnAlmNotifications=mitelCmnAlmNotifications, mitelCmnAlmConformance=mitelCmnAlmConformance, mitelAlmActiveTblTypeName=mitelAlmActiveTblTypeName, mitelAlmActiveTblSeverity=mitelAlmActiveTblSeverity, mitelAlmActiveTblSeverityDetectTime=mitelAlmActiveTblSeverityDetectTime, mitelNotifActiveAlarm=mitelNotifActiveAlarm)
