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
if mibBuilder.loadTexts: ons15501MIBCapabilities.setLastUpdated('2002-10-15 18:00')
if mibBuilder.loadTexts: ons15501MIBCapabilities.setOrganization('Cisco Systems, Inc.')
synEmbLxCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 15))
ons15501CapOld = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapOld = ons15501CapOld.setProductRelease('Release 3.0 of ONS15501 software.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapOld = ons15501CapOld.setStatus('current')
ons15501CapDC = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapDC = ons15501CapDC.setProductRelease('DC series of ONS15501, Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapDC = ons15501CapDC.setStatus('current')
ons15501CapAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapAC = ons15501CapAC.setProductRelease('AC series of ONS15501, Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapAC = ons15501CapAC.setStatus('current')
mibBuilder.exportSymbols("ONS15501-CAPABILITY", PYSNMP_MODULE_ID=ons15501MIBCapabilities, ons15501CapAC=ons15501CapAC, ons15501CapDC=ons15501CapDC, ons15501CapOld=ons15501CapOld, ons15501MIBCapabilities=ons15501MIBCapabilities, synEmbLxCapability=synEmbLxCapability)
