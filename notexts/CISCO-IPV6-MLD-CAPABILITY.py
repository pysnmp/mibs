#
# PySNMP MIB module CISCO-IPV6-MLD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IPV6-MLD-CAPABILITY
# Source digest sha256:475b5ce75f3729df47daf5cb9198b732abaed3f3eff001fa07cc92dcda26813c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cipv6mldCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 470))
cipv6mldCapability.setRevisions(('2006-01-07 00:00',))
if mibBuilder.loadTexts: cipv6mldCapability.setLastUpdated('2006-01-07 00:00')
if mibBuilder.loadTexts: cipv6mldCapability.setOrganization('Cisco Systems, Inc.')
ciscoIpv6MldCapCRS1V3R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 470, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6MldCapCRS1V3R02 = ciscoIpv6MldCapCRS1V3R02.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6MldCapCRS1V3R02 = ciscoIpv6MldCapCRS1V3R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPV6-MLD-CAPABILITY", PYSNMP_MODULE_ID=cipv6mldCapability, cipv6mldCapability=cipv6mldCapability, ciscoIpv6MldCapCRS1V3R02=ciscoIpv6MldCapCRS1V3R02)
