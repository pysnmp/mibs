#
# PySNMP MIB module DATUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/microsemi/DATUM-MIB
# Produced by pysmi-1.1.3 at Tue Nov 30 02:26:21 2021
# On host fv-az33-471 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, Counter32, NotificationType, MibIdentifier, Unsigned32, Gauge32, iso, Bits, ObjectIdentity, enterprises, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Counter32", "NotificationType", "MibIdentifier", "Unsigned32", "Gauge32", "iso", "Bits", "ObjectIdentity", "enterprises", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DATUM-MIB", austron=austron, fts=fts, bancomm=bancomm, products=products, efratom=efratom, ssu2000=ssu2000, experiment=experiment, timing=timing, datum=datum, ot21=ot21)
