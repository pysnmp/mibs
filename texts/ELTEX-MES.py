#
# PySNMP MIB module ELTEX-MES (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltex/ELTEX-MES
# Produced by pysmi-1.1.12 at Tue Dec  3 12:15:06 2024
# On host fv-az573-178 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
elHardware, eltexLtd = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "elHardware", "eltexLtd")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, Counter64, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, IpAddress, Integer32, ModuleIdentity, ObjectIdentity, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Counter64", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "IpAddress", "Integer32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMes = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23))
eltMes.setRevisions(('2015-11-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMes.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: eltMes.setLastUpdated('201511170000Z')
if mibBuilder.loadTexts: eltMes.setOrganization('Eltex Co')
if mibBuilder.loadTexts: eltMes.setContactInfo('eltex.nsk.ru')
if mibBuilder.loadTexts: eltMes.setDescription('Mib for Eltex MES ethernet switches.')
class Percents(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class NetNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class VlanPriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

eltMesNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0))
if mibBuilder.loadTexts: eltMesNotifications.setStatus('current')
if mibBuilder.loadTexts: eltMesNotifications.setDescription(" All the Eltex notifications will reside under this branch\n                         as specified in\n                         RFC2578 'Structure of Management Information Version 2 (SMIv2)' 8.5")
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
mibBuilder.exportSymbols("ELTEX-MES", eltMesCopy=eltMesCopy, eltMesIpOspfMtu=eltMesIpOspfMtu, NetNumber=NetNumber, eltMesNotifications=eltMesNotifications, eltMesHardwareMib=eltMesHardwareMib, eltMesIpSpec=eltMesIpSpec, eltMesAAA=eltMesAAA, eltMesQosCliMib=eltMesQosCliMib, eltMesMng=eltMesMng, VlanPriority=VlanPriority, eltMesBridgeSecurity=eltMesBridgeSecurity, eltMesMacMulticast=eltMesMacMulticast, eltMesIpBfd=eltMesIpBfd, eltMesLinkAgg=eltMesLinkAgg, eltMesPhy=eltMesPhy, eltMesIpUnnumbered=eltMesIpUnnumbered, eltMesIpMulticast=eltMesIpMulticast, eltMesEndOfMibGroup=eltMesEndOfMibGroup, eltMesTuning=eltMesTuning, eltMesRadius=eltMesRadius, Percents=Percents, eltMesPhdTransceiver=eltMesPhdTransceiver, eltMesSwInterfaces=eltMesSwInterfaces, PYSNMP_MODULE_ID=eltMes, eltMes=eltMes, eltMesTacacs=eltMesTacacs, eltMesQosTailDropMib=eltMesQosTailDropMib, eltMesDevParams=eltMesDevParams, eltMesSmon=eltMesSmon, eltMesDot1x=eltMesDot1x, eltMesStormCtrl=eltMesStormCtrl, eltMesSsh=eltMesSsh, eltMesSecuritySuiteMIB=eltMesSecuritySuiteMIB, eltMesDhcp=eltMesDhcp)
