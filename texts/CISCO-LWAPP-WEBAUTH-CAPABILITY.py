#
# PySNMP MIB module CISCO-LWAPP-WEBAUTH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LWAPP-WEBAUTH-CAPABILITY
# Source digest sha256:c14138e68f6509e94517fa7c0d0693a9a92ce8cb3bdde1acd771a2d3e9865e4b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappWebauthCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 5555))
ciscoLwappWebauthCapability.setRevisions(('2010-07-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setLastUpdated('2010-07-30 00:00')
if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setDescription('Agent capabilities for\n        CISCO-LWAPP-WEBAUTH-MIB.')
ciscoLwappWebAuthCapabilityCUWNSV7R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 5555, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWebAuthCapabilityCUWNSV7R0 = ciscoLwappWebAuthCapabilityCUWNSV7R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 7.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWebAuthCapabilityCUWNSV7R0 = ciscoLwappWebAuthCapabilityCUWNSV7R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappWebAuthCapabilityCUWNSV7R0.setDescription('CiscoLwappWebAuthMIB capabilities')
mibBuilder.exportSymbols("CISCO-LWAPP-WEBAUTH-CAPABILITY", PYSNMP_MODULE_ID=ciscoLwappWebauthCapability, ciscoLwappWebAuthCapabilityCUWNSV7R0=ciscoLwappWebAuthCapabilityCUWNSV7R0, ciscoLwappWebauthCapability=ciscoLwappWebauthCapability)
