#
# PySNMP MIB module AT-ALMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-ALMMON-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 11:36:46 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
DisplayStringUnsized, = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Gauge32, MibIdentifier, iso, Integer32, NotificationType, ObjectIdentity, IpAddress, Counter32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Gauge32", "MibIdentifier", "iso", "Integer32", "NotificationType", "ObjectIdentity", "IpAddress", "Counter32", "Counter64", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atAlmMon = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26))
atAlmMon.setRevisions(('2017-02-08 00:00', '2014-05-12 00:15', '2013-12-13 11:46',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atAlmMon.setRevisionsDescriptions(('Added g8032 as an alarm type.', 'Changes from maintainer review', 'Initial Revision',))
if mibBuilder.loadTexts: atAlmMon.setLastUpdated('201702080000Z')
if mibBuilder.loadTexts: atAlmMon.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: atAlmMon.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atAlmMon.setDescription('The AT Alarm Monitoring MIB for managing and\n                reporting device alarms.')
class AtAlmMonAlarmType(TextualConvention, Integer32):
    description = 'Indicates the type of a monitored alarm.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("alarmTypeInvalid", 0), ("externalPSU", 1), ("epsr", 2), ("contactInput", 3), ("portLinkDown", 4), ("loopDetect", 5), ("mainPse", 6), ("portPoeFailure", 7), ("temperature", 8), ("g8032", 9))

class AtAlmMonActionUseOutput(TextualConvention, Integer32):
    description = 'Indicates whether or not the output device (relay or fault LED) is used for this alarm.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unused", 1), ("used", 2))

class AtAlmMonAbnormalState(TextualConvention, Integer32):
    description = 'Indicates the abnormal (i.e. alarm active) state for a contact input alarm monitor.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("open", 1), ("closed", 2))

class AtAlmMonActionState(TextualConvention, Integer32):
    description = 'Indicates the current state of this alarm monitor.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inactive", 1), ("active", 2))

atAlmMonActionTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1), )
if mibBuilder.loadTexts: atAlmMonActionTable.setStatus('current')
if mibBuilder.loadTexts: atAlmMonActionTable.setDescription('A table of information describing alarm monitoring inputs\n                and consequent actions (i.e. fault LED & relay outputs).')
atAlmMonActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1), ).setIndexNames((0, "AT-ALMMON-MIB", "atAlmMonActionStackMemberId"), (0, "AT-ALMMON-MIB", "atAlmMonActionIndex"))
if mibBuilder.loadTexts: atAlmMonActionEntry.setStatus('current')
if mibBuilder.loadTexts: atAlmMonActionEntry.setDescription('The description and configuration of what to do for a specific monitored alarm.')
atAlmMonActionStackMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonActionStackMemberId.setStatus('current')
if mibBuilder.loadTexts: atAlmMonActionStackMemberId.setDescription('The index of the stack member of this alarm action.')
atAlmMonActionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonActionIndex.setStatus('current')
if mibBuilder.loadTexts: atAlmMonActionIndex.setDescription('The numeric identifier of this alarm action.')
atAlmMonAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 3), AtAlmMonAlarmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonAlarmType.setStatus('current')
if mibBuilder.loadTexts: atAlmMonAlarmType.setDescription('The type of alarm that this action monitors.')
atAlmMonAlarmTypeSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonAlarmTypeSelection.setStatus('current')
if mibBuilder.loadTexts: atAlmMonAlarmTypeSelection.setDescription('The 1-based index of the alarm of the particular type (as catagorised by atAlmMonAlarmType).')
atAlmMonActionDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 5), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonActionDescription.setStatus('current')
if mibBuilder.loadTexts: atAlmMonActionDescription.setDescription('The description of this alarm monitoring entry.')
atAlmMonActionUseRelay1 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 6), AtAlmMonActionUseOutput()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atAlmMonActionUseRelay1.setStatus('current')
if mibBuilder.loadTexts: atAlmMonActionUseRelay1.setDescription('Indicates/controls whether or not this alarm monitor drives the first relay output.')
atAlmMonActionUseRelay2 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 7), AtAlmMonActionUseOutput()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atAlmMonActionUseRelay2.setStatus('current')
if mibBuilder.loadTexts: atAlmMonActionUseRelay2.setDescription('Indicates/controls whether or not this alarm monitor drives the second relay output.')
atAlmMonActionUseRelay3 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 8), AtAlmMonActionUseOutput()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atAlmMonActionUseRelay3.setStatus('current')
if mibBuilder.loadTexts: atAlmMonActionUseRelay3.setDescription('Indicates/controls whether or not this alarm monitor drives the third relay output.')
atAlmMonActionUseFaultLed = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 9), AtAlmMonActionUseOutput()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atAlmMonActionUseFaultLed.setStatus('current')
if mibBuilder.loadTexts: atAlmMonActionUseFaultLed.setDescription('Indicates/controls whether or not this alarm monitor drives the fault LED.')
atAlmMonAbnormalState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 10), AtAlmMonAbnormalState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atAlmMonAbnormalState.setStatus('current')
if mibBuilder.loadTexts: atAlmMonAbnormalState.setDescription('Indicates/sets the abnormal (i.e. alarm active) state for a contact input.\n                 Only used for contactInput alarm monitors, ignored for all other types.')
atAlmMonActionState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 11), AtAlmMonActionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonActionState.setStatus('current')
if mibBuilder.loadTexts: atAlmMonActionState.setDescription('Indicates the current state of this alarm monitor.')
mibBuilder.exportSymbols("AT-ALMMON-MIB", atAlmMonActionDescription=atAlmMonActionDescription, PYSNMP_MODULE_ID=atAlmMon, atAlmMonActionTable=atAlmMonActionTable, AtAlmMonActionState=AtAlmMonActionState, AtAlmMonActionUseOutput=AtAlmMonActionUseOutput, atAlmMonActionUseFaultLed=atAlmMonActionUseFaultLed, atAlmMonActionUseRelay3=atAlmMonActionUseRelay3, atAlmMonActionStackMemberId=atAlmMonActionStackMemberId, atAlmMonActionIndex=atAlmMonActionIndex, atAlmMonAbnormalState=atAlmMonAbnormalState, atAlmMonActionState=atAlmMonActionState, AtAlmMonAbnormalState=AtAlmMonAbnormalState, AtAlmMonAlarmType=AtAlmMonAlarmType, atAlmMonAlarmType=atAlmMonAlarmType, atAlmMonActionUseRelay2=atAlmMonActionUseRelay2, atAlmMonAlarmTypeSelection=atAlmMonAlarmTypeSelection, atAlmMonActionUseRelay1=atAlmMonActionUseRelay1, atAlmMonActionEntry=atAlmMonActionEntry, atAlmMon=atAlmMon)
