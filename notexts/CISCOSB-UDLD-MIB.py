#
# PySNMP MIB module CISCOSB-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-UDLD-MIB
# Source digest sha256:ba253dfb453a6e056ef77661342f4be26f7c4c3b8747353ef41aadba81a13277
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rndNotifications, switch001 = mibBuilder.importSymbols("CISCOSB-MIB", "rndNotifications", "switch001")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, MacAddress, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")
class UdldString(SnmpAdminString):
    status = 'current'

class UdldPortBidirectionalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("shutdown", 1), ("idle", 2), ("detection", 3), ("undetermined", 4), ("bidirectional", 5))

class UdldNeighborCurrentState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("undefined", 3), ("bidirectional", 4))

class UdldGlobalMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("aggressive", 2), ("disabled", 3))

class UdldPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("normal", 1), ("aggressive", 2), ("disabled", 3), ("default", 4))

rlUdld = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218))
rlUdld.setRevisions(('2012-08-01 00:00',))
if mibBuilder.loadTexts: rlUdld.setLastUpdated('2012-08-01 00:00')
if mibBuilder.loadTexts: rlUdld.setOrganization('Cisco Systems, Inc.')
rlUdldPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlUdldPortTable.setStatus('current')
rlUdldPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-UDLD-MIB", "rlUdldPortIfIndex"))
if mibBuilder.loadTexts: rlUdldPortEntry.setStatus('current')
rlUdldPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlUdldPortIfIndex.setStatus('current')
rlUdldPortAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 2), UdldPortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldPortAdminMode.setStatus('current')
rlUdldPortOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 3), UdldPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldPortOperMode.setStatus('current')
rlUdldPortDefaultConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldPortDefaultConfiguration.setStatus('current')
rlUdldBidirectionalState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 5), UdldPortBidirectionalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldBidirectionalState.setStatus('current')
rlUdldNumberOfDetectedNeighbors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNumberOfDetectedNeighbors.setStatus('current')
rlUdldNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlUdldNeighborTable.setStatus('current')
rlUdldNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-UDLD-MIB", "rlUdldNeighborPortIfIndex"), (0, "CISCOSB-UDLD-MIB", "rlUdldNeighborDeviceID"), (0, "CISCOSB-UDLD-MIB", "rlUdldNeighborPortID"))
if mibBuilder.loadTexts: rlUdldNeighborEntry.setStatus('current')
rlUdldNeighborPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlUdldNeighborPortIfIndex.setStatus('current')
rlUdldNeighborDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 2), UdldString()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlUdldNeighborDeviceID.setStatus('current')
rlUdldNeighborPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 3), UdldString()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlUdldNeighborPortID.setStatus('current')
rlUdldNeighborDeviceMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 4), MacAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlUdldNeighborDeviceMACAddress.setStatus('current')
rlUdldNeighborDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 5), UdldString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborDeviceName.setStatus('current')
rlUdldNeighborMessageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborMessageTime.setStatus('current')
rlUdldNeighborLeftLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborLeftLifeTime.setStatus('current')
rlUdldNeighborCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 8), UdldNeighborCurrentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborCurrentState.setStatus('current')
rlUdldGlobalUDLDMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 3), UdldGlobalMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldGlobalUDLDMode.setStatus('current')
rlUdldGlobalMessageTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldGlobalMessageTime.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-UDLD-MIB", PYSNMP_MODULE_ID=rlUdld, UdldGlobalMode=UdldGlobalMode, UdldNeighborCurrentState=UdldNeighborCurrentState, UdldPortBidirectionalState=UdldPortBidirectionalState, UdldPortMode=UdldPortMode, UdldString=UdldString, rlUdld=rlUdld, rlUdldBidirectionalState=rlUdldBidirectionalState, rlUdldGlobalMessageTime=rlUdldGlobalMessageTime, rlUdldGlobalUDLDMode=rlUdldGlobalUDLDMode, rlUdldNeighborCurrentState=rlUdldNeighborCurrentState, rlUdldNeighborDeviceID=rlUdldNeighborDeviceID, rlUdldNeighborDeviceMACAddress=rlUdldNeighborDeviceMACAddress, rlUdldNeighborDeviceName=rlUdldNeighborDeviceName, rlUdldNeighborEntry=rlUdldNeighborEntry, rlUdldNeighborLeftLifeTime=rlUdldNeighborLeftLifeTime, rlUdldNeighborMessageTime=rlUdldNeighborMessageTime, rlUdldNeighborPortID=rlUdldNeighborPortID, rlUdldNeighborPortIfIndex=rlUdldNeighborPortIfIndex, rlUdldNeighborTable=rlUdldNeighborTable, rlUdldNumberOfDetectedNeighbors=rlUdldNumberOfDetectedNeighbors, rlUdldPortAdminMode=rlUdldPortAdminMode, rlUdldPortDefaultConfiguration=rlUdldPortDefaultConfiguration, rlUdldPortEntry=rlUdldPortEntry, rlUdldPortIfIndex=rlUdldPortIfIndex, rlUdldPortOperMode=rlUdldPortOperMode, rlUdldPortTable=rlUdldPortTable)
