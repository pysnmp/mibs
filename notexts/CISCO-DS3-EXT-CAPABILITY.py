#
# PySNMP MIB module CISCO-DS3-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DS3-EXT-CAPABILITY
# Source digest sha256:e842d42a0a53831c253034ca1cffb78ff3352272f68ad89110702efd42103f53
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDs3ExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 262))
ciscoDs3ExtCapability.setRevisions(('2003-12-23 00:00', '2003-03-20 00:00', '2002-03-25 00:00',))
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setLastUpdated('2003-12-23 00:00')
if mibBuilder.loadTexts: ciscoDs3ExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoDs3ExtAxsmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmCapabilityV2R00 = ciscoDs3ExtAxsmCapabilityV2R00.setProductRelease('MGX8850 Release 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmCapabilityV2R00 = ciscoDs3ExtAxsmCapabilityV2R00.setStatus('current')
ciscoDs3ExtAxsmeCapabilityV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmeCapabilityV21R60 = ciscoDs3ExtAxsmeCapabilityV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtAxsmeCapabilityV21R60 = ciscoDs3ExtAxsmeCapabilityV21R60.setStatus('current')
ciscoDs3ExtSrmCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtSrmCapabilityV3R00 = ciscoDs3ExtSrmCapabilityV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtSrmCapabilityV3R00 = ciscoDs3ExtSrmCapabilityV3R00.setStatus('current')
ciscoDs3ExtFrsm12CapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtFrsm12CapabilityV3R00 = ciscoDs3ExtFrsm12CapabilityV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtFrsm12CapabilityV3R00 = ciscoDs3ExtFrsm12CapabilityV3R00.setStatus('current')
ciscoDs3ExtCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV4R00 = ciscoDs3ExtCapabilityV4R00.setProductRelease('MGX8950 and MGX8850 Release \n                         4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV4R00 = ciscoDs3ExtCapabilityV4R00.setStatus('current')
ciscoDs3ExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 262, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV5R00 = ciscoDs3ExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs3ExtCapabilityV5R00 = ciscoDs3ExtCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS3-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoDs3ExtCapability, ciscoDs3ExtAxsmCapabilityV2R00=ciscoDs3ExtAxsmCapabilityV2R00, ciscoDs3ExtAxsmeCapabilityV21R60=ciscoDs3ExtAxsmeCapabilityV21R60, ciscoDs3ExtCapability=ciscoDs3ExtCapability, ciscoDs3ExtCapabilityV4R00=ciscoDs3ExtCapabilityV4R00, ciscoDs3ExtCapabilityV5R00=ciscoDs3ExtCapabilityV5R00, ciscoDs3ExtFrsm12CapabilityV3R00=ciscoDs3ExtFrsm12CapabilityV3R00, ciscoDs3ExtSrmCapabilityV3R00=ciscoDs3ExtSrmCapabilityV3R00)
