#
# PySNMP MIB module CISCO-RFC1407-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-RFC1407-CAPABILITY
# Source digest sha256:0f08794b329bc5c6de52e0a0cfcae73b8bc16ef7a149797a6ae4a9cc019b1fa3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRFC1407Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 102))
ciscoRFC1407Capability.setRevisions(('2001-08-17 00:00', '1996-06-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRFC1407Capability.setRevisionsDescriptions(('Support SET operation for dsx3LoopbackConfig object.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRFC1407Capability.setLastUpdated('2001-08-17 00:00')
if mibBuilder.loadTexts: ciscoRFC1407Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRFC1407Capability.setContactInfo('\tCisco Systems\n\t\t\t\tCustomer Service\n\t\t\t\n\t\t\tPostal:\t170 West Tasman Drive\n\t\t\t\tSan Jose, CA  95134\n\t\t\t\tUSA\n\t\t\t\n\t\t\t   Tel:\t+1 800 553-NETS\n\t\t\t\n\t\t\tE-mail:\tcs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRFC1407Capability.setDescription('Agent capabilities for RFC1407-MIB (DS3 MIB)')
ciscoRFC1407CapabilityV11R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV11R02 = ciscoRFC1407CapabilityV11R02.setProductRelease('Cisco IOS 11.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV11R02 = ciscoRFC1407CapabilityV11R02.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1407CapabilityV11R02.setDescription('ds3 capabilities')
ciscoRFC1407CapabilityV122R12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 102, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV122R12 = ciscoRFC1407CapabilityV122R12.setProductRelease('Cisco IOS 12.2(12)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1407CapabilityV122R12 = ciscoRFC1407CapabilityV122R12.setStatus('current')
if mibBuilder.loadTexts: ciscoRFC1407CapabilityV122R12.setDescription('ds3 capabilities')
mibBuilder.exportSymbols("CISCO-RFC1407-CAPABILITY", PYSNMP_MODULE_ID=ciscoRFC1407Capability, ciscoRFC1407Capability=ciscoRFC1407Capability, ciscoRFC1407CapabilityV11R02=ciscoRFC1407CapabilityV11R02, ciscoRFC1407CapabilityV122R12=ciscoRFC1407CapabilityV122R12)
