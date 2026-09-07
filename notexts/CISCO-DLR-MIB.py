#
# PySNMP MIB module CISCO-DLR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DLR-MIB
# Source digest sha256:f9f5ee055222ad9c0e54ee9079a9047dd7957cd5a816490b3d649a026d3d987f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDlrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 865))
ciscoDlrMIB.setRevisions(('2019-09-11 00:00',))
if mibBuilder.loadTexts: ciscoDlrMIB.setLastUpdated('2019-09-11 00:00')
if mibBuilder.loadTexts: ciscoDlrMIB.setOrganization('Cisco Systems, Inc.')
class DlrNetworkStatus(TextualConvention, Integer32):
    reference = 'Dlr ring network status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("ringNormal", 1), ("ringFault", 2), ("ringUnexcpectedLoop", 3), ("ringPartialFault", 4), ("ringRapidFaultRestore", 5))

class DlrDeviceState(TextualConvention, Integer32):
    reference = 'Dlr ring device status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("supBackup", 1), ("supActive", 2), ("normalRing", 3), ("nonDlr", 4))

class DlrGatewayDeviceStatus(TextualConvention, Integer32):
    reference = 'Dlr ring gateway device status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 0), ("nonGateway", 1), ("activeGateway", 2), ("backupGateway", 3), ("faultGateway", 4), ("nonSupportedGateway", 5), ("partialFaultGateway", 6))

class DlrGatewayDeviceState(TextualConvention, Integer32):
    reference = 'Dlr ring gateway device state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("gatewayIdle", 1), ("activeListen", 2), ("activeNormal", 3), ("fault", 4), ("backupNormal", 5), ("lossUplink", 6), ("partialNetworkfault", 7))

ciscoDlrMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 865, 0))
ciscoDlrRingStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 865, 0, 1)).setObjects(("CISCO-DLR-MIB", "ciscoDlrRingID"), ("CISCO-DLR-MIB", "ciscoDlrRingName"), ("CISCO-DLR-MIB", "ciscoDlrRingNetworkStatus"))
if mibBuilder.loadTexts: ciscoDlrRingStatus.setStatus('current')
ciscoDlrRingSupervisorStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 865, 0, 2)).setObjects(("CISCO-DLR-MIB", "ciscoDlrRingID"), ("CISCO-DLR-MIB", "ciscoDlrRingName"), ("CISCO-DLR-MIB", "ciscoDlrRingDeviceState"))
if mibBuilder.loadTexts: ciscoDlrRingSupervisorStatus.setStatus('current')
ciscoDlrRingGatewayStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 865, 0, 3)).setObjects(("CISCO-DLR-MIB", "ciscoDlrRingID"), ("CISCO-DLR-MIB", "ciscoDlrRingName"), ("CISCO-DLR-MIB", "ciscoDlrRingGatewayDeviceStatus"))
if mibBuilder.loadTexts: ciscoDlrRingGatewayStatus.setStatus('current')
ciscoDlrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 865, 1))
ciscoDlrMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 865, 2))
ciscoDlrRingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoDlrRingTable.setStatus('current')
ciscoDlrRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-DLR-MIB", "ciscoDlrRingIndex"))
if mibBuilder.loadTexts: ciscoDlrRingEntry.setStatus('current')
ciscoDlrRingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 1), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoDlrRingIndex.setStatus('current')
ciscoDlrRingID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingID.setStatus('current')
ciscoDlrRingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingName.setStatus('current')
ciscoDlrRingNetworkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 4), DlrNetworkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingNetworkStatus.setStatus('current')
ciscoDlrRingDeviceState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 5), DlrDeviceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingDeviceState.setStatus('current')
ciscoDlrRingGatewayDeviceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 6), DlrGatewayDeviceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingGatewayDeviceStatus.setStatus('current')
ciscoDlrRingGatewayDeviceState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 7), DlrGatewayDeviceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingGatewayDeviceState.setStatus('current')
ciscoDlrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 1))
ciscoDlrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 2))
ciscoDlrMIBModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 1, 1)).setObjects(("CISCO-DLR-MIB", "ciscoDlrMIBMainObjectGroup"), ("CISCO-DLR-MIB", "ciscoDlrMIBNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDlrMIBModuleCompliance = ciscoDlrMIBModuleCompliance.setStatus('current')
ciscoDlrMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 2, 1)).setObjects(("CISCO-DLR-MIB", "ciscoDlrRingID"), ("CISCO-DLR-MIB", "ciscoDlrRingNetworkStatus"), ("CISCO-DLR-MIB", "ciscoDlrRingDeviceState"), ("CISCO-DLR-MIB", "ciscoDlrRingGatewayDeviceStatus"), ("CISCO-DLR-MIB", "ciscoDlrRingGatewayDeviceState"), ("CISCO-DLR-MIB", "ciscoDlrRingName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDlrMIBMainObjectGroup = ciscoDlrMIBMainObjectGroup.setStatus('current')
ciscoDlrMIBNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 2, 2)).setObjects(("CISCO-DLR-MIB", "ciscoDlrRingStatus"), ("CISCO-DLR-MIB", "ciscoDlrRingSupervisorStatus"), ("CISCO-DLR-MIB", "ciscoDlrRingGatewayStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDlrMIBNotifyGroup = ciscoDlrMIBNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DLR-MIB", DlrDeviceState=DlrDeviceState, DlrGatewayDeviceState=DlrGatewayDeviceState, DlrGatewayDeviceStatus=DlrGatewayDeviceStatus, DlrNetworkStatus=DlrNetworkStatus, PYSNMP_MODULE_ID=ciscoDlrMIB, ciscoDlrMIB=ciscoDlrMIB, ciscoDlrMIBCompliances=ciscoDlrMIBCompliances, ciscoDlrMIBConform=ciscoDlrMIBConform, ciscoDlrMIBGroups=ciscoDlrMIBGroups, ciscoDlrMIBMainObjectGroup=ciscoDlrMIBMainObjectGroup, ciscoDlrMIBModuleCompliance=ciscoDlrMIBModuleCompliance, ciscoDlrMIBNotifs=ciscoDlrMIBNotifs, ciscoDlrMIBNotifyGroup=ciscoDlrMIBNotifyGroup, ciscoDlrMIBObjects=ciscoDlrMIBObjects, ciscoDlrRingDeviceState=ciscoDlrRingDeviceState, ciscoDlrRingEntry=ciscoDlrRingEntry, ciscoDlrRingGatewayDeviceState=ciscoDlrRingGatewayDeviceState, ciscoDlrRingGatewayDeviceStatus=ciscoDlrRingGatewayDeviceStatus, ciscoDlrRingGatewayStatus=ciscoDlrRingGatewayStatus, ciscoDlrRingID=ciscoDlrRingID, ciscoDlrRingIndex=ciscoDlrRingIndex, ciscoDlrRingName=ciscoDlrRingName, ciscoDlrRingNetworkStatus=ciscoDlrRingNetworkStatus, ciscoDlrRingStatus=ciscoDlrRingStatus, ciscoDlrRingSupervisorStatus=ciscoDlrRingSupervisorStatus, ciscoDlrRingTable=ciscoDlrRingTable)
