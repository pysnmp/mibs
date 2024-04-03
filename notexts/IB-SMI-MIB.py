#
# PySNMP MIB module IB-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-SMI-MIB
# Produced by pysmi-1.1.11 at Wed Apr  3 14:53:08 2024
# On host fv-az1198-695 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, NotificationType, MibIdentifier, TimeTicks, Gauge32, Counter64, Counter32, enterprises, Integer32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Gauge32", "Counter64", "Counter32", "enterprises", "Integer32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("IB-SMI-MIB", ib2000a=ib2000a, ib1220=ib1220, ib4000=ib4000, IbIpv6Addr=IbIpv6Addr, ibProduct=ibProduct, ib1050a=ib1050a, ib1852a=ib1852a, IbIpAddr=IbIpAddr, IbString=IbString, ib250=ib250, ib1550a=ib1550a, ib4020=ib4020, ib1200=ib1200, ibDNSOne=ibDNSOne, ibRsp2=ibRsp2, ib1552a=ib1552a, ib1550=ib1550, ib500=ib500, ib4010=ib4010, ibOne=ibOne, ibPlatformOne=ibPlatformOne, ib250a=ib250a, ib550a=ib550a, infoblox=infoblox, IbNode=IbNode, ibCisco=ibCisco, ib550=ib550, ib1000=ib1000, ibDefault=ibDefault, ibSNMP=ibSNMP, ib2000=ib2000, infobloxProducts=infobloxProducts, ib1552=ib1552, ibDHCPOne=ibDHCPOne, ibTrapOne=ibTrapOne, PYSNMP_MODULE_ID=infoblox, ib1050=ib1050, ibVm=ibVm, ibVnios=ibVnios)
