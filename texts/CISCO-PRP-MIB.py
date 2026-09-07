#
# PySNMP MIB module CISCO-PRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PRP-MIB
# Source digest sha256:b907178174e9d974929aac96dbb46173a69799b83b8de66433da36e3cae95a68
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 866))
ciscoPrpMIB.setRevisions(('2019-09-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPrpMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPrpMIB.setLastUpdated('2019-09-11 00:00')
if mibBuilder.loadTexts: ciscoPrpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPrpMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-<list>@cisco.com')
if mibBuilder.loadTexts: ciscoPrpMIB.setDescription('Parallel Redundancy Protocol (PRP) is defined in the\n        International Standard IEC 62439-3. PRP is designed to provide\n        hitless redundancy (zero recovery time after failures) in\n        Ethernet networks.\n\n        PRP uses a  scheme, where the end nodes implement redundancy\n        (instead of network elements) by connecting two network\n        interfaces to two independent, disjointed, parallel networks\n        (LAN-A and LAN-B). Each of these Dually Attached Nodes (DANs)\n        then have redundant paths to all other DANs in the network.')
class PrpStatus(TextualConvention, Integer32):
    reference = 'Prp channel or LAN status'
    description = 'Operational status of the DLR Device.\n        undefined(0)  Value is not valid.\n        stateUp(1)   PRP channel or LAN state UP.\n        stateDown(2) PRP channel or LAN state DOWN.\n        state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("stateUp", 1), ("stateDown", 2))

ciscoPrpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 0))
ciscoPrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 1))
ciscoPrpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2))
ciscoPrpChannelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoPrpChannelTable.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpChannelTable.setDescription('Every entry in the table specifies information about the PRP\n        channel.')
ciscoPrpChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-PRP-MIB", "ciscoPrpChannelIndex"))
if mibBuilder.loadTexts: ciscoPrpChannelEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpChannelEntry.setDescription('An entry in the prpChannelTable.')
ciscoPrpChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 1), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoPrpChannelIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpChannelIndex.setDescription('Prp table entry index value.')
ciscoPrpChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelId.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpChannelId.setDescription('Specifies the PRP channel id.')
ciscoPrpChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelName.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpChannelName.setDescription('PRP channel name.')
ciscoPrpChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 4), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpChannelStatus.setDescription('Operational status of the PRP channel.')
ciscoPrpChannelLanAStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 5), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelLanAStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpChannelLanAStatus.setDescription('Operational status of the PRP Lan A connection status.')
ciscoPrpChannelLanBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 6), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelLanBStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpChannelLanBStatus.setDescription('A ciscoPrpLanBStateChange notification is generated when the\n        value of \n        ciscoPrpChannelLanBStatus is changed to Up or Down.\n        The notification contains information of ciscoPrpChannelId,\n        ciscoPrpChannelName, ciscoPrpChannelLanBStatus.')
ciscoPrpChannelStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelStatus"))
if mibBuilder.loadTexts: ciscoPrpChannelStateChange.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpChannelStateChange.setDescription('A ciscoPrpChannelStateChange notification is generated when the\n        value of \n        ciscoPrpChannelStatus is changed to Up or Down.\n        The notification contains information of ciscoPrpChannelId,\n        ciscoPrpChannelName, ciscoPrpChannelStatus.')
ciscoPrpLanAStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 2)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanAStatus"))
if mibBuilder.loadTexts: ciscoPrpLanAStateChange.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpLanAStateChange.setDescription('A ciscoPrpLanAStateChange notification is generated when the\n        value of \n        ciscoPrpChannelLanAStatus is changed to Up or Down.\n        The notification contains information of ciscoPrpChannelId,\n        ciscoPrpChannelName, ciscoPrpChannelLanAStatus.')
ciscoPrpLanBStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 3)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanBStatus"))
if mibBuilder.loadTexts: ciscoPrpLanBStateChange.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpLanBStateChange.setDescription('Object to notify change in Lan B status of\n        a PRP channel.')
ciscoPrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 1))
ciscoPrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2))
ciscoPrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 1, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpMIBMainObjectGroup"), ("CISCO-PRP-MIB", "ciscoPrpMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBCompliance = ciscoPrpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpMIBCompliance.setDescription('This is a default module-compliance\n        containing default object groups.')
ciscoPrpMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanAStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanBStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBMainObjectGroup = ciscoPrpMIBMainObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpMIBMainObjectGroup.setDescription('Object group for PRP channel table entries.')
ciscoPrpMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2, 2)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelStateChange"), ("CISCO-PRP-MIB", "ciscoPrpLanAStateChange"), ("CISCO-PRP-MIB", "ciscoPrpLanBStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBNotificationGroup = ciscoPrpMIBNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoPrpMIBNotificationGroup.setDescription('Notification group which indicates state changes of a PRP\n        channel.')
mibBuilder.exportSymbols("CISCO-PRP-MIB", PYSNMP_MODULE_ID=ciscoPrpMIB, PrpStatus=PrpStatus, ciscoPrpChannelEntry=ciscoPrpChannelEntry, ciscoPrpChannelId=ciscoPrpChannelId, ciscoPrpChannelIndex=ciscoPrpChannelIndex, ciscoPrpChannelLanAStatus=ciscoPrpChannelLanAStatus, ciscoPrpChannelLanBStatus=ciscoPrpChannelLanBStatus, ciscoPrpChannelName=ciscoPrpChannelName, ciscoPrpChannelStateChange=ciscoPrpChannelStateChange, ciscoPrpChannelStatus=ciscoPrpChannelStatus, ciscoPrpChannelTable=ciscoPrpChannelTable, ciscoPrpLanAStateChange=ciscoPrpLanAStateChange, ciscoPrpLanBStateChange=ciscoPrpLanBStateChange, ciscoPrpMIB=ciscoPrpMIB, ciscoPrpMIBCompliance=ciscoPrpMIBCompliance, ciscoPrpMIBCompliances=ciscoPrpMIBCompliances, ciscoPrpMIBConform=ciscoPrpMIBConform, ciscoPrpMIBGroups=ciscoPrpMIBGroups, ciscoPrpMIBMainObjectGroup=ciscoPrpMIBMainObjectGroup, ciscoPrpMIBNotificationGroup=ciscoPrpMIBNotificationGroup, ciscoPrpMIBNotifs=ciscoPrpMIBNotifs, ciscoPrpMIBObjects=ciscoPrpMIBObjects)
