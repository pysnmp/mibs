#
# PySNMP MIB module WAYSTREAM-IGMP-CACHE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/waystream/WAYSTREAM-IGMP-CACHE-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 09:51:16 2023
# On host fv-az502-117 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, IpAddress, Gauge32, MibIdentifier, NotificationType, ObjectIdentity, Counter32, Counter64, Unsigned32, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "IpAddress", "Gauge32", "MibIdentifier", "NotificationType", "ObjectIdentity", "Counter32", "Counter64", "Unsigned32", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wsMgmt, = mibBuilder.importSymbols("WAYSTREAM-SMI", "wsMgmt")
wsIgmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303, 4, 13))
wsIgmp.setRevisions(('2017-02-10 11:00', '2011-01-11 17:54', '2009-04-29 13:49', '2009-03-23 11:25', '2008-04-30 13:48', '2007-06-13 14:37',))
if mibBuilder.loadTexts: wsIgmp.setLastUpdated('201702101100Z')
if mibBuilder.loadTexts: wsIgmp.setOrganization('Waystream AB')
wsIgmpCacheTable = MibTable((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2), )
if mibBuilder.loadTexts: wsIgmpCacheTable.setStatus('current')
wsIgmpCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1), ).setIndexNames((0, "WAYSTREAM-IGMP-CACHE-MIB", "wsIgmpCacheAddress"), (0, "WAYSTREAM-IGMP-CACHE-MIB", "wsIgmpCacheIfIndex"), (0, "WAYSTREAM-IGMP-CACHE-MIB", "wsIgmpCacheReporter"))
if mibBuilder.loadTexts: wsIgmpCacheEntry.setStatus('current')
wsIgmpCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: wsIgmpCacheAddress.setStatus('current')
wsIgmpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: wsIgmpCacheIfIndex.setStatus('current')
wsIgmpCacheReporter = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 3), IpAddress())
if mibBuilder.loadTexts: wsIgmpCacheReporter.setStatus('current')
wsIgmpCacheUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsIgmpCacheUpTime.setStatus('current')
mibBuilder.exportSymbols("WAYSTREAM-IGMP-CACHE-MIB", wsIgmpCacheEntry=wsIgmpCacheEntry, wsIgmpCacheTable=wsIgmpCacheTable, wsIgmpCacheUpTime=wsIgmpCacheUpTime, wsIgmp=wsIgmp, wsIgmpCacheIfIndex=wsIgmpCacheIfIndex, wsIgmpCacheAddress=wsIgmpCacheAddress, PYSNMP_MODULE_ID=wsIgmp, wsIgmpCacheReporter=wsIgmpCacheReporter)
