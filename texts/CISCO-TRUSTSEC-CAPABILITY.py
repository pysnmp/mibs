#
# PySNMP MIB module CISCO-TRUSTSEC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-TRUSTSEC-CAPABILITY
# Source digest sha256:a38262660293d4019c174fac83959747c47266b35ba369d0e501ce1c06c1d136
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CtsPasswordEncryptionType, = mibBuilder.importSymbols("CISCO-TRUSTSEC-TC-MIB", "CtsPasswordEncryptionType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoTrustSecCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 598))
ciscoTrustSecCapability.setRevisions(('2012-09-07 00:00', '2011-09-28 00:00', '2010-11-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTrustSecCapability.setRevisionsDescriptions(('Added capability statements\n        - ciscoTrustSecCapV15R0101SYPCat6kSup2T\n        - ciscoTrustSecCapV15R0101SYPCat6kSup720\n\n        Added VARITION for object ctsSgtAssignmentMethod\n        to the following capability statements:\n        - ciscoTrustSecCapV12R0250SYPCat6k\n        - ciscoTrustSecCapV15R0001SYPCat6k', 'Added capability statement\n        ciscoTrustSecCapV15R0001SYPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTrustSecCapability.setLastUpdated('2012-09-07 00:00')
if mibBuilder.loadTexts: ciscoTrustSecCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTrustSecCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-san@cisco.com,\n                    cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTrustSecCapability.setDescription('The capabilities description of\n        CISCO-TRUSTSEC-MIB.')
ciscoTrustSecCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV12R0250SYPCat6k = ciscoTrustSecCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV12R0250SYPCat6k = ciscoTrustSecCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecCapV12R0250SYPCat6k.setDescription('CISCO-TRUSTSEC-MIB capabilities.')
ciscoTrustSecCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0001SYPCat6k = ciscoTrustSecCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0001SYPCat6k = ciscoTrustSecCapV15R0001SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecCapV15R0001SYPCat6k.setDescription('CISCO-TRUSTSEC-MIB capabilities.')
ciscoTrustSecCapV15R0101SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup2T = ciscoTrustSecCapV15R0101SYPCat6kSup2T.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup2T = ciscoTrustSecCapV15R0101SYPCat6kSup2T.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecCapV15R0101SYPCat6kSup2T.setDescription('CISCO-TRUSTSEC-MIB capabilities.')
ciscoTrustSecCapV15R0101SYPCat6kSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup720 = ciscoTrustSecCapV15R0101SYPCat6kSup720.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup720 = ciscoTrustSecCapV15R0101SYPCat6kSup720.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecCapV15R0101SYPCat6kSup720.setDescription('CISCO-TRUSTSEC-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-CAPABILITY", PYSNMP_MODULE_ID=ciscoTrustSecCapability, ciscoTrustSecCapV12R0250SYPCat6k=ciscoTrustSecCapV12R0250SYPCat6k, ciscoTrustSecCapV15R0001SYPCat6k=ciscoTrustSecCapV15R0001SYPCat6k, ciscoTrustSecCapV15R0101SYPCat6kSup2T=ciscoTrustSecCapV15R0101SYPCat6kSup2T, ciscoTrustSecCapV15R0101SYPCat6kSup720=ciscoTrustSecCapV15R0101SYPCat6kSup720, ciscoTrustSecCapability=ciscoTrustSecCapability)
