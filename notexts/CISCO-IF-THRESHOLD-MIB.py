#
# PySNMP MIB module CISCO-IF-THRESHOLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IF-THRESHOLD-MIB
# Source digest sha256:0f318aae2e6f6aeb95fd7c19d60d1625f00b7e4a1a6c50d69d62e73ab9e8f321
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TimeStamp", "TruthValue")
ciscoIfThresholdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 218))
ciscoIfThresholdMIB.setRevisions(('2001-09-14 00:00', '2001-06-14 00:00',))
if mibBuilder.loadTexts: ciscoIfThresholdMIB.setLastUpdated('2001-09-14 00:00')
if mibBuilder.loadTexts: ciscoIfThresholdMIB.setOrganization('Cisco Systems, Inc.')
class CifthTemplateIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1000)

class CifthTemplateIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1000)

class CifthThresholdIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 63)

class CifthThresholdList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class CifthThresholdSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("fail", 1), ("degrade", 2), ("info", 3), ("other", 4))

class CifthThresholdSeverityOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4)

cIfThresholdMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 218, 1))
cifthTemplateGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1))
cifthTemplateIfAssignGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2))
cifthIfThresholdFiredGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3))
cifthTemplateIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 1), CifthTemplateIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifthTemplateIndexNext.setStatus('current')
cifthTemplateLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifthTemplateLastChange.setStatus('current')
cifthTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cifthTemplateTable.setStatus('current')
cifthTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IF-THRESHOLD-MIB", "cifthTemplateIndex"))
if mibBuilder.loadTexts: cifthTemplateEntry.setStatus('current')
cifthTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1, 1), CifthTemplateIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cifthTemplateIndex.setStatus('current')
cifthTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthTemplateName.setStatus('current')
cifthTemplateNotifyHoldDownType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("holdDownTimer", 2), ("fireAndClearThresholds", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthTemplateNotifyHoldDownType.setStatus('current')
cifthTemplateNotifyHoldDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthTemplateNotifyHoldDownTime.setStatus('current')
cifthTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthTemplateRowStatus.setStatus('current')
cifthThresholdLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifthThresholdLastChange.setStatus('current')
cifthThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cifthThresholdTable.setStatus('current')
cifthThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IF-THRESHOLD-MIB", "cifthTemplateIndex"), (0, "CISCO-IF-THRESHOLD-MIB", "cifthThresholdIndex"))
if mibBuilder.loadTexts: cifthThresholdEntry.setStatus('current')
cifthThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 1), CifthThresholdIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cifthThresholdIndex.setStatus('current')
cifthThresholdDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthThresholdDescr.setStatus('current')
cifthThresholdObject = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthThresholdObject.setStatus('current')
cifthThresholdSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 4), CifthThresholdSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthThresholdSeverity.setStatus('current')
cifthThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2), ("rateOfIncreaseExponentXIfSpeed", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthThresholdType.setStatus('current')
cifthThresholdDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rising", 1), ("falling", 2))).clone('rising')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthThresholdDirection.setStatus('current')
cifthThresholdFiredValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthThresholdFiredValue.setStatus('current')
cifthThresholdClearedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthThresholdClearedValue.setStatus('current')
cifthThresholdSampleInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 900000))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthThresholdSampleInterval.setStatus('current')
cifthThresholdApsSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthThresholdApsSwitchover.setStatus('current')
cifthThresholdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthThresholdRowStatus.setStatus('current')
cifthTemplateIfLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifthTemplateIfLastChange.setStatus('current')
cifthTemplateIfAssignTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cifthTemplateIfAssignTable.setStatus('current')
cifthTemplateIfAssignEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IF-THRESHOLD-MIB", "cifthTemplateIndex"), (0, "CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfAssignInterface"))
if mibBuilder.loadTexts: cifthTemplateIfAssignEntry.setStatus('current')
cifthTemplateIfAssignInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 2, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cifthTemplateIfAssignInterface.setStatus('current')
cifthTemplateIfAssignOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifthTemplateIfAssignOperStatus.setStatus('current')
cifthTemplateIfAssignRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifthTemplateIfAssignRowStatus.setStatus('current')
cifthThresholdFiredNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 1), CifthThresholdSeverityOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cifthThresholdFiredNotifyEnable.setStatus('current')
cifthThresholdFiredLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifthThresholdFiredLastChange.setStatus('current')
cifthIfThresholdFiredTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cifthIfThresholdFiredTable.setStatus('current')
cifthIfThresholdFiredEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredTemplate"))
if mibBuilder.loadTexts: cifthIfThresholdFiredEntry.setStatus('current')
cifthIfThresholdFiredTemplate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 1), CifthTemplateIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cifthIfThresholdFiredTemplate.setStatus('current')
cifthIfThresholdsFired = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 2), CifthThresholdList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifthIfThresholdsFired.setStatus('current')
cifthIfLastThresholdFired = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 3), CifthThresholdIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifthIfLastThresholdFired.setStatus('current')
cifthIfThresholdFiredLstChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifthIfThresholdFiredLstChange.setStatus('current')
cifthIfThresholdFiredLstSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 5), CifthThresholdSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifthIfThresholdFiredLstSeverity.setStatus('current')
cifthIfThresholdFiredMaxSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 6), CifthThresholdSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifthIfThresholdFiredMaxSeverity.setStatus('current')
cIfThresholdMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 218, 2))
cifthMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 218, 2, 0))
cifthIfThresholdFired = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 218, 2, 0, 1)).setObjects(("CISCO-IF-THRESHOLD-MIB", "cifthIfLastThresholdFired"), ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstChange"), ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstSeverity"))
if mibBuilder.loadTexts: cifthIfThresholdFired.setStatus('current')
cifthIfThresholdCleared = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 218, 2, 0, 2)).setObjects(("CISCO-IF-THRESHOLD-MIB", "cifthIfLastThresholdFired"), ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstChange"), ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstSeverity"))
if mibBuilder.loadTexts: cifthIfThresholdCleared.setStatus('current')
cifthTemplateIfStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 218, 2, 0, 3)).setObjects(("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfAssignOperStatus"))
if mibBuilder.loadTexts: cifthTemplateIfStatusChange.setStatus('current')
cIfThresholdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 218, 3))
cIfThresholdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 1))
cIfThresholdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2))
cIfThresholdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 1, 1)).setObjects(("CISCO-IF-THRESHOLD-MIB", "cIfThresholdTemplateGroup"), ("CISCO-IF-THRESHOLD-MIB", "cIfThresholdFiredGroup"), ("CISCO-IF-THRESHOLD-MIB", "cIfThresholdNotifsGroup"), ("CISCO-IF-THRESHOLD-MIB", "cifthHoldDownTimerGroup"), ("CISCO-IF-THRESHOLD-MIB", "cifthHoldDownHysteresisGroup"), ("CISCO-IF-THRESHOLD-MIB", "cifthApsGroup"), ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfThresholdMIBCompliance = cIfThresholdMIBCompliance.setStatus('current')
cIfThresholdTemplateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 1)).setObjects(("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIndexNext"), ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateLastChange"), ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateName"), ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateNotifyHoldDownType"), ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateRowStatus"), ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdLastChange"), ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdDescr"), ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdObject"), ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdSeverity"), ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdType"), ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdDirection"), ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdFiredValue"), ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdSampleInterval"), ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdRowStatus"), ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfLastChange"), ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfAssignOperStatus"), ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfAssignRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfThresholdTemplateGroup = cIfThresholdTemplateGroup.setStatus('current')
cIfThresholdFiredGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 2)).setObjects(("CISCO-IF-THRESHOLD-MIB", "cifthThresholdFiredNotifyEnable"), ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdFiredLastChange"), ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdsFired"), ("CISCO-IF-THRESHOLD-MIB", "cifthIfLastThresholdFired"), ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstChange"), ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstSeverity"), ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredMaxSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfThresholdFiredGroup = cIfThresholdFiredGroup.setStatus('current')
cifthHoldDownTimerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 3)).setObjects(("CISCO-IF-THRESHOLD-MIB", "cifthTemplateNotifyHoldDownTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifthHoldDownTimerGroup = cifthHoldDownTimerGroup.setStatus('current')
cifthHoldDownHysteresisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 4)).setObjects(("CISCO-IF-THRESHOLD-MIB", "cifthThresholdClearedValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifthHoldDownHysteresisGroup = cifthHoldDownHysteresisGroup.setStatus('current')
cifthApsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 5)).setObjects(("CISCO-IF-THRESHOLD-MIB", "cifthThresholdApsSwitchover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifthApsGroup = cifthApsGroup.setStatus('current')
cIfThresholdNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 6)).setObjects(("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFired"), ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfThresholdNotifsGroup = cIfThresholdNotifsGroup.setStatus('current')
cifthTemplateIfNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 7)).setObjects(("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cifthTemplateIfNotifsGroup = cifthTemplateIfNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-THRESHOLD-MIB", CifthTemplateIndex=CifthTemplateIndex, CifthTemplateIndexOrZero=CifthTemplateIndexOrZero, CifthThresholdIndex=CifthThresholdIndex, CifthThresholdList=CifthThresholdList, CifthThresholdSeverity=CifthThresholdSeverity, CifthThresholdSeverityOrZero=CifthThresholdSeverityOrZero, PYSNMP_MODULE_ID=ciscoIfThresholdMIB, cIfThresholdFiredGroup=cIfThresholdFiredGroup, cIfThresholdMIBCompliance=cIfThresholdMIBCompliance, cIfThresholdMIBCompliances=cIfThresholdMIBCompliances, cIfThresholdMIBConformance=cIfThresholdMIBConformance, cIfThresholdMIBGroups=cIfThresholdMIBGroups, cIfThresholdMIBNotifications=cIfThresholdMIBNotifications, cIfThresholdMIBObjects=cIfThresholdMIBObjects, cIfThresholdNotifsGroup=cIfThresholdNotifsGroup, cIfThresholdTemplateGroup=cIfThresholdTemplateGroup, cifthApsGroup=cifthApsGroup, cifthHoldDownHysteresisGroup=cifthHoldDownHysteresisGroup, cifthHoldDownTimerGroup=cifthHoldDownTimerGroup, cifthIfLastThresholdFired=cifthIfLastThresholdFired, cifthIfThresholdCleared=cifthIfThresholdCleared, cifthIfThresholdFired=cifthIfThresholdFired, cifthIfThresholdFiredEntry=cifthIfThresholdFiredEntry, cifthIfThresholdFiredGroup=cifthIfThresholdFiredGroup, cifthIfThresholdFiredLstChange=cifthIfThresholdFiredLstChange, cifthIfThresholdFiredLstSeverity=cifthIfThresholdFiredLstSeverity, cifthIfThresholdFiredMaxSeverity=cifthIfThresholdFiredMaxSeverity, cifthIfThresholdFiredTable=cifthIfThresholdFiredTable, cifthIfThresholdFiredTemplate=cifthIfThresholdFiredTemplate, cifthIfThresholdsFired=cifthIfThresholdsFired, cifthMIBNotificationsPrefix=cifthMIBNotificationsPrefix, cifthTemplateEntry=cifthTemplateEntry, cifthTemplateGroup=cifthTemplateGroup, cifthTemplateIfAssignEntry=cifthTemplateIfAssignEntry, cifthTemplateIfAssignGroup=cifthTemplateIfAssignGroup, cifthTemplateIfAssignInterface=cifthTemplateIfAssignInterface, cifthTemplateIfAssignOperStatus=cifthTemplateIfAssignOperStatus, cifthTemplateIfAssignRowStatus=cifthTemplateIfAssignRowStatus, cifthTemplateIfAssignTable=cifthTemplateIfAssignTable, cifthTemplateIfLastChange=cifthTemplateIfLastChange, cifthTemplateIfNotifsGroup=cifthTemplateIfNotifsGroup, cifthTemplateIfStatusChange=cifthTemplateIfStatusChange, cifthTemplateIndex=cifthTemplateIndex, cifthTemplateIndexNext=cifthTemplateIndexNext, cifthTemplateLastChange=cifthTemplateLastChange, cifthTemplateName=cifthTemplateName, cifthTemplateNotifyHoldDownTime=cifthTemplateNotifyHoldDownTime, cifthTemplateNotifyHoldDownType=cifthTemplateNotifyHoldDownType, cifthTemplateRowStatus=cifthTemplateRowStatus, cifthTemplateTable=cifthTemplateTable, cifthThresholdApsSwitchover=cifthThresholdApsSwitchover, cifthThresholdClearedValue=cifthThresholdClearedValue, cifthThresholdDescr=cifthThresholdDescr, cifthThresholdDirection=cifthThresholdDirection, cifthThresholdEntry=cifthThresholdEntry, cifthThresholdFiredLastChange=cifthThresholdFiredLastChange, cifthThresholdFiredNotifyEnable=cifthThresholdFiredNotifyEnable, cifthThresholdFiredValue=cifthThresholdFiredValue, cifthThresholdIndex=cifthThresholdIndex, cifthThresholdLastChange=cifthThresholdLastChange, cifthThresholdObject=cifthThresholdObject, cifthThresholdRowStatus=cifthThresholdRowStatus, cifthThresholdSampleInterval=cifthThresholdSampleInterval, cifthThresholdSeverity=cifthThresholdSeverity, cifthThresholdTable=cifthThresholdTable, cifthThresholdType=cifthThresholdType, ciscoIfThresholdMIB=ciscoIfThresholdMIB)
