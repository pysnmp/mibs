#
# PySNMP MIB module CISCO-ENTITY-FRU-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-FRU-CONTROL-MIB
# Source digest sha256:e92ba4ae34c917b29229ea9ebf91d11497b021f8136bf72fd0419675a09cb8eb
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalClass, entPhysicalContainedIn, entPhysicalIndex, entPhysicalModelName, entPhysicalName, entPhysicalVendorType = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalClass", "entPhysicalContainedIn", "entPhysicalIndex", "entPhysicalModelName", "entPhysicalName", "entPhysicalVendorType")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp", "TruthValue")
ciscoEntityFRUControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 117))
ciscoEntityFRUControlMIB.setRevisions(('2018-11-05 00:00', '2018-08-20 00:00', '2018-07-25 00:00', '2017-12-06 00:00', '2013-08-19 00:00', '2011-12-22 00:00', '2011-03-18 00:00', '2010-12-10 00:00', '2008-10-08 00:00', '2007-06-21 00:00', '2007-03-14 00:00', '2006-06-23 00:00', '2005-09-06 00:00', '2004-12-09 00:00', '2004-10-19 00:00', '2003-11-24 00:00', '2003-10-27 00:00', '2003-10-23 00:00', '2003-07-22 00:00', '2002-10-16 00:00', '2002-10-03 00:00', '2002-09-15 00:00', '2002-07-12 00:00', '2001-05-22 00:00', '2000-01-13 00:00', '1999-04-05 00:00',))
if mibBuilder.loadTexts: ciscoEntityFRUControlMIB.setLastUpdated('2018-11-05 00:00')
if mibBuilder.loadTexts: ciscoEntityFRUControlMIB.setOrganization('Cisco Systems, Inc.')
cefcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1))
cefcFRUMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 2))
cefcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 3))
class PowerRedundancyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notsupported", 1), ("redundant", 2), ("combined", 3), ("nonRedundant", 4), ("psRedundant", 5), ("inPwrSrcRedundant", 6), ("psRedundantSingleInput", 7))

class PowerAdminType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("on", 1), ("off", 2), ("inlineAuto", 3), ("inlineOn", 4), ("powerCycle", 5))

class PowerOperType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("offEnvOther", 1), ("on", 2), ("offAdmin", 3), ("offDenied", 4), ("offEnvPower", 5), ("offEnvTemp", 6), ("offEnvFan", 7), ("failed", 8), ("onButFanFail", 9), ("offCooling", 10), ("offConnectorRating", 11), ("onButInlinePowerFail", 12))

class FRUCurrentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class ModuleAdminType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("reset", 3), ("outOfServiceAdmin", 4))

class ModuleOperType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("unknown", 1), ("ok", 2), ("disabled", 3), ("okButDiagFailed", 4), ("boot", 5), ("selfTest", 6), ("failed", 7), ("missing", 8), ("mismatchWithParent", 9), ("mismatchConfig", 10), ("diagFailed", 11), ("dormant", 12), ("outOfServiceAdmin", 13), ("outOfServiceEnvTemp", 14), ("poweredDown", 15), ("poweredUp", 16), ("powerDenied", 17), ("powerCycled", 18), ("okButPowerOverWarning", 19), ("okButPowerOverCritical", 20), ("syncInProgress", 21), ("upgrading", 22), ("okButAuthFailed", 23), ("mdr", 24), ("fwMismatchFound", 25), ("fwDownloadSuccess", 26), ("fwDownloadFailure", 27))

class ModuleResetReasonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("unknown", 1), ("powerUp", 2), ("parityError", 3), ("clearConfigReset", 4), ("manualReset", 5), ("watchDogTimeoutReset", 6), ("resourceOverflowReset", 7), ("missingTaskReset", 8), ("lowVoltageReset", 9), ("controllerReset", 10), ("systemReset", 11), ("switchoverReset", 12), ("upgradeReset", 13), ("downgradeReset", 14), ("cacheErrorReset", 15), ("deviceDriverReset", 16), ("softwareExceptionReset", 17), ("restoreConfigReset", 18), ("abortRevReset", 19), ("burnBootReset", 20), ("standbyCdHealthierReset", 21), ("nonNativeConfigClearReset", 22), ("memoryProtectionErrorReset", 23))

class FRUTimeSeconds(TextualConvention, Unsigned32):
    status = 'current'

class FRUCoolingUnit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cfm", 1), ("watts", 2))

class CefcPercentOrMinusOne(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100), )
class CefcVmModuleOperType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("down", 1), ("up", 2), ("unknown", 3), ("goingDown", 4))

cefcFRUPower = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1))
cefcModule = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2))
cefcMIBNotificationEnables = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 3))
cefcFRUFan = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4))
cefcPhysical = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5))
cefcPowerCapacity = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6))
cefcCooling = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7))
cefcConnector = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8))
cefcFRUPowerSupplyGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcFRUPowerSupplyGroupTable.setStatus('current')
cefcFRUPowerSupplyGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcFRUPowerSupplyGroupEntry.setStatus('current')
cefcPowerRedundancyMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 1), PowerRedundancyType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcPowerRedundancyMode.setStatus('current')
cefcPowerUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPowerUnits.setStatus('current')
cefcTotalAvailableCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 3), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcTotalAvailableCurrent.setStatus('current')
cefcTotalDrawnCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 4), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcTotalDrawnCurrent.setStatus('current')
cefcPowerRedundancyOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 5), PowerRedundancyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPowerRedundancyOperMode.setStatus('current')
cefcPowerNonRedundantReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notApplicable", 1), ("unknown", 2), ("singleSupply", 3), ("mismatchedSupplies", 4), ("supplyError", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPowerNonRedundantReason.setStatus('current')
cefcTotalDrawnInlineCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 7), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcTotalDrawnInlineCurrent.setStatus('current')
cefcFRUPowerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcFRUPowerStatusTable.setStatus('current')
cefcFRUPowerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcFRUPowerStatusEntry.setStatus('current')
cefcFRUPowerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 1), PowerAdminType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcFRUPowerAdminStatus.setStatus('current')
cefcFRUPowerOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 2), PowerOperType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFRUPowerOperStatus.setStatus('current')
cefcFRUCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 3), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFRUCurrent.setStatus('current')
cefcFRUPowerCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 4), Bits().clone(namedValues=NamedValues(("realTimeCurrent", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFRUPowerCapability.setStatus('current')
cefcFRURealTimeCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 5), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFRURealTimeCurrent.setStatus('current')
cefcMaxDefaultInLinePower = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12500)).clone(12500)).setUnits('miliwatts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcMaxDefaultInLinePower.setStatus('deprecated')
cefcFRUPowerSupplyValueTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcFRUPowerSupplyValueTable.setStatus('current')
cefcFRUPowerSupplyValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcFRUPowerSupplyValueEntry.setStatus('current')
cefcFRUTotalSystemCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 1), FRUCurrentType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcFRUTotalSystemCurrent.setStatus('current')
cefcFRUDrawnSystemCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 2), FRUCurrentType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcFRUDrawnSystemCurrent.setStatus('current')
cefcFRUTotalInlineCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 3), FRUCurrentType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcFRUTotalInlineCurrent.setStatus('current')
cefcFRUDrawnInlineCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 4), FRUCurrentType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcFRUDrawnInlineCurrent.setStatus('current')
cefcFRUActualInputCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 5), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFRUActualInputCurrent.setStatus('current')
cefcFRUActualOutputCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 6), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFRUActualOutputCurrent.setStatus('current')
cefcMaxDefaultHighInLinePower = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 5), Unsigned32()).setUnits('miliwatts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcMaxDefaultHighInLinePower.setStatus('current')
cefcModuleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcModuleTable.setStatus('current')
cefcModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcModuleEntry.setStatus('current')
cefcModuleAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 1), ModuleAdminType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcModuleAdminStatus.setStatus('current')
cefcModuleOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 2), ModuleOperType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleOperStatus.setStatus('current')
cefcModuleResetReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 3), ModuleResetReasonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleResetReason.setStatus('current')
cefcModuleStatusLastChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleStatusLastChangeTime.setStatus('current')
cefcModuleLastClearConfigTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleLastClearConfigTime.setStatus('current')
cefcModuleResetReasonDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleResetReasonDescription.setStatus('current')
cefcModuleStateChangeReasonDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleStateChangeReasonDescr.setStatus('current')
cefcModuleUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 8), FRUTimeSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleUpTime.setStatus('current')
cefcVmModuleOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 9), CefcVmModuleOperType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcVmModuleOperStatus.setStatus('current')
cefcVmModuleStatusLastChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcVmModuleStatusLastChangeTime.setStatus('current')
cefcIntelliModuleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcIntelliModuleTable.setStatus('current')
cefcIntelliModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcIntelliModuleEntry.setStatus('current')
cefcIntelliModuleIPAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcIntelliModuleIPAddrType.setStatus('current')
cefcIntelliModuleIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcIntelliModuleIPAddr.setStatus('current')
cefcModuleLocalSwitchingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcModuleLocalSwitchingTable.setStatus('current')
cefcModuleLocalSwitchingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcModuleLocalSwitchingEntry.setStatus('current')
cefcModuleLocalSwitchingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcModuleLocalSwitchingMode.setStatus('current')
cefcFanTrayStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcFanTrayStatusTable.setStatus('current')
cefcFanTrayStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcFanTrayStatusEntry.setStatus('current')
cefcFanTrayOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ("warning", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanTrayOperStatus.setStatus('current')
cefcFanTrayDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("frontToBack", 2), ("backToFront", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanTrayDirection.setStatus('current')
cefcFanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcFanTable.setStatus('current')
cefcFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcFanEntry.setStatus('current')
cefcFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 2, 1, 1), Unsigned32()).setUnits('rpm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanSpeed.setStatus('current')
cefcFanSpeedPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 2, 1, 2), CefcPercentOrMinusOne()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanSpeedPercent.setStatus('current')
cefcPhysicalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcPhysicalTable.setStatus('current')
cefcPhysicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcPhysicalEntry.setStatus('current')
cefcPhysicalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("supported", 2), ("unsupported", 3), ("incompatible", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPhysicalStatus.setStatus('current')
cefcPowerSupplyInputTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcPowerSupplyInputTable.setStatus('current')
cefcPowerSupplyInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerSupplyInputIndex"))
if mibBuilder.loadTexts: cefcPowerSupplyInputEntry.setStatus('current')
cefcPowerSupplyInputIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1, 1, 1), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcPowerSupplyInputIndex.setStatus('current')
cefcPowerSupplyInputType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("acLow", 2), ("acHigh", 3), ("dcLow", 4), ("dcHigh", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPowerSupplyInputType.setStatus('current')
cefcPowerSupplyOutputTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcPowerSupplyOutputTable.setStatus('current')
cefcPowerSupplyOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeIndex"))
if mibBuilder.loadTexts: cefcPowerSupplyOutputEntry.setStatus('current')
cefcPSOutputModeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1, 1), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcPSOutputModeIndex.setStatus('current')
cefcPSOutputModeCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1, 2), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPSOutputModeCurrent.setStatus('current')
cefcPSOutputModeInOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPSOutputModeInOperation.setStatus('current')
cefcChassisCoolingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcChassisCoolingTable.setStatus('current')
cefcChassisCoolingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcChassisCoolingEntry.setStatus('current')
cefcChassisPerSlotCoolingCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcChassisPerSlotCoolingCap.setStatus('current')
cefcChassisPerSlotCoolingUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1, 1, 2), FRUCoolingUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcChassisPerSlotCoolingUnit.setStatus('current')
cefcFanCoolingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcFanCoolingTable.setStatus('current')
cefcFanCoolingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcFanCoolingEntry.setStatus('current')
cefcFanCoolingCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapacity.setStatus('current')
cefcFanCoolingCapacityUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2, 1, 2), FRUCoolingUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapacityUnit.setStatus('current')
cefcModuleCoolingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcModuleCoolingTable.setStatus('current')
cefcModuleCoolingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcModuleCoolingEntry.setStatus('current')
cefcModuleCooling = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleCooling.setStatus('current')
cefcModuleCoolingUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3, 1, 2), FRUCoolingUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleCoolingUnit.setStatus('current')
cefcFanCoolingCapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcFanCoolingCapTable.setStatus('current')
cefcFanCoolingCapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapIndex"))
if mibBuilder.loadTexts: cefcFanCoolingCapEntry.setStatus('current')
cefcFanCoolingCapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcFanCoolingCapIndex.setStatus('current')
cefcFanCoolingCapModeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapModeDescr.setStatus('current')
cefcFanCoolingCapCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapCapacity.setStatus('current')
cefcFanCoolingCapCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 4), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapCurrent.setStatus('current')
cefcFanCoolingCapCapacityUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 5), FRUCoolingUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapCapacityUnit.setStatus('current')
cefcConnectorRatingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcConnectorRatingTable.setStatus('current')
cefcConnectorRatingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcConnectorRatingEntry.setStatus('current')
cefcConnectorRating = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 1, 1, 1), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcConnectorRating.setStatus('current')
cefcModulePowerConsumptionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cefcModulePowerConsumptionTable.setStatus('current')
cefcModulePowerConsumptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcModulePowerConsumptionEntry.setStatus('current')
cefcModulePowerConsumption = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 2, 1, 1), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModulePowerConsumption.setStatus('current')
cefcMIBEnableStatusNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcMIBEnableStatusNotification.setStatus('current')
cefcEnablePSOutputChangeNotif = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 3, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcEnablePSOutputChangeNotif.setStatus('current')
cefcMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0))
cefcModuleStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 1)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleOperStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStatusLastChangeTime"))
if mibBuilder.loadTexts: cefcModuleStatusChange.setStatus('current')
cefcPowerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 2)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerOperStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerAdminStatus"))
if mibBuilder.loadTexts: cefcPowerStatusChange.setStatus('current')
cefcFRUInserted = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 3)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"))
if mibBuilder.loadTexts: cefcFRUInserted.setStatus('current')
cefcFRURemoved = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 4)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"))
if mibBuilder.loadTexts: cefcFRURemoved.setStatus('current')
cefcUnrecognizedFRU = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 5)).setObjects(("ENTITY-MIB", "entPhysicalClass"), ("ENTITY-MIB", "entPhysicalVendorType"), ("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPhysicalStatus"))
if mibBuilder.loadTexts: cefcUnrecognizedFRU.setStatus('current')
cefcFanTrayStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 6)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanTrayOperStatus"))
if mibBuilder.loadTexts: cefcFanTrayStatusChange.setStatus('current')
cefcPowerSupplyOutputChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 7)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeCurrent"))
if mibBuilder.loadTexts: cefcPowerSupplyOutputChange.setStatus('current')
cefcVmModuleStatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 8)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcVmModuleOperStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcVmModuleStatusLastChangeTime"))
if mibBuilder.loadTexts: cefcVmModuleStatusChangeNotif.setStatus('current')
cefcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1))
cefcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2))
cefcMIBPowerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 1)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance = cefcMIBPowerCompliance.setStatus('obsolete')
cefcMIBPowerCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 2)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance2 = cefcMIBPowerCompliance2.setStatus('deprecated')
cefcMIBPowerCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 3)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance3 = cefcMIBPowerCompliance3.setStatus('deprecated')
cefcMIBPowerCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 4)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance4 = cefcMIBPowerCompliance4.setStatus('deprecated')
cefcMIBPowerCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 5)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBFanTrayStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPhysicalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance5 = cefcMIBPowerCompliance5.setStatus('deprecated')
cefcMIBPowerCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 6)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBFanTrayStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPhysicalGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerOperModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleExtGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance6 = cefcMIBPowerCompliance6.setStatus('current')
cefcMIBPowerCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 7)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBFanTrayStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPhysicalGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerOperModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleExtGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerCapacityGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcCoolingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcConnectorRatingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance7 = cefcMIBPowerCompliance7.setStatus('deprecated')
cefcMIBPowerCompliance8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 8)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBFanTrayStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPhysicalGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerOperModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleExtGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerCapacityGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcCoolingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcConnectorRatingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup3"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerCurrentGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerRedundancyInfoGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance8 = cefcMIBPowerCompliance8.setStatus('deprecated')
cefcMIBPowerCompliance9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 9)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBFanTrayStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPhysicalGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerOperModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleExtGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerCapacityGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcConnectorRatingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup3"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerCurrentGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerRedundancyInfoGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleLocalSwitchingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerRealTimeStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerCapabilityGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUCoolingUnitGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUFanCoolingUnitGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcCoolingGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance9 = cefcMIBPowerCompliance9.setStatus('deprecated')
cefcMIBPowerCompliance10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 10)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBFanTrayStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPhysicalGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerOperModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleExtGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerCapacityGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcConnectorRatingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup3"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerCurrentGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerRedundancyInfoGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleLocalSwitchingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerRealTimeStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerCapabilityGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUCoolingUnitGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUFanCoolingUnitGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcCoolingGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanDirectionGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanSpeedGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerSupplyActualGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcVmModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcVmModuleNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance10 = cefcMIBPowerCompliance10.setStatus('current')
cefcMIBPowerModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 1)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerRedundancyMode"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerUnits"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcTotalAvailableCurrent"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcTotalDrawnCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerModeGroup = cefcMIBPowerModeGroup.setStatus('current')
cefcMIBPowerFRUControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 2)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerAdminStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerOperStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerFRUControlGroup = cefcMIBPowerFRUControlGroup.setStatus('current')
cefcMIBModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 3)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleAdminStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleOperStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleResetReason"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStatusLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBModuleGroup = cefcMIBModuleGroup.setStatus('current')
cefcMIBInLinePowerControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 4)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMaxDefaultInLinePower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBInLinePowerControlGroup = cefcMIBInLinePowerControlGroup.setStatus('deprecated')
cefcMIBNotificationEnablesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 5)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBEnableStatusNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBNotificationEnablesGroup = cefcMIBNotificationEnablesGroup.setStatus('current')
cefcMgmtNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 6)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStatusChange"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerStatusChange"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUInserted"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRURemoved"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMgmtNotificationsGroup = cefcMgmtNotificationsGroup.setStatus('current')
cefcModuleGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 7)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleLastClearConfigTime"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleResetReasonDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcModuleGroupRev1 = cefcModuleGroupRev1.setStatus('current')
cefcMIBPowerFRUValueGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 8)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUTotalSystemCurrent"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUDrawnSystemCurrent"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUTotalInlineCurrent"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUDrawnInlineCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerFRUValueGroup = cefcMIBPowerFRUValueGroup.setStatus('current')
cefcMIBFanTrayStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 9)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanTrayOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBFanTrayStatusGroup = cefcMIBFanTrayStatusGroup.setStatus('current')
cefcMIBPhysicalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 10)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPhysicalStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPhysicalGroup = cefcMIBPhysicalGroup.setStatus('current')
cefcMgmtNotificationsGroup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 11)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcUnrecognizedFRU"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanTrayStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMgmtNotificationsGroup2 = cefcMgmtNotificationsGroup2.setStatus('current')
cefcMIBPowerOperModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 12)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerRedundancyOperMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerOperModeGroup = cefcMIBPowerOperModeGroup.setStatus('current')
cefcMIBInLinePowerControlGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 13)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMaxDefaultHighInLinePower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBInLinePowerControlGroupRev1 = cefcMIBInLinePowerControlGroupRev1.setStatus('current')
cefcModuleExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 14)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStateChangeReasonDescr"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleUpTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcModuleExtGroup = cefcModuleExtGroup.setStatus('current')
cefcIntelliModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 15)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleIPAddrType"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleIPAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcIntelliModuleGroup = cefcIntelliModuleGroup.setStatus('current')
cefcPowerCapacityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 16)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerSupplyInputType"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeCurrent"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeInOperation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcPowerCapacityGroup = cefcPowerCapacityGroup.setStatus('current')
cefcCoolingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 17)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcChassisPerSlotCoolingCap"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapacity"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleCooling"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcCoolingGroup = cefcCoolingGroup.setStatus('deprecated')
cefcConnectorRatingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 18)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcConnectorRating"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModulePowerConsumption"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcConnectorRatingGroup = cefcConnectorRatingGroup.setStatus('current')
cefcMIBNotificationEnablesGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 19)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcEnablePSOutputChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBNotificationEnablesGroup2 = cefcMIBNotificationEnablesGroup2.setStatus('current')
cefcMgmtNotificationsGroup3 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 20)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerSupplyOutputChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMgmtNotificationsGroup3 = cefcMgmtNotificationsGroup3.setStatus('current')
cefcMIBInLinePowerCurrentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 21)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcTotalDrawnInlineCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBInLinePowerCurrentGroup = cefcMIBInLinePowerCurrentGroup.setStatus('current')
cefcMIBPowerRedundancyInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 22)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerNonRedundantReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerRedundancyInfoGroup = cefcMIBPowerRedundancyInfoGroup.setStatus('current')
cefcFanCoolingCapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 23)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapModeDescr"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapCapacity"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFanCoolingCapGroup = cefcFanCoolingCapGroup.setStatus('current')
cefcMIBModuleLocalSwitchingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 24)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleLocalSwitchingMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBModuleLocalSwitchingGroup = cefcMIBModuleLocalSwitchingGroup.setStatus('current')
cefcFRUPowerRealTimeStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 25)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRURealTimeCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFRUPowerRealTimeStatusGroup = cefcFRUPowerRealTimeStatusGroup.setStatus('current')
cefcFRUPowerCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 26)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFRUPowerCapabilityGroup = cefcFRUPowerCapabilityGroup.setStatus('current')
cefcFRUCoolingUnitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 27)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcChassisPerSlotCoolingUnit"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleCoolingUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFRUCoolingUnitGroup = cefcFRUCoolingUnitGroup.setStatus('current')
cefcFRUFanCoolingUnitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 28)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapacityUnit"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapCapacityUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFRUFanCoolingUnitGroup = cefcFRUFanCoolingUnitGroup.setStatus('current')
cefcCoolingGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 29)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcChassisPerSlotCoolingCap"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleCooling"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcCoolingGroup2 = cefcCoolingGroup2.setStatus('current')
cefcFanCoolingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 30)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapacity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFanCoolingGroup = cefcFanCoolingGroup.setStatus('current')
cefcFanDirectionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 31)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanTrayDirection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFanDirectionGroup = cefcFanDirectionGroup.setStatus('current')
cefcFanSpeedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 32)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanSpeed"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanSpeedPercent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFanSpeedGroup = cefcFanSpeedGroup.setStatus('current')
cefcPowerSupplyActualGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 33)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUActualInputCurrent"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUActualOutputCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcPowerSupplyActualGroup = cefcPowerSupplyActualGroup.setStatus('current')
cefcVmModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 34)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcVmModuleOperStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcVmModuleStatusLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcVmModuleGroup = cefcVmModuleGroup.setStatus('current')
cefcVmModuleNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 35)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcVmModuleStatusChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcVmModuleNotifsGroup = cefcVmModuleNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-FRU-CONTROL-MIB", CefcPercentOrMinusOne=CefcPercentOrMinusOne, CefcVmModuleOperType=CefcVmModuleOperType, FRUCoolingUnit=FRUCoolingUnit, FRUCurrentType=FRUCurrentType, FRUTimeSeconds=FRUTimeSeconds, ModuleAdminType=ModuleAdminType, ModuleOperType=ModuleOperType, ModuleResetReasonType=ModuleResetReasonType, PYSNMP_MODULE_ID=ciscoEntityFRUControlMIB, PowerAdminType=PowerAdminType, PowerOperType=PowerOperType, PowerRedundancyType=PowerRedundancyType, cefcChassisCoolingEntry=cefcChassisCoolingEntry, cefcChassisCoolingTable=cefcChassisCoolingTable, cefcChassisPerSlotCoolingCap=cefcChassisPerSlotCoolingCap, cefcChassisPerSlotCoolingUnit=cefcChassisPerSlotCoolingUnit, cefcConnector=cefcConnector, cefcConnectorRating=cefcConnectorRating, cefcConnectorRatingEntry=cefcConnectorRatingEntry, cefcConnectorRatingGroup=cefcConnectorRatingGroup, cefcConnectorRatingTable=cefcConnectorRatingTable, cefcCooling=cefcCooling, cefcCoolingGroup2=cefcCoolingGroup2, cefcCoolingGroup=cefcCoolingGroup, cefcEnablePSOutputChangeNotif=cefcEnablePSOutputChangeNotif, cefcFRUActualInputCurrent=cefcFRUActualInputCurrent, cefcFRUActualOutputCurrent=cefcFRUActualOutputCurrent, cefcFRUCoolingUnitGroup=cefcFRUCoolingUnitGroup, cefcFRUCurrent=cefcFRUCurrent, cefcFRUDrawnInlineCurrent=cefcFRUDrawnInlineCurrent, cefcFRUDrawnSystemCurrent=cefcFRUDrawnSystemCurrent, cefcFRUFan=cefcFRUFan, cefcFRUFanCoolingUnitGroup=cefcFRUFanCoolingUnitGroup, cefcFRUInserted=cefcFRUInserted, cefcFRUMIBNotificationPrefix=cefcFRUMIBNotificationPrefix, cefcFRUPower=cefcFRUPower, cefcFRUPowerAdminStatus=cefcFRUPowerAdminStatus, cefcFRUPowerCapability=cefcFRUPowerCapability, cefcFRUPowerCapabilityGroup=cefcFRUPowerCapabilityGroup, cefcFRUPowerOperStatus=cefcFRUPowerOperStatus, cefcFRUPowerRealTimeStatusGroup=cefcFRUPowerRealTimeStatusGroup, cefcFRUPowerStatusEntry=cefcFRUPowerStatusEntry, cefcFRUPowerStatusTable=cefcFRUPowerStatusTable, cefcFRUPowerSupplyGroupEntry=cefcFRUPowerSupplyGroupEntry, cefcFRUPowerSupplyGroupTable=cefcFRUPowerSupplyGroupTable, cefcFRUPowerSupplyValueEntry=cefcFRUPowerSupplyValueEntry, cefcFRUPowerSupplyValueTable=cefcFRUPowerSupplyValueTable, cefcFRURealTimeCurrent=cefcFRURealTimeCurrent, cefcFRURemoved=cefcFRURemoved, cefcFRUTotalInlineCurrent=cefcFRUTotalInlineCurrent, cefcFRUTotalSystemCurrent=cefcFRUTotalSystemCurrent, cefcFanCoolingCapCapacity=cefcFanCoolingCapCapacity, cefcFanCoolingCapCapacityUnit=cefcFanCoolingCapCapacityUnit, cefcFanCoolingCapCurrent=cefcFanCoolingCapCurrent, cefcFanCoolingCapEntry=cefcFanCoolingCapEntry, cefcFanCoolingCapGroup=cefcFanCoolingCapGroup, cefcFanCoolingCapIndex=cefcFanCoolingCapIndex, cefcFanCoolingCapModeDescr=cefcFanCoolingCapModeDescr, cefcFanCoolingCapTable=cefcFanCoolingCapTable, cefcFanCoolingCapacity=cefcFanCoolingCapacity, cefcFanCoolingCapacityUnit=cefcFanCoolingCapacityUnit, cefcFanCoolingEntry=cefcFanCoolingEntry, cefcFanCoolingGroup=cefcFanCoolingGroup, cefcFanCoolingTable=cefcFanCoolingTable, cefcFanDirectionGroup=cefcFanDirectionGroup, cefcFanEntry=cefcFanEntry, cefcFanSpeed=cefcFanSpeed, cefcFanSpeedGroup=cefcFanSpeedGroup, cefcFanSpeedPercent=cefcFanSpeedPercent, cefcFanTable=cefcFanTable, cefcFanTrayDirection=cefcFanTrayDirection, cefcFanTrayOperStatus=cefcFanTrayOperStatus, cefcFanTrayStatusChange=cefcFanTrayStatusChange, cefcFanTrayStatusEntry=cefcFanTrayStatusEntry, cefcFanTrayStatusTable=cefcFanTrayStatusTable, cefcIntelliModuleEntry=cefcIntelliModuleEntry, cefcIntelliModuleGroup=cefcIntelliModuleGroup, cefcIntelliModuleIPAddr=cefcIntelliModuleIPAddr, cefcIntelliModuleIPAddrType=cefcIntelliModuleIPAddrType, cefcIntelliModuleTable=cefcIntelliModuleTable, cefcMIBCompliances=cefcMIBCompliances, cefcMIBConformance=cefcMIBConformance, cefcMIBEnableStatusNotification=cefcMIBEnableStatusNotification, cefcMIBFanTrayStatusGroup=cefcMIBFanTrayStatusGroup, cefcMIBGroups=cefcMIBGroups, cefcMIBInLinePowerControlGroup=cefcMIBInLinePowerControlGroup, cefcMIBInLinePowerControlGroupRev1=cefcMIBInLinePowerControlGroupRev1, cefcMIBInLinePowerCurrentGroup=cefcMIBInLinePowerCurrentGroup, cefcMIBModuleGroup=cefcMIBModuleGroup, cefcMIBModuleLocalSwitchingGroup=cefcMIBModuleLocalSwitchingGroup, cefcMIBNotificationEnables=cefcMIBNotificationEnables, cefcMIBNotificationEnablesGroup2=cefcMIBNotificationEnablesGroup2, cefcMIBNotificationEnablesGroup=cefcMIBNotificationEnablesGroup, cefcMIBNotifications=cefcMIBNotifications, cefcMIBObjects=cefcMIBObjects, cefcMIBPhysicalGroup=cefcMIBPhysicalGroup, cefcMIBPowerCompliance10=cefcMIBPowerCompliance10, cefcMIBPowerCompliance2=cefcMIBPowerCompliance2, cefcMIBPowerCompliance3=cefcMIBPowerCompliance3, cefcMIBPowerCompliance4=cefcMIBPowerCompliance4, cefcMIBPowerCompliance5=cefcMIBPowerCompliance5, cefcMIBPowerCompliance6=cefcMIBPowerCompliance6, cefcMIBPowerCompliance7=cefcMIBPowerCompliance7, cefcMIBPowerCompliance8=cefcMIBPowerCompliance8, cefcMIBPowerCompliance9=cefcMIBPowerCompliance9, cefcMIBPowerCompliance=cefcMIBPowerCompliance, cefcMIBPowerFRUControlGroup=cefcMIBPowerFRUControlGroup, cefcMIBPowerFRUValueGroup=cefcMIBPowerFRUValueGroup, cefcMIBPowerModeGroup=cefcMIBPowerModeGroup, cefcMIBPowerOperModeGroup=cefcMIBPowerOperModeGroup, cefcMIBPowerRedundancyInfoGroup=cefcMIBPowerRedundancyInfoGroup, cefcMaxDefaultHighInLinePower=cefcMaxDefaultHighInLinePower, cefcMaxDefaultInLinePower=cefcMaxDefaultInLinePower, cefcMgmtNotificationsGroup2=cefcMgmtNotificationsGroup2, cefcMgmtNotificationsGroup3=cefcMgmtNotificationsGroup3, cefcMgmtNotificationsGroup=cefcMgmtNotificationsGroup, cefcModule=cefcModule, cefcModuleAdminStatus=cefcModuleAdminStatus, cefcModuleCooling=cefcModuleCooling, cefcModuleCoolingEntry=cefcModuleCoolingEntry, cefcModuleCoolingTable=cefcModuleCoolingTable, cefcModuleCoolingUnit=cefcModuleCoolingUnit, cefcModuleEntry=cefcModuleEntry, cefcModuleExtGroup=cefcModuleExtGroup, cefcModuleGroupRev1=cefcModuleGroupRev1, cefcModuleLastClearConfigTime=cefcModuleLastClearConfigTime, cefcModuleLocalSwitchingEntry=cefcModuleLocalSwitchingEntry, cefcModuleLocalSwitchingMode=cefcModuleLocalSwitchingMode, cefcModuleLocalSwitchingTable=cefcModuleLocalSwitchingTable, cefcModuleOperStatus=cefcModuleOperStatus, cefcModulePowerConsumption=cefcModulePowerConsumption, cefcModulePowerConsumptionEntry=cefcModulePowerConsumptionEntry, cefcModulePowerConsumptionTable=cefcModulePowerConsumptionTable, cefcModuleResetReason=cefcModuleResetReason, cefcModuleResetReasonDescription=cefcModuleResetReasonDescription, cefcModuleStateChangeReasonDescr=cefcModuleStateChangeReasonDescr, cefcModuleStatusChange=cefcModuleStatusChange, cefcModuleStatusLastChangeTime=cefcModuleStatusLastChangeTime, cefcModuleTable=cefcModuleTable, cefcModuleUpTime=cefcModuleUpTime, cefcPSOutputModeCurrent=cefcPSOutputModeCurrent, cefcPSOutputModeInOperation=cefcPSOutputModeInOperation, cefcPSOutputModeIndex=cefcPSOutputModeIndex, cefcPhysical=cefcPhysical, cefcPhysicalEntry=cefcPhysicalEntry, cefcPhysicalStatus=cefcPhysicalStatus, cefcPhysicalTable=cefcPhysicalTable, cefcPowerCapacity=cefcPowerCapacity, cefcPowerCapacityGroup=cefcPowerCapacityGroup, cefcPowerNonRedundantReason=cefcPowerNonRedundantReason, cefcPowerRedundancyMode=cefcPowerRedundancyMode, cefcPowerRedundancyOperMode=cefcPowerRedundancyOperMode, cefcPowerStatusChange=cefcPowerStatusChange, cefcPowerSupplyActualGroup=cefcPowerSupplyActualGroup, cefcPowerSupplyInputEntry=cefcPowerSupplyInputEntry, cefcPowerSupplyInputIndex=cefcPowerSupplyInputIndex, cefcPowerSupplyInputTable=cefcPowerSupplyInputTable, cefcPowerSupplyInputType=cefcPowerSupplyInputType, cefcPowerSupplyOutputChange=cefcPowerSupplyOutputChange, cefcPowerSupplyOutputEntry=cefcPowerSupplyOutputEntry, cefcPowerSupplyOutputTable=cefcPowerSupplyOutputTable, cefcPowerUnits=cefcPowerUnits, cefcTotalAvailableCurrent=cefcTotalAvailableCurrent, cefcTotalDrawnCurrent=cefcTotalDrawnCurrent, cefcTotalDrawnInlineCurrent=cefcTotalDrawnInlineCurrent, cefcUnrecognizedFRU=cefcUnrecognizedFRU, cefcVmModuleGroup=cefcVmModuleGroup, cefcVmModuleNotifsGroup=cefcVmModuleNotifsGroup, cefcVmModuleOperStatus=cefcVmModuleOperStatus, cefcVmModuleStatusChangeNotif=cefcVmModuleStatusChangeNotif, cefcVmModuleStatusLastChangeTime=cefcVmModuleStatusLastChangeTime, ciscoEntityFRUControlMIB=ciscoEntityFRUControlMIB)
