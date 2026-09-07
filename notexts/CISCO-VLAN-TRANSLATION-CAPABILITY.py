#
# PySNMP MIB module CISCO-VLAN-TRANSLATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VLAN-TRANSLATION-CAPABILITY
# Source digest sha256:a048cb2258dadeab02e40c242c2abfcf5d8aa528b40130751c296a17ff1beedf
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanTranslationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 405))
ciscoVlanTranslationCapability.setRevisions(('2012-01-09 00:00', '2006-02-08 00:00', '2004-08-11 00:00', '2004-06-07 00:00',))
if mibBuilder.loadTexts: ciscoVlanTranslationCapability.setLastUpdated('2012-01-09 00:00')
if mibBuilder.loadTexts: ciscoVlanTranslationCapability.setOrganization('Cisco Systems, Inc.')
cVlanTranslationCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTranslationCapCatOSV08R0401 = cVlanTranslationCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTranslationCapCatOSV08R0401 = cVlanTranslationCapCatOSV08R0401.setStatus('current')
cVlanTransCapV12R0218SXEPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV12R0218SXEPCat6K = cVlanTransCapV12R0218SXEPCat6K.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV12R0218SXEPCat6K = cVlanTransCapV12R0218SXEPCat6K.setStatus('current')
cVlanTransCapV15R0001SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV15R0001SYPCat6kSup2T = cVlanTransCapV15R0001SYPCat6kSup2T.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV15R0001SYPCat6kSup2T = cVlanTransCapV15R0001SYPCat6kSup2T.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-TRANSLATION-CAPABILITY", PYSNMP_MODULE_ID=ciscoVlanTranslationCapability, cVlanTransCapV12R0218SXEPCat6K=cVlanTransCapV12R0218SXEPCat6K, cVlanTransCapV15R0001SYPCat6kSup2T=cVlanTransCapV15R0001SYPCat6kSup2T, cVlanTranslationCapCatOSV08R0401=cVlanTranslationCapCatOSV08R0401, ciscoVlanTranslationCapability=ciscoVlanTranslationCapability)
