#
# PySNMP MIB module CISCO-ITP-GSCCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-GSCCP-CAPABILITY
# Source digest sha256:10354fa53b023abd53cc57d01a810c2d7bc2d8960fbf18fa6446fa187ea03e0b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGsccpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 539))
ciscoGsccpCapability.setRevisions(('2007-05-17 00:00', '2005-01-14 00:00', '2004-10-07 00:00', '2003-12-08 00:00', '2003-10-28 00:00', '2003-05-20 00:00',))
if mibBuilder.loadTexts: ciscoGsccpCapability.setLastUpdated('2007-05-17 00:00')
if mibBuilder.loadTexts: ciscoGsccpCapability.setOrganization('Cisco Systems, Inc.')
ciscoGsccpCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB10 = ciscoGsccpCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB10 = ciscoGsccpCapabilityV12R0204MB10.setStatus('current')
ciscoGsccpCapabilityV12R0204MB13 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB13 = ciscoGsccpCapabilityV12R0204MB13.setProductRelease('Cisco IOS 12.2(4)MB13')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB13 = ciscoGsccpCapabilityV12R0204MB13.setStatus('current')
ciscoGsccpCapabilityV12R022004SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R022004SW = ciscoGsccpCapabilityV12R022004SW.setProductRelease('Cisco IOS 12.2(20.4)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R022004SW = ciscoGsccpCapabilityV12R022004SW.setStatus('current')
ciscoGsccpCapabilityV12R023000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R023000SW1 = ciscoGsccpCapabilityV12R023000SW1.setProductRelease('Cisco IOS 12.2(23)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R023000SW1 = ciscoGsccpCapabilityV12R023000SW1.setStatus('current')
ciscoGsccpCapabilityV12R025000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R025000SW1 = ciscoGsccpCapabilityV12R025000SW1.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R025000SW1 = ciscoGsccpCapabilityV12R025000SW1.setStatus('current')
ciscoGsccpCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0218IXA = ciscoGsccpCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0218IXA = ciscoGsccpCapabilityV12R0218IXA.setStatus('current')
ciscoGsccpCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0411SW = ciscoGsccpCapabilityV12R0411SW.setProductRelease('Cisco IOS IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0411SW = ciscoGsccpCapabilityV12R0411SW.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-GSCCP-CAPABILITY", PYSNMP_MODULE_ID=ciscoGsccpCapability, ciscoGsccpCapability=ciscoGsccpCapability, ciscoGsccpCapabilityV12R0204MB10=ciscoGsccpCapabilityV12R0204MB10, ciscoGsccpCapabilityV12R0204MB13=ciscoGsccpCapabilityV12R0204MB13, ciscoGsccpCapabilityV12R0218IXA=ciscoGsccpCapabilityV12R0218IXA, ciscoGsccpCapabilityV12R022004SW=ciscoGsccpCapabilityV12R022004SW, ciscoGsccpCapabilityV12R023000SW1=ciscoGsccpCapabilityV12R023000SW1, ciscoGsccpCapabilityV12R025000SW1=ciscoGsccpCapabilityV12R025000SW1, ciscoGsccpCapabilityV12R0411SW=ciscoGsccpCapabilityV12R0411SW)
