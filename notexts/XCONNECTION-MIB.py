#
# PySNMP MIB module XCONNECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/XCONNECTION-MIB
# Produced by pysmi-1.1.3 at Tue Nov 30 02:57:32 2021
# On host fv-az77-605 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
SagemBoolean, = mibBuilder.importSymbols("EQUIPMENT-MIB", "SagemBoolean")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, Unsigned32, IpAddress, Counter64, MibIdentifier, TimeTicks, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "MibIdentifier", "TimeTicks", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xconnection = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 108))
if mibBuilder.loadTexts: xconnection.setLastUpdated('0205220000Z')
if mibBuilder.loadTexts: xconnection.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
link = MibIdentifier((1, 3, 6, 1, 4, 1, 1038, 108, 10))
xcon = MibIdentifier((1, 3, 6, 1, 4, 1, 1038, 108, 30))
class TrafficStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("working", 1), ("protection", 2))

class ProtectionType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("snc", 1))

class ProtectionStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("used", 1))

class LinkDirection(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unidirectional", 1), ("bidirectional", 2))

class CTPType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 10, 20, 50, 51, 52, 53, 60, 61, 62, 100))
    namedValues = NamedValues(("unknown", 0), ("au", 1), ("au4c", 2), ("au16c", 3), ("tu3", 10), ("tu12", 20), ("pdh2M", 50), ("pdh34M", 51), ("pdh45M", 52), ("pdh140M", 53), ("eth10M", 60), ("eth100M", 61), ("eth1G", 62), ("nspi", 100))

linkNumber = MibScalar((1, 3, 6, 1, 4, 1, 1038, 108, 10, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkNumber.setStatus('current')
linkTable = MibTable((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2), )
if mibBuilder.loadTexts: linkTable.setStatus('current')
linkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1), ).setIndexNames((0, "XCONNECTION-MIB", "linkIndex"))
if mibBuilder.loadTexts: linkEntry.setStatus('current')
linkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkIndex.setStatus('current')
linkSinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 2), CTPType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkSinkType.setStatus('current')
linkSrcType = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 3), CTPType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkSrcType.setStatus('current')
linkCTPSink = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkCTPSink.setStatus('current')
linkCTPSource = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkCTPSource.setStatus('current')
linkName = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: linkName.setStatus('current')
linkGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: linkGroupId.setStatus('current')
linkDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 8), LinkDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkDirection.setStatus('current')
linkProtectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 9), ProtectionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: linkProtectionType.setStatus('current')
linkProtectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 10), ProtectionStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkProtectionStatus.setStatus('current')
linkTrafficStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 11), TrafficStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkTrafficStatus.setStatus('current')
linkImplementation = MibTableColumn((1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 12), SagemBoolean()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: linkImplementation.setStatus('current')
class XconDir(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("unidirectional", 1), ("bidirectional", 2))

class ActionType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("creation", 1), ("deletion", 2))

xconNumber = MibScalar((1, 3, 6, 1, 4, 1, 1038, 108, 30, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xconNumber.setStatus('current')
xconSinkType = MibScalar((1, 3, 6, 1, 4, 1, 1038, 108, 30, 2), CTPType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xconSinkType.setStatus('current')
xconSinkIndex = MibScalar((1, 3, 6, 1, 4, 1, 1038, 108, 30, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xconSinkIndex.setStatus('current')
xconSrcType = MibScalar((1, 3, 6, 1, 4, 1, 1038, 108, 30, 4), CTPType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xconSrcType.setStatus('current')
xconSrcIndex = MibScalar((1, 3, 6, 1, 4, 1, 1038, 108, 30, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xconSrcIndex.setStatus('current')
xconDirection = MibScalar((1, 3, 6, 1, 4, 1, 1038, 108, 30, 6), XconDir()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xconDirection.setStatus('current')
xconName = MibScalar((1, 3, 6, 1, 4, 1, 1038, 108, 30, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xconName.setStatus('current')
xconAction = MibScalar((1, 3, 6, 1, 4, 1, 1038, 108, 30, 8), ActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xconAction.setStatus('current')
xconProceed = MibScalar((1, 3, 6, 1, 4, 1, 1038, 108, 30, 20), SagemBoolean()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xconProceed.setStatus('current')
xconDiagnostic = MibScalar((1, 3, 6, 1, 4, 1, 1038, 108, 30, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xconDiagnostic.setStatus('current')
mibBuilder.exportSymbols("XCONNECTION-MIB", LinkDirection=LinkDirection, ProtectionStatus=ProtectionStatus, linkProtectionType=linkProtectionType, linkTrafficStatus=linkTrafficStatus, xconSinkType=xconSinkType, linkIndex=linkIndex, linkNumber=linkNumber, linkDirection=linkDirection, CTPType=CTPType, linkProtectionStatus=linkProtectionStatus, linkGroupId=linkGroupId, link=link, linkSrcType=linkSrcType, xconSinkIndex=xconSinkIndex, linkTable=linkTable, linkSinkType=linkSinkType, TrafficStatus=TrafficStatus, XconDir=XconDir, xconNumber=xconNumber, linkName=linkName, xconSrcIndex=xconSrcIndex, linkImplementation=linkImplementation, ActionType=ActionType, ProtectionType=ProtectionType, xconDiagnostic=xconDiagnostic, xconAction=xconAction, xconSrcType=xconSrcType, xconnection=xconnection, linkEntry=linkEntry, xconName=xconName, xconDirection=xconDirection, xcon=xcon, linkCTPSink=linkCTPSink, xconProceed=xconProceed, linkCTPSource=linkCTPSource, PYSNMP_MODULE_ID=xconnection)
