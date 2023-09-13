#
# PySNMP MIB module CM-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/CM-REDUNDANCY-MIB
# Produced by pysmi-1.1.8 at Wed Sep 13 07:15:58 2023
# On host fv-az454-0 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
CardType, neIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "CardType", "neIndex")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Counter64, IpAddress, Integer32, ModuleIdentity, Bits, NotificationType, ObjectIdentity, MibIdentifier, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "IpAddress", "Integer32", "ModuleIdentity", "Bits", "NotificationType", "ObjectIdentity", "MibIdentifier", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32")
RowStatus, TextualConvention, TruthValue, VariablePointer, StorageType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "VariablePointer", "StorageType", "DisplayString")
cmRedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15))
cmRedundancyMIB.setRevisions(('2009-02-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmRedundancyMIB.setRevisionsDescriptions(('Notes from release 200902240000Z,\n             (1)MIB version ready for release FSP150CM 5.1.',))
if mibBuilder.loadTexts: cmRedundancyMIB.setLastUpdated('200902240000Z')
if mibBuilder.loadTexts: cmRedundancyMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: cmRedundancyMIB.setContactInfo('        Raghav Trivedi\n                     ADVA Optical Networking, Inc.\n                Tel: +1 972 759-1239\n             E-mail: rtrivedi@advaoptical.com\n             Postal: 2301 N. Greenville Ave. #300\n                     Richardson, TX USA 75082')
if mibBuilder.loadTexts: cmRedundancyMIB.setDescription('This module defines the Redundancy MIB definitions used by \n             the FSP150CM product line.  \n             Copyright (C) ADVA Optical Networking.')
cmRedundancyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1))
cmRedundancyNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 2))
cmRedundancyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3))
class CmRedundancyArch(TextualConvention, Integer32):
    description = 'Enumerations for Redundancy Architecture.\n             loadbalance,\n             activestandby'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("loadbalance", 1), ("activestandby", 2))

class CmRedundancyStandbyMode(TextualConvention, Integer32):
    description = 'Enumerations for Redundancy Mode.\n                                                                                       \n         coldStandby(1)     \n         \n           A method of redundancy in which the secondary (i.e., backup) system is\n            only called upon when the primary system fails. The system on cold standby\n             receives scheduled data backups, but less frequently than a warm standby. \n\n         warmStandby(2)  \n         \n           A method of redundancy in which the secondary (i.e., backup) system runs \n           in the background of the primary system. Data is mirrored to the secondary\n            server at regular intervals, which means that there are times when both \n            servers do not contain the exact same data..\n\n         hotStandby(3)\n\n           A method of redundancy in which the primary and secondary (i.e., backup)\n            systems run simultaneously. The data is mirrored to the secondary server\n             in real time so that both systems contain identical information. \n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cold", 1), ("warm", 2), ("hot", 3))

class CmRedundancyState(TextualConvention, Integer32):
    description = 'Enumerations for Redundancy State.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class CmRedundancySyncStatus(TextualConvention, Integer32):
    description = 'Enumerations for synchronization status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("out-of-synchronize", 2), ("bulk-synchronize", 3), ("incremental-synchronize", 4))

class CmRedundancySwitchOverReason(TextualConvention, Integer32):
    description = 'Enumerations for Redundancy Last Switch Over Reason.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("latestUpdatedData", 2), ("userTrigger", 3), ("cardReset", 4), ("cardRemoval", 5), ("softwareFailure", 6), ("hardwareFailure", 7))

class CmRedundancySyncMode(TextualConvention, Integer32):
    description = 'Enumerations for Redundancy Synchronization Mode.\n             automatically  - Active card automatically propagates config data to its peer             \n             manually  - User needs to manually copy config data to standby card and apply it.             \n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("automatically", 1), ("manually", 2))

class CmRedundancyAction(TextualConvention, Integer32):
    description = 'Enumerations for User initiated Redundancy Switch Action.\n             force   - Force Switch from Active Card              \n             manual  - Manual Switch from Active Card\n             releasefore - Release Force switch from Active Card             \n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("force", 1), ("manual", 2), ("releaseforce", 3))

class CmRedundancyUnitState(TextualConvention, Integer32):
    description = 'Enumerations for Redundancy Unit State.\n             none   - no state              \n             normal  - normal state\n             maintenance - maintenance state\n             faultisolation - faultisolation        \n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("none", 1), ("normal", 2), ("maintenance", 3), ("faultisolation", 4), ("lock", 5), ("extracted", 6), ("init", 7), ("stanbdby", 8))

cmRedundancyGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1), )
if mibBuilder.loadTexts: cmRedundancyGroupTable.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupTable.setDescription('A list of entries corresponding to the Redundancy Groups.\n             ')
cmRedundancyGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-REDUNDANCY-MIB", "cmRedundancyGroupIndex"))
if mibBuilder.loadTexts: cmRedundancyGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupEntry.setDescription('An entry containing information applicable to a particular\n             Redundancy Group.')
cmRedundancyGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupIndex.setDescription('Unique index value associated with the Redundancy Group.')
cmRedundancyGroupUserLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmRedundancyGroupUserLabel.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupUserLabel.setDescription('User Label associated with the Reduandancy Group.')
cmRedundancyGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 3), CardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupType.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupType.setDescription('The type of card who belongs to the Redundancy Group.')
cmRedundancyGroupSyncEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmRedundancyGroupSyncEnabled.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupSyncEnabled.setDescription('The way of the synchronization in Redundancy Group.')
cmRedundancyGroupActiveCard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 5), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupActiveCard.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupActiveCard.setDescription('The corresponding OID of the Active/Primary Card in the Redundancy Group.')
cmRedundancyGroupActiveCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 6), CmRedundancyUnitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupActiveCardState.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupActiveCardState.setDescription('The state of the Active Card in the Redundancy Group.')
cmRedundancyGroupStandbyCard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 7), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupStandbyCard.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupStandbyCard.setDescription('The corresponding OID of the Standby/Secondary Card in the Redundancy Group.')
cmRedundancyGroupStandbyCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 8), CmRedundancyUnitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupStandbyCardState.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupStandbyCardState.setDescription('The state of the Standby Card in the Redundancy Group.')
cmRedundancyGroupLastSwitchOverTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupLastSwitchOverTime.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupLastSwitchOverTime.setDescription('The value of sysUpTime when last switch over occurred.')
cmRedundancyGroupLastSwitchOverReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 10), CmRedundancySwitchOverReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupLastSwitchOverReason.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupLastSwitchOverReason.setDescription('The reason for last switch over in the Redundancy Group.')
cmRedundancyGroupState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 11), CmRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupState.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupState.setDescription('The current state of the Redundancy Group.')
cmRedundancyGroupSyncStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 12), CmRedundancySyncStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupSyncStatus.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupSyncStatus.setDescription('The current sync state of the Redundancy Group.')
cmRedundancyGroupAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 13), CmRedundancyAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmRedundancyGroupAction.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyGroupAction.setDescription('User initiated switch action of the Redundancy Group.')
cmRedundancyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 1))
cmRedundancyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 2))
cmRedundancyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 1, 1)).setObjects(("CM-REDUNDANCY-MIB", "cmRedundancyObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmRedundancyCompliance = cmRedundancyCompliance.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyCompliance.setDescription('Describes the requirements for conformance to the CM Redundancy\n             group.')
cmRedundancyObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 2, 1)).setObjects(("CM-REDUNDANCY-MIB", "cmRedundancyGroupIndex"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupUserLabel"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupType"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupSyncEnabled"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupActiveCard"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupActiveCardState"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupStandbyCard"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupStandbyCardState"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupLastSwitchOverTime"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupLastSwitchOverReason"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupState"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupSyncStatus"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmRedundancyObjectGroup = cmRedundancyObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cmRedundancyObjectGroup.setDescription('A collection of objects used to manage the CM Redundancy Object group.')
mibBuilder.exportSymbols("CM-REDUNDANCY-MIB", cmRedundancyNotifications=cmRedundancyNotifications, cmRedundancyGroupStandbyCard=cmRedundancyGroupStandbyCard, cmRedundancyGroupLastSwitchOverTime=cmRedundancyGroupLastSwitchOverTime, cmRedundancyObjects=cmRedundancyObjects, PYSNMP_MODULE_ID=cmRedundancyMIB, cmRedundancyObjectGroup=cmRedundancyObjectGroup, cmRedundancyGroupStandbyCardState=cmRedundancyGroupStandbyCardState, cmRedundancyGroupAction=cmRedundancyGroupAction, cmRedundancyCompliances=cmRedundancyCompliances, CmRedundancyAction=CmRedundancyAction, cmRedundancyGroupState=cmRedundancyGroupState, cmRedundancyConformance=cmRedundancyConformance, cmRedundancyGroups=cmRedundancyGroups, cmRedundancyGroupLastSwitchOverReason=cmRedundancyGroupLastSwitchOverReason, cmRedundancyGroupUserLabel=cmRedundancyGroupUserLabel, cmRedundancyGroupType=cmRedundancyGroupType, CmRedundancyUnitState=CmRedundancyUnitState, cmRedundancyGroupSyncStatus=cmRedundancyGroupSyncStatus, cmRedundancyGroupIndex=cmRedundancyGroupIndex, CmRedundancyState=CmRedundancyState, CmRedundancyStandbyMode=CmRedundancyStandbyMode, cmRedundancyGroupTable=cmRedundancyGroupTable, cmRedundancyGroupSyncEnabled=cmRedundancyGroupSyncEnabled, cmRedundancyMIB=cmRedundancyMIB, CmRedundancySyncMode=CmRedundancySyncMode, CmRedundancyArch=CmRedundancyArch, cmRedundancyGroupEntry=cmRedundancyGroupEntry, cmRedundancyCompliance=cmRedundancyCompliance, CmRedundancySwitchOverReason=CmRedundancySwitchOverReason, cmRedundancyGroupActiveCard=cmRedundancyGroupActiveCard, cmRedundancyGroupActiveCardState=cmRedundancyGroupActiveCardState, CmRedundancySyncStatus=CmRedundancySyncStatus)
