#
# PySNMP MIB module BKTEL-HFC862-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bktel/BKTEL-HFC862-BASE-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 14:03:34 2024
# On host fv-az1456-954 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
iso, = mibBuilder.importSymbols("RFC1155-SMI", "iso")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, NotificationType, ModuleIdentity, Gauge32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, experimental, Counter32, Unsigned32, Integer32, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "NotificationType", "ModuleIdentity", "Gauge32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "experimental", "Counter32", "Unsigned32", "Integer32", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BKTEL-HFC862-BASE-MIB", NESlotValue=NESlotValue, mgmt=mgmt, internet=internet, hfc=hfc, org=org, enterprises=enterprises, TruthValue=TruthValue, ne=ne, private=private, bktelSystems=bktelSystems, modules=modules, dod=dod, ModuleWidthValue=ModuleWidthValue, PerceivedSeverityValue=PerceivedSeverityValue, DisplayString=DisplayString)
