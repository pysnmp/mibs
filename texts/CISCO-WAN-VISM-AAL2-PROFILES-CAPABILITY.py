#
# PySNMP MIB module CISCO-WAN-VISM-AAL2-PROFILES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-VISM-AAL2-PROFILES-CAPABILITY
# Source digest sha256:8512114e4a8d19d6972eb6d035178e0733d4bd6271f436b9381ee64f5e2254a7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismAal2ProfilesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 334))
ciscoWanVismAal2ProfilesCapability.setRevisions(('2000-12-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setLastUpdated('2000-12-18 00:00')
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapability.setDescription('The Agent Capabilities for CISCO-WAN-AAL2-PROFILES-MIB.')
ciscoWanVismAal2ProfilesCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 334, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismAal2ProfilesCapabilityV2R00 = ciscoWanVismAal2ProfilesCapabilityV2R00.setProductRelease('VISM Release2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismAal2ProfilesCapabilityV2R00 = ciscoWanVismAal2ProfilesCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismAal2ProfilesCapabilityV2R00.setDescription('CISCO-WAN-AAL2-PROFILES-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-AAL2-PROFILES-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanVismAal2ProfilesCapability, ciscoWanVismAal2ProfilesCapability=ciscoWanVismAal2ProfilesCapability, ciscoWanVismAal2ProfilesCapabilityV2R00=ciscoWanVismAal2ProfilesCapabilityV2R00)
