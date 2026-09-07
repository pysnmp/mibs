#
# PySNMP MIB module CISCO-IETF-IPMROUTE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-IPMROUTE-CAPABILITY
# Source digest sha256:a632880b25d1ce54c1a1ff4f81683e46b948a7fdfd694e9c173290e57f7713b6
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfIpMrouteCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 442))
ciscoIetfIpMrouteCapability.setRevisions(('2005-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setLastUpdated('2005-07-27 00:00')
if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setContactInfo('       Cisco Systems\n                Customer Service\n\n               Postal: 170 West Tasman Drive\n               San Jose, CA  95134\n               USA\n\n               Tel: +1 800 553-NETS\n\n               E-mail: cs-ipmulticast@cisco.com')
if mibBuilder.loadTexts: ciscoIetfIpMrouteCapability.setDescription('The capabilities description of  CISCO-IETF-IPMROUTE-MIB')
cIetfIpMrouteCapV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 442, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfIpMrouteCapV320CRS1 = cIetfIpMrouteCapV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfIpMrouteCapV320CRS1 = cIetfIpMrouteCapV320CRS1.setStatus('current')
if mibBuilder.loadTexts: cIetfIpMrouteCapV320CRS1.setDescription('CISCO-IETF-IPMROUTE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IETF-IPMROUTE-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfIpMrouteCapability, cIetfIpMrouteCapV320CRS1=cIetfIpMrouteCapV320CRS1, ciscoIetfIpMrouteCapability=ciscoIetfIpMrouteCapability)
