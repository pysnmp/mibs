#
# PySNMP MIB module CISCO-ENTITY-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-EXT-MIB
# Source digest sha256:d05ccbf196c6e887a4bbe052e182514dbfa12656e912449496fe61063404daf8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Unsigned64, = mibBuilder.importSymbols("CISCO-TC", "Unsigned64")
entPhysicalContainedIn, entPhysicalDescr, entPhysicalEntry, entPhysicalIndex, entPhysicalName = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalContainedIn", "entPhysicalDescr", "entPhysicalEntry", "entPhysicalIndex", "entPhysicalName")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoEntityExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 195))
ciscoEntityExtMIB.setRevisions(('2018-04-04 00:00', '2015-04-17 00:00', '2014-09-12 00:00', '2014-03-27 00:00', '2013-08-06 00:00', '2013-08-05 00:00', '2008-11-24 00:00', '2004-07-06 00:00', '2004-03-03 00:00', '2004-01-26 00:00', '2003-08-24 00:00', '2001-05-17 00:00', '2001-04-05 00:00',))
if mibBuilder.loadTexts: ciscoEntityExtMIB.setLastUpdated('2018-04-04 00:00')
if mibBuilder.loadTexts: ciscoEntityExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoEntityExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 1))
class ConfigRegisterValue(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class BootImageList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

ceExtPhysicalProcessorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceExtPhysicalProcessorTable.setStatus('current')
ceExtPhysicalProcessorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceExtPhysicalProcessorEntry.setStatus('current')
ceExtProcessorRam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 1), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtProcessorRam.setStatus('current')
ceExtNVRAMSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 2), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtNVRAMSize.setStatus('current')
ceExtNVRAMUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 3), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtNVRAMUsed.setStatus('current')
ceExtProcessorRamOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 4), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtProcessorRamOverflow.setStatus('current')
ceExtHCProcessorRam = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 5), Unsigned64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtHCProcessorRam.setStatus('current')
ceExtNVRAMSizeOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 6), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtNVRAMSizeOverflow.setStatus('current')
ceExtHCNVRAMSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 7), Unsigned64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtHCNVRAMSize.setStatus('current')
ceExtNVRAMUsedOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 8), Unsigned32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtNVRAMUsedOverflow.setStatus('current')
ceExtHCNVRAMUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 9), Unsigned64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtHCNVRAMUsed.setStatus('current')
ceExtConfigRegTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceExtConfigRegTable.setStatus('current')
ceExtConfigRegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceExtConfigRegEntry.setStatus('current')
ceExtConfigRegister = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 1), ConfigRegisterValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtConfigRegister.setStatus('current')
ceExtConfigRegNext = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 2), ConfigRegisterValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceExtConfigRegNext.setStatus('current')
ceExtSysBootImageList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 3), BootImageList().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceExtSysBootImageList.setStatus('current')
ceExtKickstartImageList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 4), BootImageList().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceExtKickstartImageList.setStatus('current')
ceExtEntityLEDTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceExtEntityLEDTable.setStatus('current')
ceExtEntityLEDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-EXT-MIB", "ceExtEntityLEDType"))
if mibBuilder.loadTexts: ceExtEntityLEDEntry.setStatus('current')
ceExtEntityLEDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("status", 1), ("system", 2), ("active", 3), ("power", 4), ("battery", 5)))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceExtEntityLEDType.setStatus('current')
ceExtEntityLEDColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("green", 2), ("amber", 3), ("red", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtEntityLEDColor.setStatus('current')
ceExtEntPhysicalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceExtEntPhysicalTable.setStatus('current')
ceExtEntPhysicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 4, 1), ).setMaxAccess("notaccessible")
entPhysicalEntry.registerAugmentions(("CISCO-ENTITY-EXT-MIB", "ceExtEntPhysicalEntry"))
ceExtEntPhysicalEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
if mibBuilder.loadTexts: ceExtEntPhysicalEntry.setStatus('current')
ceEntPhysicalSecondSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceEntPhysicalSecondSerialNum.setStatus('current')
ceExtNotificationControlObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5))
ceExtEntDoorNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceExtEntDoorNotifEnable.setStatus('current')
ceExtEntBreakOutPortNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5, 2), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtEntBreakOutPortNotifEnable.setStatus('current')
ceExtEntUsbModemNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceExtEntUsbModemNotifEnable.setStatus('current')
ceExtUSBModemTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceExtUSBModemTable.setStatus('current')
ceExtUSBModemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceExtUSBModemEntry.setStatus('current')
ceExtUSBModemIMEI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtUSBModemIMEI.setStatus('current')
ceExtUSBModemIMSI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtUSBModemIMSI.setStatus('current')
ceExtUSBModemServiceProvider = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtUSBModemServiceProvider.setStatus('current')
ceExtUSBModemSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceExtUSBModemSignalStrength.setStatus('current')
ceExtMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 2))
ciscoEntityExtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0))
ceExtEntDoorCloseNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-MIB", "entPhysicalName"))
if mibBuilder.loadTexts: ceExtEntDoorCloseNotif.setStatus('current')
ceExtEntDoorOpenNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 2)).setObjects(("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-MIB", "entPhysicalName"))
if mibBuilder.loadTexts: ceExtEntDoorOpenNotif.setStatus('current')
ceExtBreakOutPortInserted = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 3)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"), ("ENTITY-MIB", "entPhysicalName"))
if mibBuilder.loadTexts: ceExtBreakOutPortInserted.setStatus('current')
ceExtBreakOutPortRemoved = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 4)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"), ("ENTITY-MIB", "entPhysicalName"))
if mibBuilder.loadTexts: ceExtBreakOutPortRemoved.setStatus('current')
ceExtUSBModemPlugInNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 5)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"), ("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: ceExtUSBModemPlugInNotif.setStatus('current')
ceExtUSBModemPlugOutNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 6)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"), ("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: ceExtUSBModemPlugOutNotif.setStatus('current')
ciscoEntityExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 3))
ciscoEntityExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1))
ciscoEntityExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2))
ciscoEntityExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 1)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBCompliance = ciscoEntityExtMIBCompliance.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 2)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev1 = ciscoEntityExtMIBComplianceRev1.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 3)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"), ("CISCO-ENTITY-EXT-MIB", "ciscoExtEntityPhysicalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev2 = ciscoEntityExtMIBComplianceRev2.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 4)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"), ("CISCO-ENTITY-EXT-MIB", "ciscoExtEntityPhysicalGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorOverflowGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev3 = ciscoEntityExtMIBComplianceRev3.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 5)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"), ("CISCO-ENTITY-EXT-MIB", "ciscoExtEntityPhysicalGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorOverflowGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorHCGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev4 = ciscoEntityExtMIBComplianceRev4.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 6)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"), ("CISCO-ENTITY-EXT-MIB", "ciscoExtEntityPhysicalGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorOverflowGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorHCGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifControlGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortNotifGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortNotifControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev5 = ciscoEntityExtMIBComplianceRev5.setStatus('deprecated')
ciscoEntityExtMIBComplianceRev6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 7)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtPhysicalProcessorGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtConfigRegGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroup"), ("CISCO-ENTITY-EXT-MIB", "ciscoEntityExtLEDGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageListGroupRev1"), ("CISCO-ENTITY-EXT-MIB", "ciscoExtEntityPhysicalGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorOverflowGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtPhyProcessorHCGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifControlGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortNotifGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortNotifControlGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtUsbModemNotificationsGroup"), ("CISCO-ENTITY-EXT-MIB", "ceExtUsbModemNotifControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtMIBComplianceRev6 = ciscoEntityExtMIBComplianceRev6.setStatus('current')
ceExtPhysicalProcessorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 1)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtProcessorRam"), ("CISCO-ENTITY-EXT-MIB", "ceExtNVRAMSize"), ("CISCO-ENTITY-EXT-MIB", "ceExtNVRAMUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtPhysicalProcessorGroup = ceExtPhysicalProcessorGroup.setStatus('current')
ciscoEntityExtConfigRegGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 2)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtConfigRegister"), ("CISCO-ENTITY-EXT-MIB", "ceExtConfigRegNext"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtConfigRegGroup = ciscoEntityExtConfigRegGroup.setStatus('current')
ceExtSysBootImageListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 3)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtSysBootImageListGroup = ceExtSysBootImageListGroup.setStatus('current')
ciscoEntityExtLEDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 4)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtEntityLEDColor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntityExtLEDGroup = ciscoEntityExtLEDGroup.setStatus('current')
ceExtSysBootImageListGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 5)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtKickstartImageList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtSysBootImageListGroupRev1 = ceExtSysBootImageListGroupRev1.setStatus('current')
ciscoExtEntityPhysicalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 6)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceEntPhysicalSecondSerialNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtEntityPhysicalGroup = ciscoExtEntityPhysicalGroup.setStatus('current')
ceExtPhyProcessorOverflowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 7)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtProcessorRamOverflow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtPhyProcessorOverflowGroup = ceExtPhyProcessorOverflowGroup.setStatus('current')
ceExtPhyProcessorHCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 8)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtHCProcessorRam"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtPhyProcessorHCGroup = ceExtPhyProcessorHCGroup.setStatus('current')
ceExtEntDoorNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 9)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorCloseNotif"), ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorOpenNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtEntDoorNotifGroup = ceExtEntDoorNotifGroup.setStatus('current')
ceExtEntDoorNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 10)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtEntDoorNotifControlGroup = ceExtEntDoorNotifControlGroup.setStatus('current')
ceExtBreakOutPortNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 11)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortInserted"), ("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortRemoved"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtBreakOutPortNotifGroup = ceExtBreakOutPortNotifGroup.setStatus('current')
ceExtBreakOutPortNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 12)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtEntBreakOutPortNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtBreakOutPortNotifControlGroup = ceExtBreakOutPortNotifControlGroup.setStatus('current')
ceExtUSBModemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 13)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemIMEI"), ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemIMSI"), ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemServiceProvider"), ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemSignalStrength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtUSBModemGroup = ceExtUSBModemGroup.setStatus('current')
ceExtUsbModemNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 14)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemPlugInNotif"), ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemPlugOutNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtUsbModemNotificationsGroup = ceExtUsbModemNotificationsGroup.setStatus('current')
ceExtUsbModemNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 15)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtEntUsbModemNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtUsbModemNotifControlGroup = ceExtUsbModemNotifControlGroup.setStatus('current')
ceExtNVRAMOverflowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 16)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtNVRAMSizeOverflow"), ("CISCO-ENTITY-EXT-MIB", "ceExtNVRAMUsedOverflow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtNVRAMOverflowGroup = ceExtNVRAMOverflowGroup.setStatus('current')
ceExtHCNVRAMGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 17)).setObjects(("CISCO-ENTITY-EXT-MIB", "ceExtHCNVRAMSize"), ("CISCO-ENTITY-EXT-MIB", "ceExtHCNVRAMUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceExtHCNVRAMGroup = ceExtHCNVRAMGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-EXT-MIB", BootImageList=BootImageList, ConfigRegisterValue=ConfigRegisterValue, PYSNMP_MODULE_ID=ciscoEntityExtMIB, ceEntPhysicalSecondSerialNum=ceEntPhysicalSecondSerialNum, ceExtBreakOutPortInserted=ceExtBreakOutPortInserted, ceExtBreakOutPortNotifControlGroup=ceExtBreakOutPortNotifControlGroup, ceExtBreakOutPortNotifGroup=ceExtBreakOutPortNotifGroup, ceExtBreakOutPortRemoved=ceExtBreakOutPortRemoved, ceExtConfigRegEntry=ceExtConfigRegEntry, ceExtConfigRegNext=ceExtConfigRegNext, ceExtConfigRegTable=ceExtConfigRegTable, ceExtConfigRegister=ceExtConfigRegister, ceExtEntBreakOutPortNotifEnable=ceExtEntBreakOutPortNotifEnable, ceExtEntDoorCloseNotif=ceExtEntDoorCloseNotif, ceExtEntDoorNotifControlGroup=ceExtEntDoorNotifControlGroup, ceExtEntDoorNotifEnable=ceExtEntDoorNotifEnable, ceExtEntDoorNotifGroup=ceExtEntDoorNotifGroup, ceExtEntDoorOpenNotif=ceExtEntDoorOpenNotif, ceExtEntPhysicalEntry=ceExtEntPhysicalEntry, ceExtEntPhysicalTable=ceExtEntPhysicalTable, ceExtEntUsbModemNotifEnable=ceExtEntUsbModemNotifEnable, ceExtEntityLEDColor=ceExtEntityLEDColor, ceExtEntityLEDEntry=ceExtEntityLEDEntry, ceExtEntityLEDTable=ceExtEntityLEDTable, ceExtEntityLEDType=ceExtEntityLEDType, ceExtHCNVRAMGroup=ceExtHCNVRAMGroup, ceExtHCNVRAMSize=ceExtHCNVRAMSize, ceExtHCNVRAMUsed=ceExtHCNVRAMUsed, ceExtHCProcessorRam=ceExtHCProcessorRam, ceExtKickstartImageList=ceExtKickstartImageList, ceExtMIBNotificationPrefix=ceExtMIBNotificationPrefix, ceExtNVRAMOverflowGroup=ceExtNVRAMOverflowGroup, ceExtNVRAMSize=ceExtNVRAMSize, ceExtNVRAMSizeOverflow=ceExtNVRAMSizeOverflow, ceExtNVRAMUsed=ceExtNVRAMUsed, ceExtNVRAMUsedOverflow=ceExtNVRAMUsedOverflow, ceExtNotificationControlObjects=ceExtNotificationControlObjects, ceExtPhyProcessorHCGroup=ceExtPhyProcessorHCGroup, ceExtPhyProcessorOverflowGroup=ceExtPhyProcessorOverflowGroup, ceExtPhysicalProcessorEntry=ceExtPhysicalProcessorEntry, ceExtPhysicalProcessorGroup=ceExtPhysicalProcessorGroup, ceExtPhysicalProcessorTable=ceExtPhysicalProcessorTable, ceExtProcessorRam=ceExtProcessorRam, ceExtProcessorRamOverflow=ceExtProcessorRamOverflow, ceExtSysBootImageList=ceExtSysBootImageList, ceExtSysBootImageListGroup=ceExtSysBootImageListGroup, ceExtSysBootImageListGroupRev1=ceExtSysBootImageListGroupRev1, ceExtUSBModemEntry=ceExtUSBModemEntry, ceExtUSBModemGroup=ceExtUSBModemGroup, ceExtUSBModemIMEI=ceExtUSBModemIMEI, ceExtUSBModemIMSI=ceExtUSBModemIMSI, ceExtUSBModemPlugInNotif=ceExtUSBModemPlugInNotif, ceExtUSBModemPlugOutNotif=ceExtUSBModemPlugOutNotif, ceExtUSBModemServiceProvider=ceExtUSBModemServiceProvider, ceExtUSBModemSignalStrength=ceExtUSBModemSignalStrength, ceExtUSBModemTable=ceExtUSBModemTable, ceExtUsbModemNotifControlGroup=ceExtUsbModemNotifControlGroup, ceExtUsbModemNotificationsGroup=ceExtUsbModemNotificationsGroup, ciscoEntityExtConfigRegGroup=ciscoEntityExtConfigRegGroup, ciscoEntityExtLEDGroup=ciscoEntityExtLEDGroup, ciscoEntityExtMIB=ciscoEntityExtMIB, ciscoEntityExtMIBCompliance=ciscoEntityExtMIBCompliance, ciscoEntityExtMIBComplianceRev1=ciscoEntityExtMIBComplianceRev1, ciscoEntityExtMIBComplianceRev2=ciscoEntityExtMIBComplianceRev2, ciscoEntityExtMIBComplianceRev3=ciscoEntityExtMIBComplianceRev3, ciscoEntityExtMIBComplianceRev4=ciscoEntityExtMIBComplianceRev4, ciscoEntityExtMIBComplianceRev5=ciscoEntityExtMIBComplianceRev5, ciscoEntityExtMIBComplianceRev6=ciscoEntityExtMIBComplianceRev6, ciscoEntityExtMIBCompliances=ciscoEntityExtMIBCompliances, ciscoEntityExtMIBConformance=ciscoEntityExtMIBConformance, ciscoEntityExtMIBGroups=ciscoEntityExtMIBGroups, ciscoEntityExtMIBNotifications=ciscoEntityExtMIBNotifications, ciscoEntityExtMIBObjects=ciscoEntityExtMIBObjects, ciscoExtEntityPhysicalGroup=ciscoExtEntityPhysicalGroup)
