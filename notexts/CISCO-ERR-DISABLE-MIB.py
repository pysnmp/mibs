#
# PySNMP MIB module CISCO-ERR-DISABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ERR-DISABLE-MIB
# Source digest sha256:eb06f33be7cdb260531b8260e752c5547eb20eeaa2bd11c6cef84bad34362c3a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
VlanIndexOrZero, = mibBuilder.importSymbols("CISCO-PRIVATE-VLAN-MIB", "VlanIndexOrZero")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoErrDisableMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 548))
ciscoErrDisableMIB.setRevisions(('2019-11-28 00:00', '2016-06-02 00:00', '2013-04-23 00:00', '2010-10-19 00:00', '2009-03-23 00:00', '2008-04-07 00:00', '2006-05-31 00:00',))
if mibBuilder.loadTexts: ciscoErrDisableMIB.setLastUpdated('2019-11-28 00:00')
if mibBuilder.loadTexts: ciscoErrDisableMIB.setOrganization('Cisco Systems, Inc.')
ciscoErrDisableMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 0))
ciscoErrDisableMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 1))
ciscoErrDisableMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 2))
cErrDisableGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1))
cErrDisableFeatureObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2))
cErrDisableIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3))
class CErrDisableFeatureID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62))
    namedValues = NamedValues(("udld", 1), ("bpduGuard", 2), ("channelMisconfig", 3), ("pagpFlap", 4), ("dtpFlap", 5), ("linkFlap", 6), ("l2ptGuard", 7), ("dot1xSecurityViolation", 8), ("portSecurityViolation", 9), ("gbicInvalid", 10), ("dhcpRateLimit", 11), ("unicastFlood", 12), ("vmps", 13), ("stormControl", 14), ("inlinePower", 15), ("arpInspection", 16), ("portLoopback", 17), ("packetBuffer", 18), ("macLimit", 19), ("linkMonitorFailure", 20), ("oamRemoteFailure", 21), ("dot1adIncompEtype", 22), ("dot1adIncompTunnel", 23), ("sfpConfigMismatch", 24), ("communityLimit", 25), ("invalidPolicy", 26), ("lsGroup", 27), ("ekey", 28), ("portModeFailure", 29), ("pppoeIaRateLimit", 30), ("oamRemoteCriticalEvent", 31), ("oamRemoteDyingGasp", 32), ("oamRemoteLinkFault", 33), ("mvrp", 34), ("tranceiverIncomp", 35), ("other", 36), ("portReinitLimitReached", 37), ("adminRxBBCreditPerfBufIncomp", 38), ("ficonNotEnabled", 39), ("adminModeIncomp", 40), ("adminSpeedIncomp", 41), ("adminRxBBCreditIncomp", 42), ("adminRxBufSizeIncomp", 43), ("eppFailure", 44), ("osmEPortUp", 45), ("osmNonEPortUp", 46), ("udldUniDir", 47), ("udldTxRxLoop", 48), ("udldNeighbourMismatch", 49), ("udldEmptyEcho", 50), ("udldAggrasiveModeLinkFailed", 51), ("excessivePortInterrupts", 52), ("channelErrDisabled", 53), ("hwProgFailed", 54), ("internalHandshakeFailed", 55), ("stpInconsistencyOnVpcPeerLink", 56), ("stpPortStateFailure", 57), ("ipConflict", 58), ("multipleMSapIdsRcvd", 59), ("oneHundredPdusWithoutAck", 60), ("ipQosCompatCheckFailure", 61), ("loopDetect", 62))

cErrDisableRecoveryInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1, 1), TimeIntervalSec()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableRecoveryInterval.setStatus('current')
cErrDisableNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableNotifEnable.setStatus('current')
cErrDisableNotifRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 1, 3), Unsigned32()).setUnits('Notification/Minute').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableNotifRate.setStatus('current')
cErrDisableFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cErrDisableFeatureTable.setStatus('current')
cErrDisableFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureIndex"))
if mibBuilder.loadTexts: cErrDisableFeatureEntry.setStatus('current')
cErrDisableFeatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 1), CErrDisableFeatureID()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cErrDisableFeatureIndex.setStatus('current')
cErrDisableFeatureConfigurable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 2), Bits().clone(namedValues=NamedValues(("detectionEnable", 0), ("recoveryEnable", 1), ("recoveryInterval", 2), ("detectShutdownVlan", 3), ("flapControl", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cErrDisableFeatureConfigurable.setStatus('current')
cErrDisableFeatureDetectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureDetectEnable.setStatus('current')
cErrDisableFeatureRecoveryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureRecoveryEnable.setStatus('current')
cErrDisableFeatureRecoveryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 5), TimeIntervalSec()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureRecoveryInterval.setStatus('current')
cErrDisableFeatureDetectShutdownVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureDetectShutdownVlan.setStatus('current')
cErrDisableFeatureMaxFlapCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureMaxFlapCount.setStatus('current')
cErrDisableFeatureFlapTimePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cErrDisableFeatureFlapTimePeriod.setStatus('current')
cErrDisableIfStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cErrDisableIfStatusTable.setStatus('current')
cErrDisableIfStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusVlanIndex"))
if mibBuilder.loadTexts: cErrDisableIfStatusEntry.setStatus('current')
cErrDisableIfStatusVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1, 1), VlanIndexOrZero()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cErrDisableIfStatusVlanIndex.setStatus('current')
cErrDisableIfStatusCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1, 2), CErrDisableFeatureID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cErrDisableIfStatusCause.setStatus('current')
cErrDisableIfStatusTimeToRecover = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 548, 1, 3, 1, 1, 3), TimeIntervalSec()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cErrDisableIfStatusTimeToRecover.setStatus('current')
cErrDisableNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 0, 1))
cErrDisableInterfaceEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 548, 0, 1, 1)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusCause"))
if mibBuilder.loadTexts: cErrDisableInterfaceEvent.setStatus('deprecated')
cErrDisableInterfaceEventRev1 = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 548, 0, 2)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusCause"))
if mibBuilder.loadTexts: cErrDisableInterfaceEventRev1.setStatus('current')
ciscoErrDisableMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1))
ciscoErrDisableMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2))
ciscoErrDisableMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1, 1)).setObjects(("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableGlobalCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableIfStatusGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableMIBCompliance = ciscoErrDisableMIBCompliance.setStatus('deprecated')
ciscoErrDisableMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1, 2)).setObjects(("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableGlobalCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableIfStatusGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifGroupRev1"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableShutdownVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableMIBComplianceRev1 = ciscoErrDisableMIBComplianceRev1.setStatus('deprecated')
ciscoErrDisableMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 1, 3)).setObjects(("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableGlobalCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableIfStatusGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifCfgGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableNotifGroupRev1"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableShutdownVlanGroup"), ("CISCO-ERR-DISABLE-MIB", "ciscoErrDisableFeatureFlapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableMIBComplianceRev2 = ciscoErrDisableMIBComplianceRev2.setStatus('current')
ciscoErrDisableGlobalCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 1)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableRecoveryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableGlobalCfgGroup = ciscoErrDisableGlobalCfgGroup.setStatus('current')
ciscoErrDisableFeatureCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 2)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureConfigurable"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureDetectEnable"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureRecoveryEnable"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureRecoveryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableFeatureCfgGroup = ciscoErrDisableFeatureCfgGroup.setStatus('current')
ciscoErrDisableIfStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 3)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusCause"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableIfStatusTimeToRecover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableIfStatusGroup = ciscoErrDisableIfStatusGroup.setStatus('current')
ciscoErrDisableNotifCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 4)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableNotifEnable"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableNotifRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableNotifCfgGroup = ciscoErrDisableNotifCfgGroup.setStatus('current')
ciscoErrDisableNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 5)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableInterfaceEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableNotifGroup = ciscoErrDisableNotifGroup.setStatus('deprecated')
ciscoErrDisableNotifGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 6)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableInterfaceEventRev1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableNotifGroupRev1 = ciscoErrDisableNotifGroupRev1.setStatus('current')
ciscoErrDisableShutdownVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 7)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureDetectShutdownVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableShutdownVlanGroup = ciscoErrDisableShutdownVlanGroup.setStatus('current')
ciscoErrDisableFeatureFlapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 548, 2, 2, 8)).setObjects(("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureMaxFlapCount"), ("CISCO-ERR-DISABLE-MIB", "cErrDisableFeatureFlapTimePeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErrDisableFeatureFlapGroup = ciscoErrDisableFeatureFlapGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ERR-DISABLE-MIB", CErrDisableFeatureID=CErrDisableFeatureID, PYSNMP_MODULE_ID=ciscoErrDisableMIB, cErrDisableFeatureConfigurable=cErrDisableFeatureConfigurable, cErrDisableFeatureDetectEnable=cErrDisableFeatureDetectEnable, cErrDisableFeatureDetectShutdownVlan=cErrDisableFeatureDetectShutdownVlan, cErrDisableFeatureEntry=cErrDisableFeatureEntry, cErrDisableFeatureFlapTimePeriod=cErrDisableFeatureFlapTimePeriod, cErrDisableFeatureIndex=cErrDisableFeatureIndex, cErrDisableFeatureMaxFlapCount=cErrDisableFeatureMaxFlapCount, cErrDisableFeatureObjects=cErrDisableFeatureObjects, cErrDisableFeatureRecoveryEnable=cErrDisableFeatureRecoveryEnable, cErrDisableFeatureRecoveryInterval=cErrDisableFeatureRecoveryInterval, cErrDisableFeatureTable=cErrDisableFeatureTable, cErrDisableGlobalObjects=cErrDisableGlobalObjects, cErrDisableIfObjects=cErrDisableIfObjects, cErrDisableIfStatusCause=cErrDisableIfStatusCause, cErrDisableIfStatusEntry=cErrDisableIfStatusEntry, cErrDisableIfStatusTable=cErrDisableIfStatusTable, cErrDisableIfStatusTimeToRecover=cErrDisableIfStatusTimeToRecover, cErrDisableIfStatusVlanIndex=cErrDisableIfStatusVlanIndex, cErrDisableInterfaceEvent=cErrDisableInterfaceEvent, cErrDisableInterfaceEventRev1=cErrDisableInterfaceEventRev1, cErrDisableNotifEnable=cErrDisableNotifEnable, cErrDisableNotifRate=cErrDisableNotifRate, cErrDisableNotificationsPrefix=cErrDisableNotificationsPrefix, cErrDisableRecoveryInterval=cErrDisableRecoveryInterval, ciscoErrDisableFeatureCfgGroup=ciscoErrDisableFeatureCfgGroup, ciscoErrDisableFeatureFlapGroup=ciscoErrDisableFeatureFlapGroup, ciscoErrDisableGlobalCfgGroup=ciscoErrDisableGlobalCfgGroup, ciscoErrDisableIfStatusGroup=ciscoErrDisableIfStatusGroup, ciscoErrDisableMIB=ciscoErrDisableMIB, ciscoErrDisableMIBCompliance=ciscoErrDisableMIBCompliance, ciscoErrDisableMIBComplianceRev1=ciscoErrDisableMIBComplianceRev1, ciscoErrDisableMIBComplianceRev2=ciscoErrDisableMIBComplianceRev2, ciscoErrDisableMIBCompliances=ciscoErrDisableMIBCompliances, ciscoErrDisableMIBConform=ciscoErrDisableMIBConform, ciscoErrDisableMIBGroups=ciscoErrDisableMIBGroups, ciscoErrDisableMIBNotifs=ciscoErrDisableMIBNotifs, ciscoErrDisableMIBObjects=ciscoErrDisableMIBObjects, ciscoErrDisableNotifCfgGroup=ciscoErrDisableNotifCfgGroup, ciscoErrDisableNotifGroup=ciscoErrDisableNotifGroup, ciscoErrDisableNotifGroupRev1=ciscoErrDisableNotifGroupRev1, ciscoErrDisableShutdownVlanGroup=ciscoErrDisableShutdownVlanGroup)
