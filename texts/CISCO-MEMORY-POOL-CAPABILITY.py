#
# PySNMP MIB module CISCO-MEMORY-POOL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MEMORY-POOL-CAPABILITY
# Source digest sha256:7a45db4c002c5cbde0c475704284eb063ca9d42cb1b94a48f1a933450ac739b4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMemoryPoolCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 338))
ciscoMemoryPoolCapability.setRevisions(('2006-05-02 00:00', '2005-10-26 00:00', '2003-08-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setRevisionsDescriptions(('Corrected existing Agent Capability\n                 for IOS XR release 2.0 CRS1', 'Added ciscoMemoryPoolCapabilityIOSXRV2R0CRS1\n        agent capabilities for IOS XR release 2.0 CRS1', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setLastUpdated('2006-05-02 00:00')
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com\n                        cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoMemoryPoolCapability.setDescription('The capabilities description of\n                 CISCO-MEMORY-POOL-MIB.')
ciscoMemoryPoolCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 338, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapCatOSV08R0101 = ciscoMemoryPoolCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapCatOSV08R0101 = ciscoMemoryPoolCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoMemoryPoolCapCatOSV08R0101.setDescription('CISCO-MEMORY-POOL-MIB capabilities.')
ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 338, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = ciscoMemoryPoolCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMemoryPoolCapabilityIOSXRV2R0CRS1 = ciscoMemoryPoolCapabilityIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoMemoryPoolCapabilityIOSXRV2R0CRS1.setDescription('CISCO-MEMORY-POOL-MIB capabilities for \n            IOS XR release 2.0')
mibBuilder.exportSymbols("CISCO-MEMORY-POOL-CAPABILITY", PYSNMP_MODULE_ID=ciscoMemoryPoolCapability, ciscoMemoryPoolCapCatOSV08R0101=ciscoMemoryPoolCapCatOSV08R0101, ciscoMemoryPoolCapability=ciscoMemoryPoolCapability, ciscoMemoryPoolCapabilityIOSXRV2R0CRS1=ciscoMemoryPoolCapabilityIOSXRV2R0CRS1)
