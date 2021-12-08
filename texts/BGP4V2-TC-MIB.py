#
# PySNMP MIB module BGP4V2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/BGP4V2-TC-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:36:15 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Counter32, Bits, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Counter64, IpAddress, ObjectIdentity, TimeTicks, ModuleIdentity, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Counter32", "Bits", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Counter64", "IpAddress", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bgp4V2TC = ModuleIdentity((1, 3, 6, 1, 2, 1, 100))
bgp4V2TC.setRevisions(('2010-02-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bgp4V2TC.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: bgp4V2TC.setLastUpdated('201002010000Z')
if mibBuilder.loadTexts: bgp4V2TC.setOrganization('IETF IDR Working Group')
if mibBuilder.loadTexts: bgp4V2TC.setContactInfo('E-mail:  idr@ietf.org')
if mibBuilder.loadTexts: bgp4V2TC.setDescription('Textual conventions for BGP-4.\n                     Copyright (C) The IETF Trust (2010).  This\n                     version of this MIB module is part of RFC XXX;\n                     see the RFC itself for full legal notices.')
class Bgp4V2IdentifierTC(TextualConvention, OctetString):
    reference = 'RFC 4273, Section 4.2'
    description = 'The representation of a BGP Identifier.  BGP Identifiers\n             are presented in the received network byte order.\n\n             The BGP Identifier is displayed as if it is an IP address,\n             even if it would be an illegal one.'
    status = 'current'
    displayHint = '1d.'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class Bgp4V2AddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3'
    description = 'The representation of a BGP AFI.  The value of this object\n             should be restricted to be between the values of 0 and 65535.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class Bgp4V2SubsequentAddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3.  The value of this object should be\n             restricted to be between the values of 0 and 255.'
    description = 'The representation of a BGP SAFI'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("unicast", 1), ("multicast", 2), ("mpls", 4))

mibBuilder.exportSymbols("BGP4V2-TC-MIB", bgp4V2TC=bgp4V2TC, Bgp4V2IdentifierTC=Bgp4V2IdentifierTC, Bgp4V2AddressFamilyIdentifierTC=Bgp4V2AddressFamilyIdentifierTC, Bgp4V2SubsequentAddressFamilyIdentifierTC=Bgp4V2SubsequentAddressFamilyIdentifierTC, PYSNMP_MODULE_ID=bgp4V2TC)
