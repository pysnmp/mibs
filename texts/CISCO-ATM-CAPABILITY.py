#
# PySNMP MIB module CISCO-ATM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-CAPABILITY
# Source digest sha256:7ff0a300d1be02fa37615f2ad82d220d496a9a10487af33c6e54c268c861e745
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoAtmCapability.setRevisions(('2002-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmCapability.setRevisionsDescriptions(('Initial Version of the MIB module.',))
if mibBuilder.loadTexts: ciscoAtmCapability.setLastUpdated('2002-06-12 00:00')
if mibBuilder.loadTexts: ciscoAtmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmCapability.setDescription('The Agent Capabilities for ATM-MIB.')
ciscoAtmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmCapabilityV2R00 = ciscoAtmCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                BPX SES Release 1.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmCapabilityV2R00 = ciscoAtmCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmCapabilityV2R00.setDescription('ATM MIB Capabilities')
mibBuilder.exportSymbols("CISCO-ATM-CAPABILITY", PYSNMP_MODULE_ID=ciscoAtmCapability, ciscoAtmCapability=ciscoAtmCapability, ciscoAtmCapabilityV2R00=ciscoAtmCapabilityV2R00)
