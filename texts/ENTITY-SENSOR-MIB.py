#
# PySNMP MIB module ENTITY-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/ENTITY-SENSOR-MIB
# Produced by pysmi-1.1.11 at Wed Dec  6 02:58:10 2023
# On host fv-az520-882 platform Linux version 6.2.0-1016-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
entityPhysicalGroup, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entityPhysicalGroup", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, NotificationType, Bits, mib_2, IpAddress, Counter32, ModuleIdentity, ObjectIdentity, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "NotificationType", "Bits", "mib-2", "IpAddress", "Counter32", "ModuleIdentity", "ObjectIdentity", "Integer32", "Counter64")
TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString")
entitySensorMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 99))
entitySensorMIB.setRevisions(('2002-12-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: entitySensorMIB.setRevisionsDescriptions(('Initial version of the Entity Sensor MIB module, published\n             as RFC 3433.',))
if mibBuilder.loadTexts: entitySensorMIB.setLastUpdated('200212160000Z')
if mibBuilder.loadTexts: entitySensorMIB.setOrganization('IETF Entity MIB Working Group')
if mibBuilder.loadTexts: entitySensorMIB.setContactInfo('        Andy Bierman\n                     Cisco Systems, Inc.\n                Tel: +1 408-527-3711\n             E-mail: abierman@cisco.com\n             Postal: 170 West Tasman Drive\n                     San Jose, CA USA 95134\n\n                     Dan Romascanu\n                     Avaya Inc.\n                Tel: +972-3-645-8414\n              Email: dromasca@avaya.com\n             Postal: Atidim technology Park, Bldg. #3\n                     Tel Aviv, Israel, 61131\n\n                     K.C. Norseth\n                     L-3 Communications\n                Tel: +1 801-594-2809\n              Email: kenyon.c.norseth@L-3com.com\n             Postal: 640 N. 2200 West.\n\n\n\n                     Salt Lake City, Utah 84116-0850\n\n             Send comments to <entmib@ietf.org>\n             Mailing list subscription info:\n               http://www.ietf.org/mailman/listinfo/entmib ')
if mibBuilder.loadTexts: entitySensorMIB.setDescription('This module defines Entity MIB extensions for physical\n             sensors.\n\n             Copyright (C) The Internet Society (2002). This version\n             of this MIB module is part of RFC 3433; see the RFC\n             itself for full legal notices.')
entitySensorObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 1))
entitySensorConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3))
class EntitySensorDataType(TextualConvention, Integer32):
    description = 'An object using this data type represents the Entity Sensor\n            measurement data type associated with a physical sensor\n            value. The actual data units are determined by examining an\n            object of this type together with the associated\n            EntitySensorDataScale object.\n\n            An object of this type SHOULD be defined together with\n            objects of type EntitySensorDataScale and\n            EntitySensorPrecision.  Together, associated objects of\n            these three types are used to identify the semantics of an\n            object of type EntitySensorValue.\n\n\n\n\n\n\n            Valid values are:\n\n               other(1):        a measure other than those listed below\n               unknown(2):      unknown measurement, or arbitrary,\n                                relative numbers\n               voltsAC(3):      electric potential\n               voltsDC(4):      electric potential\n               amperes(5):      electric current\n               watts(6):        power\n               hertz(7):        frequency\n               celsius(8):      temperature\n               percentRH(9):    percent relative humidity\n               rpm(10):         shaft revolutions per minute\n               cmm(11),:        cubic meters per minute (airflow)\n               truthvalue(12):  value takes { true(1), false(2) }\n\n            '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("voltsAC", 3), ("voltsDC", 4), ("amperes", 5), ("watts", 6), ("hertz", 7), ("celsius", 8), ("percentRH", 9), ("rpm", 10), ("cmm", 11), ("truthvalue", 12))

class EntitySensorDataScale(TextualConvention, Integer32):
    reference = 'The International System of Units (SI),\n\n\n\n            National Institute of Standards and Technology,\n            Spec. Publ. 330, August 1991.'
    description = 'An object using this data type represents a data scaling\n            factor, represented with an International System of Units\n            (SI) prefix.  The actual data units are determined by\n            examining an object of this type together with the\n            associated EntitySensorDataType object.\n\n            An object of this type SHOULD be defined together with\n            objects of type EntitySensorDataType and\n            EntitySensorPrecision.  Together, associated objects of\n            these three types are used to identify the semantics of an\n            object of type EntitySensorValue.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class EntitySensorPrecision(TextualConvention, Integer32):
    description = "An object using this data type represents a sensor\n            precision range.\n\n            An object of this type SHOULD be defined together with\n            objects of type EntitySensorDataType and\n            EntitySensorDataScale.  Together, associated objects of\n            these three types are used to identify the semantics of an\n            object of type EntitySensorValue.\n\n            If an object of this type contains a value in the range 1 to\n            9, it represents the number of decimal places in the\n            fractional part of an associated EntitySensorValue fixed-\n            point number.\n\n            If an object of this type contains a value in the range -8\n            to -1, it represents the number of accurate digits in the\n            associated EntitySensorValue fixed-point number.\n\n            The value zero indicates the associated EntitySensorValue\n            object is not a fixed-point number.\n\n            Agent implementors must choose a value for the associated\n            EntitySensorPrecision object so that the precision and\n\n\n\n            accuracy of the associated EntitySensorValue object is\n            correctly indicated.\n\n            For example, a physical entity representing a temperature\n            sensor that can measure 0 degrees to 100 degrees C in 0.1\n            degree increments, +/- 0.05 degrees, would have an\n            EntitySensorPrecision value of '1', an EntitySensorDataScale\n            value of 'units(9)', and an EntitySensorValue ranging from\n            '0' to '1000'.  The EntitySensorValue would be interpreted\n            as 'degrees C * 10'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-8, 9)

class EntitySensorValue(TextualConvention, Integer32):
    description = "An object using this data type represents an Entity Sensor\n            value.\n            An object of this type SHOULD be defined together with\n            objects of type EntitySensorDataType, EntitySensorDataScale\n            and EntitySensorPrecision.  Together, associated objects of\n            those three types are used to identify the semantics of an\n            object of this data type.\n\n            The semantics of an object using this data type are\n            determined by the value of the associated\n            EntitySensorDataType object.\n\n            If the associated EntitySensorDataType object is equal to\n            'voltsAC(3)', 'voltsDC(4)', 'amperes(5)', 'watts(6),\n            'hertz(7)', 'celsius(8)', or 'cmm(11)', then an object of\n            this type MUST contain a fixed point number ranging from\n            -999,999,999 to +999,999,999.  The value -1000000000\n            indicates an underflow error. The value +1000000000\n            indicates an overflow error.  The EntitySensorPrecision\n            indicates how many fractional digits are represented in the\n            associated EntitySensorValue object.\n\n            If the associated EntitySensorDataType object is equal to\n            'percentRH(9)', then an object of this type MUST contain a\n            number ranging from 0 to 100.\n\n            If the associated EntitySensorDataType object is equal to\n            'rpm(10)', then an object of this type MUST contain a number\n            ranging from -999,999,999 to +999,999,999.\n\n            If the associated EntitySensorDataType object is equal to\n            'truthvalue(12)', then an object of this type MUST contain\n            either the value 'true(1)' or the value 'false(2)'.\n\n\n\n            If the associated EntitySensorDataType object is equal to\n            'other(1)' or unknown(2)', then an object of this type MUST\n            contain a number ranging from -1000000000 to 1000000000."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class EntitySensorStatus(TextualConvention, Integer32):
    description = "An object using this data type represents the operational\n            status of a physical sensor.\n\n            The value 'ok(1)' indicates that the agent can obtain the\n            sensor value.\n\n            The value 'unavailable(2)' indicates that the agent\n            presently cannot obtain the sensor value.\n\n            The value 'nonoperational(3)' indicates that the agent\n            believes the sensor is broken.  The sensor could have a hard\n            failure (disconnected wire), or a soft failure such as out-\n            of-range, jittery, or wildly fluctuating readings."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3))

entPhySensorTable = MibTable((1, 3, 6, 1, 2, 1, 99, 1, 1), )
if mibBuilder.loadTexts: entPhySensorTable.setStatus('current')
if mibBuilder.loadTexts: entPhySensorTable.setDescription('This table contains one row per physical sensor represented\n            by an associated row in the entPhysicalTable.')
entPhySensorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 99, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entPhySensorEntry.setStatus('current')
if mibBuilder.loadTexts: entPhySensorEntry.setDescription('Information about a particular physical sensor.\n\n\n\n\n\n            An entry in this table describes the present reading of a\n            sensor, the measurement units and scale, and sensor\n            operational status.\n\n            Entries are created in this table by the agent.  An entry\n            for each physical sensor SHOULD be created at the same time\n            as the associated entPhysicalEntry.  An entry SHOULD be\n            destroyed if the associated entPhysicalEntry is destroyed.')
entPhySensorType = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 1), EntitySensorDataType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorType.setStatus('current')
if mibBuilder.loadTexts: entPhySensorType.setDescription('The type of data returned by the associated\n            entPhySensorValue object.\n\n            This object SHOULD be set by the agent during entry\n            creation, and the value SHOULD NOT change during operation.')
entPhySensorScale = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 2), EntitySensorDataScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorScale.setStatus('current')
if mibBuilder.loadTexts: entPhySensorScale.setDescription('The exponent to apply to values returned by the associated\n            entPhySensorValue object.\n\n            This object SHOULD be set by the agent during entry\n            creation, and the value SHOULD NOT change during operation.')
entPhySensorPrecision = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 3), EntitySensorPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorPrecision.setStatus('current')
if mibBuilder.loadTexts: entPhySensorPrecision.setDescription("The number of decimal places of precision in fixed-point\n            sensor values returned by the associated entPhySensorValue\n            object.\n\n            This object SHOULD be set to '0' when the associated\n            entPhySensorType value is not a fixed-point type: e.g.,\n            'percentRH(9)', 'rpm(10)', 'cmm(11)', or 'truthvalue(12)'.\n\n            This object SHOULD be set by the agent during entry\n            creation, and the value SHOULD NOT change during operation.")
entPhySensorValue = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 4), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValue.setStatus('current')
if mibBuilder.loadTexts: entPhySensorValue.setDescription('The most recent measurement obtained by the agent for this\n            sensor.\n\n            To correctly interpret the value of this object, the\n            associated entPhySensorType, entPhySensorScale, and\n            entPhySensorPrecision objects must also be examined.')
entPhySensorOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 5), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorOperStatus.setStatus('current')
if mibBuilder.loadTexts: entPhySensorOperStatus.setDescription('The operational status of the sensor.')
entPhySensorUnitsDisplay = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorUnitsDisplay.setStatus('current')
if mibBuilder.loadTexts: entPhySensorUnitsDisplay.setDescription('A textual description of the data units that should be used\n            in the display of entPhySensorValue.')
entPhySensorValueTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueTimeStamp.setStatus('current')
if mibBuilder.loadTexts: entPhySensorValueTimeStamp.setDescription('The value of sysUpTime at the time the status and/or value\n            of this sensor was last obtained by the agent.')
entPhySensorValueUpdateRate = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 8), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueUpdateRate.setStatus('current')
if mibBuilder.loadTexts: entPhySensorValueUpdateRate.setDescription('An indication of the frequency that the agent updates the\n            associated entPhySensorValue object, representing in\n            milliseconds.\n\n            The value zero indicates:\n\n                - the sensor value is updated on demand (e.g.,\n                  when polled by the agent for a get-request),\n                - the sensor value is updated when the sensor\n                  value changes (event-driven),\n                - the agent does not know the update rate.\n\n            ')
entitySensorCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3, 1))
entitySensorGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3, 2))
entitySensorCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 99, 3, 1, 1)).setObjects(("ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("ENTITY-MIB", "entityPhysicalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorCompliance = entitySensorCompliance.setStatus('current')
if mibBuilder.loadTexts: entitySensorCompliance.setDescription('Describes the requirements for conformance to the Entity\n            Sensor MIB module.')
entitySensorValueGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 99, 3, 2, 1)).setObjects(("ENTITY-SENSOR-MIB", "entPhySensorType"), ("ENTITY-SENSOR-MIB", "entPhySensorScale"), ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("ENTITY-SENSOR-MIB", "entPhySensorOperStatus"), ("ENTITY-SENSOR-MIB", "entPhySensorUnitsDisplay"), ("ENTITY-SENSOR-MIB", "entPhySensorValueTimeStamp"), ("ENTITY-SENSOR-MIB", "entPhySensorValueUpdateRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorValueGroup = entitySensorValueGroup.setStatus('current')
if mibBuilder.loadTexts: entitySensorValueGroup.setDescription('A collection of objects representing physical entity sensor\n            information.')
mibBuilder.exportSymbols("ENTITY-SENSOR-MIB", entitySensorValueGroup=entitySensorValueGroup, PYSNMP_MODULE_ID=entitySensorMIB, entPhySensorScale=entPhySensorScale, EntitySensorDataScale=EntitySensorDataScale, EntitySensorValue=EntitySensorValue, entPhySensorUnitsDisplay=entPhySensorUnitsDisplay, entitySensorGroups=entitySensorGroups, entPhySensorOperStatus=entPhySensorOperStatus, entPhySensorValue=entPhySensorValue, EntitySensorStatus=EntitySensorStatus, entPhySensorPrecision=entPhySensorPrecision, entPhySensorType=entPhySensorType, entitySensorConformance=entitySensorConformance, EntitySensorDataType=EntitySensorDataType, entPhySensorValueTimeStamp=entPhySensorValueTimeStamp, entitySensorCompliance=entitySensorCompliance, entPhySensorValueUpdateRate=entPhySensorValueUpdateRate, entitySensorCompliances=entitySensorCompliances, entPhySensorTable=entPhySensorTable, entitySensorMIB=entitySensorMIB, EntitySensorPrecision=EntitySensorPrecision, entPhySensorEntry=entPhySensorEntry, entitySensorObjects=entitySensorObjects)
