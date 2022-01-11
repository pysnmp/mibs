#
# PySNMP MIB module LANGTAG-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/RFC5131-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:08:07 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, Gauge32, mib_2, TimeTicks, Bits, MibIdentifier, Integer32, Counter32, IpAddress, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Gauge32", "mib-2", "TimeTicks", "Bits", "MibIdentifier", "Integer32", "Counter32", "IpAddress", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
langTagTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 165))
langTagTcMIB.setRevisions(('2007-11-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: langTagTcMIB.setRevisionsDescriptions(('Initial revision, published as RFC 5131.\n\n            Copyright (C) The IETF Trust (2007).  This version of this\n            MIB module is part of RFC 5131; see the RFC itself for full\n            legal notices.',))
if mibBuilder.loadTexts: langTagTcMIB.setLastUpdated('200711090000Z')
if mibBuilder.loadTexts: langTagTcMIB.setOrganization('IETF Operations and Management (OPS) Area')
if mibBuilder.loadTexts: langTagTcMIB.setContactInfo('EMail: ops-area@ietf.org\n                  Home page: http://www.ops.ietf.org/')
if mibBuilder.loadTexts: langTagTcMIB.setDescription('This MIB module defines a textual convention for\n            representing BCP 47 language tags.')
class LangTag(TextualConvention, OctetString):
    reference = 'RFC 4646 BCP 47'
    description = "A language tag, constructed in accordance with BCP 47.\n\n            Only lowercase characters are allowed.  The purpose of this\n            restriction is to provide unique language tags for use as\n            indexes.  BCP 47 recommends case conventions for user\n            interfaces, but objects using this TEXTUAL-CONVENTION MUST\n            use only lowercase.\n\n            Values MUST be well-formed language tags, in conformance\n            with the definition of well-formed tags in BCP 47.  An\n            implementation MAY further limit the values it accepts to\n            those permitted by a 'validating' processor, as defined in\n            BCP 47.\n\n            In theory, BCP 47 language tags are of unlimited length.\n            The language tag described in this TEXTUAL-CONVENTION is of\n            limited length.  The analysis of language tag lengths in BCP\n            47 confirms that this limit will not pose a problem in\n            practice.  In particular, this length is greater than the\n            minimum requirements set out in Section 4.3.1.\n\n            A zero-length language tag is not a valid language tag.\n            This can be used to express 'language tag absent' where\n            required, for example, when used as an index field."
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 63), )
mibBuilder.exportSymbols("LANGTAG-TC-MIB", LangTag=LangTag, langTagTcMIB=langTagTcMIB, PYSNMP_MODULE_ID=langTagTcMIB)
