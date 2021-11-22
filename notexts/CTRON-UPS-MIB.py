#
# PySNMP MIB module CTRON-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-UPS-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:34:29 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ctUPowerSupply, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctUPowerSupply")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, iso, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Counter32, ModuleIdentity, TimeTicks, Unsigned32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "iso", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Counter32", "ModuleIdentity", "TimeTicks", "Unsigned32", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CTRON-UPS-MIB", ctUpsID=ctUpsID, ctUPS=ctUPS, ctUpsBatteryCapacity=ctUpsBatteryCapacity, ctUpsBatteryVoltsOut=ctUpsBatteryVoltsOut, ctUpsDisconnect=ctUpsDisconnect, ctUpsDisable=ctUpsDisable, ctUpsTest=ctUpsTest, ctUpsUpTime=ctUpsUpTime, ctUpsACLineVoltsIn=ctUpsACLineVoltsIn)
