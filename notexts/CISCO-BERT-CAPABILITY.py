#
# PySNMP MIB module CISCO-BERT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-BERT-CAPABILITY
# Source digest sha256:d5a0de63d1ae5b4d41015d11563be5783202a83803bec36a64f7e334e4f508f5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoBertCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 274))
ciscoBertCapability.setRevisions(('2004-08-07 00:00', '2003-12-22 00:00', '2003-09-19 00:00', '2002-10-30 00:00', '2002-06-11 00:00',))
if mibBuilder.loadTexts: ciscoBertCapability.setLastUpdated('2004-08-07 00:00')
if mibBuilder.loadTexts: ciscoBertCapability.setOrganization('Cisco Systems, Inc.')
ciscoBertAxsmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 274, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertAxsmeCapabilityV3R00 = ciscoBertAxsmeCapabilityV3R00.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertAxsmeCapabilityV3R00 = ciscoBertAxsmeCapabilityV3R00.setStatus('current')
ciscoBertCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 274, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R00 = ciscoBertCapabilityV5R00.setProductRelease('MGX8850 Release 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R00 = ciscoBertCapabilityV5R00.setStatus('current')
ciscoBertCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 274, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R015 = ciscoBertCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBertCapabilityV5R015 = ciscoBertCapabilityV5R015.setStatus('current')
mibBuilder.exportSymbols("CISCO-BERT-CAPABILITY", PYSNMP_MODULE_ID=ciscoBertCapability, ciscoBertAxsmeCapabilityV3R00=ciscoBertAxsmeCapabilityV3R00, ciscoBertCapability=ciscoBertCapability, ciscoBertCapabilityV5R00=ciscoBertCapabilityV5R00, ciscoBertCapabilityV5R015=ciscoBertCapabilityV5R015)
