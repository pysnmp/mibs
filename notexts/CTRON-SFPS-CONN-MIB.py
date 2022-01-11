#
# PySNMP MIB module CTRON-SFPS-CONN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-CONN-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:21:40 2022
# On host fv-az74-997 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
sfpsServiceCenter, = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsServiceCenter")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Gauge32, IpAddress, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Counter32, TimeTicks, Integer32, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Gauge32", "IpAddress", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Counter32", "TimeTicks", "Integer32", "Counter64", "Unsigned32")
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
mibBuilder.exportSymbols("CTRON-SFPS-CONN-MIB", sfpsServiceCenterConnectTable=sfpsServiceCenterConnectTable, sfpsServiceCenterConnectOperStatus=sfpsServiceCenterConnectOperStatus, sfpsServiceCenterConnectEntry=sfpsServiceCenterConnectEntry, sfpsServiceCenterConnectResponses=sfpsServiceCenterConnectResponses, sfpsServiceCenterConnectAdminStatus=sfpsServiceCenterConnectAdminStatus, sfpsServiceCenterConnectMetric=sfpsServiceCenterConnectMetric, sfpsServiceCenterConnectName=sfpsServiceCenterConnectName, sfpsServiceCenterConnectAddress=sfpsServiceCenterConnectAddress, sfpsServiceCenterConnectRequests=sfpsServiceCenterConnectRequests, HexInteger=HexInteger, sfpsServiceCenterConnectStatusTime=sfpsServiceCenterConnectStatusTime)
