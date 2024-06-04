#
# PySNMP MIB module AT-ALMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-ALMMON-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 02:36:40 2024
# On host fv-az1200-411 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
DisplayStringUnsized, = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Integer32, ModuleIdentity, IpAddress, MibIdentifier, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Bits, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Integer32", "ModuleIdentity", "IpAddress", "MibIdentifier", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atAlmMon = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26))
atAlmMon.setRevisions(('2017-02-08 00:00', '2014-05-12 00:15', '2013-12-13 11:46',))
if mibBuilder.loadTexts: atAlmMon.setLastUpdated('201702080000Z')
if mibBuilder.loadTexts: atAlmMon.setOrganization('Allied Telesis, Inc')
class AtAlmMonAlarmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("alarmTypeInvalid", 0), ("externalPSU", 1), ("epsr", 2), ("contactInput", 3), ("portLinkDown", 4), ("loopDetect", 5), ("mainPse", 6), ("portPoeFailure", 7), ("temperature", 8), ("g8032", 9))

class AtAlmMonActionUseOutput(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unused", 1), ("used", 2))

class AtAlmMonAbnormalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("open", 1), ("closed", 2))

class AtAlmMonActionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inactive", 1), ("active", 2))

atAlmMonActionTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1), )
if mibBuilder.loadTexts: atAlmMonActionTable.setStatus('current')
atAlmMonActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1), ).setIndexNames((0, "AT-ALMMON-MIB", "atAlmMonActionStackMemberId"), (0, "AT-ALMMON-MIB", "atAlmMonActionIndex"))
if mibBuilder.loadTexts: atAlmMonActionEntry.setStatus('current')
atAlmMonActionStackMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonActionStackMemberId.setStatus('current')
atAlmMonActionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonActionIndex.setStatus('current')
atAlmMonAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 3), AtAlmMonAlarmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonAlarmType.setStatus('current')
atAlmMonAlarmTypeSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonAlarmTypeSelection.setStatus('current')
atAlmMonActionDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 5), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonActionDescription.setStatus('current')
atAlmMonActionUseRelay1 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 6), AtAlmMonActionUseOutput()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atAlmMonActionUseRelay1.setStatus('current')
atAlmMonActionUseRelay2 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 7), AtAlmMonActionUseOutput()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atAlmMonActionUseRelay2.setStatus('current')
atAlmMonActionUseRelay3 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 8), AtAlmMonActionUseOutput()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atAlmMonActionUseRelay3.setStatus('current')
atAlmMonActionUseFaultLed = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 9), AtAlmMonActionUseOutput()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atAlmMonActionUseFaultLed.setStatus('current')
atAlmMonAbnormalState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 10), AtAlmMonAbnormalState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atAlmMonAbnormalState.setStatus('current')
atAlmMonActionState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 26, 1, 1, 11), AtAlmMonActionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atAlmMonActionState.setStatus('current')
mibBuilder.exportSymbols("AT-ALMMON-MIB", atAlmMonActionUseRelay1=atAlmMonActionUseRelay1, PYSNMP_MODULE_ID=atAlmMon, atAlmMonActionStackMemberId=atAlmMonActionStackMemberId, atAlmMonActionUseFaultLed=atAlmMonActionUseFaultLed, atAlmMonAbnormalState=atAlmMonAbnormalState, AtAlmMonActionState=AtAlmMonActionState, atAlmMonAlarmTypeSelection=atAlmMonAlarmTypeSelection, atAlmMonAlarmType=atAlmMonAlarmType, atAlmMonActionState=atAlmMonActionState, atAlmMonActionEntry=atAlmMonActionEntry, AtAlmMonAlarmType=AtAlmMonAlarmType, atAlmMonActionUseRelay3=atAlmMonActionUseRelay3, atAlmMonActionUseRelay2=atAlmMonActionUseRelay2, AtAlmMonActionUseOutput=AtAlmMonActionUseOutput, atAlmMon=atAlmMon, atAlmMonActionIndex=atAlmMonActionIndex, atAlmMonActionDescription=atAlmMonActionDescription, atAlmMonActionTable=atAlmMonActionTable, AtAlmMonAbnormalState=AtAlmMonAbnormalState)
