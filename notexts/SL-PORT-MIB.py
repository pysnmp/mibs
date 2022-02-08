#
# PySNMP MIB module SL-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-PORT-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 23:21:00 2022
# On host fv-az42-507 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Integer32, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Counter32, MibIdentifier, NotificationType, Unsigned32, ModuleIdentity, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Counter32", "MibIdentifier", "NotificationType", "Unsigned32", "ModuleIdentity", "iso", "Bits")
DateAndTime, TruthValue, RowStatus, TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TruthValue", "RowStatus", "TextualConvention", "DisplayString", "TimeStamp")
slPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14))
if mibBuilder.loadTexts: slPort.setLastUpdated('200101180000Z')
if mibBuilder.loadTexts: slPort.setOrganization('PacketLight Networks Ltd.')
class LedColor(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("off", 1), ("red", 2), ("yellow", 3), ("green", 4))

class LedMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("stable", 1), ("fastBlinking", 2), ("slowBlinking", 3))

slPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1))
slPortNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2))
slPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1), )
if mibBuilder.loadTexts: slPortConfigTable.setStatus('current')
slPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1), ).setIndexNames((0, "SL-PORT-MIB", "slPortConfigIndex"))
if mibBuilder.loadTexts: slPortConfigEntry.setStatus('current')
slPortConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPortConfigIndex.setStatus('current')
slPortConfigLedColor = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 2), LedColor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPortConfigLedColor.setStatus('current')
slPortConfigLedMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 3), LedMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPortConfigLedMode.setStatus('current')
slPortConfigChangeType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slPortConfigChangeType.setStatus('current')
slPortConfigAlarmMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slPortConfigAlarmMask.setStatus('current')
slPortConfigLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPortConfigLabel.setStatus('current')
slPortConfigLastChange = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPortConfigLastChange.setStatus('current')
slPortConfigChanged = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 1)).setObjects(("SL-PORT-MIB", "slPortConfigIndex"), ("SL-PORT-MIB", "slPortConfigLedColor"), ("SL-PORT-MIB", "slPortConfigLedMode"), ("SL-PORT-MIB", "slPortConfigChangeType"), ("SL-PORT-MIB", "slPortConfigAlarmMask"), ("SL-PORT-MIB", "slPortConfigLabel"))
if mibBuilder.loadTexts: slPortConfigChanged.setStatus('current')
slPortConfigChangedType = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 2)).setObjects(("SL-PORT-MIB", "slPortConfigIndex"), ("SL-PORT-MIB", "slPortConfigChangeType"))
if mibBuilder.loadTexts: slPortConfigChangedType.setStatus('current')
slPortConfigChangedMask = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 3)).setObjects(("SL-PORT-MIB", "slPortConfigIndex"), ("SL-PORT-MIB", "slPortConfigAlarmMask"))
if mibBuilder.loadTexts: slPortConfigChangedMask.setStatus('current')
slPortConfigChangedLabel = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 4)).setObjects(("SL-PORT-MIB", "slPortConfigIndex"), ("SL-PORT-MIB", "slPortConfigLabel"))
if mibBuilder.loadTexts: slPortConfigChangedLabel.setStatus('current')
slPortConfigChangedApsEnabled = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 2, 5)).setObjects(("SL-PORT-MIB", "slPortConfigIndex"))
if mibBuilder.loadTexts: slPortConfigChangedApsEnabled.setStatus('current')
mibBuilder.exportSymbols("SL-PORT-MIB", slPortConfigLedMode=slPortConfigLedMode, slPortConfigLedColor=slPortConfigLedColor, LedColor=LedColor, slPortConfigChangedApsEnabled=slPortConfigChangedApsEnabled, slPortConfigChangedLabel=slPortConfigChangedLabel, slPortConfigChangedMask=slPortConfigChangedMask, slPortConfigLabel=slPortConfigLabel, PYSNMP_MODULE_ID=slPort, slPortConfigChanged=slPortConfigChanged, slPortConfigChangeType=slPortConfigChangeType, slPortConfigTable=slPortConfigTable, slPort=slPort, slPortNotification=slPortNotification, slPortConfigChangedType=slPortConfigChangedType, slPortConfigIndex=slPortConfigIndex, LedMode=LedMode, slPortConfig=slPortConfig, slPortConfigEntry=slPortConfigEntry, slPortConfigLastChange=slPortConfigLastChange, slPortConfigAlarmMask=slPortConfigAlarmMask)
