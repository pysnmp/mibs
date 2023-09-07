#
# PySNMP MIB module AH-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-SMI-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:07:38 2023
# On host fv-az548-537 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Bits, Counter64, Unsigned32, IpAddress, enterprises, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, iso, Counter32, NotificationType, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "Counter64", "Unsigned32", "IpAddress", "enterprises", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "iso", "Counter32", "NotificationType", "Integer32", "TimeTicks")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
aerohive = ModuleIdentity((1, 3, 6, 1, 4, 1, 26928))
if mibBuilder.loadTexts: aerohive.setLastUpdated('201608310000Z')
if mibBuilder.loadTexts: aerohive.setOrganization('Aerohive Networks, Inc')
ahProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1))
ahAP = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1))
ahAPCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1))
ahAPTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1))
ahAPInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2))
ahAPMRP = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3))
ahAPIDP = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 4))
ahAPHiveAP020_ag = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 2)).setLabel("ahAPHiveAP020-ag")
ahAPHiveAP028_ag = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 3)).setLabel("ahAPHiveAP028-ag")
ahAPHiveAP320_n = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 4)).setLabel("ahAPHiveAP320-n")
ahAPHiveAP340_n = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 5)).setLabel("ahAPHiveAP340-n")
class AhString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class AhNodeID(MacAddress):
    status = 'current'

class AhInterfaceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ahPHYSICAL", 0), ("ahVIRTURAL", 1))

class AhInterfaceMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ahNotUsed", 0), ("ahAccess", 1), ("ahBackhaul", 2), ("ahBridge", 3))

class AhMACProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("ah11a", 0), ("ah11b", 1), ("ah11g", 2), ("ah11na", 3), ("ah11ng", 4))

mibBuilder.exportSymbols("AH-SMI-MIB", PYSNMP_MODULE_ID=aerohive, AhString=AhString, ahAPHiveAP340_n=ahAPHiveAP340_n, ahAPHiveAP028_ag=ahAPHiveAP028_ag, ahAPTrap=ahAPTrap, ahAP=ahAP, AhNodeID=AhNodeID, ahAPHiveAP320_n=ahAPHiveAP320_n, ahAPInterface=ahAPInterface, AhInterfaceType=AhInterfaceType, AhInterfaceMode=AhInterfaceMode, ahProduct=ahProduct, ahAPIDP=ahAPIDP, AhMACProtocol=AhMACProtocol, ahAPHiveAP020_ag=ahAPHiveAP020_ag, aerohive=aerohive, ahAPCommon=ahAPCommon, ahAPMRP=ahAPMRP)
