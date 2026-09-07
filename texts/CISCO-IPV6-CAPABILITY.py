#
# PySNMP MIB module CISCO-IPV6-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IPV6-CAPABILITY
# Source digest sha256:52e6779566e9319321987c72905aaeaea392d5349e20fae4363be894314d83c5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cipv6Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 503))
cipv6Capability.setRevisions(('2006-05-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cipv6Capability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cipv6Capability.setLastUpdated('2006-05-17 00:00')
if mibBuilder.loadTexts: cipv6Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cipv6Capability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com\n                        cs-snmp@cisco.com')
if mibBuilder.loadTexts: cipv6Capability.setDescription('The capabilities description of\n                 RFC 2465 Based IPV6-MIB.')
ciscoIpv6CapCRS1V3R3R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 503, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6CapCRS1V3R3R1 = ciscoIpv6CapCRS1V3R3R1.setProductRelease('Cisco IOS XR 3.3.1 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6CapCRS1V3R3R1 = ciscoIpv6CapCRS1V3R3R1.setStatus('current')
if mibBuilder.loadTexts: ciscoIpv6CapCRS1V3R3R1.setDescription('IPV6-MIB capabilities for\n                        IOS XR release 3.3.1')
mibBuilder.exportSymbols("CISCO-IPV6-CAPABILITY", PYSNMP_MODULE_ID=cipv6Capability, cipv6Capability=cipv6Capability, ciscoIpv6CapCRS1V3R3R1=ciscoIpv6CapCRS1V3R3R1)
