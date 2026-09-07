#
# PySNMP MIB module CISCO-CAS-IF-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CAS-IF-EXT-CAPABILITY
# Source digest sha256:08ffa30cf2253659b37e090522223ee74cf1474932fc2e71e193bec023ceaa92
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCasIfExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 349))
ciscoCasIfExtCapability.setRevisions(('2004-01-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCasIfExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCasIfExtCapability.setLastUpdated('2004-01-19 00:00')
if mibBuilder.loadTexts: ciscoCasIfExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCasIfExtCapability.setContactInfo('        Cisco Systems\n                 Customer Service\n        Postal: 170 W Tasman Drive\n                San Jose, CA 95134\n                USA\n           Tel: +1 800 553-NETS\n        E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoCasIfExtCapability.setDescription('The agent capabilities for CISCO-CAS-IF-EXT-MIB.')
ciscoCasIfExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 349, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfExtCapabilityV5R00 = ciscoCasIfExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfExtCapabilityV5R00 = ciscoCasIfExtCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoCasIfExtCapabilityV5R00.setDescription('CISCO-CAS-IF-EXT-MIB capabilities for Voice \n                         Switch Service Module(VXSM) in \n                         Release 5.0.0.')
mibBuilder.exportSymbols("CISCO-CAS-IF-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoCasIfExtCapability, ciscoCasIfExtCapability=ciscoCasIfExtCapability, ciscoCasIfExtCapabilityV5R00=ciscoCasIfExtCapabilityV5R00)
