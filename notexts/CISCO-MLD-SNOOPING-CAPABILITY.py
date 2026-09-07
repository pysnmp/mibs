#
# PySNMP MIB module CISCO-MLD-SNOOPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MLD-SNOOPING-CAPABILITY
# Source digest sha256:8f38168bc1b936fb405a5eb7099e7d9f3aa9c96ece52acda27ae96a77fb751fb
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMldSnoopingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 586))
ciscoMldSnoopingCapability.setRevisions(('2010-03-02 00:00',))
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setLastUpdated('2010-03-02 00:00')
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setOrganization('Cisco Systems, Inc.')
ciscoMldSnoopingCapabilityV04R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 586, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMldSnoopingCapabilityV04R01 = ciscoMldSnoopingCapabilityV04R01.setProductRelease('Cisco IOS-XR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMldSnoopingCapabilityV04R01 = ciscoMldSnoopingCapabilityV04R01.setStatus('current')
mibBuilder.exportSymbols("CISCO-MLD-SNOOPING-CAPABILITY", PYSNMP_MODULE_ID=ciscoMldSnoopingCapability, ciscoMldSnoopingCapability=ciscoMldSnoopingCapability, ciscoMldSnoopingCapabilityV04R01=ciscoMldSnoopingCapabilityV04R01)
