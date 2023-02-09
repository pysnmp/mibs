#
# PySNMP MIB module OG-FAILOVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-FAILOVER-MIB
# Produced by pysmi-1.1.8 at Thu Feb  9 14:05:54 2023
# On host fv-az796-878 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, Bits, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Gauge32, ModuleIdentity, TimeTicks, MibIdentifier, iso, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Gauge32", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ogFailoverMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 15))
ogFailoverMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))
if mibBuilder.loadTexts: ogFailoverMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogFailoverMib.setOrganization('Opengear Inc.')
ogFailoverMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10))
ogfovrEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1))
ogfovrEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1), )
if mibBuilder.loadTexts: ogfovrEventTable.setStatus('current')
ogfovrEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1), ).setIndexNames((0, "OG-FAILOVER-MIB", "ogfovrEventIndex"))
if mibBuilder.loadTexts: ogfovrEventEntry.setStatus('current')
ogfovrEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogfovrEventIndex.setStatus('current')
ogfovrEventPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogfovrEventPrimary.setStatus('current')
ogfovrEventSecondary = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogfovrEventSecondary.setStatus('current')
ogFailoverMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 2))
ogfovrMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 2, 0))
ogfovrEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 15, 2, 0, 200)).setObjects(("OG-FAILOVER-MIB", "ogfovrEventPrimary"), ("OG-FAILOVER-MIB", "ogfovrEventSecondary"))
if mibBuilder.loadTexts: ogfovrEventOccurred.setStatus('current')
ogFailoverMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3))
ogFailoverMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 1))
ogFailoverMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2))
ogFailoverMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 1, 1)).setObjects(("OG-FAILOVER-MIB", "ogFailoverMibGroup"), ("OG-FAILOVER-MIB", "ogfovrNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogFailoverMibCompliance = ogFailoverMibCompliance.setStatus('current')
ogFailoverMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2, 1)).setObjects(("OG-FAILOVER-MIB", "ogfovrEventPrimary"), ("OG-FAILOVER-MIB", "ogfovrEventSecondary"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogFailoverMibGroup = ogFailoverMibGroup.setStatus('current')
ogfovrNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2, 2)).setObjects(("OG-FAILOVER-MIB", "ogfovrEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogfovrNotificationsGroup = ogfovrNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OG-FAILOVER-MIB", ogFailoverMibConformance=ogFailoverMibConformance, ogFailoverMibGroup=ogFailoverMibGroup, ogfovrEventIndex=ogfovrEventIndex, ogfovrEventOccurred=ogfovrEventOccurred, ogFailoverMib=ogFailoverMib, ogfovrEventSecondary=ogfovrEventSecondary, ogfovrNotificationsGroup=ogfovrNotificationsGroup, ogFailoverMibNotificationPrefix=ogFailoverMibNotificationPrefix, ogFailoverMibGroups=ogFailoverMibGroups, ogFailoverMibCompliances=ogFailoverMibCompliances, ogFailoverMibCompliance=ogFailoverMibCompliance, ogfovrEventTable=ogfovrEventTable, ogFailoverMibObjects=ogFailoverMibObjects, PYSNMP_MODULE_ID=ogFailoverMib, ogfovrEventEntry=ogfovrEventEntry, ogfovrEventPrimary=ogfovrEventPrimary, ogfovrEvent=ogfovrEvent, ogfovrMibNotifications=ogfovrMibNotifications)
