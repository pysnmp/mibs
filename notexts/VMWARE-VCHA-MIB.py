#
# PySNMP MIB module VMWARE-VCHA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VCHA-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 20:56:31 2022
# On host fv-az42-180 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, iso, Counter32, Counter64, Gauge32, ObjectIdentity, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Counter32", "Counter64", "Gauge32", "ObjectIdentity", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "MibIdentifier", "Integer32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
vmwVCHA, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwVCHA")
vmwVchaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 53, 1))
vmwVchaMIB.setRevisions(('2016-07-19 00:00', '2016-04-06 00:00', '2016-02-03 00:00', '2016-01-27 00:00', '2016-01-15 00:00', '2016-01-04 00:00',))
if mibBuilder.loadTexts: vmwVchaMIB.setLastUpdated('201607190000Z')
if mibBuilder.loadTexts: vmwVchaMIB.setOrganization('VMware, Inc')
vmwVCHANotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 0))
vmwVchaActive = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 250))
vmwVchaPassive = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 255))
vmwVchaWitness = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 260))
class VmwVchaNodeRoleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("passive", 2), ("witness", 3), ("unknown", 4))

class VmwVchaClusterModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("maintenance", 3))

class VmwVchaClusterStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("healthy", 1), ("degraded", 2), ("isolated", 3))

class VmwVchaDbReplicationStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4))
    namedValues = NamedValues(("noReplication", 1), ("sync", 3), ("async", 4))

class VmwVchaFileReplicationProviderType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("serviceConfig", 1), ("serviceState", 2))

vmwVchaNodeJoined = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 100)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"), ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"))
if mibBuilder.loadTexts: vmwVchaNodeJoined.setStatus('current')
vmwVchaNodeLeft = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 105)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"), ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"))
if mibBuilder.loadTexts: vmwVchaNodeLeft.setStatus('current')
vmwVchaNodeIsolated = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 110)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"), ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"))
if mibBuilder.loadTexts: vmwVchaNodeIsolated.setStatus('current')
vmwVchaClusterStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 130)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaClusterState"))
if mibBuilder.loadTexts: vmwVchaClusterStateChanged.setStatus('current')
vmwVchaClusterModeChanged = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 150)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaClusterMode"))
if mibBuilder.loadTexts: vmwVchaClusterModeChanged.setStatus('current')
vmwVchaPublicIpUp = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 205)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressAddr"))
if mibBuilder.loadTexts: vmwVchaPublicIpUp.setStatus('current')
vmwVchaPublicIpDown = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 206)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressAddr"))
if mibBuilder.loadTexts: vmwVchaPublicIpDown.setStatus('current')
vmwVchaFailoverTriggered = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 210)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaIsPlannedFailover"))
if mibBuilder.loadTexts: vmwVchaFailoverTriggered.setStatus('current')
vmwVchaFailoverSucceeded = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 220)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"))
if mibBuilder.loadTexts: vmwVchaFailoverSucceeded.setStatus('current')
vmwVchaFailoverFailedDisabledMode = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 225)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"))
if mibBuilder.loadTexts: vmwVchaFailoverFailedDisabledMode.setStatus('current')
vmwVchaFailoverFailedNodeLost = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 226)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"))
if mibBuilder.loadTexts: vmwVchaFailoverFailedNodeLost.setStatus('current')
vmwVchaFailoverFailedPassiveNotReady = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 227)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"))
if mibBuilder.loadTexts: vmwVchaFailoverFailedPassiveNotReady.setStatus('current')
vmwVchaContinueAsActive = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 230)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"))
if mibBuilder.loadTexts: vmwVchaContinueAsActive.setStatus('current')
vmwVchaDbReplicationStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 300)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaDbReplicationState"))
if mibBuilder.loadTexts: vmwVchaDbReplicationStateChanged.setStatus('current')
vmwVchaFileReplicationStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 350)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaFileReplicationProvider"), ("VMWARE-VCHA-MIB", "vmwVchaIsFileProviderInSync"))
if mibBuilder.loadTexts: vmwVchaFileReplicationStateChanged.setStatus('current')
vmwVchaInstanceUuid = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 5), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaInstanceUuid.setStatus('current')
vmwVchaPrivateAddressType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 11), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaPrivateAddressType.setStatus('current')
vmwVchaPublicAddressType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 12), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaPublicAddressType.setStatus('current')
vmwVchaPrivateAddressAddr = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 15), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaPrivateAddressAddr.setStatus('current')
vmwVchaPublicAddressAddr = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 16), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaPublicAddressAddr.setStatus('current')
vmwVchaTargetNodeRole = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 20), VmwVchaNodeRoleType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaTargetNodeRole.setStatus('current')
vmwVchaClusterState = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 25), VmwVchaClusterStateType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaClusterState.setStatus('current')
vmwVchaClusterMode = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 30), VmwVchaClusterModeType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaClusterMode.setStatus('current')
vmwVchaIsPlannedFailover = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 40), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaIsPlannedFailover.setStatus('current')
vmwVchaDbReplicationState = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 50), VmwVchaDbReplicationStateType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaDbReplicationState.setStatus('current')
vmwVchaIsFileProviderInSync = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 55), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaIsFileProviderInSync.setStatus('current')
vmwVchaFileReplicationProvider = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 60), VmwVchaFileReplicationProviderType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaFileReplicationProvider.setStatus('current')
vmwVchaMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2))
vmwVchaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 1))
vmwVchaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 2))
vmwVchaMIBBasicComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 1, 3)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaNotificationInfoGroup"), ("VMWARE-VCHA-MIB", "vmwVchaNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVchaMIBBasicComplianceRev2 = vmwVchaMIBBasicComplianceRev2.setStatus('current')
vmwVchaNotificationInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 2, 1)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressAddr"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"), ("VMWARE-VCHA-MIB", "vmwVchaClusterState"), ("VMWARE-VCHA-MIB", "vmwVchaClusterMode"), ("VMWARE-VCHA-MIB", "vmwVchaIsPlannedFailover"), ("VMWARE-VCHA-MIB", "vmwVchaDbReplicationState"), ("VMWARE-VCHA-MIB", "vmwVchaIsFileProviderInSync"), ("VMWARE-VCHA-MIB", "vmwVchaFileReplicationProvider"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVchaNotificationInfoGroup = vmwVchaNotificationInfoGroup.setStatus('current')
vmwVchaNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 2, 2)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaNodeJoined"), ("VMWARE-VCHA-MIB", "vmwVchaNodeLeft"), ("VMWARE-VCHA-MIB", "vmwVchaNodeIsolated"), ("VMWARE-VCHA-MIB", "vmwVchaClusterStateChanged"), ("VMWARE-VCHA-MIB", "vmwVchaClusterModeChanged"), ("VMWARE-VCHA-MIB", "vmwVchaPublicIpUp"), ("VMWARE-VCHA-MIB", "vmwVchaPublicIpDown"), ("VMWARE-VCHA-MIB", "vmwVchaFailoverTriggered"), ("VMWARE-VCHA-MIB", "vmwVchaFailoverSucceeded"), ("VMWARE-VCHA-MIB", "vmwVchaFailoverFailedDisabledMode"), ("VMWARE-VCHA-MIB", "vmwVchaFailoverFailedNodeLost"), ("VMWARE-VCHA-MIB", "vmwVchaFailoverFailedPassiveNotReady"), ("VMWARE-VCHA-MIB", "vmwVchaContinueAsActive"), ("VMWARE-VCHA-MIB", "vmwVchaDbReplicationStateChanged"), ("VMWARE-VCHA-MIB", "vmwVchaFileReplicationStateChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVchaNotificationGroup = vmwVchaNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("VMWARE-VCHA-MIB", vmwVchaClusterState=vmwVchaClusterState, vmwVchaTargetNodeRole=vmwVchaTargetNodeRole, vmwVchaMIB=vmwVchaMIB, PYSNMP_MODULE_ID=vmwVchaMIB, vmwVchaWitness=vmwVchaWitness, vmwVchaClusterStateChanged=vmwVchaClusterStateChanged, vmwVchaPublicAddressType=vmwVchaPublicAddressType, vmwVchaFailoverFailedNodeLost=vmwVchaFailoverFailedNodeLost, vmwVchaFailoverTriggered=vmwVchaFailoverTriggered, VmwVchaClusterStateType=VmwVchaClusterStateType, vmwVchaFailoverFailedPassiveNotReady=vmwVchaFailoverFailedPassiveNotReady, vmwVchaNodeIsolated=vmwVchaNodeIsolated, VmwVchaDbReplicationStateType=VmwVchaDbReplicationStateType, vmwVchaNotificationInfoGroup=vmwVchaNotificationInfoGroup, vmwVchaDbReplicationStateChanged=vmwVchaDbReplicationStateChanged, vmwVchaNotificationGroup=vmwVchaNotificationGroup, vmwVchaFailoverFailedDisabledMode=vmwVchaFailoverFailedDisabledMode, vmwVchaFileReplicationProvider=vmwVchaFileReplicationProvider, vmwVchaActive=vmwVchaActive, vmwVchaMIBBasicComplianceRev2=vmwVchaMIBBasicComplianceRev2, vmwVchaPublicAddressAddr=vmwVchaPublicAddressAddr, VmwVchaNodeRoleType=VmwVchaNodeRoleType, vmwVchaPublicIpUp=vmwVchaPublicIpUp, vmwVchaPassive=vmwVchaPassive, vmwVchaClusterModeChanged=vmwVchaClusterModeChanged, vmwVchaClusterMode=vmwVchaClusterMode, vmwVchaIsFileProviderInSync=vmwVchaIsFileProviderInSync, vmwVchaMIBGroups=vmwVchaMIBGroups, vmwVchaPublicIpDown=vmwVchaPublicIpDown, vmwVchaPrivateAddressAddr=vmwVchaPrivateAddressAddr, vmwVchaDbReplicationState=vmwVchaDbReplicationState, vmwVchaNodeJoined=vmwVchaNodeJoined, vmwVchaFileReplicationStateChanged=vmwVchaFileReplicationStateChanged, vmwVCHANotifications=vmwVCHANotifications, VmwVchaFileReplicationProviderType=VmwVchaFileReplicationProviderType, VmwVchaClusterModeType=VmwVchaClusterModeType, vmwVchaNodeLeft=vmwVchaNodeLeft, vmwVchaInstanceUuid=vmwVchaInstanceUuid, vmwVchaContinueAsActive=vmwVchaContinueAsActive, vmwVchaIsPlannedFailover=vmwVchaIsPlannedFailover, vmwVchaMIBConformance=vmwVchaMIBConformance, vmwVchaFailoverSucceeded=vmwVchaFailoverSucceeded, vmwVchaPrivateAddressType=vmwVchaPrivateAddressType, vmwVchaMIBCompliances=vmwVchaMIBCompliances)
