#
# PySNMP MIB module AT-ALMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-ALMMON-MIB
# Produced by pysmi-1.1.12 at Wed May 29 10:52:01 2024
# On host fv-az1200-312 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
DisplayStringUnsized, = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Gauge32, Unsigned32, Counter32, Counter64, IpAddress, MibIdentifier, Integer32, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Gauge32", "Unsigned32", "Counter32", "Counter64", "IpAddress", "MibIdentifier", "Integer32", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("AT-ALMMON-MIB", atAlmMonActionUseRelay2=atAlmMonActionUseRelay2, atAlmMonActionEntry=atAlmMonActionEntry, AtAlmMonAbnormalState=AtAlmMonAbnormalState, atAlmMonAlarmType=atAlmMonAlarmType, atAlmMonActionUseRelay3=atAlmMonActionUseRelay3, AtAlmMonActionState=AtAlmMonActionState, atAlmMonActionState=atAlmMonActionState, atAlmMonActionStackMemberId=atAlmMonActionStackMemberId, atAlmMonActionUseRelay1=atAlmMonActionUseRelay1, atAlmMonActionDescription=atAlmMonActionDescription, atAlmMonAbnormalState=atAlmMonAbnormalState, atAlmMonAlarmTypeSelection=atAlmMonAlarmTypeSelection, atAlmMonActionTable=atAlmMonActionTable, atAlmMonActionUseFaultLed=atAlmMonActionUseFaultLed, atAlmMon=atAlmMon, PYSNMP_MODULE_ID=atAlmMon, AtAlmMonActionUseOutput=AtAlmMonActionUseOutput, AtAlmMonAlarmType=AtAlmMonAlarmType, atAlmMonActionIndex=atAlmMonActionIndex)
