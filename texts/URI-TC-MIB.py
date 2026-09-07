#
# PySNMP MIB module URI-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source URI-TC-MIB
# Source digest sha256:fc808797a60dc5da78d578a8b7a17ea5ec64a0230645a5f924c1cc478290951a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
uriTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 164))
uriTcMIB.setRevisions(('2007-09-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: uriTcMIB.setRevisionsDescriptions(('Initial revision, published as RFC 5017.\n\n            Copyright (C) The IETF Trust (2007).  This version of this\n            MIB module is part of RFC 5017; see the RFC itself for full\n            legal notices.',))
if mibBuilder.loadTexts: uriTcMIB.setLastUpdated('2007-09-10 00:00')
if mibBuilder.loadTexts: uriTcMIB.setOrganization('IETF Operations and Management (OPS) Area')
if mibBuilder.loadTexts: uriTcMIB.setContactInfo('EMail: ops-area@ietf.org\n                  Home page: http://www.ops.ietf.org/')
if mibBuilder.loadTexts: uriTcMIB.setDescription('This MIB module defines textual conventions for\n            representing URIs, as defined by RFC 3986 STD 66.')
class Uri(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    description = "A Uniform Resource Identifier (URI) as defined by STD 66.\n\n            Objects using this TEXTUAL-CONVENTION MUST be in US-ASCII\n            encoding, and MUST be normalized as described by RFC 3986\n            Sections 6.2.1, 6.2.2.1, and 6.2.2.2.  All unnecessary\n            percent-encoding is removed, and all case-insensitive\n            characters are set to lowercase except for hexadecimal\n            digits, which are normalized to uppercase as described in\n            Section 6.2.2.1.\n\n            The purpose of this normalization is to help provide unique\n            URIs.  Note that this normalization is not sufficient to\n            provide uniqueness.  Two URIs that are textually distinct\n            after this normalization may still be equivalent.\n\n            Objects using this TEXTUAL-CONVENTION MAY restrict the\n            schemes that they permit.  For example, 'data:' and 'urn:'\n            schemes might not be appropriate.\n\n            A zero-length URI is not a valid URI.  This can be used to\n            express 'URI absent' where required, for example when used\n            as an index field.\n\n            Where this TEXTUAL-CONVENTION is used for an index field,\n            it MUST be subtyped to restrict its length.  There is an\n            absolute limit of 128 subids for an OID, and it is not\n            efficient to have OIDs whose length approaches this\n            limit."
    status = 'current'
    displayHint = '1a'

class Uri255(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    description = "A Uniform Resource Identifier (URI) as defined by STD 66.\n\n            Objects using this TEXTUAL-CONVENTION MUST be in US-ASCII\n            encoding, and MUST be normalized as described by RFC 3986\n            Sections 6.2.1, 6.2.2.1, and 6.2.2.2.  All unnecessary\n            percent-encoding is removed, and all case-insensitive\n            characters are set to lowercase except for hexadecimal\n            digits, which are normalized to uppercase as described in\n            Section 6.2.2.1.\n\n            The purpose of this normalization is to help provide unique\n            URIs.  Note that this normalization is not sufficient to\n            provide uniqueness.  Two URIs that are textually distinct\n            after this normalization may still be equivalent.\n\n            Objects using this TEXTUAL-CONVENTION MAY restrict the\n            schemes that they permit.  For example, 'data:' and 'urn:'\n            schemes might not be appropriate.\n\n            A zero-length URI is not a valid URI.  This can be used to\n            express 'URI absent' where required, for example when used\n            as an index field.\n\n            STD 66 URIs are of unlimited length.  Objects using this\n            TEXTUAL-CONVENTION impose a length limit on the URIs that\n            they can represent.  Where no length restriction is\n            required, objects SHOULD use the 'Uri' TEXTUAL-CONVENTION\n            instead.  Objects used as indices SHOULD subtype the 'Uri'\n            TEXTUAL-CONVENTION."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Uri1024(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    description = "A Uniform Resource Identifier (URI) as defined by STD 66.\n\n            Objects using this TEXTUAL-CONVENTION MUST be in US-ASCII\n            encoding, and MUST be normalized as described by RFC 3986\n            Sections 6.2.1, 6.2.2.1, and 6.2.2.2.  All unnecessary\n            percent-encoding is removed, and all case-insensitive\n            characters are set to lowercase except for hexadecimal\n            digits, which are normalized to uppercase as described in\n            Section 6.2.2.1.\n\n            The purpose of this normalization is to help provide unique\n            URIs.  Note that this normalization is not sufficient to\n            provide uniqueness.  Two URIs that are textually distinct\n            after this normalization may still be equivalent.\n\n            Objects using this TEXTUAL-CONVENTION MAY restrict the\n            schemes that they permit.  For example, 'data:' and 'urn:'\n            schemes might not be appropriate.\n            A zero-length URI is not a valid URI.  This can be used to\n            express 'URI absent' where required, for example when used\n            as an index field.\n\n            STD 66 URIs are of unlimited length.  Objects using this\n            TEXTUAL-CONVENTION impose a length limit on the URIs that\n            they can represent.  Where no length restriction is\n            required, objects SHOULD use the 'Uri' TEXTUAL-CONVENTION\n            instead.  Objects used as indices SHOULD subtype the 'Uri'\n            TEXTUAL-CONVENTION."
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

mibBuilder.exportSymbols("URI-TC-MIB", PYSNMP_MODULE_ID=uriTcMIB, Uri1024=Uri1024, Uri255=Uri255, Uri=Uri, uriTcMIB=uriTcMIB)
