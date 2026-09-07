#
# PySNMP MIB module CISCO-C8500-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-C8500-REDUNDANCY-MIB
# Source digest sha256:2cd4f40e18518176ece884f870f41b0c8b5282e9bb952e68c9306202d3434ca8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp", "TruthValue")
ciscoC8500RedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 105))
ciscoC8500RedundancyMIB.setRevisions(('2003-05-04 00:00', '1998-06-22 00:00',))
if mibBuilder.loadTexts: ciscoC8500RedundancyMIB.setLastUpdated('2003-05-04 00:00')
if mibBuilder.loadTexts: ciscoC8500RedundancyMIB.setOrganization('Cisco Systems, Inc.')
class RedundancyStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notPresent", 1), ("ok", 2), ("fault", 3))

class RedundancyMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("standby", 2), ("unused", 3), ("notPresent", 4))

class RedundancySlotIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

ciscoC8500RedundancyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 1))
ccrCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1))
ccrSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2))
ccrCpuTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccrCpuTable.setStatus('current')
ccrCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-C8500-REDUNDANCY-MIB", "ccrCpuSlotIndex"))
if mibBuilder.loadTexts: ccrCpuEntry.setStatus('current')
ccrCpuSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 1), RedundancySlotIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccrCpuSlotIndex.setStatus('current')
ccrCpuMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 2), RedundancyMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrCpuMode.setStatus('current')
ccrCpuStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 3), RedundancyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrCpuStatus.setStatus('current')
ccrSyncConfigOnSet = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 2), Bits().clone(namedValues=NamedValues(("runningConfig", 0), ("startupConfig", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrSyncConfigOnSet.setStatus('current')
ccrCpuStandbyEnableMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrCpuStandbyEnableMode.setStatus('current')
ccrCpuSwitchoverTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrCpuSwitchoverTime.setStatus('current')
ccrForceCounterSync = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forcesync", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrForceCounterSync.setStatus('current')
ccrIfCounterSyncFreq = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrIfCounterSyncFreq.setStatus('current')
ccrVcCounterSyncFreq = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrVcCounterSyncFreq.setStatus('current')
ccrSigCounterSyncEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrSigCounterSyncEnable.setStatus('current')
ccrSwitchTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccrSwitchTable.setStatus('current')
ccrSwitchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchSlotIndex"))
if mibBuilder.loadTexts: ccrSwitchEntry.setStatus('current')
ccrSwitchSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 1), RedundancySlotIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccrSwitchSlotIndex.setStatus('current')
ccrSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 2), RedundancyMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrSwitchMode.setStatus('current')
ccrSwitchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 3), RedundancyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrSwitchStatus.setStatus('current')
ccrSwitchLastSwitchoverTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrSwitchLastSwitchoverTime.setStatus('current')
ccrSwitchLastSwitchoverReason = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("notKnown", 2), ("userInitiated", 3), ("cardFailed", 4), ("cardRecovered", 5), ("cardRemoved", 6), ("cardInserted", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrSwitchLastSwitchoverReason.setStatus('current')
ccrSwitchBw = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tenGbps", 1), ("twentyGbps", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccrSwitchBw.setStatus('current')
ccrDesiredSwitchBw = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tenGbps", 1), ("twentyGbps", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccrDesiredSwitchBw.setStatus('current')
ciscoC8500RedundancyMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 2))
ccrMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0))
ccrCpuStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 1)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatus"))
if mibBuilder.loadTexts: ccrCpuStatusChange.setStatus('current')
ccrSwitchStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 2)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchStatus"))
if mibBuilder.loadTexts: ccrSwitchStatusChange.setStatus('current')
ccrSwitchModeChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 3)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchMode"))
if mibBuilder.loadTexts: ccrSwitchModeChange.setStatus('current')
ciscoC8500RedundancyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 3))
ciscoC8500RedundancyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 1))
ciscoC8500RedundancyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2))
ciscoC8500RedundancyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 1, 1)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuMibGroup"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchMibGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoC8500RedundancyMIBCompliance = ciscoC8500RedundancyMIBCompliance.setStatus('obsolete')
ciscoC8500RedundancyMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 1, 2)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuMibGroup1"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchMibGroup"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoC8500RedundancyMIBComplianceRev1 = ciscoC8500RedundancyMIBComplianceRev1.setStatus('current')
ccrCpuMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 1)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuMode"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatus"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSyncConfigOnSet"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrCpuMibGroup = ccrCpuMibGroup.setStatus('obsolete')
ccrSwitchMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 2)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchMode"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchStatus"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchLastSwitchoverTime"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchLastSwitchoverReason"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchBw"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrDesiredSwitchBw"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrSwitchMibGroup = ccrSwitchMibGroup.setStatus('current')
ccrNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 3)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatusChange"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchStatusChange"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchModeChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrNotificationsGroup = ccrNotificationsGroup.setStatus('current')
ccrCpuMibGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 4)).setObjects(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuMode"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatus"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSyncConfigOnSet"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStandbyEnableMode"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuSwitchoverTime"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrForceCounterSync"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrIfCounterSyncFreq"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrVcCounterSyncFreq"), ("CISCO-C8500-REDUNDANCY-MIB", "ccrSigCounterSyncEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrCpuMibGroup1 = ccrCpuMibGroup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-C8500-REDUNDANCY-MIB", PYSNMP_MODULE_ID=ciscoC8500RedundancyMIB, RedundancyMode=RedundancyMode, RedundancySlotIndex=RedundancySlotIndex, RedundancyStatus=RedundancyStatus, ccrCpu=ccrCpu, ccrCpuEntry=ccrCpuEntry, ccrCpuMibGroup1=ccrCpuMibGroup1, ccrCpuMibGroup=ccrCpuMibGroup, ccrCpuMode=ccrCpuMode, ccrCpuSlotIndex=ccrCpuSlotIndex, ccrCpuStandbyEnableMode=ccrCpuStandbyEnableMode, ccrCpuStatus=ccrCpuStatus, ccrCpuStatusChange=ccrCpuStatusChange, ccrCpuSwitchoverTime=ccrCpuSwitchoverTime, ccrCpuTable=ccrCpuTable, ccrDesiredSwitchBw=ccrDesiredSwitchBw, ccrForceCounterSync=ccrForceCounterSync, ccrIfCounterSyncFreq=ccrIfCounterSyncFreq, ccrMIBNotifications=ccrMIBNotifications, ccrNotificationsGroup=ccrNotificationsGroup, ccrSigCounterSyncEnable=ccrSigCounterSyncEnable, ccrSwitch=ccrSwitch, ccrSwitchBw=ccrSwitchBw, ccrSwitchEntry=ccrSwitchEntry, ccrSwitchLastSwitchoverReason=ccrSwitchLastSwitchoverReason, ccrSwitchLastSwitchoverTime=ccrSwitchLastSwitchoverTime, ccrSwitchMibGroup=ccrSwitchMibGroup, ccrSwitchMode=ccrSwitchMode, ccrSwitchModeChange=ccrSwitchModeChange, ccrSwitchSlotIndex=ccrSwitchSlotIndex, ccrSwitchStatus=ccrSwitchStatus, ccrSwitchStatusChange=ccrSwitchStatusChange, ccrSwitchTable=ccrSwitchTable, ccrSyncConfigOnSet=ccrSyncConfigOnSet, ccrVcCounterSyncFreq=ccrVcCounterSyncFreq, ciscoC8500RedundancyMIB=ciscoC8500RedundancyMIB, ciscoC8500RedundancyMIBCompliance=ciscoC8500RedundancyMIBCompliance, ciscoC8500RedundancyMIBComplianceRev1=ciscoC8500RedundancyMIBComplianceRev1, ciscoC8500RedundancyMIBCompliances=ciscoC8500RedundancyMIBCompliances, ciscoC8500RedundancyMIBConformance=ciscoC8500RedundancyMIBConformance, ciscoC8500RedundancyMIBGroups=ciscoC8500RedundancyMIBGroups, ciscoC8500RedundancyMIBNotificationPrefix=ciscoC8500RedundancyMIBNotificationPrefix, ciscoC8500RedundancyMIBObjects=ciscoC8500RedundancyMIBObjects)
