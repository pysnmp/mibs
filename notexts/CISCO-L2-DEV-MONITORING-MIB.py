#
# PySNMP MIB module CISCO-L2-DEV-MONITORING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-L2-DEV-MONITORING-MIB
# Source digest sha256:f348b12e2d79f15d18623bc999fa9fadbd321131cc7d07aa6f97a00ab5ee87cb
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, MacAddress, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")
ciscoL2DevMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 271))
ciscoL2DevMonMIB.setRevisions(('2003-07-22 00:00', '2001-09-27 00:00',))
if mibBuilder.loadTexts: ciscoL2DevMonMIB.setLastUpdated('2003-07-22 00:00')
if mibBuilder.loadTexts: ciscoL2DevMonMIB.setOrganization('Cisco System Inc.')
ciscoL2DevMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 1))
cl2DevMonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1))
cl2DevMonInStandbyMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cl2DevMonInStandbyMode.setStatus('current')
cl2DevMonNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cl2DevMonNotifEnabled.setStatus('current')
cl2DevMonActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cl2DevMonActiveTable.setStatus('current')
cl2DevMonActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveMacAddress"))
if mibBuilder.loadTexts: cl2DevMonActiveEntry.setStatus('current')
cl2DevMonActiveMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 1), MacAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cl2DevMonActiveMacAddress.setStatus('current')
cl2DevMonActivePollingFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActivePollingFrequency.setStatus('current')
cl2DevMonActivePollingTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActivePollingTimeOut.setStatus('current')
cl2DevMonActiveRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActiveRowStatus.setStatus('current')
cl2DevMonActiveRadioMacType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ieee802dot11a", 1), ("ieee802dot11b", 2), ("ieee802dot11g", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActiveRadioMacType.setStatus('current')
cl2DevMonActiveLocalRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 271, 1, 1, 3, 1, 6), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cl2DevMonActiveLocalRadioIndex.setStatus('current')
ciscoL2DevMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 0))
cl2DevMonSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 271, 0, 1)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingFrequency"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingTimeOut"))
if mibBuilder.loadTexts: cl2DevMonSwitchover.setStatus('current')
ciscoL2DevMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 2))
ciscoL2DevMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1))
ciscoL2DevMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2))
ciscoL2DevMonCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1, 1)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonConfigGroup"), ("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonCompliance = ciscoL2DevMonCompliance.setStatus('deprecated')
ciscoL2DevMonComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 1, 2)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonConfigGroup"), ("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonNotificationGroup"), ("CISCO-L2-DEV-MONITORING-MIB", "ciscoL2DevMonRadioConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonComplianceRev1 = ciscoL2DevMonComplianceRev1.setStatus('current')
ciscoL2DevMonConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 1)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonInStandbyMode"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonNotifEnabled"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingFrequency"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActivePollingTimeOut"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonConfigGroup = ciscoL2DevMonConfigGroup.setStatus('current')
ciscoL2DevMonNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 2)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonSwitchover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonNotificationGroup = ciscoL2DevMonNotificationGroup.setStatus('current')
ciscoL2DevMonRadioConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 271, 2, 2, 3)).setObjects(("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveRadioMacType"), ("CISCO-L2-DEV-MONITORING-MIB", "cl2DevMonActiveLocalRadioIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoL2DevMonRadioConfigGroup = ciscoL2DevMonRadioConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-L2-DEV-MONITORING-MIB", PYSNMP_MODULE_ID=ciscoL2DevMonMIB, ciscoL2DevMonCompliance=ciscoL2DevMonCompliance, ciscoL2DevMonComplianceRev1=ciscoL2DevMonComplianceRev1, ciscoL2DevMonConfigGroup=ciscoL2DevMonConfigGroup, ciscoL2DevMonMIB=ciscoL2DevMonMIB, ciscoL2DevMonMIBCompliances=ciscoL2DevMonMIBCompliances, ciscoL2DevMonMIBConformance=ciscoL2DevMonMIBConformance, ciscoL2DevMonMIBGroups=ciscoL2DevMonMIBGroups, ciscoL2DevMonMIBNotifications=ciscoL2DevMonMIBNotifications, ciscoL2DevMonMIBObjects=ciscoL2DevMonMIBObjects, ciscoL2DevMonNotificationGroup=ciscoL2DevMonNotificationGroup, ciscoL2DevMonRadioConfigGroup=ciscoL2DevMonRadioConfigGroup, cl2DevMonActiveEntry=cl2DevMonActiveEntry, cl2DevMonActiveLocalRadioIndex=cl2DevMonActiveLocalRadioIndex, cl2DevMonActiveMacAddress=cl2DevMonActiveMacAddress, cl2DevMonActivePollingFrequency=cl2DevMonActivePollingFrequency, cl2DevMonActivePollingTimeOut=cl2DevMonActivePollingTimeOut, cl2DevMonActiveRadioMacType=cl2DevMonActiveRadioMacType, cl2DevMonActiveRowStatus=cl2DevMonActiveRowStatus, cl2DevMonActiveTable=cl2DevMonActiveTable, cl2DevMonConfig=cl2DevMonConfig, cl2DevMonInStandbyMode=cl2DevMonInStandbyMode, cl2DevMonNotifEnabled=cl2DevMonNotifEnabled, cl2DevMonSwitchover=cl2DevMonSwitchover)
