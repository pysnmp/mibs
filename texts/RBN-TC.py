#
# PySNMP MIB module RBN-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/RBN-TC
# Produced by pysmi-1.1.12 at Tue Jun  4 11:45:37 2024
# On host fv-az1427-842 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
rbnModules, = mibBuilder.importSymbols("RBN-SMI", "rbnModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, Bits, iso, NotificationType, Counter32, Gauge32, Counter64, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Bits", "iso", "NotificationType", "Counter32", "Gauge32", "Counter64", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 5, 2))
rbnTC.setRevisions(('2011-01-19 18:00', '2009-10-20 17:00', '2004-06-19 17:00', '2003-03-17 17:00', '2002-11-11 00:00', '2002-06-26 00:00', '2000-07-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnTC.setRevisionsDescriptions(('Update CONTACT-INFO & ORGANIZATION. ', 'Added new textual convention: RbnUnsigned64 for read-write\n        capable 64 bit integer value.', 'Added new textual convention: RbnPortMediumType. Correct \n        warnings given by smilint.', 'Added new textual convention: RbnVidOrUntagged.', 'Moved definitions of RbnSlot and RbnPort from RBN-PVC-MIB.\n        Updated range on RbnSlot and RbnPort.', 'Updated CONTACT-INFO. Added new textual conventions:\n        RbnKBytes and RbnPercentage.', 'Initial version.',))
if mibBuilder.loadTexts: rbnTC.setLastUpdated('201101191800Z')
if mibBuilder.loadTexts: rbnTC.setOrganization('Ericsson AB.')
if mibBuilder.loadTexts: rbnTC.setContactInfo('       Ericsson AB.\n\n            Postal: 100 Headquarters Dr\n                    San Jose, CA  95134\n                    USA\n\n             Phone: +1 408 750 5000\n               Fax: +1 408 750 5599\n            ')
if mibBuilder.loadTexts: rbnTC.setDescription('Defines common textual conventions used in RBN mib\n        modules.')
class RbnCircuitHandle(TextualConvention, OctetString):
    description = 'A unique identifier for individual circuits. The string is\n        composed of the following:\n        \n            Octet 1     slot\n                  2     port\n                  3-8   circuit identifier\n        \n        slots/ports are numbered 0..n. The SMS CLI also numbers slots/ports\n        0..n but SE CLI numbers slots/ports 1..n. For example: When the \n        SE CLI refers to slot/port 1/2, this maps to to the RbnCircuitHandle\n        slot/port 0/1   \n        '
    status = 'current'
    displayHint = '1d:1d:2x-2x-2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class RbnKBytes(TextualConvention, Integer32):
    description = 'Storage size, expressed in units of 1024 bytes.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class RbnPercentage(TextualConvention, Integer32):
    description = 'This Textual Convention describes an object that stores \n        a whole integer percentage value.'
    status = 'current'
    displayHint = 'd%'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class RbnSlot(TextualConvention, Unsigned32):
    description = "The chassis slot number.  This is the physical slot\n        number as reported in the CLI command 'show hardware'\n        on SMS and the CLI command 'show port' on SE."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class RbnPort(TextualConvention, Unsigned32):
    description = "The chassis port number.  This is the physical port\n        number as reported in the CLI command 'show hardware'\n        on SMS and the CLI command 'show port' on SE."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class RbnVidOrUntagged(TextualConvention, Integer32):
    description = 'The twelve-bit VLAN Identifer (VID) used to uniquely\n        identify the VLAN to which the frame belongs.  The VID is\n        encoded as an unsigned binary number.  An untagged frame\n        does not carry any identification of the VLAN to which it\n        belongs and is designated with a value of 4096.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4096)

class RbnPortMediumType(TextualConvention, Integer32):
    description = 'Medium type of NAS port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 11, 12, 13, 14))
    namedValues = NamedValues(("unknown", 0), ("dsl", 11), ("cable", 12), ("wireless", 13), ("satellite", 14))

class RbnUnsigned64(TextualConvention, OctetString):
    description = 'Unsigned 64 bit integer value is represented as an\n         OCTET STRING.  This allows an unsigned integer value in\n         the range 0..18446744073709551615.  \n\n         The octets are ordered with the first octet containing\n         the highest ordered bits of the integer and the 8th octet\n         containing the lowest ordered bits, corresponding to\n         network byte order.'
    status = 'current'
    displayHint = '8d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

mibBuilder.exportSymbols("RBN-TC", RbnPortMediumType=RbnPortMediumType, RbnPercentage=RbnPercentage, RbnCircuitHandle=RbnCircuitHandle, RbnSlot=RbnSlot, rbnTC=rbnTC, RbnKBytes=RbnKBytes, RbnUnsigned64=RbnUnsigned64, RbnPort=RbnPort, RbnVidOrUntagged=RbnVidOrUntagged, PYSNMP_MODULE_ID=rbnTC)
