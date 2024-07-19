#
# PySNMP MIB module SAEUROPE-ADMINISTRATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saeurope/SAEUROPE-ADMINISTRATION-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 09:41:02 2024
# On host fv-az1110-714 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
common, = mibBuilder.importSymbols("SAEUROPE-ROOT-MIB", "common")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, ModuleIdentity, IpAddress, Counter64, NotificationType, Gauge32, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "ModuleIdentity", "IpAddress", "Counter64", "NotificationType", "Gauge32", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "ObjectIdentity", "Bits")
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
mibBuilder.exportSymbols("SAEUROPE-ADMINISTRATION-MIB", adminState=adminState, adminRestart=adminRestart, adminModelNumber=adminModelNumber, saEuropeAdministration=saEuropeAdministration, adminTime=adminTime, adminVendor=adminVendor, adminVendorInfo=adminVendorInfo, adminAlarmDetectionControl=adminAlarmDetectionControl, adminSerialNumber=adminSerialNumber)
