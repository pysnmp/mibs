#
# PySNMP MIB module IB-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-SMI-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:21:35 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter32, Counter64, Unsigned32, IpAddress, iso, Gauge32, MibIdentifier, enterprises, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "Counter64", "Unsigned32", "IpAddress", "iso", "Gauge32", "MibIdentifier", "enterprises", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
infoblox = ModuleIdentity((1, 3, 6, 1, 4, 1, 7779))
infoblox.setRevisions(('2008-01-14 00:00', '2005-01-10 00:00', '2004-05-21 00:00',))
if mibBuilder.loadTexts: infoblox.setLastUpdated('200911120000Z')
if mibBuilder.loadTexts: infoblox.setOrganization('Infoblox')
infobloxProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1))
ibDefault = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1000))
ibRsp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1001))
ibCisco = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1002))
ibVm = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1003))
ibVnios = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1004))
ib1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1101))
ib1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1102))
ib500 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1103))
ib550 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1201))
ib1050 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1202))
ib1550 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1203))
ib1552 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1204))
ib2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1205))
ib250 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1206))
ib1220 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1207))
ib550a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1301))
ib1050a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1302))
ib1550a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1303))
ib1552a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1304))
ib1852a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1305))
ib250a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1306))
ib2000a = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1307))
ib4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1420))
ib4010 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1421))
ib4020 = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 1, 1422))
ibSNMP = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3))
ibProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1))
ibOne = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1))
ibTrapOne = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 1))
ibPlatformOne = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 2))
ibDNSOne = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3))
ibDHCPOne = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4))
class IbString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class IbNode(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class IbIpAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class IbIpv6Addr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 46)

mibBuilder.exportSymbols("IB-SMI-MIB", ibProduct=ibProduct, ibTrapOne=ibTrapOne, ib500=ib500, ib1552a=ib1552a, ib1050=ib1050, ib250a=ib250a, ib1000=ib1000, ib1550a=ib1550a, infoblox=infoblox, ib1220=ib1220, ibVm=ibVm, ibDHCPOne=ibDHCPOne, ibOne=ibOne, ibRsp2=ibRsp2, ib1200=ib1200, ib2000=ib2000, ib250=ib250, ibDNSOne=ibDNSOne, PYSNMP_MODULE_ID=infoblox, ibDefault=ibDefault, ib550a=ib550a, IbNode=IbNode, ib1050a=ib1050a, ib4020=ib4020, ib550=ib550, infobloxProducts=infobloxProducts, ib1552=ib1552, IbString=IbString, ibPlatformOne=ibPlatformOne, IbIpAddr=IbIpAddr, ibCisco=ibCisco, ib4000=ib4000, ib1852a=ib1852a, ib2000a=ib2000a, ib1550=ib1550, ib4010=ib4010, ibVnios=ibVnios, ibSNMP=ibSNMP, IbIpv6Addr=IbIpv6Addr)
