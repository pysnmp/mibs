#
# PySNMP MIB module AH-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-SMI-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 18:18:10 2022
# On host fv-az83-345 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ObjectIdentity, enterprises, Unsigned32, MibIdentifier, iso, Gauge32, Bits, Counter32, NotificationType, TimeTicks, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "enterprises", "Unsigned32", "MibIdentifier", "iso", "Gauge32", "Bits", "Counter32", "NotificationType", "TimeTicks", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
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

mibBuilder.exportSymbols("AH-SMI-MIB", ahAPHiveAP340_n=ahAPHiveAP340_n, AhMACProtocol=AhMACProtocol, ahProduct=ahProduct, AhInterfaceMode=AhInterfaceMode, ahAPHiveAP320_n=ahAPHiveAP320_n, ahAPIDP=ahAPIDP, ahAP=ahAP, aerohive=aerohive, ahAPHiveAP020_ag=ahAPHiveAP020_ag, AhString=AhString, ahAPInterface=ahAPInterface, ahAPHiveAP028_ag=ahAPHiveAP028_ag, ahAPMRP=ahAPMRP, ahAPTrap=ahAPTrap, AhNodeID=AhNodeID, ahAPCommon=ahAPCommon, AhInterfaceType=AhInterfaceType, PYSNMP_MODULE_ID=aerohive)
