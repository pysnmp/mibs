#
# PySNMP MIB module CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY
# Source digest sha256:b5327e53e510b532f2eb2a543c756d09a57d89761d31d57f123fe579ae697d21
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeInterval")
ciscoLwappClientRoamingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 501))
ciscoLwappClientRoamingCapability.setRevisions(('2010-02-06 00:00', '2006-05-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setRevisionsDescriptions(('Added ciscoLwappClientRoamingCapabilityCUWNSV7R0', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setLastUpdated('2010-02-06 00:00')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapability.setDescription('Agent capabilities for\n        CISCO-LWAPP-CLIENT-ROAMING-MIB.')
ciscoLwappClientRoamingCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 501, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV4R0 = ciscoLwappClientRoamingCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV4R0 = ciscoLwappClientRoamingCapabilityCUWNSV4R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapabilityCUWNSV4R0.setDescription('CISCO-LWAPP-CLIENT-ROAMING-MIB\n        capabilities.')
ciscoLwappClientRoamingCapabilityCUWNSV7R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 501, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV7R0 = ciscoLwappClientRoamingCapabilityCUWNSV7R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 7.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappClientRoamingCapabilityCUWNSV7R0 = ciscoLwappClientRoamingCapabilityCUWNSV7R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappClientRoamingCapabilityCUWNSV7R0.setDescription('CISCO-LWAPP-CLIENT-ROAMING-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-LWAPP-CLIENT-ROAMING-CAPABILITY", PYSNMP_MODULE_ID=ciscoLwappClientRoamingCapability, ciscoLwappClientRoamingCapability=ciscoLwappClientRoamingCapability, ciscoLwappClientRoamingCapabilityCUWNSV4R0=ciscoLwappClientRoamingCapabilityCUWNSV4R0, ciscoLwappClientRoamingCapabilityCUWNSV7R0=ciscoLwappClientRoamingCapabilityCUWNSV7R0)
