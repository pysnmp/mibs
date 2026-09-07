#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DOT11-CONTEXT-SERVICES-CAPABILITY
# Source digest sha256:a2fadef34d6e8d9f92de9962f03176f811fea39974f2a275d90f2e294ee63873
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cDot11ContextServicesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 347))
if mibBuilder.loadTexts: cDot11ContextServicesCapability.setLastUpdated('2003-09-17 00:00')
if mibBuilder.loadTexts: cDot11ContextServicesCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cDot11ContextServicesCapability.setContactInfo('             Cisco Systems\n                              Customer Service\n\n                              Postal: 170 W Tasman Drive\n                              San Jose, CA  95134\n                              USA\n  \n                              Tel: +1 800 553-NETS\n \n                              E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: cDot11ContextServicesCapability.setDescription('Agent capabilities for \n                 CISCO-DOT11-CONTEXT-SERVICES-MIB')
cDot11ContextServicesCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 347, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11ContextServicesCapabilityV1 = cDot11ContextServicesCapabilityV1.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11ContextServicesCapabilityV1 = cDot11ContextServicesCapabilityV1.setStatus('current')
if mibBuilder.loadTexts: cDot11ContextServicesCapabilityV1.setDescription('Cisco Context Services MIB capabilities')
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-CAPABILITY", PYSNMP_MODULE_ID=cDot11ContextServicesCapability, cDot11ContextServicesCapability=cDot11ContextServicesCapability, cDot11ContextServicesCapabilityV1=cDot11ContextServicesCapabilityV1)
