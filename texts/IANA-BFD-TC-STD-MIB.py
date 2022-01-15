#
# PySNMP MIB module IANA-BFD-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IANA-BFD-TC-STD-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:08:23 2022
# On host fv-az74-933 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, NotificationType, Unsigned32, iso, mib_2, ModuleIdentity, Counter64, Counter32, ObjectIdentity, Bits, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32", "iso", "mib-2", "ModuleIdentity", "Counter64", "Counter32", "ObjectIdentity", "Bits", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaBfdTCStdMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 224))
ianaBfdTCStdMib.setRevisions(('2014-08-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaBfdTCStdMib.setRevisionsDescriptions(('Initial version.  Published as RFC 7330.',))
if mibBuilder.loadTexts: ianaBfdTCStdMib.setLastUpdated('201408120000Z')
if mibBuilder.loadTexts: ianaBfdTCStdMib.setOrganization('IANA')
if mibBuilder.loadTexts: ianaBfdTCStdMib.setContactInfo('Internet Assigned Numbers Authority\n                    Postal: 12025 Waterfront Drive, Suite 300\n                            Los Angeles, CA  90094-2536\n                    Tel:    +1 310 301 5800\n                    EMail:  iana&iana.org')
if mibBuilder.loadTexts: ianaBfdTCStdMib.setDescription("Copyright (c) 2014 IETF Trust and the persons identified as\n           authors of the code.  All rights reserved.\n\n           Redistribution and use in source and binary forms, with or\n           without modification, is permitted pursuant to, and subject\n           to the license terms contained in, the Simplified BSD License\n           set forth in Section 4.c of the IETF Trust's Legal Provisions\n           Relating to IETF Documents\n           (http://trustee.ietf.org/license-info).")
class IANAbfdDiagTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding\n         Detection (BFD), RFC 5880, June 2010.\n\n         Allan, D., Swallow, G., and Drake, J., Proactive Connectivity\n         Verification, Continuity Check, and Remote Defect\n         Indication for the MPLS Transport Profile, RFC 6428,\n         November 2011.'
    description = 'A common BFD diagnostic code.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noDiagnostic", 0), ("controlDetectionTimeExpired", 1), ("echoFunctionFailed", 2), ("neighborSignaledSessionDown", 3), ("forwardingPlaneReset", 4), ("pathDown", 5), ("concatenatedPathDown", 6), ("administrativelyDown", 7), ("reverseConcatenatedPathDown", 8), ("misConnectivityDefect", 9))

class IANAbfdSessTypeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding\n         Detection (BFD), RFC 5880, June 2010.\n\n         Katz, D. and D. Ward, Bidirectional Forwarding\n         Detection (BFD) for IPv4 and IPv6 (Single Hop),\n         RFC 5881, June 2010.\n\n         Katz, D. and D. Ward, Bidirectional Forwarding\n         Detection (BFD) for Multihop Paths, RFC 5883,\n         June 2010.'
    description = 'BFD session type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("singleHop", 1), ("multiHopTotallyArbitraryPaths", 2), ("multiHopOutOfBandSignaling", 3), ("multiHopUnidirectionalLinks", 4))

class IANAbfdSessOperModeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding\n         Detection (BFD), RFC 5880, June 2010.'
    description = 'BFD session operating mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("asyncModeWEchoFunction", 1), ("asynchModeWOEchoFunction", 2), ("demandModeWEchoFunction", 3), ("demandModeWOEchoFunction", 4))

class IANAbfdSessStateTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding\n         Detection (BFD), RFC 5880, June 2010.'
    description = 'BFD session state.  State failing(5) is only applicable if\n         corresponding session is running in BFD version 0.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("adminDown", 1), ("down", 2), ("init", 3), ("up", 4), ("failing", 5))

class IANAbfdSessAuthenticationTypeTC(TextualConvention, Integer32):
    reference = 'Sections 4.2 - 4.4 from Katz, D. and D. Ward,\n         Bidirectional Forwarding Detection (BFD),\n         RFC 5880, June 2010.'
    description = 'BFD authentication type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("noAuthentication", -1), ("reserved", 0), ("simplePassword", 1), ("keyedMD5", 2), ("meticulousKeyedMD5", 3), ("keyedSHA1", 4), ("meticulousKeyedSHA1", 5))

class IANAbfdSessAuthenticationKeyTC(TextualConvention, OctetString):
    reference = 'Sections 4.2 - 4.4 from Katz, D. and D. Ward, Bidirectional\n         Forwarding Detection (BFD), RFC 5880, June 2010.'
    description = "BFD authentication key type.\n\n         An IANAbfdSessAuthenticationKeyTC is always interpreted\n         within the context of an IANAbfdSessAuthenticationTypeTC\n         value.  Every usage of the IANAbfdSessAuthenticationTypeTC\n         textual convention is required to specify the\n         IANAbfdSessAuthenticationKeyTC object that provides the\n         context.  It is suggested that the\n         IANAbfdSessAuthenticationKeyTC object be logically registered\n         before the object(s) that use the\n         IANAbfdSessAuthenticationKeyTC textual convention, if they\n         appear in the same logical row.\n\n         The value of an IANAbfdSessAuthenticationKeyTC must\n         always be consistent with the value of the associated\n         IANAbfdSessAuthenticationTypeTC object.  Attempts to set an\n         IANAbfdSessAuthenticationKeyTC object to a value inconsistent\n         with the associated IANAbfdSessAuthenticationTypeTC must fail\n         with an inconsistentValue error.\n\n         The following size constraints for an\n         IANAbfdSessAuthenticationKeyTC object are defined for the\n         associated IANAbfdSessAuthenticationTypeTC values show below:\n\n         noAuthentication(-1): SIZE(0)\n         reserved(0): SIZE(0)\n         simplePassword(1): SIZE(1..16)\n         keyedMD5(2): SIZE(16)\n         meticulousKeyedMD5(3): SIZE(16)\n         keyedSHA1(4): SIZE(20)\n         meticulousKeyedSHA1(5): SIZE(20)\n\n         When this textual convention is used as the syntax of an\n         index object, there may be issues with the limit of 128\n         sub-identifiers specified in SMIv2, STD 58.  In this case,\n         the object definition MUST include a 'SIZE' clause to limit\n         the number of potential instance sub-identifiers; otherwise,\n         the applicable constraints MUST be stated in the appropriate\n         conceptual row DESCRIPTION clauses, or in the surrounding\n         documentation if there is no single DESCRIPTION clause that\n         is appropriate."
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 252)

mibBuilder.exportSymbols("IANA-BFD-TC-STD-MIB", IANAbfdSessStateTC=IANAbfdSessStateTC, PYSNMP_MODULE_ID=ianaBfdTCStdMib, IANAbfdSessAuthenticationKeyTC=IANAbfdSessAuthenticationKeyTC, ianaBfdTCStdMib=ianaBfdTCStdMib, IANAbfdSessTypeTC=IANAbfdSessTypeTC, IANAbfdSessAuthenticationTypeTC=IANAbfdSessAuthenticationTypeTC, IANAbfdSessOperModeTC=IANAbfdSessOperModeTC, IANAbfdDiagTC=IANAbfdDiagTC)
