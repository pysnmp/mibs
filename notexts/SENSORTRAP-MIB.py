#
# PySNMP MIB module SENSORTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source SENSORTRAP-MIB
# Source digest sha256:bd371723389080daed1165fc938666e3c1aab3764b0cbbb901a34bf90942996d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rielloMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 5491))
sensorgroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5491, 9))
sensor = MibIdentifier((1, 3, 6, 1, 4, 1, 5491, 9, 1))
sensorId = MibScalar((1, 3, 6, 1, 4, 1, 5491, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorId.setStatus('mandatory')
sensorTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2))
sensorAlarmTMax = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,1)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorAlarmTMaxRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,2)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorAlarmTMin = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,3)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorAlarmTMinRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,4)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorIOAlarm = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,5)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorIOAlarmRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,6)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorHumidityAlarm = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,7)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorHumidityAlarmRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,8)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorHumidityLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,9)).setObjects(("SENSORTRAP-MIB", "sensorId"))
sensorHumidityLowAlarmRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5491, 9, 1, 2) + (0,10)).setObjects(("SENSORTRAP-MIB", "sensorId"))
mibBuilder.exportSymbols("SENSORTRAP-MIB", rielloMIB=rielloMIB, sensor=sensor, sensorAlarmTMax=sensorAlarmTMax, sensorAlarmTMaxRemoved=sensorAlarmTMaxRemoved, sensorAlarmTMin=sensorAlarmTMin, sensorAlarmTMinRemoved=sensorAlarmTMinRemoved, sensorHumidityAlarm=sensorHumidityAlarm, sensorHumidityAlarmRemoved=sensorHumidityAlarmRemoved, sensorHumidityLowAlarm=sensorHumidityLowAlarm, sensorHumidityLowAlarmRemoved=sensorHumidityLowAlarmRemoved, sensorIOAlarm=sensorIOAlarm, sensorIOAlarmRemoved=sensorIOAlarmRemoved, sensorId=sensorId, sensorTrapGroup=sensorTrapGroup, sensorgroup=sensorgroup)
