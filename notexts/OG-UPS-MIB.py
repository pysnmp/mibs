#
# PySNMP MIB module OG-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-UPS-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 08:52:58 2023
# On host fv-az447-590 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, Gauge32, Bits, ObjectIdentity, TimeTicks, Counter32, Unsigned32, NotificationType, MibIdentifier, iso, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Gauge32", "Bits", "ObjectIdentity", "TimeTicks", "Counter32", "Unsigned32", "NotificationType", "MibIdentifier", "iso", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogNetUpsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 16))
ogNetUpsMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-06-13 11:00',))
if mibBuilder.loadTexts: ogNetUpsMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogNetUpsMib.setOrganization('Opengear Inc.')
ogNetUpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10))
ognupsEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1))
ognupsEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1), )
if mibBuilder.loadTexts: ognupsEventTable.setStatus('current')
ognupsEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1), ).setIndexNames((0, "OG-UPS-MIB", "ognupsEventIndex"))
if mibBuilder.loadTexts: ognupsEventEntry.setStatus('current')
ognupsEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ognupsEventIndex.setStatus('current')
ognupsEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ognupsEventName.setStatus('current')
ognupsEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 16, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ognupsEventType.setStatus('current')
ogNetUpsMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 2))
ognupsMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 2, 0))
ognupsEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 16, 2, 0, 200)).setObjects(("OG-UPS-MIB", "ognupsEventName"), ("OG-UPS-MIB", "ognupsEventType"))
if mibBuilder.loadTexts: ognupsEventOccurred.setStatus('current')
ogNetUpsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3))
ogNetUpsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 1))
ogNetUpsMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 2))
ogNetUpsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 1, 1)).setObjects(("OG-UPS-MIB", "ogNetUpsMibGroup"), ("OG-UPS-MIB", "ognupsNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogNetUpsMibCompliance = ogNetUpsMibCompliance.setStatus('current')
ogNetUpsMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 2, 1)).setObjects(("OG-UPS-MIB", "ognupsEventName"), ("OG-UPS-MIB", "ognupsEventType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogNetUpsMibGroup = ogNetUpsMibGroup.setStatus('current')
ognupsNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 16, 3, 2, 2)).setObjects(("OG-UPS-MIB", "ognupsEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ognupsNotificationsGroup = ognupsNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OG-UPS-MIB", ognupsMibNotifications=ognupsMibNotifications, ognupsEventName=ognupsEventName, ogNetUpsMibCompliances=ogNetUpsMibCompliances, ognupsNotificationsGroup=ognupsNotificationsGroup, ogNetUpsMibObjects=ogNetUpsMibObjects, ogNetUpsMibGroups=ogNetUpsMibGroups, ognupsEventType=ognupsEventType, ogNetUpsMibGroup=ogNetUpsMibGroup, ognupsEventEntry=ognupsEventEntry, ogNetUpsMibNotificationPrefix=ogNetUpsMibNotificationPrefix, ognupsEventOccurred=ognupsEventOccurred, ogNetUpsMibCompliance=ogNetUpsMibCompliance, ogNetUpsMib=ogNetUpsMib, ogNetUpsMibConformance=ogNetUpsMibConformance, ognupsEventIndex=ognupsEventIndex, ognupsEventTable=ognupsEventTable, ognupsEvent=ognupsEvent, PYSNMP_MODULE_ID=ogNetUpsMib)
