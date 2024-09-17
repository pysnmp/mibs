#
# PySNMP MIB module SAEUROPE-ADMINISTRATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/saeurope/SAEUROPE-ADMINISTRATION-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 10:05:21 2024
# On host fv-az1427-100 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
common, = mibBuilder.importSymbols("SAEUROPE-ROOT-MIB", "common")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, Unsigned32, iso, NotificationType, Counter64, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, MibIdentifier, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Unsigned32", "iso", "NotificationType", "Counter64", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "MibIdentifier", "IpAddress", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SAEUROPE-ADMINISTRATION-MIB", adminModelNumber=adminModelNumber, adminSerialNumber=adminSerialNumber, adminVendorInfo=adminVendorInfo, adminTime=adminTime, adminRestart=adminRestart, adminVendor=adminVendor, saEuropeAdministration=saEuropeAdministration, adminState=adminState, adminAlarmDetectionControl=adminAlarmDetectionControl)
