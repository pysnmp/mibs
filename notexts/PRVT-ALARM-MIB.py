#
# PySNMP MIB module PRVT-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-ALARM-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 14:00:47 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
software, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "software")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Integer32, ObjectIdentity, Counter32, Gauge32, iso, IpAddress, MibIdentifier, TimeTicks, ModuleIdentity, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Integer32", "ObjectIdentity", "Counter32", "Gauge32", "iso", "IpAddress", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Counter64", "Bits")
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
mibBuilder.exportSymbols("PRVT-ALARM-MIB", prvtAlarmCurrentRaisedTime=prvtAlarmCurrentRaisedTime, prvtUpdatedCurrentAlarmCounter=prvtUpdatedCurrentAlarmCounter, prvtAlarmCurrentDescription=prvtAlarmCurrentDescription, prvtAlarmMIB=prvtAlarmMIB, prvtAlarmCurrentSeverity=prvtAlarmCurrentSeverity, prvtAlarmMIBObjects=prvtAlarmMIBObjects, prvtAlarmCurrentTable=prvtAlarmCurrentTable, prvtAlarmCurrentCounter=prvtAlarmCurrentCounter, PYSNMP_MODULE_ID=prvtAlarmMIB, prvtAlarmCurrentEntry=prvtAlarmCurrentEntry)
