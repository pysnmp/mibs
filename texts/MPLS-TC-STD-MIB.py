#
# PySNMP MIB module MPLS-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/MPLS-TC-STD-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 07:48:00 2023
# On host fv-az178-832 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, transmission, Gauge32, Unsigned32, IpAddress, TimeTicks, ModuleIdentity, Counter32, Bits, NotificationType, iso, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "transmission", "Gauge32", "Unsigned32", "IpAddress", "TimeTicks", "ModuleIdentity", "Counter32", "Bits", "NotificationType", "iso", "ObjectIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mplsTCStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 1))
mplsTCStdMIB.setRevisions(('2004-06-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsTCStdMIB.setRevisionsDescriptions(('Initial version published as part of RFC 3811.',))
if mibBuilder.loadTexts: mplsTCStdMIB.setLastUpdated('200406030000Z')
if mibBuilder.loadTexts: mplsTCStdMIB.setOrganization('IETF Multiprotocol Label Switching (MPLS) Working\n              Group.')
if mibBuilder.loadTexts: mplsTCStdMIB.setContactInfo('        Thomas D. Nadeau\n                        Cisco Systems, Inc.\n                        tnadeau@cisco.com\n\n                        Joan Cucchiara\n                        Marconi Communications, Inc.\n                        jcucchiara@mindspring.com\n\n                        Cheenu Srinivasan\n                        Bloomberg L.P.\n                        cheenu@bloomberg.net\n\n                        Arun Viswanathan\n                        Force10 Networks, Inc.\n                        arunv@force10networks.com\n\n                        Hans Sjostrand\n                        ipUnplugged\n                        hans@ipunplugged.com\n\n                        Kireeti Kompella\n                        Juniper Networks\n                        kireeti@juniper.net\n\n             Email comments to the MPLS WG Mailing List at\n             mpls@uu.net.')
if mibBuilder.loadTexts: mplsTCStdMIB.setDescription('Copyright (C) The Internet Society (2004). The\n              initial version of this MIB module was published\n              in RFC 3811. For full legal notices see the RFC\n              itself or see:\n              http://www.ietf.org/copyrights/ianamib.html\n\n              This MIB module defines TEXTUAL-CONVENTIONs\n              for concepts used in Multiprotocol Label\n              Switching (MPLS) networks.')
mplsStdMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166))
class MplsAtmVcIdentifier(TextualConvention, Integer32):
    reference = 'MPLS using LDP and ATM VC Switching, RFC3035.'
    description = 'A Label Switching Router (LSR) that\n              creates LDP sessions on ATM interfaces\n              uses the VCI or VPI/VCI field to hold the\n              LDP Label.\n\n              VCI values MUST NOT be in the 0-31 range.\n              The values 0 to 31 are reserved for other uses\n              by the ITU and ATM Forum.  The value\n              of 32 can only be used for the Control VC,\n              although values greater than 32 could be\n              configured for the Control VC.\n\n              If a value from 0 to 31 is used for a VCI\n              the management entity controlling the LDP\n              subsystem should reject this with an\n              inconsistentValue error.  Also, if\n              the value of 32 is used for a VC which is\n              NOT the Control VC, this should\n              result in an inconsistentValue error.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(32, 65535)

class MplsBitRate(TextualConvention, Unsigned32):
    description = "If the value of this object is greater than zero,\n              then this represents the bandwidth of this MPLS\n              interface (or Label Switched Path) in units of\n              '1,000 bits per second'.\n\n              The value, when greater than zero, represents the\n              bandwidth of this MPLS interface (rounded to the\n              nearest 1,000) in units of 1,000 bits per second.\n              If the bandwidth of the MPLS interface is between\n              ((n * 1000) - 500) and ((n * 1000) + 499), the value\n              of this object is n, such that n > 0.\n\n              If the value of this object is 0 (zero), this\n              means that the traffic over this MPLS interface is\n              considered to be best effort."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class MplsBurstSize(TextualConvention, Unsigned32):
    description = 'The number of octets of MPLS data that the stream\n              may send back-to-back without concern for policing.\n              The value of zero indicates that an implementation\n              does not support Burst Size.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsExtendedTunnelId(TextualConvention, Unsigned32):
    reference = 'RSVP-TE: Extensions to RSVP for LSP Tunnels,\n              [RFC3209].\n\n              Constraint-Based LSP Setup using LDP, [RFC3212].'
    description = 'A unique identifier for an MPLS Tunnel.  This may\n              represent an IPv4 address of the ingress or egress\n              LSR for the tunnel.  This value is derived from the\n              Extended Tunnel Id in RSVP or the Ingress Router ID\n              for CR-LDP.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsLabel(TextualConvention, Unsigned32):
    reference = 'Multiprotocol Label Switching Architecture,\n              RFC3031.\n\n              MPLS Label Stack Encoding, [RFC3032].\n\n              Use of Label Switching on Frame Relay Networks,\n              RFC3034.\n\n              MPLS using LDP and ATM VC Switching, RFC3035.\n              Generalized Multiprotocol Label Switching\n              (GMPLS) Architecture, [RFC3471].'
    description = "This value represents an MPLS label as defined in\n              [RFC3031],  [RFC3032], [RFC3034], [RFC3035] and\n              [RFC3471].\n\n              The label contents are specific to the label being\n              represented, such as:\n\n              * The label carried in an MPLS shim header\n                (for LDP this is the Generic Label) is a 20-bit\n                number represented by 4 octets.  Bits 0-19 contain\n                a label or a reserved label value.  Bits 20-31\n                MUST be zero.\n\n                The following is quoted directly from [RFC3032].\n                There are several reserved label values:\n\n                   i. A value of 0 represents the\n                      'IPv4 Explicit NULL Label'.  This label\n                      value is only legal at the bottom of the\n                      label stack.  It indicates that the label\n                      stack must be popped, and the forwarding\n                      of the packet must then be based on the\n                      IPv4 header.\n\n                  ii. A value of 1 represents the\n                      'Router Alert Label'.  This label value is\n                      legal anywhere in the label stack except at\n                      the bottom.  When a received packet\n                      contains this label value at the top of\n                      the label stack, it is delivered to a\n                      local software module for processing.\n                      The actual forwarding of the packet\n                      is determined by the label beneath it\n                      in the stack.  However, if the packet is\n                      forwarded further, the Router Alert Label\n                      should be pushed back onto the label stack\n                      before forwarding.  The use of this label\n                      is analogous to the use of the\n                      'Router Alert Option' in IP packets\n                      [RFC2113].  Since this label\n                      cannot occur at the bottom of the stack,\n                      it is not associated with a\n                      particular network layer protocol.\n\n                 iii. A value of 2 represents the\n                      'IPv6 Explicit NULL Label'.  This label\n                      value is only legal at the bottom of the\n                      label stack.  It indicates that the label\n                      stack must be popped, and the forwarding\n                      of the packet must then be based on the\n                      IPv6 header.\n\n                  iv. A value of 3 represents the\n                      'Implicit NULL Label'.\n                      This is a label that an LSR may assign and\n                      distribute, but which never actually\n                      appears in the encapsulation.  When an\n                      LSR would otherwise replace the label\n                      at the top of the stack with a new label,\n                      but the new label is 'Implicit NULL',\n                      the LSR will pop the stack instead of\n                      doing the replacement.  Although\n                      this value may never appear in the\n                      encapsulation, it needs to be specified in\n                      the Label Distribution Protocol, so a value\n                      is reserved.\n\n                   v. Values 4-15 are reserved.\n\n              * The frame relay label can be either 10-bits or\n                23-bits depending on the DLCI field size and the\n                upper 22-bits or upper 9-bits must be zero,\n                respectively.\n\n              * For an ATM label the lower 16-bits represents the\n                VCI, the next 12-bits represents the VPI and the\n                remaining bits MUST be zero.\n\n              * The Generalized-MPLS (GMPLS) label contains a\n                value greater than 2^24-1 and used in GMPLS\n                as defined in [RFC3471]."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsLabelDistributionMethod(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture,\n              RFC3031.\n\n              LDP Specification, RFC3036, Section 2.6.3.'
    description = 'The label distribution method which is also called\n              the label advertisement mode [RFC3036].\n              Each interface on an LSR is configured to operate\n              in either Downstream Unsolicited or Downstream\n              on Demand.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("downstreamOnDemand", 1), ("downstreamUnsolicited", 2))

class MplsLdpIdentifier(TextualConvention, OctetString):
    description = 'The LDP identifier is a six octet\n              quantity which is used to identify a\n              Label Switching Router (LSR) label space.\n\n              The first four octets identify the LSR and\n              must be a globally unique value, such as a\n              32-bit router ID assigned to the LSR, and the\n              last two octets identify a specific label\n              space within the LSR.'
    status = 'current'
    displayHint = '1d.1d.1d.1d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class MplsLsrIdentifier(TextualConvention, OctetString):
    description = 'The Label Switching Router (LSR) identifier is the\n              first 4 bytes of the Label Distribution Protocol\n              (LDP) identifier.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MplsLdpLabelType(TextualConvention, Integer32):
    description = 'The Layer 2 label types which are defined for MPLS\n              LDP and/or CR-LDP are generic(1), atm(2), or\n              frameRelay(3).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("generic", 1), ("atm", 2), ("frameRelay", 3))

class MplsLSPID(TextualConvention, OctetString):
    reference = 'RSVP-TE:  Extensions to RSVP for LSP Tunnels,\n              [RFC3209].\n\n              Constraint-Based LSP Setup using LDP,\n              [RFC3212].'
    description = 'A unique identifier within an MPLS network that is\n              assigned to each LSP.  This is assigned at the head\n              end of the LSP and can be used by all LSRs\n              to identify this LSP.  This value is piggybacked by\n              the signaling protocol when this LSP is signaled\n              within the network.  This identifier can then be\n              used at each LSR to identify which labels are\n              being swapped to other labels for this LSP.  This\n              object  can also be used to disambiguate LSPs that\n              share the same RSVP sessions between the same\n              source and destination.\n\n              For LSPs established using CR-LDP, the LSPID is\n              composed of the ingress LSR Router ID (or any of\n              its own IPv4 addresses) and a locally unique\n              CR-LSP ID to that LSR.  The first two bytes carry\n              the CR-LSPID, and the remaining 4 bytes carry\n              the Router ID.  The LSPID is useful in network\n              management, in CR-LSP repair, and in using\n              an already established CR-LSP as a hop in\n              an ER-TLV.\n\n              For LSPs signaled using RSVP-TE, the LSP ID is\n              defined as a 16-bit (2 byte) identifier used\n              in the SENDER_TEMPLATE and the FILTER_SPEC\n              that can be changed to allow a sender to\n              share resources with itself.  The length of this\n              object should only be 2 or 6 bytes.  If the length\n              of this octet string is 2 bytes, then it must\n              identify an RSVP-TE LSPID, or it is 6 bytes,\n              it must contain a CR-LDP LSPID.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(2, 2), ValueSizeConstraint(6, 6), )
class MplsLspType(TextualConvention, Integer32):
    description = 'Types of Label Switch Paths (LSPs)\n              on a Label Switching Router (LSR) or a\n              Label Edge Router (LER) are:\n\n                 unknown(1)         -- if the LSP is not known\n                                       to be one of the following.\n\n                 terminatingLsp(2)  -- if the LSP terminates\n                                       on the LSR/LER, then this\n                                       is an egressing LSP\n                                       which ends on the LSR/LER,\n\n                 originatingLsp(3)  -- if the LSP originates\n                                       from this LSR/LER, then\n                                       this is an ingressing LSP\n                                       which is the head-end of\n                                       the LSP,\n\n              crossConnectingLsp(4) -- if the LSP ingresses\n                                       and egresses on the LSR,\n                                       then it is\n                                       cross-connecting on that\n                                       LSR.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("terminatingLsp", 2), ("originatingLsp", 3), ("crossConnectingLsp", 4))

class MplsOwner(TextualConvention, Integer32):
    description = 'This object indicates the local network\n              management subsystem that originally created\n              the object(s) in question.  The values of\n              this enumeration are defined as follows:\n\n              unknown(1) - the local network management\n              subsystem cannot discern which\n              component created the object.\n\n              other(2) - the local network management\n              subsystem is able to discern which component\n              created the object, but the component is not\n              listed within the following choices,\n              e.g., command line interface (cli).\n\n              snmp(3) - The Simple Network Management Protocol\n              was used to configure this object initially.\n\n              ldp(4) - The Label Distribution Protocol was\n              used to configure this object initially.\n\n              crldp(5) - The Constraint-Based Label Distribution\n              Protocol was used to configure this object\n              initially.\n\n              rsvpTe(6) - The Resource Reservation Protocol was\n              used to configure this object initially.\n\n              policyAgent(7) - A policy agent (perhaps in\n              combination with one of the above protocols) was\n              used to configure this object initially.\n\n              An object created by any of the above choices\n              MAY be modified or destroyed by the same or a\n              different choice.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("snmp", 3), ("ldp", 4), ("crldp", 5), ("rsvpTe", 6), ("policyAgent", 7))

class MplsPathIndexOrZero(TextualConvention, Unsigned32):
    description = 'A unique identifier used to identify a specific\n              path used by a tunnel.  A value of 0 (zero) means\n              that no path is in use.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsPathIndex(TextualConvention, Unsigned32):
    description = 'A unique value to index (by Path number) an\n              entry in a table.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class MplsRetentionMode(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture,\n              RFC3031.\n\n              LDP Specification, RFC3036, Section 2.6.2.'
    description = 'The label retention mode which specifies whether\n              an LSR maintains a label binding for a FEC\n              learned from a neighbor that is not its next hop\n              for the FEC.\n\n              If the value is conservative(1) then advertised\n              label mappings are retained only if they will be\n              used to forward packets, i.e., if label came from\n              a valid next hop.\n\n              If the value is liberal(2) then all advertised\n              label mappings are retained whether they are from\n              a valid next hop or not.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("conservative", 1), ("liberal", 2))

class MplsTunnelAffinity(TextualConvention, Unsigned32):
    reference = 'RSVP-TE:  Extensions to RSVP for LSP Tunnels,\n              RFC3209, Section 4.7.4.'
    description = 'Describes the configured 32-bit Include-any,\n              include-all, or exclude-all constraint for\n              constraint-based link selection.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsTunnelIndex(TextualConvention, Unsigned32):
    description = 'A unique index into mplsTunnelTable.\n              For tunnels signaled using RSVP, this value\n              should correspond to the RSVP Tunnel ID\n              used for the RSVP-TE session.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class MplsTunnelInstanceIndex(TextualConvention, Unsigned32):
    description = 'The tunnel entry with instance index 0\n              should refer to the configured tunnel\n              interface (if one exists).\n\n              Values greater than 0, but less than or\n              equal to 65535, should be used to indicate\n              signaled (or backup) tunnel LSP instances.\n              For tunnel LSPs signaled using RSVP,\n              this value should correspond to the\n              RSVP LSP ID used for the RSVP-TE\n              LSP.\n\n              Values greater than 65535 apply to FRR\n              detour instances.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ValueRangeConstraint(65536, 4294967295), )
class TeHopAddressType(TextualConvention, Integer32):
    reference = 'TEXTUAL-CONVENTIONs for Internet Network\n              Addresses, RFC3291.\n\n              Constraint-Based LSP Setup using LDP,\n              [RFC3212]'
    description = 'A value that represents a type of address for a\n              Traffic Engineered (TE) Tunnel hop.\n\n              unknown(0)   An unknown address type.  This value\n                           MUST be used if the value of the\n                           corresponding TeHopAddress object is a\n                           zero-length string.  It may also be\n                           used to indicate a TeHopAddress which\n                           is not in one of the formats defined\n                           below.\n\n              ipv4(1)      An IPv4 network address as defined by\n                           the InetAddressIPv4 TEXTUAL-CONVENTION\n                           [RFC3291].\n\n              ipv6(2)      A global IPv6 address as defined by\n                           the InetAddressIPv6 TEXTUAL-CONVENTION\n                           [RFC3291].\n\n              asnumber(3)  An Autonomous System (AS) number as\n                           defined by the TeHopAddressAS\n                           TEXTUAL-CONVENTION.\n\n              unnum(4)     An unnumbered interface index as\n                           defined by the TeHopAddressUnnum\n                           TEXTUAL-CONVENTION.\n\n              lspid(5)     An LSP ID for TE Tunnels\n                           (RFC3212) as defined by the\n                           MplsLSPID TEXTUAL-CONVENTION.\n\n              Each definition of a concrete TeHopAddressType\n              value must be accompanied by a definition\n              of a TEXTUAL-CONVENTION for use with that\n              TeHopAddress.\n\n              To support future extensions, the TeHopAddressType\n              TEXTUAL-CONVENTION SHOULD NOT be sub-typed in\n              object type definitions.  It MAY be sub-typed in\n              compliance statements in order to require only a\n              subset of these address types for a compliant\n              implementation.\n\n              Implementations must ensure that TeHopAddressType\n              objects and any dependent objects\n              (e.g., TeHopAddress objects) are consistent.\n              An inconsistentValue error must be generated\n              if an attempt to change a TeHopAddressType\n              object would, for example, lead to an\n              undefined TeHopAddress value that is\n              not defined herein.  In particular,\n              TeHopAddressType/TeHopAddress pairs\n              must be changed together if the address\n              type changes (e.g., from ipv6(2) to ipv4(1)).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("asnumber", 3), ("unnum", 4), ("lspid", 5))

class TeHopAddress(TextualConvention, OctetString):
    description = "Denotes a generic Tunnel hop address,\n              that is, the address of a node which\n              an LSP traverses, including the source\n              and destination nodes.  An address may be\n              very concrete, for example, an IPv4 host\n              address (i.e., with prefix length 32);\n              if this IPv4 address is an interface\n              address, then that particular interface\n              must be traversed.  An address may also\n              specify an 'abstract node', for example,\n              an IPv4 address with prefix length\n              less than 32, in which case, the LSP\n              can traverse any node whose address\n              falls in that range.  An address may\n              also specify an Autonomous System (AS),\n              in which  case the LSP can traverse any\n              node that falls within that AS.\n\n              A TeHopAddress value is always interpreted within\n              the context of an TeHopAddressType value.  Every\n              usage of the TeHopAddress TEXTUAL-CONVENTION\n              is required to specify the TeHopAddressType object\n              which provides the context.  It is suggested that\n              the TeHopAddressType object is logically registered\n              before the object(s) which use the TeHopAddress\n              TEXTUAL-CONVENTION if they appear in the\n              same logical row.\n\n              The value of a TeHopAddress object must always be\n              consistent with the value of the associated\n              TeHopAddressType object.  Attempts to set a\n              TeHopAddress object to a value which is\n              inconsistent with the associated TeHopAddressType\n              must fail with an inconsistentValue error."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TeHopAddressAS(TextualConvention, OctetString):
    reference = 'Textual Conventions for Internet Network\n              Addresses, [RFC3291].  The\n              InetAutonomousSystemsNumber TEXTUAL-CONVENTION\n              has a SYNTAX of Unsigned32, whereas this TC\n              has a SYNTAX of OCTET STRING (SIZE (4)).\n              Both TCs represent an autonomous system number\n              but use different syntaxes to do so.'
    description = 'Represents a two or four octet AS number.\n              The AS number is represented in network byte\n              order (MSB first).  A two-octet AS number has\n              the two MSB octets set to zero.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TeHopAddressUnnum(TextualConvention, OctetString):
    description = 'Represents an unnumbered interface:\n\n              octets   contents               encoding\n               1-4     unnumbered interface   network-byte order\n\n              The corresponding TeHopAddressType value is\n              unnum(5).'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

mibBuilder.exportSymbols("MPLS-TC-STD-MIB", mplsTCStdMIB=mplsTCStdMIB, MplsLabel=MplsLabel, TeHopAddress=TeHopAddress, MplsLdpIdentifier=MplsLdpIdentifier, MplsBurstSize=MplsBurstSize, TeHopAddressType=TeHopAddressType, MplsLdpLabelType=MplsLdpLabelType, mplsStdMIB=mplsStdMIB, MplsOwner=MplsOwner, MplsTunnelAffinity=MplsTunnelAffinity, MplsLsrIdentifier=MplsLsrIdentifier, MplsLspType=MplsLspType, MplsLSPID=MplsLSPID, MplsPathIndexOrZero=MplsPathIndexOrZero, MplsBitRate=MplsBitRate, MplsExtendedTunnelId=MplsExtendedTunnelId, PYSNMP_MODULE_ID=mplsTCStdMIB, MplsTunnelInstanceIndex=MplsTunnelInstanceIndex, TeHopAddressAS=TeHopAddressAS, MplsRetentionMode=MplsRetentionMode, MplsTunnelIndex=MplsTunnelIndex, MplsAtmVcIdentifier=MplsAtmVcIdentifier, MplsLabelDistributionMethod=MplsLabelDistributionMethod, MplsPathIndex=MplsPathIndex, TeHopAddressUnnum=TeHopAddressUnnum)
