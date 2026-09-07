#
# PySNMP MIB module CISCO-FLEX-LINKS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-FLEX-LINKS-CAPABILITY
# Source digest sha256:251d94bdf5d35b7f0cd155ccab64d5fe862eb526e1e41f3d2969b690ff3d6851
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoFlexLinksCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 444))
ciscoFlexLinksCapability.setRevisions(('2010-05-18 00:00', '2005-07-28 00:00', '2005-06-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFlexLinksCapability.setRevisionsDescriptions(('Added cFlexLinksCapV12R0254SGPCat4K.\n\n                 Updated cFlexLinksCapV12R0218SXFPCat6k with\n                 VARIATION clause of cflIfConfigStatus.', 'Added cFlexLinksCapV12R0218SXFPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setLastUpdated('2010-05-18 00:00')
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoFlexLinksCapability.setDescription('The capabilities description of CISCO-FLEX-LINKS-MIB.')
ciscoFlexLinksCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksCapCatOSV08R0501 = ciscoFlexLinksCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFlexLinksCapCatOSV08R0501 = ciscoFlexLinksCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoFlexLinksCapCatOSV08R0501.setDescription('CISCO-FLEX-LINKS-MIB capabilities.')
cFlexLinksCapV12R0218SXFPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0218SXFPCat6k = cFlexLinksCapV12R0218SXFPCat6k.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0218SXFPCat6k = cFlexLinksCapV12R0218SXFPCat6k.setStatus('current')
if mibBuilder.loadTexts: cFlexLinksCapV12R0218SXFPCat6k.setDescription('CISCO-FLEX-LINKS-MIB capabilities.')
cFlexLinksCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 444, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0254SGPCat4K = cFlexLinksCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cFlexLinksCapV12R0254SGPCat4K = cFlexLinksCapV12R0254SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cFlexLinksCapV12R0254SGPCat4K.setDescription('CISCO-FLEX-LINKS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-FLEX-LINKS-CAPABILITY", PYSNMP_MODULE_ID=ciscoFlexLinksCapability, cFlexLinksCapV12R0218SXFPCat6k=cFlexLinksCapV12R0218SXFPCat6k, cFlexLinksCapV12R0254SGPCat4K=cFlexLinksCapV12R0254SGPCat4K, ciscoFlexLinksCapCatOSV08R0501=ciscoFlexLinksCapCatOSV08R0501, ciscoFlexLinksCapability=ciscoFlexLinksCapability)
