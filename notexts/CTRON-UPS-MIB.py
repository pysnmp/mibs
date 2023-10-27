#
# PySNMP MIB module CTRON-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-UPS-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 07:40:14 2023
# On host fv-az1236-588 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ctUPowerSupply, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctUPowerSupply")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, Bits, Integer32, TimeTicks, Gauge32, MibIdentifier, ObjectIdentity, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Bits", "Integer32", "TimeTicks", "Gauge32", "MibIdentifier", "ObjectIdentity", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "NotificationType")
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
mibBuilder.exportSymbols("CTRON-UPS-MIB", ctUpsACLineVoltsIn=ctUpsACLineVoltsIn, ctUpsBatteryCapacity=ctUpsBatteryCapacity, ctUpsID=ctUpsID, ctUpsUpTime=ctUpsUpTime, ctUPS=ctUPS, ctUpsDisable=ctUpsDisable, ctUpsTest=ctUpsTest, ctUpsBatteryVoltsOut=ctUpsBatteryVoltsOut, ctUpsDisconnect=ctUpsDisconnect)
