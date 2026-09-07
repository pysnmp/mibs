#
# PySNMP MIB module CISCO-IPSEC-TC (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IPSEC-TC
# Source digest sha256:abbccb829ebabb285d3c48a625f32f58bbf283ca5ae93d7700b52edf847ce31a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIPsecTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 422))
ciscoIPsecTc.setRevisions(('2004-07-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIPsecTc.setRevisionsDescriptions(('\n          Initial version of this module.\n          ',))
if mibBuilder.loadTexts: ciscoIPsecTc.setLastUpdated('2004-07-22 00:00')
if mibBuilder.loadTexts: ciscoIPsecTc.setOrganization('Cisco Systems Inc. and Tivoli Systems Inc.')
if mibBuilder.loadTexts: ciscoIPsecTc.setContactInfo('           Cisco Systems\n                     Customer Service\n\n             Postal: 170 W Tasman Drive\n                     San Jose, CA  95134\n                     USA\n\n                     Tivoli Systems\n                     Research Triangle Park, NC\n\n\n             Tel:    +1 800 553-NETS\n             E-mail: cs-ipsecmib@external.cisco.com\n                     bret_harrison@tivoli.com\n         ')
if mibBuilder.loadTexts: ciscoIPsecTc.setDescription('\n          This MIB module defines the textual conventions \n          used in the IPsec suite of MIBs. This includes \n          Internet DOI numbers defined in RFC 2407, ISAKMP \n          numbers defined in RFC 2408, and IKE numbers \n          defined in RFC 2409.\n          ')
class CCryptoMD5Hash(TextualConvention, OctetString):
    description = 'This type denotes a 128-bit MD5 output string \n             of an input string'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class CIKEIsakmpDoi(TextualConvention, Integer32):
    description = 'The Domain of Interpretation of the IKE \n             implementation. This type is used to implement \n             distinctions between the configuration of the \n             IKE implementation for distinct Phase 2 protocols \n             that use IKE.\n             \n             Description of enum constants of this type:\n              isakmpDoiIPsec:\n                     Denotes that IPsec protocol is used in Phase-2\n\n              isakmpDoiFcsp:\n                     Denotes that FC-SP protocol is used in Phase-2\n\n              isakmpDoiCps:\n                     Denotes that Cps protocol is used in Phase-2\n\n              isakmpDoiFcCtAuth:\n                     Denotes that Fc-Ct-Auth protocol is used in \n                     Phase-2\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("isakmpDoiUnknown", 1), ("isakmpDoiOther", 2), ("isakmpDoiIPsec", 3), ("isakmpDoiFcsp", 4), ("isakmpDoiCps", 5), ("isakmpDoiFcCtAuth", 6))

class CIKELifetime(TextualConvention, Unsigned32):
    description = '\n             This type corresponds to the lifetime of\n             ISAKMP security associations.\n             \n             The unit of information is seconds.\n             '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(60, 86400)

class CIKELifesize(TextualConvention, Unsigned32):
    description = '\n             This type corresponds to the lifesize of\n             a ISAKMP security association in the number \n             of kilobytes of data that has been processed\n             by the security association.\n\n             The unit of information is kilobytes.\n             '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(2560, 4294967295)

class CIPsecEncryptionKeySize(TextualConvention, Unsigned32):
    description = "\n             This type is used by objects that denote the\n             size in bits of key of an encryption transform.\n\n             The value of 0 has been allowed to provide for\n             'NULL' encryption transforms.\n             "
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CIPsecControlProtocol(TextualConvention, Integer32):
    description = "\n             The protocol used for keying and control in \n             IPsec connections. The value of 'cpManual' \n             indicates manual administration of IPsec tunnels. \n             This enumeration will be expanded as new keying \n             protocols are standardized.\n \n             The value 'cpAll' does not denote a specific \n             keying protocol; it has been defined only as a \n             convenience to facilitate aggregation of metrics \n             across all control protocols.\n\n             Description of enum constants of this type:\n               cpManual:\n                     Denotes manual keying (i.e., no signaling).\n\n               cpIkev1:\n                     Denotes keying signaling using IKEv1 protocol.\n\n               cpIkev2:\n                     Denotes keying signaling using IKEv2 protocol.\n\n               cpKink:\n                     Denotes keying signaling using KINK.\n\n               cpPhoturis:\n                     Denotes keying signaling using Photuris.\n             "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("cpUnknown", 1), ("cpAll", 2), ("cpOther", 3), ("cpManual", 4), ("cpIkev1", 5), ("cpIkev2", 6), ("cpKink", 7), ("cpPhoturis", 8))

class CIPsecProtocol(TextualConvention, Integer32):
    reference = 'rfc2402, rfc2406 and rfc2409'
    description = '\n             A protocol used for encapsulating the Phase-2 \n             tunneled traffic. The enumerations correspond \n             to Authentication Header, Encapsulating Security \n             Payload and IP compression protocols.\n \n             The enum constants used in this denote the standard\n             IPsec protocols, viz., Authentication Header (AH),\n             ESP and IP compression.\n\n             Description of enum constants of this type:\n               ipsecProtAh:\n                     Denotes IPsec Authentication Header (AH)\n                     protocol.\n\n               ipsecProtEsp:\n                     Denotes IPsec Encapsulating Security\n                     Payload (ESP) protocol.\n\n               ipsecProtIPcomp:\n                     Denotes IPsec Packet Compression\n                     protocol.\n\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ipsecProtUnknown", 1), ("ipsecProtAh", 2), ("ipsecProtEsp", 3), ("ipsecProtIPcomp", 4))

class CIPsecPhase1PeerIdentityType(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = '\n             The type of IPsec Phase-1 peer identity.\n             The peer may be identified by one of the ID \n             types defined in IPSEC DOI.\n\n\n             Description of enum constants of this type:\n               idIpv4Addr:\n                   IPv4 address\n\n               idFqdn:\n                   Fully QUalified Domain Name\n\n               idDn:\n                   Represents the binary DER encoding of \n                   the identity.\n\n               idIpv6Addr:\n                   IPv6 address\n                   \n               idUserFqdn:\n                   User FQDN (such as an email address).\n\n               idIpv4AddrSubnet:\n                   IPv4 subnet specification (comprising\n                   a subnet identifier and a subnet mask).\n\n               idIpv6AddrSubnet:\n                   IPv6 subnet specification (comprising\n                   a subnet identifier and a subnet mask).\n\n               idIpv4AddrRange:\n                   A range of IPv4 addresses (comprising\n                   a starting address and an ending address)\n\n               idIpv6AddrRange:\n                   A range of IPv6 addresses (comprising\n                   a starting address and an ending address)\n\n               idDerAsn1Gn:\n                   The ASN.1 encoded general number.\n\n               idKeyId:\n                   This is the symbolic name (key identifier).\n\n               idWwn:\n                   World Wide Number or the encoding of\n                   the layer-2 address used by MDS switches.\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("idOther", 1), ("idIpv4Addr", 2), ("idFqdn", 3), ("idDn", 4), ("idIpv6Addr", 5), ("idUserFqdn", 6), ("idIpv4AddrSubnet", 7), ("idIpv6AddrSubnet", 8), ("idIpv4AddrRange", 9), ("idIpv6AddrRange", 10), ("idDerAsn1Gn", 11), ("idKeyId", 12), ("idWwn", 13))

class CIPsecIkeNegoMode(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = '\n             The negotiation mode used by IKE \n             protocol in Phase-1.\n\n             The type enumerates constants to denote the\n             two distinct modes of operation of ISAKMP-based\n             IPsec signaling in Phase-2, viz., Main Mode \n             (mainMode) and Aggressive Mode (aggressiveMode).\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mainMode", 1), ("aggressiveMode", 2))

class CIPsecIkeHashAlgorithm(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = '\n             The hash algorithm used in IPsec Phase-1\n             IKE negotiations.\n\n             Description of enum constants of this type:\n              md5:\n                Hash payload using MD5 algorithm.\n\n              sha:\n                Hash payload using 96-bit SHA-1 algorithm \n                as defined in FIPS 180-1.\n\n              tiger:\n                Hash payload using Tiger hash algorithm.\n\n              sha256:\n                Hash payload using 256-bit key SHA-1 algorithm.\n\n              sha384:\n                Hash payload using 384-bit key SHA-1 algorithm.\n\n              sha512:\n                Hash payload using 512-bit key SHA-1 algorithm.\n\n              aesMac\n                Hash payload using AES-XCBC-MAC-96 algorithm.\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("none", 1), ("other", 2), ("md5", 3), ("sha", 4), ("tiger", 5), ("sha256", 6), ("sha384", 7), ("sha512", 8), ("aesMac", 9))

class CIPsecIkeAuthMethod(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = '\n             The authentication method used in IPsec \n             Phase-1 IKE negotiations.\n\n             Description of enum constants of this type:\n              preSharedKey:\n                Peer authentication using pre-shared keys.\n\n              rsaSignature:\n                Peer authentication using digital signatures.\n\n              rsaEncryption:\n                Peer authentication using encrypted nonces.\n\n              revRsaEncryption:\n                Peer authentication using revised RSA encryption.\n\n              dssSignature:\n                Peer authentication using DSS signatures.\n\n              elGamalEncryption:\n                Peer authentication using El Gamal.\n\n              revElGamalEncryption:\n                Peer authentication using revised El Gamal.\n\n              ecdsaSignature:\n                Peer authentication using Elliptic Curve Digital \n                Signatures.\n\n              gssApiV1:\n                Peer authentication using Generic Security Services \n                API v1.\n\n              gssApiV2:\n                Peer authentication using Generic Security Services \n                API v2.\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("preSharedKey", 2), ("rsaSignature", 3), ("rsaEncryption", 4), ("revRsaEncryption", 5), ("dssSignature", 6), ("elGamalEncryption", 7), ("revElGamalEncryption", 8), ("ecsdaSignature", 9), ("gssApiV1", 10), ("gssApiV2", 11))

class CIPsecDiffHellmanGrp(TextualConvention, Integer32):
    reference = 'rfc2408, rfc2409 and rfc3526'
    description = "\n             An indication of whether a Diffie Hellman Group has \n             been specified to be used in negotiations and the\n             type of group as follows. \n             \n               'notDH'     -- indicates no use of a Diffie Hellman\n               'modp768'   -- 768-bit MODP\n               'modp1024'  -- 1024-bit MODP\n               'modp1536'  -- 1536-bit MODP group\n               'ec2nGP155' -- EC2N group on GP[2^155]\n               'ec2nGP185' -- EC2N group on GP[2^185]\n               'ec2nGF163' -- EC2N group over GF[2^163]\n               'ec2nGF283' -- EC2N group over GF[2^283]\n               'ec2nGF409' -- EC2N group over GF[2^409]\n               'ec2nGF571' -- EC2N group over GF[2^571]\n               'modp2048'  -- 2048-bit MODP group\n\n             "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("notDH", 2), ("modp768", 3), ("modp1024", 4), ("ec2nGP155", 5), ("ec2nGP185", 6), ("modp1536", 7), ("ec2nGF163", 8), ("ec2nGF283", 9), ("ec2nGF409", 10), ("ec2nGF571", 11), ("modp2048", 12))

class CIPsecEncapMode(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = '\n             The encapsulation mode used by an IPsec Phase-2\n             Tunnel.\n\n             The type enumerates values to denote the two modes \n             of encapsulation of payload used by IPsec, viz.,\n             transport mode (encapTunnel) and tunnel mode\n             (encapTransport).\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("encapTunnel", 1), ("encapTransport", 2))

class CIPsecTransform(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = '\n             The transform to be used by an IPsec Phase-2 \n             protocol (ESP or AH or IPCP).\n\n             Description of enum constants of this type:\n               xformAhRFC1829:\n                 Authentication Header per RFC1829\n    \n               xformAhMD5:\n                 Authentication Header using MD5\n\n               xformAhSHA1:\n                 Authentication Header using SHA1\n\n               xformEspNULL:\n                 ESP with NULL encryption.\n\n               xformEspDES:\n                 ESP with DES encryption.\n\n               xformEsp3DES:\n                 ESP with 3DES encryption.\n\n               xformEspAES128:\n                 ESP with AES encryption using CBC mode (128-bit key).\n\n               xformEspAES192:\n                 ESP with AES encryption using CBC mode (192-bit key).\n\n               xformEspAES256:\n                 ESP with AES encryption using CBC mode (256-bit key).\n\n               xformEspMD5:\n                 ESP with MD5 hash.\n\n               xformEspSHA1:\n                 ESP with SHA-1 hash.\n\n               xformCompLZS:\n                 IP compression using LZS.\n                 \n               xformEspRc5:\n                 Payload encryption using RC5. \n                  \n               xformEspIdea:\n                 Payload encryption using International \n                 Data Encryption Algorithm.\n                 \n               xformEspCast:\n                 Payload encryption using CAST.\n               \n               xformEspTwofish:\n                 Payload encryption using TwoFish.\n                 \n               xformEspBlowfish:\n                 Payload encryption using BlowFish.\n\n               xformEsp3idea:\n                 Payload encryption using International \n                 Data Encryption Algorithm.\n \n               xformEspRc4:\n                 Payload encryption using RC4.\n                  \n               xformEspDesMac:\n                  ESP with DES MAC hash.\n                    \n               xformEspHmacSha256:\n                  ESP with HMAC SHA-1 hash (256-bit key).\n               \n               xformEspHmacSha384:\n                  ESP with HMAC SHA-1 has (384-bit key).\n                  \n               xformEspHmacSha512:\n                  ESP with HMAC SHA-1 has (512-bit key).\n                  \n               xformEspRipemd:\n                  ESP with RIPEMD cryptographic hash.\n                   \n               xformAHDesMac:\n                  AH with DES MAC hash.\n                  \n               xformAHHmacSha256:\n                  AH with HMAC SHA-1 hash (256-bit key).\n                  \n               xformAHHmacSha384:\n                  AH with HMAC SHA-1 hash (384-bit key).\n                  \n               xformAHHmacSha512:\n                  AH with HMAC SHA-1 hash (512-bit key).\n                  \n               xformAHRipemd:\n                  AH with RIPEMD cryptographic hash. \n\n               xformEspAESXCbcMac:\n                 ESP with AES XCBC MAC authentication.\n\n               xformAHAESXCbcMac:\n                 AH with AES XCBC MAC authentication.\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))
    namedValues = NamedValues(("xformNONE", 1), ("xformOTHER", 2), ("xformAhRFC1829", 3), ("xformAhMD5", 4), ("xformAhSHA1", 5), ("xformEspNULL", 6), ("xformEspDES", 7), ("xformEsp3DES", 8), ("xformEspAES128", 9), ("xformEspAES192", 10), ("xformEspAES256", 11), ("xformEspMD5", 12), ("xformEspSHA1", 13), ("xformCompLZS", 14), ("xformEspAESCtr128", 15), ("xformEspAESCtr192", 16), ("xformEspAESCtr256", 17), ("xformEspRc5", 18), ("xformEspIdea", 19), ("xformEspCast", 20), ("xformEspTwofish", 21), ("xformEspBlowfish", 22), ("xformEsp3idea", 23), ("xformEspRc4", 24), ("xformEspDesMac", 25), ("xformEspHmacSha256", 26), ("xformEspHmacSha384", 27), ("xformEspHmacSha512", 28), ("xformEspRipemd", 29), ("xformAHDesMac", 30), ("xformAHHmacSha256", 31), ("xformAHHmacSha384", 32), ("xformAHHmacSha512", 33), ("xformAHRipemd", 34), ("xformEspAESXCbcMac", 35), ("xformAHAESXCbcMac", 36))

class CIPsecSecuritySuite(TextualConvention, Integer32):
    reference = 'rfc2408 and rfc2409'
    description = '\n             The combination of IPsec Phase-2 protocols.\n\n             suiteConfEsp:\n                 Confidentiality using ESP.\n\n             suiteIntegEsp:\n                 Confidentiality and Integrity check \n                 using ESP.\n\n             suiteIntegAh:\n                 Integrity check with AH.\n\n             suiteConfComp:\n                 Confidentiality using ESP;\n                 Packet compression.\n \n             suiteIntegEspComp:\n                 Packet Integrity using ESP;\n                 Packet compression.\n\n             suiteIntegAhComp:\n                 Packet Integrity using AH;\n                 Packet compression.\n\n             suiteConfAh:\n                 Confidentiality using ESP; \n                 Packet Integrity using AH.\n\n             suiteConfAhComp:\n                 Confidentiality using ESP; \n                 Packet Integrity using AH;\n                 Packet compression.\n\n             suiteIntegEspAh:\n                 Packet Integrity using ESP and AH.\n\n             suiteIntegEspAhComp:\n                 Packet Integrity using ESP and AH;\n                 Packet compression.\n\n             suiteConfIntegEsp:\n                 Confidentiality and Packet Integrity \n                 using ESP.\n\n             suiteConfIntegEspComp:\n                 Confidentiality and Packet Integrity \n                 using ESP;\n                 Packet compression.\n\n             suiteConfIntegEspAh:\n                 Confidentiality using ESP;\n                 Packet Integrity using ESP and AH.\n\n             suiteConfIntegEspAhComp:\n                 Confidentiality using ESP;\n                 Packet Integrity using ESP and AH;\n                 Packet compression.\n\n             suiteOther:\n                 A suite that does not fit any of the\n                 above definitions.\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("suiteOther", 1), ("suiteConfEsp", 2), ("suiteIntegEsp", 3), ("suiteIntegAh", 4), ("suiteConfComp", 5), ("suiteIntegEspComp", 6), ("suiteIntegAhComp", 7), ("suiteConfAh", 8), ("suiteConfAhComp", 9), ("suiteIntegEspAh", 10), ("suiteIntegEspAhComp", 11), ("suiteConfIntegEsp", 12), ("suiteConfIntegEspComp", 13), ("suiteConfIntegEspAh", 14), ("suiteConfIntegEspAhComp", 15))

class CIPsecNATTraversalMode(TextualConvention, Integer32):
    description = "\n             The encapsulation mode used to implement NAT \n             traversal.\n\n             Both 'EncapMode' and 'NATTraversalMode' are \n             attributes of a Phase-2 IPsec tunnel. Value of \n             an object of this type is constrained based on \n             the value of its tunnel encapsulation mode: if \n             the tunnel encapsulation mode is 'encapTransport', \n             then the value of this attribute may be one of \n             'natEncapNone' or 'natEncapNATT'.\n\n             Description of enum constants of this type:\n               natEncapIPsecOverUdp:\n                 IPsec encapsulation over UDP.\n\n               natEncapIPsecOverTcp:\n                 IPsec encapsulation over TCP.\n\n               natEncapNATT:\n                 IPsec encapsulation over NAT-T protocol.\n             "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("natEncapNone", 1), ("natEncapOther", 2), ("natEncapIPsecOverUdp", 3), ("natEncapIPsecOverTcp", 4), ("natEncapNATT", 5))

class CIPsecEncryptAlgorithm(TextualConvention, Integer32):
    description = "\n              The encryption algorithm used in negotiations.\n              Since payload encryption is done by the ESP \n              protocol, these enums are prefixed with 'esp'.\n\n              Description of enum constants of this type:\n               espDes:\n                Payload encryption using 56-bit key DES.\n\n               esp3des:\n                Payload encryption using 168-bit 3DES.\n\n               espRc5:\n                Payload encryption using RC5.\n\n               espIdea:\n                Payload encryption using International \n                Data Encryption Algorithm.\n\n               espCast:\n                Payload encryption using CAST.\n\n               espTwofish:\n                Payload encryption using TwoFish.\n\n               espBlowfish:\n                Payload encryption using BlowFish.\n\n               esp3idea:\n                Payload encryption using International \n                Data Encryption Algorithm.\n\n               espRc4:\n                Payload encryption using RC4.\n\n               espNull:\n                NULL Payload encryption.\n\n               espAes128:\n               espAes192:\n               espAes256:\n                Payload encryption using AES CBC mode and keysizes of\n                128, 192 and 256 bit keys.\n                \n               espAesCtr128:\n               espAesCtr192:\n               espAesCtr256:\n                Payload encryption using AES CTR mode and keysizes of\n                128, 192 and 256 bit keys.  \n               \n             "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("none", 1), ("other", 2), ("espDes", 3), ("esp3des", 4), ("espRc5", 5), ("espIdea", 6), ("espCast", 7), ("espTwofish", 8), ("espBlowfish", 9), ("esp3idea", 10), ("espRc4", 11), ("espNull", 12), ("espAes128", 13), ("espAes192", 14), ("espAes256", 15), ("espAesCtr128", 16), ("espAesCtr192", 17), ("espAesCtr256", 18))

class CIPsecSpi(TextualConvention, Unsigned32):
    description = '\n             The type of the SPI (Security Parameter Index)\n             associated with IPsec Phase-2 security associations.\n             '
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(256, 4294967295)

class CIPsecAuthAlgorithm(TextualConvention, Integer32):
    description = '\n             The authentication algorithm used by a\n             security association of an IPsec Phase-2 \n             Tunnel.\n\n             Description of enum constants of this type:\n               hmacMd5:\n                 Hash validation using HMAC MD5.\n\n               hmacSha:\n                 Hash validation using HMAC SHA-1.\n\n               desMac:\n                 Hash validation using DES as MAC.\n\n               hmacSha256:\n                 Hash validation using 256-bit SHA-1.\n\n               hmacSha384:\n                 Hash validation using 384-bit SHA-1.\n\n               hmacSha512:\n                 Hash validation using 512-bit SHA-1.\n\n               ripemd:\n                 Hash validation using RIPEMD \n                 cryptographic hash function.\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("none", 1), ("other", 2), ("hmacMd5", 3), ("hmacSha", 4), ("desMac", 5), ("hmacSha256", 6), ("hmacSha384", 7), ("hmacSha512", 8), ("ripemd", 9))

class CIPsecCompAlgorithm(TextualConvention, Integer32):
    description = '\n             The compression algorithm used by a\n             security association of an IPsec Phase-2 \n             Tunnel.\n\n             Description of enum constants of this type:\n               compOui:\n                 IP payload compression using a proprietary\n                 algorithm identified using an Organization\n                 Unique Identifier (OUI).\n\n               compDeflate:\n                 IP payload compression using deflate algorithm.\n\n               compLzs:\n                 IP payload compression using LZS algorithm.\n\n               compLzjh:\n                 IP payload compression using LZJH algorithm.\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 1), ("other", 2), ("compOui", 3), ("compDeflate", 4), ("compLzs", 5), ("compLzjh", 6))

class CIPsecEndPtType(TextualConvention, Integer32):
    description = "\n             The type of identity use to specify an IPsec \n             End Point.\n      \n             For a description of the enum values, please refer\n             to the description of type \n             'CIPsecPhase1PeerIdentityType'.\n             "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("idIpv4Addr", 2), ("idIpv4AddrRange", 3), ("idIpv4AddrSubnet", 4), ("idFqdn", 5), ("idUserFqdn", 6), ("idIpv6Addr", 7), ("idIpv6AddrRange", 8), ("idIpv6AddrSubnet", 9), ("idDerAsn1Dn", 10), ("idDerAsn1Gn", 11), ("idKeyId", 12))

class CIPsecPhase2SaDirection(TextualConvention, Integer32):
    reference = 'rfc2409'
    description = '\n             Phase-2 IPsec security associations are simplex. \n             This textual convention is used as the type of \n             attribute(s) of a Phase-2 security association.\n\n             Description of enum constants of this type:\n              saDirectionIn:\n                 The IPsec security association is used to\n                 process incoming traffic.\n\n              saDirectionOut:\n                 The IPsec security association is used to\n                 process outgoing traffic.\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("saDirectionUnknown", 1), ("saDirectionIn", 2), ("saDirectionOut", 3))

class CIPsecPhase1TunnelIndex(TextualConvention, Unsigned32):
    description = '\n             The index of the IPsec Phase-1 (IKE) Tunnel \n             Table. An index of this type is a number which \n             begins at 1 and is incremented with each tunnel \n             that is created.  The value of this object will \n             wrap at 2,147,483,647.\n             '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class CIPsecPhase1TunnelIndexOrZero(TextualConvention, Unsigned32):
    description = "\n             This type defines a range of values for index of \n             the IPsec Phase-1 (IKE) Tunnel Table, including\n             the invalid index '0'. An object of this type\n             is used to implement a soft reference to an IKE\n             tunnel. The value of zero is used to denote the\n             fact that the reference points to a non-existent\n             IKE tunnel.\n             "
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CIPsecPhase2TunnelIndex(TextualConvention, Unsigned32):
    description = '\n             The type of the index of the IPsec Phase-2 Tunnel \n             Table. An index of this type is a number which\n             begins at one and is incremented with each tunnel \n             that is created. The value of this object will \n             wrap at 2,147,483,647.\n             '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class CIPsecPmtu(TextualConvention, Unsigned32):
    description = '\n             The type of the Path MTU (Maximum Transmission \n             Unit) of an IPsec Phase-2 Tunnel.\n             '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(68, 1500)

class CIPsecLifetime(TextualConvention, Unsigned32):
    description = '\n             This type corresponds to the lifetime in\n             seconds of IPsec Phase-2 security associations.\n             '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(120, 86400), )
class CIPsecLifesize(TextualConvention, Unsigned32):
    description = '\n             This type corresponds to the life-size of\n             a Phase-2 security association in the number \n             of kilobytes of data that has been processed\n             by the security association.\n             '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2560, 4294967295), )
class CIPsecTunnelIdleTime(TextualConvention, Unsigned32):
    description = '\n             This type corresponds to the time interval\n             specified in seconds during which no traffic\n             has been processed by a Phase-2 security\n             association.\n             '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 86400), )
class CIPsecNumCryptoMaps(TextualConvention, Gauge32):
    description = '\n              Integral units representing count of \n              cryptomaps.\n              '
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CIPsecTunnelStatus(TextualConvention, Integer32):
    description = '\n             This type represents the status of an IPsec \n             Phase-1 or Phase-2 Tunnel. Objects of this type \n             may be used to bring down the tunnel they represent \n             by setting value of the object to destroy(5). \n             Objects of this type cannot be used to create \n             a tunnel.\n\n             Description of enum constants of this type:\n              initializePhase1:\n                The tunnel is initializing Phase 1 operations \n                (applies only to IKE tunnels).\n\n              awaitXauth:\n                The tunnel has concluded peer authentication\n                successfully and is awaiting the completion of\n                extended Authentication (applies only to IKE \n                tunnels).\n\n              awaitCommit:\n                The tunnel has concluded initialization and\n                is awaiting a signal (commit bit) from the peer \n                to start operations.\n\n              active:\n                The tunnel is active.\n\n              destroy:\n                This value is used in SNMP SET operations to\n                tear down the specified tunnel.\n\n              rekey:\n                This value is used in SNMP SET operations to\n                force a rekeying.\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initializePhase1", 1), ("awaitXauth", 2), ("awaitCommit", 3), ("active", 4), ("destroy", 5), ("rekey", 6))

class CIPsecCryptomapType(TextualConvention, Integer32):
    description = '\n             The type of a cryptomap entry. Cryptomap \n             is a unit of IOS IPSec policy specification.\n\n             Description of enum constants of this type:\n                cryptomapTypeMANUAL:\n                  The cryptomap entry uses manual keying.\n\n                cryptomapTypeISAKMP:\n                  The cryptomap entry uses IKE protocol\n                  for keying.\n\n                cryptomapTypeDYNAMIC:\n                  The cryptomap entry is dynamically instantiated.\n\n                cryptomapTypeDYNAMICDISCOVERY:\n                  The cryptomap entry is dynamically instantiated\n                  and uses tunnel endpoint discovery to identify \n                  the peer during tunnel setup.\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cryptomapTypeNONE", 1), ("cryptomapTypeMANUAL", 2), ("cryptomapTypeISAKMP", 3), ("cryptomapTypeCET", 4), ("cryptomapTypeDYNAMIC", 5), ("cryptomapTypeDYNAMICDISCOVERY", 6))

class CIPsecCryptomapSetBindStatus(TextualConvention, Integer32):
    description = "\n             The status of the binding of a cryptomap set to \n             the specified interface. The value when queried \n             is always 'attached'. When set to 'detached', the \n             cryptomap set if detached from the specified \n             interface. Setting the value to 'attached' will \n             result in SNMP General Error.\n\n             Description of enum constants of this type:\n                attached:\n                  The cryptomap set is attached to an interface.\n\n                detached:\n                  The cryptomap set is not attached to any interface.\n             "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("attached", 2), ("detached", 3))

class CIPsecIkePRFAlgorithm(TextualConvention, Integer32):
    description = '\n             The Pseudo Random Function algorithm used in\n             IPsec Phase-1 IKEv2 negotiations.\n\n             Description of enum constants of this type:\n               prfHmacMd5:\n                 HMAC version of MDS.\n               \n               prfHmacSha1:\n                 HMAC version of SHA-1 algorithm\n             '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("other", 2), ("prfHmacMd5", 3), ("prfHmacSha1", 4))

mibBuilder.exportSymbols("CISCO-IPSEC-TC", CCryptoMD5Hash=CCryptoMD5Hash, CIKEIsakmpDoi=CIKEIsakmpDoi, CIKELifesize=CIKELifesize, CIKELifetime=CIKELifetime, CIPsecAuthAlgorithm=CIPsecAuthAlgorithm, CIPsecCompAlgorithm=CIPsecCompAlgorithm, CIPsecControlProtocol=CIPsecControlProtocol, CIPsecCryptomapSetBindStatus=CIPsecCryptomapSetBindStatus, CIPsecCryptomapType=CIPsecCryptomapType, CIPsecDiffHellmanGrp=CIPsecDiffHellmanGrp, CIPsecEncapMode=CIPsecEncapMode, CIPsecEncryptAlgorithm=CIPsecEncryptAlgorithm, CIPsecEncryptionKeySize=CIPsecEncryptionKeySize, CIPsecEndPtType=CIPsecEndPtType, CIPsecIkeAuthMethod=CIPsecIkeAuthMethod, CIPsecIkeHashAlgorithm=CIPsecIkeHashAlgorithm, CIPsecIkeNegoMode=CIPsecIkeNegoMode, CIPsecIkePRFAlgorithm=CIPsecIkePRFAlgorithm, CIPsecLifesize=CIPsecLifesize, CIPsecLifetime=CIPsecLifetime, CIPsecNATTraversalMode=CIPsecNATTraversalMode, CIPsecNumCryptoMaps=CIPsecNumCryptoMaps, CIPsecPhase1PeerIdentityType=CIPsecPhase1PeerIdentityType, CIPsecPhase1TunnelIndex=CIPsecPhase1TunnelIndex, CIPsecPhase1TunnelIndexOrZero=CIPsecPhase1TunnelIndexOrZero, CIPsecPhase2SaDirection=CIPsecPhase2SaDirection, CIPsecPhase2TunnelIndex=CIPsecPhase2TunnelIndex, CIPsecPmtu=CIPsecPmtu, CIPsecProtocol=CIPsecProtocol, CIPsecSecuritySuite=CIPsecSecuritySuite, CIPsecSpi=CIPsecSpi, CIPsecTransform=CIPsecTransform, CIPsecTunnelIdleTime=CIPsecTunnelIdleTime, CIPsecTunnelStatus=CIPsecTunnelStatus, PYSNMP_MODULE_ID=ciscoIPsecTc, ciscoIPsecTc=ciscoIPsecTc)
