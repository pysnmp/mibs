#
# PySNMP MIB module OG-CONNECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-CONNECT-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 11:12:21 2023
# On host fv-az590-991 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, iso, Counter64, Unsigned32, Gauge32, Bits, ObjectIdentity, MibIdentifier, Counter32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "iso", "Counter64", "Unsigned32", "Gauge32", "Bits", "ObjectIdentity", "MibIdentifier", "Counter32", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogConnectMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 10))
ogConnectMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))
if mibBuilder.loadTexts: ogConnectMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogConnectMib.setOrganization('Opengear Inc.')
ogConnectMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10))
ogconnEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1))
ogconnEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1), )
if mibBuilder.loadTexts: ogconnEventTable.setStatus('current')
ogconnEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1), ).setIndexNames((0, "OG-CONNECT-MIB", "ogconnEventIndex"))
if mibBuilder.loadTexts: ogconnEventEntry.setStatus('current')
ogconnEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogconnEventIndex.setStatus('current')
ogconnEventUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventUsername.setStatus('current')
ogconnEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventType.setStatus('current')
ogconnEventPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventPortNumber.setStatus('current')
ogconnEventPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventPortLabel.setStatus('current')
ogConnectMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 2))
ogconnMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 2, 0))
ogconnEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 10, 2, 0, 200)).setObjects(("OG-CONNECT-MIB", "ogconnEventUsername"), ("OG-CONNECT-MIB", "ogconnEventType"), ("OG-CONNECT-MIB", "ogconnEventPortNumber"), ("OG-CONNECT-MIB", "ogconnEventPortLabel"))
if mibBuilder.loadTexts: ogconnEventOccurred.setStatus('current')
ogConnectMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3))
ogConnectMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 1))
ogConnectMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 2))
ogConnectMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 1, 1)).setObjects(("OG-CONNECT-MIB", "ogConnectMibGroup"), ("OG-CONNECT-MIB", "ogconnNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogConnectMibCompliance = ogConnectMibCompliance.setStatus('current')
ogConnectMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 2, 1)).setObjects(("OG-CONNECT-MIB", "ogconnEventUsername"), ("OG-CONNECT-MIB", "ogconnEventType"), ("OG-CONNECT-MIB", "ogconnEventPortNumber"), ("OG-CONNECT-MIB", "ogconnEventPortLabel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogConnectMibGroup = ogConnectMibGroup.setStatus('current')
ogconnNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 2, 2)).setObjects(("OG-CONNECT-MIB", "ogconnEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogconnNotificationsGroup = ogconnNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OG-CONNECT-MIB", ogconnEventEntry=ogconnEventEntry, ogconnEventOccurred=ogconnEventOccurred, ogconnEventTable=ogconnEventTable, ogConnectMibGroups=ogConnectMibGroups, ogConnectMib=ogConnectMib, ogconnMibNotifications=ogconnMibNotifications, ogConnectMibGroup=ogConnectMibGroup, ogConnectMibObjects=ogConnectMibObjects, PYSNMP_MODULE_ID=ogConnectMib, ogconnEventPortLabel=ogconnEventPortLabel, ogconnEventPortNumber=ogconnEventPortNumber, ogconnNotificationsGroup=ogconnNotificationsGroup, ogconnEventIndex=ogconnEventIndex, ogconnEventType=ogconnEventType, ogConnectMibNotificationPrefix=ogConnectMibNotificationPrefix, ogconnEventUsername=ogconnEventUsername, ogConnectMibCompliance=ogConnectMibCompliance, ogconnEvent=ogconnEvent, ogConnectMibCompliances=ogConnectMibCompliances, ogConnectMibConformance=ogConnectMibConformance)
