#
# PySNMP MIB module CISCO-ITP-SP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-SP-CAPABILITY
# Source digest sha256:84f8ac72ed8d280c58d236de75e27727650dd476cddb42e0b2c43c61027cecf5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpSpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 217))
ciscoItpSpCapability.setRevisions(('2002-01-21 00:00', '2001-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpSpCapability.setRevisionsDescriptions(('Updated capabilities MIB as required for \n                         new group.\n                         \n                         cItpSpStatsGroup', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpSpCapability.setLastUpdated('2002-01-21 00:00')
if mibBuilder.loadTexts: ciscoItpSpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpSpCapability.setContactInfo('       Cisco Systems\n                                Customer Service\n                        \n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                        \n                           Tel: +1 800 553-NETS\n                        \n                        E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpSpCapability.setDescription('Agent capabilities for the CISCO-ITP-SP-MIB.')
ciscoItpSpCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 217, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R024MB1 = ciscoItpSpCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R024MB1 = ciscoItpSpCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoItpSpCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-ITP-SP-MIB.my User Agent\n                     MIB capabilities.')
ciscoItpSpCapabilityV12R0204MB3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 217, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R0204MB3 = ciscoItpSpCapabilityV12R0204MB3.setProductRelease('Cisco IOS 12.2(4)MB3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSpCapabilityV12R0204MB3 = ciscoItpSpCapabilityV12R0204MB3.setStatus('current')
if mibBuilder.loadTexts: ciscoItpSpCapabilityV12R0204MB3.setDescription('IOS 12.2(4)MB3 Cisco CISCO-ITP-SP-MIB.my User \n                     Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-SP-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpSpCapability, ciscoItpSpCapability=ciscoItpSpCapability, ciscoItpSpCapabilityV12R0204MB3=ciscoItpSpCapabilityV12R0204MB3, ciscoItpSpCapabilityV12R024MB1=ciscoItpSpCapabilityV12R024MB1)
