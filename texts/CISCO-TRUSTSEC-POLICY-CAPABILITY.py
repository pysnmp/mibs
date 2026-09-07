#
# PySNMP MIB module CISCO-TRUSTSEC-POLICY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-TRUSTSEC-POLICY-CAPABILITY
# Source digest sha256:bcc61c501c8c593854fb13640c1d1474ee29bb9534a76c80f921b52c0d6b7b11
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTrustSecPolicyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 601))
ciscoTrustSecPolicyCapability.setRevisions(('2013-05-01 00:00', '2013-01-09 00:00', '2010-11-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setRevisionsDescriptions(('Added the following VARIATION clauses in capability\n        statement ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720:\n        - ctspPeerPolicyUpdatedNotifEnable\n        - ctspOldPeerSgt\n        - ctspPeerPolicyUpdatedNotif', 'Added capability statement\n        ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T and \n        ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setLastUpdated('2013-05-01 00:00')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setDescription('The capabilities description of\n        CISCO-TRUSTSEC-POLICY-MIB.')
ciscoTrustSecPolicyCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV12R0250SYPCat6k = ciscoTrustSecPolicyCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV12R0250SYPCat6k = ciscoTrustSecPolicyCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapV12R0250SYPCat6k.setDescription('CISCO-TRUSTSEC-POLICY-MIB capabilities.')
ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T.setDescription('CISCO-TRUSTSEC-POLICY-MIB capabilities.')
ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.setDescription('CISCO-TRUSTSEC-POLICY-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-POLICY-CAPABILITY", PYSNMP_MODULE_ID=ciscoTrustSecPolicyCapability, ciscoTrustSecPolicyCapV12R0250SYPCat6k=ciscoTrustSecPolicyCapV12R0250SYPCat6k, ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T=ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T, ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720=ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720, ciscoTrustSecPolicyCapability=ciscoTrustSecPolicyCapability)
