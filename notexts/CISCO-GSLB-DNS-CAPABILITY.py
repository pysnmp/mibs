#
# PySNMP MIB module CISCO-GSLB-DNS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-GSLB-DNS-CAPABILITY
# Source digest sha256:a9d55ea0df572faf2efdebc497001f4894c02ef321430d6beaabf529e2c113ec
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGslbDnsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 535))
ciscoGslbDnsCapability.setRevisions(('2009-03-18 00:00', '2007-02-23 00:00',))
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setLastUpdated('2009-03-18 00:00')
if mibBuilder.loadTexts: ciscoGslbDnsCapability.setOrganization('Cisco Systems, Inc.')
ciscoGslbDnsCapabilityV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 535, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV02R00 = ciscoGslbDnsCapabilityV02R00.setProductRelease('GSS 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV02R00 = ciscoGslbDnsCapabilityV02R00.setStatus('current')
ciscoGslbDnsCapabilityV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 535, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV03R01 = ciscoGslbDnsCapabilityV03R01.setProductRelease('GSS 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbDnsCapabilityV03R01 = ciscoGslbDnsCapabilityV03R01.setStatus('current')
mibBuilder.exportSymbols("CISCO-GSLB-DNS-CAPABILITY", PYSNMP_MODULE_ID=ciscoGslbDnsCapability, ciscoGslbDnsCapability=ciscoGslbDnsCapability, ciscoGslbDnsCapabilityV02R00=ciscoGslbDnsCapabilityV02R00, ciscoGslbDnsCapabilityV03R01=ciscoGslbDnsCapabilityV03R01)
