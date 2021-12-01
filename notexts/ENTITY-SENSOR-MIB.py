#
# PySNMP MIB module ENTITY-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/ENTITY-SENSOR-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 16:55:39 2021
# On host fv-az33-471 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
entityPhysicalGroup, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entityPhysicalGroup", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, mib_2, Integer32, MibIdentifier, Bits, Counter64, Counter32, Gauge32, ObjectIdentity, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "mib-2", "Integer32", "MibIdentifier", "Bits", "Counter64", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
entitySensorMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 99))
entitySensorMIB.setRevisions(('2002-12-16 00:00',))
if mibBuilder.loadTexts: entitySensorMIB.setLastUpdated('200212160000Z')
if mibBuilder.loadTexts: entitySensorMIB.setOrganization('IETF Entity MIB Working Group')
entitySensorObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 1))
entitySensorConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3))
class EntitySensorDataType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("voltsAC", 3), ("voltsDC", 4), ("amperes", 5), ("watts", 6), ("hertz", 7), ("celsius", 8), ("percentRH", 9), ("rpm", 10), ("cmm", 11), ("truthvalue", 12))

class EntitySensorDataScale(TextualConvention, Integer32):
    reference = 'The International System of Units (SI), National Institute of Standards and Technology, Spec. Publ. 330, August 1991.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class EntitySensorPrecision(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-8, 9)

class EntitySensorValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class EntitySensorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3))

entPhySensorTable = MibTable((1, 3, 6, 1, 2, 1, 99, 1, 1), )
if mibBuilder.loadTexts: entPhySensorTable.setStatus('current')
entPhySensorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 99, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entPhySensorEntry.setStatus('current')
entPhySensorType = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 1), EntitySensorDataType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorType.setStatus('current')
entPhySensorScale = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 2), EntitySensorDataScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorScale.setStatus('current')
entPhySensorPrecision = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 3), EntitySensorPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorPrecision.setStatus('current')
entPhySensorValue = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 4), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValue.setStatus('current')
entPhySensorOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 5), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorOperStatus.setStatus('current')
entPhySensorUnitsDisplay = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorUnitsDisplay.setStatus('current')
entPhySensorValueTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueTimeStamp.setStatus('current')
entPhySensorValueUpdateRate = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 8), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueUpdateRate.setStatus('current')
entitySensorCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3, 1))
entitySensorGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3, 2))
entitySensorCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 99, 3, 1, 1)).setObjects(("ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("ENTITY-MIB", "entityPhysicalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorCompliance = entitySensorCompliance.setStatus('current')
entitySensorValueGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 99, 3, 2, 1)).setObjects(("ENTITY-SENSOR-MIB", "entPhySensorType"), ("ENTITY-SENSOR-MIB", "entPhySensorScale"), ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("ENTITY-SENSOR-MIB", "entPhySensorOperStatus"), ("ENTITY-SENSOR-MIB", "entPhySensorUnitsDisplay"), ("ENTITY-SENSOR-MIB", "entPhySensorValueTimeStamp"), ("ENTITY-SENSOR-MIB", "entPhySensorValueUpdateRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorValueGroup = entitySensorValueGroup.setStatus('current')
mibBuilder.exportSymbols("ENTITY-SENSOR-MIB", entitySensorCompliances=entitySensorCompliances, entPhySensorOperStatus=entPhySensorOperStatus, entPhySensorEntry=entPhySensorEntry, entitySensorConformance=entitySensorConformance, entitySensorCompliance=entitySensorCompliance, entitySensorGroups=entitySensorGroups, EntitySensorDataScale=EntitySensorDataScale, entitySensorObjects=entitySensorObjects, entPhySensorType=entPhySensorType, entPhySensorUnitsDisplay=entPhySensorUnitsDisplay, entPhySensorValueTimeStamp=entPhySensorValueTimeStamp, entitySensorMIB=entitySensorMIB, entPhySensorScale=entPhySensorScale, EntitySensorValue=EntitySensorValue, entPhySensorValueUpdateRate=entPhySensorValueUpdateRate, entPhySensorValue=entPhySensorValue, EntitySensorPrecision=EntitySensorPrecision, EntitySensorDataType=EntitySensorDataType, entPhySensorTable=entPhySensorTable, EntitySensorStatus=EntitySensorStatus, PYSNMP_MODULE_ID=entitySensorMIB, entitySensorValueGroup=entitySensorValueGroup, entPhySensorPrecision=entPhySensorPrecision)
