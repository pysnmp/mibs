#
# PySNMP MIB module TIMETRA-TC-MG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source TIMETRA-TC-MG-MIB
# Source digest sha256:4de63920911732ec9f93cf0df03e22daf148174c175e877503a7c852db7660fa
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
TNamedItem, TNamedItemOrEmpty, timetraTCMIBModule = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TNamedItem", "TNamedItemOrEmpty", "timetraTCMIBModule")
timetraTCMGMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 2, 1))
timetraTCMGMIBModule.setRevisions(('2017-01-01 00:00', '2013-11-08 00:00',))
if mibBuilder.loadTexts: timetraTCMGMIBModule.setLastUpdated('2017-01-01 00:00')
if mibBuilder.loadTexts: timetraTCMGMIBModule.setOrganization('Nokia')
class TmnxMobProfName(TNamedItem):
    status = 'current'

class TmnxMobProfNameOrEmpty(TNamedItemOrEmpty):
    status = 'current'

class TmnxMobProfIpTtl(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class TmnxMobProfMsgReTxTimeout(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 30)

class TmnxMobProfMsgReTxRetryCount(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TmnxMobProfKeepAliveTimeout(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 180), )
class TmnxMobProfKeepAliveRetryCount(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class TmnxMobProfKeepAliveResponse(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 20)

class TmnxMobProfKeepAliveInterval(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 180), )
class TmnxMobDiaTransTimer(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 180)

class TmnxMobDiaRetryCount(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 8)

class TmnxMobDiaPeerHost(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TmnxMobGwId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TmnxMobNode(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 30)

class TmnxMobBufferLimit(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 12000)

class TmnxMobQueueLimit(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 12000)

class TmnxMobRtrAdvtInterval(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 60)

class TmnxMobRtrAdvtLifeTime(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 24)

class TmnxMobAddrScheme(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stateful", 1), ("stateless", 2))

class TmnxMobQciValue(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 9)

class TmnxMobQciValueOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9)

class TmnxMobArpValue(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class TmnxMobArpValueOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class TmnxMobApn(DisplayString):
    reference = '3GPP TS 23.003 Section 9.1'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 100)

class TmnxMobApnOrZero(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 100)

class TmnxMobApnDomainName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 108)

class TmnxMobImsi(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobMsisdn(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 15)

class TmnxMobImei(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
class TmnxMobNai(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 72)

class TmnxMobMcc(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TmnxMobMnc(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(2, 2), ValueSizeConstraint(3, 3), )
class TmnxMobMccOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(3, 3), )
class TmnxMobMncOrEmpty(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), ValueSizeConstraint(3, 3), )
class TmnxMobUeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("idle", 1), ("active", 2), ("paging", 3), ("init", 4), ("suspend", 5), ("ddnDamp", 6))

class TmnxMobUeRat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("utran", 1), ("geran", 2), ("wlan", 3), ("gan", 4), ("hspa", 5), ("eutran", 6), ("ehrpd", 7), ("hrpd", 8), ("oneXrtt", 9), ("umb", 10))

class TmnxMobUeSubType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("homer", 1), ("roamer", 2), ("visitor", 3))

class TmnxMobPdnType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("ipv4v6", 3))

class TmnxMobPgwSigProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("gtp", 1), ("pmip", 2))

class TmnxMobPdnSessionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("invalid", 0), ("init", 1), ("waitPcrfResponse", 2), ("waitPgwResponse", 3), ("waitEnodebUpdate", 4), ("connected", 5), ("ulDelPending", 6), ("dlDelPending", 7), ("idleMode", 8), ("pageMode", 9), ("dlHandover", 10), ("incomingHandover", 11), ("outgoingHandover", 12), ("stateMax", 13))

class TmnxMobPdnSessionEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("sessionInvalid", 0), ("gtpCreateSessReq", 1), ("gtpUpdateBearerReq", 2), ("gtpDeleteSessReq", 3), ("gtpDeleteBearerResp", 4), ("gtpUpdateBearerResp", 5), ("gtpModifyActiveToIdle", 6), ("gtpResrcAllocCmd", 7), ("gtpModifyQosCmd", 8), ("gtpX1eNodeBTeidUpdate", 9), ("gtpX2SrcSgwDeleteSessReq", 10), ("gtpS1CreateIndirectTunnel", 11), ("dlPktRecvIndication", 12), ("dlPktNotificationAck", 13), ("dlPktNotificationFail", 14), ("pcrfSessEstResp", 15), ("pcrfSessTerminateRsp", 16), ("pcrfProvQosRules", 17), ("pmipSessResp", 18), ("pmipSessUpdate", 19), ("pmipSessDeleteRsp", 20), ("pmipSessDeleteReq", 21), ("eventMax", 22))

class TmnxMobBearerId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class TmnxMobBearerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("dedicated", 2))

class TmnxMobQci(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9)

class TmnxMobArp(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class TmnxMobSdf(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxMobSdfFilter(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxMobSdfFilterNum(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxMobSdfRuleName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 64)

class TmnxMobSdfFilterDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("preRel7", 0), ("downLink", 1), ("upLink", 2), ("biDir", 3))

class TmnxMobSdfFilterProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140))
    namedValues = NamedValues(("any", -1), ("ipv6HopByOpOpt", 0), ("icmp", 1), ("igmp", 2), ("ggp", 3), ("ip", 4), ("st", 5), ("tcp", 6), ("cbt", 7), ("egp", 8), ("igp", 9), ("bbnRccMon", 10), ("nvp2", 11), ("pup", 12), ("argus", 13), ("emcon", 14), ("xnet", 15), ("chaos", 16), ("udp", 17), ("mux", 18), ("dcnMeas", 19), ("hmp", 20), ("prm", 21), ("xnsIdp", 22), ("trunk1", 23), ("trunk2", 24), ("leaf1", 25), ("leaf2", 26), ("rdp", 27), ("irdp", 28), ("isoTp4", 29), ("netblt", 30), ("mfeNsp", 31), ("meritInp", 32), ("dccp", 33), ("pc3", 34), ("idpr", 35), ("xtp", 36), ("ddp", 37), ("idprCmtp", 38), ("tpplusplus", 39), ("il", 40), ("ipv6", 41), ("sdrp", 42), ("ipv6Route", 43), ("ipv6Frag", 44), ("idrp", 45), ("rsvp", 46), ("gre", 47), ("dsr", 48), ("bna", 49), ("esp", 50), ("ah", 51), ("iNlsp", 52), ("swipe", 53), ("narp", 54), ("mobile", 55), ("tlsp", 56), ("skip", 57), ("ipv6Icmp", 58), ("ipv6NoNxt", 59), ("ipv6Opts", 60), ("anyHostIntl", 61), ("cftp", 62), ("anyLocalNet", 63), ("satExpak", 64), ("kryptolan", 65), ("rvd", 66), ("ippc", 67), ("anyDFS", 68), ("satMon", 69), ("visa", 70), ("ipcv", 71), ("cpnx", 72), ("cphb", 73), ("wsn", 74), ("pvp", 75), ("brSatMon", 76), ("sunNd", 77), ("wbMon", 78), ("wbExpak", 79), ("isoIp", 80), ("vmtp", 81), ("secureVmpt", 82), ("vines", 83), ("ttp", 84), ("nsfnetIgp", 85), ("dgp", 86), ("tcf", 87), ("eiGrp", 88), ("ospfIgp", 89), ("spriteRpc", 90), ("larp", 91), ("mtp", 92), ("ax25", 93), ("ipip", 94), ("micp", 95), ("sccSp", 96), ("etherIp", 97), ("encap", 98), ("anyPEC", 99), ("gmtp", 100), ("ifmp", 101), ("pnni", 102), ("pim", 103), ("aris", 104), ("scps", 105), ("qnx", 106), ("activeNet", 107), ("ipComp", 108), ("snp", 109), ("compaqPeer", 110), ("ipxInIp", 111), ("vrrp", 112), ("pgm", 113), ("any0hop", 114), ("l2tp", 115), ("ddx", 116), ("iatp", 117), ("stp", 118), ("srp", 119), ("uti", 120), ("smp", 121), ("sm", 122), ("ptp", 123), ("isis", 124), ("fire", 125), ("crtp", 126), ("crudp", 127), ("sscopmce", 128), ("iplt", 129), ("sps", 130), ("pipe", 131), ("sctp", 132), ("fc", 133), ("rsvpE2eIgnore", 134), ("mobHeader", 135), ("udpLite", 136), ("mplsInIp", 137), ("manet", 138), ("hip", 139), ("shim6", 140))

class TmnxMobPathMgmtState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("disabled", 0), ("up", 1), ("reqTimeOut", 2), ("fault", 3), ("idle", 4), ("restart", 5))

class TmnxMobDiaPathMgmtState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("shutDown", 0), ("shuttingDown", 1), ("inactive", 2), ("active", 3))

class TmnxMobDiaDetailPathMgmtState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("error", 0), ("idle", 1), ("closed", 2), ("localShutdown", 3), ("remoteClosing", 4), ("waitConnAck", 5), ("waitCea", 6), ("open", 7), ("openCoolingDown", 8), ("waitDns", 9))

class TmnxMobGwType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sgw", 1), ("pgw", 2), ("wlanGw", 3))

class TmnxMobChargingProfile(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxMobChargingProfileOrInherit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TmnxMobAuthType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("radius", 1), ("diameter", 2))

class TmnxMobAuthUserName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("imsi", 1), ("msisdn", 2), ("pco", 3))

class TmnxMobProfGbrRate(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000)

class TmnxMobProfMbrRate(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000)

class TmnxMobPeerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sgw", 1), ("pgw", 2), ("hsgw", 3))

class TmnxMobRfAcctLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pdnLevel", 1), ("qciLevel", 2))

class TmnxMobProfPolReportingLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("servId", 1), ("ratingGrp", 2))

class TmnxMobProfPolChargingMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("profChargingMtd", 0), ("online", 1), ("offline", 2), ("both", 3))

class TmnxMobProfPolMeteringMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("timeBased", 1), ("volBased", 2), ("both", 3))

class TmnxMobServerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2))

class TmnxMobChargingBearerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("home", 1), ("visiting", 2), ("roaming", 3))

class TmnxMobChargingLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pdn", 1), ("bearer", 2))

class TmnxMobIpCanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("epc3gpp", 1), ("gprs3gpp", 2))

class TmnxMobStaticPolPrecedence(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65536)

class TmnxMobStaticPolPrecedenceOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxMobDualStackPref(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("useCplane", 3))

class TmnxMobDfPeerId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class TmnxMobLiTarget(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobLiTargetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("imsi", 1), ("msisdn", 2), ("imei", 3))

class TmnxMobUeId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobUeIdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("imsi", 0), ("imei", 1), ("msisdn", 2))

class TmnxMobImsiStr(DisplayString):
    reference = '3GPP TS 23.003 Numbering, addressing and identification, section 2.2 Composition of IMSI.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(9, 15), )
class TmnxMobRatingGrpState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("allowFlow", 1), ("disallowFlow", 2), ("redWebPortal", 3), ("allowResRules", 4), ("iom1stPktTrigger", 5), ("dis1stPktTrigger", 6), ("creditsToppedUp", 7), ("waitForFpt", 8))

class TmnxMobPresenceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("absent", 0), ("present", 1))

class TmnxMobPdnGyChrgTriggerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))
    namedValues = NamedValues(("sgsnIpAddrRecvd", 0), ("qosRecvd", 1), ("locRecvd", 2), ("ratRecvd", 3), ("qosTrfClsRecvd", 4), ("qosRlbClsRecvd", 5), ("qosDlyClsRecvd", 6), ("qosPeakThrptRecvd", 7), ("qosPrcClsRecvd", 8), ("qosMeanTrptRecvd", 9), ("qosMxBtRtUplnkRecvd", 10), ("qosMxBtRtDllnkRecvd", 11), ("qosResBerRecvd", 12), ("qosSduErrRatRecvd", 13), ("qosTransDelayRecvd", 14), ("qosTrfHndPriRecvd", 15), ("qosGrtBtRtUplnkRecvd", 16), ("qosGrtBtRtDllnkRecvd", 17), ("locMccRecvd", 18), ("locMncRecvd", 19), ("locRacRecvd", 20), ("locLacRecvd", 21), ("locCellIdRecvd", 22), ("medCompRecvd", 23), ("partcNmbRecvd", 24), ("thrldPartcNmbRecvd", 25), ("usrPartcTypeRecvd", 26), ("servCondRecvd", 27), ("servNodeRecvd", 28), ("usrCsgInfoRecvd", 29))

class TmnxMobPdnRefPointType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("s5", 1), ("s8", 2), ("gn", 3), ("s2a", 4), ("gp", 5))

class TmnxMobService(DisplayString):
    reference = '3GPP TS 23.003 Section 19.4.3'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TmnxMobServRefPointType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("s5", 1), ("s8", 2), ("s2a", 4))

class TmnxMobAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("eps", 1), ("gprs", 2), ("non3gpp", 3))

class TmnxMobUeStrPrefix(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(4, 15)

mibBuilder.exportSymbols("TIMETRA-TC-MG-MIB", PYSNMP_MODULE_ID=timetraTCMGMIBModule, TmnxMobAccessType=TmnxMobAccessType, TmnxMobAddrScheme=TmnxMobAddrScheme, TmnxMobApn=TmnxMobApn, TmnxMobApnDomainName=TmnxMobApnDomainName, TmnxMobApnOrZero=TmnxMobApnOrZero, TmnxMobArp=TmnxMobArp, TmnxMobArpValue=TmnxMobArpValue, TmnxMobArpValueOrZero=TmnxMobArpValueOrZero, TmnxMobAuthType=TmnxMobAuthType, TmnxMobAuthUserName=TmnxMobAuthUserName, TmnxMobBearerId=TmnxMobBearerId, TmnxMobBearerType=TmnxMobBearerType, TmnxMobBufferLimit=TmnxMobBufferLimit, TmnxMobChargingBearerType=TmnxMobChargingBearerType, TmnxMobChargingLevel=TmnxMobChargingLevel, TmnxMobChargingProfile=TmnxMobChargingProfile, TmnxMobChargingProfileOrInherit=TmnxMobChargingProfileOrInherit, TmnxMobDfPeerId=TmnxMobDfPeerId, TmnxMobDiaDetailPathMgmtState=TmnxMobDiaDetailPathMgmtState, TmnxMobDiaPathMgmtState=TmnxMobDiaPathMgmtState, TmnxMobDiaPeerHost=TmnxMobDiaPeerHost, TmnxMobDiaRetryCount=TmnxMobDiaRetryCount, TmnxMobDiaTransTimer=TmnxMobDiaTransTimer, TmnxMobDualStackPref=TmnxMobDualStackPref, TmnxMobGwId=TmnxMobGwId, TmnxMobGwType=TmnxMobGwType, TmnxMobImei=TmnxMobImei, TmnxMobImsi=TmnxMobImsi, TmnxMobImsiStr=TmnxMobImsiStr, TmnxMobIpCanType=TmnxMobIpCanType, TmnxMobLiTarget=TmnxMobLiTarget, TmnxMobLiTargetType=TmnxMobLiTargetType, TmnxMobMcc=TmnxMobMcc, TmnxMobMccOrEmpty=TmnxMobMccOrEmpty, TmnxMobMnc=TmnxMobMnc, TmnxMobMncOrEmpty=TmnxMobMncOrEmpty, TmnxMobMsisdn=TmnxMobMsisdn, TmnxMobNai=TmnxMobNai, TmnxMobNode=TmnxMobNode, TmnxMobPathMgmtState=TmnxMobPathMgmtState, TmnxMobPdnGyChrgTriggerType=TmnxMobPdnGyChrgTriggerType, TmnxMobPdnRefPointType=TmnxMobPdnRefPointType, TmnxMobPdnSessionEvent=TmnxMobPdnSessionEvent, TmnxMobPdnSessionState=TmnxMobPdnSessionState, TmnxMobPdnType=TmnxMobPdnType, TmnxMobPeerType=TmnxMobPeerType, TmnxMobPgwSigProtocol=TmnxMobPgwSigProtocol, TmnxMobPresenceState=TmnxMobPresenceState, TmnxMobProfGbrRate=TmnxMobProfGbrRate, TmnxMobProfIpTtl=TmnxMobProfIpTtl, TmnxMobProfKeepAliveInterval=TmnxMobProfKeepAliveInterval, TmnxMobProfKeepAliveResponse=TmnxMobProfKeepAliveResponse, TmnxMobProfKeepAliveRetryCount=TmnxMobProfKeepAliveRetryCount, TmnxMobProfKeepAliveTimeout=TmnxMobProfKeepAliveTimeout, TmnxMobProfMbrRate=TmnxMobProfMbrRate, TmnxMobProfMsgReTxRetryCount=TmnxMobProfMsgReTxRetryCount, TmnxMobProfMsgReTxTimeout=TmnxMobProfMsgReTxTimeout, TmnxMobProfName=TmnxMobProfName, TmnxMobProfNameOrEmpty=TmnxMobProfNameOrEmpty, TmnxMobProfPolChargingMethod=TmnxMobProfPolChargingMethod, TmnxMobProfPolMeteringMethod=TmnxMobProfPolMeteringMethod, TmnxMobProfPolReportingLevel=TmnxMobProfPolReportingLevel, TmnxMobQci=TmnxMobQci, TmnxMobQciValue=TmnxMobQciValue, TmnxMobQciValueOrZero=TmnxMobQciValueOrZero, TmnxMobQueueLimit=TmnxMobQueueLimit, TmnxMobRatingGrpState=TmnxMobRatingGrpState, TmnxMobRfAcctLevel=TmnxMobRfAcctLevel, TmnxMobRtrAdvtInterval=TmnxMobRtrAdvtInterval, TmnxMobRtrAdvtLifeTime=TmnxMobRtrAdvtLifeTime, TmnxMobSdf=TmnxMobSdf, TmnxMobSdfFilter=TmnxMobSdfFilter, TmnxMobSdfFilterDirection=TmnxMobSdfFilterDirection, TmnxMobSdfFilterNum=TmnxMobSdfFilterNum, TmnxMobSdfFilterProtocol=TmnxMobSdfFilterProtocol, TmnxMobSdfRuleName=TmnxMobSdfRuleName, TmnxMobServRefPointType=TmnxMobServRefPointType, TmnxMobServerState=TmnxMobServerState, TmnxMobService=TmnxMobService, TmnxMobStaticPolPrecedence=TmnxMobStaticPolPrecedence, TmnxMobStaticPolPrecedenceOrZero=TmnxMobStaticPolPrecedenceOrZero, TmnxMobUeId=TmnxMobUeId, TmnxMobUeIdType=TmnxMobUeIdType, TmnxMobUeRat=TmnxMobUeRat, TmnxMobUeState=TmnxMobUeState, TmnxMobUeStrPrefix=TmnxMobUeStrPrefix, TmnxMobUeSubType=TmnxMobUeSubType, timetraTCMGMIBModule=timetraTCMGMIBModule)
