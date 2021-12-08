#
# PySNMP MIB module OG-FAILOVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-FAILOVER-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 21:23:36 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, Gauge32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Unsigned32, Integer32, Counter32, NotificationType, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Gauge32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Unsigned32", "Integer32", "Counter32", "NotificationType", "iso", "IpAddress")
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
mibBuilder.exportSymbols("OG-FAILOVER-MIB", ogfovrEvent=ogfovrEvent, ogfovrEventPrimary=ogfovrEventPrimary, ogfovrEventSecondary=ogfovrEventSecondary, ogfovrEventTable=ogfovrEventTable, ogFailoverMibObjects=ogFailoverMibObjects, ogFailoverMibCompliances=ogFailoverMibCompliances, ogfovrNotificationsGroup=ogfovrNotificationsGroup, ogFailoverMibGroups=ogFailoverMibGroups, ogFailoverMib=ogFailoverMib, ogFailoverMibGroup=ogFailoverMibGroup, ogfovrEventEntry=ogfovrEventEntry, ogfovrMibNotifications=ogfovrMibNotifications, PYSNMP_MODULE_ID=ogFailoverMib, ogFailoverMibConformance=ogFailoverMibConformance, ogFailoverMibNotificationPrefix=ogFailoverMibNotificationPrefix, ogfovrEventOccurred=ogfovrEventOccurred, ogfovrEventIndex=ogfovrEventIndex, ogFailoverMibCompliance=ogFailoverMibCompliance)
