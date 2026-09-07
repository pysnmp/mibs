#
# PySNMP MIB module CISCO-TRUSTSEC-SXP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-TRUSTSEC-SXP-CAPABILITY
# Source digest sha256:d545d18a0162f6fb53e6be51c10d76d88f8422d4590fae7fc92cfaaededee9f3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CiscoVrfName, = mibBuilder.importSymbols("CISCO-TC", "CiscoVrfName")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoTrustSecSxpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 591))
ciscoTrustSecSxpCapability.setRevisions(('2012-09-07 00:00', '2012-04-10 00:00', '2011-09-28 00:00', '2011-03-23 00:00', '2010-11-03 00:00', '2010-03-25 00:00',))
if mibBuilder.loadTexts: ciscoTrustSecSxpCapability.setLastUpdated('2012-09-07 00:00')
if mibBuilder.loadTexts: ciscoTrustSecSxpCapability.setOrganization('Cisco Systems, Inc.')
ciscoTrustSecSxpCapV12R0233SXI4PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXI4PCat6k = ciscoTrustSecSxpCapV12R0233SXI4PCat6k.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXI4PCat6k = ciscoTrustSecSxpCapV12R0233SXI4PCat6k.setStatus('current')
ciscoTrustSecSxpCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0250SYPCat6k = ciscoTrustSecSxpCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0250SYPCat6k = ciscoTrustSecSxpCapV12R0250SYPCat6k.setStatus('current')
ciscoTrustSecSxpCapV12R0233SXJPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXJPCat6k = ciscoTrustSecSxpCapV12R0233SXJPCat6k.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV12R0233SXJPCat6k = ciscoTrustSecSxpCapV12R0233SXJPCat6k.setStatus('current')
ciscoTrustSecSxpCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0001SYPCat6k = ciscoTrustSecSxpCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0001SYPCat6k = ciscoTrustSecSxpCapV15R0001SYPCat6k.setStatus('current')
ciscoTrustSecSxpCapV15R0101SGPCat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SGPCat4k = ciscoTrustSecSxpCapV15R0101SGPCat4k.setProductRelease('Cisco IOS 15.1(1)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SGPCat4k = ciscoTrustSecSxpCapV15R0101SGPCat4k.setStatus('current')
ciscoTrustSecSxpCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 591, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SYPCat6k = ciscoTrustSecSxpCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecSxpCapV15R0101SYPCat6k = ciscoTrustSecSxpCapV15R0101SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-SXP-CAPABILITY", PYSNMP_MODULE_ID=ciscoTrustSecSxpCapability, ciscoTrustSecSxpCapV12R0233SXI4PCat6k=ciscoTrustSecSxpCapV12R0233SXI4PCat6k, ciscoTrustSecSxpCapV12R0233SXJPCat6k=ciscoTrustSecSxpCapV12R0233SXJPCat6k, ciscoTrustSecSxpCapV12R0250SYPCat6k=ciscoTrustSecSxpCapV12R0250SYPCat6k, ciscoTrustSecSxpCapV15R0001SYPCat6k=ciscoTrustSecSxpCapV15R0001SYPCat6k, ciscoTrustSecSxpCapV15R0101SGPCat4k=ciscoTrustSecSxpCapV15R0101SGPCat4k, ciscoTrustSecSxpCapV15R0101SYPCat6k=ciscoTrustSecSxpCapV15R0101SYPCat6k, ciscoTrustSecSxpCapability=ciscoTrustSecSxpCapability)
