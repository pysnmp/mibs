#
# PySNMP MIB module BKTEL-HFC862-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bktel/BKTEL-HFC862-BASE-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 22:27:18 2022
# On host fv-az36-646 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
iso, = mibBuilder.importSymbols("RFC1155-SMI", "iso")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, Counter32, NotificationType, ObjectIdentity, MibIdentifier, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Unsigned32, Counter64, Bits, experimental = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter32", "NotificationType", "ObjectIdentity", "MibIdentifier", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Unsigned32", "Counter64", "Bits", "experimental")
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
mibBuilder.exportSymbols("BKTEL-HFC862-BASE-MIB", ModuleWidthValue=ModuleWidthValue, TruthValue=TruthValue, PerceivedSeverityValue=PerceivedSeverityValue, internet=internet, DisplayString=DisplayString, enterprises=enterprises, org=org, private=private, ne=ne, dod=dod, hfc=hfc, modules=modules, bktelSystems=bktelSystems, NESlotValue=NESlotValue, mgmt=mgmt)
