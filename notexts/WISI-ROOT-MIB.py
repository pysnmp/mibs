#
# PySNMP MIB module WISI-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-ROOT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:31:10 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, TimeTicks, ModuleIdentity, enterprises, Integer32, Counter64, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Unsigned32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "TimeTicks", "ModuleIdentity", "enterprises", "Integer32", "Counter64", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Unsigned32", "NotificationType", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("WISI-ROOT-MIB", transponders=transponders, compact=compact, hfc=hfc, scrambler=scrambler, wisi=wisi, equipment=equipment, common=common, headend=headend, devices=devices, remultiplexer=remultiplexer, ioBoards=ioBoards, tangram=tangram, configuration=configuration)
