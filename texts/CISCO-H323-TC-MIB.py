#
# PySNMP MIB module CISCO-H323-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-H323-TC-MIB
# Source digest sha256:5ee63e749812445d00d93442da08db43aa967d0100228f45e07fea4bdc870fb1
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoH323TCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 41))
ciscoH323TCMIB.setRevisions(('1998-10-09 12:00', '2000-03-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoH323TCMIB.setRevisionsDescriptions(('The initial version of the mib.', 'Removed CgkUtf8String as it is a duplicate definition of\n         SnmpAdminString.',))
if mibBuilder.loadTexts: ciscoH323TCMIB.setLastUpdated('2000-03-10 00:00')
if mibBuilder.loadTexts: ciscoH323TCMIB.setOrganization('Cisco Systems, Inc')
if mibBuilder.loadTexts: ciscoH323TCMIB.setContactInfo('        Cisco Systems\n\t         Customer Service\n\n        Postal:  170 West Tasman Drive\n                 San Jose, CA  95134\n                 USA\n\n        Tel:    +1 800 553-NETS\n\n        E-mail: h323-support@cisco.com')
if mibBuilder.loadTexts: ciscoH323TCMIB.setDescription('The MIB Module defines a common set of Textual Conventions used\n\tin mib modules supporting ITU-T H.323.0 and ITU-T H.225.0\n\tRecommendations.')
class CgkIA5String(TextualConvention, OctetString):
    description = 'Corresponds to an IA5String.'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkE164String(TextualConvention, OctetString):
    description = "An IA5String limited to the character set '0123456789*#,.' "
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkTAddressTag(TextualConvention, Integer32):
    description = 'A tag to identify the type of the transport address contained \n        in the TAddress data type.  The values correlate to the \n        TransportAddress defined in the H.225.0 V2 ITU protocol\n        specification. The tag indicates how to interpret the value of\n        a TAddress data type defined in this specification.  All\n        TAddress values are in network byte order \n\n                        TAddress size       TAddress contents\n                 ipv4      6 octets         IPv4 (4 octets), port (2 octets)\n                 ipv6     18                IPv6 (16), port (2)\n                 ipx      12                net (4), node (6), port (2)\n                 nsap     1-20              nsap(1-20)\n                 netbios  16                netbios(16)\n         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("other", 0), ("ipv4", 1), ("ipv6", 2), ("ipx", 3), ("nsap", 4))

class CgkNAddressTag(TextualConvention, Integer32):
    description = 'A tag to identify the type of the network address contained in the\n\tCgkNAddress textual convention defined in this specification.  All\n\tCgkNAddress values are in network byte order. \n\n                        NAddress size\n                 ipv4      4 octets\n                 ipv6     16\n                 ipx      10                net (4), node (6)\n                 nsap     1-20              nsap(1-20)\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("other", 0), ("ipv4", 1), ("ipv6", 2), ("ipx", 3), ("nsap", 4))

class CgkNAddress(TextualConvention, OctetString):
    description = 'Denotes a network address.  An object defined with this syntax\n\tmust have a corresponding CgkNAddressTag object which identifies\n\tthe actual size and type.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkGlobalIdentifier(TextualConvention, OctetString):
    reference = 'ITU-T H225.0, Version 2 section 7.6'
    description = 'A 16 octet field containing a unique identifier.  The\n        identifier contains the following fields:\n        \n           60 bit       nanosecond time (octets 0-6, low 4 bits of octet 7)\n           4  bit       version  (hi 4 bits of octet 7)\n           3  octet     0 (a variant field)\n           1  octet     hi 2bits 0, low 6bits clock sequence.\n           6  octet     MAC Address \n        \n        See Reference for generation of this value.\n        '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class CgkAliasTag(TextualConvention, Integer32):
    description = 'A tag to identify the type of the Alias address contained in\n         the CgkAliasAddress data type.  The values correlate to the \n         AliasAddress defined in the H.225.0 V2 ITU protocol specification. \n         The tag indicates how to interpret the value of an AliasAddress \n         data type defined in that specification.\n\n                              AliasAddress contents\n                 other        unknown\n                 e164         CgkE164String\n                 h323Id       CgkUtf8String\n                 urlId        CgkIA5String containing a URL\n                 transportId  CgkTAddressTag, TAddress\n                 emailId      CgkIA5String containing e-mail address\n                 partyNumber  contains PartyNumber (E164String)\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 0), ("e164", 1), ("h323Id", 2), ("urlId", 3), ("transportId", 4), ("emailId", 5), ("partyNumber", 6))

class CgkAliasAddress(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    description = 'A data type corresponding to AliasAddress defined in H.225.0. \n        The value of an object of this type has the syntax and\n        symantics identified by CgkAliasTag.  An object defined as\n        CgkAliasAddress must have a corresponding CgkAliasTag object.'
    status = 'current'
    displayHint = '512a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 512)

class CgkEndpointID(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    description = 'A CgkUtf8String corresponding to EndpointIdentifer defined\n        in H.225.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkGatekeeperID(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    description = 'A CgkUtf8String corresponding to GatekeeperIdentifier defined\n        in H.225.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

mibBuilder.exportSymbols("CISCO-H323-TC-MIB", CgkAliasAddress=CgkAliasAddress, CgkAliasTag=CgkAliasTag, CgkE164String=CgkE164String, CgkEndpointID=CgkEndpointID, CgkGatekeeperID=CgkGatekeeperID, CgkGlobalIdentifier=CgkGlobalIdentifier, CgkIA5String=CgkIA5String, CgkNAddress=CgkNAddress, CgkNAddressTag=CgkNAddressTag, CgkTAddressTag=CgkTAddressTag, PYSNMP_MODULE_ID=ciscoH323TCMIB, ciscoH323TCMIB=ciscoH323TCMIB)
