#
# PySNMP MIB module CTRON-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-UPS-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 10:04:28 2024
# On host fv-az1771-969 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ctUPowerSupply, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctUPowerSupply")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Gauge32, Unsigned32, ModuleIdentity, TimeTicks, Integer32, Counter32, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Gauge32", "Unsigned32", "ModuleIdentity", "TimeTicks", "Integer32", "Counter32", "iso", "IpAddress")
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
mibBuilder.exportSymbols("CTRON-UPS-MIB", ctUpsBatteryCapacity=ctUpsBatteryCapacity, ctUpsBatteryVoltsOut=ctUpsBatteryVoltsOut, ctUpsTest=ctUpsTest, ctUpsDisconnect=ctUpsDisconnect, ctUpsDisable=ctUpsDisable, ctUpsID=ctUpsID, ctUPS=ctUPS, ctUpsACLineVoltsIn=ctUpsACLineVoltsIn, ctUpsUpTime=ctUpsUpTime)
