#
# PySNMP MIB module CISCO-CASA-FA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CASA-FA-CAPABILITY
# Source digest sha256:7a4a29d2e552ae8426b9f50040df740abe4a9295ce7604ed9e061f8262879c82
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCasaFaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 135))
ciscoCasaFaCapability.setRevisions(('2000-12-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCasaFaCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCasaFaCapability.setLastUpdated('2000-12-01 00:00')
if mibBuilder.loadTexts: ciscoCasaFaCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCasaFaCapability.setContactInfo('       Cisco Systems\n                                Customer Service\n                        \n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                        \n                           Tel: +1 800 553-NETS\n                        \n                        E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCasaFaCapability.setDescription('Agent capabilities for the CASA-FA-MIB')
ciscoCasaFaCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 135, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasaFaCapabilityV12R01 = ciscoCasaFaCapabilityV12R01.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasaFaCapabilityV12R01 = ciscoCasaFaCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoCasaFaCapabilityV12R01.setDescription('IOS 12.1 Cisco Casa Forwarding Agent MIB capabilities')
mibBuilder.exportSymbols("CISCO-CASA-FA-CAPABILITY", PYSNMP_MODULE_ID=ciscoCasaFaCapability, ciscoCasaFaCapability=ciscoCasaFaCapability, ciscoCasaFaCapabilityV12R01=ciscoCasaFaCapabilityV12R01)
