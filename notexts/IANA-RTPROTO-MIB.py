#
# PySNMP MIB module IANA-RTPROTO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IANA-RTPROTO-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 11:13:52 2024
# On host fv-az1493-704 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, TimeTicks, IpAddress, MibIdentifier, Counter64, Unsigned32, Gauge32, ModuleIdentity, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "TimeTicks", "IpAddress", "MibIdentifier", "Counter64", "Unsigned32", "Gauge32", "ModuleIdentity", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("IANA-RTPROTO-MIB", PYSNMP_MODULE_ID=ianaRtProtoMIB, IANAipRouteProtocol=IANAipRouteProtocol, ianaRtProtoMIB=ianaRtProtoMIB, IANAipMRouteProtocol=IANAipMRouteProtocol)
