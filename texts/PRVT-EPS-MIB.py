#
# PySNMP MIB module PRVT-EPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-EPS-MIB
# Produced by pysmi-1.1.0 at Tue Nov 16 11:56:29 2021
# On host fv-az121-894 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
Dot1agCfmMepIdOrZero, Dot1agCfmMDLevelOrNone = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "Dot1agCfmMepIdOrZero", "Dot1agCfmMDLevelOrNone")
sdpInfoEntry, = mibBuilder.importSymbols("PRVT-SERV-MIB", "sdpInfoEntry")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Unsigned32, Integer32, NotificationType, Counter32, iso, ModuleIdentity, ObjectIdentity, Gauge32, Bits, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Integer32", "NotificationType", "Counter32", "iso", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Bits", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
prvtEpsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 132))
prvtEpsMib.setRevisions(('2011-03-23 00:00', '2010-04-17 00:00', '2009-07-15 00:00', '2009-03-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtEpsMib.setRevisionsDescriptions(('Added Protection Counter', 'Add protection failure trap. Add recovery traps.', 'Updates for 9.4 release', 'Initial',))
if mibBuilder.loadTexts: prvtEpsMib.setLastUpdated('201004170000Z')
if mibBuilder.loadTexts: prvtEpsMib.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtEpsMib.setContactInfo(' BATM/Telco Systems Support team\n\tEmail:\n\tFor North America: techsupport@telco.com\n\tFor North Europe: support@batm.de, info@batm.de\n\tFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtEpsMib.setDescription('Private MIB supporting Linear Ethernet Protection Switching (ITU-T G.8031)')
prvtEpsMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0))
prvtEpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1))
class PrvtEpsRequestStateType(TextualConvention, Integer32):
    reference = 'G.8031 clause 11.3'
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 4, 5, 6, 7, 9, 11, 13, 14, 15))
    namedValues = NamedValues(("rsNone", -1), ("rsNoRequest", 0), ("rsDoNotRevert", 1), ("rsReverseRequest", 2), ("rsExercise", 4), ("rsWaitToRestore", 5), ("rsClear", 6), ("rsManualSwitch", 7), ("rsSignalDegrade", 9), ("rsSignalFail", 11), ("rsForcedSwitch", 13), ("rsSignalFailForProtection", 14), ("rsLockoutOfProtection", 15))

class PrvtEpsProtectionType(TextualConvention, Integer32):
    reference = 'G.8031 clause 11.4'
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("pt1Plus1", 0), ("pt1To1", 1))

class PrvtEpsDirectionType(TextualConvention, Integer32):
    reference = 'G.8031 clause 11.4'
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("dtUnidirectional", 0), ("dtBidirectional", 1))

class PrvtEpsActivePathType(TextualConvention, Integer32):
    reference = 'G.8031 clause 11.6'
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("working", 0), ("protection", 1))

class PrvtEpsMonitoringType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("cfmPM", 1), ("saa", 2))

class PrvtEpsDefectFopType(TextualConvention, Bits):
    reference = 'G.8031 clause 11.15'
    description = ''
    status = 'current'
    namedValues = NamedValues(("fullyIncompatibleProvisioning", 0), ("protectionSwitchingIncomplete", 1), ("protectionConfigurationMismatch", 2), ("epsConfigurationMismatch", 3))

class PrvtEpsPathStatusType(TextualConvention, Integer32):
    description = 'Status of the primary or backup links'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("psOk", 0), ("psFailed", 1))

prvtEpsService = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1))
prvtEpsServiceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1), )
if mibBuilder.loadTexts: prvtEpsServiceTable.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceTable.setDescription('The table contains Ethernet Protection Switching services information.')
prvtEpsServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1), ).setIndexNames((0, "PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsServiceEntry.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceEntry.setDescription('Ethernet Protection Switching information about a specific service.')
prvtEpsSvcId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsSvcId.setStatus('current')
if mibBuilder.loadTexts: prvtEpsSvcId.setDescription('The service ID.')
prvtEpsServiceCfmMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 2), Dot1agCfmMDLevelOrNone().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceCfmMdLevel.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceCfmMdLevel.setDescription('Value of the CFM MD level where the protected domain is situated.')
prvtEpsServicePrimaryLocalCfmMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 3), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServicePrimaryLocalCfmMep.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServicePrimaryLocalCfmMep.setDescription('Primary local CFM MEP Id.')
prvtEpsServicePrimaryRemoteCfmMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 4), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServicePrimaryRemoteCfmMep.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServicePrimaryRemoteCfmMep.setDescription('Primary remote CFM MEP Id.')
prvtEpsServiceSecondaryLocalCfmMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 5), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceSecondaryLocalCfmMep.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceSecondaryLocalCfmMep.setDescription('Backup local CFM MEP Id.')
prvtEpsServiceSecondaryRemoteCfmMep = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 6), Dot1agCfmMepIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceSecondaryRemoteCfmMep.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceSecondaryRemoteCfmMep.setDescription('Backup remote CFM MEP Id.')
prvtEpsServiceLocalState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 7), PrvtEpsRequestStateType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceLocalState.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceLocalState.setDescription('Protection state of the local side. The values can be set:\n\t rsManualSwitch(7), rsClear(6) or rsLockoutOfProtection(15).\n\t The values can be get:\n\t rsNoRequest                     (0),\n\t rsDoNotRevert                   (1),\n\t rsReverseRequest                (2),\n\t rsExercise                      (4),\n\t rsWaitToRestore                 (5),\n\t rsClear                         (6),\n\t rsManualSwitch                  (7),\n\t rsSignalDegrade                 (9),\n\t rsSignalFail                   (11),\n\t rsForcedSwitch                 (13),\n\t rsSignalFailForProtection      (14),\n\t rsLockoutOfProtection          (15).')
prvtEpsServiceHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceHoldOffTimer.setReference('G.8031 clause 11.12')
if mibBuilder.loadTexts: prvtEpsServiceHoldOffTimer.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceHoldOffTimer.setDescription('Value of the Hold Off timer in msec (increments of 100msec).')
prvtEpsServiceWaitToRestoreTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 12), )).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceWaitToRestoreTimer.setReference('G.8031 clause 11.13')
if mibBuilder.loadTexts: prvtEpsServiceWaitToRestoreTimer.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceWaitToRestoreTimer.setDescription('Value of the Wait To Restore timer in seconds (0 to disable it).')
prvtEpsServiceApsChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceApsChannel.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceApsChannel.setDescription('Active APS communication.')
prvtEpsServiceProtection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 11), PrvtEpsProtectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceProtection.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceProtection.setDescription('Type of protection (1+1 or 1:1).')
prvtEpsServiceDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 12), PrvtEpsDirectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceDirection.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceDirection.setDescription('Type of protection (unidirectional or bidirectional).')
prvtEpsServiceRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 13), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceRevertive.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceRevertive.setDescription('Protection type (revertive or non-revertive).')
prvtEpsServiceActivePath = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 14), PrvtEpsActivePathType().clone('working')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceActivePath.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceActivePath.setDescription('Protected service active path.')
prvtEpsServiceDegradeTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 15), PrvtEpsMonitoringType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestType.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestType.setDescription('Type of test used for monitoring signal degrade situations.')
prvtEpsServiceDegradeTestOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="00")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestOwner.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestOwner.setDescription('Owner of the SAA test used for monitoring.')
prvtEpsServiceDegradeTestName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="00")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestName.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestName.setDescription('Name of the CFM or SAA test used for monitoring.')
prvtEpsServiceDegradeTestEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 18), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestEnable.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceDegradeTestEnable.setDescription('Start/stop CFM or SAA test for performance monitoring.')
prvtEpsServiceDefectFop = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 19), PrvtEpsDefectFopType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceDefectFop.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceDefectFop.setDescription("Defects noticed by APS protocol could be either none or a composition of the bits (0-3):\n\t fullyIncompatibleProvisioning(0)   - occures by the reception of three APS frames with the\n\t  incompatible 'B' bit value during the period of 22.5 seconds;\n\t protectionSwitchingIncomplete(1)   - occures if the transmitted 'Requested Signal' and the\n\t  received 'Bridged Signal' do not match for a period of 50ms or longer;\n\t protectionConfigurationMismatch(2) - working/protection configuration mismatch, occures by\n\t  the reception of three APS frames from the working transport entity during the period of\n\t  22.5 seconds;\n\t epsConfigurationMismatch(3)        - provisioning mismatch - for example the local side is\n\t  set in revertive mode, the remote side is set in non revertive mode.")
prvtEpsServiceOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceOperationalStatus.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceOperationalStatus.setDescription('The purpose of this status is to identify to the User whether\n\t this service is ready for running. The operational status can\n\t be up or down. When creating the service the operational\n\t status will be down. Receiving CCMs from both transport\n\t entities and establishment of APS on the protection transport\n\t entity will bring the operational status to up.')
prvtEpsServicePrimaryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 21), PrvtEpsPathStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServicePrimaryStatus.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServicePrimaryStatus.setDescription('Primary path state (psOk(0) or psFailed(1)).')
prvtEpsServiceSecondaryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 22), PrvtEpsPathStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceSecondaryStatus.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceSecondaryStatus.setDescription('Secondary path state (psOk(0) or psFailed(1)).')
prvtEpsServiceRemoteState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 23), PrvtEpsRequestStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceRemoteState.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceRemoteState.setDescription('Protection state of the remote side.\n\t The values can be get:\n\t rsNoRequest                     (0),\n\t rsDoNotRevert                   (1),\n\t rsReverseRequest                (2),\n\t rsExercise                      (4),\n\t rsWaitToRestore                 (5),\n\t rsClear                         (6),\n\t rsManualSwitch                  (7),\n\t rsSignalDegrade                 (9),\n\t rsSignalFail                   (11),\n\t rsForcedSwitch                 (13),\n\t rsSignalFailForProtection      (14),\n\t rsLockoutOfProtection          (15).')
prvtEpsServiceRemoteApsChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 24), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceRemoteApsChannel.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceRemoteApsChannel.setDescription('Active APS communication reported by the remote.')
prvtEpsServiceRemoteProtection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 25), PrvtEpsProtectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceRemoteProtection.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceRemoteProtection.setDescription('Type of protection (1+1 or 1:1) reported by the remote.')
prvtEpsServiceRemoteDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 26), PrvtEpsDirectionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceRemoteDirection.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceRemoteDirection.setDescription('Type of protection (unidirectional or bidirectional) reported by the remote.')
prvtEpsServiceRemoteRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 27), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceRemoteRevertive.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceRemoteRevertive.setDescription('Protection type (revertive or non-revertive) reported by the remote.')
prvtEpsServiceAdminFreeze = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 28), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceAdminFreeze.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceAdminFreeze.setDescription('Used to freeze the state of the protection service.')
prvtEpsServiceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceAdminStatus.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceAdminStatus.setDescription('Administrative status of the protection.')
prvtEpsServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 30), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtEpsServiceRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceRowStatus.setDescription('The status of the row.\n\t The writable columns in a row can not be changed if the row\n\t is active. All columns must have a valid value before a row\n\t can be activated.')
prvtEpsServiceProtectionCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 1, 1, 1, 1, 31), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtEpsServiceProtectionCounter.setStatus('current')
if mibBuilder.loadTexts: prvtEpsServiceProtectionCounter.setDescription('Counts how many times the service has gone to Protection.')
prvtEpsDefectAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 1)).setObjects(("PRVT-EPS-MIB", "prvtEpsServiceOperationalStatus"), ("PRVT-EPS-MIB", "prvtEpsServiceDefectFop"))
if mibBuilder.loadTexts: prvtEpsDefectAlarm.setStatus('current')
if mibBuilder.loadTexts: prvtEpsDefectAlarm.setDescription('1. EPS service is either operational or not operational;\n        2. Failure of protocol defects.')
prvtEpsSwitchoverAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 2)).setObjects(("PRVT-EPS-MIB", "prvtEpsServiceActivePath"))
if mibBuilder.loadTexts: prvtEpsSwitchoverAlarm.setStatus('current')
if mibBuilder.loadTexts: prvtEpsSwitchoverAlarm.setDescription('The alarm is issued if the active link is changed,\n        pointing to the path where the switchover occured.')
prvtEpsLostCommunication = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 3)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsLostCommunication.setStatus('current')
if mibBuilder.loadTexts: prvtEpsLostCommunication.setDescription('The alarm is issued in case of non reception of APS frames\n        in three consecutive intervals each representing 5 seconds.')
prvtEpsRestoredCommunication = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 4)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsRestoredCommunication.setStatus('current')
if mibBuilder.loadTexts: prvtEpsRestoredCommunication.setDescription('APS frames are received normally after APS communication failure.')
prvtEpsSignalFailDetected = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 5)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsSignalFailDetected.setStatus('current')
if mibBuilder.loadTexts: prvtEpsSignalFailDetected.setDescription('The alarm is issued in case of CCMs are not received\n        and (3.5 * CCMtime(CCMinterval)) has expired.')
prvtEpsSignalDegradeDetected = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 6)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsSignalDegradeDetected.setStatus('current')
if mibBuilder.loadTexts: prvtEpsSignalDegradeDetected.setDescription('The alarm is issued in case of monitored error threshold is crossed:\n        1W Jitter error,\n        2W Jitter error,\n        Latency error,\n        Frame loss error.')
prvtEpsProtctSignalFailDetected = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 7)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsProtctSignalFailDetected.setStatus('current')
if mibBuilder.loadTexts: prvtEpsProtctSignalFailDetected.setDescription('The alarm is issued in case of CCMs are not received on the protected link\n        and (3.5 * CCMtime(CCMinterval)) has expired or the protected link is down.')
prvtEpsSignalFailRecovery = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 8)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsSignalFailRecovery.setStatus('current')
if mibBuilder.loadTexts: prvtEpsSignalFailRecovery.setDescription('The alarm is issued in case of CCMs start to be received\n\t    correctly again after a prvtEpsSignalFailDetected alarm occured\n        and (3.5 * CCMtime(CCMinterval)) timer no longer expires or the link is up .')
prvtEpsSignalDegradeRecovery = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 9)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsSignalDegradeRecovery.setStatus('current')
if mibBuilder.loadTexts: prvtEpsSignalDegradeRecovery.setDescription('The alarm is issued in case of monitored error threshold is crossed bellow limis:\n        1W Jitter error,\n        2W Jitter error,\n        Latency error,\n        Frame loss error.')
prvtEpsProtctSignalFailRecovery = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 132, 0, 10)).setObjects(("PRVT-EPS-MIB", "prvtEpsSvcId"))
if mibBuilder.loadTexts: prvtEpsProtctSignalFailRecovery.setStatus('current')
if mibBuilder.loadTexts: prvtEpsProtctSignalFailRecovery.setDescription('The alarm is issued in case of CCMs start to be received correctly again \n        on the protected link after a prvtEpsProtctSignalFailDetected alarm occured\n        and (3.5 * CCMtime(CCMinterval)) timer no longer expires or the link is up .')
mibBuilder.exportSymbols("PRVT-EPS-MIB", prvtEpsRestoredCommunication=prvtEpsRestoredCommunication, PrvtEpsActivePathType=PrvtEpsActivePathType, PrvtEpsRequestStateType=PrvtEpsRequestStateType, prvtEpsServiceDegradeTestEnable=prvtEpsServiceDegradeTestEnable, PrvtEpsProtectionType=PrvtEpsProtectionType, prvtEpsServiceSecondaryRemoteCfmMep=prvtEpsServiceSecondaryRemoteCfmMep, prvtEpsLostCommunication=prvtEpsLostCommunication, prvtEpsServiceApsChannel=prvtEpsServiceApsChannel, prvtEpsServiceProtectionCounter=prvtEpsServiceProtectionCounter, prvtEpsServiceRemoteState=prvtEpsServiceRemoteState, prvtEpsServiceRowStatus=prvtEpsServiceRowStatus, prvtEpsServiceRemoteApsChannel=prvtEpsServiceRemoteApsChannel, prvtEpsServiceAdminStatus=prvtEpsServiceAdminStatus, prvtEpsServiceWaitToRestoreTimer=prvtEpsServiceWaitToRestoreTimer, prvtEpsServiceProtection=prvtEpsServiceProtection, prvtEpsServiceActivePath=prvtEpsServiceActivePath, prvtEpsDefectAlarm=prvtEpsDefectAlarm, prvtEpsProtctSignalFailDetected=prvtEpsProtctSignalFailDetected, prvtEpsMib=prvtEpsMib, prvtEpsSwitchoverAlarm=prvtEpsSwitchoverAlarm, prvtEpsServiceLocalState=prvtEpsServiceLocalState, prvtEpsServiceCfmMdLevel=prvtEpsServiceCfmMdLevel, prvtEpsServiceDegradeTestType=prvtEpsServiceDegradeTestType, prvtEpsServiceDefectFop=prvtEpsServiceDefectFop, prvtEpsServiceHoldOffTimer=prvtEpsServiceHoldOffTimer, prvtEpsServicePrimaryStatus=prvtEpsServicePrimaryStatus, prvtEpsServiceDirection=prvtEpsServiceDirection, PYSNMP_MODULE_ID=prvtEpsMib, prvtEpsSvcId=prvtEpsSvcId, prvtEpsSignalDegradeRecovery=prvtEpsSignalDegradeRecovery, PrvtEpsPathStatusType=PrvtEpsPathStatusType, prvtEpsServiceRevertive=prvtEpsServiceRevertive, prvtEpsProtctSignalFailRecovery=prvtEpsProtctSignalFailRecovery, prvtEpsSignalFailDetected=prvtEpsSignalFailDetected, prvtEpsSignalFailRecovery=prvtEpsSignalFailRecovery, PrvtEpsMonitoringType=PrvtEpsMonitoringType, prvtEpsMibNotifications=prvtEpsMibNotifications, prvtEpsServiceDegradeTestName=prvtEpsServiceDegradeTestName, prvtEpsServiceEntry=prvtEpsServiceEntry, prvtEpsServiceSecondaryLocalCfmMep=prvtEpsServiceSecondaryLocalCfmMep, prvtEpsServiceSecondaryStatus=prvtEpsServiceSecondaryStatus, prvtEpsServiceRemoteProtection=prvtEpsServiceRemoteProtection, prvtEpsMibObjects=prvtEpsMibObjects, prvtEpsServiceDegradeTestOwner=prvtEpsServiceDegradeTestOwner, prvtEpsServiceAdminFreeze=prvtEpsServiceAdminFreeze, prvtEpsServiceRemoteRevertive=prvtEpsServiceRemoteRevertive, PrvtEpsDefectFopType=PrvtEpsDefectFopType, PrvtEpsDirectionType=PrvtEpsDirectionType, prvtEpsSignalDegradeDetected=prvtEpsSignalDegradeDetected, prvtEpsServiceTable=prvtEpsServiceTable, prvtEpsService=prvtEpsService, prvtEpsServiceRemoteDirection=prvtEpsServiceRemoteDirection, prvtEpsServicePrimaryLocalCfmMep=prvtEpsServicePrimaryLocalCfmMep, prvtEpsServicePrimaryRemoteCfmMep=prvtEpsServicePrimaryRemoteCfmMep, prvtEpsServiceOperationalStatus=prvtEpsServiceOperationalStatus)
