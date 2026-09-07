#
# PySNMP MIB module CISCO-LWAPP-SYS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LWAPP-SYS-CAPABILITY
# Source digest sha256:81ccecdd1038548f81d455b3081e97e776da86b30ae5965cec338c9d5ff09f47
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappSysCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 3333))
ciscoLwappSysCapability.setRevisions(('2010-08-17 00:00',))
if mibBuilder.loadTexts: ciscoLwappSysCapability.setLastUpdated('2010-08-17 00:00')
if mibBuilder.loadTexts: ciscoLwappSysCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappSysCapabilityCUWNSR7V0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 3333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V0 = ciscoLwappSysCapabilityCUWNSR7V0.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.0 for Cisco WLAN controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V0 = ciscoLwappSysCapabilityCUWNSR7V0.setStatus('current')
ciscoLwappSysCapabilityCUWNSR7V2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 3333, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V2 = ciscoLwappSysCapabilityCUWNSR7V2.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.2 for Cisco WLAN controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V2 = ciscoLwappSysCapabilityCUWNSR7V2.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-SYS-CAPABILITY", PYSNMP_MODULE_ID=ciscoLwappSysCapability, ciscoLwappSysCapability=ciscoLwappSysCapability, ciscoLwappSysCapabilityCUWNSR7V0=ciscoLwappSysCapabilityCUWNSR7V0, ciscoLwappSysCapabilityCUWNSR7V2=ciscoLwappSysCapabilityCUWNSR7V2)
