#
# PySNMP MIB module CISCO-DISMAN-EVENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DISMAN-EVENT-CAPABILITY
# Source digest sha256:d689c051bffe9e551c772c6fd78846c0f97c9af70a49449fd41e9ecef4ef9180
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cdismanEventCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 473))
cdismanEventCapability.setRevisions(('2006-01-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cdismanEventCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cdismanEventCapability.setLastUpdated('2006-01-16 00:00')
if mibBuilder.loadTexts: cdismanEventCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cdismanEventCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com\n                        cs-snmp@cisco.com')
if mibBuilder.loadTexts: cdismanEventCapability.setDescription('The capabilities description of\n                 DISMAN-EVENT-MIB.')
cdismanEventCapabilityIOSXRV3R2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 473, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdismanEventCapabilityIOSXRV3R2R0CRS1 = cdismanEventCapabilityIOSXRV3R2R0CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdismanEventCapabilityIOSXRV3R2R0CRS1 = cdismanEventCapabilityIOSXRV3R2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: cdismanEventCapabilityIOSXRV3R2R0CRS1.setDescription('DISMAN-EVENT-MIB capabilities for\n                        IOS XR release 3.2.0')
mibBuilder.exportSymbols("CISCO-DISMAN-EVENT-CAPABILITY", PYSNMP_MODULE_ID=cdismanEventCapability, cdismanEventCapability=cdismanEventCapability, cdismanEventCapabilityIOSXRV3R2R0CRS1=cdismanEventCapabilityIOSXRV3R2R0CRS1)
