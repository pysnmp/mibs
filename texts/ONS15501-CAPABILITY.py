#
# PySNMP MIB module ONS15501-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source ONS15501-CAPABILITY
# Source digest sha256:29ae3ab09a6a81f46624b8c2bd8a6c4aeb5d6ffa58a37544b0d6a2b34b540923
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
synchronous, = mibBuilder.importSymbols("ONS15501-MIB", "synchronous")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ons15501MIBCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 1869, 15, 11))
ons15501MIBCapabilities.setRevisions(('2002-10-15 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ons15501MIBCapabilities.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ons15501MIBCapabilities.setLastUpdated('2002-10-15 18:00')
if mibBuilder.loadTexts: ons15501MIBCapabilities.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ons15501MIBCapabilities.setContactInfo('   Cisco Systems\n                Customer Service\n\n             Postal: 170 W Tasman Drive\n                     San Jose, CA 95134\n                     USA\n\n                Tel: +1 800 553-NETS\n\n             E-mail: cs-dwdm@cisco.com')
if mibBuilder.loadTexts: ons15501MIBCapabilities.setDescription('The MIB capability definition for ONS-15501 Optical \n         Amplifier.')
synEmbLxCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 15))
ons15501CapOld = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapOld = ons15501CapOld.setProductRelease('Release 3.0 of ONS15501 software.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapOld = ons15501CapOld.setStatus('current')
if mibBuilder.loadTexts: ons15501CapOld.setDescription('The agent capability for ONS15501 release 3.0.\n         The entity MIB is modeled as a single chassis\n         containing 2 ports (input /output) and a power\n         supply units. None of the parts are Field Replaceable\n         Units (FRU). \n         Main purpose of supporting the Entity MIB is for\n         proper notification correlation.')
ons15501CapDC = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapDC = ons15501CapDC.setProductRelease('DC series of ONS15501, Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapDC = ons15501CapDC.setStatus('current')
if mibBuilder.loadTexts: ons15501CapDC.setDescription('The agent capability for ONS15501 release 4.0\n         for DC series.\n         The entity MIB is modeled as a single chassis\n         containing 2 ports (input /output) and two power\n         supply units. None of the parts are FRU. \n         Main purpose of supporting the Entity MIB is for\n         proper notification correlation.')
ons15501CapAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapAC = ons15501CapAC.setProductRelease('AC series of ONS15501, Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapAC = ons15501CapAC.setStatus('current')
if mibBuilder.loadTexts: ons15501CapAC.setDescription('The agent capability for ONS15501 release 4.0\n         for AC series.\n         The entity MIB is modeled as a single chassis\n         containing 2 ports (input /output) and two power\n         supply units. None of the parts are FRU. \n         Main purpose of supporting the Entity MIB is for\n         proper notification correlation.')
mibBuilder.exportSymbols("ONS15501-CAPABILITY", PYSNMP_MODULE_ID=ons15501MIBCapabilities, ons15501CapAC=ons15501CapAC, ons15501CapDC=ons15501CapDC, ons15501CapOld=ons15501CapOld, ons15501MIBCapabilities=ons15501MIBCapabilities, synEmbLxCapability=synEmbLxCapability)
