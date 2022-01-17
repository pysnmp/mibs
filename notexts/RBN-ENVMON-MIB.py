#
# PySNMP MIB module RBN-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/RBN-ENVMON-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 18:26:07 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, ObjectIdentity, MibIdentifier, Counter32, iso, NotificationType, IpAddress, Unsigned32, Counter64, ModuleIdentity, TimeTicks, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "MibIdentifier", "Counter32", "iso", "NotificationType", "IpAddress", "Unsigned32", "Counter64", "ModuleIdentity", "TimeTicks", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rbnEnvMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 4))
rbnEnvMonMIB.setRevisions(('2012-10-03 00:00', '2011-01-19 18:00', '2010-11-11 00:00', '2006-01-16 00:00', '2002-06-05 00:00', '2001-07-25 00:00', '2000-04-24 00:00', '1999-03-10 00:00',))
if mibBuilder.loadTexts: rbnEnvMonMIB.setLastUpdated('201210030000Z')
if mibBuilder.loadTexts: rbnEnvMonMIB.setOrganization('Ericsson AB.')
rbnEnvMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 4, 0))
rbnEnvMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1))
rbnEnvMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2))
class RbnVoltage(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 50000)

class RbnTemperature(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

class RbnFanSpeed(TextualConvention, Unsigned32):
    status = 'current'

rbnFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1), )
if mibBuilder.loadTexts: rbnFanStatusTable.setStatus('current')
rbnFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1), ).setIndexNames((0, "RBN-ENVMON-MIB", "rbnFanIndex"))
if mibBuilder.loadTexts: rbnFanStatusEntry.setStatus('current')
rbnFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rbnFanIndex.setStatus('current')
rbnFanDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFanDescr.setStatus('current')
rbnFanFail = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFanFail.setStatus('deprecated')
rbnFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("failed", 2), ("absent", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFanStatus.setStatus('current')
rbnPowerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2), )
if mibBuilder.loadTexts: rbnPowerStatusTable.setStatus('current')
rbnPowerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1), ).setIndexNames((0, "RBN-ENVMON-MIB", "rbnPowerIndex"))
if mibBuilder.loadTexts: rbnPowerStatusEntry.setStatus('current')
rbnPowerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rbnPowerIndex.setStatus('current')
rbnPowerDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnPowerDescr.setStatus('current')
rbnPowerFail = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnPowerFail.setStatus('deprecated')
rbnPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal", 1), ("failed", 2), ("absent", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnPowerStatus.setStatus('current')
rbnVoltageSensorTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3), )
if mibBuilder.loadTexts: rbnVoltageSensorTable.setStatus('current')
rbnVoltageSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "RBN-ENVMON-MIB", "rbnVoltageIndex"))
if mibBuilder.loadTexts: rbnVoltageSensorEntry.setStatus('current')
rbnVoltageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rbnVoltageIndex.setStatus('current')
rbnVoltageDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnVoltageDescr.setStatus('current')
rbnVoltageDesired = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3, 1, 3), RbnVoltage()).setUnits('millivolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnVoltageDesired.setStatus('current')
rbnVoltageCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 3, 1, 4), RbnVoltage()).setUnits('millivolts').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnVoltageCurrent.setStatus('current')
rbnCpuTempSensorTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 4), )
if mibBuilder.loadTexts: rbnCpuTempSensorTable.setStatus('deprecated')
rbnCpuTempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "RBN-ENVMON-MIB", "rbnCpuTempIndex"))
if mibBuilder.loadTexts: rbnCpuTempSensorEntry.setStatus('deprecated')
rbnCpuTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rbnCpuTempIndex.setStatus('deprecated')
rbnCpuTempDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuTempDescr.setStatus('deprecated')
rbnCpuTempCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 4, 1, 3), RbnTemperature()).setUnits('degrees').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnCpuTempCurrent.setStatus('deprecated')
rbnFanSpeedTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 5), )
if mibBuilder.loadTexts: rbnFanSpeedTable.setStatus('current')
rbnFanSpeedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 5, 1), ).setIndexNames((0, "RBN-ENVMON-MIB", "rbnFanIndex"), (0, "RBN-ENVMON-MIB", "rbnFanUnitID"))
if mibBuilder.loadTexts: rbnFanSpeedEntry.setStatus('current')
rbnFanUnitID = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rbnFanUnitID.setStatus('current')
rbnFanUnitDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFanUnitDescr.setStatus('current')
rbnFanSpeedCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 5, 1, 3), RbnFanSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFanSpeedCurrent.setStatus('current')
rbnEntityTempSensorTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 6), )
if mibBuilder.loadTexts: rbnEntityTempSensorTable.setStatus('current')
rbnEntityTempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 6, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "RBN-ENVMON-MIB", "rbnEntityTempIndex"))
if mibBuilder.loadTexts: rbnEntityTempSensorEntry.setStatus('current')
rbnEntityTempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rbnEntityTempIndex.setStatus('current')
rbnEntityTempDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEntityTempDescr.setStatus('current')
rbnEntityTempCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 6, 1, 3), RbnTemperature()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnEntityTempCurrent.setStatus('current')
rbnFanFailChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 1)).setObjects(("RBN-ENVMON-MIB", "rbnFanFail"))
if mibBuilder.loadTexts: rbnFanFailChange.setStatus('deprecated')
rbnPowerFailChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 2)).setObjects(("RBN-ENVMON-MIB", "rbnPowerFail"))
if mibBuilder.loadTexts: rbnPowerFailChange.setStatus('deprecated')
rbnFanStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 3)).setObjects(("RBN-ENVMON-MIB", "rbnFanStatus"))
if mibBuilder.loadTexts: rbnFanStatusChange.setStatus('current')
rbnPowerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 4)).setObjects(("RBN-ENVMON-MIB", "rbnPowerStatus"))
if mibBuilder.loadTexts: rbnPowerStatusChange.setStatus('current')
rbnEnvMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1))
rbnEnvMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2))
rbnEnvMonMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 1)).setObjects(("RBN-ENVMON-MIB", "rbnFanDescr"), ("RBN-ENVMON-MIB", "rbnFanFail"), ("RBN-ENVMON-MIB", "rbnPowerDescr"), ("RBN-ENVMON-MIB", "rbnPowerFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBObjectGroup = rbnEnvMonMIBObjectGroup.setStatus('deprecated')
rbnEnvMonMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 2)).setObjects(("RBN-ENVMON-MIB", "rbnFanFailChange"), ("RBN-ENVMON-MIB", "rbnPowerFailChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBNotificationGroup = rbnEnvMonMIBNotificationGroup.setStatus('deprecated')
rbnEnvMonVoltageObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 3)).setObjects(("RBN-ENVMON-MIB", "rbnVoltageDescr"), ("RBN-ENVMON-MIB", "rbnVoltageDesired"), ("RBN-ENVMON-MIB", "rbnVoltageCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonVoltageObjectGroup = rbnEnvMonVoltageObjectGroup.setStatus('current')
rbnEnvMonTempObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 4)).setObjects(("RBN-ENVMON-MIB", "rbnCpuTempDescr"), ("RBN-ENVMON-MIB", "rbnCpuTempCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonTempObjectGroup = rbnEnvMonTempObjectGroup.setStatus('deprecated')
rbnEnvMonMIBObjectGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 5)).setObjects(("RBN-ENVMON-MIB", "rbnFanDescr"), ("RBN-ENVMON-MIB", "rbnFanStatus"), ("RBN-ENVMON-MIB", "rbnPowerDescr"), ("RBN-ENVMON-MIB", "rbnPowerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBObjectGroupV2 = rbnEnvMonMIBObjectGroupV2.setStatus('current')
rbnEnvMonMIBNotificationGroupV2 = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 6)).setObjects(("RBN-ENVMON-MIB", "rbnFanStatusChange"), ("RBN-ENVMON-MIB", "rbnPowerStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBNotificationGroupV2 = rbnEnvMonMIBNotificationGroupV2.setStatus('current')
rbnEnvMonFanSpeedObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 7)).setObjects(("RBN-ENVMON-MIB", "rbnFanUnitDescr"), ("RBN-ENVMON-MIB", "rbnFanSpeedCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonFanSpeedObjectGroup = rbnEnvMonFanSpeedObjectGroup.setStatus('current')
rbnEnvMonEntityObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 8)).setObjects(("RBN-ENVMON-MIB", "rbnEntityTempDescr"), ("RBN-ENVMON-MIB", "rbnEntityTempCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonEntityObjectGroup = rbnEnvMonEntityObjectGroup.setStatus('current')
rbnEnvMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 1)).setObjects(("RBN-ENVMON-MIB", "rbnEnvMonMIBObjectGroup"), ("RBN-ENVMON-MIB", "rbnEnvMonMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBCompliance = rbnEnvMonMIBCompliance.setStatus('obsolete')
rbnEnvMonMIBComplianceV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 2)).setObjects(("RBN-ENVMON-MIB", "rbnEnvMonMIBObjectGroup"), ("RBN-ENVMON-MIB", "rbnEnvMonMIBNotificationGroup"), ("RBN-ENVMON-MIB", "rbnEnvMonVoltageObjectGroup"), ("RBN-ENVMON-MIB", "rbnEnvMonTempObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBComplianceV2 = rbnEnvMonMIBComplianceV2.setStatus('deprecated')
rbnEnvMonMIBComplianceV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 3)).setObjects(("RBN-ENVMON-MIB", "rbnEnvMonMIBObjectGroupV2"), ("RBN-ENVMON-MIB", "rbnEnvMonMIBNotificationGroupV2"), ("RBN-ENVMON-MIB", "rbnEnvMonVoltageObjectGroup"), ("RBN-ENVMON-MIB", "rbnEnvMonTempObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBComplianceV3 = rbnEnvMonMIBComplianceV3.setStatus('deprecated')
rbnEnvMonMIBComplianceV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 4)).setObjects(("RBN-ENVMON-MIB", "rbnEnvMonMIBObjectGroupV2"), ("RBN-ENVMON-MIB", "rbnEnvMonMIBNotificationGroupV2"), ("RBN-ENVMON-MIB", "rbnEnvMonVoltageObjectGroup"), ("RBN-ENVMON-MIB", "rbnEnvMonTempObjectGroup"), ("RBN-ENVMON-MIB", "rbnEnvMonFanSpeedObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBComplianceV4 = rbnEnvMonMIBComplianceV4.setStatus('deprecated')
rbnEnvMonMIBComplianceV5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 5)).setObjects(("RBN-ENVMON-MIB", "rbnEnvMonMIBObjectGroupV2"), ("RBN-ENVMON-MIB", "rbnEnvMonMIBNotificationGroupV2"), ("RBN-ENVMON-MIB", "rbnEnvMonVoltageObjectGroup"), ("RBN-ENVMON-MIB", "rbnEnvMonFanSpeedObjectGroup"), ("RBN-ENVMON-MIB", "rbnEnvMonEntityObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBComplianceV5 = rbnEnvMonMIBComplianceV5.setStatus('current')
mibBuilder.exportSymbols("RBN-ENVMON-MIB", rbnEnvMonEntityObjectGroup=rbnEnvMonEntityObjectGroup, rbnPowerDescr=rbnPowerDescr, rbnEnvMonMIBNotifications=rbnEnvMonMIBNotifications, rbnFanStatusTable=rbnFanStatusTable, rbnEnvMonMIBComplianceV3=rbnEnvMonMIBComplianceV3, rbnEntityTempSensorEntry=rbnEntityTempSensorEntry, rbnFanStatusEntry=rbnFanStatusEntry, rbnVoltageDescr=rbnVoltageDescr, rbnCpuTempSensorTable=rbnCpuTempSensorTable, rbnFanUnitDescr=rbnFanUnitDescr, rbnCpuTempSensorEntry=rbnCpuTempSensorEntry, rbnFanFail=rbnFanFail, rbnEnvMonMIBObjects=rbnEnvMonMIBObjects, rbnVoltageDesired=rbnVoltageDesired, rbnFanStatus=rbnFanStatus, rbnEntityTempDescr=rbnEntityTempDescr, rbnFanStatusChange=rbnFanStatusChange, rbnEnvMonMIBComplianceV5=rbnEnvMonMIBComplianceV5, rbnEnvMonMIBNotificationGroup=rbnEnvMonMIBNotificationGroup, rbnEnvMonTempObjectGroup=rbnEnvMonTempObjectGroup, rbnEntityTempCurrent=rbnEntityTempCurrent, rbnEnvMonMIBComplianceV4=rbnEnvMonMIBComplianceV4, RbnVoltage=RbnVoltage, rbnEnvMonMIBCompliance=rbnEnvMonMIBCompliance, rbnVoltageSensorTable=rbnVoltageSensorTable, rbnPowerIndex=rbnPowerIndex, rbnCpuTempDescr=rbnCpuTempDescr, rbnVoltageIndex=rbnVoltageIndex, rbnPowerStatusTable=rbnPowerStatusTable, rbnPowerStatusEntry=rbnPowerStatusEntry, rbnCpuTempIndex=rbnCpuTempIndex, rbnEnvMonMIBNotificationGroupV2=rbnEnvMonMIBNotificationGroupV2, PYSNMP_MODULE_ID=rbnEnvMonMIB, rbnFanDescr=rbnFanDescr, rbnVoltageSensorEntry=rbnVoltageSensorEntry, rbnEnvMonMIBGroups=rbnEnvMonMIBGroups, rbnEnvMonMIBObjectGroup=rbnEnvMonMIBObjectGroup, rbnEntityTempSensorTable=rbnEntityTempSensorTable, rbnFanFailChange=rbnFanFailChange, rbnEnvMonMIBCompliances=rbnEnvMonMIBCompliances, rbnFanSpeedEntry=rbnFanSpeedEntry, rbnEnvMonFanSpeedObjectGroup=rbnEnvMonFanSpeedObjectGroup, rbnEnvMonMIBComplianceV2=rbnEnvMonMIBComplianceV2, rbnFanSpeedTable=rbnFanSpeedTable, rbnFanSpeedCurrent=rbnFanSpeedCurrent, rbnPowerStatusChange=rbnPowerStatusChange, RbnTemperature=RbnTemperature, rbnVoltageCurrent=rbnVoltageCurrent, rbnFanUnitID=rbnFanUnitID, rbnEnvMonMIB=rbnEnvMonMIB, rbnEnvMonMIBConformance=rbnEnvMonMIBConformance, rbnPowerFailChange=rbnPowerFailChange, rbnPowerStatus=rbnPowerStatus, rbnCpuTempCurrent=rbnCpuTempCurrent, rbnEntityTempIndex=rbnEntityTempIndex, rbnPowerFail=rbnPowerFail, rbnEnvMonMIBObjectGroupV2=rbnEnvMonMIBObjectGroupV2, RbnFanSpeed=RbnFanSpeed, rbnFanIndex=rbnFanIndex, rbnEnvMonVoltageObjectGroup=rbnEnvMonVoltageObjectGroup)
