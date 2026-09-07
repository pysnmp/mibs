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
if mibBuilder.loadTexts: arubaWiredLoopProtectMIB.setLastUpdated('2017-11-02 00:00')
if mibBuilder.loadTexts: arubaWiredLoopProtectMIB.setOrganization('HPE/Aruba Networking Division')
class ConfigStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3))

class VidList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(512, 512)
    fixedLength = 512

arubaWiredLoopProtectObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1))
class LoopProtectReceiverAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disableTx", 1), ("noDisable", 2), ("disableTxRx", 3))

arubaWiredLoopProtect = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5))
arubaWiredLoopProtectNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0))
arubaWiredLoopProtectBase = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1))
arubaWiredLoopProtectPort = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2))
arubaWiredLoopProtectInterval = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectInterval.setStatus('current')
arubaWiredLoopProtectTrapLoopDetectEnable = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectTrapLoopDetectEnable.setStatus('current')
arubaWiredLoopProtectEnableTimer = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectEnableTimer.setStatus('current')
arubaWiredLoopProtectMode = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("port", 1), ("vlan", 2))).clone('port')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectMode.setStatus('current')
arubaWiredLoopProtectVIDList = MibScalar((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 1, 5), VidList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectVIDList.setStatus('current')
arubaWiredLoopProtectPortInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortInterfaceIndex.setStatus('current')
arubaWiredLoopProtectPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortEnable.setStatus('current')
arubaWiredLoopProtectPortLoopDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLoopDetected.setStatus('current')
arubaWiredLoopProtectPortLastLoopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLastLoopTime.setStatus('current')
arubaWiredLoopProtectPortLoopCount = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortLoopCount.setStatus('current')
arubaWiredLoopProtectPortReceiverAction = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 6), LoopProtectReceiverAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortReceiverAction.setStatus('current')
arubaWiredLoopProtectLoopDetectedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaWiredLoopProtectLoopDetectedVlan.setStatus('current')
arubaWiredLoopProtectPortVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1, 8), VidList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortVlanList.setStatus('current')
arubaWiredLoopProtectPortTable = MibTable((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: arubaWiredLoopProtectPortTable.setStatus('current')
arubaWiredLoopProtectPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortInterfaceIndex"))
if mibBuilder.loadTexts: arubaWiredLoopProtectPortEntry.setStatus('current')
arubaWiredLoopProtectLoopDetectedNotification = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"))
if mibBuilder.loadTexts: arubaWiredLoopProtectLoopDetectedNotification.setStatus('current')
arubaWiredLoopProtectVlanLoopDetectedNotification = NotificationType((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectLoopDetectedVlan"))
if mibBuilder.loadTexts: arubaWiredLoopProtectVlanLoopDetectedNotification.setStatus('current')
arubaWiredLoopProtectConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3))
arubaWiredLoopProtectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1))
arubaWiredLoopProtectCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 2))
arubaWiredLoopProtectBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1, 4)).setObjects(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectInterval"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectEnableTimer"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectTrapLoopDetectEnable"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortEnable"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopDetected"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLastLoopTime"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortLoopCount"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectPortReceiverAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLoopProtectBaseGroup = arubaWiredLoopProtectBaseGroup.setStatus('current')
arubaWiredLoopProtectVLANGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 1, 10)).setObjects(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectMode"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectVIDList"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectLoopDetectedVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLoopProtectVLANGroup = arubaWiredLoopProtectVLANGroup.setStatus('current')
arubaWiredLoopProtectCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1, 1, 5, 3, 2, 5)).setObjects(("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectBaseGroup"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectNotifications"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectBaseGroup"), ("ARUBAWIRED-LOOPPROTECT-MIB", "arubaWiredLoopProtectNotifications"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arubaWiredLoopProtectCompliance = arubaWiredLoopProtectCompliance.setStatus('current')
mibBuilder.exportSymbols("ARUBAWIRED-LOOPPROTECT-MIB", ConfigStatus=ConfigStatus, LoopProtectReceiverAction=LoopProtectReceiverAction, PYSNMP_MODULE_ID=arubaWiredLoopProtectMIB, VidList=VidList, arubaWiredLoopProtect=arubaWiredLoopProtect, arubaWiredLoopProtectBase=arubaWiredLoopProtectBase, arubaWiredLoopProtectBaseGroup=arubaWiredLoopProtectBaseGroup, arubaWiredLoopProtectCompliance=arubaWiredLoopProtectCompliance, arubaWiredLoopProtectCompliances=arubaWiredLoopProtectCompliances, arubaWiredLoopProtectConformance=arubaWiredLoopProtectConformance, arubaWiredLoopProtectEnableTimer=arubaWiredLoopProtectEnableTimer, arubaWiredLoopProtectGroups=arubaWiredLoopProtectGroups, arubaWiredLoopProtectInterval=arubaWiredLoopProtectInterval, arubaWiredLoopProtectLoopDetectedNotification=arubaWiredLoopProtectLoopDetectedNotification, arubaWiredLoopProtectLoopDetectedVlan=arubaWiredLoopProtectLoopDetectedVlan, arubaWiredLoopProtectMIB=arubaWiredLoopProtectMIB, arubaWiredLoopProtectMode=arubaWiredLoopProtectMode, arubaWiredLoopProtectNotifications=arubaWiredLoopProtectNotifications, arubaWiredLoopProtectObjects=arubaWiredLoopProtectObjects, arubaWiredLoopProtectPort=arubaWiredLoopProtectPort, arubaWiredLoopProtectPortEnable=arubaWiredLoopProtectPortEnable, arubaWiredLoopProtectPortEntry=arubaWiredLoopProtectPortEntry, arubaWiredLoopProtectPortInterfaceIndex=arubaWiredLoopProtectPortInterfaceIndex, arubaWiredLoopProtectPortLastLoopTime=arubaWiredLoopProtectPortLastLoopTime, arubaWiredLoopProtectPortLoopCount=arubaWiredLoopProtectPortLoopCount, arubaWiredLoopProtectPortLoopDetected=arubaWiredLoopProtectPortLoopDetected, arubaWiredLoopProtectPortReceiverAction=arubaWiredLoopProtectPortReceiverAction, arubaWiredLoopProtectPortTable=arubaWiredLoopProtectPortTable, arubaWiredLoopProtectPortVlanList=arubaWiredLoopProtectPortVlanList, arubaWiredLoopProtectTrapLoopDetectEnable=arubaWiredLoopProtectTrapLoopDetectEnable, arubaWiredLoopProtectVIDList=arubaWiredLoopProtectVIDList, arubaWiredLoopProtectVLANGroup=arubaWiredLoopProtectVLANGroup, arubaWiredLoopProtectVlanLoopDetectedNotification=arubaWiredLoopProtectVlanLoopDetectedNotification)
