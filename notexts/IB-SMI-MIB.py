#
# PySNMP MIB module IB-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-SMI-MIB
# Produced by pysmi-1.1.3 at Tue Nov 30 02:17:58 2021
# On host fv-az33-471 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, enterprises, ObjectIdentity, Integer32, iso, Counter32, Bits, Counter64, MibIdentifier, ModuleIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "enterprises", "ObjectIdentity", "Integer32", "iso", "Counter32", "Bits", "Counter64", "MibIdentifier", "ModuleIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
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

mibBuilder.exportSymbols("IB-SMI-MIB", ib1552a=ib1552a, IbString=IbString, infoblox=infoblox, ib1050a=ib1050a, ib500=ib500, ibSNMP=ibSNMP, IbIpAddr=IbIpAddr, ibTrapOne=ibTrapOne, ibPlatformOne=ibPlatformOne, infobloxProducts=infobloxProducts, ibProduct=ibProduct, ib4010=ib4010, ib250=ib250, ib2000=ib2000, ibDefault=ibDefault, ib1000=ib1000, ib2000a=ib2000a, ibDHCPOne=ibDHCPOne, ibRsp2=ibRsp2, ib1550=ib1550, ib1200=ib1200, ib1552=ib1552, ib1220=ib1220, ib550a=ib550a, ibCisco=ibCisco, ib1852a=ib1852a, ib1550a=ib1550a, ibVnios=ibVnios, ibDNSOne=ibDNSOne, PYSNMP_MODULE_ID=infoblox, ib4020=ib4020, ib250a=ib250a, ib550=ib550, ib4000=ib4000, ibOne=ibOne, IbIpv6Addr=IbIpv6Addr, IbNode=IbNode, ib1050=ib1050, ibVm=ibVm)
