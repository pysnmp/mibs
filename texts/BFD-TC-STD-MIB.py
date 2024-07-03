#
# PySNMP MIB module BFD-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/BFD-TC-STD-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:19:32 2024
# On host fv-az1022-995 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, Bits, mib_2, Counter64, ObjectIdentity, Unsigned32, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, iso, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Bits", "mib-2", "Counter64", "ObjectIdentity", "Unsigned32", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "iso", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bfdTCStdMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 223))
bfdTCStdMib.setRevisions(('2014-08-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bfdTCStdMib.setRevisionsDescriptions(('Initial version.  Published as RFC 7330.',))
if mibBuilder.loadTexts: bfdTCStdMib.setLastUpdated('201408120000Z')
if mibBuilder.loadTexts: bfdTCStdMib.setOrganization('IETF Bidirectional Forwarding Detection\n                  Working Group')
if mibBuilder.loadTexts: bfdTCStdMib.setContactInfo('Thomas D. Nadeau\n         Brocade\n         Email:  tnadeau@lucidvision.com\n\n         Zafar Ali\n         Cisco Systems, Inc.\n         Email:  zali@cisco.com\n\n         Nobo Akiya\n         Cisco Systems, Inc.\n         Email:  nobo@cisco.com\n\n         Comments about this document should be emailed directly\n         to the BFD working group mailing list at\n         rtg-bfd@ietf.org')
if mibBuilder.loadTexts: bfdTCStdMib.setDescription("Copyright (c) 2014 IETF Trust and the persons identified as\n       authors of the code.  All rights reserved.\n\n       Redistribution and use in source and binary forms, with or\n       without modification, is permitted pursuant to, and subject\n\n       to the license terms contained in, the Simplified BSD License\n       set forth in Section 4.c of the IETF Trust's Legal Provisions\n       Relating to IETF Documents\n       (http://trustee.ietf.org/license-info).")
class BfdSessIndexTC(TextualConvention, Unsigned32):
    description = 'An index used to uniquely identify BFD sessions.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class BfdIntervalTC(TextualConvention, Unsigned32):
    description = 'The BFD interval in microseconds.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class BfdMultiplierTC(TextualConvention, Unsigned32):
    description = 'The BFD failure detection multiplier.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class BfdCtrlDestPortNumberTC(TextualConvention, Unsigned32):
    reference = 'Use of port 3784 from Katz, D. and D. Ward,\n     Bidirectional Forwarding Detection (BFD) for\n     IPv4 and IPv6 (Single Hop), RFC 5881, June 2010.\n\n     Use of port 4784 from Katz, D. and D. Ward,\n     Bidirectional Forwarding Detection (BFD) for\n     Multihop Paths, RFC 5883, June 2010.\n\n     Use of port 6784 from Bhatia, M., Chen, M., Boutros, S.,\n     Binderberger, M., and J. Haas, Bidirectional Forwarding\n     Detection (BFD) on Link Aggregation Group (LAG)\n     Interfaces, RFC 7130, February 2014.'
    description = 'UDP destination port number of BFD control packets.\n     3784 represents single-hop BFD session.\n     4784 represents multi-hop BFD session.\n     6784 represents BFD on Link Aggregation Group (LAG) session.\n\n     However, syntax is left open to wider range of values\n     purposely for two reasons:\n     1. Implementation uses non-compliant port number for\n        valid proprietary reason.\n     2. Potential future extension documents.\n\n     The value of 0 is a special, reserved value used\n     to indicate special conditions and should not be considered\n     a valid port number.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class BfdCtrlSourcePortNumberTC(TextualConvention, Unsigned32):
    reference = 'Port 49152..65535 from RFC5881'
    description = 'UDP source port number of BFD control packets.\n     However, syntax is left open to wider range of values\n     purposely for two reasons:\n     1. Implementation uses non-compliant port number for\n        valid proprietary reason.\n     2. Potential future extension documents.\n\n     The value of 0 is a special, reserved value used\n     to indicate special conditions and should not be considered\n     a valid port number.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

mibBuilder.exportSymbols("BFD-TC-STD-MIB", PYSNMP_MODULE_ID=bfdTCStdMib, bfdTCStdMib=bfdTCStdMib, BfdSessIndexTC=BfdSessIndexTC, BfdIntervalTC=BfdIntervalTC, BfdMultiplierTC=BfdMultiplierTC, BfdCtrlSourcePortNumberTC=BfdCtrlSourcePortNumberTC, BfdCtrlDestPortNumberTC=BfdCtrlDestPortNumberTC)
