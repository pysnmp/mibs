#
# PySNMP MIB module CTRON-SFPS-CONN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-CONN-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 09:11:03 2024
# On host fv-az2021-432 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
sfpsServiceCenter, = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsServiceCenter")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, Integer32, Unsigned32, ModuleIdentity, MibIdentifier, NotificationType, Counter64, ObjectIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Integer32", "Unsigned32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Counter64", "ObjectIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso")
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
mibBuilder.exportSymbols("CTRON-SFPS-CONN-MIB", sfpsServiceCenterConnectStatusTime=sfpsServiceCenterConnectStatusTime, sfpsServiceCenterConnectRequests=sfpsServiceCenterConnectRequests, sfpsServiceCenterConnectMetric=sfpsServiceCenterConnectMetric, sfpsServiceCenterConnectOperStatus=sfpsServiceCenterConnectOperStatus, sfpsServiceCenterConnectAddress=sfpsServiceCenterConnectAddress, sfpsServiceCenterConnectAdminStatus=sfpsServiceCenterConnectAdminStatus, sfpsServiceCenterConnectResponses=sfpsServiceCenterConnectResponses, sfpsServiceCenterConnectTable=sfpsServiceCenterConnectTable, HexInteger=HexInteger, sfpsServiceCenterConnectEntry=sfpsServiceCenterConnectEntry, sfpsServiceCenterConnectName=sfpsServiceCenterConnectName)
