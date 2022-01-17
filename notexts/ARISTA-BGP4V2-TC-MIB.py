#
# PySNMP MIB module ARISTA-BGP4V2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-BGP4V2-TC-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 22:00:30 2022
# On host fv-az74-933 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
aristaExperiment, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaExperiment")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, IpAddress, Bits, Integer32, Counter32, NotificationType, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "IpAddress", "Bits", "Integer32", "Counter32", "NotificationType", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaBgp4V2TC = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 4, 2))
aristaBgp4V2TC.setRevisions(('2014-08-15 00:00', '2012-10-19 00:00', '2011-01-17 00:00',))
if mibBuilder.loadTexts: aristaBgp4V2TC.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaBgp4V2TC.setOrganization('Arista Networks, Inc.')
class AristaBgp4V2IdentifierTC(TextualConvention, OctetString):
    reference = 'RFC 4273, Section 4.2'
    status = 'current'
    displayHint = '1d.'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class AristaBgp4V2AddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class AristaBgp4V2SubsequentAddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3. The value of this object should be restricted to be between the values of 0 and 255.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("unicast", 1), ("multicast", 2), ("mpls", 4))

mibBuilder.exportSymbols("ARISTA-BGP4V2-TC-MIB", aristaBgp4V2TC=aristaBgp4V2TC, AristaBgp4V2SubsequentAddressFamilyIdentifierTC=AristaBgp4V2SubsequentAddressFamilyIdentifierTC, PYSNMP_MODULE_ID=aristaBgp4V2TC, AristaBgp4V2AddressFamilyIdentifierTC=AristaBgp4V2AddressFamilyIdentifierTC, AristaBgp4V2IdentifierTC=AristaBgp4V2IdentifierTC)
