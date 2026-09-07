#
# PySNMP MIB module CISCO-ENTITY-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-SENSOR-MIB
# Source digest sha256:8ef6e1cfdfaa517021cd6fc9ee75d87859e95701dbaeac1331025cc1a211accd
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp", "TruthValue")
entitySensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 91))
entitySensorMIB.setRevisions(('2020-09-22 00:00', '2002-09-18 00:00', '2000-06-20 00:00',))
if mibBuilder.loadTexts: entitySensorMIB.setLastUpdated('2020-09-22 00:00')
if mibBuilder.loadTexts: entitySensorMIB.setOrganization('Cisco Systems, Inc.')
entitySensorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1))
entitySensorMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 2))
entitySensorMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3))
class SensorDataType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("voltsAC", 3), ("voltsDC", 4), ("amperes", 5), ("watts", 6), ("hertz", 7), ("celsius", 8), ("percentRH", 9), ("rpm", 10), ("cmm", 11), ("truthvalue", 12), ("specialEnum", 13))

class SensorDataScale(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class SensorPrecision(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-8, 9)

class SensorValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class SensorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3))

class SensorValueUpdateRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 999999999)

class SensorThresholdSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30))
    namedValues = NamedValues(("other", 1), ("minor", 10), ("major", 20), ("critical", 30))

class SensorThresholdRelation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("lessThan", 1), ("lessOrEqual", 2), ("greaterThan", 3), ("greaterOrEqual", 4), ("equalTo", 5), ("notEqualTo", 6))

entSensorValues = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1))
entSensorThresholds = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2))
entSensorValueTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entSensorValueTable.setStatus('current')
entSensorValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entSensorValueEntry.setStatus('current')
entSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 1), SensorDataType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorType.setStatus('current')
entSensorScale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 2), SensorDataScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorScale.setStatus('current')
entSensorPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 3), SensorPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorPrecision.setStatus('current')
entSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 4), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValue.setStatus('current')
entSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 5), SensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorStatus.setStatus('current')
entSensorValueTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValueTimeStamp.setStatus('current')
entSensorValueUpdateRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 7), SensorValueUpdateRate()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValueUpdateRate.setStatus('current')
entSensorMeasuredEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorMeasuredEntity.setStatus('current')
entSensorThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entSensorThresholdTable.setStatus('current')
entSensorThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdIndex"))
if mibBuilder.loadTexts: entSensorThresholdEntry.setStatus('current')
entSensorThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99999999))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entSensorThresholdIndex.setStatus('current')
entSensorThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 2), SensorThresholdSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdSeverity.setStatus('current')
entSensorThresholdRelation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 3), SensorThresholdRelation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdRelation.setStatus('current')
entSensorThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 4), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdValue.setStatus('current')
entSensorThresholdEvaluation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorThresholdEvaluation.setStatus('current')
entSensorThresholdNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdNotificationEnable.setStatus('current')
entitySensorMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0))
entSensorThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"))
if mibBuilder.loadTexts: entSensorThresholdNotification.setStatus('current')
entitySensorMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1))
entitySensorMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2))
entitySensorMIBComplianceV01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV01 = entitySensorMIBComplianceV01.setStatus('deprecated')
entitySensorMIBComplianceV02 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 2)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV02 = entitySensorMIBComplianceV02.setStatus('current')
entitySensorValueGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorType"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorScale"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorPrecision"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorStatus"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValueTimeStamp"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValueUpdateRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorValueGroup = entitySensorValueGroup.setStatus('current')
entitySensorThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 2)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdSeverity"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdRelation"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdEvaluation"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorThresholdGroup = entitySensorThresholdGroup.setStatus('current')
entitySensorThresholdNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 3)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorThresholdNotificationGroup = entitySensorThresholdNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-MIB", PYSNMP_MODULE_ID=entitySensorMIB, SensorDataScale=SensorDataScale, SensorDataType=SensorDataType, SensorPrecision=SensorPrecision, SensorStatus=SensorStatus, SensorThresholdRelation=SensorThresholdRelation, SensorThresholdSeverity=SensorThresholdSeverity, SensorValue=SensorValue, SensorValueUpdateRate=SensorValueUpdateRate, entSensorMeasuredEntity=entSensorMeasuredEntity, entSensorPrecision=entSensorPrecision, entSensorScale=entSensorScale, entSensorStatus=entSensorStatus, entSensorThresholdEntry=entSensorThresholdEntry, entSensorThresholdEvaluation=entSensorThresholdEvaluation, entSensorThresholdIndex=entSensorThresholdIndex, entSensorThresholdNotification=entSensorThresholdNotification, entSensorThresholdNotificationEnable=entSensorThresholdNotificationEnable, entSensorThresholdRelation=entSensorThresholdRelation, entSensorThresholdSeverity=entSensorThresholdSeverity, entSensorThresholdTable=entSensorThresholdTable, entSensorThresholdValue=entSensorThresholdValue, entSensorThresholds=entSensorThresholds, entSensorType=entSensorType, entSensorValue=entSensorValue, entSensorValueEntry=entSensorValueEntry, entSensorValueTable=entSensorValueTable, entSensorValueTimeStamp=entSensorValueTimeStamp, entSensorValueUpdateRate=entSensorValueUpdateRate, entSensorValues=entSensorValues, entitySensorMIB=entitySensorMIB, entitySensorMIBComplianceV01=entitySensorMIBComplianceV01, entitySensorMIBComplianceV02=entitySensorMIBComplianceV02, entitySensorMIBCompliances=entitySensorMIBCompliances, entitySensorMIBConformance=entitySensorMIBConformance, entitySensorMIBGroups=entitySensorMIBGroups, entitySensorMIBNotificationPrefix=entitySensorMIBNotificationPrefix, entitySensorMIBNotifications=entitySensorMIBNotifications, entitySensorMIBObjects=entitySensorMIBObjects, entitySensorThresholdGroup=entitySensorThresholdGroup, entitySensorThresholdNotificationGroup=entitySensorThresholdNotificationGroup, entitySensorValueGroup=entitySensorValueGroup)
