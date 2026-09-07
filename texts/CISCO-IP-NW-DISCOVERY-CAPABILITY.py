#
# PySNMP MIB module CISCO-IP-NW-DISCOVERY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IP-NW-DISCOVERY-CAPABILITY
# Source digest sha256:5d9aaeaab5539dcb066ffd86eb7684cf8d39a30e6ca420a6cf5f4a3ba62ad7da
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpNwDiscoveryCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 523))
ciscoIpNwDiscoveryCapability.setRevisions(('2006-11-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setLastUpdated('2006-11-07 00:00')
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIpNwDiscoveryCapability.setDescription('The capabilities description of\n        CISCO-IP-NW-DISCOVERY-MIB.')
cIpNwDiscoverCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 523, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpNwDiscoverCapSanOSV30R1MDS9000 = cIpNwDiscoverCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0 on Cisco MDS 9000                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpNwDiscoverCapSanOSV30R1MDS9000 = cIpNwDiscoverCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cIpNwDiscoverCapSanOSV30R1MDS9000.setDescription('Cisco IP NW Discovery MIB capabilities')
mibBuilder.exportSymbols("CISCO-IP-NW-DISCOVERY-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpNwDiscoveryCapability, cIpNwDiscoverCapSanOSV30R1MDS9000=cIpNwDiscoverCapSanOSV30R1MDS9000, ciscoIpNwDiscoveryCapability=ciscoIpNwDiscoveryCapability)
