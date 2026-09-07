#
# PySNMP MIB module CISCO-LWAPP-MFP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LWAPP-MFP-CAPABILITY
# Source digest sha256:1fdbf39c92f942980bcbf033839177b30d040af12a5f3a08229fa5600e291e10
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappMfpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 504))
ciscoLwappMfpCapability.setRevisions(('2006-05-16 00:00',))
if mibBuilder.loadTexts: ciscoLwappMfpCapability.setLastUpdated('2006-05-16 00:00')
if mibBuilder.loadTexts: ciscoLwappMfpCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappMfpCapabilityCUWNSV4R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 504, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpCapabilityCUWNSV4R0 = ciscoLwappMfpCapabilityCUWNSV4R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 4.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMfpCapabilityCUWNSV4R0 = ciscoLwappMfpCapabilityCUWNSV4R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-MFP-CAPABILITY", PYSNMP_MODULE_ID=ciscoLwappMfpCapability, ciscoLwappMfpCapability=ciscoLwappMfpCapability, ciscoLwappMfpCapabilityCUWNSV4R0=ciscoLwappMfpCapabilityCUWNSV4R0)
