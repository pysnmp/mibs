#
# PySNMP MIB module CISCO-MEDIA-GATEWAY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MEDIA-GATEWAY-CAPABILITY
# Source digest sha256:e31be6aff93a95105b39a888779972e2d1cf37c9ecef9eb1a87122680c535081
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMediaGatewayCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 375))
ciscoMediaGatewayCapability.setRevisions(('2004-02-05 00:00',))
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setLastUpdated('2004-02-05 00:00')
if mibBuilder.loadTexts: ciscoMediaGatewayCapability.setOrganization('Cisco Systems, Inc.')
cMediaGatewayCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 375, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMediaGatewayCapV5R00 = cMediaGatewayCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cMediaGatewayCapV5R00 = cMediaGatewayCapV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-MEDIA-GATEWAY-CAPABILITY", PYSNMP_MODULE_ID=ciscoMediaGatewayCapability, cMediaGatewayCapV5R00=cMediaGatewayCapV5R00, ciscoMediaGatewayCapability=ciscoMediaGatewayCapability)
