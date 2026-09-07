#
# PySNMP MIB module CISCO-POP-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-POP-MGMT-CAPABILITY
# Source digest sha256:59db0430d26beee0ab8107720cd694cc90e72d062d007f1a84fd40b1b3852832
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPopMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 447))
ciscoPopMgmtCapability.setRevisions(('2005-10-12 00:00', '2005-08-25 00:00',))
if mibBuilder.loadTexts: ciscoPopMgmtCapability.setLastUpdated('2005-10-12 00:00')
if mibBuilder.loadTexts: ciscoPopMgmtCapability.setOrganization('Cisco Systems, Inc.')
ciscoPopMgmtCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 447, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPopMgmtCapabilityV12R04 = ciscoPopMgmtCapabilityV12R04.setProductRelease('Cisco IOS 12.4 for C3600 family platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPopMgmtCapabilityV12R04 = ciscoPopMgmtCapabilityV12R04.setStatus('current')
mibBuilder.exportSymbols("CISCO-POP-MGMT-CAPABILITY", PYSNMP_MODULE_ID=ciscoPopMgmtCapability, ciscoPopMgmtCapability=ciscoPopMgmtCapability, ciscoPopMgmtCapabilityV12R04=ciscoPopMgmtCapabilityV12R04)
