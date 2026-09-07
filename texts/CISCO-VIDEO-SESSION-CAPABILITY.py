#
# PySNMP MIB module CISCO-VIDEO-SESSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VIDEO-SESSION-CAPABILITY
# Source digest sha256:31d58143cbf98e03eb8cd4c8e24e44f67fcbbaf64fe911447331d53dbb8b5263
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVideoSessionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 599))
ciscoVideoSessionCapability.setRevisions(('2011-05-24 00:00', '2010-11-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVideoSessionCapability.setRevisionsDescriptions(('Added ciscoVideoSessionCapabilityV152T02.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setLastUpdated('2011-05-24 00:00')
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-video@cisco.com')
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setDescription('Agent capabilities for CISCO-VIDEO-SESSION-MIB.')
ciscoVideoSessionCapabilityV15R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 599, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV15R01 = ciscoVideoSessionCapabilityV15R01.setProductRelease('OS=IOS\n                     OSVERSION=15.1\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV15R01 = ciscoVideoSessionCapabilityV15R01.setStatus('current')
if mibBuilder.loadTexts: ciscoVideoSessionCapabilityV15R01.setDescription('Cisco Video Session MIB capabilities.')
ciscoVideoSessionCapabilityV152T02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 599, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV152T02 = ciscoVideoSessionCapabilityV152T02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV152T02 = ciscoVideoSessionCapabilityV152T02.setStatus('current')
if mibBuilder.loadTexts: ciscoVideoSessionCapabilityV152T02.setDescription('Cisco Video Session MIB capabilities.\n        Some objects are not implemented due to DSP statistics reporting\n        capabilities.')
mibBuilder.exportSymbols("CISCO-VIDEO-SESSION-CAPABILITY", PYSNMP_MODULE_ID=ciscoVideoSessionCapability, ciscoVideoSessionCapability=ciscoVideoSessionCapability, ciscoVideoSessionCapabilityV152T02=ciscoVideoSessionCapabilityV152T02, ciscoVideoSessionCapabilityV15R01=ciscoVideoSessionCapabilityV15R01)
