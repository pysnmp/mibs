#
# PySNMP MIB module ALCATEL-IND1-TIMETRA-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-TIMETRA-TC-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 17:15:06 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
timetraModules, = mibBuilder.importSymbols("ALCATEL-IND1-TIMETRA-GLOBAL-MIB", "timetraModules")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Counter64, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Integer32, Gauge32, Counter32, NotificationType, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter64", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Integer32", "Gauge32", "Counter32", "NotificationType", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
timetraTCMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 2))
timetraTCMIBModule.setRevisions(('1908-01-01 00:00', '1907-01-01 00:00', '1906-03-23 00:00', '1905-08-31 00:00', '1905-01-24 00:00', '1904-01-15 00:00', '1903-08-15 00:00', '1903-01-20 00:00', '1901-05-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timetraTCMIBModule.setRevisionsDescriptions(('Rev 6.0                01 Jan 2008 00:00\n                         6.0 release of the TIMETRA-TC-MIB.', 'Rev 5.0                01 Jan 2007 00:00\n                         5.0 release of the TIMETRA-TC-MIB.', 'Rev 4.0                23 Mar 2006 00:00\n                         4.0 release of the TIMETRA-TC-MIB.', 'Rev 3.0                31 Aug 2005 00:00\n                         3.0 release of the TIMETRA-TC-MIB.', 'Rev 2.1                24 Jan 2005 00:00\n                         2.1 release of the TIMETRA-TC-MIB.', 'Rev 2.0                15 Jan 2004 00:00\n                         2.0 release of the TIMETRA-TC-MIB.', 'Rev 1.2                15 Aug 2003 00:00\n                         1.2 release of the TIMETRA-TC-MIB.', 'Rev 1.0                20 Jan 2003 00:00\n                         1.0 Release of the TIMETRA-TC-MIB.', 'Rev 0.1                14 Aug 2000 00:00\n                         First version of the TIMETRA-TC-MIB.',))
if mibBuilder.loadTexts: timetraTCMIBModule.setLastUpdated('0801010000Z')
if mibBuilder.loadTexts: timetraTCMIBModule.setOrganization('Alcatel')
if mibBuilder.loadTexts: timetraTCMIBModule.setContactInfo('Alcatel 7x50 Support\n             Web: http://www.alcatel.com/comps/pages/carrier_support.jhtml')
if mibBuilder.loadTexts: timetraTCMIBModule.setDescription("This document is the SNMP MIB module for the SNMP Textual\n        Conventions (TCs) used in the Alcatel 7x50 manageability\n        instrumentation.\n\n        Copyright 2003-2008 Alcatel-Lucent. All rights reserved.\n        Reproduction of this document is authorized on the condition\n        that the foregoing copyright notice is included.\n\n        This SNMP MIB module (Specification) embodies Alcatel's\n        proprietary intellectual property.  Alcatel retains\n        all title and ownership in the Specification, including any\n        revisions.\n\n        Alcatel grants all interested parties a non-exclusive\n        license to use and distribute an unmodified copy of this\n        Specification in connection with management of Alcatel\n        products, and without fee, provided this copyright notice and\n        license appear on all copies.\n\n        This Specification is supplied `as is', and Alcatel\n        makes no warranty, either express or implied, as to the use,\n        operation, condition, or performance of the Specification.")
class InterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface\n        or interface sub-layer in the managed system.  It is\n        recommended that values are assigned contiguously\n        starting from 1.  The value for each interface sub-\n        layer must remain constant at least from one re-\n        initialization of the entity's network management\n        system to the next re-initialization."
    status = 'current'
    displayHint = 'd'

class TmnxPortID(TextualConvention, Unsigned32):
    description = "A portid is an unique 32 bit number encoded as shown below.\n            \n            32 30 | 29 26 | 25 22 | 21 16 | 15  1 |\n            +-----+-------+-------+-------+-------+\n            |000  |  slot |  mda  | port  |  zero | Physical Port\n            +-----+-------+-------+-------+-------+\n\n            32 30 | 29 26 | 25 22 | 21 16 | 15  1 |\n            +-----+-------+-------+-------+-------+\n            |001  |  slot |  mda  | port  |channel| Channel\n            +-----+-------+-------+-------+-------+\n\n         Slots, mdas (if present), ports, and channels are numbered\n         starting with 1.\n\n            32     29 | 28             10 | 9   1 |\n            +---------+-------------------+-------+\n            | 0 1 0 0 |   zeros           |   ID  | Virtual Port\n            +---------+-------------------+-------+\n\n            32     29 | 28                9 | 8 1 |\n            +---------+---------------------+-----+\n            | 0 1 0 1 |   zeros             | ID  | LAG Port\n            +---------+---------------------+-----+\n\n        A card port number (cpn) has significance within the context\n        of the card on which it resides(ie., cpn 2 may exist in one or\n        more cards in the chassis).  Whereas, portid is an\n        unique/absolute port number (apn) within a given chassis.\n        \n        An 'invalid portid' is a TmnxPortID with a value of 0x1e000000 as \n        represented below.\n        \n            32 30 | 29 26 | 25 22 | 21 16 | 15  1 |\n            +-----+-------+-------+-------+-------+\n            |zero | ones  | zero  |  zero |  zero | Invalid Port\n            +-----+-------+-------+-------+-------+"
    status = 'current'

class TmnxEncapVal(TextualConvention, Unsigned32):
    description = 'The value of the label used to identify the entity using the\n       specified encapsulation value on a specific port.\n\n       The format of this object depends on the encapsulation type\n       defined on this port.\n\n       When the encapsulation is nullEncap the value of this object\n       must be zero.\n\n       31                                   0\n       +--------+--------+--------+--------+\n       |00000000 00000000 00000000 00000000|\n       +--------+--------+--------+--------+\n\n       When the encapsulation is dot1qEncap the value of this object\n       is equal to the 12-bit IEEE 802.1Q VLAN ID.\n\n       31                                   0\n       +--------+--------+--------+--------+\n       |00000000 00000000 0000XXXX XXXXXXXX|\n       +--------+--------+--------+--------+\n\n       When the encapsulation is mplsEncap the value of this object\n       is equal to the 20-bit LSP ID.\n\n       31                                   0\n       +--------+--------+--------+--------+\n       |00000000 0000XXXX XXXXXXXX XXXXXXXX|\n       +--------+--------+--------+--------+\n\n       When the encapsulation is frEncap, the value of this object is\n       equal to the 10-bit Frame Relay DLCI.\n\n       31                                   0\n       +--------+--------+--------+--------+\n       |00000000 00000000 000000XX XXXXXXXX|\n       +--------+--------+--------+--------+\n\n       When the encapsulation is qinqEncap, the value of the outer\n       802.1Q VLAN ID is encoded in the least significant 16 bits,\n       and the value of the inner VLAN ID is encoded in the most\n       significant 16 bits.\n\n       31                                   0\n       +--------+--------+--------+--------+\n       |0000YYYY YYYYYYYY 0000XXXX XXXXXXXX|\n       +--------+--------+--------+--------+\n\n       When the encapsulation is atmEncap, the value\n       of the ATM VCI is encoded in the least significant \n       16 bits, and the value of the ATM VPI is encoded \n       in the next 12 bits.\n\n       For ATM VCs, the top 2 bits are 00.  The value of\n       the ATM VCI is encoded in the least significant 16 \n       bits, and the value of the ATM VPI is encoded in the next\n       12 bits.\n                     \n       31                                   0\n       +--------+--------+--------+--------+\n       |0000YYYY YYYYYYYY XXXXXXXX XXXXXXXX|\n       +--------+--------+--------+--------+   \n\n       For ATM VPs, the top 2 bits are 01.  The value of\n       the ATM VPI is encoded in the least significant 12 bits.\n\n       31                                   0\n       +--------+--------+--------+--------+\n       |01000000 00000000 0000XXXX XXXXXXXX|\n       +--------+--------+--------+--------+          \n\n       For ATM VP ranges, the top 2 bits are 10.  The value of\n       the start of the ATM VPI range is encoded in the least significant \n       12 bits, and the value of the end of the ATM VP range is encoded\n       in the next 12 bits.\n\n       31                                   0\n       +--------+--------+--------+--------+\n       |10000000 YYYYYYYY YYYYXXXX XXXXXXXX|\n       +--------+--------+--------+--------+         \n\n       For ATM ports, the top 2 bits are 11, and the rest of the bits \n       must be zero.  \n\n       31                                   0\n       +--------+--------+--------+--------+\n       |11000000 00000000 00000000 00000000|\n       +--------+--------+--------+--------+         \n\n       When the encapsulation is wanMirrorEncap the value of this \n       object is equal to the 12-bit value.\n                     \n       31                                   0\n       +--------+--------+--------+--------+\n       |00000000 00000000 0000XXXX XXXXXXXX|\n       +--------+--------+--------+--------+      \n\n       Some ports have a restrictions to the encapsulation types that\n       they can support and hence impose restrictions on the respective\n       formats defined above.'
    status = 'current'

class QTag(TextualConvention, Integer32):
    description = 'The QTag data type is a 12-bit integer tag used to identify\n        a service.  The values 0 and 4095 are not allowed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class QTagOrZero(TextualConvention, Unsigned32):
    description = "The data type QTagOrZero represents a VLAN tag. \n        \n         The value '0' indicates that no VLAN tag is provisioned, or that its value\n         is unknown."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4094)

class TmnxStrSapId(TextualConvention, OctetString):
    description = 'The value of TmnxStrSapId is a printable string which\n        contains the owner SAP Id or equivalent on a remote system.\n\n        The string should contain the printable string equivalent of the\n        textual-conventions TmnxPortID and TmnxEncapVal in the format\n        specified as TmnxPortID[:TmnxEncapVal]'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class IpAddressPrefixLength(TextualConvention, Integer32):
    reference = ''
    description = 'the number of bits to match in an IP address mask.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32)

class TmnxActionType(TextualConvention, Integer32):
    description = "The TmnxActionType data type is an enumerated integer\n        that describes the values used to support action or\n        operation style commands.  Setting a variable of this\n        type to 'doAction' causes the action to occur.  GETs and\n        GETNEXTs on this variable return 'not-applicable'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("doAction", 1), ("notApplicable", 2))

class TmnxAdminState(TextualConvention, Integer32):
    description = 'The TmnxAdminState data type is an enumerated integer that describes\n        the values used to identify the administratively desired state of\n        functional modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noop", 1), ("inService", 2), ("outOfService", 3))

class TmnxOperState(TextualConvention, Integer32):
    description = 'The TmnxOperState data type is an enumerated integer that describes\n        the values used to identify the current operational state of functional\n        modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("inService", 2), ("outOfService", 3), ("transition", 4))

class TmnxStatus(TextualConvention, Integer32):
    description = "The TmnxStatus data type is an enumerated integer that describes the\n        values used to identify the current status of functional modules in the\n        system such as OSPF and MPLS protocols. Setting this variable to\n        'create' causes instantiation of the feature in the system.  Setting it\n        to 'delete' removes the instance and all associated configuration\n        information."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("create", 1), ("delete", 2))

class TmnxEnabledDisabled(TextualConvention, Integer32):
    description = "The TmnxEnabledDisabled data type is an enumerated integer that\n         describes the values used to identify whether an entity is\n         'enabled' or 'disabled'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class TNamedItem(TextualConvention, OctetString):
    description = 'The name of an item.  When used as an index to a table, the item\n         name uniquely identifies the instance.  When used in a reference\n         (TNamedItemOrEmpty) the item name entry must exist in the table.\n\n         Note, use only NVT ASCII displayable characters\n         here, no control characters, no UTF-8, etc.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TNamedItemOrEmpty(TextualConvention, OctetString):
    description = 'The name of an item, or an empty string.  When used in a reference\n         (TNamedItemOrEmpty) the item name entry must exist in the table.\n\n         Note, use only NVT ASCII displayable characters\n         here, no control characters, no UTF-8, etc.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), )
class TItemDescription(TextualConvention, OctetString):
    description = 'Description for an item.  Note, use only NVT ASCII displayable characters\n        here, no control characters, no UTF-8, etc.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 80)

class TItemLongDescription(TextualConvention, OctetString):
    description = 'Longer description for an item.  Note, use only NVT ASCII displayable\n        characters here, no control characters, no UTF-8, etc.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 160)

class TmnxVRtrID(TextualConvention, Integer32):
    description = 'A number used to identify a virtual router instance in the system.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4096)

class TmnxVRtrIDOrZero(TextualConvention, Integer32):
    description = 'A number used to identify a virtual router instance in the system.\n         The number 0 will have special significance in the context the TC \n         is used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4096)

class TmnxBgpAutonomousSystem(TextualConvention, Integer32):
    reference = 'BGP4-MIB.bgpPeerRemoteAs'
    description = 'an autonomous system (AS) number.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxBgpLocalPreference(TextualConvention, Unsigned32):
    reference = 'RFC 1771 section 4.3 Path Attributes e)'
    description = 'a local route preference value.'
    status = 'current'

class TmnxBgpPreference(TextualConvention, Unsigned32):
    reference = 'RFC 1771 section 4.3 Path Attributes e)'
    description = 'a route preference value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxCustId(TextualConvention, Unsigned32):
    description = 'A number used to identify a Customer or\n                     Subscriber. This ID must be unique within\n                     the Service Domain. The value 0 is used as\n                     the null ID.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), )
class TmnxServId(TextualConvention, Unsigned32):
    description = 'A number used to identify a Service. This ID\n                     must be unique within the Service Domain.\n                     The value 0 is used as the null ID.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), )
class ServiceAdminStatus(TextualConvention, Integer32):
    reference = ''
    description = 'ServiceAdminStatus data type is an enumerated integer that\n                  describes the values used to identify the administrative\n                  state of a service.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class ServiceOperStatus(TextualConvention, Integer32):
    reference = ''
    description = 'ServiceOperStatus data type is an enumerated integer that\n                  describes the values used to identify the current operational\n                  state of a service.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class TPolicyID(TextualConvention, Unsigned32):
    description = 'The identification number of a policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TSapIngressPolicyID(TextualConvention, Unsigned32):
    description = 'The identification number of a SAP ingress policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TSapEgressPolicyID(TextualConvention, Unsigned32):
    description = 'The identification number of a SAP egress policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TPolicyStatementNameOrEmpty(TextualConvention, OctetString):
    description = 'The name of a policy statement, when an object refers to it.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), )
class TmnxVcType(TextualConvention, Integer32):
    description = "The value of TmnxVcType is an enumerated integer that\n                     indicates a Virtual Circuit (VC) type. 'frDlciMartini(1)'\n                     replaces the old 'frDlci' when used over martini tunnels."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 9, 10, 11, 17, 18, 19, 20, 21, 23, 25, 4096))
    namedValues = NamedValues(("frDlciMartini", 1), ("atmSdu", 2), ("atmCell", 3), ("ethernetVlan", 4), ("ethernet", 5), ("atmVccCell", 9), ("atmVpcCell", 10), ("ipipe", 11), ("satopE1", 17), ("satopT1", 18), ("satopE3", 19), ("satopT3", 20), ("cesopsn", 21), ("cesopsnCas", 23), ("frDlci", 25), ("mirrorDest", 4096))

class TmnxVcId(TextualConvention, Unsigned32):
    description = 'A 32 bit number is used to identify a VC(Virtual Circuit).\n                     The VC ID cannot be 0.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TmnxVcIdOrNone(TextualConvention, Unsigned32):
    description = 'A 32 bit number is used to identify a VC(Virtual Circuit).\n                     A value of 0 indicates no VC ID is configured or \n                     available.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class Dot1PPriority(TextualConvention, Integer32):
    reference = ''
    description = 'IEEE 802.1p priority.  zero is lowest, seven is highest.\n         -1 means not set'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class ServiceAccessPoint(TextualConvention, Integer32):
    reference = 'assigned numbers:  http://www.iana.org/assignments/ieee-802-numbers'
    description = '802.2 LLC SAP value, Source and Destination.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TLspExpValue(TextualConvention, Integer32):
    reference = ''
    description = 'MPLS Experimental bits. -1 means not set.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class TIpProtocol(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/protocol-numbers'
    description = 'IP protocol number.  well known protocol numbers include ICMP(1),\n         TCP(6), UDP(17).\n\n         -1 means value not set.\n         -2 indicates protocol wildcard for UDP and TCP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TIpOption(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/ip-parameters'
    description = 'IP packet options octet.  explanation of the octet bits:\n\n     IP OPTION NUMBERS\n\n     The Internet Protocol (IP) has provision for optional header fields\n     identified by an option type field.  Options 0 and 1 are exactly one\n     octet which is their type field.  All other options have their one\n     octet type field, followed by a one octet length field, followed by\n     length-2 octets of option data.  The option type field is sub-divided\n     into a one bit copied flag, a two bit class field, and a five bit\n     option number.  These taken together form an eight bit value for the\n     option type field.  IP options are commonly refered to by this value.\n\n\n     Copy Class Number Value Name                Reference\n     ---- ----- ------ ----- ------------------------------- ---------\n        0     0      0     0 EOOL   - End of Options List    [RFC791,JBP]\n        0     0      1     1 NOP    - No Operation           [RFC791,JBP]\n        1     0      2   130 SEC    - Security                  [RFC1108]\n        1     0      3   131 LSR    - Loose Source Route     [RFC791,JBP]\n        0     2      4    68 TS     - Time Stamp             [RFC791,JBP]\n        1     0      5   133 E-SEC  - Extended Security         [RFC1108]\n        1     0      6   134 CIPSO  - Commercial Security           [???]\n        0     0      7     7 RR     - Record Route           [RFC791,JBP]\n        1     0      8   136 SID    - Stream ID              [RFC791,JBP]\n        1     0      9   137 SSR    - Strict Source Route    [RFC791,JBP]\n        0     0     10    10 ZSU    - Experimental Measurement      [ZSu]\n        0     0     11    11 MTUP   - MTU Probe                 [RFC1191]*\n        0     0     12    12 MTUR   - MTU Reply                 [RFC1191]*\n        1     2     13   205 FINN   - Experimental Flow Control    [Finn]\n        1     0     14   142 VISA   - Expermental Access Control [Estrin]\n        0     0     15    15 ENCODE - ???                      [VerSteeg]\n        1     0     16   144 IMITD  - IMI Traffic Descriptor        [Lee]\n        1     0     17   145 EIP    - Extended Internet Protocol[RFC1385]\n        0     2     18    82 TR     - Traceroute        [RFC1393]\n        1     0     19   147 ADDEXT - Address Extension    [Ullmann IPv7]\n        1     0     20   148 RTRALT - Router Alert              [RFC2113]\n        1     0     21   149 SDB    - Selective Directed Broadcast[Graff]\n        1     0     22   150 NSAPA  - NSAP Addresses          [Carpenter]\n        1     0     23   151 DPS    - Dynamic Packet State        [Malis]\n        1     0     24   152 UMP    - Upstream Multicast Pkt. [Farinacci]\n\n     [Note, an asterisk (*) denotes an obsoleted IP Option Number.]\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class TTcpUdpPort(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/port-numbers'
    description = 'The number of a TCP or UDP port.\n         Well known port numbers include\n         ftp-data(20), ftp(21), telnet(23), smtp(25), http(80),\n         pop3(110), nntp(119), snmp(161), snmptrap(162), etc.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TTcpUdpPortOperator(TextualConvention, Integer32):
    description = "The operator specifies the manner in which a couple of other\n        MIB objects in the table are supposed to be used.\n\n        Operator        Value1               Value2\n        ----------------------------------------------------\n        none(0)         Any(0)               Any(0)\n        eq(1)           Specified Value      Any(0)\n        range(2)        Starting Value       Ending Value\n        lt(3)           Specified Value      Any(0)\n        gt(4)           Specified Value      Any(0)\n\n        'Any(0)' specifies that, this object can accept any values\n         but would default to 0. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("eq", 1), ("range", 2), ("lt", 3), ("gt", 4))

class TFrameType(TextualConvention, Integer32):
    description = 'The type of the frame for which this mac filter match criteria is\n        defined.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("e802dot3", 0), ("e802dot2LLC", 1), ("e802dot2SNAP", 2), ("ethernetII", 3))

class TQueueId(TextualConvention, Integer32):
    description = 'The value of TQueueId specifies the identification number of a\n         queue.  A value of zero (0) indicates that no specific queue \n         identification has been assigned for this object. When an object\n         of type TQueueId is an SNMP table index, an index value of zero \n         (0) is not allowed and a noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TIngressQueueId(TextualConvention, Integer32):
    description = 'The value of TIngressQueueId specifies the identification number \n         of an ingress queue.  A value of zero (0) indicates that no \n         specific queue identification has been assigned for this object. \n         When an object of type TIngressQueueId is an SNMP table index,\n         an index value of zero (0) is not allowed and a noCreation error\n         will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TEgressQueueId(TextualConvention, Integer32):
    description = 'The value of TEgressQueueId specifies the identification number \n         of an egress queue.  A value of zero (0) indicates that no \n         specific queue identification has been assigned for this object. \n         When an object of type TEgressQueueId is an SNMP table index,\n         an index value of zero (0) is not allowed and a noCreation error\n         will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TDSCPName(TextualConvention, OctetString):
    description = 'The name of a Differential Services Code Point value.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TDSCPNameOrEmpty(TextualConvention, OctetString):
    description = 'The name of a Differential Services Code Point value.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), )
class TDSCPValue(TextualConvention, Integer32):
    description = 'The value of a Differential Services Code Point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

class TDSCPValueOrNone(TextualConvention, Integer32):
    description = 'The value of a Differential Services Code Point (DSCP). A value\n         of -1 means that no DSCP value is configured or available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 63), )
class TDSCPFilterActionValue(TextualConvention, Integer32):
    description = 'The value of a Differential Services Code Point. -1 means not set.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TFCName(TextualConvention, OctetString):
    description = 'The name of a Forwarding Class entry.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TFCNameOrEmpty(TextualConvention, OctetString):
    description = 'The name of a Forwarding Class entry.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), )
class TFCSet(TextualConvention, Bits):
    description = 'This data type describes a set of Forwarding Classes.'
    status = 'current'
    namedValues = NamedValues(("be", 0), ("l2", 1), ("af", 2), ("l1", 3), ("h2", 4), ("ef", 5), ("h1", 6), ("nc", 7))

class TFCType(TextualConvention, Integer32):
    description = 'This data type enumerates the Forwarding Classes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("be", 0), ("l2", 1), ("af", 2), ("l1", 3), ("h2", 4), ("ef", 5), ("h1", 6), ("nc", 7))

class TmnxTunnelType(TextualConvention, Integer32):
    description = 'The type of this tunnel entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("sdp", 1), ("ldp", 2), ("rsvp", 3), ("gre", 4), ("bypass", 5), ("invalid", 6))

class TmnxTunnelID(TextualConvention, Unsigned32):
    description = 'The identifying value for a BGP-VPRN tunnel.  Depending on the\n        tunnel type the associated tunnel-id may be an sdp-id, an lsp-id\n        or zero(0).'
    status = 'current'

class TmnxBgpRouteTarget(TextualConvention, OctetString):
    description = 'TmnxBgpRouteTarget is an readable string that specifies the\n         extended community name to be accepted by a Route Reflector Server\n         or advertised by the router when reflecting any routes. I.e, it\n         does not apply to routes that are not reflected by the router.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxVPNRouteDistinguisher(TextualConvention, OctetString):
    description = 'The VPRN route distinguisher is a 8-octet object. It contains a\n         2-octet type field followed by a 6-octet value field. The type\n         field specify how to interpret the value field.\n\n         Type 0 specifies two subfields as a 2-octet administrative field\n         and a 4-octet assigned number subfield.\n\n         Type 1 specifies two subfields as a 4-octet administrative field\n         which must contain an IP address and a 2-octet assigned number\n         subfield.\n\n         Type 2 specifies two subfields as a 4-octet administrative field\n         which contains a 4-octet AS number and a 2-octet assigned number\n         subfield.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class SdpBindId(TextualConvention, OctetString):
    description = 'The value used to uniquely identify an SDP Binding.\n                     The first four octets correspond to the zero-extended\n                     16-bit SDP ID, while the remaining four octets\n                     correspond to the 32-bit VC ID, both encoded in network\n                     byte order.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxVRtrMplsLspID(TextualConvention, Unsigned32):
    description = 'A unique value, greater than zero, for each Label\n                     Switched Path in the managed system.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TPortSchedulerPIR(TextualConvention, Integer32):
    description = 'The Peak Information Rate (PIR) rate to be used in kbps.\n         The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 40000000), )
class TPortSchedulerCIR(TextualConvention, Integer32):
    description = 'The Committed Information Rate (CIR) rate to be used in kbps.\n         The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 40000000), )
class TWeight(TextualConvention, Integer32):
    description = 'The weight of the specified entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TCIRRate(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class TPIRRate(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class TSecondaryShaper10GPIRRate(TextualConvention, Integer32):
    description = 'The secondary shaper PIR rate to be used in Mbps.\n         The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10000), )
class TPIRRateOverride(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate.\n         A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class TPIRRateOrZero(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate.\n         The value 0 means undefined rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class TmnxDHCP6MsgType(TextualConvention, Integer32):
    description = 'The DHCP6 messagetype.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("dhcp6MsgTypeSolicit", 1), ("dhcp6MsgTypeAdvertise", 2), ("dhcp6MsgTypeRequest", 3), ("dhcp6MsgTypeConfirm", 4), ("dhcp6MsgTypeRenew", 5), ("dhcp6MsgTypeRebind", 6), ("dhcp6MsgTypeReply", 7), ("dhcp6MsgTypeRelease", 8), ("dhcp6MsgTypeDecline", 9), ("dhcp6MsgTypeReconfigure", 10), ("dhcp6MsgTypeInfoRequest", 11), ("dhcp6MsgTypeRelayForw", 12), ("dhcp6MsgTypeRelayReply", 13), ("dhcp6MsgTypeMaxValue", 14))

class TmnxOspfInstance(TextualConvention, Unsigned32):
    description = 'A number used to identify an instance of OSPF.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 31)

class TmnxBGPFamilyType(TextualConvention, Bits):
    description = 'The value of TmnxBGPFamilyType specifies the AFI-SAFI family for\n         BGP peer.'
    status = 'current'
    namedValues = NamedValues(("ipv4Unicast", 0), ("ipv4Multicast", 1), ("ipv4UastMcast", 2), ("ipv4MplsLabel", 3), ("ipv4Vpn", 4), ("ipv6Unicast", 5), ("ipv6Multicast", 6), ("ipv6UcastMcast", 7), ("ipv6MplsLabel", 8), ("ipv6Vpn", 9))

class TmnxIgmpGroupFilterMode(TextualConvention, Integer32):
    description = "The data type TmnxIgmpGroupFilterMode describes the filter-mode of\n         a group.\n\n         In 'include(1)' mode, reception of packets sent to the specified\n         multicast address is requested only from those IPv4 Source addresses\n         listed in the corresponding source-list.\n\n         In 'exclude(2)' mode, reception of packets sent to the given multicast\n         address is requested from all IPv4 Source addresses, except those\n         listed in the corresponding source-list (if any)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("include", 1), ("exclude", 2))

class TmnxIgmpGroupType(TextualConvention, Integer32):
    description = 'The data type TmnxIgmpGroupType describes how a multicast group is\n         learned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class TmnxIgmpVersion(TextualConvention, Integer32):
    description = "The data type TmnxIgmpVersion denotes the version of the IGMP protocol:\n         - 'version1(1)': means version 1 of the IGMP protocol\n         - 'version2(2)': means version 2 of the IGMP protocol\n         - 'version3(3)': means version 3 of the IGMP protocol."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("version1", 1), ("version2", 2), ("version3", 3))

class TmnxMldGroupFilterMode(TextualConvention, Integer32):
    description = "The data type TmnxMldGroupFilterMode describes the filter-mode of a\n         group.\n\n         In 'include(1)' mode, reception of packets sent to the specified\n         multicast address is requested only from those IPv6 source addresses\n         listed in the corresponding source-list.\n\n         In 'exclude(2)' mode, reception of packets sent to the given multicast\n         address is requested from all IPv6 source addresses, except those\n         listed in the corresponding source-list (if any)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("include", 1), ("exclude", 2))

class TmnxMldGroupType(TextualConvention, Integer32):
    description = 'The data type TmnxMldGroupType describes how a multicast group is\n         learned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class TmnxMldVersion(TextualConvention, Integer32):
    description = "The data type TmnxMldVersion denotes the version of the MLD protocol:\n         - 'version1(1)': means version 1 of the MLD protocol\n         - 'version2(2)': means version 2 of the MLD protocol"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("version1", 1), ("version2", 2))

class TmnxManagedRouteStatus(TextualConvention, Integer32):
    description = 'The data type TmnxManagedRouteStatus denotes the status of a Managed Route.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("installed", 0), ("notYetInstalled", 1), ("wrongAntiSpoofType", 2), ("outOfMemory", 3), ("shadowed", 4), ("routeTableFull", 5), ("parentInterfaceDown", 6))

class TmnxAncpString(TextualConvention, OctetString):
    description = 'The TmnxAncpString data type contains a valid ancp string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 63)

class TmnxAncpStringOrZero(TextualConvention, OctetString):
    description = 'The TmnxAncpStringOrZero data type contains a valid ancp string.\n        An empty string indicates that no ANCP string is defined.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 63)

class TmnxMulticastAddrFamily(TextualConvention, Integer32):
    description = 'The data type TmnxMulticastAddrFamily denotes the family for\n         multicast protocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ipv4Multicast", 0), ("ipv6Multicast", 1))

class TmnxSubIdentString(TextualConvention, OctetString):
    description = 'The data type TmnxSubIdentString denotes the subscriber\n         identification string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxSubIdentStringOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxSubIdentStringOrEmpty denotes the subscriber\n         identification string. The empty string denotes the absence of a\n         subscriber identification string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubProfileString(TextualConvention, OctetString):
    description = 'The data type TmnxSubProfileString denotes the subscriber\n         profile string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxSubProfileStringOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxSubProfileStringOrEmpty denotes the subscriber\n         profile string. The empty string denotes the absence of a\n         subscriber profile.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxSlaProfileString(TextualConvention, OctetString):
    description = 'The data type TmnxSlaProfileString denotes the SLA \n         profile string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxSlaProfileStringOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxSlaProfileStringOrEmpty denotes the SLA\n         profile string. The empty string denotes the absence of a\n         SLA profile.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxAppProfileString(TextualConvention, OctetString):
    description = 'The data type TmnxAppProfileString denotes the application\n         profile string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxAppProfileStringOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxAppProfileStringOrEmpty denotes the application\n         profile string. The empty string denotes the absence of a\n         application profile.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxSubMgtIntDestIdOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxSubMgtIntDestIdOrEmpty denotes the intermediate\n         destination id. The empty string denotes the absence of an\n         intermediate destination id.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubMgtIntDestId(TextualConvention, OctetString):
    description = 'The data type TmnxSubMgtIntDestId denotes the intermediate \n         destination id.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxDhcpOptionType(TextualConvention, Integer32):
    description = "The data type TmnxDhcpOptionType represents how the value\n         of this option is encoded:\n         - 'ipv4 (1)': this option contains an IPv4 address (4 octets)\n         - 'ascii(2)': this option contains seven-bit ASCII characters\n         - 'hex  (3)': this option contains octets. It must be displayed in\n                       hexadecimal format because it contains non-printable\n                       characters."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ipv4", 1), ("ascii", 2), ("hex", 3))

class TmnxDhcpVendorOption(TextualConvention, Bits):
    description = 'This value specifies what is encoded in the Alcatel vendor specific\n         sub-option of option 82.'
    status = 'current'
    namedValues = NamedValues(("systemId", 0), ("clientMac", 1), ("serviceId", 2), ("sapId", 3))

class TmnxPppoeUserNameOrEmpty(TextualConvention, OctetString):
    description = 'The data type TmnxPppoeUserNameOrEmpty denotes the PPPoE username.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class TCpmProtPolicyID(TextualConvention, Unsigned32):
    description = "The data type TCpmProtPolicyID represents the identification number \n         of a CPM Protection policy.\n        \n         The value '0' indicates that no CPM Protection policy is provisioned."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TMlpppQoSProfileId(TextualConvention, Unsigned32):
    description = 'This textual-convention uniquely identifies MLPPP Bundle QoS\n        profile in the ingress and egress MLPPP QoS profile tables. \n        The value 0 indicates default MLPPP QoS Profile as applicable to\n        a given H/W'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

mibBuilder.exportSymbols("ALCATEL-IND1-TIMETRA-TC-MIB", TPortSchedulerPIR=TPortSchedulerPIR, TmnxVRtrMplsLspID=TmnxVRtrMplsLspID, TmnxBgpRouteTarget=TmnxBgpRouteTarget, TMlpppQoSProfileId=TMlpppQoSProfileId, TPIRRateOrZero=TPIRRateOrZero, TmnxTunnelID=TmnxTunnelID, TPolicyID=TPolicyID, TDSCPName=TDSCPName, TmnxVPNRouteDistinguisher=TmnxVPNRouteDistinguisher, QTag=QTag, TPolicyStatementNameOrEmpty=TPolicyStatementNameOrEmpty, TmnxBgpAutonomousSystem=TmnxBgpAutonomousSystem, TPIRRate=TPIRRate, TmnxAncpString=TmnxAncpString, TmnxBgpLocalPreference=TmnxBgpLocalPreference, TmnxVcIdOrNone=TmnxVcIdOrNone, TSapEgressPolicyID=TSapEgressPolicyID, QTagOrZero=QTagOrZero, TmnxMldGroupType=TmnxMldGroupType, TSecondaryShaper10GPIRRate=TSecondaryShaper10GPIRRate, TmnxMldVersion=TmnxMldVersion, TmnxIgmpGroupFilterMode=TmnxIgmpGroupFilterMode, TQueueId=TQueueId, TmnxCustId=TmnxCustId, TWeight=TWeight, timetraTCMIBModule=timetraTCMIBModule, TmnxSlaProfileStringOrEmpty=TmnxSlaProfileStringOrEmpty, TmnxDHCP6MsgType=TmnxDHCP6MsgType, TmnxTunnelType=TmnxTunnelType, TmnxSubIdentStringOrEmpty=TmnxSubIdentStringOrEmpty, TDSCPFilterActionValue=TDSCPFilterActionValue, TFrameType=TFrameType, TFCName=TFCName, TmnxIgmpGroupType=TmnxIgmpGroupType, TmnxVRtrID=TmnxVRtrID, TmnxBgpPreference=TmnxBgpPreference, TItemDescription=TItemDescription, TmnxOperState=TmnxOperState, TmnxSlaProfileString=TmnxSlaProfileString, TmnxEncapVal=TmnxEncapVal, ServiceAccessPoint=ServiceAccessPoint, TmnxDhcpOptionType=TmnxDhcpOptionType, TmnxActionType=TmnxActionType, TLspExpValue=TLspExpValue, TNamedItem=TNamedItem, TmnxManagedRouteStatus=TmnxManagedRouteStatus, TTcpUdpPort=TTcpUdpPort, TmnxAdminState=TmnxAdminState, TItemLongDescription=TItemLongDescription, TmnxAncpStringOrZero=TmnxAncpStringOrZero, TTcpUdpPortOperator=TTcpUdpPortOperator, TIpOption=TIpOption, TmnxEnabledDisabled=TmnxEnabledDisabled, TmnxMldGroupFilterMode=TmnxMldGroupFilterMode, TSapIngressPolicyID=TSapIngressPolicyID, TFCNameOrEmpty=TFCNameOrEmpty, TmnxPortID=TmnxPortID, TIngressQueueId=TIngressQueueId, PYSNMP_MODULE_ID=timetraTCMIBModule, TmnxAppProfileString=TmnxAppProfileString, TmnxStatus=TmnxStatus, TPIRRateOverride=TPIRRateOverride, TmnxSubProfileString=TmnxSubProfileString, TmnxVcType=TmnxVcType, TIpProtocol=TIpProtocol, TDSCPNameOrEmpty=TDSCPNameOrEmpty, TmnxVRtrIDOrZero=TmnxVRtrIDOrZero, ServiceAdminStatus=ServiceAdminStatus, TFCType=TFCType, TPortSchedulerCIR=TPortSchedulerCIR, Dot1PPriority=Dot1PPriority, TmnxBGPFamilyType=TmnxBGPFamilyType, TmnxVcId=TmnxVcId, IpAddressPrefixLength=IpAddressPrefixLength, SdpBindId=SdpBindId, TmnxIgmpVersion=TmnxIgmpVersion, TDSCPValue=TDSCPValue, TDSCPValueOrNone=TDSCPValueOrNone, TmnxStrSapId=TmnxStrSapId, TmnxSubProfileStringOrEmpty=TmnxSubProfileStringOrEmpty, TmnxDhcpVendorOption=TmnxDhcpVendorOption, TmnxMulticastAddrFamily=TmnxMulticastAddrFamily, TmnxSubIdentString=TmnxSubIdentString, TmnxSubMgtIntDestId=TmnxSubMgtIntDestId, TmnxServId=TmnxServId, TCpmProtPolicyID=TCpmProtPolicyID, TmnxSubMgtIntDestIdOrEmpty=TmnxSubMgtIntDestIdOrEmpty, TFCSet=TFCSet, TNamedItemOrEmpty=TNamedItemOrEmpty, TmnxAppProfileStringOrEmpty=TmnxAppProfileStringOrEmpty, TmnxOspfInstance=TmnxOspfInstance, ServiceOperStatus=ServiceOperStatus, TEgressQueueId=TEgressQueueId, TCIRRate=TCIRRate, InterfaceIndex=InterfaceIndex, TmnxPppoeUserNameOrEmpty=TmnxPppoeUserNameOrEmpty)
