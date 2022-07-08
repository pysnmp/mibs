#
# PySNMP MIB module VMWARE-VCHA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VCHA-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:29:30 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, Counter64, Gauge32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, ObjectIdentity, IpAddress, Counter32, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "ObjectIdentity", "IpAddress", "Counter32", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
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
mibBuilder.exportSymbols("VMWARE-VCHA-MIB", vmwVchaDbReplicationStateChanged=vmwVchaDbReplicationStateChanged, VmwVchaClusterStateType=VmwVchaClusterStateType, vmwVchaNodeJoined=vmwVchaNodeJoined, VmwVchaNodeRoleType=VmwVchaNodeRoleType, vmwVchaFileReplicationStateChanged=vmwVchaFileReplicationStateChanged, vmwVchaNodeLeft=vmwVchaNodeLeft, vmwVchaNotificationGroup=vmwVchaNotificationGroup, vmwVchaPublicIpUp=vmwVchaPublicIpUp, vmwVchaFailoverFailedNodeLost=vmwVchaFailoverFailedNodeLost, vmwVchaDbReplicationState=vmwVchaDbReplicationState, vmwVchaPrivateAddressType=vmwVchaPrivateAddressType, vmwVchaWitness=vmwVchaWitness, vmwVchaFailoverFailedDisabledMode=vmwVchaFailoverFailedDisabledMode, vmwVchaFileReplicationProvider=vmwVchaFileReplicationProvider, VmwVchaDbReplicationStateType=VmwVchaDbReplicationStateType, vmwVchaContinueAsActive=vmwVchaContinueAsActive, vmwVchaActive=vmwVchaActive, vmwVchaClusterState=vmwVchaClusterState, vmwVchaMIBBasicComplianceRev2=vmwVchaMIBBasicComplianceRev2, vmwVchaFailoverTriggered=vmwVchaFailoverTriggered, vmwVchaMIBGroups=vmwVchaMIBGroups, vmwVchaMIBCompliances=vmwVchaMIBCompliances, VmwVchaFileReplicationProviderType=VmwVchaFileReplicationProviderType, vmwVchaIsPlannedFailover=vmwVchaIsPlannedFailover, vmwVchaPublicAddressType=vmwVchaPublicAddressType, vmwVchaNotificationInfoGroup=vmwVchaNotificationInfoGroup, vmwVchaClusterModeChanged=vmwVchaClusterModeChanged, vmwVCHANotifications=vmwVCHANotifications, vmwVchaNodeIsolated=vmwVchaNodeIsolated, vmwVchaInstanceUuid=vmwVchaInstanceUuid, vmwVchaPassive=vmwVchaPassive, vmwVchaFailoverFailedPassiveNotReady=vmwVchaFailoverFailedPassiveNotReady, vmwVchaClusterMode=vmwVchaClusterMode, vmwVchaFailoverSucceeded=vmwVchaFailoverSucceeded, vmwVchaIsFileProviderInSync=vmwVchaIsFileProviderInSync, vmwVchaPrivateAddressAddr=vmwVchaPrivateAddressAddr, vmwVchaMIB=vmwVchaMIB, vmwVchaMIBConformance=vmwVchaMIBConformance, vmwVchaClusterStateChanged=vmwVchaClusterStateChanged, vmwVchaPublicIpDown=vmwVchaPublicIpDown, vmwVchaTargetNodeRole=vmwVchaTargetNodeRole, vmwVchaPublicAddressAddr=vmwVchaPublicAddressAddr, PYSNMP_MODULE_ID=vmwVchaMIB, VmwVchaClusterModeType=VmwVchaClusterModeType)
