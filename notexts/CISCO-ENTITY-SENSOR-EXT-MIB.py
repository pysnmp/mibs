#
# PySNMP MIB module CISCO-ENTITY-SENSOR-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-SENSOR-EXT-MIB
# Source digest sha256:3f28e890b97ac630e86361f5fb5a9ae9d8850a23d924c80bf8d50c4b749983b9
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalDescr, entPhysicalIndex, entPhysicalName = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalDescr", "entPhysicalIndex", "entPhysicalName")
EntitySensorValue, entPhySensorType, entPhySensorValue = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue", "entPhySensorType", "entPhySensorValue")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoEntitySensorExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 745))
ciscoEntitySensorExtMIB.setRevisions(('2010-06-09 00:00',))
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setLastUpdated('2010-06-10 00:00')
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoEntitySensorExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 0))
ciscoEntitySensorExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 1))
ciscoEntitySensorExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2))
class CiscoSensorThresholdSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30))
    namedValues = NamedValues(("other", 1), ("minor", 10), ("major", 20), ("critical", 30))

class CiscoSensorThresholdRelation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("lessThan", 1), ("lessOrEqual", 2), ("greaterThan", 3), ("greaterOrEqual", 4), ("equalTo", 5), ("notEqualTo", 6))

ceSensorExtThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceSensorExtThresholdTable.setStatus('current')
ceSensorExtThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdIndex"))
if mibBuilder.loadTexts: ceSensorExtThresholdEntry.setStatus('current')
ceSensorExtThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceSensorExtThresholdIndex.setStatus('current')
ceSensorExtThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 2), CiscoSensorThresholdSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdSeverity.setStatus('current')
ceSensorExtThresholdRelation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 3), CiscoSensorThresholdRelation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdRelation.setStatus('current')
ceSensorExtThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 4), EntitySensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdValue.setStatus('current')
ceSensorExtThresholdEvaluation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceSensorExtThresholdEvaluation.setStatus('current')
ceSensorExtThresholdNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("transparent", 3))).clone('transparent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdNotifEnable.setStatus('current')
ciscoEntSensorExtGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 2))
ceSensorExtThresholdNotifGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdNotifGlobalEnable.setStatus('current')
ceSensorExtThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 745, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("ENTITY-SENSOR-MIB", "entPhySensorType"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdValue"))
if mibBuilder.loadTexts: ceSensorExtThresholdNotification.setStatus('current')
ciscoEntSensorExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 1))
ciscoEntSensorExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2))
ciscoEntSensorExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 1, 1)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtThresholdGroup"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtNotificationCtrlGroup"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtMIBCompliance = ciscoEntSensorExtMIBCompliance.setStatus('current')
ciscoEntSensorExtThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 1)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdSeverity"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdRelation"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdValue"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdEvaluation"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtThresholdGroup = ciscoEntSensorExtThresholdGroup.setStatus('current')
ciscoEntSensorExtNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 2)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtNotificationGroup = ciscoEntSensorExtNotificationGroup.setStatus('current')
ciscoEntSensorExtNotificationCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 3)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotifGlobalEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtNotificationCtrlGroup = ciscoEntSensorExtNotificationCtrlGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-EXT-MIB", CiscoSensorThresholdRelation=CiscoSensorThresholdRelation, CiscoSensorThresholdSeverity=CiscoSensorThresholdSeverity, PYSNMP_MODULE_ID=ciscoEntitySensorExtMIB, ceSensorExtThresholdEntry=ceSensorExtThresholdEntry, ceSensorExtThresholdEvaluation=ceSensorExtThresholdEvaluation, ceSensorExtThresholdIndex=ceSensorExtThresholdIndex, ceSensorExtThresholdNotifEnable=ceSensorExtThresholdNotifEnable, ceSensorExtThresholdNotifGlobalEnable=ceSensorExtThresholdNotifGlobalEnable, ceSensorExtThresholdNotification=ceSensorExtThresholdNotification, ceSensorExtThresholdRelation=ceSensorExtThresholdRelation, ceSensorExtThresholdSeverity=ceSensorExtThresholdSeverity, ceSensorExtThresholdTable=ceSensorExtThresholdTable, ceSensorExtThresholdValue=ceSensorExtThresholdValue, ciscoEntSensorExtGlobalObjects=ciscoEntSensorExtGlobalObjects, ciscoEntSensorExtMIBCompliance=ciscoEntSensorExtMIBCompliance, ciscoEntSensorExtMIBCompliances=ciscoEntSensorExtMIBCompliances, ciscoEntSensorExtMIBGroups=ciscoEntSensorExtMIBGroups, ciscoEntSensorExtNotificationCtrlGroup=ciscoEntSensorExtNotificationCtrlGroup, ciscoEntSensorExtNotificationGroup=ciscoEntSensorExtNotificationGroup, ciscoEntSensorExtThresholdGroup=ciscoEntSensorExtThresholdGroup, ciscoEntitySensorExtMIB=ciscoEntitySensorExtMIB, ciscoEntitySensorExtMIBConform=ciscoEntitySensorExtMIBConform, ciscoEntitySensorExtMIBNotifs=ciscoEntitySensorExtMIBNotifs, ciscoEntitySensorExtMIBObjects=ciscoEntitySensorExtMIBObjects)
