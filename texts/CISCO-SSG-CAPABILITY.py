#
# PySNMP MIB module CISCO-SSG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SSG-CAPABILITY
# Source digest sha256:f19eb9e4857c5089280ea6dff62c7148e4521e4c6671c4d76e74a12bfe229567
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSsgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 1500))
ciscoSsgCapability.setRevisions(('2004-08-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSsgCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSsgCapability.setLastUpdated('2004-08-13 00:00')
if mibBuilder.loadTexts: ciscoSsgCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSsgCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-ssg@cisco.com')
if mibBuilder.loadTexts: ciscoSsgCapability.setDescription('This is the Agent Capability MIB for\n                 CISCO-SSG-MIB.')
ciscoSsgCapabilityV12R03RevT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 1500, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSsgCapabilityV12R03RevT = ciscoSsgCapabilityV12R03RevT.setProductRelease('Cisco IOS 12.3T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSsgCapabilityV12R03RevT = ciscoSsgCapabilityV12R03RevT.setStatus('current')
if mibBuilder.loadTexts: ciscoSsgCapabilityV12R03RevT.setDescription('CISCO-SSG-MIB capabilities')
mibBuilder.exportSymbols("CISCO-SSG-CAPABILITY", PYSNMP_MODULE_ID=ciscoSsgCapability, ciscoSsgCapability=ciscoSsgCapability, ciscoSsgCapabilityV12R03RevT=ciscoSsgCapabilityV12R03RevT)
