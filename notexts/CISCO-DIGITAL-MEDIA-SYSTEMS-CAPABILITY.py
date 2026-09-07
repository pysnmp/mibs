#
# PySNMP MIB module CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY
# Source digest sha256:3f76b4424c7e0afd40fc50a6964e4550928677c15200200a2452ac223a90c36b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDigitalMediaSystemsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 570))
ciscoDigitalMediaSystemsCapability.setRevisions(('2008-06-04 00:00',))
if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapability.setLastUpdated('2008-06-04 00:00')
if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapability.setOrganization('Cisco Systems, Inc.')
ciscoDigitalMediaSystemsCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 570, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDigitalMediaSystemsCapabilityV5R00 = ciscoDigitalMediaSystemsCapabilityV5R00.setProductRelease('DMS Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDigitalMediaSystemsCapabilityV5R00 = ciscoDigitalMediaSystemsCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY", PYSNMP_MODULE_ID=ciscoDigitalMediaSystemsCapability, ciscoDigitalMediaSystemsCapability=ciscoDigitalMediaSystemsCapability, ciscoDigitalMediaSystemsCapabilityV5R00=ciscoDigitalMediaSystemsCapabilityV5R00)
