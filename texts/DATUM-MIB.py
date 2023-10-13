#
# PySNMP MIB module DATUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/microsemi/DATUM-MIB
# Produced by pysmi-1.1.8 at Fri Oct 13 14:09:06 2023
# On host fv-az877-675 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, ObjectIdentity, iso, NotificationType, Gauge32, enterprises, Unsigned32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "ObjectIdentity", "iso", "NotificationType", "Gauge32", "enterprises", "Unsigned32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "IpAddress", "TimeTicks")
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
mibBuilder.exportSymbols("DATUM-MIB", timing=timing, bancomm=bancomm, products=products, austron=austron, fts=fts, experiment=experiment, datum=datum, ssu2000=ssu2000, ot21=ot21, efratom=efratom)
