#
# PySNMP MIB module ARISTA-BGP4V2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-BGP4V2-TC-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 15:36:48 2022
# On host fv-az135-436 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
aristaExperiment, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaExperiment")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Bits, ObjectIdentity, Gauge32, IpAddress, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Bits", "ObjectIdentity", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "Integer32")
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

mibBuilder.exportSymbols("ARISTA-BGP4V2-TC-MIB", AristaBgp4V2SubsequentAddressFamilyIdentifierTC=AristaBgp4V2SubsequentAddressFamilyIdentifierTC, AristaBgp4V2AddressFamilyIdentifierTC=AristaBgp4V2AddressFamilyIdentifierTC, aristaBgp4V2TC=aristaBgp4V2TC, AristaBgp4V2IdentifierTC=AristaBgp4V2IdentifierTC, PYSNMP_MODULE_ID=aristaBgp4V2TC)
