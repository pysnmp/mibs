#
# PySNMP MIB module BKTEL-HFC862-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bktel/BKTEL-HFC862-BASE-MIB
# Produced by pysmi-1.1.8 at Wed Sep 13 14:22:40 2023
# On host fv-az612-215 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
iso, = mibBuilder.importSymbols("RFC1155-SMI", "iso")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, NotificationType, ModuleIdentity, Unsigned32, Bits, TimeTicks, experimental, ObjectIdentity, IpAddress, iso, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "NotificationType", "ModuleIdentity", "Unsigned32", "Bits", "TimeTicks", "experimental", "ObjectIdentity", "IpAddress", "iso", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class NESlotValue(Integer32):
    pass

class ModuleWidthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 8)

class PerceivedSeverityValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 5))
    namedValues = NamedValues(("notification", 0), ("alarm", 2), ("warning", 3), ("clear", 5))

org = MibIdentifier((1, 3))
dod = MibIdentifier((1, 3, 6))
internet = MibIdentifier((1, 3, 6, 1))
mgmt = MibIdentifier((1, 3, 6, 1, 2))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
bktelSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 7501))
hfc = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1))
ne = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 1))
modules = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 2))
mibBuilder.exportSymbols("BKTEL-HFC862-BASE-MIB", modules=modules, NESlotValue=NESlotValue, DisplayString=DisplayString, org=org, mgmt=mgmt, bktelSystems=bktelSystems, ne=ne, ModuleWidthValue=ModuleWidthValue, PerceivedSeverityValue=PerceivedSeverityValue, private=private, dod=dod, internet=internet, hfc=hfc, TruthValue=TruthValue, enterprises=enterprises)
