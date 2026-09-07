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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timetraTCMGMIBModule.setRevisionsDescriptions(('Rev 15.0               01 Jan 2017 00:00\n         15.0 release of the TIMETRA-TC-MG-MIB.', 'Rev 1.0                08 Nov 2013 00:00\n         1.0 Release of the TIMETRA-TC-MG-MIB.',))
if mibBuilder.loadTexts: timetraTCMGMIBModule.setLastUpdated('2017-01-01 00:00')
if mibBuilder.loadTexts: timetraTCMGMIBModule.setOrganization('Nokia')
if mibBuilder.loadTexts: timetraTCMGMIBModule.setContactInfo('Nokia SROS Support\n         Web: http://www.nokia.com')
if mibBuilder.loadTexts: timetraTCMGMIBModule.setDescription("This document is the SNMP MIB module for the SNMP Textual Conventions\n         (TCs) used in the Nokia SROS manageability instrumentation.\n\n         Copyright 2003-2018 Nokia. All rights reserved. Reproduction of this\n         document is authorized on the condition that the foregoing copyright\n         notice is included.\n\n         This SNMP MIB module (Specification) embodies Nokia's\n         proprietary intellectual property.  Nokia retains\n         all title and ownership in the Specification, including any\n         revisions.\n\n         Nokia grants all interested parties a non-exclusive license to use and\n         distribute an unmodified copy of this Specification in connection with\n         management of Nokia products, and without fee, provided this copyright\n         notice and license appear on all copies.\n\n         This Specification is supplied `as is', and Nokia makes no warranty,\n         either express or implied, as to the use, operation, condition, or\n         performance of the Specification.")
class TmnxMobProfName(TNamedItem):
    description = 'The data type TmnxMobProfName describes the name of a profile used by\n         mobile gateways.'
    status = 'current'

class TmnxMobProfNameOrEmpty(TNamedItemOrEmpty):
    description = 'The data type TmnxMobProfNameOrEmpty describes the name of a profile\n         used by mobile gateways.'
    status = 'current'

class TmnxMobProfIpTtl(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfIpTtl describes the Time-To-Live (TTL) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class TmnxMobProfMsgReTxTimeout(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfMsgReTxTimeout describes the message\n         retransmit timeout value in seconds.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 30)

class TmnxMobProfMsgReTxRetryCount(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfMsgReTxRetryCount describes the message\n         retransmit retry count value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TmnxMobProfKeepAliveTimeout(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfKeepAliveTimeout describes the keep-alive\n         timeout value in seconds.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 180), )
class TmnxMobProfKeepAliveRetryCount(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfKeepAliveRetryCount describes the keep-alive\n         retry count value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class TmnxMobProfKeepAliveResponse(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfKeepAliveResponse describes the keep-alive T3\n         response value in seconds.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 20)

class TmnxMobProfKeepAliveInterval(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfKeepAliveInterval describes the intervals\n         between heartbeat messages'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 180), )
class TmnxMobDiaTransTimer(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobDiaTransTimer describes the diameter peer\n         transaction timer value in seconds.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 180)

class TmnxMobDiaRetryCount(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobDiaRetryCount describes the diameter peer retry\n         count value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 8)

class TmnxMobDiaPeerHost(DisplayString):
    description = 'The data type TmnxMobDiaPeerHost describes the name of a destination\n         realm, originating realm and originating host.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TmnxMobGwId(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobGwId identifies mobile gateways.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TmnxMobNode(DisplayString):
    description = 'The data type TmnxMobNode describes the name of a mobile gateway which\n         consists of Mobile Country Code (MCC), Mobile Network Code (MNC),\n         Region string, Group Id, Node Id.\n\n         A mobile gateway name can be described as follows:\n\n         <MCC>.<MNC>.<SGW|PGW>.<Region String>.<Group Id>.<Node Id>\n\n         MCC : 3 digits (000-999)\n         MNC : 2 or 3 digits\n         Application Type : SGW or PGW (3 characters)\n         Region String : 10 characters\n         Group Id : 3 characters\n         Node Id : 3 characters'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 30)

class TmnxMobBufferLimit(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobBufferLimit describes the buffer limit in bytes.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 12000)

class TmnxMobQueueLimit(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobQueueLimit describes the queue limit in bytes.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 12000)

class TmnxMobRtrAdvtInterval(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobRtrAdvtInterval describes the router\n         advertisement interval in minutes.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 60)

class TmnxMobRtrAdvtLifeTime(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobRtrAdvtLifeTime describes the router\n         advertisement life time in hours.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 24)

class TmnxMobAddrScheme(TextualConvention, Integer32):
    description = "The data type TmnxMobAddrScheme describes the addressing scheme. If\n         the value is set to 'stateful', User Equipment (UE) uses DHCPv6 to get\n         IPv6 address. If the value is set to 'stateless', UE uses ICMPv6 to\n         get IPv6 address."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stateful", 1), ("stateless", 2))

class TmnxMobQciValue(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobQciValue describes the QoS Class Identifier (QCI)\n         value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 9)

class TmnxMobQciValueOrZero(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobQciValueOrZero describes the QoS Class Identifier\n         (QCI) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9)

class TmnxMobArpValue(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobArpValue describes the Allocation and Retention\n         Priority (ARP) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class TmnxMobArpValueOrZero(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobArpValueOrZero describes the Allocation and\n         Retention Priority (ARP) value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class TmnxMobApn(DisplayString):
    reference = '3GPP TS 23.003 Section 9.1'
    description = 'The data type TmnxMobApn describes the Access Point Name (APN)\n         associated with an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 100)

class TmnxMobApnOrZero(DisplayString):
    description = 'The data type TmnxMobApnOrZero describes the Access Point Name (APN)\n         associated with an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 100)

class TmnxMobApnDomainName(DisplayString):
    description = 'The data type TmnxMobApnDomainName holds a DNS Domain Name derived\n         from an Access Point Name (APN).\n\n         The maximum size is arbitrarily chosen in order to be large enough to\n         hold a Network Identifier of length 63, and small enough to be used as\n         index in a table.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 108)

class TmnxMobImsi(TextualConvention, OctetString):
    description = 'The data type TmnxMobImsi describes the International Mobile\n         Subscriber Identity (IMSI) of an User Equipment (UE).\n\n         IMSI is defined as a number consisting of up to 15 BCD digits. The\n         first 3 digits are the Mobile Country Code (MCC). The next 2 or 3\n         digits are the Mobile Network Code (MNC). The value of MCC determines\n         whether the MNC is 2 digits or 3 digits. The remaining digits are the\n         Mobile Subscriber Identification Number (MSIN). The internal\n         representation of the IMSI is as follows:\n\n         Bits 63-62 are reserved.\n\n         Bits 61-60 indicate the length of the MNC field: 10 indicates a\n         2-digit MNC while 11 indicates a 3-digit MNC.\n\n         Bits 59-0 hold the 15 IMSI BCD digits D1-15.\n\n         When the total number of digits in the IMSI is less than 15, the\n         nibble 0xf is used a filler.\n\n\n         IMSI encoding for a 2-digit MNC:\n\n         63          55         47          39                         0\n\n         +-----------+-----------+-----------+-------------------------+\n\n         | 0010| MCC1| MCC2| MCC3| MNC1| MNC2| MSIN (up to 10 digits)\n\n         +-----------+-----------+-----------+-------------------------+\n\n\n         IMSI encoding for a 3-digit MNC:\n\n         63          55         47          39     35                  0\n\n         +-----------+-----------+-----------+-------------------------+\n\n         | 0011| MCC1| MCC2| MCC3| MNC1| MNC2| MNC3| MSIN (up to 9 digits)\n\n         +-----------+-----------+-----------+-------------------------+\n\n         Bits 63-56 of the IMSI are carried in octet number 1 of the octet\n         string and bits 7-0 are carried in octet number 8 of the octet string.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobMsisdn(DisplayString):
    description = 'The data type TmnxMobMsisdn describes the Mobile Subscriber Integrated\n         Services Digital Network (MSISDN) number of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 15)

class TmnxMobImei(DisplayString):
    description = 'The data type TmnxMobImei describes the International Mobile Equipment\n         Identity (IMEI) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
class TmnxMobNai(DisplayString):
    description = 'The data type TmnxMobNai describes the Network Address Identifier\n         (NAI) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 72)

class TmnxMobMcc(DisplayString):
    description = 'The data type TmnxMobMcc describes the Mobile Country Code (MCC) of an\n         User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TmnxMobMnc(DisplayString):
    description = 'The data type TmnxMobMnc describes the Mobile Network Code (MNC) of an\n         User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(2, 2), ValueSizeConstraint(3, 3), )
class TmnxMobMccOrEmpty(DisplayString):
    description = 'The data type TmnxMobMccOrEmpty describes the Mobile Country Code\n         (MCC) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(3, 3), )
class TmnxMobMncOrEmpty(DisplayString):
    description = 'The data type TmnxMobMncOrEmpty describes the Mobile Network Code\n         (MNC) of an User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), ValueSizeConstraint(3, 3), )
class TmnxMobUeState(TextualConvention, Integer32):
    description = 'The data type TmnxMobUeState describes the state of an User Equipment\n         (UE).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("idle", 1), ("active", 2), ("paging", 3), ("init", 4), ("suspend", 5), ("ddnDamp", 6))

class TmnxMobUeRat(TextualConvention, Integer32):
    description = 'The data type TmnxMobUeRat describes the Radio Access Type (RAT) of an\n         User Equipment (UE).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("utran", 1), ("geran", 2), ("wlan", 3), ("gan", 4), ("hspa", 5), ("eutran", 6), ("ehrpd", 7), ("hrpd", 8), ("oneXrtt", 9), ("umb", 10))

class TmnxMobUeSubType(TextualConvention, Integer32):
    description = 'The data type TmnxMobUeSubType describes the subscription type of User\n         Equipment (UE).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("homer", 1), ("roamer", 2), ("visitor", 3))

class TmnxMobPdnType(TextualConvention, Integer32):
    description = 'The data type TmnxMobPdnType describes the type of a Packet Data\n         Network (PDN).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("ipv4v6", 3))

class TmnxMobPgwSigProtocol(TextualConvention, Integer32):
    description = 'The data type TmnxMobPgwSigProtocol describes the signaling protocol\n         used on S5 or S8 reference point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("gtp", 1), ("pmip", 2))

class TmnxMobPdnSessionState(TextualConvention, Integer32):
    description = 'The data type TmnxMobPdnSessionState describes the feedback signaling\n         message (FSM) state of a Packet Data Network (PDN) session.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("invalid", 0), ("init", 1), ("waitPcrfResponse", 2), ("waitPgwResponse", 3), ("waitEnodebUpdate", 4), ("connected", 5), ("ulDelPending", 6), ("dlDelPending", 7), ("idleMode", 8), ("pageMode", 9), ("dlHandover", 10), ("incomingHandover", 11), ("outgoingHandover", 12), ("stateMax", 13))

class TmnxMobPdnSessionEvent(TextualConvention, Integer32):
    description = 'The data type TmnxMobPdnSessionEvent describes the feedback signaling\n         message (FSM) event of a Packet Data Network (PDN) session.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("sessionInvalid", 0), ("gtpCreateSessReq", 1), ("gtpUpdateBearerReq", 2), ("gtpDeleteSessReq", 3), ("gtpDeleteBearerResp", 4), ("gtpUpdateBearerResp", 5), ("gtpModifyActiveToIdle", 6), ("gtpResrcAllocCmd", 7), ("gtpModifyQosCmd", 8), ("gtpX1eNodeBTeidUpdate", 9), ("gtpX2SrcSgwDeleteSessReq", 10), ("gtpS1CreateIndirectTunnel", 11), ("dlPktRecvIndication", 12), ("dlPktNotificationAck", 13), ("dlPktNotificationFail", 14), ("pcrfSessEstResp", 15), ("pcrfSessTerminateRsp", 16), ("pcrfProvQosRules", 17), ("pmipSessResp", 18), ("pmipSessUpdate", 19), ("pmipSessDeleteRsp", 20), ("pmipSessDeleteReq", 21), ("eventMax", 22))

class TmnxMobBearerId(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobBearerId describes the bearer identifier.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class TmnxMobBearerType(TextualConvention, Integer32):
    description = 'The data type TmnxMobBearerType describes the type of a bearer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("dedicated", 2))

class TmnxMobQci(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobQci describes the QoS Class Identifier.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9)

class TmnxMobArp(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobArp describes the QoS parameter, Allocation and\n         Retention Priority (ARP).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class TmnxMobSdf(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobSdf describes the number of Service Data Flows\n         (SDFs).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxMobSdfFilter(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobSdfFilter describes a IP filter in a Service Data\n         Flow (SDF) or Traffic Flow Template (TFT).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxMobSdfFilterNum(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobSdfFilterNum describes the number of IP filters.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxMobSdfRuleName(DisplayString):
    description = 'The data type TmnxMobSdfRuleName describes the policy rule name of a\n         Service Data Flow (SDF).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 64)

class TmnxMobSdfFilterDirection(TextualConvention, Integer32):
    description = 'The data type TmnxMobSdfFilterDirection describes the direction on\n         which a Service Data Flow (SDF) filter rule is valid.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("preRel7", 0), ("downLink", 1), ("upLink", 2), ("biDir", 3))

class TmnxMobSdfFilterProtocol(TextualConvention, Integer32):
    description = 'The data type TmnxMobSdfFilterProtocol describes IPv4 protocol or IPv6\n         next header on which Service Data Flow (SDF) filter matches.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140))
    namedValues = NamedValues(("any", -1), ("ipv6HopByOpOpt", 0), ("icmp", 1), ("igmp", 2), ("ggp", 3), ("ip", 4), ("st", 5), ("tcp", 6), ("cbt", 7), ("egp", 8), ("igp", 9), ("bbnRccMon", 10), ("nvp2", 11), ("pup", 12), ("argus", 13), ("emcon", 14), ("xnet", 15), ("chaos", 16), ("udp", 17), ("mux", 18), ("dcnMeas", 19), ("hmp", 20), ("prm", 21), ("xnsIdp", 22), ("trunk1", 23), ("trunk2", 24), ("leaf1", 25), ("leaf2", 26), ("rdp", 27), ("irdp", 28), ("isoTp4", 29), ("netblt", 30), ("mfeNsp", 31), ("meritInp", 32), ("dccp", 33), ("pc3", 34), ("idpr", 35), ("xtp", 36), ("ddp", 37), ("idprCmtp", 38), ("tpplusplus", 39), ("il", 40), ("ipv6", 41), ("sdrp", 42), ("ipv6Route", 43), ("ipv6Frag", 44), ("idrp", 45), ("rsvp", 46), ("gre", 47), ("dsr", 48), ("bna", 49), ("esp", 50), ("ah", 51), ("iNlsp", 52), ("swipe", 53), ("narp", 54), ("mobile", 55), ("tlsp", 56), ("skip", 57), ("ipv6Icmp", 58), ("ipv6NoNxt", 59), ("ipv6Opts", 60), ("anyHostIntl", 61), ("cftp", 62), ("anyLocalNet", 63), ("satExpak", 64), ("kryptolan", 65), ("rvd", 66), ("ippc", 67), ("anyDFS", 68), ("satMon", 69), ("visa", 70), ("ipcv", 71), ("cpnx", 72), ("cphb", 73), ("wsn", 74), ("pvp", 75), ("brSatMon", 76), ("sunNd", 77), ("wbMon", 78), ("wbExpak", 79), ("isoIp", 80), ("vmtp", 81), ("secureVmpt", 82), ("vines", 83), ("ttp", 84), ("nsfnetIgp", 85), ("dgp", 86), ("tcf", 87), ("eiGrp", 88), ("ospfIgp", 89), ("spriteRpc", 90), ("larp", 91), ("mtp", 92), ("ax25", 93), ("ipip", 94), ("micp", 95), ("sccSp", 96), ("etherIp", 97), ("encap", 98), ("anyPEC", 99), ("gmtp", 100), ("ifmp", 101), ("pnni", 102), ("pim", 103), ("aris", 104), ("scps", 105), ("qnx", 106), ("activeNet", 107), ("ipComp", 108), ("snp", 109), ("compaqPeer", 110), ("ipxInIp", 111), ("vrrp", 112), ("pgm", 113), ("any0hop", 114), ("l2tp", 115), ("ddx", 116), ("iatp", 117), ("stp", 118), ("srp", 119), ("uti", 120), ("smp", 121), ("sm", 122), ("ptp", 123), ("isis", 124), ("fire", 125), ("crtp", 126), ("crudp", 127), ("sscopmce", 128), ("iplt", 129), ("sps", 130), ("pipe", 131), ("sctp", 132), ("fc", 133), ("rsvpE2eIgnore", 134), ("mobHeader", 135), ("udpLite", 136), ("mplsInIp", 137), ("manet", 138), ("hip", 139), ("shim6", 140))

class TmnxMobPathMgmtState(TextualConvention, Integer32):
    description = "The data type TmnxMobPathMgmtState describes the state of a path for a\n         reference point. A value of 'reqTimeOut' indicates that the peer is\n         not replying to the Echo Request messages the SGW is sending out."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("disabled", 0), ("up", 1), ("reqTimeOut", 2), ("fault", 3), ("idle", 4), ("restart", 5))

class TmnxMobDiaPathMgmtState(TextualConvention, Integer32):
    description = 'The data type TmnxMobDiaPathMgmtState describes the state of a path\n         for a diameter connection.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("shutDown", 0), ("shuttingDown", 1), ("inactive", 2), ("active", 3))

class TmnxMobDiaDetailPathMgmtState(TextualConvention, Integer32):
    description = 'The data type TmnxMobDiaDetailPathMgmtState describes the detail state\n         of a path for a diameter connection.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("error", 0), ("idle", 1), ("closed", 2), ("localShutdown", 3), ("remoteClosing", 4), ("waitConnAck", 5), ("waitCea", 6), ("open", 7), ("openCoolingDown", 8), ("waitDns", 9))

class TmnxMobGwType(TextualConvention, Integer32):
    description = 'The data type TmnxMobGwType describes the mobile gateway type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sgw", 1), ("pgw", 2), ("wlanGw", 3))

class TmnxMobChargingProfile(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobChargingProfile describes the charging trigger\n         rules applied for generating Charging Data Records (CDR) for\n         subscribers.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxMobChargingProfileOrInherit(TextualConvention, Integer32):
    description = "The data type TmnxMobChargingProfileOrInherit describes the charging\n         trigger rules applied for generating Charging Data Records (CDR) for\n         subscribers. A value of '-1' indicates that identifier will be\n         inherited from another object that is usually in another mib table."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TmnxMobAuthType(TextualConvention, Integer32):
    description = 'The data type TmnxMobAuthType describes the authentication type used\n         by mobile gateways.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("radius", 1), ("diameter", 2))

class TmnxMobAuthUserName(TextualConvention, Integer32):
    description = 'The data type TmnxMobAuthUserName describes the user name used in\n         authentication requests by mobile gateways.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("imsi", 1), ("msisdn", 2), ("pco", 3))

class TmnxMobProfGbrRate(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfGbrRate describes the Guaranteed Bit Rate\n         (GBR) value in kilobits per second(kbps).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000)

class TmnxMobProfMbrRate(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobProfMbrRate describes the Maximum Bit Rate (MBR)\n         value in kilobits per second(kbps).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000)

class TmnxMobPeerType(TextualConvention, Integer32):
    description = 'The data type TmnxMobPeerType describes the type of the mobile gateway\n         peer as Serving Gateway (SGW), Packet Data Network Gateway (PGW) or\n         High Rate Packet Data (HRPD) Serving Gateway (HSGW).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sgw", 1), ("pgw", 2), ("hsgw", 3))

class TmnxMobRfAcctLevel(TextualConvention, Integer32):
    description = 'TmnxMobRfAcctLevel data type is an enumerated integer that describes\n         the accounting level.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pdnLevel", 1), ("qciLevel", 2))

class TmnxMobProfPolReportingLevel(TextualConvention, Integer32):
    description = 'TmnxMobProfPolReportingLevel data type is an enumerated integer that\n         describes the Reporting level for the Policy and Charging Control\n         (PCC) rule.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("servId", 1), ("ratingGrp", 2))

class TmnxMobProfPolChargingMethod(TextualConvention, Integer32):
    description = "TmnxMobProfPolChargingMethod data type is an enumerated integer that\n         describes the Charging Method for the Policy and Charging Control\n         (PCC) rule. A variable of this type could be set to 'online' charging\n         method, 'offline' charging method or 'both'.\n\n         If the variable is set to 'profChargingMtd' the charging method is set\n         to 'offline' if 'tmnxMobProfPgwChrgOffLineState' is set to 'enabled',\n         the charging method is set to 'online' if 'tmnxMobProfPgwChrgGyState'\n         is set to 'enabled' and the charging method is set to 'both' if both\n         'tmnxMobProfPgwChrgOffLineState' and 'tmnxMobProfPgwChrgGyState' are\n         set to 'enabled'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("profChargingMtd", 0), ("online", 1), ("offline", 2), ("both", 3))

class TmnxMobProfPolMeteringMethod(TextualConvention, Integer32):
    description = 'TmnxMobProfPolMeteringMethod data type is an enumerated integer that\n         describes the Metering Method for the Policy and Charging Control\n         (PCC) rule.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("timeBased", 1), ("volBased", 2), ("both", 3))

class TmnxMobServerState(TextualConvention, Integer32):
    description = 'The data type TmnxMobServerState describes the state of a server\n         connected with a mobile gateway.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2))

class TmnxMobChargingBearerType(TextualConvention, Integer32):
    description = 'The data type TmnxMobChargingBearerType describes the type of a bearer\n         context used in charging applications.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("home", 1), ("visiting", 2), ("roaming", 3))

class TmnxMobChargingLevel(TextualConvention, Integer32):
    description = 'The data type TmnxMobChargingLevel describes the level where the\n         charging is done.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pdn", 1), ("bearer", 2))

class TmnxMobIpCanType(TextualConvention, Integer32):
    description = 'The data type TmnxMobIpCanType describes the type of Internet Protocol\n         Connectivity Access Network (IP-CAN) session as Evolved Packet Core\n         (epc3gpp) or GPRS (gprs3gpp).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("epc3gpp", 1), ("gprs3gpp", 2))

class TmnxMobStaticPolPrecedence(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobStaticPolPrecedence describes the precedence\n         value for a static policy configured in the system.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65536)

class TmnxMobStaticPolPrecedenceOrZero(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobStaticPolPrecedence describes the precedence\n         value for a static policy configured in the system.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxMobDualStackPref(TextualConvention, Integer32):
    description = "The data type TmnxMobDualStackPref describes the preference in a dual\n         IP stack.\n\n         The value 'useCplane' specifies that the value is inherited from the\n         preference in a dual IP stack on control plane."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("useCplane", 3))

class TmnxMobDfPeerId(TextualConvention, Unsigned32):
    description = 'The data type TmnxMobDfPeerId identifies Delivery Function (DF) peer\n         for the mobile gateways.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class TmnxMobLiTarget(TextualConvention, OctetString):
    description = 'The data type TmnxMobLiTarget describes the target for the\n         interception.\n\n         The target can be of type International Mobile Subscriber Identity\n         (IMSI), Mobile Subscriber Integrated Services Digital Network (MSISDN)\n         or International Mobile Equipment Identity (IMEI).\n\n         IMSI is defined as a number consisting of up to 15 BCD digits. The\n         first 3 digits are the Mobile Country Code (MCC). The next 2 or 3\n         digits are the Mobile Network Code (MNC). The value of MCC determines\n         whether the MNC is 2 digits or 3 digits. The remaining digits are the\n         Mobile Subscriber Identification Number (MSIN). The internal\n         representation of the IMSI is as follows:\n\n         Bits 63-62 are reserved.\n\n         Bits 61-60 indicate the length of the MNC field: 10 indicates a\n         2-digit MNC while 11 indicates a 3-digit MNC.\n\n         Bits 59-0 hold the 15 IMSI BCD digits D1-15.\n\n         When the total number of digits in the IMSI is less than 15, the\n         nibble 0xf is used a filler.\n\n         IMSI encoding for a 2-digit MNC:\n\n         63          55         47          39                         0\n\n         +-----------+-----------+-----------+-------------------------+\n\n         | 0010| MCC1| MCC2| MCC3| MNC1| MNC2| MSIN (up to 10 digits)\n\n         +-----------+-----------+-----------+-------------------------+\n\n\n         IMSI encoding for a 3-digit MNC:\n\n         63          55         47          39     35                  0\n\n         +-----------+-----------+-----------+-------------------------+\n\n         | 0011| MCC1| MCC2| MCC3| MNC1| MNC2| MNC3| MSIN (up to 9 digits)\n\n         +-----------+-----------+-----------+-------------------------+\n\n         Bits 63-56 of the IMSI are carried in octet number 1 of the octet\n         string and bits 7-0 are carried in octet number 8 of the octet string.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobLiTargetType(TextualConvention, Integer32):
    description = 'The data type TmnxMobLiTargetType describes the types of target in\n         Lawful Interception (LI).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("imsi", 1), ("msisdn", 2), ("imei", 3))

class TmnxMobUeId(TextualConvention, OctetString):
    description = 'The data type TmnxMobUeId describes the identity of an User Equipment.\n         TmnxMobUeId can be of the following types: International Mobile\n         Subscriber Identity (IMSI), International Mobile station Equipment\n         Identity (IMEI), Mobile Subscriber Integrated Services Digital network\n         Number (MSISDN). IMSI, IMEI, MSISDN are defined in 3GPP TS 23.003.\n\n         IMSI is defined as a number consisting of up to 15 BCD digits. The\n         first 3 digits are the Mobile Country Code (MCC). The next 2 or 3\n         digits are the Mobile Network Code (MNC). The value of MCC determines\n         whether the MNC is 2 digits or 3 digits. The remaining digits are the\n         Mobile Subscriber Identification Number (MSIN).\n\n         IMEI is defined as a number consisting of up to 16 BCD digits. The\n         first 8 digits consists of Type Allocation Code (TAC). The next 6\n         digits consist of Serial Number (SNR) which could be followed by a\n         Check Digit (CD) or Spare Digit (SD) of size 1 digit or by a Software\n         Version Number (SVN) of size 2 digits.\n\n         MSISDN is defined as a number consisting of 9 to 15 BCD digits. MSISDN\n         consists of Country Code (CC) followed by National Destination Code\n         (NDC) and Subscriber Number (SN).\n\n         Bits 63-56 of the IMSI or IMEI or MSISDN are carried in octet number 1\n         of the octet string and bits 7-0 are carried in octet number 8 of the\n         octet string.\n\n         The internal representation of the IMSI is as follows:\n\n         Bits 63-62 are reserved.\n\n         Bits 61-60 indicate the length of the MNC field: 10 indicates a\n         2-digit MNC while 11 indicates a 3-digit MNC.\n\n         Bits 59-0 hold the 15 IMSI BCD digits D1-15.\n\n         When the total number of digits in the IMSI is less than 15, the\n         nibble 0xf is used a filler.\n\n         IMSI encoding for a 2-digit MNC:\n\n\n         63          55         47          39                         0\n\n         +-----------+-----------+-----------+-------------------------+\n\n         | 0010| MCC1| MCC2| MCC3| MNC1| MNC2| MSIN (up to 10 digits)\n\n         +-----------+-----------+-----------+-------------------------+\n\n\n         IMSI encoding for a 3-digit MNC:\n\n\n         63          55         47          39     35                  0\n\n         +-----------+-----------+-----------+-------------------------+\n\n         | 0011| MCC1| MCC2| MCC3| MNC1| MNC2| MNC3| MSIN (up to 9 digits)\n\n         +-----------+-----------+-----------+-------------------------+\n\n\n         The internal representation of the IMEI and MSISDN is as follows:\n\n         IMEI encoding:\n\n\n         63          55         31                      7       0\n\n         +-----------+-----------+----------------------+-------+\n\n         |          TAC          |         SNR          |  SNV  |\n         |N2|N1|N4|N3|N6|N5|N8|N7|N10|N9|N12|N11|N14|N13|N16|N15|\n\n         +-----------+-----------+-----------+------------------+\n\n\n         MSISDN encoding:\n\n         63          55         31                      7       0\n\n         +-----------+-----------+----------------------+-------+\n\n         |   CC   |   NDC  |                  SN                |\n         |N2|N1|N4|N3|N6|N5|N8|N7|N10|N9|N12|N11|N14|N13|N16|N15|\n\n         +-----------+-----------+-----------+------------------+\n\n         When the total number of digits in the IMEI or MSISDN is less than 15,\n         the nibble 0x0 is used a filler.\n\n         In each byte both nibbles are swapped and it is stored as shown in the\n         above format. For example, in the format N3 & N4 present the nibble\n         number 3 and 4 respectively and they are stored in reverse order.\n\n         When the total number of digits are odd in IMEI and MSISDB, the last\n         digit will be paired with nibble 0xf.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxMobUeIdType(TextualConvention, Integer32):
    description = 'The data type TmnxMobUeIdType describes the types of identification\n         for User Equipment (UE).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("imsi", 0), ("imei", 1), ("msisdn", 2))

class TmnxMobImsiStr(DisplayString):
    reference = '3GPP TS 23.003 Numbering, addressing and identification,\n         section 2.2 Composition of IMSI.'
    description = 'The data type TmnxMobImsiStr describes the International Mobile\n         Subscriber Identity (IMSI) of a User Equipment (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(9, 15), )
class TmnxMobRatingGrpState(TextualConvention, Integer32):
    description = 'The data type TmnxMobRatingGrpState describes the state of a rating\n         group.\n\n         allowFlow - Allow the traffic to flow disallowFlow - Disallow the\n         traffic to Flow redWebPortal - Redirect the traffic to web portal\n         allowResRules - Allow restricted rules iom1stPktTrigger - Get the\n         trigger from on IOM on arrival of 1st packet dis1stPktTrigger -\n         Disable 1st packet trigger and allow the traffic creditsToppedUp -\n         Credits topped up waitForFpt - Unblocked and waiting for First Packet\n         Trigger (FPT)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("allowFlow", 1), ("disallowFlow", 2), ("redWebPortal", 3), ("allowResRules", 4), ("iom1stPktTrigger", 5), ("dis1stPktTrigger", 6), ("creditsToppedUp", 7), ("waitForFpt", 8))

class TmnxMobPresenceState(TextualConvention, Integer32):
    description = 'The data type TmnxMobPresenceState describes the whether the given\n         field is present.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("absent", 0), ("present", 1))

class TmnxMobPdnGyChrgTriggerType(TextualConvention, Integer32):
    description = "The data type TmnxMobPdnGyChrgTriggerType describes type of the\n         trigger activated by the Online Charging System (OCS).\n\n         sgsnIpAddrRecvd       - Change in Serving GPRS Support Node (SGSN) IP\n                                 address\n         qosRecvd              - Change in Quality of Service (QoS)\n         locRecvd              - Location Change\n         ratRecvd              - Router Advertisement Trigger (RAT) Change\n         qosTrfClsRecvd        - Change in QoS Traffic class\n         qosRlbClsRecvd        - Change in QoS Reliability class\n         qosDlyClsRecvd        - Change in QoS Delay class\n         qosPeakThrptRecvd     - Change in QoS Peak Throughput\n         qosPrcClsRecvd        - Change in QoS Precedence class\n         qosMeanTrptRecvd      - Change in QoS Mean Throughput\n         qosMxBtRtUplnkRecvd   - Change in QoS MBR for Uplink\n         qosMxBtRtDllnkRecvd   - Change in QoS MBR for Downlink\n         qosResBerRecvd        - Change in QoS Residual Bit Error Rate (BER)\n         qosSduErrRatRecvd     - Change in QoS Service Data Unit (SDU) Error\n                                 Ratio class\n         qosTransDelayRecvd    - Change in QoS Transfer Delay\n         qosTrfHndPriRecvd     - Change in QoS Traffic Handling Priority\n         qosGrtBtRtUplnkRecvd  - Change in QoS Guaranteed Bit Rate (GBR) for\n                                 Uplink\n         qosGrtBtRtDllnkRecvd  - Change in QoS GBR for Downlink\n         locMccRecvd           - Change in Location Mobile Country Code (MCC)\n         locMncRecvd           - Change in Location Mobile Network Code (MNC)\n         locRacRecvd           - Change in Location Routing Area Code (RAC)\n         locLacRecvd           - Change in Location Location Area Code (LAC)\n         locCellIdRecvd        - Change in Location Cell ID\n         medCompRecvd          - Change in Media Composition\n         partcNmbRecvd         - Change in Participants' number\n         thrldPartcNmbRecvd    - Change in Threshold of Participants' number\n         usrPartcTypeRecvd     - Change in User Participating Type\n         servCondRecvd         - Change in Service Condition\n         servNodeRecvd         - Change in Service Node\n         usrCsgInfoRecvd       - Change in User Closed Subscription Group (CSG)\n                                 Information"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))
    namedValues = NamedValues(("sgsnIpAddrRecvd", 0), ("qosRecvd", 1), ("locRecvd", 2), ("ratRecvd", 3), ("qosTrfClsRecvd", 4), ("qosRlbClsRecvd", 5), ("qosDlyClsRecvd", 6), ("qosPeakThrptRecvd", 7), ("qosPrcClsRecvd", 8), ("qosMeanTrptRecvd", 9), ("qosMxBtRtUplnkRecvd", 10), ("qosMxBtRtDllnkRecvd", 11), ("qosResBerRecvd", 12), ("qosSduErrRatRecvd", 13), ("qosTransDelayRecvd", 14), ("qosTrfHndPriRecvd", 15), ("qosGrtBtRtUplnkRecvd", 16), ("qosGrtBtRtDllnkRecvd", 17), ("locMccRecvd", 18), ("locMncRecvd", 19), ("locRacRecvd", 20), ("locLacRecvd", 21), ("locCellIdRecvd", 22), ("medCompRecvd", 23), ("partcNmbRecvd", 24), ("thrldPartcNmbRecvd", 25), ("usrPartcTypeRecvd", 26), ("servCondRecvd", 27), ("servNodeRecvd", 28), ("usrCsgInfoRecvd", 29))

class TmnxMobPdnRefPointType(TextualConvention, Integer32):
    description = 'The data type TmnxMobPdnRefPointType describes the types of reference\n         point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("s5", 1), ("s8", 2), ("gn", 3), ("s2a", 4), ("gp", 5))

class TmnxMobService(DisplayString):
    reference = '3GPP TS 23.003 Section 19.4.3'
    description = 'The data type TmnxMobService describes the Service and Protocol\n         service names for 3GPP.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TmnxMobServRefPointType(TextualConvention, Integer32):
    description = 'The data type TmnxMobServRefPointType describes the types of reference\n         point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("s5", 1), ("s8", 2), ("s2a", 4))

class TmnxMobAccessType(TextualConvention, Integer32):
    description = 'The data type TmnxMobAccessType describes the various access types.\n         eps     - evolved packet system.\n         gprs    - general packet radio services.\n         non3gpp - trusted non-3gpp network such as evolved High Rate\n                   Packet Data (eHRPD) and untrusted non-3gpp network.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("eps", 1), ("gprs", 2), ("non3gpp", 3))

class TmnxMobUeStrPrefix(DisplayString):
    description = 'The data type TmnxMobUeStrPrefix describes the prefix for\n         International Mobile Subscriber Identity (IMSI) or Mobile Subscriber\n         Integrated Services Digital Network (MSISDN) of an User Equipment\n         (UE).'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(4, 15)

mibBuilder.exportSymbols("TIMETRA-TC-MG-MIB", PYSNMP_MODULE_ID=timetraTCMGMIBModule, TmnxMobAccessType=TmnxMobAccessType, TmnxMobAddrScheme=TmnxMobAddrScheme, TmnxMobApn=TmnxMobApn, TmnxMobApnDomainName=TmnxMobApnDomainName, TmnxMobApnOrZero=TmnxMobApnOrZero, TmnxMobArp=TmnxMobArp, TmnxMobArpValue=TmnxMobArpValue, TmnxMobArpValueOrZero=TmnxMobArpValueOrZero, TmnxMobAuthType=TmnxMobAuthType, TmnxMobAuthUserName=TmnxMobAuthUserName, TmnxMobBearerId=TmnxMobBearerId, TmnxMobBearerType=TmnxMobBearerType, TmnxMobBufferLimit=TmnxMobBufferLimit, TmnxMobChargingBearerType=TmnxMobChargingBearerType, TmnxMobChargingLevel=TmnxMobChargingLevel, TmnxMobChargingProfile=TmnxMobChargingProfile, TmnxMobChargingProfileOrInherit=TmnxMobChargingProfileOrInherit, TmnxMobDfPeerId=TmnxMobDfPeerId, TmnxMobDiaDetailPathMgmtState=TmnxMobDiaDetailPathMgmtState, TmnxMobDiaPathMgmtState=TmnxMobDiaPathMgmtState, TmnxMobDiaPeerHost=TmnxMobDiaPeerHost, TmnxMobDiaRetryCount=TmnxMobDiaRetryCount, TmnxMobDiaTransTimer=TmnxMobDiaTransTimer, TmnxMobDualStackPref=TmnxMobDualStackPref, TmnxMobGwId=TmnxMobGwId, TmnxMobGwType=TmnxMobGwType, TmnxMobImei=TmnxMobImei, TmnxMobImsi=TmnxMobImsi, TmnxMobImsiStr=TmnxMobImsiStr, TmnxMobIpCanType=TmnxMobIpCanType, TmnxMobLiTarget=TmnxMobLiTarget, TmnxMobLiTargetType=TmnxMobLiTargetType, TmnxMobMcc=TmnxMobMcc, TmnxMobMccOrEmpty=TmnxMobMccOrEmpty, TmnxMobMnc=TmnxMobMnc, TmnxMobMncOrEmpty=TmnxMobMncOrEmpty, TmnxMobMsisdn=TmnxMobMsisdn, TmnxMobNai=TmnxMobNai, TmnxMobNode=TmnxMobNode, TmnxMobPathMgmtState=TmnxMobPathMgmtState, TmnxMobPdnGyChrgTriggerType=TmnxMobPdnGyChrgTriggerType, TmnxMobPdnRefPointType=TmnxMobPdnRefPointType, TmnxMobPdnSessionEvent=TmnxMobPdnSessionEvent, TmnxMobPdnSessionState=TmnxMobPdnSessionState, TmnxMobPdnType=TmnxMobPdnType, TmnxMobPeerType=TmnxMobPeerType, TmnxMobPgwSigProtocol=TmnxMobPgwSigProtocol, TmnxMobPresenceState=TmnxMobPresenceState, TmnxMobProfGbrRate=TmnxMobProfGbrRate, TmnxMobProfIpTtl=TmnxMobProfIpTtl, TmnxMobProfKeepAliveInterval=TmnxMobProfKeepAliveInterval, TmnxMobProfKeepAliveResponse=TmnxMobProfKeepAliveResponse, TmnxMobProfKeepAliveRetryCount=TmnxMobProfKeepAliveRetryCount, TmnxMobProfKeepAliveTimeout=TmnxMobProfKeepAliveTimeout, TmnxMobProfMbrRate=TmnxMobProfMbrRate, TmnxMobProfMsgReTxRetryCount=TmnxMobProfMsgReTxRetryCount, TmnxMobProfMsgReTxTimeout=TmnxMobProfMsgReTxTimeout, TmnxMobProfName=TmnxMobProfName, TmnxMobProfNameOrEmpty=TmnxMobProfNameOrEmpty, TmnxMobProfPolChargingMethod=TmnxMobProfPolChargingMethod, TmnxMobProfPolMeteringMethod=TmnxMobProfPolMeteringMethod, TmnxMobProfPolReportingLevel=TmnxMobProfPolReportingLevel, TmnxMobQci=TmnxMobQci, TmnxMobQciValue=TmnxMobQciValue, TmnxMobQciValueOrZero=TmnxMobQciValueOrZero, TmnxMobQueueLimit=TmnxMobQueueLimit, TmnxMobRatingGrpState=TmnxMobRatingGrpState, TmnxMobRfAcctLevel=TmnxMobRfAcctLevel, TmnxMobRtrAdvtInterval=TmnxMobRtrAdvtInterval, TmnxMobRtrAdvtLifeTime=TmnxMobRtrAdvtLifeTime, TmnxMobSdf=TmnxMobSdf, TmnxMobSdfFilter=TmnxMobSdfFilter, TmnxMobSdfFilterDirection=TmnxMobSdfFilterDirection, TmnxMobSdfFilterNum=TmnxMobSdfFilterNum, TmnxMobSdfFilterProtocol=TmnxMobSdfFilterProtocol, TmnxMobSdfRuleName=TmnxMobSdfRuleName, TmnxMobServRefPointType=TmnxMobServRefPointType, TmnxMobServerState=TmnxMobServerState, TmnxMobService=TmnxMobService, TmnxMobStaticPolPrecedence=TmnxMobStaticPolPrecedence, TmnxMobStaticPolPrecedenceOrZero=TmnxMobStaticPolPrecedenceOrZero, TmnxMobUeId=TmnxMobUeId, TmnxMobUeIdType=TmnxMobUeIdType, TmnxMobUeRat=TmnxMobUeRat, TmnxMobUeState=TmnxMobUeState, TmnxMobUeStrPrefix=TmnxMobUeStrPrefix, TmnxMobUeSubType=TmnxMobUeSubType, timetraTCMGMIBModule=timetraTCMGMIBModule)
