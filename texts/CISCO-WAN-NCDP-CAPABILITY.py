#
# PySNMP MIB module CISCO-WAN-NCDP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-NCDP-CAPABILITY
# Source digest sha256:28f7924c64f580f531858236d7d897a668f9c8b60d258e92c6f9334856f2a114
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanNcdpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
if mibBuilder.loadTexts: ciscoWanNcdpCapability.setLastUpdated('2001-09-14 00:00')
if mibBuilder.loadTexts: ciscoWanNcdpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanNcdpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanNcdpCapability.setDescription('The Agent Capabilities for CISCO-WAN-NCDP-MIB.')
ciscoWanNcdpCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanNcdpCapabilityV3R00 = ciscoWanNcdpCapabilityV3R00.setProductRelease('MGX8850 Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanNcdpCapabilityV3R00 = ciscoWanNcdpCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanNcdpCapabilityV3R00.setDescription('NCDP MIB Capabilities.')
mibBuilder.exportSymbols("CISCO-WAN-NCDP-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanNcdpCapability, ciscoWanNcdpCapability=ciscoWanNcdpCapability, ciscoWanNcdpCapabilityV3R00=ciscoWanNcdpCapabilityV3R00)
