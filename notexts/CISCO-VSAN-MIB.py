#
# PySNMP MIB module CISCO-VSAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VSAN-MIB
# Source digest sha256:e9ec498779e2421300d6ce3ba59eeaa0e3d0f7bf58e1d94433280e221c91254a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameId, VsanIndex = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameId", "VsanIndex")
CiscoMilliSeconds, ListIndex, ListIndexOrZero = mibBuilder.importSymbols("CISCO-TC", "CiscoMilliSeconds", "ListIndex", "ListIndexOrZero")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TimeStamp", "TruthValue")
ciscoVsanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 282))
ciscoVsanMIB.setRevisions(('2006-02-06 00:00', '2005-12-07 00:00', '2005-10-07 00:00', '2005-06-07 00:00', '2004-02-18 00:00', '2003-12-02 00:00', '2003-05-07 00:00', '2003-04-23 00:00', '2002-12-18 00:00', '2002-11-04 00:00', '2002-09-23 00:00',))
if mibBuilder.loadTexts: ciscoVsanMIB.setLastUpdated('2006-02-06 00:00')
if mibBuilder.loadTexts: ciscoVsanMIB.setOrganization('Cisco Systems Inc. ')
ciscoVsanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1))
vsanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 3))
vsanConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1))
vsanMembership = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2))
vsanNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3))
vsanFcConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4))
vsanStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 5))
vsanNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3, 0))
class VsanMediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("fibreChannel", 1), ("ethernet", 2), ("infiniband", 3), ("other", 4))

class VsanAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("suspended", 2))

class VsanOperationalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class VsanLoadBalancingType(TextualConvention, Integer32):
    reference = 'For more information on OX_ID, refer to Fibre Channel Switch Fabric 2 (FC-SW2) section 5.8.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("srcIdDestId", 1), ("srcIdDestIdOxId", 2))

vsanNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanNumber.setStatus('current')
vsanLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanLastChange.setStatus('current')
vsanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: vsanTable.setStatus('current')
vsanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: vsanEntry.setStatus('current')
vsanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 1), VsanIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: vsanIndex.setStatus('current')
vsanName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanName.setStatus('current')
vsanMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 3), VsanMediaType().clone('fibreChannel')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanMediaType.setStatus('current')
vsanAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 4), VsanAdminState().clone('active')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanAdminState.setStatus('current')
vsanMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(2112)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanMtu.setStatus('current')
vsanLoadBalancingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 6), VsanLoadBalancingType().clone('srcIdDestIdOxId')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanLoadBalancingType.setStatus('current')
vsanInterOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanInterOperMode.setStatus('deprecated')
vsanOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 8), VsanOperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanOperState.setStatus('current')
vsanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanRowStatus.setStatus('current')
vsanInterOperValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanInterOperValue.setStatus('current')
vsanInorderDelivery = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanInorderDelivery.setStatus('current')
vsanNetworkDropLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 12), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(500, 60000)).clone(2000)).setUnits('msec').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanNetworkDropLatency.setStatus('current')
notifyVsanIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 4), VsanIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: notifyVsanIndex.setStatus('current')
vsanDenyUnknownWwn = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vsanDenyUnknownWwn.setStatus('current')
vsanWwnListNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanWwnListNumber.setStatus('current')
vsanWwnListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: vsanWwnListTable.setStatus('current')
vsanWwnListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VSAN-MIB", "vsanWwnListIndex"), (0, "CISCO-VSAN-MIB", "vsanWwnListWwnIndex"))
if mibBuilder.loadTexts: vsanWwnListEntry.setStatus('current')
vsanWwnListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 1), ListIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: vsanWwnListIndex.setStatus('current')
vsanWwnListWwnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: vsanWwnListWwnIndex.setStatus('current')
vsanWwnListWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 3), FcNameId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanWwnListWwn.setStatus('current')
vsanWwnListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanWwnListRowStatus.setStatus('current')
vsanIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanIfNumber.setStatus('current')
vsanIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: vsanIfTable.setStatus('current')
vsanIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vsanIfEntry.setStatus('current')
vsanIfVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5, 1, 1), VsanIndex().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vsanIfVsan.setStatus('current')
vsanIfDenyList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5, 1, 2), ListIndexOrZero().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vsanIfDenyList.setStatus('current')
vsanDynamicListNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanDynamicListNumber.setStatus('current')
vsanDynamicTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: vsanDynamicTable.setStatus('current')
vsanDynamicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VSAN-MIB", "vsanWwnListIndex"))
if mibBuilder.loadTexts: vsanDynamicEntry.setStatus('current')
vsanDynamicVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7, 1, 1), VsanIndex().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanDynamicVsan.setStatus('current')
vsanDynamicRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanDynamicRowStatus.setStatus('current')
vsanMembershipSummaryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: vsanMembershipSummaryTable.setStatus('current')
vsanMembershipSummaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-VSAN-MIB", "vsanMembershipSummaryInterface"))
if mibBuilder.loadTexts: vsanMembershipSummaryEntry.setStatus('current')
vsanMembershipSummaryInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanMembershipSummaryInterface.setStatus('current')
vsanMembershipSummaryIntfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("static", 2), ("dynamic", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanMembershipSummaryIntfType.setStatus('current')
fcTimerRatov = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 1), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(5000, 100000)).clone(10000)).setUnits('msec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcTimerRatov.setStatus('current')
fcTimerEdtov = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 2), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(1000, 100000)).clone(2000)).setUnits('msec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcTimerEdtov.setStatus('current')
fcTimerFstov = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 3), CiscoMilliSeconds()).setUnits('msec').setMaxAccess("readonly")
if mibBuilder.loadTexts: fcTimerFstov.setStatus('current')
fcTimerDstov = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 4), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(5000, 100000)).clone(5000)).setUnits('msec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcTimerDstov.setStatus('current')
fcNetworkDropLatency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 5), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(500, 60000)).clone(2000)).setUnits('msec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcNetworkDropLatency.setStatus('current')
fcSwitchDropLatency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 6), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(0, 60000)).clone(500)).setUnits('msec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcSwitchDropLatency.setStatus('current')
fcInorderDelivery = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcInorderDelivery.setStatus('current')
vsanFcTimerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: vsanFcTimerTable.setStatus('current')
vsanFcTimerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1), ).setMaxAccess("notaccessible")
vsanEntry.registerAugmentions(("CISCO-VSAN-MIB", "vsanFcTimerEntry"))
vsanFcTimerEntry.setIndexNames(*vsanEntry.getIndexNames())
if mibBuilder.loadTexts: vsanFcTimerEntry.setStatus('current')
vsanFcTimerForceFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 1), Bits().clone(namedValues=NamedValues(("ratov", 0), ("edtov", 1), ("dstov", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanFcTimerForceFlag.setStatus('current')
vsanFcTimerRatov = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 2), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(5000, 100000)).clone(10000)).setUnits('msec').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanFcTimerRatov.setStatus('current')
vsanFcTimerEdtov = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 3), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(1000, 100000)).clone(2000)).setUnits('msec').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanFcTimerEdtov.setStatus('current')
vsanFcTimerDstov = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 4), CiscoMilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(5000, 100000)).clone(5000)).setUnits('msec').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vsanFcTimerDstov.setStatus('current')
vsanFcTimerFstov = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 5), CiscoMilliSeconds()).setUnits('msec').setMaxAccess("readonly")
if mibBuilder.loadTexts: vsanFcTimerFstov.setStatus('current')
vsanFcFeElementName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 5, 1), FcNameId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vsanFcFeElementName.setStatus('current')
vsanStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3, 0, 1)).setObjects(("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-VSAN-MIB", "vsanAdminState"), ("CISCO-VSAN-MIB", "vsanOperState"))
if mibBuilder.loadTexts: vsanStatusChange.setStatus('current')
vsanPortMembershipChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3, 0, 2)).setObjects(("CISCO-VSAN-MIB", "vsanFcFeElementName"), ("IF-MIB", "ifIndex"), ("CISCO-VSAN-MIB", "notifyVsanIndex"))
if mibBuilder.loadTexts: vsanPortMembershipChange.setStatus('current')
vsanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1))
vsanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2))
vsanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 1)).setObjects(("CISCO-VSAN-MIB", "vsanGroup"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroup"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance = vsanMIBCompliance.setStatus('deprecated')
vsanMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 2)).setObjects(("CISCO-VSAN-MIB", "vsanGroup"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroup"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance1 = vsanMIBCompliance1.setStatus('deprecated')
vsanMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 3)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev1"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroup"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance2 = vsanMIBCompliance2.setStatus('deprecated')
vsanMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 4)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev1"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance3 = vsanMIBCompliance3.setStatus('deprecated')
vsanMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 5)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev2"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance4 = vsanMIBCompliance4.setStatus('deprecated')
vsanMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 6)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev2"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroup"), ("CISCO-VSAN-MIB", "vsanFcTimerGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanMembershipSummaryGroupRev1"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance5 = vsanMIBCompliance5.setStatus('deprecated')
vsanMIBCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 7)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev2"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcTimerGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanMembershipSummaryGroupRev1"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance6 = vsanMIBCompliance6.setStatus('deprecated')
vsanMIBCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 8)).setObjects(("CISCO-VSAN-MIB", "vsanGroupRev3"), ("CISCO-VSAN-MIB", "vsanMembershipGroup"), ("CISCO-VSAN-MIB", "vsanStaticMembershipGroup"), ("CISCO-VSAN-MIB", "vsanNotificationGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcTimerGroupRev1"), ("CISCO-VSAN-MIB", "vsanFcLatencyGroup"), ("CISCO-VSAN-MIB", "vsanVsanMembershipSummaryGroup"), ("CISCO-VSAN-MIB", "vsanMembershipSummaryGroupRev1"), ("CISCO-VSAN-MIB", "vsanDynamicMembershipGroup"), ("CISCO-VSAN-MIB", "vsanWWNListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMIBCompliance7 = vsanMIBCompliance7.setStatus('current')
vsanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 1)).setObjects(("CISCO-VSAN-MIB", "vsanNumber"), ("CISCO-VSAN-MIB", "vsanLastChange"), ("CISCO-VSAN-MIB", "vsanName"), ("CISCO-VSAN-MIB", "vsanMediaType"), ("CISCO-VSAN-MIB", "vsanMtu"), ("CISCO-VSAN-MIB", "vsanAdminState"), ("CISCO-VSAN-MIB", "vsanLoadBalancingType"), ("CISCO-VSAN-MIB", "vsanInterOperMode"), ("CISCO-VSAN-MIB", "vsanOperState"), ("CISCO-VSAN-MIB", "vsanRowStatus"), ("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-VSAN-MIB", "fcInorderDelivery"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanGroup = vsanGroup.setStatus('deprecated')
vsanMembershipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 3)).setObjects(("CISCO-VSAN-MIB", "vsanDenyUnknownWwn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMembershipGroup = vsanMembershipGroup.setStatus('current')
vsanStaticMembershipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 4)).setObjects(("CISCO-VSAN-MIB", "vsanIfNumber"), ("CISCO-VSAN-MIB", "vsanIfVsan"), ("CISCO-VSAN-MIB", "vsanIfDenyList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanStaticMembershipGroup = vsanStaticMembershipGroup.setStatus('current')
vsanWWNListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 5)).setObjects(("CISCO-VSAN-MIB", "vsanWwnListNumber"), ("CISCO-VSAN-MIB", "vsanWwnListWwn"), ("CISCO-VSAN-MIB", "vsanWwnListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanWWNListGroup = vsanWWNListGroup.setStatus('current')
vsanDynamicMembershipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 6)).setObjects(("CISCO-VSAN-MIB", "vsanDynamicListNumber"), ("CISCO-VSAN-MIB", "vsanDynamicVsan"), ("CISCO-VSAN-MIB", "vsanDynamicRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanDynamicMembershipGroup = vsanDynamicMembershipGroup.setStatus('current')
vsanNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 7)).setObjects(("CISCO-VSAN-MIB", "vsanStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanNotificationGroup = vsanNotificationGroup.setStatus('deprecated')
vsanFcTimerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 8)).setObjects(("CISCO-VSAN-MIB", "fcTimerRatov"), ("CISCO-VSAN-MIB", "fcTimerEdtov"), ("CISCO-VSAN-MIB", "fcTimerFstov"), ("CISCO-VSAN-MIB", "fcTimerDstov"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanFcTimerGroup = vsanFcTimerGroup.setStatus('deprecated')
vsanFcLatencyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 9)).setObjects(("CISCO-VSAN-MIB", "fcNetworkDropLatency"), ("CISCO-VSAN-MIB", "fcSwitchDropLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanFcLatencyGroup = vsanFcLatencyGroup.setStatus('current')
vsanVsanMembershipSummaryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 10)).setObjects(("CISCO-VSAN-MIB", "vsanMembershipSummaryInterface"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanVsanMembershipSummaryGroup = vsanVsanMembershipSummaryGroup.setStatus('current')
vsanGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 11)).setObjects(("CISCO-VSAN-MIB", "vsanNumber"), ("CISCO-VSAN-MIB", "vsanLastChange"), ("CISCO-VSAN-MIB", "vsanName"), ("CISCO-VSAN-MIB", "vsanMediaType"), ("CISCO-VSAN-MIB", "vsanMtu"), ("CISCO-VSAN-MIB", "vsanAdminState"), ("CISCO-VSAN-MIB", "vsanLoadBalancingType"), ("CISCO-VSAN-MIB", "vsanOperState"), ("CISCO-VSAN-MIB", "vsanRowStatus"), ("CISCO-VSAN-MIB", "vsanInterOperValue"), ("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-VSAN-MIB", "fcInorderDelivery"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanGroupRev1 = vsanGroupRev1.setStatus('deprecated')
vsanFcTimerGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 12)).setObjects(("CISCO-VSAN-MIB", "fcTimerRatov"), ("CISCO-VSAN-MIB", "fcTimerEdtov"), ("CISCO-VSAN-MIB", "fcTimerDstov"), ("CISCO-VSAN-MIB", "fcTimerFstov"), ("CISCO-VSAN-MIB", "vsanFcTimerForceFlag"), ("CISCO-VSAN-MIB", "vsanFcTimerRatov"), ("CISCO-VSAN-MIB", "vsanFcTimerEdtov"), ("CISCO-VSAN-MIB", "vsanFcTimerDstov"), ("CISCO-VSAN-MIB", "vsanFcTimerFstov"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanFcTimerGroupRev1 = vsanFcTimerGroupRev1.setStatus('current')
vsanGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 13)).setObjects(("CISCO-VSAN-MIB", "vsanNumber"), ("CISCO-VSAN-MIB", "vsanLastChange"), ("CISCO-VSAN-MIB", "vsanName"), ("CISCO-VSAN-MIB", "vsanMediaType"), ("CISCO-VSAN-MIB", "vsanMtu"), ("CISCO-VSAN-MIB", "vsanAdminState"), ("CISCO-VSAN-MIB", "vsanLoadBalancingType"), ("CISCO-VSAN-MIB", "vsanOperState"), ("CISCO-VSAN-MIB", "vsanRowStatus"), ("CISCO-VSAN-MIB", "vsanInterOperValue"), ("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-VSAN-MIB", "fcInorderDelivery"), ("CISCO-VSAN-MIB", "vsanInorderDelivery"), ("CISCO-VSAN-MIB", "vsanNetworkDropLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanGroupRev2 = vsanGroupRev2.setStatus('deprecated')
vsanMembershipSummaryGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 14)).setObjects(("CISCO-VSAN-MIB", "vsanMembershipSummaryIntfType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanMembershipSummaryGroupRev1 = vsanMembershipSummaryGroupRev1.setStatus('current')
vsanNotificationGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 15)).setObjects(("CISCO-VSAN-MIB", "vsanStatusChange"), ("CISCO-VSAN-MIB", "vsanPortMembershipChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanNotificationGroupRev1 = vsanNotificationGroupRev1.setStatus('current')
vsanGroupRev3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 16)).setObjects(("CISCO-VSAN-MIB", "vsanNumber"), ("CISCO-VSAN-MIB", "vsanLastChange"), ("CISCO-VSAN-MIB", "vsanName"), ("CISCO-VSAN-MIB", "vsanMediaType"), ("CISCO-VSAN-MIB", "vsanMtu"), ("CISCO-VSAN-MIB", "vsanAdminState"), ("CISCO-VSAN-MIB", "vsanLoadBalancingType"), ("CISCO-VSAN-MIB", "vsanOperState"), ("CISCO-VSAN-MIB", "vsanRowStatus"), ("CISCO-VSAN-MIB", "vsanInterOperValue"), ("CISCO-VSAN-MIB", "notifyVsanIndex"), ("CISCO-VSAN-MIB", "fcInorderDelivery"), ("CISCO-VSAN-MIB", "vsanInorderDelivery"), ("CISCO-VSAN-MIB", "vsanNetworkDropLatency"), ("CISCO-VSAN-MIB", "vsanFcFeElementName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vsanGroupRev3 = vsanGroupRev3.setStatus('current')
mibBuilder.exportSymbols("CISCO-VSAN-MIB", PYSNMP_MODULE_ID=ciscoVsanMIB, VsanAdminState=VsanAdminState, VsanLoadBalancingType=VsanLoadBalancingType, VsanMediaType=VsanMediaType, VsanOperationalState=VsanOperationalState, ciscoVsanMIB=ciscoVsanMIB, ciscoVsanMIBObjects=ciscoVsanMIBObjects, fcInorderDelivery=fcInorderDelivery, fcNetworkDropLatency=fcNetworkDropLatency, fcSwitchDropLatency=fcSwitchDropLatency, fcTimerDstov=fcTimerDstov, fcTimerEdtov=fcTimerEdtov, fcTimerFstov=fcTimerFstov, fcTimerRatov=fcTimerRatov, notifyVsanIndex=notifyVsanIndex, vsanAdminState=vsanAdminState, vsanConfiguration=vsanConfiguration, vsanDenyUnknownWwn=vsanDenyUnknownWwn, vsanDynamicEntry=vsanDynamicEntry, vsanDynamicListNumber=vsanDynamicListNumber, vsanDynamicMembershipGroup=vsanDynamicMembershipGroup, vsanDynamicRowStatus=vsanDynamicRowStatus, vsanDynamicTable=vsanDynamicTable, vsanDynamicVsan=vsanDynamicVsan, vsanEntry=vsanEntry, vsanFcConfiguration=vsanFcConfiguration, vsanFcFeElementName=vsanFcFeElementName, vsanFcLatencyGroup=vsanFcLatencyGroup, vsanFcTimerDstov=vsanFcTimerDstov, vsanFcTimerEdtov=vsanFcTimerEdtov, vsanFcTimerEntry=vsanFcTimerEntry, vsanFcTimerForceFlag=vsanFcTimerForceFlag, vsanFcTimerFstov=vsanFcTimerFstov, vsanFcTimerGroup=vsanFcTimerGroup, vsanFcTimerGroupRev1=vsanFcTimerGroupRev1, vsanFcTimerRatov=vsanFcTimerRatov, vsanFcTimerTable=vsanFcTimerTable, vsanGroup=vsanGroup, vsanGroupRev1=vsanGroupRev1, vsanGroupRev2=vsanGroupRev2, vsanGroupRev3=vsanGroupRev3, vsanIfDenyList=vsanIfDenyList, vsanIfEntry=vsanIfEntry, vsanIfNumber=vsanIfNumber, vsanIfTable=vsanIfTable, vsanIfVsan=vsanIfVsan, vsanIndex=vsanIndex, vsanInorderDelivery=vsanInorderDelivery, vsanInterOperMode=vsanInterOperMode, vsanInterOperValue=vsanInterOperValue, vsanLastChange=vsanLastChange, vsanLoadBalancingType=vsanLoadBalancingType, vsanMIBCompliance1=vsanMIBCompliance1, vsanMIBCompliance2=vsanMIBCompliance2, vsanMIBCompliance3=vsanMIBCompliance3, vsanMIBCompliance4=vsanMIBCompliance4, vsanMIBCompliance5=vsanMIBCompliance5, vsanMIBCompliance6=vsanMIBCompliance6, vsanMIBCompliance7=vsanMIBCompliance7, vsanMIBCompliance=vsanMIBCompliance, vsanMIBCompliances=vsanMIBCompliances, vsanMIBConformance=vsanMIBConformance, vsanMIBGroups=vsanMIBGroups, vsanMediaType=vsanMediaType, vsanMembership=vsanMembership, vsanMembershipGroup=vsanMembershipGroup, vsanMembershipSummaryEntry=vsanMembershipSummaryEntry, vsanMembershipSummaryGroupRev1=vsanMembershipSummaryGroupRev1, vsanMembershipSummaryInterface=vsanMembershipSummaryInterface, vsanMembershipSummaryIntfType=vsanMembershipSummaryIntfType, vsanMembershipSummaryTable=vsanMembershipSummaryTable, vsanMtu=vsanMtu, vsanName=vsanName, vsanNetworkDropLatency=vsanNetworkDropLatency, vsanNotification=vsanNotification, vsanNotificationGroup=vsanNotificationGroup, vsanNotificationGroupRev1=vsanNotificationGroupRev1, vsanNotifications=vsanNotifications, vsanNumber=vsanNumber, vsanOperState=vsanOperState, vsanPortMembershipChange=vsanPortMembershipChange, vsanRowStatus=vsanRowStatus, vsanStaticMembershipGroup=vsanStaticMembershipGroup, vsanStats=vsanStats, vsanStatusChange=vsanStatusChange, vsanTable=vsanTable, vsanVsanMembershipSummaryGroup=vsanVsanMembershipSummaryGroup, vsanWWNListGroup=vsanWWNListGroup, vsanWwnListEntry=vsanWwnListEntry, vsanWwnListIndex=vsanWwnListIndex, vsanWwnListNumber=vsanWwnListNumber, vsanWwnListRowStatus=vsanWwnListRowStatus, vsanWwnListTable=vsanWwnListTable, vsanWwnListWwn=vsanWwnListWwn, vsanWwnListWwnIndex=vsanWwnListWwnIndex)
