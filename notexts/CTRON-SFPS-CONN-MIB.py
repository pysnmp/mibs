#
# PySNMP MIB module CTRON-SFPS-CONN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-CONN-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 16:42:44 2022
# On host fv-az119-924 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
sfpsServiceCenter, = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsServiceCenter")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Bits, Counter64, iso, ObjectIdentity, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, NotificationType, Counter32, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Counter64", "iso", "ObjectIdentity", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "NotificationType", "Counter32", "Unsigned32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class HexInteger(Integer32):
    pass

sfpsServiceCenterConnectTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4), )
if mibBuilder.loadTexts: sfpsServiceCenterConnectTable.setStatus('mandatory')
sfpsServiceCenterConnectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1), ).setIndexNames((0, "CTRON-SFPS-CONN-MIB", "sfpsServiceCenterConnectAddress"))
if mibBuilder.loadTexts: sfpsServiceCenterConnectEntry.setStatus('mandatory')
sfpsServiceCenterConnectAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 1), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterConnectAddress.setStatus('mandatory')
sfpsServiceCenterConnectMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterConnectMetric.setStatus('mandatory')
sfpsServiceCenterConnectName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterConnectName.setStatus('mandatory')
sfpsServiceCenterConnectOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterConnectOperStatus.setStatus('mandatory')
sfpsServiceCenterConnectAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsServiceCenterConnectAdminStatus.setStatus('mandatory')
sfpsServiceCenterConnectStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterConnectStatusTime.setStatus('mandatory')
sfpsServiceCenterConnectRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterConnectRequests.setStatus('mandatory')
sfpsServiceCenterConnectResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsServiceCenterConnectResponses.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-CONN-MIB", sfpsServiceCenterConnectResponses=sfpsServiceCenterConnectResponses, sfpsServiceCenterConnectAddress=sfpsServiceCenterConnectAddress, sfpsServiceCenterConnectMetric=sfpsServiceCenterConnectMetric, sfpsServiceCenterConnectEntry=sfpsServiceCenterConnectEntry, sfpsServiceCenterConnectOperStatus=sfpsServiceCenterConnectOperStatus, sfpsServiceCenterConnectRequests=sfpsServiceCenterConnectRequests, HexInteger=HexInteger, sfpsServiceCenterConnectTable=sfpsServiceCenterConnectTable, sfpsServiceCenterConnectStatusTime=sfpsServiceCenterConnectStatusTime, sfpsServiceCenterConnectName=sfpsServiceCenterConnectName, sfpsServiceCenterConnectAdminStatus=sfpsServiceCenterConnectAdminStatus)
