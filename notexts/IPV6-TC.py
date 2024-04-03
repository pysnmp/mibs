#
# PySNMP MIB module IPV6-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IPV6-TC
# Produced by pysmi-1.1.11 at Wed Apr  3 15:17:27 2024
# On host fv-az979-188 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Counter32, IpAddress, Unsigned32, Bits, ModuleIdentity, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Counter32", "IpAddress", "Unsigned32", "Bits", "ModuleIdentity", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Ipv6Address(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class Ipv6AddressPrefix(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class Ipv6AddressIfIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class Ipv6IfIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Ipv6IfIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mibBuilder.exportSymbols("IPV6-TC", Ipv6AddressPrefix=Ipv6AddressPrefix, Ipv6IfIndex=Ipv6IfIndex, Ipv6Address=Ipv6Address, Ipv6IfIndexOrZero=Ipv6IfIndexOrZero, Ipv6AddressIfIdentifier=Ipv6AddressIfIdentifier)
