#
# PySNMP MIB module CISCO-VISM-SESSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VISM-SESSION-CAPABILITY
# Source digest sha256:fb2943b86642b5adc9e770da56878d635d932388ba254e8c46bcc510e9f11516
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismSessionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 415))
ciscoVismSessionCapability.setRevisions(('2005-09-19 00:00', '2004-09-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVismSessionCapability.setRevisionsDescriptions(('Added capabilities for VISM Release 3.3.25.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVismSessionCapability.setLastUpdated('2005-09-19 00:00')
if mibBuilder.loadTexts: ciscoVismSessionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVismSessionCapability.setContactInfo('        Cisco Systems\n                 Customer Service\n        Postal: 170 W Tasman Drive\n                San Jose, CA 95134\n                USA\n           Tel: +1 800 553-NETS\n        E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoVismSessionCapability.setDescription('This MIB defines the agent capabilities for \n         CISCO-VISM-SESSION-MIB.')
ciscoVismSessionCapV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 415, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV5R015 = ciscoVismSessionCapV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV5R015 = ciscoVismSessionCapV5R015.setStatus('current')
if mibBuilder.loadTexts: ciscoVismSessionCapV5R015.setDescription('Agent capabilities for Voice Switch \n                     Service Module (VXSM) in MGX8850\n                     release 5.0.15.')
ciscoVismSessionCapV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 415, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV3325 = ciscoVismSessionCapV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV3325 = ciscoVismSessionCapV3325.setStatus('current')
if mibBuilder.loadTexts: ciscoVismSessionCapV3325.setDescription('CISCO-VISM-SESSION-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VISM-SESSION-CAPABILITY", PYSNMP_MODULE_ID=ciscoVismSessionCapability, ciscoVismSessionCapV3325=ciscoVismSessionCapV3325, ciscoVismSessionCapV5R015=ciscoVismSessionCapV5R015, ciscoVismSessionCapability=ciscoVismSessionCapability)
