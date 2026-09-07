#
# PySNMP MIB module CISCO-INT-SERV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-INT-SERV-CAPABILITY
# Source digest sha256:86c3a18a4244f28c8552f54a8e142abbcc8e166060873a54aa7f8a497673b1c5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIntServCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
if mibBuilder.loadTexts: ciscoIntServCapability.setLastUpdated('2002-06-21 00:00')
if mibBuilder.loadTexts: ciscoIntServCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIntServCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-rsvp@cisco.com')
if mibBuilder.loadTexts: ciscoIntServCapability.setDescription('The Agent Capabilities for INT-SERV-MIB.')
ciscoIntServCapabilityVismV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIntServCapabilityVismV3R00 = ciscoIntServCapabilityVismV3R00.setProductRelease('VISM Release 3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIntServCapabilityVismV3R00 = ciscoIntServCapabilityVismV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIntServCapabilityVismV3R00.setDescription('INT-SERV-MIB Capabilities.')
mibBuilder.exportSymbols("CISCO-INT-SERV-CAPABILITY", PYSNMP_MODULE_ID=ciscoIntServCapability, ciscoIntServCapability=ciscoIntServCapability, ciscoIntServCapabilityVismV3R00=ciscoIntServCapabilityVismV3R00)
