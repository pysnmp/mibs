#
# PySNMP MIB module OG-CONNECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-CONNECT-MIB
# Produced by pysmi-1.1.10 at Mon Feb 12 02:26:00 2024
# On host fv-az1251-48 platform Linux version 6.2.0-1019-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, Unsigned32, Counter64, Gauge32, MibIdentifier, Bits, Integer32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "Unsigned32", "Counter64", "Gauge32", "MibIdentifier", "Bits", "Integer32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity")
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
mibBuilder.exportSymbols("OG-CONNECT-MIB", ogconnEventTable=ogconnEventTable, ogConnectMib=ogConnectMib, ogconnMibNotifications=ogconnMibNotifications, ogconnEvent=ogconnEvent, PYSNMP_MODULE_ID=ogConnectMib, ogConnectMibConformance=ogConnectMibConformance, ogconnNotificationsGroup=ogconnNotificationsGroup, ogconnEventPortLabel=ogconnEventPortLabel, ogconnEventUsername=ogconnEventUsername, ogconnEventPortNumber=ogconnEventPortNumber, ogconnEventEntry=ogconnEventEntry, ogconnEventIndex=ogconnEventIndex, ogconnEventOccurred=ogconnEventOccurred, ogConnectMibGroup=ogConnectMibGroup, ogConnectMibObjects=ogConnectMibObjects, ogConnectMibNotificationPrefix=ogConnectMibNotificationPrefix, ogconnEventType=ogconnEventType, ogConnectMibCompliance=ogConnectMibCompliance, ogConnectMibCompliances=ogConnectMibCompliances, ogConnectMibGroups=ogConnectMibGroups)
