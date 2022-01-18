#
# PySNMP MIB module IANA-RTPROTO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IANA-RTPROTO-MIB
# Produced by pysmi-1.1.8 at Tue Jan 18 14:52:58 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Unsigned32, NotificationType, IpAddress, Bits, ModuleIdentity, Counter64, MibIdentifier, Counter32, Integer32, mib_2, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Unsigned32", "NotificationType", "IpAddress", "Bits", "ModuleIdentity", "Counter64", "MibIdentifier", "Counter32", "Integer32", "mib-2", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaRtProtoMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 84))
ianaRtProtoMIB.setRevisions(('2016-04-25 00:00', '2016-04-06 00:00', '2012-08-30 00:00', '2011-07-22 00:00', '2000-09-26 00:00',))
if mibBuilder.loadTexts: ianaRtProtoMIB.setLastUpdated('201604250000Z')
if mibBuilder.loadTexts: ianaRtProtoMIB.setOrganization('IANA')
class IANAipRouteProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("isIs", 9), ("esIs", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15), ("ciscoEigrp", 16), ("dvmrp", 17), ("rpl", 18), ("dhcp", 19), ("ttdp", 20))

class IANAipMRouteProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("dvmrp", 4), ("mospf", 5), ("pimSparseDense", 6), ("cbt", 7), ("pimSparseMode", 8), ("pimDenseMode", 9), ("igmpOnly", 10), ("bgmp", 11), ("msdp", 12))

mibBuilder.exportSymbols("IANA-RTPROTO-MIB", IANAipMRouteProtocol=IANAipMRouteProtocol, IANAipRouteProtocol=IANAipRouteProtocol, ianaRtProtoMIB=ianaRtProtoMIB, PYSNMP_MODULE_ID=ianaRtProtoMIB)
