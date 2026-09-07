#
# PySNMP MIB module CISCO-APPNAV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-APPNAV-CAPABILITY
# Source digest sha256:25c175bf1b90eaa1ef4e2bc9406e01e8d70b93fd4502795b3497b3fabb609edf
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAppnavCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 610))
ciscoAppnavCapability.setRevisions(('2012-04-17 00:00',))
if mibBuilder.loadTexts: ciscoAppnavCapability.setLastUpdated('2012-04-17 00:00')
if mibBuilder.loadTexts: ciscoAppnavCapability.setOrganization('Cisco Systems, Inc.')
ciscoAppNavCapabilityWAASV5R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 610, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavCapabilityWAASV5R0 = ciscoAppNavCapabilityWAASV5R0.setProductRelease('OS=WAAS\n                     OSVERSION=V501')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavCapabilityWAASV5R0 = ciscoAppNavCapabilityWAASV5R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-APPNAV-CAPABILITY", PYSNMP_MODULE_ID=ciscoAppnavCapability, ciscoAppNavCapabilityWAASV5R0=ciscoAppNavCapabilityWAASV5R0, ciscoAppnavCapability=ciscoAppnavCapability)
