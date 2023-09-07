#
# PySNMP MIB module S5-TCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/S5-TCS-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 13:31:32 2023
# On host fv-az422-951 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
s5Tcs, = mibBuilder.importSymbols("S5-ROOT-MIB", "s5Tcs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, ObjectIdentity, Integer32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Counter64, TimeTicks, Gauge32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "ObjectIdentity", "Integer32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Counter64", "TimeTicks", "Gauge32", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
s5TcsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 17, 0))
s5TcsMib.setRevisions(('2013-10-10 00:00', '2004-07-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: s5TcsMib.setRevisionsDescriptions(('Version 114:  Add Integer32 to IMPORTS.', 'Version 113:  Conversion to SMIv2',))
if mibBuilder.loadTexts: s5TcsMib.setLastUpdated('201310100000Z')
if mibBuilder.loadTexts: s5TcsMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: s5TcsMib.setContactInfo('Nortel Networks')
if mibBuilder.loadTexts: s5TcsMib.setDescription("5000 Common Textual Conventions MIB\n\n            Copyright 1993-2004 Nortel Networks, Inc.\n            All rights reserved.\n            This Nortel Networks SNMP Management Information Base Specification\n            (Specification) embodies Nortel Networks' confidential and\n            proprietary intellectual property. Nortel Networks retains all\n            title and ownership in the Specification, including any\n            revisions.\n\n            This Specification is supplied 'AS IS,' and Nortel Networks makes\n            no warranty, either express or implied, as to the use,\n            operation, condition, or performance of the Specification.")
class IpxAddress(TextualConvention, OctetString):
    description = "A textual convention for IPX addresses. The first four bytes\n         are the network number in 'network order'. The last 6 bytes\n         are the MAC address."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

class TimeIntervalHrd(TextualConvention, Integer32):
    description = 'A textual convention for a period of time measured\n         in units of 0.01 seconds.'
    status = 'current'

class TimeIntervalSec(TextualConvention, Integer32):
    description = 'A textual convention for a period of time measured\n         in units of seconds.'
    status = 'current'

class SrcIndx(TextualConvention, Integer32):
    description = "A textual convention for an Index of a 'source'.\n         The values are encoded so that the same MIB object\n         can be used to describe the same type of data, but\n         from different sources.\n         For the 5000 Chassis, this is encoded in the\n         following base 10 fields:\n           1bbiii - identifies an interface on an NMM\n                      where 'bb' is the board index and\n                      'iii' is the interface number.\n        \n           2bbppp - identifies a connectivity port on\n                      a board where 'bb' is the board INDEX\n                      and 'ppp' is the port INDEX.\n        \n           3bblll - identifies a local channel on a\n                      board where 'bb' is the board INDEX\n                      and 'll' is the local channel INDEX.\n        \n           4bbccc - identifies a cluster on a board\n                      where 'bb' is the board INDEX and\n                      'cc' is the cluster INDEX.\n        \n           5bbfff - identifies a FPU on a board where\n                      'bb' is the board INDEX, and 'fff' is\n                      the FPU INDEX.\n        \n           6bbnnn - identifies host board backplane counters\n                      where 'bb' is the board INDEX, and\n                      'nnn' is the segment INDEX.\n        \n           7bbccc - identifies a NULL segment on a board\n                      where 'bb' is the board INDEX, and\n                      'ccc' is the cluster INDEX.\n        \n           8mmnnn - identifies a sum across all host board(s)\n                      connected to a given backplane segment\n                      where 'mm' is media type, and 'nnn' is\n                      the segment INDEX. (NOTE: This is currently\n                      only valid for Ethernet.)"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 999999)

class MediaType(TextualConvention, Integer32):
    description = 'A textual convention for Media types'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("eth", 2), ("tok", 3), ("fddi", 4))

class FddiBkNetMode(TextualConvention, Integer32):
    description = 'The FDDI backplane mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("thruLow", 2), ("thruHigh", 3), ("thruLowThruHigh", 4))

class BkNetId(TextualConvention, Integer32):
    description = 'The backplane network ID. This is a numeric assignment\n         made to a backplane channel, a piece of a divided\n         backplane channel, or a grouping of several backplane\n         channels (which is done for FDDI). The number (and values)\n         of the backplane networks is determined by the setting\n         of the channel divider(s) which split some or all\n         the backplane channels into networks, and by\n         grouping when allowed by the media (such as FDDI).\n         Different media and backplane implementations may\n         have a divider or not. Also, there may be different\n         mappings of backplane network IDs to a divided (or\n         undivided) backplane channel.\n        \n         Note to agent implementors - you must map the divided\n         (or undivided) backplane channel to the numbering here\n         based on the setting of the backplane channel divider(s),\n         and/or the grouping of the channels for FDDI.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class BkChan(TextualConvention, Integer32):
    description = 'The physical backplane channel identification.\n         This does not change when a backplane is divided.\n         A value of zero means no channel. Otherwise, the\n         channels are numbered starting at one.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class LocChan(TextualConvention, Integer32):
    description = 'The physical local channel identification.\n         A value of zero means no channel. Otherwise, the\n         channels are numbered starting at one.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class AttId(TextualConvention, Integer32):
    description = 'The attachment ID. This is either a backplane\n         network ID, a local channel, or as an indication\n         of no backplane network attachment. Negative numbers\n         are used to identify local channels on a board.\n         Where used, the board must also be specified\n         (or implied). A value of zero is used to indicate\n         no (or null) attachment. Positive numbers are the\n         backplane network IDs. The number (and values) of\n         the backplane networks is determined by the setting\n         of the channel divider(s) which split some or all\n         the backplane channels into backplane networks,\n         and by grouping when allowed by the media (such as\n         FDDI). Different media and implementations may have\n         a divider or not. Also, there may be different\n         mappings of backplane network IDs to a divided\n         (or undivided) backplane channel.\n        \n         Note to agent implementors - you must map the divided\n         (or undivided) backplane channel to the numbering here\n         based on the setting of the backplane channel divider(s),\n         and/or the grouping of the channels for FDDI.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-255, 255)

mibBuilder.exportSymbols("S5-TCS-MIB", PYSNMP_MODULE_ID=s5TcsMib, MediaType=MediaType, IpxAddress=IpxAddress, BkChan=BkChan, s5TcsMib=s5TcsMib, TimeIntervalHrd=TimeIntervalHrd, TimeIntervalSec=TimeIntervalSec, SrcIndx=SrcIndx, BkNetId=BkNetId, AttId=AttId, FddiBkNetMode=FddiBkNetMode, LocChan=LocChan)
