#
# PySNMP MIB module CISCO-VSI-CONTROLLER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VSI-CONTROLLER-CAPABILITY
# Source digest sha256:0a453d0ad543a5ae5db05e325ad56f3ed75e358e350dc51315b0f20ac3a6b761
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVsiControllerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoVsiControllerCapability.setRevisions(('2002-05-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVsiControllerCapability.setRevisionsDescriptions(('Initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setLastUpdated('2002-05-02 00:00')
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setContactInfo('       Cisco Systems\n\n                Customer Service\n\n           Postal: 170 West Tasman Drive\n           San Jose, CA  95134\n           USA\n\n           Tel: +1 800 553-NETS\n\n          E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVsiControllerCapability.setDescription('Agent capabilities for CISCO-VSI-CONTROLLER-MIB.')
ciscoVsiControllerCapabilityVR200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVsiControllerCapabilityVR200 = ciscoVsiControllerCapabilityVR200.setProductRelease('MGX8850 Release 2.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVsiControllerCapabilityVR200 = ciscoVsiControllerCapabilityVR200.setStatus('current')
if mibBuilder.loadTexts: ciscoVsiControllerCapabilityVR200.setDescription('The agent capabilities for \n                CISCO-VSI-CONTROLLER-MIB.')
mibBuilder.exportSymbols("CISCO-VSI-CONTROLLER-CAPABILITY", PYSNMP_MODULE_ID=ciscoVsiControllerCapability, ciscoVsiControllerCapability=ciscoVsiControllerCapability, ciscoVsiControllerCapabilityVR200=ciscoVsiControllerCapabilityVR200)
