#
# PySNMP MIB module VMWARE-VCHA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VCHA-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 09:16:37 2023
# On host fv-az351-145 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, ObjectIdentity, Counter32, NotificationType, Integer32, Counter64, Gauge32, TimeTicks, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter32", "NotificationType", "Integer32", "Counter64", "Gauge32", "TimeTicks", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
vmwVCHA, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwVCHA")
vmwVchaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 53, 1))
vmwVchaMIB.setRevisions(('2016-07-19 00:00', '2016-04-06 00:00', '2016-02-03 00:00', '2016-01-27 00:00', '2016-01-15 00:00', '2016-01-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwVchaMIB.setRevisionsDescriptions(('Removed vmwVchaFileReplicationEventQueueOverflowed and cleaned up a few\n     descriptions. Fixed vCenter HA related terminologies and typos.', 'Aggregate vmwVchaFileWatchFailed, vmwVchaFileReplicationFailed and\n     vmwVchaFileResyncSucceeded into vmwVchaFileReplicationStateChanged\n     notification. Add three more notification for failover failure cases.\n     Combine syncPeerStarted and syncPeerCompleted into a single state: sync.', 'Add two more notifications vmwVchaFailoverSucceeded and\n     vmwVchaContinueAsActive to indicate whether a failover succeeds. Also add\n     one more parameter to vmwVchaNodeJoined and vmwVchaNodeLeft to distinguish\n     between the role of sender node and target node.', 'Change the terminology from DB replication mode to DB replication state\n     and add one more state to it. Also use past tense for all notification\n     names.', 'Add two more notifications vmwVchaClusterStateChange and\n     vmwVchaFileReplicationEventQueueOverflowed.', 'This is the first version of this MIB module.',))
if mibBuilder.loadTexts: vmwVchaMIB.setLastUpdated('201607190000Z')
if mibBuilder.loadTexts: vmwVchaMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwVchaMIB.setContactInfo('VMware, Inc\n    3401 Hillview Ave\n    Palo Alto, CA 94304\n    Tel: 1-877-486-9273 or 650-427-5000\n    Fax: 650-427-5001\n    Web: http://communities.vmware.com/community/developer/forums/managementapi\n    ')
if mibBuilder.loadTexts: vmwVchaMIB.setDescription('This MIB module describes the vCenter High Availability Service (VCHA).\n     A VCHA cluster consists of three VMs identified by a single instance UUID.\n     One is the Active vCenter VM that serves client requests. Second is the\n     Passive VM that is identical to the Active vCenter VM in terms of database\n     and filesystem state. Passive VM constantly receives updates from Active\n     VM and takes over the role of Active vCenter VM in the event of a\n     failover. Third is the Witness VM that acts as a quorum VM in a VCHA\n     cluster. The sole purpose of Witness VM is to avoid classic split-brain\n     problem in a VCHA cluster.\n\n                             client\n                                +\n                                |\n                                |\n               +----------------v---+       +--------------------+\n               |            Public IP       |                    |\n               |                    |       |                    |\n               |   Active vCenter   |       |  Passive vCenter   |\n               |                    |       |                    |\n               +---Private-IP+------+       +------+Private-IP---+\n                        ^ <--------------------------> ^\n                        |    DB & File replication     |\n                         +                            +\n                          +                          +\n                           +                        +\n                            +------>    <----------+\n                              +----Private-IP----+\n                              |                  |\n                              |  Witness vCenter |\n                              |     (Quorum)     |\n                              |                  |\n                              +------------------+\n\n    All events will not be repeated for the duration of a given state entered.\n\n    It is highly recommended that the administrator links the SNMP trap receiver\n    to both public network and vCenter HA cluster network, so that the\n    monitoring system is able to get notified as long as one of the\n    networks is up.\n    ')
vmwVCHANotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 0))
vmwVchaActive = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 250))
vmwVchaPassive = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 255))
vmwVchaWitness = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 260))
class VmwVchaNodeRoleType(TextualConvention, Integer32):
    description = 'Represent the role each node in the cluster is running as.\n            active (1)      Active vCenter serves client requests.\n\n            passive (2)     Passive node is identical to the Active node in\n                            terms of database and filesystem state. Passive\n                            node constantly receives updates from the Active\n                            node and takes over the role of Active node in the\n                            event of a failover.\n\n            witness (3)     Witness node acts as a quorum node in a vCenter HA\n                            cluster. Sole purpose of Witness VM is to avoid\n                            the classic split-brain problem in a VCHA cluster.\n\n            unknown (4)     Node without any role assigned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("passive", 2), ("witness", 3), ("unknown", 4))

class VmwVchaClusterModeType(TextualConvention, Integer32):
    description = 'Represent VCHA cluster modes: enabled, disabled or maintenance:\n\n            enabled (1)     State replication between Active and Passive nodes\n                            is enabled and automatic failover happens if the\n                            Active node fails while the VCHA cluster is healthy.\n\n            disabled (2)    All three nodes are part of VCHA cluster but the\n                            state replication and automatic failover are\n                            disabled.\n\n            maintenance (3) All three nodes are part of VCHA cluster but\n                            automatic failover is disabled while state\n                            replication continues. The Active node continues to\n                            serve client requests even if Passive and Witness\n                            nodes are lost.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("maintenance", 3))

class VmwVchaClusterStateType(TextualConvention, Integer32):
    description = 'Represent the health state of the vCenter HA cluster.\n\n            healthy (1)     All three nodes in a VCHA cluster are healthy and\n                            connected. State replication between the Active and\n                            Passive nodes is working and both nodes are in-sync.\n\n            degraded (2)    A VCHA cluster is said to be in degraded state when\n                            it has lost one of the three nodes. Node loss can\n                            be due to various reasons and as a result, the lost\n                            node is not visible to other two nodes. If the\n                            Active node is lost, the Passive node will take the\n                            role of the Active node. If the Passive or Witness\n                            node is lost, the Active node will continue to serve\n                            requests. A VCHA cluster can also be in degraded\n                            state if state replication fails between the Active\n                            and Passive nodes.\n\n            isolated (3)    All three nodes are isolated from each other. If\n                            this happens when VCHA cluster is in enabled mode,\n                            the Active node stops serving client requests. If\n                            nodes are isolated in a disabled VCHA cluster mode,\n                            the Active node continues to serve client requests.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("healthy", 1), ("degraded", 2), ("isolated", 3))

class VmwVchaDbReplicationStateType(TextualConvention, Integer32):
    description = 'Represent DB replication states: sync, async or no replication.\n\n            noReplication (1)   There is no DB replication between the Active\n                                and Passive nodes. This could happen when\n                                vPostgres is not running on the Passive node.\n\n            sync (3)            In sync state, the Passive vCenter keeps the\n                                up-to-date state with the Active vCenter.\n\n            async (4)           Async state replication makes the state of\n                                Passive node fall behind the Active vCenter.\n                                This causes a data loss when an automatic\n                                failover happens.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4))
    namedValues = NamedValues(("noReplication", 1), ("sync", 3), ("async", 4))

class VmwVchaFileReplicationProviderType(TextualConvention, Integer32):
    description = 'Represent the file replication providers.\n\n            serviceConfig (1)   This provider maintains the replication of\n                                service configuration files, which are small in\n                                size.\n\n            serviceState (2)    This provider maintains the replication of\n                                service state files, which are large in size.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("serviceConfig", 1), ("serviceState", 2))

vmwVchaNodeJoined = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 100)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"), ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"))
if mibBuilder.loadTexts: vmwVchaNodeJoined.setStatus('current')
if mibBuilder.loadTexts: vmwVchaNodeJoined.setDescription('This informative notification is sent from the Active node when it\n        notices a peer node rejoin the cluster. It is sent only once.')
vmwVchaNodeLeft = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 105)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"), ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"))
if mibBuilder.loadTexts: vmwVchaNodeLeft.setStatus('current')
if mibBuilder.loadTexts: vmwVchaNodeLeft.setDescription('This warning notification is sent from the Active node when it notices\n        a peer node has left the cluster. This is sent only once. Operator\n        should check the liveness and connectivity of the departed node and try\n        to bring it back by either rebooting the appliance or resolving the\n        network problem.')
vmwVchaNodeIsolated = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 110)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"), ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"))
if mibBuilder.loadTexts: vmwVchaNodeIsolated.setStatus('current')
if mibBuilder.loadTexts: vmwVchaNodeIsolated.setDescription('This warning notification is sent when a node is network isolated from\n        the cluster. This notification can only be sent from the isolated node,\n        not by other nodes in the cluster. After being isolated, the node will\n        reboot itself trigging coldStart notification. In case of Active node\n        failure, the cluster will trigger a reelection and every slave node will\n        be declared as isolated temporarily before the cluster re-election\n        completes.')
vmwVchaClusterStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 130)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaClusterState"))
if mibBuilder.loadTexts: vmwVchaClusterStateChanged.setStatus('current')
if mibBuilder.loadTexts: vmwVchaClusterStateChanged.setDescription('This notification is sent only once from the Active node when vCenter\n        HA cluster state changes to either healthy, degraded or isolated. Please\n        see VmwVchaClusterStateType for detailed description of each state. And\n        administrator should receive another notification describing the state\n        change of cluster subsystem (cluster membership, DB replication or file\n        replication) which is trigger of cluster state change.')
vmwVchaClusterModeChanged = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 150)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaClusterMode"))
if mibBuilder.loadTexts: vmwVchaClusterModeChanged.setStatus('current')
if mibBuilder.loadTexts: vmwVchaClusterModeChanged.setDescription('This notification is sent only once from the Active node when vCenter\n        HA cluster mode changes to either enabled, maintenance or disabled.')
vmwVchaPublicIpUp = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 205)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressAddr"))
if mibBuilder.loadTexts: vmwVchaPublicIpUp.setStatus('current')
if mibBuilder.loadTexts: vmwVchaPublicIpUp.setDescription('This informative notification is sent only once when the public IP\n        address is brought up on the Active node. At this time, the Active node\n        is reachable from the client and will be able to serve client requests\n        when services are up and running.')
vmwVchaPublicIpDown = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 206)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressAddr"))
if mibBuilder.loadTexts: vmwVchaPublicIpDown.setStatus('current')
if mibBuilder.loadTexts: vmwVchaPublicIpDown.setDescription('This informative notification is sent only once when the public\n        network interface is brought down on the Active node. This can happen\n        when InitiateFailover is invoked on the Active node or vcha process\n        gracefully shuts down resulting in a reboot of the appliance (triggered\n        by network isolation). During this time, clients cannot connect to\n        vCenter Server and users will experience downtime until the public\n        network interface is brought up. In either case, users should not\n        expect more than five minutes of downtime. If VCHA cluster is still not\n        connectable, the operator should verify the reachability of each node\n        through the cluster network.')
vmwVchaFailoverTriggered = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 210)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaIsPlannedFailover"))
if mibBuilder.loadTexts: vmwVchaFailoverTriggered.setStatus('current')
if mibBuilder.loadTexts: vmwVchaFailoverTriggered.setDescription('This informative notification is sent only once when a failover is\n        triggered from the Active node to Passive node. Passive node should\n        take over the Active role if the cluster is in healthy state.')
vmwVchaFailoverSucceeded = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 220)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"))
if mibBuilder.loadTexts: vmwVchaFailoverSucceeded.setStatus('current')
if mibBuilder.loadTexts: vmwVchaFailoverSucceeded.setDescription('This informative notification is sent only once when the Passive node\n        takes over the Active role and brings up the public network interface.')
vmwVchaFailoverFailedDisabledMode = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 225)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"))
if mibBuilder.loadTexts: vmwVchaFailoverFailedDisabledMode.setStatus('current')
if mibBuilder.loadTexts: vmwVchaFailoverFailedDisabledMode.setDescription('This warning notification is sent only once when the Active node fails\n        to initiate a failover because the cluster is in disabled mode.')
vmwVchaFailoverFailedNodeLost = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 226)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"))
if mibBuilder.loadTexts: vmwVchaFailoverFailedNodeLost.setStatus('current')
if mibBuilder.loadTexts: vmwVchaFailoverFailedNodeLost.setDescription('This warning notification is sent only once when the Active node fails\n        to initiate a failover because the cluster does not have all three\n        nodes connected.')
vmwVchaFailoverFailedPassiveNotReady = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 227)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"))
if mibBuilder.loadTexts: vmwVchaFailoverFailedPassiveNotReady.setStatus('current')
if mibBuilder.loadTexts: vmwVchaFailoverFailedPassiveNotReady.setDescription('This warning notification is sent only once when the Active node fails\n        to initiate a failover because vPostgres service on the Passive node is\n        not ready to take over.')
vmwVchaContinueAsActive = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 230)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"))
if mibBuilder.loadTexts: vmwVchaContinueAsActive.setStatus('current')
if mibBuilder.loadTexts: vmwVchaContinueAsActive.setDescription("This informative notification is sent only once when the last Active\n        node continue as the Active node to servce client's request. This can\n        happen in many scenarios:\n        1. After triggering a planned failover, DB or file replicator failed to\n        flush data to the Passive node and failover didn't proceed because of\n        data loss.\n        2. After triggering a planned or forced failover, Passive node failed to\n        pick up the Active role for reasons like: auto failover cannot happen in\n        maintenance mode or cluster is in disabled mode.")
vmwVchaDbReplicationStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 300)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaDbReplicationState"))
if mibBuilder.loadTexts: vmwVchaDbReplicationStateChanged.setStatus('current')
if mibBuilder.loadTexts: vmwVchaDbReplicationStateChanged.setDescription('This informative notification is sent only once from the Active node\n        when database replication state changes to sync, async or no\n        replication. Database replication is not healthy when it is in async or\n        no replication state. Reasons include large network delays or vPostgres\n        service becoming unresponsive on the Passive node.')
vmwVchaFileReplicationStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 6876, 53, 0, 350)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaFileReplicationProvider"), ("VMWARE-VCHA-MIB", "vmwVchaIsFileProviderInSync"))
if mibBuilder.loadTexts: vmwVchaFileReplicationStateChanged.setStatus('current')
if mibBuilder.loadTexts: vmwVchaFileReplicationStateChanged.setDescription('This informative notification is sent only once from the Active node\n        when file replication state changes to in-sync or out-of-sync. File\n        replication state is out-of-sync when VCHA fails to set a watch on a\n        file at the Active node or fails to replicate a file from the Active\n        node to Passive. Administrators should check the corresponding KB\n        article for recovery action.')
vmwVchaInstanceUuid = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 5), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaInstanceUuid.setStatus('current')
if mibBuilder.loadTexts: vmwVchaInstanceUuid.setDescription('A string that uniquely identify the vCenter HA cluster. This is the same\n    as instance UUID of the active vCenter Server.')
vmwVchaPrivateAddressType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 11), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaPrivateAddressType.setStatus('current')
if mibBuilder.loadTexts: vmwVchaPrivateAddressType.setDescription('The type of cluster network interface: ipv4 or ipv6.')
vmwVchaPublicAddressType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 12), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaPublicAddressType.setStatus('current')
if mibBuilder.loadTexts: vmwVchaPublicAddressType.setDescription('The type of public network interface: ipv4 or ipv6.')
vmwVchaPrivateAddressAddr = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 15), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaPrivateAddressAddr.setStatus('current')
if mibBuilder.loadTexts: vmwVchaPrivateAddressAddr.setDescription('This is the IP address of each node in cluster network that is used to\n    communicate with other nodes in the cluster and transfer data between\n    the Active node and the Passive node.')
vmwVchaPublicAddressAddr = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 16), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaPublicAddressAddr.setStatus('current')
if mibBuilder.loadTexts: vmwVchaPublicAddressAddr.setDescription("The IP address of a node in public network that serves client's request.")
vmwVchaTargetNodeRole = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 20), VmwVchaNodeRoleType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaTargetNodeRole.setStatus('current')
if mibBuilder.loadTexts: vmwVchaTargetNodeRole.setDescription('Represents the role of node being affected by the given event. See MIB\n    module general description for detailed expalanation for each role.')
vmwVchaClusterState = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 25), VmwVchaClusterStateType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaClusterState.setStatus('current')
if mibBuilder.loadTexts: vmwVchaClusterState.setDescription('vCenter HA cluster states: healthy, degraded or isolated.')
vmwVchaClusterMode = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 30), VmwVchaClusterModeType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaClusterMode.setStatus('current')
if mibBuilder.loadTexts: vmwVchaClusterMode.setDescription('vCenter HA cluster modes: enabled, maintenance or disabled.')
vmwVchaIsPlannedFailover = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 40), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaIsPlannedFailover.setStatus('current')
if mibBuilder.loadTexts: vmwVchaIsPlannedFailover.setDescription('For planned failover, the Active node flushes all the state to the Passive\n     node, waits for the flush to complete before causing a failover.\n     After the failover, the Passive node starts without any data loss.\n     For unplanned failover, the failover is initiated immediately and may\n     result in data loss.')
vmwVchaDbReplicationState = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 50), VmwVchaDbReplicationStateType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaDbReplicationState.setStatus('current')
if mibBuilder.loadTexts: vmwVchaDbReplicationState.setDescription('Database replication states: sync, async or no replication.')
vmwVchaIsFileProviderInSync = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 55), TruthValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaIsFileProviderInSync.setStatus('current')
if mibBuilder.loadTexts: vmwVchaIsFileProviderInSync.setDescription('This variable represents the file replication provider state. When it is\n    false, the service configuration and state files are out of sync between\n    the Passive and Active nodes. This could result from file replication\n    failures.')
vmwVchaFileReplicationProvider = MibScalar((1, 3, 6, 1, 4, 1, 6876, 53, 60), VmwVchaFileReplicationProviderType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVchaFileReplicationProvider.setStatus('current')
if mibBuilder.loadTexts: vmwVchaFileReplicationProvider.setDescription('File replication providers: service-config or service-state.')
vmwVchaMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2))
vmwVchaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 1))
vmwVchaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 2))
vmwVchaMIBBasicComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 1, 3)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaNotificationInfoGroup"), ("VMWARE-VCHA-MIB", "vmwVchaNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVchaMIBBasicComplianceRev2 = vmwVchaMIBBasicComplianceRev2.setStatus('current')
if mibBuilder.loadTexts: vmwVchaMIBBasicComplianceRev2.setDescription('The compliance statement for entities which implement VMWARE-VCHA-MIB.')
vmwVchaNotificationInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 2, 1)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaInstanceUuid"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressAddr"), ("VMWARE-VCHA-MIB", "vmwVchaPrivateAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressAddr"), ("VMWARE-VCHA-MIB", "vmwVchaPublicAddressType"), ("VMWARE-VCHA-MIB", "vmwVchaTargetNodeRole"), ("VMWARE-VCHA-MIB", "vmwVchaClusterState"), ("VMWARE-VCHA-MIB", "vmwVchaClusterMode"), ("VMWARE-VCHA-MIB", "vmwVchaIsPlannedFailover"), ("VMWARE-VCHA-MIB", "vmwVchaDbReplicationState"), ("VMWARE-VCHA-MIB", "vmwVchaIsFileProviderInSync"), ("VMWARE-VCHA-MIB", "vmwVchaFileReplicationProvider"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVchaNotificationInfoGroup = vmwVchaNotificationInfoGroup.setStatus('current')
if mibBuilder.loadTexts: vmwVchaNotificationInfoGroup.setDescription('These objects provide notification details.')
vmwVchaNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 53, 1, 2, 2, 2)).setObjects(("VMWARE-VCHA-MIB", "vmwVchaNodeJoined"), ("VMWARE-VCHA-MIB", "vmwVchaNodeLeft"), ("VMWARE-VCHA-MIB", "vmwVchaNodeIsolated"), ("VMWARE-VCHA-MIB", "vmwVchaClusterStateChanged"), ("VMWARE-VCHA-MIB", "vmwVchaClusterModeChanged"), ("VMWARE-VCHA-MIB", "vmwVchaPublicIpUp"), ("VMWARE-VCHA-MIB", "vmwVchaPublicIpDown"), ("VMWARE-VCHA-MIB", "vmwVchaFailoverTriggered"), ("VMWARE-VCHA-MIB", "vmwVchaFailoverSucceeded"), ("VMWARE-VCHA-MIB", "vmwVchaFailoverFailedDisabledMode"), ("VMWARE-VCHA-MIB", "vmwVchaFailoverFailedNodeLost"), ("VMWARE-VCHA-MIB", "vmwVchaFailoverFailedPassiveNotReady"), ("VMWARE-VCHA-MIB", "vmwVchaContinueAsActive"), ("VMWARE-VCHA-MIB", "vmwVchaDbReplicationStateChanged"), ("VMWARE-VCHA-MIB", "vmwVchaFileReplicationStateChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVchaNotificationGroup = vmwVchaNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: vmwVchaNotificationGroup.setDescription('Group of objects describing notifications (traps).')
mibBuilder.exportSymbols("VMWARE-VCHA-MIB", vmwVchaNotificationInfoGroup=vmwVchaNotificationInfoGroup, VmwVchaNodeRoleType=VmwVchaNodeRoleType, vmwVchaClusterState=vmwVchaClusterState, vmwVchaDbReplicationState=vmwVchaDbReplicationState, vmwVchaNotificationGroup=vmwVchaNotificationGroup, PYSNMP_MODULE_ID=vmwVchaMIB, vmwVchaMIBBasicComplianceRev2=vmwVchaMIBBasicComplianceRev2, vmwVchaInstanceUuid=vmwVchaInstanceUuid, vmwVCHANotifications=vmwVCHANotifications, vmwVchaNodeIsolated=vmwVchaNodeIsolated, vmwVchaMIB=vmwVchaMIB, vmwVchaClusterModeChanged=vmwVchaClusterModeChanged, vmwVchaTargetNodeRole=vmwVchaTargetNodeRole, vmwVchaClusterMode=vmwVchaClusterMode, vmwVchaFailoverTriggered=vmwVchaFailoverTriggered, vmwVchaContinueAsActive=vmwVchaContinueAsActive, vmwVchaPassive=vmwVchaPassive, vmwVchaActive=vmwVchaActive, VmwVchaFileReplicationProviderType=VmwVchaFileReplicationProviderType, vmwVchaNodeJoined=vmwVchaNodeJoined, vmwVchaMIBGroups=vmwVchaMIBGroups, vmwVchaClusterStateChanged=vmwVchaClusterStateChanged, vmwVchaMIBCompliances=vmwVchaMIBCompliances, VmwVchaDbReplicationStateType=VmwVchaDbReplicationStateType, vmwVchaFailoverFailedDisabledMode=vmwVchaFailoverFailedDisabledMode, vmwVchaPublicIpDown=vmwVchaPublicIpDown, vmwVchaFailoverSucceeded=vmwVchaFailoverSucceeded, vmwVchaFileReplicationStateChanged=vmwVchaFileReplicationStateChanged, vmwVchaIsFileProviderInSync=vmwVchaIsFileProviderInSync, vmwVchaFileReplicationProvider=vmwVchaFileReplicationProvider, vmwVchaMIBConformance=vmwVchaMIBConformance, vmwVchaNodeLeft=vmwVchaNodeLeft, vmwVchaIsPlannedFailover=vmwVchaIsPlannedFailover, vmwVchaWitness=vmwVchaWitness, VmwVchaClusterModeType=VmwVchaClusterModeType, vmwVchaPrivateAddressType=vmwVchaPrivateAddressType, vmwVchaPrivateAddressAddr=vmwVchaPrivateAddressAddr, vmwVchaFailoverFailedPassiveNotReady=vmwVchaFailoverFailedPassiveNotReady, vmwVchaDbReplicationStateChanged=vmwVchaDbReplicationStateChanged, vmwVchaPublicAddressType=vmwVchaPublicAddressType, VmwVchaClusterStateType=VmwVchaClusterStateType, vmwVchaPublicIpUp=vmwVchaPublicIpUp, vmwVchaPublicAddressAddr=vmwVchaPublicAddressAddr, vmwVchaFailoverFailedNodeLost=vmwVchaFailoverFailedNodeLost)
