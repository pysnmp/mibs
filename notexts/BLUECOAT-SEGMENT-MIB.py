#
# PySNMP MIB module BLUECOAT-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SEGMENT-MIB
# Produced by pysmi-1.1.3 at Tue Nov 30 13:50:17 2021
# On host fv-az77-605 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Counter64, Bits, Unsigned32, ObjectIdentity, MibIdentifier, NotificationType, TimeTicks, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Counter64", "Bits", "Unsigned32", "ObjectIdentity", "MibIdentifier", "NotificationType", "TimeTicks", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BLUECOAT-SEGMENT-MIB", segmentMIBNotifGroups=segmentMIBNotifGroups, segmentMIBCompliance=segmentMIBCompliance, segmentMIBConformance=segmentMIBConformance, segmentStateTrap=segmentStateTrap, segmentStatusTable=segmentStatusTable, SegmentMode=SegmentMode, segmentMIBCompliances=segmentMIBCompliances, segmentStatusEntry=segmentStatusEntry, segmentStatusDownIfList=segmentStatusDownIfList, segmentStatusComment=segmentStatusComment, segmentMIBGroups=segmentMIBGroups, SegmentState=SegmentState, segmentMIBNotificationsPrefix=segmentMIBNotificationsPrefix, segments=segments, segmentMIBGroup=segmentMIBGroup, segmentStatusIfList=segmentStatusIfList, segmentStatusIdentifier=segmentStatusIdentifier, segmentMIBObjects=segmentMIBObjects, segmentMIBNotifGroup=segmentMIBNotifGroup, segmentStatusIndex=segmentStatusIndex, segmentMIB=segmentMIB, segmentStatusCopyIfList=segmentStatusCopyIfList, segmentStatusState=segmentStatusState, PYSNMP_MODULE_ID=segmentMIB, segmentMIBNotifications=segmentMIBNotifications, segmentStatusMode=segmentStatusMode)
