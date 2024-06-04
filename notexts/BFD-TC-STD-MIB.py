#
# PySNMP MIB module BFD-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/BFD-TC-STD-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:14:18 2024
# On host fv-az1385-751 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, iso, Unsigned32, Gauge32, ObjectIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, NotificationType, Integer32, Counter64, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "iso", "Unsigned32", "Gauge32", "ObjectIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "NotificationType", "Integer32", "Counter64", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bfdTCStdMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 223))
bfdTCStdMib.setRevisions(('2014-08-12 00:00',))
if mibBuilder.loadTexts: bfdTCStdMib.setLastUpdated('201408120000Z')
if mibBuilder.loadTexts: bfdTCStdMib.setOrganization('IETF Bidirectional Forwarding Detection Working Group')
class BfdSessIndexTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class BfdIntervalTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class BfdMultiplierTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class BfdCtrlDestPortNumberTC(TextualConvention, Unsigned32):
    reference = 'Use of port 3784 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), RFC 5881, June 2010. Use of port 4784 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for Multihop Paths, RFC 5883, June 2010. Use of port 6784 from Bhatia, M., Chen, M., Boutros, S., Binderberger, M., and J. Haas, Bidirectional Forwarding Detection (BFD) on Link Aggregation Group (LAG) Interfaces, RFC 7130, February 2014.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class BfdCtrlSourcePortNumberTC(TextualConvention, Unsigned32):
    reference = 'Port 49152..65535 from RFC5881'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

mibBuilder.exportSymbols("BFD-TC-STD-MIB", BfdMultiplierTC=BfdMultiplierTC, BfdIntervalTC=BfdIntervalTC, BfdSessIndexTC=BfdSessIndexTC, PYSNMP_MODULE_ID=bfdTCStdMib, BfdCtrlSourcePortNumberTC=BfdCtrlSourcePortNumberTC, BfdCtrlDestPortNumberTC=BfdCtrlDestPortNumberTC, bfdTCStdMib=bfdTCStdMib)
