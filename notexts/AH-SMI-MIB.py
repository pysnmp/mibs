#
# PySNMP MIB module AH-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-SMI-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 09:26:26 2024
# On host fv-az1146-179 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Gauge32, TimeTicks, Bits, iso, Counter64, enterprises, NotificationType, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Gauge32", "TimeTicks", "Bits", "iso", "Counter64", "enterprises", "NotificationType", "ObjectIdentity", "IpAddress")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("AH-SMI-MIB", AhMACProtocol=AhMACProtocol, AhString=AhString, ahAPInterface=ahAPInterface, ahAPIDP=ahAPIDP, ahAPMRP=ahAPMRP, ahAPCommon=ahAPCommon, PYSNMP_MODULE_ID=aerohive, ahProduct=ahProduct, ahAPHiveAP028_ag=ahAPHiveAP028_ag, ahAPHiveAP340_n=ahAPHiveAP340_n, AhInterfaceType=AhInterfaceType, ahAP=ahAP, AhInterfaceMode=AhInterfaceMode, AhNodeID=AhNodeID, ahAPHiveAP020_ag=ahAPHiveAP020_ag, ahAPHiveAP320_n=ahAPHiveAP320_n, aerohive=aerohive, ahAPTrap=ahAPTrap)
