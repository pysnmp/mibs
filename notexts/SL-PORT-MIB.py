#
# PySNMP MIB module SL-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source SL-PORT-MIB
# Source digest sha256:b7912eef485c765ab954f4ec611121d06c13967c6259657917ee62e357454f65
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DateAndTime, DisplayString, RowStatus, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "RowStatus", "TextualConvention", "TimeStamp", "TruthValue")
slPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14))
if mibBuilder.loadTexts: slPort.setLastUpdated('2001-01-18 00:00')
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
slPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: slPortConfigTable.setStatus('current')
slPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 14, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "SL-PORT-MIB", "slPortConfigIndex"))
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
mibBuilder.exportSymbols("SL-PORT-MIB", LedColor=LedColor, LedMode=LedMode, PYSNMP_MODULE_ID=slPort, slPort=slPort, slPortConfig=slPortConfig, slPortConfigAlarmMask=slPortConfigAlarmMask, slPortConfigChangeType=slPortConfigChangeType, slPortConfigChanged=slPortConfigChanged, slPortConfigChangedApsEnabled=slPortConfigChangedApsEnabled, slPortConfigChangedLabel=slPortConfigChangedLabel, slPortConfigChangedMask=slPortConfigChangedMask, slPortConfigChangedType=slPortConfigChangedType, slPortConfigEntry=slPortConfigEntry, slPortConfigIndex=slPortConfigIndex, slPortConfigLabel=slPortConfigLabel, slPortConfigLastChange=slPortConfigLastChange, slPortConfigLedColor=slPortConfigLedColor, slPortConfigLedMode=slPortConfigLedMode, slPortConfigTable=slPortConfigTable, slPortNotification=slPortNotification)
