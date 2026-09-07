#
# PySNMP MIB module ALCATEL-IND1-STACK-MANAGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ALCATEL-IND1-STACK-MANAGER-MIB
# Source digest sha256:9befc476bee721299d7850052e42d10dd4e83e285051f3383d35153795490fc1
# Produced by pysmi-2.3.0
#
softentIND1StackMgr, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1StackMgr")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alcatelIND1StackMgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1))
alcatelIND1StackMgrMIB.setRevisions(('2009-02-06 00:00', '2009-02-06 00:00', '2007-04-03 00:00', '2005-07-15 00:00', '2004-07-01 00:00', '2004-04-23 00:00', '2004-04-08 00:00', '2004-04-04 00:00', '2004-03-22 00:00', '2004-03-08 00:00', '2019-10-07 00:00',))
if mibBuilder.loadTexts: alcatelIND1StackMgrMIB.setLastUpdated('2019-10-07 00:00')
if mibBuilder.loadTexts: alcatelIND1StackMgrMIB.setOrganization('ALE USA Inc')
alcatelIND1StackMgrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1))
alcatelIND1StackMgrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2))
alcatelIND1StackMgrTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 3))
alaStackMgrTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4))
class AlaStackMgrLinkNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(27, 28, 51, 52, 31, 32, 25, 26, 29, 30, 1, 2, 11, 12))
    namedValues = NamedValues(("linkA27", 27), ("linkB28", 28), ("linkA51", 51), ("linkB52", 52), ("linkA31", 31), ("linkB32", 32), ("linkA25", 25), ("linkB26", 26), ("linkA29", 29), ("linkB30", 30), ("linkA", 1), ("linkB", 2), ("linkA11", 11), ("linkB12", 12))

class AlaStackMgrNINumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1008)

class AlaStackMgrLinkStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class AlaStackMgrSlotRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unassigned", 0), ("primary", 1), ("secondary", 2), ("idle", 3), ("standalone", 4), ("passthrough", 5))

class AlaStackMgrStackStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("loop", 1), ("noloop", 2))

class AlaStackMgrSlotState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("running", 1), ("duplicateSlot", 2), ("clearedSlot", 3), ("outOfSlots", 4), ("outOfTokens", 5), ("badMix", 6), ("inc-Lic", 7))

class AlaStackMgrCommandAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notSignificant", 0), ("clearSlot", 1), ("clearSlotImmediately", 2), ("reloadAny", 3), ("reloadPassThru", 4))

class AlaStackMgrCommandStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notSignificant", 0), ("clearSlotInProgress", 1), ("clearSlotFailed", 2), ("clearSlotSuccess", 3), ("setSlotInProgress", 4), ("setSlotFailed", 5), ("setSlotSuccess", 6))

class AlaStackMgrStackingMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackable", 1), ("standalone", 2))

class AlaStackMgrStackMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("os6850", 1), ("os6850e", 2))

class AlaStackMgrLicenseType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("notSignificant", 0), ("metro", 1))

class AlaSSPTableSlotNINumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), ValueRangeConstraint(255, 255), ValueRangeConstraint(1001, 1008), )
class AlaSSPTableSspOpStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("active", 1), ("protection", 2), ("notinstack", 3))

alaStackMgrChassisTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaStackMgrChassisTable.setStatus('current')
alaStackMgrChassisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrChassisEntry.setStatus('current')
alaStackMgrSlotNINumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 1), AlaStackMgrNINumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrSlotNINumber.setStatus('current')
alaStackMgrSlotCMMNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 72))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrSlotCMMNumber.setStatus('current')
alaStackMgrChasRole = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 3), AlaStackMgrSlotRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrChasRole.setStatus('current')
alaStackMgrLocalLinkStateA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 4), AlaStackMgrLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrLocalLinkStateA.setStatus('current')
alaStackMgrRemoteNISlotA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 5), AlaStackMgrNINumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteNISlotA.setStatus('current')
alaStackMgrRemoteLinkA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 6), AlaStackMgrLinkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteLinkA.setStatus('current')
alaStackMgrLocalLinkStateB = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 7), AlaStackMgrLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrLocalLinkStateB.setStatus('current')
alaStackMgrRemoteNISlotB = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 8), AlaStackMgrNINumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteNISlotB.setStatus('current')
alaStackMgrRemoteLinkB = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 9), AlaStackMgrLinkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteLinkB.setStatus('current')
alaStackMgrChasState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 10), AlaStackMgrSlotState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrChasState.setStatus('current')
alaStackMgrSavedSlotNINumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 11), AlaStackMgrNINumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrSavedSlotNINumber.setStatus('current')
alaStackMgrCommandAction = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 12), AlaStackMgrCommandAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrCommandAction.setStatus('current')
alaStackMgrCommandStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 13), AlaStackMgrCommandStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrCommandStatus.setStatus('current')
alaStackMgrOperStackingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 14), AlaStackMgrStackingMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrOperStackingMode.setStatus('current')
alaStackMgrAdminStackingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 1, 1, 15), AlaStackMgrStackingMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrAdminStackingMode.setStatus('current')
alaStackMgrStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaStackMgrStatsTable.setStatus('current')
alaStackMgrStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStatLinkNumber"))
if mibBuilder.loadTexts: alaStackMgrStatsEntry.setStatus('current')
alaStackMgrStatLinkNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 2, 1, 1), AlaStackMgrLinkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatLinkNumber.setStatus('current')
alaStackMgrStatPktsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatPktsRx.setStatus('current')
alaStackMgrStatPktsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatPktsTx.setStatus('current')
alaStackMgrStatErrorsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatErrorsRx.setStatus('current')
alaStackMgrStatErrorsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatErrorsTx.setStatus('current')
alaStackMgrStatDelayFromLastMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatDelayFromLastMsg.setStatus('current')
alaStackMgrStackStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 3), AlaStackMgrStackStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStackStatus.setStatus('current')
alaStackMgrTokensUsed = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrTokensUsed.setStatus('current')
alaStackMgrTokensAvailable = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrTokensAvailable.setStatus('current')
alaStackMgrStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 6), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaStackMgrStaticRouteTable.setStatus('current')
alaStackMgrStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 6, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteSrcStartIf"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteSrcEndIf"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteDstStartIf"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteDstEndIf"))
if mibBuilder.loadTexts: alaStackMgrStaticRouteEntry.setStatus('current')
alaStackMgrStaticRouteSrcStartIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 6, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaStackMgrStaticRouteSrcStartIf.setStatus('current')
alaStackMgrStaticRouteSrcEndIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 6, 1, 2), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaStackMgrStaticRouteSrcEndIf.setStatus('current')
alaStackMgrStaticRouteDstStartIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 6, 1, 3), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaStackMgrStaticRouteDstStartIf.setStatus('current')
alaStackMgrStaticRouteDstEndIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 6, 1, 4), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaStackMgrStaticRouteDstEndIf.setStatus('current')
alaStackMgrStaticRoutePort = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 6, 1, 5), AlaStackMgrLinkNumber().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaStackMgrStaticRoutePort.setStatus('current')
alaStackMgrStaticRoutePortState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 6, 1, 6), AlaStackMgrLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStaticRoutePortState.setStatus('current')
alaStackMgrStaticRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaStackMgrStaticRouteStatus.setStatus('current')
alaStackMgrStaticRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 6, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaStackMgrStaticRouteRowStatus.setStatus('current')
alaStackMgrStackModeTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 7), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaStackMgrStackModeTable.setStatus('current')
alaStackMgrStackModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 7, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStackModeIndex"))
if mibBuilder.loadTexts: alaStackMgrStackModeEntry.setStatus('current')
alaStackMgrStackModeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 7, 1, 1), AlaStackMgrNINumber()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaStackMgrStackModeIndex.setStatus('current')
alaStackMgrAdminStackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 7, 1, 2), AlaStackMgrStackMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrAdminStackMode.setStatus('current')
alaStackMgrOperStackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 7, 1, 3), AlaStackMgrStackMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrOperStackMode.setStatus('current')
alaStackMgrCmdAction = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3))).clone(namedValues=NamedValues(("reloadAny", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrCmdAction.setStatus('current')
alaSSPHelperGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 9))
alaSspHelperStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSspHelperStatus.setStatus('current')
alaSspHelperqAggregateTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 10), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaSspHelperqAggregateTable.setStatus('current')
alaSspHelperqAggregateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 10, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaSspHelperAggregateId"))
if mibBuilder.loadTexts: alaSspHelperqAggregateEntry.setStatus('current')
alaSspHelperAggregateId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaSspHelperAggregateId.setStatus('current')
alaSspHelperAggregateStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSspHelperAggregateStatus.setStatus('current')
alaSSPConfigInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 8))
alaSspConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSspConfigStatus.setStatus('current')
alaSspLinkaggId = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 8, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 31)).clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSspLinkaggId.setStatus('current')
alaSspGuardTimer = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 100)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSspGuardTimer.setStatus('current')
alaSspUpTime = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 8, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaSspUpTime.setStatus('current')
alaSspStateUpTime = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 8, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaSspStateUpTime.setStatus('current')
alaSSPStateTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 8), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaSSPStateTable.setStatus('current')
alaSSPStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 8, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaSSPTableSlotNINumber"))
if mibBuilder.loadTexts: alaSSPStateEntry.setStatus('current')
alaSSPTableSlotNINumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 8, 1, 1), AlaSSPTableSlotNINumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaSSPTableSlotNINumber.setStatus('current')
alaSSPTableSspOpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 1, 8, 1, 2), AlaSSPTableSspOpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaSSPTableSspOpStatus.setStatus('current')
alaStackMgrTrapLinkNumber = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 3, 1), AlaStackMgrLinkNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaStackMgrTrapLinkNumber.setStatus('current')
alaStackMgrPrimary = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 3, 2), AlaStackMgrNINumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaStackMgrPrimary.setStatus('current')
alaStackMgrSecondary = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 3, 3), AlaStackMgrNINumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaStackMgrSecondary.setStatus('current')
alaStackMgrPrimaryLicense = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 3, 4), AlaStackMgrLicenseType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaStackMgrPrimaryLicense.setStatus('current')
alaStackMgrDuplicateSlotTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 1)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrDuplicateSlotTrap.setStatus('current')
alaStackMgrNeighborChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 2)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStackStatus"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrTrapLinkNumber"))
if mibBuilder.loadTexts: alaStackMgrNeighborChangeTrap.setStatus('current')
alaStackMgrRoleChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 3)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrPrimary"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSecondary"))
if mibBuilder.loadTexts: alaStackMgrRoleChangeTrap.setStatus('current')
alaStackMgrDuplicateRoleTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 4)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasRole"))
if mibBuilder.loadTexts: alaStackMgrDuplicateRoleTrap.setStatus('current')
alaStackMgrClearedSlotTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 5)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrClearedSlotTrap.setStatus('current')
alaStackMgrOutOfSlotsTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 6))
if mibBuilder.loadTexts: alaStackMgrOutOfSlotsTrap.setStatus('current')
alaStackMgrOutOfTokensTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 7)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrOutOfTokensTrap.setStatus('current')
alaStackMgrOutOfPassThruSlotsTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 8))
if mibBuilder.loadTexts: alaStackMgrOutOfPassThruSlotsTrap.setStatus('current')
alaStackMgrBadMixTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 9)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrBadMixTrap.setStatus('current')
alaStackMgrIncompatibleLicenseTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 10)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrPrimaryLicense"))
if mibBuilder.loadTexts: alaStackMgrIncompatibleLicenseTrap.setStatus('current')
alaStackSplitProtectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 11)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackSplitProtectionTrap.setStatus('current')
alaStackSplitRecoveryTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 4, 0, 12)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackSplitRecoveryTrap.setStatus('current')
alcatelIND1StackMgrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1))
alcatelIND1StackMgrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 2))
alaStackMgrCfgMgrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotCMMNumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasRole"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrLocalLinkStateA"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteNISlotA"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteLinkA"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrLocalLinkStateB"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteNISlotB"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteLinkB"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasState"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSavedSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrCommandAction"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrCommandStatus"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOperStackingMode"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrAdminStackingMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackMgrCfgMgrGroup = alaStackMgrCfgMgrGroup.setStatus('current')
alaStackMgrNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrDuplicateSlotTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrNeighborChangeTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRoleChangeTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrDuplicateRoleTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrClearedSlotTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfSlotsTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfTokensTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfPassThruSlotsTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrBadMixTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrIncompatibleLicenseTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackSplitProtectionTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackSplitRecoveryTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackMgrNotificationGroup = alaStackMgrNotificationGroup.setStatus('current')
alaStackMgrStackModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrAdminStackMode"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOperStackMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackMgrStackModeGroup = alaStackMgrStackModeGroup.setStatus('current')
alaStackMgrTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrPrimary"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSecondary"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStackStatus"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrTrapLinkNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackMgrTrapGroup = alaStackMgrTrapGroup.setStatus('current')
alaStackMgrStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 5)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStatLinkNumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStatPktsRx"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStatPktsTx"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStatErrorsRx"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStatErrorsTx"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStatDelayFromLastMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackMgrStatGroup = alaStackMgrStatGroup.setStatus('current')
alaStackMgrStaticRouteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 6)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRoutePort"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRoutePortState"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteStatus"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackMgrStaticRouteGroup = alaStackMgrStaticRouteGroup.setStatus('current')
alaStackMgrMIBObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 7)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrTokensAvailable"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrTokensUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackMgrMIBObjectsGroup = alaStackMgrMIBObjectsGroup.setStatus('current')
alaStackSplitProtectionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 1, 9)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaSspHelperStatus"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaSspHelperAggregateId"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaSspHelperAggregateStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackSplitProtectionGroup = alaStackSplitProtectionGroup.setStatus('current')
alcatelIND1StackMgrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 24, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrCfgMgrGroup"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrNotificationGroup"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStackModeGroup"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrTrapGroup"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStatGroup"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteGroup"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrMIBObjectsGroup"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaSSPConfigInfo"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackSplitProtectionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1StackMgrMIBCompliance = alcatelIND1StackMgrMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-STACK-MANAGER-MIB", AlaSSPTableSlotNINumber=AlaSSPTableSlotNINumber, AlaSSPTableSspOpStatus=AlaSSPTableSspOpStatus, AlaStackMgrCommandAction=AlaStackMgrCommandAction, AlaStackMgrCommandStatus=AlaStackMgrCommandStatus, AlaStackMgrLicenseType=AlaStackMgrLicenseType, AlaStackMgrLinkNumber=AlaStackMgrLinkNumber, AlaStackMgrLinkStatus=AlaStackMgrLinkStatus, AlaStackMgrNINumber=AlaStackMgrNINumber, AlaStackMgrSlotRole=AlaStackMgrSlotRole, AlaStackMgrSlotState=AlaStackMgrSlotState, AlaStackMgrStackMode=AlaStackMgrStackMode, AlaStackMgrStackStatus=AlaStackMgrStackStatus, AlaStackMgrStackingMode=AlaStackMgrStackingMode, PYSNMP_MODULE_ID=alcatelIND1StackMgrMIB, alaSSPConfigInfo=alaSSPConfigInfo, alaSSPHelperGlobalConfig=alaSSPHelperGlobalConfig, alaSSPStateEntry=alaSSPStateEntry, alaSSPStateTable=alaSSPStateTable, alaSSPTableSlotNINumber=alaSSPTableSlotNINumber, alaSSPTableSspOpStatus=alaSSPTableSspOpStatus, alaSspConfigStatus=alaSspConfigStatus, alaSspGuardTimer=alaSspGuardTimer, alaSspHelperAggregateId=alaSspHelperAggregateId, alaSspHelperAggregateStatus=alaSspHelperAggregateStatus, alaSspHelperStatus=alaSspHelperStatus, alaSspHelperqAggregateEntry=alaSspHelperqAggregateEntry, alaSspHelperqAggregateTable=alaSspHelperqAggregateTable, alaSspLinkaggId=alaSspLinkaggId, alaSspStateUpTime=alaSspStateUpTime, alaSspUpTime=alaSspUpTime, alaStackMgrAdminStackMode=alaStackMgrAdminStackMode, alaStackMgrAdminStackingMode=alaStackMgrAdminStackingMode, alaStackMgrBadMixTrap=alaStackMgrBadMixTrap, alaStackMgrCfgMgrGroup=alaStackMgrCfgMgrGroup, alaStackMgrChasRole=alaStackMgrChasRole, alaStackMgrChasState=alaStackMgrChasState, alaStackMgrChassisEntry=alaStackMgrChassisEntry, alaStackMgrChassisTable=alaStackMgrChassisTable, alaStackMgrClearedSlotTrap=alaStackMgrClearedSlotTrap, alaStackMgrCmdAction=alaStackMgrCmdAction, alaStackMgrCommandAction=alaStackMgrCommandAction, alaStackMgrCommandStatus=alaStackMgrCommandStatus, alaStackMgrDuplicateRoleTrap=alaStackMgrDuplicateRoleTrap, alaStackMgrDuplicateSlotTrap=alaStackMgrDuplicateSlotTrap, alaStackMgrIncompatibleLicenseTrap=alaStackMgrIncompatibleLicenseTrap, alaStackMgrLocalLinkStateA=alaStackMgrLocalLinkStateA, alaStackMgrLocalLinkStateB=alaStackMgrLocalLinkStateB, alaStackMgrMIBObjectsGroup=alaStackMgrMIBObjectsGroup, alaStackMgrNeighborChangeTrap=alaStackMgrNeighborChangeTrap, alaStackMgrNotificationGroup=alaStackMgrNotificationGroup, alaStackMgrOperStackMode=alaStackMgrOperStackMode, alaStackMgrOperStackingMode=alaStackMgrOperStackingMode, alaStackMgrOutOfPassThruSlotsTrap=alaStackMgrOutOfPassThruSlotsTrap, alaStackMgrOutOfSlotsTrap=alaStackMgrOutOfSlotsTrap, alaStackMgrOutOfTokensTrap=alaStackMgrOutOfTokensTrap, alaStackMgrPrimary=alaStackMgrPrimary, alaStackMgrPrimaryLicense=alaStackMgrPrimaryLicense, alaStackMgrRemoteLinkA=alaStackMgrRemoteLinkA, alaStackMgrRemoteLinkB=alaStackMgrRemoteLinkB, alaStackMgrRemoteNISlotA=alaStackMgrRemoteNISlotA, alaStackMgrRemoteNISlotB=alaStackMgrRemoteNISlotB, alaStackMgrRoleChangeTrap=alaStackMgrRoleChangeTrap, alaStackMgrSavedSlotNINumber=alaStackMgrSavedSlotNINumber, alaStackMgrSecondary=alaStackMgrSecondary, alaStackMgrSlotCMMNumber=alaStackMgrSlotCMMNumber, alaStackMgrSlotNINumber=alaStackMgrSlotNINumber, alaStackMgrStackModeEntry=alaStackMgrStackModeEntry, alaStackMgrStackModeGroup=alaStackMgrStackModeGroup, alaStackMgrStackModeIndex=alaStackMgrStackModeIndex, alaStackMgrStackModeTable=alaStackMgrStackModeTable, alaStackMgrStackStatus=alaStackMgrStackStatus, alaStackMgrStatDelayFromLastMsg=alaStackMgrStatDelayFromLastMsg, alaStackMgrStatErrorsRx=alaStackMgrStatErrorsRx, alaStackMgrStatErrorsTx=alaStackMgrStatErrorsTx, alaStackMgrStatGroup=alaStackMgrStatGroup, alaStackMgrStatLinkNumber=alaStackMgrStatLinkNumber, alaStackMgrStatPktsRx=alaStackMgrStatPktsRx, alaStackMgrStatPktsTx=alaStackMgrStatPktsTx, alaStackMgrStaticRouteDstEndIf=alaStackMgrStaticRouteDstEndIf, alaStackMgrStaticRouteDstStartIf=alaStackMgrStaticRouteDstStartIf, alaStackMgrStaticRouteEntry=alaStackMgrStaticRouteEntry, alaStackMgrStaticRouteGroup=alaStackMgrStaticRouteGroup, alaStackMgrStaticRoutePort=alaStackMgrStaticRoutePort, alaStackMgrStaticRoutePortState=alaStackMgrStaticRoutePortState, alaStackMgrStaticRouteRowStatus=alaStackMgrStaticRouteRowStatus, alaStackMgrStaticRouteSrcEndIf=alaStackMgrStaticRouteSrcEndIf, alaStackMgrStaticRouteSrcStartIf=alaStackMgrStaticRouteSrcStartIf, alaStackMgrStaticRouteStatus=alaStackMgrStaticRouteStatus, alaStackMgrStaticRouteTable=alaStackMgrStaticRouteTable, alaStackMgrStatsEntry=alaStackMgrStatsEntry, alaStackMgrStatsTable=alaStackMgrStatsTable, alaStackMgrTokensAvailable=alaStackMgrTokensAvailable, alaStackMgrTokensUsed=alaStackMgrTokensUsed, alaStackMgrTrapGroup=alaStackMgrTrapGroup, alaStackMgrTrapLinkNumber=alaStackMgrTrapLinkNumber, alaStackMgrTraps=alaStackMgrTraps, alaStackSplitProtectionGroup=alaStackSplitProtectionGroup, alaStackSplitProtectionTrap=alaStackSplitProtectionTrap, alaStackSplitRecoveryTrap=alaStackSplitRecoveryTrap, alcatelIND1StackMgrMIB=alcatelIND1StackMgrMIB, alcatelIND1StackMgrMIBCompliance=alcatelIND1StackMgrMIBCompliance, alcatelIND1StackMgrMIBCompliances=alcatelIND1StackMgrMIBCompliances, alcatelIND1StackMgrMIBConformance=alcatelIND1StackMgrMIBConformance, alcatelIND1StackMgrMIBGroups=alcatelIND1StackMgrMIBGroups, alcatelIND1StackMgrMIBObjects=alcatelIND1StackMgrMIBObjects, alcatelIND1StackMgrTrapObjects=alcatelIND1StackMgrTrapObjects)
