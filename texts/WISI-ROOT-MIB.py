#
# PySNMP MIB module WISI-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-ROOT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 05:00:22 2022
# On host fv-az83-73 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Counter32, Counter64, ObjectIdentity, ModuleIdentity, Unsigned32, Integer32, IpAddress, TimeTicks, Bits, NotificationType, MibIdentifier, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Counter32", "Counter64", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Integer32", "IpAddress", "TimeTicks", "Bits", "NotificationType", "MibIdentifier", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wisi = MibIdentifier((1, 3, 6, 1, 4, 1, 7465))
equipment = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 1))
devices = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2))
hfc = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 1))
transponders = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 2))
configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 3))
ioBoards = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 4))
compact = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 5))
headend = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 6))
scrambler = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 7))
remultiplexer = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 8))
tangram = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9))
mibBuilder.exportSymbols("WISI-ROOT-MIB", compact=compact, hfc=hfc, equipment=equipment, tangram=tangram, remultiplexer=remultiplexer, devices=devices, wisi=wisi, common=common, ioBoards=ioBoards, transponders=transponders, headend=headend, scrambler=scrambler, configuration=configuration)
