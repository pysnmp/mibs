#
# PySNMP MIB module SL-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-PORT-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 07:42:05 2023
# On host fv-az437-489 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Integer32, NotificationType, MibIdentifier, ModuleIdentity, Bits, iso, Counter32, ObjectIdentity, Counter64, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Integer32", "NotificationType", "MibIdentifier", "ModuleIdentity", "Bits", "iso", "Counter32", "ObjectIdentity", "Counter64", "IpAddress", "Gauge32")
TimeStamp, RowStatus, TruthValue, TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "RowStatus", "TruthValue", "TextualConvention", "DateAndTime", "DisplayString")
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
mibBuilder.exportSymbols("SL-PORT-MIB", PYSNMP_MODULE_ID=slPort, slPort=slPort, slPortConfigLastChange=slPortConfigLastChange, slPortConfigTable=slPortConfigTable, slPortConfigChanged=slPortConfigChanged, slPortConfigEntry=slPortConfigEntry, slPortConfigIndex=slPortConfigIndex, slPortConfigLedMode=slPortConfigLedMode, slPortConfigChangedLabel=slPortConfigChangedLabel, slPortConfigChangedType=slPortConfigChangedType, LedColor=LedColor, slPortConfigChangeType=slPortConfigChangeType, LedMode=LedMode, slPortNotification=slPortNotification, slPortConfigChangedApsEnabled=slPortConfigChangedApsEnabled, slPortConfig=slPortConfig, slPortConfigAlarmMask=slPortConfigAlarmMask, slPortConfigLedColor=slPortConfigLedColor, slPortConfigChangedMask=slPortConfigChangedMask, slPortConfigLabel=slPortConfigLabel)
