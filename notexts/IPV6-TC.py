#
# PySNMP MIB module IPV6-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IPV6-TC
# Produced by pysmi-1.1.3 at Wed Dec  1 17:24:59 2021
# On host fv-az77-605 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, Unsigned32, IpAddress, Integer32, Gauge32, MibIdentifier, ObjectIdentity, Bits, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Unsigned32", "IpAddress", "Integer32", "Gauge32", "MibIdentifier", "ObjectIdentity", "Bits", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class Ipv6Address(TextualConvention, OctetString):
    status = 'obsolete'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class Ipv6AddressPrefix(TextualConvention, OctetString):
    status = 'obsolete'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class Ipv6AddressIfIdentifier(TextualConvention, OctetString):
    status = 'obsolete'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class Ipv6IfIndex(TextualConvention, Integer32):
    status = 'obsolete'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Ipv6IfIndexOrZero(TextualConvention, Integer32):
    status = 'obsolete'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mibBuilder.exportSymbols("IPV6-TC", Ipv6AddressPrefix=Ipv6AddressPrefix, Ipv6Address=Ipv6Address, Ipv6AddressIfIdentifier=Ipv6AddressIfIdentifier, Ipv6IfIndex=Ipv6IfIndex, Ipv6IfIndexOrZero=Ipv6IfIndexOrZero)
