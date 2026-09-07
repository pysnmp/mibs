#
# PySNMP MIB module CISCO-RSVP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-RSVP-CAPABILITY
# Source digest sha256:fbc6148461902af056ede5a6ae250801d62f5771b5b8dc4d35c297cb796dda2b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRsvpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 10000))
if mibBuilder.loadTexts: ciscoRsvpCapability.setLastUpdated('2002-06-21 00:00')
if mibBuilder.loadTexts: ciscoRsvpCapability.setOrganization('Cisco Systems, Inc.')
ciscoRsvpCapabilityVismV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 10000, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRsvpCapabilityVismV3R00 = ciscoRsvpCapabilityVismV3R00.setProductRelease('VISM Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRsvpCapabilityVismV3R00 = ciscoRsvpCapabilityVismV3R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-RSVP-CAPABILITY", PYSNMP_MODULE_ID=ciscoRsvpCapability, ciscoRsvpCapability=ciscoRsvpCapability, ciscoRsvpCapabilityVismV3R00=ciscoRsvpCapabilityVismV3R00)
