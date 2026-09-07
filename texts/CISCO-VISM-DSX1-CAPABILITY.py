#
# PySNMP MIB module CISCO-VISM-DSX1-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VISM-DSX1-CAPABILITY
# Source digest sha256:f2b3c2c65dbdf0d85ffc344d7c8c5c2bf6572d7ade8367a1ac093cfefaa20c94
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismDsx1Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 450))
ciscoVismDsx1Capability.setRevisions(('2005-09-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVismDsx1Capability.setRevisionsDescriptions(('Initial version of this capability file.',))
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setLastUpdated('2005-09-26 00:00')
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setDescription('Agent capabilities for \n                 CISCO-VISM-DSX1-MIB.')
cVismDsx1CapabilityV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 450, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismDsx1CapabilityV3325 = cVismDsx1CapabilityV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismDsx1CapabilityV3325 = cVismDsx1CapabilityV3325.setStatus('current')
if mibBuilder.loadTexts: cVismDsx1CapabilityV3325.setDescription('CISCO-VISM-DSX1-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VISM-DSX1-CAPABILITY", PYSNMP_MODULE_ID=ciscoVismDsx1Capability, cVismDsx1CapabilityV3325=cVismDsx1CapabilityV3325, ciscoVismDsx1Capability=ciscoVismDsx1Capability)
