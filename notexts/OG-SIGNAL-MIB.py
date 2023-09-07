#
# PySNMP MIB module OG-SIGNAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-SIGNAL-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:29:41 2023
# On host fv-az448-504 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Unsigned32, TimeTicks, IpAddress, Integer32, Bits, Counter64, ObjectIdentity, Gauge32, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "TimeTicks", "IpAddress", "Integer32", "Bits", "Counter64", "ObjectIdentity", "Gauge32", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ogSignalMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 11))
ogSignalMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))
if mibBuilder.loadTexts: ogSignalMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogSignalMib.setOrganization('Opengear Inc.')
ogSignalMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 11, 10))
ogsgnlEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1))
ogsgnlEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1), )
if mibBuilder.loadTexts: ogsgnlEventTable.setStatus('current')
ogsgnlEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1), ).setIndexNames((0, "OG-SIGNAL-MIB", "ogsgnlEventIndex"))
if mibBuilder.loadTexts: ogsgnlEventEntry.setStatus('current')
ogsgnlEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogsgnlEventIndex.setStatus('current')
ogsgnlEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventType.setStatus('current')
ogsgnlEventState = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventState.setStatus('current')
ogsgnlEventPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventPortNumber.setStatus('current')
ogsgnlEventPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 11, 10, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogsgnlEventPortLabel.setStatus('current')
ogSignalMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 11, 2))
ogsgnlMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 11, 2, 0))
ogsgnlEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 11, 2, 0, 200)).setObjects(("OG-SIGNAL-MIB", "ogsgnlEventType"), ("OG-SIGNAL-MIB", "ogsgnlEventState"), ("OG-SIGNAL-MIB", "ogsgnlEventPortNumber"), ("OG-SIGNAL-MIB", "ogsgnlEventPortLabel"))
if mibBuilder.loadTexts: ogsgnlEventOccurred.setStatus('current')
ogSignalMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 11, 3))
ogSignalMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 11, 3, 1))
ogSignalMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 11, 3, 2))
ogSignalMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 11, 3, 1, 1)).setObjects(("OG-SIGNAL-MIB", "ogSignalMibGroup"), ("OG-SIGNAL-MIB", "ogsgnlNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogSignalMibCompliance = ogSignalMibCompliance.setStatus('current')
ogSignalMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 11, 3, 2, 1)).setObjects(("OG-SIGNAL-MIB", "ogsgnlEventType"), ("OG-SIGNAL-MIB", "ogsgnlEventState"), ("OG-SIGNAL-MIB", "ogsgnlEventPortNumber"), ("OG-SIGNAL-MIB", "ogsgnlEventPortLabel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogSignalMibGroup = ogSignalMibGroup.setStatus('current')
ogsgnlNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 11, 3, 2, 2)).setObjects(("OG-SIGNAL-MIB", "ogsgnlEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogsgnlNotificationsGroup = ogsgnlNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OG-SIGNAL-MIB", ogsgnlEvent=ogsgnlEvent, ogSignalMibObjects=ogSignalMibObjects, ogsgnlEventType=ogsgnlEventType, ogsgnlEventOccurred=ogsgnlEventOccurred, ogSignalMib=ogSignalMib, PYSNMP_MODULE_ID=ogSignalMib, ogSignalMibGroup=ogSignalMibGroup, ogSignalMibCompliance=ogSignalMibCompliance, ogsgnlEventEntry=ogsgnlEventEntry, ogSignalMibNotificationPrefix=ogSignalMibNotificationPrefix, ogsgnlEventState=ogsgnlEventState, ogsgnlNotificationsGroup=ogsgnlNotificationsGroup, ogSignalMibCompliances=ogSignalMibCompliances, ogsgnlEventPortNumber=ogsgnlEventPortNumber, ogSignalMibGroups=ogSignalMibGroups, ogSignalMibConformance=ogSignalMibConformance, ogsgnlEventIndex=ogsgnlEventIndex, ogsgnlEventTable=ogsgnlEventTable, ogsgnlEventPortLabel=ogsgnlEventPortLabel, ogsgnlMibNotifications=ogsgnlMibNotifications)
