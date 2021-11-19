#
# PySNMP MIB module OG-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-UPS-MIB
# Produced by pysmi-1.1.0 at Fri Nov 19 14:46:52 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Bits, iso, Gauge32, Integer32, ObjectIdentity, IpAddress, Counter32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Bits", "iso", "Gauge32", "Integer32", "ObjectIdentity", "IpAddress", "Counter32", "NotificationType", "Counter64")
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
mibBuilder.exportSymbols("OG-UPS-MIB", ogNetUpsMibConformance=ogNetUpsMibConformance, ognupsEventTable=ognupsEventTable, ogNetUpsMibCompliance=ogNetUpsMibCompliance, ognupsEvent=ognupsEvent, ogNetUpsMibGroups=ogNetUpsMibGroups, ogNetUpsMibGroup=ogNetUpsMibGroup, ognupsEventEntry=ognupsEventEntry, ognupsMibNotifications=ognupsMibNotifications, ognupsEventName=ognupsEventName, ognupsEventIndex=ognupsEventIndex, ognupsEventType=ognupsEventType, ogNetUpsMibCompliances=ogNetUpsMibCompliances, ognupsNotificationsGroup=ognupsNotificationsGroup, ogNetUpsMib=ogNetUpsMib, PYSNMP_MODULE_ID=ogNetUpsMib, ogNetUpsMibNotificationPrefix=ogNetUpsMibNotificationPrefix, ognupsEventOccurred=ognupsEventOccurred, ogNetUpsMibObjects=ogNetUpsMibObjects)
