#
# PySNMP MIB module AT-G8032v2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-G8032v2-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 23:11:05 2022
# On host fv-az42-507 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
modules, DisplayStringUnsized = mibBuilder.importSymbols("AT-SMI-MIB", "modules", "DisplayStringUnsized")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, ObjectIdentity, Integer32, MibIdentifier, Gauge32, Unsigned32, Counter64, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "ObjectIdentity", "Integer32", "MibIdentifier", "Gauge32", "Unsigned32", "Counter64", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "iso")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
atG8032v2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604))
atG8032v2.setRevisions(('2017-02-06 00:00', '2017-01-17 00:00',))
if mibBuilder.loadTexts: atG8032v2.setLastUpdated('201702060000Z')
if mibBuilder.loadTexts: atG8032v2.setOrganization('Allied Telesis, Inc')
class AtG8032v2InstanceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("init", 2), ("idle", 3), ("protection", 4), ("manualSwitch", 5), ("forcedSwitch", 6), ("pending", 7))

atG8032v2Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 0))
atG8032v2InstanceNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 0, 1)).setObjects(("AT-G8032v2-MIB", "atG8032v2NotificationInstanceName"), ("AT-G8032v2-MIB", "atG8032v2NotificationInstanceFromState"), ("AT-G8032v2-MIB", "atG8032v2NotificationInstanceCurrentState"))
if mibBuilder.loadTexts: atG8032v2InstanceNotify.setStatus('current')
atG8032v2SystemAlarmNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 0, 2)).setObjects(("AT-G8032v2-MIB", "atG8032v2NotificationSystemAlarmState"))
if mibBuilder.loadTexts: atG8032v2SystemAlarmNotify.setStatus('current')
atG8032v2NotificationVariable = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1))
atG8032v2NotificationInstanceName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 1), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atG8032v2NotificationInstanceName.setStatus('current')
atG8032v2NotificationInstanceFromState = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 2), AtG8032v2InstanceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atG8032v2NotificationInstanceFromState.setStatus('current')
atG8032v2NotificationInstanceCurrentState = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 3), AtG8032v2InstanceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atG8032v2NotificationInstanceCurrentState.setStatus('current')
atG8032v2NotificationSystemAlarmState = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atG8032v2NotificationSystemAlarmState.setStatus('current')
mibBuilder.exportSymbols("AT-G8032v2-MIB", atG8032v2SystemAlarmNotify=atG8032v2SystemAlarmNotify, atG8032v2NotificationVariable=atG8032v2NotificationVariable, atG8032v2NotificationInstanceName=atG8032v2NotificationInstanceName, atG8032v2NotificationSystemAlarmState=atG8032v2NotificationSystemAlarmState, PYSNMP_MODULE_ID=atG8032v2, atG8032v2NotificationInstanceCurrentState=atG8032v2NotificationInstanceCurrentState, AtG8032v2InstanceState=AtG8032v2InstanceState, atG8032v2InstanceNotify=atG8032v2InstanceNotify, atG8032v2Notifications=atG8032v2Notifications, atG8032v2=atG8032v2, atG8032v2NotificationInstanceFromState=atG8032v2NotificationInstanceFromState)
