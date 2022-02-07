#
# PySNMP MIB module IEEE8021-SPB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-SPB-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:21 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ieee8021BridgeBasePort, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort")
dot1agCfmMdIndex, dot1agCfmMepEntry, dot1agCfmMaIndex = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "dot1agCfmMdIndex", "dot1agCfmMepEntry", "dot1agCfmMaIndex")
IEEE8021PbbServiceIdentifier, IEEE8021PbbTeEsp, ieee802dot1mibs, IEEE8021PbbIngressEgress, IEEE8021BridgePortNumber = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021PbbServiceIdentifier", "IEEE8021PbbTeEsp", "ieee802dot1mibs", "IEEE8021PbbIngressEgress", "IEEE8021BridgePortNumber")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
VlanIdOrNone, VlanIdOrAny, VlanId = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone", "VlanIdOrAny", "VlanId")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Bits, MibIdentifier, NotificationType, IpAddress, Integer32, ModuleIdentity, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "MibIdentifier", "NotificationType", "IpAddress", "Integer32", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Gauge32", "Unsigned32")
DisplayString, TextualConvention, TruthValue, RowStatus, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus", "MacAddress")
ieee8021SpbMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 26))
ieee8021SpbMib.setRevisions(('2018-06-28 00:00', '2015-06-23 00:00', '2013-05-13 00:00', '2012-02-03 00:00',))
if mibBuilder.loadTexts: ieee8021SpbMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021SpbMib.setOrganization('IEEE 802.1 Working Group')
class IEEE8021SpbAreaAddress(TextualConvention, OctetString):
    reference = '12.25.1.1.2 a), 12.25.1.2.2 a), 12.25.1.3.2 a), 12.25.1.4.2 a)'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class IEEE8021SpbEctAlgorithm(TextualConvention, OctetString):
    reference = '12.3 q)'
    status = 'current'
    displayHint = '1x-'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class IEEE8021SpbMode(TextualConvention, Integer32):
    reference = '27.10'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("manual", 2))

class IEEE8021SpbEctMode(TextualConvention, Integer32):
    reference = '12.25.5.1.3 c), 12.25.9.1.3 e)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("spbm", 2), ("spbv", 3))

class IEEE8021SpbDigestConvention(TextualConvention, Integer32):
    reference = '28.4.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("loopFreeBoth", 2), ("loopFreeMcastOnly", 3))

class IEEE8021SpbLinkMetric(TextualConvention, Integer32):
    reference = '28.2'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16777215)

class IEEE8021SpbAdjState(TextualConvention, Integer32):
    reference = '12.25.6.1.3 d), 12.25.6.2.3 d), 12.25.7.1.3 (e'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3))

class IEEE8021SpbmSPsourceId(TextualConvention, OctetString):
    reference = '27.15'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class IEEE8021SpbDigest(TextualConvention, OctetString):
    reference = '28.4'
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class IEEE8021SpbMCID(TextualConvention, OctetString):
    reference = '13.8'
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(51, 51)
    fixedLength = 51

class IEEE8021SpbBridgePriority(TextualConvention, OctetString):
    reference = '13.26.3'
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class IEEE8021SpbMTID(TextualConvention, Unsigned32):
    reference = '3.157, 3.158'
    status = 'current'
    displayHint = 'd'

class IEEE8021SpbServiceIdentifierOrAny(TextualConvention, Unsigned32):
    reference = '3.157, 3.158'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(255, 16777215)

ieee8021SpbObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 26, 1))
ieee8021PcrObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 26, 3))
ieee8021SpbSys = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 26, 1, 1))
ieee8021SpbSysAreaAddress = MibScalar((1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 1), IEEE8021SpbAreaAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpbSysAreaAddress.setStatus('current')
ieee8021SpbSysId = MibScalar((1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpbSysId.setStatus('current')
ieee8021SpbSysControlAddr = MibScalar((1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpbSysControlAddr.setStatus('current')
ieee8021SpbSysName = MibScalar((1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbSysName.setStatus('current')
ieee8021SpbSysBridgePriority = MibScalar((1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 5), IEEE8021SpbBridgePriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbSysBridgePriority.setStatus('current')
ieee8021SpbmSysSPSourceId = MibScalar((1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 6), IEEE8021SpbmSPsourceId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpbmSysSPSourceId.setStatus('current')
ieee8021SpbvSysMode = MibScalar((1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 7), IEEE8021SpbMode().clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpbvSysMode.setStatus('current')
ieee8021SpbmSysMode = MibScalar((1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 8), IEEE8021SpbMode().clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpbmSysMode.setStatus('current')
ieee8021SpbSysDigestConvention = MibScalar((1, 3, 111, 2, 802, 1, 1, 26, 1, 1, 9), IEEE8021SpbDigestConvention().clone('loopFreeBoth')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SpbSysDigestConvention.setStatus('current')
ieee8021SpbMtidStaticTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 2), )
if mibBuilder.loadTexts: ieee8021SpbMtidStaticTable.setStatus('current')
ieee8021SpbMtidStaticTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 2, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbMtidStaticEntryMtid"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopIx"))
if mibBuilder.loadTexts: ieee8021SpbMtidStaticTableEntry.setStatus('current')
ieee8021SpbMtidStaticEntryMtid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 2, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbMtidStaticEntryMtid.setStatus('current')
ieee8021SpbMTidStaticEntryMtidOverload = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbMTidStaticEntryMtidOverload.setStatus('current')
ieee8021SpbMtidStaticEntryRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbMtidStaticEntryRowStatus.setStatus('current')
ieee8021SpbTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 2, 1, 4), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbTopIx.setStatus('current')
ieee8021SpbTopIxDynamicTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 3), )
if mibBuilder.loadTexts: ieee8021SpbTopIxDynamicTable.setStatus('current')
ieee8021SpbTopIxDynamicTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 3, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryTopIx"))
if mibBuilder.loadTexts: ieee8021SpbTopIxDynamicTableEntry.setStatus('current')
ieee8021SpbTopIxDynamicEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 3, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbTopIxDynamicEntryTopIx.setStatus('current')
ieee8021SpbTopIxDynamicEntryAgreeDigest = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 3, 1, 2), IEEE8021SpbDigest()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbTopIxDynamicEntryAgreeDigest.setStatus('current')
ieee8021SpbTopIxDynamicEntryMCID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 3, 1, 3), IEEE8021SpbMCID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbTopIxDynamicEntryMCID.setStatus('current')
ieee8021SpbTopIxDynamicEntryAuxMCID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 3, 1, 4), IEEE8021SpbMCID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbTopIxDynamicEntryAuxMCID.setStatus('current')
ieee8021SpbEctStaticTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 4), )
if mibBuilder.loadTexts: ieee8021SpbEctStaticTable.setStatus('current')
ieee8021SpbEctStaticTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryTopIx"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryBaseVid"))
if mibBuilder.loadTexts: ieee8021SpbEctStaticTableEntry.setStatus('current')
ieee8021SpbEctStaticEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbEctStaticEntryTopIx.setStatus('current')
ieee8021SpbEctStaticEntryBaseVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1, 2), VlanIdOrAny())
if mibBuilder.loadTexts: ieee8021SpbEctStaticEntryBaseVid.setStatus('current')
ieee8021SpbEctStaticEntryEctAlgorithm = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1, 3), IEEE8021SpbEctAlgorithm().clone('00-80-c2-01')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbEctStaticEntryEctAlgorithm.setStatus('current')
ieee8021SpbvEctStaticEntrySpvid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1, 4), VlanIdOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbvEctStaticEntrySpvid.setStatus('current')
ieee8021SpbEctStaticEntryRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbEctStaticEntryRowStatus.setStatus('current')
ieee8021SpbEctDynamicTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 5), )
if mibBuilder.loadTexts: ieee8021SpbEctDynamicTable.setStatus('current')
ieee8021SpbEctDynamicTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryTopIx"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryBaseVid"))
if mibBuilder.loadTexts: ieee8021SpbEctDynamicTableEntry.setStatus('current')
ieee8021SpbEctDynamicEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbEctDynamicEntryTopIx.setStatus('current')
ieee8021SpbEctDynamicEntryBaseVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 2), VlanId())
if mibBuilder.loadTexts: ieee8021SpbEctDynamicEntryBaseVid.setStatus('current')
ieee8021SpbEctDynamicEntryMode = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 3), IEEE8021SpbEctMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbEctDynamicEntryMode.setStatus('current')
ieee8021SpbEctDynamicEntryLocalUse = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbEctDynamicEntryLocalUse.setStatus('current')
ieee8021SpbEctDynamicEntryRemoteUse = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbEctDynamicEntryRemoteUse.setStatus('current')
ieee8021SpbEctDynamicEntryIngressCheckDiscards = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbEctDynamicEntryIngressCheckDiscards.setStatus('current')
ieee8021SpbAdjStaticTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 6), )
if mibBuilder.loadTexts: ieee8021SpbAdjStaticTable.setStatus('current')
ieee8021SpbAdjStaticTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryTopIx"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryIfIndex"))
if mibBuilder.loadTexts: ieee8021SpbAdjStaticTableEntry.setStatus('current')
ieee8021SpbAdjStaticEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbAdjStaticEntryTopIx.setStatus('current')
ieee8021SpbAdjStaticEntryIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1, 2), InterfaceIndexOrZero())
if mibBuilder.loadTexts: ieee8021SpbAdjStaticEntryIfIndex.setStatus('current')
ieee8021SpbAdjStaticEntryMetric = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1, 3), IEEE8021SpbLinkMetric()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbAdjStaticEntryMetric.setStatus('current')
ieee8021SpbAdjStaticEntryIfAdminState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1, 4), IEEE8021SpbAdjState()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbAdjStaticEntryIfAdminState.setStatus('current')
ieee8021SpbAdjStaticEntryRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbAdjStaticEntryRowStatus.setStatus('current')
ieee8021SpbAdjDynamicTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 7), )
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicTable.setStatus('current')
ieee8021SpbAdjDynamicTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryTopIx"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIfIndex"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerSysId"))
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicTableEntry.setStatus('current')
ieee8021SpbAdjDynamicEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryTopIx.setStatus('current')
ieee8021SpbAdjDynamicEntryIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 2), InterfaceIndexOrZero())
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryIfIndex.setStatus('current')
ieee8021SpbAdjDynamicEntryPeerSysId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 3), MacAddress())
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryPeerSysId.setStatus('current')
ieee8021SpbAdjDynamicEntryPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 4), IEEE8021BridgePortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryPort.setStatus('current')
ieee8021SpbAdjDynamicEntryIfOperState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 5), IEEE8021SpbAdjState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryIfOperState.setStatus('current')
ieee8021SpbAdjDynamicEntryPeerSysName = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryPeerSysName.setStatus('current')
ieee8021SpbAdjDynamicEntryPeerAgreeDigest = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 7), IEEE8021SpbDigest()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryPeerAgreeDigest.setStatus('current')
ieee8021SpbAdjDynamicEntryPeerMCID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 8), IEEE8021SpbMCID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryPeerMCID.setStatus('current')
ieee8021SpbAdjDynamicEntryPeerAuxMCID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 9), IEEE8021SpbMCID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryPeerAuxMCID.setStatus('current')
ieee8021SpbAdjDynamicEntryLocalCircuitID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryLocalCircuitID.setStatus('current')
ieee8021SpbAdjDynamicEntryPeerLocalCircuitID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryPeerLocalCircuitID.setStatus('current')
ieee8021SpbAdjDynamicEntryPortIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryPortIdentifier.setStatus('current')
ieee8021SpbAdjDynamicEntryPeerPortIdentifier = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryPeerPortIdentifier.setStatus('current')
ieee8021SpbAdjDynamicEntryIsisCircIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 7, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbAdjDynamicEntryIsisCircIndex.setStatus('current')
ieee8021SpbTopNodeTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 8), )
if mibBuilder.loadTexts: ieee8021SpbTopNodeTable.setStatus('current')
ieee8021SpbTopNodeTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntryTopIx"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntrySysId"))
if mibBuilder.loadTexts: ieee8021SpbTopNodeTableEntry.setStatus('current')
ieee8021SpbTopNodeEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbTopNodeEntryTopIx.setStatus('current')
ieee8021SpbTopNodeEntrySysId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1, 2), MacAddress())
if mibBuilder.loadTexts: ieee8021SpbTopNodeEntrySysId.setStatus('current')
ieee8021SpbTopNodeEntryBridgePriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1, 3), IEEE8021SpbBridgePriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbTopNodeEntryBridgePriority.setStatus('current')
ieee8021SpbmTopNodeEntrySPsourceID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1, 4), IEEE8021SpbmSPsourceId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbmTopNodeEntrySPsourceID.setStatus('current')
ieee8021SpbTopNodeEntrySysName = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 8, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbTopNodeEntrySysName.setStatus('current')
ieee8021SpbTopEctTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 9), )
if mibBuilder.loadTexts: ieee8021SpbTopEctTable.setStatus('current')
ieee8021SpbTopEctTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryTopIx"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntrySysId"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryBaseVid"))
if mibBuilder.loadTexts: ieee8021SpbTopEctTableEntry.setStatus('current')
ieee8021SpbTopEctEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbTopEctEntryTopIx.setStatus('current')
ieee8021SpbTopEctEntrySysId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 2), MacAddress())
if mibBuilder.loadTexts: ieee8021SpbTopEctEntrySysId.setStatus('current')
ieee8021SpbTopEctEntryBaseVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 3), VlanIdOrAny())
if mibBuilder.loadTexts: ieee8021SpbTopEctEntryBaseVid.setStatus('current')
ieee8021SpbTopEctEntryEctAlgorithm = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 4), IEEE8021SpbEctAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbTopEctEntryEctAlgorithm.setStatus('current')
ieee8021SpbTopEctEntryMode = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 5), IEEE8021SpbEctMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbTopEctEntryMode.setStatus('current')
ieee8021SpbvTopEctSysMode = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 6), IEEE8021SpbMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbvTopEctSysMode.setStatus('current')
ieee8021SpbvTopEctEntrySpvid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 7), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbvTopEctEntrySpvid.setStatus('current')
ieee8021SpbTopEctEntryLocalUse = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 9, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbTopEctEntryLocalUse.setStatus('current')
ieee8021SpbTopEdgeTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 10), )
if mibBuilder.loadTexts: ieee8021SpbTopEdgeTable.setStatus('current')
ieee8021SpbTopEdgeTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryTopIx"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntrySysIdNear"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntrySysIdFar"))
if mibBuilder.loadTexts: ieee8021SpbTopEdgeTableEntry.setStatus('current')
ieee8021SpbTopEdgeEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbTopEdgeEntryTopIx.setStatus('current')
ieee8021SpbTopEdgeEntrySysIdNear = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1, 2), MacAddress())
if mibBuilder.loadTexts: ieee8021SpbTopEdgeEntrySysIdNear.setStatus('current')
ieee8021SpbTopEdgeEntrySysIdFar = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1, 3), MacAddress())
if mibBuilder.loadTexts: ieee8021SpbTopEdgeEntrySysIdFar.setStatus('current')
ieee8021SpbTopEdgeEntryMetricNear2Far = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1, 4), IEEE8021SpbLinkMetric()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbTopEdgeEntryMetricNear2Far.setStatus('current')
ieee8021SpbTopEdgeEntryMetricFar2Near = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 10, 1, 5), IEEE8021SpbLinkMetric()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbTopEdgeEntryMetricFar2Near.setStatus('current')
ieee8021SpbmTopSrvTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 11), )
if mibBuilder.loadTexts: ieee8021SpbmTopSrvTable.setStatus('current')
ieee8021SpbmTopSrvTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntryTopIx"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntrySysId"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntryIsid"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntryBaseVid"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntryMac"))
if mibBuilder.loadTexts: ieee8021SpbmTopSrvTableEntry.setStatus('current')
ieee8021SpbmTopSrvEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbmTopSrvEntryTopIx.setStatus('current')
ieee8021SpbmTopSrvEntrySysId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 2), MacAddress())
if mibBuilder.loadTexts: ieee8021SpbmTopSrvEntrySysId.setStatus('current')
ieee8021SpbmTopSrvEntryIsid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 3), IEEE8021SpbServiceIdentifierOrAny())
if mibBuilder.loadTexts: ieee8021SpbmTopSrvEntryIsid.setStatus('current')
ieee8021SpbmTopSrvEntryBaseVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 4), VlanIdOrAny())
if mibBuilder.loadTexts: ieee8021SpbmTopSrvEntryBaseVid.setStatus('current')
ieee8021SpbmTopSrvEntryMac = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 5), MacAddress())
if mibBuilder.loadTexts: ieee8021SpbmTopSrvEntryMac.setStatus('current')
ieee8021SpbmTopSrvEntryIsidFlags = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 11, 1, 6), IEEE8021PbbIngressEgress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbmTopSrvEntryIsidFlags.setStatus('current')
ieee8021SpbvTopSrvTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 12), )
if mibBuilder.loadTexts: ieee8021SpbvTopSrvTable.setStatus('current')
ieee8021SpbvTopSrvTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryTopIx"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntrySysId"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryMMac"))
if mibBuilder.loadTexts: ieee8021SpbvTopSrvTableEntry.setStatus('current')
ieee8021SpbvTopSrvEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021SpbvTopSrvEntryTopIx.setStatus('current')
ieee8021SpbvTopSrvEntrySysId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1, 2), MacAddress())
if mibBuilder.loadTexts: ieee8021SpbvTopSrvEntrySysId.setStatus('current')
ieee8021SpbvTopSrvEntryMMac = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1, 3), MacAddress())
if mibBuilder.loadTexts: ieee8021SpbvTopSrvEntryMMac.setStatus('current')
ieee8021SpbvTopSrvEntryBaseVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1, 4), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbvTopSrvEntryBaseVid.setStatus('current')
ieee8021SpbvTopSrvEntryMMacFlags = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 12, 1, 5), IEEE8021PbbIngressEgress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SpbvTopSrvEntryMMacFlags.setStatus('current')
ieee8021SpbmBsiStaticTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 13), )
if mibBuilder.loadTexts: ieee8021SpbmBsiStaticTable.setStatus('current')
ieee8021SpbmBsiStaticEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbTopIx"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryIsid"), (0, "IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryBaseVid"))
if mibBuilder.loadTexts: ieee8021SpbmBsiStaticEntry.setStatus('current')
ieee8021SpbmBsiStaticEntryIsid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 1), IEEE8021PbbServiceIdentifier())
if mibBuilder.loadTexts: ieee8021SpbmBsiStaticEntryIsid.setStatus('current')
ieee8021SpbmBsiStaticEntryBaseVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 2), VlanId())
if mibBuilder.loadTexts: ieee8021SpbmBsiStaticEntryBaseVid.setStatus('current')
ieee8021SpbmBsiStaticEntryTBit = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbmBsiStaticEntryTBit.setStatus('current')
ieee8021SpbmBsiStaticEntryRBit = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbmBsiStaticEntryRBit.setStatus('current')
ieee8021SpbmBsiStaticEntryTsBit = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbmBsiStaticEntryTsBit.setStatus('current')
ieee8021SpbmBsiStaticEntryTieBreakMask = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbmBsiStaticEntryTieBreakMask.setStatus('current')
ieee8021SpbmBsiStaticEntryRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 13, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SpbmBsiStaticEntryRowStatus.setStatus('current')
dot1agCfmMepSpbmTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 14), )
if mibBuilder.loadTexts: dot1agCfmMepSpbmTable.setStatus('current')
dot1agCfmMepSpbmEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 14, 1), )
dot1agCfmMepEntry.registerAugmentions(("IEEE8021-SPB-MIB", "dot1agCfmMepSpbmEntry"))
dot1agCfmMepSpbmEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
if mibBuilder.loadTexts: dot1agCfmMepSpbmEntry.setStatus('current')
dot1agCfmMepTransmitLbmSpbmDA = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 14, 1, 1), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmSpbmDA.setStatus('current')
dot1agCfmMepTransmitLtmSpbmDA = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 14, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmSpbmDA.setStatus('current')
dot1agCfmMepSpbmEspTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 1, 15), )
if mibBuilder.loadTexts: dot1agCfmMepSpbmEspTable.setStatus('current')
dot1agCfmMepSpbmEspEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 1, 15, 1), ).setIndexNames((0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"), (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"), (0, "IEEE8021-SPB-MIB", "dot1agCfmMepSpbmEspIndex"))
if mibBuilder.loadTexts: dot1agCfmMepSpbmEspEntry.setStatus('current')
dot1agCfmMepSpbmEspIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 15, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmMepSpbmEspIndex.setStatus('current')
dot1agCfmMepSpbmEspEsp = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 15, 1, 2), IEEE8021PbbTeEsp()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepSpbmEspEsp.setStatus('current')
dot1agCfmMepSpbmEspRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 1, 15, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepSpbmEspRowStatus.setStatus('current')
ieee8021PcrEctStaticTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 3, 1), )
if mibBuilder.loadTexts: ieee8021PcrEctStaticTable.setStatus('current')
ieee8021PcrEctStaticTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021PcrEctStaticEntryTopIx"), (0, "IEEE8021-SPB-MIB", "ieee8021PcrEctStaticEntryBaseVid"))
if mibBuilder.loadTexts: ieee8021PcrEctStaticTableEntry.setStatus('current')
ieee8021PcrEctStaticEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021PcrEctStaticEntryTopIx.setStatus('current')
ieee8021PcrEctStaticEntryBaseVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1, 2), VlanIdOrAny())
if mibBuilder.loadTexts: ieee8021PcrEctStaticEntryBaseVid.setStatus('current')
ieee8021PcrEctStaticEntryMrtBlueVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1, 3), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PcrEctStaticEntryMrtBlueVid.setStatus('current')
ieee8021PcrEctStaticEntryMrtRedVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1, 4), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PcrEctStaticEntryMrtRedVid.setStatus('current')
ieee8021PcrEctStaticEntryRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 3, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PcrEctStaticEntryRowStatus.setStatus('current')
ieee8021PcrTopEctTable = MibTable((1, 3, 111, 2, 802, 1, 1, 26, 3, 2), )
if mibBuilder.loadTexts: ieee8021PcrTopEctTable.setStatus('current')
ieee8021PcrTopEctTableEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntryTopIx"), (0, "IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntrySysId"), (0, "IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntryBaseVid"))
if mibBuilder.loadTexts: ieee8021PcrTopEctTableEntry.setStatus('current')
ieee8021PcrTopEctEntryTopIx = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 1), IEEE8021SpbMTID())
if mibBuilder.loadTexts: ieee8021PcrTopEctEntryTopIx.setStatus('current')
ieee8021PcrTopEctEntrySysId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 2), MacAddress())
if mibBuilder.loadTexts: ieee8021PcrTopEctEntrySysId.setStatus('current')
ieee8021PcrTopEctEntryBaseVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 3), VlanIdOrAny())
if mibBuilder.loadTexts: ieee8021PcrTopEctEntryBaseVid.setStatus('current')
ieee8021PcrTopEctEntryMode = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 4), IEEE8021SpbEctMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PcrTopEctEntryMode.setStatus('current')
ieee8021PcrTopEctEntryMrtBlueVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 5), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PcrTopEctEntryMrtBlueVid.setStatus('current')
ieee8021PcrTopEctEntryMrtRedVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 26, 3, 2, 1, 6), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PcrTopEctEntryMrtRedVid.setStatus('current')
ieee8021SpbConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 26, 2))
ieee8021SpbGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 26, 2, 1))
ieee8021SpbCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 26, 2, 2))
ieee8021PcrConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 26, 4))
ieee8021PcrGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 26, 4, 1))
ieee8021PcrCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 26, 4, 2))
ieee8021SpbSysGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 1)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbSysAreaAddress"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysId"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysControlAddr"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysName"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysBridgePriority"), ("IEEE8021-SPB-MIB", "ieee8021SpbmSysSPSourceId"), ("IEEE8021-SPB-MIB", "ieee8021SpbmSysMode"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysDigestConvention"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbSysGroupSPBM = ieee8021SpbSysGroupSPBM.setStatus('current')
ieee8021SpbMtidStaticTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 2)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbMTidStaticEntryMtidOverload"), ("IEEE8021-SPB-MIB", "ieee8021SpbMtidStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbMtidStaticTableGroupSPBM = ieee8021SpbMtidStaticTableGroupSPBM.setStatus('current')
ieee8021SpbTopIxDynamicTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 3)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAgreeDigest"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryMCID"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAuxMCID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbTopIxDynamicTableGroupSPBM = ieee8021SpbTopIxDynamicTableGroupSPBM.setStatus('current')
ieee8021SpbEctStaticTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 4)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryEctAlgorithm"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbEctStaticTableGroupSPBM = ieee8021SpbEctStaticTableGroupSPBM.setStatus('current')
ieee8021SpbEctDynamicTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 5)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryMode"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryLocalUse"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryRemoteUse"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryIngressCheckDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbEctDynamicTableGroupSPBM = ieee8021SpbEctDynamicTableGroupSPBM.setStatus('current')
ieee8021SpbAdjStaticTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 6)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryMetric"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryIfAdminState"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbAdjStaticTableGroupSPBM = ieee8021SpbAdjStaticTableGroupSPBM.setStatus('current')
ieee8021SpbAdjDynamicTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 7)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPort"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIfOperState"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerSysName"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAgreeDigest"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerMCID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAuxMCID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryLocalCircuitID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerLocalCircuitID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPortIdentifier"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerPortIdentifier"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIsisCircIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbAdjDynamicTableGroupSPBM = ieee8021SpbAdjDynamicTableGroupSPBM.setStatus('current')
ieee8021SpbTopNodeTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 8)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntryBridgePriority"), ("IEEE8021-SPB-MIB", "ieee8021SpbmTopNodeEntrySPsourceID"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntrySysName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbTopNodeTableGroupSPBM = ieee8021SpbTopNodeTableGroupSPBM.setStatus('current')
ieee8021SpbTopEctTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 9)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryEctAlgorithm"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryMode"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryLocalUse"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbTopEctTableGroupSPBM = ieee8021SpbTopEctTableGroupSPBM.setStatus('current')
ieee8021SpbTopEdgeTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 10)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricNear2Far"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricFar2Near"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbTopEdgeTableGroupSPBM = ieee8021SpbTopEdgeTableGroupSPBM.setStatus('current')
ieee8021SpbmTopSrvTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 11)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvEntryIsidFlags"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbmTopSrvTableGroupSPBM = ieee8021SpbmTopSrvTableGroupSPBM.setStatus('current')
ieee8021SpbSysGroupSPBV = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 12)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbSysAreaAddress"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysId"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysControlAddr"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysName"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysBridgePriority"), ("IEEE8021-SPB-MIB", "ieee8021SpbvSysMode"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysDigestConvention"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbSysGroupSPBV = ieee8021SpbSysGroupSPBV.setStatus('current')
ieee8021SpbMtidStaticTableGroupSPBV = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 13)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbMTidStaticEntryMtidOverload"), ("IEEE8021-SPB-MIB", "ieee8021SpbMtidStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbMtidStaticTableGroupSPBV = ieee8021SpbMtidStaticTableGroupSPBV.setStatus('current')
ieee8021SpbTopIxDynamicTableGroupSPBV = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 14)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAgreeDigest"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryMCID"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAuxMCID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbTopIxDynamicTableGroupSPBV = ieee8021SpbTopIxDynamicTableGroupSPBV.setStatus('current')
ieee8021SpbEctStaticTableGroupSPBV = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 15)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryEctAlgorithm"), ("IEEE8021-SPB-MIB", "ieee8021SpbvEctStaticEntrySpvid"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbEctStaticTableGroupSPBV = ieee8021SpbEctStaticTableGroupSPBV.setStatus('current')
ieee8021SpbEctDynamicTableGroupSPBV = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 16)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryMode"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryLocalUse"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryRemoteUse"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryIngressCheckDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbEctDynamicTableGroupSPBV = ieee8021SpbEctDynamicTableGroupSPBV.setStatus('current')
ieee8021SpbAdjStaticTableGroupSPBV = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 17)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryMetric"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryIfAdminState"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbAdjStaticTableGroupSPBV = ieee8021SpbAdjStaticTableGroupSPBV.setStatus('current')
ieee8021SpbAdjDynamicTableGroupSPBV = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 18)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPort"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIfOperState"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerSysName"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAgreeDigest"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerMCID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAuxMCID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryLocalCircuitID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerLocalCircuitID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPortIdentifier"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerPortIdentifier"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIsisCircIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbAdjDynamicTableGroupSPBV = ieee8021SpbAdjDynamicTableGroupSPBV.setStatus('current')
ieee8021SpbTopNodeTableGroupSPBV = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 19)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntryBridgePriority"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntrySysName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbTopNodeTableGroupSPBV = ieee8021SpbTopNodeTableGroupSPBV.setStatus('current')
ieee8021SpbTopEctTableGroupSPBV = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 20)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryEctAlgorithm"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryMode"), ("IEEE8021-SPB-MIB", "ieee8021SpbvTopEctSysMode"), ("IEEE8021-SPB-MIB", "ieee8021SpbvTopEctEntrySpvid"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopEctEntryLocalUse"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbTopEctTableGroupSPBV = ieee8021SpbTopEctTableGroupSPBV.setStatus('current')
ieee8021SpbTopEdgeTableGroupSPBV = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 21)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricNear2Far"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricFar2Near"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbTopEdgeTableGroupSPBV = ieee8021SpbTopEdgeTableGroupSPBV.setStatus('current')
ieee8021SpbvTopSrvTableGroupSPBV = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 22)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryBaseVid"), ("IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryMMacFlags"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbvTopSrvTableGroupSPBV = ieee8021SpbvTopSrvTableGroupSPBV.setStatus('current')
ieee8021SpbmBsiStaticTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 23)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryTBit"), ("IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryRBit"), ("IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryTsBit"), ("IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryTieBreakMask"), ("IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbmBsiStaticTableGroupSPBM = ieee8021SpbmBsiStaticTableGroupSPBM.setStatus('current')
dot1agCfmMepSpbmTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 24)).setObjects(("IEEE8021-SPB-MIB", "dot1agCfmMepTransmitLbmSpbmDA"), ("IEEE8021-SPB-MIB", "dot1agCfmMepTransmitLtmSpbmDA"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmMepSpbmTableGroupSPBM = dot1agCfmMepSpbmTableGroupSPBM.setStatus('current')
dot1agCfmMepSpbmEspTableGroupSPBM = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 2, 1, 25)).setObjects(("IEEE8021-SPB-MIB", "dot1agCfmMepSpbmEspEsp"), ("IEEE8021-SPB-MIB", "dot1agCfmMepSpbmEspRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1agCfmMepSpbmEspTableGroupSPBM = dot1agCfmMepSpbmEspTableGroupSPBM.setStatus('current')
ieee8021PcrSysGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 1)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbSysAreaAddress"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysId"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysControlAddr"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysName"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysBridgePriority"), ("IEEE8021-SPB-MIB", "ieee8021SpbmSysSPSourceId"), ("IEEE8021-SPB-MIB", "ieee8021SpbmSysMode"), ("IEEE8021-SPB-MIB", "ieee8021SpbvSysMode"), ("IEEE8021-SPB-MIB", "ieee8021SpbSysDigestConvention"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrSysGroup = ieee8021PcrSysGroup.setStatus('current')
ieee8021PcrMtidStaticTableGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 2)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbMTidStaticEntryMtidOverload"), ("IEEE8021-SPB-MIB", "ieee8021SpbMtidStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrMtidStaticTableGroup = ieee8021PcrMtidStaticTableGroup.setStatus('current')
ieee8021PcrTopIxDynamicTableGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 3)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAgreeDigest"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryMCID"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicEntryAuxMCID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrTopIxDynamicTableGroup = ieee8021PcrTopIxDynamicTableGroup.setStatus('current')
ieee8021PcrEctStaticTableGroupMAC = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 4)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryEctAlgorithm"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrEctStaticTableGroupMAC = ieee8021PcrEctStaticTableGroupMAC.setStatus('current')
ieee8021PcrEctStaticTableGroupVID = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 5)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryEctAlgorithm"), ("IEEE8021-SPB-MIB", "ieee8021SpbvEctStaticEntrySpvid"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrEctStaticTableGroupVID = ieee8021PcrEctStaticTableGroupVID.setStatus('current')
ieee8021PcrEctStaticTableGroupMrt = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 6)).setObjects(("IEEE8021-SPB-MIB", "ieee8021PcrEctStaticEntryMrtBlueVid"), ("IEEE8021-SPB-MIB", "ieee8021PcrEctStaticEntryMrtRedVid"), ("IEEE8021-SPB-MIB", "ieee8021PcrEctStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrEctStaticTableGroupMrt = ieee8021PcrEctStaticTableGroupMrt.setStatus('current')
ieee8021PcrEctDynamicTableGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 7)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryMode"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryLocalUse"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryRemoteUse"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicEntryIngressCheckDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrEctDynamicTableGroup = ieee8021PcrEctDynamicTableGroup.setStatus('current')
ieee8021PcrAdjStaticTableGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 8)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryMetric"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryIfAdminState"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrAdjStaticTableGroup = ieee8021PcrAdjStaticTableGroup.setStatus('current')
ieee8021PcrAdjDynamicTableGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 9)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPort"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIfOperState"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerSysName"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAgreeDigest"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerMCID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerAuxMCID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryLocalCircuitID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerLocalCircuitID"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPortIdentifier"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryPeerPortIdentifier"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicEntryIsisCircIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrAdjDynamicTableGroup = ieee8021PcrAdjDynamicTableGroup.setStatus('current')
ieee8021PcrTopNodeTableGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 10)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntryBridgePriority"), ("IEEE8021-SPB-MIB", "ieee8021SpbmTopNodeEntrySPsourceID"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeEntrySysName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrTopNodeTableGroup = ieee8021PcrTopNodeTableGroup.setStatus('current')
ieee8021PcrTopEctTableGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 11)).setObjects(("IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntryMode"), ("IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntryMrtBlueVid"), ("IEEE8021-SPB-MIB", "ieee8021PcrTopEctEntryMrtRedVid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrTopEctTableGroup = ieee8021PcrTopEctTableGroup.setStatus('current')
ieee8021PcrTopEdgeTableGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 12)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricNear2Far"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeEntryMetricFar2Near"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrTopEdgeTableGroup = ieee8021PcrTopEdgeTableGroup.setStatus('current')
ieee8021PcrTopSrvTableGroupVid = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 26, 4, 1, 13)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryBaseVid"), ("IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvEntryMMacFlags"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrTopSrvTableGroupVid = ieee8021PcrTopSrvTableGroupVid.setStatus('current')
ieee8021SpbComplianceSPBM = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 26, 2, 2, 1)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbSysGroupSPBM"), ("IEEE8021-SPB-MIB", "ieee8021SpbMtidStaticTableGroupSPBM"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicTableGroupSPBM"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticTableGroupSPBM"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicTableGroupSPBM"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticTableGroupSPBM"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicTableGroupSPBM"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeTableGroupSPBM"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopEctTableGroupSPBM"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeTableGroupSPBM"), ("IEEE8021-SPB-MIB", "ieee8021SpbmTopSrvTableGroupSPBM"), ("IEEE8021-SPB-MIB", "ieee8021SpbmBsiStaticTableGroupSPBM"), ("IEEE8021-SPB-MIB", "dot1agCfmMepSpbmTableGroupSPBM"), ("IEEE8021-SPB-MIB", "dot1agCfmMepSpbmEspTableGroupSPBM"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbComplianceSPBM = ieee8021SpbComplianceSPBM.setStatus('current')
ieee8021SpbComplianceSPBV = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 26, 2, 2, 2)).setObjects(("IEEE8021-SPB-MIB", "ieee8021SpbSysGroupSPBV"), ("IEEE8021-SPB-MIB", "ieee8021SpbMtidStaticTableGroupSPBV"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopIxDynamicTableGroupSPBV"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctStaticTableGroupSPBV"), ("IEEE8021-SPB-MIB", "ieee8021SpbEctDynamicTableGroupSPBV"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjStaticTableGroupSPBV"), ("IEEE8021-SPB-MIB", "ieee8021SpbAdjDynamicTableGroupSPBV"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopNodeTableGroupSPBV"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopEctTableGroupSPBV"), ("IEEE8021-SPB-MIB", "ieee8021SpbTopEdgeTableGroupSPBV"), ("IEEE8021-SPB-MIB", "ieee8021SpbvTopSrvTableGroupSPBV"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SpbComplianceSPBV = ieee8021SpbComplianceSPBV.setStatus('current')
ieee8021PcrCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 26, 4, 2, 1)).setObjects(("IEEE8021-SPB-MIB", "ieee8021PcrSysGroup"), ("IEEE8021-SPB-MIB", "ieee8021PcrMtidStaticTableGroup"), ("IEEE8021-SPB-MIB", "ieee8021PcrTopIxDynamicTableGroup"), ("IEEE8021-SPB-MIB", "ieee8021PcrEctStaticTableGroupMAC"), ("IEEE8021-SPB-MIB", "ieee8021PcrEctStaticTableGroupVID"), ("IEEE8021-SPB-MIB", "ieee8021PcrEctStaticTableGroupMrt"), ("IEEE8021-SPB-MIB", "ieee8021PcrEctDynamicTableGroup"), ("IEEE8021-SPB-MIB", "ieee8021PcrAdjStaticTableGroup"), ("IEEE8021-SPB-MIB", "ieee8021PcrAdjDynamicTableGroup"), ("IEEE8021-SPB-MIB", "ieee8021PcrTopNodeTableGroup"), ("IEEE8021-SPB-MIB", "ieee8021PcrTopEctTableGroup"), ("IEEE8021-SPB-MIB", "ieee8021PcrTopEdgeTableGroup"), ("IEEE8021-SPB-MIB", "ieee8021PcrTopSrvTableGroupVid"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PcrCompliance = ieee8021PcrCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-SPB-MIB", ieee8021SpbAdjStaticEntryMetric=ieee8021SpbAdjStaticEntryMetric, ieee8021SpbAdjDynamicEntryPeerSysName=ieee8021SpbAdjDynamicEntryPeerSysName, ieee8021SpbTopIxDynamicEntryAuxMCID=ieee8021SpbTopIxDynamicEntryAuxMCID, ieee8021SpbTopNodeEntryTopIx=ieee8021SpbTopNodeEntryTopIx, ieee8021PcrTopEctEntryMrtRedVid=ieee8021PcrTopEctEntryMrtRedVid, ieee8021SpbCompliances=ieee8021SpbCompliances, ieee8021SpbEctStaticEntryRowStatus=ieee8021SpbEctStaticEntryRowStatus, dot1agCfmMepSpbmEntry=dot1agCfmMepSpbmEntry, ieee8021SpbSysId=ieee8021SpbSysId, dot1agCfmMepTransmitLbmSpbmDA=dot1agCfmMepTransmitLbmSpbmDA, dot1agCfmMepSpbmEspRowStatus=dot1agCfmMepSpbmEspRowStatus, ieee8021SpbmBsiStaticEntryTsBit=ieee8021SpbmBsiStaticEntryTsBit, ieee8021SpbTopNodeTable=ieee8021SpbTopNodeTable, ieee8021SpbTopNodeTableGroupSPBV=ieee8021SpbTopNodeTableGroupSPBV, ieee8021PcrCompliances=ieee8021PcrCompliances, IEEE8021SpbMCID=IEEE8021SpbMCID, ieee8021SpbEctDynamicTableGroupSPBM=ieee8021SpbEctDynamicTableGroupSPBM, ieee8021SpbTopEdgeTableGroupSPBM=ieee8021SpbTopEdgeTableGroupSPBM, ieee8021SpbEctDynamicEntryRemoteUse=ieee8021SpbEctDynamicEntryRemoteUse, ieee8021PcrAdjDynamicTableGroup=ieee8021PcrAdjDynamicTableGroup, ieee8021SpbTopEctEntryMode=ieee8021SpbTopEctEntryMode, ieee8021PcrEctDynamicTableGroup=ieee8021PcrEctDynamicTableGroup, ieee8021PcrTopEctEntrySysId=ieee8021PcrTopEctEntrySysId, ieee8021SpbTopEctTableGroupSPBM=ieee8021SpbTopEctTableGroupSPBM, ieee8021PcrAdjStaticTableGroup=ieee8021PcrAdjStaticTableGroup, ieee8021SpbEctDynamicEntryBaseVid=ieee8021SpbEctDynamicEntryBaseVid, ieee8021SpbvTopSrvEntryBaseVid=ieee8021SpbvTopSrvEntryBaseVid, ieee8021PcrObjects=ieee8021PcrObjects, ieee8021SpbConformance=ieee8021SpbConformance, ieee8021SpbvEctStaticEntrySpvid=ieee8021SpbvEctStaticEntrySpvid, ieee8021SpbTopEctTableEntry=ieee8021SpbTopEctTableEntry, ieee8021SpbmTopSrvEntryBaseVid=ieee8021SpbmTopSrvEntryBaseVid, ieee8021SpbmTopSrvEntryIsidFlags=ieee8021SpbmTopSrvEntryIsidFlags, dot1agCfmMepSpbmTableGroupSPBM=dot1agCfmMepSpbmTableGroupSPBM, ieee8021PcrTopNodeTableGroup=ieee8021PcrTopNodeTableGroup, ieee8021SpbTopNodeEntrySysName=ieee8021SpbTopNodeEntrySysName, ieee8021SpbAdjDynamicTableEntry=ieee8021SpbAdjDynamicTableEntry, ieee8021PcrEctStaticEntryBaseVid=ieee8021PcrEctStaticEntryBaseVid, ieee8021SpbMtidStaticTableEntry=ieee8021SpbMtidStaticTableEntry, ieee8021SpbEctDynamicEntryLocalUse=ieee8021SpbEctDynamicEntryLocalUse, ieee8021SpbTopNodeTableEntry=ieee8021SpbTopNodeTableEntry, ieee8021SpbTopIxDynamicTableGroupSPBM=ieee8021SpbTopIxDynamicTableGroupSPBM, ieee8021SpbAdjDynamicEntryTopIx=ieee8021SpbAdjDynamicEntryTopIx, ieee8021SpbTopNodeEntryBridgePriority=ieee8021SpbTopNodeEntryBridgePriority, IEEE8021SpbAdjState=IEEE8021SpbAdjState, IEEE8021SpbMode=IEEE8021SpbMode, ieee8021SpbComplianceSPBM=ieee8021SpbComplianceSPBM, ieee8021PcrTopEdgeTableGroup=ieee8021PcrTopEdgeTableGroup, ieee8021SpbAdjDynamicTableGroupSPBV=ieee8021SpbAdjDynamicTableGroupSPBV, IEEE8021SpbEctAlgorithm=IEEE8021SpbEctAlgorithm, ieee8021PcrEctStaticEntryMrtBlueVid=ieee8021PcrEctStaticEntryMrtBlueVid, ieee8021SpbAdjStaticEntryRowStatus=ieee8021SpbAdjStaticEntryRowStatus, ieee8021SpbmBsiStaticEntryRBit=ieee8021SpbmBsiStaticEntryRBit, ieee8021SpbvTopSrvEntryMMacFlags=ieee8021SpbvTopSrvEntryMMacFlags, ieee8021PcrEctStaticTable=ieee8021PcrEctStaticTable, ieee8021PcrEctStaticTableGroupMAC=ieee8021PcrEctStaticTableGroupMAC, ieee8021SpbTopEctEntryEctAlgorithm=ieee8021SpbTopEctEntryEctAlgorithm, ieee8021SpbmBsiStaticEntryIsid=ieee8021SpbmBsiStaticEntryIsid, ieee8021SpbAdjDynamicEntryPeerMCID=ieee8021SpbAdjDynamicEntryPeerMCID, ieee8021SpbTopEctEntryBaseVid=ieee8021SpbTopEctEntryBaseVid, ieee8021SpbTopEctEntryTopIx=ieee8021SpbTopEctEntryTopIx, dot1agCfmMepSpbmEspEsp=dot1agCfmMepSpbmEspEsp, ieee8021SpbTopEdgeEntryTopIx=ieee8021SpbTopEdgeEntryTopIx, ieee8021SpbTopEdgeEntrySysIdFar=ieee8021SpbTopEdgeEntrySysIdFar, ieee8021SpbmTopSrvEntryIsid=ieee8021SpbmTopSrvEntryIsid, ieee8021PcrTopEctEntryMode=ieee8021PcrTopEctEntryMode, ieee8021SpbAdjDynamicEntryPortIdentifier=ieee8021SpbAdjDynamicEntryPortIdentifier, ieee8021SpbTopIxDynamicEntryMCID=ieee8021SpbTopIxDynamicEntryMCID, ieee8021SpbvTopEctSysMode=ieee8021SpbvTopEctSysMode, ieee8021SpbEctDynamicTable=ieee8021SpbEctDynamicTable, ieee8021SpbEctDynamicTableEntry=ieee8021SpbEctDynamicTableEntry, IEEE8021SpbDigestConvention=IEEE8021SpbDigestConvention, ieee8021PcrEctStaticEntryTopIx=ieee8021PcrEctStaticEntryTopIx, ieee8021SpbmTopSrvEntrySysId=ieee8021SpbmTopSrvEntrySysId, ieee8021SpbEctStaticTableGroupSPBM=ieee8021SpbEctStaticTableGroupSPBM, ieee8021SpbAdjDynamicTableGroupSPBM=ieee8021SpbAdjDynamicTableGroupSPBM, dot1agCfmMepSpbmEspTableGroupSPBM=dot1agCfmMepSpbmEspTableGroupSPBM, ieee8021SpbEctDynamicEntryIngressCheckDiscards=ieee8021SpbEctDynamicEntryIngressCheckDiscards, ieee8021SpbSysControlAddr=ieee8021SpbSysControlAddr, IEEE8021SpbEctMode=IEEE8021SpbEctMode, ieee8021SpbmTopSrvTable=ieee8021SpbmTopSrvTable, ieee8021PcrTopEctTableEntry=ieee8021PcrTopEctTableEntry, ieee8021SpbvTopSrvEntryTopIx=ieee8021SpbvTopSrvEntryTopIx, ieee8021SpbMtidStaticEntryMtid=ieee8021SpbMtidStaticEntryMtid, dot1agCfmMepSpbmEspEntry=dot1agCfmMepSpbmEspEntry, ieee8021SpbvTopSrvTable=ieee8021SpbvTopSrvTable, IEEE8021SpbmSPsourceId=IEEE8021SpbmSPsourceId, ieee8021SpbTopEdgeTableEntry=ieee8021SpbTopEdgeTableEntry, ieee8021SpbSysBridgePriority=ieee8021SpbSysBridgePriority, ieee8021SpbmBsiStaticEntry=ieee8021SpbmBsiStaticEntry, ieee8021SpbTopIxDynamicEntryAgreeDigest=ieee8021SpbTopIxDynamicEntryAgreeDigest, ieee8021PcrGroups=ieee8021PcrGroups, ieee8021PcrEctStaticTableGroupMrt=ieee8021PcrEctStaticTableGroupMrt, ieee8021PcrTopEctEntryBaseVid=ieee8021PcrTopEctEntryBaseVid, ieee8021SpbmBsiStaticTable=ieee8021SpbmBsiStaticTable, ieee8021SpbTopEctTable=ieee8021SpbTopEctTable, ieee8021SpbAdjStaticTableGroupSPBM=ieee8021SpbAdjStaticTableGroupSPBM, ieee8021SpbEctStaticEntryBaseVid=ieee8021SpbEctStaticEntryBaseVid, ieee8021PcrTopEctEntryTopIx=ieee8021PcrTopEctEntryTopIx, ieee8021SpbGroups=ieee8021SpbGroups, ieee8021SpbAdjStaticEntryIfIndex=ieee8021SpbAdjStaticEntryIfIndex, ieee8021SpbTopIxDynamicEntryTopIx=ieee8021SpbTopIxDynamicEntryTopIx, ieee8021SpbComplianceSPBV=ieee8021SpbComplianceSPBV, ieee8021SpbvTopSrvEntryMMac=ieee8021SpbvTopSrvEntryMMac, ieee8021SpbAdjDynamicEntryPort=ieee8021SpbAdjDynamicEntryPort, ieee8021SpbmBsiStaticEntryBaseVid=ieee8021SpbmBsiStaticEntryBaseVid, IEEE8021SpbAreaAddress=IEEE8021SpbAreaAddress, ieee8021SpbAdjDynamicEntryIfIndex=ieee8021SpbAdjDynamicEntryIfIndex, ieee8021SpbTopEdgeEntryMetricNear2Far=ieee8021SpbTopEdgeEntryMetricNear2Far, IEEE8021SpbDigest=IEEE8021SpbDigest, ieee8021SpbmTopNodeEntrySPsourceID=ieee8021SpbmTopNodeEntrySPsourceID, ieee8021SpbAdjStaticTableGroupSPBV=ieee8021SpbAdjStaticTableGroupSPBV, ieee8021SpbMTidStaticEntryMtidOverload=ieee8021SpbMTidStaticEntryMtidOverload, ieee8021SpbTopIxDynamicTableGroupSPBV=ieee8021SpbTopIxDynamicTableGroupSPBV, dot1agCfmMepTransmitLtmSpbmDA=dot1agCfmMepTransmitLtmSpbmDA, ieee8021PcrTopEctTableGroup=ieee8021PcrTopEctTableGroup, ieee8021SpbmTopSrvTableGroupSPBM=ieee8021SpbmTopSrvTableGroupSPBM, ieee8021SpbTopNodeEntrySysId=ieee8021SpbTopNodeEntrySysId, ieee8021SpbmSysMode=ieee8021SpbmSysMode, ieee8021SpbAdjDynamicEntryLocalCircuitID=ieee8021SpbAdjDynamicEntryLocalCircuitID, ieee8021PcrEctStaticEntryRowStatus=ieee8021PcrEctStaticEntryRowStatus, ieee8021SpbAdjDynamicEntryIsisCircIndex=ieee8021SpbAdjDynamicEntryIsisCircIndex, dot1agCfmMepSpbmEspIndex=dot1agCfmMepSpbmEspIndex, ieee8021SpbAdjDynamicEntryPeerSysId=ieee8021SpbAdjDynamicEntryPeerSysId, ieee8021PcrTopEctTable=ieee8021PcrTopEctTable, ieee8021SpbMtidStaticTableGroupSPBV=ieee8021SpbMtidStaticTableGroupSPBV, ieee8021PcrSysGroup=ieee8021PcrSysGroup, ieee8021SpbObjects=ieee8021SpbObjects, ieee8021SpbSys=ieee8021SpbSys, ieee8021SpbTopIxDynamicTable=ieee8021SpbTopIxDynamicTable, ieee8021SpbAdjStaticEntryIfAdminState=ieee8021SpbAdjStaticEntryIfAdminState, ieee8021SpbTopEdgeEntryMetricFar2Near=ieee8021SpbTopEdgeEntryMetricFar2Near, ieee8021SpbmBsiStaticEntryTieBreakMask=ieee8021SpbmBsiStaticEntryTieBreakMask, ieee8021SpbSysGroupSPBV=ieee8021SpbSysGroupSPBV, ieee8021SpbmBsiStaticEntryTBit=ieee8021SpbmBsiStaticEntryTBit, ieee8021SpbEctStaticTableEntry=ieee8021SpbEctStaticTableEntry, ieee8021PcrEctStaticEntryMrtRedVid=ieee8021PcrEctStaticEntryMrtRedVid, ieee8021PcrTopEctEntryMrtBlueVid=ieee8021PcrTopEctEntryMrtBlueVid, ieee8021SpbEctDynamicTableGroupSPBV=ieee8021SpbEctDynamicTableGroupSPBV, ieee8021SpbSysName=ieee8021SpbSysName, ieee8021SpbTopEctEntryLocalUse=ieee8021SpbTopEctEntryLocalUse, ieee8021PcrCompliance=ieee8021PcrCompliance, ieee8021SpbTopEdgeTable=ieee8021SpbTopEdgeTable, ieee8021SpbSysAreaAddress=ieee8021SpbSysAreaAddress, ieee8021SpbmSysSPSourceId=ieee8021SpbmSysSPSourceId, IEEE8021SpbLinkMetric=IEEE8021SpbLinkMetric, ieee8021SpbTopEdgeEntrySysIdNear=ieee8021SpbTopEdgeEntrySysIdNear, ieee8021SpbAdjStaticTable=ieee8021SpbAdjStaticTable, ieee8021SpbvTopSrvTableGroupSPBV=ieee8021SpbvTopSrvTableGroupSPBV, ieee8021SpbvSysMode=ieee8021SpbvSysMode, ieee8021SpbEctStaticEntryTopIx=ieee8021SpbEctStaticEntryTopIx, ieee8021SpbMtidStaticTableGroupSPBM=ieee8021SpbMtidStaticTableGroupSPBM, ieee8021SpbEctStaticTable=ieee8021SpbEctStaticTable, ieee8021SpbAdjDynamicEntryPeerPortIdentifier=ieee8021SpbAdjDynamicEntryPeerPortIdentifier, ieee8021SpbTopIxDynamicTableEntry=ieee8021SpbTopIxDynamicTableEntry, ieee8021SpbAdjDynamicTable=ieee8021SpbAdjDynamicTable, ieee8021SpbTopNodeTableGroupSPBM=ieee8021SpbTopNodeTableGroupSPBM, ieee8021SpbAdjStaticTableEntry=ieee8021SpbAdjStaticTableEntry, ieee8021SpbmTopSrvTableEntry=ieee8021SpbmTopSrvTableEntry, dot1agCfmMepSpbmTable=dot1agCfmMepSpbmTable, ieee8021PcrTopSrvTableGroupVid=ieee8021PcrTopSrvTableGroupVid, ieee8021SpbvTopSrvTableEntry=ieee8021SpbvTopSrvTableEntry, ieee8021SpbEctStaticEntryEctAlgorithm=ieee8021SpbEctStaticEntryEctAlgorithm, IEEE8021SpbServiceIdentifierOrAny=IEEE8021SpbServiceIdentifierOrAny, IEEE8021SpbBridgePriority=IEEE8021SpbBridgePriority, ieee8021PcrTopIxDynamicTableGroup=ieee8021PcrTopIxDynamicTableGroup, ieee8021PcrMtidStaticTableGroup=ieee8021PcrMtidStaticTableGroup, ieee8021SpbmBsiStaticTableGroupSPBM=ieee8021SpbmBsiStaticTableGroupSPBM, ieee8021PcrEctStaticTableEntry=ieee8021PcrEctStaticTableEntry, dot1agCfmMepSpbmEspTable=dot1agCfmMepSpbmEspTable, ieee8021SpbvTopEctEntrySpvid=ieee8021SpbvTopEctEntrySpvid, ieee8021SpbTopEdgeTableGroupSPBV=ieee8021SpbTopEdgeTableGroupSPBV, ieee8021SpbAdjDynamicEntryIfOperState=ieee8021SpbAdjDynamicEntryIfOperState, ieee8021SpbvTopSrvEntrySysId=ieee8021SpbvTopSrvEntrySysId, ieee8021SpbEctDynamicEntryTopIx=ieee8021SpbEctDynamicEntryTopIx, ieee8021SpbAdjDynamicEntryPeerLocalCircuitID=ieee8021SpbAdjDynamicEntryPeerLocalCircuitID, ieee8021PcrEctStaticTableGroupVID=ieee8021PcrEctStaticTableGroupVID, ieee8021SpbSysDigestConvention=ieee8021SpbSysDigestConvention, IEEE8021SpbMTID=IEEE8021SpbMTID, PYSNMP_MODULE_ID=ieee8021SpbMib, ieee8021SpbMtidStaticTable=ieee8021SpbMtidStaticTable, ieee8021SpbMib=ieee8021SpbMib, ieee8021SpbmTopSrvEntryMac=ieee8021SpbmTopSrvEntryMac, ieee8021SpbmTopSrvEntryTopIx=ieee8021SpbmTopSrvEntryTopIx, ieee8021PcrConformance=ieee8021PcrConformance, ieee8021SpbEctDynamicEntryMode=ieee8021SpbEctDynamicEntryMode, ieee8021SpbAdjDynamicEntryPeerAgreeDigest=ieee8021SpbAdjDynamicEntryPeerAgreeDigest, ieee8021SpbAdjDynamicEntryPeerAuxMCID=ieee8021SpbAdjDynamicEntryPeerAuxMCID, ieee8021SpbEctStaticTableGroupSPBV=ieee8021SpbEctStaticTableGroupSPBV, ieee8021SpbTopIx=ieee8021SpbTopIx, ieee8021SpbTopEctEntrySysId=ieee8021SpbTopEctEntrySysId, ieee8021SpbmBsiStaticEntryRowStatus=ieee8021SpbmBsiStaticEntryRowStatus, ieee8021SpbSysGroupSPBM=ieee8021SpbSysGroupSPBM, ieee8021SpbAdjStaticEntryTopIx=ieee8021SpbAdjStaticEntryTopIx, ieee8021SpbTopEctTableGroupSPBV=ieee8021SpbTopEctTableGroupSPBV, ieee8021SpbMtidStaticEntryRowStatus=ieee8021SpbMtidStaticEntryRowStatus)
