#
# PySNMP MIB module IANA-BFD-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IANA-BFD-TC-STD-MIB
# Produced by pysmi-1.1.8 at Thu Sep 29 08:40:43 2022
# On host fv-az460-75 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Integer32, Bits, Counter32, mib_2, ObjectIdentity, TimeTicks, ModuleIdentity, Gauge32, IpAddress, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Integer32", "Bits", "Counter32", "mib-2", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Gauge32", "IpAddress", "iso", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("IANA-BFD-TC-STD-MIB", PYSNMP_MODULE_ID=ianaBfdTCStdMib, IANAbfdDiagTC=IANAbfdDiagTC, IANAbfdSessAuthenticationTypeTC=IANAbfdSessAuthenticationTypeTC, IANAbfdSessStateTC=IANAbfdSessStateTC, IANAbfdSessOperModeTC=IANAbfdSessOperModeTC, ianaBfdTCStdMib=ianaBfdTCStdMib, IANAbfdSessAuthenticationKeyTC=IANAbfdSessAuthenticationKeyTC, IANAbfdSessTypeTC=IANAbfdSessTypeTC)
