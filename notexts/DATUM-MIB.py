#
# PySNMP MIB module DATUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/microsemi/DATUM-MIB
# Produced by pysmi-1.1.12 at Wed May 29 08:04:35 2024
# On host fv-az1024-251 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, Integer32, ObjectIdentity, TimeTicks, Counter64, Counter32, Bits, Gauge32, Unsigned32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Integer32", "ObjectIdentity", "TimeTicks", "Counter64", "Counter32", "Bits", "Gauge32", "Unsigned32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
datum = MibIdentifier((1, 3, 6, 1, 4, 1, 601))
bancomm = MibIdentifier((1, 3, 6, 1, 4, 1, 601, 1))
timing = MibIdentifier((1, 3, 6, 1, 4, 1, 601, 2))
austron = MibIdentifier((1, 3, 6, 1, 4, 1, 601, 3))
fts = MibIdentifier((1, 3, 6, 1, 4, 1, 601, 4))
efratom = MibIdentifier((1, 3, 6, 1, 4, 1, 601, 5))
experiment = MibIdentifier((1, 3, 6, 1, 4, 1, 601, 99))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 601, 3, 1))
ssu2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 601, 3, 1, 1))
ot21 = MibIdentifier((1, 3, 6, 1, 4, 1, 601, 3, 1, 2))
mibBuilder.exportSymbols("DATUM-MIB", austron=austron, datum=datum, bancomm=bancomm, ssu2000=ssu2000, experiment=experiment, ot21=ot21, efratom=efratom, products=products, timing=timing, fts=fts)
