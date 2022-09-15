#
# PySNMP MIB module BLUECOAT-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SEGMENT-MIB
# Produced by pysmi-1.1.8 at Thu Sep 15 09:06:40 2022
# On host fv-az343-490 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, Gauge32, ObjectIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, ModuleIdentity, TimeTicks, Bits, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "ModuleIdentity", "TimeTicks", "Bits", "MibIdentifier", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
segmentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 17))
segmentMIB.setRevisions(('2016-02-24 03:00', '2015-01-13 03:00',))
if mibBuilder.loadTexts: segmentMIB.setLastUpdated('201602240300Z')
if mibBuilder.loadTexts: segmentMIB.setOrganization('Blue Coat Systems, Inc.')
segmentMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1))
segmentMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 17, 2))
segmentMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 17, 3))
segmentMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 17, 2, 0))
segmentMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 1))
segmentMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 2))
segmentMIBNotifGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 3))
segmentMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 1, 1)).setObjects(("BLUECOAT-SEGMENT-MIB", "segmentMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    segmentMIBCompliance = segmentMIBCompliance.setStatus('current')
class SegmentMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("invalid", 0), ("activeInlineFailToAppliance", 1), ("asymActiveInlineFailToAppliance", 2), ("activeInlineFailToNetwork", 3), ("asymActiveInlineFailToNetwork", 4), ("passiveInline", 5), ("asymPassiveInline", 6), ("passiveTap", 7), ("asymPassiveTap", 8), ("passiveTap2xAggrInputs", 9), ("passiveTap3xAggrInputs", 10))

class SegmentState(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("softwareFailure", 0), ("manualFailure", 1), ("linkFailure", 2), ("activationFailure", 3))

segments = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1))
segmentStatusTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1), )
if mibBuilder.loadTexts: segmentStatusTable.setStatus('current')
segmentStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SEGMENT-MIB", "segmentStatusIndex"))
if mibBuilder.loadTexts: segmentStatusEntry.setStatus('current')
segmentStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: segmentStatusIndex.setStatus('current')
segmentStatusIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentStatusIdentifier.setStatus('current')
segmentStatusMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 3), SegmentMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentStatusMode.setStatus('current')
segmentStatusIfList = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 4), PortList().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentStatusIfList.setStatus('current')
segmentStatusDownIfList = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 5), PortList().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentStatusDownIfList.setStatus('current')
segmentStatusCopyIfList = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 6), PortList().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentStatusCopyIfList.setStatus('current')
segmentStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 7), SegmentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentStatusState.setStatus('current')
segmentStatusComment = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: segmentStatusComment.setStatus('current')
segmentStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 17, 2, 0, 1)).setObjects(("BLUECOAT-SEGMENT-MIB", "segmentStatusIdentifier"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusMode"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusIfList"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusDownIfList"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusCopyIfList"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusState"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusComment"))
if mibBuilder.loadTexts: segmentStateTrap.setStatus('current')
segmentMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 2, 1)).setObjects(("BLUECOAT-SEGMENT-MIB", "segmentStatusIdentifier"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusMode"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusIfList"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusDownIfList"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusCopyIfList"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusState"), ("BLUECOAT-SEGMENT-MIB", "segmentStatusComment"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    segmentMIBGroup = segmentMIBGroup.setStatus('current')
segmentMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 3, 1)).setObjects(("BLUECOAT-SEGMENT-MIB", "segmentStateTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    segmentMIBNotifGroup = segmentMIBNotifGroup.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SEGMENT-MIB", segmentStatusState=segmentStatusState, segmentMIBNotifGroup=segmentMIBNotifGroup, segmentMIBGroups=segmentMIBGroups, segmentMIBGroup=segmentMIBGroup, segmentMIBNotifGroups=segmentMIBNotifGroups, segmentStatusIndex=segmentStatusIndex, segmentMIBNotificationsPrefix=segmentMIBNotificationsPrefix, segmentStatusMode=segmentStatusMode, segmentStatusComment=segmentStatusComment, segmentStatusDownIfList=segmentStatusDownIfList, segmentStateTrap=segmentStateTrap, segmentMIBObjects=segmentMIBObjects, segmentMIBConformance=segmentMIBConformance, segmentStatusTable=segmentStatusTable, segmentStatusCopyIfList=segmentStatusCopyIfList, segmentStatusEntry=segmentStatusEntry, PYSNMP_MODULE_ID=segmentMIB, segmentStatusIdentifier=segmentStatusIdentifier, segments=segments, segmentMIBNotifications=segmentMIBNotifications, SegmentState=SegmentState, segmentMIBCompliances=segmentMIBCompliances, SegmentMode=SegmentMode, segmentMIBCompliance=segmentMIBCompliance, segmentMIB=segmentMIB, segmentStatusIfList=segmentStatusIfList)
