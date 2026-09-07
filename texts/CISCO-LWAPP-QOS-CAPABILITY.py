#
# PySNMP MIB module CISCO-LWAPP-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LWAPP-QOS-CAPABILITY
# Source digest sha256:13b0b344acb400ed0b9488ee904573f3cb666b36e5b9a7f80fb04d1d79709044
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 505))
ciscoLwappQosCapability.setRevisions(('2006-05-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappQosCapability.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoLwappQosCapability.setLastUpdated('2006-05-15 00:00')
if mibBuilder.loadTexts: ciscoLwappQosCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappQosCapability.setContactInfo('             Cisco Systems\n                              Customer Service\n\n                      Postal: 170 W Tasman Drive\n                              San Jose, CA  95134\n                              USA\n  \n                         Tel: +1 800 553-NETS\n \n                      E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappQosCapability.setDescription('Agent capabilities for CISCO-LWAPP-QOS-MIB. ')
ciscoLwappQosCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 505, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosCapabilityCUWNSV4R0 = ciscoLwappQosCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosCapabilityCUWNSV4R0 = ciscoLwappQosCapabilityCUWNSV4R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappQosCapabilityCUWNSV4R0.setDescription('CISCO-LWAPP-QOS-MIB capabilities. ')
mibBuilder.exportSymbols("CISCO-LWAPP-QOS-CAPABILITY", PYSNMP_MODULE_ID=ciscoLwappQosCapability, ciscoLwappQosCapability=ciscoLwappQosCapability, ciscoLwappQosCapabilityCUWNSV4R0=ciscoLwappQosCapabilityCUWNSV4R0)
