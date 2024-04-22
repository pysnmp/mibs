#
# PySNMP MIB module CTRON-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-UPS-MIB
# Produced by pysmi-1.1.12 at Mon Apr 22 02:12:17 2024
# On host fv-az569-486 platform Linux version 6.5.0-1018-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ctUPowerSupply, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctUPowerSupply")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, iso, TimeTicks, MibIdentifier, Gauge32, NotificationType, Integer32, IpAddress, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "iso", "TimeTicks", "MibIdentifier", "Gauge32", "NotificationType", "Integer32", "IpAddress", "Counter64", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctUPS = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1))
ctUpsID = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268))).clone(namedValues=NamedValues(("other", 1), ("aPCModel370", 257), ("aPCModel400", 258), ("aPCModel600", 259), ("aPCModel900", 260), ("aPCModel1250", 261), ("aPCModel2000", 262), ("matrix3000", 263), ("matrix5000", 264), ("su700", 265), ("su1400", 266), ("su2000XL", 267), ("aPCGeneric", 268)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctUpsID.setStatus('mandatory')
ctUpsUpTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctUpsUpTime.setStatus('deprecated')
ctUpsDisable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctUpsDisable.setStatus('deprecated')
ctUpsDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctUpsDisconnect.setStatus('mandatory')
ctUpsTest = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unitOK", 1), ("unitFailed", 2), ("badBattery", 3), ("noRecentTest", 4), ("underTest", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctUpsTest.setStatus('mandatory')
ctUpsBatteryCapacity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctUpsBatteryCapacity.setStatus('mandatory')
ctUpsACLineVoltsIn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctUpsACLineVoltsIn.setStatus('mandatory')
ctUpsBatteryVoltsOut = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctUpsBatteryVoltsOut.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-UPS-MIB", ctUpsUpTime=ctUpsUpTime, ctUpsBatteryVoltsOut=ctUpsBatteryVoltsOut, ctUpsID=ctUpsID, ctUpsTest=ctUpsTest, ctUPS=ctUPS, ctUpsACLineVoltsIn=ctUpsACLineVoltsIn, ctUpsDisable=ctUpsDisable, ctUpsBatteryCapacity=ctUpsBatteryCapacity, ctUpsDisconnect=ctUpsDisconnect)
