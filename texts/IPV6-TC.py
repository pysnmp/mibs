#
# PySNMP MIB module IPV6-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-TC
# Produced by pysmi-1.1.8 at Sat Jan 15 05:10:58 2022
# On host fv-az77-149 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Integer32, Gauge32, MibIdentifier, Unsigned32, ModuleIdentity, NotificationType, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Integer32", "Gauge32", "MibIdentifier", "Unsigned32", "ModuleIdentity", "NotificationType", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Ipv6Address(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 addresses.\n        This is a binary string of 16 octets in network\n        byte-order.\n\n        This object is obsoleted by INET-ADDRESS-MIB::InetAddress.'
    status = 'obsolete'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class Ipv6AddressPrefix(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 address\n       prefixes.  This is a binary string of up to 16\n       octets in network byte-order.\n       This object is obsoleted by INET-ADDRESS-MIB::InetAddress.'
    status = 'obsolete'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class Ipv6AddressIfIdentifier(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 address\n       interface identifiers.  This is a binary string\n        of up to 8 octets in network byte-order.\n\n       This object is obsoleted by IP-MIB::Ipv6AddressIfIdentifierTC.'
    status = 'obsolete'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class Ipv6IfIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero for each\n       internetwork-layer interface in the managed\n       system.  It is recommended that values are assigned\n       contiguously starting from 1.  The value for each\n       internetwork-layer interface must remain constant\n       at least from one re-initialization of the entity's\n       network management system to the next\n       re-initialization.\n\n       This object is obsoleted by IF-MIB::InterfaceIndex."
    status = 'obsolete'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Ipv6IfIndexOrZero(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the\n         Ipv6IfIndex convention.  The latter defines\n         a greater than zero value used to identify an IPv6\n         interface in the managed system.  This extension\n         permits the additional value of zero.  The value\n         zero is object-specific and must therefore be\n         defined as part of the description of any object\n         which uses this syntax.  Examples of the usage of\n         zero might include situations where interface was\n         unknown, or when none or all interfaces need to be\n         referenced.\n\n         This object is obsoleted by IF-MIB::InterfaceIndexOrZero.'
    status = 'obsolete'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mibBuilder.exportSymbols("IPV6-TC", Ipv6Address=Ipv6Address, Ipv6IfIndex=Ipv6IfIndex, Ipv6AddressIfIdentifier=Ipv6AddressIfIdentifier, Ipv6AddressPrefix=Ipv6AddressPrefix, Ipv6IfIndexOrZero=Ipv6IfIndexOrZero)
