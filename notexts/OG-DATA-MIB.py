#
# PySNMP MIB module OG-DATA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-DATA-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 14:19:37 2021
# On host fv-az39-900 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, NotificationType, Gauge32, MibIdentifier, Integer32, Unsigned32, TimeTicks, ModuleIdentity, Counter32, Counter64, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "NotificationType", "Gauge32", "MibIdentifier", "Integer32", "Unsigned32", "TimeTicks", "ModuleIdentity", "Counter32", "Counter64", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("OG-DATA-MIB", ogdataEventBytes=ogdataEventBytes, ogdataEventState=ogdataEventState, ogdataEventEntry=ogdataEventEntry, ogDataMibCompliances=ogDataMibCompliances, ogDataMibCompliance=ogDataMibCompliance, ogdataEventOccurred=ogdataEventOccurred, ogDataMibObjects=ogDataMibObjects, ogdataEventIndex=ogdataEventIndex, ogdataNotificationsGroup=ogdataNotificationsGroup, ogDataMibGroups=ogDataMibGroups, ogdataEventTable=ogdataEventTable, ogDataMibGroup=ogDataMibGroup, ogDataMibNotificationPrefix=ogDataMibNotificationPrefix, PYSNMP_MODULE_ID=ogDataMib, ogdataEvent=ogdataEvent, ogdataEventSeconds=ogdataEventSeconds, ogdataEventDevice=ogdataEventDevice, ogDataMib=ogDataMib, ogdataMibNotifications=ogdataMibNotifications, ogDataMibConformance=ogDataMibConformance)
