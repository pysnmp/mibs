#
# PySNMP MIB module ELTEX-MES (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltex/ELTEX-MES
# Produced by pysmi-1.1.12 at Thu Nov 28 02:57:17 2024
# On host fv-az885-149 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
elHardware, eltexLtd = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "elHardware", "eltexLtd")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, Unsigned32, ModuleIdentity, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, TimeTicks, MibIdentifier, Integer32, Gauge32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Gauge32", "Counter32", "Bits")
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
mibBuilder.exportSymbols("ELTEX-MES", eltMesPhdTransceiver=eltMesPhdTransceiver, eltMesAAA=eltMesAAA, eltMes=eltMes, eltMesDhcp=eltMesDhcp, eltMesDot1x=eltMesDot1x, eltMesMng=eltMesMng, eltMesMacMulticast=eltMesMacMulticast, eltMesCopy=eltMesCopy, eltMesSwInterfaces=eltMesSwInterfaces, eltMesPhy=eltMesPhy, Percents=Percents, eltMesRadius=eltMesRadius, eltMesDevParams=eltMesDevParams, eltMesQosCliMib=eltMesQosCliMib, eltMesEndOfMibGroup=eltMesEndOfMibGroup, eltMesSmon=eltMesSmon, eltMesLinkAgg=eltMesLinkAgg, eltMesIpOspfMtu=eltMesIpOspfMtu, eltMesIpUnnumbered=eltMesIpUnnumbered, NetNumber=NetNumber, eltMesBridgeSecurity=eltMesBridgeSecurity, eltMesHardwareMib=eltMesHardwareMib, eltMesIpSpec=eltMesIpSpec, eltMesQosTailDropMib=eltMesQosTailDropMib, eltMesIpBfd=eltMesIpBfd, eltMesTacacs=eltMesTacacs, PYSNMP_MODULE_ID=eltMes, eltMesNotifications=eltMesNotifications, eltMesSecuritySuiteMIB=eltMesSecuritySuiteMIB, eltMesIpMulticast=eltMesIpMulticast, eltMesSsh=eltMesSsh, eltMesStormCtrl=eltMesStormCtrl, eltMesTuning=eltMesTuning, VlanPriority=VlanPriority)
