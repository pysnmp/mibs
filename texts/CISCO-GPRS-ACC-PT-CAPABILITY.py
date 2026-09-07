#
# PySNMP MIB module CISCO-GPRS-ACC-PT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-GPRS-ACC-PT-CAPABILITY
# Source digest sha256:f247dc88595872318631b1a644b52b6baea9de8e1506de82ab8451827d8c3c20
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cgprsAccPtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 298))
cgprsAccPtCapability.setRevisions(('2003-04-08 17:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cgprsAccPtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cgprsAccPtCapability.setLastUpdated('2003-04-08 17:50')
if mibBuilder.loadTexts: cgprsAccPtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cgprsAccPtCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                                Tel: +1 800 553-NETS\n\n                        E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: cgprsAccPtCapability.setDescription('Agent capabilities for CISCO-GPRS-ACC-PT-MIB.')
cgprsAccPtCapabilityV12R2M4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 298, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M4 = cgprsAccPtCapabilityV12R2M4.setProductRelease('Cisco IOS 12.2(4)MX & 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M4 = cgprsAccPtCapabilityV12R2M4.setStatus('current')
if mibBuilder.loadTexts: cgprsAccPtCapabilityV12R2M4.setDescription('Cisco GPRS ACCESS POINT MIB capabilities.')
cgprsAccPtCapabilityV12R2M8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 298, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M8 = cgprsAccPtCapabilityV12R2M8.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M8 = cgprsAccPtCapabilityV12R2M8.setStatus('current')
if mibBuilder.loadTexts: cgprsAccPtCapabilityV12R2M8.setDescription('Cisco GPRS ACCESS POINT MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GPRS-ACC-PT-CAPABILITY", PYSNMP_MODULE_ID=cgprsAccPtCapability, cgprsAccPtCapability=cgprsAccPtCapability, cgprsAccPtCapabilityV12R2M4=cgprsAccPtCapabilityV12R2M4, cgprsAccPtCapabilityV12R2M8=cgprsAccPtCapabilityV12R2M8)
