#
# PySNMP MIB module CISCO-IETF-PW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-PW-CAPABILITY
# Source digest sha256:28a60133c2b35afb26bc1b06c028aa3c76097c6ed4f0b295256dd8e363fc8360
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfPwCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 432))
ciscoIetfPwCapability.setRevisions(('2005-02-09 12:00',))
if mibBuilder.loadTexts: ciscoIetfPwCapability.setLastUpdated('2005-02-09 12:00')
if mibBuilder.loadTexts: ciscoIetfPwCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfPwCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 432, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwCapabilityV12R00 = ciscoIetfPwCapabilityV12R00.setProductRelease('Cisco IOS 12.0(28)S, Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwCapabilityV12R00 = ciscoIetfPwCapabilityV12R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-PW-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfPwCapability, ciscoIetfPwCapability=ciscoIetfPwCapability, ciscoIetfPwCapabilityV12R00=ciscoIetfPwCapabilityV12R00)
