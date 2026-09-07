#
# PySNMP MIB module CISCO-SVI-AUTOSTATE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SVI-AUTOSTATE-CAPABILITY
# Source digest sha256:f6005c10f24cbb6eea470d7048b2258da5d7165c38e993fc682ca2ba725f3399
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoSVIAutostateCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 384))
ciscoSVIAutostateCapability.setRevisions(('2004-04-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setLastUpdated('2004-04-08 00:00')
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSVIAutostateCapability.setDescription('The capabilities description of\n                 CISCO-SVI-AUTOSTATE-MIB.')
csaCapabilityCatOSV08R0301Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 384, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityCatOSV08R0301Cat6k = csaCapabilityCatOSV08R0301Cat6k.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityCatOSV08R0301Cat6k = csaCapabilityCatOSV08R0301Cat6k.setStatus('current')
if mibBuilder.loadTexts: csaCapabilityCatOSV08R0301Cat6k.setDescription('CISCO-SVI-AUTOSTATE-MIB capabilities.')
csaCapabilityV12R0218SXDCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 384, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityV12R0218SXDCat6k = csaCapabilityV12R0218SXDCat6k.setProductRelease('Cisco IOS 12.2(18)SXD on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaCapabilityV12R0218SXDCat6k = csaCapabilityV12R0218SXDCat6k.setStatus('current')
if mibBuilder.loadTexts: csaCapabilityV12R0218SXDCat6k.setDescription('CISCO-SVI-AUTOSTATE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SVI-AUTOSTATE-CAPABILITY", PYSNMP_MODULE_ID=ciscoSVIAutostateCapability, ciscoSVIAutostateCapability=ciscoSVIAutostateCapability, csaCapabilityCatOSV08R0301Cat6k=csaCapabilityCatOSV08R0301Cat6k, csaCapabilityV12R0218SXDCat6k=csaCapabilityV12R0218SXDCat6k)
