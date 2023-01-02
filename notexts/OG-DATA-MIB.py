#
# PySNMP MIB module OG-DATA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-DATA-MIB
# Produced by pysmi-1.1.8 at Mon Jan  2 13:26:55 2023
# On host fv-az552-501 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Integer32, Unsigned32, iso, Gauge32, TimeTicks, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Unsigned32", "iso", "Gauge32", "TimeTicks", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogDataMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 17))
ogDataMib.setRevisions(('2013-08-11 00:00', '2011-01-30 21:10',))
if mibBuilder.loadTexts: ogDataMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogDataMib.setOrganization('Opengear Inc.')
ogDataMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 17, 10))
ogdataEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1))
ogdataEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1), )
if mibBuilder.loadTexts: ogdataEventTable.setStatus('current')
ogdataEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1), ).setIndexNames((0, "OG-DATA-MIB", "ogdataEventIndex"))
if mibBuilder.loadTexts: ogdataEventEntry.setStatus('current')
ogdataEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogdataEventIndex.setStatus('current')
ogdataEventBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventBytes.setStatus('current')
ogdataEventSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventSeconds.setStatus('current')
ogdataEventDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventDevice.setStatus('current')
ogdataEventState = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 17, 10, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogdataEventState.setStatus('current')
ogDataMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 17, 2))
ogdataMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 17, 2, 0))
ogdataEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 17, 2, 0, 200)).setObjects(("OG-DATA-MIB", "ogdataEventBytes"), ("OG-DATA-MIB", "ogdataEventSeconds"), ("OG-DATA-MIB", "ogdataEventDevice"), ("OG-DATA-MIB", "ogdataEventState"))
if mibBuilder.loadTexts: ogdataEventOccurred.setStatus('current')
ogDataMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 17, 3))
ogDataMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 17, 3, 1))
ogDataMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 17, 3, 2))
ogDataMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 17, 3, 1, 1)).setObjects(("OG-DATA-MIB", "ogDataMibGroup"), ("OG-DATA-MIB", "ogdataNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogDataMibCompliance = ogDataMibCompliance.setStatus('current')
ogDataMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 17, 3, 2, 1)).setObjects(("OG-DATA-MIB", "ogdataEventBytes"), ("OG-DATA-MIB", "ogdataEventSeconds"), ("OG-DATA-MIB", "ogdataEventDevice"), ("OG-DATA-MIB", "ogdataEventState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogDataMibGroup = ogDataMibGroup.setStatus('current')
ogdataNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 17, 3, 2, 2)).setObjects(("OG-DATA-MIB", "ogdataEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogdataNotificationsGroup = ogdataNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OG-DATA-MIB", ogDataMibGroup=ogDataMibGroup, ogdataEventDevice=ogdataEventDevice, ogdataEventState=ogdataEventState, ogdataNotificationsGroup=ogdataNotificationsGroup, ogdataMibNotifications=ogdataMibNotifications, ogdataEventTable=ogdataEventTable, ogdataEventSeconds=ogdataEventSeconds, ogDataMibConformance=ogDataMibConformance, ogdataEventOccurred=ogdataEventOccurred, ogDataMibCompliances=ogDataMibCompliances, ogDataMibGroups=ogDataMibGroups, ogdataEventBytes=ogdataEventBytes, ogdataEventIndex=ogdataEventIndex, ogDataMibNotificationPrefix=ogDataMibNotificationPrefix, ogDataMibObjects=ogDataMibObjects, ogdataEvent=ogdataEvent, ogDataMib=ogDataMib, ogdataEventEntry=ogdataEventEntry, PYSNMP_MODULE_ID=ogDataMib, ogDataMibCompliance=ogDataMibCompliance)
