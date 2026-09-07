#
# PySNMP MIB module CISCO-MEGACO-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MEGACO-EXT-CAPABILITY
# Source digest sha256:78f322eff76ecc16910fa9d5fc5bdb2363d82e34a018bb1dcbc6fb0e8f278ec2
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMegacoExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 376))
ciscoMegacoExtCapability.setRevisions(('2004-01-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMegacoExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMegacoExtCapability.setLastUpdated('2004-01-19 00:00')
if mibBuilder.loadTexts: ciscoMegacoExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMegacoExtCapability.setContactInfo('        Cisco Systems\n                 Customer Service\n        Postal: 170 W Tasman Drive\n                San Jose, CA 95134\n                USA\n           Tel: +1 800 553-NETS\n        E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoMegacoExtCapability.setDescription('The agent capabilities for CISCO-MEGACO-EXT-MIB.')
ciscoMegacoExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 376, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMegacoExtCapabilityV5R00 = ciscoMegacoExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMegacoExtCapabilityV5R00 = ciscoMegacoExtCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoMegacoExtCapabilityV5R00.setDescription('Megaco extension MIB capabilities for VXSM \n                 in release 5.0.0.')
mibBuilder.exportSymbols("CISCO-MEGACO-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoMegacoExtCapability, ciscoMegacoExtCapability=ciscoMegacoExtCapability, ciscoMegacoExtCapabilityV5R00=ciscoMegacoExtCapabilityV5R00)
