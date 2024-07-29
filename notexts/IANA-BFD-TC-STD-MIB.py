#
# PySNMP MIB module IANA-BFD-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-BFD-TC-STD-MIB
# Produced by pysmi-1.1.12 at Mon Jul 29 02:30:42 2024
# On host fv-az654-133 platform Linux version 6.5.0-1024-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, Counter64, Gauge32, Integer32, iso, IpAddress, mib_2, Bits, Unsigned32, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Counter64", "Gauge32", "Integer32", "iso", "IpAddress", "mib-2", "Bits", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaBfdTCStdMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 224))
ianaBfdTCStdMib.setRevisions(('2014-08-12 00:00',))
if mibBuilder.loadTexts: ianaBfdTCStdMib.setLastUpdated('201408120000Z')
if mibBuilder.loadTexts: ianaBfdTCStdMib.setOrganization('IANA')
class IANAbfdDiagTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010. Allan, D., Swallow, G., and Drake, J., Proactive Connectivity Verification, Continuity Check, and Remote Defect Indication for the MPLS Transport Profile, RFC 6428, November 2011.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noDiagnostic", 0), ("controlDetectionTimeExpired", 1), ("echoFunctionFailed", 2), ("neighborSignaledSessionDown", 3), ("forwardingPlaneReset", 4), ("pathDown", 5), ("concatenatedPathDown", 6), ("administrativelyDown", 7), ("reverseConcatenatedPathDown", 8), ("misConnectivityDefect", 9))

class IANAbfdSessTypeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010. Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), RFC 5881, June 2010. Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for Multihop Paths, RFC 5883, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("singleHop", 1), ("multiHopTotallyArbitraryPaths", 2), ("multiHopOutOfBandSignaling", 3), ("multiHopUnidirectionalLinks", 4))

class IANAbfdSessOperModeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("asyncModeWEchoFunction", 1), ("asynchModeWOEchoFunction", 2), ("demandModeWEchoFunction", 3), ("demandModeWOEchoFunction", 4))

class IANAbfdSessStateTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("adminDown", 1), ("down", 2), ("init", 3), ("up", 4), ("failing", 5))

class IANAbfdSessAuthenticationTypeTC(TextualConvention, Integer32):
    reference = 'Sections 4.2 - 4.4 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("noAuthentication", -1), ("reserved", 0), ("simplePassword", 1), ("keyedMD5", 2), ("meticulousKeyedMD5", 3), ("keyedSHA1", 4), ("meticulousKeyedSHA1", 5))

class IANAbfdSessAuthenticationKeyTC(TextualConvention, OctetString):
    reference = 'Sections 4.2 - 4.4 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 252)

mibBuilder.exportSymbols("IANA-BFD-TC-STD-MIB", IANAbfdSessAuthenticationKeyTC=IANAbfdSessAuthenticationKeyTC, IANAbfdSessTypeTC=IANAbfdSessTypeTC, ianaBfdTCStdMib=ianaBfdTCStdMib, IANAbfdDiagTC=IANAbfdDiagTC, IANAbfdSessAuthenticationTypeTC=IANAbfdSessAuthenticationTypeTC, IANAbfdSessOperModeTC=IANAbfdSessOperModeTC, IANAbfdSessStateTC=IANAbfdSessStateTC, PYSNMP_MODULE_ID=ianaBfdTCStdMib)
