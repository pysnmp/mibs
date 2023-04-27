#
# PySNMP MIB module WATCHGUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/WATCHGUARD-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 10:09:12 2023
# On host fv-az338-106 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Unsigned32, Counter32, enterprises, NotificationType, Gauge32, Counter64, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Unsigned32", "Counter32", "enterprises", "NotificationType", "Gauge32", "Counter64", "TimeTicks", "Bits")
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
mibBuilder.exportSymbols("WATCHGUARD-MIB", fbX550e=fbX550e, fbX8500e=fbX8500e, fbX700=fbX700, fbX500=fbX500, fbX6000=fbX6000, fbX5500e=fbX5500e, watchguard=watchguard, fbX8000=fbX8000, fbX5000=fbX5000, fbX1250e=fbX1250e, wgProducts=wgProducts, fbX1250e_4=fbX1250e_4, fbX8500e_F=fbX8500e_F, fbX1000=fbX1000, fbX750e=fbX750e, fbX6500e=fbX6500e, fbX2500=fbX2500, fbXSeries=fbXSeries, fbX750e_4=fbX750e_4)
