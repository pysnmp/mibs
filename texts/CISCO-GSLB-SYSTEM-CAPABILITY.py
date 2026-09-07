#
# PySNMP MIB module CISCO-GSLB-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-GSLB-SYSTEM-CAPABILITY
# Source digest sha256:4846039933bcf69ae5cd1040bf5bcb72e4f4b1032decbd85cfbbb052ac8d57a4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGslbSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 534))
ciscoGslbSystemCapability.setRevisions(('2011-09-14 00:00', '2008-09-15 00:00', '2007-02-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGslbSystemCapability.setRevisionsDescriptions(('Added ciscoGslbSystemCapabilityV04R01 agent\n        capabilities for Global Site Selector(GSS)\n        release 4.1.0.', 'Added ciscoGslbSystemCapabilityV03R00 agent\n        capabilities for Global Site Selector(GSS)\n        release 3.0.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setLastUpdated('2011-09-14 00:00')
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal:  170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel:  +1 800 553-NETS\n\n            E-mail:  cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setDescription('The capabilities description\n        of CISCO-GSLB-SYSTEM-MIB.')
ciscoGslbSystemCapabilityV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV02R00 = ciscoGslbSystemCapabilityV02R00.setProductRelease('GSS 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV02R00 = ciscoGslbSystemCapabilityV02R00.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbSystemCapabilityV02R00.setDescription('GSS 2.0 Cisco GSLB SYSTEM MIB capabilities')
ciscoGslbSystemCapabilityV03R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV03R00 = ciscoGslbSystemCapabilityV03R00.setProductRelease('Global Site Selector(GSS) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV03R00 = ciscoGslbSystemCapabilityV03R00.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbSystemCapabilityV03R00.setDescription('GSS 3.0 Cisco GSLB SYSTEM MIB capabilities')
ciscoGslbSystemCapabilityV04R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV04R01 = ciscoGslbSystemCapabilityV04R01.setProductRelease('Global Site Selector(GSS) 4.1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV04R01 = ciscoGslbSystemCapabilityV04R01.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbSystemCapabilityV04R01.setDescription('GSS 4.1.0 Cisco GSLB SYSTEM MIB capabilities')
mibBuilder.exportSymbols("CISCO-GSLB-SYSTEM-CAPABILITY", PYSNMP_MODULE_ID=ciscoGslbSystemCapability, ciscoGslbSystemCapability=ciscoGslbSystemCapability, ciscoGslbSystemCapabilityV02R00=ciscoGslbSystemCapabilityV02R00, ciscoGslbSystemCapabilityV03R00=ciscoGslbSystemCapabilityV03R00, ciscoGslbSystemCapabilityV04R01=ciscoGslbSystemCapabilityV04R01)
