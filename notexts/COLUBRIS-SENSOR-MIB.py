#
# PySNMP MIB module COLUBRIS-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SENSOR-MIB.my
# Produced by pysmi-1.1.8 at Tue Jul 26 16:17:29 2022
# On host fv-az377-45 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, IpAddress, Counter32, NotificationType, TimeTicks, Unsigned32, MibIdentifier, Bits, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Counter32", "NotificationType", "TimeTicks", "Unsigned32", "MibIdentifier", "Bits", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ObjectIdentity")
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
mibBuilder.exportSymbols("COLUBRIS-SENSOR-MIB", colubrisSensorMIBCompliances=colubrisSensorMIBCompliances, colubrisSensorMIB=colubrisSensorMIB, coSensorOperState=coSensorOperState, coSensorOperMode=coSensorOperMode, coSensorConfigMode=coSensorConfigMode, colubrisSensorMIBCompliance=colubrisSensorMIBCompliance, PYSNMP_MODULE_ID=colubrisSensorMIB, colubrisSensorMIBObjects=colubrisSensorMIBObjects, colubrisSensorStatusMIBGroup=colubrisSensorStatusMIBGroup, colubrisSensorMIBGroups=colubrisSensorMIBGroups, colubrisSensorMIBConformance=colubrisSensorMIBConformance, coSensorStatusGroup=coSensorStatusGroup)
