#
# PySNMP MIB module AT-G8032v2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-G8032v2-MIB
# Produced by pysmi-1.1.3 at Tue Nov 30 02:34:04 2021
# On host fv-az33-471 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Counter32, NotificationType, Unsigned32, MibIdentifier, IpAddress, TimeTicks, Counter64, ObjectIdentity, Bits, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter32", "NotificationType", "Unsigned32", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "ObjectIdentity", "Bits", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
atG8032v2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604))
atG8032v2.setRevisions(('2017-02-06 00:00', '2017-01-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atG8032v2.setRevisionsDescriptions(('Defined system alarm trap.', 'Initial Revision of this MIB module.',))
if mibBuilder.loadTexts: atG8032v2.setLastUpdated('201702060000Z')
if mibBuilder.loadTexts: atG8032v2.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: atG8032v2.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atG8032v2.setDescription('G.8032v2 Ethernet Ring Protection Switching.')
class AtG8032v2InstanceState(TextualConvention, Integer32):
    description = 'Defines the EPRS Instance states that are sent\n                in G8032 State Notification Traps.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("init", 2), ("idle", 3), ("protection", 4), ("manualSwitch", 5), ("forcedSwitch", 6), ("pending", 7))

atG8032v2Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 0))
atG8032v2InstanceNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 0, 1)).setObjects(("AT-G8032v2-MIB", "atG8032v2NotificationInstanceName"), ("AT-G8032v2-MIB", "atG8032v2NotificationInstanceFromState"), ("AT-G8032v2-MIB", "atG8032v2NotificationInstanceCurrentState"))
if mibBuilder.loadTexts: atG8032v2InstanceNotify.setStatus('current')
if mibBuilder.loadTexts: atG8032v2InstanceNotify.setDescription('G8032 ERP Instance state transition notification.')
atG8032v2SystemAlarmNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 0, 2)).setObjects(("AT-G8032v2-MIB", "atG8032v2NotificationSystemAlarmState"))
if mibBuilder.loadTexts: atG8032v2SystemAlarmNotify.setStatus('current')
if mibBuilder.loadTexts: atG8032v2SystemAlarmNotify.setDescription('G8032 ERP system alarm transition notification.\n                 Indicates whether any ERP instance is in a\n                 state that is considered to be an alarm condition.')
atG8032v2NotificationVariable = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1))
atG8032v2NotificationInstanceName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 1), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atG8032v2NotificationInstanceName.setStatus('current')
if mibBuilder.loadTexts: atG8032v2NotificationInstanceName.setDescription('Assigned name of the G8032 ERP Instance.')
atG8032v2NotificationInstanceFromState = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 2), AtG8032v2InstanceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atG8032v2NotificationInstanceFromState.setStatus('current')
if mibBuilder.loadTexts: atG8032v2NotificationInstanceFromState.setDescription('Defined state that a G8032 ERP instance is transitioning from.')
atG8032v2NotificationInstanceCurrentState = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 3), AtG8032v2InstanceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atG8032v2NotificationInstanceCurrentState.setStatus('current')
if mibBuilder.loadTexts: atG8032v2NotificationInstanceCurrentState.setDescription('Defined current state that a G8032 ERP instance is transitioning to.')
atG8032v2NotificationSystemAlarmState = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atG8032v2NotificationSystemAlarmState.setStatus('current')
if mibBuilder.loadTexts: atG8032v2NotificationSystemAlarmState.setDescription('Has value of 1 (true) if one or more G8032 ERP instance(s) are\n                 in alarm state, else has value of 2 (false).')
mibBuilder.exportSymbols("AT-G8032v2-MIB", AtG8032v2InstanceState=AtG8032v2InstanceState, atG8032v2SystemAlarmNotify=atG8032v2SystemAlarmNotify, atG8032v2InstanceNotify=atG8032v2InstanceNotify, atG8032v2NotificationVariable=atG8032v2NotificationVariable, atG8032v2=atG8032v2, atG8032v2NotificationInstanceCurrentState=atG8032v2NotificationInstanceCurrentState, atG8032v2NotificationSystemAlarmState=atG8032v2NotificationSystemAlarmState, PYSNMP_MODULE_ID=atG8032v2, atG8032v2NotificationInstanceName=atG8032v2NotificationInstanceName, atG8032v2NotificationInstanceFromState=atG8032v2NotificationInstanceFromState, atG8032v2Notifications=atG8032v2Notifications)
