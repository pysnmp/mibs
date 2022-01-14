#
# PySNMP MIB module WAYSTREAM-IGMP-CACHE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/waystream/WAYSTREAM-IGMP-CACHE-MIB
# Produced by pysmi-1.1.8 at Fri Jan 14 00:04:01 2022
# On host fv-az74-435 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, TimeTicks, Counter64, Unsigned32, Counter32, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, IpAddress, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "TimeTicks", "Counter64", "Unsigned32", "Counter32", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "IpAddress", "Bits", "MibIdentifier")
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
mibBuilder.exportSymbols("WAYSTREAM-IGMP-CACHE-MIB", wsIgmp=wsIgmp, wsIgmpCacheAddress=wsIgmpCacheAddress, wsIgmpCacheUpTime=wsIgmpCacheUpTime, PYSNMP_MODULE_ID=wsIgmp, wsIgmpCacheEntry=wsIgmpCacheEntry, wsIgmpCacheTable=wsIgmpCacheTable, wsIgmpCacheReporter=wsIgmpCacheReporter, wsIgmpCacheIfIndex=wsIgmpCacheIfIndex)
