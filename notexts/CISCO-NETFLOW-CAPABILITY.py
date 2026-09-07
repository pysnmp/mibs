#
# PySNMP MIB module CISCO-NETFLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-NETFLOW-CAPABILITY
# Source digest sha256:78627e5bb32cee64c494d950bfd1afd202cf1a702989200a01a20c2cd8cba899
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NfTopFlowsSortTypes, = mibBuilder.importSymbols("CISCO-NETFLOW-MIB", "NfTopFlowsSortTypes")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNetflowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 407))
ciscoNetflowCapability.setRevisions(('2010-11-04 00:01', '2007-08-24 00:00', '2004-06-21 00:00',))
if mibBuilder.loadTexts: ciscoNetflowCapability.setLastUpdated('2010-11-04 00:01')
if mibBuilder.loadTexts: ciscoNetflowCapability.setOrganization('Cisco Systems, Inc.')
ciscoNetflowCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapCatOSV08R0401 = ciscoNetflowCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapCatOSV08R0401 = ciscoNetflowCapCatOSV08R0401.setStatus('current')
ciscoNetflowCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0233SXHPCat6K = ciscoNetflowCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0233SXHPCat6K = ciscoNetflowCapV12R0233SXHPCat6K.setStatus('current')
ciscoNetflowCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0250SYPCat6kPfc4 = ciscoNetflowCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500 \n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0250SYPCat6kPfc4 = ciscoNetflowCapV12R0250SYPCat6kPfc4.setStatus('current')
mibBuilder.exportSymbols("CISCO-NETFLOW-CAPABILITY", PYSNMP_MODULE_ID=ciscoNetflowCapability, ciscoNetflowCapCatOSV08R0401=ciscoNetflowCapCatOSV08R0401, ciscoNetflowCapV12R0233SXHPCat6K=ciscoNetflowCapV12R0233SXHPCat6K, ciscoNetflowCapV12R0250SYPCat6kPfc4=ciscoNetflowCapV12R0250SYPCat6kPfc4, ciscoNetflowCapability=ciscoNetflowCapability)
