#
# PySNMP MIB module COLUBRIS-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SENSOR-MIB.my
# Produced by pysmi-1.1.12 at Tue May 28 12:49:28 2024
# On host fv-az847-244 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter64, Gauge32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Bits, NotificationType, Integer32, Counter32, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "Gauge32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Bits", "NotificationType", "Integer32", "Counter32", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisSensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 31))
if mibBuilder.loadTexts: colubrisSensorMIB.setLastUpdated('200606010000Z')
if mibBuilder.loadTexts: colubrisSensorMIB.setOrganization('Colubris Networks, Inc.')
colubrisSensorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 31, 1))
coSensorStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1))
coSensorOperState = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coSensorOperState.setStatus('current')
coSensorConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("shared", 1), ("dedicated", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coSensorConfigMode.setStatus('current')
coSensorOperMode = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 31, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("unknown", 1), ("workingNormally", 2), ("troubleshootingBG", 3), ("intrusionPreventionBG", 4), ("troubleshootingA", 5), ("troubleshootingABG", 6), ("troubleshootingAIntrusionPreventionBG", 7), ("intrusionPreventionA", 8), ("intrusionPreventionATroubleshootingBG", 9), ("intrusionPreventionABG", 10), ("upgradingSoftware", 11), ("noEthernetLink", 12), ("noIpAddress", 13), ("noRfManagerServer", 14), ("notActiveOrStarting", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coSensorOperMode.setStatus('current')
colubrisSensorMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 31, 2))
colubrisSensorMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 1))
colubrisSensorMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 2))
colubrisSensorMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 1, 1)).setObjects(("COLUBRIS-SENSOR-MIB", "colubrisSensorStatusMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSensorMIBCompliance = colubrisSensorMIBCompliance.setStatus('current')
colubrisSensorStatusMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 31, 2, 2, 1)).setObjects(("COLUBRIS-SENSOR-MIB", "coSensorOperState"), ("COLUBRIS-SENSOR-MIB", "coSensorConfigMode"), ("COLUBRIS-SENSOR-MIB", "coSensorOperMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSensorStatusMIBGroup = colubrisSensorStatusMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-SENSOR-MIB", colubrisSensorMIB=colubrisSensorMIB, coSensorOperState=coSensorOperState, colubrisSensorStatusMIBGroup=colubrisSensorStatusMIBGroup, colubrisSensorMIBCompliance=colubrisSensorMIBCompliance, colubrisSensorMIBConformance=colubrisSensorMIBConformance, coSensorOperMode=coSensorOperMode, coSensorStatusGroup=coSensorStatusGroup, colubrisSensorMIBObjects=colubrisSensorMIBObjects, colubrisSensorMIBGroups=colubrisSensorMIBGroups, colubrisSensorMIBCompliances=colubrisSensorMIBCompliances, PYSNMP_MODULE_ID=colubrisSensorMIB, coSensorConfigMode=coSensorConfigMode)
