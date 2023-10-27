#
# PySNMP MIB module OG-PATTERN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-PATTERN-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 07:11:21 2023
# On host fv-az550-936 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, IpAddress, Counter64, Gauge32, Integer32, Bits, Counter32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "IpAddress", "Counter64", "Gauge32", "Integer32", "Bits", "Counter32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogPatternMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 12))
ogPatternMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))
if mibBuilder.loadTexts: ogPatternMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogPatternMib.setOrganization('Opengear Inc.')
ogPatternMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10))
ogpatnEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1))
ogpatnEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1), )
if mibBuilder.loadTexts: ogpatnEventTable.setStatus('current')
ogpatnEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1), ).setIndexNames((0, "OG-PATTERN-MIB", "ogpatnEventIndex"))
if mibBuilder.loadTexts: ogpatnEventEntry.setStatus('current')
ogpatnEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogpatnEventIndex.setStatus('current')
ogpatnEventDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventDescription.setStatus('current')
ogpatnEventText = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventText.setStatus('current')
ogpatnEventPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventPortNumber.setStatus('current')
ogpatnEventPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 12, 10, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogpatnEventPortLabel.setStatus('current')
ogPatternMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 2))
ogpatnMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 2, 0))
ogpatnEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 12, 2, 0, 200)).setObjects(("OG-PATTERN-MIB", "ogpatnEventDescription"), ("OG-PATTERN-MIB", "ogpatnEventText"), ("OG-PATTERN-MIB", "ogpatnEventPortNumber"), ("OG-PATTERN-MIB", "ogpatnEventPortLabel"))
if mibBuilder.loadTexts: ogpatnEventOccurred.setStatus('current')
ogPatternMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3))
ogPatternMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 1))
ogPatternMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 2))
ogPatternMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 1, 1)).setObjects(("OG-PATTERN-MIB", "ogPatternMibGroup"), ("OG-PATTERN-MIB", "ogpatnNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogPatternMibCompliance = ogPatternMibCompliance.setStatus('current')
ogPatternMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 2, 1)).setObjects(("OG-PATTERN-MIB", "ogpatnEventDescription"), ("OG-PATTERN-MIB", "ogpatnEventText"), ("OG-PATTERN-MIB", "ogpatnEventPortNumber"), ("OG-PATTERN-MIB", "ogpatnEventPortLabel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogPatternMibGroup = ogPatternMibGroup.setStatus('current')
ogpatnNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 12, 3, 2, 2)).setObjects(("OG-PATTERN-MIB", "ogpatnEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogpatnNotificationsGroup = ogpatnNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OG-PATTERN-MIB", ogpatnEventTable=ogpatnEventTable, ogPatternMibNotificationPrefix=ogPatternMibNotificationPrefix, ogpatnEventText=ogpatnEventText, ogpatnEventDescription=ogpatnEventDescription, ogpatnEventEntry=ogpatnEventEntry, PYSNMP_MODULE_ID=ogPatternMib, ogpatnNotificationsGroup=ogpatnNotificationsGroup, ogpatnEvent=ogpatnEvent, ogpatnEventOccurred=ogpatnEventOccurred, ogPatternMibGroup=ogPatternMibGroup, ogPatternMibCompliances=ogPatternMibCompliances, ogPatternMibObjects=ogPatternMibObjects, ogPatternMibConformance=ogPatternMibConformance, ogPatternMibCompliance=ogPatternMibCompliance, ogPatternMib=ogPatternMib, ogpatnEventIndex=ogpatnEventIndex, ogpatnMibNotifications=ogpatnMibNotifications, ogpatnEventPortLabel=ogpatnEventPortLabel, ogPatternMibGroups=ogPatternMibGroups, ogpatnEventPortNumber=ogpatnEventPortNumber)
