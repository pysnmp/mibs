#
# PySNMP MIB module ELTEX-MES (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltex/ELTEX-MES
# Produced by pysmi-1.1.8 at Wed Jun 29 13:32:53 2022
# On host fv-az128-12 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
elHardware, eltexLtd = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "elHardware", "eltexLtd")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, Gauge32, NotificationType, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, MibIdentifier, ObjectIdentity, Unsigned32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Gauge32", "NotificationType", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ELTEX-MES", eltMesDevParams=eltMesDevParams, eltMesTacacs=eltMesTacacs, eltMesNotifications=eltMesNotifications, eltMesMacMulticast=eltMesMacMulticast, eltMesDhcp=eltMesDhcp, eltMesSecuritySuiteMIB=eltMesSecuritySuiteMIB, eltMesIpUnnumbered=eltMesIpUnnumbered, eltMesHardwareMib=eltMesHardwareMib, eltMesQosTailDropMib=eltMesQosTailDropMib, Percents=Percents, eltMesCopy=eltMesCopy, eltMesLinkAgg=eltMesLinkAgg, eltMesStormCtrl=eltMesStormCtrl, eltMesSmon=eltMesSmon, eltMesPhy=eltMesPhy, eltMesSwInterfaces=eltMesSwInterfaces, NetNumber=NetNumber, eltMesIpOspfMtu=eltMesIpOspfMtu, eltMesRadius=eltMesRadius, eltMesIpSpec=eltMesIpSpec, eltMesSsh=eltMesSsh, eltMesAAA=eltMesAAA, eltMesQosCliMib=eltMesQosCliMib, eltMesIpBfd=eltMesIpBfd, eltMesTuning=eltMesTuning, eltMesIpMulticast=eltMesIpMulticast, eltMesDot1x=eltMesDot1x, eltMesBridgeSecurity=eltMesBridgeSecurity, VlanPriority=VlanPriority, PYSNMP_MODULE_ID=eltMes, eltMesEndOfMibGroup=eltMesEndOfMibGroup, eltMesMng=eltMesMng, eltMesPhdTransceiver=eltMesPhdTransceiver, eltMes=eltMes)
