#
# PySNMP MIB module CISCO-SRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SRP-CAPABILITY
# Source digest sha256:3a50dfb91486939de333096fe8cf3011c60dbb5b34a63bc626d67f9837483ac5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSrpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
if mibBuilder.loadTexts: ciscoSrpCapability.setLastUpdated('2000-05-26 00:00')
if mibBuilder.loadTexts: ciscoSrpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSrpCapability.setContactInfo('       Cisco Systems\n                                 Customer Service\n\n                         Postal: 170 West Tasman Drive\n                                 San Jose, CA  95134\n                                 USA\n\n                            Tel: +1 800 553-NETS\n\n                         E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSrpCapability.setDescription('Initial version of this MIB module.')
ciscoSrpCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSrpCapabilityV12R00 = ciscoSrpCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSrpCapabilityV12R00 = ciscoSrpCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSrpCapabilityV12R00.setDescription('CISCO-SRP-MIB agent capabilities')
mibBuilder.exportSymbols("CISCO-SRP-CAPABILITY", PYSNMP_MODULE_ID=ciscoSrpCapability, ciscoSrpCapability=ciscoSrpCapability, ciscoSrpCapabilityV12R00=ciscoSrpCapabilityV12R00)
