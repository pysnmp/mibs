#
# PySNMP MIB module PRVT-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-ALARM-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:20:47 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
software, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "software")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Gauge32, Unsigned32, NotificationType, iso, Bits, Counter32, ObjectIdentity, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Gauge32", "Unsigned32", "NotificationType", "iso", "Bits", "Counter32", "ObjectIdentity", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtAlarmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 111, 4))
prvtAlarmMIB.setRevisions(('2013-03-25 00:00',))
if mibBuilder.loadTexts: prvtAlarmMIB.setLastUpdated('201303250000Z')
if mibBuilder.loadTexts: prvtAlarmMIB.setOrganization('BATM Advanced Communication')
prvtAlarmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 111, 4, 1))
prvtUpdatedCurrentAlarmCounter = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 111, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtUpdatedCurrentAlarmCounter.setStatus('current')
prvtAlarmCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 111, 4, 1, 2), )
if mibBuilder.loadTexts: prvtAlarmCurrentTable.setStatus('current')
prvtAlarmCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 111, 4, 1, 2, 1), ).setIndexNames((0, "PRVT-ALARM-MIB", "prvtAlarmCurrentCounter"))
if mibBuilder.loadTexts: prvtAlarmCurrentEntry.setStatus('current')
prvtAlarmCurrentCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 111, 4, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtAlarmCurrentCounter.setStatus('current')
prvtAlarmCurrentRaisedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 111, 4, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtAlarmCurrentRaisedTime.setStatus('current')
prvtAlarmCurrentSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 111, 4, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 99))).clone(namedValues=NamedValues(("clear", 0), ("event", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtAlarmCurrentSeverity.setStatus('current')
prvtAlarmCurrentDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 111, 4, 1, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtAlarmCurrentDescription.setStatus('current')
mibBuilder.exportSymbols("PRVT-ALARM-MIB", prvtAlarmCurrentCounter=prvtAlarmCurrentCounter, prvtAlarmMIBObjects=prvtAlarmMIBObjects, prvtAlarmCurrentDescription=prvtAlarmCurrentDescription, prvtUpdatedCurrentAlarmCounter=prvtUpdatedCurrentAlarmCounter, prvtAlarmMIB=prvtAlarmMIB, prvtAlarmCurrentEntry=prvtAlarmCurrentEntry, prvtAlarmCurrentSeverity=prvtAlarmCurrentSeverity, PYSNMP_MODULE_ID=prvtAlarmMIB, prvtAlarmCurrentTable=prvtAlarmCurrentTable, prvtAlarmCurrentRaisedTime=prvtAlarmCurrentRaisedTime)
