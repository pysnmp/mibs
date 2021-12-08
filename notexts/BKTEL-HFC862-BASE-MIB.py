#
# PySNMP MIB module BKTEL-HFC862-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bktel/BKTEL-HFC862-BASE-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:39:27 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
iso, = mibBuilder.importSymbols("RFC1155-SMI", "iso")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, experimental, Counter64, Unsigned32, ObjectIdentity, Gauge32, Counter32, Bits, iso, Integer32, MibIdentifier, NotificationType, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "experimental", "Counter64", "Unsigned32", "ObjectIdentity", "Gauge32", "Counter32", "Bits", "iso", "Integer32", "MibIdentifier", "NotificationType", "IpAddress", "TimeTicks")
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
mibBuilder.exportSymbols("BKTEL-HFC862-BASE-MIB", ModuleWidthValue=ModuleWidthValue, dod=dod, internet=internet, private=private, hfc=hfc, modules=modules, mgmt=mgmt, TruthValue=TruthValue, enterprises=enterprises, PerceivedSeverityValue=PerceivedSeverityValue, NESlotValue=NESlotValue, org=org, ne=ne, bktelSystems=bktelSystems, DisplayString=DisplayString)
