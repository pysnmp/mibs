#
# PySNMP MIB module CT-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-BROADCAST-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 17:08:38 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ctBroadcast, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctBroadcast")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Bits, ObjectIdentity, MibIdentifier, Integer32, IpAddress, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ModuleIdentity, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "ObjectIdentity", "MibIdentifier", "Integer32", "IpAddress", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ModuleIdentity", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("CT-BROADCAST-MIB", ctBroadcastPeakBroadcastRateTime=ctBroadcastPeakBroadcastRateTime, ctBroadcastPeakBroadcastClear=ctBroadcastPeakBroadcastClear, ctBroadcastCtlTable=ctBroadcastCtlTable, ctBroadcastTotalBroadcastFrames=ctBroadcastTotalBroadcastFrames, ctBroadcastPeakBroadcastRate=ctBroadcastPeakBroadcastRate, ctBroadcastDesiredBroadcastThreshold=ctBroadcastDesiredBroadcastThreshold, ctBroadcastCtlInterface=ctBroadcastCtlInterface, ctBroadcastCtlSlotID=ctBroadcastCtlSlotID, ctBroadcastCtl=ctBroadcastCtl, ctBroadcastCtlEntry=ctBroadcastCtlEntry)
