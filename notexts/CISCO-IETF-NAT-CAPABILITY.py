#
# PySNMP MIB module CISCO-IETF-NAT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-NAT-CAPABILITY
# Source digest sha256:4c1ccdfa3e24beab4fdb837f2336cace02b11cf5ddd311d7386389a260139400
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfNatCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 99999))
ciscoIetfNatCapability.setRevisions(('2001-09-10 00:00',))
if mibBuilder.loadTexts: ciscoIetfNatCapability.setLastUpdated('2001-09-10 00:00')
if mibBuilder.loadTexts: ciscoIetfNatCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfNatCapabilityV12R02T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfNatCapabilityV12R02T = ciscoIetfNatCapabilityV12R02T.setProductRelease('Cisco IOS 12.2T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfNatCapabilityV12R02T = ciscoIetfNatCapabilityV12R02T.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-NAT-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfNatCapability, ciscoIetfNatCapability=ciscoIetfNatCapability, ciscoIetfNatCapabilityV12R02T=ciscoIetfNatCapabilityV12R02T)
