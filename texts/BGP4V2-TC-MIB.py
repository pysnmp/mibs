#
# PySNMP MIB module BGP4V2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/BGP4V2-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 04:23:21 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, Gauge32, ModuleIdentity, IpAddress, ObjectIdentity, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, MibIdentifier, TimeTicks, Bits, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Gauge32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "MibIdentifier", "TimeTicks", "Bits", "NotificationType", "Integer32")
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

mibBuilder.exportSymbols("BGP4V2-TC-MIB", PYSNMP_MODULE_ID=bgp4V2TC, bgp4V2TC=bgp4V2TC, Bgp4V2SubsequentAddressFamilyIdentifierTC=Bgp4V2SubsequentAddressFamilyIdentifierTC, Bgp4V2IdentifierTC=Bgp4V2IdentifierTC, Bgp4V2AddressFamilyIdentifierTC=Bgp4V2AddressFamilyIdentifierTC)
