#
# PySNMP MIB module SAEUROPE-ADMINISTRATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saeurope/SAEUROPE-ADMINISTRATION-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 16:02:50 2024
# On host fv-az1205-935 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
common, = mibBuilder.importSymbols("SAEUROPE-ROOT-MIB", "common")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, NotificationType, Bits, iso, Integer32, Counter32, MibIdentifier, Gauge32, TimeTicks, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "NotificationType", "Bits", "iso", "Integer32", "Counter32", "MibIdentifier", "Gauge32", "TimeTicks", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
saEuropeAdministration = MibIdentifier((1, 3, 6, 1, 4, 1, 1482, 20, 1, 6))
adminVendor = MibScalar((1, 3, 6, 1, 4, 1, 1482, 20, 1, 6, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adminVendor.setStatus('mandatory')
adminModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 1482, 20, 1, 6, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adminModelNumber.setStatus('mandatory')
adminSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 1482, 20, 1, 6, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adminSerialNumber.setStatus('mandatory')
adminVendorInfo = MibScalar((1, 3, 6, 1, 4, 1, 1482, 20, 1, 6, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adminVendorInfo.setStatus('mandatory')
adminAlarmDetectionControl = MibScalar((1, 3, 6, 1, 4, 1, 1482, 20, 1, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("detectionDisabled", 1), ("detectionEnabled", 2), ("detectionEnabledAndRegenerate", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAlarmDetectionControl.setStatus('mandatory')
adminTime = MibScalar((1, 3, 6, 1, 4, 1, 1482, 20, 1, 6, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adminTime.setStatus('mandatory')
adminState = MibScalar((1, 3, 6, 1, 4, 1, 1482, 20, 1, 6, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("responding", 1), ("localControl", 2), ("maintenance", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adminState.setStatus('mandatory')
adminRestart = MibScalar((1, 3, 6, 1, 4, 1, 1482, 20, 1, 6, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("warmRestart", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminRestart.setStatus('mandatory')
mibBuilder.exportSymbols("SAEUROPE-ADMINISTRATION-MIB", adminSerialNumber=adminSerialNumber, adminVendorInfo=adminVendorInfo, adminRestart=adminRestart, adminTime=adminTime, adminAlarmDetectionControl=adminAlarmDetectionControl, adminVendor=adminVendor, saEuropeAdministration=saEuropeAdministration, adminState=adminState, adminModelNumber=adminModelNumber)
