#
# PySNMP MIB module CISCO-RADIUS-AUTH-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-RADIUS-AUTH-CLIENT-CAPABILITY
# Source digest sha256:9fd22f4a3968f9fea59afb7fc2c1b5806ca695acc61b32654f8cc59cb608e932
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRadiusAuthClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 494))
ciscoRadiusAuthClientCapability.setRevisions(('2006-03-06 00:00',))
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setLastUpdated('2006-03-06 00:00')
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setOrganization('Cisco Systems, Inc.')
ciscoRadiusAuthClientCapV330CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 494, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAuthClientCapV330CRS1 = ciscoRadiusAuthClientCapV330CRS1.setProductRelease('Cisco IOS XR release 3.3.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAuthClientCapV330CRS1 = ciscoRadiusAuthClientCapV330CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-RADIUS-AUTH-CLIENT-CAPABILITY", PYSNMP_MODULE_ID=ciscoRadiusAuthClientCapability, ciscoRadiusAuthClientCapV330CRS1=ciscoRadiusAuthClientCapV330CRS1, ciscoRadiusAuthClientCapability=ciscoRadiusAuthClientCapability)
