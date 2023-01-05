#
# PySNMP MIB module CT-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-BROADCAST-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 09:05:06 2023
# On host fv-az351-145 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ctBroadcast, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctBroadcast")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Counter64, IpAddress, iso, Integer32, Unsigned32, MibIdentifier, Gauge32, ObjectIdentity, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Counter64", "IpAddress", "iso", "Integer32", "Unsigned32", "MibIdentifier", "Gauge32", "ObjectIdentity", "NotificationType", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctBroadcastCtl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1))
ctBroadcastCtlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1), )
if mibBuilder.loadTexts: ctBroadcastCtlTable.setStatus('mandatory')
ctBroadcastCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1), ).setIndexNames((0, "CT-BROADCAST-MIB", "ctBroadcastCtlSlotID"), (0, "CT-BROADCAST-MIB", "ctBroadcastCtlInterface"))
if mibBuilder.loadTexts: ctBroadcastCtlEntry.setStatus('mandatory')
ctBroadcastCtlSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBroadcastCtlSlotID.setStatus('mandatory')
ctBroadcastCtlInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBroadcastCtlInterface.setStatus('mandatory')
ctBroadcastTotalBroadcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBroadcastTotalBroadcastFrames.setStatus('mandatory')
ctBroadcastPeakBroadcastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBroadcastPeakBroadcastRate.setStatus('mandatory')
ctBroadcastPeakBroadcastRateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBroadcastPeakBroadcastRateTime.setStatus('mandatory')
ctBroadcastPeakBroadcastClear = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("noClear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBroadcastPeakBroadcastClear.setStatus('mandatory')
ctBroadcastDesiredBroadcastThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBroadcastDesiredBroadcastThreshold.setStatus('mandatory')
mibBuilder.exportSymbols("CT-BROADCAST-MIB", ctBroadcastCtlInterface=ctBroadcastCtlInterface, ctBroadcastCtlEntry=ctBroadcastCtlEntry, ctBroadcastPeakBroadcastRateTime=ctBroadcastPeakBroadcastRateTime, ctBroadcastCtl=ctBroadcastCtl, ctBroadcastCtlSlotID=ctBroadcastCtlSlotID, ctBroadcastPeakBroadcastClear=ctBroadcastPeakBroadcastClear, ctBroadcastPeakBroadcastRate=ctBroadcastPeakBroadcastRate, ctBroadcastCtlTable=ctBroadcastCtlTable, ctBroadcastTotalBroadcastFrames=ctBroadcastTotalBroadcastFrames, ctBroadcastDesiredBroadcastThreshold=ctBroadcastDesiredBroadcastThreshold)
