#
# PySNMP MIB module SPRIF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/SPRIF-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 21:14:06 2021
# On host fv-az33-735 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
SagemBoolean, = mibBuilder.importSymbols("EQUIPMENT-MIB", "SagemBoolean")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, ObjectIdentity, NotificationType, IpAddress, iso, TimeTicks, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "IpAddress", "iso", "TimeTicks", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sprif = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 180))
if mibBuilder.loadTexts: sprif.setLastUpdated('0012120000Z')
if mibBuilder.loadTexts: sprif.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
debug = MibIdentifier((1, 3, 6, 1, 4, 1, 1038, 180, 10))
debug3 = MibIdentifier((1, 3, 6, 1, 4, 1, 1038, 180, 30))
class NodeId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 255))
    namedValues = NamedValues(("node0", 0), ("node1", 1), ("node2", 2), ("node3", 3), ("node4", 4), ("node5", 5), ("node6", 6), ("node7", 7), ("node8", 8), ("node9", 9), ("node10", 10), ("node11", 11), ("node12", 12), ("node13", 13), ("node14", 14), ("node15", 15), ("nodeUNK", 255))

class STATE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("off", 0), ("idle", 1), ("pass", 2), ("switch", 3), ("unknown", 4))

class SWITCHSTATUS(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notSw", 0), ("br", 1), ("sw", 2), ("brsw", 3), ("unknown", 4))

class K1ASK(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(15, 13, 11, 8, 6, 5, 3, 1, 0))
    namedValues = NamedValues(("lps", 15), ("fsr", 13), ("sfr", 11), ("sdr", 8), ("msr", 6), ("wtr", 5), ("exerr", 3), ("rr", 1), ("nr", 0))

class LOGTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("receiveK", 0), ("transmitK", 1), ("opCmd", 2), ("failure", 3), ("timer", 4), ("unknown", 5))

class LOCALCOMMAND(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(20, 19, 18, 17, 16, 15, 13, 6, 5, 3, 0))
    namedValues = NamedValues(("on", 20), ("off", 19), ("lopas", 18), ("lowr", 17), ("clear", 16), ("lps", 15), ("fsr", 13), ("msr", 6), ("wtr", 5), ("exerr", 3), ("none", 0))

class LOCALFAIL(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(27, 24, 11, 8, 0))
    namedValues = NamedValues(("endsf", 27), ("endsd", 24), ("sf", 11), ("sd", 8), ("none", 0))

class K2STAT(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(7, 6, 3, 2, 1, 0))
    namedValues = NamedValues(("msais", 7), ("msrdi", 6), ("extra", 3), ("brsw", 2), ("br", 1), ("idle", 0))

class K2PATH(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("short", 0), ("long", 1))

class TrafficStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("working", 1), ("protection", 2))

class LINE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("west", 0), ("east", 1), ("unknown", 2))

class TIMER(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("stop", 0), ("start", 1), ("restart", 2))

debugNumber = MibScalar((1, 3, 6, 1, 4, 1, 1038, 180, 10, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugNumber.setStatus('current')
debugTable = MibTable((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2), )
if mibBuilder.loadTexts: debugTable.setStatus('current')
debugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1), ).setIndexNames((0, "SPRIF-MIB", "debugIndex"))
if mibBuilder.loadTexts: debugEntry.setStatus('current')
debugIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugIndex.setStatus('current')
debugDate = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugDate.setStatus('current')
debugNodeID = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 3), NodeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugNodeID.setStatus('current')
debugLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 4), LOGTYPE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugLogType.setStatus('current')
debugLine = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 5), LINE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugLine.setStatus('current')
debugNodeState = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 6), STATE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugNodeState.setStatus('current')
debugTrafficStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 7), TrafficStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugTrafficStatus.setStatus('current')
debugSwitchingState = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 8), SWITCHSTATUS()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugSwitchingState.setStatus('current')
debugTxK1Ask = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 9), K1ASK()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugTxK1Ask.setStatus('current')
debugTxK1Dst = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 10), NodeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugTxK1Dst.setStatus('current')
debugTxK2Src = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 11), NodeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugTxK2Src.setStatus('current')
debugTxK2Path = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 12), K2PATH()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugTxK2Path.setStatus('current')
debugTxK2Stat = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 13), K2STAT()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugTxK2Stat.setStatus('current')
debugRxK1Ask = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 14), K1ASK()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugRxK1Ask.setStatus('current')
debugRxK1Dst = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 15), NodeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugRxK1Dst.setStatus('current')
debugRxK2Src = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 16), NodeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugRxK2Src.setStatus('current')
debugRxK2Path = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 17), K2PATH()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugRxK2Path.setStatus('current')
debugRxK2Stat = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 18), K2STAT()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugRxK2Stat.setStatus('current')
debugWtr = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugWtr.setStatus('current')
debugLastDistantCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 20), K1ASK()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugLastDistantCommand.setStatus('current')
debugLastDetectedFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 21), LOCALFAIL()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugLastDetectedFailure.setStatus('current')
debugLastLocalCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 22), LOCALCOMMAND()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugLastLocalCommand.setStatus('current')
debugTimerAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 23), TIMER()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debugTimerAction.setStatus('current')
debugActivated = MibScalar((1, 3, 6, 1, 4, 1, 1038, 180, 10, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: debugActivated.setStatus('current')
debug3Table = MibTable((1, 3, 6, 1, 4, 1, 1038, 180, 30, 2), )
if mibBuilder.loadTexts: debug3Table.setStatus('current')
debug3Entry = MibTableRow((1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1), ).setIndexNames((0, "SPRIF-MIB", "debugIndex"))
if mibBuilder.loadTexts: debug3Entry.setStatus('current')
debug3Date = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: debug3Date.setStatus('current')
debug3Line = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 5), LINE()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debug3Line.setStatus('current')
debug3arv = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 23), SagemBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debug3arv.setStatus('current')
debug3ato = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 24), SagemBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debug3ato.setStatus('current')
debug3aun = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 25), SagemBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debug3aun.setStatus('current')
debug3ptm = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 26), SagemBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debug3ptm.setStatus('current')
debug3mms = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 27), SagemBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debug3mms.setStatus('current')
debug3exr = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 28), SagemBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: debug3exr.setStatus('current')
mibBuilder.exportSymbols("SPRIF-MIB", debug3exr=debug3exr, K1ASK=K1ASK, LINE=LINE, debugEntry=debugEntry, debug3Table=debug3Table, debugWtr=debugWtr, debugRxK2Src=debugRxK2Src, debug3arv=debug3arv, debugTxK1Dst=debugTxK1Dst, K2PATH=K2PATH, debugLogType=debugLogType, debug3mms=debug3mms, debugActivated=debugActivated, debug=debug, debugTxK2Stat=debugTxK2Stat, debugTxK1Ask=debugTxK1Ask, SWITCHSTATUS=SWITCHSTATUS, K2STAT=K2STAT, debugLastLocalCommand=debugLastLocalCommand, debugLastDetectedFailure=debugLastDetectedFailure, debugRxK2Stat=debugRxK2Stat, LOCALFAIL=LOCALFAIL, debugLine=debugLine, debug3Line=debug3Line, debug3Date=debug3Date, STATE=STATE, debug3=debug3, debugTable=debugTable, debugNodeState=debugNodeState, LOGTYPE=LOGTYPE, LOCALCOMMAND=LOCALCOMMAND, debugTxK2Path=debugTxK2Path, debugNodeID=debugNodeID, debugSwitchingState=debugSwitchingState, debugTrafficStatus=debugTrafficStatus, debugTxK2Src=debugTxK2Src, debugDate=debugDate, debug3Entry=debug3Entry, debugRxK1Dst=debugRxK1Dst, NodeId=NodeId, debugRxK2Path=debugRxK2Path, debug3aun=debug3aun, debugIndex=debugIndex, debug3ato=debug3ato, debugLastDistantCommand=debugLastDistantCommand, sprif=sprif, debug3ptm=debug3ptm, TrafficStatus=TrafficStatus, PYSNMP_MODULE_ID=sprif, debugTimerAction=debugTimerAction, debugNumber=debugNumber, TIMER=TIMER, debugRxK1Ask=debugRxK1Ask)
