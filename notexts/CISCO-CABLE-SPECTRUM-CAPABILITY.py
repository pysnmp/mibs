#
# PySNMP MIB module CISCO-CABLE-SPECTRUM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CABLE-SPECTRUM-CAPABILITY
# Source digest sha256:3763bc9169aa018738aae2bd9e6b98df5dff1e4546b3feee8a0a3c15637b113d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCableSpectrumCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoCableSpectrumCapability.setRevisions(('2002-12-18 00:00',))
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setLastUpdated('2002-12-18 00:00')
if mibBuilder.loadTexts: ciscoCableSpectrumCapability.setOrganization('Cisco Systems, Inc.')
ciscoCableSpectrumCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R00 = ciscoCableSpectrumCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R00 = ciscoCableSpectrumCapabilityV12R00.setStatus('current')
ciscoCableSpectrumCapabilityV12R01Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R01Rev1 = ciscoCableSpectrumCapabilityV12R01Rev1.setProductRelease('Cisco IOS 12.1(05)EC and 12.2 BC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableSpectrumCapabilityV12R01Rev1 = ciscoCableSpectrumCapabilityV12R01Rev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-CABLE-SPECTRUM-CAPABILITY", PYSNMP_MODULE_ID=ciscoCableSpectrumCapability, ciscoCableSpectrumCapability=ciscoCableSpectrumCapability, ciscoCableSpectrumCapabilityV12R00=ciscoCableSpectrumCapabilityV12R00, ciscoCableSpectrumCapabilityV12R01Rev1=ciscoCableSpectrumCapabilityV12R01Rev1)
