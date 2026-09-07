#
# PySNMP MIB module CISCO-RS-232-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-RS-232-CAPABILITY
# Source digest sha256:7ceafb2c6bfc8a3d8f1f2e81609729a6b8c6a9e757e106f1b360562e67538da1
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRS232Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 115))
ciscoRS232Capability.setRevisions(('2002-05-16 00:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRS232Capability.setLastUpdated('2002-05-16 00:00')
if mibBuilder.loadTexts: ciscoRS232Capability.setOrganization('Cisco Systems, Inc.')
ciscoRS232CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 115, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV10R02 = ciscoRS232CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV10R02 = ciscoRS232CapabilityV10R02.setStatus('current')
ciscoRS232CapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 115, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV2R00 = ciscoRS232CapabilityV2R00.setProductRelease('MGX8850 Release 2.0,\n                BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRS232CapabilityV2R00 = ciscoRS232CapabilityV2R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-RS-232-CAPABILITY", PYSNMP_MODULE_ID=ciscoRS232Capability, ciscoRS232Capability=ciscoRS232Capability, ciscoRS232CapabilityV10R02=ciscoRS232CapabilityV10R02, ciscoRS232CapabilityV2R00=ciscoRS232CapabilityV2R00)
