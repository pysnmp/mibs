#
# PySNMP MIB module CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY
# Source digest sha256:5ee187e79ab3980211b77e49274e37fc747268536a5d7c58ea46d2a2997a5b93
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpslaVideoProfileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 605))
ciscoIpslaVideoProfileCapability.setRevisions(('2011-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setLastUpdated('2011-06-01 00:00')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setDescription('Agent capabilities for CISCO-IPSLA-VIDEO-PROFILE-MIB')
ciscoIpslaVideoProfileCapabilityV152R02T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 605, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileCapabilityV152R02T = ciscoIpslaVideoProfileCapabilityV152R02T.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileCapabilityV152R02T = ciscoIpslaVideoProfileCapabilityV152R02T.setStatus('current')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapabilityV152R02T.setDescription('Cisco IPSLA Video Profile MIB Capabilities in 15.2(2)T Release')
mibBuilder.exportSymbols("CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpslaVideoProfileCapability, ciscoIpslaVideoProfileCapability=ciscoIpslaVideoProfileCapability, ciscoIpslaVideoProfileCapabilityV152R02T=ciscoIpslaVideoProfileCapabilityV152R02T)
