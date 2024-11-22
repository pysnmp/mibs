#
# PySNMP MIB module CT-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-BROADCAST-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 15:59:34 2024
# On host fv-az1245-338 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ctBroadcast, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctBroadcast")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Gauge32, ModuleIdentity, iso, Unsigned32, Counter64, Bits, Integer32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Gauge32", "ModuleIdentity", "iso", "Unsigned32", "Counter64", "Bits", "Integer32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks")
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
mibBuilder.exportSymbols("CT-BROADCAST-MIB", ctBroadcastPeakBroadcastClear=ctBroadcastPeakBroadcastClear, ctBroadcastTotalBroadcastFrames=ctBroadcastTotalBroadcastFrames, ctBroadcastCtlEntry=ctBroadcastCtlEntry, ctBroadcastPeakBroadcastRate=ctBroadcastPeakBroadcastRate, ctBroadcastCtlTable=ctBroadcastCtlTable, ctBroadcastCtlSlotID=ctBroadcastCtlSlotID, ctBroadcastCtlInterface=ctBroadcastCtlInterface, ctBroadcastCtl=ctBroadcastCtl, ctBroadcastPeakBroadcastRateTime=ctBroadcastPeakBroadcastRateTime, ctBroadcastDesiredBroadcastThreshold=ctBroadcastDesiredBroadcastThreshold)
