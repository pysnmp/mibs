#
# PySNMP MIB module PRVT-MPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-MPLS-LDP-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 20:48:04 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
prvtcrldpSigIndex, prvtcrldpPmIndex = mibBuilder.importSymbols("PRVT-CR-LDP-MIB", "prvtcrldpSigIndex", "prvtcrldpPmIndex")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, TimeTicks, Integer32, NotificationType, Unsigned32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, MibIdentifier, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "TimeTicks", "Integer32", "NotificationType", "Unsigned32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "MibIdentifier", "IpAddress", "Bits")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
prvtMplsLdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1))
prvtMplsLdpMIB.setRevisions(('2009-11-26 00:00', '2006-06-03 00:00',))
if mibBuilder.loadTexts: prvtMplsLdpMIB.setLastUpdated('200911260000Z')
if mibBuilder.loadTexts: prvtMplsLdpMIB.setOrganization('BATM Advanced Communication')
class MplsRetentionMode(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture, RFC3031. LDP Specification, RFC3036, Section 2.6.2.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("conservative", 1), ("liberal", 2))

class MplsLdpLabelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("generic", 1), ("atm", 2), ("frameRelay", 3))

class MplsLabelDistributionMethod(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture, RFC3031. LDP Specification, RFC3036, Section 2.6.3.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("downstreamOnDemand", 1), ("downstreamUnsolicited", 2))

class PrvtMplsLdpIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 20)

class MplsIndexType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PrvtMplsLdpInetAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class PrvtMplsLdpTimeStamp(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class PrvtMplsLdpTimeInterval(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

mplsLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1))
mplsLdpEntityTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1), )
if mibBuilder.loadTexts: mplsLdpEntityTable.setStatus('current')
mplsLdpEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"))
if mibBuilder.loadTexts: mplsLdpEntityEntry.setStatus('current')
mplsLdpEntityLdpId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 1), PrvtMplsLdpIdentifier())
if mibBuilder.loadTexts: mplsLdpEntityLdpId.setStatus('current')
mplsLdpEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: mplsLdpEntityIndex.setStatus('current')
mplsLdpEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityRowStatus.setStatus('current')
mplsLdpEntityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityAdminStatus.setStatus('current')
mplsLdpEntityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpEntityOperStatus.setStatus('current')
mplsLdpEntityMaxPduLength = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 6), Unsigned32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpEntityMaxPduLength.setStatus('current')
mplsLdpEntityKeepAliveHoldTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 7), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityKeepAliveHoldTimer.setStatus('current')
mplsLdpEntityHelloHoldTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityHelloHoldTimer.setStatus('current')
mplsLdpEntityTargetPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityTargetPeer.setStatus('current')
mplsLdpEntityTargetPeerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 10), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityTargetPeerAddrType.setStatus('current')
mplsLdpEntityTargetPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 11), PrvtMplsLdpInetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityTargetPeerAddr.setStatus('current')
mplsLdpPeerTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2), )
if mibBuilder.loadTexts: mplsLdpPeerTable.setStatus('current')
mplsLdpPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"))
if mibBuilder.loadTexts: mplsLdpPeerEntry.setStatus('current')
mplsLdpPeerLdpId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2, 1, 1), PrvtMplsLdpIdentifier())
if mibBuilder.loadTexts: mplsLdpPeerLdpId.setStatus('current')
mplsLdpPeerLabelDistMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2, 1, 2), MplsLabelDistributionMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpPeerLabelDistMethod.setStatus('current')
mplsLdpPeerTransportAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpPeerTransportAddrType.setStatus('current')
mplsLdpPeerTransportAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2, 1, 4), PrvtMplsLdpInetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpPeerTransportAddr.setStatus('current')
mplsLdpSessionTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3), )
if mibBuilder.loadTexts: mplsLdpSessionTable.setStatus('current')
mplsLdpSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"))
if mibBuilder.loadTexts: mplsLdpSessionEntry.setStatus('current')
mplsLdpSessionStateLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 1), PrvtMplsLdpTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionStateLastChange.setStatus('current')
mplsLdpSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("nonexistent", 1), ("initialized", 2), ("openrec", 3), ("opensent", 4), ("operational", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionState.setStatus('current')
mplsLdpSessionKeepAliveHoldTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 3), PrvtMplsLdpTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionKeepAliveHoldTimeRemaining.setStatus('current')
mplsLdpSessionKeepAliveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 4), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionKeepAliveTime.setStatus('current')
mplsLdpSessionMaxPduLength = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 5), Unsigned32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionMaxPduLength.setStatus('current')
mplsLdpSessionConfiguredHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionConfiguredHoldTime.setStatus('current')
mplsLdpSessionPeerHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionPeerHoldTime.setStatus('current')
mplsLdpSessionHoldTimeInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionHoldTimeInUse.setStatus('current')
mplsLdpHelloAdjacencyTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4), )
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyTable.setStatus('current')
mplsLdpHelloAdjacencyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpHelloAdjacencyIndex"))
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyEntry.setStatus('current')
mplsLdpHelloAdjacencyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyIndex.setStatus('current')
mplsLdpHelloAdjacencyHoldTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 2), PrvtMplsLdpTimeInterval()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyHoldTimeRemaining.setStatus('current')
mplsLdpHelloAdjacencyHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyHoldTime.setStatus('current')
mplsLdpHelloAdjacencyType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link", 1), ("targeted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyType.setStatus('current')
mplsLdpHelloAdjacencyConfiguredHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyConfiguredHoldTime.setStatus('current')
mplsLdpHelloAdjacencyPeerHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyPeerHoldTime.setStatus('current')
mplsLdpSessionPeerAddrTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 5), )
if mibBuilder.loadTexts: mplsLdpSessionPeerAddrTable.setStatus('current')
mplsLdpSessionPeerAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 5, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpSessionPeerAddrIndex"))
if mibBuilder.loadTexts: mplsLdpSessionPeerAddrEntry.setStatus('current')
mplsLdpSessionPeerAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: mplsLdpSessionPeerAddrIndex.setStatus('current')
mplsLdpSessionPeerNextHopAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 5, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionPeerNextHopAddrType.setStatus('current')
mplsLdpSessionPeerNextHopAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 5, 1, 3), PrvtMplsLdpInetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionPeerNextHopAddr.setStatus('current')
mibBuilder.exportSymbols("PRVT-MPLS-LDP-MIB", mplsLdpHelloAdjacencyIndex=mplsLdpHelloAdjacencyIndex, mplsLdpSessionState=mplsLdpSessionState, mplsLdpObjects=mplsLdpObjects, mplsLdpEntityTargetPeer=mplsLdpEntityTargetPeer, mplsLdpEntityTargetPeerAddrType=mplsLdpEntityTargetPeerAddrType, mplsLdpHelloAdjacencyHoldTimeRemaining=mplsLdpHelloAdjacencyHoldTimeRemaining, mplsLdpPeerLdpId=mplsLdpPeerLdpId, PrvtMplsLdpTimeStamp=PrvtMplsLdpTimeStamp, mplsLdpSessionPeerHoldTime=mplsLdpSessionPeerHoldTime, mplsLdpEntityIndex=mplsLdpEntityIndex, PrvtMplsLdpTimeInterval=PrvtMplsLdpTimeInterval, mplsLdpEntityLdpId=mplsLdpEntityLdpId, mplsLdpSessionKeepAliveHoldTimeRemaining=mplsLdpSessionKeepAliveHoldTimeRemaining, mplsLdpEntityEntry=mplsLdpEntityEntry, mplsLdpEntityOperStatus=mplsLdpEntityOperStatus, mplsLdpHelloAdjacencyTable=mplsLdpHelloAdjacencyTable, MplsLabelDistributionMethod=MplsLabelDistributionMethod, mplsLdpEntityTargetPeerAddr=mplsLdpEntityTargetPeerAddr, prvtMplsLdpMIB=prvtMplsLdpMIB, mplsLdpEntityAdminStatus=mplsLdpEntityAdminStatus, mplsLdpHelloAdjacencyConfiguredHoldTime=mplsLdpHelloAdjacencyConfiguredHoldTime, mplsLdpPeerEntry=mplsLdpPeerEntry, mplsLdpSessionTable=mplsLdpSessionTable, mplsLdpSessionHoldTimeInUse=mplsLdpSessionHoldTimeInUse, mplsLdpEntityKeepAliveHoldTimer=mplsLdpEntityKeepAliveHoldTimer, mplsLdpSessionConfiguredHoldTime=mplsLdpSessionConfiguredHoldTime, mplsLdpSessionPeerNextHopAddr=mplsLdpSessionPeerNextHopAddr, MplsLdpLabelType=MplsLdpLabelType, mplsLdpPeerTable=mplsLdpPeerTable, mplsLdpHelloAdjacencyType=mplsLdpHelloAdjacencyType, mplsLdpHelloAdjacencyHoldTime=mplsLdpHelloAdjacencyHoldTime, mplsLdpSessionPeerAddrIndex=mplsLdpSessionPeerAddrIndex, mplsLdpEntityTable=mplsLdpEntityTable, mplsLdpSessionPeerAddrTable=mplsLdpSessionPeerAddrTable, mplsLdpEntityRowStatus=mplsLdpEntityRowStatus, mplsLdpSessionStateLastChange=mplsLdpSessionStateLastChange, mplsLdpPeerTransportAddrType=mplsLdpPeerTransportAddrType, mplsLdpPeerLabelDistMethod=mplsLdpPeerLabelDistMethod, PrvtMplsLdpIdentifier=PrvtMplsLdpIdentifier, mplsLdpSessionKeepAliveTime=mplsLdpSessionKeepAliveTime, MplsRetentionMode=MplsRetentionMode, mplsLdpSessionMaxPduLength=mplsLdpSessionMaxPduLength, mplsLdpHelloAdjacencyPeerHoldTime=mplsLdpHelloAdjacencyPeerHoldTime, PYSNMP_MODULE_ID=prvtMplsLdpMIB, PrvtMplsLdpInetAddress=PrvtMplsLdpInetAddress, mplsLdpPeerTransportAddr=mplsLdpPeerTransportAddr, mplsLdpEntityHelloHoldTimer=mplsLdpEntityHelloHoldTimer, mplsLdpHelloAdjacencyEntry=mplsLdpHelloAdjacencyEntry, MplsIndexType=MplsIndexType, mplsLdpSessionPeerAddrEntry=mplsLdpSessionPeerAddrEntry, mplsLdpSessionPeerNextHopAddrType=mplsLdpSessionPeerNextHopAddrType, mplsLdpEntityMaxPduLength=mplsLdpEntityMaxPduLength, mplsLdpSessionEntry=mplsLdpSessionEntry)
