#
# PySNMP MIB module PRVT-EPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-EPS-MIB
# Produced by pysmi-1.1.8 at Fri Jan 14 00:02:12 2022
# On host fv-az74-435 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
Dot1agCfmMepIdOrZero, Dot1agCfmMDLevelOrNone = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "Dot1agCfmMepIdOrZero", "Dot1agCfmMDLevelOrNone")
sdpInfoEntry, = mibBuilder.importSymbols("PRVT-SERV-MIB", "sdpInfoEntry")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, ObjectIdentity, Unsigned32, Bits, Counter32, Counter64, Integer32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "ObjectIdentity", "Unsigned32", "Bits", "Counter32", "Counter64", "Integer32", "NotificationType", "TimeTicks")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
prvtEpsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 132))
prvtEpsMib.setRevisions(('2011-03-23 00:00', '2010-04-17 00:00', '2009-07-15 00:00', '2009-03-24 00:00',))
if mibBuilder.loadTexts: prvtEpsMib.setLastUpdated('201004170000Z')
if mibBuilder.loadTexts: prvtEpsMib.setOrganization('BATM Advanced Communication')
prvtEpsMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0))
prvtEpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1))
class PrvtEpsRequestStateType(TextualConvention, Integer32):
    reference = 'G.8031 clause 11.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 4, 5, 6, 7, 9, 11, 13, 14, 15))
    namedValues = NamedValues(("rsNone", -1), ("rsNoRequest", 0), ("rsDoNotRevert", 1), ("rsReverseRequest", 2), ("rsExercise", 4), ("rsWaitToRestore", 5), ("rsClear", 6), ("rsManualSwitch", 7), ("rsSignalDegrade", 9), ("rsSignalFail", 11), ("rsForcedSwitch", 13), ("rsSignalFailForProtection", 14), ("rsLockoutOfProtection", 15))

class PrvtEpsProtectionType(TextualConvention, Integer32):
    reference = 'G.8031 clause 11.4'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("pt1Plus1", 0), ("pt1To1", 1))

class PrvtEpsDirectionType(TextualConvention, Integer32):
    reference = 'G.8031 clause 11.4'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("dtUnidirectional", 0), ("dtBidirectional", 1))

class PrvtEpsActivePathType(TextualConvention, Integer32):
    reference = 'G.8031 clause 11.6'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("working", 0), ("protection", 1))

class PrvtEpsMonitoringType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("cfmPM", 1), ("saa", 2))

class PrvtEpsDefectFopType(TextualConvention, Bits):
    reference = 'G.8031 clause 11.15'
    status = 'current'
    namedValues = NamedValues(("fullyIncompatibleProvisioning", 0), ("protectionSwitchingIncomplete", 1), ("protectionConfigurationMismatch", 2), ("epsConfigurationMismatch", 3))

class PrvtEpsPathStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("psOk", 0), ("psFailed", 1))

prvtEpsService = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1))
prvtEpsServiceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1), )
if mibBuilder.loadTexts: prvtEpsServiceTable.setStatus('current')
prvtEpsServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1), ).setIndexNames((0, "PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsServiceEntry.setStatus('current')
prvtEpsSvcId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsSvcId.setStatus('current')
prvtEpsServiceCfmMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 2), Dot1agCfmMDLevelOrNone().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceCfmMdLevel.setStatus('current')
prvtEpsServicePrimaryLocalCfmMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 3), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServicePrimaryLocalCfmMep.setStatus('current')
prvtEpsServicePrimaryRemoteCfmMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 4), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServicePrimaryRemoteCfmMep.setStatus('current')
prvtEpsServiceSecondaryLocalCfmMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 5), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceSecondaryLocalCfmMep.setStatus('current')
prvtEpsServiceSecondaryRemoteCfmMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 6), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceSecondaryRemoteCfmMep.setStatus('current')
prvtEpsServiceLocalState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 7), PrvtEpsRequestStateType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceLocalState.setStatus('current')
prvtEpsServiceHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceHoldOffTimer.setStatus('current')
prvtEpsServiceWaitToRestoreTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 12), )).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceWaitToRestoreTimer.setStatus('current')
prvtEpsServiceApsChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceApsChannel.setStatus('current')
prvtEpsServiceProtection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 11), PrvtEpsProtectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceProtection.setStatus('current')
prvtEpsServiceDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 12), PrvtEpsDirectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceDirection.setStatus('current')
prvtEpsServiceRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 13), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceRevertive.setStatus('current')
prvtEpsServiceActivePath = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 14), PrvtEpsActivePathType().clone('working')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceActivePath.setStatus('current')
prvtEpsServiceDegradeTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 15), PrvtEpsMonitoringType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestType.setStatus('current')
prvtEpsServiceDegradeTestOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="00")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestOwner.setStatus('current')
prvtEpsServiceDegradeTestName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="00")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestName.setStatus('current')
prvtEpsServiceDegradeTestEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 18), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestEnable.setStatus('current')
prvtEpsServiceDefectFop = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 19), PrvtEpsDefectFopType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceDefectFop.setStatus('current')
prvtEpsServiceOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceOperationalStatus.setStatus('current')
prvtEpsServicePrimaryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 21), PrvtEpsPathStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServicePrimaryStatus.setStatus('current')
prvtEpsServiceSecondaryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 22), PrvtEpsPathStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceSecondaryStatus.setStatus('current')
prvtEpsServiceRemoteState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 23), PrvtEpsRequestStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceRemoteState.setStatus('current')
prvtEpsServiceRemoteApsChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 24), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceRemoteApsChannel.setStatus('current')
prvtEpsServiceRemoteProtection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 25), PrvtEpsProtectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceRemoteProtection.setStatus('current')
prvtEpsServiceRemoteDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 26), PrvtEpsDirectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceRemoteDirection.setStatus('current')
prvtEpsServiceRemoteRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 27), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceRemoteRevertive.setStatus('current')
prvtEpsServiceAdminFreeze = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 28), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceAdminFreeze.setStatus('current')
prvtEpsServiceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceAdminStatus.setStatus('current')
prvtEpsServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 30), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceRowStatus.setStatus('current')
prvtEpsServiceProtectionCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 31), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceProtectionCounter.setStatus('current')
prvtEpsDefectAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 1)).setObjects(("PRVT-EPS-MIB", "prvtEpsServiceOperationalStatus"), ("PRVT-EPS-MIB", "prvtEpsServiceDefectFop"))
if mibBuilder.loadTexts: prvtEpsDefectAlarm.setStatus('current')
prvtEpsSwitchoverAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 2)).setObjects(("PRVT-EPS-MIB", "prvtEpsServiceActivePath"))
if mibBuilder.loadTexts: prvtEpsSwitchoverAlarm.setStatus('current')
prvtEpsLostCommunication = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 3)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsLostCommunication.setStatus('current')
prvtEpsRestoredCommunication = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 4)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsRestoredCommunication.setStatus('current')
prvtEpsSignalFailDetected = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 5)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsSignalFailDetected.setStatus('current')
prvtEpsSignalDegradeDetected = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 6)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsSignalDegradeDetected.setStatus('current')
prvtEpsProtctSignalFailDetected = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 7)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsProtctSignalFailDetected.setStatus('current')
prvtEpsSignalFailRecovery = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 8)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsSignalFailRecovery.setStatus('current')
prvtEpsSignalDegradeRecovery = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 9)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsSignalDegradeRecovery.setStatus('current')
prvtEpsProtctSignalFailRecovery = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 10)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsProtctSignalFailRecovery.setStatus('current')
mibBuilder.exportSymbols("PRVT-EPS-MIB", prvtEpsMibNotifications=prvtEpsMibNotifications, PrvtEpsDefectFopType=PrvtEpsDefectFopType, prvtEpsSignalDegradeRecovery=prvtEpsSignalDegradeRecovery, prvtEpsSignalFailDetected=prvtEpsSignalFailDetected, prvtEpsMib=prvtEpsMib, prvtEpsServiceRemoteApsChannel=prvtEpsServiceRemoteApsChannel, prvtEpsServiceApsChannel=prvtEpsServiceApsChannel, prvtEpsServiceRemoteDirection=prvtEpsServiceRemoteDirection, prvtEpsServiceDegradeTestType=prvtEpsServiceDegradeTestType, prvtEpsServiceRowStatus=prvtEpsServiceRowStatus, prvtEpsSignalFailRecovery=prvtEpsSignalFailRecovery, prvtEpsServiceDefectFop=prvtEpsServiceDefectFop, prvtEpsServicePrimaryRemoteCfmMep=prvtEpsServicePrimaryRemoteCfmMep, prvtEpsServiceRevertive=prvtEpsServiceRevertive, prvtEpsServicePrimaryStatus=prvtEpsServicePrimaryStatus, prvtEpsServiceTable=prvtEpsServiceTable, PYSNMP_MODULE_ID=prvtEpsMib, prvtEpsLostCommunication=prvtEpsLostCommunication, prvtEpsServiceHoldOffTimer=prvtEpsServiceHoldOffTimer, prvtEpsServicePrimaryLocalCfmMep=prvtEpsServicePrimaryLocalCfmMep, prvtEpsServiceProtectionCounter=prvtEpsServiceProtectionCounter, PrvtEpsPathStatusType=PrvtEpsPathStatusType, prvtEpsServiceAdminStatus=prvtEpsServiceAdminStatus, prvtEpsRestoredCommunication=prvtEpsRestoredCommunication, prvtEpsServiceAdminFreeze=prvtEpsServiceAdminFreeze, prvtEpsServiceProtection=prvtEpsServiceProtection, PrvtEpsDirectionType=PrvtEpsDirectionType, prvtEpsServiceSecondaryRemoteCfmMep=prvtEpsServiceSecondaryRemoteCfmMep, prvtEpsServiceRemoteState=prvtEpsServiceRemoteState, prvtEpsServiceDegradeTestName=prvtEpsServiceDegradeTestName, prvtEpsServiceCfmMdLevel=prvtEpsServiceCfmMdLevel, prvtEpsProtctSignalFailDetected=prvtEpsProtctSignalFailDetected, prvtEpsServiceRemoteProtection=prvtEpsServiceRemoteProtection, PrvtEpsActivePathType=PrvtEpsActivePathType, PrvtEpsProtectionType=PrvtEpsProtectionType, prvtEpsSvcId=prvtEpsSvcId, prvtEpsServiceLocalState=prvtEpsServiceLocalState, prvtEpsServiceOperationalStatus=prvtEpsServiceOperationalStatus, prvtEpsServiceDegradeTestEnable=prvtEpsServiceDegradeTestEnable, prvtEpsMibObjects=prvtEpsMibObjects, PrvtEpsMonitoringType=PrvtEpsMonitoringType, prvtEpsSignalDegradeDetected=prvtEpsSignalDegradeDetected, PrvtEpsRequestStateType=PrvtEpsRequestStateType, prvtEpsProtctSignalFailRecovery=prvtEpsProtctSignalFailRecovery, prvtEpsSwitchoverAlarm=prvtEpsSwitchoverAlarm, prvtEpsServiceRemoteRevertive=prvtEpsServiceRemoteRevertive, prvtEpsServiceActivePath=prvtEpsServiceActivePath, prvtEpsServiceWaitToRestoreTimer=prvtEpsServiceWaitToRestoreTimer, prvtEpsServiceEntry=prvtEpsServiceEntry, prvtEpsServiceDegradeTestOwner=prvtEpsServiceDegradeTestOwner, prvtEpsDefectAlarm=prvtEpsDefectAlarm, prvtEpsServiceSecondaryLocalCfmMep=prvtEpsServiceSecondaryLocalCfmMep, prvtEpsServiceSecondaryStatus=prvtEpsServiceSecondaryStatus, prvtEpsServiceDirection=prvtEpsServiceDirection, prvtEpsService=prvtEpsService)
