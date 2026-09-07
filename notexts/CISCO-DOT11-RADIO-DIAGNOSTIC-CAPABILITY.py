#
# PySNMP MIB module CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY
# Source digest sha256:7c36f6092b8c825a1ccafa29af8a2062f42991c669c3802f398bee4b97aa0d31
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDot11RadioDiagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 335))
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setLastUpdated('2003-09-03 00:00')
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setOrganization('Cisco Systems, Inc.')
ciscoDot11RadioDiagCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 335, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadioDiagCapabilityV1 = ciscoDot11RadioDiagCapabilityV1.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadioDiagCapabilityV1 = ciscoDot11RadioDiagCapabilityV1.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY", PYSNMP_MODULE_ID=ciscoDot11RadioDiagCapability, ciscoDot11RadioDiagCapability=ciscoDot11RadioDiagCapability, ciscoDot11RadioDiagCapabilityV1=ciscoDot11RadioDiagCapabilityV1)
