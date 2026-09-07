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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDlrMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDlrMIB.setLastUpdated('2019-09-11 00:00')
if mibBuilder.loadTexts: ciscoDlrMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDlrMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-<list>@cisco.com')
if mibBuilder.loadTexts: ciscoDlrMIB.setDescription('The CISCO-DLR-MIB is used to monitor the Device Level Ring\n        (DLR) and notifying their state change. \n        The Device Level Ring Protocol (DLR) is a redundancy protocol\n        for EtherNet/IP and operates on OSI Layer 2. It can detect bus\n        faults in a single line topology compensated by activating      \n        a redundant communication path. Thus DLR allows to build fast\n        recovering and redundant network topologies that do not\n        influence the controlling applications')
class DlrNetworkStatus(TextualConvention, Integer32):
    reference = 'Dlr ring network status'
    description = 'Operational status of the DLR ring.\n        undefined(0)  Value is not valid.\n        ringNormal(1) DLR ring is in normal state.\n        ringFault(2)  DLR ring is in fault state.\n        ringUnexcpectedLoop(3) DLR ring is in unexpected loop.\n        ringPartialFault(4) DLR ring is in partial fault state.\n        ringRapidFaultRestore(5) DLR ring is in rapid fault restore\n        cycle state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("ringNormal", 1), ("ringFault", 2), ("ringUnexcpectedLoop", 3), ("ringPartialFault", 4), ("ringRapidFaultRestore", 5))

class DlrDeviceState(TextualConvention, Integer32):
    reference = 'Dlr ring device status'
    description = 'Operational status of the DLR Device.\n        undefined(0)  Value is not valid. \n        supBackup(1)  DLR device is in Supervisor backup state. \n        supActive(2)  DLR device is in Supervisor active state.\n        normalRing(3) DLR device is a normal ring device.\n        nonDlr(4) Device is a non DLR device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("supBackup", 1), ("supActive", 2), ("normalRing", 3), ("nonDlr", 4))

class DlrGatewayDeviceStatus(TextualConvention, Integer32):
    reference = 'Dlr ring gateway device status'
    description = 'Operational status of the DLR ring.\n        undefined(0)  Value is not valid. \n        nonGateway(1) Not a Gateway device.\n        activeGateway(2)  Device is a active gateway.\n        backupGateway(3)  Device is a backup gateway.\n        faultGateway(4)   Device is an fault gateway state.\n        nonSupportedGateway(5) Device donot support gateway.\n        partialFaultGateway(6) Device is a partial fault gateway.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 0), ("nonGateway", 1), ("activeGateway", 2), ("backupGateway", 3), ("faultGateway", 4), ("nonSupportedGateway", 5), ("partialFaultGateway", 6))

class DlrGatewayDeviceState(TextualConvention, Integer32):
    reference = 'Dlr ring gateway device state'
    description = 'Operational status of the DLR Device.\n        undefined(0)  Value is not valid.\n        gatewayIdle(1)  DLR gateway device is in idle state.\n        activeListen(2) DLR gateway device is in active listen state.\n        activeNormal(3) DLR gateway device is in active normal state.\n        fault(4) DLR gateway device is in fault state.\n        backupNormal(5) DLR gateway device is in backup normal state.\n        lossUplink(6) DLR gateway device is lost up link.\n        partialNetworkfault(7) DLR gateway device partial network fault\n        state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("gatewayIdle", 1), ("activeListen", 2), ("activeNormal", 3), ("fault", 4), ("backupNormal", 5), ("lossUplink", 6), ("partialNetworkfault", 7))

ciscoDlrMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 865, 0))
ciscoDlrRingStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 865, 0, 1)).setObjects(("CISCO-DLR-MIB", "ciscoDlrRingID"), ("CISCO-DLR-MIB", "ciscoDlrRingName"), ("CISCO-DLR-MIB", "ciscoDlrRingNetworkStatus"))
if mibBuilder.loadTexts: ciscoDlrRingStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingStatus.setDescription('A ciscoDlrRingSatus notification is generated when the value of\n        ciscoDlrRingNetworkStatus is changed to Normal or Fault.\n        The notification contains information of ciscoDlrRingID,\n        ciscoDlrRingName, ciscoDlrNetworkStatus.')
ciscoDlrRingSupervisorStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 865, 0, 2)).setObjects(("CISCO-DLR-MIB", "ciscoDlrRingID"), ("CISCO-DLR-MIB", "ciscoDlrRingName"), ("CISCO-DLR-MIB", "ciscoDlrRingDeviceState"))
if mibBuilder.loadTexts: ciscoDlrRingSupervisorStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingSupervisorStatus.setDescription('A ciscoDlrRingSupervisorSatus notification is generated when\n        the value of ciscoDlrRingDeviceState is changed to ACTIVE or\n        BACKUP.\n        The notification contains ciscoDlrRingID,\n        ciscoDlrRingName, ciscoDlrDeviceStatus.')
ciscoDlrRingGatewayStatus = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 865, 0, 3)).setObjects(("CISCO-DLR-MIB", "ciscoDlrRingID"), ("CISCO-DLR-MIB", "ciscoDlrRingName"), ("CISCO-DLR-MIB", "ciscoDlrRingGatewayDeviceStatus"))
if mibBuilder.loadTexts: ciscoDlrRingGatewayStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingGatewayStatus.setDescription('A ciscoDlrRingGatewaySatus notification is generated when the\n        value of ciscoDlrRingGatewayDeviceState is changed to ACTIVE or\n        BACKUP.\n        The notification contains ciscoDlrRingID,\n        ciscoDlrRingName, ciscoDlrGatewayDeviceStatus.')
ciscoDlrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 865, 1))
ciscoDlrMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 865, 2))
ciscoDlrRingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoDlrRingTable.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingTable.setDescription('This table contains one row per each Device\n        Level redundancy ring  configured on the device.')
ciscoDlrRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-DLR-MIB", "ciscoDlrRingIndex"))
if mibBuilder.loadTexts: ciscoDlrRingEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingEntry.setDescription('Information about a particular DLR ring entry.Each entry\n        provides objects (ciscoDlrRingId, ciscoDlrDomainName ,\n        ciscoDlrRingNetworkStatus, ciscoDlrRingDeviceState,\n        ciscoDlrRingGatewayDeviceStatus and\n        ciscoDlrRingGatewayDevicetate) to help an  NMS\n        identify and characterize the entry and objects.')
ciscoDlrRingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 1), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoDlrRingIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingIndex.setDescription('The index of the entry')
ciscoDlrRingID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingID.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingID.setDescription('A ring identifier of a DLR ring.')
ciscoDlrRingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingName.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingName.setDescription('A textual description of DLR ring. This object should contain a\n        string which identifies the dlr ring name.')
ciscoDlrRingNetworkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 4), DlrNetworkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingNetworkStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingNetworkStatus.setDescription('Operational status of the DLR network. The different opertions\n        status of are defined as part of DlrNetworkStatus.')
ciscoDlrRingDeviceState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 5), DlrDeviceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingDeviceState.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingDeviceState.setDescription('Operational status of the DLR Device. The different opertional\n        state of the device is defined as part of DlrDeviceState.')
ciscoDlrRingGatewayDeviceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 6), DlrGatewayDeviceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingGatewayDeviceStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingGatewayDeviceStatus.setDescription('Operational status of the DLR Gateway Device. The different\n        operational staus of the gateway device are defined as part of\n        DlrGatewayStatus.')
ciscoDlrRingGatewayDeviceState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 865, 1, 1, 1, 7), DlrGatewayDeviceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoDlrRingGatewayDeviceState.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrRingGatewayDeviceState.setDescription('Operational state of the DLR Gateway Device. The different\n        opertional state are defined as part of DlrGatewayState.')
ciscoDlrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 1))
ciscoDlrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 2))
ciscoDlrMIBModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 1, 1)).setObjects(("CISCO-DLR-MIB", "ciscoDlrMIBMainObjectGroup"), ("CISCO-DLR-MIB", "ciscoDlrMIBNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDlrMIBModuleCompliance = ciscoDlrMIBModuleCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrMIBModuleCompliance.setDescription('This includes all the mandatory groups required for DLR mib')
ciscoDlrMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 2, 1)).setObjects(("CISCO-DLR-MIB", "ciscoDlrRingID"), ("CISCO-DLR-MIB", "ciscoDlrRingNetworkStatus"), ("CISCO-DLR-MIB", "ciscoDlrRingDeviceState"), ("CISCO-DLR-MIB", "ciscoDlrRingGatewayDeviceStatus"), ("CISCO-DLR-MIB", "ciscoDlrRingGatewayDeviceState"), ("CISCO-DLR-MIB", "ciscoDlrRingName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDlrMIBMainObjectGroup = ciscoDlrMIBMainObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrMIBMainObjectGroup.setDescription('A collection of objects required for monitoring of DLR ring.')
ciscoDlrMIBNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 865, 2, 2, 2)).setObjects(("CISCO-DLR-MIB", "ciscoDlrRingStatus"), ("CISCO-DLR-MIB", "ciscoDlrRingSupervisorStatus"), ("CISCO-DLR-MIB", "ciscoDlrRingGatewayStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDlrMIBNotifyGroup = ciscoDlrMIBNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDlrMIBNotifyGroup.setDescription('Collection of notification which indicates diffferent state\n        changes of DLR ring, Supervisor Device, Gateway device.')
mibBuilder.exportSymbols("CISCO-DLR-MIB", DlrDeviceState=DlrDeviceState, DlrGatewayDeviceState=DlrGatewayDeviceState, DlrGatewayDeviceStatus=DlrGatewayDeviceStatus, DlrNetworkStatus=DlrNetworkStatus, PYSNMP_MODULE_ID=ciscoDlrMIB, ciscoDlrMIB=ciscoDlrMIB, ciscoDlrMIBCompliances=ciscoDlrMIBCompliances, ciscoDlrMIBConform=ciscoDlrMIBConform, ciscoDlrMIBGroups=ciscoDlrMIBGroups, ciscoDlrMIBMainObjectGroup=ciscoDlrMIBMainObjectGroup, ciscoDlrMIBModuleCompliance=ciscoDlrMIBModuleCompliance, ciscoDlrMIBNotifs=ciscoDlrMIBNotifs, ciscoDlrMIBNotifyGroup=ciscoDlrMIBNotifyGroup, ciscoDlrMIBObjects=ciscoDlrMIBObjects, ciscoDlrRingDeviceState=ciscoDlrRingDeviceState, ciscoDlrRingEntry=ciscoDlrRingEntry, ciscoDlrRingGatewayDeviceState=ciscoDlrRingGatewayDeviceState, ciscoDlrRingGatewayDeviceStatus=ciscoDlrRingGatewayDeviceStatus, ciscoDlrRingGatewayStatus=ciscoDlrRingGatewayStatus, ciscoDlrRingID=ciscoDlrRingID, ciscoDlrRingIndex=ciscoDlrRingIndex, ciscoDlrRingName=ciscoDlrRingName, ciscoDlrRingNetworkStatus=ciscoDlrRingNetworkStatus, ciscoDlrRingStatus=ciscoDlrRingStatus, ciscoDlrRingSupervisorStatus=ciscoDlrRingSupervisorStatus, ciscoDlrRingTable=ciscoDlrRingTable)
