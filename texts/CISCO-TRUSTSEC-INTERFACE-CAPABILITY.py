#
# PySNMP MIB module CISCO-TRUSTSEC-INTERFACE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-TRUSTSEC-INTERFACE-CAPABILITY
# Source digest sha256:a9bcc938f378960ef28457eb39a97ea4a27b4a7fcbe57b8cbb5876997ddc8bfb
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoTrustSecInterfaceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 597))
ciscoTrustSecInterfaceCapability.setRevisions(('2012-09-04 00:00', '2010-10-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoTrustSecInterfaceCapV15R0101SYPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setLastUpdated('2012-09-04 00:00')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setContactInfo('Cisco Systems, Inc\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n               Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setDescription('The capabilities description of CISCO-TRUSTSEC-INTERFACE-MIB.')
ciscoTrustSecInterfaceCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 597, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV12R0250SYPCat6k = ciscoTrustSecInterfaceCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV12R0250SYPCat6k = ciscoTrustSecInterfaceCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapV12R0250SYPCat6k.setDescription('CISCO-TRUSTSEC-INTERFACE-MIB capabilities.')
ciscoTrustSecInterfaceCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 597, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV15R0101SYPCat6k = ciscoTrustSecInterfaceCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV15R0101SYPCat6k = ciscoTrustSecInterfaceCapV15R0101SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapV15R0101SYPCat6k.setDescription('CISCO-TRUSTSEC-INTERFACE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-INTERFACE-CAPABILITY", PYSNMP_MODULE_ID=ciscoTrustSecInterfaceCapability, ciscoTrustSecInterfaceCapV12R0250SYPCat6k=ciscoTrustSecInterfaceCapV12R0250SYPCat6k, ciscoTrustSecInterfaceCapV15R0101SYPCat6k=ciscoTrustSecInterfaceCapV15R0101SYPCat6k, ciscoTrustSecInterfaceCapability=ciscoTrustSecInterfaceCapability)
