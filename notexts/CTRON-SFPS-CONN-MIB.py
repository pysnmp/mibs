#
# PySNMP MIB module CTRON-SFPS-CONN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-CONN-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 08:03:41 2023
# On host fv-az447-19 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
sfpsServiceCenter, = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsServiceCenter")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, iso, TimeTicks, Bits, ObjectIdentity, Integer32, IpAddress, Counter64, ModuleIdentity, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "iso", "TimeTicks", "Bits", "ObjectIdentity", "Integer32", "IpAddress", "Counter64", "ModuleIdentity", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CTRON-SFPS-CONN-MIB", sfpsServiceCenterConnectStatusTime=sfpsServiceCenterConnectStatusTime, sfpsServiceCenterConnectEntry=sfpsServiceCenterConnectEntry, HexInteger=HexInteger, sfpsServiceCenterConnectRequests=sfpsServiceCenterConnectRequests, sfpsServiceCenterConnectAdminStatus=sfpsServiceCenterConnectAdminStatus, sfpsServiceCenterConnectAddress=sfpsServiceCenterConnectAddress, sfpsServiceCenterConnectName=sfpsServiceCenterConnectName, sfpsServiceCenterConnectTable=sfpsServiceCenterConnectTable, sfpsServiceCenterConnectMetric=sfpsServiceCenterConnectMetric, sfpsServiceCenterConnectResponses=sfpsServiceCenterConnectResponses, sfpsServiceCenterConnectOperStatus=sfpsServiceCenterConnectOperStatus)
