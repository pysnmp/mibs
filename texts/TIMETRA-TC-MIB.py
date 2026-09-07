#
# PySNMP MIB module TIMETRA-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source TIMETRA-TC-MIB
# Source digest sha256:5a8bc9c19fa7d10cfdb25679434ecf3057a8b9a4b0da9d226c048d5d66596f15
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InetAddress, InetAddressIPv6, InetAddressPrefixLength, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressIPv6", "InetAddressPrefixLength", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
timetraModules, = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "timetraModules")
timetraTCMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 2))
timetraTCMIBModule.setRevisions(('2017-01-01 00:00', '2016-01-01 00:00', '2015-01-01 00:00', '2014-01-01 00:00', '2011-02-01 00:00', '2009-02-28 00:00', '2008-07-01 00:00', '2008-01-01 00:00', '2007-01-01 00:00', '2006-03-23 00:00', '2005-08-31 00:00', '2005-01-24 00:00', '2004-01-15 00:00', '2003-08-15 00:00', '2003-01-20 00:00', '2001-05-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timetraTCMIBModule.setRevisionsDescriptions(('Rev 15.0               1 Jan 2017 00:00\n         15.0 release of the TIMETRA-TC-MIB.', 'Rev 14.0               1 Jan 2016 00:00\n         14.0 release of the TIMETRA-TC-MIB.', 'Rev 13.0               1 Jan 2015 00:00\n         13.0 release of the TIMETRA-TC-MIB.', 'Rev 12.0               1 Jan 2014 00:00\n         12.0 release of the TIMETRA-TC-MIB.', 'Rev 9.0                1 Feb 2011 00:00\n         9.0 release of the TIMETRA-TC-MIB.', 'Rev 7.0                28 Feb 2009 00:00\n         7.0 release of the TIMETRA-TC-MIB.', 'Rev 6.1                01 Jul 2008 00:00\n         6.1 release of the TIMETRA-TC-MIB.', 'Rev 6.0                01 Jan 2008 00:00\n         6.0 release of the TIMETRA-TC-MIB.', 'Rev 5.0                01 Jan 2007 00:00\n         5.0 release of the TIMETRA-TC-MIB.', 'Rev 4.0                23 Mar 2006 00:00\n         4.0 release of the TIMETRA-TC-MIB.', 'Rev 3.0                31 Aug 2005 00:00\n         3.0 release of the TIMETRA-TC-MIB.', 'Rev 2.1                24 Jan 2005 00:00\n         2.1 release of the TIMETRA-TC-MIB.', 'Rev 2.0                15 Jan 2004 00:00\n         2.0 release of the TIMETRA-TC-MIB.', 'Rev 1.2                15 Aug 2003 00:00\n         1.2 release of the TIMETRA-TC-MIB.', 'Rev 1.0                20 Jan 2003 00:00\n         1.0 Release of the TIMETRA-TC-MIB.', 'Rev 0.1                14 Aug 2000 00:00\n         First version of the TIMETRA-TC-MIB.',))
if mibBuilder.loadTexts: timetraTCMIBModule.setLastUpdated('2017-01-01 00:00')
if mibBuilder.loadTexts: timetraTCMIBModule.setOrganization('Nokia')
if mibBuilder.loadTexts: timetraTCMIBModule.setContactInfo('Nokia SROS Support\n         Web: http://www.nokia.com')
if mibBuilder.loadTexts: timetraTCMIBModule.setDescription("This document is the SNMP MIB module for the SNMP Textual Conventions\n         (TCs) used in the Nokia SROS manageability instrumentation.\n\n         Copyright 2003-2018 Nokia. All rights reserved. Reproduction of this\n         document is authorized on the condition that the foregoing copyright\n         notice is included.\n\n         This SNMP MIB module (Specification) embodies Nokia's\n         proprietary intellectual property.  Nokia retains\n         all title and ownership in the Specification, including any\n         revisions.\n\n         Nokia grants all interested parties a non-exclusive license to use and\n         distribute an unmodified copy of this Specification in connection with\n         management of Nokia products, and without fee, provided this copyright\n         notice and license appear on all copies.\n\n         This Specification is supplied `as is', and Nokia makes no warranty,\n         either express or implied, as to the use, operation, condition, or\n         performance of the Specification.")
class TmnxFPNumber(TextualConvention, Unsigned32):
    description = 'The unique value that identifies the forwarding plane within a\n         specific IOM card in the system.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TmnxFPNumberOrZero(TextualConvention, Unsigned32):
    description = 'The unique value that identifies the forwarding plane within a\n         specific IOM card in the system.\n\n         Value 0 means this value is not applicable.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class InterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface\n         or interface sub-layer in the managed system.  It is\n         recommended that values are assigned contiguously\n         starting from 1.  The value for each interface sub-\n         layer must remain constant at least from one re-\n         initialization of the entity's network management\n         system to the next re-initialization."
    status = 'current'
    displayHint = 'd'

class TmnxPortID(TextualConvention, Unsigned32):
    description = "A portid is a unique 32 bit number with special encoding.\n\n         Refer to TIMETRA-CHASSIS-MIB::tmnxChassisPortIdScheme for a\n         description of the various port mapping schemes used by the system for\n         physical ports and channels.\n\n         Virtual ports and LAGs are encoded as:\n            32     29 | 28             10 | 9   1 |\n            +---------+-------------------+-------+\n            | 0 1 0 0 |   zeros           |   ID  | Virtual Port\n            +---------+-------------------+-------+\n\n            32     29 | 28             11 | 10  1 |\n            +---------+-------------------+-------+\n            | 0 1 0 1 |   zeros           |   ID  | LAG Port\n            +---------+-------------------+-------+\n\n         A card port number (cpn) has significance within the context\n         of the card on which it resides(i.e., cpn 2 may exist in one or\n         more cards in the chassis).  Whereas, portid is an\n         unique/absolute port number (apn) within a given chassis.\n\n         An 'invalid portid' is a TmnxPortID with a value of 0x1e000000 as\n         represented below.\n\n            32 30 | 29 26 | 25 22 | 21 16 | 15  1 |\n            +-----+-------+-------+-------+-------+\n            |zero | ones  | zero  |  zero |  zero | Invalid Port\n            +-----+-------+-------+-------+-------+"
    status = 'current'

class TmnxEncapVal(TextualConvention, Unsigned32):
    description = "The value of the label used to identify the entity using the specified\n         encapsulation value on a specific port.\n\n         The format of this object depends on the encapsulation type defined on\n         this port.\n\n         When the encapsulation is nullEncap the value of this object must be\n         zero.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |00000000 00000000 00000000 00000000|\n         +--------+--------+--------+--------+\n\n         When the encapsulation is dot1qEncap the value of this object is equal\n         to the 12-bit IEEE 802.1Q VLAN ID.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |00000000 00000000 0000XXXX XXXXXXXX|\n         +--------+--------+--------+--------+\n\n         Bit 31 is set to 0 in the case of tagged-VLAN.\n         Bit 31 is set to 1 in the case of dotq-CP as follows:\n         31                                   0\n         +--------+--------+--------+--------+\n         |10000000 00000000 0000XXXX XXXXXXXX|\n         +--------+--------+--------+--------+\n\n         When the encapsulation is mplsEncap the value of this object is equal\n         to the 20-bit LSP ID.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |00000000 0000XXXX XXXXXXXX XXXXXXXX|\n         +--------+--------+--------+--------+\n\n         When the encapsulation is frEncap, the value of this object is equal\n         to the 10-bit Frame Relay DLCI.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |00000000 00000000 000000XX XXXXXXXX|\n         +--------+--------+--------+--------+\n\n         When the encapsulation is qinqEncap, the value of the outer 802.1Q\n         VLAN ID is encoded in the least significant 16 bits, and the value of\n         the inner VLAN ID is encoded in the most significant 16 bits.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |0000YYYY YYYYYYYY 0000XXXX XXXXXXXX|\n         +--------+--------+--------+--------+\n\n         where:\n             - '*' is represented as 4095.\n             - '0' is represented as 0.\n             - any other value in between as a valid tag.\n             - '*.null' is represented in the following way:\n\n               31                                  0\n               +--------+--------+--------+--------+\n               |10000000 00000000 00001111 11111111|\n               +--------+--------+--------+--------+\n\n         Bit 30 is set to 0 in the case of tagged-qinq for the bottom tag.\n         Bit 30 is set to 1 in the case of qinq-CP with bottom tag.\n         Bit 15 is set to 0 in the case of tagged-qinq for the top tag.\n         Bit 15 is set to 1 in the case of qinq-CP with top tag as follows:\n         31                                   0\n         +--------+--------+--------+--------+\n         |0100YYYY YYYYYYYY 0100XXXX XXXXXXXX|\n         +--------+--------+--------+--------+\n\n         When the encapsulation is atmEncap, the value of the ATM VCI is\n         encoded in the least significant 16 bits, and the value of the ATM VPI\n         is encoded in the next 12 bits.\n\n         For ATM VCs, the top 3 bits are 000.  The value of\n         the ATM VCI is encoded in the least significant 16\n         bits, and the value of the ATM VPI is encoded in the next\n         12 bits.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |0000YYYY YYYYYYYY XXXXXXXX XXXXXXXX|\n         +--------+--------+--------+--------+\n\n         For ATM capture VCs, bits 0 and 28 are 1.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |00010000 00000000 00000000 00000001|\n         +--------+--------+--------+--------+\n\n         For ATM VPs, the top 3 bits are 010.  The value of\n         the ATM VPI is encoded in the least significant 12 bits.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |01000000 00000000 0000XXXX XXXXXXXX|\n         +--------+--------+--------+--------+\n\n         For ATM VP ranges, the top 3 bits are 100.  The value of\n         the start of the ATM VPI range is encoded in the least significant\n         12 bits, and the value of the end of the ATM VP range is encoded\n         in the next 12 bits.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |10000000 YYYYYYYY YYYYXXXX XXXXXXXX|\n         +--------+--------+--------+--------+\n\n         For ATM ports, the top 3 bits are 110, and the rest of the bits must\n         be zero.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |11000000 00000000 00000000 00000000|\n         +--------+--------+--------+--------+\n\n         For ATM CPs, the top 3 bits are 001.  The value of\n         the ATM CP is encoded in the least significant 13 bits.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |00100000 00000000 000XXXXX XXXXXXXX|\n         +--------+--------+--------+--------+\n\n         When the encapsulation is wanMirrorEncap the value of this object is\n         equal to the 12-bit value.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |00000000 00000000 0000XXXX XXXXXXXX|\n         +--------+--------+--------+--------+\n\n         Some ports have a restrictions to the encapsulation types that they\n         can support and hence impose restrictions on the respective formats\n         defined above."
    status = 'current'

class QTag(TextualConvention, Integer32):
    description = 'The QTag data type is a 12-bit integer tag used to identify\n         a service.  The values 0 and 4095 are not allowed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class QTagOrZero(TextualConvention, Unsigned32):
    description = "The data type QTagOrZero represents a VLAN tag.\n\n         The value '0' indicates that no VLAN tag is provisioned, or that its\n         value is unknown."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4094)

class QTagFullRange(TextualConvention, Unsigned32):
    description = 'The data type QTagFullRange represents a VLAN tag. A VLAN tag is 12\n         bits is size. The data type QTagFullRange covers the whole range of\n         possible values. (0..4095 or 0x0 .. 0xFFF)'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4095)

class QTagFullRangeOrNone(TextualConvention, Integer32):
    description = "The data type QTagFullRangeOrNone represents a VLAN tag. A VLAN tag is\n         12 bits is size. The data type QTagFullRange covers the whole range of\n         possible values. (0..4095 or 0x0 .. 0xFFF).\n\n         The value '-1' indicates the absence of a VLAN tag."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 4095), )
class TmnxSapAASubScope(TextualConvention, Integer32):
    description = 'The TmnxSapAASubScope data type is an enumerated integer\n         that specifies the scope of the AA subscriber.\n         Values:\n           none       (0) - The AA subscriber has no scope.\n           subscriber (1) - The AA subscriber has esm subscriber scope.\n           mac        (2) - The AA subscriber has esm MAC host scope.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("subscriber", 1), ("mac", 2))

class TmnxStrSapId(DisplayString):
    description = 'The value of TmnxStrSapId is a printable string which contains the\n         owner SAP Id or equivalent on a remote system.\n\n         The string should contain the printable string equivalent of the\n         textual conventions TmnxPortID and TmnxEncapVal in the format\n         specified as TmnxPortID[:TmnxEncapVal]'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class IpAddressPrefixLength(TextualConvention, Integer32):
    description = 'the number of bits to match in an IP address mask.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32)

class TmnxActionType(TextualConvention, Integer32):
    description = "The TmnxActionType data type is an enumerated integer\n         that describes the values used to support action or\n         operation style commands.  Setting a variable of this\n         type to 'doAction' causes the action to occur.  GETs and\n         GETNEXTs on this variable return 'not-applicable'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("doAction", 1), ("notApplicable", 2))

class TmnxAdminState(TextualConvention, Integer32):
    description = 'The TmnxAdminState data type is an enumerated integer that describes\n         the values used to identify the administratively desired state of\n         functional modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noop", 1), ("inService", 2), ("outOfService", 3))

class TmnxOperState(TextualConvention, Integer32):
    description = 'The TmnxOperState data type is an enumerated integer that describes\n         the values used to identify the current operational state of\n         functional modules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("inService", 2), ("outOfService", 3), ("transition", 4))

class TmnxStatus(TextualConvention, Integer32):
    description = "The TmnxStatus data type is an enumerated integer that describes the\n         values used to identify the current status of functional modules in the\n         system such as OSPF and MPLS protocols. Setting this variable to\n         'create' causes instantiation of the feature in the system.  Setting it\n         to 'delete' removes the instance and all associated configuration\n         information."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("create", 1), ("delete", 2))

class TmnxEnabledDisabledAdminState(TextualConvention, Integer32):
    description = "The TmnxEnabledDisabledAdminState data type is an enumerated integer\n         that describes the values used to identify whether an entity is\n         'enabled' or 'disabled'. It is to be used for admin state leafs."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class TmnxEnabledDisabled(TextualConvention, Integer32):
    description = "The TmnxEnabledDisabled data type is an enumerated integer that\n         describes the values used to identify whether an entity is 'enabled'\n         or 'disabled'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class TmnxEnabledDisabledOrNA(TextualConvention, Integer32):
    description = 'An object of type TmnxEnabledDisabledOrNA indicates if an entity is\n         enabled or disabled, or if enabled/disabled is not applicable to the\n         entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("notApplicable", 3))

class TmnxEnabledDisabledOrInherit(TextualConvention, Integer32):
    description = "The TmnxEnabledDisabledOrInherit data type is an enumerated integer\n         that describes the values used to identify whether an entity is\n         'enabled', 'disabled' or inherits its state from another object that\n         is usually in another mib table."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("inherit", 3))

class TmnxTimeInterval(TextualConvention, Unsigned32):
    description = 'The TmnxTimeInterval data type is used anywhere the SNMPv2-TC\n         TimeInterval TEXTUAL-CONVENTION can be used when an object requires\n         longer intervals than 248 days.\n\n         A period of time, measured in units of centiseconds.'
    status = 'current'

class TNamedItem(DisplayString):
    description = 'The name of an item.  When used as an index to a table, the item\n         name uniquely identifies the instance.  When used in a reference\n         (TNamedItemOrEmpty) the item name entry must exist in the table.\n\n         Note, use only NVT ASCII displayable characters here, no control\n         characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class TNamedItemOrEmpty(DisplayString):
    description = 'The name of an item, or an empty string.  When used in a reference\n         (TNamedItemOrEmpty) the item name entry must exist in the table.\n\n         Note, use only NVT ASCII displayable characters here, no control\n         characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), )
class TLNamedItem(DisplayString):
    description = 'The long name of an item.  When used as an index to a table, the item\n         name uniquely identifies the instance.  When used in a reference\n         (TLNamedItemOrEmpty) the item name entry must exist in the table.\n\n         Note, use only NVT ASCII displayable characters here, no control\n         characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 64)

class TLNamedItemOrEmpty(DisplayString):
    description = 'The long name of an item, or an empty string.  When used in a reference\n         (TLNamedItemOrEmpty) the item name entry must exist in the table.\n\n         Note, use only NVT ASCII displayable characters here, no control\n         characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 64), )
class TXLNamedItem(DisplayString):
    description = 'The extra long name of an item.  When used as an index to a table,\n         the item name uniquely identifies the instance. When used in a\n         reference (TXLNamedItemOrEmpty) the item name entry must\n         exist in the table.\n\n         Note, use only NVT ASCII displayable characters here, no control\n         characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 255)

class TXLNamedItemOrEmpty(DisplayString):
    description = 'The extra long name of an item, or an empty string.  When used in a\n         reference (TXLNamedItemOrEmpty) the item name entry must exist in\n         the table.\n\n         Note, use only NVT ASCII displayable characters here, no control\n         characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 255), )
class TItemDescription(DisplayString):
    description = 'Description for an item.  Note, use only NVT ASCII displayable characters\n         here, no control characters, no UTF-8, etc.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

class TItemLongDescription(DisplayString):
    description = 'Longer description for an item.  Note, use only NVT ASCII displayable\n         characters here, no control characters, no UTF-8, etc.'
    status = 'current'

class TRegularExpression(DisplayString):
    description = 'A regular expression string.'
    status = 'current'

class TmnxHttpRedirectUrl(DisplayString):
    description = "A string that represents an HTTP URL configured for HTTP redirection.\n\n         The string may contain a macro '$URL' that specifies substitution of\n         '$URL' by another string; the origin of that string is documented\n         where this textual convention is used.\n\n         The string may contain a macro '$MAC' that specifies substitution of\n         '$MAC' by another string, representing a MAC address; the origin of\n         that string is documented where this textual convention is used.\n\n         The string may contain a macro '$IP' that specifies substitution of\n         '$IP' by another string, representing an IP address; the origin of\n         that string is documented where this textual convention is used.\n\n         The string may contain a macro '$SUB' that specifies substitution of\n         '$SUB' by another string, representing an subscriber ID; the origin of\n         that string is documented where this textual convention is used.\n\n         The string may contain a macro '$SAP' that specifies substitution of\n         '$SAP' by another string, representing a SAP (Service Access Point);\n         the origin of that string is documented where this textual convention\n         is used.\n\n         The string may contain a macro '$SAPDESC' that specifies substitution\n         of '$SAPDESC' by another string; the origin of that string is\n         documented where this textual convention is used.\n\n         The string may contain a macro '$CID' that specifies substitution of\n         '$CID' by a bytestring, representing a circuit-id or interface-id; the\n         origin of that string is documented where this textual convention is\n         used.\n\n         The string may contain a macro '$RID' that specifies substitution of\n         '$RID' by a bytestring, representing a remote-id; the origin of that\n         string is documented where this textual convention is used.\n\n         Not all substitution macro's are supported in every situation; an\n         unsupported macro is ignored (substituted with nothing); the set of\n         supported macro's should be documented where this textual convention\n         is used."
    status = 'current'

class TmnxDisplayStringURL(DisplayString):
    description = "A string that represents an URL. If the URL contains login information\n         in the form of 'username:password' this login information will be\n         blanked out in the SNMP get response, by replacing the login\n         information with '*:*'."
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 180)

class TmnxVRtrID(TextualConvention, Integer32):
    description = 'A number used to identify a virtual router instance in the system.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 10240)

class TmnxVRtrIDOrZero(TextualConvention, Integer32):
    description = 'A number used to identify a virtual router instance in the system. The\n         number 0 will have special significance in the context the TC is used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10240)

class VRtrIgmpHostMcRDstStatType(TextualConvention, Integer32):
    description = 'The VRtrIgmpHostMcRDstStatType data type is an enumerated integer that\n         indicates a type of IGMP host mcast reporting destination statistics.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("joinTx", 1), ("joinDenyTx", 2), ("dropTx", 3), ("joinLost", 4), ("joinDenyLost", 5), ("dropLost", 6))

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
    description = 'A number used to identify a Customer or Subscriber. This ID must be\n         unique within the Service Domain. The value 0 is used as the null ID.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), )
class TmnxCustIdNoZero(TextualConvention, Unsigned32):
    description = 'A number used to identify a Customer or Subscriber. This ID must be\n         unique within the Service Domain.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class BgpPeeringStatus(TextualConvention, Integer32):
    description = 'The status of the BGP peering session.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("notApplicable", 0), ("installed", 1), ("notInstalled", 2), ("noEnhancedSubmgt", 3), ("wrongAntiSpoof", 4), ("parentItfDown", 5), ("hostInactive", 6), ("noDualHomingSupport", 7), ("invalidRadiusAttr", 8), ("noDynamicPeerGroup", 9), ("duplicatePeer", 10), ("maxPeersReached", 11), ("l2AwNotSupported", 12), ("gtpNotSupported", 13), ("genError", 14))

class TmnxRipListenerStatus(TextualConvention, Integer32):
    description = 'The status of the RIP Listener session.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("notApplicable", 0), ("active", 1), ("inactive", 2), ("noEnhancedSubmgt", 3), ("wrongAntiSpoof", 4), ("parentItfDown", 5), ("hostInactive", 6), ("l2AwNotSupported", 7), ("gtpNotSupported", 8), ("mcStandby", 9), ("ripDisabled", 10))

class TmnxServId(TextualConvention, Unsigned32):
    description = 'A number used to identify a Service. This ID must be unique within the\n         Service Domain. The value 0 is used as the null ID.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ValueRangeConstraint(2147483648, 2147483648), ValueRangeConstraint(2147483649, 2147483649), ValueRangeConstraint(2147483650, 2147483650), ValueRangeConstraint(2147483651, 2147483690), ValueRangeConstraint(2147483691, 2148007980), ValueRangeConstraint(2148007981, 2148012076), ValueRangeConstraint(2148012077, 2148016172), ValueRangeConstraint(2148016173, 2148278316), ValueRangeConstraint(2148278317, 2148278317), ValueRangeConstraint(2148278318, 2148278381), ValueRangeConstraint(2148278382, 2148278382), ValueRangeConstraint(2148278382, 2148278386), )
class TmnxExtServId(TextualConvention, Unsigned32):
    description = 'A number used to identify an external Service. This ID must be unique\n         within the Service Domain. The value 0 is used as the null ID.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), )
class TmnxAdminStateUpDown(TextualConvention, Integer32):
    description = 'TmnxAdminStateUpDown data type is an enumerated integer that describes\n         the values used to identify the administrative state of a snmp row.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class TmnxAdminStateTruthValue(TruthValue):
    description = "TmnxAdminStateTruthValue data type is an TruthValue object used to\n         identify the administrative state of a snmp row.\n\n         A value of 'true' means the snmp row is administrative 'up'."
    status = 'current'

class TruthValueNoTypeTranslator(TextualConvention, Integer32):
    description = 'Represents a boolean value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class ServiceAdminStatus(TextualConvention, Integer32):
    description = 'ServiceAdminStatus data type is an enumerated integer that describes\n         the values used to identify the administrative state of a service.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class ServiceOperStatus(TextualConvention, Integer32):
    description = 'ServiceOperStatus data type is an enumerated integer that describes\n         the values used to identify the current operational state of a\n         service.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class TPolicyID(TextualConvention, Unsigned32):
    description = 'The identification number of a policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 65535), ValueRangeConstraint(65536, 65536), ValueRangeConstraint(65537, 65537), ValueRangeConstraint(65538, 65538), ValueRangeConstraint(65539, 65539), )
class TTmplPolicyID(TextualConvention, Unsigned32):
    description = 'The identification number of a policy for template objects.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TQosIngressPolicyID(TPolicyID):
    description = 'The identification number of a QoS ingress policy.'
    status = 'current'

class TSapIngressPolicyID(TPolicyID):
    description = 'The identification number of a SAP ingress policy.'
    status = 'current'

class TSapEgressPolicyID(TPolicyID):
    description = 'The identification number of a SAP egress policy.'
    status = 'current'
    subtypeSpec = TPolicyID.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 65535), ValueRangeConstraint(65536, 65536), ValueRangeConstraint(65537, 65537), ValueRangeConstraint(65538, 65538), ValueRangeConstraint(65539, 65539), )
class TAnyQosPolicyID(TextualConvention, Unsigned32):
    description = "The identification number of QoS policy. Any value greater than 65535\n         indicates the policy was created by the system.\n\n         The format is:\n            +--------------------------------+\n            |<----C-----><-B><------A------->|\n            +--------------------------------+\n            31                               0\n\n         where:\n          A (16 bits) is the base policy identifier.\n          B (4 bits) is the 'policy type'.\n          C (12 bits) is the auxiliary identifier.\n\n         When policy type = 0 (0000b), the acceptable range for base policy\n                                      identifier is 1..65535. This is the user\n                                      configured values.\n         When policy type = 1 (0001b)  [NAT/LNS], the acceptable range for base\n                                      policy identifier is 0..3. These policies\n                                      are considered 'internal' and cannot be\n                                      created or modified by the user.\n         When policy type = 2 (0010b)  The auxiliary identifier represents\n                                      internal policies that are created\n                                      by the system based on dynamic flow based\n                                      requests from diameter and cannot be\n                                      modified by the user. These polices\n                                      ranges from 1..2047. For all other policy\n                                      types, the auxiliary identifier must be\n                                      zero."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TAnyQosPolicyIDorZero(TextualConvention, Unsigned32):
    description = 'The identification number of QoS policy. Refer to the description of\n         the textual convention TAnyQosPolicyID for more info on how this\n         number is to be interpreted.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class TSdpIngressPolicyID(TPolicyID):
    description = 'The identification number of a SDP ingress network policy.'
    status = 'current'

class TSdpEgressPolicyID(TPolicyID):
    description = 'The identification number of a SDP egress network policy.'
    status = 'current'

class TQosQGrpInstanceIDorZero(TextualConvention, Unsigned32):
    description = "The identification number of a QoS queue group instance.\n\n         The value of '0' indicates the system determined default value."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxCreateOrigin(TextualConvention, Integer32):
    description = 'The TmnxCreateOrigin indicates the entity that created the entry.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 26))
    namedValues = NamedValues(("manual", 1), ("bgp-l2vpn", 2), ("radius", 3), ("bgpSignalL2vpn", 4), ("multiSegmentPW", 5), ("vplsPmsi", 6), ("dynScript", 7), ("bof", 8), ("bgpSignalVpws", 9), ("vsd", 12), ("evpn", 13), ("vsd-sd", 14), ("satellites", 15), ("fpe", 16), ("evpnIsa", 17), ("greBridged", 18), ("tli", 19), ("pdn", 20), ("ipsec", 23), ("reserved24", 24), ("reserved25", 25), ("manual-mci", 26))

class TmnxBsxTransitIpPolicyId(TextualConvention, Unsigned32):
    description = 'TmnxBsxTransitIpPolicyId identifies a transit IP policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TmnxBsxTransitIpPolicyIdOrZero(TextualConvention, Unsigned32):
    description = "TmnxBsxTransitIpPolicyId identifies a transit ip policy.\n\n         The value '0' indicates an invalid transit IP policy."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxBsxTransPrefPolicyId(TextualConvention, Unsigned32):
    description = 'TmnxBsxTransPrefPolicyId identifies a transit prefix policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TmnxBsxTransPrefPolicyIdOrZero(TextualConvention, Unsigned32):
    description = "TmnxBsxTransPrefPolicyId identifies a transit prefix policy.\n\n         The value '0' indicates an invalid transit prefix policy."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxBsxAarpId(TextualConvention, Unsigned32):
    description = 'TmnxBsxAarpId identifies an instance of the AA Redundancy Protocol\n         (AARP).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TmnxBsxAarpIdOrZero(TextualConvention, Unsigned32):
    description = "TmnxBsxAarpIdOrZero identifies an instance of the AA Redundancy\n         Protocol (AARP).\n\n         The value of '0' indicates an invalid AARP instance."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TmnxBsxAarpServiceRefType(TextualConvention, Integer32):
    description = "TmnxBsxAarpServiceRefType identifies the role of the SAP or Spoke SDP\n         service point being referenced by an AARP instance. This reference is\n         made in the context of a AARP instance identified by\n         TmnxBsxAarpIdOrZero.\n\n         The service reference types are:\n\n         none(0)                - service reference type is not applicable.\n\n         dualHomed(1)           - the service reference point is a SAP or\n                                  Spoke SDP connected into a dually homed\n                                  network being protected by the AARP instance.\n\n         shuntSubscriberSide(2) - the service reference point is a Spoke SDP\n                                  acting as a subscriber side shunt used by\n                                  the AARP instance. A subscriber side shunt\n                                  carries the local from/to subscriber\n                                  traffic when AA is performed remotely.\n\n         shuntNetworkSide(3)    - the service reference point is a Spoke SDP\n                                  acting as a network side shunt used by\n                                  the AARP instance. A network side shunt\n                                  carries the local from/to network\n                                  traffic when AA is performed remotely.\n\n         dualHomedSecondary(4)  - the secondary service reference point is a\n                                  SAP or Spoke SDP connected into a dually\n                                  homed network being protected by the AARP\n                                  instance. It functions as a backup to the\n                                  'dualHomed(1)' primary reference point.\n\n         For the case when TmnxBsxAarpIdOrZero refers to the invalid AARP\n         instance '0', the service reference type is 'none(0)'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("dualHomed", 1), ("shuntSubscriberSide", 2), ("shuntNetworkSide", 3), ("dualHomedSecondary", 4))

class TmnxBsxIsaAaGroupIndexOrZero(TextualConvention, Unsigned32):
    description = 'TmnxBsxIsaAaGroupIndexOrZero is an index of a group of BSX MDAs. The\n         value of zero indicates that no BSX MDA group is specified.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxBsxAaGrpPartIndexOrZero(TextualConvention, Unsigned32):
    description = "TmnxBsxAaGrpPartIndexOrZero is an index of an Application Assurance\n         partition within an Application Assurance group, and is a unique\n         32-bit number encoded as follows.\n\n         | 32   25 | 24    9 | 8      1 |\n         +---------+---------+----------+\n         |    0    | partidx |  groupidx|  Partition Index\n         +---------+---------+----------+\n\n         - groupidx represents a group of ISA MDAs and has\n          a valid range from 1..255. The corresponding\n          TmnxBsxIsaAaGroupIndex must already exist in the\n          tmnxBsxIsaAaGrpTable.\n\n         - partidx represents a partition within a group and\n          has a valid range from 0..65535. A partition index\n          of '0' represents group wide information.\n\n         The value of zero indicates that no Application Assurance partition is\n         specified"
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16777215)

class TSapEgrEncapGrpQosPolicyIdOrZero(TextualConvention, Unsigned32):
    description = "TSapEgrEncapGrpQosPolicyIdOrZero identifies SAP egress Encapsulation\n         group QoS policy.\n\n         The value '0' indicates no QoS policy is set."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TSapEgrEncapGroupType(TextualConvention, Integer32):
    description = 'TSapEgrEncapGroupType identifies Encapsulation group type on SAP\n         egress.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("isid", 1))

class TSapEgrEncapGroupActionType(TextualConvention, Integer32):
    description = 'TSapEgrEncapGroupActionType identifies Encapsulation group action type\n         on SAP egress. It is used to create or destroy row entries in an\n         associated table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("create", 1), ("destroy", 2))

class TPerPacketOffset(TextualConvention, Integer32):
    description = 'The value, in bytes, of the adjustment to make to the size of each\n         packet for accounting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32, 31)

class TPerPacketOffsetOvr(TextualConvention, Integer32):
    description = 'The value, in bytes, of the override of the adjustment to make to the\n         size of each packet for accounting. A value of -128 indicates no\n         override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-128, -128), ValueRangeConstraint(-32, 31), )
class TIngressHsmdaPerPacketOffset(TextualConvention, Integer32):
    description = 'The value, in bytes, of the adjustment to make to the size of each\n         incoming packet for accounting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32, 31)

class TIngHsmdaPerPacketOffsetOvr(TextualConvention, Integer32):
    description = 'The value, in bytes, of the override of the adjustment to make to the\n         size of each incoming packet for accounting. A value of -128 indicates\n         no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-128, -128), ValueRangeConstraint(-32, 31), )
class TEgressQPerPacketOffset(TextualConvention, Integer32):
    description = 'The value, in bytes, of the adjustment to make to the size of each\n         packet for accounting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-64, 32)

class TEgressPerPacketOffset(TextualConvention, Integer32):
    description = 'The value, in bytes, of the adjustment to make to the size of each\n         packet for accounting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-64, 31)

class TEgressPerPacketOffsetOvr(TextualConvention, Integer32):
    description = 'The value, in bytes, of the override for the adjustment to make to the\n         size of each packet for accounting. A value of -128 indicates no\n         override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-128, -128), ValueRangeConstraint(-64, 31), )
class TEgressHsmdaPerPacketOffset(TextualConvention, Integer32):
    description = 'The value, in bytes, of the adjustment to make to the size of each\n         outgoing packet for accounting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-64, 31)

class TEgrHsmdaPerPacketOffsetOvr(TextualConvention, Integer32):
    description = 'The value, in bytes, of the override of the adjustment to make to the\n         size of each outgoing packet for accounting. A value of -128 indicates\n         no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-128, -128), ValueRangeConstraint(-64, 31), )
class TIngressQPerPacketOffset(TextualConvention, Integer32):
    description = 'The value, in bytes, of the adjustment to make to the size of each\n         incoming packet for accounting.\n\n         Only even values are supported.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32, 30)

class THsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    description = 'The identification number of a HSMDA  counter.\n         The value 0 indicates an undefined counter id.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class THsmdaCounterIdOrZeroOrAll(TextualConvention, Integer32):
    description = 'The identification number of a HSMDA  counter.\n         The value (0) indicates an undefined counter id.\n         The value (-1) is used to indicate all counters.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TIngressHsmdaCounterId(TextualConvention, Unsigned32):
    description = 'The identification number of a HSMDA ingress counter.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TIngressHsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    description = 'The identification number of a HSMDA ingress counter. The value 0\n         indicates an undefined counter id.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgressHsmdaCounterId(TextualConvention, Unsigned32):
    description = 'The identification number of a HSMDA egress counter.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

class TEgressHsmdaCounterIdOrZero(TextualConvention, Unsigned32):
    description = 'The identification number of a HSMDA egress counter. The value 0\n         indicates an undefined counter id.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgrRateModType(TextualConvention, Integer32):
    description = 'The data type TEgrRateModType represents the type of egress-rate\n         modification that is to be applied.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("aggRateLimit", 2), ("namedScheduler", 3))

class TPolicyStatementName(TNamedItem):
    description = 'The name of a policy statement, when used as index in a table.'
    status = 'current'

class TPolicyStatementNameOrEmpty(TNamedItemOrEmpty):
    description = 'The name of a policy statement, when an object refers to it.'
    status = 'current'

class TLPolicyStatementNameOrEmpty(TLNamedItemOrEmpty):
    description = 'The long name of a policy statement, when an object refers to it.'
    status = 'current'

class TLPolicyNameOrExpOrEmpty(TLNamedItemOrEmpty):
    description = "The long name of a policy statement or an expression or an empty\n         string.\n\n         A logical expression contains terms and operators and can contain\n         sub-expressions enclosed in round brackets.\n\n         A term is a string of type TPolicyStatementName.\n\n         An operator can be the string 'AND', 'OR', and 'NOT'."
    status = 'current'

class TXLPolicyNameOrExpOrEmpty(TXLNamedItemOrEmpty):
    description = "The extra long name of a policy statement or an expression or an empty\n         string.\n\n         A logical expression contains terms and operators and can contain\n         sub-expressions enclosed in round brackets.\n\n         A term is a string of type TPolicyStatementName.\n\n         An operator can be the string 'AND', 'OR', and 'NOT'."
    status = 'current'

class TmnxVcType(TextualConvention, Integer32):
    description = "The value of TmnxVcType is an enumerated integer that indicates a\n         Virtual Circuit (VC) type. 'frDlciMartini(1)' replaces the old\n         'frDlci' when used over martini tunnels."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 9, 10, 11, 17, 18, 19, 20, 21, 23, 25, 4096))
    namedValues = NamedValues(("frDlciMartini", 1), ("atmSdu", 2), ("atmCell", 3), ("ethernetVlan", 4), ("ethernet", 5), ("atmVccCell", 9), ("atmVpcCell", 10), ("ipipe", 11), ("satopE1", 17), ("satopT1", 18), ("satopE3", 19), ("satopT3", 20), ("cesopsn", 21), ("cesopsnCas", 23), ("frDlci", 25), ("mirrorDest", 4096))

class TmnxVcId(TextualConvention, Unsigned32):
    description = 'A 32 bit number is used to identify a VC(Virtual Circuit). The VC ID\n         cannot be 0.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TmnxVcIdOrNone(TextualConvention, Unsigned32):
    description = 'A 32 bit number is used to identify a VC(Virtual Circuit). A value of\n         0 indicates no VC ID is configured or available.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class DateAndTimeOrEmpty(TextualConvention, OctetString):
    description = 'An object of type DateAndTimeOrEmpty data type contains a date-time\n         specification as in SNMPv2-TC::DateAndTime, or is empty'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class ClassIndex(TextualConvention, Unsigned32):
    description = 'Source/Destination class index.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class ClassIndexOrNone(TextualConvention, Unsigned32):
    description = 'Source/Destination class index or none(0).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 255), )
class Dot1PPriority(TextualConvention, Integer32):
    description = 'IEEE 802.1p priority.  zero is lowest, seven is highest.\n         -1 means not set'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class Dot1PPriorityMask(TextualConvention, Integer32):
    description = 'IEEE 802.1p priority mask.  zero is lowest, seven is highest.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class Dot1PPriorityNonZeroMask(TextualConvention, Integer32):
    description = 'IEEE 802.1p priority mask.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 7)

class ServiceAccessPoint(TextualConvention, Integer32):
    reference = 'assigned numbers:  http://www.iana.org/assignments/ieee-802-numbers'
    description = '802.2 LLC SAP value, Source and Destination.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TLspExpValue(TextualConvention, Integer32):
    description = 'MPLS Experimental bits. -1 means not set.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class TIpProtocol(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/protocol-numbers'
    description = 'IP protocol number. Well known protocol numbers include ICMP(1),\n         TCP(6), UDP(17).\n\n         -1 means value not set.\n         -2 indicates protocol wildcard for UDP and TCP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TIpProtocolNumber(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/protocol-numbers'
    description = 'IP protocol number.\n\n         Well known protocol numbers include ICMP(1), TCP(6), UDP(17).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class TIpOption(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/ip-parameters'
    description = 'IP packet options octet.  explanation of the octet bits:\n\n         IP OPTION NUMBERS\n\n         The Internet Protocol (IP) has provision for optional header fields\n         identified by an option type field.  Options 0 and 1 are exactly one\n         octet which is their type field.  All other options have their one\n         octet type field, followed by a one octet length field, followed by\n         length-2 octets of option data.  The option type field is subdivided\n         into a one bit copied flag, a two bit class field, and a five bit\n         option number.  These taken together form an eight bit value for the\n         option type field.  IP options are commonly referred to by this value.\n\n\n         Copy Class Number Value Name                Reference\n         ---- ----- ------ ----- ------------------------------- ---------\n            0     0      0     0 EOOL   - End of Options List    [RFC791,JBP]\n            0     0      1     1 NOP    - No Operation           [RFC791,JBP]\n            1     0      2   130 SEC    - Security                  [RFC1108]\n            1     0      3   131 LSR    - Loose Source Route     [RFC791,JBP]\n            0     2      4    68 TS     - Time Stamp             [RFC791,JBP]\n            1     0      5   133 E-SEC  - Extended Security         [RFC1108]\n            1     0      6   134 CIPSO  - Commercial Security           [???]\n            0     0      7     7 RR     - Record Route           [RFC791,JBP]\n            1     0      8   136 SID    - Stream ID              [RFC791,JBP]\n            1     0      9   137 SSR    - Strict Source Route    [RFC791,JBP]\n            0     0     10    10 ZSU    - Experimental Measurement      [ZSu]\n            0     0     11    11 MTUP   - MTU Probe                 [RFC1191]*\n            0     0     12    12 MTUR   - MTU Reply                 [RFC1191]*\n            1     2     13   205 FINN   - Experimental Flow Control    [Finn]\n            1     0     14   142 VISA   - Experimental Access Control [Estrin]\n            0     0     15    15 ENCODE - ???                      [VerSteeg]\n            1     0     16   144 IMITD  - IMI Traffic Descriptor        [Lee]\n            1     0     17   145 EIP    - Extended Internet Protocol[RFC1385]\n            0     2     18    82 TR     - Traceroute        [RFC1393]\n            1     0     19   147 ADDEXT - Address Extension    [Ullmann IPv7]\n            1     0     20   148 RTRALT - Router Alert              [RFC2113]\n            1     0     21   149 SDB    - Selective Directed Broadcast[Graff]\n            1     0     22   150 NSAPA  - NSAP Addresses          [Carpenter]\n            1     0     23   151 DPS    - Dynamic Packet State        [Malis]\n            1     0     24   152 UMP    - Upstream Multicast Pkt. [Farinacci]\n\n         [Note, an asterisk (*) denotes an obsoleted IP Option Number.]\n            '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class TIcmpTypeOrNone(TextualConvention, Integer32):
    reference = 'www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml#icmp-parameters-types'
    description = 'ICMP type.\n\n         The value -1 means ICMP type is not set.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TIcmpCodeOrNone(TextualConvention, Integer32):
    reference = 'www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml#icmp-parameters-codes'
    description = 'ICMP code.\n\n         The value -1 means ICMP code is not set.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TTcpUdpPort(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/port-numbers'
    description = 'The number of a TCP or UDP port. Well known port numbers include\n         ftp-data(20), ftp(21), telnet(23), smtp(25), http(80), pop3(110),\n         nntp(119), snmp(161), snmptrap(162), etc.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class TOperator(TextualConvention, Integer32):
    description = "The operator specifies the manner in which a couple of other MIB\n         objects in the table are supposed to be used.\n\n         Operator        Value1               Value2\n         ----------------------------------------------------\n         none(0)         Any(0)               Any(0)\n         eq(1)           Specified Value      Any(0)\n         range(2)        Starting Value       Ending Value\n         lt(3)           Specified Value      Any(0)\n         gt(4)           Specified Value      Any(0)\n\n         'Any(0)' specifies that, this object can accept any values\n          but would default to 0. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("eq", 1), ("range", 2), ("lt", 3), ("gt", 4))

class TTcpUdpPortOperator(TOperator):
    description = 'The operator used for checking on TCP/UDP ports values and ranges'
    status = 'current'

class TFrameType(TextualConvention, Integer32):
    description = 'The type of the frame for which this mac filter match criteria is\n         defined.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5))
    namedValues = NamedValues(("e802dot3", 0), ("e802dot2LLC", 1), ("e802dot2SNAP", 2), ("ethernetII", 3), ("atm", 5))

class TQueueId(TextualConvention, Integer32):
    description = 'The value of TQueueId specifies the identification number of a\n         queue.  A value of zero (0) indicates that no specific queue\n         identification has been assigned for this object. When an object\n         of type TQueueId is an SNMP table index, an index value of zero\n         (0) is not allowed and a noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TQueueIdOrAll(TextualConvention, Integer32):
    description = "The value of TQueueIdOrAll specifies the identification number of a\n         queue\n\n         A value of zero (0) indicates that no specific queue identification\n         has been assigned for this object.\n\n         A value of (-1) indicates 'all queues'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TIngressQueueId(TextualConvention, Integer32):
    description = 'The value of TIngressQueueId specifies the identification number\n         of an ingress queue.  A value of zero (0) indicates that no\n         specific queue identification has been assigned for this object.\n         When an object of type TIngressQueueId is an SNMP table index,\n         an index value of zero (0) is not allowed and a noCreation error\n         will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TEgressQueueId(TextualConvention, Integer32):
    description = 'The value of TEgressQueueId specifies the identification number\n         of an egress queue.  A value of zero (0) indicates that no\n         specific queue identification has been assigned for this object.\n         When an object of type TEgressQueueId is an SNMP table index,\n         an index value of zero (0) is not allowed and a noCreation error\n         will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TIngressHsmdaQueueId(TextualConvention, Integer32):
    description = 'The value of TIngressHsmdaQueueId specifies the identification number\n         of a HSMDA ingress queue.  A value of zero (0) indicates that no\n         specific queue identification has been assigned for this object.\n         When an object of type TIngressHsmdaQueueId is an SNMP table index,\n         an index value of zero (0) is not allowed and a noCreation error\n         will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgressHsmdaQueueId(TextualConvention, Integer32):
    description = 'The value of TEgressHsmdaQueueId specifies the identification number\n         of a HSMDA egress queue.  A value of zero (0) indicates that no\n         specific queue identification has been assigned for this object.\n         When an object of type TEgressHsmdaQueueId is an SNMP table index,\n         an index value of zero (0) is not allowed and a noCreation error\n         will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class THsmdaSchedulerPolicyGroupId(TextualConvention, Integer32):
    description = 'The value of THsmdaSchedulerPolicyGroupId specifies the identification\n         number of a HSMDA scheduler policy group.  A value of zero (0)\n         indicates that no specific group identification has been assigned for\n         this object. When an object of type THsmdaSchedulerPolicyGroupId is\n         an SNMP table index, an index value of zero (0) is not allowed and a\n         noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2), )
class THsmdaPolicyIncludeQueues(TextualConvention, Integer32):
    description = 'The value of THsmdaPolicyIncludeQueues specifies which queues are to\n         be scheduled in the same class in a HSMDA scheduler.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("q1to2", 1), ("q1to3", 2))

class THsmdaPolicyScheduleClass(TextualConvention, Integer32):
    description = 'The value of THsmdaPolicyScheduleClass the class at which the queues\n         specified by THsmdaPolicyIncludeQueues in a HSMDA scheduler.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3)

class TDSCPName(TNamedItem):
    description = 'The name of a Differential Services Code Point value.'
    status = 'current'

class TDSCPNameOrEmpty(TNamedItemOrEmpty):
    description = 'The name of a Differential Services Code Point value.'
    status = 'current'

class TDSCPValue(TextualConvention, Integer32):
    description = 'The value of a Differential Services Code Point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

class TDSCPValueOrNone(TextualConvention, Integer32):
    description = 'The value of a Differential Services Code Point (DSCP). A value of -1\n         means that no DSCP value is configured or available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 63), )
class TDSCPFilterActionValue(TextualConvention, Integer32):
    description = 'The value of a Differential Services Code Point. -1 means not set.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TFCName(TNamedItem):
    description = 'The name of a Forwarding Class entry.'
    status = 'current'

class TFCNameOrEmpty(TNamedItemOrEmpty):
    description = 'The name of a Forwarding Class entry.'
    status = 'current'

class TFCSet(TextualConvention, Bits):
    description = 'This data type describes a set of Forwarding Classes.'
    status = 'current'
    namedValues = NamedValues(("be", 0), ("l2", 1), ("af", 2), ("l1", 3), ("h2", 4), ("ef", 5), ("h1", 6), ("nc", 7))

class TFCType(TextualConvention, Integer32):
    description = 'This data type enumerates the Forwarding Classes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("be", 0), ("l2", 1), ("af", 2), ("l1", 3), ("h2", 4), ("ef", 5), ("h1", 6), ("nc", 7))

class TFCTypeOrNone(TextualConvention, Integer32):
    description = 'This data type enumerates the Forwarding Classes.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", -1), ("be", 0), ("l2", 1), ("af", 2), ("l1", 3), ("h2", 4), ("ef", 5), ("h1", 6), ("nc", 7))

class TmnxTunnelType(TextualConvention, Integer32):
    description = 'The type of this tunnel entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("sdp", 1), ("ldp", 2), ("rsvp", 3), ("gre", 4), ("bypass", 5), ("invalid", 6), ("bgp", 7))

class TmnxTunnelID(TextualConvention, Unsigned32):
    description = 'The identifying value for a BGP-VPRN tunnel.  Depending on the\n         tunnel type the associated tunnel id may be an sdp-id, an LSP ID\n         or zero(0).'
    status = 'current'

class TmnxBgpRouteTarget(TextualConvention, OctetString):
    description = 'TmnxBgpRouteTarget is an readable string that specifies the extended\n         community name to be accepted by a Route Reflector Server or\n         advertised by the router when reflecting any routes. I.e, it does not\n         apply to routes that are not reflected by the router.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxVPNRouteDistinguisher(TextualConvention, OctetString):
    description = 'The VPRN route distinguisher is a 8-octet object. It contains a\n         2-octet type field followed by a 6-octet value field. The type field\n         specify how to interpret the value field.\n\n         Type 0 specifies two subfields as a 2-octet administrative field and a\n         4-octet assigned number subfield.\n\n         Type 1 specifies two subfields as a 4-octet administrative field which\n         must contain an IP address and a 2-octet assigned number subfield.\n\n         Type 2 specifies two subfields as a 4-octet administrative field which\n         contains a 4-octet AS number and a 2-octet assigned number subfield.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class SdpBindId(TextualConvention, OctetString):
    description = 'The value used to uniquely identify an SDP Binding. The first four\n         octets correspond to the zero-extended 16-bit SDP ID, while the\n         remaining four octets correspond to the 32-bit VC ID, both encoded in\n         network byte order.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TmnxVRtrMplsLspID(TextualConvention, Unsigned32):
    description = 'A unique value for each Label Switched Path in the managed system.\n\n         The higher range IDs are used for segment routing LSPs.\n\n         The lower range IDs are used for regular LSPs.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 65535), ValueRangeConstraint(65536, 131070), )
class TmnxVRtrMplsLspIDNoZero(TextualConvention, Unsigned32):
    description = 'A unique value, greater than zero, for each Label Switched Path in the\n         managed system.\n\n         The higher range IDs are used for segment routing LSPs.\n\n         The lower range IDs are used for regular LSPs.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 65535), ValueRangeConstraint(65536, 131070), )
class TPortSchedulerPIR(TextualConvention, Integer32):
    description = 'The Peak Information Rate (PIR) rate to be used in kbps. The value -1\n         means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class TPortSchedulerAggRateLimitPIR(TextualConvention, Integer32):
    description = 'The Peak Information Rate (PIR) rate to be used in kbps. The value -1\n         means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 800000000), )
class TPortSchedulerPIRRate(TextualConvention, Integer32):
    description = 'The Peak Information Rate (PIR) rate to be used in kbps. The value -1\n         means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 800000000), )
class TPortSchedulerCIR(TextualConvention, Integer32):
    description = 'The Committed Information Rate (CIR) rate to be used in kbps. The\n         value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 800000000), )
class TPortQosPIRRate(TextualConvention, Unsigned32):
    description = 'The Peak Information Rate (PIR) rate to be used in kbps.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 10000)

class TPortQosCIRRate(TextualConvention, Unsigned32):
    description = 'The Committed Information Rate (CIR) rate to be used in kbps.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 10000)

class TWeight(TextualConvention, Integer32):
    description = 'The weight of the specified entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TWeightOverride(TextualConvention, Integer32):
    description = 'The weight of the specified entity while feeding into the parent. A\n         value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(0, 100), )
class TNonZeroWeight(TextualConvention, Integer32):
    description = 'The weight of the specified entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class TPolicerWeight(TextualConvention, Integer32):
    description = 'The relative weight of the specified entity while feeding into the\n         parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class THsWrrWeightOvr(TextualConvention, Integer32):
    description = 'The THsWrrWeightOvr data type specifies the override weight of the\n         corresponding HS queue feeding into its parent WRR scheduler. A value\n         of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 127), )
class THsClassWeightOverride(TextualConvention, Integer32):
    description = 'The THsClassWeightOverride data type specifies the weight of the\n         corresponding HS class feeding into its parent shaper. A value of -2\n         specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ValueRangeConstraint(4, 4), ValueRangeConstraint(8, 8), )
class THsmdaWeight(TextualConvention, Integer32):
    description = 'The weight of the specified HSMDA entity while feeding into the\n         parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class THsmdaWrrWeight(TextualConvention, Integer32):
    description = 'The weight of the specified HSMDA entity while feeding into the\n         parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 32)

class THsmdaWeightClass(TextualConvention, Integer32):
    description = 'The weight of the specified HSMDA entity while feeding into the\n         parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8))
    namedValues = NamedValues(("class1", 1), ("class2", 2), ("class4", 4), ("class8", 8))

class THsmdaWeightOverride(TextualConvention, Integer32):
    description = 'The weight of the specified HSMDA entity while feeding into the\n         parent. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 100), )
class THsmdaWrrWeightOverride(TextualConvention, Integer32):
    description = 'The weight of the specified HSMDA entity while feeding into the\n         parent. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 32), )
class TCIRRate(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THPolCIRRate(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2000000000), )
class TRateType(TextualConvention, Integer32):
    description = "The type of the PIR/CIR rate. The value 'kbps' means the rate is\n         specified in kbps. The value 'percent' means the rate is specified in\n         percentage"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("kbps", 1), ("percent", 2))

class TBWRateType(TextualConvention, Integer32):
    description = "The type of the PIR/CIR percent rate. The value 'kbps' means the rate\n         is specified in kbps. The value 'percentPortLimit' means the rate is\n         specified in percentage of port limit. The value 'percentLocalLimit'\n         means the rate is specified in percentage of local limit."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("kbps", 1), ("percentPortLimit", 2), ("percentLocalLimit", 3))

class TPSPRateType(TextualConvention, Integer32):
    description = "The type of the PIR/CIR rate being applied to port scheduler policy.\n         The value of 'kbps' means the rate is specified in kbps. The value of\n         'percentActivePortLimit' means the rate is specified in percentage of\n         active port bandwidth, that is, bandwidth of active ports in a LAG."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("kbps", 1), ("percentLocal", 2), ("percentLagActive", 3))

class TPolicerRateType(TextualConvention, Integer32):
    description = "The type of the PIR/CIR percent rate. The value 'kbps' means the rate\n         is specified in kbps. The value 'percentLocalLimit' means the rate is\n         specified in percentage of local limit."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("kbps", 1), ("percentLocalLimit", 2))

class TCIRRateOverride(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate. A\n         value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THPolCIRRateOverride(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate. A\n         value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2000000000), )
class TCIRPercentOverride(TextualConvention, Integer32):
    description = 'The CIR percentage rate specified in centipercent. A value of -2\n         specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(0, 10000), )
class THsmdaCIRKRate(TextualConvention, Integer32):
    description = 'The HSMDA CIR rate to be used in Kbps. The value -1 means maximum\n         rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THsmdaCIRKRateOverride(TextualConvention, Integer32):
    description = 'The HSMDA CIR rate to be used in Kbps. The value -1 means maximum\n         rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THsmdaCIRMRate(TextualConvention, Integer32):
    description = 'The HSMDA CIR rate to be used in Mbps. The value -1 means maximum\n         rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000), )
class THsmdaCIRMRateOverride(TextualConvention, Integer32):
    description = 'The HSMDA CIR rate to be used in Mbps. The value -1 means maximum\n         rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000), )
class TPIRRate(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class THPolVirtualSchePIRRate(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 800000000), )
class THPolVirtualScheCIRRate(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 800000000), )
class TAdvCfgRate(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100000000)

class TMaxDecRate(TextualConvention, Integer32):
    description = 'The Advanced Configuration policy Max-Decrement rate to be used in\n         kbps.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 100000000), )
class THPolPIRRate(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 2000000000), )
class TSecondaryShaper10GPIRRate(TextualConvention, Integer32):
    description = 'The secondary shaper PIR rate to be used in Mbps. The value -1 means\n         maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10000), )
class TExpSecondaryShaperPIRRate(TextualConvention, Integer32):
    description = 'The expanded secondary shaper PIR rate to be used in Kbps. The value\n         -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10000000), )
class TExpSecondaryShaperClassRate(TextualConvention, Integer32):
    description = 'The expanded secondary shaper class PIR rate to be used in Kbps. The\n         value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10000000), )
class TPIRRateOverride(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate. A\n         value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class TPIRAggRateLimitOverride(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate. A\n         value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 800000000), )
class THPolPIRRateOverride(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate. A\n         value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 2000000000), )
class TPIRPercentOverride(TextualConvention, Integer32):
    description = 'The PIR percentage rate specified in centipercent. A value of -2\n         specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 10000), )
class TPIRRateOrZero(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate. The\n         value 0 means undefined rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100000000), )
class THsmdaPIRKRate(TextualConvention, Integer32):
    description = 'The HSMDA PIR rate to be used in Kbps. The value -1 means maximum\n         rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class THsmdaPIRKRateOverride(TextualConvention, Integer32):
    description = 'The HSMDA PIR rate to be used in Kbps. The value -1 means maximum\n         rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class THsmdaPIRMRate(TextualConvention, Integer32):
    description = 'The HSMDA PIR rate to be used in Mbps. The value -1 means maximum\n         rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000), )
class THsmdaPIRMRateOverride(TextualConvention, Integer32):
    description = 'The HSMDA PIR rate to be used in Mbps. The value -1 means maximum\n         rate. A value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000), )
class TmnxDHCP6MsgType(TextualConvention, Integer32):
    description = 'The DHCP6 messagetype.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("dhcp6MsgTypeSolicit", 1), ("dhcp6MsgTypeAdvertise", 2), ("dhcp6MsgTypeRequest", 3), ("dhcp6MsgTypeConfirm", 4), ("dhcp6MsgTypeRenew", 5), ("dhcp6MsgTypeRebind", 6), ("dhcp6MsgTypeReply", 7), ("dhcp6MsgTypeRelease", 8), ("dhcp6MsgTypeDecline", 9), ("dhcp6MsgTypeReconfigure", 10), ("dhcp6MsgTypeInfoRequest", 11), ("dhcp6MsgTypeRelayForw", 12), ("dhcp6MsgTypeRelayReply", 13), ("dhcp6MsgTypeLeasequery", 14), ("dhcp6MsgTypeLeasequeryReply", 15))

class TmnxDhcpClientState(TextualConvention, Integer32):
    description = 'The state of a DHCP client.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("init", 0), ("init-reboot", 1), ("rebooting", 2), ("selecting", 3), ("requesting", 4), ("rebinding", 5), ("bound", 6), ("renewing", 7))

class TmnxIgpInstance(TextualConvention, Unsigned32):
    reference = "RFC 5838, 'Support of Address Families in OSPFv3', Section 2.1,\n         'Instance ID Values for New AFs'."
    description = 'An object of type TmnxIgpInstance identifies an instance of an\n         Interior Gateway Protocol (IGP).\n\n         Supported IGPs are Intermediate System to Intermediate System (IS-IS)\n         and Open Shortest Path First (OSPF).\n\n         The supported range varies with the IGP and address family, as\n         follows.\n\n         IGP      Address Family   Supported Range\n         ------   --------------   ---------------\n         IS-IS    all                        0..31\n         OSPFv2   all                        0..31\n         OSPFv3   IPv4 unicast              64..95\n         OSPFv3   IPv6 unicast               0..31 '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 31), ValueRangeConstraint(64, 95), )
class TmnxOspfInstance(TextualConvention, Unsigned32):
    description = 'A number used to identify an instance of OSPF,\n\n         For OSPFv2 only 0..31 is supported,\n\n         For OSPFv3 the range is divided in address families as follows:\n\n           0..31   ipv6-unicast address family (supported)\n           32..63  ipv6-multicast address family (not supported)\n           64..95  ipv4-unicast address family (supported)\n           96..127 ipv4-multicast address family (not supported)'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 127)

class TmnxBGPFamilyType(TextualConvention, Bits):
    description = 'The value of TmnxBGPFamilyType specifies the AFI-SAFI family for BGP\n         peer.'
    status = 'current'
    namedValues = NamedValues(("ipv4Unicast", 0), ("ipv4Multicast", 1), ("ipv4UastMcast", 2), ("ipv4MplsLabel", 3), ("ipv4Vpn", 4), ("ipv6Unicast", 5), ("ipv6Multicast", 6), ("ipv6UcastMcast", 7), ("ipv6MplsLabel", 8), ("ipv6Vpn", 9), ("l2Vpn", 10), ("ipv4Mvpn", 11), ("msPw", 12), ("ipv4Flow", 13), ("mdtSafi", 14), ("routeTarget", 15), ("mcastVpnIpv4", 16), ("mvpnIpv6", 17), ("ipv6Flow", 18), ("evpn", 19), ("bgpLs", 20), ("mcastVpnIpv6", 21), ("srplcyIpv4", 22), ("srplcyIpv6", 23))

class TmnxIgmpGroupFilterMode(TextualConvention, Integer32):
    description = "The data type TmnxIgmpGroupFilterMode describes the filter-mode of a\n         group.\n\n         In 'include(1)' mode, reception of packets sent to the specified\n         multicast address is requested only from those IPv4 Source addresses\n         listed in the corresponding source-list.\n\n         In 'exclude(2)' mode, reception of packets sent to the given multicast\n         address is requested from all IPv4 Source addresses, except those\n         listed in the corresponding source-list (if any)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("include", 1), ("exclude", 2))

class TmnxIgmpGroupType(TextualConvention, Integer32):
    description = 'The data type TmnxIgmpGroupType describes how a multicast group is\n         learned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class TmnxIgmpSnpgGroupType(TextualConvention, Integer32):
    description = 'The data type TmnxIgmpSnpgGroupType describes how a multicast  group\n         is learned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("static", 1), ("dynamic", 2), ("bgp-smet", 3))

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
    description = 'The data type TmnxManagedRouteStatus denotes the status of a Managed\n         Route.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("installed", 0), ("notYetInstalled", 1), ("wrongAntiSpoofType", 2), ("outOfMemory", 3), ("shadowed", 4), ("routeTableFull", 5), ("parentInterfaceDown", 6), ("hostInactive", 7), ("enhancedSubMgmtRequired", 8), ("deprecated1", 9), ("l2AwNotSupported", 10), ("nextHopLimitExceeded", 11), ("notApplicable", 12), ("noNextHop", 13), ("gtpNotSupported", 14))

class TmnxTunnelTypeExt(TextualConvention, Integer32):
    description = 'The type of this tunnel entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("invalid", 1), ("sdp", 2), ("rsvp", 3), ("ldp", 4), ("ospf", 5), ("isis", 6), ("bypass", 7), ("gre", 8), ("bgp", 9), ("srTe", 10), ("fpe", 11), ("udp", 12), ("ospfV3", 13), ("mplsFwdPolicy", 14), ("srPolicy", 15), ("ribApi", 16), ("reserved17", 17))

class TmnxIgpSCFamilyType(TextualConvention, Integer32):
    description = 'The data type to specify IGP shortcut tunnel next hop family.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ipv4", 0), ("ipv6", 1), ("srv4", 2), ("srv6", 3))

class TmnxAdjacencySetFamilyType(TextualConvention, Integer32):
    description = 'The data type to specify Adjacency Set family.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ipv4", 0), ("ipv6", 1))

class TmnxAncpString(DisplayString):
    description = 'The TmnxAncpString data type contains a valid ancp string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 63)

class TmnxAncpStringOrZero(DisplayString):
    description = 'The TmnxAncpStringOrZero data type contains a valid ancp string. An\n         empty string indicates that no ANCP string is defined.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 63)

class TmnxMulticastAddrFamily(TextualConvention, Integer32):
    description = 'The data type TmnxMulticastAddrFamily denotes the family for multicast\n         protocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ipv4Multicast", 0), ("ipv6Multicast", 1))

class TmnxNatIsaGrpId(TextualConvention, Unsigned32):
    description = 'The TmnxNatIsaGrpId data type contains an identification number for a\n         Network Address Translation Integrated Service Adaptor group.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4)

class TmnxNatIsaGrpIdOrZero(TextualConvention, Unsigned32):
    description = 'The TmnxNatIsaGrpIdOrZero data type contains an identification number\n         for a Network Address Translation Integrated Service Adaptor (ISA)\n         group.\n\n         The value zero means that no NAT ISA Group is defined.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4)

class TmnxNatL2AwAccessMode(TextualConvention, Integer32):
    description = "TmnxNatL2AwAccessMode is an enumerated integer that specifies the\n         Layer-2-Aware NAT access mode.\n\n         The value 'auto' means that the system automatically derives the\n         access mode from the configuration (of the access SAP)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("bridged", 2))

class TmnxNatSubscriberType(TextualConvention, Integer32):
    description = "TmnxNatSubscriberType is an enumerated integer that specifies the NAT\n         subscriber type.\n\n         The possible values are 'classicLsnSub' and 'dsliteLsnSub' for classic\n         and Dual Stack Lite Large Scale NAT subscribers respectively,\n         'l2AwareSub' for Layer-2-Aware NAT subscribers, and 'nat64LsnSub' for\n         NAT-64 subscribers respectively."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("l2AwareSub", 1), ("classicLsnSub", 2), ("dsliteLsnSub", 3), ("nat64LsnSub", 4))

class TmnxNatSubscriberTypeOrNone(TextualConvention, Integer32):
    description = "TmnxNatSubscriberTypeOrNone is an enumerated integer that specifies\n         the NAT subscriber type.\n\n         The value 'none' indicates that NAT subscriber type is not specified.\n\n         The values 'classicLsnSub' and 'dsliteLsnSub' are for classic and Dual\n         Stack Lite Large Scale NAT subscribers respectively. The value\n         'l2AwareSub' is for Layer-2-Aware NAT subscribers, and the value\n         'nat64LsnSub' is for NAT-64 subscribers."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("l2AwareSub", 1), ("classicLsnSub", 2), ("dsliteLsnSub", 3), ("nat64LsnSub", 4))

class TmnxNatWaterMark(TextualConvention, Unsigned32):
    description = 'The TmnxNatWaterMark data type contains an unsigned number that marks\n         a usage level in percent.\n\n         The value zero means that no watermark is defined.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

class TmnxAuthPassword(DisplayString):
    description = 'The TmnxAuthPassword data type contains a password used for\n         authentication of subscribers.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class TmnxAsciiSpecification(DisplayString):
    description = "The data type TmnxAsciiSpecification is a format string that specifies\n         how to form a target ASCII string.\n\n         The format is as follows:\n\n         <ascii-specification> ::= <char-specification>+\n\n         <char-specification>  ::= <ascii-char> | <char-origin>\n\n         <char-origin>         ::= '%' <origin>\n\n         <ascii-char> refers to a printable ASCII character.\n\n         Examples and supported char-origin specifiers are supplied with the\n         object definitions."
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class TmnxMacSpecification(DisplayString):
    description = "The data type TmnxMacSpecification is a string of ASCII characters\n         that specifies how to format a string that represents a MAC address.\n\n         The format is as follows:\n\n         <mac-specification> ::= <alpha-string> [<delimiter-char>]\n\n         <alpha-string>      ::= <ucase-alpha>+ | <lcase-alpha>+\n         <ucase-alpha>       ::= 'A' | 'B' | 'B' ... | 'Z'\n         <lcase-alpha>       ::= 'a' | 'b' | 'c' ... | 'z'\n\n         <delimiter-char>    any ASCII character that is not an <alpha-char>\n                            or a decimal digit\n\n         Only the number of alphabetic characters and the case is relevant.\n         Examples:\n\n         'ab:'               00:0c:f1:99:85:b8  Nokia SROS style\n         'XY-'               00-0C-F1-99-85-B8  IEEE canonical style\n         'mmmm.'             0002.03aa.abff     Cisco style.\n         'xx'                000cf19985b8"
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 17)

class TmnxBinarySpecification(DisplayString):
    description = "The data type TmnxBinarySpecification is a string of ASCII characters\n         that specifies how to form a binary number.\n\n         The format is as follows:\n\n         <binary-specification> ::= <bit-specification>+\n\n         <bit-specification>    ::= '0' | '1' | <bit-origin>\n\n         <bit-origin>           ::= '*' <number-of-bits> <origin>\n\n         <number-of-bits>       ::= [1..32]\n\n         Examples and supported bit-origin specifiers are supplied with the\n         object definitions."
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class TmnxDefSubIdSource(TextualConvention, Integer32):
    description = "The data type TmnxDefSubIdSource specifies what will be used as the\n         default subscriber identification.\n\n         This value is used in case no other source (like RADIUS) provides a\n         subscriber identification string.\n\n         If the value of this object is set to 'useSapId', the SAP-id will be\n         used as the default subscriber identification string.\n\n         If the value of this object is set to 'useAutoId', the auto-generated\n         subscriber identification string, as defined in\n         tmnxSubMgmtAutoSubIdObjs, is used as the default subscriber\n         identification string.\n\n         If the value of this object is set to 'useString', the value of the\n         string contained in another object will be used as the default\n         subscriber identification string; that object must be identified where\n         this datatype is used."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("useSapId", 1), ("useString", 2), ("useAutoId", 3))

class TmnxSubAuthPlcyUserNameOp(TextualConvention, Integer32):
    description = 'The TmnxSubAuthPlcyUserNameOp data type is an enumerated integer that\n         specifies the operation to perform on the user-name before sending it\n         to the RADIUS server.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("noOperation", 0), ("appendDomain", 1), ("stripDomain", 2), ("replaceDomain", 3), ("defaultDomain", 4))

class TmnxSubCallingStationIdType(TextualConvention, Integer32):
    description = "The TmnxSubCallingStationIdType data type is an enumerated integer that\n         specifies what string will be put in the RADIUS or DIAMETER Calling-Station-Id\n         attribute:\n         - sapString (1): the value of TIMETRA-SAP-MIB::sapCallingStationId of\n                          the subscriber host SAP;\n         - mac       (2): the subscriber host MAC address, formatted as a\n                          lower case ASCII string with octet values\n                          separated by a ':';\n         - sapId     (3): the subscriber host SAP identifier, formatted as\n                          an ASCII string.\n         - remoteId  (4): the intermediate agent Remote ID as received by means\n                          of, for example, a PPPoE vendor-specific tag,\n                          a DHCP Agent Remote ID Sub-option or\n                          an L2TP Access Line Agent-Remote-Id AVP.\n         - llid      (5): the logical link identifier as received during\n                          pre-authentication."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("sapString", 1), ("mac", 2), ("sapId", 3), ("remoteId", 4), ("llid", 5))

class TmnxSubAcctSessionId(DisplayString):
    description = 'The data type TmnxSubAcctSessionId contains a string that identifies a\n         subscriber for the purposes of accounting.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 22)

class TmnxSubHostGrouping(TextualConvention, Integer32):
    description = 'The TmnxSubHostGrouping data type is an enumerated integer that\n         indicates the way hosts associated with a given subscriber and SAP are\n         grouped together to share an SLA profile instance.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("perSap", 1), ("perGroup", 2), ("perSessionPpp", 3), ("perSessionIpoe", 4))

class TmnxSubIdentString(DisplayString):
    description = 'The data type TmnxSubIdentString denotes the subscriber identification\n         string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 64)

class TmnxSubIdentStringOrEmpty(DisplayString):
    description = 'The data type TmnxSubIdentStringOrEmpty denotes the subscriber\n         identification string. The empty string denotes the absence of a\n         subscriber identification string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class TmnxSubIdentShortString(DisplayString):
    description = 'The data type TmnxSubIdentShortString denotes the short subscriber\n         identification string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxSubRadServAlgorithm(TextualConvention, Integer32):
    description = 'The TmnxSubRadServAlgorithm data type is an enumerated integer that\n         indicates the algorithm used to access the list of configured RADIUS\n         servers:\n         - direct     (1): The first server will be used as primary server for\n                            all requests, the second as secondary and so on.\n         - roundRobin (2): The first server will be used as primary server for\n                            the first request, the second server as primary for\n                            the second request, and so on. If the router gets\n                            to the end of the list, it starts again with the\n                            first server.\n         - hashBased  (3): The server will be selected based on a specified\n                            hash value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("direct", 1), ("roundRobin", 2), ("hashBased", 3))

class TmnxSubRadIsaServAlgorithm(TextualConvention, Integer32):
    description = 'The TmnxSubRadIsaServAlgorithm data type is an enumerated integer that\n         indicates the algorithm used to access the list of configured RADIUS\n         servers:\n         - direct         (1): The first server will be used as primary server for\n                                all requests, the second as secondary and so on.\n         - roundRobin     (2): The first server will be used as primary server for\n                                the first request, the second server as primary for\n                                the second request, and so on. If the router gets\n                                to the end of the list, it starts again with the\n                                first server.\n         - hashBased      (3): The server will be selected based on a specified\n                                hash value.\n         - directPriority (4): The first server will be used as primary server for\n                                all requests, the second as secondary and so on.\n                                Higher priority servers that are operationally down\n                                will be probed and put back into service upon a\n                                response.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("direct", 1), ("roundRobin", 2), ("hashBased", 3), ("directPriority", 4))

class TmnxSubRadiusAttrType(TextualConvention, Unsigned32):
    reference = 'RFC 2865 Remote Authentication Dial In User Service (RADIUS)\n         section 5. Attributes'
    description = 'The TmnxSubRadiusAttrType data type contains a number that indicates a\n         RADIUS attribute type.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxSubRadiusVendorId(TextualConvention, Unsigned32):
    reference = 'RFC 2865 Remote Authentication Dial In User Service (RADIUS)\n         section 5.26. Vendor-Specific.'
    description = 'The TmnxSubRadiusVendorId data type contains a number that indicates a\n         RADIUS Vendor-Id.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16777215)

class TmnxSubRadiusDisplayString(DisplayString):
    reference = 'RFC 2865 Remote Authentication Dial In User Service (RADIUS)\n         section 5.  Attributes.'
    description = 'The TmnxSubRadiusOctetString data type contains a character string\n         that corresponds to a Radius attribute.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 253)

class TmnxSubRadiusOctetString(TextualConvention, OctetString):
    reference = 'RFC 2865 Remote Authentication Dial In User Service (RADIUS)\n         section 5.26. Vendor-Specific.'
    description = 'The TmnxSubRadiusOctetString data type contains an octet string that\n         corresponds to a Radius attribute'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(253, 253)
    fixedLength = 253

class TmnxSubSlaMode(TextualConvention, Integer32):
    description = 'The TmnxSubSlaMode data type is an enumerated integer that specifies\n         the handling of SLA profile instances for a subscriber.\n         - Expanded sla-mode: a subscriber is allowed to have multiple SLA\n           profile instances, using different SLA profiles and/or different\n           VLANs.\n         - Single sla-mode: only 1 single SLA profile instance is allowed for a\n           subscriber. This restriction has 2 implications:\n           - Last SLA profile wins: if a new host is added with an SLA profile\n             that is different from the existing hosts of the subscriber, or an\n             existing host is changed to use a different SLA profile, then all\n             existing hosts of that subscriber will be changed to the new SLA\n             profile.\n           - First VLAN wins: All hosts of a subscriber must use the same VLAN,\n             i.e. a new host on different VLAN is rejected.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("expanded", 0), ("single", 1))

class TmnxRadiusPendingReqLimit(TextualConvention, Unsigned32):
    description = 'The TmnxRadiusPendingReqLimit data type is a number that specifies the\n         limit to the number of pending RADIUS request messages.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4096)

class TmnxRadiusServerOperState(TextualConvention, Integer32):
    description = 'The TmnxRadiusServerOperState data type is an enumerated integer that\n         describes the values used to identify the operational state of a\n         RADIUS server.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("inService", 2), ("outOfService", 3), ("transition", 4), ("overloaded", 5), ("probing", 6))

class TmnxSubShcvAction(TextualConvention, Integer32):
    description = 'The TmnxSubShcvAction data type is an enumerated integer that\n         describes the values used to identify the action taken when Subscriber\n         Host Connectivity Verification (SHCV) failed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("alarm", 1), ("remove", 2))

class TmnxSubShcvInterval(TextualConvention, Unsigned32):
    description = 'The TmnxSubShcvInterval data type is a number that specifies the\n         interval in minutes between connectivity checks.\n\n         The value zero means no connectivity checking.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 6000)

class TmnxSubShcvRetryCount(TextualConvention, Unsigned32):
    description = 'The TmnxSubShcvRetryTimeout data type is a number that specifies the\n         number of connectivity check retransmissions.\n\n         Setting the value to n specifies that, for any given host, at most\n         (n+1) probes are done each interval, and (n+1) missed replies are\n         considered as a connectivity failure.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(2, 29)

class TmnxSubShcvRetryTimeout(TextualConvention, Unsigned32):
    description = 'The TmnxSubShcvRetryTimeout data type is a number that specifies the\n         timeout in seconds before a connectivity check retransmission.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(10, 60)

class TmnxSubShcvSrcIpOrigin(TextualConvention, Integer32):
    description = "The TmnxSubShcvSrcIpOrigin data type is an enumerated integer that\n         describes the values used to identify the origin of the source IP\n         address used for connectivity verification in a layer-3 service (IES\n         or VPRN).\n\n         The value 'interface' means that the IP address of the interface is\n         used.\n\n         The value 'vrrp' means that the primary IP address of the Virtual\n         Router Redundancy Protocol (VRRP) is used."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("interface", 1), ("vrrp", 2))

class TmnxSubSpiGroupId(TextualConvention, Integer32):
    description = 'The TmnxSubSpiGroupId data type is an integer that specifies  the SLA\n         profile instance group identifier.\n\n         A value of minus one means that there is no group identifier\n         configured.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 65535)

class TmnxSubOperSpiGroupId(TextualConvention, Integer32):
    description = 'The TmnxSubOperSpiGroupId data type is an integer that indicates  the\n         SLA profile instance group identifier specified by the AAA server.\n\n         A value of minus one indicates that the AAA server  did not specify\n         such a group identifier.'
    status = 'current'

class TmnxReferenceBandwidth(TextualConvention, Unsigned32):
    description = 'The TmnxRadiusPendingReqLimit data type is a number that specifies the\n         reference bandwidth used for cost calculation.\n\n         The formula is:  Cost = reference-bandwidth / bandwidth.\n\n         The unit is 1000 bps.\n\n         The value zero specifies that no reference-bandwidth is configured.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4000000000)

class TmnxSubPoolName(TLNamedItem):
    description = 'The name of a pool'
    status = 'current'

class TmnxSubProfileString(DisplayString):
    description = 'The data type TmnxSubProfileString denotes the subscriber profile\n         string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxSubProfileStringOrEmpty(DisplayString):
    description = 'The data type TmnxSubProfileStringOrEmpty denotes the subscriber\n         profile string. The empty string denotes the absence of a subscriber\n         profile.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSlaProfileString(DisplayString):
    description = 'The data type TmnxSlaProfileString denotes the SLA profile string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxSlaProfileStringOrEmpty(DisplayString):
    description = 'The data type TmnxSlaProfileStringOrEmpty denotes the SLA profile\n         string. The empty string denotes the absence of a SLA profile.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxAppProfileString(DisplayString):
    description = 'The data type TmnxAppProfileString denotes the application profile\n         string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 16)

class TmnxAppProfileStringOrEmpty(DisplayString):
    description = 'The data type TmnxAppProfileStringOrEmpty denotes the application\n         profile string. The empty string denotes the absence of a application\n         profile.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxSubMgtIntDestIdOrEmpty(DisplayString):
    description = 'The data type TmnxSubMgtIntDestIdOrEmpty denotes the intermediate\n         destination id. The empty string denotes the absence of an\n         intermediate destination id.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubMgtIntDestId(TmnxSubMgtIntDestIdOrEmpty):
    description = 'The data type TmnxSubMgtIntDestId denotes the intermediate destination\n         id.'
    status = 'current'
    subtypeSpec = TmnxSubMgtIntDestIdOrEmpty.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxDefInterDestIdSource(TextualConvention, Integer32):
    description = "The data type TmnxDefInterDestIdSource specifies what will be used as\n         the default intermediate destination identifier.\n\n         This value is used in case no other source (like RADIUS) provides an\n         intermediate destination identifier.\n\n         If the value of this object is set to 'useString', the value of the\n         string contained in another object will be used as the default\n         intermediate destination identifier; that object must be identified\n         where this datatype is used.\n\n         If the value of this object is set to 'useTopQTag', the top q-tag of\n         the ingress SAP will be used as the default subscriber intermediate\n         destination identifier.\n\n         If the value of this object is set to 'useVpi', the ATM VPI of the\n         ingress SAP will be used as the default subscriber intermediate\n         destination identifier."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("useString", 1), ("useTopQTag", 2), ("useVpi", 3))

class TmnxSubNasPortSuffixType(TextualConvention, Integer32):
    description = 'The TmnxSubNasPortSuffixType data type is an enumerated integer that\n         specifies what suffix will be added to the RADIUS NAS-Port attribute:\n         - none      (0): No suffix will be added.\n         - circuitId (1): If available, the circuit-id will be added.\n         - remoteId  (2): If available, the remote-id will be added.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("circuitId", 1), ("remoteId", 2))

class TmnxSubNasPortPrefixType(TextualConvention, Integer32):
    description = 'The TmnxSubNasPortPrefixType data type is an enumerated integer that\n         specifies what prefix will be added to the RADIUS NAS-Port attribute:\n         - none       (0): No prefix will be added.\n         - userString (1): A user configurable string will be added.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("userString", 1))

class TmnxSubNasPortTypeType(TextualConvention, Integer32):
    description = 'The TmnxSubNasPortTypeType data type is an enumerated integer that\n         specifies what value will be put in the NAS-Port-Type attribute\n         of RADIUS or DIAMETER messages:\n         - standard  (1): according to the RADIUS specification\n                          RFC 2865 section 5.41 NAS-Port-Type and\n                          RFC 4603 Additional Values for the NAS-Port-Type Attribute;\n         - config    (2): a configured value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("standard", 1), ("config", 2))

class TmnxSubCreditVolumeUnit(TextualConvention, Integer32):
    description = 'The TmnxSubCreditVolumeUnit data type is an enumerated integer that\n         specifies the unit in which the volume-credit is expressed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("bytes", 0), ("kilobytes", 1), ("megabytes", 2), ("gigabytes", 3))

class TmnxPccRuleFilterForwardAction(TextualConvention, Integer32):
    description = 'The TmnxPccRuleFilterForwardAction data type is an enumerated integer\n         that specifies the filter action taken in a PCC rule. The value\n         redirNhOrFwd (5) means: forward to the specified next hop, but if no\n         next-hop ip address or service id is given then just forward.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("forward", 1), ("drop", 2), ("redirUrl", 3), ("redirNh", 4), ("redirNhOrFwd", 5))

class TmnxPccRuleQosForwardAction(TextualConvention, Bits):
    description = 'The TmnxPccRuleQosForwardAction data type is an enumerated integer\n         that specifies the qos action taken in a PCC rule.'
    status = 'current'
    namedValues = NamedValues(("rateLimit", 0), ("fcRemark", 1), ("monitor", 2), ("account", 3), ("forward", 4))

class TmnxRadiusFramedRouteMetric(TextualConvention, Unsigned32):
    description = 'The TmnxRadiusFramedRouteMetric data type is a number that represents\n         the value of the metric in a RADIUS Framed-Route option Text field.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxRadiusFramedRoutePreference(TextualConvention, Unsigned32):
    description = 'The TmnxRadiusFramedRouteMetric data type is a number that represents\n         the value of the preference in a RADIUS Framed-Route option Text\n         field.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TmnxRadiusFramedRouteTag(TextualConvention, Unsigned32):
    description = 'The TmnxRadiusFramedRouteMetric data type is a number that represents\n         the value of the tag in a RADIUS Framed-Route option Text field.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TmnxSubMgtOrgStrOrZero(DisplayString):
    description = 'The data type TmnxSubMgtOrgStrOrZero denotes the organization string.\n         The empty string denotes the absence of an organization string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class TmnxSubMgtOrgString(TmnxSubMgtOrgStrOrZero):
    description = 'The data type TmnxSubMgtOrgStrOrZero denotes the organization string.'
    status = 'current'
    subtypeSpec = TmnxSubMgtOrgStrOrZero.subtypeSpec + ValueSizeConstraint(1, 32)

class TmnxFilterProfileStringOrEmpty(DisplayString):
    description = 'The data type TmnxFilterProfileStringOrEmpty denotes the filter\n         profile string. The empty string denotes the absence of a filter\n         profile.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxFpeId(TextualConvention, Unsigned32):
    description = 'The data type TmnxFpeId is a number that uniquely identifies a Forward\n         Path Extension (FPE).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 64)

class TmnxFpeIdOrZero(TextualConvention, Unsigned32):
    description = 'The data type TmnxFpeIdOrZero is a number that either  uniquely\n         identifies a Forward Path Extension (FPE), or is equal to zero.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 64)

class TmnxAccessLoopEncapDataLink(TextualConvention, Integer32):
    description = 'The data type TmnxAccessLoopEncapDataLink specifies the data link used\n         by the subscriber on the DSL access loop.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("aal5", 0), ("ethernet", 1))

class TmnxAccessLoopEncaps1(TextualConvention, Integer32):
    description = 'The data type TmnxAccessLoopEncaps1 specifies the encapsulation used\n         by the subscriber on the DSL access loop.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notAvailable", 0), ("untaggedEthernet", 1), ("singleTaggedEthernet", 2))

class TmnxAccessLoopEncaps2(TextualConvention, Integer32):
    description = 'The data type TmnxAccessLoopEncaps2 specifies the encapsulation used\n         by the subscriber on the DSL access loop.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("notAvailable", 0), ("pppoaLlc", 1), ("pppoaNull", 2), ("ipoaLlc", 3), ("ipoaNull", 4), ("ethernetOverAal5LlcFcs", 5), ("ethernetOverAal5LlcNoFcs", 6), ("ethernetOverAal5NullFcs", 7), ("ethernetOverAal5NullNoFcs", 8))

class TmnxSubAleOffsetMode(TextualConvention, Integer32):
    description = "The data type TmnxSubAleOffsetMode specifies the way the encapsulation\n         offset of the subscriber in the DSL access loop is learned by the 7xxx\n         system.\n\n         This offset is used in 7xxx egress shaping, adjusting the subscriber\n         aggregate rate to account for the fixed encapsulation offset and per\n         packet variable expansion of the last mile for the specific session\n         used by the subscriber host.\n\n         The value 'none' disables the adjustment.\n\n         While the value is 'auto', the encapsulation offset will be learned\n         for example from the encapsulation type value signaled in the\n         Access-loop-encapsulation sub-TLV in the Vendor-Specific PPPoE Tags or\n         DHCP Relay Options [rfc4679]."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("auto", 1))

class TmnxSubAleOffset(TextualConvention, Integer32):
    description = 'The data type TmnxSubAleOffset specifies the encapsulation offset\n         value of the subscriber in the DSL access loop as used by the 7xxx\n         system.\n\n         This offset is used in 7xxx egress shaping in order to accurately\n         shape the end user payload.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("none", 0), ("pppoaLlc", 1), ("pppoaNull", 2), ("pppoeoaLlc", 3), ("pppoeoaLlcFcs", 4), ("pppoeoaLlcTagged", 5), ("pppoeoaLlcTaggedFcs", 6), ("pppoeoaNull", 7), ("pppoeoaNullFcs", 8), ("pppoeoaNullTagged", 9), ("pppoeoaNullTaggedFcs", 10), ("ipoaLlc", 11), ("ipoaNull", 12), ("ipoeoaLlc", 13), ("ipoeoaLlcFcs", 14), ("ipoeoaLlcTagged", 15), ("ipoeoaLlcTaggedFcs", 16), ("ipoeoaNull", 17), ("ipoeoaNullFcs", 18), ("ipoeoaNullTagged", 19), ("ipoeoaNullTaggedFcs", 20), ("pppoe", 21), ("pppoeTagged", 22), ("ipoe", 23), ("ipoeTagged", 24))

class TmnxDataFormat(TextualConvention, Integer32):
    description = "The data type TmnxDataFormat represents how the input data\n         is specified:\n         - 'ascii (2)': the data contains seven-bit ASCII characters\n         - 'hex   (3)': the data contains octets. It must be displayed in\n                        hexadecimal format because it contains non-printable\n                        characters."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3))
    namedValues = NamedValues(("ascii", 2), ("hex", 3))

class TmnxDhcpOptionType(TextualConvention, Integer32):
    description = "The data type TmnxDhcpOptionType represents how the value\n         of this option is encoded:\n         - 'ipv4 (1)'  : this option contains an IPv4 address (4 octets)\n         - 'ascii(2)'  : this option contains seven-bit ASCII characters\n         - 'hex  (3)'  : this option contains octets. It must be displayed in\n                         hexadecimal format because it contains non-printable\n                         characters.\n         - 'ipv6 (4)'  : this option contains an IPv6 address (16 octets)\n         - 'domain (5)': this option contains a domain name that will be\n                         encoded as specified by RFC 1035 section 3.1."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ipv4", 1), ("ascii", 2), ("hex", 3), ("ipv6", 4), ("domain", 5))

class TmnxDhcpOptionDisplay(TextualConvention, Integer32):
    description = "The data type TmnxDhcpOptionDisplay represents a hint of\n         how the value of a DHCP option can be displayed:\n         - 'default (1)'             : display the option according to the type;\n         - 'hexDuration (2)'         : display the hex option as a duration;\n         - 'hexNetbiosNodeType (3)'  : display the hex option as a Netbios node type.;\n         - 'hexIpv4Address (4)'      : display the hex option as a list of IPv4 addresses.;\n         - 'hexIpv6Address (5)'      : display the hex option as a list of IPv6 addresses."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("default", 1), ("hexDuration", 2), ("hexNetbiosNodeType", 3), ("hexIpv4Address", 4), ("hexIpv6Address", 5))

class TmnxDhcpServerDUIDTypeCode(TextualConvention, Integer32):
    description = 'The data type TmnxDhcpServerDUIDTypeCode represents the type code of\n         the DHCP Unique Identifier (DUID) as specified by RFC 3315 section\n         9.1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3))
    namedValues = NamedValues(("duidEnterprise", 2), ("duidLinkLocal", 3))

class TmnxPppoeUserName(DisplayString):
    description = 'The data type TmnxPppoeUserName denotes the PPPoE username.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 253)

class TmnxPppoeUserNameOrEmpty(DisplayString):
    description = 'The data type TmnxPppoeUserNameOrEmpty denotes the PPPoE username.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 253)

class TCpmProtPolicyID(TextualConvention, Unsigned32):
    description = "The data type TCpmProtPolicyID represents the identification number of\n         a CPM Protection policy.\n\n         The value '0' indicates that no CPM Protection policy is provisioned."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TCpmProtPolicyIDOrDefault(TextualConvention, Integer32):
    description = "The data type TCpmProtPolicyIDOrDefault represents the identification\n         number of a CPM Protection policy.\n\n         The value of '-1' indicates the system determined default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 255), )
class TMlpppQoSProfileId(TextualConvention, Unsigned32):
    description = 'This textual convention uniquely identifies MLPPP Bundle QoS profile\n         in the ingress and egress MLPPP QoS profile tables. The value 0\n         indicates default MLPPP QoS Profile as applicable to a given H/W'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TMcFrQoSProfileId(TextualConvention, Unsigned32):
    description = 'This textual convention uniquely identifies Multi-class Frame relay\n         QoS profiles in the ingress and egress multi-class frame relay QoS\n         profile tables. The value 0 indicates a default QoS Profile as\n         applicable to a given hardware.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxPppoeSessionId(TextualConvention, Unsigned32):
    description = 'The TmnxPppoeSessionId indicates the 16 bit wide PPPoE session Id.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxPppoePadoDelay(TextualConvention, Unsigned32):
    description = 'The data type TmnxPppoePadoDelay specifies the delay timeout in\n         deciseconds before sending a PADO (PPPoE Active Discovery Offer).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 30), )
class TmnxPppoeSessionInfoOrigin(TextualConvention, Integer32):
    description = 'The TmnxPppoeSessionInfoOrigin indicates the originator of the\n         provided information.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("none", 0), ("default", 1), ("radius", 2), ("localUserDb", 3), ("dhcp", 4), ("midSessionChange", 5), ("tags", 6), ("l2tp", 7), ("localPool", 8), ("diameterNasreq", 9), ("diameterGx", 10), ("gtp", 11), ("python", 12), ("bonding", 13))

class TmnxPppoeSessionType(TextualConvention, Integer32):
    description = 'The TmnxPppoeSessionType indicates the type of PPPoE session.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("local", 1), ("localWholesale", 2), ("localRetail", 3), ("l2tp", 4))

class TmnxPppNcpProtocol(TextualConvention, Integer32):
    description = 'The TmnxPppNcpProtocol data type represents the PPP Network Control\n         Protocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipcp", 1), ("ipv6cp", 2))

class TmnxDiamCcFailureHndlng(TextualConvention, Integer32):
    description = 'The TmnxDiamCcFailureHndlng data type is an enumerated integer that\n         describes the different actions that can be taken after a DCCA\n         (Diameter Credit Control Application) session failure has occurred.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("terminate", 1), ("continue", 2), ("retryAndTerminate", 3))

class TmnxMlpppEpClass(TextualConvention, Integer32):
    description = 'The TmnxMlpppEpClass type represents the address class of the MLPPP\n         Endpoint Discriminator option.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("null", 0), ("local", 1), ("ipv4Address", 2), ("macAddress", 3), ("magicNumber", 4), ("directoryNumber", 5))

class TNetworkPolicyID(TPolicyID):
    description = 'the identification number of a network policy.'
    status = 'current'
    subtypeSpec = TPolicyID.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 65535), ValueRangeConstraint(65536, 65536), ValueRangeConstraint(65537, 65537), ValueRangeConstraint(65538, 65538), ValueRangeConstraint(65539, 65539), )
class TItemScope(TextualConvention, Integer32):
    description = "This textual convention determines some aspects of an item's behavior\n         regarding creation and use, unused entry garbage collection, and\n         automated promulgation by Element Management System to other systems\n         in the service domain.\n\n         TItemScope applies to SAP-ingress, SAP-egress, and Network policies,\n         and to IP filters and MAC filters.\n\n         exclusive:\n\n             When the scope of an item is defined as exclusive, the item can\n             only be applied once, for example to a single SAP.  Attempting\n             to assign the policy to a second SAP is not allowed and will\n             result in an error.  If the item is removed from the exclusive\n             SAP, it will become available for assignment to another\n             exclusive SAP.\n\n             A non-applied exclusive scope policy is a candidate to be removed\n             from the system by a TBD garbage collection command.\n\n             The system default policies cannot be put into the exclusive scope.\n             An error will be generated if scope exclusive is executed in\n             any policies with a policy-id equal to 1.\n\n         template:\n\n             When the scope of an item is defined as template, the item can be\n             applied any number of times.  Policies with template scope\n             will not be considered for deletion by a TBD garbage collection\n             command; all items of scope 'template' must be deleted explicitly.\n\n             The system default policies will always be scope template.\n             An error will occur if a policy-id 1 is attempted to be\n             set to scope exclusive."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("exclusive", 1), ("template", 2))

class TItemMatch(TextualConvention, Integer32):
    description = 'when set to off, the item is not matched. when set to false, packets\n         without the item match the filter. when set to true, packets with the\n         item match the filter.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("false", 2), ("true", 3))

class TPriority(TextualConvention, Integer32):
    description = 'the priority to apply to a packet'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("low", 1), ("high", 2))

class TPriorityOrDefault(TextualConvention, Integer32):
    description = 'the priority to apply to a packet. when set to default(3), the\n         priority from the default action is used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("low", 1), ("high", 2), ("default", 3))

class TPriorityOrUndefined(TextualConvention, Integer32):
    description = 'the priority to apply to a packet. when set to undefined(0), the\n         priority is not applicable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("low", 1), ("high", 2))

class TProfile(TextualConvention, Integer32):
    description = 'the profile marking of a packet at the ingress.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("in", 1), ("out", 2))

class TProfileOrNone(TextualConvention, Integer32):
    description = 'Profile marking of a packet.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("in", 1), ("out", 2))

class TDEProfile(TextualConvention, Integer32):
    description = "This textual convention specifies the profile marking of a packet.\n\n         Value of 'in' specifies the in-profile marking.\n\n         Value of 'out' specifies the out-profile marking.\n\n         Value of 'de' specifies that the profile marking will be based on the DE\n         (Drop-Eligible) bit.  DE bit-value of '0' specifies in-profile and DE\n         bit value of '1' specifies out-profile marking."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("in", 1), ("out", 2), ("de", 3))

class TEgressProfile(TextualConvention, Integer32):
    description = "The profile marking of a packet. Value of 'in' specifies in-profile\n         marking. Value of 'out' specifies out-profile marking. Value of 'none'\n         specifies the profile marking of the packet will be inherited from the\n         existing enqueuing priority derived from earlier matches in the\n         classification hierarchy."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))
    namedValues = NamedValues(("in", 1), ("out", 2), ("exceed", 4), ("inplus", 5))

class TEgressProfileOrNone(TextualConvention, Integer32):
    description = "The profile marking of a packet. Value of 'in' specifies in-profile\n         marking. Value of 'out' specifies out-profile marking. Value of 'de'\n         specifies that the profile marking of the packet will be based on the\n         DE (Drop-Eligible) bit of the packet. DE bit value of '0' specifies\n         in-profile and DE bit value of '1' specifies out-profile marking.\n\n         Value of 'none' specifies the profile marking of the packet will be\n         inherited from the existing enqueuing priority derived from earlier\n         matches in the classification hierarchy."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("in", 1), ("out", 2), ("de", 3), ("exceed", 4), ("inplus", 5))

class TAdaptationRule(TextualConvention, Integer32):
    description = 'The adaptation rule to be applied to calculate the operational values\n         for the specified entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("max", 1), ("min", 2), ("closest", 3))

class TAdaptationRuleOverride(TextualConvention, Integer32):
    description = 'The adaptation rule to be applied to calculate the operational values\n         for the specified entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noOverride", 0), ("max", 1), ("min", 2), ("closest", 3))

class TRemarkType(TextualConvention, Integer32):
    description = 'The remarking to be used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("dscp", 2), ("precedence", 3))

class TIngClassRemarkType(TextualConvention, Integer32):
    description = 'The remarking to be used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("any", 1), ("dot1pExp", 2))

class TPrecValue(TextualConvention, Integer32):
    description = 'The precedence bits as used in the IPv4 header. This constitutes of 3\n         bits and hence can hold the values from 0 to 7.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class TPrecValueOrNone(TextualConvention, Integer32):
    description = "The precedence bits as used in the IPv4 header. This constitutes of 3\n         bits and hence can hold the values from 0 to 7. The value '-1'\n         specifies that the precedence value is undefined/unused."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class TCpmFilterBurstSize(TextualConvention, Integer32):
    description = "The amount of buffer space (in kbytes) assigned to a queue. The value\n         -1 means that the actual value is derived from the corresponding\n         buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 131072), )
class TBurstSize(TextualConvention, Integer32):
    description = "The amount of buffer space (in kbytes) assigned to a queue. The value\n         -1 means that the actual value is derived from the corresponding\n         buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1048576), )
class TBurstSizeOverride(TextualConvention, Integer32):
    description = "The amount of buffer space (in kbytes) assigned to a queue. The value\n         -1 means that the actual value is derived from the corresponding\n         buffer policy's default value. A value of -2 specifies no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1048576), )
class TBurstSizeBytesOvr(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a queue. The value\n         -1 means that the actual value is derived from the corresponding\n         buffer policy's default value. A value of -2 specifies no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1073741824), )
class TBurstPercent(TextualConvention, Integer32):
    description = 'The percentage of buffer space assigned to a queue that is reserved\n         for some purpose.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TBurstHundredthsOfPercent(TextualConvention, Integer32):
    description = 'The percentage of buffer space assigned to a queue that is reserved\n         for some purpose, defined to two decimal places.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10000)

class TBurstPercentOrDefault(TextualConvention, Integer32):
    description = "The percentage of buffer space assigned to a queue that is reserved\n         for some purpose. The value -1 means that the actual value is derived\n         from the corresponding buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100), )
class TBurstPercentOrDefaultOverride(TextualConvention, Integer32):
    description = "The percentage of buffer space assigned to a queue that is reserved\n         for some purpose.\n\n         The value -1 means that the actual value is derived from the\n         corresponding buffer policy's default value.\n\n         A value of -2 specifies no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 100), )
class TRatePercent(TextualConvention, Integer32):
    description = 'The percentage of maximum rate allowed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class TPIRRatePercent(TextualConvention, Integer32):
    description = 'The percentage of maximum PIR rate allowed. A value of 0 is not\n         acceptable, so the range begins at 1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 100)

class TLevel(TextualConvention, Integer32):
    description = 'The level of the specified entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

class TPortSchedLevel(TextualConvention, Integer32):
    description = 'The priority level for the specified port scheduler entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

class TLevelOrDefault(TextualConvention, Integer32):
    description = 'The level of the specified entity while feeding into the parent. The\n         value 0 is used to denote a default value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TQueueMode(TextualConvention, Integer32):
    description = "The mode in which the queue is operating.\n\n         If the queue is operating in the 'priority' mode, it is capable of\n         handling traffic differently with two distinct priorities. These\n         priorities are assigned by the stages preceding the queueing framework\n         in the system.\n\n         When the queue is operating in the 'profile' mode, in other words the\n         color aware mode, the queue tries to provide the appropriate bandwidth\n         to the packets with different profiles.\n\n         The profiles are assigned according to the configuration of the\n         forwarding class or the sub-forwarding class.\n\n         In 'priority' mode, the queue does not have the functionality to\n         support the profiled traffic and in such cases the queue will have a\n         degraded performance. However, the converse is not valid and a queue\n         in 'profile' mode should be capable of supporting the different\n         priorities of traffic."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("priority", 1), ("profile", 2))

class TQueueStatModeFormat(TextualConvention, Integer32):
    description = "The mode in which the queue stats are collected.\n\n         In 'priority' mode separate stats are collected for high and low\n         priority packets/octets.\n\n         In 'profile' mode separate stats are collected for in profile and out\n         of profile packets/octets.\n\n         In 'v4V6' mode separate stats are collected for IPv4 and IPv6\n         packets/octets"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("priority", 1), ("profile", 2), ("v4V6", 3))

class TEntryIndicator(TextualConvention, Unsigned32):
    description = 'Uniquely identifies an entry in a policy or filter table. The value 0\n         is not a valid entry-id. When used as insertion point the value 0\n         indicates that entries must be inserted at the very beginning,\n         i.e.before the first entry defined.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TEntryId(TEntryIndicator):
    description = 'uniquely identifies an entry in a policy or filter table.\n         to facilitate insertion of entries in the tables, we recommend\n         assigning entry IDs by 10s:  10, 20, 30, etc. '
    status = 'current'
    subtypeSpec = TEntryIndicator.subtypeSpec + ValueRangeConstraint(1, 65535)

class TMatchCriteria(TextualConvention, Integer32):
    description = 'determines whether the entry matches traffic using IP match entries or\n         MAC match entries.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ip", 1), ("mac", 2), ("none", 3))

class TmnxMdaQos(TextualConvention, Integer32):
    description = 'TmnxMdaQos is an enumerated integer whose value specifies the Quality\n         of Service support of a Media Dependent Adapter (MDA).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("mda", 1), ("hsmda1", 2), ("hsmda2", 3), ("hs", 4))

class TAtmTdpDescrType(TextualConvention, Integer32):
    description = 'The TAtmTdpDescrType is an enumerated integer whose value indicates\n         the types of cell loss priority to be used in conjunction with traffic\n         parameters.\n\n         The following values are outlined:\n          Integer Value               Interpretation\n          -------------               ------------------------\n          clp0And1pcr                 PCR applies to CLP 0 and\n                                      CLP 1 cell flows\n          clp0And1pcrPlusClp0And1scr  PCR applies to CLP 0 and\n                                      CLP 1 cell flows.\n                                      SCR applies to CLP 0 and\n                                      CLP 1 cell flows.\n          clp0And1pcrPlusClp0scr      PCR applies to CLP 0 and\n                                      CLP 1 cell flows.\n                                      SCR applies to CLP 0 cell flows.\n          clp0And1pcrPlusClp0scrTag   PCR applies to CLP 0 and\n                                      CLP 1 cell flows.\n                                      SCR applies to CLP 0 cell flows. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("clp0And1pcr", 0), ("clp0And1pcrPlusClp0And1scr", 1), ("clp0And1pcrPlusClp0scr", 2), ("clp0And1pcrPlusClp0scrTag", 3))

class TDEValue(TextualConvention, Integer32):
    description = "This textual convention specifies the DE (Drop Eligible) bit value.\n         The value of '-1' means DE value is not specified."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1), )
class TQGroupType(TextualConvention, Integer32):
    description = 'This textual convention specifies the type of the Queue-Group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("port", 0), ("vpls", 1))

class TQosOverrideType(TextualConvention, Integer32):
    description = 'This textual convention specifies the type of the Qos Override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("queue", 1), ("policer", 2), ("aggRateLimit", 3), ("arbiter", 4), ("scheduler", 5), ("slaAggRateLimit", 6), ("wrrGroup", 7))

class TQosOverrideTypeId(TextualConvention, Integer32):
    description = 'This textual convention indicates the identifier of the queue or\n         policer that is overridden, or zero if the item that is overridden is\n         not a queue or a policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

class TmnxIPsecTunnelTemplateId(TextualConvention, Unsigned32):
    description = 'A number used to identify an entry in the tIPsecTnlTempTable.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2048)

class TmnxIPsecTunnelTemplateIdOrZero(TextualConvention, Unsigned32):
    description = 'A number used to identify an entry in the tIPsecTnlTempTable or zero.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 2048)

class TmnxIpSecIsaOperFlags(TextualConvention, Bits):
    description = 'The value of TmnxIpSecIsaOperFlags specifies the operational flags\n         that determine the status of the MDAs associated with IPsec ISA.'
    status = 'current'
    namedValues = NamedValues(("adminDown", 0), ("noActive", 1), ("noResources", 2), ("mcAdminDown", 3))

class TmnxIkePolicyAuthMethod(TextualConvention, Integer32):
    description = 'TmnxIkePolicyAuthMethod data type is an enumerated integer that\n         describes the type of authentication method used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("psk", 1), ("hybridX509XAuth", 2), ("plainX509XAuth", 3), ("plainPskXAuth", 4), ("cert", 5), ("pskRadius", 6), ("certRadius", 7), ("eap", 8), ("autoEapRadius", 9), ("autoEap", 10))

class TmnxIkePolicyAutoEapMethod(TextualConvention, Integer32):
    description = 'TmnxIkePolicyAutoEapMethod data type is an enumerated integer that\n         describes the type of fallback authentication method use in\n         conjunction with the automatic EAP authentication method.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("psk", 1), ("cert", 2), ("pskOrCert", 3))

class TmnxIkePolicyAutoEapOwnMethod(TextualConvention, Integer32):
    description = 'TmnxIkePolicyAutoEapOwnMethod data type is an enumerated integer that\n         describes the type of fallback authentication method use in\n         conjunction with the automatic EAP authentication method on its own\n         side.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("psk", 1), ("cert", 2))

class TmnxIkePolicyOwnAuthMethod(TextualConvention, Integer32):
    description = 'TmnxIkePolicyOwnAuthMethod data type is an enumerated integer that\n         describes the type of authentication method used for its own side.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 5, 8))
    namedValues = NamedValues(("symmetric", 0), ("psk", 1), ("cert", 5), ("eapOnly", 8))

class TmnxRsvpDSTEClassType(TextualConvention, Unsigned32):
    description = 'TmnxRsvpDSTEClassType is an unsigned integer in the range of (0..7)\n         that defines the class type (CT).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class TmnxAccPlcyQICounters(TextualConvention, Bits):
    description = 'This data type describes a set ingress counters for which accounting\n         data can be collected associated with a given queue.'
    status = 'current'
    namedValues = NamedValues(("hpo", 0), ("lpo", 1), ("ucp", 2), ("hoo", 3), ("loo", 4), ("uco", 5), ("apo", 6), ("aoo", 7), ("hpd", 8), ("lpd", 9), ("hod", 10), ("lod", 11), ("ipf", 12), ("opf", 13), ("iof", 14), ("oof", 15))

class TmnxAccPlcyQECounters(TextualConvention, Bits):
    description = 'This data type describes a set egress counters for which accounting\n         data can be collected associated with a given queue.'
    status = 'current'
    namedValues = NamedValues(("ipf", 0), ("ipd", 1), ("opf", 2), ("opd", 3), ("iof", 4), ("iod", 5), ("oof", 6), ("ood", 7))

class TmnxAccPlcyPolicerICounters(TextualConvention, Bits):
    description = 'This data type describes a set of ingress counters for which\n         accounting data can be collected associated with a given policer.\n\n         ipo : In-profile Packets Offered\n         ipd : In-profile Packets Discarded\n         opo : Out-profile Packets Offered\n         opd : Out-profile Packets Discarded\n         ioo : In-profile Octets Offered\n         iod : In-profile Octets Discarded\n         ooo : Out-profile Octets Offered\n         ood : Out-profile Octets Discarded\n         ucp : Uncoloured Packets Offered\n         uco : Uncoloured Octets Offered\n         ipf : In-profile Packets Forwarded\n         iof : In-profile Octets Forwarded\n         opf : Out-profile Packets Forwarded\n         oof : Out-profile Octets Forwarded.'
    status = 'current'
    namedValues = NamedValues(("ipo", 0), ("ipd", 1), ("opo", 2), ("opd", 3), ("ioo", 4), ("iod", 5), ("ooo", 6), ("ood", 7), ("ucp", 8), ("uco", 9), ("ipf", 10), ("iof", 11), ("opf", 12), ("oof", 13))

class TmnxAccPlcyPolicerECounters(TextualConvention, Bits):
    description = 'This data type describes a set of egress counters for which accounting\n         data can be collected associated with a given policer.\n\n          ipo  : In-profile Packets Offered\n          ipd  : In-profile Packets Discarded\n          opo  : Out-profile Packets Offered\n          opd  : Out-profile Packets Discarded\n          ioo  : In-profile Octets Offered\n          iod  : In-profile Octets Discarded\n          ooo  : Out-profile Octets Offered\n          ood  : Out-profile Octets Discarded\n          ucp  : Uncoloured Packets Offered\n          uco  : Uncoloured Octets Offered\n          ipf  : In-profile Packets Forwarded\n          iof  : In-profile Octets Forwarded\n          opf  : Out-Profile Packets Forwarded\n          oof  : Out-Profile Octets Forwarded\n          xpo  : Exceed-profile Packets Offered;\n          xpd  : Exceed-profile Packets Discarded;\n          xpf  : Exceed-profile Packets Forwarded;\n          xoo  : Exceed-profile Octets Offered;\n          xod  : Exceed-profile Octets Discarded;\n          xof  : Exceed-profile Octets Forwarded;\n          ppo  : In-plus-profile Packets Offered;\n          ppd  : In-plus-profile Packets Discarded;\n          ppf  : In-plus-profile Packets Forwarded;\n          poo  : In-plus-profile Octets Offered;\n          pod  : In-plus-profile Octets Discarded;\n          pof  : In-plus-profile Octets Forwarded;'
    status = 'current'
    namedValues = NamedValues(("ipo", 0), ("ipd", 1), ("opo", 2), ("opd", 3), ("ioo", 4), ("iod", 5), ("ooo", 6), ("ood", 7), ("ucp", 8), ("uco", 9), ("ipf", 10), ("iof", 11), ("opf", 12), ("oof", 13), ("xpo", 14), ("xpd", 15), ("xpf", 16), ("xoo", 17), ("xod", 18), ("xof", 19), ("ppo", 20), ("ppd", 21), ("ppf", 22), ("poo", 23), ("pod", 24), ("pof", 25))

class TmnxAccPlcyOICounters(TextualConvention, Bits):
    description = 'This data type describes a set ingress counters for which accounting\n         data can be collected associated with a given counter.'
    status = 'current'
    namedValues = NamedValues(("apo", 0), ("aoo", 1), ("hpd", 2), ("lpd", 3), ("hod", 4), ("lod", 5), ("ipf", 6), ("opf", 7), ("iof", 8), ("oof", 9))

class TmnxAccPlcyOECounters(TextualConvention, Bits):
    description = 'This data type describes a set egress counters for which accounting\n         data can be collected associated with a given counter.'
    status = 'current'
    namedValues = NamedValues(("ipf", 0), ("ipd", 1), ("opf", 2), ("opd", 3), ("iof", 4), ("iod", 5), ("oof", 6), ("ood", 7))

class TmnxAccPlcyAACounters(TextualConvention, Bits):
    description = 'This data type describes a set of AA (Application Assurance) counters\n         for which accounting data can be collected.\n\n         The bits are defined as follows:\n               any (0)  -  enables reporting when there is a change\n                           to any counter\n               sfa (1)  -  allowed flows from sub\n               nfa (2)  -  allowed flows to sub\n               sfd (3)  -  denied flows from sub\n               nfd (4)  -  denied flows to sub\n               saf (5)  -  active flows from sub\n               naf (6)  -  active flows to sub\n               spa (7)  -  total packets from sub\n               npa (8)  -  total packets to sub\n               sba (9)  -  total bytes from sub\n               nba (10) -  total bytes to sub\n               spd (11) -  total discard packets from sub\n               npd (12) -  total discard packets to sub\n               sbd (13) -  total discard bytes from sub\n               nbd (14) -  total discard bytes to sub\n               sdf (15) -  short  duration flows\n               mdf (16) -  medium duration flows\n               ldf (17) -  long   duration flows\n               tfd (18) -  total flow duration\n               tfc (19) -  total flows completed\n               sbm (20) -  max throughput in bytes from sub\n               spm (21) -  max throughput in packets from sub\n               smt (22) -  max throughput timestamp from sub\n               nbm (23) -  max throughput in bytes to sub\n               npm (24) -  max throughput in packets to sub\n               nmt (25) -  max throughput timestamp to sub\n               sfc (26) -  forwarding class from sub\n               nfc (27) -  forwarding class to sub'
    status = 'current'
    namedValues = NamedValues(("any", 0), ("sfa", 1), ("nfa", 2), ("sfd", 3), ("nfd", 4), ("saf", 5), ("naf", 6), ("spa", 7), ("npa", 8), ("sba", 9), ("nba", 10), ("spd", 11), ("npd", 12), ("sbd", 13), ("nbd", 14), ("sdf", 15), ("mdf", 16), ("ldf", 17), ("tfd", 18), ("tfc", 19), ("sbm", 20), ("spm", 21), ("smt", 22), ("nbm", 23), ("npm", 24), ("nmt", 25), ("sfc", 26), ("nfc", 27))

class TmnxAccPlcyAASubAttributes(TextualConvention, Bits):
    description = 'This data type describes a set of AA (Application Assurance)\n         subscriber attributes which must be included in accounting data.\n\n         The bits are defined as follows:\n              appProfile       (0)  - application profile\n              appServiceOption (1)  - application service option'
    status = 'current'
    namedValues = NamedValues(("appProfile", 0), ("appServiceOption", 1))

class TmnxIsaBbGrpId(TextualConvention, Unsigned32):
    description = "The TmnxIsaBbGrpId data type contains an identification number for an\n         ISA-BB group.\n\n         An ISA-BB group is a set of MDA of type 'isa-bb' that together\n         performs a particular function such as NAT (Network Address\n         Translation) or IP datagram fragment reassembly.\n\n         The value zero means that no ISA-BB Group is defined."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4)

class TmnxIsaScalingProfile(TextualConvention, Integer32):
    description = 'TmnxIsaScalingProfile is an enumerated integer that specifies the ISA\n         scaling profile.\n\n         The meaning of each profile is explained in the customer\n         documentation.\n\n         ISA scaling profiles are only used in a virtual machine\n         implementation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("profile1", 1), ("profile2", 2))

class TmnxVdoGrpIdIndex(TextualConvention, Unsigned32):
    description = 'TmnxVdoGrpIdIndex data type describes the id of a\n         TIMETRA-VIDEO-MIB::tmnxVdoGrpEntry and is the primary index for the\n         table.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4)

class TmnxVdoGrpId(TextualConvention, Unsigned32):
    description = 'TmnxVdoGrpId data type describes the identifier for a video group.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4)

class TmnxVdoGrpIdOrInherit(TextualConvention, Integer32):
    description = "The data type describes the identifier for a video group. A value of\n         '-1' indicates that identifier will be inherited from another object\n         that is usually in another mib table."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 4), )
class TmnxVdoFccServerMode(TextualConvention, Integer32):
    description = "The TmnxVdoFccServerMode data type is an enumerated integer that\n         describes the mode of the Fast Channel Change (FCC) server.\n\n         A value of 'burst' indicates that the FCC server is enabled and will\n         send the channel at a nominally faster rate than the channel was\n         received based on the\n         TIMETRA-MCAST-PATH-MGMT-MIB::tmnxMcPathVdoPlcyFCCBurst setting.\n\n         A value of 'dent' indicates that the FCC server will selectively\n         discard frames from the original stream based on the value of\n         TIMETRA-MCAST-PATH-MGMT-MIB::tmnxMcPathVdoPlcyFCCDentThd.\n\n         A value of 'hybrid' indicates that the FCC server will use combination\n         of 'burst' and 'dent' to send the unicast stream to the client.\n\n         A value of 'none' indicates that FCC server is disabled."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("burst", 1), ("dent", 2), ("hybrid", 3))

class TmnxVdoPortNumber(TextualConvention, Unsigned32):
    description = 'The data type describes the port number of an Internet transport layer\n         protocol.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1024, 5999), ValueRangeConstraint(6251, 65535), )
class TmnxVdoIfName(TNamedItem):
    description = 'The data type describes the name of a video interface. The name of a\n         video interface must always start with a letter.'
    status = 'current'

class TmnxTimeInSec(TextualConvention, Unsigned32):
    description = 'The data type TmnxTimeInSec describes the Tariff Time for the Charging\n         Data Record (CDR).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 86400)

class TmnxReasContextVal(TextualConvention, Unsigned32):
    description = 'The value of the label used to identify the entity using the specified\n         context value on a specific port.\n\n         31                                   0\n         +--------+--------+--------+--------+\n         |00000000 00000000 00000000 000XXXXX|\n         +--------+--------+--------+--------+\n\n         The value of this object is encoded in the least significant 5 bits\n         and represents the context value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 31)

class TmnxVdoStatInt(TextualConvention, Integer32):
    description = "The data type TmnxVdoStatInt is an enumerated integer that specifies\n         the time duration for which the video statistics are being counted.\n         Setting a variable of this type to 'current' causes the time duration\n         to be set to one second which is the least allowed value. A value of\n         'interval' makes it necessary for some other MIB object to actually\n         quantify the time interval."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("current", 1), ("interval", 2))

class TmnxVdoOutputFormat(TextualConvention, Integer32):
    description = "The data type TmnxVdoOutputFormat is an enumerated integer that\n         specifies the output format of the video stream. Setting a variable of\n         this type to 'udp' causes the video stream to be of type 'udp' whereas\n         setting a value of 'rtp-udp' causes the video stream to be of type\n         'rtp-udp'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("udp", 1), ("rtp-udp", 2))

class TmnxVdoAnalyzerAlarm(TextualConvention, Integer32):
    description = "The data type TmnxVdoAnalyzerAlarm is an enumerated integer that\n         specifies the severity of the analyzer state alarm. Setting a variable\n         of this type to 'none' indicates no error level. A value of 'tnc'\n         indicates a TNC (Tech Non-Conformance) error level.A value of 'qos'\n         indicates a QOS (Quality of Service) error level. A value of 'poa'\n         indicates a POA (Program off Air) error level."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("tnc", 1), ("qos", 2), ("poa", 3))

class TmnxVdoAnalyzerAlarmStates(TextualConvention, OctetString):
    description = "The data type TmnxVdoAnalyzerAlarmStates is an octet string that\n         represents the analyzer state for the past 10 seconds. Setting a\n         variable of this type to 'good'(00) indicates either there was no\n         alarm during that second or the state of the stream has been cleared\n         from a prior errored state. A value of 'tnc'(01)indicates a TNC (Tech\n         Non-Conformance) error occurred during that second. A value of\n         'qos'(02) indicates a QOS (Quality of Service) error occurred during\n         that second. A value of 'poa'(03) indicates a POA (Program off Air)\n         error occurred during that second.\n\n         Since the octet string is 10 bytes long, the 10th byte indicates\n         the most recent state of the stream. Below is how an example stream\n         would appear. Each byte in the stream holds an alarm state for a\n         second.\n         good (00),  --  stream was good during 1st second\n         tnc  (01),  --  stream had tnc error during 2nd second\n         qos  (02),  --  stream had qos error during 3rd second\n         qos  (02),  --  stream had qos error during 4th second\n         qos  (02),  --  stream had qos error during 5th second\n         good (00),  --  stream error was cleared during 6th second\n         good (00),  --  stream was good during 7th second\n         tnc  (01),  --  stream had tnc error during 8th second\n         poa  (03),  --  stream had poa error during 9th second\n         good (00)   --  stream error was cleared during 10th second."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

class SvcISID(TextualConvention, Integer32):
    description = 'The SvcISID specifies a 24 bit (0..16777215) service instance\n         identifier for the service. As part of the Provider Backbone Bridging\n         frames, it is used at the destination PE as a demultiplexor field.\n\n         The value of -1 is used to indicate the value of this object is\n         unspecified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 16777215), )
class TmnxISID(TextualConvention, Integer32):
    description = 'The TmnxISID specifies a 24 bit (1..16777215) service instance\n         identifier for the service. As part of the Shortest Path Bridging\n         (SPB) frames, it is used at the destination PE as a demultiplexor\n         field.\n\n         The value of 0 is used to indicate the value of this object is\n         unspecified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 16777215), )
class TIngPolicerId(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on ingress\n         side.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 32)

class TNetIngPolicerId(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on network\n         ingress side.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16)

class TNetIngPolicerIdOrNone(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on network\n         ingress side or zero when not specified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 16), )
class TIngPolicerIdOrNone(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on ingress\n         side or zero when not specified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32), )
class TIngressPolicerId(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on ingress\n         side.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 63)

class TIngressPolicerIdOrNone(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on ingress\n         side or zero when not specified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 63), )
class TIngDynPolicerIdOrNone(TextualConvention, Integer32):
    description = 'The data type describes the QoS dynamic policer identifier on ingress\n         side or zero when not specified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 63), )
class TEgrPolicerId(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on egress\n         side.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

class TEgrPolicerIdOrNone(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on egress\n         side or zero when not specified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), )
class TEgressPolicerId(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on egress\n         side.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 63)

class TEgressPolicerIdOrNone(TextualConvention, Integer32):
    description = 'The data type describes the QoS control policer identifier on egress\n         side or zero when not specified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 63), )
class TEgrDynPolicerIdOrNone(TextualConvention, Integer32):
    description = 'The data type describes the QoS dynamic policer identifier on egress\n         side or zero when not specified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 63), )
class TFIRRate(TextualConvention, Integer32):
    description = 'The static fair rate to be used in kbps. The value -1 means maximum\n         rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 100000000), )
class TBurstSizeBytes(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a queue. The value\n         -1 means that the actual value is derived from the corresponding\n         buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1073741824), )
class THSMDABurstSizeBytes(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a HSMDA queue. The\n         value -1 means that the actual value is derived from the corresponding\n         buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2688000), )
class THSMDAQueueBurstLimit(TextualConvention, Integer32):
    description = "An explicit shaping burst size of a HSMDA queue. The value -1 means\n         that the actual value is derived from the corresponding queue's\n         default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 1000000), )
class TClassBurstLimit(TextualConvention, Integer32):
    description = "An explicit shaping burst size for a class. The value -1 means that\n         the actual value is derived from the corresponding class's default\n         value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 327680), )
class TNetIngPlcrBurstSizeBytes(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a queue by policer.\n         The value -1 means that the actual value is derived from the\n         corresponding buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(128, 4161536), )
class TPlcrBurstSizeBytes(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a queue by policer.\n         The value -1 means that the actual value is derived from the\n         corresponding buffer policy's default value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 16777216), )
class TBurstSizeBytesOverride(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a queue. The value\n         -1 means that the actual value is derived from the corresponding\n         buffer policy's default value. A value of -2 specifies no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 134217728), )
class THSMDABurstSizeBytesOverride(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a HSMDA queue. The\n         value -1 means that the actual value is derived from the corresponding\n         buffer policy's default value. A value of -2 specifies no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2688000), )
class TPlcrBurstSizeBytesOverride(TextualConvention, Integer32):
    description = "The amount of buffer space (in bytes) assigned to a queue by policer.\n         The value -1 means that the actual value is derived from the\n         corresponding buffer policy's default value. A value of -2 specifies\n         no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 16777216), )
class TmnxBfdSessionProtocols(TextualConvention, Bits):
    description = 'This data type indicates what protocols are using a BFD session.'
    status = 'current'
    namedValues = NamedValues(("ospfv2", 0), ("pim", 1), ("isis", 2), ("staticRoute", 3), ("mcRing", 4), ("rsvp", 5), ("bgp", 6), ("vrrp", 7), ("srrp", 8), ("mcep", 9), ("ldp", 10), ("ipsecTunnel", 11), ("ospfv3", 12), ("mcIpsec", 13), ("mcMobile", 14), ("mplsTp", 15), ("lag", 16), ("opergrp", 17), ("vccv", 18), ("rsvpLsp", 19), ("ldpLsp", 20), ("bgpLsp", 21), ("rip", 22), ("ripng", 23), ("mplsLsp", 24), ("reserved25", 25), ("reserved26", 26))

class TmnxBfdSessOperState(TextualConvention, Integer32):
    description = 'The TmnxBfdSessOperState data type is an enumerated integer that\n         describes the values used to identify the operational state of a BFD\n         session the instance is relying upon for its fast triggering\n         mechanism.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("connected", 2), ("broken", 3), ("peerDetectsDown", 4), ("notConfigured", 5), ("noResources", 6))

class TmnxBfdOnLspSessFecType(TextualConvention, Integer32):
    reference = "RFC 5884, 'Bidirectional Forwarding Detection (BFD) for MPLS Label\n         Switched Paths (LSPs)', Section 3.1, 'BFD for MPLS LSPs: Motivation'."
    description = 'An object of type TmnxBfdOnLspSessFecType indicates the Forwarding\n         Equivalence Class (FEC) type of a Bidirectional Forwarding Detection\n         (BFD) session running on an LSP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("rsvp", 1), ("ldp", 2), ("bgp", 3), ("srTe", 4), ("reserved5", 5))

class TmnxIngPolicerStatMode(TextualConvention, Integer32):
    description = 'TmnxIngPolicerStatMode specifies the mode of statistics collected by\n         this ingress policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredPriorityNoCIR", 4), ("offeredProfileCIR", 5), ("offeredPriorityCIR", 6), ("offeredLimitedProfileCIR", 7), ("offeredProfileCappedCIR", 8), ("offeredLimitedCappedCIR", 9))

class TmnxSapIngPolicerStatMode(TextualConvention, Integer32):
    description = 'TmnxSapIngPolicerStatMode specifies the mode of statistics collected\n         by this sap ingress policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredPriorityNoCIR", 4), ("offeredProfileCIR", 5), ("offeredPriorityCIR", 6), ("offeredLimitedProfileCIR", 7), ("offeredProfileCappedCIR", 8), ("offeredLimitedCappedCIR", 9), ("offeredProfileWithDiscards", 10), ("offeredFourProfileWithDiscards", 11))

class TmnxNetIngPlcyPolicerStatMode(TextualConvention, Integer32):
    description = 'TmnxIngPolicerStatMode specifies the mode of statistics collected by\n         this network ingress policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 10))
    namedValues = NamedValues(("noStats", 0), ("offeredProfileWithDiscards", 10))

class TmnxIngPolicerStatModeOverride(TextualConvention, Integer32):
    description = 'TmnxIngPolicerStatModeOverride specifies the override mode of\n         statistics collected by this ingress policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noOverride", -1), ("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredPriorityNoCIR", 4), ("offeredProfileCIR", 5), ("offeredPriorityCIR", 6), ("offeredLimitedProfileCIR", 7), ("offeredProfileCappedCIR", 8), ("offeredLimitedCappedCIR", 9))

class TmnxEgrPolicerStatMode(TextualConvention, Integer32):
    description = 'TmnxEgrPolicerStatMode specifies the mode of statistics collected by\n         this egress policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 8, 9, 10))
    namedValues = NamedValues(("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredProfileCIR", 4), ("offeredLimitedCappedCIR", 5), ("offeredProfileCappedCIR", 6), ("offeredTotalCirExceed", 8), ("offeredFourProfileNoCir", 9), ("offeredTotalCirFourProfile", 10))

class TmnxEgrPolicerStatModeOverride(TextualConvention, Integer32):
    description = 'TmnxEgrPolicerStatModeOverride specifies the override mode of\n         statistics collected by this egress policer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 8, 9, 10))
    namedValues = NamedValues(("noOverride", -1), ("noStats", 0), ("minimal", 1), ("offeredProfileNoCIR", 2), ("offeredTotalCIR", 3), ("offeredProfileCIR", 4), ("offeredLimitedCappedCIR", 5), ("offeredProfileCappedCIR", 6), ("offeredTotalCirExceed", 8), ("offeredFourProfileNoCir", 9), ("offeredTotalCirFourProfile", 10))

class TmnxTlsGroupId(TextualConvention, Unsigned32):
    description = 'A number used to identify a TLS Group. This ID must be unique within\n         that Service Domain.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4094)

class TSubHostId(TextualConvention, Unsigned32):
    description = 'A number used to uniquely identify a subscriber host in the system'
    status = 'current'

class TDirection(TextualConvention, Integer32):
    description = 'TDirection denotes a direction.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("both", 0), ("ingress", 1), ("egress", 2))

class TDirectionIngEgr(TextualConvention, Integer32):
    description = 'TDirectionIngEgr denotes a direction.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ingress", 1), ("egress", 2))

class TBurstLimit(TextualConvention, Integer32):
    description = 'An explicit shaping burst size for a queue. The value of -1 specifies\n         system default value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 14000000), )
class TMacFilterType(TextualConvention, Integer32):
    description = 'A type containing the possible types of MAC filters provided by the\n         system'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("isid", 2), ("vid", 3))

class TIPFilterType(TextualConvention, Integer32):
    description = 'A type containing the possible types of IP/IPv6 filters provided by\n         the system.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("vxlanVni", 2))

class TmnxPwGlobalId(TextualConvention, Unsigned32):
    description = 'A number used to identify a global pseudo-wire routing identifier.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TmnxPwGlobalIdOrZero(TextualConvention, Unsigned32):
    description = 'A number used to identify a global pseudo-wire routing identifier or\n         zero.'
    status = 'current'

class TmnxPwPathHopId(TextualConvention, Unsigned32):
    description = 'A number used to identify a specific hop associated with pseudo-wire\n         routing path.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class TmnxPwPathHopIdOrZero(TextualConvention, Unsigned32):
    description = 'A number used to identify a specific hop associated with pseudo-wire\n         routing path.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxSpokeSdpId(TextualConvention, Unsigned32):
    description = 'A number used to identify a multi-segment pseudo-wire provider-edge\n         identifier.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TmnxSpokeSdpIdOrZero(TextualConvention, Unsigned32):
    description = 'A number used to identify a multi-segment pseudo-wire provider-edge\n         identifier.'
    status = 'current'

class TmnxMsPwPeSignaling(TextualConvention, Integer32):
    description = 'A number used to identify a multi-segment pseudo-wire provider-edge\n         signaling type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("master", 2))

class TmnxLdpFECType(TextualConvention, Integer32):
    description = 'TmnxLdpFECType determines the kind of FEC that the label mapping,\n         withdraw, release and request messages are referring to.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 128, 129, 130))
    namedValues = NamedValues(("addrWildcard", 1), ("addrPrefix", 2), ("addrHost", 3), ("vll", 128), ("vpws", 129), ("vpls", 130))

class TmnxSvcOperGrpCreationOrigin(TextualConvention, Integer32):
    description = 'A number used to identify creation origin for the service operational\n         group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 7, 12))
    namedValues = NamedValues(("manual", 1), ("mvrp", 2), ("dynScript", 7), ("vsd", 12))

class TmnxOperGrpHoldUpTime(TextualConvention, Unsigned32):
    description = 'TmnxOperGrpHoldUpTime indicates time-interval in seconds for the\n         service operational-group hold uptime.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 3600)

class TmnxOperGrpHoldDownTime(TextualConvention, Unsigned32):
    description = 'TmnxOperGrpHoldDownTime indicates time-interval in seconds for the\n         service operational-group hold down time.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 3600)

class TmnxSrrpPriorityStep(TextualConvention, Integer32):
    description = 'TmnxSrrpPriorityStep indicates the range of the priority steps used by\n         the operational group to monitor SRRP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10)

class TmnxAiiType(TextualConvention, Integer32):
    description = 'TmnxAiiType indicates LDP FEC 129 Attachment Individual Identifier\n         (AII) type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("aiiType1", 1), ("aiiType2", 2))

class TmnxSpbFid(TextualConvention, Integer32):
    description = 'TmnxSpbFid indicates Shortest Path Bridging forwarding database\n         identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4095)

class TmnxSpbFidOrZero(TextualConvention, Integer32):
    description = 'TmnxSpbFid indicates Shortest Path Bridging forwarding database\n         identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class TmnxSpbBridgePriority(TextualConvention, Integer32):
    description = 'TmnxSpbFid indicates the bridge priority for Shortest Path Bridging.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

class TmnxSlopeMap(TextualConvention, Integer32):
    description = 'TmnxSlopeMap indicates the mapping style of the slope.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("low", 1), ("high", 2), ("highLow", 3))

class TmnxCdrType(TextualConvention, Integer32):
    description = 'The TmnxCdrType is an enumerated integer that describes the current\n         charging type in Charging Data Record (CDR).\n\n         pgwCdr - indicates Packet data network Gateway CDR\n         gCdr - indicates Gateway GPRS Support Node (GGSN) CDR, where\n                   GPRS stands for General Packet Radio Service.\n         eGCdr - indicates Enhanced Gateway GPRS Support Node (GGSN) CDR.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("pgwCdr", 1), ("gCdr", 2), ("eGCdr", 3))

class TmnxThresholdGroupType(TextualConvention, Integer32):
    description = 'The TmnxThresholdGroupType is an enumerated integer that describes the\n         group type in threshold based monitoring.\n\n         brMgmtLimit - indicates the group for bearer management limit\n         brMgmtCfSuccess - indicates the group for bearer management\n                           call flow success\n         brMgmtCfFailure - indicates the group for bearer management\n                           call flow failure\n         brMgmtTraffic - indicates the group for bearer management traffic\n         pathMgmt - indicates the group for path management\n         mgIsmSystem - indicates the group for the system of mobile gateway\n                       integrated service module\n         pdnConnections - indicates the group for the Packet Data Network (PDN)\n                          connections.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("brMgmtLimit", 1), ("brMgmtCfSuccess", 2), ("brMgmtCfFailure", 3), ("brMgmtTraffic", 4), ("pathMgmt", 5), ("pdnConnections", 6), ("mgIsmSystem", 7))

class TmnxVpnIpBackupFamily(TextualConvention, Bits):
    description = 'The value of TmnxVpnIpBackupFamily specifies the respective vpn family\n         for which backup paths would be enabled.'
    status = 'current'
    namedValues = NamedValues(("ipv4", 0), ("ipv6", 1))

class TmnxTunnelGroupId(TextualConvention, Unsigned32):
    description = 'The value of TmnxTunnelGroupId specifies the tunnel-group identifier.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class TmnxTunnelGroupIdOrZero(TextualConvention, Unsigned32):
    description = 'The value of TmnxTunnelGroupId specifies the tunnel-group identifier\n         including zero indicating that group-id is not specified.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

class TmnxQosBytesHex(TextualConvention, OctetString):
    description = 'Represents the QoS bytes that has been requested for the bearer\n         context of an User Equipment (UE).'
    status = 'current'
    displayHint = '2x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

class TSiteOperStatus(TextualConvention, Integer32):
    description = 'TSiteOperStatus data type is an enumerated integer that describes the\n         values used to identify the current operational state of a site.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("outOfResource", 3))

class TmnxSpbFdbLocale(TextualConvention, Integer32):
    description = 'TmnxSpbFdbLocale data type is an enumerated integer that describes the\n         values used to indicate source of forwarding database (FDB) entry for\n         Shortest Path Bridging (SPB).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("local", 1), ("sap", 2), ("sdp", 3), ("unknown", 4))

class TmnxSpbFdbState(TextualConvention, Integer32):
    description = 'TmnxSpbFdbState data type is an enumerated integer that describes the\n         values used to indicate state of the forwarding database FDB entry for\n         Shortest Path Bridging (SPB).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ok", 0), ("addModPending", 1), ("delPending", 2), ("sysFdbLimit", 3), ("noFateShared", 4), ("svcFdbLimit", 5), ("noUcast", 6))

class TmnxCdrDiagnosticAction(TextualConvention, Integer32):
    description = 'The TmnxCdrDiagnosticAction is an enumerated integer that describes\n         whether the Diagnostics should be included or excluded in the Charging\n         Data Record (CDR).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("included", 1), ("excluded", 2))

class TmnxLinkMapProfileId(TextualConvention, Integer32):
    description = 'The data type TmnxLinkMapProfileId describes the link map profile\n         identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 64)

class TmnxLinkMapProfileIdOrZero(TextualConvention, Integer32):
    description = 'The data type TmnxLinkMapProfileId describes the link map profile\n         identifier or zero.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 64), )
class TmnxDayOfWeek(TextualConvention, Integer32):
    description = 'The TmnxDayOfWeek is an enumerated integer that describes the day of\n         the week.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unspecified", 0), ("sunday", 1), ("monday", 2), ("tuesday", 3), ("wednesday", 4), ("thursday", 5), ("friday", 6), ("saturday", 7))

class TmnxDayOfWeekList(TextualConvention, Bits):
    description = 'The TmnxDayOfWeekList describes days of the week in a bitset format.'
    status = 'current'
    namedValues = NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6))

class TmnxMplsTpGlobalID(TextualConvention, Unsigned32):
    reference = "RFC 6370, 'MPLS Transport Profile (MPLS-TP) Identifiers',\n         Section 3, 'Uniquely Identifying an Operator - the Global_ID'."
    description = 'The value of TmnxMplsTpGlobalID specifies the MPLS-TP global\n         identifier.'
    status = 'current'

class TmnxMplsTpNodeID(TextualConvention, Unsigned32):
    reference = "RFC 6370, 'MPLS Transport Profile (MPLS-TP) Identifiers',\n         Section 4, 'Node and Interface Identifiers'."
    description = 'The value of TmnxMplsTpNodeID specifies the MPLS-TP node identifier.'
    status = 'current'

class TmnxMplsTpTunnelType(TextualConvention, Integer32):
    description = 'The type of this MPLS-TP tunnel entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("mplsTpStatic", 1))

class TmnxDistCpuProtPacketRateLimit(TextualConvention, Integer32):
    description = 'A packet rate limit expressed in packets per second for Distributed\n         CPU Protection Policy parameters. The value -1 means max rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )
class TmnxDistCpuProtRate(TextualConvention, Integer32):
    description = 'A kbps limiting rate in kilobits per second for Distributed CPU\n         Protection Policy parameters. The value -1 means max rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 20000000), )
class TmnxDistCpuProtBurstSize(TextualConvention, Integer32):
    description = 'The amount of buffer space (in kilobytes) assigned to a queue by\n         policer for Distributed CPU Protection Policy parameters.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 4194304), )
class TmnxDistCpuProtActionDuration(TextualConvention, Integer32):
    description = 'An exceed action rate in seconds for Distributed CPU Protection Policy\n         parameters determining hold-down duration for specified exceed-action.\n         The value of 0 means no hold-down and value of -1 means indefinite\n         hold-down duration.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 10080), )
class TmnxDistCpuProtAction(TextualConvention, Integer32):
    description = 'The TmnxDistCpuProtAction data type is an enumerated integer\n         that describes the values used to specify the action to be taken on the\n         traffic when the filter entry matches.\n         discard      (1)  packets matching the filter entry are discarded\n         low-priority (2)  packets matching the filter entry are marked as\n                           low-priority\n         none         (3)  no action is taken.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("discard", 1), ("low-priority", 2), ("none", 3))

class TmnxDistCpuProtEnforceType(TextualConvention, Integer32):
    description = 'The TmnxDistCpuProtEnforceType data type is an enumerated integer that\n         describes the values used to specify the enforcement type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class TmnxDistCpuProtProtocolId(TextualConvention, Integer32):
    description = 'The TmnxDistCpuProtProtocolId data type is an enumerated integer that\n         indicates the protocols supported for the Distributed CPU Protection\n         Policy.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("arp", 1), ("dhcp", 2), ("http-redirect", 3), ("icmp", 4), ("igmp", 5), ("mld", 6), ("ndis", 7), ("pppoe-pppoa", 8), ("all-unspecified", 9), ("mpls-ttl", 10), ("bfd-cpm", 11), ("bgp", 12), ("eth-cfm", 13), ("isis", 14), ("ldp", 15), ("ospf", 16), ("pim", 17), ("rsvp", 18))

class TmnxDistCpuProtRateType(TextualConvention, Integer32):
    description = 'The TmnxDistCpuProtRateType data type is an enumerated integer that\n         describes the rate type being applied by the policer for the\n         Distributed CPU Protection Policy.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("packets", 1), ("kbps", 2))

class TmnxDistCpuProtLogEventType(TextualConvention, Integer32):
    description = "The TmnxDistCpuProtLogEventType data type is an enumerated integer\n         that describes the state of log events for Distributed CPU Protection\n         Policy.\n         none         (0)  indicates log events is disabled\n         enable       (1)  indicates log events is enabled\n         verbose      (2)  indicates generation of additional log events to be\n                           used for debug/tuning/investigations which would have\n                           not been generated when TmnxDistCpuProtLogEventType\n                           is set to 'enable'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("enable", 1), ("verbose", 2))

class TmnxDistCpuProtState(TextualConvention, Integer32):
    description = 'The TmnxDistCpuProtState data type is an enumerated integer that\n         describes the state of the policer for the Distributed CPU Protection\n         Policy.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("exceed", 1), ("conform", 2), ("not-applicable", 3))

class TmnxIsidMFibStatus(TextualConvention, Bits):
    description = 'The TmnxIsidMFibStatus data type describes the MFIB status of the\n         ISID.'
    status = 'current'
    namedValues = NamedValues(("ok", 0), ("addPending", 1), ("delPending", 2), ("sysMFibLimit", 3), ("useDefMCTree", 4))

class TmnxBfdIntfSessOperState(TextualConvention, Integer32):
    description = 'The TmnxBfdIntfSessOperState data type is an enumerated integer that\n         describes the values used to identify the operational state of a BFD\n         session is relying upon for its fast triggering mechanism.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("connected", 2), ("broken", 3), ("peerDetectsDown", 4), ("notConfigured", 5), ("noResources", 6))

class TmnxBfdEncap(TextualConvention, Integer32):
    description = 'The TmnxBfdEncap data type is an enumerated integer indicating\n         encapsulation used for in the BFD operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("ipv4", 1))

class TLDisplayString(TextualConvention, OctetString):
    description = 'The TLDisplayString is DisplayString of 1022 characters.\n\n         Any object defined using this syntax may not exceed 1022 characters in\n         length.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1022)

class IPv6FlowLabel(TextualConvention, Integer32):
    description = "The flow identifier or Flow Label in an IPv6\n         packet header that may be used to discriminate\n         traffic flows.  (RFC3595).\n         The value -1 indicates 'no flowLabel' "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1048575), )
class IPv6FlowLabelMask(TextualConvention, Unsigned32):
    description = 'IPv6 flow label mask'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1048575)

class TmnxWlanGwIsaGrpId(TextualConvention, Unsigned32):
    description = 'The TmnxWlanGwIsaGrpId data type contains an identification number for\n         a Wireless Local Access Network Gateway Integrated Service Adaptor\n         group.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4)

class TmnxWlanGwIsaGrpIdOrZero(TextualConvention, Unsigned32):
    description = 'The TmnxWlanGwIsaGrpIdOrZero data type contains an identification\n         number for a Wireless Local Access Network Gateway Integrated Service\n         Adaptor (ISA) group.\n\n         The value zero means that no WLAN Gateway ISA Group is defined.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4)

class TmnxMplsLdpNgIdType(TextualConvention, Integer32):
    description = 'A value that represents the type of LDP identifier\n\n         ipv4(1)     An IPv4 identifier type as defined by the\n                     InetAddressIPv4 textual convention.\n\n         ipv6(2)     An IPv6 identifier type as defined by the\n                     InetAddressIPv6 textual convention.\n\n         Each definition of a concrete TmnxMplsLdpNgIdType value must be\n         accompanied by a definition of a textual convention for use with that\n         TmnxMplsLdpNgIdType.\n\n         Implementations must ensure that TmnxMplsLdpNgIdType objects\n         and any dependent objects (e.g., TmnxMplsLdpNgIdentifier objects) are\n         consistent.  An inconsistentValue error must be generated\n         if an attempt to change an TmnxMplsLdpNgIdType object would,\n         for example, lead to an undefined TmnxMplsLdpNgIdentifier value. In\n         particular, TmnxMplsLdpNgIdType/TmnxMplsLdpNgIdentifier pairs must be\n         changed together if the identifier type changes (e.g., from\n         ipv6(2) to ipv4(1)).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class TmnxMplsLdpNgIdentifier(TextualConvention, OctetString):
    description = "The LDP identifier is a eighteen octet quantity which is used to\n         identify a Label Switch Router (LSR) label space.\n\n         When the LDP Id type is 'ipv4', the first four octets encode an IP\n         address assigned to the LSR, and next two octets identify a specific\n         label space within the LSR assigned to the LSR.\n\n         When the LDP Id type is 'ipv6', the first sixteen octets encode an IP\n         address an assigned to the LSR, and last two octets identify a\n         specific label space within the LSR."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 18)

class TmnxMplsLsrNgIdentifier(TextualConvention, OctetString):
    description = 'The Label Switch Router (LSR) identifier is the first 16 bytes or the\n         Router Id component of the IPv6 Label Distribution Protocol (LDP)\n         identifier.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class TmnxLagPerLinkHashClass(TextualConvention, Integer32):
    description = 'The TmnxLagPerLinkHashClass is the class of traffic which along with\n         the relative weight is used in the egress hashing on the LAG.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3)

class TmnxLagPerLinkHashClassOrNone(TextualConvention, Integer32):
    description = 'The TmnxLagPerLinkHashClass is the class of traffic which along with\n         the relative weight is used in the egress hashing on the LAG.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 3)

class TmnxLagPerLinkHashWeight(TextualConvention, Integer32):
    description = 'The TmnxLagPerLinkHashWeight is the relative weight of the traffic\n         which along with the class is used in the egress hashing on the LAG.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1024)

class BgpConnectRetryTime(TextualConvention, Integer32):
    reference = 'BGP4-MIB.bgpPeerConnectRetryInterval'
    description = "The value of BgpConnectRetryTime is a time interval in seconds for a\n         'ConnectRetry' timer.default is 120 seconds."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class BgpHoldTime(TextualConvention, Integer32):
    reference = 'BGP4-MIB.bgpPeerHoldTime'
    description = 'The value of BgpHoldTime is a time interval in seconds for Hold Timer.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), )
class TmnxInternalSchedWeightMode(TextualConvention, Integer32):
    description = "The value of TmnxInternalSchedWeightMode specifies the weight-mode\n         applied to queues using internal-scheduler. Various modes can be\n         enumerated as follows:\n\n            noOverride (1)        - follows queue behavior specified at the card\n                                    level.\n            default (2)           - queues are equally weighted except for\n                                    mixed-speed LAG (when the value of\n                                    TIMETRA-LAG-MIB.mib::tLagPerFpIngQueuing is\n                                    set to 'false (2)') where queues are weighted\n                                    based on port-speed.\n            forceEqual (3)        - all queues are always equally weighted.\n            offeredLoad (4)       - queues are weighted based on offered load.\n            cappedOfferedLoad (5) - queues are weighted based on offered load\n                                    capped by admin PIR."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("noOverride", 1), ("default", 2), ("forceEqual", 3), ("offeredLoad", 4), ("cappedOfferedLoad", 5))

class TmnxHigh32(TextualConvention, Unsigned32):
    description = 'The upper 32 bits of a 64 bit value.'
    status = 'current'

class TmnxLow32(TextualConvention, Unsigned32):
    description = 'The lower 32 bits of a 64 bit value.'
    status = 'current'

class TQosQueuePIRRate(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 2000000000), )
class TQosQueueCIRRate(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2000000000), )
class TQosQueuePIRRateOverride(TextualConvention, Integer32):
    description = 'The PIR rate to be used in kbps. The value -1 means maximum rate. A\n         value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 2000000000), )
class TQosQueueCIRRateOverride(TextualConvention, Integer32):
    description = 'The CIR rate to be used in kbps. The value -1 means maximum rate. A\n         value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2000000000), )
class TResolveStatus(TextualConvention, Integer32):
    description = 'The TResolveStatus indicates resolution status of the tunnels.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disabled", 0), ("filter", 1), ("any", 2), ("match-family-ip", 3))

class LAGInterfaceNumber(TextualConvention, Integer32):
    description = "The unique number identifying a LAG interface.\n\n         There are maximum 64 LAG interfaces, when the value of\n         TIMETRA-CHASSIS-MIB::tmnxChassisType is '5' (ESS-1/SR-1)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 800)

class LAGInterfaceNumberOrZero(TextualConvention, Integer32):
    description = 'LAGInterfaceNumberOrZero is similar to LAGInterfaceNumber but includes\n         zero indicating invalid LAG identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 800), )
class TmnxRouteTargetOrigin(TextualConvention, Integer32):
    description = 'TmnxRouteTargetOrigin indicates the origin of the route-target policy.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("configured", 1), ("derivedVpls", 2), ("derivedEvi", 3), ("vsi", 4))

class TmnxRouteDistType(TextualConvention, Integer32):
    description = 'TmnxRouteDistType indicates the type of the route-distinguisher.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("configured", 1), ("derivedVpls", 2), ("derivedEvi", 3), ("auto", 4), ("default", 5))

class TmnxScriptAuthType(TextualConvention, Integer32):
    description = 'The tmnxCliScriptAuthUserType datatype is an enumerated integer that\n         indicates the type of module executing a CLI command script.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("cron", 1), ("xmpp", 2), ("event-script", 3), ("vsd", 4))

class TmnxISIDNoZero(TextualConvention, Integer32):
    description = 'The TmnxISID specifies a 24 bit (1..16777215) service instance\n         identifier for the service. As part of the Shortest Path Bridging\n         (SPB) frames, it is used at the destination PE as a demultiplexor\n         field.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16777215)

class TmnxSvcEvi(TextualConvention, Integer32):
    description = 'The TmnxSvcEvi specifies an ethernet EVPN identifier value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TmnxSecRadiusServAlgorithm(TextualConvention, Integer32):
    description = 'The TmnxSecRadiusServAlgorithm data type is an enumerated integer that\n         indicates the algorithm used to access the list of configured RADIUS\n         servers:\n         - direct      (1): The first server will be used as primary server for\n                            all requests, the second as secondary and so on.\n         - round-robin (2): The first server will be used as primary server for\n                            the first request, the second server as primary for\n                            the second request, and so on. If the router gets\n                            to the end of the list, it starts again with the\n                            first server.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("direct", 1), ("round-robin", 2))

class TmnxSvcEviOrZero(TextualConvention, Integer32):
    description = 'The TmnxSvcEviOrZero specifies an ethernet EVPN identifier value. Zero\n         indicates no such value specified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxSubTerminationType(TextualConvention, Integer32):
    description = 'The TmnxSubTerminationType indicates how the subscriber host or\n         session is terminated.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("local", 1), ("localWholesale", 2), ("localRetail", 3))

class TmnxSubTerminationTypeOrZero(TextualConvention, Integer32):
    description = 'The TmnxSubTerminationType indicates how the subscriber host or\n         session is terminated. Zero indicates no subscriber host is\n         terminated.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("local", 1), ("localWholesale", 2), ("localRetail", 3))

class TmnxLongDisplayString(TextualConvention, OctetString):
    description = 'The TmnxLongDisplayString indicates a long DisplayString.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class TmnxLongDisplayStringToBinary(TmnxLongDisplayString):
    description = 'The TmnxLongDisplayString indicates a long DisplayString.'
    status = 'current'

class TmnxLongDisplayStringLegacyBinary(TextualConvention, OctetString):
    description = 'The TmnxLongDisplayString indicates a long DisplayString.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 900)

class TmnxProxyEntryType(TextualConvention, Integer32):
    description = 'The TmnxProxyEntryType indicates type of proxy ARP or ND entry.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("evpn", 1), ("stat", 2), ("dyn", 3), ("dup", 4))

class TmnxCBFClasses(TextualConvention, Bits):
    description = 'The TmnxCBFClasses indicates a set of forwarding classes.'
    status = 'current'
    namedValues = NamedValues(("be", 0), ("l2", 1), ("af", 2), ("l1", 3), ("h2", 4), ("ef", 5), ("h1", 6), ("nc", 7), ("defaultLsp", 8))

class TmnxUrpfCheckMode(TextualConvention, Integer32):
    description = "The TmnxUrpfCheckMode is the mode of operation of Unicast Reverse Path\n         Forwarding (uRPF).\n\n         A value of 'strict' means that uRPF checks if the incoming packet has\n         a source address that matches a prefix in the routing table, and if\n         the interface expects to receive a packet with this source address\n         prefix.\n\n         A value of 'loose' means that the uRPF checks if the incoming packet\n         has a source address with a corresponding prefix in the routing table,\n         but not if the interface expects to receive a packet with a specific\n         source address prefix.\n\n         A value of 'strictNoEcmp' means that the uRPF drops a packet with a\n         source address that matches an ECMP route and otherwise behaves the\n         same as in 'strict' mode."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("strict", 1), ("loose", 2), ("strictNoEcmp", 3))

class TmnxUserPassword(DisplayString):
    description = 'The value of TmnxUserPassword indicates a password as a plaintext\n         string, or as a bcrypt encrypted hash.\n\n         The value of TmnxUserPassword cannot be more than 56 characters if it\n         is a plaintext string.\n\n         Any GET request on this type of object returns an empty string.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 60)

class TmnxUdpPort(TextualConvention, Integer32):
    description = 'The value of TmnxUdpPort is the port used to send messages\n         to an event collector target.  514 is the IANA assigned port number\n         for syslog.  162 is the IANA assigned port number for SNMP\n         notifications.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxUuid(TextualConvention, OctetString):
    description = 'The value of TmnxUuid specifies the Universally Unique Identifier\n         (UUID). The UUID consists of 32 hexadecimal digits.'
    status = 'current'
    displayHint = '4x-2x-2x-2x-6x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class TmnxSyslogFacility(TextualConvention, Integer32):
    reference = 'The Syslog Protocol (RFC5424): Table 1'
    description = 'The value of TmnxSyslogFacility is an enumerated integer that\n         specifies which syslog facility is the intended destination for the\n         log event stream.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kernel", 0), ("user", 1), ("mail", 2), ("systemd", 3), ("auth", 4), ("syslogd", 5), ("printer", 6), ("netnews", 7), ("uucp", 8), ("cron", 9), ("authpriv", 10), ("ftp", 11), ("ntp", 12), ("logaudit", 13), ("logalert", 14), ("cron2", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

class TmnxSyslogSeverity(TextualConvention, Integer32):
    reference = 'The Syslog Protocol (RFC5424): Table 2'
    description = 'The value of TmnxSyslogSeverity is an enumerated integer that\n         specifies the severity levels of syslog messages.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7))

class TmnxEvpnMultiHomingState(TextualConvention, Integer32):
    description = 'The value of TmnxEvpnMultiHomingState indicates multi-homing state of\n         the element.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disabled", 0), ("singleActive", 1), ("singleActiveNoEsiLabel", 2), ("allActive", 3))

class TmnxBgpEvpnAcEthTag(TextualConvention, Integer32):
    description = 'The TmnxBgpEvpnAcEthTag indicates ethernet tag value of the BGP EVPN\n         attachment circuit.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 16777215)

class TmnxL2tpTunnelGroupName(DisplayString):
    description = 'The TmnxL2tpTunnelGroupName data type contains a valid string to\n         identify a Layer Two Tunneling Protocol Tunnel Group.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 63)

class TmnxL2tpTunnelGroupNameOrEmpty(DisplayString):
    description = 'The TmnxL2tpTunnelGroupNameOrEmpty data type contains a valid string\n         to identify a Layer Two Tunneling Protocol Tunnel Group.\n\n         An empty string indicates that no Tunnel Group is defined.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 63)

class TFilterID(TextualConvention, Unsigned32):
    description = 'The identification number of a filter. 0 indicates an invalid\n         filter-id.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TIPFilterID(TFilterID):
    description = 'The identification number of an IP filter.'
    status = 'current'

class TDHCPFilterID(TFilterID):
    description = 'The identification number of a DHCP filter.'
    status = 'current'

class TEntryIdOrZero(TEntryIndicator):
    description = 'uniquely identifies an entry in a policy or filter table.\n         to facilitate insertion of entries in the tables, we recommend\n         assigning entry IDs by 10s:  10, 20, 30, etc.\n         The value 0, means that the object does not refer to a filter\n         entry at this time.'
    status = 'current'
    subtypeSpec = TEntryIndicator.subtypeSpec + ValueRangeConstraint(0, 65535)

class MciBoolean(TextualConvention, Integer32):
    description = 'This provides MCI type to for the objects which do not have well\n         defined defaults'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mciTrue", 1), ("mciFalse", 2))

class TmnxPppCpState(TextualConvention, Integer32):
    description = 'The TmnxPppCpState data type is an enumerated integer that\n         describes the current status of a PPP link.  It can be applied\n         to both LCP and NCP links.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("initial", 1), ("starting", 2), ("closed", 3), ("stopped", 4), ("closing", 5), ("stopping", 6), ("requestSent", 7), ("ackReceived", 8), ("ackSent", 9), ("opened", 10))

class TmnxRipNgAuthType(TextualConvention, Integer32):
    reference = 'RIP2-MIB.rip2IfConfAuthType'
    description = 'The TmnxRipNgAuthType TC defines the authentication method to be\n         used for RIP/RIP-NG. Allowed values are :\n           noAuthentication(1) - No authentication method\n           simplePassword(2)   - Simple password based authentication\n              md5(3)              - 16 byte MD5 Authentication\n              md20(4)             - 20 byte MD5 Authentication.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noAuthentication", 1), ("simplePassword", 2), ("md5", 3), ("md20", 4))

class TmnxRipNgAuthKey(TextualConvention, OctetString):
    reference = 'RIP2-MIB.rip2IfConfAuthKey'
    description = 'The TmnxRipNgAuthKey TC defines the authentication key to be used when\n         the authentication type has been configured to either\n         simplePassword(2), md5(3) or md20(4) $feature (RIP_AUTH_EXTENSION) {or\n         md16(5) or md5-20(6) }(see TmnxRipNgAuthType).'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TmnxAddressAndPrefixType(InetAddressType):
    description = ''
    status = 'current'

class TmnxAddressAndPrefixAddress(InetAddress):
    description = ''
    status = 'current'

class TmnxAddressAndPrefixPrefix(InetAddressPrefixLength):
    description = ''
    status = 'current'

class TmnxIpv6AddressAndPrefixAddress(InetAddressIPv6):
    description = ''
    status = 'current'

class TmnxIpv6AddressAndPrefixPrefix(InetAddressPrefixLength):
    description = ''
    status = 'current'

class TmnxIpv4AddressAndMaskOrPrefixAddress(TextualConvention, IpAddress):
    description = ''
    status = 'current'

class TmnxIpv4AddressAndMaskOrPrefixMask(TextualConvention, IpAddress):
    description = ''
    status = 'current'

class TmnxIpv4AddressAndMaskOrPrefixPrefix(IpAddressPrefixLength):
    description = ''
    status = 'current'

class TmnxIpv4AddressAndPrefixAddress(TextualConvention, IpAddress):
    description = ''
    status = 'current'

class TmnxIpv4AddressAndPrefixPrefix(IpAddressPrefixLength):
    description = ''
    status = 'current'

class TmnxIpv6AddressAndMaskOrPrefixAddress(InetAddressIPv6):
    description = ''
    status = 'current'

class TmnxIpv6AddressAndMaskOrPrefixMask(InetAddressIPv6):
    description = ''
    status = 'current'

class TmnxIpv6AddressAndMaskOrPrefixPrefix(InetAddressPrefixLength):
    description = ''
    status = 'current'

class TmnxAddressAndMaskOrPrefixType(InetAddressType):
    description = ''
    status = 'current'

class TmnxAddressAndMaskOrPrefixAddress(InetAddress):
    description = ''
    status = 'current'

class TmnxAddressAndMaskOrPrefixPrefix(InetAddressPrefixLength):
    description = ''
    status = 'current'

class TmnxAddressAndMaskOrPrefixMask(InetAddress):
    description = ''
    status = 'current'

class TmnxAddressWithZoneType(InetAddressType):
    description = ''
    status = 'current'

class TmnxAddressWithZoneAddress(InetAddress):
    description = ''
    status = 'current'

class THsPirRate(TextualConvention, Unsigned32):
    description = 'The HS PIR rate to be used in Mbps. The value of\n         4294967295(0xFFFFFFFF) means maximum rate.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 100000), ValueRangeConstraint(4294967295, 4294967295), )
class THsPirRateOverride(TextualConvention, Unsigned32):
    description = 'The HS PIR rate to be used in Mbps. The value of\n         4294967295(0xFFFFFFFF) means maximum rate. The value of\n         4294967294(0xFFFFFFFE) means no override.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 100000), ValueRangeConstraint(4294967294, 4294967294), ValueRangeConstraint(4294967295, 4294967295), )
class THsSchedulerPolicyGroupId(TextualConvention, Integer32):
    description = 'The value of THsSchedulerPolicyGroupId specifies the identification\n         number of a HS scheduler policy group.  A value of zero (0)\n         indicates that no specific group identification has been assigned for\n         this object. When an object of type THsSchedulerPolicyGroupId is\n         an SNMP table index, an index value of zero (0) is not allowed and a\n         noCreation error will be returned.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1), )
class THsSchedulerPolicyWeight(TextualConvention, Integer32):
    description = 'The weight of the specified HS entity while feeding into the parent.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 127)

class THsSchedulerPolicyWeightOverride(TextualConvention, Integer32):
    description = 'The weight of the specified HS entity while feeding into the parent. A\n         value of -2 specifies no override.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(1, 127), )
class TmnxWaveKey(TextualConvention, Unsigned32):
    description = "The value of TmnxWaveKey specifies the Wavelength to be transmitted on\n         the interface's optical signal.\n\n         The following table describes the possible values based on ITU\n         channel. Key1 and Key2 must match in modulo 2 with each other.\n\n         Index   ITU          Key 1        Key 2\n                channel   First Last      First Last\n         -------------------------------------------\n            0      61     1548  1548      2032  2032  // 1696 Test Channel\n\n            // Original Tropic Channels (index 1 to 32)\n            1      59        1    15       545   559\n            2      58       18    32       562   576\n            3      57       35    49       579   593\n            4      56       52    66       596   610\n            5      54       69    83       613   627\n            6      53       86   100       630   644\n            7      52      103   117       647   661\n            8      51      120   134       664   678\n            9      49      137   151       681   695\n           10      48      154   168       698   712\n           11      47      171   185       715   729\n           12      46      188   202       732   746\n           13      44      205   219       749   763\n           14      43      222   236       766   780\n           15      42      239   253       783   797\n           16      41      256   270       800   814\n           17      39      273   287       817   831\n           18      38      290   304       834   848\n           19      37      307   321       851   865\n           20      36      324   338       868   882\n           21      34      341   355       885   899\n           22      33      358   372       902   916\n           23      32      375   389       919   933\n           24      31      392   406       936   950\n           25      29      409   423       953   967\n           26      28      426   440       970   984\n           27      27      443   457       987  1001\n           28      26      460   474      1004  1018\n           29      24      477   491      1021  1035\n           30      23      494   508      1038  1052\n           31      22      511   525      1055  1069\n           32      21      528   542      1072  1086\n\n           // 1696 Extension 42 channels (index 33 to 42)\n           33      60     1089  1103      1573  1587\n           34      55     1106  1120      1590  1604\n           35      50     1123  1137      1607  1621\n           36      45     1140  1154      1624  1638\n           37      40     1157  1171      1641  1655\n           38      35     1174  1188      1658  1672\n           39      30     1191  1205      1675  1689\n           40      25     1208  1222      1692  1706\n           41      20     1225  1239      1709  1723\n           42      19     1242  1256      1726  1740\n\n           // 1830 Extension to 44 channels (index 43 and 44)\n           43      18     1259  1273      1743  1757\n           44      17     1276  1290      1760  1774\n\n           // 1830 Extension to 88 channels (index 45 to 88)\n           45     595     1293  1307      1777  1791\n           46     585     1310  1324      1794  1808\n           47     575     1327  1341      1811  1825\n           48     565     1344  1358      1828  1842\n           49     545     1361  1375      1845  1859\n           50     535     1378  1392      1862  1876\n           51     525     1395  1409      1879  1893\n           52     515     1412  1426      1896  1910\n           53     495     1429  1443      1913  1927\n           54     485     1446  1460      1930  1944\n           55     475     1463  1477      1947  1961\n           56     465     1480  1494      1964  1978\n           57     445     1497  1511      1981  1995\n           58     435     1514  1528      1998  2012\n           59     425     1531  1545      2015  2029\n           60     415     1548  1562      2032  2046\n           61     395     3585  3599      2049  2063\n           62     385     3602  3616      2066  2080\n           63     375     3619  3633      2083  2097\n           64     365     3636  3650      2100  2114\n           65     345     3653  3667      2117  2131\n           66     335     3670  3684      2134  2148\n           67     325     3687  3701      2151  2165\n           68     315     3704  3718      2168  2182\n           69     295     3721  3735      2185  2199\n           70     285     3738  3752      2202  2216\n           71     275     3755  3769      2219  2233\n           72     265     3772  3786      2236  2250\n           73     245     3789  3803      2253  2267\n           74     235     3806  3820      2270  2284\n           75     225     3823  3837      2287  2301\n           76     215     3840  3854      2304  2318\n           77     605     3857  3871      2321  2335\n           78     555     3874  3888      2338  2352\n           79     505     3891  3905      2355  2369\n           80     455     3908  3922      2372  2386\n           81     405     3434  3448      3946  3960\n           82     355     3451  3465      3963  3977\n           83     305     3468  3482      3980  3994\n           84     255     3485  3499      3997  4011\n           85     205     3502  3516      4014  4028\n           86     195     3519  3533      4031  4045\n           87     185     3536  3550      4048  4062\n           88     175     3553  3567      4065  4079\n         -------------------------------------------"
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4095)

class TmnxSubBondingConnIdOrEmpty(TextualConvention, Unsigned32):
    description = "The data type TmnxSubBondingConnId represents the index of the bonding\n         connection. The value '0' means that index is not specified."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2), )
class TBurstLimitOverride(TextualConvention, Integer32):
    description = "An explicit shaping burst size for a queue. or scheduler or\n         aggregate-rate-limit. The value -1 means that the actual value is\n         derived from the corresponding buffer policy's default value. A value\n         of -2 specifies no override."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-2, -2), ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 14000000), )
class TmnxEvpnMHEthSegStatus(TextualConvention, Integer32):
    description = 'The TmnxEvpnMHEthSegStatus data type is an enumerated integer that\n         describes the status of an ethernet segment associated with the given\n         SAP or SDP binding.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("df", 1), ("ndf", 2), ("notesmanaged", 3))

class TmnxVxlanInstance(TextualConvention, Unsigned32):
    description = 'The TmnxVxlanInstance data type indicates range for the VXLAN\n         instance.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1)

class TmnxSvcEvpnMplsTransportType(TextualConvention, Integer32):
    description = 'The type of this transport entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("invalid", 0), ("local", 1), ("static", 2), ("rsvp", 3), ("ldp", 4), ("ospf", 5), ("isis", 6), ("bgp", 7), ("srTe", 8), ("udp", 9), ("srPolicy", 10), ("mplsFwdPolicy", 11), ("ribApi", 12), ("srOspf3", 13))

class TmnxMplsLabel(TextualConvention, Unsigned32):
    description = 'The TmnxMplsLabel data type indicates range for MPLS label.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(32, 1048575)

class TmnxMplsLabelOrZero(TextualConvention, Unsigned32):
    description = 'The TmnxMplsLabelOrZero data type indicates range for MPLS label.  The\n         value 0 indicates that no MPLS label is specified.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(32, 1048575), )
class TmnxMplsLspBandwidth(TextualConvention, Unsigned32):
    description = 'The TmnxMplsLspBandwidth data type indicates maximum bandwidth range.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 6400000)

class TmnxVni(TextualConvention, Unsigned32):
    description = 'The TmnxVni data type indicates range for VNI.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16777215)

class TmnxVniOrZero(TextualConvention, Unsigned32):
    description = 'The TmnxVni data type indicates range for VNI.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16777215)

class PwPortIdOrZero(TextualConvention, Unsigned32):
    description = "PwPortIdOrZero indicates the range for pw port id's with 0 as the\n         default value."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32767), )
class TmnxCliEngine(TextualConvention, Integer32):
    description = 'The value of TmnxCliEngine specifies the CLI engine type.\n         Values:\n           classicCli    (1) - Classic CLI engine.\n           mdCli         (2) - Model-Driven CLI engine.\n           systemDerived (3) - Default value. CLI engine derived from system configuration-mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("classicCli", 1), ("mdCli", 2), ("systemDerived", 3))

class TmnxRsvpSessionNameString(DisplayString):
    description = 'The TmnxRsvpSessionNameString type indicates the RSVP session name\n         which has extended from 80 to 160 characters.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 160)

class TmnxQosMdAutoPolicyID(TextualConvention, Unsigned32):
    description = 'The identification number of a policy for Qos objects. This ID must be\n         unique within the Qos Domain. The value 0 is used as the null ID.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 65535), )
class TmnxQosMdAutoIDCount(TextualConvention, Unsigned32):
    description = 'This data type describes the count of policy IDs that has already been\n         assigned for Qos objects.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TmnxNhgDownReason(TextualConvention, Integer32):
    description = 'The reason for next-hop group being operationally down.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3, 4, 5))
    namedValues = NamedValues(("notApplicable", 0), ("nextHopNotResolved", 1), ("nextHopIsLocal", 3), ("nextHopIsMcast", 4), ("resTypeMismatch", 5))

class TmnxQosRateHigh32(TmnxHigh32):
    description = 'The upper 32 bits of a 64 bit rate value.'
    status = 'current'
    subtypeSpec = TmnxHigh32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1), ValueRangeConstraint(4294967295, 4294967295), )
class TmnxQosRateLow32(TmnxLow32):
    description = 'The lower 32 bits of a 64 bit rate value.'
    status = 'current'
    subtypeSpec = TmnxLow32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class AluNgeKeygroupIdOrZero(TextualConvention, Unsigned32):
    description = 'A number used to identify an entry in the aluNgeKeygroupTable or zero.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 127)

class TmnxEsaNum(TextualConvention, Unsigned32):
    description = "The TmnxEsaNum data type contains an identification number for an\n         Extended Service Appliance. The value '0' indicates an invalid\n         reference."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 16), )
class TmnxEsaVappNum(TextualConvention, Unsigned32):
    description = "The TmnxEsaVappNum type contains an identification number for the\n         Virtual Application on an Extended Service Appliance. The value '0'\n         indicates an invalid reference."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4), )
class TPolRateTypeRefOrLocalLimit(TextualConvention, Integer32):
    description = "The type of the PIR/CIR percent rate. The value 'kbps' means the rate\n         is specified in kbps. The value 'percentLocalLimit' means the rate is\n         specified in percentage of local limit. The value\n         'percentReferPortLimit' means the rate is specified in percentage of\n         reference port limit."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("kbps", 1), ("percentLocalLimit", 2), ("reserved3", 3))

class TPolicerRateTypeWithRefLimit(TextualConvention, Integer32):
    description = "The type of the PIR/CIR percent rate. The value 'kbps' means the rate\n         is specified in kbps. The value 'percentPortLimit' means the rate is\n         specified in percentage of port limit. The value 'percentLocalLimit'\n         means the rate is specified in percentage of local limit. The value\n         'percentReferPortLimit' means the rate is specified in percentage of\n         reference port limit."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("kbps", 1), ("percentPortLimit", 2), ("percentLocalLimit", 3), ("reserved4", 4))

class TWredSlopeProfile(TextualConvention, Integer32):
    description = "The profile marking of a packet. Value of 'in' specifies in-profile\n         marking. Value of 'out' specifies out-profile marking. Value of 'none'\n         specifies the profile marking of the packet will be inherited from the\n         existing enqueuing priority derived from earlier matches in the\n         classification hierarchy."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))
    namedValues = NamedValues(("in", 1), ("out", 2), ("exceed", 4), ("inplus", 5))

class TDEWredSlopeProfile(TextualConvention, Integer32):
    description = "This textual convention specifies the profile marking of a packet.\n\n         Value of 'in' specifies the in-profile marking.\n\n         Value of 'out' specifies the out-profile marking.\n\n         Value of 'de' specifies that the profile marking will be based on the DE\n         (Drop-Eligible) bit.  DE bit-value of '0' specifies in-profile and DE\n         bit value of '1' specifies out-profile marking."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("in", 1), ("out", 2), ("de", 3), ("exceed", 4), ("inplus", 5))

class TmnxFlexAlgoId(TextualConvention, Unsigned32):
    description = 'TmnxFlexAlgoId identifies a specific Flexible Algorithm in the system.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(128, 255)

class TmnxTreeSidOwner(TextualConvention, Integer32):
    description = 'TmnxTreeSidOwner identifies owner information for tree-sid feature.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("static", 1), ("pce", 2), ("srPol", 3))

class TmnxTreeSidOrigin(TextualConvention, Integer32):
    description = 'TmnxTreeSidOrigin identifies origin information for tree-sid feature.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(10, 20, 30))
    namedValues = NamedValues(("pcep", 10), ("bgpSrPolicy", 20), ("configuration", 30))

mibBuilder.exportSymbols("TIMETRA-TC-MIB", AluNgeKeygroupIdOrZero=AluNgeKeygroupIdOrZero, BgpConnectRetryTime=BgpConnectRetryTime, BgpHoldTime=BgpHoldTime, BgpPeeringStatus=BgpPeeringStatus, ClassIndex=ClassIndex, ClassIndexOrNone=ClassIndexOrNone, DateAndTimeOrEmpty=DateAndTimeOrEmpty, Dot1PPriority=Dot1PPriority, Dot1PPriorityMask=Dot1PPriorityMask, Dot1PPriorityNonZeroMask=Dot1PPriorityNonZeroMask, IPv6FlowLabel=IPv6FlowLabel, IPv6FlowLabelMask=IPv6FlowLabelMask, InterfaceIndex=InterfaceIndex, IpAddressPrefixLength=IpAddressPrefixLength, LAGInterfaceNumber=LAGInterfaceNumber, LAGInterfaceNumberOrZero=LAGInterfaceNumberOrZero, MciBoolean=MciBoolean, PYSNMP_MODULE_ID=timetraTCMIBModule, PwPortIdOrZero=PwPortIdOrZero, QTag=QTag, QTagFullRange=QTagFullRange, QTagFullRangeOrNone=QTagFullRangeOrNone, QTagOrZero=QTagOrZero, SdpBindId=SdpBindId, ServiceAccessPoint=ServiceAccessPoint, ServiceAdminStatus=ServiceAdminStatus, ServiceOperStatus=ServiceOperStatus, SvcISID=SvcISID, TAdaptationRule=TAdaptationRule, TAdaptationRuleOverride=TAdaptationRuleOverride, TAdvCfgRate=TAdvCfgRate, TAnyQosPolicyID=TAnyQosPolicyID, TAnyQosPolicyIDorZero=TAnyQosPolicyIDorZero, TAtmTdpDescrType=TAtmTdpDescrType, TBWRateType=TBWRateType, TBurstHundredthsOfPercent=TBurstHundredthsOfPercent, TBurstLimit=TBurstLimit, TBurstLimitOverride=TBurstLimitOverride, TBurstPercent=TBurstPercent, TBurstPercentOrDefault=TBurstPercentOrDefault, TBurstPercentOrDefaultOverride=TBurstPercentOrDefaultOverride, TBurstSize=TBurstSize, TBurstSizeBytes=TBurstSizeBytes, TBurstSizeBytesOverride=TBurstSizeBytesOverride, TBurstSizeBytesOvr=TBurstSizeBytesOvr, TBurstSizeOverride=TBurstSizeOverride, TCIRPercentOverride=TCIRPercentOverride, TCIRRate=TCIRRate, TCIRRateOverride=TCIRRateOverride, TClassBurstLimit=TClassBurstLimit, TCpmFilterBurstSize=TCpmFilterBurstSize, TCpmProtPolicyID=TCpmProtPolicyID, TCpmProtPolicyIDOrDefault=TCpmProtPolicyIDOrDefault, TDEProfile=TDEProfile, TDEValue=TDEValue, TDEWredSlopeProfile=TDEWredSlopeProfile, TDHCPFilterID=TDHCPFilterID, TDSCPFilterActionValue=TDSCPFilterActionValue, TDSCPName=TDSCPName, TDSCPNameOrEmpty=TDSCPNameOrEmpty, TDSCPValue=TDSCPValue, TDSCPValueOrNone=TDSCPValueOrNone, TDirection=TDirection, TDirectionIngEgr=TDirectionIngEgr, TEgrDynPolicerIdOrNone=TEgrDynPolicerIdOrNone, TEgrHsmdaPerPacketOffsetOvr=TEgrHsmdaPerPacketOffsetOvr, TEgrPolicerId=TEgrPolicerId, TEgrPolicerIdOrNone=TEgrPolicerIdOrNone, TEgrRateModType=TEgrRateModType, TEgressHsmdaCounterId=TEgressHsmdaCounterId, TEgressHsmdaCounterIdOrZero=TEgressHsmdaCounterIdOrZero, TEgressHsmdaPerPacketOffset=TEgressHsmdaPerPacketOffset, TEgressHsmdaQueueId=TEgressHsmdaQueueId, TEgressPerPacketOffset=TEgressPerPacketOffset, TEgressPerPacketOffsetOvr=TEgressPerPacketOffsetOvr, TEgressPolicerId=TEgressPolicerId, TEgressPolicerIdOrNone=TEgressPolicerIdOrNone, TEgressProfile=TEgressProfile, TEgressProfileOrNone=TEgressProfileOrNone, TEgressQPerPacketOffset=TEgressQPerPacketOffset, TEgressQueueId=TEgressQueueId, TEntryId=TEntryId, TEntryIdOrZero=TEntryIdOrZero, TEntryIndicator=TEntryIndicator, TExpSecondaryShaperClassRate=TExpSecondaryShaperClassRate, TExpSecondaryShaperPIRRate=TExpSecondaryShaperPIRRate, TFCName=TFCName, TFCNameOrEmpty=TFCNameOrEmpty, TFCSet=TFCSet, TFCType=TFCType, TFCTypeOrNone=TFCTypeOrNone, TFIRRate=TFIRRate, TFilterID=TFilterID, TFrameType=TFrameType, THPolCIRRate=THPolCIRRate, THPolCIRRateOverride=THPolCIRRateOverride, THPolPIRRate=THPolPIRRate, THPolPIRRateOverride=THPolPIRRateOverride, THPolVirtualScheCIRRate=THPolVirtualScheCIRRate, THPolVirtualSchePIRRate=THPolVirtualSchePIRRate, THSMDABurstSizeBytes=THSMDABurstSizeBytes, THSMDABurstSizeBytesOverride=THSMDABurstSizeBytesOverride, THSMDAQueueBurstLimit=THSMDAQueueBurstLimit, THsClassWeightOverride=THsClassWeightOverride, THsPirRate=THsPirRate, THsPirRateOverride=THsPirRateOverride, THsSchedulerPolicyGroupId=THsSchedulerPolicyGroupId, THsSchedulerPolicyWeight=THsSchedulerPolicyWeight, THsSchedulerPolicyWeightOverride=THsSchedulerPolicyWeightOverride, THsWrrWeightOvr=THsWrrWeightOvr, THsmdaCIRKRate=THsmdaCIRKRate, THsmdaCIRKRateOverride=THsmdaCIRKRateOverride, THsmdaCIRMRate=THsmdaCIRMRate, THsmdaCIRMRateOverride=THsmdaCIRMRateOverride, THsmdaCounterIdOrZero=THsmdaCounterIdOrZero, THsmdaCounterIdOrZeroOrAll=THsmdaCounterIdOrZeroOrAll, THsmdaPIRKRate=THsmdaPIRKRate, THsmdaPIRKRateOverride=THsmdaPIRKRateOverride, THsmdaPIRMRate=THsmdaPIRMRate, THsmdaPIRMRateOverride=THsmdaPIRMRateOverride, THsmdaPolicyIncludeQueues=THsmdaPolicyIncludeQueues, THsmdaPolicyScheduleClass=THsmdaPolicyScheduleClass, THsmdaSchedulerPolicyGroupId=THsmdaSchedulerPolicyGroupId, THsmdaWeight=THsmdaWeight, THsmdaWeightClass=THsmdaWeightClass, THsmdaWeightOverride=THsmdaWeightOverride, THsmdaWrrWeight=THsmdaWrrWeight, THsmdaWrrWeightOverride=THsmdaWrrWeightOverride, TIPFilterID=TIPFilterID, TIPFilterType=TIPFilterType, TIcmpCodeOrNone=TIcmpCodeOrNone, TIcmpTypeOrNone=TIcmpTypeOrNone, TIngClassRemarkType=TIngClassRemarkType, TIngDynPolicerIdOrNone=TIngDynPolicerIdOrNone, TIngHsmdaPerPacketOffsetOvr=TIngHsmdaPerPacketOffsetOvr, TIngPolicerId=TIngPolicerId, TIngPolicerIdOrNone=TIngPolicerIdOrNone, TIngressHsmdaCounterId=TIngressHsmdaCounterId, TIngressHsmdaCounterIdOrZero=TIngressHsmdaCounterIdOrZero, TIngressHsmdaPerPacketOffset=TIngressHsmdaPerPacketOffset, TIngressHsmdaQueueId=TIngressHsmdaQueueId, TIngressPolicerId=TIngressPolicerId, TIngressPolicerIdOrNone=TIngressPolicerIdOrNone, TIngressQPerPacketOffset=TIngressQPerPacketOffset, TIngressQueueId=TIngressQueueId, TIpOption=TIpOption, TIpProtocol=TIpProtocol, TIpProtocolNumber=TIpProtocolNumber, TItemDescription=TItemDescription, TItemLongDescription=TItemLongDescription, TItemMatch=TItemMatch, TItemScope=TItemScope, TLDisplayString=TLDisplayString, TLNamedItem=TLNamedItem, TLNamedItemOrEmpty=TLNamedItemOrEmpty, TLPolicyNameOrExpOrEmpty=TLPolicyNameOrExpOrEmpty, TLPolicyStatementNameOrEmpty=TLPolicyStatementNameOrEmpty, TLevel=TLevel, TLevelOrDefault=TLevelOrDefault, TLspExpValue=TLspExpValue, TMacFilterType=TMacFilterType, TMatchCriteria=TMatchCriteria, TMaxDecRate=TMaxDecRate, TMcFrQoSProfileId=TMcFrQoSProfileId, TMlpppQoSProfileId=TMlpppQoSProfileId, TNamedItem=TNamedItem, TNamedItemOrEmpty=TNamedItemOrEmpty, TNetIngPlcrBurstSizeBytes=TNetIngPlcrBurstSizeBytes, TNetIngPolicerId=TNetIngPolicerId, TNetIngPolicerIdOrNone=TNetIngPolicerIdOrNone, TNetworkPolicyID=TNetworkPolicyID, TNonZeroWeight=TNonZeroWeight, TOperator=TOperator, TPIRAggRateLimitOverride=TPIRAggRateLimitOverride, TPIRPercentOverride=TPIRPercentOverride, TPIRRate=TPIRRate, TPIRRateOrZero=TPIRRateOrZero, TPIRRateOverride=TPIRRateOverride, TPIRRatePercent=TPIRRatePercent, TPSPRateType=TPSPRateType, TPerPacketOffset=TPerPacketOffset, TPerPacketOffsetOvr=TPerPacketOffsetOvr, TPlcrBurstSizeBytes=TPlcrBurstSizeBytes, TPlcrBurstSizeBytesOverride=TPlcrBurstSizeBytesOverride, TPolRateTypeRefOrLocalLimit=TPolRateTypeRefOrLocalLimit, TPolicerRateType=TPolicerRateType, TPolicerRateTypeWithRefLimit=TPolicerRateTypeWithRefLimit, TPolicerWeight=TPolicerWeight, TPolicyID=TPolicyID, TPolicyStatementName=TPolicyStatementName, TPolicyStatementNameOrEmpty=TPolicyStatementNameOrEmpty, TPortQosCIRRate=TPortQosCIRRate, TPortQosPIRRate=TPortQosPIRRate, TPortSchedLevel=TPortSchedLevel, TPortSchedulerAggRateLimitPIR=TPortSchedulerAggRateLimitPIR, TPortSchedulerCIR=TPortSchedulerCIR, TPortSchedulerPIR=TPortSchedulerPIR, TPortSchedulerPIRRate=TPortSchedulerPIRRate, TPrecValue=TPrecValue, TPrecValueOrNone=TPrecValueOrNone, TPriority=TPriority, TPriorityOrDefault=TPriorityOrDefault, TPriorityOrUndefined=TPriorityOrUndefined, TProfile=TProfile, TProfileOrNone=TProfileOrNone, TQGroupType=TQGroupType, TQosIngressPolicyID=TQosIngressPolicyID, TQosOverrideType=TQosOverrideType, TQosOverrideTypeId=TQosOverrideTypeId, TQosQGrpInstanceIDorZero=TQosQGrpInstanceIDorZero, TQosQueueCIRRate=TQosQueueCIRRate, TQosQueueCIRRateOverride=TQosQueueCIRRateOverride, TQosQueuePIRRate=TQosQueuePIRRate, TQosQueuePIRRateOverride=TQosQueuePIRRateOverride, TQueueId=TQueueId, TQueueIdOrAll=TQueueIdOrAll, TQueueMode=TQueueMode, TQueueStatModeFormat=TQueueStatModeFormat, TRatePercent=TRatePercent, TRateType=TRateType, TRegularExpression=TRegularExpression, TRemarkType=TRemarkType, TResolveStatus=TResolveStatus, TSapEgrEncapGroupActionType=TSapEgrEncapGroupActionType, TSapEgrEncapGroupType=TSapEgrEncapGroupType, TSapEgrEncapGrpQosPolicyIdOrZero=TSapEgrEncapGrpQosPolicyIdOrZero, TSapEgressPolicyID=TSapEgressPolicyID, TSapIngressPolicyID=TSapIngressPolicyID, TSdpEgressPolicyID=TSdpEgressPolicyID, TSdpIngressPolicyID=TSdpIngressPolicyID, TSecondaryShaper10GPIRRate=TSecondaryShaper10GPIRRate, TSiteOperStatus=TSiteOperStatus, TSubHostId=TSubHostId, TTcpUdpPort=TTcpUdpPort, TTcpUdpPortOperator=TTcpUdpPortOperator, TTmplPolicyID=TTmplPolicyID, TWeight=TWeight, TWeightOverride=TWeightOverride, TWredSlopeProfile=TWredSlopeProfile, TXLNamedItem=TXLNamedItem, TXLNamedItemOrEmpty=TXLNamedItemOrEmpty, TXLPolicyNameOrExpOrEmpty=TXLPolicyNameOrExpOrEmpty, TmnxAccPlcyAACounters=TmnxAccPlcyAACounters, TmnxAccPlcyAASubAttributes=TmnxAccPlcyAASubAttributes, TmnxAccPlcyOECounters=TmnxAccPlcyOECounters, TmnxAccPlcyOICounters=TmnxAccPlcyOICounters, TmnxAccPlcyPolicerECounters=TmnxAccPlcyPolicerECounters, TmnxAccPlcyPolicerICounters=TmnxAccPlcyPolicerICounters, TmnxAccPlcyQECounters=TmnxAccPlcyQECounters, TmnxAccPlcyQICounters=TmnxAccPlcyQICounters, TmnxAccessLoopEncapDataLink=TmnxAccessLoopEncapDataLink, TmnxAccessLoopEncaps1=TmnxAccessLoopEncaps1, TmnxAccessLoopEncaps2=TmnxAccessLoopEncaps2, TmnxActionType=TmnxActionType)
mibBuilder.exportSymbols("TIMETRA-TC-MIB", TmnxAddressAndMaskOrPrefixAddress=TmnxAddressAndMaskOrPrefixAddress, TmnxAddressAndMaskOrPrefixMask=TmnxAddressAndMaskOrPrefixMask, TmnxAddressAndMaskOrPrefixPrefix=TmnxAddressAndMaskOrPrefixPrefix, TmnxAddressAndMaskOrPrefixType=TmnxAddressAndMaskOrPrefixType, TmnxAddressAndPrefixAddress=TmnxAddressAndPrefixAddress, TmnxAddressAndPrefixPrefix=TmnxAddressAndPrefixPrefix, TmnxAddressAndPrefixType=TmnxAddressAndPrefixType, TmnxAddressWithZoneAddress=TmnxAddressWithZoneAddress, TmnxAddressWithZoneType=TmnxAddressWithZoneType, TmnxAdjacencySetFamilyType=TmnxAdjacencySetFamilyType, TmnxAdminState=TmnxAdminState, TmnxAdminStateTruthValue=TmnxAdminStateTruthValue, TmnxAdminStateUpDown=TmnxAdminStateUpDown, TmnxAiiType=TmnxAiiType, TmnxAncpString=TmnxAncpString, TmnxAncpStringOrZero=TmnxAncpStringOrZero, TmnxAppProfileString=TmnxAppProfileString, TmnxAppProfileStringOrEmpty=TmnxAppProfileStringOrEmpty, TmnxAsciiSpecification=TmnxAsciiSpecification, TmnxAuthPassword=TmnxAuthPassword, TmnxBGPFamilyType=TmnxBGPFamilyType, TmnxBfdEncap=TmnxBfdEncap, TmnxBfdIntfSessOperState=TmnxBfdIntfSessOperState, TmnxBfdOnLspSessFecType=TmnxBfdOnLspSessFecType, TmnxBfdSessOperState=TmnxBfdSessOperState, TmnxBfdSessionProtocols=TmnxBfdSessionProtocols, TmnxBgpAutonomousSystem=TmnxBgpAutonomousSystem, TmnxBgpEvpnAcEthTag=TmnxBgpEvpnAcEthTag, TmnxBgpLocalPreference=TmnxBgpLocalPreference, TmnxBgpPreference=TmnxBgpPreference, TmnxBgpRouteTarget=TmnxBgpRouteTarget, TmnxBinarySpecification=TmnxBinarySpecification, TmnxBsxAaGrpPartIndexOrZero=TmnxBsxAaGrpPartIndexOrZero, TmnxBsxAarpId=TmnxBsxAarpId, TmnxBsxAarpIdOrZero=TmnxBsxAarpIdOrZero, TmnxBsxAarpServiceRefType=TmnxBsxAarpServiceRefType, TmnxBsxIsaAaGroupIndexOrZero=TmnxBsxIsaAaGroupIndexOrZero, TmnxBsxTransPrefPolicyId=TmnxBsxTransPrefPolicyId, TmnxBsxTransPrefPolicyIdOrZero=TmnxBsxTransPrefPolicyIdOrZero, TmnxBsxTransitIpPolicyId=TmnxBsxTransitIpPolicyId, TmnxBsxTransitIpPolicyIdOrZero=TmnxBsxTransitIpPolicyIdOrZero, TmnxCBFClasses=TmnxCBFClasses, TmnxCdrDiagnosticAction=TmnxCdrDiagnosticAction, TmnxCdrType=TmnxCdrType, TmnxCliEngine=TmnxCliEngine, TmnxCreateOrigin=TmnxCreateOrigin, TmnxCustId=TmnxCustId, TmnxCustIdNoZero=TmnxCustIdNoZero, TmnxDHCP6MsgType=TmnxDHCP6MsgType, TmnxDataFormat=TmnxDataFormat, TmnxDayOfWeek=TmnxDayOfWeek, TmnxDayOfWeekList=TmnxDayOfWeekList, TmnxDefInterDestIdSource=TmnxDefInterDestIdSource, TmnxDefSubIdSource=TmnxDefSubIdSource, TmnxDhcpClientState=TmnxDhcpClientState, TmnxDhcpOptionDisplay=TmnxDhcpOptionDisplay, TmnxDhcpOptionType=TmnxDhcpOptionType, TmnxDhcpServerDUIDTypeCode=TmnxDhcpServerDUIDTypeCode, TmnxDiamCcFailureHndlng=TmnxDiamCcFailureHndlng, TmnxDisplayStringURL=TmnxDisplayStringURL, TmnxDistCpuProtAction=TmnxDistCpuProtAction, TmnxDistCpuProtActionDuration=TmnxDistCpuProtActionDuration, TmnxDistCpuProtBurstSize=TmnxDistCpuProtBurstSize, TmnxDistCpuProtEnforceType=TmnxDistCpuProtEnforceType, TmnxDistCpuProtLogEventType=TmnxDistCpuProtLogEventType, TmnxDistCpuProtPacketRateLimit=TmnxDistCpuProtPacketRateLimit, TmnxDistCpuProtProtocolId=TmnxDistCpuProtProtocolId, TmnxDistCpuProtRate=TmnxDistCpuProtRate, TmnxDistCpuProtRateType=TmnxDistCpuProtRateType, TmnxDistCpuProtState=TmnxDistCpuProtState, TmnxEgrPolicerStatMode=TmnxEgrPolicerStatMode, TmnxEgrPolicerStatModeOverride=TmnxEgrPolicerStatModeOverride, TmnxEnabledDisabled=TmnxEnabledDisabled, TmnxEnabledDisabledAdminState=TmnxEnabledDisabledAdminState, TmnxEnabledDisabledOrInherit=TmnxEnabledDisabledOrInherit, TmnxEnabledDisabledOrNA=TmnxEnabledDisabledOrNA, TmnxEncapVal=TmnxEncapVal, TmnxEsaNum=TmnxEsaNum, TmnxEsaVappNum=TmnxEsaVappNum, TmnxEvpnMHEthSegStatus=TmnxEvpnMHEthSegStatus, TmnxEvpnMultiHomingState=TmnxEvpnMultiHomingState, TmnxExtServId=TmnxExtServId, TmnxFPNumber=TmnxFPNumber, TmnxFPNumberOrZero=TmnxFPNumberOrZero, TmnxFilterProfileStringOrEmpty=TmnxFilterProfileStringOrEmpty, TmnxFlexAlgoId=TmnxFlexAlgoId, TmnxFpeId=TmnxFpeId, TmnxFpeIdOrZero=TmnxFpeIdOrZero, TmnxHigh32=TmnxHigh32, TmnxHttpRedirectUrl=TmnxHttpRedirectUrl, TmnxIPsecTunnelTemplateId=TmnxIPsecTunnelTemplateId, TmnxIPsecTunnelTemplateIdOrZero=TmnxIPsecTunnelTemplateIdOrZero, TmnxISID=TmnxISID, TmnxISIDNoZero=TmnxISIDNoZero, TmnxIgmpGroupFilterMode=TmnxIgmpGroupFilterMode, TmnxIgmpGroupType=TmnxIgmpGroupType, TmnxIgmpSnpgGroupType=TmnxIgmpSnpgGroupType, TmnxIgmpVersion=TmnxIgmpVersion, TmnxIgpInstance=TmnxIgpInstance, TmnxIgpSCFamilyType=TmnxIgpSCFamilyType, TmnxIkePolicyAuthMethod=TmnxIkePolicyAuthMethod, TmnxIkePolicyAutoEapMethod=TmnxIkePolicyAutoEapMethod, TmnxIkePolicyAutoEapOwnMethod=TmnxIkePolicyAutoEapOwnMethod, TmnxIkePolicyOwnAuthMethod=TmnxIkePolicyOwnAuthMethod, TmnxIngPolicerStatMode=TmnxIngPolicerStatMode, TmnxIngPolicerStatModeOverride=TmnxIngPolicerStatModeOverride, TmnxInternalSchedWeightMode=TmnxInternalSchedWeightMode, TmnxIpSecIsaOperFlags=TmnxIpSecIsaOperFlags, TmnxIpv4AddressAndMaskOrPrefixAddress=TmnxIpv4AddressAndMaskOrPrefixAddress, TmnxIpv4AddressAndMaskOrPrefixMask=TmnxIpv4AddressAndMaskOrPrefixMask, TmnxIpv4AddressAndMaskOrPrefixPrefix=TmnxIpv4AddressAndMaskOrPrefixPrefix, TmnxIpv4AddressAndPrefixAddress=TmnxIpv4AddressAndPrefixAddress, TmnxIpv4AddressAndPrefixPrefix=TmnxIpv4AddressAndPrefixPrefix, TmnxIpv6AddressAndMaskOrPrefixAddress=TmnxIpv6AddressAndMaskOrPrefixAddress, TmnxIpv6AddressAndMaskOrPrefixMask=TmnxIpv6AddressAndMaskOrPrefixMask, TmnxIpv6AddressAndMaskOrPrefixPrefix=TmnxIpv6AddressAndMaskOrPrefixPrefix, TmnxIpv6AddressAndPrefixAddress=TmnxIpv6AddressAndPrefixAddress, TmnxIpv6AddressAndPrefixPrefix=TmnxIpv6AddressAndPrefixPrefix, TmnxIsaBbGrpId=TmnxIsaBbGrpId, TmnxIsaScalingProfile=TmnxIsaScalingProfile, TmnxIsidMFibStatus=TmnxIsidMFibStatus, TmnxL2tpTunnelGroupName=TmnxL2tpTunnelGroupName, TmnxL2tpTunnelGroupNameOrEmpty=TmnxL2tpTunnelGroupNameOrEmpty, TmnxLagPerLinkHashClass=TmnxLagPerLinkHashClass, TmnxLagPerLinkHashClassOrNone=TmnxLagPerLinkHashClassOrNone, TmnxLagPerLinkHashWeight=TmnxLagPerLinkHashWeight, TmnxLdpFECType=TmnxLdpFECType, TmnxLinkMapProfileId=TmnxLinkMapProfileId, TmnxLinkMapProfileIdOrZero=TmnxLinkMapProfileIdOrZero, TmnxLongDisplayString=TmnxLongDisplayString, TmnxLongDisplayStringLegacyBinary=TmnxLongDisplayStringLegacyBinary, TmnxLongDisplayStringToBinary=TmnxLongDisplayStringToBinary, TmnxLow32=TmnxLow32, TmnxMacSpecification=TmnxMacSpecification, TmnxManagedRouteStatus=TmnxManagedRouteStatus, TmnxMdaQos=TmnxMdaQos, TmnxMldGroupFilterMode=TmnxMldGroupFilterMode, TmnxMldGroupType=TmnxMldGroupType, TmnxMldVersion=TmnxMldVersion, TmnxMlpppEpClass=TmnxMlpppEpClass, TmnxMplsLabel=TmnxMplsLabel, TmnxMplsLabelOrZero=TmnxMplsLabelOrZero, TmnxMplsLdpNgIdType=TmnxMplsLdpNgIdType, TmnxMplsLdpNgIdentifier=TmnxMplsLdpNgIdentifier, TmnxMplsLspBandwidth=TmnxMplsLspBandwidth, TmnxMplsLsrNgIdentifier=TmnxMplsLsrNgIdentifier, TmnxMplsTpGlobalID=TmnxMplsTpGlobalID, TmnxMplsTpNodeID=TmnxMplsTpNodeID, TmnxMplsTpTunnelType=TmnxMplsTpTunnelType, TmnxMsPwPeSignaling=TmnxMsPwPeSignaling, TmnxMulticastAddrFamily=TmnxMulticastAddrFamily, TmnxNatIsaGrpId=TmnxNatIsaGrpId, TmnxNatIsaGrpIdOrZero=TmnxNatIsaGrpIdOrZero, TmnxNatL2AwAccessMode=TmnxNatL2AwAccessMode, TmnxNatSubscriberType=TmnxNatSubscriberType, TmnxNatSubscriberTypeOrNone=TmnxNatSubscriberTypeOrNone, TmnxNatWaterMark=TmnxNatWaterMark, TmnxNetIngPlcyPolicerStatMode=TmnxNetIngPlcyPolicerStatMode, TmnxNhgDownReason=TmnxNhgDownReason, TmnxOperGrpHoldDownTime=TmnxOperGrpHoldDownTime, TmnxOperGrpHoldUpTime=TmnxOperGrpHoldUpTime, TmnxOperState=TmnxOperState, TmnxOspfInstance=TmnxOspfInstance, TmnxPccRuleFilterForwardAction=TmnxPccRuleFilterForwardAction, TmnxPccRuleQosForwardAction=TmnxPccRuleQosForwardAction, TmnxPortID=TmnxPortID, TmnxPppCpState=TmnxPppCpState, TmnxPppNcpProtocol=TmnxPppNcpProtocol, TmnxPppoePadoDelay=TmnxPppoePadoDelay, TmnxPppoeSessionId=TmnxPppoeSessionId, TmnxPppoeSessionInfoOrigin=TmnxPppoeSessionInfoOrigin, TmnxPppoeSessionType=TmnxPppoeSessionType, TmnxPppoeUserName=TmnxPppoeUserName, TmnxPppoeUserNameOrEmpty=TmnxPppoeUserNameOrEmpty, TmnxProxyEntryType=TmnxProxyEntryType, TmnxPwGlobalId=TmnxPwGlobalId, TmnxPwGlobalIdOrZero=TmnxPwGlobalIdOrZero, TmnxPwPathHopId=TmnxPwPathHopId, TmnxPwPathHopIdOrZero=TmnxPwPathHopIdOrZero, TmnxQosBytesHex=TmnxQosBytesHex, TmnxQosMdAutoIDCount=TmnxQosMdAutoIDCount, TmnxQosMdAutoPolicyID=TmnxQosMdAutoPolicyID, TmnxQosRateHigh32=TmnxQosRateHigh32, TmnxQosRateLow32=TmnxQosRateLow32, TmnxRadiusFramedRouteMetric=TmnxRadiusFramedRouteMetric, TmnxRadiusFramedRoutePreference=TmnxRadiusFramedRoutePreference, TmnxRadiusFramedRouteTag=TmnxRadiusFramedRouteTag, TmnxRadiusPendingReqLimit=TmnxRadiusPendingReqLimit, TmnxRadiusServerOperState=TmnxRadiusServerOperState, TmnxReasContextVal=TmnxReasContextVal, TmnxReferenceBandwidth=TmnxReferenceBandwidth, TmnxRipListenerStatus=TmnxRipListenerStatus, TmnxRipNgAuthKey=TmnxRipNgAuthKey, TmnxRipNgAuthType=TmnxRipNgAuthType, TmnxRouteDistType=TmnxRouteDistType, TmnxRouteTargetOrigin=TmnxRouteTargetOrigin, TmnxRsvpDSTEClassType=TmnxRsvpDSTEClassType, TmnxRsvpSessionNameString=TmnxRsvpSessionNameString, TmnxSapAASubScope=TmnxSapAASubScope, TmnxSapIngPolicerStatMode=TmnxSapIngPolicerStatMode, TmnxScriptAuthType=TmnxScriptAuthType, TmnxSecRadiusServAlgorithm=TmnxSecRadiusServAlgorithm, TmnxServId=TmnxServId, TmnxSlaProfileString=TmnxSlaProfileString, TmnxSlaProfileStringOrEmpty=TmnxSlaProfileStringOrEmpty, TmnxSlopeMap=TmnxSlopeMap, TmnxSpbBridgePriority=TmnxSpbBridgePriority, TmnxSpbFdbLocale=TmnxSpbFdbLocale, TmnxSpbFdbState=TmnxSpbFdbState, TmnxSpbFid=TmnxSpbFid, TmnxSpbFidOrZero=TmnxSpbFidOrZero, TmnxSpokeSdpId=TmnxSpokeSdpId, TmnxSpokeSdpIdOrZero=TmnxSpokeSdpIdOrZero, TmnxSrrpPriorityStep=TmnxSrrpPriorityStep, TmnxStatus=TmnxStatus, TmnxStrSapId=TmnxStrSapId, TmnxSubAcctSessionId=TmnxSubAcctSessionId, TmnxSubAleOffset=TmnxSubAleOffset, TmnxSubAleOffsetMode=TmnxSubAleOffsetMode, TmnxSubAuthPlcyUserNameOp=TmnxSubAuthPlcyUserNameOp, TmnxSubBondingConnIdOrEmpty=TmnxSubBondingConnIdOrEmpty, TmnxSubCallingStationIdType=TmnxSubCallingStationIdType, TmnxSubCreditVolumeUnit=TmnxSubCreditVolumeUnit, TmnxSubHostGrouping=TmnxSubHostGrouping, TmnxSubIdentShortString=TmnxSubIdentShortString, TmnxSubIdentString=TmnxSubIdentString, TmnxSubIdentStringOrEmpty=TmnxSubIdentStringOrEmpty, TmnxSubMgtIntDestId=TmnxSubMgtIntDestId, TmnxSubMgtIntDestIdOrEmpty=TmnxSubMgtIntDestIdOrEmpty, TmnxSubMgtOrgStrOrZero=TmnxSubMgtOrgStrOrZero, TmnxSubMgtOrgString=TmnxSubMgtOrgString, TmnxSubNasPortPrefixType=TmnxSubNasPortPrefixType, TmnxSubNasPortSuffixType=TmnxSubNasPortSuffixType, TmnxSubNasPortTypeType=TmnxSubNasPortTypeType, TmnxSubOperSpiGroupId=TmnxSubOperSpiGroupId, TmnxSubPoolName=TmnxSubPoolName, TmnxSubProfileString=TmnxSubProfileString, TmnxSubProfileStringOrEmpty=TmnxSubProfileStringOrEmpty, TmnxSubRadIsaServAlgorithm=TmnxSubRadIsaServAlgorithm, TmnxSubRadServAlgorithm=TmnxSubRadServAlgorithm, TmnxSubRadiusAttrType=TmnxSubRadiusAttrType, TmnxSubRadiusDisplayString=TmnxSubRadiusDisplayString, TmnxSubRadiusOctetString=TmnxSubRadiusOctetString, TmnxSubRadiusVendorId=TmnxSubRadiusVendorId, TmnxSubShcvAction=TmnxSubShcvAction, TmnxSubShcvInterval=TmnxSubShcvInterval, TmnxSubShcvRetryCount=TmnxSubShcvRetryCount, TmnxSubShcvRetryTimeout=TmnxSubShcvRetryTimeout, TmnxSubShcvSrcIpOrigin=TmnxSubShcvSrcIpOrigin, TmnxSubSlaMode=TmnxSubSlaMode, TmnxSubSpiGroupId=TmnxSubSpiGroupId, TmnxSubTerminationType=TmnxSubTerminationType, TmnxSubTerminationTypeOrZero=TmnxSubTerminationTypeOrZero, TmnxSvcEvi=TmnxSvcEvi)
mibBuilder.exportSymbols("TIMETRA-TC-MIB", TmnxSvcEviOrZero=TmnxSvcEviOrZero, TmnxSvcEvpnMplsTransportType=TmnxSvcEvpnMplsTransportType, TmnxSvcOperGrpCreationOrigin=TmnxSvcOperGrpCreationOrigin, TmnxSyslogFacility=TmnxSyslogFacility, TmnxSyslogSeverity=TmnxSyslogSeverity, TmnxThresholdGroupType=TmnxThresholdGroupType, TmnxTimeInSec=TmnxTimeInSec, TmnxTimeInterval=TmnxTimeInterval, TmnxTlsGroupId=TmnxTlsGroupId, TmnxTreeSidOrigin=TmnxTreeSidOrigin, TmnxTreeSidOwner=TmnxTreeSidOwner, TmnxTunnelGroupId=TmnxTunnelGroupId, TmnxTunnelGroupIdOrZero=TmnxTunnelGroupIdOrZero, TmnxTunnelID=TmnxTunnelID, TmnxTunnelType=TmnxTunnelType, TmnxTunnelTypeExt=TmnxTunnelTypeExt, TmnxUdpPort=TmnxUdpPort, TmnxUrpfCheckMode=TmnxUrpfCheckMode, TmnxUserPassword=TmnxUserPassword, TmnxUuid=TmnxUuid, TmnxVPNRouteDistinguisher=TmnxVPNRouteDistinguisher, TmnxVRtrID=TmnxVRtrID, TmnxVRtrIDOrZero=TmnxVRtrIDOrZero, TmnxVRtrMplsLspID=TmnxVRtrMplsLspID, TmnxVRtrMplsLspIDNoZero=TmnxVRtrMplsLspIDNoZero, TmnxVcId=TmnxVcId, TmnxVcIdOrNone=TmnxVcIdOrNone, TmnxVcType=TmnxVcType, TmnxVdoAnalyzerAlarm=TmnxVdoAnalyzerAlarm, TmnxVdoAnalyzerAlarmStates=TmnxVdoAnalyzerAlarmStates, TmnxVdoFccServerMode=TmnxVdoFccServerMode, TmnxVdoGrpId=TmnxVdoGrpId, TmnxVdoGrpIdIndex=TmnxVdoGrpIdIndex, TmnxVdoGrpIdOrInherit=TmnxVdoGrpIdOrInherit, TmnxVdoIfName=TmnxVdoIfName, TmnxVdoOutputFormat=TmnxVdoOutputFormat, TmnxVdoPortNumber=TmnxVdoPortNumber, TmnxVdoStatInt=TmnxVdoStatInt, TmnxVni=TmnxVni, TmnxVniOrZero=TmnxVniOrZero, TmnxVpnIpBackupFamily=TmnxVpnIpBackupFamily, TmnxVxlanInstance=TmnxVxlanInstance, TmnxWaveKey=TmnxWaveKey, TmnxWlanGwIsaGrpId=TmnxWlanGwIsaGrpId, TmnxWlanGwIsaGrpIdOrZero=TmnxWlanGwIsaGrpIdOrZero, TruthValueNoTypeTranslator=TruthValueNoTypeTranslator, VRtrIgmpHostMcRDstStatType=VRtrIgmpHostMcRDstStatType, timetraTCMIBModule=timetraTCMIBModule)
