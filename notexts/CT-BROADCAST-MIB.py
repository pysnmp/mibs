#
# PySNMP MIB module CT-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-BROADCAST-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:22:25 2024
# On host fv-az1022-995 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ctBroadcast, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctBroadcast")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, IpAddress, MibIdentifier, Integer32, Gauge32, iso, ObjectIdentity, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "IpAddress", "MibIdentifier", "Integer32", "Gauge32", "iso", "ObjectIdentity", "Counter64", "Unsigned32")
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
mibBuilder.exportSymbols("CT-BROADCAST-MIB", ctBroadcastCtlEntry=ctBroadcastCtlEntry, ctBroadcastTotalBroadcastFrames=ctBroadcastTotalBroadcastFrames, ctBroadcastPeakBroadcastRateTime=ctBroadcastPeakBroadcastRateTime, ctBroadcastPeakBroadcastRate=ctBroadcastPeakBroadcastRate, ctBroadcastPeakBroadcastClear=ctBroadcastPeakBroadcastClear, ctBroadcastDesiredBroadcastThreshold=ctBroadcastDesiredBroadcastThreshold, ctBroadcastCtl=ctBroadcastCtl, ctBroadcastCtlTable=ctBroadcastCtlTable, ctBroadcastCtlInterface=ctBroadcastCtlInterface, ctBroadcastCtlSlotID=ctBroadcastCtlSlotID)
