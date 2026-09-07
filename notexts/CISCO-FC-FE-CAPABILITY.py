#
# PySNMP MIB module CISCO-FC-FE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-FC-FE-CAPABILITY
# Source digest sha256:d6d1f9d4fd920e5349304ff5b2499b98443a173128782cdb3f60708692d35610
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoMilliSeconds, = mibBuilder.importSymbols("CISCO-TC", "CiscoMilliSeconds")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFcFeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 627))
ciscoFcFeCapability.setRevisions(('2015-06-23 00:00', '2005-05-24 00:00',))
if mibBuilder.loadTexts: ciscoFcFeCapability.setLastUpdated('2015-06-23 00:00')
if mibBuilder.loadTexts: ciscoFcFeCapability.setOrganization('Cisco Systems, Inc.')
ciscoFcFeCapabilityMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 627, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityMDS3R0 = ciscoFcFeCapabilityMDS3R0.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityMDS3R0 = ciscoFcFeCapabilityMDS3R0.setStatus('current')
ciscoFcFeCapabilityV06R0213PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 627, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityV06R0213PMds = ciscoFcFeCapabilityV06R0213PMds.setProductRelease('Cisco NX-OS 6.2(13) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcFeCapabilityV06R0213PMds = ciscoFcFeCapabilityV06R0213PMds.setStatus('current')
mibBuilder.exportSymbols("CISCO-FC-FE-CAPABILITY", PYSNMP_MODULE_ID=ciscoFcFeCapability, ciscoFcFeCapability=ciscoFcFeCapability, ciscoFcFeCapabilityMDS3R0=ciscoFcFeCapabilityMDS3R0, ciscoFcFeCapabilityV06R0213PMds=ciscoFcFeCapabilityV06R0213PMds)
