#
# PySNMP MIB module CISCO-LWAPP-TSM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LWAPP-TSM-CAPABILITY
# Source digest sha256:07bdb03fdef5b09c05fe8ad4c891b4fd2522b0b0ee97429905b74ec6bbed5a60
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappTsmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 506))
ciscoLwappTsmCapability.setRevisions(('2006-05-15 00:00',))
if mibBuilder.loadTexts: ciscoLwappTsmCapability.setLastUpdated('2006-05-15 00:00')
if mibBuilder.loadTexts: ciscoLwappTsmCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappTsmCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 506, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappTsmCapabilityCUWNSV4R0 = ciscoLwappTsmCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappTsmCapabilityCUWNSV4R0 = ciscoLwappTsmCapabilityCUWNSV4R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-TSM-CAPABILITY", PYSNMP_MODULE_ID=ciscoLwappTsmCapability, ciscoLwappTsmCapability=ciscoLwappTsmCapability, ciscoLwappTsmCapabilityCUWNSV4R0=ciscoLwappTsmCapabilityCUWNSV4R0)
