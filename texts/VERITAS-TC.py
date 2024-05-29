#
# PySNMP MIB module VERITAS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veritas/VERITAS-TC.mib
# Produced by pysmi-1.1.12 at Wed May 29 08:16:33 2024
# On host fv-az698-992 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter64, iso, Unsigned32, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, NotificationType, ObjectIdentity, Bits, Gauge32, Counter32, enterprises, Opaque = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "iso", "Unsigned32", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Bits", "Gauge32", "Counter32", "enterprises", "Opaque")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
veritasModules, = mibBuilder.importSymbols("VERITAS-REG", "veritasModules")
veritastc = ModuleIdentity((1, 3, 6, 1, 4, 1, 1302, 5, 2))
if mibBuilder.loadTexts: veritastc.setLastUpdated('0401082030Z')
if mibBuilder.loadTexts: veritastc.setOrganization('VERITAS Software Corp.')
if mibBuilder.loadTexts: veritastc.setContactInfo('VERITAS Software Corp.\n                     1600 Plymouth Street.\n                     Mountain View, CA 94043 US\n                     Tel: +1 650 318 4464\n                     Email: support@veritas.com')
if mibBuilder.loadTexts: veritastc.setDescription('A private TEXTUAL CONVENTION module for VERITAS')
class Float(TextualConvention, Opaque):
    description = "A single precision floating-point number.  The semantics\n         and encoding are identical for type 'single' defined in\n         IEEE Standard for Binary Floating-Point,\n         ANSI/IEEE Std 754-1985.\n         The value is restricted to the BER serialization of\n         the following ASN.1 type:\n             FLOATTYPE ::= [120] IMPLICIT FloatType\n         (note: the value 120 is the sum of '30'h and '48'h)\n         The BER serialization of the length for values of\n         this type must use the definite length, short\n         encoding form.\n\n         For example, the BER serialization of value 123\n         of type FLOATTYPE is '9f780442f60000'h.  (The tag\n         is '9f78'h; the length is '04'h; and the value is\n         '42f60000'h.) The BER serialization of value\n         '9f780442f60000'h of data type Opaque is\n         '44079f780442f60000'h. (The tag is '44'h; the length\n         is '07'h; and the value is '9f780442f60000'h."
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

class Utf8StringLong(TextualConvention, OctetString):
    description = 'A human readable string represented using the ISO/IEC IS\n         10646-1 character set, encoded as an octet string using\n         the UTF-8 transformation format described in RFC 2279.\n\n         Since additional code points are added by amendments to\n         the 10646 standard from time to time, implementations must\n         be prepared to encounter any code point from 0x00000000 to\n         0x7fffffff.  Byte sequences that do not correspond to the\n         valid UTF-8 encoding of a code point or are outside this\n         range are prohibited.\n         \n         The use of control codes should be avoided. When it is\n         necessary to represent a newline, the control code\n         sequence CR LF should be used.\n \n         The use of leading or trailing white space should be\n         avoided.\n \n         For code points not directly supported by user interface\n         hardware or software, an alternative means of entry and\n         display, such as hexadecimal, may be provided.\n \n         For information encoded in 7-bit US-ASCII, the UTF-8\n         encoding is identical to the US-ASCII encoding.\n \n         UTF-8 may require multiple bytes to represent a single\n         character / code point; thus the length of a Utf8String in\n         octets may be different from the number of characters\n         encoded.  Similarly, size constraints refer to the number\n         of encoded octets, not the number of characters\n         represented by an encoding.\n\n         Note that the size of an Utf8String is measured in octets,\n         not characters.'
    status = 'current'
    displayHint = '65535t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 65535)

class Utf8StringShort(TextualConvention, OctetString):
    description = 'A Utf8String with a maximum length of 255 octets.  Note\n         that the size of an Utf8String is measured in octets, not\n         characters.'
    status = 'current'
    displayHint = '255t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Uint64ReadOnly(TextualConvention, Counter64):
    description = "This textual convention implements a READ-ONLY, unsigned, 64-bit\n\t\t integer, per the PROPOSED STANDARD RFC2856: 'Textual Conventions\n\t\t for Additional High Capacity Data Types' by A. Bierman,\n\t\t K. McCloghrie, R. Presuhn, June 2000.\n         \n         This textual convention may only be used if the object type being\n         defined will not take on signed values and is defined as read only."
    status = 'current'

class Int64ReadWrite(TextualConvention, OctetString):
    description = 'This textual convention implements a READ/WRITE, signed or unsigned,\n\t\t64-bit integer as a 21 character octet string.  The first character \n\t\tcould be a sign the remaining 20 characters should be treated as\n\t\tdecimal digits.\n\t\t\n\t\tThe valid values for this textual convention are 0 to (2^64)-1 \n\t\t[18446744073709551615] for unsigned integers and -(2^64)/2 \n\t\t[-9223372036854775808] to ((2^64)/2)-1 [9223372036854775807] for \n\t\tsigned integers.'
    status = 'current'
    displayHint = '21a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 21)

mibBuilder.exportSymbols("VERITAS-TC", Float=Float, Utf8StringLong=Utf8StringLong, veritastc=veritastc, Int64ReadWrite=Int64ReadWrite, PYSNMP_MODULE_ID=veritastc, Uint64ReadOnly=Uint64ReadOnly, Utf8StringShort=Utf8StringShort)
