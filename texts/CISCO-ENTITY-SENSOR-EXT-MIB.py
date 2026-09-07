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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setLastUpdated('2010-06-10 00:00')
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setContactInfo('Postal: Cisco Systems, Inc.\n            170 West Tasman Drive\n            San Jose, CA 95134-1706\n            USA\n\n            Tel: +1 408 526 4000\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntitySensorExtMIB.setDescription('This MIB is extension to ENTITY-SENSOR-MIB(RFC 3433). This MIB\n        also defines the notifications applicable for sensors reported\n        in ENTITY-MIB(RFC 4133).')
ciscoEntitySensorExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 0))
ciscoEntitySensorExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 1))
ciscoEntitySensorExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2))
class CiscoSensorThresholdSeverity(TextualConvention, Integer32):
    description = 'sensor threshold severity.  Valid values are:\n\n        other(1)    : a severity other than those listed below.\n        minor(10)   : Minor Problem threshold.\n        major(20)   : Major Problem threshold.\n        critical(30): Critical problem threshold. A system might shut\n                      down the sensor associated FRU automatically if\n                      the sensor value reach the critical problem\n                      threshold.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30))
    namedValues = NamedValues(("other", 1), ("minor", 10), ("major", 20), ("critical", 30))

class CiscoSensorThresholdRelation(TextualConvention, Integer32):
    description = 'sensor threshold relational operator types.  valid values are:\n\n        lessThan(1):        if the sensor value is less than\n                            the threshold value\n        lessOrEqual(2):     if the sensor value is less than or equal to\n                            the threshold value\n        greaterThan(3):     if the sensor value is greater than \n                            the threshold value\n        greaterOrEqual(4):  if the sensor value is greater than or equal\n                            to the threshold value\n        equalTo(5):         if the sensor value is equal to\n                            the threshold value\n        notEqualTo(6):      if the sensor value is not equal to\n                            the threshold value'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("lessThan", 1), ("lessOrEqual", 2), ("greaterThan", 3), ("greaterOrEqual", 4), ("equalTo", 5), ("notEqualTo", 6))

ceSensorExtThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceSensorExtThresholdTable.setReference('ENTITY-MIB contains definition for entPhysicalTable')
if mibBuilder.loadTexts: ceSensorExtThresholdTable.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdTable.setDescription('This table lists the threshold severity, relation, and\n        comparison value, for a sensor entity listed in  \n        entPhysicalTable.')
ceSensorExtThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdIndex"))
if mibBuilder.loadTexts: ceSensorExtThresholdEntry.setReference('ENTITY-MIB contains definition for entPhysicalClass')
if mibBuilder.loadTexts: ceSensorExtThresholdEntry.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdEntry.setDescription("An ceSensorExtThresholdTable entry describes the\n        thresholds for a sensor: the threshold severity,\n        the threshold value, the relation, and the \n        evaluation of the threshold.\n\n        Only entities with entPhysicalClass 'sensor' \n        are listed in this table.\n\n        For non FRU entities the entries are created by the agent at\n        system startup and entries are never deleted by the agent.\n\n        For FRU entities the entries are created at system startup \n        if FRU is inserted at system startup, else entries are created \n        when FRU is inserted.  Entries are deleted by the agent when\n        FRU is removed.")
ceSensorExtThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceSensorExtThresholdIndex.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdIndex.setDescription('An index that uniquely identifies an entry\n        in the ceSensorExtThresholdTable. This index\n        permits the same sensor to have several \n        different thresholds.')
ceSensorExtThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 2), CiscoSensorThresholdSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdSeverity.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdSeverity.setDescription('This object specifies the severity of this threshold.')
ceSensorExtThresholdRelation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 3), CiscoSensorThresholdRelation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdRelation.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdRelation.setDescription("This object specifies the boolean relation between\n        sensor value (entPhySensorValue) and threshold value \n        (ceSensorExtThresholdValue), required to \n        trigger the alarm.  \n\n        in pseudo-code, the evaluation-alarm mechanism is:\n\n        ...\n        if (evaluate(entPhySensorValue, \n                     ceSensorExtThresholdRelation,\n                     ceSensorExtThresholdValue)) \n        then\n            if (((ceSensorExtThresholdNotifEnable \n                    == enabled) || \n                  (ceSensorExtThresholdNotifEnable\n                    == transparent)) &&\n                  (ceSensorExtThresholdNotifGlobalEnable \n                    == enabled)) \n            then\n                raise_alarm(sensor's entPhysicalIndex);\n               endif\n        endif\n        ...")
ceSensorExtThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 4), EntitySensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdValue.setReference('ENTITY-SENSOR-MIB contains definitions for \n          entPhysSensorScale and entPhySensorPrecision')
if mibBuilder.loadTexts: ceSensorExtThresholdValue.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdValue.setDescription('This object specifies the value of the threshold.\n\n        The value of objects entPhySensorType, entPhysSensorScale \n        and entPhySensorPrecision for this sensor entity defines\n        how ceSensorExtThresholdValue can be displayed or\n        intepreted by the user.\n\n        entPhySensorValue can be compared with\n        ceSensorExtThresholdValue without taking\n        care of semantics of both objects.')
ceSensorExtThresholdEvaluation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceSensorExtThresholdEvaluation.setReference('ENTITY-SENSOR-MIB contains definition for \n        entPhySensorValueUpdateRate')
if mibBuilder.loadTexts: ceSensorExtThresholdEvaluation.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdEvaluation.setDescription("This object indicates the result of the most\n        recent evaluation of the threshold.  \n\n        The agent will execute the below 'evaluate' function\n        to generate the notification. 'evaluate' function\n        returns a boolean value.\n\n        evaluate(entPhySensorValue, \n                 ceSensorExtThresholdRelation,\n                 ceSensorExtThresholdValue)\n\n        If evalute function returns true then \n        ceSensorExtThresholdEvaluation is set to 'true'\n\n        If evaluate function returns false then  \n        ceSensorExtThresholdEvaluation is set to 'false'.\n\n        Thresholds are evaluated at the rate indicated by \n        entPhySensorValueUpdateRate.")
ceSensorExtThresholdNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("transparent", 3))).clone('transparent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdNotifEnable.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdNotifEnable.setDescription("A control object to activate/deactivate\n        ceSensorExtThresholdNotification.\n\n        This object should hold any of the below values.\n        enabled(1)    - The notification is enabled for this entity\n        disabled(2)   - The notification is disabled for this entity\n        transparent(3)- The notification is enabled/disabled based on\n                        ceSensorExtThresholdNotifGlobalEnable\n                        object\n\n        This object controls generation of\n        ceSensorExtThresholdNotification for this threshold.\n        An exception to this is, if this object is set to 'transparent'\n        then ceSensorExtThresholdNotification for this threshold\n        is controlled by ceSensorExtThresholdNotifGlobalEnable\n        object.\n\n        This truth table explains how\n        ceSensorExtThresholdNotifEnable is related with \n        ceSensorExtThresholdNotifGlobalEnable to control the\n        ceSensorExtThresholdNotification for this threshold\n\n        E = enabled, D = Disabled, T = Transparent\n        local_flag =  ceSensorExtThresholdNotifEnable\n        global_flag = ceSensorExtThresholdNotifGlobalEnable\n\n        local_flag  global_flag   outcome_per_interface\n        ---------------------------------------------\n           E            E            E\n           E            D            D\n           D            E            D\n           D            D            D\n           T            E            E\n           T            D            D")
ciscoEntSensorExtGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 2))
ceSensorExtThresholdNotifGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 745, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceSensorExtThresholdNotifGlobalEnable.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdNotifGlobalEnable.setDescription("A control object to activate/deactivate\n        ceSensorExtThresholdNotification.\n\n        This object should hold any of the below values.\n        enabled(1) - The notification is enabled globally \n                     on the device\n        disabled(2)- The notification is disabled globally \n                     on the device  \n\n        This object enables the generation of\n        ceSensorExtThresholdNotification globally\n        on the device. If this object value is\n        'disabled', then no ceSensorExtThresholdNotification\n        will be generated on this device. If this object\n        value is 'enabled', then whether a \n        ceSensorExtThresholdNotification for a threshold will\n        be generated or not depends on the instance value of\n        ceSensorExtThresholdNotifEnable for that\n        threshold.")
ceSensorExtThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 745, 0, 1)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("ENTITY-SENSOR-MIB", "entPhySensorType"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdValue"))
if mibBuilder.loadTexts: ceSensorExtThresholdNotification.setStatus('current')
if mibBuilder.loadTexts: ceSensorExtThresholdNotification.setDescription('This notification is generated once each time\n        the sensor value crosses the threshold value\n        specified by ceSensorExtThresholdValue object.')
ciscoEntSensorExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 1))
ciscoEntSensorExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2))
ciscoEntSensorExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 1, 1)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtThresholdGroup"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtNotificationCtrlGroup"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ciscoEntSensorExtNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtMIBCompliance = ciscoEntSensorExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoEntSensorExtMIBCompliance.setDescription('An ENTITY-MIB implementation that adds notification\n        for sensors in the entPhysicalTable must implement\n        this group.')
ciscoEntSensorExtThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 1)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdSeverity"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdRelation"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdValue"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdEvaluation"), ("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtThresholdGroup = ciscoEntSensorExtThresholdGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoEntSensorExtThresholdGroup.setDescription('The collection of objects which are used\n        to describe and monitor thresholds for\n        sensors.')
ciscoEntSensorExtNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 2)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtNotificationGroup = ciscoEntSensorExtNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoEntSensorExtNotificationGroup.setDescription('The collection of notifications used for\n        monitoring sensor threshold activity.')
ciscoEntSensorExtNotificationCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 745, 2, 2, 3)).setObjects(("CISCO-ENTITY-SENSOR-EXT-MIB", "ceSensorExtThresholdNotifGlobalEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntSensorExtNotificationCtrlGroup = ciscoEntSensorExtNotificationCtrlGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoEntSensorExtNotificationCtrlGroup.setDescription('The collection of objects which provide the global\n        notification control on \n        ceSensorExtThresholdNotification.')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-EXT-MIB", CiscoSensorThresholdRelation=CiscoSensorThresholdRelation, CiscoSensorThresholdSeverity=CiscoSensorThresholdSeverity, PYSNMP_MODULE_ID=ciscoEntitySensorExtMIB, ceSensorExtThresholdEntry=ceSensorExtThresholdEntry, ceSensorExtThresholdEvaluation=ceSensorExtThresholdEvaluation, ceSensorExtThresholdIndex=ceSensorExtThresholdIndex, ceSensorExtThresholdNotifEnable=ceSensorExtThresholdNotifEnable, ceSensorExtThresholdNotifGlobalEnable=ceSensorExtThresholdNotifGlobalEnable, ceSensorExtThresholdNotification=ceSensorExtThresholdNotification, ceSensorExtThresholdRelation=ceSensorExtThresholdRelation, ceSensorExtThresholdSeverity=ceSensorExtThresholdSeverity, ceSensorExtThresholdTable=ceSensorExtThresholdTable, ceSensorExtThresholdValue=ceSensorExtThresholdValue, ciscoEntSensorExtGlobalObjects=ciscoEntSensorExtGlobalObjects, ciscoEntSensorExtMIBCompliance=ciscoEntSensorExtMIBCompliance, ciscoEntSensorExtMIBCompliances=ciscoEntSensorExtMIBCompliances, ciscoEntSensorExtMIBGroups=ciscoEntSensorExtMIBGroups, ciscoEntSensorExtNotificationCtrlGroup=ciscoEntSensorExtNotificationCtrlGroup, ciscoEntSensorExtNotificationGroup=ciscoEntSensorExtNotificationGroup, ciscoEntSensorExtThresholdGroup=ciscoEntSensorExtThresholdGroup, ciscoEntitySensorExtMIB=ciscoEntitySensorExtMIB, ciscoEntitySensorExtMIBConform=ciscoEntitySensorExtMIBConform, ciscoEntitySensorExtMIBNotifs=ciscoEntitySensorExtMIBNotifs, ciscoEntitySensorExtMIBObjects=ciscoEntitySensorExtMIBObjects)
