#
# PySNMP MIB module BGP4V2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/BGP4V2-TC-MIB
# Produced by pysmi-1.1.0 at Fri Nov 19 15:06:49 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, mib_2, Bits, iso, TimeTicks, NotificationType, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "mib-2", "Bits", "iso", "TimeTicks", "NotificationType", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bgp4V2TC = ModuleIdentity((1, 3, 6, 1, 2, 1, 100))
bgp4V2TC.setRevisions(('2010-02-01 00:00',))
if mibBuilder.loadTexts: bgp4V2TC.setLastUpdated('201002010000Z')
if mibBuilder.loadTexts: bgp4V2TC.setOrganization('IETF IDR Working Group')
class Bgp4V2IdentifierTC(TextualConvention, OctetString):
    reference = 'RFC 4273, Section 4.2'
    status = 'current'
    displayHint = '1d.'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class Bgp4V2AddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class Bgp4V2SubsequentAddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3. The value of this object should be restricted to be between the values of 0 and 255.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("unicast", 1), ("multicast", 2), ("mpls", 4))

mibBuilder.exportSymbols("BGP4V2-TC-MIB", PYSNMP_MODULE_ID=bgp4V2TC, Bgp4V2AddressFamilyIdentifierTC=Bgp4V2AddressFamilyIdentifierTC, bgp4V2TC=bgp4V2TC, Bgp4V2IdentifierTC=Bgp4V2IdentifierTC, Bgp4V2SubsequentAddressFamilyIdentifierTC=Bgp4V2SubsequentAddressFamilyIdentifierTC)
