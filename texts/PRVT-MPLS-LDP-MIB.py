#
# PySNMP MIB module PRVT-MPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-MPLS-LDP-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 21:19:51 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
prvtcrldpPmIndex, prvtcrldpSigIndex = mibBuilder.importSymbols("PRVT-CR-LDP-MIB", "prvtcrldpPmIndex", "prvtcrldpSigIndex")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, iso, Unsigned32, TimeTicks, Integer32, NotificationType, Bits, MibIdentifier, Gauge32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "iso", "Unsigned32", "TimeTicks", "Integer32", "NotificationType", "Bits", "MibIdentifier", "Gauge32", "ModuleIdentity", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
prvtMplsLdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1))
prvtMplsLdpMIB.setRevisions(('2009-11-26 00:00', '2006-06-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtMplsLdpMIB.setRevisionsDescriptions(('Created MplsLdpIdentifier TC.', 'Initial version published as part of RFC 3815.',))
if mibBuilder.loadTexts: prvtMplsLdpMIB.setLastUpdated('200911260000Z')
if mibBuilder.loadTexts: prvtMplsLdpMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtMplsLdpMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtMplsLdpMIB.setDescription("This MIB contains managed object definitions for the\n         'Multiprotocol Label Switching, Label Distribution\n         Protocol, LDP'.")
class MplsRetentionMode(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture,\n         RFC3031.\n         \n         LDP Specification, RFC3036, Section 2.6.2.'
    description = 'The label retention mode which specifies whether\n         an LSR maintains a label binding for a FEC\n         learned from a neighbor that is not its next hop\n         for the FEC.\n         \n         If the value is conservative(1) then advertised\n         label mappings are retained only if they will be\n         used to forward packets, i.e., if label came from\n         a valid next hop.\n         \n         If the value is liberal(2) then all advertised\n         label mappings are retained whether they are from\n         a valid next hop or not.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("conservative", 1), ("liberal", 2))

class MplsLdpLabelType(TextualConvention, Integer32):
    description = 'The Layer 2 label types which are defined for MPLS\n         LDP and/or CR-LDP are generic(1), atm(2), or\n         frameRelay(3).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("generic", 1), ("atm", 2), ("frameRelay", 3))

class MplsLabelDistributionMethod(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture,\n         RFC3031.\n         \n         LDP Specification, RFC3036, Section 2.6.3.'
    description = 'The label distribution method which is also called\n         the label advertisement mode [RFC3036].\n         Each interface on an LSR is configured to operate\n         in either Downstream Unsolicited or Downstream\n         on Demand.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("downstreamOnDemand", 1), ("downstreamUnsolicited", 2))

class PrvtMplsLdpIdentifier(TextualConvention, OctetString):
    description = 'The LDP identifier is used to identify a\n         Label Switching Router (LSR) label space.\n         \n         The format is an ASCII representation of\n         a string in the form A.B.C.D:S,\n         where A,B,C,D identify the LSR and must\n         be a globally unique value, such as a 32-bit\n         router ID assigned to the LSR,\n         and S identifies a specific label space\n         within the LSR.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 20)

class MplsIndexType(TextualConvention, Integer32):
    description = 'This is an octet string that can be used as a table\n         index in cases where a large addressable space is\n         required such as on an LSR where many applications\n         may be provisioning labels.\n         \n         Note that the string containing the single octet with\n         the value 0x00 is a reserved value used to represent\n         special cases. When this TEXTUAL-CONVENTION is used\n         as the SYNTAX of an object, the DESCRIPTION clause\n         MUST specify if this special value is valid and if so\n         what the special meaning is.\n         \n         In systems that provide write access to the MPLS-LSR-STD\n         MIB, mplsIndexType SHOULD be used as a simple multi-digit\n         integer encoded as an octet string.\n         No further overloading of the meaning of an index SHOULD\n         be made.\n         \n         In systems that do not offer write access to the MPLS-LSR-STD\n         MIB, the mplsIndexType may contain implicit formatting that is\n         specific to the implementation to convey additional\n         information such as interface index, physical card or\n         device, or application id. The interpretation of this\n         additional formatting is implementation dependent and\n         not covered in this document. Such formatting MUST\n         NOT impact the basic functionality of read-only access\n         to the MPLS-LSR-STD MIB by management applications that are\n         not aware of the formatting rules.\n         \n         The MIB is implemented in PRVT-LMGR with write-access.\n         As specified above, PRVT-LMGR treats the index values of this type\n         as simple integer types.\n         \n         In order to reduce the effort required to upgrade from earlier\n         versions of the MIB, and to simplify management of static LSPs,\n         this type is mapped on to an Integer32 in this implementation.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PrvtMplsLdpInetAddress(TextualConvention, OctetString):
    description = 'Same as InetAddress from INET-ADDRESS-MIB except restricted\n         to IPv4 or IPv6 addresses.'
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class PrvtMplsLdpTimeStamp(TextualConvention, Integer32):
    description = 'Same as TimeStamp from SNMPv2-TC, but has syntax Integer32'
    status = 'current'
    displayHint = 'd'

class PrvtMplsLdpTimeInterval(TextualConvention, Integer32):
    description = 'Same as TimeInterval from SNMPv2-TC, but has syntax Integer32'
    status = 'current'
    displayHint = 'd'

mplsLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1))
mplsLdpEntityTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1), )
if mibBuilder.loadTexts: mplsLdpEntityTable.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityTable.setDescription('This table contains information about the\n         MPLS Label Distribution Protocol Entities which\n         exist on this Label Switching Router (LSR)\n         or Label Edge Router (LER).')
mplsLdpEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"))
if mibBuilder.loadTexts: mplsLdpEntityEntry.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityEntry.setDescription('An entry in this table represents an LDP entity.\n         An entry can be created by a network administrator\n         or by an SNMP agent as instructed by LDP.')
mplsLdpEntityLdpId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 1), PrvtMplsLdpIdentifier())
if mibBuilder.loadTexts: mplsLdpEntityLdpId.setReference('RFC3036, LDP Specification, Section on LDP Identifiers.')
if mibBuilder.loadTexts: mplsLdpEntityLdpId.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityLdpId.setDescription('The LDP identifier. The first four octets encode an IP\n         address assigned to the LSR, and the last two octets\n         identify a specific label space within the LSR.')
mplsLdpEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: mplsLdpEntityIndex.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityIndex.setDescription('This index is used as a secondary index to uniquely\n         identify this row.\n         \n         A secondary index (this object) is meaningful to some\n         but not all, LDP implementations. For example\n         an LDP implementation which uses PPP would\n         use this index to differentiate PPP sub-links.\n         \n         Another way to use this index is to give this the\n         value of ifIndex. However, this is dependant\n         on the implementation.\n         \n         This field is deprecated in the following tables provided\n         by PRVT-CR-LDP Session Controller.\n         \n         - mplsLdpEntityTable.\n         - mplsLdpPeerTable.\n         \n         In these tables the value of the Entity Index will always\n         be filled in to be 1.')
mplsLdpEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityRowStatus.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityRowStatus.setDescription("An object that allows entries in this table to\n         be created and deleted using the\n         RowStatus convention.\n         \n         Once the 'mplsLdpEntityAdminStatus' object has\n         the value of 'up' and this object has the value\n         of 'active' then the Entity will atttempt to\n         contact an LDP Peer. If the value of this object\n         is changed to 'notInService', then the Entity looses\n         contact with the LDP Peer and all information related\n         to that Peer must be removed from the MIB. This has\n         the same effect as changing 'mplsLdpEntityAdminStatus'\n         from 'enable' to 'disable'.\n         \n         When this object is set to 'active' and the value of\n         the 'mplsLdpEntityAdminStatus' is 'enable' then\n         this Entity will attempt to contact the Peer and\n         establish new sessions.")
mplsLdpEntityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityAdminStatus.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityAdminStatus.setDescription("The administrative status of this LDP Entity.\n         If this object is changed from 'enable' to 'disable'\n         and this entity has already attempted to establish\n         contact with a Peer (which implies that the\n         'mplsLdpEntityRowStatus' object has been set to\n         'active'), then all contact with that\n         Peer is lost and all information from that Peer\n         needs to be removed from the MIB. (This implies\n         that the network management subsystem should clean\n         up any related entry in the mplsLdpPeerTable. This\n         further implies that a 'tear-down' for that session\n         is issued and the session and all information related\n         to that session cease to exist).\n         \n         At this point the user is able to change values\n         which are related to this entity.\n         \n         When the admin status is set back to 'enable', then\n         this Entity will attempt to establish a new session\n         with the Peer.")
mplsLdpEntityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpEntityOperStatus.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityOperStatus.setDescription('The operational status of this LDP Entity.\n         \n         The value of unknown(1) indicates that the\n         operational status cannot be determined at\n         this time. The value of unknown should be\n         a transient condition before changing\n         to enabled(2) or disabled(3).')
mplsLdpEntityMaxPduLength = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 6), Unsigned32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpEntityMaxPduLength.setReference('RFC3036, LDP Specification, Section 3.5.3.\n         Initialization Message.')
if mibBuilder.loadTexts: mplsLdpEntityMaxPduLength.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityMaxPduLength.setDescription("The maximum PDU Length that is sent in\n         the Common Session Parameters of an Initialization\n         Message. According to the LDP Specification [RFC3036]\n         a value of 255 or less specifies the\n         default maximum length of 4096 octets.\n         \n         The receiving LSR MUST calculate the maximum PDU\n         length for the session by using the smaller of its and\n         its peer's proposals for Max PDU Length.")
mplsLdpEntityKeepAliveHoldTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 7), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityKeepAliveHoldTimer.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityKeepAliveHoldTimer.setDescription('The 16-bit integer value which is the proposed keep\n         alive hold timer for this LDP Entity.')
mplsLdpEntityHelloHoldTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityHelloHoldTimer.setReference('RFC3036, LDP Specification, Section 3.5.2.,\n         Hello Message.')
if mibBuilder.loadTexts: mplsLdpEntityHelloHoldTimer.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityHelloHoldTimer.setDescription("The 16-bit integer value which is the proposed Hello\n         hold timer for this LDP Entity. The Hello Hold time\n         in seconds.\n         \n         An LSR maintains a record of Hellos received\n         from potential peers. This object represents\n         the Hold Time in the Common Hello Parameters TLV of\n         the Hello Message.\n         \n         A value of 0 is a default value and should be\n         interpretted in conjunction with the\n         mplsLdpEntityTargetPeer object.\n         \n         If the value of this object is 0: if the value of the\n         mplsLdpEntityTargetPeer object is false(2), then this\n         specifies that the Hold Time's actual default value is\n         15 seconds (i.e., the default Hold time for Link Hellos\n         is 15 seconds). Otherwise if the value of the\n         mplsLdpEntityTargetPeer object is true(1), then this\n         specifies that the Hold Time's actual default value is\n         45 seconds (i.e., the default Hold time for Targeted\n         Hellos is 45 seconds).\n         \n         A value of 65535 means infinite (i.e., wait forever).\n         \n         All other values represent the amount of time in\n         seconds to wait for a Hello Message. Setting the\n         hold time to a value smaller than 15 is not\n         recommended, although not forbidden according\n         to RFC3036.\n         \n         For auto-created entities that use the global label space\n         (and therefore might correspond to more than one\n         adjacency over more than one interface), this value will\n         only be meaningful if all interfaces that correspond to\n         this entity are configured to use the same hello hold\n         time, since this property can be configured on a per\n         interface basis.\n         \n         If the interfaces have differing configurations, the\n         value returned on a MIB Get will be 0.")
mplsLdpEntityTargetPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityTargetPeer.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityTargetPeer.setDescription('If this LDP entity uses targeted peer then set\n         this to true.')
mplsLdpEntityTargetPeerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 10), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityTargetPeerAddrType.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityTargetPeerAddrType.setDescription('The type of the internetwork layer address used for\n         the Extended Discovery. This object indicates how\n         the value of mplsLdpEntityTargetPeerAddr is to\n         be interpreted.')
mplsLdpEntityTargetPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 1, 1, 11), PrvtMplsLdpInetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityTargetPeerAddr.setStatus('current')
if mibBuilder.loadTexts: mplsLdpEntityTargetPeerAddr.setDescription('The value of the internetwork layer address\n         used for the Extended Discovery. The value of\n         mplsLdpEntityTargetPeerAddrType specifies how\n         this address is to be interpreted.')
mplsLdpPeerTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2), )
if mibBuilder.loadTexts: mplsLdpPeerTable.setStatus('current')
if mibBuilder.loadTexts: mplsLdpPeerTable.setDescription('Information about LDP peers known by Entities in\n         the mplsLdpEntityTable. The information in this table\n         is based on information from the Entity-Peer interaction\n         during session initialization but is not appropriate\n         for the mplsLdpSessionTable, because objects in this\n         table may or may not be used in session establishment.')
mplsLdpPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"))
if mibBuilder.loadTexts: mplsLdpPeerEntry.setStatus('current')
if mibBuilder.loadTexts: mplsLdpPeerEntry.setDescription('Information about a single Peer which is related\n         to a Session. NOTE: this table is used to\n         augment the mplsLdpSessionTable.')
mplsLdpPeerLdpId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2, 1, 1), PrvtMplsLdpIdentifier())
if mibBuilder.loadTexts: mplsLdpPeerLdpId.setStatus('current')
if mibBuilder.loadTexts: mplsLdpPeerLdpId.setDescription('The LDP identifier of this LDP Peer.')
mplsLdpPeerLabelDistMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2, 1, 2), MplsLabelDistributionMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpPeerLabelDistMethod.setStatus('current')
if mibBuilder.loadTexts: mplsLdpPeerLabelDistMethod.setDescription('For any given LDP session, the method of\n         label distribution must be specified.')
mplsLdpPeerTransportAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpPeerTransportAddrType.setReference('RFC3036, LDP Specification, Section 2.5.2\n         Transport Connection Establishment and\n         Section 3.5.2.1 Hello Message Procedures.')
if mibBuilder.loadTexts: mplsLdpPeerTransportAddrType.setStatus('current')
if mibBuilder.loadTexts: mplsLdpPeerTransportAddrType.setDescription("The type of the Internet address for the\n         mplsLdpPeerTransportAddr object. The LDP\n         specification describes this as being either\n         an IPv4 Transport Address or IPv6 Transport\n         Address which is used in opening the LDP session's\n         TCP connection, or if the optional TLV is not\n         present, then this is the IPv4/IPv6 source\n         address for the UPD packet carrying the Hellos.\n         \n         This object specifies how the value of the\n         mplsLdpPeerTransportAddr object should be\n         interpreted.")
mplsLdpPeerTransportAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 2, 1, 4), PrvtMplsLdpInetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpPeerTransportAddr.setReference('RFC3036, LDP Specification, Section 2.5.2\n         Transport Connection Establishment and\n         Section 3.5.2.1 Hello Message Procedures.')
if mibBuilder.loadTexts: mplsLdpPeerTransportAddr.setStatus('current')
if mibBuilder.loadTexts: mplsLdpPeerTransportAddr.setDescription('The Internet address advertised by the peer\n         in the Hello Message or the Hello source address.\n         \n         The type of this address is specified by the\n         value of the mplsLdpPeerTransportAddrType\n         object.')
mplsLdpSessionTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3), )
if mibBuilder.loadTexts: mplsLdpSessionTable.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionTable.setDescription('A table of Sessions between the LDP Entities\n         and LDP Peers. Each row in this table\n         represents a single session.')
mplsLdpSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"))
if mibBuilder.loadTexts: mplsLdpSessionEntry.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionEntry.setDescription("An entry in this table represents information on a\n         single session between an LDP Entity and LDP Peer.\n         The information contained in a row is read-only.\n         \n         Please note: the Path Vector Limit for the\n         Session is the value which is configured in\n         the corresponding mplsLdpEntityEntry. The\n         Peer's Path Vector Limit is in the\n         mplsLdpPeerPathVectorLimit object in the\n         mplsLdpPeerTable.\n         \n         Values which may differ from those configured are\n         noted in the objects of this table. A value will\n         differ if it was negotiated between the\n         Entity and the Peer. Values may or may not\n         be negotiated. For example, if the values\n         are the same then no negotiation takes place.\n         If they are negotiated, then they may differ.")
mplsLdpSessionStateLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 1), PrvtMplsLdpTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionStateLastChange.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionStateLastChange.setDescription('The value of sysUpTime at the time this\n         Session entered its current state as\n         denoted by the mplsLdpSessionState\n         object.')
mplsLdpSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("nonexistent", 1), ("initialized", 2), ("openrec", 3), ("opensent", 4), ("operational", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionState.setReference('RFC3036, LDP Specification, Section 2.5.4,\n         Initialization State Machine.')
if mibBuilder.loadTexts: mplsLdpSessionState.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionState.setDescription('The current state of the session, all of the\n         states 1 - 5 are based on the state machine\n         for session negotiation behavior.')
mplsLdpSessionKeepAliveHoldTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 3), PrvtMplsLdpTimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionKeepAliveHoldTimeRemaining.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionKeepAliveHoldTimeRemaining.setDescription("The keep alive hold time remaining for this session in\n         units of hundredths of a second. This interval will\n         change when the 'next' Keep Alive message which\n         corresponds to this session is received. A value of zero\n         indicates that the keep alive hold timer is not running.")
mplsLdpSessionKeepAliveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 4), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionKeepAliveTime.setReference('RFC3036, LDP Specification, Section 3.5.3,\n         Initialization Message.')
if mibBuilder.loadTexts: mplsLdpSessionKeepAliveTime.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionKeepAliveTime.setDescription("The negotiated KeepAlive Time which\n         represents the amount of seconds between\n         keep alive messages. The\n         mplsLdpEntityKeepAliveHoldTimer\n         related to this Session is the\n         value that was proposed as the\n         KeepAlive Time for this session.\n         \n         This value is negotiated during\n         session initialization between\n         the entity's proposed value\n         (i.e., the value configured in\n         mplsLdpEntityKeepAliveHoldTimer)\n         and the peer's proposed\n         KeepAlive Hold Timer value.\n         This value is the smaller\n         of the two proposed values.")
mplsLdpSessionMaxPduLength = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 5), Unsigned32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionMaxPduLength.setReference('RFC3036, LDP Specification, Section 3.5.3,\n         Initialization Message.')
if mibBuilder.loadTexts: mplsLdpSessionMaxPduLength.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionMaxPduLength.setDescription('The value of maximum allowable length for LDP PDUs for\n         this session. This value may have been negotiated\n         during the Session Initialization. This object is\n         related to the mplsLdpEntityMaxPduLength object. The\n         mplsLdpEntityMaxPduLength object specifies the requested\n         LDP PDU length, and this object reflects the negotiated\n         LDP PDU length between the Entity and\n         the Peer.')
mplsLdpSessionConfiguredHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionConfiguredHoldTime.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionConfiguredHoldTime.setDescription('The locally configured keepalive hold time for this\n         session, in seconds. Note that the value of this field\n         reflects configuration at the time of session\n         initialization; this may differ from the configuration\n         that would apply to a new session, if configuration has\n         changed since this session was initialized.')
mplsLdpSessionPeerHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionPeerHoldTime.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionPeerHoldTime.setDescription("The peer's advertised keepalive hold time for this session\n         in seconds. Note that the value of this field reflects\n         the peer's configuration at the time of session\n         initialization; this may differ from the configuration\n         that would apply to a new session, if the peer's\n         configuration has changed since this session was\n         initialized.")
mplsLdpSessionHoldTimeInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionHoldTimeInUse.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionHoldTimeInUse.setDescription('The keepalive hold time that is currently in use for this\n         session, in seconds.')
mplsLdpHelloAdjacencyTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4), )
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyTable.setStatus('current')
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyTable.setDescription('A table of Hello Adjacencies for Sessions.')
mplsLdpHelloAdjacencyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpHelloAdjacencyIndex"))
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyEntry.setStatus('current')
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyEntry.setDescription('Each row represents a single LDP Hello Adjacency.\n         An LDP Session can have one or more Hello adjacencies.')
mplsLdpHelloAdjacencyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyIndex.setStatus('current')
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyIndex.setDescription('An identifier for this specific adjacency.')
mplsLdpHelloAdjacencyHoldTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 2), PrvtMplsLdpTimeInterval()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyHoldTimeRemaining.setStatus('current')
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyHoldTimeRemaining.setDescription("If the value of this object is 65535,\n         this means that the hold time is infinite\n         (i.e., wait forever).\n         \n         Otherwise, the time remaining for\n         this Hello Adjacency to receive its\n         next Hello Message.\n         \n         This interval will change when the 'next'\n         Hello Message which corresponds to this\n         Hello Adjacency is received unless it\n         is infinite.")
mplsLdpHelloAdjacencyHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyHoldTime.setReference('RFC3036, LDP Specification, Section 3.5.2 Hello Message')
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyHoldTime.setStatus('current')
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyHoldTime.setDescription('The Hello hold time which is negotiated between\n         the Entity and the Peer. The entity associated\n         with this Hello Adjacency issues a proposed\n         Hello Hold Time value in the\n         mplsLdpEntityHelloHoldTimer object. The peer\n         also proposes a value and this object represents\n         the negotiated value.\n         \n         A value of 0 means the default,\n         which is 15 seconds for Link Hellos\n         and 45 seconds for Targeted Hellos.\n         A value of 65535 indicates an\n         infinite hold time.')
mplsLdpHelloAdjacencyType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link", 1), ("targeted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyType.setStatus('current')
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyType.setDescription("This adjacency is the result of a 'link'\n         hello if the value of this object is link(1).\n         Otherwise, it is a result of a 'targeted'\n         hello, targeted(2).")
mplsLdpHelloAdjacencyConfiguredHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyConfiguredHoldTime.setStatus('current')
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyConfiguredHoldTime.setDescription('The locally configured hello hold time for this adjacency,\n         in seconds.')
mplsLdpHelloAdjacencyPeerHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyPeerHoldTime.setStatus('current')
if mibBuilder.loadTexts: mplsLdpHelloAdjacencyPeerHoldTime.setDescription("The peer's advertised hello hold time for this adjacency,\n         in seconds.")
mplsLdpSessionPeerAddrTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 5), )
if mibBuilder.loadTexts: mplsLdpSessionPeerAddrTable.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionPeerAddrTable.setDescription("This table 'extends' the mplsLdpSessionTable.\n         This table is used to store Label Address Information\n         from Label Address Messages received by this LSR from\n         Peers. This table is read-only and should be updated\n         when Label Withdraw Address Messages are received, i.e.,\n         Rows should be deleted as appropriate.\n         \n         NOTE: since more than one address may be contained\n         in a Label Address Message, this table 'sparse augments',\n         the mplsLdpSessionTable's information.")
mplsLdpSessionPeerAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 5, 1), ).setIndexNames((0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpEntityIndex"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpPeerLdpId"), (0, "PRVT-MPLS-LDP-MIB", "mplsLdpSessionPeerAddrIndex"))
if mibBuilder.loadTexts: mplsLdpSessionPeerAddrEntry.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionPeerAddrEntry.setDescription("An entry in this table represents information on\n         a session's single next hop address which was\n         advertised in an Address Message from the LDP peer.\n         The information contained in a row is read-only.")
mplsLdpSessionPeerAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: mplsLdpSessionPeerAddrIndex.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionPeerAddrIndex.setDescription('An index which uniquely identifies this entry within\n         a given session.')
mplsLdpSessionPeerNextHopAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 5, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionPeerNextHopAddrType.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionPeerNextHopAddrType.setDescription('The internetwork layer address type of this Next Hop\n         Address as specified in the Label Address Message\n         associated with this Session. The value of this\n         object indicates how to interpret the value of\n         mplsLdpSessionPeerNextHopAddr.')
mplsLdpSessionPeerNextHopAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 1, 1, 5, 1, 3), PrvtMplsLdpInetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsLdpSessionPeerNextHopAddr.setReference('RFC3036, Section 2.7. LDP Identifiers\n         and Next Hop Addresses')
if mibBuilder.loadTexts: mplsLdpSessionPeerNextHopAddr.setStatus('current')
if mibBuilder.loadTexts: mplsLdpSessionPeerNextHopAddr.setDescription('The next hop address. The type of this address\n         is specified by the value of the\n         mplsLdpSessionPeerNextHopAddrType.')
mibBuilder.exportSymbols("PRVT-MPLS-LDP-MIB", mplsLdpPeerLabelDistMethod=mplsLdpPeerLabelDistMethod, mplsLdpEntityHelloHoldTimer=mplsLdpEntityHelloHoldTimer, mplsLdpPeerLdpId=mplsLdpPeerLdpId, mplsLdpEntityAdminStatus=mplsLdpEntityAdminStatus, MplsLdpLabelType=MplsLdpLabelType, mplsLdpPeerTransportAddr=mplsLdpPeerTransportAddr, mplsLdpSessionConfiguredHoldTime=mplsLdpSessionConfiguredHoldTime, PYSNMP_MODULE_ID=prvtMplsLdpMIB, mplsLdpHelloAdjacencyIndex=mplsLdpHelloAdjacencyIndex, mplsLdpPeerTable=mplsLdpPeerTable, mplsLdpEntityTargetPeerAddr=mplsLdpEntityTargetPeerAddr, mplsLdpSessionKeepAliveHoldTimeRemaining=mplsLdpSessionKeepAliveHoldTimeRemaining, mplsLdpHelloAdjacencyTable=mplsLdpHelloAdjacencyTable, mplsLdpSessionEntry=mplsLdpSessionEntry, PrvtMplsLdpInetAddress=PrvtMplsLdpInetAddress, prvtMplsLdpMIB=prvtMplsLdpMIB, mplsLdpEntityOperStatus=mplsLdpEntityOperStatus, mplsLdpSessionTable=mplsLdpSessionTable, mplsLdpEntityTargetPeer=mplsLdpEntityTargetPeer, mplsLdpEntityKeepAliveHoldTimer=mplsLdpEntityKeepAliveHoldTimer, mplsLdpSessionPeerAddrEntry=mplsLdpSessionPeerAddrEntry, mplsLdpSessionPeerNextHopAddr=mplsLdpSessionPeerNextHopAddr, mplsLdpSessionPeerAddrIndex=mplsLdpSessionPeerAddrIndex, mplsLdpEntityIndex=mplsLdpEntityIndex, mplsLdpSessionKeepAliveTime=mplsLdpSessionKeepAliveTime, mplsLdpSessionHoldTimeInUse=mplsLdpSessionHoldTimeInUse, mplsLdpEntityEntry=mplsLdpEntityEntry, mplsLdpEntityMaxPduLength=mplsLdpEntityMaxPduLength, mplsLdpSessionState=mplsLdpSessionState, PrvtMplsLdpTimeInterval=PrvtMplsLdpTimeInterval, mplsLdpHelloAdjacencyHoldTime=mplsLdpHelloAdjacencyHoldTime, MplsLabelDistributionMethod=MplsLabelDistributionMethod, MplsIndexType=MplsIndexType, mplsLdpSessionPeerNextHopAddrType=mplsLdpSessionPeerNextHopAddrType, mplsLdpHelloAdjacencyType=mplsLdpHelloAdjacencyType, mplsLdpPeerTransportAddrType=mplsLdpPeerTransportAddrType, PrvtMplsLdpIdentifier=PrvtMplsLdpIdentifier, mplsLdpHelloAdjacencyPeerHoldTime=mplsLdpHelloAdjacencyPeerHoldTime, mplsLdpObjects=mplsLdpObjects, mplsLdpEntityTable=mplsLdpEntityTable, mplsLdpSessionMaxPduLength=mplsLdpSessionMaxPduLength, PrvtMplsLdpTimeStamp=PrvtMplsLdpTimeStamp, mplsLdpEntityRowStatus=mplsLdpEntityRowStatus, mplsLdpSessionPeerHoldTime=mplsLdpSessionPeerHoldTime, mplsLdpHelloAdjacencyHoldTimeRemaining=mplsLdpHelloAdjacencyHoldTimeRemaining, mplsLdpSessionPeerAddrTable=mplsLdpSessionPeerAddrTable, mplsLdpPeerEntry=mplsLdpPeerEntry, mplsLdpEntityTargetPeerAddrType=mplsLdpEntityTargetPeerAddrType, mplsLdpHelloAdjacencyConfiguredHoldTime=mplsLdpHelloAdjacencyConfiguredHoldTime, MplsRetentionMode=MplsRetentionMode, mplsLdpSessionStateLastChange=mplsLdpSessionStateLastChange, mplsLdpHelloAdjacencyEntry=mplsLdpHelloAdjacencyEntry, mplsLdpEntityLdpId=mplsLdpEntityLdpId)
