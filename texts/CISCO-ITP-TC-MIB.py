#
# PySNMP MIB module CISCO-ITP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-TC-MIB
# Source digest sha256:d894be5dd9e1b0897d1a1d412d79cbcc07aebde600548055737149d344b40019
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 231))
ciscoItpTextualConventions.setRevisions(('2004-04-26 00:00', '2003-08-03 00:00', '2003-01-29 00:00', '2001-12-11 00:00', '2001-10-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpTextualConventions.setRevisionsDescriptions(('Updated CItpTcPointCodeType to allow M3UA and\n                 SUA point-code types.', 'Updated CItpTcPointCode textual convention to \n                 include descriptions for Japanese NTT and TTC\n                 variants.', 'Added textual convention used to support the \n                 ability to define multiple instances of the \n                 signalling points.  The following textual conventions\n                 were added.                                         \n                    CItpTcNetworkName\n                    CItpTcInstanceNumber\n                    CItpTcSls\n\n                 Also deprecated CItpTcGtaAddr and CItpTcGtaDisplayZB.\n                 Added CItpTcGtaLongAddr and CItpTcGtaLongDisplay.\n                 \n                 Added new enumerated value to CItpTcLinkType object\n                 for virtual link used to connect signalling points\n                 acting as gateways.', 'Added new enumerated value to CItpTcLinkType object\n                 for high speed link support. Add new enumerated\n                 value to the CItpTcSs7Variant object to support\n                 China national variant. A new textual convention has\n                 been added to address 0..15 range for Global Title\n                 addresses.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpTextualConventions.setLastUpdated('2004-04-26 00:00')
if mibBuilder.loadTexts: ciscoItpTextualConventions.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpTextualConventions.setContactInfo('       Cisco Systems, Inc\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpTextualConventions.setDescription('The defines textual conventions used by to manage\n                devices related to the SS7 network.  The\n                relevant ITU documents describing this technology is\n                the ITU Q series, including ITU Q.700: Introduction to\n                CCITT Signalling System No. 7 and ITU Q.701 Functional\n                description of the message transfer part (MTP) of\n                Signalling System No. 7.\n\n        Abbreviations:\n          CDPA  - Called Party Point Code\n          CGPA  - Calling Party Point Code\n          CLLI  - Common Language Location Codes\n          CR    - Connection Request message\n          CREF  - Connection Refusal message\n          DPC   - Destination Point Code\n          ERR   - Error message\n          GTA   - Global Title Address \n          GTI   - Global Title Indicator\n          GTT   - Global Title Translation\n          LUDT  - long unitdata message\n          LUDTS - long unitdata service message\n          M2PA  - MTP2 Peer-to-Peer Adaptation Layer\n          M3UA  - MTP3-User Adaptation \n          MAP   - Mated Application Table\n          MSU   - Message Signal Unit \n          MTP   - Message Transport Protocol\n          MTP2  - Layer 2 of Message Transport Protocol\n          MTP3  - Layer 3 of Message Transport Protocol\n          NAI   - Nature of Address Indicator\n          NP    - Numbering Plan         \n          NTT   - The Japanese Nippon Telephone & Telegraph \n          OPC   - Originating Point Code\n          PC    - Point Code\n          RTN   - Route Table Name\n          RSR   - Reset Request message\n          SCCP  - Signalling Connection Control Part\n          SCTP  - Stream Transmission Protocol(RFC 2960)\n          SI    - Signalling Indicator\n          SP    - Signalling Point\n          SLC   - Signalling Link Code\n          SLS   - Signalling Link Selector\n          SSN   - Subsystem Number\n          SUA   - SCCP-User Adaptation \n          TFR   - Transfer Restricted messages  \n          TT    - Title Translation\n          TTC   - The Japanese Telecommunications Technology \n                  Committee \n          UDT   - unitdata message\n          UDTS  - unitdata service message\n          XUDT  - extended unitdata message\n          XUDTS - extended unitdata service message\n        ')
class CItpTcAclId(TextualConvention, Unsigned32):
    description = 'An numeric Identifier used to specify an access list \n             used to permit and deny packets based on MTP3 \n             information. Either the value 0 or the value of access list\n             identifier. A value of zero indicates that an access list\n             is not specified.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2700, 2999), )
class CItpTcCLLI(TextualConvention, OctetString):
    reference = 'Complete listings of geographical and geopolitical \n             codes can be found in the BR 751-401-xxx series and\n             BR 751-100-055, respectively.'
    description = 'Common Language Location Codes (CLLI Codes). \n             An 11-character standardized geographic identifier\n             that uniquely identifies the geographic location of\n             telecommunication equipment.\n             \n             The CLLI code is supported as octet string containing\n             administrative information in human-readable form.\n\n             The use of control codes should be avoided.\n             \n             The use of newline should be avoided.\n\n             The use of leading or trailing white space should\n             be avoided.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 11)

class CItpTcDisplayPC(TextualConvention, OctetString):
    description = 'The Point Code in formatted based on the variant\n             and the customer defined parameters.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 12)

class CItpTcEncodingSchemeValue(TextualConvention, Integer32):
    description = 'The encoding scheme value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

class CItpTcGlobalTitleSelector(TextualConvention, Integer32):
    description = "Global Title Selector.\n            'nai'       : Global title translation based on\n                          nature of address indicator.\n                          \n            'tt'        : Global title translation based on\n                          translation type.\n                          \n            'ttNpEs'    : Global title translation based on\n                          translation type, numbering plan \n                          value and Encoding Scheme Value.\n                \n            'ttNpNaiEs' : Global title translation based on\n                          translation type, numbering plan,\n                          value, nature of address indicator\n                          and encoding scheme value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("nai", 1), ("tt", 2), ("ttNpEs", 3), ("ttNpNaiEs", 4))

class CItpTcGlobalTitleSelectorName(TextualConvention, OctetString):
    description = 'The configured name associated with SCCP GTT\n                 Selector.\n\n                 An octet string specified by an administrator that\n                 must be in human-readable form.  The names must\n                 conform to the allowed characters that can be \n                 specified via Command Line Interface(CLI).  The \n                 names cannot contain control character and should \n                 not contain leading or trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 9)

class CItpTcGtaAddr(TextualConvention, OctetString):
    description = 'The configured digits in the SCCP GTT\n                 Global Title Address.\n                 \n                 An octet string specified by an administrator\n                 must be in human-readable form.  The names must\n                 conform to the allowed characters that can be \n                 specified via Command Line Interface(CLI).  The \n                 names cannot contain control character and should \n                 not contain leading or trailing white space.'
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class CItpTcGtaLongAddr(TextualConvention, OctetString):
    description = 'The configured hexadecimal digits in the SCCP GTT\n                 Global Title Address.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CItpTcGtaDisplay(TextualConvention, OctetString):
    description = 'The configured digits in the SCCP GTT\n                 Global Title Address. It consists of ASCII\n                 representation of GTA hex digits.\n\n                 This textual convention has been deprecated and\n                 replaced by CItpTcGtaDisplayZB.'
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 15)

class CItpTcGtaDisplayZB(TextualConvention, OctetString):
    description = 'The configured digits in the SCCP GTT\n                 Global Title Address. It consists of ASCII\n                 representation of GTA hex digits.'
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 15)

class CItpTcGtaLongDisplay(TextualConvention, OctetString):
    description = 'The configured digits in the SCCP GTT\n                 Global Title Address. It consists of ASCII\n                 representation of GTA hex digits.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CItpTcGtaDisplayLen(TextualConvention, Unsigned32):
    description = 'The SCCP GTT Global Title Address length.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 15)

class CItpTcGtaLongDisplayLen(TextualConvention, Unsigned32):
    description = 'The SCCP GTT Global Title Address length.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 64)

class CItpTcNetworkName(TextualConvention, OctetString):
    description = 'The network name is used to indicate the network\n             in which this signalling point is participating.\n             One or more instances of signalling points can \n             exist in the same physical device.  This identifier\n             will be used to correlate instances of signalling \n             points by network.\n             \n             When multiple instance support is not enable the \n             network name will default to the null string.\n              \n             An octet string specified by an administrator that\n             must be in human-readable form.  The names must conform\n             to the allowed characters that can be specified via \n             Command Line Interface(CLI).  The names cannot contain\n             control character and should not contain leading or \n             trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 19)

class CItpTcInstanceNumber(TextualConvention, Unsigned32):
    description = 'The instance number used to select a particular\n                 Signalling point.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class CItpTcLinksetId(TextualConvention, OctetString):
    description = 'The configured name associated with an Signalling\n             Point Linkset.\n                 \n             An octet string specified by an administrator that must\n             be in human-readable form.  The names must conform to \n             the allowed characters that can be specified via \n             Command Line Interface(CLI).  The names cannot contain\n             control character and should not contain leading or \n             trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 19)

class CItpTcLinkSLC(TextualConvention, Unsigned32):
    description = 'The Signalling Link Code. This is the link identifier\n             within a linkset.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class CItpTcLinkType(TextualConvention, Integer32):
    description = "The link types.\n            'other'  : This link is of some type not listed below.\n            'serial' : This link is a serial link transporting\n                         SS7 traffic.\n            'sctpIp' : This a SCTP/IP link transporting \n                         SS7 traffic.\n            'hsl'    : This link is a high speed link using the ATM \n                       protocol for transporting SS7 traffic.\n            'virtual': This link is virtual link used to connect to \n                       instance of signalling point running on the \n                       same physical device.  The link will be used to \n                       send and manage traffic between two signalling\n                       acting as a gateway."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("serial", 2), ("sctpIp", 3), ("hsl", 4), ("virtual", 5))

class CItpTcNAI(TextualConvention, Integer32):
    description = 'The SCCP GTT Network Address Indicator (NAI).\n            The following values are generally used:\n              Unknown Nature of Address (0),\n              Subscriber Number (1),\n              Reserved for national use (2),\n              National Significant Number (3),\n              International Number (4),\n              Maximum NAI (127),\n              Invalid NAI (253),\n              Wild    NAI (254).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class CItpTcNetworkIndicator(TextualConvention, Integer32):
    description = "Network Indicator:\n             international - International network\n             national      - National network\n             reserved      - Reserved for national use\n             spare         - Spare (for international use only)\n            'international'      : International network\n            'internationalSpare' : International network spare\n            'national'           : National network\n            'nationalSpare'      : National network Spare"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("international", 0), ("internationatSpare", 1), ("national", 2), ("nationalSpare", 3))

class CItpTcNumberingPlan(TextualConvention, Integer32):
    description = 'The SCCP GTT Numbering Plan (NP).\n            The following values are generally used:\n              Unknown NP (0),\n              ISDN/Telephony NP (1),\n              Spare    (2),\n              Data  NP (3),\n              Telex NP (4),\n              Maritime Mobile NP (5),\n              Land Mobile     NP (6),\n              ISDN/Mobile     NP (7),\n              Private NP (8).\n              Max     NP (15),\n              Invalid NP (253),\n              Wild    NP (254).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class CItpTcPointCode(TextualConvention, Unsigned32):
    reference = 'The SS7 network node address as specified in the\n             International Telecommunication Union standard Q.708:\n             Specifications of Signalling System No. 7 - Numbering\n             of International Signalling Point Codes, and by ANSI\n             T1.111.8 Numbering of Signalling Point Codes.\n\n             GF 001-9001 - Technical Specifications of Signalling\n             System No. 7 for National Telephone Network of China.'
    description = 'The SS7 network node address as specified in the\n            following references.  The format of the Point\n            code depends on the variant defined in the \n            CgspSS7Variant object as follows.\n            \n                   33222222222211111111110000000000\n                   10987654321098765432109876543210\n            ANSI:          nnnnnnnn                 - Network\n                                   cccccccc         - Cluster\n                                           mmmmmmmm - Member\n            ITU:                     zzz            - Zone\n                                        aaaaaaaa    - Area/Network\n                                                iii - Identifier\n            NTT:                   zzzzz            - Zone         \n                                        aaaa        - Area/Network \n                                            iiiiiii - Identifier   \n            TTC:                   zzzzz            - Zone         \n                                        aaaa        - Area/Network \n                                            iiiiiii - Identifier   \n            \n            Note: The China variant has the same format as ANSI.\n                                                \n            This form of the point-code is not intended for\n            for presentation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16777216)

class CItpTcPointCodeMask(TextualConvention, Unsigned32):
    reference = 'The SS7 network node address as specified in the\n             International Telecommunication Union standard Q.708:\n             Specifications of Signalling System No. 7 - Numbering\n             of International Signalling Point Codes, and by ANSI\n             T1.111.8 Numbering of Signalling Point Codes.'
    description = 'A mask used to perform different operations on\n            pointcodes.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16777216)

class CItpTcPointCodeType(TextualConvention, Integer32):
    description = "List of the possible Point Code types.\n                'primary'     : The primary point used to communicate\n                                information on the Signalling point.\n                'additional'  : Additional point codes.\n                'capability'  : capability point codes.\n                'xua'         : MTP3-User Adaptation point codes or\n                                SCCP-User Adaptation point codes."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("primary", 1), ("additional", 2), ("capability", 3), ("xua", 4))

class CItpTcQos(TextualConvention, Unsigned32):
    description = 'The quality of service classification to be assigned \n             to the IP packets used to transport the SS7 messages.\n             The value can be from one to seven when selecting\n             a Qos class or 255 to indicate the packet will not\n             be assigned a Qos class. This value will be set to\n             zero when cItpSpLinkType indicates that \n             Quality of Service does not apply to this link.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(255, 255), )
class CItpTcRouteTableName(TextualConvention, OctetString):
    description = 'The configured name associated with an SP Route\n             Table.\n                 \n             An octet string specified by an administrator that must\n             be in human-readable form.  The names must conform to \n             the allowed characters that can be specified via \n             Command Line Interface(CLI).  The names cannot contain\n             control character and should not contain leading or \n             trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 19)

class CItpTcServiceIndicator(TextualConvention, Integer32):
    reference = 'ITU Q.704 Signalling network functions and messages section\n            14.2.1 Service indicator.'
    description = "The list of possible Service Indicator values. This\n            identifies the type of SS7 packet.\n\n            The service indicator codes for the international\n            Signalling network are allocated as follows:\n\n            'SNMM'        : Signalling network management \n                            messages (SNMM)\n            'SNTM'        : Signalling network testing and \n                            maintenance messages (SNTM)\n            'Spare2'      : Spare 2\n            'SCCP'        : SCCP\n            'TUP'         : Telephone User Part (TUP)\n            'ISUP'        : ISDN User Part      (ISUP)\n            'DUPC'        : Data User Part, call and circuit-related \n                            messages (DUPC)\n            'DUPF'        : Data User Part, facility registration and\n                            cancellation messages (DUPF)\n            'MTUP'        : Reserved for MTP Testing User Part (MTUP)\n            'BISUP'       : Broadband ISDN User Part  (BISUP)\n            'SISUP'       : Satellite ISDN User Part (SISUP)\n            'Spare11'     : Spare 11\n            'Spare12'     : Spare 12\n            'Spare13'     : Spare 13\n            'Spare14'     : Spare 14\n            'Spare15'     : Spare 15"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("snmm", 0), ("sntm", 1), ("spare2", 2), ("sccp", 3), ("tup", 4), ("isup", 5), ("dupc", 6), ("dupf", 7), ("mtup", 8), ("bisup", 9), ("sisup", 10), ("spare11", 11), ("spare12", 12), ("spare13", 13), ("spare14", 14), ("spare15", 15))

class CItpTcSls(TextualConvention, Unsigned32):
    description = 'The Signalling Link Selector is a numeric value that\n             contains the MTP3 packets to allow load balancing of\n             traffic across a link within a linkset or combined linkset.\n             Each linkset provides one or more tables used to map\n             Signalling Link Selectors to Signalling Link Codes.  The\n             number of Signalling Link Selectors is 16 for ITU and 256\n             for ANSI.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class CItpTcSs7Variant(TextualConvention, Integer32):
    reference = 'GF 001-9001 - Technical Specifications of Signalling\n             System No. 7 for National Telephone Network of China.'
    description = "The list of SS7 variants.\n            'ANSI'    : The ANSI variant of the SS7 specification.\n            'ITU'     : The ITU variant of the SS7 specification.\n            'China'   : The China national variant. This variant\n                        is a combination of ITU and ANSI. The \n                        protocol matches ITU except where the \n                        point-code has been expanded to ANSI format."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ansi", 1), ("itu", 2), ("china", 3))

class CItpTcSubSystemNumber(TextualConvention, Unsigned32):
    description = 'The SCCP Subsystem Number .  A  value of zero \n             indicates that a subsystem is not specified.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 255), )
class CItpTcSubSystemNumberMask(TextualConvention, Unsigned32):
    description = 'The SCCP Subsystem Number Mask.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(2, 255)

class CItpTcTableLoadStatus(TextualConvention, Integer32):
    description = "The status of the current or prior load operation.\n             'loadNotRequested' : load operations have not been\n                                  requested.\n\n             'loadInProgress'  : load request is active.\n        \n             'loadComplete' : load request complete without errors.\n        \n             'loadCompleteWithErrors' : Load request completed with\n                                        some type of errors that\n                                        prevented the adding of one\n                                        or more entries.\n           \n             'loadFailed' : Load request failed."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("loadNotRequested", 1), ("loadInProgress", 2), ("loadComplete", 3), ("loadCompleteWithErrors", 4), ("loadFailed", 5))

class CItpTcTimerMtp2T01(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link.\n            ANSI T1.111.3 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Alignment ready timer. The default and valid range is\n            dependant on the value of variant. \n            \n                  Min      Max      Def \n                  ------   ------   ------  \n            ANSI   12500    16000    13000  \n            ITU    40000    50000    40000 \n            \n            The SYNTAX statement allows values for both\n            the ANSI, ITU variants and MTP2 Peer-to-Peer \n            Adaptation Layer.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(5000, 150000)

class CItpTcTimerMtp2T02(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link.\n            ANSI T1.111.3 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Not aligned timer. The default and valid range is\n            dependant on the value of variant.\n\n            This timer is only applicable if cItpTcLinkType\n            is serial. A get on this object will return a\n            zero if the link is not serial.\n            \n                  Min      Max      Def \n                  ------   ------   ------  \n            ANSI    5000    14000    11500  \n            ITU     5000   150000     5000 \n            \n            The SYNTAX statement allows values for both\n            the ANSI and ITU variants.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5000, 150000), )
class CItpTcTimerMtp2T03(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link.\n            ANSI T1.111.3 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Aligned timer. The default and valid range is\n            dependant on the value of variant. \n             \n            This timer is only applicable if cItpTcLinkType\n            is serial. A get on this object will return a\n            zero if the link is not serial.\n            \n                  Min      Max      Def\n                  ------   ------   ------  \n            ANSI    5000    14000    11500   \n            ITU     1000     2000     1500 \n            \n            The SYNTAX statement allows values for both\n            the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1000, 14000), )
class CItpTcTimerMtp2T04E(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link.\n            ANSI T1.111.3 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Proving period timer emergency timer. The default and\n            valid range is dependant on the value of \n            variant.\n         \n            This timer is only applicable if cItpTcLinkType\n            is serial. A get on this object will return a\n            zero if the link is not serial.\n\n                  Min      Max      Def\n                  ------   ------   ------  \n            ANSI     540      660      600    \n            ITU      400      600      500 \n            \n            The SYNTAX statement allows values for both\n            the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(400, 660), )
class CItpTcTimerMtp2T04N(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link.\n            ANSI T1.111.3 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Proving period timer normal timer. The default and\n            valid range is dependant on the value of\n            variant.\n         \n            This timer is only applicable if cItpTcLinkType\n            is serial. A get on this object will return a\n            zero if the link is not serial.\n            \n                  Min      Max      Def\n                  ------   ------   ------  \n            ANSI    2007     2530     2300   \n            ITU     7500     9500     8200 \n            \n            The SYNTAX statement allows values for both\n            the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2007, 9500), )
class CItpTcTimerMtp2T05(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link.\n            ANSI T1.111.3 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Sending SIB timer. The default and valid range is\n            dependant on the value of variant.\n         \n            This timer is only applicable if cItpTcLinkType\n            is serial. A get on this object will return a\n            zero if the link is not serial.\n\n                  Min      Max      Def\n                  ------   ------   ------  \n            ANSI      80      120       80   \n            ITU       80      120      100 \n            \n            The SYNTAX statement allows values for both\n            the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(80, 120), )
class CItpTcTimerMtp2T06(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link.\n            ANSI T1.111.3 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Remote congestion timer. The default and valid range is\n            dependant on the value of variant.\n         \n                  Min      Max      Def\n                  ------   ------   ------  \n            ANSI    1000     6000     1000   \n            ITU     3000     6000     3000 \n            \n            The SYNTAX statement allows values for both\n            the ANSI, ITU variants and MTP2 Peer-to-Peer \n            Adaptation Layer.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 6000)

class CItpTcTimerMtp2T07(TextualConvention, Unsigned32):
    reference = 'ITU Q.703 Signalling Link.\n            ANSI T1.111.3 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Excessive delay of acknowledgement timer. The default\n             and valid range is dependant on the value of\n             variant().\n             \n             This timer is only applicable if cItpTcLinkType\n             is serial. A get on this object will return a\n             zero if the link is not serial.\n         \n                  Min      Max      Def\n                  ------   ------   ------  \n            ANSI     500     2000     1000    \n            ITU      500     2000     1000 \n            \n            The SYNTAX statement allows values for both\n            the ANSI and ITU variants.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(100, 6000), )
class CItpTcTimerMtp3T01(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n            ANSI T1.111 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Delay to avoid message mis-sequencing on changeover.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI     500     1200      800   \n             ITU      500     1200      800   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 1200)

class CItpTcTimerMtp3T02(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n            ANSI T1.111 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for changeover acknowledgement.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI     700     2000     1400      \n             ITU      700     2000     1400   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(700, 2000)

class CItpTcTimerMtp3T03(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n            ANSI T1.111 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Time controlled diversion-delay to avoid\n            mis-sequencing on change back.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI     500     1200      800      \n             ITU      500     1200      800   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 1200)

class CItpTcTimerMtp3T04(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n            ANSI T1.111 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for change back acknowledgement (first\n            attempt).\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI     500     1200      800      \n             ITU      500     1200      800   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 1200)

class CItpTcTimerMtp3T05(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n            ANSI T1.111 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for change back acknowledgement (second\n             attempt).\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI     500     1200      800      \n             ITU      500     1200      800   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 1200)

class CItpTcTimerMtp3T06(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n            ANSI T1.111 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Delay to avoid message mis-sequencing on controlled\n             rerouting.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI     500     1200      800      \n             ITU      500     1200      800   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 1200)

class CItpTcTimerMtp3T07(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for Signalling data link connection\n             acknowledgement.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI    1000     2000     1500      \n             ITU     1000     2000     1500 \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. A value of zero \n             indicates a value is not defined for a particular\n             variant or is not supported by the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1000, 2000), )
class CItpTcTimerMtp3T08(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Transfer prohibited inhibition timer (transient\n             solution).\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI     800     1200     1000    \n             ITU      800     1200     1000\n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(800, 1200)

class CItpTcTimerMtp3T10(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting to repeat Signalling routeset test message.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   30000    60000    45000      \n             ITU    30000    60000    45000   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(30000, 60000)

class CItpTcTimerMtp3T11(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Transfer restricted timer. (This is one way of\n             implementing the function described in 13.4/Q.704 and\n             mainly intended to simplify SPs.).\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   30000    90000    60000      \n             ITU    30000    90000    60000   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(30000, 90000)

class CItpTcTimerMtp3T12(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for uninhibit acknowledgement.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI     800     1500     1150      \n             ITU      800     1500     1150 \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(800, 1500)

class CItpTcTimerMtp3T13(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for force uninhibit.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI     800     1500     1150    \n             ITU      800     1500     1150 \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(800, 1500)

class CItpTcTimerMtp3T14(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for inhibition acknowledgement.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI    2000     3000     2500      \n             ITU     2000     3000     2500   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(2000, 3000)

class CItpTcTimerMtp3T15(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting to start Signalling routeset congestion\n             test. Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI    2000     3000     2500      \n             ITU     2000     3000     2500   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(2000, 3000)

class CItpTcTimerMtp3T16(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Waiting for routeset congestion status update.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI    1400     2000     1700      \n             ITU     1400     2000     1700   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1400, 2000)

class CItpTcTimerMtp3T17(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Delay to avoid oscillation of initial alignment\n             failure and link restart.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI     800     1500     1150       \n             ITU      800     1500     1150    \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(800, 1500)

class CItpTcTimerMtp3T18(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the \n             variant.\n             \n             ANSI: Repeat TFR once by response method\n             ITU:  MTP restart link supervision\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI    2000    20000    11000      \n             ITU     1000    31000    30000   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 31000)

class CItpTcTimerMtp3T19(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the \n             variant.\n             \n             ANSI: failed craft timer referral timer\n             ITU:  supervision timer during MTP restart\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI  480000   600000   540000      \n             ITU    67000    69000    68000   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(67000, 600000)

class CItpTcTimerMtp3T20(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the \n             variant.\n             \n             ANSI: waiting to repeat local inhibit test\n             ITU:  MTP restart timer at the Signalling point\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   90000   120000   105000      \n             ITU     1000    61000    60000   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1000, 120000)

class CItpTcTimerMtp3T21(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the \n             variant.\n             \n             ANSI: waiting to repeat remote inhibit test)       \n             ITU:  MTP restart timer at adjacent Signalling point\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   90000   120000   105000      \n             ITU    63000    65000    64000   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(63000, 120000)

class CItpTcTimerMtp3T22(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the \n             variant.\n             \n             ANSI: restarting SP waiting for Signalling links avail\n             ITU:  local inhibit test timer \n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   36000    60000    30000      \n             ITU    80000   360000   300000   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(36000, 360000)

class CItpTcTimerMtp3T23(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the \n             variant.\n             \n             ANSI: restarting SP waiting to receive all TRA msgs\n             ITU:  remote inhibit test timer\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI    9000    60000    30000      \n             ITU    80000   360000   300000   \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(9000, 360000)

class CItpTcTimerMtp3T24(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'This timers servers different function based on the \n             variant.\n             \n             ANSI: restarting SP waiting to broadcast all TRA msgs\n             ITU:  stabilizing timer after local processor outage\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI    9000    60000    30000    \n             ITU      500      500      500 \n             \n             The SYNTAX statement allows values for both\n             the ANSI and ITU variants. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(500, 60000)

class CItpTcTimerMtp3T25(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Timer at Signalling Point (SP) adjacent to restarting\n            SP, waiting for traffic restart allowed message.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   30000    35000    30000      \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by the\n             implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30000, 35000), )
class CItpTcTimerMtp3T26(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Timer at restarting SP waiting to repeat traffic\n            restart waiting message.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   12000    15000    12000     \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(12000, 15000), )
class CItpTcTimerMtp3T27(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Minimum duration of unavailability for full restart.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI    2000    50000     4000     \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 50000), )
class CItpTcTimerMtp3T28(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Timer at SP adjacent to restarting SP waiting for\n            traffic restart waiting message.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI    3000    35000    30000    \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3000, 35000), )
class CItpTcTimerMtp3T29(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Timer started when TRA sent in response to unexpected\n             TRA or TRW.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   60000    65000    63000      \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60000, 65000), )
class CItpTcTimerMtp3T30(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Timer to limit sending of TFPs and TFRs in response\n             to unexpected TRA or TRW.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   30000    35000    33000      \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30000, 35000), )
class CItpTcTimerMtp3T31(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'False link congestion detection timer.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   10000   120000    60000     \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10000, 120000), )
class CItpTcTimerMtp3T32(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Link oscillation timer - Procedure A.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI    5000   120000    60000      \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5000, 120000), )
class CItpTcTimerMtp3T33(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Probation timer for link oscillation - Procedure B.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   60000   600000   300000      \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60000, 600000), )
class CItpTcTimerMtp3T34(TextualConvention, Unsigned32):
    reference = 'ANSI T1.111 Telecommunications - Signalling system\n            No. 7 (SS7)-Message Transfer Part (MTP)'
    description = 'Suspension timer for link oscillation - Procedure B.\n             Ranges by variant.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI    5000   120000    60000      \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5000, 120000), )
class CItpTcTimerLinkTest(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Signalling Link test acknowledgement timer.\n             \n                    Min      Max      Def\n                   ------   ------   ------  \n             ANSI    4000    12000     8000      \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(4000, 12000), )
class CItpTcTimerLinkMessage(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Interval timer for sending test messages.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   30000    90000    60000      \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30000, 90000), )
class CItpTcTimerLinkActRetry(TextualConvention, Unsigned32):
    reference = 'ITU Q.704 Signalling network functions and messages.\n             ANSI T1.111 Telecommunications - Signalling system\n             No. 7 (SS7)-Message Transfer Part (MTP).'
    description = 'Link activation retry timer.\n             \n                   Min      Max      Def\n                   ------   ------   ------  \n             ANSI   60000    90000    60000      \n             \n             This timer is not used when the variant is ITU.\n             A value of zero indicates a value is not defined \n             for a particular variant or is not supported by\n             the implementation.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60000, 90000), )
class CItpTcTranslationType(TextualConvention, Integer32):
    description = "The Translation Type for SCCP GTT GTA specifies Title \n            Translation or Subsystem Number (SSN)\n           'tt'  : The GTT GTA has specified Title Translation\n           'ssn' : The GTT GTA has specified Subsystem Number."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tt", 1), ("ssn", 2))

class CItpTcURL(TextualConvention, OctetString):
    description = 'The URL used to load a configuration file.\n                 \n             An octet string specified by an administrator that must\n             be in human-readable form.  The names must conform to \n             the allowed characters that can be specified via \n             Command Line Interface(CLI).  The names cannot contain\n             control character and should not contain leading or \n             trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CItpTcXuaName(TextualConvention, OctetString):
    description = 'The configured name associated with M3UA/SUA\n                 ASP or AS name.\n                 \n                 An octet string specified by an administrator that\n                 must be in human-readable form.  The names must\n                 conform to the allowed characters that can be \n                 specified via Command Line Interface(CLI).  The \n                 names cannot contain control character and should \n                 not contain leading or trailing white space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 12)

mibBuilder.exportSymbols("CISCO-ITP-TC-MIB", CItpTcAclId=CItpTcAclId, CItpTcCLLI=CItpTcCLLI, CItpTcDisplayPC=CItpTcDisplayPC, CItpTcEncodingSchemeValue=CItpTcEncodingSchemeValue, CItpTcGlobalTitleSelector=CItpTcGlobalTitleSelector, CItpTcGlobalTitleSelectorName=CItpTcGlobalTitleSelectorName, CItpTcGtaAddr=CItpTcGtaAddr, CItpTcGtaDisplay=CItpTcGtaDisplay, CItpTcGtaDisplayLen=CItpTcGtaDisplayLen, CItpTcGtaDisplayZB=CItpTcGtaDisplayZB, CItpTcGtaLongAddr=CItpTcGtaLongAddr, CItpTcGtaLongDisplay=CItpTcGtaLongDisplay, CItpTcGtaLongDisplayLen=CItpTcGtaLongDisplayLen, CItpTcInstanceNumber=CItpTcInstanceNumber, CItpTcLinkSLC=CItpTcLinkSLC, CItpTcLinkType=CItpTcLinkType, CItpTcLinksetId=CItpTcLinksetId, CItpTcNAI=CItpTcNAI, CItpTcNetworkIndicator=CItpTcNetworkIndicator, CItpTcNetworkName=CItpTcNetworkName, CItpTcNumberingPlan=CItpTcNumberingPlan, CItpTcPointCode=CItpTcPointCode, CItpTcPointCodeMask=CItpTcPointCodeMask, CItpTcPointCodeType=CItpTcPointCodeType, CItpTcQos=CItpTcQos, CItpTcRouteTableName=CItpTcRouteTableName, CItpTcServiceIndicator=CItpTcServiceIndicator, CItpTcSls=CItpTcSls, CItpTcSs7Variant=CItpTcSs7Variant, CItpTcSubSystemNumber=CItpTcSubSystemNumber, CItpTcSubSystemNumberMask=CItpTcSubSystemNumberMask, CItpTcTableLoadStatus=CItpTcTableLoadStatus, CItpTcTimerLinkActRetry=CItpTcTimerLinkActRetry, CItpTcTimerLinkMessage=CItpTcTimerLinkMessage, CItpTcTimerLinkTest=CItpTcTimerLinkTest, CItpTcTimerMtp2T01=CItpTcTimerMtp2T01, CItpTcTimerMtp2T02=CItpTcTimerMtp2T02, CItpTcTimerMtp2T03=CItpTcTimerMtp2T03, CItpTcTimerMtp2T04E=CItpTcTimerMtp2T04E, CItpTcTimerMtp2T04N=CItpTcTimerMtp2T04N, CItpTcTimerMtp2T05=CItpTcTimerMtp2T05, CItpTcTimerMtp2T06=CItpTcTimerMtp2T06, CItpTcTimerMtp2T07=CItpTcTimerMtp2T07, CItpTcTimerMtp3T01=CItpTcTimerMtp3T01, CItpTcTimerMtp3T02=CItpTcTimerMtp3T02, CItpTcTimerMtp3T03=CItpTcTimerMtp3T03, CItpTcTimerMtp3T04=CItpTcTimerMtp3T04, CItpTcTimerMtp3T05=CItpTcTimerMtp3T05, CItpTcTimerMtp3T06=CItpTcTimerMtp3T06, CItpTcTimerMtp3T07=CItpTcTimerMtp3T07, CItpTcTimerMtp3T08=CItpTcTimerMtp3T08, CItpTcTimerMtp3T10=CItpTcTimerMtp3T10, CItpTcTimerMtp3T11=CItpTcTimerMtp3T11, CItpTcTimerMtp3T12=CItpTcTimerMtp3T12, CItpTcTimerMtp3T13=CItpTcTimerMtp3T13, CItpTcTimerMtp3T14=CItpTcTimerMtp3T14, CItpTcTimerMtp3T15=CItpTcTimerMtp3T15, CItpTcTimerMtp3T16=CItpTcTimerMtp3T16, CItpTcTimerMtp3T17=CItpTcTimerMtp3T17, CItpTcTimerMtp3T18=CItpTcTimerMtp3T18, CItpTcTimerMtp3T19=CItpTcTimerMtp3T19, CItpTcTimerMtp3T20=CItpTcTimerMtp3T20, CItpTcTimerMtp3T21=CItpTcTimerMtp3T21, CItpTcTimerMtp3T22=CItpTcTimerMtp3T22, CItpTcTimerMtp3T23=CItpTcTimerMtp3T23, CItpTcTimerMtp3T24=CItpTcTimerMtp3T24, CItpTcTimerMtp3T25=CItpTcTimerMtp3T25, CItpTcTimerMtp3T26=CItpTcTimerMtp3T26, CItpTcTimerMtp3T27=CItpTcTimerMtp3T27, CItpTcTimerMtp3T28=CItpTcTimerMtp3T28, CItpTcTimerMtp3T29=CItpTcTimerMtp3T29, CItpTcTimerMtp3T30=CItpTcTimerMtp3T30, CItpTcTimerMtp3T31=CItpTcTimerMtp3T31, CItpTcTimerMtp3T32=CItpTcTimerMtp3T32, CItpTcTimerMtp3T33=CItpTcTimerMtp3T33, CItpTcTimerMtp3T34=CItpTcTimerMtp3T34, CItpTcTranslationType=CItpTcTranslationType, CItpTcURL=CItpTcURL, CItpTcXuaName=CItpTcXuaName, PYSNMP_MODULE_ID=ciscoItpTextualConventions, ciscoItpTextualConventions=ciscoItpTextualConventions)
