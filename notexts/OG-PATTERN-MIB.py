#
# PySNMP MIB module OG-PATTERN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-PATTERN-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 11:43:37 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, ModuleIdentity, TimeTicks, Unsigned32, Counter32, Bits, iso, Gauge32, MibIdentifier, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "ModuleIdentity", "TimeTicks", "Unsigned32", "Counter32", "Bits", "iso", "Gauge32", "MibIdentifier", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("OG-PATTERN-MIB", ogpatnEventTable=ogpatnEventTable, ogPatternMibCompliances=ogPatternMibCompliances, ogPatternMibObjects=ogPatternMibObjects, ogpatnEventOccurred=ogpatnEventOccurred, ogpatnEventText=ogpatnEventText, ogpatnEvent=ogpatnEvent, ogpatnEventDescription=ogpatnEventDescription, ogPatternMibNotificationPrefix=ogPatternMibNotificationPrefix, ogpatnMibNotifications=ogpatnMibNotifications, ogpatnEventIndex=ogpatnEventIndex, ogPatternMibGroups=ogPatternMibGroups, ogPatternMibCompliance=ogPatternMibCompliance, PYSNMP_MODULE_ID=ogPatternMib, ogpatnEventPortLabel=ogpatnEventPortLabel, ogpatnEventEntry=ogpatnEventEntry, ogpatnEventPortNumber=ogpatnEventPortNumber, ogpatnNotificationsGroup=ogpatnNotificationsGroup, ogPatternMib=ogPatternMib, ogPatternMibConformance=ogPatternMibConformance, ogPatternMibGroup=ogPatternMibGroup)
