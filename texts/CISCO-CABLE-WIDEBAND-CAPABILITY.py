#
# PySNMP MIB module CISCO-CABLE-WIDEBAND-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CABLE-WIDEBAND-CAPABILITY
# Source digest sha256:6484c9ac45ad217399c591f1568976494818614ca8db51fe9ed6d8ad9d68529f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TextualConvention")
ciscoCableWidebandCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 520))
ciscoCableWidebandCapability.setRevisions(('2010-06-09 00:00', '2006-09-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableWidebandCapability.setRevisionsDescriptions(('Add notInService status for ccwbRFChannelRowStatus', 'This is the Initial version',))
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setLastUpdated('2010-06-09 00:00')
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: Cisco Systems\n            170 West Tasman Drive\n            San Jose, CA 95134\n            U.S.A.\n            Phone:  +1 800 553-NETS\n            E-mail: cs-ubr@cisco.com')
if mibBuilder.loadTexts: ciscoCableWidebandCapability.setDescription('Agent capabilities for CISCO-CABLE-WIDEBAND-MIB')
ciscoCableWidebandCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 520, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV12R00 = ciscoCableWidebandCapabilityV12R00.setProductRelease('Cisco IOS 12.3BC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV12R00 = ciscoCableWidebandCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCableWidebandCapabilityV12R00.setDescription('Cisco Cable Wideband MIB capabilities.')
ciscoCableWidebandCapabilityV122R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 520, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV122R00 = ciscoCableWidebandCapabilityV122R00.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableWidebandCapabilityV122R00 = ciscoCableWidebandCapabilityV122R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCableWidebandCapabilityV122R00.setDescription('Cisco Cable Wideband MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CABLE-WIDEBAND-CAPABILITY", PYSNMP_MODULE_ID=ciscoCableWidebandCapability, ciscoCableWidebandCapability=ciscoCableWidebandCapability, ciscoCableWidebandCapabilityV122R00=ciscoCableWidebandCapabilityV122R00, ciscoCableWidebandCapabilityV12R00=ciscoCableWidebandCapabilityV12R00)
