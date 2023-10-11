#
# PySNMP MIB module ELTEX-MES (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltex/ELTEX-MES
# Produced by pysmi-1.1.8 at Wed Oct 11 08:30:50 2023
# On host fv-az791-264 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
eltexLtd, elHardware = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd", "elHardware")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, MibIdentifier, iso, Gauge32, NotificationType, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, IpAddress, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "MibIdentifier", "iso", "Gauge32", "NotificationType", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "IpAddress", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMes = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23))
eltMes.setRevisions(('2015-11-17 00:00',))
if mibBuilder.loadTexts: eltMes.setLastUpdated('201511170000Z')
if mibBuilder.loadTexts: eltMes.setOrganization('Eltex Co')
class Percents(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class NetNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class VlanPriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

eltMesNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0))
if mibBuilder.loadTexts: eltMesNotifications.setStatus('current')
eltMesMng = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1))
eltMesDevParams = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 2))
eltMesCopy = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 3))
eltMesIpOspfMtu = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4))
eltMesIpBfd = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 6))
eltMesIpUnnumbered = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 7))
eltMesDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8))
eltMesLinkAgg = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 9))
eltMesQosTailDropMib = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 12))
eltMesHardwareMib = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 14))
eltMesSsh = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 15))
eltMesSecuritySuiteMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 19))
eltMesTuning = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 29))
eltMesSwInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 43))
eltMesIpMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 46))
eltMesPhdTransceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 53))
eltMesMacMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 55))
eltMesStormCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 77))
eltMesAAA = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 79))
eltMesRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 80))
eltMesTacacs = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 81))
eltMesSmon = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84))
eltMesQosCliMib = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 88))
eltMesPhy = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 90))
eltMesIpSpec = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 91))
eltMesDot1x = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 95))
eltMesBridgeSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 112))
eltMesEndOfMibGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1000))
mibBuilder.exportSymbols("ELTEX-MES", eltMesRadius=eltMesRadius, NetNumber=NetNumber, eltMesSwInterfaces=eltMesSwInterfaces, eltMesBridgeSecurity=eltMesBridgeSecurity, Percents=Percents, eltMesIpMulticast=eltMesIpMulticast, eltMesIpBfd=eltMesIpBfd, eltMesPhdTransceiver=eltMesPhdTransceiver, eltMesMng=eltMesMng, eltMesIpOspfMtu=eltMesIpOspfMtu, PYSNMP_MODULE_ID=eltMes, eltMesSmon=eltMesSmon, eltMesPhy=eltMesPhy, eltMesSsh=eltMesSsh, VlanPriority=VlanPriority, eltMesEndOfMibGroup=eltMesEndOfMibGroup, eltMesStormCtrl=eltMesStormCtrl, eltMesLinkAgg=eltMesLinkAgg, eltMesIpUnnumbered=eltMesIpUnnumbered, eltMesTuning=eltMesTuning, eltMesQosCliMib=eltMesQosCliMib, eltMesMacMulticast=eltMesMacMulticast, eltMesNotifications=eltMesNotifications, eltMes=eltMes, eltMesSecuritySuiteMIB=eltMesSecuritySuiteMIB, eltMesQosTailDropMib=eltMesQosTailDropMib, eltMesDevParams=eltMesDevParams, eltMesHardwareMib=eltMesHardwareMib, eltMesIpSpec=eltMesIpSpec, eltMesCopy=eltMesCopy, eltMesDhcp=eltMesDhcp, eltMesAAA=eltMesAAA, eltMesTacacs=eltMesTacacs, eltMesDot1x=eltMesDot1x)
