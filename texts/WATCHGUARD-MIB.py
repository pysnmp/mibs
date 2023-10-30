#
# PySNMP MIB module WATCHGUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/WATCHGUARD-MIB
# Produced by pysmi-1.1.10 at Mon Oct 30 02:27:22 2023
# On host fv-az882-479 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, TimeTicks, IpAddress, Counter64, Bits, ObjectIdentity, iso, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, ModuleIdentity, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "TimeTicks", "IpAddress", "Counter64", "Bits", "ObjectIdentity", "iso", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "ModuleIdentity", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
watchguard = MibIdentifier((1, 3, 6, 1, 4, 1, 3097))
wgProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1))
fbXSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4))
fbX500 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 1))
fbX550e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 2))
fbX700 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 3))
fbX750e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 4))
fbX750e_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 5)).setLabel("fbX750e-4")
fbX1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 6))
fbX1250e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 7))
fbX1250e_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 8)).setLabel("fbX1250e-4")
fbX2500 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 9))
fbX5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 10))
fbX5500e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 11))
fbX6000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 12))
fbX6500e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 13))
fbX8000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 14))
fbX8500e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 15))
fbX8500e_F = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 16)).setLabel("fbX8500e-F")
mibBuilder.exportSymbols("WATCHGUARD-MIB", fbX500=fbX500, fbX8000=fbX8000, wgProducts=wgProducts, fbX6000=fbX6000, watchguard=watchguard, fbX5500e=fbX5500e, fbX2500=fbX2500, fbX1000=fbX1000, fbX750e=fbX750e, fbX750e_4=fbX750e_4, fbX5000=fbX5000, fbX8500e_F=fbX8500e_F, fbX550e=fbX550e, fbX6500e=fbX6500e, fbX700=fbX700, fbX1250e_4=fbX1250e_4, fbXSeries=fbXSeries, fbX8500e=fbX8500e, fbX1250e=fbX1250e)
