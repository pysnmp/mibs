#
# PySNMP MIB module PRVT-RAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-RAPS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 16:43:37 2021
# On host fv-az126-355 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
serviceAccessSwitch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "serviceAccessSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, NotificationType, Counter64, MibIdentifier, Unsigned32, IpAddress, Bits, TimeTicks, ModuleIdentity, Gauge32, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "NotificationType", "Counter64", "MibIdentifier", "Unsigned32", "IpAddress", "Bits", "TimeTicks", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "MacAddress", "RowStatus")
prvtRapsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 7, 4))
prvtRapsMIB.setRevisions(('2010-11-11 00:00', '2010-03-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtRapsMIB.setRevisionsDescriptions(('Added description for rings and subrings.', 'Initial version.',))
if mibBuilder.loadTexts: prvtRapsMIB.setLastUpdated('201011110000Z')
if mibBuilder.loadTexts: prvtRapsMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtRapsMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtRapsMIB.setDescription('The SNMP MIB module for Ring Automatic Protection Switching (G.8032).')
class PrvtRapsInstIndexType(TextualConvention, Unsigned32):
    description = 'A Ring APS instance index.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 10)

class PrvtRapsRingIdType(TextualConvention, Integer32):
    description = 'Ring identifier.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class PrvtRapsVlanIdType(TextualConvention, Integer32):
    description = 'VLAN identifier'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class PrvtRapsLinkOperStatusType(TextualConvention, Integer32):
    description = 'Operational status of a link.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("up", 0), ("blocked", 1), ("failed", 2), ("na", 3))

class PrvtRapsMepIdType(TextualConvention, Integer32):
    description = 'A maintenance entity group end point identifier.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8191)

class PrvtRapsLinkAggIdType(TextualConvention, Integer32):
    description = 'A link aggregation identifier.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 14)

class PrvtRapsHoldOffType(TextualConvention, Integer32):
    description = 'Hold-off timer value in milliseconds.\n         Valid values are increments of 100 milliseconds.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10000)

class PrvtRapsWaitTimerType(TextualConvention, Integer32):
    description = 'Wait to Restore timer value in minutes.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 12)

class PrvtRapsCfmLevelType(TextualConvention, Integer32):
    description = 'Connectivity Fault Management level.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class PrvtRapsGuardTimerType(TextualConvention, Integer32):
    description = 'Guard timer value in milliseconds.\n         Valid values are increments of 10 milliseconds.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(10, 2000)

class PrvtRapsBlockTimerType(TextualConvention, Integer32):
    description = 'Wait to Block timer value in milliseconds.\n         This time is actually the Guard Timer + 5 seconds.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(5010, 7000)

class PrvtRapsModeType(TextualConvention, Integer32):
    description = 'The G.8032 mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("version1", 1), ("version2", 2))

class PrvtRapsRoleType(TextualConvention, Integer32):
    description = 'The role of a node inside a ring.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("simpleNode", 0), ("rplNeighbor", 1), ("rplOwner", 2))

class PrvtRapsInstStatusType(TextualConvention, Integer32):
    description = 'R-APS instance operational status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrvtRapsStatesType(TextualConvention, Integer32):
    description = 'R-APS instance states.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("init", 0), ("idle", 1), ("protection", 2), ("manualSwitch", 3), ("forcedSwitch", 4), ("pending", 5))

class PrvtRapsReceivedCommandType(TextualConvention, Integer32):
    description = 'Request/State field of received R-APS message.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 7, 11, 13, 14, 16))
    namedValues = NamedValues(("noRequest", 0), ("manualSwitch", 7), ("signalFail", 11), ("forcedSwitch", 13), ("event", 14), ("na", 16))

class PrvtRapsReceivedInfoType(TextualConvention, Bits):
    description = 'Bits field of received R-APS message.'
    status = 'current'
    namedValues = NamedValues(("bpr", 0), ("dnf", 1), ("rp", 2))

class PrvtRapsTopPriCmdType(TextualConvention, Integer32):
    description = 'Top Priority Request and Status Values.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("clear", 0), ("forcedSwitch", 1), ("remoteForcedSwitch", 2), ("signalFail", 3), ("signalFailRecover", 4), ("remoteSignalFail", 5), ("remoteManualSwitch", 6), ("manualSwitch", 7), ("wtrExpire", 8), ("wtrRunning", 9), ("wtbExpire", 10), ("wtbRunning", 11), ("noRequestRplBlocked", 12), ("noRequest", 13), ("na", 14))

class PrvtRapsActionType(TextualConvention, Integer32):
    description = "Used to perform an action.\n         Setting to 'performAction' will cause the action to be performed.\n         Setting to 'idle' (or any other value except 'performAction') has\n         no effect (no action is performed).\n         Reads will always return 'idle'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("idle", 1), ("performAction", 2))

class PrvtRapsIfIndexOrAgIdType(TextualConvention, Integer32):
    description = 'The ifIndex of a physical port or the ID of a LAG interface.\n         LAG interfaces have values 1..14.\n         Physical ports (ifIndex) have values > 1000.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class PrvtRapsMonitoringMethodType(TextualConvention, Integer32):
    description = 'Ethernet ring protection monitoring methods'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ccm", 1), ("link-status", 2))

prvtRapsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 0))
prvtRapsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1))
prvtRapsInstTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1), )
if mibBuilder.loadTexts: prvtRapsInstTable.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstTable.setDescription('R-APS Instance table.\n         Each entry in this table defines an instance of a Ring APS.')
prvtRapsInstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"))
if mibBuilder.loadTexts: prvtRapsInstEntry.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstEntry.setDescription('An entry in prvtRapsInstTable.')
prvtRapsInstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 1), PrvtRapsInstIndexType())
if mibBuilder.loadTexts: prvtRapsInstIndex.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstIndex.setDescription('An arbitrary index uniquely identifying a Ring APS instance.')
prvtRapsInstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRowStatus.setDescription('The RowStatus for this R-APS instance.')
prvtRapsInstMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 3), PrvtRapsModeType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstMode.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstMode.setDescription("The G.8032 mode for this R-APS instance.\n         Only applicable when main ring's control protocol is raps (prvtRapsInstControlProtocol equals 'raps').\n         In version 1 mode (prvtRapsInstMode equals 'version1'),\n         ring ID (prvtRapsInstRingId) must be 1.")
prvtRapsInstRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 4), PrvtRapsRingIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingId.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingId.setDescription("The Ring ID for this R-APS instance.\n         Only applicable when main ring's control protocol is raps (prvtRapsInstControlProtocol equals 'raps').\n         In version 1 mode (prvtRapsInstMode equals 'version1'),\n         ring ID (prvtRapsInstRingId) must be 1.")
prvtRapsInstRole = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 5), PrvtRapsRoleType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRole.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRole.setDescription('The role of the node for this R-APS instance.\n         Must perform shutdown to change this object.')
prvtRapsInstControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 6), PrvtRapsVlanIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstControlVlan.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstControlVlan.setDescription("The control VLAN for this R-APS instance.\n         When main ring's control protocol is vpls (prvtRapsInstControlProtocol equals 'vpls'), this\n         should be set equal to the ring's instance ID (prvtRapsInstIndex).\n         This object must be set to the ID of an existing VLAN.\n         Each R-APS instance must use a unique VLAN for the control VLAN.\n         Must perform shutdown to change this object.")
prvtRapsInstCfmDomainLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 7), PrvtRapsCfmLevelType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstCfmDomainLevel.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstCfmDomainLevel.setDescription('The CFM domain level for this R-APS instance.\n         Must perform shutdown to change this object.')
prvtRapsInstRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 8), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRevertiveMode.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRevertiveMode.setDescription("Set to 'true' to select revertive behavior for this R-APS instance.\n         Only applicable when main ring's control protocol is raps (prvtRapsInstControlProtocol equals 'raps').\n         Non-revertive behavior is not available in version 1 mode.")
prvtRapsInstDisableVirtChan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 9), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstDisableVirtChan.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstDisableVirtChan.setDescription("Set to 'true' to select that the node is part of a sub-ring without\n         a RAPS virtual channel.\n         Only applicable when main ring's control protocol is raps (prvtRapsInstControlProtocol equals 'raps').\n         Must be set 'false' when in version 1 mode.")
prvtRapsInstHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 10), PrvtRapsHoldOffType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstHoldOffTimer.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstHoldOffTimer.setDescription("The hold-off timer time-out value for this R-APS instance.\n         Only applicable when main ring's control protocol is raps (prvtRapsInstControlProtocol equals 'raps').")
prvtRapsInstWaitToRestoreTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 11), PrvtRapsWaitTimerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstWaitToRestoreTimer.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstWaitToRestoreTimer.setDescription("The wait-to-restore timer time-out value for this R-APS instance.\n         Only applicable when main ring's control protocol is raps (prvtRapsInstControlProtocol equals 'raps').")
prvtRapsInstGuardTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 12), PrvtRapsGuardTimerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstGuardTimer.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstGuardTimer.setDescription("The guard timer time-out value for this R-APS instance.\n         Only applicable when main ring's control protocol is raps (prvtRapsInstControlProtocol equals 'raps').")
prvtRapsInstWaitToBlockTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 13), PrvtRapsBlockTimerType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstWaitToBlockTimer.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstWaitToBlockTimer.setDescription('The wait to block timer time-out value for this sub-ring.')
prvtRapsInstShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 14), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstShutdown.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstShutdown.setDescription("Set to 'true' to de-activate this R-APS instance.")
prvtRapsInstClear = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 15), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstClear.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstClear.setDescription('Sends the Clear command to this R-APS instance.')
prvtRapsInstOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 16), PrvtRapsInstStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstOperStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstOperStatus.setDescription('The operational status of this R-APS instance.')
prvtRapsInstRapsState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 17), PrvtRapsStatesType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstRapsState.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRapsState.setDescription('The current state for this R-APS instance.')
prvtRapsInstTopPriCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 18), PrvtRapsTopPriCmdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstTopPriCmd.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstTopPriCmd.setDescription('The received Top Priority Request and Status value for this R-APS instance.')
prvtRapsInstDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstDescription.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstDescription.setDescription('RAPS instance description.')
prvtRapsInstControlProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("raps", 0), ("vpls", 1))).clone('raps')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstControlProtocol.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstControlProtocol.setDescription('The protocol that controls the main ring.')
prvtRapsInstMonVlanTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 2), )
if mibBuilder.loadTexts: prvtRapsInstMonVlanTable.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstMonVlanTable.setDescription("Monitor VLAN Table\n         Each entry in this table defines a VLAN that will be monitored.\n         Only applicable when main ring's control protocol is raps (prvtRapsInstControlProtocol equals 'raps').")
prvtRapsInstMonVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 2, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstMonVlanId"))
if mibBuilder.loadTexts: prvtRapsInstMonVlanEntry.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstMonVlanEntry.setDescription('An entry in prvtRapsInstMonVlanTable.')
prvtRapsInstMonVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 2, 1, 1), PrvtRapsVlanIdType())
if mibBuilder.loadTexts: prvtRapsInstMonVlanId.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstMonVlanId.setDescription('Uniquely identifies a VLAN to be monitored.\n         This object must be the ID of an existing VLAN.\n         Must not be the same VLAN as the control VLAN (prvtRapsInstControlVlan).')
prvtRapsInstMonVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstMonVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstMonVlanRowStatus.setDescription('The RowStatus for this monitored VLAN.')
prvtRapsInstRingPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3), )
if mibBuilder.loadTexts: prvtRapsInstRingPortTable.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingPortTable.setDescription("R-APS Instance Ring Port Table.\n         Each entry in this table defines a port belonging to a R-APS instance.\n         Only applicable when main ring's control protocol is raps (prvtRapsInstControlProtocol equals 'raps').\n         Exactly two interfaces must be defined per instance. This includes physical\n         ports (defined in prvtRapsInstRingPortTable) and LAG interfaces (defined\n         in prvtRapsInstRingLagTable). In the case when one physical port and one\n         LAG interface is used, the two port index values must be unique (i.e.\n         prvtRapsInstRingPortIndex must not equal prvtRapsInstRingLagIndex)")
prvtRapsInstRingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstRingPortIndex"))
if mibBuilder.loadTexts: prvtRapsInstRingPortEntry.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingPortEntry.setDescription('An entry in prvtRapsInstRingPortTable.')
prvtRapsInstRingPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: prvtRapsInstRingPortIndex.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingPortIndex.setDescription('An arbitrary index uniquely identifying a physical port belonging to a\n         R-APS instance.\n         When a physical port and a LAG port are used in the same R-APS instance,\n         the two ports must use unique index values (i.e.\n         prvtRapsInstRingPortIndex must not equal prvtRapsInstRingLagIndex).')
prvtRapsInstRingPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingPortRowStatus.setDescription('The RowStatus for this ring port.')
prvtRapsInstRingPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingPortIfIndex.setDescription('The ifIndex of the physical port assigned to this ring port.\n         No two ports within the same ring instance can use the same physical port.')
prvtRapsInstRingPortMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 4), PrvtRapsMepIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortMep.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingPortMep.setDescription('The peer maintenance entity group end point ID that should monitor this ring port.\n         No two ports within the same ring instance can use the same MEP ID.')
prvtRapsInstRingPortRpl = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortRpl.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingPortRpl.setDescription("Set to 'true' to define this ring port as a Ring Protection Link port.\n         Exactly one RPL port must be defined when ring role (prvtRapsInstRole)\n         is not 'simpleNode'.\n         In 'simpleNode' role, no RPL ports must be defined.")
prvtRapsInstRingPortManSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 6), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortManSwitch.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingPortManSwitch.setDescription('Send the Manual Switch command to this ring port.')
prvtRapsInstRingPortForcedSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 7), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortForcedSwitch.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingPortForcedSwitch.setDescription('Send the Forced Switch command to this ring port.')
prvtRapsInstRingPortMonitoringMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 3, 1, 8), PrvtRapsMonitoringMethodType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingPortMonitoringMethod.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingPortMonitoringMethod.setDescription('Ethernet ring protection monitoring methods')
prvtRapsInstRingLagTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4), )
if mibBuilder.loadTexts: prvtRapsInstRingLagTable.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingLagTable.setDescription("R-APS Instance Ring LAG Table\n         Each entry in this table defines a Link Aggregation Group interface belonging\n         to a R-APS instance.\n         Only applicable when main ring's control protocol is raps (prvtRapsInstControlProtocol equals 'raps').\n         Exactly two interfaces must be defined per instance. This includes physical\n         ports (defined in prvtRapsInstRingPortTable) and LAG interfaces (defined\n         in prvtRapsInstRingLagTable).")
prvtRapsInstRingLagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstRingLagIndex"))
if mibBuilder.loadTexts: prvtRapsInstRingLagEntry.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingLagEntry.setDescription('An entry in prvtRapsInstRingLagTable.')
prvtRapsInstRingLagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
if mibBuilder.loadTexts: prvtRapsInstRingLagIndex.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingLagIndex.setDescription('An arbitrary index uniquely identifying a LAG interface belonging to a\n         R-APS instance.\n         When a physical port and a LAG port are used in the same R-APS instance,\n         the two ports must use unique index values (i.e.\n         prvtRapsInstRingPortIndex must not equal prvtRapsInstRingLagIndex).')
prvtRapsInstRingLagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingLagRowStatus.setDescription('The RowStatus for this LAG interface.')
prvtRapsInstRingLagId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 3), PrvtRapsLinkAggIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagId.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingLagId.setDescription('The ID of a LAG interface belonging to a R-APS instance.\n         This object must be set to the ID of an existing LAG interface.\n         No two LAG ports within the same ring instance can use the same LAG port.')
prvtRapsInstRingLagMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 4), PrvtRapsMepIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagMep.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingLagMep.setDescription('The peer maintenance entity group end point ID that should monitor this LAG interface.\n         No two LAG ports within the same ring instance can use the same MEP ID.')
prvtRapsInstRingLagRpl = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagRpl.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingLagRpl.setDescription("Set to 'true' to define this ring LAG port as a Ring Protection Link port.\n         Exactly one RPL port must be defined when ring role (prvtRapsInstRole)\n         is not 'simpleNode'.\n         In 'simpleNode' role, no RPL ports must be defined.")
prvtRapsInstRingLagManSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 6), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagManSwitch.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingLagManSwitch.setDescription('Send the Manual Switch command to this LAG interface.')
prvtRapsInstRingLagForcedSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 4, 1, 7), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstRingLagForcedSwitch.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstRingLagForcedSwitch.setDescription('Send the Forced Switch command to this LAG interface.')
prvtRapsInstPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5), )
if mibBuilder.loadTexts: prvtRapsInstPortStatusTable.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstPortStatusTable.setDescription('R-APS Instance Port Status Table\n         Each entry in this table gives status information concerning a\n         particular port (physical port or LAG interface port) belonging\n         to a R-APS instance.')
prvtRapsInstPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstPortStatusIfIndex"))
if mibBuilder.loadTexts: prvtRapsInstPortStatusEntry.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstPortStatusEntry.setDescription('An entry in prvtRapsInstPortStatusTable.')
prvtRapsInstPortStatusIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 1), PrvtRapsIfIndexOrAgIdType())
if mibBuilder.loadTexts: prvtRapsInstPortStatusIfIndex.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstPortStatusIfIndex.setDescription('Uniquely identifies a physical port (ifIndex) or a LAG port (LAG ID)\n         belonging to a R-APS instance.')
prvtRapsInstPortStatusLink = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 2), PrvtRapsLinkOperStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstPortStatusLink.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstPortStatusLink.setDescription('The operational status of this port.')
prvtRapsInstPortStatusRemoteMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 3), PrvtRapsMepIdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstPortStatusRemoteMep.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstPortStatusRemoteMep.setDescription('The maintenance entity group end point ID for the remote port connected to this port.')
prvtRapsInstPortStatusRcvdNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstPortStatusRcvdNodeId.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstPortStatusRcvdNodeId.setDescription('The MAC address of the remote R-APS device connected to this port.')
prvtRapsInstPortStatusRcvdCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 5), PrvtRapsReceivedCommandType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstPortStatusRcvdCmd.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstPortStatusRcvdCmd.setDescription('The command received on this port.')
prvtRapsInstPortStatusRcvdInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 5, 1, 6), PrvtRapsReceivedInfoType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstPortStatusRcvdInfo.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstPortStatusRcvdInfo.setDescription('The info received on this port.')
prvtRapsInstSubRingTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6), )
if mibBuilder.loadTexts: prvtRapsInstSubRingTable.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingTable.setDescription('R-APS Instance Sub-ring Table\n         Each entry in this table defines a sub-ring belonging to a R-APS instance.\n         Sub-rings are not available in version 1 mode.')
prvtRapsInstSubRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstSubRingIndex"))
if mibBuilder.loadTexts: prvtRapsInstSubRingEntry.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingEntry.setDescription('An entry in prvtRapsInstSubRingTable.')
prvtRapsInstSubRingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 1), PrvtRapsInstIndexType())
if mibBuilder.loadTexts: prvtRapsInstSubRingIndex.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingIndex.setDescription('An arbitrary index uniquely identifying a sub-ring for this R-APS instance.')
prvtRapsInstSubRingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingRowStatus.setDescription('The RowStatus for this sub-ring.')
prvtRapsInstSubRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 3), PrvtRapsRingIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingId.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingId.setDescription('The ring ID for this sub-ring.')
prvtRapsInstSubRingRole = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 4), PrvtRapsRoleType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingRole.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingRole.setDescription('The role of the node inside this sub-ring.\n         Must perform shutdown to change this object.')
prvtRapsInstSubRingVirtChanVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 5), PrvtRapsVlanIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingVirtChanVlan.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingVirtChanVlan.setDescription("Configures the virtual channel VLAN for this sub-ring.\n         Only applicable when main ring's control protocol is raps (prvtRapsInstControlProtocol equals 'raps').\n         Must be a VLAN from the prvtRapsInstMonVlanTable.\n         No two sub-rings can use the same VLAN for the virtual channel VLAN.")
prvtRapsInstSubRingRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingRevertiveMode.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingRevertiveMode.setDescription("Set to 'true' to select revertive behavior for this sub-ring.")
prvtRapsInstSubRingHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 7), PrvtRapsHoldOffType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingHoldOffTimer.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingHoldOffTimer.setDescription('The hold-off timer time-out value for this sub-ring.')
prvtRapsInstSubRingWaitTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 8), PrvtRapsWaitTimerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingWaitTimer.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingWaitTimer.setDescription('The wait-to-restore timer time-out value for this sub-ring.')
prvtRapsInstSubRingGuardTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 9), PrvtRapsGuardTimerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingGuardTimer.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingGuardTimer.setDescription('The guard timer time-out value for this sub-ring.')
prvtRapsInstSubRingBlockTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 10), PrvtRapsBlockTimerType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingBlockTimer.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingBlockTimer.setDescription('The wait to block timer time-out value for this sub-ring.')
prvtRapsInstSubRingPropTopChng = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 11), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingPropTopChng.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingPropTopChng.setDescription("Set to 'true' to enable topology change propagation for this sub-ring.")
prvtRapsInstSubRingShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 12), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingShutdown.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingShutdown.setDescription("Set to 'true' to de-activate this sub-ring.")
prvtRapsInstSubRingClear = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 13), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingClear.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingClear.setDescription('Send the Clear command to this sub-ring.')
prvtRapsInstSubRingManualSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 14), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingManualSwitch.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingManualSwitch.setDescription('Send the Manual Switch command to this sub-ring.')
prvtRapsInstSubRingForcedSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 15), PrvtRapsActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingForcedSwitch.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingForcedSwitch.setDescription('Send the Forced Switch command to this sub-ring.')
prvtRapsInstSubRingOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 16), PrvtRapsInstStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingOperStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingOperStatus.setDescription('The operational status of this sub-ring.')
prvtRapsInstSubRingRapsState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 17), PrvtRapsStatesType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingRapsState.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingRapsState.setDescription('The current state of this sub-ring.')
prvtRapsInstSubRingTopPriCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 18), PrvtRapsTopPriCmdType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingTopPriCmd.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingTopPriCmd.setDescription('The received Top Priority Request and Status value for this sub-ring.')
prvtRapsInstSubRingPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingPortName.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingPortName.setDescription('The textual name of the port belonging to this sub-ring.\n         For a physical port, the format is U/S/P.\n         For a LAG interface, the format is agX.')
prvtRapsInstSubRingLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 20), PrvtRapsLinkOperStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingLinkStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingLinkStatus.setDescription('The operational status of the port belonging to this sub-ring.')
prvtRapsInstSubRingRcvdNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 21), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingRcvdNodeId.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingRcvdNodeId.setDescription('The MAC address of the remote R-APS device connected to the port belonging to this sub-ring.')
prvtRapsInstSubRingRcvdCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 22), PrvtRapsReceivedCommandType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingRcvdCmd.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingRcvdCmd.setDescription('The command received on the port belonging to this sub-ring.')
prvtRapsInstSubRingRcvdInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 23), PrvtRapsReceivedInfoType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingRcvdInfo.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingRcvdInfo.setDescription('The info received on the port belonging to this sub-ring.')
prvtRapsInstSubRingDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingDescription.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingDescription.setDescription('RAPS instance sub-ring description.')
prvtRapsInstSubRingVcRcvdNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 25), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingVcRcvdNodeId.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingVcRcvdNodeId.setDescription('The MAC address of the remote R-APS device connected through the virtual channel.')
prvtRapsInstSubRingVcRcvdCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 26), PrvtRapsReceivedCommandType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingVcRcvdCmd.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingVcRcvdCmd.setDescription('The command received through the virtual channel belonging to this sub-ring.')
prvtRapsInstSubRingVcRcvdInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 27), PrvtRapsReceivedInfoType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRapsInstSubRingVcRcvdInfo.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingVcRcvdInfo.setDescription('The info received through the virtual channel belonging to this sub-ring.')
prvtRapsInstSubRingVirtChanSvc = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 28), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967294))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingVirtChanSvc.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingVirtChanSvc.setDescription("Configure the virtual channel service for this sub-ring.\n         Only applicable when main ring's control protocol is vpls (prvtRapsInstControlProtocol equals 'vpls').\n         Must be a service ID from PRVT-SERV-MIB::serviceId.\n         No two sub-rings can use the same service ID for the virtual channel service.")
prvtRapsInstSubRingControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 6, 1, 29), PrvtRapsVlanIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingControlVlan.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingControlVlan.setDescription('The control VLAN for this sub-ring.\n         This object must be set to the ID of an existing VLAN.\n         Must not be the same VLAN as a monitored VLAN in any instance.\n         Must perform shutdown to change this object.')
prvtRapsInstSubRingPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7), )
if mibBuilder.loadTexts: prvtRapsInstSubRingPortTable.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingPortTable.setDescription('R-APS Instance Sub-ring port Table\n         An entry in this table defines a physical port belonging to a sub-ring.\n         Exactly one interface must be defined per sub-ring. This includes physical\n         ports (defined in prvtRapsInstSubRingPortTable) and LAG interfaces (defined\n         in prvtRapsInstSubRingLagTable).\n         A sub-ring port can not be part of the main ring.')
prvtRapsInstSubRingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstSubRingIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtRapsInstSubRingPortEntry.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingPortEntry.setDescription('An entry in prvtRapsInstSubRingPortTable.')
prvtRapsInstSubRingPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingPortRowStatus.setDescription('The RowStatus for this sub-ring port.')
prvtRapsInstSubRingPortMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7, 1, 2), PrvtRapsMepIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingPortMep.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingPortMep.setDescription('The peer maintenance entity group end point ID that should monitor this sub-ring port.\n         A sub-ring MEP can not be used in another ring.')
prvtRapsInstSubRingPortRpl = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingPortRpl.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingPortRpl.setDescription("Set to 'true' to define this sub-ring port as a Ring Protection Link port.\n         Exactly one RPL port must be defined when sub-ring role (prvtRapsInstSubRingRole)\n         is not 'simpleNode'.\n         In 'simpleNode' role, no RPL ports must be defined.")
prvtRapsInstSubRingPortMonitoringMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 7, 1, 4), PrvtRapsMonitoringMethodType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingPortMonitoringMethod.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingPortMonitoringMethod.setDescription('Ethernet ring protection monitoring methods')
prvtRapsInstSubRingLagTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8), )
if mibBuilder.loadTexts: prvtRapsInstSubRingLagTable.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingLagTable.setDescription('R-APS Instance Sub-ring LAG interface Table\n         An entry in this table defines a LAG interface belonging to a sub-ring.\n         Exactly one interface must be defined per sub-ring. This includes physical\n         ports (defined in prvtRapsInstSubRingPortTable) and LAG interfaces (defined\n         in prvtRapsInstSubRingLagTable).')
prvtRapsInstSubRingLagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1), ).setIndexNames((0, "PRVT-RAPS-MIB", "prvtRapsInstIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstSubRingIndex"), (0, "PRVT-RAPS-MIB", "prvtRapsInstSubRingLagId"))
if mibBuilder.loadTexts: prvtRapsInstSubRingLagEntry.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingLagEntry.setDescription('An entry in prvtRapsInstSubRingLagTable.')
prvtRapsInstSubRingLagId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1, 1), PrvtRapsLinkAggIdType())
if mibBuilder.loadTexts: prvtRapsInstSubRingLagId.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingLagId.setDescription('Uniquely identifies a LAG interface belonging to a sub-ring.\n         Must be set to the LAG ID of an existing LAG interface.\n         A sub-ring LAG port can not be part of the main ring.')
prvtRapsInstSubRingLagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingLagRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingLagRowStatus.setDescription('The RowStatus for this sub-ring LAG interface.')
prvtRapsInstSubRingLagMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1, 3), PrvtRapsMepIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingLagMep.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingLagMep.setDescription('The peer maintenance entity group end point ID that should monitor this sub-ring LAG interface.\n         A sub-ring MEP can not be used in another ring.')
prvtRapsInstSubRingLagRpl = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingLagRpl.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingLagRpl.setDescription("Set to 'true' to define this sub-ring LAG port as a Ring Protection Link port.\n         Exactly one RPL port must be defined when sub-ring role (prvtRapsInstSubRingRole)\n         is not 'simpleNode'.\n         In 'simpleNode' role, no RPL ports must be defined.")
prvtRapsInstSubRingLagMonitoringMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 1, 8, 1, 5), PrvtRapsMonitoringMethodType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRapsInstSubRingLagMonitoringMethod.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingLagMonitoringMethod.setDescription('Ethernet ring protection monitoring methods')
prvtRapsDefectAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 0, 1)).setObjects(("PRVT-RAPS-MIB", "prvtRapsInstOperStatus"), ("PRVT-RAPS-MIB", "prvtRapsInstControlVlan"))
if mibBuilder.loadTexts: prvtRapsDefectAlarm.setStatus('current')
if mibBuilder.loadTexts: prvtRapsDefectAlarm.setDescription('This trap will be sent by any instance when it notices a defect.\n         So far only the situation when two or more RPL-owners are defined\n         in the ring is identified as a defect. This scenario is noticed when\n         the instance with the RPL-Owner role receives a RAPS packet with the\n         RB bit set in its status field from a different NodeID than its own.\n         The management entity receiving the notification can identify\n         the system from the network source address of the\n         notification.')
prvtRapsSwitchoverAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 0, 2)).setObjects(("PRVT-RAPS-MIB", "prvtRapsInstRapsState"), ("PRVT-RAPS-MIB", "prvtRapsInstControlVlan"))
if mibBuilder.loadTexts: prvtRapsSwitchoverAlarm.setStatus('current')
if mibBuilder.loadTexts: prvtRapsSwitchoverAlarm.setDescription('This trap will be sent by any instance when it changes state.\n         The management entity receiving the notification can identify\n         the system from the network source address of the\n         notification')
prvtRapsInstSubRingDefectAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 0, 3)).setObjects(("PRVT-RAPS-MIB", "prvtRapsInstSubRingOperStatus"), ("PRVT-RAPS-MIB", "prvtRapsInstSubRingControlVlan"))
if mibBuilder.loadTexts: prvtRapsInstSubRingDefectAlarm.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingDefectAlarm.setDescription('This trap will be sent by any subring instance when it notices a defect.\n         So far only the situation when two or more RPL-owners are defined\n         in the ring is identified as a defect. This scenario is noticed when\n         the instance with the RPL-Owner role receives a RAPS packet with the\n         RB bit set in its status field from a different NodeID than its own.\n         The management entity receiving the notification can identify\n         the system from the network source address of the\n         notification, and can identify the instance reporting the change\n         by the indices in the OID of the prvtRapsInstSubRingOperStatus\n         variable in the notification.')
prvtRapsInstSubRingSwitchoverAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 7, 4, 0, 4)).setObjects(("PRVT-RAPS-MIB", "prvtRapsInstSubRingRapsState"), ("PRVT-RAPS-MIB", "prvtRapsInstSubRingControlVlan"))
if mibBuilder.loadTexts: prvtRapsInstSubRingSwitchoverAlarm.setStatus('current')
if mibBuilder.loadTexts: prvtRapsInstSubRingSwitchoverAlarm.setDescription('This trap will be sent by any subring instance when it changes state.\n         The management entity receiving the notification can identify\n         the system from the network source address of the\n         notification, and can identify the instance reporting the change\n         by the indices in the OID of the prvtRapsInstSubRingRapsState\n         variable in the notification.')
mibBuilder.exportSymbols("PRVT-RAPS-MIB", prvtRapsInstSubRingTopPriCmd=prvtRapsInstSubRingTopPriCmd, prvtRapsInstSubRingPortMep=prvtRapsInstSubRingPortMep, prvtRapsInstRingLagId=prvtRapsInstRingLagId, prvtRapsInstSubRingId=prvtRapsInstSubRingId, prvtRapsInstSubRingWaitTimer=prvtRapsInstSubRingWaitTimer, PrvtRapsBlockTimerType=PrvtRapsBlockTimerType, PrvtRapsReceivedInfoType=PrvtRapsReceivedInfoType, PrvtRapsReceivedCommandType=PrvtRapsReceivedCommandType, prvtRapsInstSubRingLinkStatus=prvtRapsInstSubRingLinkStatus, prvtRapsInstRingPortMonitoringMethod=prvtRapsInstRingPortMonitoringMethod, prvtRapsInstGuardTimer=prvtRapsInstGuardTimer, prvtRapsInstMonVlanTable=prvtRapsInstMonVlanTable, prvtRapsMIBNotifications=prvtRapsMIBNotifications, prvtRapsInstDescription=prvtRapsInstDescription, prvtRapsInstRingPortForcedSwitch=prvtRapsInstRingPortForcedSwitch, prvtRapsInstControlProtocol=prvtRapsInstControlProtocol, prvtRapsInstSubRingRevertiveMode=prvtRapsInstSubRingRevertiveMode, prvtRapsInstRingLagRowStatus=prvtRapsInstRingLagRowStatus, prvtRapsInstSubRingOperStatus=prvtRapsInstSubRingOperStatus, prvtRapsInstSubRingBlockTimer=prvtRapsInstSubRingBlockTimer, prvtRapsInstSubRingEntry=prvtRapsInstSubRingEntry, prvtRapsInstTable=prvtRapsInstTable, prvtRapsInstSubRingPortRpl=prvtRapsInstSubRingPortRpl, PrvtRapsMonitoringMethodType=PrvtRapsMonitoringMethodType, prvtRapsInstCfmDomainLevel=prvtRapsInstCfmDomainLevel, prvtRapsInstMode=prvtRapsInstMode, prvtRapsInstRingPortRpl=prvtRapsInstRingPortRpl, prvtRapsInstRevertiveMode=prvtRapsInstRevertiveMode, prvtRapsInstSubRingIndex=prvtRapsInstSubRingIndex, prvtRapsInstSubRingPortMonitoringMethod=prvtRapsInstSubRingPortMonitoringMethod, PrvtRapsInstIndexType=PrvtRapsInstIndexType, prvtRapsInstPortStatusRcvdCmd=prvtRapsInstPortStatusRcvdCmd, prvtRapsInstRingPortIfIndex=prvtRapsInstRingPortIfIndex, prvtRapsInstRingPortTable=prvtRapsInstRingPortTable, prvtRapsInstRingLagIndex=prvtRapsInstRingLagIndex, prvtRapsInstSubRingVcRcvdInfo=prvtRapsInstSubRingVcRcvdInfo, prvtRapsInstRingPortIndex=prvtRapsInstRingPortIndex, prvtRapsInstSubRingRapsState=prvtRapsInstSubRingRapsState, PrvtRapsVlanIdType=PrvtRapsVlanIdType, prvtRapsInstRingLagRpl=prvtRapsInstRingLagRpl, prvtRapsSwitchoverAlarm=prvtRapsSwitchoverAlarm, prvtRapsInstRingLagManSwitch=prvtRapsInstRingLagManSwitch, prvtRapsInstSubRingLagTable=prvtRapsInstSubRingLagTable, prvtRapsInstClear=prvtRapsInstClear, prvtRapsInstSubRingLagRowStatus=prvtRapsInstSubRingLagRowStatus, prvtRapsInstWaitToRestoreTimer=prvtRapsInstWaitToRestoreTimer, PrvtRapsWaitTimerType=PrvtRapsWaitTimerType, prvtRapsInstWaitToBlockTimer=prvtRapsInstWaitToBlockTimer, prvtRapsMIBObjects=prvtRapsMIBObjects, prvtRapsInstSubRingShutdown=prvtRapsInstSubRingShutdown, prvtRapsInstSubRingLagMep=prvtRapsInstSubRingLagMep, prvtRapsInstSubRingPortTable=prvtRapsInstSubRingPortTable, PrvtRapsRoleType=PrvtRapsRoleType, prvtRapsInstRole=prvtRapsInstRole, PrvtRapsInstStatusType=PrvtRapsInstStatusType, prvtRapsInstRapsState=prvtRapsInstRapsState, prvtRapsInstSubRingLagId=prvtRapsInstSubRingLagId, PrvtRapsGuardTimerType=PrvtRapsGuardTimerType, prvtRapsInstSubRingGuardTimer=prvtRapsInstSubRingGuardTimer, prvtRapsInstOperStatus=prvtRapsInstOperStatus, prvtRapsInstSubRingSwitchoverAlarm=prvtRapsInstSubRingSwitchoverAlarm, prvtRapsInstSubRingLagRpl=prvtRapsInstSubRingLagRpl, prvtRapsInstSubRingHoldOffTimer=prvtRapsInstSubRingHoldOffTimer, prvtRapsInstSubRingManualSwitch=prvtRapsInstSubRingManualSwitch, prvtRapsInstRingPortMep=prvtRapsInstRingPortMep, prvtRapsInstIndex=prvtRapsInstIndex, prvtRapsInstSubRingRcvdNodeId=prvtRapsInstSubRingRcvdNodeId, PrvtRapsLinkAggIdType=PrvtRapsLinkAggIdType, prvtRapsInstSubRingDescription=prvtRapsInstSubRingDescription, prvtRapsInstSubRingLagMonitoringMethod=prvtRapsInstSubRingLagMonitoringMethod, prvtRapsInstSubRingRole=prvtRapsInstSubRingRole, prvtRapsMIB=prvtRapsMIB, prvtRapsInstSubRingPortRowStatus=prvtRapsInstSubRingPortRowStatus, prvtRapsInstSubRingPropTopChng=prvtRapsInstSubRingPropTopChng, prvtRapsInstRowStatus=prvtRapsInstRowStatus, prvtRapsInstSubRingLagEntry=prvtRapsInstSubRingLagEntry, PrvtRapsMepIdType=PrvtRapsMepIdType, prvtRapsInstRingId=prvtRapsInstRingId, prvtRapsInstTopPriCmd=prvtRapsInstTopPriCmd, prvtRapsInstPortStatusRemoteMep=prvtRapsInstPortStatusRemoteMep, PrvtRapsTopPriCmdType=PrvtRapsTopPriCmdType, PrvtRapsHoldOffType=PrvtRapsHoldOffType, prvtRapsInstSubRingVirtChanVlan=prvtRapsInstSubRingVirtChanVlan, prvtRapsInstDisableVirtChan=prvtRapsInstDisableVirtChan, PrvtRapsRingIdType=PrvtRapsRingIdType, prvtRapsInstEntry=prvtRapsInstEntry, prvtRapsInstMonVlanEntry=prvtRapsInstMonVlanEntry, prvtRapsInstRingLagTable=prvtRapsInstRingLagTable, prvtRapsInstSubRingVcRcvdCmd=prvtRapsInstSubRingVcRcvdCmd, prvtRapsInstSubRingRcvdCmd=prvtRapsInstSubRingRcvdCmd, prvtRapsInstRingLagEntry=prvtRapsInstRingLagEntry, prvtRapsInstPortStatusRcvdInfo=prvtRapsInstPortStatusRcvdInfo, PrvtRapsLinkOperStatusType=PrvtRapsLinkOperStatusType, prvtRapsInstShutdown=prvtRapsInstShutdown, prvtRapsInstSubRingClear=prvtRapsInstSubRingClear, prvtRapsInstSubRingVirtChanSvc=prvtRapsInstSubRingVirtChanSvc, prvtRapsInstPortStatusIfIndex=prvtRapsInstPortStatusIfIndex, prvtRapsInstRingLagForcedSwitch=prvtRapsInstRingLagForcedSwitch, prvtRapsInstHoldOffTimer=prvtRapsInstHoldOffTimer, prvtRapsInstRingPortManSwitch=prvtRapsInstRingPortManSwitch, PYSNMP_MODULE_ID=prvtRapsMIB, prvtRapsInstRingPortEntry=prvtRapsInstRingPortEntry, prvtRapsInstMonVlanId=prvtRapsInstMonVlanId, prvtRapsInstSubRingTable=prvtRapsInstSubRingTable, PrvtRapsModeType=PrvtRapsModeType, prvtRapsInstPortStatusRcvdNodeId=prvtRapsInstPortStatusRcvdNodeId, prvtRapsInstSubRingControlVlan=prvtRapsInstSubRingControlVlan, PrvtRapsCfmLevelType=PrvtRapsCfmLevelType, prvtRapsInstSubRingPortEntry=prvtRapsInstSubRingPortEntry, prvtRapsInstSubRingRcvdInfo=prvtRapsInstSubRingRcvdInfo, prvtRapsInstRingLagMep=prvtRapsInstRingLagMep, prvtRapsInstMonVlanRowStatus=prvtRapsInstMonVlanRowStatus, prvtRapsInstSubRingVcRcvdNodeId=prvtRapsInstSubRingVcRcvdNodeId, PrvtRapsStatesType=PrvtRapsStatesType, prvtRapsInstRingPortRowStatus=prvtRapsInstRingPortRowStatus, prvtRapsInstPortStatusEntry=prvtRapsInstPortStatusEntry, PrvtRapsActionType=PrvtRapsActionType, prvtRapsInstControlVlan=prvtRapsInstControlVlan, prvtRapsInstPortStatusTable=prvtRapsInstPortStatusTable, prvtRapsInstSubRingRowStatus=prvtRapsInstSubRingRowStatus, prvtRapsInstSubRingForcedSwitch=prvtRapsInstSubRingForcedSwitch, PrvtRapsIfIndexOrAgIdType=PrvtRapsIfIndexOrAgIdType, prvtRapsInstSubRingDefectAlarm=prvtRapsInstSubRingDefectAlarm, prvtRapsDefectAlarm=prvtRapsDefectAlarm, prvtRapsInstSubRingPortName=prvtRapsInstSubRingPortName, prvtRapsInstPortStatusLink=prvtRapsInstPortStatusLink)
