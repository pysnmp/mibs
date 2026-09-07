#
# PySNMP MIB module ARUBAWIRED-LOOPPROTECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ARUBAWIRED-LOOPPROTECT-MIB
# Source digest sha256:fb1f98872b860af9c5ec5379e6154d0460b46a88e09309da33a99620d47c6307
# Produced by pysmi-2.3.0
#
wndFeatures, = mibBuilder.importSymbols("ARUBAWIRED-NETWORKING-OID", "wndFeatures")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
VlanId, VlanIndex, dot1qVlanStaticEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "VlanIndex", "dot1qVlanStaticEntry")
portCopyEntry, = mibBuilder.importSymbols("SMON-MIB", "portCopyEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp", "TruthValue")
arubaWiredLoopProtectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1))
arubaWiredLoopProtectMIB.setRevisions(('2017-11-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arubaWiredLoopProtectMIB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: arubaWiredLoopProtectMIB.setLastUpdated('2017-11-02 00:00')
if mibBuilder.loadTexts: arubaWiredLoopProtectMIB.setOrganization('HPE/Aruba Networking Division')
if mibBuilder.loadTexts: arubaWiredLoopProtectMIB.setContactInfo('Hewlett-Packard Company\r\n                      8000 Foothills Blvd.\r\n                      Roseville, CA 95747')
if mibBuilder.loadTexts: arubaWiredLoopProtectMIB.setDescription('This MIB module contains HP proprietary\r\n                      extensions to the standard Loop Protect MIBs.')
class ConfigStatus(TextualConvention, Integer32):
    description = "Used to indicate the configuration status for\r\n                    a group of objects.  'active' means that the\r\n                    values of the related objects are currently in\r\n                    use by the device.  'notInService' indicates that\r\n                    the objects have been reconfigured in such a way\r\n                    that the values cannot take effect until after the\r\n                    next reboot of the device.  'notReady' indicates\r\n                    that the objects are not consistent with each other."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3))

class VidList(TextualConvention, OctetString):
    description = 'Each octet within this value specifies a set of eight\r\n                    VlanIIndex (VID), with the first octet specifying VIDs 1\r\n                    through 8, the second octet specifying VIDs 9 through 16,\r\n                    etc.  Within each octet, the most significant bit represents\r\n                    the lowest numbered VID, and the least significant bit\r\n                    represents the highest numbered VID.  Thus, each VID\r\n                    is represented by a single bit within the value of this\r\n                    object.  If that bit has a value of 1 then that VID is\r\n                    included in the set of VIDs; the VID is not included if its\r\n                    bit has a value of 0.  This list represents the entire\r\n                    range of VlanIndex values defined in the scope of IEEE\r\n                    802.1Q.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(512, 512)
    fixedLength = 512

arubaWiredLoopProtectObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1))
class LoopProtectReceiverAction(TextualConvention, Integer32):
    description = ' This TC describes the actions a port that receives a Loop\r\n              Protection Protocol packet can take.\r\n\r\n              The disableTx(1) enumeration indicates that the sender of\r\n              the Loop Protect packet will be disabled.\r\n\r\n              The noDisable(2) enumeration indicates that no port is to\r\n              be disabled.\r\n\r\n              The disableTxRx(3) enumeration indicates that the senders\r\n              and receivers of the Loop Protect packets will be disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disableTx", 1), ("noDisable", 2), ("disableTxRx", 3))

arubaWiredLoopProtect = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5))
arubaWiredLoopProtectNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0))
arubaWiredLoopProtectBase = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1))
arubaWiredLoopProtectPort = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2))
arubaWiredLoopProtectInterval = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectInterval.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectInterval.setDescription('The interval in seconds at which Loop Protection packets are\r\n                     transmitted. The default value is 5 seconds.')
arubaWiredLoopProtectTrapLoopDetectEnable = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectTrapLoopDetectEnable.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectTrapLoopDetectEnable.setDescription('Indicates whether notifications should be sent when a loop\r\n                     is detected on a port.  By default this object will\r\n                     have a value of false(2).')
arubaWiredLoopProtectEnableTimer = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectEnableTimer.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectEnableTimer.setDescription('The time in seconds to wait before re-enabling a port\r\n                     disabled by Loop Protection. When a port is disabled by\r\n                     Loop Protection, a re-enable timer for the port is initialized.\r\n                     If the re-enable timer value is specified as zero seconds the port remains\r\n                     disabled, else the port is re-enabled after the specified time.')
arubaWiredLoopProtectMode = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("port", 1), ("vlan", 2))).clone('port')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectMode.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectMode.setDescription('This object is used to configure the operational mode of Loop Protection\r\n                     feature. The Loop Protection feature can be configured to operate in port mode\r\n                     or VLAN mode.')
arubaWiredLoopProtectVIDList = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 5), VidList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectVIDList.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectVIDList.setDescription('A list of VLANs on which Loop Protection is enabled.')
arubaWiredLoopProtectPortInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectPortInterfaceIndex.setDescription("The index value that uniquely identifies the interface to\r\n                    which this entry is applicable.  The interface identified by\r\n                    a particular value of this index is the same interface as\r\n                    identified by the same value of the IF-MIB's ifIndex.")
arubaWiredLoopProtectPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortEnable.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectPortEnable.setDescription('This object indicates whether the Loop Protection is enabled\r\n                     on a port. The default value is FALSE')
arubaWiredLoopProtectPortLoopDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLoopDetected.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLoopDetected.setDescription("This object will be set to TRUE when a loop is detected on\r\n                     the port. The value of this object will be reset to FALSE when\r\n                     the port's arubaWiredLoopProtectPortEnable is set to\r\n                     FALSE.")
arubaWiredLoopProtectPortLastLoopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLastLoopTime.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLastLoopTime.setDescription('The value of sysUpTime when a loop was last detected\r\n                     on this port. A value of 0 means that the timestamp has\r\n                     not been set.')
arubaWiredLoopProtectPortLoopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLoopCount.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLoopCount.setDescription('This object provides the number of loops detected on a Loop Protection enabled\r\n                     port. The value of this object is set to zero when Loop Protection is disabled on\r\n                     a port.')
arubaWiredLoopProtectPortReceiverAction = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 6), LoopProtectReceiverAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortReceiverAction.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectPortReceiverAction.setDescription("Controls the action taken when a Loop Protection packet is\r\n                     received on this port.\r\n                     When set to 'disableTx' the port that transmitted the packet is disabled.\r\n\r\n                     When set to 'noDisable' the transmitting port is not disabled.\r\n\r\n                     When set to 'disableTxRx' the ports transmitting and receiving the packets are disabled.")
arubaWiredLoopProtectLoopDetectedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectLoopDetectedVlan.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectLoopDetectedVlan.setDescription('Refers to this object for the port on which loop is\r\n                     detected.')
arubaWiredLoopProtectPortVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 8), VidList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortVlanList.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectPortVlanList.setDescription('A list of VLANs for this interface in which Loop Protection is enabled.')
arubaWiredLoopProtectPortTable = MibTable((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortTable.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectPortTable.setDescription('Per-interface configuration for Loop Protection.')
arubaWiredLoopProtectPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortInterfaceIndex"))
if mibBuilder.loadTexts: arubaWiredLoopProtectPortEntry.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectPortEntry.setDescription('Loop Protection configuration information for\r\n                     a single port.')
arubaWiredLoopProtectLoopDetectedNotification = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"))
if mibBuilder.loadTexts: arubaWiredLoopProtectLoopDetectedNotification.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectLoopDetectedNotification.setDescription('A arubaWiredLoopProtectLoopDetectedNotification signifies\r\n                     that a loop is detected by the Loop Protection Protocol.\r\n                     Generation of this notification is controlled by\r\n                     arubaWiredLoopProtectTrapLoopDetectEnable.\r\n\r\n                     To prevent excessive notifications, this trap allows only\r\n                     one notifications every 30 seconds.\r\n                     Notifications that are missed due to this limitation are\r\n                     dropped and are not sent later.')
arubaWiredLoopProtectVlanLoopDetectedNotification = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectLoopDetectedVlan"))
if mibBuilder.loadTexts: arubaWiredLoopProtectVlanLoopDetectedNotification.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectVlanLoopDetectedNotification.setDescription('A arubaWiredLoopProtectVlanLoopDetectedNotification signifies\r\n                     that a loop is detected by the Loop Protection feature while\r\n                     operating in VLAN  mode. Generation of this notification is\r\n                     controlled by arubaWiredLoopProtectTrapLoopDetectEnable.\r\n\r\n                     To prevent excessive notifications, this trap allows only\r\n                     one notifications every 30 seconds.\r\n                     Notifications that are missed due to this limitation are\r\n                     dropped and are not sent later.')
arubaWiredLoopProtectConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3))
arubaWiredLoopProtectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1))
arubaWiredLoopProtectCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 2))
arubaWiredLoopProtectBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1, 4)).setObjects(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectInterval"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectEnableTimer"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectTrapLoopDetectEnable"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortEnable"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopDetected"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLastLoopTime"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLoopProtectBaseGroup = arubaWiredLoopProtectBaseGroup.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectBaseGroup.setDescription('A collection of objects providing basic instrumentation\r\n                     and control of the HP Loop protection entity.')
arubaWiredLoopProtectVLANGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1, 10)).setObjects(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectMode"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectVIDList"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectLoopDetectedVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLoopProtectVLANGroup = arubaWiredLoopProtectVLANGroup.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectVLANGroup.setDescription('A collection of objects providing support for Loop Protect\r\n                     per VLAN feature.')
arubaWiredLoopProtectCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 2, 5)).setObjects(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectBaseGroup"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectNotifications"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectBaseGroup"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectNotifications"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLoopProtectCompliance = arubaWiredLoopProtectCompliance.setStatus('current')
if mibBuilder.loadTexts: arubaWiredLoopProtectCompliance.setDescription('The compliance statement for HP Switches with\r\n                     support for arubaWired loop protection objects.')
mibBuilder.exportSymbols("ARUBAWIRED-LOOPPROTECT-MIB", ConfigStatus=ConfigStatus, LoopProtectReceiverAction=LoopProtectReceiverAction, PYSNMP_MODULE_ID=arubaWiredLoopProtectMIB, VidList=VidList, arubaWiredLoopProtect=arubaWiredLoopProtect, arubaWiredLoopProtectBase=arubaWiredLoopProtectBase, arubaWiredLoopProtectBaseGroup=arubaWiredLoopProtectBaseGroup, arubaWiredLoopProtectCompliance=arubaWiredLoopProtectCompliance, arubaWiredLoopProtectCompliances=arubaWiredLoopProtectCompliances, arubaWiredLoopProtectConformance=arubaWiredLoopProtectConformance, arubaWiredLoopProtectEnableTimer=arubaWiredLoopProtectEnableTimer, arubaWiredLoopProtectGroups=arubaWiredLoopProtectGroups, arubaWiredLoopProtectInterval=arubaWiredLoopProtectInterval, arubaWiredLoopProtectLoopDetectedNotification=arubaWiredLoopProtectLoopDetectedNotification, arubaWiredLoopProtectLoopDetectedVlan=arubaWiredLoopProtectLoopDetectedVlan, arubaWiredLoopProtectMIB=arubaWiredLoopProtectMIB, arubaWiredLoopProtectMode=arubaWiredLoopProtectMode, arubaWiredLoopProtectNotifications=arubaWiredLoopProtectNotifications, arubaWiredLoopProtectObjects=arubaWiredLoopProtectObjects, arubaWiredLoopProtectPort=arubaWiredLoopProtectPort, arubaWiredLoopProtectPortEnable=arubaWiredLoopProtectPortEnable, arubaWiredLoopProtectPortEntry=arubaWiredLoopProtectPortEntry, arubaWiredLoopProtectPortInterfaceIndex=arubaWiredLoopProtectPortInterfaceIndex, arubaWiredLoopProtectPortLastLoopTime=arubaWiredLoopProtectPortLastLoopTime, arubaWiredLoopProtectPortLoopCount=arubaWiredLoopProtectPortLoopCount, arubaWiredLoopProtectPortLoopDetected=arubaWiredLoopProtectPortLoopDetected, arubaWiredLoopProtectPortReceiverAction=arubaWiredLoopProtectPortReceiverAction, arubaWiredLoopProtectPortTable=arubaWiredLoopProtectPortTable, arubaWiredLoopProtectPortVlanList=arubaWiredLoopProtectPortVlanList, arubaWiredLoopProtectTrapLoopDetectEnable=arubaWiredLoopProtectTrapLoopDetectEnable, arubaWiredLoopProtectVIDList=arubaWiredLoopProtectVIDList, arubaWiredLoopProtectVLANGroup=arubaWiredLoopProtectVLANGroup, arubaWiredLoopProtectVlanLoopDetectedNotification=arubaWiredLoopProtectVlanLoopDetectedNotification)
