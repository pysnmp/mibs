#
# PySNMP MIB module CISCO-IETF-PIM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-PIM-CAPABILITY
# Source digest sha256:38a07c1d3529f9064177ddb4ac000a5759323792b3243de429f8c6a5d928d35f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfPimCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 441))
ciscoIetfPimCapability.setRevisions(('2005-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfPimCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfPimCapability.setLastUpdated('2005-07-27 00:00')
if mibBuilder.loadTexts: ciscoIetfPimCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfPimCapability.setContactInfo('       Cisco Systems\n                Customer Service\n\n               Postal: 170 West Tasman Drive\n               San Jose, CA  95134\n               USA\n\n               Tel: +1 800 553-NETS\n\n               E-mail: cs-ipmulticast@cisco.com')
if mibBuilder.loadTexts: ciscoIetfPimCapability.setDescription('The capabilities description of  CISCO-IETF-PIM-MIB')
cIetfPimCapV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 441, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfPimCapV320CRS1 = cIetfPimCapV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfPimCapV320CRS1 = cIetfPimCapV320CRS1.setStatus('current')
if mibBuilder.loadTexts: cIetfPimCapV320CRS1.setDescription('CISCO-IETF-PIM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IETF-PIM-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfPimCapability, cIetfPimCapV320CRS1=cIetfPimCapV320CRS1, ciscoIetfPimCapability=ciscoIetfPimCapability)
