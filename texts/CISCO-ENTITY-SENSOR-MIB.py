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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: entitySensorMIB.setRevisionsDescriptions(('Changed exa(10^18), peta(10^15) values of \n\t\t\t sensorDataScale in comments.', '[1] Add critical(30) in CSensorThresholdSeverity.\n             [2] Change to MAX-ACCESS read-write for 3 objects.\n             [3] Add entitySensorMIBComplianceV02.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: entitySensorMIB.setLastUpdated('2020-09-22 00:00')
if mibBuilder.loadTexts: entitySensorMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: entitySensorMIB.setContactInfo('Postal: Cisco Systems, Inc.\n             170 West Tasman Drive\n             San Jose, CA 95134-1706\n             USA\n\n             Tel: +1 408 526 4000\n\n             E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: entitySensorMIB.setDescription('The CISCO-ENTITY-SENSOR-MIB is used to monitor \n            the values of sensors in the Entity-MIB (RFC 2037) \n            entPhysicalTable.')
entitySensorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1))
entitySensorMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 2))
entitySensorMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3))
class SensorDataType(TextualConvention, Integer32):
    description = 'sensor measurement data types.  valid values are:\n        other(1):        a measure other than those listed below\n        unknown(2):      unknown measurement, or \n                         arbitrary, relative numbers    \n        voltsAC(3):      electric potential\n        voltsDC(4):      electric potential\n        amperes(5):      electric current\n        watts(6):        power\n        hertz(7):        frequency\n        celsius(8):      temperature\n        percentRH(9):    percent relative humidity\n        rpm(10):         shaft revolutions per minute\n        cmm(11),:        cubic meters per minute (airflow)\n        truthvalue(12):  value takes { true(1), false(2) }\n        specialEnum(13): value takes user defined enumerated values\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("voltsAC", 3), ("voltsDC", 4), ("amperes", 5), ("watts", 6), ("hertz", 7), ("celsius", 8), ("percentRH", 9), ("rpm", 10), ("cmm", 11), ("truthvalue", 12), ("specialEnum", 13))

class SensorDataScale(TextualConvention, Integer32):
    description = 'International System of Units (SI) prefixes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class SensorPrecision(TextualConvention, Integer32):
    description = "When in the range 1 to 9, SensorPrecision is the number \n        of decimal places in the fractional part of \n        a SensorValue fixed-point number.  When in the range -8 to\n        -1, SensorPrecision is the number of accurate digits in \n        a SensorValue fixed-point number.\n\n        SensorPrecision is 0 for non-fixed-point numbers.\n\n        Agent implementors must choose a value for SensorPrecision \n        so that the precision and accuracy of a SensorValue is \n        correctly indicated.\n\n        For example, a temperature sensor that can measure 0o to \n        100o C in 0.1o increments, +/- 0.05o, would have a \n        SensorPrecision of 1, a SensorDataScale of units(0), and a \n        SensorValue ranging from 0 to 1000.  \n        The SensorValue would be interpreted as (degrees C * 10).\n\n        If that temperature sensor's precision were 0.1o but its \n        accuracy were only +/- 0.5o, then the SensorPrecision would \n        be 0. The SensorValue would be interpreted as degrees C.\n\n        Another example: a fan rotation speed sensor that measures RPM \n        from 0 to 10,000 in 100 RPM increments, with an accuracy of \n        +50/-37 RPM, would have a SensorPrecision of -2, a \n        SensorDataScale of units(9), and a SensorValue ranging from 0 \n        to 10000. The 10s and 1s digits of SensorValue would always \n        be 0.\n        "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-8, 9)

class SensorValue(TextualConvention, Integer32):
    description = 'For sensors that measure voltsAC, voltsDC, \n        amperes, watts, hertz, celsius, cmm\n        this item is a fixed point number ranging from \n        -999,999,999 to +999,999,999.  Use the value \n        -1000000000 to indicate underflow. Use the value \n        +1000000000 to indicate overflow.  Use SensorPrecision\n        to indicate how many fractional digits the SensorValue\n        has.\n\n\n        For sensors that measure percentRH, this item\n        is a number ranging from 0 to 100.\n\n        For sensors that measure rpm, this item\n        can take only nonnegative values, 0..999999999.\n\n        For sensors of type truthvalue, this item \n        can take only two values: true(1), false(2).\n\n        For sensors of type specialEnum, this item\n        can take any value in the range (-1000000000..1000000000),\n        but the meaning of each value is specific to the \n        sensor.\n\n        For sensors of type other and unknown, \n        this item can take any value in the range \n        (-1000000000..1000000000), but the meaning of the values \n        are specific to the sensor.\n\n        Use Entity-MIB entPhysicalTable.entPhysicalVendorType\n        to learn about the sensor type.\n    '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class SensorStatus(TextualConvention, Integer32):
    description = 'Indicates the operational status of the sensor.\n\n        ok(1) means the agent can read the sensor \n        value.\n\n        unavailable(2) means that the agent presently \n        can not report the sensor value.\n\n        nonoperational(3) means that the agent believes\n        the sensor is broken.  The sensor could have a \n        hard failure (disconnected wire), or a soft failure\n        such as out-of-range, jittery, or wildly fluctuating\n        readings.\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3))

class SensorValueUpdateRate(TextualConvention, Integer32):
    description = "Indicates the interval in seconds between updates to the\n        sensor's value.  \n\n        The value zero indicates:\n        - the sensor value is updated on demand (when polled by the \n          agent for a get-request), \n        - or when the sensor value changes (event-driven), \n        - or the agent does not know the rate\n\n        "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 999999999)

class SensorThresholdSeverity(TextualConvention, Integer32):
    description = 'sensor threshold severity.  Valid values are:\n\n        other(1)    : a severity other than those listed below.\n        minor(10)   : Minor Problem threshold.\n        major(20)   : Major Problem threshold.\n        critical(30): Critical problem threshold. A system might shut\n                      down the sensor associated FRU automatically if\n                      the sensor value reach the critical problem\n                      threshold.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30))
    namedValues = NamedValues(("other", 1), ("minor", 10), ("major", 20), ("critical", 30))

class SensorThresholdRelation(TextualConvention, Integer32):
    description = 'sensor threshold relational operator types.  valid values are:\n\n        lessThan(1):        if the sensor value is less than\n                            the threshold value\n        lessOrEqual(2):     if the sensor value is less than or equal to\n                            the threshold value\n        greaterThan(3):     if the sensor value is greater than \n                            the threshold value\n        greaterOrEqual(4):  if the sensor value is greater than or equal to \n                            the threshold value\n        equalTo(5):         if the sensor value is equal to\n                            the threshold value\n        notEqualTo(6):      if the sensor value is not equal to\n                            the threshold value\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("lessThan", 1), ("lessOrEqual", 2), ("greaterThan", 3), ("greaterOrEqual", 4), ("equalTo", 5), ("notEqualTo", 6))

entSensorValues = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1))
entSensorThresholds = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2))
entSensorValueTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entSensorValueTable.setStatus('current')
if mibBuilder.loadTexts: entSensorValueTable.setDescription('This table lists the type, scale, and present value\n        of a sensor listed in the Entity-MIB entPhysicalTable.')
entSensorValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entSensorValueEntry.setStatus('current')
if mibBuilder.loadTexts: entSensorValueEntry.setDescription('An entSensorValueTable entry describes the \n        present reading of a sensor, the measurement units\n        and scale, and sensor operational status.')
entSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 1), SensorDataType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorType.setStatus('current')
if mibBuilder.loadTexts: entSensorType.setDescription('This variable indicates the type of data \n        reported by the entSensorValue.\n\n        This variable is set by the agent at start-up\n        and the value does not change during operation.')
entSensorScale = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 2), SensorDataScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorScale.setStatus('current')
if mibBuilder.loadTexts: entSensorScale.setDescription('This variable indicates the exponent to apply\n        to sensor values reported by entSensorValue.\n\n        This variable is set by the agent at start-up\n        and the value does not change during operation.')
entSensorPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 3), SensorPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorPrecision.setStatus('current')
if mibBuilder.loadTexts: entSensorPrecision.setDescription('This variable indicates the number of decimal\n        places of precision in fixed-point\n        sensor values reported by entSensorValue.\n\n        This variable is set to 0 when entSensorType\n        is not a fixed-point type:  voltsAC(1), voltsDC(2), \n        amperes(3), watts(4), hertz(5), celsius(6), or cmm(9).\n\n        This variable is set by the agent at start-up\n        and the value does not change during operation.')
entSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 4), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValue.setStatus('current')
if mibBuilder.loadTexts: entSensorValue.setDescription("This variable reports the most recent measurement seen\n        by the sensor.\n\n        To correctly display or interpret this variable's value, \n        you must also know entSensorType, entSensorScale, and \n        entSensorPrecision.\n\n        However, you can compare entSensorValue with the threshold\n        values given in entSensorThresholdTable without any semantic\n        knowledge.\n        ")
entSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 5), SensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorStatus.setStatus('current')
if mibBuilder.loadTexts: entSensorStatus.setDescription('This variable indicates the present operational status\n        of the sensor.')
entSensorValueTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValueTimeStamp.setStatus('current')
if mibBuilder.loadTexts: entSensorValueTimeStamp.setDescription('This variable indicates the age of the value reported by \n        entSensorValue')
entSensorValueUpdateRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 7), SensorValueUpdateRate()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorValueUpdateRate.setStatus('current')
if mibBuilder.loadTexts: entSensorValueUpdateRate.setDescription('This variable indicates the rate that the agent\n        updates entSensorValue.')
entSensorMeasuredEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorMeasuredEntity.setStatus('current')
if mibBuilder.loadTexts: entSensorMeasuredEntity.setDescription('This object identifies the physical entity for which the\n        sensor is taking measurements.  For example, for a sensor\n        measuring the voltage output of a power-supply, this object\n        would be the entPhysicalIndex of that power-supply; for a sensor\n        measuring the temperature inside one chassis of a multi-chassis\n        system, this object would be the enPhysicalIndex of that\n        chassis.\n\n        This object has a value of zero when the physical entity\n        for which the sensor is taking measurements can not be\n        represented by any one row in the entPhysicalTable, or that\n        there is no such physical entity.')
entSensorThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entSensorThresholdTable.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdTable.setDescription('This table lists the threshold severity, relation, and\n        comparison value, for a sensor listed in the Entity-MIB \n        entPhysicalTable.')
entSensorThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdIndex"))
if mibBuilder.loadTexts: entSensorThresholdEntry.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdEntry.setDescription('An entSensorThresholdTable entry describes the \n         thresholds for a sensor: the threshold severity,\n         the threshold value, the relation, and the \n         evaluation of the threshold.\n\n         Only entities of type sensor(8) are listed in this table.\n         Only pre-configured thresholds are listed in this table.\n\n         Users can create sensor-value monitoring instruments\n         in different ways, such as RMON alarms, Expression-MIB, etc.\n\n         Entries are created by the agent at system startup and\n         FRU insertion.  Entries are deleted by the agent at\n         FRU removal.')
entSensorThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99999999))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entSensorThresholdIndex.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdIndex.setDescription('An index that uniquely identifies an entry\n        in the entSensorThreshold table. This index\n        permits the same sensor to have several \n        different thresholds.')
entSensorThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 2), SensorThresholdSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdSeverity.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdSeverity.setDescription('This variable indicates the severity of this threshold.')
entSensorThresholdRelation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 3), SensorThresholdRelation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdRelation.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdRelation.setDescription('This variable indicates the relation between sensor value \n        (entSensorValue) and threshold value (entSensorThresholdValue), \n        required to trigger the alarm.  when evaluating the relation, \n        entSensorValue is on the left of entSensorThresholdRelation, \n        entSensorThresholdValue is on the right. \n\n        in pseudo-code, the evaluation-alarm mechanism is:\n \n        ...\n        if (entSensorStatus == ok) then\n            if (evaluate(entSensorValue, entSensorThresholdRelation,  \n                entSensorThresholdValue)) \n            then\n                if (entSensorThresholdNotificationEnable == true)) \n                then\n                    raise_alarm(entSensorThresholdAlarmOID);\n                endif\n            endif\n        endif\n        ...\n        ')
entSensorThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 4), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdValue.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdValue.setDescription("This variable indicates the value of the threshold.\n\n        To correctly display or interpret this variable's value, \n        you must also know entSensorType, entSensorScale, and \n        entSensorPrecision.\n\n        However, you can directly compare entSensorValue \n        with the threshold values given in entSensorThresholdTable \n        without any semantic knowledge.\n        ")
entSensorThresholdEvaluation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entSensorThresholdEvaluation.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdEvaluation.setDescription('This variable indicates the result of the most\n        recent evaluation of the threshold.  If the threshold\n        condition is true, entSensorThresholdEvaluation \n        is true(1).  If the threshold condition is false, \n        entSensorThresholdEvaluation is false(2).\n\n        Thresholds are evaluated at the rate indicated by \n        entSensorValueUpdateRate.        \n        ')
entSensorThresholdNotificationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entSensorThresholdNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdNotificationEnable.setDescription('This variable controls generation of \n        entSensorThresholdNotification for this threshold.\n\n        When this variable is true(1), generation of \n        entSensorThresholdNotification is enabled.  When this\n        variable is false(2), generation of \n        entSensorThresholdNotification is disabled.\n\n        This variable only controls generation of \n        entSensorThresholdNotification.\n        ')
entitySensorMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0))
entSensorThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"))
if mibBuilder.loadTexts: entSensorThresholdNotification.setStatus('current')
if mibBuilder.loadTexts: entSensorThresholdNotification.setDescription('The sensor value crossed the threshold \n        listed in entSensorThresholdTable.\n\n        This notification is generated once each time\n        the sensor value crosses the threshold.\n        \n        The agent implementation guarantees prompt, timely\n        evaluation of threshold and generation of this\n        notification.\n        ')
entitySensorMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1))
entitySensorMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2))
entitySensorMIBComplianceV01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV01 = entitySensorMIBComplianceV01.setStatus('deprecated')
if mibBuilder.loadTexts: entitySensorMIBComplianceV01.setDescription('An Entity-MIB implementation that lists\n        sensors in its entPhysicalTable must implement\n        this group.')
entitySensorMIBComplianceV02 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 2)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorMIBComplianceV02 = entitySensorMIBComplianceV02.setStatus('current')
if mibBuilder.loadTexts: entitySensorMIBComplianceV02.setDescription('An Entity-MIB implementation that lists \n        sensors in its entPhysicalTable must implement\n        this group.')
entitySensorValueGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 1)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorType"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorScale"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorPrecision"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorStatus"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValueTimeStamp"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorValueUpdateRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorValueGroup = entitySensorValueGroup.setStatus('current')
if mibBuilder.loadTexts: entitySensorValueGroup.setDescription('The collection of objects which are used\n        to describe and monitor values of Entity-MIB \n        entPhysicalTable entries of sensors.\n        ')
entitySensorThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 2)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdSeverity"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdRelation"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdEvaluation"), ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorThresholdGroup = entitySensorThresholdGroup.setStatus('current')
if mibBuilder.loadTexts: entitySensorThresholdGroup.setDescription('The collection of objects which are used\n        to describe and monitor thresholds for\n        sensors.')
entitySensorThresholdNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 3)).setObjects(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorThresholdNotificationGroup = entitySensorThresholdNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: entitySensorThresholdNotificationGroup.setDescription('the collection of notifications used for\n       monitoring sensor threshold activity.')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-MIB", PYSNMP_MODULE_ID=entitySensorMIB, SensorDataScale=SensorDataScale, SensorDataType=SensorDataType, SensorPrecision=SensorPrecision, SensorStatus=SensorStatus, SensorThresholdRelation=SensorThresholdRelation, SensorThresholdSeverity=SensorThresholdSeverity, SensorValue=SensorValue, SensorValueUpdateRate=SensorValueUpdateRate, entSensorMeasuredEntity=entSensorMeasuredEntity, entSensorPrecision=entSensorPrecision, entSensorScale=entSensorScale, entSensorStatus=entSensorStatus, entSensorThresholdEntry=entSensorThresholdEntry, entSensorThresholdEvaluation=entSensorThresholdEvaluation, entSensorThresholdIndex=entSensorThresholdIndex, entSensorThresholdNotification=entSensorThresholdNotification, entSensorThresholdNotificationEnable=entSensorThresholdNotificationEnable, entSensorThresholdRelation=entSensorThresholdRelation, entSensorThresholdSeverity=entSensorThresholdSeverity, entSensorThresholdTable=entSensorThresholdTable, entSensorThresholdValue=entSensorThresholdValue, entSensorThresholds=entSensorThresholds, entSensorType=entSensorType, entSensorValue=entSensorValue, entSensorValueEntry=entSensorValueEntry, entSensorValueTable=entSensorValueTable, entSensorValueTimeStamp=entSensorValueTimeStamp, entSensorValueUpdateRate=entSensorValueUpdateRate, entSensorValues=entSensorValues, entitySensorMIB=entitySensorMIB, entitySensorMIBComplianceV01=entitySensorMIBComplianceV01, entitySensorMIBComplianceV02=entitySensorMIBComplianceV02, entitySensorMIBCompliances=entitySensorMIBCompliances, entitySensorMIBConformance=entitySensorMIBConformance, entitySensorMIBGroups=entitySensorMIBGroups, entitySensorMIBNotificationPrefix=entitySensorMIBNotificationPrefix, entitySensorMIBNotifications=entitySensorMIBNotifications, entitySensorMIBObjects=entitySensorMIBObjects, entitySensorThresholdGroup=entitySensorThresholdGroup, entitySensorThresholdNotificationGroup=entitySensorThresholdNotificationGroup, entitySensorValueGroup=entitySensorValueGroup)
