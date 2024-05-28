#
# PySNMP MIB module MPLS-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/MPLS-TC-STD-MIB
# Produced by pysmi-1.1.12 at Tue May 28 13:44:34 2024
# On host fv-az768-311 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
transmission, NotificationType, ModuleIdentity, Gauge32, MibIdentifier, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Counter64, IpAddress, Bits, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "transmission", "NotificationType", "ModuleIdentity", "Gauge32", "MibIdentifier", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Counter64", "IpAddress", "Bits", "ObjectIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mplsTCStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 1))
mplsTCStdMIB.setRevisions(('2004-06-03 00:00',))
if mibBuilder.loadTexts: mplsTCStdMIB.setLastUpdated('200406030000Z')
if mibBuilder.loadTexts: mplsTCStdMIB.setOrganization('IETF Multiprotocol Label Switching (MPLS) Working Group.')
mplsStdMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166))
class MplsAtmVcIdentifier(TextualConvention, Integer32):
    reference = 'MPLS using LDP and ATM VC Switching, RFC3035.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(32, 65535)

class MplsBitRate(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class MplsBurstSize(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsExtendedTunnelId(TextualConvention, Unsigned32):
    reference = 'RSVP-TE: Extensions to RSVP for LSP Tunnels, [RFC3209]. Constraint-Based LSP Setup using LDP, [RFC3212].'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsLabel(TextualConvention, Unsigned32):
    reference = 'Multiprotocol Label Switching Architecture, RFC3031. MPLS Label Stack Encoding, [RFC3032]. Use of Label Switching on Frame Relay Networks, RFC3034. MPLS using LDP and ATM VC Switching, RFC3035. Generalized Multiprotocol Label Switching (GMPLS) Architecture, [RFC3471].'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsLabelDistributionMethod(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture, RFC3031. LDP Specification, RFC3036, Section 2.6.3.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("downstreamOnDemand", 1), ("downstreamUnsolicited", 2))

class MplsLdpIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class MplsLsrIdentifier(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MplsLdpLabelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("generic", 1), ("atm", 2), ("frameRelay", 3))

class MplsLSPID(TextualConvention, OctetString):
    reference = 'RSVP-TE: Extensions to RSVP for LSP Tunnels, [RFC3209]. Constraint-Based LSP Setup using LDP, [RFC3212].'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(2, 2), ValueSizeConstraint(6, 6), )
class MplsLspType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("terminatingLsp", 2), ("originatingLsp", 3), ("crossConnectingLsp", 4))

class MplsOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("snmp", 3), ("ldp", 4), ("crldp", 5), ("rsvpTe", 6), ("policyAgent", 7))

class MplsPathIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsPathIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class MplsRetentionMode(TextualConvention, Integer32):
    reference = 'Multiprotocol Label Switching Architecture, RFC3031. LDP Specification, RFC3036, Section 2.6.2.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("conservative", 1), ("liberal", 2))

class MplsTunnelAffinity(TextualConvention, Unsigned32):
    reference = 'RSVP-TE: Extensions to RSVP for LSP Tunnels, RFC3209, Section 4.7.4.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsTunnelIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class MplsTunnelInstanceIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ValueRangeConstraint(65536, 4294967295), )
class TeHopAddressType(TextualConvention, Integer32):
    reference = 'TEXTUAL-CONVENTIONs for Internet Network Addresses, RFC3291. Constraint-Based LSP Setup using LDP, [RFC3212]'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("asnumber", 3), ("unnum", 4), ("lspid", 5))

class TeHopAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TeHopAddressAS(TextualConvention, OctetString):
    reference = 'Textual Conventions for Internet Network Addresses, [RFC3291]. The InetAutonomousSystemsNumber TEXTUAL-CONVENTION has a SYNTAX of Unsigned32, whereas this TC has a SYNTAX of OCTET STRING (SIZE (4)). Both TCs represent an autonomous system number but use different syntaxes to do so.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TeHopAddressUnnum(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

mibBuilder.exportSymbols("MPLS-TC-STD-MIB", MplsRetentionMode=MplsRetentionMode, MplsTunnelIndex=MplsTunnelIndex, MplsLdpIdentifier=MplsLdpIdentifier, TeHopAddressType=TeHopAddressType, MplsLSPID=MplsLSPID, mplsTCStdMIB=mplsTCStdMIB, PYSNMP_MODULE_ID=mplsTCStdMIB, MplsTunnelInstanceIndex=MplsTunnelInstanceIndex, MplsLsrIdentifier=MplsLsrIdentifier, MplsTunnelAffinity=MplsTunnelAffinity, TeHopAddressAS=TeHopAddressAS, MplsPathIndex=MplsPathIndex, mplsStdMIB=mplsStdMIB, MplsPathIndexOrZero=MplsPathIndexOrZero, MplsLdpLabelType=MplsLdpLabelType, TeHopAddressUnnum=TeHopAddressUnnum, MplsAtmVcIdentifier=MplsAtmVcIdentifier, MplsLabelDistributionMethod=MplsLabelDistributionMethod, MplsBitRate=MplsBitRate, MplsLspType=MplsLspType, MplsExtendedTunnelId=MplsExtendedTunnelId, MplsOwner=MplsOwner, MplsBurstSize=MplsBurstSize, TeHopAddress=TeHopAddress, MplsLabel=MplsLabel)
