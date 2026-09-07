#
# PySNMP MIB module CISCO-XGCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-XGCP-CAPABILITY
# Source digest sha256:66edc4f9bda04a6b8a8cce94b637dafecc79d9ad2c4e89b4f9c5590f4bf3c34e
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
CCallControlProfileIndexOrZero, = mibBuilder.importSymbols("CISCO-MEDIA-GATEWAY-MIB", "CCallControlProfileIndexOrZero")
CMgcGroupIndexOrZero, = mibBuilder.importSymbols("CISCO-MGC-MIB", "CMgcGroupIndexOrZero")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoPort, = mibBuilder.importSymbols("CISCO-TC", "CiscoPort")
CXgcpRetryMethod, = mibBuilder.importSymbols("CISCO-XGCP-MIB", "CXgcpRetryMethod")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoXgcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 408))
ciscoXgcpCapability.setRevisions(('2006-03-01 00:00', '2006-02-14 00:00', '2005-06-24 00:00', '2005-01-06 00:00', '2004-10-04 00:00', '2004-06-16 00:00', '2002-12-31 00:00',))
if mibBuilder.loadTexts: ciscoXgcpCapability.setLastUpdated('2006-03-01 00:00')
if mibBuilder.loadTexts: ciscoXgcpCapability.setOrganization('Cisco Systems, Inc.')
ciscoXgcpCapabilityV4R010 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV4R010 = ciscoXgcpCapabilityV4R010.setProductRelease('MGX8850 Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV4R010 = ciscoXgcpCapabilityV4R010.setStatus('current')
ciscoXgcpCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03 = ciscoXgcpCapabilityV12R03.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03 = ciscoXgcpCapabilityV12R03.setStatus('deprecated')
ciscoXgcpCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R015 = ciscoXgcpCapabilityV5R015.setProductRelease('MGX8850 release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R015 = ciscoXgcpCapabilityV5R015.setStatus('current')
ciscoXgcpCapabilityV5R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R100 = ciscoXgcpCapabilityV5R100.setProductRelease('MGX8880 release 5.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R100 = ciscoXgcpCapabilityV5R100.setStatus('current')
ciscoXgcpCapabilityV5R300 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R300 = ciscoXgcpCapabilityV5R300.setProductRelease('MGX8880 release 5.3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV5R300 = ciscoXgcpCapabilityV5R300.setStatus('current')
ciscoXgcpCapabilityV12R03AS5000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03AS5000 = ciscoXgcpCapabilityV12R03AS5000.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R03AS5000 = ciscoXgcpCapabilityV12R03AS5000.setStatus('deprecated')
ciscoXgcpCapabilityV12R04AS5000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 408, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R04AS5000 = ciscoXgcpCapabilityV12R04AS5000.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpCapabilityV12R04AS5000 = ciscoXgcpCapabilityV12R04AS5000.setStatus('current')
mibBuilder.exportSymbols("CISCO-XGCP-CAPABILITY", PYSNMP_MODULE_ID=ciscoXgcpCapability, ciscoXgcpCapability=ciscoXgcpCapability, ciscoXgcpCapabilityV12R03=ciscoXgcpCapabilityV12R03, ciscoXgcpCapabilityV12R03AS5000=ciscoXgcpCapabilityV12R03AS5000, ciscoXgcpCapabilityV12R04AS5000=ciscoXgcpCapabilityV12R04AS5000, ciscoXgcpCapabilityV4R010=ciscoXgcpCapabilityV4R010, ciscoXgcpCapabilityV5R015=ciscoXgcpCapabilityV5R015, ciscoXgcpCapabilityV5R100=ciscoXgcpCapabilityV5R100, ciscoXgcpCapabilityV5R300=ciscoXgcpCapabilityV5R300)
