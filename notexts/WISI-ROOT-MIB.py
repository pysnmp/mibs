#
# PySNMP MIB module WISI-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-ROOT-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 11:38:49 2023
# On host fv-az280-773 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, TimeTicks, enterprises, Gauge32, Counter64, Counter32, Bits, MibIdentifier, ModuleIdentity, iso, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "TimeTicks", "enterprises", "Gauge32", "Counter64", "Counter32", "Bits", "MibIdentifier", "ModuleIdentity", "iso", "Unsigned32", "NotificationType")
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
mibBuilder.exportSymbols("WISI-ROOT-MIB", ioBoards=ioBoards, devices=devices, remultiplexer=remultiplexer, compact=compact, tangram=tangram, wisi=wisi, headend=headend, configuration=configuration, scrambler=scrambler, hfc=hfc, transponders=transponders, equipment=equipment, common=common)
