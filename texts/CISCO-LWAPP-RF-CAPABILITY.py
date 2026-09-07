#
# PySNMP MIB module CISCO-LWAPP-RF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LWAPP-RF-CAPABILITY
# Source digest sha256:f978f68317144274aaf62341de5a9e186047735b3fa1440cfc37080038421285
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappRFCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 23999))
ciscoLwappRFCapability.setRevisions(('2012-02-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappRFCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappRFCapability.setLastUpdated('2012-02-28 00:00')
if mibBuilder.loadTexts: ciscoLwappRFCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappRFCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappRFCapability.setDescription('Agent capabilities for CISCO-LWAPP-RF-MIB.')
ciscoLwappRFCapabilityCUWNSV7R3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 23999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRFCapabilityCUWNSV7R3 = ciscoLwappRFCapabilityCUWNSV7R3.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.3 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappRFCapabilityCUWNSV7R3 = ciscoLwappRFCapabilityCUWNSV7R3.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappRFCapabilityCUWNSV7R3.setDescription('CISCO-LWAPP-RF-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-LWAPP-RF-CAPABILITY", PYSNMP_MODULE_ID=ciscoLwappRFCapability, ciscoLwappRFCapability=ciscoLwappRFCapability, ciscoLwappRFCapabilityCUWNSV7R3=ciscoLwappRFCapabilityCUWNSV7R3)
