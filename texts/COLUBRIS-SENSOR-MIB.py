#
# PySNMP MIB module COLUBRIS-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SENSOR-MIB.my
# Produced by pysmi-1.1.12 at Tue Dec  3 10:56:36 2024
# On host fv-az1117-982 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, TimeTicks, Counter64, Unsigned32, iso, ModuleIdentity, NotificationType, Gauge32, IpAddress, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "TimeTicks", "Counter64", "Unsigned32", "iso", "ModuleIdentity", "NotificationType", "Gauge32", "IpAddress", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisSensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 31))
if mibBuilder.loadTexts: colubrisSensorMIB.setLastUpdated('200606010000Z')
if mibBuilder.loadTexts: colubrisSensorMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisSensorMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisSensorMIB.setDescription('Colubris Sensor MIB.')
colubrisSensorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 31, 1))
coSensorStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1))
coSensorOperState = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coSensorOperState.setStatus('current')
if mibBuilder.loadTexts: coSensorOperState.setDescription('Indicates if at least one radio on the access point is\n                 currently in sensor mode.')
coSensorConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("shared", 1), ("dedicated", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coSensorConfigMode.setStatus('current')
if mibBuilder.loadTexts: coSensorConfigMode.setDescription('Indicates if the sensor uses one radio (shared) or both radios (dedicated).')
coSensorOperMode = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("unknown", 1), ("workingNormally", 2), ("troubleshootingBG", 3), ("intrusionPreventionBG", 4), ("troubleshootingA", 5), ("troubleshootingABG", 6), ("troubleshootingAIntrusionPreventionBG", 7), ("intrusionPreventionA", 8), ("intrusionPreventionATroubleshootingBG", 9), ("intrusionPreventionABG", 10), ("upgradingSoftware", 11), ("noEthernetLink", 12), ("noIpAddress", 13), ("noRfManagerServer", 14), ("notActiveOrStarting", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coSensorOperMode.setStatus('current')
if mibBuilder.loadTexts: coSensorOperMode.setDescription('Indicates the current operational mode of the sensor.')
colubrisSensorMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 31, 2))
colubrisSensorMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 1))
colubrisSensorMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 2))
colubrisSensorMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 1, 1)).setObjects(("COLUBRIS-SENSOR-MIB", "colubrisSensorStatusMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSensorMIBCompliance = colubrisSensorMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisSensorMIBCompliance.setDescription('The compliance statement for the Sensor MIB.')
colubrisSensorStatusMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 2, 1)).setObjects(("COLUBRIS-SENSOR-MIB", "coSensorOperState"), ("COLUBRIS-SENSOR-MIB", "coSensorConfigMode"), ("COLUBRIS-SENSOR-MIB", "coSensorOperMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSensorStatusMIBGroup = colubrisSensorStatusMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisSensorStatusMIBGroup.setDescription('A collection of objects for Sensor status.')
mibBuilder.exportSymbols("COLUBRIS-SENSOR-MIB", colubrisSensorMIBCompliances=colubrisSensorMIBCompliances, colubrisSensorMIBGroups=colubrisSensorMIBGroups, colubrisSensorMIB=colubrisSensorMIB, coSensorOperState=coSensorOperState, colubrisSensorMIBObjects=colubrisSensorMIBObjects, colubrisSensorMIBCompliance=colubrisSensorMIBCompliance, colubrisSensorMIBConformance=colubrisSensorMIBConformance, coSensorConfigMode=coSensorConfigMode, colubrisSensorStatusMIBGroup=colubrisSensorStatusMIBGroup, coSensorStatusGroup=coSensorStatusGroup, coSensorOperMode=coSensorOperMode, PYSNMP_MODULE_ID=colubrisSensorMIB)
