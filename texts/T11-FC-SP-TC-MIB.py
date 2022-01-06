#
# PySNMP MIB module T11-FC-SP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/T11-FC-SP-TC-MIB
# Produced by pysmi-1.1.8 at Thu Jan  6 19:59:57 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, ModuleIdentity, Bits, Counter64, Gauge32, IpAddress, mib_2, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "ModuleIdentity", "Bits", "Counter64", "Gauge32", "IpAddress", "mib-2", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
t11FcTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 175))
t11FcTcMIB.setRevisions(('2008-08-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: t11FcTcMIB.setRevisionsDescriptions(('Initial version of this MIB module, published as RFC 5324.',))
if mibBuilder.loadTexts: t11FcTcMIB.setLastUpdated('200808200000Z')
if mibBuilder.loadTexts: t11FcTcMIB.setOrganization('This MIB module was developed through the\n                  coordinated effort of two organizations:\n                  T11 began the development and the IETF (in\n                  the IMSS Working Group) finished it.')
if mibBuilder.loadTexts: t11FcTcMIB.setContactInfo('     Claudio DeSanti\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA 95134 USA\n                  EMail: cds@cisco.com\n\n                  Keith McCloghrie\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA 95134 USA\n                  Email: kzm@cisco.com')
if mibBuilder.loadTexts: t11FcTcMIB.setDescription('This MIB module defines Textual Conventions for use in\n           the multiple MIB modules, which together define the\n           instrumentation for an implementation of the Fibre Channel\n           Security Protocols (FC-SP) specification.\n\n           This MIB module also defines Object Identities (for use as\n           possible values of MIB objects with syntax AutonomousType),\n           including OIDs for the Cryptographic Algorithms defined\n           in FC-SP.\n\n           Copyright (C) The IETF Trust (2008).  This version\n           of this MIB module is part of RFC 5324;  see the RFC\n           itself for full legal notices.')
t11FcSpIdentities = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1))
t11FcSpAlgorithms = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1, 1))
class T11FcSpPolicyHashFormat(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, section 7.1.3.1 and table 106.\n            - FIPS PUB 180-2.'
    description = "Identifies a cryptographic hash function used to create\n           a hash value that summarizes an FC-SP Policy Object.\n\n           Each definition of an object with this TC as its syntax\n           must be accompanied by a corresponding definition of an\n           object with T11FcSpPolicyHashValue as its syntax, and\n           containing the hash value.\n\n           The first two cryptographic hash functions are:\n\n                Hash Type    Hash Tag     Hash Length (Bytes)\n                  SHA-1     '00000001'h        20\n                 SHA-256    '00000002'h        32\n           "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class T11FcSpPolicyHashValue(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, section 7.1.3.1 and table 106.'
    description = 'Represents the value of the cryptographic hash function\n           of an FC-SP Policy Object.\n\n           Each definition of an object with this TC as its syntax\n           must be accompanied by a corresponding definition of an\n           object with T11FcSpPolicyHashFormat as its syntax.\n           The corresponding object identifies the cryptographic\n           hash function used to create the hash value.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class T11FcSpHashCalculationStatus(TextualConvention, Integer32):
    description = "When some kind of 'database' is defined in a set of\n           read-write MIB objects, it is common that multiple changes\n           in the data need to be made at the same time.  So, if hash\n           values are maintained for that data, those hash values are\n           only correct if and when they are re-calculated after every\n           change.  In such circumstances, the use of an object with\n           this syntax allows the re-calculation of the hash values to\n           be deferred until all changes have been made, and therefore\n           the calculation need only be done once after all changes,\n           rather than repeatedly/after each individual change.\n\n           The definition of an object defined using this TC is\n           required to specify which one or more instances of which\n           MIB objects contain the hash values operated upon (or\n           whose status is given) by the value of this TC.\n\n           When read, the value of an object with this syntax is\n           either:\n\n             correct -- the identified MIB object instance(s)\n                        contain the correct hash values; or\n             stale   -- the identified MIB object instance(s)\n                        contain stale (possibly incorrect) values.\n\n           Writing a value of 'calculate' is a request to re-calculate\n           and update the values of the corresponding instances of the\n           identified MIB objects.  Writing a value of 'correct' or\n           'stale' to this object is an error (e.g., 'wrongValue')."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("calculate", 1), ("correct", 2), ("stale", 3))

class T11FcSpAuthRejectReasonCode(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 17, 48, 52.'
    description = 'A reason code contained in an AUTH_Reject message, or\n           in an SW_RJT (rejecting an AUTH_ILS), or in an LS_RJT\n           (rejecting an AUTH-ELS).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("authFailure", 1), ("logicalError", 2), ("logicalBusy", 3), ("authILSNotSupported", 4), ("authELSNotSupported", 5), ("notLoggedIn", 6))

class T11FcSpAuthRejReasonCodeExp(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Tables 18, 48, 52.'
    description = 'A reason code explanation contained in an AUTH_Reject\n           message, or in an SW_RJT (rejecting an AUTH_ILS), or in\n           an LS_RJT (rejecting an AUTH-ELS).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("authMechanismNotUsable", 1), ("dhGroupNotUsable", 2), ("hashFunctionNotUsable", 3), ("authTransactionAlreadyStarted", 4), ("authenticationFailed", 5), ("incorrectPayload", 6), ("incorrectAuthProtocolMessage", 7), ("restartAuthProtocol", 8), ("authConcatNotSupported", 9), ("unsupportedProtocolVersion", 10), ("logicalBusy", 11), ("authILSNotSupported", 12), ("authELSNotSupported", 13), ("notLoggedIn", 14))

class T11FcSpHashFunctions(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 14.'
    description = 'A set of zero, one, or more hash functions defined for\n           use in FC-SP.'
    status = 'current'
    namedValues = NamedValues(("md5", 0), ("sha1", 1))

class T11FcSpSignFunctions(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, tables 38 & 39.'
    description = 'A set of zero, one, or more signature functions defined\n           for signing certificates for use with FCAP in FC-SP.'
    status = 'current'
    namedValues = NamedValues(("rsaSha1", 0))

class T11FcSpDhGroups(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 15.'
    description = 'A set of zero, one, or more DH Groups defined for use\n           in FC-SP.'
    status = 'current'
    namedValues = NamedValues(("null", 0), ("group1024", 1), ("group1280", 2), ("group1536", 3), ("group2048", 4), ("group3072", 5), ("group4096", 6), ("group6144", 7), ("group8192", 8))

class T11FcSpPolicyObjectType(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 102.'
    description = 'A value that identifies the type of an FC-SP Policy\n           Object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("summary", 1), ("switchMemberList", 2), ("nodeMemberList", 3), ("switchConnectivity", 4), ("ipMgmtList", 5), ("attribute", 6))

class T11FcSpPolicyNameType(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 103.'
    description = "The format and usage of a companion object having\n           T11FcSpPolicyName as its syntax.\n\n           Six of the values indicate the same format, i.e., they\n           differ only in semantics.  That common format is a Fibre\n           Channel 'Name_Identifier', i.e., the same syntax as\n           'FcNameIdOrZero (SIZE(8))'.\n\n           These six are three pairs of one restricted and one\n           unrestricted.  Each usage of this syntax must specify\n           what the meaning of 'restricted' is for that usage and\n           how the characteristics and behavior of restricted\n           names differ from unrestricted names.\n\n           The six are:\n\n             'nodeName'           - a Node_Name, which is the\n                                    Name_Identifier associated\n                                    with a Fibre Channel Node.\n\n             'restrictedNodeName' - a Restricted Node_Name.\n\n             'portName'           - the Name_Identifier associated\n                                    with a Fibre Channel Port.\n\n             'restrictedPortName' - a Restricted Port_Name.\n\n             'wildcard'           - a Wildcard value that is used to\n                                    identify 'all others' (typically,\n                                    all other members of a Policy\n                                    Object, not all other Policy\n                                    Objects).\n\n             'restrictedWildcard' - a Restricted Wildcard value.\n\n           Other possible values are:\n\n             'alphaNumericName'   - the value begins with an ASCII\n           letter (upper or lower case) followed by (0 ... 63)\n           characters from the set:  lower case letters, upper case\n           letters, digits, and the four symbols: dollar-sign ($),\n           dash (-), caret (^), and underscore (_).\n\n             'ipv6AddressRange'   - two IPv6 addresses in network\n           byte order, the numerically smallest first and the\n           numerically largest second; total length is 32 bytes.\n\n             'ipv4AddressRange'   - two IPv4 addresses in network\n           byte order, the numerically smallest first and the\n           numerically largest second; total length is 8 bytes."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("nodeName", 1), ("restrictedNodeName", 2), ("portName", 3), ("restrictedPortName", 4), ("wildcard", 5), ("restrictedWildcard", 6), ("alphaNumericName", 7), ("ipv6AddressRange", 8), ("ipv4AddressRange", 9))

class T11FcSpPolicyName(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 103.'
    description = "A syntax used, when defining Policy Objects, for the\n           name of something.\n\n           An object that uses this syntax always identifies a\n           companion object with syntax T11FcSpPolicyNameType\n           such that the companion object specifies the format\n           and usage of the object with this syntax.\n\n           When the companion object has the value 'wildcard' or\n           'restrictedWildcard', the value of the T11FcSpPolicyName\n           object is:  '0000000000000000'h."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class T11FcSpAlphaNumName(TextualConvention, OctetString):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 103.'
    description = "A syntax used when defining Policy Objects for the\n           name of something, where the name is always in the format\n           specified by:\n\n               T11FcSpPolicyNameType = 'alphaNumericName'\n           "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class T11FcSpAlphaNumNameOrAbsent(TextualConvention, OctetString):
    description = 'An extension of the T11FcSpAlphaNumName TC with\n           one additional possible value: the zero-length string\n           to indicate the absence of a name.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class T11FcSaDirection(TextualConvention, Integer32):
    description = 'The direction of frame transmission on a Security\n           Association.  Note that Security Associations are\n           unidirectional, but they always exist as part of an\n           SA pair of the same type in opposite directions.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ingress", 1), ("egress", 2))

class T11FcSpiIndex(TextualConvention, Unsigned32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, section 4.7.2 and 4.7.3.'
    description = 'An SPI (Security Parameter Index) value is carried in the\n           SPI field of a frame protected by the ESP_Header.  An SPI\n           is also carried in the SAID field of a Common Transport\n           Information Unit (CT_IU) protected by CT_Authentication.\n           An SPI value identifies the Security Association on which\n           the frame is being transmitted.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class T11FcSpPrecedence(TextualConvention, Unsigned32):
    description = 'The precedence of a Traffic Selector.  If a frame\n           matches with two or more Traffic Selectors, then the match\n           that takes precedence is the one with the Traffic Selector\n           having the numerically smallest precedence value.  Note that\n           precedence values are not necessarily contiguous.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class T11FcRoutingControl(TextualConvention, OctetString):
    reference = '- Fibre Channel - Framing and Signaling-2 (FC-FS-2),\n              ANSI INCITS 424-2007, Project T11/1619-D,\n              February 2007, section 9.3.\n            - Fibre Channel - Generic Services-5 (FC-GS-5),\n              ANSI INCITS 427-2006, sections 4.5.2.4.2, 4.5.2.4.3\n              and table 12.'
    description = "A value stored in the R_CTL (Routing Control) 8-bit field\n           of an FC-2 frame containing routing and information bits to\n           categorize the frame function.\n\n           For FC-2 frames, an R_CTL value typically distinguishes\n           between control versus data frames and/or solicited versus\n           unsolicited frames, and in combination with the TYPE field\n           (see T11FcSpType), identifies a particular link-layer\n           service/protocol using FC-2.\n\n           For CT_Authentication, the information field in the R_CTL\n           field contains '02'h for Request CT_IUs and '03'h for\n           Response CT_IUs.\n\n           The comparison of two values having this syntax is done\n           by treating each string as an 8-bit numeric value."
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class T11FcSpType(TextualConvention, OctetString):
    reference = '- Fibre Channel - Framing and Signaling-2 (FC-FS-2),\n              ANSI INCITS 424-2007, Project T11/1619-D,\n              February 2007, section 9.6.\n            - Fibre Channel - Generic Services-5 (FC-GS-5),\n              ANSI INCITS 427-2006, sections 4.3.2.4 and 4.3.2.5.'
    description = "A value, or combination of values, contained in a frame\n           header used in identifying the link layer service/protocol\n           of a frame.  The value is always two octets:\n\n             - for FC-2 frames, the first octet is zero and the second\n               octet contains the Data structure type (TYPE) value\n               defined by FC-FS-2.  The TYPE value is used in\n               combination with T11FcRoutingControl to identify a link\n\n               layer service/protocol.\n\n             - for Common Transport Information Units (CT_IUs), the\n               first octet contains a GS_Type value and the second\n               octet contains a GS_Subtype value, defined by FC-GS-5.\n\n           The comparison of two values having this syntax is done\n           by treating each string as the numeric value obtained by\n           numerically combining the individual octet's value as\n           follows:\n\n               (256 * 1st-octet) + 2nd-octet\n           "
    status = 'current'
    displayHint = '2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class T11FcSpTransforms(TextualConvention, Bits):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP), February 2007,\n              Appendix A.3.1, tables A.23, A.24, A.25, A.26.'
    description = 'A list of the standardized transforms that are defined\n           by FC-SP for use with ESP_Header, CT_Authentication, and/or\n           IKEv2 Support.'
    status = 'current'
    namedValues = NamedValues(("encrNull", 0), ("encrAesCbc", 1), ("encrAesCtr", 2), ("encrAesGcm", 3), ("encr3Des", 4), ("prfHmacMd5", 5), ("prfHmacSha1", 6), ("prfAesCbc", 7), ("authHmacMd5L96", 8), ("authHmacSha1L96", 9), ("authHmacMd5L128", 10), ("authHmacSha1L160", 11), ("encrNullAuthAesGmac", 12), ("dhGroups1024bit", 13), ("dhGroups2048bit", 14))

class T11FcSpSecurityProtocolId(TextualConvention, Integer32):
    reference = '- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, section 6.3.2.2 and table 67.'
    description = 'A Security Protocol identifier to identify\n           the protocol by which traffic is to be protected,\n           e.g., ESP_Header or CT_Authentication.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("espHeader", 1), ("ctAuth", 2))

class T11FcSpLifetimeLeft(TextualConvention, Unsigned32):
    description = 'This TC is used for one object of an associated pair\n           of objects.  The object with this syntax specifies a\n           remaining lifetime of something, e.g., of an SA, where\n           the lifetime is given in the units specified by the other\n           object of the pair which has T11FcSpLifetimeLeftUnits\n           as its syntax.'
    status = 'current'

class T11FcSpLifetimeLeftUnits(TextualConvention, Integer32):
    description = 'An object, defined using T11FcSpLifetimeLeft TC as\n           its syntax, is required to be one of an associated\n           pair of objects such that the other object of the pair\n           is defined with this T11FcSpLifetimeLeftUnits TC as\n           its syntax and with its value specifying the\n           units of the remaining lifetime given by the\n           value of the T11FcSpLifetimeLeft object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("seconds", 1), ("kiloBytes", 2), ("megaBytes", 3), ("gigaBytes", 4), ("teraBytes", 5), ("petaBytes", 6), ("exaBytes", 7), ("zettaBytes", 8), ("yottaBytes", 9))

t11FcSpEncryptAlgorithms = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1, 1, 1))
t11FcSpEncrNull = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 1))
if mibBuilder.loadTexts: t11FcSpEncrNull.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncrNull.setDescription('The ENCR_NULL algorithm.')
if mibBuilder.loadTexts: t11FcSpEncrNull.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 70.')
t11FcSpEncrAesCbc = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 2))
if mibBuilder.loadTexts: t11FcSpEncrAesCbc.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncrAesCbc.setDescription('The ENCR_AES_CBC algorithm.')
if mibBuilder.loadTexts: t11FcSpEncrAesCbc.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 70.')
t11FcSpEncrAesCtr = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 3))
if mibBuilder.loadTexts: t11FcSpEncrAesCtr.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncrAesCtr.setDescription('The ENCR_AES_CTR algorithm.')
if mibBuilder.loadTexts: t11FcSpEncrAesCtr.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 70.')
t11FcSpEncrAesGcm = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 4))
if mibBuilder.loadTexts: t11FcSpEncrAesGcm.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncrAesGcm.setDescription('The ENCR_AES_GCM algorithm.')
if mibBuilder.loadTexts: t11FcSpEncrAesGcm.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 70.')
t11FcSpEncr3Des = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 5))
if mibBuilder.loadTexts: t11FcSpEncr3Des.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncr3Des.setDescription('The ENCR_3DES algorithm.')
if mibBuilder.loadTexts: t11FcSpEncr3Des.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 70.')
t11FcSpAuthAlgorithms = MibIdentifier((1, 3, 6, 1, 2, 1, 175, 1, 1, 2))
t11FcSpAuthNull = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 1))
if mibBuilder.loadTexts: t11FcSpAuthNull.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuthNull.setDescription('The AUTH_NONE algorithm.')
if mibBuilder.loadTexts: t11FcSpAuthNull.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 72.')
t11FcSpAuthHmacMd5L96 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 2))
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L96.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L96.setDescription('The AUTH_HMAC_MD5_96 algorithm.')
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L96.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 72.')
t11FcSpAuthHmacSha1L96 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 3))
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L96.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L96.setDescription('The AUTH_HMAC_SHA1_96 algorithm.')
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L96.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 72.')
t11FcSpAuthHmacMd5L128 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 4))
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L128.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L128.setDescription('The AUTH_HMAC_MD5_128 algorithm.')
if mibBuilder.loadTexts: t11FcSpAuthHmacMd5L128.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 72.')
t11FcSpAuthHmacSha1L160 = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 5))
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L160.setStatus('current')
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L160.setDescription('The AUTH_HMAC_SHA1_160 algorithm.')
if mibBuilder.loadTexts: t11FcSpAuthHmacSha1L160.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 72.')
t11FcSpEncrNullAuthAesGmac = ObjectIdentity((1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 6))
if mibBuilder.loadTexts: t11FcSpEncrNullAuthAesGmac.setStatus('current')
if mibBuilder.loadTexts: t11FcSpEncrNullAuthAesGmac.setDescription('The ENCR_NULL_AUTH_AES_GMAC algorithm.')
if mibBuilder.loadTexts: t11FcSpEncrNullAuthAesGmac.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 70.')
mibBuilder.exportSymbols("T11-FC-SP-TC-MIB", T11FcSpPrecedence=T11FcSpPrecedence, t11FcSpAuthNull=t11FcSpAuthNull, t11FcSpEncrAesGcm=t11FcSpEncrAesGcm, T11FcSpPolicyNameType=T11FcSpPolicyNameType, t11FcSpEncrNull=t11FcSpEncrNull, T11FcSpAlphaNumNameOrAbsent=T11FcSpAlphaNumNameOrAbsent, t11FcSpIdentities=t11FcSpIdentities, t11FcSpEncrAesCtr=t11FcSpEncrAesCtr, T11FcSpLifetimeLeft=T11FcSpLifetimeLeft, t11FcSpAuthHmacMd5L96=t11FcSpAuthHmacMd5L96, T11FcSpHashCalculationStatus=T11FcSpHashCalculationStatus, T11FcSpAlphaNumName=T11FcSpAlphaNumName, T11FcSpPolicyName=T11FcSpPolicyName, t11FcSpEncryptAlgorithms=t11FcSpEncryptAlgorithms, T11FcSaDirection=T11FcSaDirection, T11FcSpTransforms=T11FcSpTransforms, T11FcSpLifetimeLeftUnits=T11FcSpLifetimeLeftUnits, PYSNMP_MODULE_ID=t11FcTcMIB, t11FcSpAuthAlgorithms=t11FcSpAuthAlgorithms, t11FcSpAuthHmacMd5L128=t11FcSpAuthHmacMd5L128, T11FcSpSecurityProtocolId=T11FcSpSecurityProtocolId, T11FcSpAuthRejectReasonCode=T11FcSpAuthRejectReasonCode, t11FcSpAuthHmacSha1L160=t11FcSpAuthHmacSha1L160, T11FcSpiIndex=T11FcSpiIndex, T11FcSpPolicyHashFormat=T11FcSpPolicyHashFormat, t11FcSpEncrAesCbc=t11FcSpEncrAesCbc, T11FcSpPolicyHashValue=T11FcSpPolicyHashValue, T11FcSpSignFunctions=T11FcSpSignFunctions, t11FcSpEncr3Des=t11FcSpEncr3Des, t11FcTcMIB=t11FcTcMIB, t11FcSpAlgorithms=t11FcSpAlgorithms, T11FcSpType=T11FcSpType, T11FcSpAuthRejReasonCodeExp=T11FcSpAuthRejReasonCodeExp, T11FcSpDhGroups=T11FcSpDhGroups, t11FcSpAuthHmacSha1L96=t11FcSpAuthHmacSha1L96, T11FcRoutingControl=T11FcRoutingControl, t11FcSpEncrNullAuthAesGmac=t11FcSpEncrNullAuthAesGmac, T11FcSpPolicyObjectType=T11FcSpPolicyObjectType, T11FcSpHashFunctions=T11FcSpHashFunctions)
