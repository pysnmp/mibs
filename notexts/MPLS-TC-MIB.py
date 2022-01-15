#
# PySNMP MIB module MPLS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 05:10:38 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, Bits, ModuleIdentity, Integer32, Counter32, Gauge32, ObjectIdentity, TimeTicks, transmission, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Bits", "ModuleIdentity", "Integer32", "Counter32", "Gauge32", "ObjectIdentity", "TimeTicks", "transmission", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mplsTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 9999, 1))
mplsTCMIB.setRevisions(('2001-01-04 12:00',))
if mibBuilder.loadTexts: mplsTCMIB.setLastUpdated('200101040000Z')
if mibBuilder.loadTexts: mplsTCMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
mplsMIB = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9999))
class MplsAtmVcIdentifier(TextualConvention, Integer32):
    reference = 'Definitions of Textual Conventions and OBJECT- IDENTITIES for ATM Management, RFC 2514, Feb. 1999.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(32, 65535)

class MplsBitRate(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MplsBurstSize(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class MplsExtendedTunnelId(TextualConvention, Unsigned32):
    reference = '1. Awduche, D., et al., RSVP-TE: Extensions to RSVP for LSP Tunnels, RFC 3209, December 2001. 2. Constraint-Based LSP Setup using LDP, Jamoussi, B., et al., draft-ietf-mpls-cr-ldp-06.txt, November 2001.'
    status = 'current'

class MplsInitialCreationSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("snmp", 2), ("ldp", 3), ("rsvp", 4), ("crldp", 5), ("policyAgent", 6), ("unknown", 7))

class MplsLSPID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class MplsLabel(TextualConvention, Unsigned32):
    reference = '1. Multiprotocol Label Switching Architecture, Rosen et al, RFC 3031, August 1999. 2. MPLS Label Stack Encoding, Rosen et al, RFC 3032, January 2001. 3. Use of Label Switching on Frame Relay Networks, Conta et al, RFC 3034, January 2001. 4. MPLS using LDP and ATM VC switching, Davie et al, RFC 3035, January 2001.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsLdpGenAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class MplsLdpIdentifier(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class MplsLdpLabelTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("generic", 1), ("atm", 2), ("frameRelay", 3))

class MplsLsrIdentifier(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MplsPathIndex(TextualConvention, Unsigned32):
    status = 'current'

class MplsPathIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'

class MplsPortNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class MplsTunnelAffinity(TextualConvention, Unsigned32):
    status = 'current'

class MplsTunnelIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class MplsTunnelInstanceIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

mibBuilder.exportSymbols("MPLS-TC-MIB", MplsLdpIdentifier=MplsLdpIdentifier, MplsExtendedTunnelId=MplsExtendedTunnelId, MplsLsrIdentifier=MplsLsrIdentifier, MplsAtmVcIdentifier=MplsAtmVcIdentifier, MplsInitialCreationSource=MplsInitialCreationSource, MplsLSPID=MplsLSPID, MplsPathIndex=MplsPathIndex, MplsLdpGenAddr=MplsLdpGenAddr, MplsPathIndexOrZero=MplsPathIndexOrZero, MplsBurstSize=MplsBurstSize, MplsTunnelAffinity=MplsTunnelAffinity, PYSNMP_MODULE_ID=mplsTCMIB, MplsPortNumber=MplsPortNumber, MplsLdpLabelTypes=MplsLdpLabelTypes, MplsTunnelIndex=MplsTunnelIndex, mplsTCMIB=mplsTCMIB, mplsMIB=mplsMIB, MplsBitRate=MplsBitRate, MplsLabel=MplsLabel, MplsTunnelInstanceIndex=MplsTunnelInstanceIndex)
