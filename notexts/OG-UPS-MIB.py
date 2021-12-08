#
# PySNMP MIB module OG-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-UPS-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 20:11:57 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Counter64, ObjectIdentity, Integer32, Bits, IpAddress, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, NotificationType, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "Integer32", "Bits", "IpAddress", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "NotificationType", "ModuleIdentity", "TimeTicks")
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
mibBuilder.exportSymbols("OG-UPS-MIB", ogNetUpsMibCompliance=ogNetUpsMibCompliance, ogNetUpsMibNotificationPrefix=ogNetUpsMibNotificationPrefix, ognupsEventOccurred=ognupsEventOccurred, ognupsEventType=ognupsEventType, ognupsEventIndex=ognupsEventIndex, ogNetUpsMibConformance=ogNetUpsMibConformance, ogNetUpsMibGroup=ogNetUpsMibGroup, ogNetUpsMib=ogNetUpsMib, ognupsEventTable=ognupsEventTable, ognupsMibNotifications=ognupsMibNotifications, ognupsEventEntry=ognupsEventEntry, ogNetUpsMibObjects=ogNetUpsMibObjects, ogNetUpsMibCompliances=ogNetUpsMibCompliances, ogNetUpsMibGroups=ogNetUpsMibGroups, ognupsNotificationsGroup=ognupsNotificationsGroup, ognupsEventName=ognupsEventName, PYSNMP_MODULE_ID=ogNetUpsMib, ognupsEvent=ognupsEvent)
