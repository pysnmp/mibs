#
# PySNMP MIB module DLINKSW-STORM-CTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLINKSW-STORM-CTRL-MIB
# Source digest sha256:2c5d3443285ea1ddda2c4cb40653d25709756f7532db3010c057169b7621428d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkSwStormCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 25))
dlinkSwStormCtrlMIB.setRevisions(('2013-06-13 00:00',))
if mibBuilder.loadTexts: dlinkSwStormCtrlMIB.setLastUpdated('2013-06-13 00:00')
if mibBuilder.loadTexts: dlinkSwStormCtrlMIB.setOrganization('D-Link Corp.')
class DStormCtlTrafficType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("broadcast", 1), ("multicast", 2), ("unicast", 3))

class DStormCtlThrType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("pps", 1), ("kbps", 2), ("percentage", 3))

class DStormCtlThrTypeValue(TextualConvention, Integer32):
    status = 'current'

dStormCtrlMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 0))
dStormCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 1))
dStormCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 2))
dStormCtrlGentrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1))
dStormCtrlNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("stormOccurred", 2), ("stormCleared", 3), ("both", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlNotifyEnable.setStatus('current')
dStormCtrlPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 600)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlPollingInterval.setStatus('current')
dStormCtrlPollingRetries = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 360), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlPollingRetries.setStatus('current')
dStormCtrlThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dStormCtrlThresholdTable.setStatus('current')
dStormCtrlThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficType"))
if mibBuilder.loadTexts: dStormCtrlThresholdEntry.setStatus('current')
dStormCtrlTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 1), DStormCtlTrafficType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dStormCtrlTrafficType.setStatus('current')
dStormCtrlThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 2), DStormCtlThrType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dStormCtrlThresholdType.setStatus('current')
dStormCtrlRiseThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 3), DStormCtlThrTypeValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dStormCtrlRiseThresholdValue.setStatus('current')
dStormCtrlLowThresholdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 2, 1, 4), DStormCtlThrTypeValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dStormCtrlLowThresholdValue.setStatus('current')
dStormCtrlIfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dStormCtrlIfTable.setStatus('current')
dStormCtrlIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dStormCtrlIfEntry.setStatus('current')
dStormCtrlIfActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("shutdown", 2), ("drop", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dStormCtrlIfActionType.setStatus('current')
dStormCtrlTrafficInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dStormCtrlTrafficInfoTable.setStatus('current')
dStormCtrlTrafficInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficType"))
if mibBuilder.loadTexts: dStormCtrlTrafficInfoEntry.setStatus('current')
dStormCtrlCurTrafficUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 1), DStormCtlThrType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dStormCtrlCurTrafficUnitType.setStatus('current')
dStormCtrlCurTrafficValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 2), DStormCtlThrTypeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dStormCtrlCurTrafficValue.setStatus('current')
dStormCtrlTrafficInfoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("forwarding", 1), ("dropped", 2), ("errorDisabled", 3), ("linkDown", 4), ("inactive", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dStormCtrlTrafficInfoStatus.setStatus('current')
dStormCtrlNotifyInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 5))
dStormCtrlNotifyTrafficType = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 25, 1, 5, 1), DStormCtlTrafficType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dStormCtrlNotifyTrafficType.setStatus('current')
dStormCtrlOccurred = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 25, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
if mibBuilder.loadTexts: dStormCtrlOccurred.setStatus('current')
dStormCtrlStormCleared = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 25, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
if mibBuilder.loadTexts: dStormCtrlStormCleared.setStatus('current')
dStormCtrlCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 1))
dStormCtrlCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 1, 1)).setObjects(("DLINKSW-STORM-CTRL-MIB", "dStormCtrlBaiscGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dStormCtrlCompliance = dStormCtrlCompliance.setStatus('current')
dStormCtrlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2))
dStormCtrlBaiscGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2, 1)).setObjects(("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyEnable"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlPollingInterval"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlPollingRetries"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlThresholdType"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlRiseThresholdValue"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlLowThresholdValue"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlIfActionType"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlCurTrafficUnitType"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlCurTrafficValue"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlTrafficInfoStatus"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlNotifyTrafficType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dStormCtrlBaiscGroup = dStormCtrlBaiscGroup.setStatus('current')
dStormCtrlNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 171, 14, 25, 2, 2, 2)).setObjects(("DLINKSW-STORM-CTRL-MIB", "dStormCtrlOccurred"), ("DLINKSW-STORM-CTRL-MIB", "dStormCtrlStormCleared"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dStormCtrlNotifyGroup = dStormCtrlNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-STORM-CTRL-MIB", DStormCtlThrType=DStormCtlThrType, DStormCtlThrTypeValue=DStormCtlThrTypeValue, DStormCtlTrafficType=DStormCtlTrafficType, PYSNMP_MODULE_ID=dlinkSwStormCtrlMIB, dStormCtrlBaiscGroup=dStormCtrlBaiscGroup, dStormCtrlCompliance=dStormCtrlCompliance, dStormCtrlCompliances=dStormCtrlCompliances, dStormCtrlCurTrafficUnitType=dStormCtrlCurTrafficUnitType, dStormCtrlCurTrafficValue=dStormCtrlCurTrafficValue, dStormCtrlGentrl=dStormCtrlGentrl, dStormCtrlGroup=dStormCtrlGroup, dStormCtrlIfActionType=dStormCtrlIfActionType, dStormCtrlIfEntry=dStormCtrlIfEntry, dStormCtrlIfTable=dStormCtrlIfTable, dStormCtrlLowThresholdValue=dStormCtrlLowThresholdValue, dStormCtrlMIBConformance=dStormCtrlMIBConformance, dStormCtrlMIBNotifications=dStormCtrlMIBNotifications, dStormCtrlMIBObjects=dStormCtrlMIBObjects, dStormCtrlNotifyEnable=dStormCtrlNotifyEnable, dStormCtrlNotifyGroup=dStormCtrlNotifyGroup, dStormCtrlNotifyInfo=dStormCtrlNotifyInfo, dStormCtrlNotifyTrafficType=dStormCtrlNotifyTrafficType, dStormCtrlOccurred=dStormCtrlOccurred, dStormCtrlPollingInterval=dStormCtrlPollingInterval, dStormCtrlPollingRetries=dStormCtrlPollingRetries, dStormCtrlRiseThresholdValue=dStormCtrlRiseThresholdValue, dStormCtrlStormCleared=dStormCtrlStormCleared, dStormCtrlThresholdEntry=dStormCtrlThresholdEntry, dStormCtrlThresholdTable=dStormCtrlThresholdTable, dStormCtrlThresholdType=dStormCtrlThresholdType, dStormCtrlTrafficInfoEntry=dStormCtrlTrafficInfoEntry, dStormCtrlTrafficInfoStatus=dStormCtrlTrafficInfoStatus, dStormCtrlTrafficInfoTable=dStormCtrlTrafficInfoTable, dStormCtrlTrafficType=dStormCtrlTrafficType, dlinkSwStormCtrlMIB=dlinkSwStormCtrlMIB)
