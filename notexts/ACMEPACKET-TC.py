#
# PySNMP MIB module ACMEPACKET-TC (http://snmplabs.com/pysmi)
# ASN.1 source ACMEPACKET-TC
# Source digest sha256:f0f9b29c00d3b9d09c13a4216f670dd0a0cf75404e4918011cd58ad4c212eb3f
# Produced by pysmi-2.3.0
#
acmepacket, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacket")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
apTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 0))
apTextualConventions.setRevisions(('2012-02-06 23:05', '2012-05-05 23:05', '2014-06-26 00:00', '2020-07-20 00:00', '2020-10-26 00:00', '2020-12-14 00:00', '2021-06-07 00:00', '2022-02-16 00:00', '2022-02-16 00:00', '2022-03-17 00:00', '2022-03-22 00:00', '2022-03-01 00:00', '2022-03-24 00:00', '2022-05-17 00:00',))
if mibBuilder.loadTexts: apTextualConventions.setLastUpdated('2022-03-24 00:00')
if mibBuilder.loadTexts: apTextualConventions.setOrganization('Oracle Communications')
class ApHardwareModuleFamily(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 17, 18, 19, 24, 25, 26, 240, 241, 242))
    namedValues = NamedValues(("unknown", 0), ("spu", 17), ("npu", 18), ("tcu", 19), ("niuCopper", 24), ("niuFiber", 25), ("miu", 26), ("fanTray", 240), ("powerSupply", 241), ("niu10g", 242))

class ApRedundancyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 0), ("initial", 1), ("active", 2), ("standby", 3), ("outOfService", 4), ("unassigned", 5), ("activePending", 6), ("standbyPending", 7), ("outOfServicePending", 8), ("recovery", 9))

class ApPhyPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unknown", 0), ("sfp", 1))

class ApPresence(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("inserted", 1), ("removed", 2))

class ApTransportType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("tcp", 1), ("sctp", 2))

class ApServerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("inservice", 0), ("lowerpriority", 1), ("oosunreachable", 2))

class ApDiamResultCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1001, 2001, 2002, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 4001, 4002, 4003, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012, 5013, 5014, 5015, 5016, 5017))
    namedValues = NamedValues(("diameterMultiRoundAuth", 1001), ("diameterSuccess", 2001), ("diameterLimitedSuccess", 2002), ("diameterCommandUnsupported", 3001), ("diameterUnableToDeliver", 3002), ("diameterRealmNotServed", 3003), ("diameterTooBusy", 3004), ("diameterLoopDetected", 3005), ("diameterRedirectIndicatoion", 3006), ("diameterApplicationUnsupported", 3007), ("diameterInvalidHdrBits", 3008), ("diameterInvalidAvpBits", 3009), ("diameterUnknownPeer", 3010), ("diameterAuthenticationRejected", 4001), ("diameterOutOfSpace", 4002), ("electionLost", 4003), ("diameterAvpUnsupported", 5001), ("diameterUnknownSessionId", 5002), ("diameterAuthoriszationRejected", 5003), ("diameterInvalidAvpValue", 5004), ("diameterMissingAvp", 5005), ("diameterResourcesExceeded", 5006), ("diameterContradictingAvps", 5007), ("diameterAvpNotAllowed", 5008), ("diameterAvpTooManyTimes", 5009), ("diameterNoCommonApplication", 5010), ("diameterUnsupportedVersion", 5011), ("diameterUnableToComply", 5012), ("diameterInvalidBitInHeader", 5013), ("diameterInvalidAvpLength", 5014), ("diameterInvalidMessageLength", 5015), ("diameterInvalidAvpBitCombo", 5016), ("diameterNoCommonSecurity", 5017))

class ApPercentage(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class ApSipMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("other", 1), ("invite", 2), ("ack", 3), ("bye", 4), ("register", 5), ("cancel", 6), ("prack", 7), ("options", 8), ("info", 9), ("subscribe", 10), ("notify", 11), ("refer", 12), ("update", 13), ("message", 14), ("publish", 15))

class ApThreadOverloaded(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notApplicable", 1), ("true", 2), ("false", 3))

class ApCommMonitorState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("outofservice", 0), ("connecting", 1), ("connected", 2), ("inservice", 3))

class ApAclType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("untrusted", 0), ("trusted", 1))

class ApDosThresholdTrafficType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("trusted", 1), ("untrusted", 2), ("arp", 3))

class ApDosThresholdCrossState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("not-crossed", 0), ("crossed", 1))

class ApCounterStatsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("recent", 1), ("total", 2), ("permax", 3))

class ApStirStatsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26))
    namedValues = NamedValues(("asQueries", 1), ("asSuccessResponses", 2), ("asFailResponses", 3), ("asFailServiceException", 4), ("asFailPolicyException", 5), ("vsQueries", 6), ("vsSuccessResponses", 7), ("vsFailResponses", 8), ("vsSuccessVerification", 9), ("vsFailVerification", 10), ("vsFailServiceException", 11), ("vsFailPolicyException", 12), ("serverUnreachable", 13), ("asSentInviteswithShakenPASSportA", 14), ("asSentInviteswithShakenPASSportB", 15), ("asSentInviteswithShakenPASSportC", 16), ("asSentInviteswithdivPASSport", 17), ("vsReceivedInviteswithNoPASSport", 18), ("vsReceivedInviteswithShakenPASSport", 19), ("vsReceivedInviteswithDivPASSport", 20), ("vsSentInviteswithTNValidationPassed", 21), ("vsSentInviteswithTNValidationFailed", 22), ("vsSentInviteswithNoTNValidation", 23), ("asServiceUnreachable", 24), ("vsServiceUnreachable", 25), ("apStirStatsTypeMax", 26))

class ApMsrpKpiStatsCounterType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("recent", 1), ("high", 2), ("total", 3), ("ltotal", 4), ("lpermax", 5), ("lhigh", 6))

class ApMsrpKpiStatsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125))
    namedValues = NamedValues(("msrp-AvgSENDTransTx", 1), ("msrp-AvgChatSENDTransTx", 2), ("msrp-AvgIsTypingSENDTransTx", 3), ("msrp-AvgReceiptSENDTransTx", 4), ("msrp-AvgSENDMsgBytesTx", 5), ("msrp-AvgChatSENDMsgBytesTx", 6), ("msrp-AvgIsTypingSENDMsgBytesTx", 7), ("msrp-AvgReceiptSENDMsgBytesTx", 8), ("msrp-SENDMsgBytesTx", 9), ("msrp-ChatSENDMsgBytesTx", 10), ("msrp-IsTypingSENDMsgBytesTx", 11), ("msrp-ReceiptSENDMsgBytesTx", 12), ("msrp-SuccessREPORTTransTx", 13), ("msrp-FailureREPORTTransTx", 14), ("msrp-AvgSuccessREPORTMsgBytesTx", 15), ("msrp-AvgFailureREPORTMsgBytesTx", 16), ("msrp-AvgFailureREPORTRateTx", 17), ("msrp-AvgSuccessREPORTRateTx", 18), ("msrp-REPORTTrans400Tx", 19), ("msrp-REPORTTrans401Tx", 20), ("msrp-REPORTTrans403Tx", 21), ("msrp-REPORTTrans404Tx", 22), ("msrp-REPORTTrans408Tx", 23), ("msrp-REPORTTrans413Tx", 24), ("msrp-REPORTTrans415Tx", 25), ("msrp-REPORTTrans423Tx", 26), ("msrp-REPORTTrans424Tx", 27), ("msrp-REPORTTrans425Tx", 28), ("msrp-REPORTTrans428Tx", 29), ("msrp-REPORTTrans481Tx", 30), ("msrp-REPORTTrans501Tx", 31), ("msrp-REPORTTrans506Tx", 32), ("msrp-AvgFailureREPORTMsgBytes400Tx", 33), ("msrp-AvgFailureREPORTMsgBytes401Tx", 34), ("msrp-AvgFailureREPORTMsgBytes403Tx", 35), ("msrp-AvgFailureREPORTMsgBytes404Tx", 36), ("msrp-AvgFailureREPORTMsgBytes408Tx", 37), ("msrp-AvgFailureREPORTMsgBytes413Tx", 38), ("msrp-AvgFailureREPORTMsgBytes415Tx", 39), ("msrp-AvgFailureREPORTMsgBytes423Tx", 40), ("msrp-AvgFailureREPORTMsgBytes424Tx", 41), ("msrp-AvgFailureREPORTMsgBytes425Tx", 42), ("msrp-AvgFailureREPORTMsgBytes428Tx", 43), ("msrp-AvgFailureREPORTMsgBytes481Tx", 44), ("msrp-AvgFailureREPORTMsgBytes501Tx", 45), ("msrp-AvgFailureREPORTMsgBytes506Tx", 46), ("msrp-TransResponsesTx", 47), ("msrp-SuccessTransResponsesTx", 48), ("msrp-TransResp400Tx", 49), ("msrp-TransResp401Tx", 50), ("msrp-TransResp403Tx", 51), ("msrp-TransResp404Tx", 52), ("msrp-TransResp408Tx", 53), ("msrp-TransResp413Tx", 54), ("msrp-TransResp415Tx", 55), ("msrp-TransResp423Tx", 56), ("msrp-TransResp424Tx", 57), ("msrp-TransResp425Tx", 58), ("msrp-TransResp428Tx", 59), ("msrp-TransResp481Tx", 60), ("msrp-TransResp501Tx", 61), ("msrp-TransResp506Tx", 62), ("msrp-AvgSENDTransRx", 63), ("msrp-AvgChatSENDTransRx", 64), ("msrp-AvgIsTypingSENDTransRx", 65), ("msrp-AvgReceiptSENDTransRx", 66), ("msrp-AvgSENDMsgBytesRx", 67), ("msrp-AvgChatSENDMsgBytesRx", 68), ("msrp-AvgIsTypingSENDMsgBytesRx", 69), ("msrp-AvgReceiptSENDMsgBytesRx", 70), ("msrp-SENDMsgBytesRx", 71), ("msrp-ChatSENDMsgBytesRx", 72), ("msrp-IsTypingSENDMsgBytesRx", 73), ("msrp-ReceiptSENDMsgBytesRx", 74), ("msrp-SuccessREPORTTransRx", 75), ("msrp-FailureREPORTTransRx", 76), ("msrp-AvgSuccessREPORTMsgBytesRx", 77), ("msrp-AvgFailureREPORTMsgBytesRx", 78), ("msrp-AvgFailureREPORTRateRx", 79), ("msrp-AvgSuccessREPORTRateRx", 80), ("msrp-REPORTTrans400Rx", 81), ("msrp-REPORTTrans401Rx", 82), ("msrp-REPORTTrans403Rx", 83), ("msrp-REPORTTrans404Rx", 84), ("msrp-REPORTTrans408Rx", 85), ("msrp-REPORTTrans413Rx", 86), ("msrp-REPORTTrans415Rx", 87), ("msrp-REPORTTrans423Rx", 88), ("msrp-REPORTTrans424Rx", 89), ("msrp-REPORTTrans425Rx", 90), ("msrp-REPORTTrans428Rx", 91), ("msrp-REPORTTrans481Rx", 92), ("msrp-REPORTTrans501Rx", 93), ("msrp-REPORTTrans506Rx", 94), ("msrp-AvgFailureREPORTMsgBytes400Rx", 95), ("msrp-AvgFailureREPORTMsgBytes401Rx", 96), ("msrp-AvgFailureREPORTMsgBytes403Rx", 97), ("msrp-AvgFailureREPORTMsgBytes404Rx", 98), ("msrp-AvgFailureREPORTMsgBytes408Rx", 99), ("msrp-AvgFailureREPORTMsgBytes413Rx", 100), ("msrp-AvgFailureREPORTMsgBytes415Rx", 101), ("msrp-AvgFailureREPORTMsgBytes423Rx", 102), ("msrp-AvgFailureREPORTMsgBytes424Rx", 103), ("msrp-AvgFailureREPORTMsgBytes425Rx", 104), ("msrp-AvgFailureREPORTMsgBytes428Rx", 105), ("msrp-AvgFailureREPORTMsgBytes481Rx", 106), ("msrp-AvgFailureREPORTMsgBytes501Rx", 107), ("msrp-AvgFailureREPORTMsgBytes506Rx", 108), ("msrp-TransResponsesRx", 109), ("msrp-SuccessTransResponsesRx", 110), ("msrp-TransResp400Rx", 111), ("msrp-TransResp401Rx", 112), ("msrp-TransResp403Rx", 113), ("msrp-TransResp404Rx", 114), ("msrp-TransResp408Rx", 115), ("msrp-TransResp413Rx", 116), ("msrp-TransResp415Rx", 117), ("msrp-TransResp423Rx", 118), ("msrp-TransResp424Rx", 119), ("msrp-TransResp425Rx", 120), ("msrp-TransResp428Rx", 121), ("msrp-TransResp481Rx", 122), ("msrp-TransResp501Rx", 123), ("msrp-TransResp506Rx", 124), ("msrp-ApMsrpKpiStatsTypeMax", 125))

class ApNSEPRealmRvalueDNIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(10, 11, 12, 13, 14, 20, 21, 22, 23, 24, 30, 31, 32, 33, 34, 40, 41, 42, 43, 44, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 81, 82, 83, 84, 85, 91, 92, 93, 94, 95, 96, 100))
    namedValues = NamedValues(("ets0", 10), ("ets1", 11), ("ets2", 12), ("ets3", 13), ("ets4", 14), ("wps0", 20), ("wps1", 21), ("wps2", 22), ("wps3", 23), ("wps4", 24), ("q7350", 30), ("q7351", 31), ("q7352", 32), ("q7353", 33), ("q7354", 34), ("esnet0", 40), ("esnet1", 41), ("esnet2", 42), ("esnet3", 43), ("esnet4", 44), ("wps0ets0", 50), ("wps0ets1", 51), ("wps0ets2", 52), ("wps0ets3", 53), ("wps0ets4", 54), ("wps1ets0", 55), ("wps1ets1", 56), ("wps1ets2", 57), ("wps1ets3", 58), ("wps1ets4", 59), ("wps2ets0", 60), ("wps2ets1", 61), ("wps2ets2", 62), ("wps2ets3", 63), ("wps2ets4", 64), ("wps3ets0", 65), ("wps3ets1", 66), ("wps3ets2", 67), ("wps3ets3", 68), ("wps3ets4", 69), ("wps4ets0", 70), ("wps4ets1", 71), ("wps4ets2", 72), ("wps4ets3", 73), ("wps4ets4", 74), ("dsnroutine", 81), ("dsnpriority", 82), ("dsnimmediate", 83), ("dsnflash", 84), ("dsnflashoverride", 85), ("drsnroutine", 91), ("drsnpriority", 92), ("drsnimmediate", 93), ("drsnflash", 94), ("drsnflashoverride", 95), ("drsnflashoverrideoverride", 96), ("dialedNumbers", 100))

class ApNSEPRealmStatsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("inboundactivesessions", 1), ("inboundtotalsessions", 2), ("inboundhighsessions", 3), ("inboundtotalrejectedsessions", 4), ("outboundactivesessions", 5), ("outboundtotalsessions", 6), ("outboundhighsessions", 7), ("outboundtotalrejectedsessions", 8))

mibBuilder.exportSymbols("ACMEPACKET-TC", ApAclType=ApAclType, ApCommMonitorState=ApCommMonitorState, ApCounterStatsType=ApCounterStatsType, ApDiamResultCode=ApDiamResultCode, ApDosThresholdCrossState=ApDosThresholdCrossState, ApDosThresholdTrafficType=ApDosThresholdTrafficType, ApHardwareModuleFamily=ApHardwareModuleFamily, ApMsrpKpiStatsCounterType=ApMsrpKpiStatsCounterType, ApMsrpKpiStatsType=ApMsrpKpiStatsType, ApNSEPRealmRvalueDNIndex=ApNSEPRealmRvalueDNIndex, ApNSEPRealmStatsType=ApNSEPRealmStatsType, ApPercentage=ApPercentage, ApPhyPortType=ApPhyPortType, ApPresence=ApPresence, ApRedundancyState=ApRedundancyState, ApServerStatus=ApServerStatus, ApSipMethod=ApSipMethod, ApStirStatsType=ApStirStatsType, ApThreadOverloaded=ApThreadOverloaded, ApTransportType=ApTransportType, PYSNMP_MODULE_ID=apTextualConventions, apTextualConventions=apTextualConventions)
