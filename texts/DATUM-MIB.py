#
# PySNMP MIB module DATUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/microsemi/DATUM-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:28:38 2023
# On host fv-az448-504 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Gauge32, ModuleIdentity, Counter32, MibIdentifier, ObjectIdentity, iso, Counter64, Unsigned32, NotificationType, IpAddress, TimeTicks, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Gauge32", "ModuleIdentity", "Counter32", "MibIdentifier", "ObjectIdentity", "iso", "Counter64", "Unsigned32", "NotificationType", "IpAddress", "TimeTicks", "Integer32", "Bits")
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
mibBuilder.exportSymbols("DATUM-MIB", datum=datum, bancomm=bancomm, ot21=ot21, products=products, efratom=efratom, timing=timing, experiment=experiment, fts=fts, ssu2000=ssu2000, austron=austron)
