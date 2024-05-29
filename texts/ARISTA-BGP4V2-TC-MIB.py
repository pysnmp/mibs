#
# PySNMP MIB module ARISTA-BGP4V2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-BGP4V2-TC-MIB
# Produced by pysmi-1.1.12 at Wed May 29 10:18:55 2024
# On host fv-az1984-402 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
aristaExperiment, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaExperiment")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, Counter32, NotificationType, iso, Counter64, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, ObjectIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Counter32", "NotificationType", "iso", "Counter64", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "ObjectIdentity", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaBgp4V2TC = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 4, 2))
aristaBgp4V2TC.setRevisions(('2014-08-15 00:00', '2012-10-19 00:00', '2011-01-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaBgp4V2TC.setRevisionsDescriptions(('Updated postal and e-mail addresses.', 'Renumbered inside the Arista enterprise space.', 'Initial version.',))
if mibBuilder.loadTexts: aristaBgp4V2TC.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaBgp4V2TC.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaBgp4V2TC.setContactInfo('Arista Networks, Inc.\n\n                  Postal: 5453 Great America Parkway\n                          Santa Clara, CA 95054\n\n                  Tel: +1 408 547-5500\n\n                  E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaBgp4V2TC.setDescription('Textual conventions for BGP-4.\n                      This version was published in\n                      draft-ietf-idr-bgp4-mibv2-13, and\n                      modified to be homed inside the Arista\n                      enterprise.  There were no other\n                      modifications.\n\n\n                      Copyright (C) The IETF Trust (2011).  This\n                      version of this MIB module is part of\n                      draft-ietf-idr-bgp4-mibv2-13.txt;\n                      see the draft itself for full legal notices.')
class AristaBgp4V2IdentifierTC(TextualConvention, OctetString):
    reference = 'RFC 4273, Section 4.2'
    description = 'The representation of a BGP Identifier.  BGP Identifiers\n              are presented in the received network byte order.\n\n              The BGP Identifier is displayed as if it is an IP address,\n              even if it would be an illegal one.'
    status = 'current'
    displayHint = '1d.'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class AristaBgp4V2AddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3'
    description = 'The representation of a BGP AFI.  The value of this object\n              should be restricted to be between the values of 0 and\n              65535.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class AristaBgp4V2SubsequentAddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3.  The value of this object should be\n              restricted to be between the values of 0 and 255.'
    description = 'The representation of a BGP SAFI'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("unicast", 1), ("multicast", 2), ("mpls", 4))

mibBuilder.exportSymbols("ARISTA-BGP4V2-TC-MIB", AristaBgp4V2AddressFamilyIdentifierTC=AristaBgp4V2AddressFamilyIdentifierTC, PYSNMP_MODULE_ID=aristaBgp4V2TC, aristaBgp4V2TC=aristaBgp4V2TC, AristaBgp4V2IdentifierTC=AristaBgp4V2IdentifierTC, AristaBgp4V2SubsequentAddressFamilyIdentifierTC=AristaBgp4V2SubsequentAddressFamilyIdentifierTC)
