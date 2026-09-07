#
# PySNMP MIB module CISCO-SWITCH-FABRIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SWITCH-FABRIC-MIB
# Source digest sha256:42f648f298b4df99b868e09ddc44d9d511d5ac3f49f752840d7403389c087596
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
PhysicalIndex, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DateAndTime, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "TruthValue")
ciscoSwitchFabricMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 803))
ciscoSwitchFabricMIB.setRevisions(('2014-07-30 00:00', '2012-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setRevisionsDescriptions(('Added the following OBJECT-GROUP\n         - csfFabricCrcErrorNotifsControlGroup \n         - csfFabricCrcErrorNotifsInfoGroup \n         - csfFabricCrcErrorNotifsGroup.\n         Added new compliance csfSwitchFabricMIBCompliance1.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setLastUpdated('2014-07-30 00:00')
if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setContactInfo('Cisco Systems\n            Customer Service\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchFabricMIB.setDescription('This MIB module defined managed objects that\n        facilitates the management of switching fabric\n        information in a Cisco switch.')
ciscoSwitchFabricMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 0))
ciscoSwitchFabricMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1))
ciscoSwitchFabricMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 2))
csfFabricStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1))
csfNotifsControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 2))
csfNotifsOnlyInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3))
class CsfFabricLinkType(TextualConvention, Integer32):
    description = 'The type of fabric link.\n\n        other                       - none of the following\n        qEngineFacingLcXbarLink     - queue engine facing linecard \n                                      crossbar link \n        fabricXbarLink              - fabric module crossbar link\n        fabricFacingLcXbarLink      - fabric module facing linecard \n                                      crossbar link\n        lcXbarInterLink             - linecard crossbar interlink\n        fabricXbarInterLink         - fabric module crossbar interlink\n        centralXbarLink             - central fabric link'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("qEngineFacingLcXbarLink", 2), ("fabricXbarLink", 3), ("fabricFacingLcXbarLink", 4), ("lcXbarInterLink", 5), ("fabricXbarInterLink", 6), ("centralXbarLink", 7))

class CsfPercentOrMinusOne(TextualConvention, Integer32):
    description = 'An integer that is in the range of a percent value.\n\n        A value of -1 means that the percentage is not available.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100), )
csfFabricUtilTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: csfFabricUtilTable.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilTable.setDescription('A table containing fabric utilization information.')
csfFabricUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilLinkType"), (0, "CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilIndex"))
if mibBuilder.loadTexts: csfFabricUtilEntry.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilEntry.setDescription('A conceptual row containing the fabric utilization\n        information for a particular type of traffic utilization\n        of a fabric entity.\n\n        An entry of this table is created if a traffic utilization\n        on a fabric entity is detected by the managed system.\n\n        An entry of this table is deleted when the removal of fabric\n        entity.')
csfFabricUtilLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 1), CsfFabricLinkType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: csfFabricUtilLinkType.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilLinkType.setDescription('This object indicates the type of fabric link on which \n        fabric traffic utilization is monitored.')
csfFabricUtilIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 2), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: csfFabricUtilIndex.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilIndex.setDescription('This object indicates an arbitrary integer value which\n        uniquely identifies the type of traffic utilization.')
csfFabricUtilDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilDescr.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilDescr.setDescription('This object indicates the human-readable description of\n        the type of fabric traffic utilization.')
csfFabricUtilBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 4), Unsigned32()).setUnits('gigabits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilBandwidth.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilBandwidth.setDescription('This object indicates the bandwidth of the fabric link.')
csfFabricUtilIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 5), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilIn.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilIn.setDescription('This object indicates the utilization on the\n        fabric link input.')
csfFabricUtilInPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 6), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilInPeak.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilInPeak.setDescription('This object indicates the peak utilization on the\n        fabric link input.')
csfFabricUtilInPeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilInPeakTime.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilInPeakTime.setDescription("This object indicates the time of the most recent change in\n        the corresponding instance value of csfFabricUtilInPeak.\n\n        This object contains value 0x0000010100000000 when the\n        corresponding instance value of csfFabricUtilInPeak is\n        '0 or '-1'.")
csfFabricUtilOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 8), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilOut.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilOut.setDescription('This object indicates the utilization on the\n        fabric link output.')
csfFabricUtilOutPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 9), CsfPercentOrMinusOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilOutPeak.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilOutPeak.setDescription('This object indicates the peak utilization on the\n        fabric link output.')
csfFabricUtilOutPeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 1, 1, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfFabricUtilOutPeakTime.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilOutPeakTime.setDescription("This object indicates the time of the most recent change in\n        the corresponding instance value of csfFabricUtilOutPeak.\n\n        This object contains value 0x0000010100000000 when the\n        corresponding instance value of csfFabricUtilInPeak is\n        '0 or '-1'.")
csfFabricCrcErrorNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfFabricCrcErrorNotifEnable.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorNotifEnable.setDescription("This object specifies whether the system generates the\n         cfsFabricCrcErrorNotif.\n\n         A value of 'false' will prevent cfsFabricCrcErrorNotif\n         notifications from being generated by this system.")
csfFabricCrcErrorEntPhysicalIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3, 1), PhysicalIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: csfFabricCrcErrorEntPhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorEntPhysicalIndex.setDescription('This object indicates the entPhysicalIndex of the fabric\n        entity on which fabric CRC error happens.')
csfFabricCrcErrorDescr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 803, 1, 3, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: csfFabricCrcErrorDescr.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorDescr.setDescription('This object indicates the fabric CRC error description.\n        A zero-length string indicates that the error description\n        is not available.')
csfFabricCrcErrorNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 803, 0, 1)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorEntPhysicalIndex"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorDescr"))
if mibBuilder.loadTexts: csfFabricCrcErrorNotif.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorNotif.setDescription('A cfsFabricCrcErrorNotif is generated when\n        fabric CRC errors are detected by the managed system.')
csfSwitchFabricMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1))
csfSwitchFabricMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2))
csfSwitchFabricMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1, 1)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfSwitchFabricMIBCompliance = csfSwitchFabricMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: csfSwitchFabricMIBCompliance.setDescription('The compliance statement for\n        the CISCO-SWITCH-FABRIC-MIB.')
csfSwitchFabricMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 1, 2)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilGroup"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifsControlGroup"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifsInfoGroup"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfSwitchFabricMIBCompliance1 = csfSwitchFabricMIBCompliance1.setStatus('current')
if mibBuilder.loadTexts: csfSwitchFabricMIBCompliance1.setDescription('The compliance statement for\n        the CISCO-SWITCH-FABRIC-MIB.')
csfFabricUtilGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 1)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilDescr"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilBandwidth"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilIn"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilInPeak"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilInPeakTime"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOut"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOutPeak"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricUtilOutPeakTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricUtilGroup = csfFabricUtilGroup.setStatus('current')
if mibBuilder.loadTexts: csfFabricUtilGroup.setDescription('A collection of objects providing the information\n        about utilization on the fabric link.')
csfFabricCrcErrorNotifsControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 2)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricCrcErrorNotifsControlGroup = csfFabricCrcErrorNotifsControlGroup.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorNotifsControlGroup.setDescription('A collection of objects providing notification \n        control for csfFabricCrcErrorNotif.')
csfFabricCrcErrorNotifsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 3)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorEntPhysicalIndex"), ("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricCrcErrorNotifsInfoGroup = csfFabricCrcErrorNotifsInfoGroup.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorNotifsInfoGroup.setDescription('A collection of object(s) providing the variable binding  \n        for csfFabricCrcErrorNotif.')
csfFabricCrcErrorNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 803, 2, 2, 4)).setObjects(("CISCO-SWITCH-FABRIC-MIB", "csfFabricCrcErrorNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csfFabricCrcErrorNotifsGroup = csfFabricCrcErrorNotifsGroup.setStatus('current')
if mibBuilder.loadTexts: csfFabricCrcErrorNotifsGroup.setDescription('A collection of Fabric CRC Error notifications for \n        CISCO-SWITCH-FABRIC-MIB.')
mibBuilder.exportSymbols("CISCO-SWITCH-FABRIC-MIB", CsfFabricLinkType=CsfFabricLinkType, CsfPercentOrMinusOne=CsfPercentOrMinusOne, PYSNMP_MODULE_ID=ciscoSwitchFabricMIB, ciscoSwitchFabricMIB=ciscoSwitchFabricMIB, ciscoSwitchFabricMIBConform=ciscoSwitchFabricMIBConform, ciscoSwitchFabricMIBNotifs=ciscoSwitchFabricMIBNotifs, ciscoSwitchFabricMIBObjects=ciscoSwitchFabricMIBObjects, csfFabricCrcErrorDescr=csfFabricCrcErrorDescr, csfFabricCrcErrorEntPhysicalIndex=csfFabricCrcErrorEntPhysicalIndex, csfFabricCrcErrorNotif=csfFabricCrcErrorNotif, csfFabricCrcErrorNotifEnable=csfFabricCrcErrorNotifEnable, csfFabricCrcErrorNotifsControlGroup=csfFabricCrcErrorNotifsControlGroup, csfFabricCrcErrorNotifsGroup=csfFabricCrcErrorNotifsGroup, csfFabricCrcErrorNotifsInfoGroup=csfFabricCrcErrorNotifsInfoGroup, csfFabricStatistics=csfFabricStatistics, csfFabricUtilBandwidth=csfFabricUtilBandwidth, csfFabricUtilDescr=csfFabricUtilDescr, csfFabricUtilEntry=csfFabricUtilEntry, csfFabricUtilGroup=csfFabricUtilGroup, csfFabricUtilIn=csfFabricUtilIn, csfFabricUtilInPeak=csfFabricUtilInPeak, csfFabricUtilInPeakTime=csfFabricUtilInPeakTime, csfFabricUtilIndex=csfFabricUtilIndex, csfFabricUtilLinkType=csfFabricUtilLinkType, csfFabricUtilOut=csfFabricUtilOut, csfFabricUtilOutPeak=csfFabricUtilOutPeak, csfFabricUtilOutPeakTime=csfFabricUtilOutPeakTime, csfFabricUtilTable=csfFabricUtilTable, csfNotifsControl=csfNotifsControl, csfNotifsOnlyInfo=csfNotifsOnlyInfo, csfSwitchFabricMIBCompliance1=csfSwitchFabricMIBCompliance1, csfSwitchFabricMIBCompliance=csfSwitchFabricMIBCompliance, csfSwitchFabricMIBCompliances=csfSwitchFabricMIBCompliances, csfSwitchFabricMIBGroups=csfSwitchFabricMIBGroups)
