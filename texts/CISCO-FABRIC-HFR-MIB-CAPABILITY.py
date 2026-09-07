#
# PySNMP MIB module CISCO-FABRIC-HFR-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-FABRIC-HFR-MIB-CAPABILITY
# Source digest sha256:6f4dd18321811b4e224422ef0c60816158784746a5b55725e7d52b4998da5c35
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricHfrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 511))
ciscoFabricHfrCapability.setRevisions(('2006-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFabricHfrCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFabricHfrCapability.setLastUpdated('2006-06-12 00:00')
if mibBuilder.loadTexts: ciscoFabricHfrCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFabricHfrCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-fabric@cisco.com')
if mibBuilder.loadTexts: ciscoFabricHfrCapability.setDescription('The capabilities description of\n                 CISCO-FABRIC-HFR-MIB.')
cfhCapabilityIOSXRV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 511, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfhCapabilityIOSXRV3R03 = cfhCapabilityIOSXRV3R03.setProductRelease('Cisco IOS XR 3.3 on CRS-1 ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfhCapabilityIOSXRV3R03 = cfhCapabilityIOSXRV3R03.setStatus('current')
if mibBuilder.loadTexts: cfhCapabilityIOSXRV3R03.setDescription('CISCO-FABRIC-HFR-MIB\n                        capabilities for IOS XR release 3.3')
mibBuilder.exportSymbols("CISCO-FABRIC-HFR-MIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoFabricHfrCapability, cfhCapabilityIOSXRV3R03=cfhCapabilityIOSXRV3R03, ciscoFabricHfrCapability=ciscoFabricHfrCapability)
