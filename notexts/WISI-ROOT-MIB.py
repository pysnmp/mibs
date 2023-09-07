#
# PySNMP MIB module WISI-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-ROOT-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 09:26:05 2023
# On host fv-az1234-541 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.12 (main, Jun  7 2023, 13:43:11) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Counter32, Unsigned32, iso, ModuleIdentity, TimeTicks, IpAddress, Bits, Integer32, Gauge32, NotificationType, enterprises, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Counter32", "Unsigned32", "iso", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "Integer32", "Gauge32", "NotificationType", "enterprises", "Counter64")
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
mibBuilder.exportSymbols("WISI-ROOT-MIB", hfc=hfc, configuration=configuration, equipment=equipment, compact=compact, ioBoards=ioBoards, common=common, headend=headend, devices=devices, tangram=tangram, remultiplexer=remultiplexer, transponders=transponders, scrambler=scrambler, wisi=wisi)
