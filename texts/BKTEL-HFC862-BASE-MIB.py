#
# PySNMP MIB module BKTEL-HFC862-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bktel/BKTEL-HFC862-BASE-MIB
# Produced by pysmi-1.1.8 at Tue Jan 18 13:38:46 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
iso, = mibBuilder.importSymbols("RFC1155-SMI", "iso")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, TimeTicks, Bits, ModuleIdentity, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, experimental, Counter64, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Bits", "ModuleIdentity", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "experimental", "Counter64", "NotificationType", "Counter32")
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
mibBuilder.exportSymbols("BKTEL-HFC862-BASE-MIB", internet=internet, private=private, TruthValue=TruthValue, DisplayString=DisplayString, org=org, bktelSystems=bktelSystems, ne=ne, hfc=hfc, modules=modules, PerceivedSeverityValue=PerceivedSeverityValue, ModuleWidthValue=ModuleWidthValue, mgmt=mgmt, enterprises=enterprises, NESlotValue=NESlotValue, dod=dod)
