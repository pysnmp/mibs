#
# PySNMP MIB module WISI-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-ROOT-MIB
# Produced by pysmi-1.1.8 at Thu Jan 27 21:47:08 2022
# On host fv-az135-463 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, ModuleIdentity, IpAddress, NotificationType, MibIdentifier, Counter32, iso, Gauge32, Bits, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "ModuleIdentity", "IpAddress", "NotificationType", "MibIdentifier", "Counter32", "iso", "Gauge32", "Bits", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32")
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
mibBuilder.exportSymbols("WISI-ROOT-MIB", equipment=equipment, transponders=transponders, remultiplexer=remultiplexer, wisi=wisi, hfc=hfc, common=common, compact=compact, headend=headend, ioBoards=ioBoards, scrambler=scrambler, tangram=tangram, configuration=configuration, devices=devices)
