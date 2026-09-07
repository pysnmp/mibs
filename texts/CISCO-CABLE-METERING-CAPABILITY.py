#
# PySNMP MIB module CISCO-CABLE-METERING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CABLE-METERING-CAPABILITY
# Source digest sha256:8da19fa48ba28ebf1b2a80f034bad67bee6242798abb49f3de257772e4ea6f21
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCableMeteringCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 582))
ciscoCableMeteringCapability.setRevisions(('2009-06-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableMeteringCapability.setRevisionsDescriptions(('Initial version of this MIB Module.',))
if mibBuilder.loadTexts: ciscoCableMeteringCapability.setLastUpdated('2009-06-16 00:00')
if mibBuilder.loadTexts: ciscoCableMeteringCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCableMeteringCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ubr@cisco.com')
if mibBuilder.loadTexts: ciscoCableMeteringCapability.setDescription('Agent capabilities for CISCO-CABLE-METERING-MIB')
ciscoCableMeteringCapabilityV122R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 582, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableMeteringCapabilityV122R01 = ciscoCableMeteringCapabilityV122R01.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableMeteringCapabilityV122R01 = ciscoCableMeteringCapabilityV122R01.setStatus('current')
if mibBuilder.loadTexts: ciscoCableMeteringCapabilityV122R01.setDescription('Cisco Cable Metering MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CABLE-METERING-CAPABILITY", PYSNMP_MODULE_ID=ciscoCableMeteringCapability, ciscoCableMeteringCapability=ciscoCableMeteringCapability, ciscoCableMeteringCapabilityV122R01=ciscoCableMeteringCapabilityV122R01)
