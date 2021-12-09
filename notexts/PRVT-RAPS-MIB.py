#
# PySNMP MIB module PRVT-RAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-RAPS-MIB
# Produced by pysmi-1.1.3 at Thu Dec  9 14:56:11 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
serviceAccessSwitch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "serviceAccessSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ObjectIdentity, iso, TimeTicks, Integer32, Bits, Counter64, Unsigned32, ModuleIdentity, IpAddress, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ObjectIdentity", "iso", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "ModuleIdentity", "IpAddress", "MibIdentifier", "Gauge32")
DisplayString, RowStatus, MacAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "MacAddress", "TruthValue", "TextualConvention")
prvtRapsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 7, 4))
prvtRapsMIB.setRevisions(('2010-11-11 00:00', '2010-03-08 00:00',))
if mibBuilder.loadTexts: prvtRapsMIB.setLastUpdated('201011110000Z')
if mibBuilder.loadTexts: prvtRapsMIB.setOrganization('BATM Advanced Communication')
class PrvtRapsInstIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 10)

class PrvtRapsRingIdType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class PrvtRapsVlanIdType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class PrvtRapsLinkOperStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("up", 0), ("blocked", 1), ("failed", 2), ("na", 3))

class PrvtRapsMepIdType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8191)

class PrvtRapsLinkAggIdType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 14)

class PrvtRapsHoldOffType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10000)

class PrvtRapsWaitTimerType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 12)

class PrvtRapsCfmLevelType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class PrvtRapsGuardTimerType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(10, 2000)

class PrvtRapsBlockTimerType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(5010, 7000)

class PrvtRapsModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("version1", 1), ("version2", 2))

class PrvtRapsRoleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("simpleNode", 0), ("rplNeighbor", 1), ("rplOwner", 2))

class PrvtRapsInstStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrvtRapsStatesType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("init", 0), ("idle", 1), ("protection", 2), ("manualSwitch", 3), ("forcedSwitch", 4), ("pending", 5))

class PrvtRapsReceivedCommandType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 7, 11, 13, 14, 16))
    namedValues = NamedValues(("noRequest", 0), ("manualSwitch", 7), ("signalFail", 11), ("forcedSwitch", 13), ("event", 14), ("na", 16))

class PrvtRapsReceivedInfoType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bpr", 0), ("dnf", 1), ("rp", 2))

class PrvtRapsTopPriCmdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("clear", 0), ("forcedSwitch", 1), ("remoteForcedSwitch", 2), ("signalFail", 3), ("signalFailRecover", 4), ("remoteSignalFail", 5), ("remoteManualSwitch", 6), ("manualSwitch", 7), ("wtrExpire", 8), ("wtrRunning", 9), ("wtbExpire", 10), ("wtbRunning", 11), ("noRequestRplBlocked", 12), ("noRequest", 13), ("na", 14))

class PrvtRapsActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("idle", 1), ("performAction", 2))

class PrvtRapsIfIndexOrAgIdType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class PrvtRapsMonitoringMethodType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ccm", 1), ("link-status", 2))

prvtRapsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 0))
prvtRapsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1))
prvtRapsInstTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1), )
if mibBuilder.loadTexts: prvtRapsInstTable.setStatus('current')
prvtRapsInstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"))
if mibBuilder.loadTexts: prvtRapsInstEntry.setStatus('current')
prvtRapsInstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 1), PrvtRapsInstIndexType())
if mibBuilder.loadTexts: prvtRapsInstIndex.setStatus('current')
prvtRapsInstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRowStatus.setStatus('current')
prvtRapsInstMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 3), PrvtRapsModeType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstMode.setStatus('current')
prvtRapsInstRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 4), PrvtRapsRingIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingId.setStatus('current')
prvtRapsInstRole = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 5), PrvtRapsRoleType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRole.setStatus('current')
prvtRapsInstControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 6), PrvtRapsVlanIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstControlVlan.setStatus('current')
prvtRapsInstCfmDomainLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 7), PrvtRapsCfmLevelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstCfmDomainLevel.setStatus('current')
prvtRapsInstRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 8), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRevertiveMode.setStatus('current')
prvtRapsInstDisableVirtChan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 9), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstDisableVirtChan.setStatus('current')
prvtRapsInstHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 10), PrvtRapsHoldOffType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstHoldOffTimer.setStatus('current')
prvtRapsInstWaitToRestoreTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 11), PrvtRapsWaitTimerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstWaitToRestoreTimer.setStatus('current')
prvtRapsInstGuardTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 12), PrvtRapsGuardTimerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstGuardTimer.setStatus('current')
prvtRapsInstWaitToBlockTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 13), PrvtRapsBlockTimerType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstWaitToBlockTimer.setStatus('current')
prvtRapsInstShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 14), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstShutdown.setStatus('current')
prvtRapsInstClear = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 15), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstClear.setStatus('current')
prvtRapsInstOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 16), PrvtRapsInstStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstOperStatus.setStatus('current')
prvtRapsInstRapsState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 17), PrvtRapsStatesType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstRapsState.setStatus('current')
prvtRapsInstTopPriCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 18), PrvtRapsTopPriCmdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstTopPriCmd.setStatus('current')
prvtRapsInstDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstDescription.setStatus('current')
prvtRapsInstControlProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("raps", 0), ("vpls", 1))).clone('raps')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstControlProtocol.setStatus('current')
prvtRapsInstMonVlanTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 2), )
if mibBuilder.loadTexts: prvtRapsInstMonVlanTable.setStatus('current')
prvtRapsInstMonVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 2, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstMonVlanId"))
if mibBuilder.loadTexts: prvtRapsInstMonVlanEntry.setStatus('current')
prvtRapsInstMonVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 2, 1, 1), PrvtRapsVlanIdType())
if mibBuilder.loadTexts: prvtRapsInstMonVlanId.setStatus('current')
prvtRapsInstMonVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstMonVlanRowStatus.setStatus('current')
prvtRapsInstRingPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3), )
if mibBuilder.loadTexts: prvtRapsInstRingPortTable.setStatus('current')
prvtRapsInstRingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstRingPortIndex"))
if mibBuilder.loadTexts: prvtRapsInstRingPortEntry.setStatus('current')
prvtRapsInstRingPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: prvtRapsInstRingPortIndex.setStatus('current')
prvtRapsInstRingPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortRowStatus.setStatus('current')
prvtRapsInstRingPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortIfIndex.setStatus('current')
prvtRapsInstRingPortMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 4), PrvtRapsMepIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortMep.setStatus('current')
prvtRapsInstRingPortRpl = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortRpl.setStatus('current')
prvtRapsInstRingPortManSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 6), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortManSwitch.setStatus('current')
prvtRapsInstRingPortForcedSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 7), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortForcedSwitch.setStatus('current')
prvtRapsInstRingPortMonitoringMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 8), PrvtRapsMonitoringMethodType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortMonitoringMethod.setStatus('current')
prvtRapsInstRingLagTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4), )
if mibBuilder.loadTexts: prvtRapsInstRingLagTable.setStatus('current')
prvtRapsInstRingLagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstRingLagIndex"))
if mibBuilder.loadTexts: prvtRapsInstRingLagEntry.setStatus('current')
prvtRapsInstRingLagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: prvtRapsInstRingLagIndex.setStatus('current')
prvtRapsInstRingLagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagRowStatus.setStatus('current')
prvtRapsInstRingLagId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 3), PrvtRapsLinkAggIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagId.setStatus('current')
prvtRapsInstRingLagMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 4), PrvtRapsMepIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagMep.setStatus('current')
prvtRapsInstRingLagRpl = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagRpl.setStatus('current')
prvtRapsInstRingLagManSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 6), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagManSwitch.setStatus('current')
prvtRapsInstRingLagForcedSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 7), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagForcedSwitch.setStatus('current')
prvtRapsInstPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5), )
if mibBuilder.loadTexts: prvtRapsInstPortStatusTable.setStatus('current')
prvtRapsInstPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstPortStatusIfIndex"))
if mibBuilder.loadTexts: prvtRapsInstPortStatusEntry.setStatus('current')
prvtRapsInstPortStatusIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 1), PrvtRapsIfIndexOrAgIdType())
if mibBuilder.loadTexts: prvtRapsInstPortStatusIfIndex.setStatus('current')
prvtRapsInstPortStatusLink = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 2), PrvtRapsLinkOperStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstPortStatusLink.setStatus('current')
prvtRapsInstPortStatusRemoteMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 3), PrvtRapsMepIdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstPortStatusRemoteMep.setStatus('current')
prvtRapsInstPortStatusRcvdNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstPortStatusRcvdNodeId.setStatus('current')
prvtRapsInstPortStatusRcvdCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 5), PrvtRapsReceivedCommandType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstPortStatusRcvdCmd.setStatus('current')
prvtRapsInstPortStatusRcvdInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 6), PrvtRapsReceivedInfoType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstPortStatusRcvdInfo.setStatus('current')
prvtRapsInstSubRingTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6), )
if mibBuilder.loadTexts: prvtRapsInstSubRingTable.setStatus('current')
prvtRapsInstSubRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstSubRingIndex"))
if mibBuilder.loadTexts: prvtRapsInstSubRingEntry.setStatus('current')
prvtRapsInstSubRingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 1), PrvtRapsInstIndexType())
if mibBuilder.loadTexts: prvtRapsInstSubRingIndex.setStatus('current')
prvtRapsInstSubRingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingRowStatus.setStatus('current')
prvtRapsInstSubRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 3), PrvtRapsRingIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingId.setStatus('current')
prvtRapsInstSubRingRole = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 4), PrvtRapsRoleType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingRole.setStatus('current')
prvtRapsInstSubRingVirtChanVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 5), PrvtRapsVlanIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingVirtChanVlan.setStatus('current')
prvtRapsInstSubRingRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingRevertiveMode.setStatus('current')
prvtRapsInstSubRingHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 7), PrvtRapsHoldOffType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingHoldOffTimer.setStatus('current')
prvtRapsInstSubRingWaitTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 8), PrvtRapsWaitTimerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingWaitTimer.setStatus('current')
prvtRapsInstSubRingGuardTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 9), PrvtRapsGuardTimerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingGuardTimer.setStatus('current')
prvtRapsInstSubRingBlockTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 10), PrvtRapsBlockTimerType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingBlockTimer.setStatus('current')
prvtRapsInstSubRingPropTopChng = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 11), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingPropTopChng.setStatus('current')
prvtRapsInstSubRingShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 12), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingShutdown.setStatus('current')
prvtRapsInstSubRingClear = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 13), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingClear.setStatus('current')
prvtRapsInstSubRingManualSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 14), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingManualSwitch.setStatus('current')
prvtRapsInstSubRingForcedSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 15), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingForcedSwitch.setStatus('current')
prvtRapsInstSubRingOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 16), PrvtRapsInstStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingOperStatus.setStatus('current')
prvtRapsInstSubRingRapsState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 17), PrvtRapsStatesType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingRapsState.setStatus('current')
prvtRapsInstSubRingTopPriCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 18), PrvtRapsTopPriCmdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingTopPriCmd.setStatus('current')
prvtRapsInstSubRingPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingPortName.setStatus('current')
prvtRapsInstSubRingLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 20), PrvtRapsLinkOperStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingLinkStatus.setStatus('current')
prvtRapsInstSubRingRcvdNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 21), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingRcvdNodeId.setStatus('current')
prvtRapsInstSubRingRcvdCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 22), PrvtRapsReceivedCommandType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingRcvdCmd.setStatus('current')
prvtRapsInstSubRingRcvdInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 23), PrvtRapsReceivedInfoType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingRcvdInfo.setStatus('current')
prvtRapsInstSubRingDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingDescription.setStatus('current')
prvtRapsInstSubRingVcRcvdNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 25), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingVcRcvdNodeId.setStatus('current')
prvtRapsInstSubRingVcRcvdCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 26), PrvtRapsReceivedCommandType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingVcRcvdCmd.setStatus('current')
prvtRapsInstSubRingVcRcvdInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 27), PrvtRapsReceivedInfoType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingVcRcvdInfo.setStatus('current')
prvtRapsInstSubRingVirtChanSvc = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 28), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967294))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingVirtChanSvc.setStatus('current')
prvtRapsInstSubRingControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 29), PrvtRapsVlanIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingControlVlan.setStatus('current')
prvtRapsInstSubRingPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7), )
if mibBuilder.loadTexts: prvtRapsInstSubRingPortTable.setStatus('current')
prvtRapsInstSubRingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstSubRingIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtRapsInstSubRingPortEntry.setStatus('current')
prvtRapsInstSubRingPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingPortRowStatus.setStatus('current')
prvtRapsInstSubRingPortMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7, 1, 2), PrvtRapsMepIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingPortMep.setStatus('current')
prvtRapsInstSubRingPortRpl = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingPortRpl.setStatus('current')
prvtRapsInstSubRingPortMonitoringMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7, 1, 4), PrvtRapsMonitoringMethodType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingPortMonitoringMethod.setStatus('current')
prvtRapsInstSubRingLagTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8), )
if mibBuilder.loadTexts: prvtRapsInstSubRingLagTable.setStatus('current')
prvtRapsInstSubRingLagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstSubRingIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstSubRingLagId"))
if mibBuilder.loadTexts: prvtRapsInstSubRingLagEntry.setStatus('current')
prvtRapsInstSubRingLagId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1, 1), PrvtRapsLinkAggIdType())
if mibBuilder.loadTexts: prvtRapsInstSubRingLagId.setStatus('current')
prvtRapsInstSubRingLagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingLagRowStatus.setStatus('current')
prvtRapsInstSubRingLagMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1, 3), PrvtRapsMepIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingLagMep.setStatus('current')
prvtRapsInstSubRingLagRpl = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingLagRpl.setStatus('current')
prvtRapsInstSubRingLagMonitoringMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1, 5), PrvtRapsMonitoringMethodType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingLagMonitoringMethod.setStatus('current')
prvtRapsDefectAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 0, 1)).setObjects(("PRVT-RAPS-MIB", "prvtRapsInstOperStatus"), ("PRVT-RAPS-MIB", "prvtRapsInstControlVlan"))
if mibBuilder.loadTexts: prvtRapsDefectAlarm.setStatus('current')
prvtRapsSwitchoverAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 0, 2)).setObjects(("PRVT-RAPS-MIB", "prvtRapsInstRapsState"), ("PRVT-RAPS-MIB", "prvtRapsInstControlVlan"))
if mibBuilder.loadTexts: prvtRapsSwitchoverAlarm.setStatus('current')
prvtRapsInstSubRingDefectAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 0, 3)).setObjects(("PRVT-RAPS-MIB", "prvtRapsInstSubRingOperStatus"), ("PRVT-RAPS-MIB", "prvtRapsInstSubRingControlVlan"))
if mibBuilder.loadTexts: prvtRapsInstSubRingDefectAlarm.setStatus('current')
prvtRapsInstSubRingSwitchoverAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 0, 4)).setObjects(("PRVT-RAPS-MIB", "prvtRapsInstSubRingRapsState"), ("PRVT-RAPS-MIB", "prvtRapsInstSubRingControlVlan"))
if mibBuilder.loadTexts: prvtRapsInstSubRingSwitchoverAlarm.setStatus('current')
mibBuilder.exportSymbols("PRVT-RAPS-MIB", prvtRapsInstMonVlanId=prvtRapsInstMonVlanId, prvtRapsInstEntry=prvtRapsInstEntry, prvtRapsInstControlVlan=prvtRapsInstControlVlan, PrvtRapsCfmLevelType=PrvtRapsCfmLevelType, prvtRapsInstSubRingManualSwitch=prvtRapsInstSubRingManualSwitch, prvtRapsInstRingLagRpl=prvtRapsInstRingLagRpl, PrvtRapsWaitTimerType=PrvtRapsWaitTimerType, prvtRapsInstSubRingRowStatus=prvtRapsInstSubRingRowStatus, prvtRapsInstSubRingIndex=prvtRapsInstSubRingIndex, prvtRapsInstSubRingShutdown=prvtRapsInstSubRingShutdown, prvtRapsInstSubRingDescription=prvtRapsInstSubRingDescription, prvtRapsInstSubRingPortMep=prvtRapsInstSubRingPortMep, prvtRapsInstSubRingVirtChanVlan=prvtRapsInstSubRingVirtChanVlan, PrvtRapsStatesType=PrvtRapsStatesType, PrvtRapsGuardTimerType=PrvtRapsGuardTimerType, prvtRapsInstPortStatusLink=prvtRapsInstPortStatusLink, prvtRapsInstSubRingClear=prvtRapsInstSubRingClear, prvtRapsInstRingLagRowStatus=prvtRapsInstRingLagRowStatus, prvtRapsInstRingPortManSwitch=prvtRapsInstRingPortManSwitch, PrvtRapsMepIdType=PrvtRapsMepIdType, PrvtRapsRingIdType=PrvtRapsRingIdType, prvtRapsInstRole=prvtRapsInstRole, prvtRapsInstPortStatusRemoteMep=prvtRapsInstPortStatusRemoteMep, prvtRapsInstOperStatus=prvtRapsInstOperStatus, prvtRapsInstMonVlanRowStatus=prvtRapsInstMonVlanRowStatus, prvtRapsInstPortStatusEntry=prvtRapsInstPortStatusEntry, prvtRapsInstRapsState=prvtRapsInstRapsState, prvtRapsSwitchoverAlarm=prvtRapsSwitchoverAlarm, PrvtRapsActionType=PrvtRapsActionType, prvtRapsInstCfmDomainLevel=prvtRapsInstCfmDomainLevel, prvtRapsMIBNotifications=prvtRapsMIBNotifications, PrvtRapsModeType=PrvtRapsModeType, PrvtRapsLinkAggIdType=PrvtRapsLinkAggIdType, prvtRapsInstSubRingLagTable=prvtRapsInstSubRingLagTable, prvtRapsInstRingPortForcedSwitch=prvtRapsInstRingPortForcedSwitch, prvtRapsInstSubRingRevertiveMode=prvtRapsInstSubRingRevertiveMode, prvtRapsInstPortStatusTable=prvtRapsInstPortStatusTable, prvtRapsInstSubRingLagMep=prvtRapsInstSubRingLagMep, prvtRapsInstSubRingTable=prvtRapsInstSubRingTable, prvtRapsInstSubRingRcvdCmd=prvtRapsInstSubRingRcvdCmd, prvtRapsInstRevertiveMode=prvtRapsInstRevertiveMode, PrvtRapsInstIndexType=PrvtRapsInstIndexType, prvtRapsInstRingPortMep=prvtRapsInstRingPortMep, prvtRapsInstTable=prvtRapsInstTable, prvtRapsInstSubRingPropTopChng=prvtRapsInstSubRingPropTopChng, PrvtRapsTopPriCmdType=PrvtRapsTopPriCmdType, prvtRapsInstMonVlanTable=prvtRapsInstMonVlanTable, prvtRapsInstControlProtocol=prvtRapsInstControlProtocol, prvtRapsInstSubRingPortMonitoringMethod=prvtRapsInstSubRingPortMonitoringMethod, PrvtRapsReceivedInfoType=PrvtRapsReceivedInfoType, prvtRapsInstRingLagForcedSwitch=prvtRapsInstRingLagForcedSwitch, prvtRapsInstSubRingRcvdInfo=prvtRapsInstSubRingRcvdInfo, prvtRapsInstRingPortMonitoringMethod=prvtRapsInstRingPortMonitoringMethod, prvtRapsInstSubRingRcvdNodeId=prvtRapsInstSubRingRcvdNodeId, PrvtRapsVlanIdType=PrvtRapsVlanIdType, prvtRapsInstSubRingLagEntry=prvtRapsInstSubRingLagEntry, prvtRapsInstRingId=prvtRapsInstRingId, prvtRapsInstMode=prvtRapsInstMode, prvtRapsDefectAlarm=prvtRapsDefectAlarm, prvtRapsInstMonVlanEntry=prvtRapsInstMonVlanEntry, prvtRapsInstRingPortIndex=prvtRapsInstRingPortIndex, PrvtRapsReceivedCommandType=PrvtRapsReceivedCommandType, prvtRapsInstSubRingBlockTimer=prvtRapsInstSubRingBlockTimer, prvtRapsInstRingPortEntry=prvtRapsInstRingPortEntry, prvtRapsInstSubRingPortRpl=prvtRapsInstSubRingPortRpl, PrvtRapsHoldOffType=PrvtRapsHoldOffType, prvtRapsInstSubRingPortEntry=prvtRapsInstSubRingPortEntry, prvtRapsInstDescription=prvtRapsInstDescription, prvtRapsInstRingPortTable=prvtRapsInstRingPortTable, prvtRapsInstGuardTimer=prvtRapsInstGuardTimer, prvtRapsInstSubRingVcRcvdNodeId=prvtRapsInstSubRingVcRcvdNodeId, prvtRapsInstSubRingRole=prvtRapsInstSubRingRole, prvtRapsInstPortStatusRcvdInfo=prvtRapsInstPortStatusRcvdInfo, prvtRapsInstRingLagTable=prvtRapsInstRingLagTable, prvtRapsMIB=prvtRapsMIB, prvtRapsInstSubRingTopPriCmd=prvtRapsInstSubRingTopPriCmd, prvtRapsInstSubRingLagMonitoringMethod=prvtRapsInstSubRingLagMonitoringMethod, PrvtRapsRoleType=PrvtRapsRoleType, prvtRapsInstSubRingOperStatus=prvtRapsInstSubRingOperStatus, PrvtRapsInstStatusType=PrvtRapsInstStatusType, prvtRapsInstHoldOffTimer=prvtRapsInstHoldOffTimer, prvtRapsInstSubRingId=prvtRapsInstSubRingId, prvtRapsInstTopPriCmd=prvtRapsInstTopPriCmd, prvtRapsInstSubRingControlVlan=prvtRapsInstSubRingControlVlan, prvtRapsInstRingPortRpl=prvtRapsInstRingPortRpl, prvtRapsInstSubRingLagRpl=prvtRapsInstSubRingLagRpl, prvtRapsInstSubRingWaitTimer=prvtRapsInstSubRingWaitTimer, prvtRapsInstSubRingVcRcvdInfo=prvtRapsInstSubRingVcRcvdInfo, prvtRapsInstRingLagEntry=prvtRapsInstRingLagEntry, PrvtRapsLinkOperStatusType=PrvtRapsLinkOperStatusType, prvtRapsInstClear=prvtRapsInstClear, prvtRapsInstShutdown=prvtRapsInstShutdown, prvtRapsInstDisableVirtChan=prvtRapsInstDisableVirtChan, prvtRapsInstRingLagId=prvtRapsInstRingLagId, prvtRapsInstPortStatusRcvdCmd=prvtRapsInstPortStatusRcvdCmd, prvtRapsInstSubRingPortRowStatus=prvtRapsInstSubRingPortRowStatus, prvtRapsInstSubRingEntry=prvtRapsInstSubRingEntry, prvtRapsInstPortStatusRcvdNodeId=prvtRapsInstPortStatusRcvdNodeId, prvtRapsInstSubRingPortName=prvtRapsInstSubRingPortName, prvtRapsInstRingLagManSwitch=prvtRapsInstRingLagManSwitch, prvtRapsInstSubRingVirtChanSvc=prvtRapsInstSubRingVirtChanSvc, prvtRapsInstRingLagMep=prvtRapsInstRingLagMep, prvtRapsInstSubRingLagId=prvtRapsInstSubRingLagId, prvtRapsInstIndex=prvtRapsInstIndex, PYSNMP_MODULE_ID=prvtRapsMIB, prvtRapsInstSubRingVcRcvdCmd=prvtRapsInstSubRingVcRcvdCmd, prvtRapsInstSubRingRapsState=prvtRapsInstSubRingRapsState, prvtRapsInstSubRingSwitchoverAlarm=prvtRapsInstSubRingSwitchoverAlarm, prvtRapsInstWaitToRestoreTimer=prvtRapsInstWaitToRestoreTimer, prvtRapsInstRowStatus=prvtRapsInstRowStatus, prvtRapsInstWaitToBlockTimer=prvtRapsInstWaitToBlockTimer, prvtRapsInstSubRingGuardTimer=prvtRapsInstSubRingGuardTimer, prvtRapsInstRingLagIndex=prvtRapsInstRingLagIndex, prvtRapsInstSubRingDefectAlarm=prvtRapsInstSubRingDefectAlarm, prvtRapsMIBObjects=prvtRapsMIBObjects, prvtRapsInstSubRingLinkStatus=prvtRapsInstSubRingLinkStatus, prvtRapsInstSubRingHoldOffTimer=prvtRapsInstSubRingHoldOffTimer, prvtRapsInstSubRingForcedSwitch=prvtRapsInstSubRingForcedSwitch, prvtRapsInstRingPortRowStatus=prvtRapsInstRingPortRowStatus, prvtRapsInstPortStatusIfIndex=prvtRapsInstPortStatusIfIndex, prvtRapsInstSubRingLagRowStatus=prvtRapsInstSubRingLagRowStatus, PrvtRapsMonitoringMethodType=PrvtRapsMonitoringMethodType, PrvtRapsIfIndexOrAgIdType=PrvtRapsIfIndexOrAgIdType, prvtRapsInstSubRingPortTable=prvtRapsInstSubRingPortTable, PrvtRapsBlockTimerType=PrvtRapsBlockTimerType, prvtRapsInstRingPortIfIndex=prvtRapsInstRingPortIfIndex)
