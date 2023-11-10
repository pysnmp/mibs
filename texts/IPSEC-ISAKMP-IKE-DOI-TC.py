#
# PySNMP MIB module IPSEC-ISAKMP-IKE-DOI-TC (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/IPSEC-ISAKMP-IKE-DOI-TC
# Produced by pysmi-1.1.10 at Fri Nov 10 08:52:32 2023
# On host fv-az447-590 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, Integer32, ModuleIdentity, iso, Bits, experimental, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, MibIdentifier, mib_2, IpAddress, NotificationType, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "iso", "Bits", "experimental", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "MibIdentifier", "mib-2", "IpAddress", "NotificationType", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
watchguard, = mibBuilder.importSymbols("WATCHGUARD-MIB", "watchguard")
ipsecIsakmpIkeDoiTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097, 100))
ipsecIsakmpIkeDoiTC.setRevisions(('1999-02-18 17:05', '1999-03-05 15:45', '1999-07-13 21:45', '1999-10-05 17:05', '1999-10-15 19:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setRevisionsDescriptions(('Added IsakmpDOI TEXTUAL-CONVENTION.', 'Changed CONTACT-INFO.', 'Put in real experimental branch number for module.', 'Added exchange types, tracked IKE standard.  Split\n                   IkeNotifyMessageType off of IsakmpNotifyMessageType.', 'Removed stray comma in IsakmpNotifyMessageType.',))
if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setLastUpdated('9907132145Z')
if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setOrganization('Shiva')
if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setContactInfo('John Shriver\n                   Intel Corporation\n                   28 Crosby Drive\n                   Bedford, MA 01730\n\n                   Phone:\n                   +1-781-687-1329\n\n                   E-mail:\n                   John.Shriver@intel.com')
if mibBuilder.loadTexts: ipsecIsakmpIkeDoiTC.setDescription('The MIB module which defines the textual conventions\n                   used in IPSEC MIBs.  This includes Internet DOI\n                   numbers defined in RFC 2407, ISAKMP numbers defined\n                   in RFC 2408, and IKE numbers defined in RFC 2409.\n\n                   These Textual Conventions are defined in a seperate\n                   MIB module since they are protocol numbers managed\n                   by the IANA.  Revision control after publication\n                   will be under the authority of the IANA.')
class IpsecDoiSituation(TextualConvention, Unsigned32):
    reference = 'RFC 2407 sections 4.2 and 6.2'
    description = 'The IPSEC DOI Situation provides information that\n                   can be used by the responder to make a policy\n                   determination about how to process the incoming\n                   Security Association request.\n\n                   It is a four (4) octet bitmask, with the following\n                   values:\n\n                   sitIdentityOnly            0x01\n                   sitSecrecy                 0x02\n                   sitIntegrity               0x04\n\n                   The upper two bits (0x80000000 and 0x40000000) are\n                   reserved for private use amongst cooperating\n                   systems.'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class IpsecDoiSecProtocolId(TextualConvention, Integer32):
    reference = 'RFC 2407 section 4.4.1'
    description = 'These are the IPSEC DOI values for the Protocol-Id\n                   field in an ISAKMP Proposal Payload, and in all\n                   Notification Payloads.\n\n                   They are also used as the Protocol-ID In the\n                   Notification Payload and the Delete Payload.\n\n                   The values 249-255 are reserved for private use\n                   amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("protoIsakmp", 1), ("protoIpsecAh", 2), ("protoIpsecEsp", 3), ("protoIpcomp", 4))

class IpsecDoiTransformIdent(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.2 and 6.3'
    description = 'The IPSEC DOI ISAKMP Transform Identifier is an\n                   8-bit value which identifies a key exchange protocol\n                   to be used for the negotiation.  It is used in the\n                   Transform-Id field of an IKE Phase I Transform\n                   Payload.\n\n                   The values 249-255 are reserved for private use\n                   amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("reserved", 0), ("keyIke", 1))

class IpsecDoiAhTransform(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.3 and 6.4'
    description = 'The IPSEC DOI AH Transform Identifier is an 8-bit\n                   value which identifies a particular algorithm to be\n                   used to provide integrity protection for AH.  It is\n                   used in the Tranform-ID field of a ISAKMP Transform\n                   Payload for the IPSEC DOI, when the Protocol-Id of\n                   the associated Proposal Payload is 2 (AH).\n\n                   The values 249-255 are reserved for private use\n                   amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("reserved1", 1), ("ahMd5", 2), ("ahSha", 3), ("ahDes", 4))

class IpsecDoiEspTransform(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.4 and 6.5'
    description = 'The IPSEC DOI ESP Transform Identifier is an 8-bit\n                   value which identifies a particular algorithm to be\n                   used to provide secrecy protection for ESP.  It is\n                   used in the Tranform-ID field of a ISAKMP Transform\n                   Payload for the IPSEC DOI, when the Protocol-Id of\n                   the associated Proposal Payload is 2 (AH), 3 (ESP),\n                   and 4 (IPCOMP).\n\n                   The values 249-255 are reserved for private use\n                   amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("reserved", 0), ("espDesIv64", 1), ("espDes", 2), ("esp3Des", 3), ("espRc5", 4), ("espIdea", 5), ("espCast", 6), ("espBlowfish", 7), ("esp3Idea", 8), ("espDesIv32", 9), ("espRc4", 10), ("espNull", 11))

class IpsecDoiAuthAlgorithm(TextualConvention, Integer32):
    reference = 'RFC 2407 section 4.5'
    description = 'The ESP Authentication Algorithm used in the IPSEC\n                   DOI as a SA Attributes definition in the Transform\n                   Payload of Phase II of an IKE negotiation.  This\n                   set of values defines the AH authentication\n                   algorithm, when the associated Proposal Payload has\n                   a Protocol-ID of 2 (AH).  This set of values\n                   defines the ESP authentication algorithm, when the\n                   associated Proposal Payload has a Protocol-ID\n                   of 3 (ESP).\n\n                   Values 5-61439 are reserved to IANA.\n\n                   Values 61440-65535 are for private use.\n\n                   In a MIB, a value of 0 indicates that ESP\n                   has been negotiated without authentication.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("reserved", 0), ("hmacMd5", 1), ("hmacSha", 2), ("desMac", 3), ("kpdk", 4))

class IpsecDoiIpcompTransform(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.5 and 6.6'
    description = 'The IPSEC DOI IPCOMP Transform Identifier is an\n                   8-bit value which identifies a particular algorithm\n                   to be used to provide IP-level compression before\n                   ESP.  It is used in the Tranform-ID field of a ISAKMP\n                   Transform Payload for the IPSEC DOI, when the\n                   Protocol-Id of the associated Proposal Payload\n                   is 4 (IPCOMP).\n\n                   The values 1-47 are reserved for algorithms for which\n                   an RFC has been approved for publication.\n\n                   The values 48-63 are reserved for private use amongst\n                   cooperating systems.\n\n                   The values 64-255 are reserved for future expansion.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("reserved", 0), ("ipcompOui", 1), ("ipcompDeflate", 2), ("ipcompLzs", 3))

class IpsecDoiEncapsulationMode(TextualConvention, Integer32):
    description = 'The Encapsulation Mode used as an IPSEC DOI\n                   SA Attributes definition in the Transform Payload\n                   of a Phase II IKE negotiation.  This set of\n                   values defines encapsulation modes used for AH,\n                   ESP, and IPCOMP when the associated Proposal Payload\n                   has a Protocol-ID of 3 (ESP).\n\n                   Values 3-61439 are reserved to IANA.\n\n                   Values 61440-65535 are for private use.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("reserved", 0), ("tunnel", 1), ("transport", 2))

class IpsecDoiIdentType(TextualConvention, Integer32):
    reference = 'RFC 2407 sections 4.4.5, 4.6.2.1, and 6.9'
    description = 'The IPSEC DOI Identification Type is an 8-bit value\n                   which is used in the ID Type field as a discriminant\n                   for interpretation of the variable-length\n                   Identification Payload.\n\n                   The values 249-255 are reserved for private use\n                   amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("reserved", 0), ("idIpv4Addr", 1), ("idFqdn", 2), ("idUserFqdn", 3), ("idIpv4AddrSubnet", 4), ("idIpv6Addr", 5), ("idIpv6AddrSubnet", 6), ("idIpv4AddrRange", 7), ("idIpv6AddrRange", 8), ("idDerAsn1Dn", 9), ("idDerAsn1Gn", 10), ("idKeyId", 11))

class IsakmpDOI(TextualConvention, Integer32):
    reference = 'RFC 2048 section 3.4.'
    description = 'These are the domain of interpretation values for\n                   the ISAKMP Protocol.  They are a 32-bit value\n                   used in the Domain of Interpretation field of the\n                   Security Association Payload.\n                   Values 2-4294967295 are reserved to the IANA.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("isakmp", 0), ("ipsecDOI", 1))

class IsakmpCertificateEncoding(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.9'
    description = 'These are the values for the types of\n                   certificate-related information contained in the\n                   Certificate Data field of a Certificate Payload.\n                   They are used in the Cert Encoding field of the\n                   Certificate Payload.\n\n                   Values 11-255 are reserved.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("pkcs7", 1), ("pgp", 2), ("dnsSignedKey", 3), ("x509Signature", 4), ("x509KeyExchange", 5), ("kerberosTokens", 6), ("crl", 7), ("arl", 8), ("spki", 9), ("x509Attribute", 10))

class IsakmpExchangeType(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.1'
    description = 'These are the values used for the exchange types in\n                   the ISAKMP header.\n\n                   Values up to 31 are reserved for future\n                   DOI-independent assignment for ISAKMP.\n\n                   The values 240-255 are reserved for private use\n                   amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("reserved", 0), ("base", 1), ("identityProtect", 2), ("authOnly", 3), ("aggressive", 4), ("informational", 5))

class IsakmpNotifyMessageType(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.14.1'
    description = 'These are the values for the types of notification\n                   messages.  They are used as the Notify Message Type\n                   field in the Notification Payload.\n\n                   This textual convention merges the types\n                   for error types (in the range 1-16386) and for\n                   notification types (in the range 16384-65535).\n\n                   The values 16001-16383 are reserved for private use\n                   as error types amongst cooperating systems.\n\n                   The values 24576-32767 are reserved for use in\n                   each DOI.  Each DOI should have a clone of this\n                   textual convention adding local values.\n\n                   The values 32768-40958 are reserved for private use\n                   as notification types amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30))
    namedValues = NamedValues(("reserved", 0), ("invalidPayloadType", 1), ("doiNotSupported", 2), ("situationNotSupported", 3), ("invalidCookie", 4), ("invalidMajorVersion", 5), ("invalidMinorVersion", 6), ("invalidExchangeType", 7), ("invalidFlags", 8), ("invalidMessageId", 9), ("invalidProtocolId", 10), ("invalidSpi", 11), ("invalidTransformId", 12), ("attributesNotSupported", 13), ("noProposalChosen", 14), ("badProposalSyntax", 15), ("payloadMalformed", 16), ("invalidKeyInformation", 17), ("invalidIdInformation", 18), ("invalidCertEncoding", 19), ("invalidCertificate", 20), ("certTypeUnsupported", 21), ("invalidCertAuthority", 22), ("invalidHashInformation", 23), ("authenticationFailed", 24), ("invalidSignature", 25), ("addressNotification", 26), ("notifySaLifetime", 27), ("certificateUnavailable", 28), ("unsupportedExchangeType", 29), ("unequalPayloadLengths", 30))

class IkeExchangeType(TextualConvention, Integer32):
    reference = 'RFC 2409 Appendix A,\n                   draft-ietf-ipsec-ike-01.txt appendix A'
    description = 'These are the values used for the exchange types in\n                   the ISAKMP header.\n\n                   The values 32-239 are DOI-specific, these values are\n                   for the IPSec DOI used by IKE.\n\n                   The values 240-255 are reserved for private use\n                   amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 32, 33, 34))
    namedValues = NamedValues(("reserved", 0), ("base", 1), ("mainMode", 2), ("authOnly", 3), ("aggressive", 4), ("informational", 5), ("quickMode", 32), ("newGroupMode", 33), ("acknowledgedInfo", 34))

class IkeEncryptionAlgorithm(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A'
    description = 'Values for encryption algorithms negotiated\n                   for the ISAKMP SA by IKE in Phase I.  These are\n                   values for SA Attrbute type Encryption\n                   Algorithm (1).\n\n                   Values 7-65000 are reserved to IANA.\n\n                   Values 65001-65535 are for private use among\n                   mutually consenting parties.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("reserved", 0), ("desCbc", 1), ("ideaCbc", 2), ("blowfishCbc", 3), ("rc5R16B64Cbc", 4), ("tripleDesCbc", 5), ("castCbc", 6))

class IkeHashAlgorithm(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A'
    description = 'Values for hash algorithms negotiated\n                   for the ISAKMP SA by IKE in Phase I.  These are\n                   values for SA Attrbute type Hash Algorithm (2).\n\n                   Values 4-65000 are reserved to IANA.\n\n                   Values 65001-65535 are for private use among\n                   mutually consenting parties.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("reserved", 0), ("md5", 1), ("sha", 2), ("tiger", 3))

class IkeAuthMethod(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A,\n                   draft-ietf-ipsec-ike-01.txt appendix A'
    description = 'Values for authentication methods negotiated\n                   for the ISAKMP SA by IKE in Phase I.  These are\n                   values for SA Attrbute type Authentication\n                   Method (3).\n\n                   Values 6-65000 are reserved to IANA.\n\n                   Values 65001-65535 are for private use among\n                   mutually consenting parties.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("reserved", 0), ("preSharedKey", 1), ("dssSignatures", 2), ("rsaSignatures", 3), ("encryptionWithRsa", 4), ("revisedEncryptionWithRsa", 5), ("encryptionWithElGamal", 6), ("revisedEncryptionWithElGamal", 7))

class IkeGroupDescription(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A,\n                   draft-ietf-ipsec-ike-01.txt appendix A'
    description = 'Values for Oakley key computation groups for\n                   Diffie-Hellman exchange negotiated for the ISAKMP\n                   SA by IKE in Phase I.  They are also used in Phase II\n                   when perfect forward secrecy is in use.  These are\n                   values for SA Attrbute type Group Description (4).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("reserved", 0), ("modp768", 1), ("modp1024", 2), ("ec2nGalois2P155", 3), ("ec2nGalois2P185", 4), ("modp1536", 5))

class IkeGroupType(TextualConvention, Integer32):
    reference = 'RFC 2409 appendix A'
    description = 'Values for Oakley key computation group types\n                   negotiated for the ISAKMP SA by IKE in Phase I.\n                   They are also used in Phase II when perfect forward\n                   secrecy is in use.  These are values for SA Attribute\n                   type Group Type (5).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("reserved", 0), ("modp", 1), ("ecp", 2), ("ec2n", 3))

class IkePrf(TextualConvention, Unsigned32):
    reference = 'RFC 2409 appendix A'
    description = 'Values for Pseudo-Random Functions used with\n                   with the hash algorithm negotiated for the ISAKMP SA\n                   by IKE in Phase I.  There are currently no\n                   pseudo-random functions defined, the default HMAC is\n                   always used.  These are values for SA Attribute type\n                   PRF (13).\n\n                   Values 1-65000 are reserved to IANA.\n\n                   Values 65001-65535 are for private use among\n                   mutually consenting parties.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IkeNotifyMessageType(TextualConvention, Integer32):
    reference = 'RFC 2408 section 3.14.1 and RFC 2407 sections 4.6.3\n                   and 6.10'
    description = 'These are the values for the types of notification\n                   messages.  They are used as the Notify Message Type\n                   field in the Notification Payload.\n\n                   This textual convention merges the types\n                   for error types (in the range 1-16386) and for\n                   notification types (in the range 16384-65535).\n\n                   This textual convention is a merge of values\n                   defined by ISAKMP with the additional values\n                   defined in the IPSEC DOI.\n\n                   The values 16001-16383 are reserved for private use\n                   as error types amongst cooperating systems.\n\n                   The values 32001-32767 are reserved for private use\n                   as notification types amongst cooperating systems.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 24576, 24577, 24578))
    namedValues = NamedValues(("reserved", 0), ("invalidPayloadType", 1), ("doiNotSupported", 2), ("situationNotSupported", 3), ("invalidCookie", 4), ("invalidMajorVersion", 5), ("invalidMinorVersion", 6), ("invalidExchangeType", 7), ("invalidFlags", 8), ("invalidMessageId", 9), ("invalidProtocolId", 10), ("invalidSpi", 11), ("invalidTransformId", 12), ("attributesNotSupported", 13), ("noProposalChosen", 14), ("badProposalSyntax", 15), ("payloadMalformed", 16), ("invalidKeyInformation", 17), ("invalidIdInformation", 18), ("invalidCertEncoding", 19), ("invalidCertificate", 20), ("certTypeUnsupported", 21), ("invalidCertAuthority", 22), ("invalidHashInformation", 23), ("authenticationFailed", 24), ("invalidSignature", 25), ("addressNotification", 26), ("notifySaLifetime", 27), ("certificateUnavailable", 28), ("unsupportedExchangeType", 29), ("unequalPayloadLengths", 30), ("responderLifetime", 24576), ("replayStatus", 24577), ("initialContact", 24578))

mibBuilder.exportSymbols("IPSEC-ISAKMP-IKE-DOI-TC", IsakmpDOI=IsakmpDOI, IkeAuthMethod=IkeAuthMethod, IpsecDoiSecProtocolId=IpsecDoiSecProtocolId, IpsecDoiSituation=IpsecDoiSituation, IkePrf=IkePrf, IpsecDoiAhTransform=IpsecDoiAhTransform, IsakmpExchangeType=IsakmpExchangeType, IsakmpNotifyMessageType=IsakmpNotifyMessageType, IpsecDoiEncapsulationMode=IpsecDoiEncapsulationMode, ipsecIsakmpIkeDoiTC=ipsecIsakmpIkeDoiTC, IkeExchangeType=IkeExchangeType, IpsecDoiIpcompTransform=IpsecDoiIpcompTransform, IsakmpCertificateEncoding=IsakmpCertificateEncoding, IpsecDoiEspTransform=IpsecDoiEspTransform, IpsecDoiIdentType=IpsecDoiIdentType, IkeGroupDescription=IkeGroupDescription, IpsecDoiAuthAlgorithm=IpsecDoiAuthAlgorithm, IkeHashAlgorithm=IkeHashAlgorithm, IpsecDoiTransformIdent=IpsecDoiTransformIdent, PYSNMP_MODULE_ID=ipsecIsakmpIkeDoiTC, IkeGroupType=IkeGroupType, IkeEncryptionAlgorithm=IkeEncryptionAlgorithm, IkeNotifyMessageType=IkeNotifyMessageType)
