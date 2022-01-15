#
# PySNMP MIB module MPLS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:04:53 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, NotificationType, ObjectIdentity, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Counter32, Gauge32, MibIdentifier, Integer32, transmission, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "NotificationType", "ObjectIdentity", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Counter32", "Gauge32", "MibIdentifier", "Integer32", "transmission", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mplsTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 9999, 1))
mplsTCMIB.setRevisions(('2001-01-04 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsTCMIB.setRevisionsDescriptions(('Initial version published as part of RFC XXXX.',))
if mibBuilder.loadTexts: mplsTCMIB.setLastUpdated('200101040000Z')
if mibBuilder.loadTexts: mplsTCMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: mplsTCMIB.setContactInfo('        Thomas D. Nadeau\n                 Cisco Systems, Inc.\n                 tnadeau@cisco.com\n\n                 Joan Cucchiara\n                 Crescent Networks\n                 jcucchiara@crescentnetworks.com\n\n                 Cheenu Srinivasan\n                 Parama Networks, Inc.\n                 cheenu@paramanet.com\n\n                 Arun Viswanathan\n                 Force10 Networks, Inc.\n                 arun@force10networks.com\n\n                 Hans Sjostrand\n                 ipUnplugged\n                 hans@ipunplugged.com\n\n        Email comments to the MPLS WG Mailing List at\n          mpls@uu.net.')
if mibBuilder.loadTexts: mplsTCMIB.setDescription('This MIB module defines Textual Conventions and\n          OBJECT-IDENTITIES for use in documents defining\n          management information bases (MIBs) for managing\n          MPLS networks.')
mplsMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9999))
class MplsAtmVcIdentifier(TextualConvention, Integer32):
    reference = 'Definitions of Textual Conventions and OBJECT-\n          IDENTITIES for ATM Management, RFC 2514, Feb.\n          1999.'
    description = 'The VCI value for a VCL. The maximum VCI value\n          cannot exceed the value allowable by\n          atmInterfaceMaxVciBits defined in ATM-MIB. The\n          minimum value is 32, values 0 to 31 are reserved\n          for other uses by the ITU and ATM Forum.  32 is\n          typically the  default value for the Control VC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(32, 65535)

class MplsBitRate(TextualConvention, Integer32):
    description = "An estimate of bandwidth in units of 1,000 bits per\n          second.  If this object reports a value of 'n' then\n          the rate of the object is somewhere in the range of\n          'n-500' to 'n+499'. For objects which do not vary\n          in bit rate, or for those where no accurate\n          estimation can be made, this object should contain\n          the nominal bit rate."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MplsBurstSize(TextualConvention, Unsigned32):
    description = 'The number of octets of MPLS data that the stream\n          may send back-to-back without concern for\n          policing.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class MplsExtendedTunnelId(TextualConvention, Unsigned32):
    reference = '1. Awduche, D., et al., RSVP-TE: Extensions to RSVP\n          for LSP Tunnels,  RFC 3209, December 2001.\n         2. Constraint-Based LSP Setup using LDP, Jamoussi,\n          B., et al., draft-ietf-mpls-cr-ldp-06.txt, November\n          2001.'
    description = 'A unique identifier for an MPLS Tunnel. This MAY\n          represent an IpV4 address of the ingress or egress\n          LSR for the tunnel. This value is derived from the\n          Extended Tunnel Id in RSVP or the Ingress Router ID\n          for CR-LDP.'
    status = 'current'

class MplsInitialCreationSource(TextualConvention, Integer32):
    description = 'The entity that originally created the object in\n          question. The values of this enumeration are\n          defined as follows:\n\n         other(1) - This is used when an entity which has not\n          been enumerated in this textual convention but\n          which is known by the agent.\n\n         snmp(2) - The Simple Network Management Protocol was\n          used to configure this object initially.\n\n         ldp(3 - The Label Distribution Protocol was used to\n          configure this object initially.\n\n         rsvp(4) - The Resource Reservation Protocol was used\n          to configure this object initially.\n\n         crldp(5) - The Constraint-Based Label Distribution\n          Protocol was used to configure this object\n          initially.\n\n         policyAgent(6) - A policy agent (perhaps in\n          combination with one of the above protocols) was\n          used to configure this object initially.\n\n         unknown(7) - the agent cannot discern which\n          component created the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("snmp", 2), ("ldp", 3), ("rsvp", 4), ("crldp", 5), ("policyAgent", 6), ("unknown", 7))

class MplsLSPID(TextualConvention, OctetString):
    description = 'An identifier that is assigned to each LSP and is\n          used to uniquely identify it.  This is assigned at\n          the head end of the LSP and can be used by all LSRs\n          to identify this LSP.  This value is piggybacked by\n          the signaling protocol when this LSP is signaled\n\n\n          within the network.  This identifier can then be\n          used at each LSR to identify which labels are being\n          swapped to other labels for this LSP.  For IPv4\n          addresses this results in a 6-octet long cookie.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class MplsLabel(TextualConvention, Unsigned32):
    reference = '1. Multiprotocol Label Switching Architecture, Rosen\n          et al, RFC 3031, August 1999.\n         2. MPLS Label Stack Encoding, Rosen et al, RFC 3032,\n          January 2001.\n         3. Use of Label Switching on Frame Relay Networks,\n          Conta et al, RFC 3034, January 2001.\n         4. MPLS using LDP and ATM VC switching, Davie et al,\n          RFC 3035, January 2001.'
    description = 'This value represents an MPLS label as defined in\n          [RFC3031],  [RFC3032], [RFC3034] and [RFC3035].'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsLdpGenAddr(TextualConvention, OctetString):
    description = 'The value of an network layer or data link layer\n          address.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class MplsLdpIdentifier(TextualConvention, OctetString):
    description = 'The LDP identifier is a six octet quantity which is\n          used to identify an Label Switch Router (LSR) label\n          space.\n\n         The first four octets identify the LSR and must be a\n          globally unique value, such as a 32-bit router ID\n          assigned to the LSR, and the last two octets\n          identify a specific label space within the LSR.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class MplsLdpLabelTypes(TextualConvention, Integer32):
    description = 'The Layer 2 label types which are defined for MPLS\n          LDP/CRLDP are generic(1), atm(2), or\n          frameRelay(3).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("generic", 1), ("atm", 2), ("frameRelay", 3))

class MplsLsrIdentifier(TextualConvention, OctetString):
    description = 'The Label Switch Router (LSR) identifier is the\n          first 4 bytes of the Label Distribution Protocol\n          (LDP) identifier.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MplsPathIndex(TextualConvention, Unsigned32):
    description = 'A unique identifier used to identify a specific path\n          used by a tunnel.'
    status = 'current'

class MplsPathIndexOrZero(TextualConvention, Unsigned32):
    description = 'A unique identifier used to identify a specific path\n          used by a tunnel. If this value is set to 0, it\n          indicates that no path is in use.'
    status = 'current'

class MplsPortNumber(TextualConvention, Integer32):
    description = 'A TCP or UDP port number. Along with an IP address\n          identifies a stream of IP traffic uniquely.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class MplsTunnelAffinity(TextualConvention, Unsigned32):
    description = 'Include-any, include-all, or exclude-all constraint\n          for link selection.'
    status = 'current'

class MplsTunnelIndex(TextualConvention, Integer32):
    description = 'Index into mplsTunnelTable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class MplsTunnelInstanceIndex(TextualConvention, Unsigned32):
    description = 'Instance index into mplsTunnelTable.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

mibBuilder.exportSymbols("MPLS-TC-MIB", MplsAtmVcIdentifier=MplsAtmVcIdentifier, MplsExtendedTunnelId=MplsExtendedTunnelId, MplsLsrIdentifier=MplsLsrIdentifier, MplsPathIndexOrZero=MplsPathIndexOrZero, MplsLdpGenAddr=MplsLdpGenAddr, MplsInitialCreationSource=MplsInitialCreationSource, MplsPortNumber=MplsPortNumber, MplsTunnelAffinity=MplsTunnelAffinity, MplsTunnelIndex=MplsTunnelIndex, MplsBitRate=MplsBitRate, MplsTunnelInstanceIndex=MplsTunnelInstanceIndex, MplsLSPID=MplsLSPID, MplsBurstSize=MplsBurstSize, PYSNMP_MODULE_ID=mplsTCMIB, MplsLdpLabelTypes=MplsLdpLabelTypes, mplsMIB=mplsMIB, MplsLdpIdentifier=MplsLdpIdentifier, mplsTCMIB=mplsTCMIB, MplsPathIndex=MplsPathIndex, MplsLabel=MplsLabel)
