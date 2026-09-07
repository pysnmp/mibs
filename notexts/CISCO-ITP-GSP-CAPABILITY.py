#
# PySNMP MIB module CISCO-ITP-GSP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-GSP-CAPABILITY
# Source digest sha256:a5087988714e017106aa09ea2e4a1af45288ef948dee23aabd74212dd2e5cb95
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGspCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 306))
ciscoGspCapability.setRevisions(('2007-07-16 00:00', '2006-01-06 00:00', '2003-10-15 00:00', '2003-07-17 00:00',))
if mibBuilder.loadTexts: ciscoGspCapability.setLastUpdated('2007-07-16 00:00')
if mibBuilder.loadTexts: ciscoGspCapability.setOrganization('Cisco Systems, Inc.')
ciscoGspCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0204MB10 = ciscoGspCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0204MB10 = ciscoGspCapabilityV12R0204MB10.setStatus('current')
ciscoGspCapabilityV12R0219SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0219SW = ciscoGspCapabilityV12R0219SW.setProductRelease('Cisco IOS 12.2(19)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0219SW = ciscoGspCapabilityV12R0219SW.setStatus('current')
ciscoGspCapabilityV12R0225SW3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0225SW3 = ciscoGspCapabilityV12R0225SW3.setProductRelease('Cisco IOS 12.2(25)SW3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0225SW3 = ciscoGspCapabilityV12R0225SW3.setStatus('current')
ciscoGspCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0218IXA = ciscoGspCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0218IXA = ciscoGspCapabilityV12R0218IXA.setStatus('current')
ciscoGspCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0411SW = ciscoGspCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0411SW = ciscoGspCapabilityV12R0411SW.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-GSP-CAPABILITY", PYSNMP_MODULE_ID=ciscoGspCapability, ciscoGspCapability=ciscoGspCapability, ciscoGspCapabilityV12R0204MB10=ciscoGspCapabilityV12R0204MB10, ciscoGspCapabilityV12R0218IXA=ciscoGspCapabilityV12R0218IXA, ciscoGspCapabilityV12R0219SW=ciscoGspCapabilityV12R0219SW, ciscoGspCapabilityV12R0225SW3=ciscoGspCapabilityV12R0225SW3, ciscoGspCapabilityV12R0411SW=ciscoGspCapabilityV12R0411SW)
